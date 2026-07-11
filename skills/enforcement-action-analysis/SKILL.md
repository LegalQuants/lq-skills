---
name: enforcement-action-analysis
description: Use when you have a U.S. government enforcement document (such as DOJ, SEC, OFAC, BIS, or FinCEN) and need a structured, citation-backed summary of the parties, conduct, statutory basis, penalties, and resolution. Reads one enforcement document and produces a consistent extraction for compliance and investigations work.
license: Apache-2.0
lq_ai:
  title: Enforcement Action Analysis — U.S. Regulatory & Criminal Enforcement Summaries
  version: 1.0.0
  author: Andrea Ren
  tags: [enforcement, compliance, investigations, regulatory, settlement, doj, sec, ofac, bis, fincen]
  jurisdiction: us
  trigger_examples:
    - "Summarize this enforcement action."
    - "Pull the key facts, statutes, and penalty terms out of this DPA."
    - "What did the company do and what did it pay?"
    - "Give me a structured read of this OFAC settlement."
    - "Extract the statutory violations and penalty terms from this order."
  inputs:
    required:
      - "One enforcement document, as text or a machine-readable PDF"
    optional:
      - "A perspective note (e.g., 'focus on the export-control angle') to bias emphasis"
  output_format: report
  self_improvement: false
---

# Enforcement Action Analysis

Turns a single U.S. regulatory or criminal enforcement document into a structured, citation-backed summary. It reads what the document actually says — parties, conduct, statutes cited, penalty, and resolution terms — and lays it out in a consistent format a compliance or investigations professional can scan in under a minute.

This skill extracts and organizes. It does not draw legal conclusions beyond what the source supports, and it does not pull in outside facts.

## Audience and Work Shape

**Audience:** in-house compliance, ethics, and investigations professionals — and the outside counsel who support them — who read a steady stream of enforcement actions and want a consistent structured read instead of re-deriving one by hand each time.

**Work shape:** *Pattern-Matched Review.* The skill applies a fixed extraction template to a single document, escalates on out-of-pattern input rather than improvising, and makes no recommendations. It surfaces what the source says in a standard shape; the reader supplies the judgment.

## When to Use

Use this skill when you have **one** enforcement document and want a clean structured read of it. Typical inputs:

- A DOJ press release, deferred/non-prosecution agreement (DPA/NPA), plea agreement, or information/indictment
- An SEC administrative order or litigation release
- An OFAC settlement agreement or civil penalty notice
- A BIS order, charging letter, or settlement
- A FinCEN consent order or assessment of civil money penalty

Phrasings that should trigger it: *"summarize this enforcement action," "pull the key facts out of this DPA," "what did the company do and what did it pay," "give me a structured read of this OFAC settlement," "extract the statutory violations and penalty terms."*

Do **not** use it for: policy guidance, proposed rules, speeches, regulatory agendas, or multi-case roundups — those are not single enforcement actions and the template will not fit.

## Inputs

**Required:** one enforcement document, as text or a machine-readable PDF.

**Optional:** a perspective note (e.g., "focus on the export-control angle") to bias what gets emphasized — but the skill still extracts the full structure regardless.

Before proceeding, confirm the input is a single enforcement action with a subject entity. If it is a policy document, a speech, or covers only an individual with no corporate entity, flag that and stop — see *Edge cases*.

## How It Works

Work through the document in this order. Cite the source page for every extracted item. Where the document is silent, say so — never infer to fill a gap.

1. **Confirm the instrument.** Identify the enforcing authority and the instrument type (DPA, NPA, plea, civil settlement, administrative order, penalty notice, consent order). If the document is not an enforcement action, stop and flag it.
2. **Identify the parties.** Name the subject entity and any named affiliates or successors. Note individuals only insofar as they bear on the entity's conduct; do not profile individuals.
3. **Extract the conduct.** What the entity did, over what time period, in what jurisdictions. Distinguish clearly between what is **alleged**, what is **admitted**, and what is **adjudicated**.
4. **Map the statutory basis.** For each statute or regulation cited: the provision, the conduct that violated it, whether civil or criminal, and whether the entity was charged, admitted, or neither.
5. **Capture the resolution.** Monetary penalty (with component breakdown, cross-agency credits, or installment schedule if stated); any monitor or independent-oversight requirement; self-reporting and certification obligations; mandated remediation; collateral consequences (debarment, suspension, license actions, M&A restrictions); and the agreement term, including termination or clawback conditions.
6. **Note compliance observations.** Summarize what the **document itself** says about how the conduct occurred — control gaps, missed red flags, cooperation, remediation credit. Report what the source states; do not diagnose root cause beyond it.
7. **Note aggravating and mitigating factors.** Including voluntary self-disclosure, timeliness of cooperation, prior history, and any factors the agency expressly credited or held against the entity.
8. **Flag what is unresolved.** Anything material the document does not address — the size of a component penalty, the identity of a monitor, the scope of a foreign parallel proceeding — goes in *Open Questions*.

Throughout, hold to three disciplines: (a) cite pages, (b) distinguish what the evidence shows from what it suggests, and (c) flag uncertainty explicitly rather than papering over it.

## Confidence Bands

Every extracted item carries an implicit confidence level. Handle the three bands distinctly — do not collapse the middle into a silent guess:

- **High** — the document states the item expressly. Report it with a page citation.
- **Medium** — the document supports the item but ambiguously (e.g., the instrument reads like a DPA by structure but is never labeled one; a penalty figure is stated but its components are not). Surface it *with the rationale and the ambiguity flagged* — "likely X because Y; not stated expressly" — rather than silently picking one reading.
- **Low / not addressed** — the document does not resolve the item. Route it to *Open Questions*; never infer to fill the gap.

## Output

A markdown summary with these sections, in order. Omit a section only if the document offers nothing for it, and say so rather than dropping it silently.

- **At a Glance** — one line each: entity · agency · instrument type · announcement date · headline penalty.
- **Parties & Instrument** — the subject entity, affiliates, and the exact instrument.
- **Conduct & Allegations** — what happened, when, where; alleged vs. admitted vs. adjudicated.
- **Statutory & Regulatory Basis** — one entry per statute/regulation: provision, conduct, civil/criminal, charged/admitted/neither.
- **Penalties & Resolution** — monetary terms, monitor, reporting/certification, remediation, collateral consequences, agreement term.
- **Compliance Observations** — what the document states about control gaps, red flags, and remediation.
- **Aggravating / Mitigating Factors** — including voluntary disclosure and cooperation.
- **Open Questions / Not Addressed** — material items the source leaves unresolved.

Every bullet carries a page citation, e.g. `(p. 4)` or `(pp. 12–14)`.

### Illustrative example (hypothetical facts)

**Input (excerpt):** *"The U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC) announced a $3.2 million settlement with Northwind Logistics Inc. for 214 apparent violations of the [sanctions program] between 2019 and 2022. Northwind processed shipments on behalf of a sanctioned party through a third-party intermediary... OFAC determined the conduct was non-egregious and voluntarily self-disclosed... Northwind has since implemented a sanctions screening program... (pp. 1–3)."*

**Output (excerpt):**

> **At a Glance**
> - Entity: Northwind Logistics Inc. · Agency: OFAC · Instrument: Settlement Agreement or Enforcement Release · Date: [as stated] · Penalty: $3.2M (p. 1)
>
> **Conduct & Allegations**
> - 214 apparent violations from 2019–2022; processed shipments for a sanctioned party via a third-party intermediary (p. 1). Characterized as *apparent* violations settled without admission (p. 2).
>
> **Penalties & Resolution**
> - $3.2M civil settlement; OFAC deemed the conduct **non-egregious** and **voluntarily self-disclosed**, reducing the base penalty (p. 2).
> - Remediation: sanctions screening program implemented post-conduct (p. 3).
>
> **Aggravating / Mitigating Factors**
> - Mitigating: voluntary self-disclosure; non-egregious determination; remedial screening program (pp. 2–3).
> - Aggravating: repeat offender due to previous government settlement (recidivism)
>
> **Open Questions / Not Addressed**
> - Base penalty amount before mitigation not stated (p. 2). Identity of the third-party intermediary not disclosed (p. 1).

*(Facts above are hypothetical, for format illustration only.)*

## Edge cases and refusals

- **Not an enforcement document.** Policy guidance, proposed/final rules, speeches, or regulatory agendas — say so and do not force the template.
- **Individual-only matter.** If the document concerns only a natural person with no corporate entity, flag that the skill is entity-focused and proceed, if at all, only on any entity dimension present.
- **Non-English document.** Flag the language and confirm with the user before proceeding.
- **Thin source.** A bare press release with no underlying order or details — produce what is supported and mark thin areas as "not addressed in source"; do not invent detail.
- **Multiple actions in one document.** Ask which action to summarize, or summarize each separately under its own heading.
- **Unreadable input.** If the document is a scanned or image-only PDF with no extractable text, state that the text could not be read and ask for a text-based version.

## Scope and Legal Use

- This skill is designed for **public** government enforcement documents. A summary based solely on such documents is non-privileged and shareable.
- If it is applied to internal, draft, or matter-specific material, the output **inherits the confidentiality and privilege of its inputs** — label it accordingly before any external sharing.
- The output is a **draft for attorney review**. It extracts and organizes; it does not provide legal advice and does not reach legal conclusions beyond what the source document states. Escalate anything consequential to counsel and read the underlying order.

## Characteristic Risks

Beyond the legal-use boundaries above, watch for model-side failure patterns specific to this extraction:

- **Instrument misclassification** — unusual or hybrid formats (a combined order, a novel resolution vehicle) can be mislabeled. When the type is not stated expressly, treat it as Medium confidence per *Confidence Bands* rather than asserting a label.
- **Garbled or OCR'd text** — a poorly extracted PDF can silently corrupt figures, dates, or party names. If the text looks garbled, flag it rather than reporting suspect values as fact.
- **Characterization vs. adjudicated fact** — an agency's narrative framing of conduct is not the same as an admitted or adjudicated finding. Preserve the *alleged / admitted / adjudicated* distinction; do not upgrade characterization to fact.

## Limitations

- The summary is only as good as the source. It does not pull in related dockets, prior actions, parallel foreign proceedings, or any fact outside the document provided.
- Model training cutoffs and jurisdiction-specific nuance mean substantive points should be verified against the primary source and, where warranted, local counsel.
- It is not a substitute for reading the underlying order or agreement for any decision that matters.
