#!/usr/bin/env python3
"""
generate_dpas.py — synthesize a controlled 50-DPA benchmark set with matching gold labels.

Each generated Data Processing Agreement is assembled from clause templates. For every GDPR
Art. 28 requirement we hold three variants — a COMPLIANT clause, a DEFICIENT clause (a specific,
realistic weakness), and ABSENT (clause omitted). Because the gold verdict is decided *before*
the text is emitted, the label file is guaranteed consistent with the document a reviewer sees.

Deterministic: same --seed → identical documents + gold (so results are reproducible and the
harness scores against ground truth, not guesswork).

Usage:
  python3 generate_dpas.py --n 50 --seed 7 --out-dpas ./dpas --out-gold ./gold
Then:
  python3 benchmark_dpa.py --dpa-dir ./dpas --gold-dir ./gold --models bulk:x --dry-run   # validates pairing

Verdicts: present | deficient | absent  (must match benchmark_dpa.py RUBRIC ids)
"""
import argparse, json, os, random, textwrap

# rubric id -> (section title, compliant text, deficient text, deficiency note, absence note)
CLAUSES = {
 "a28_1": ("Processing on Documented Instructions",
   "The Processor shall process Personal Data only on documented instructions from the Controller, including with regard to transfers of Personal Data to a third country, unless required to do so by Union or Member State law.",
   "The Processor may process Personal Data as reasonably necessary to provide the Services and for its own legitimate business purposes.",
   "Permits processing for the Processor's 'own legitimate business purposes' — breaches the Art.28(3)(a) 'documented instructions only' limit.",
   "No instruction-limitation clause at all — Art.28(3)(a) unaddressed."),
 "a28_2": ("Confidentiality of Authorised Persons",
   "The Processor shall ensure that persons authorised to process the Personal Data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality.",
   "Processor personnel are subject to the confidentiality terms of the main Services Agreement.",
   "Relies on generic contract confidentiality, not a specific personnel confidentiality commitment per Art.28(3)(b).",
   "No personnel confidentiality obligation — Art.28(3)(b) unaddressed."),
 "a28_3": ("Security of Processing (Art. 32)",
   "The Processor shall implement the technical and organisational measures set out in Annex II to ensure a level of security appropriate to the risk, in accordance with Article 32.",
   "The Processor shall use commercially reasonable efforts to keep Personal Data secure.",
   "'Commercially reasonable efforts' with no measures annex — falls short of Art.32/28(3)(c) specificity.",
   "No security-measures clause — Art.28(3)(c) unaddressed."),
 "a28_4": ("Sub-processors",
   "The Processor shall not engage another processor without prior specific or general written authorisation of the Controller, and shall impose on any sub-processor the same data-protection obligations as set out in this Agreement by way of contract.",
   "The Processor may appoint sub-processors and shall remain liable for their acts; a current list is available on request.",
   "Authorises sub-processors but does NOT flow down equivalent Art.28 obligations by contract (28(2)&(4)).",
   "No sub-processor clause — Art.28(3)(d)/28(4) unaddressed."),
 "a28_5": ("Assistance with Data-Subject Rights",
   "Taking into account the nature of the processing, the Processor shall assist the Controller by appropriate technical and organisational measures for the fulfilment of the Controller's obligation to respond to requests for exercising the data subject's rights under Chapter III.",
   "The Processor will forward any data-subject request it receives to the Controller.",
   "Only forwards requests; provides no technical/organisational assistance to fulfil them per Art.28(3)(e).",
   "No data-subject-rights assistance clause — Art.28(3)(e) unaddressed."),
 "a28_6": ("Assistance with Arts. 32-36",
   "The Processor shall assist the Controller in ensuring compliance with the obligations pursuant to Articles 32 to 36, taking into account the nature of processing and information available to the Processor.",
   "The Processor will provide such assistance with security and breach matters as it deems appropriate.",
   "Discretionary ('as it deems appropriate') assistance — weaker than the mandatory Art.28(3)(f) duty.",
   "No Art.32-36 assistance clause — Art.28(3)(f) unaddressed."),
 "a28_7": ("Deletion or Return of Data",
   "At the choice of the Controller, the Processor shall delete or return all Personal Data after the end of the provision of Services and delete existing copies, unless storage is required by law.",
   "Upon termination the Processor will delete Personal Data within a commercially reasonable period.",
   "Deletion only (no return option) and no copy-deletion / legal-retention carve-out per Art.28(3)(g).",
   "No deletion/return clause — Art.28(3)(g) unaddressed."),
 "a28_8": ("Audits and Information",
   "The Processor shall make available to the Controller all information necessary to demonstrate compliance with Article 28 and allow for and contribute to audits, including inspections, conducted by the Controller or an auditor mandated by the Controller.",
   "The Processor shall, upon request, provide a completed security self-assessment questionnaire once per year.",
   "Audit obligation met by a self-assessment questionnaire only — no on-site/third-party audit right per Art.28(3)(h).",
   "No audit / information-availability clause — Art.28(3)(h) unaddressed."),
 "c_transfer": ("International Transfers",
   "Any transfer of Personal Data outside the EEA shall be governed by the Standard Contractual Clauses set out in Annex III or another lawful transfer mechanism under Chapter V.",
   "The Processor may transfer Personal Data internationally within its group as needed to provide the Services.",
   "International transfers permitted with no SCCs or Chapter V mechanism identified.",
   "No international-transfer clause — transfer lawfulness unaddressed."),
 "c_breach_window": ("Personal Data Breach Notification",
   "The Processor shall notify the Controller without undue delay and in any event within 72 hours after becoming aware of a Personal Data Breach.",
   "The Processor shall notify the Controller of any Personal Data Breach without undue delay.",
   "'Without undue delay' with no fixed hours — negotiate a <=72h window to support the Controller's Art.33 duty.",
   "No breach-notification clause — breach timeline unaddressed."),
 "c_audit": ("Audit Frequency and Scope",
   "The Controller may audit the Processor once per year and additionally for cause following a Personal Data Breach, on reasonable notice.",
   "Audits are limited to one remote questionnaire every two years.",
   "Audit right limited to a biennial questionnaire; no for-cause or on-site audit.",
   "No audit-frequency clause — audit scope unaddressed."),
 "c_liability": ("Liability",
   "Each party's liability under this Agreement is subject to the limitations in the Services Agreement, provided such limitations do not exclude liability for breaches of data-protection law.",
   "The Processor's total liability for any data-protection claim is capped at one month's fees.",
   "Caps data-protection liability at one month's fees — commercially unfavourable and may be unenforceable for GDPR breaches.",
   "No liability clause — allocation unaddressed."),
 "c_return": ("Data Return Format",
   "On return, Personal Data shall be provided in a structured, commonly used, machine-readable format within 30 days.",
   "Data will be returned in the Processor's standard proprietary export format.",
   "Return only in a proprietary format — impedes portability/continuity.",
   "No data-return-format clause — return mechanics unaddressed."),
 "c_subproc_list": ("Sub-processor List and Changes",
   "Annex I lists current sub-processors. The Processor shall give 30 days' prior notice of any intended change, during which the Controller may object.",
   "A list of sub-processors is available in the Processor's online trust centre and may change from time to time.",
   "Points to an online list with no notice period or objection right for changes.",
   "No sub-processor list or change-notification mechanism present."),
}
RUBRIC = list(CLAUSES.keys())
PARTIES = ["Northwind Ltd", "Acme Iberia S.L.", "Meridian GmbH", "Solaris Data BV", "Cobalt Systems Oy",
           "Verda Analytics S.A.", "Harbor Labs Inc.", "Lumen Tech S.L.", "Praxis Cloud AB", "Orion Retail SpA"]


def choose_profile(i: int) -> str:
    if i < 10:  return "clean"          # 10 fully compliant
    if i < 25:  return "single"         # 15 one-defect
    if i < 40:  return "multi"          # 15 two-to-four defects
    return "hostile"                    # 10 several defects + hostile commercials


def degrade(rng, profile):
    """Return {item: verdict} for all rubric items given a profile."""
    verdicts = {k: "present" for k in RUBRIC}
    if profile == "clean":
        return verdicts
    if profile == "single":
        item = rng.choice(RUBRIC)
        verdicts[item] = rng.choice(["deficient", "absent"])
    elif profile == "multi":
        for item in rng.sample(RUBRIC, rng.randint(2, 4)):
            verdicts[item] = rng.choice(["deficient", "absent"])
    elif profile == "hostile":
        forced = ["a28_1", "a28_4", "c_liability", "c_breach_window", "c_audit"]
        for item in forced:
            verdicts[item] = rng.choice(["deficient", "absent"])
        for item in rng.sample([k for k in RUBRIC if k not in forced], rng.randint(0, 2)):
            verdicts[item] = "deficient"
    return verdicts


def render_dpa(dpa_id, controller, processor, verdicts) -> str:
    body = [f"DATA PROCESSING AGREEMENT ({dpa_id})",
            f"\nbetween {controller} (\"Controller\") and {processor} (\"Processor\"),",
            "made pursuant to Article 28 of Regulation (EU) 2016/679 (GDPR).\n",
            "This Agreement governs the processing of Personal Data by the Processor on behalf of "
            "the Controller in connection with the Services.\n"]
    n = 1
    for item in RUBRIC:
        title, present, deficient, _, _ = CLAUSES[item]
        v = verdicts[item]
        if v == "absent":
            continue
        text = present if v == "present" else deficient
        body.append(f"{n}. {title}\n" + textwrap.fill(text, 100))
        n += 1
    body.append("\nSigned for and on behalf of the parties as of the Effective Date.")
    return "\n\n".join(body) + "\n"


def build_gold(dpa_id, controller, processor, profile, verdicts) -> dict:
    notes = {}
    for item, v in verdicts.items():
        if v == "deficient":
            notes[item] = CLAUSES[item][3]
        elif v == "absent":
            notes[item] = CLAUSES[item][4]
    issues = [k for k, v in verdicts.items() if v != "present"]
    return {
        "dpa_id": dpa_id, "profile": profile, "controller": controller, "processor": processor,
        "graded_by": "synthetic-generator", "graded_at": "2026-07-02",
        "verdicts": verdicts, "notes": notes,
        "reference_redline_hint": ("No Art.28 defects — document is compliant."
                                   if not issues else
                                   "Remediate: " + ", ".join(CLAUSES[k][0] for k in issues) + "."),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out-dpas", default="dpas")
    ap.add_argument("--out-gold", default="gold")
    args = ap.parse_args()
    os.makedirs(args.out_dpas, exist_ok=True)
    os.makedirs(args.out_gold, exist_ok=True)

    counts = {}
    for i in range(args.n):
        rng = random.Random(args.seed * 1000 + i)     # per-doc deterministic stream
        profile = choose_profile(int(i * 50 / args.n)) # keep the 10/15/15/10 shape at any n
        controller = PARTIES[i % len(PARTIES)]
        processor = PARTIES[(i + 3) % len(PARTIES)]
        dpa_id = f"syn-{i+1:03d}"
        verdicts = degrade(rng, profile)
        with open(os.path.join(args.out_dpas, f"{dpa_id}.txt"), "w", encoding="utf-8") as fh:
            fh.write(render_dpa(dpa_id, controller, processor, verdicts))
        with open(os.path.join(args.out_gold, f"{dpa_id}.json"), "w", encoding="utf-8") as fh:
            json.dump(build_gold(dpa_id, controller, processor, profile, verdicts), fh, indent=2)
        counts[profile] = counts.get(profile, 0) + 1

    total_defects = 0
    for i in range(args.n):
        g = json.load(open(os.path.join(args.out_gold, f"syn-{i+1:03d}.json")))
        total_defects += sum(1 for v in g["verdicts"].values() if v != "present")
    print(f"[ok] wrote {args.n} DPAs -> {args.out_dpas}/  and gold -> {args.out_gold}/")
    print(f"[ok] profile mix: {counts}")
    print(f"[ok] {total_defects} injected defects total (avg {total_defects/args.n:.1f} per DPA)")
    print(f"[ok] reproducible with --seed {args.seed}. Validate pairing:")
    print(f"     python3 benchmark_dpa.py --dpa-dir {args.out_dpas} --gold-dir {args.out_gold} --models bulk:x --dry-run")


if __name__ == "__main__":
    main()
