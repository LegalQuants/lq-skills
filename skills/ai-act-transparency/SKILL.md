---
name: ai-act-transparency
description: |
  EU AI Act Article 50 Transparency Obligations Assessor — identifies which of the Art. 50(1)–(5)
  transparency duties apply to a provider or deployer and produces both a formal mini-report and a
  per-obligation compliance checklist with gap flags, grounded in the final Code of Practice on
  Transparency of AI-Generated Content (June 2026) and the Commission's final Art. 50 Guidelines
  (20 July 2026).
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
> (Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744), the final **Code of Practice on
> Transparency of AI-Generated Content** (10 Jun 2026), and the Commission's **final** Art. 50 Guidelines
> (20 Jul 2026). It is **not legal advice**; final decisions need qualified counsel, and only the **CJEU**
> can authoritatively interpret Art. 50.
> • **Penalty band:** non-compliance is **Tier 2 — up to EUR 15,000,000 or 3% of worldwide annual
> turnover** (Art. 99(4)(g); €750k for EU bodies; for SMEs the *lower* of the two). *Not* the €35M / 7%
> band (that is Art. 5 prohibited practices). Guidelines para. 152.
> • **Dates:** Art. 50 applies from **2 August 2026** (Chapter IV general application — *not* the 2 Aug
> 2025 tranche). The 50(2) **legacy-system marking deadline of 2 December 2026 is settled law**:
> **Regulation (EU) 2026/1744** (Digital Omnibus on AI) was published in the OJ on **24 Jul 2026** and
> entered into force on **27 Jul 2026**, inserting **Art. 111(4)** AI Act. No OJ caveat is needed any more.
> • **Soft law:** the Code of Practice is **final and has been assessed as adequate** by the Commission and
> the AI Board — but it remains **voluntary**, is **not** a presumption of conformity, and adherence is
> **not conclusive evidence** of compliance. The Commission Guidelines are **final** but **non-binding**.
> See [references/sources.md](references/sources.md) for the live source manifest and uncertainty tiers.

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

- **[Settled law]** — the Regulation (Art. 50, 3(60), 99(4)(g), 111(4)); in force.
- **[Official guidance]** — the Commission Art. 50 Guidelines (final, 20 Jul 2026); authoritative-in-practice
  but **non-binding**; the Commission has said it will revise them as experience accrues (para. 155).
- **[Best practice]** — the Code of Practice (adequacy-assessed but voluntary) / EU icon set; adherence
  ≠ conclusive evidence.
- **[Open issue]** — un-litigated: **no CJEU ruling on Art. 50**, and several tests the Guidelines leave to
  a "case-by-case assessment by the deployer" (appreciable resemblance, evidently-artistic, substantiality).

State the **most load-bearing** uncertainty explicitly. Since the Omnibus and the Guidelines both landed in
July 2026, the residual uncertainty is now **interpretive**, not legislative — do not manufacture doubt about
dates that are settled.

---

## When to Search the Web (run quietly; report as one line)

Do these checks **without narrating the research**. Collapse the result into a single **Source status** line
in the output (Phase 6.0), e.g.:
`Source status (checked <date>): Guidelines final (20 Jul 2026) · Omnibus in force (Reg. 2026/1744) · CoP adequacy-assessed · icons published.`

The three big 2026 status questions (Guidelines finalisation, Omnibus OJ publication, CoP adequacy) are all
**now resolved** — so the searches below are for *movement since*, not for re-establishing the baseline.

**On activation — always search for:**
```
EU AI Act Article 50 Commission guidelines revised update 2026 2027
Code of Practice transparency AI-generated content signatories enforcement 2026
```

**For any first CJEU / national enforcement movement (the remaining real uncertainty):**
```
AI Act Article 50 enforcement decision market surveillance authority deepfake labelling
```

**For 50(2) marking / standards:**
```
EU AI Act Art 50(2) machine-readable marking C2PA implementing act harmonised standard 2026
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
companions** the exemption is largely closed — the Guidelines say the exception "should be interpreted
**restrictively**", and general public awareness that chatbots exist does **not** make a given interaction
obvious (para. 45). **What does *not* satisfy 50(1)** (para. 38): disclosure buried in **T&Cs, URLs or
documentation**, **machine-readable signals alone**, a generic "**assistant**" label, **platform-wide generic
notices** ("services on this website use AI"), or "this system uses LLMs". **AI agents** must disclose **both
their artificial nature *and* the person on whose behalf they act**, at key steps (authorisation, reporting,
validation) and **at every new interaction**; where the provider cannot determine in advance whether the agent
will meet a natural person, it must self-disclose in every reasonably-likely interaction (para. 31).
Authorised law-enforcement use is the only statutory exception.

**3.2 — Art. 50(2) synthetic-content marking (provider).**
Trigger: the system generates synthetic audio/image/video/text — **not GPAI-specific**; single-purpose tools,
multi-purpose systems, GPAI systems and **agentic** systems all count (paras. 57–58). Test the
**assistive-function / no-substantial-alteration** exemptions (paras. 90–92): standard editing prepares
existing content for publication without generating new content; editing that changes meaning, style or
intent goes beyond it. **⚠ Machine translation is now OUT of scope** — the final Guidelines list
"**AI-generated translations of text**" among the standard-editing examples (para. 92), **reversing the draft**.
Note the scope exclusions: **source code** in the broad sense — programming/scripting/markup/query/config
languages plus SDKs, SQL, IaC, YAML, JSON config, schemas, APIs and libraries, and NL comments integral to the
code (para. 68); **short sequences** (single words, captions, alt-text, UI labels); **machine-to-machine-only
outputs**; **mere reproduction/arrangement** of existing content, e.g. recommenders (para. 65); narrow
**cumulative B2B/industrial** (para. 87); **ephemeral real-time in-game/VR generation** (para. 88).
**Detection is a co-equal element, not an add-on** — marking without available detection means does **not**
comply (paras. 69–70). **Flag the market-placement date** — it decides whether the legacy grace applies
(Phase 5).

**3.3 — Art. 50(3) emotion-recognition / biometric-categorisation notice (deployer).**
Trigger: the system performs emotion recognition or biometric categorisation. **First check Art. 5:** if
the use is in the workplace/education (5(1)(f)) or targets sensitive characteristics (5(1)(g)) it is
**prohibited** — 50(3) does not apply and the Art. 5 violation governs. Otherwise the 50(3) notice is owed
**in addition to** any high-risk/Art. 5 analysis and **regardless of risk tier** — it covers **all**
biometric categorisation, *including non-high-risk* age- or gender-inference for ads or analytics
(para. 104). **Race/ethnicity inference is not a 50(3) example — it is a *prohibited* 5(1)(g)
categorisation; see the Art. 5 gate above.** Note the scope limit on the *content* of the notice: 50(3)
requires telling people they are **exposed to** such a system — it does **not** require explaining the
system's reasons or other processing purposes; those come from **GDPR Art. 13/14** (para. 105). Coordinate
the two notices.

**3.4 — Art. 50(4) deepfake & public-interest-text labelling (deployer).**
Two steps, not one categorical rule. **Step 1 — is it a deepfake?** Apply the Art. 3(60) **four cumulative
criteria** (para. 113 — the final Guidelines expressly keep four; the Commission FAQ's "three" merely merges
criteria (ii) and (iii)): *(i) appreciable resemblance · (ii) existing — or plausibly could exist ·
(iii) persons/objects/places/**entities**/events · (iv) false appearance of authenticity or truthfulness*.
Criterion (iv) is assessed **objectively and as a whole** against the **intended and reasonably foreseeable
audience** and deployment context — **no intent to deceive is required** (para. 114). A photorealistic
**invented** person is IN (plausibly could exist); dragons/impossible content are OUT; **substantive** AI
editing of a journalistic image beyond standard editorial practice can be IN, while cosmetic edits
(backgrounds, lighting, colour, compression) generally are not (para. 116). **Step 2 — exception?** law
enforcement; **evidently** artistic/creative/satirical/fictional → *attenuated* disclosure that does not hamper
display or enjoyment (form only — the duty itself survives, para. 123); public-interest **text** under human
review or editorial control. **Marketing has no blanket pass** — content whose nature is **exclusively
informative or commercial and recognisable as such** is excluded from the artistic limb (para. 122); don't say
marketing categorically qualifies, nor that it never can. (Or the AI-text limb: public-interest text without
human editorial control.)

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
  The Code has been **assessed as adequate**, so signing is a recognised way to *demonstrate* compliance
  (Art. 50(7); Guidelines §8.1) — but it is still **voluntary**, and adherence is **not conclusive evidence**
  and **not a presumption of conformity**. Non-signatories must show an equally effective route. If the system
  uses a GPAI model: Art. 50(2) binds it at the **system** layer; model-level marking is **encouraged best
  practice** (Guidelines para. 27; Code Measure 1.1.2) — **not** an Art. 53(1)(d) duty (53(1)(d) is the
  training-data summary).
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

- **22 Jul 2026 — PASSED.** This was the *initial*-signatory form deadline for the list published before
  2 Aug 2026. **Signing remains open** and is still encouraged; ~190 organisations had signed by end-July 2026.
  Do **not** present this as a live deadline — point the user at the published signatory list instead.
- **2 Aug 2026** — 50(1)/(3)/(4) and 50(2) for newly-placed systems apply, **no transition**.
- **2 Dec 2026** — legacy 50(2) marking — **[Settled law]**: **Art. 111(4)** AI Act, inserted by
  **Regulation (EU) 2026/1744** (OJ 24 Jul 2026, in force 27 Jul 2026). Systems that are **partly interactive
  and partly generative** get this transition **only** for the 50(2) marking limb — 50(1) disclosure is still
  owed from 2 Aug 2026 (Guidelines para. 153).
- **2 Dec 2026** — new **Art. 5(1)(ba)/(bb)** prohibitions (non-consensual intimate imagery; CSAM) begin to
  apply. Art. 5 **prohibition**, not a transparency duty — a 50(4) label cannot cure it.
- **2 Feb 2027** — the Code's watermark-detection **interoperability** obligation (distinct from the
  superseded original legacy-marking proposal of the same date).
- **No retrospective marking — but the trigger is the date of *generation*, not publication** (para. 154):
  50(2) outputs and 50(4) first-subparagraph **deepfakes generated or manipulated before 2 Aug 2026** need no
  retroactive marking/labelling. **Public-interest text is the exception**: it escapes only if it was **both
  generated and published** before 2 Aug 2026 — text generated before but **published on or after** that date
  **must be labelled**. Holders of pre-existing unlabelled deepfakes are *encouraged* (not required) to label,
  without disproportionate effort such as auditing back-catalogues or reprinting packaging.

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

1. **Penalty is €15M / 3% (Tier 2, Art. 99(4)(g); €750k EU bodies; the *lower* figure for SMEs)** — never the
   €35M / 7% Art. 5 band (Guidelines para. 152).
2. **The 2 Dec 2026 legacy-marking deadline is SETTLED LAW** — **Art. 111(4)** AI Act, inserted by
   **Regulation (EU) 2026/1744** (OJ 24 Jul 2026, in force 27 Jul 2026). **Do not** call it "politically
   agreed", "awaiting OJ", "conditional", or an open issue. It covers **only** the 50(2) marking limb.
3. **The Code of Practice has been assessed as adequate, but is still voluntary** — signing is a recognised
   way to *demonstrate* compliance (Art. 50(7)), **not** a presumption of conformity and **not** conclusive
   evidence. Separate the **statutory floor** from the **Code's layered architecture**. Do **not** say the
   adequacy assessment is pending.
4. **The Commission Art. 50 Guidelines are FINAL (20 Jul 2026)** — authoritative in practice but still
   **non-binding**; only the CJEU can interpret Art. 50 authoritatively. Paragraph numbers in this skill are
   **final-Guidelines** numbers; draft (8 May 2026) numbering is superseded and must not be re-cited.
5. **AI agents disclose their artificial nature *and* who they act for**, at key steps and every new
   interaction (para. 31). 50(1) is **not** satisfied by T&Cs/URLs/documentation, machine-readable signals
   alone, "assistant", platform-wide generic notices, or "uses LLMs" (para. 38); the obviousness exception is
   read **restrictively** (para. 45).
6. **50(3) is gated by Art. 5** (workplace/education emotion recognition and sensitive biometric
   categorisation are prohibited — a notice cannot cure it), but otherwise applies **additively and to all
   biometric categorisation, incl. non-high-risk** age- or gender-inference (para. 104) — race/ethnicity
   inference is itself *prohibited* under 5(1)(g), not a 50(3) case.
7. **Deepfake = Art. 3(60)** — apply the **four cumulative criteria** (para. 113; the FAQ's "three" just merges
   (ii)+(iii) — do not drop an element); no intent to deceive is needed, and the audience test is the
   **intended and reasonably foreseeable** audience (para. 114). A photorealistic **invented** person is IN.
   **Marketing has no blanket pass**: exclusively informative/commercial content is outside the artistic limb
   (para. 122) — but don't say marketing can *never* be artistic.
8. **⚠ Machine translation is OUT of 50(2) scope under the final Guidelines** — "AI-generated translations of
   text" is listed as **standard editing** (para. 92). This **reverses the draft**. Do not tell a user a
   translation engine owes 50(2) marking on that basis alone; a translation that materially changes meaning,
   style or intent can still fall back in.
9. **Model-level GPAI marking is encouraged best practice — NOT an Art. 53(1)(d) duty** (53(1)(d) is the
   training-data summary). Art. 50(2) binds the **AI-system** layer, including GPAI systems (para. 27).
10. **50(2) statutory floor vs Code route — keep them apart.** *Statutory* **[Settled law]**: machine-readable
    marking **and** available detection, both required — one without the other does not comply (paras. 69–70);
    four criteria "as far as technically feasible"; **no technique and no "two layers" are mandated**.
    *Code route* **[Best practice]**, and only for signatories/those relying on it: ≥ 2 layers, free per-technique
    detection, **text > 200 tokens watermarked**. Never state the 200-token rule or the two-layer architecture
    as the statutory minimum.
11. **No retrospective marking keys on the date of GENERATION, not publication** (para. 154) — except
    public-interest **text**, which must be **both generated and published** before 2 Aug 2026 to escape;
    text generated before but published on/after that date **must be labelled**.
12. **Provider 50(2) marking ≠ deployer 50(4) labelling** — distinct duties on distinct parties; a deepfake
    can require both. Hosting services, online platforms and broadcasters **merely disseminating** third-party
    content are **not deployers** (para. 16) — but a VLOP creating its own marketing visuals **is**.

---

## What this skill does not do

This section is a feature, not a disclaimer reflex — it tells you when to escalate beyond the skill.

- **It is not legal advice and is not a compliance decision.** It produces a structured Art. 50 analysis and a readiness view; only qualified counsel can give advice, and only the CJEU can authoritatively interpret Art. 50.
- **It does not run the full risk-tier or role analysis.** It takes the provider/deployer role and the risk tier as given; prohibited-practice (Art. 5) and high-risk (Annex I/III) questions are flagged, not decided. Art. 25 quasi-provider edge cases are flagged for a full role analysis, not resolved here.
- **It does not invent legal substance or citations.** Article, paragraph, and Guidelines/Code references come from the reference files; where the inputs are too thin, the skill marks the field `[UNCLEAR]` or tags it `[Open issue]` and proceeds on stated cautious assumptions rather than guessing.
- **It does not certify compliance or quantify actual fines.** Penalty figures are the Art. 99 statutory maxima for context, not a prediction of exposure in a given case.
- **It does not track live enforcement or guideline status for you.** The Art. 50 Guidelines were adopted in final form on 20 July 2026 and the Digital Omnibus is in force as Regulation (EU) 2026/1744, so the picture is settled as at authoring time; the skill still prompts a quick web-check on activation for any later revision or enforcement practice.
- **It is self-contained at LegalQuants.** Where it mentions a companion skill (roles, report), that is a pointer to the author's wider suite — not a dependency; the assessment runs fully on its own.

## Liability

This skill provides structured analysis and drafting support only. **It is not legal advice, creates no attorney–client relationship, and is no substitute for advice from counsel admitted in the relevant jurisdiction.** It is provided "as is" under the Apache License 2.0, without warranties of any kind and subject to the limitation of liability in §§ 7–8 of that license. To the fullest extent permitted by law, the author accepts no liability for any use of or reliance on this skill or its output; users are solely responsible for validating results and for their own compliance decisions.
