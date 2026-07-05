---
name: ai-act-transparency
description: |
  EU AI Act Article 50 Transparency Obligations Assessor — identifies which of the Art. 50(1)–(5)
  transparency duties apply to a provider or deployer and produces both a formal mini-report and a
  per-obligation compliance checklist with gap flags, grounded in the final Code of Practice on
  Transparency of AI-Generated Content (June 2026) and the Commission's draft Art. 50 Guidelines.
  This skill should be used when the user asks to "check Art. 50 transparency obligations", "do we need
  to label AI content or deepfakes", "AI chatbot disclosure", "synthetic content marking / watermarking",
  "emotion-recognition notice", "what must we implement under Art. 50 and by when", or mentions
  "Kennzeichnungspflicht", "Transparenzpflichten", deepfake labelling, AI-content watermarking, or the
  Code of Practice on AI-generated content.
license: Apache-2.0
lq_ai:
  title: EU AI Act Article 50 Transparency Assessor
  version: 1.0.0
  author: Oliver Schmidt-Prietz
  tags: [eu-ai-act, regulation-2024-1689, article-50, transparency, deepfake, watermarking, synthetic-content, labelling, gpai]
  jurisdiction: eu
  trigger_examples:
    - "Which Article 50 transparency duties apply to our AI chatbot and image generator?"
    - "Do we need to label AI-generated deepfakes in our marketing videos?"
    - "Müssen wir KI-Inhalte kennzeichnen? Welche Transparenzpflichten treffen uns nach Art. 50?"
    - "What must we implement for synthetic-content watermarking under Art. 50(2), and by when?"
  inputs:
    required:
      - "What the AI system does (its function, and whether it generates or manipulates content)"
      - "The organization's role — provider (build/place on the market) and/or deployer (use under own authority)"
    optional:
      - "Content modalities (audio / image / video / text); whether it interacts directly with people"
      - "EU market-placement date (drives the 50(2) legacy-grace logic); any prior AI Act triage context block"
  output_format: report
  minimum_inference_tier: 2
  self_improvement: false
---

# EU AI Act — Article 50 Transparency Assessor

Identify which **Article 50 transparency duties** (Regulation (EU) 2024/1689) apply to a system, decide
**what must be implemented and by when**, and produce a formal mini-report plus a per-obligation
compliance checklist. Works standalone, or ingests a prior AI Act triage's `ASSESSMENT CONTEXT` block if you have one.

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured Art. 50 transparency guidance based on the EU AI Act
> (Regulation (EU) 2024/1689), the final **Code of Practice on Transparency of AI-Generated Content**
> (10 Jun 2026), and the Commission's **draft** Art. 50 Guidelines (8 May 2026). It is **not legal
> advice**; final decisions need qualified counsel, and only the **CJEU** can authoritatively interpret
> Art. 50.
> • **Penalty band:** non-compliance is **Tier 2 — up to EUR 15,000,000 or 3% of worldwide annual
> turnover** (Art. 99(4)(g); €750k for EU bodies). *Not* the €35M / 7% band (that is Art. 5 prohibited practices).
> • **Dates:** Art. 50 applies from **2 August 2026** (Chapter IV general application — *not* the 2 Aug
> 2025 tranche). The 50(2) **legacy-system marking grace to 2 December 2026** is now **adopted** — the Digital
> Omnibus cleared the European Parliament (Jun 2026) and the **Council (final green light, 29 Jun 2026)** and
> is **awaiting OJ publication** ("shortly"; in force the 3rd day after). Treat 2 Dec 2026 as near-settled;
> only until the OJ text appears does the statutory 2 Aug 2026 date formally still govern legacy systems.
> Recommend a quick live OJ / law-tracker check.
> • **Soft law:** the Code of Practice is **final but voluntary** and under adequacy assessment (still
> pending) — adherence is **not conclusive evidence** of compliance. The Commission Guidelines are still
> **draft** (8 May 2026; consultation closed 3 Jun 2026). See [references/sources.md](references/sources.md)
> for the live source manifest and uncertainty tiers.

---

## Start here: pick a mode (ask this first)

Before intake, offer the user a route — do **not** default straight to the full report:

> **How deep do you need to go?**
> **1. Quick triage** — a yes/no on which duties bite and the earliest deadline (a few questions, a short answer).
> **2. Full assessment** — the formal mini-report + per-obligation checklist + portable compliance block.
> **3. Implementation plan** — what product / legal / engineering actually has to build, per triggered duty.

- **Quick triage** → run a compressed intake (role + what it does + market date), output only the
  **Bottom line** block (see Phase 6.0) and the top gaps; then offer to escalate to Full.
- **Full assessment** → the whole six-phase workflow.
- **Implementation plan** → Phases 1–4 focused on the build, load
  [references/implementation-checklists.md](references/implementation-checklists.md).

If the user doesn't choose, assume **Quick triage** and offer to go deeper — leading light beats a wall of report.

## Uncertainty markers (use these in every output)

Tag each material statement so the user can see how firm it is (this is the user-facing view of the
statute / soft-law / open-issue strata — see [references/sources.md](references/sources.md)):

- **[Settled law]** — the Regulation (Art. 50, 3(60), 99(4)(g)); in force.
- **[Draft guidance]** — the Commission Art. 50 Guidelines (draft, 8 May 2026); persuasive, non-binding.
- **[Best practice]** — the voluntary Code of Practice / EU icon set; adherence ≠ conclusive evidence.
- **[Open issue]** — adopted-but-unpublished (Omnibus/OJ), pending (CoP adequacy assessment), or un-litigated
  (no CJEU ruling on Art. 50).

State the **most load-bearing** uncertainty explicitly (e.g. "the 2 Dec 2026 grace is **[Open issue]** until OJ").

---

## When to Search the Web (run quietly; report as one line)

Do these checks **without narrating the research**. Collapse the result into a single **Source status** line
in the output (Phase 6.0), e.g.:
`Source status (checked <date>): Guidelines draft · Omnibus adopted, awaiting OJ · CoP adequacy pending · icons published.`

**On activation — always search for (these change month to month):**
```
EU AI Act Article 50 Commission guidelines final adopted 2026
Code of Practice transparency AI-generated content adequacy assessment AI Board 2026
```

**Digital Omnibus OJ check — always (the 2 Dec 2026 grace is adopted, awaiting OJ publication):**
```
Digital Omnibus AI Act Article 50 watermarking grace 2 December 2026 Official Journal published
```

**For 50(2) marking / standards:**
```
EU AI Act Art 50(2) machine-readable marking C2PA implementing act standard 2026
AI Office transparency code signatories list 22 July 2026
```

**For 50(4) labelling / icons:**
```
EU official AI-generated content labelling icons set 2026
```

If web results conflict with this skill's reference files, **prefer the newer official source** and tell
the user what changed.

---

## Workflow: Ask Questions ONE AT A TIME

Read the reference files as each phase needs them. Do not dump all questions at once — this is a
conversational assessment.

### Phase 1: Intake

**Prior Assessment Context (optional):**
> "If you have already run an EU AI Act risk-tier triage, paste its `ASSESSMENT CONTEXT` block here.
> I'll use `Art. 50:`, `Role:`, `Classification:`, and `GPAI:` to skip questions you've already answered."

If a block is provided:
- a non-empty `Art. 50: [triggers]` → pre-populate Phase 3 and confirm rather than re-derive;
- `Role:` → satisfies Phase 2;
- `Classification:` / `GPAI:` → informs the Art. 50 ↔ Art. 53 layering note (Phase 4);
- if any field conflicts with the user's answers, **flag the inconsistency** before proceeding.

If no block is provided, run the intake as a **short decision-tree, one step at a time** — not one dense
four-part question (honour the "one at a time" rule below). Walk these in order, adapting to answers:

1. **What does the system do?** (one-line description)
2. **Does it generate content?** If yes, **which modalities** — audio / image / video / text?
3. **Does it interact directly with people?** (chatbot, voice agent, autonomous agent)
4. **What's your role** — do you **build/place it on the market** (provider), **use it under your authority**
   (deployer), or **both**?
5. **When was it / will it be placed on the EU market?** — this date drives the 50(2) grace logic.

In **Quick triage** mode, ask only 2, 4 and 5 (plus 3 if relevant) and skip to the Bottom line.
Once you have the facts, **echo them back** as a "Facts I'm relying on" block (Phase 6.6) and ask the user
to correct anything before you analyse.

Read [references/art50-duties.md](references/art50-duties.md) for the duty definitions before Phase 3.

### Phase 2: Role determination

Art. 50 splits duties by role:

| Duty | Binds |
|------|-------|
| 50(1) interaction disclosure, 50(2) synthetic-content marking | **Provider** |
| 50(3) emotion/biometric notice, 50(4) deepfake/PI-text labelling | **Deployer** |
| 50(5) delivery quality | whoever owes (1)–(4) |

- If the context block carries `Role:`, use it.
- Otherwise ask whether the organisation **builds/places the system on the market** (provider), **uses it
  under its own authority** (deployer), or **both** (a provider that also deploys owes all four duties).
- For Art. 25 quasi-provider / substantial-modification depth (a rebrand or material fine-tuning can make
  a deployer a provider), **flag it for a full role analysis and qualified counsel** rather than
  re-deriving that edge case here (it is covered in depth by the author's `ai-act-roles` skill — see
  *Part of a wider EU AI Act suite* below).

### Phase 3: Trigger determination (one sub-section per duty)

For each duty: apply the **trigger test**, then the **obviousness / exception test**. Read
[references/obviousness-and-exceptions.md](references/obviousness-and-exceptions.md).

**3.1 — Art. 50(1) interaction disclosure (provider).**
Trigger: the system interacts directly with natural persons. Then test **obviousness** against the
**average-consumer** multi-factor standard (context, vulnerable groups, AI literacy, realism); dev-only
code assistants and in-game NPCs are plausibly "obvious", but for general-audience systems and **AI
companions** the exemption is largely closed. **What does *not* satisfy 50(1)** (draft Guidelines para. 35):
disclosure buried in **T&Cs**, **machine-readable signals alone**, a generic "**assistant**" label, or
"this system uses LLMs". **Agentic AI** must self-disclose in every reasonably-foreseeable human interaction
(para. 28). Authorised law-enforcement use is the only statutory exception.

**3.2 — Art. 50(2) synthetic-content marking (provider).**
Trigger: the system generates synthetic audio/image/video/text — **not GPAI-specific**; single-purpose
tools count, and **machine translation is IN scope** (a translation engine generates new text; draft
Guidelines para. 54). Test the **assistive-function** exemption (trivial in-place editing that preserves
meaning → out; generation → in). Note the Guidelines' carve-outs: **source code** (para. 64), narrow
**cumulative B2B/industrial** (para. 81), **in-game generation** (para. 82). **Flag the market-placement
date** — it decides whether the legacy grace applies (Phase 5).

**3.3 — Art. 50(3) emotion-recognition / biometric-categorisation notice (deployer).**
Trigger: the system performs emotion recognition or biometric categorisation. **First check Art. 5:** if
the use is in the workplace/education (5(1)(f)) or targets sensitive characteristics (5(1)(g)) it is
**prohibited** — 50(3) does not apply and the Art. 5 violation governs. Otherwise the 50(3) notice is owed
**in addition to** any high-risk/Art. 5 analysis and **regardless of risk tier** — it covers **all**
biometric categorisation, *including non-high-risk* age- or gender-inference for ads or analytics
(para. 98). **Race/ethnicity inference is not a 50(3) example — it is a *prohibited* 5(1)(g)
categorisation; see the Art. 5 gate above.** Coordinate with GDPR Art. 13/14.

**3.4 — Art. 50(4) deepfake & public-interest-text labelling (deployer).**
Two steps, not one categorical rule. **Step 1 — is it a deepfake?** Apply the Art. 3(60) four-element test
(draft Guidelines para. 107): *appreciable resemblance · capable of existing in reality · existing persons/
objects/places/**entities**/events · false authenticity judged by the **actual audience** (para. 108)*. A
photorealistic **invented** person is IN (plausibly could exist); dragons/impossible content are OUT; a
substantive AI edit of a journalistic image can be IN. **Step 2 — exception?** law enforcement; **evidently**
artistic/creative/fictional → *proportionate* disclosure (form only); public-interest **text** under human
editorial review. **Marketing has no blanket pass** — *primarily-commercial* content gets **full disclosure**
(para. 114); don't say marketing categorically qualifies, nor that it never can. (Or the AI-text limb:
public-interest text without human editorial control.)

**3.5 — Art. 50(5) delivery quality (cross-cutting).**
For every triggered duty, disclosure must be clear, distinguishable, timely (≤ first interaction/exposure)
and accessible — conform to the **applicable accessibility requirements** (assess EAA applicability; use
**WCAG AA** as the design benchmark for web/mobile UI). Art. 50(5) does not itself name the EAA.

**Close Phase 3 with the trigger-summary table:**

| Duty | Binds | Triggered? | Trigger basis | Obviousness / Exception verdict |
|------|-------|-----------|---------------|---------------------------------|
| 50(1) | Provider | [Y/N] | … | … |
| 50(2) | Provider | [Y/N] | … | … |
| 50(3) | Deployer | [Y/N] | … | … |
| 50(4) | Deployer | [Y/N] | … | … |
| 50(5) | [owner] | [Y/N] | … | … |

### Phase 4: Implementation deep-dive (per triggered duty)

For each **triggered** duty, explain what to build. Load the matching reference:

- **50(2) marking** → [references/code-of-practice-final.md](references/code-of-practice-final.md).
  Distinguish **three tiers**: (1) **statutory floor** *[Settled law]* — machine-readable + detectable, four
  criteria *"as far as technically feasible"* (no technique and no "two layers" mandated); (2) **Code route**
  *[Best practice]* — **≥ 2 layers** (signed metadata + imperceptible watermark), detection is **half the
  duty** (free-of-charge, per-technique), text **> 200 tokens must be watermarked**; (3) robust best practice.
  Adherence to the Code is **not conclusive evidence** of compliance. If the system uses a GPAI model:
  Art. 50(2) binds it at the **system** layer; model-level marking is **encouraged best practice** (Guidelines
  paras. 24/70; Code Measure 1.1.2) — **not** an Art. 53(1)(d) duty (53(1)(d) is the training-data summary).
- **50(4) labelling** → [references/eu-labelling-icons.md](references/eu-labelling-icons.md): the **three
  official EU icons** (**Basic**, **Fully AI-Generated**, **Partially AI-Modified**) — icons **optional**, the
  mandatory core is the capitalised **"AI"** acronym; **GENERATED/MODIFIED** is optional and copyright-
  sensitive; **audio needs a mandatory audible disclaimer**; embed-by-default placement, WCAG contrast,
  persistence. For **published text**, the Commitment 4 editorial-responsibility policy.
- **50(1) / 50(3) notices** → notice content, placement, and timing (Art. 50(5)); for 50(3), the GDPR
  Art. 13/14 coordination.

Concrete action items per role are in
[references/implementation-checklists.md](references/implementation-checklists.md).

### Phase 5: Dated roadmap

Read [references/timeline-and-grace.md](references/timeline-and-grace.md). Anchor the roadmap on:

- **22 Jul 2026** — Code **initial-signatory** form deadline (to appear on the list published before 2 Aug
  2026; signing is encouraged, not mandatory, and possible later too).
- **2 Aug 2026** — 50(1)/(3)/(4) and 50(2) for newly-placed systems apply, **no transition**.
- **2 Dec 2026** — legacy 50(2) marking — **[Open issue → near-settled]**: the Digital Omnibus grace is
  **adopted** (EP Jun 2026; Council final green light **29 Jun 2026**) and **awaiting OJ publication** (in
  force the 3rd day after). Until the OJ text appears, 2 Aug 2026 formally still governs legacy systems.
  **Recommend a quick live OJ / law-tracker check** — but do not overstate the residual risk.
- **2 Feb 2027** — the Code's watermark-detection **interoperability** obligation (distinct from the
  superseded original legacy-marking proposal of the same date).
- Content already public **before 2 Aug 2026** needs **no retrospective** marking/labelling.

### Phase 6: Output (lead light, then the formal artifacts)

Read [references/report-template-art50.md](references/report-template-art50.md). **Always show 6.0–6.6 first**
as a short conversational answer; only produce the heavy artifacts (a)–(c) when the user is in **Full**
mode or asks for them.

- **6.0 Bottom line** (always, ≤ 6 lines): role · duties triggered · earliest deadline · biggest gap · the
  one load-bearing legal uncertainty (tagged with an uncertainty marker).
- **6.5 Readiness** (operational indicator, **not** legal advice): `Readiness: Low / Med / High` ·
  `Critical blockers: N` · `Must-fix before deadline: N` · `Counsel review needed: yes/no`.
- **6.6 Facts I'm relying on**: the intake echoed back, so the user can correct a misread before trusting
  the analysis.
- **Source status** line: one line, `checked <date>`, per the uncertainty markers.

Then, on request / in Full mode:

1. **(a) the mini-report** (Subject/Scope → Role → Trigger analysis → Implementation → Exceptions →
   Roadmap → Gaps + penalty exposure → Conclusion);
2. **(b) the per-obligation checklist** with `✓ / ◐ / ✗ / N/A` gap flags and a SUMMARY line;
3. **(c) the portable `ART. 50 TRANSPARENCY COMPLIANCE BLOCK`** for chaining.

Offer to **format the report as a document** (Word / PDF / Markdown) on request. (The author's separate
`ai-act-report` skill in the EU AI Act suite produces a consolidated Prüfbericht with a Word export — see
*Part of a wider EU AI Act suite* below; this standalone skill needs none of it.)

---

## Part of a wider EU AI Act suite

This skill is **fully self-contained** — give it your inputs and it produces the complete Art. 50
assessment on its own, with no dependency on any other installed skill.

It is also one piece of the author's broader **EU AI Act skill suite** — breadth-first risk-tier
classification, role analysis (Art. 25 quasi-provider depth), the full role × tier obligation matrix, a
regulation-text knowledge base, and a consolidated Prüfbericht/report generator. Where an assessment here
notes an edge case that wants more depth, those companion skills cover it:
**github.com/oliverschmidtprietz/EU-AI-Act-Suite**. None of them are required to use this skill.

---

## Critical Reminders

1. **Penalty is €15M / 3% (Tier 2, Art. 99(4)(g); €750k EU bodies)** — never the €35M / 7% Art. 5 band.
2. **The 2 Dec 2026 legacy-marking grace is ADOPTED, awaiting OJ** — the Digital Omnibus cleared EP (Jun 2026)
   and Council (final green light 29 Jun 2026); treat 2 Dec 2026 as near-settled, recommend a live OJ check,
   and note 2 Aug 2026 formally governs only until the OJ text appears. **Do not** call it "politically agreed"
   or "conditional / may not happen".
3. **The Code of Practice is voluntary and adherence is not conclusive evidence of compliance** — it is a
   strong evidentiary anchor, not a safe harbour; do **not** call it a "presumption of conformity". Separate
   the **statutory floor** from the **Code's layered architecture**.
4. **The Commission Art. 50 Guidelines are draft (8 May 2026)** — non-binding; only the CJEU is authoritative.
5. **Agentic AI self-discloses** in every reasonably-foreseeable human interaction (Guidelines para. 28).
   50(1) is **not** satisfied by T&Cs, machine-readable signals alone, "assistant", or "uses LLMs" (para. 35).
6. **50(3) is gated by Art. 5** (workplace/education emotion recognition and sensitive biometric
   categorisation are prohibited — a notice cannot cure it), but otherwise applies **additively and to all
   biometric categorisation, incl. non-high-risk** age- or gender-inference (para. 98) — race/ethnicity
   inference is itself *prohibited* under 5(1)(g), not a 50(3) case.
7. **Deepfake = Art. 3(60)** — apply the **four-element test** (para. 107); a photorealistic **invented**
   person is IN. **Marketing has no blanket pass**: primarily-commercial content gets full disclosure — but
   don't say marketing can *never* be artistic. **Machine translation is IN scope** (para. 54).
8. **Model-level GPAI marking is encouraged best practice — NOT an Art. 53(1)(d) duty** (53(1)(d) is the
   training-data summary). Art. 50(2) binds the **AI-system** layer, including GPAI systems.
9. **50(2): no single technique** satisfies all four criteria; **text > 200 tokens must be watermarked**;
   **detection is half the duty**. **No retrospective marking** of content already public before 2 Aug 2026.
10. **Provider 50(2) marking ≠ deployer 50(4) labelling** — distinct duties on distinct parties; a deepfake
    can require both. A platform **merely passing on** third-party content is **not a deployer** (para. 12).

---

## What this skill does not do

This section is a feature, not a disclaimer reflex — it tells you when to escalate beyond the skill.

- **It is not legal advice and is not a compliance decision.** It produces a structured Art. 50 analysis and a readiness view; only qualified counsel can give advice, and only the CJEU can authoritatively interpret Art. 50.
- **It does not run the full risk-tier or role analysis.** It takes the provider/deployer role and the risk tier as given; prohibited-practice (Art. 5) and high-risk (Annex I/III) questions are flagged, not decided. Art. 25 quasi-provider edge cases are flagged for a full role analysis, not resolved here.
- **It does not invent legal substance or citations.** Article, paragraph, and Guidelines/Code references come from the reference files; where the inputs are too thin, the skill marks the field `[UNCLEAR]` or tags it `[Open issue]` and proceeds on stated cautious assumptions rather than guessing.
- **It does not certify compliance or quantify actual fines.** Penalty figures are the Art. 99 statutory maxima for context, not a prediction of exposure in a given case.
- **It does not track live enforcement or guideline status for you.** The Art. 50 Guidelines are still draft and the Digital Omnibus legacy-marking grace is awaiting Official Journal publication, so the skill prompts a quick web-check on activation and calibrates to the picture at authoring time.
- **It is self-contained at LegalQuants.** Where it mentions a companion skill (roles, report), that is a pointer to the author's wider suite — not a dependency; the assessment runs fully on its own.

## Liability

This skill provides structured analysis and drafting support only. **It is not legal advice, creates no attorney–client relationship, and is no substitute for advice from counsel admitted in the relevant jurisdiction.** It is provided "as is" under the Apache License 2.0, without warranties of any kind and subject to the limitation of liability in §§ 7–8 of that license. To the fullest extent permitted by law, the author accepts no liability for any use of or reliance on this skill or its output; users are solely responsible for validating results and for their own compliance decisions.
