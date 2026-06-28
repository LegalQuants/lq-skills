---
name: gs-classifier
description: Use when a user needs to classify goods and services for an EU trademark application — mapping a business description or a product/service list to the correct Nice classes and to the harmonised terms accepted by the EUIPO. Queries the EUIPO Goods & Services (TMclass / harmonised database) via a configured EUIPO connector and returns class numbers with accepted term wording. Two modes: a detailed mode for a concrete product/service list, and an exploratory mode that maps a business type to candidate classes. Outputs a draft classification for attorney review. Requires a configured EUIPO connector — coverage and freshness depend on that connector.
author: Jatocao
jurisdiction: EU
tags: [trademark, euipo, nice-classification, goods-and-services, tmclass, classification, ip, eu-trademark]
version: 1.0.0
last_reviewed: 2026-06
lq_ai:
  title: EUIPO Goods & Services Classifier
  version: 1.0.0
  author: Jatocao
  tags: [trademark, euipo, nice-classification, tmclass, goods-and-services]
  jurisdiction: EU
  trigger_examples:
    - "Classify these goods for a trademark application"
    - "Which Nice classes does my product fall into?"
    - "Prepare the goods and services list for an EUTM filing"
    - "We're a legal tech startup — which classes should we file in?"
    - "Check whether these terms are accepted in the EUIPO harmonised database"
  inputs:
    required:
      - name: description
        type: text
        description: Either a concrete list of goods/services to classify, or a plain-language description of the business
    optional:
      - name: mode
        type: text
        description: "detailed (precise classification of a given list) or general (exploratory mapping of a business type to candidate classes). If omitted, the skill asks."
      - name: language
        type: text
        description: "Working language for the term wording — es, en, or both. Default en."
  output_format: markdown
  self_improvement: false
---

# EUIPO Goods & Services Classifier

This skill maps goods and services to the correct Nice Classification classes and to the **harmonised terms accepted by the EUIPO**, via a configured EUIPO connector to the Goods & Services (TMclass / harmonised database, "HDB") service. It supports the preparation of an EU trademark (EUTM) specification before filing.

Coverage and freshness of the term data depend entirely on the connector configured by the user — this skill does not itself guarantee live or complete access to the EUIPO database. All outputs are a first-line draft specification for attorney review. They do not constitute a filed specification, a classification opinion, or legal advice.

> **Scope and Legal Use**
> This skill processes information that may relate to client matters and pending filings. Treat all outputs as privileged work product unless the supervising attorney has decided otherwise. The classification produced is a draft for qualified-counsel review — it does not constitute a legal opinion or a final specification. The choice of classes and terms drives filing cost and scope of protection and must be approved by a named responsible attorney before any application is filed.

---

## How this skill behaves

**Work shape — bounded transactional.** Classification is a constrained-scope task with explicit gates: every term is checked against the EUIPO harmonised database (HDB), and anything that cannot be confirmed is flagged rather than guessed. The skill works quickly but never skips those gates, and it escalates anything outside the pattern (vague inputs, non-EU targets, the final filing decision) to counsel.

**Confidence bands.** The skill operationalises three confidence levels and behaves accordingly:
- **High** — the term is confirmed in the HDB: include it as-is.
- **Medium** — a close but unconfirmed match exists: surface the suggested HDB alternative, mark the original `[?]`, and ask before relying on it.
- **Low** — no acceptable HDB match: do not force one; flag `[?]` and hand the term to counsel.

---

## When this skill applies

Apply this skill when:
- A client is preparing an EUTM (or national) application and needs the goods/services classified into Nice classes
- An attorney needs the exact harmonised wording accepted by the EUIPO to minimise classification objections
- A business is exploring which classes are relevant to its activity before deciding the scope of a filing
- A specification needs to be checked against the EUIPO harmonised database before filing

This skill covers the **EUIPO Goods & Services / harmonised database**. National offices may apply their own practice; flag this where the filing target is a national office rather than the EUIPO.

---

## Inputs

**Required:**
- `description` — either a concrete list of goods/services (e.g., "sports clothing, hiking boots, backpacks") or a plain-language description of the business (e.g., "an online language academy").

**Optional:**
- `mode` — `detailed` or `general`. If not provided, ask which the user wants (see the two modes below).
- `language` — `es`, `en`, or `both`. Default `en`. If the user writes in Spanish, work in Spanish.

If the request is ambiguous, ask: *"Do you already have a concrete list of goods/services to classify (detailed mode), or would you prefer to explore which classes fit your type of business (general mode)?"*

---

## Workflow

### Mode A — Detailed (precise classification of a given list)

Use when the user provides concrete goods/services and wants the exact terms accepted by the EUIPO.

**Step 1 — Collect inputs**
Confirm, if not already provided: the brand/business name, the list of goods/services, the working language, and whether the scope is goods only, services only, or both.

**Step 2 — Query the harmonised database**
For each item or coherent group of items, using the configured EUIPO connector:
1. Call `suggest_goods_and_services` with the descriptive text (`language`: `es` or `en`; `max_suggestions`: 20).
2. Select the most relevant suggestions by semantic match.
3. If the user wants both languages, repeat with the other language code, or use `translate_classification` for consistent wording across languages.

**Step 3 — Validate**
Call `validate_classification` with the selected terms to confirm they are in the harmonised database (HDB). Mark any term not confirmed as `[?]` for attorney review — never silently drop or invent a term.

**Step 4 — Present the result**
Produce the output in the **Output → Detailed mode** format below.

### Mode B — General (exploratory mapping of a business type)

Use when the user describes a business in broad terms and wants to know which classes may be relevant, without a detailed product/service list.

**Step 1 — Understand the business**
Ask 2-3 quick questions to scope it, e.g.: Do you manufacture the products or distribute them? Do you also offer related services (training, consultancy, a digital platform)? Is there a specific activity you want to protect?

**Step 2 — Identify candidate classes**
From the description, identify the likely relevant Nice areas. For example: a restaurant → class 43; software → class 42 (and possibly 9); cosmetics → class 3 (and possibly 44). Use `get_nice_class_headings` and `get_nice_taxonomy` to anchor the analysis in official headings rather than assumptions.

**Step 3 — Query the database by area**
For each candidate class, call `search_goods_and_services` with the class number and representative terms (`language`: `es` or `en`) to retrieve accepted wording.

**Step 4 — Present an exploratory proposal**
Produce the output in the **Output → General mode** format below, grouped by priority, and point the user to Mode A to generate the final specification.

---

## Output

### Detailed mode

```
## Proposed classification — [Brand / business name]
Language: [ES / EN / ES+EN]

### CLASS [N] — [Class heading]
Goods/Services:
- [Accepted HDB term 1]
- [Accepted HDB term 2]
- [Accepted HDB term 3]

### CLASS [N] — [Class heading]
...

---
LEGAL NOTICE
This classification is a draft based on the EUIPO harmonised database (HDB).
The reviewing attorney must check and approve the final specification before filing.
Terms marked [?] could not be confirmed against the HDB and need review.
Reviewing attorney: ___________________________
```

### General mode

```
## Classification proposal — [Business description]

Identified [N] potentially relevant Nice classes:

### 🔵 PRIORITY CLASSES (very likely)
**CLASS [N] — [Heading]**
Why it is relevant: [brief, plain-language explanation]
Suggested terms:
- [term 1]
- [term 2]

### 🟡 CLASSES TO CONSIDER (depending on protection strategy)
**CLASS [N] — [Heading]**
Why it might matter: [brief explanation]
Suggested terms:
- [term 1]

### 🔴 CLASSES THAT MIGHT BE RELEVANT (discuss with counsel)
- Class [N]: [reason]

---
NEXT STEPS
1. Review with the client which activities they want to protect
2. Decide which classes to file in
3. Use detailed mode to generate the final goods/services list
4. Validate and have counsel approve the specification before filing

LEGAL NOTICE
This proposal is indicative. The final selection of classes and terms must be
approved by the attorney responsible for the matter.
```

---

## General rules

1. **Harmonised terms only.** Only include terms that are in the EUIPO harmonised database (HDB) or are clearly acceptable. Never invent wording. Mark unconfirmed terms `[?]`.
2. **Language.** Respond in the language the user writes in. If both languages are requested, present both, keeping the wording consistent via `translate_classification`.
3. **Cost awareness.** Do not propose more than 6-8 classes without justification — more classes means higher filing fees. Flag the trade-off.
4. **Defensive classes.** Where relevant, mention the option of defensive classes (e.g., class 35 for retail/distribution) as an option to evaluate, not as a recommendation.
5. **Legal notice always.** Every output must carry the notice that it is a draft to be reviewed and approved by the responsible attorney before filing.
6. **Default mode.** If the user does not specify, ask which mode they want before querying.

---

## Edge cases and refusals

- **No EUIPO connector available:** If no connector is configured, explain that the harmonised database cannot be queried and offer a preliminary classification from general knowledge only, clearly marked as "not validated against the EUIPO HDB."
- **Vague single-word business descriptions (e.g., "technology"):** Ask for more detail before classifying — an over-broad description produces an unreliable class list.
- **Terms not found in the HDB:** Do not invent or force a match. Mark the term `[?]`, suggest the closest accepted alternative via `suggest_goods_and_services`, and leave the decision to counsel.
- **Non-EU / national-office filings:** This skill reflects EUIPO harmonised-database practice. National offices may classify differently; flag this where the filing target is a national office.
- **User asks which classes to actually file in:** This skill proposes and validates classification options. The final choice of classes and scope is a legal and commercial decision for counsel — redirect accordingly.

---

## Scope and Legal Use

This skill is intended for use by qualified IP professionals (trademark attorneys, patent attorneys, legal professionals) as a first-line classification tool. All outputs are privileged work product unless the supervising attorney decides otherwise.

- Outputs should be treated as confidential and matter-specific
- The reviewing-attorney line must be completed by a named qualified attorney before any specification is filed or shared with a client
- This skill does not constitute legal advice and does not create an attorney-client relationship
- This skill does not decide the final specification. It proposes and validates classification options; the choice of classes and terms — which determines filing cost and scope of protection — is for the reviewing attorney, taking into account all relevant factors
- Harmonised-database coverage and term acceptance depend on the connector configured by the user and on EUIPO practice at the time of filing
