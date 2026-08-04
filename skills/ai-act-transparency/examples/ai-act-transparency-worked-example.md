# Worked Example — Art. 50 Transparency Assessor (provider: chatbot + image generator)

An end-to-end **Full assessment** run: mode pick → intake → role → per-duty triggers → implementation →
dated roadmap → bottom line + portable block. Inputs are illustrative. Every material statement carries
an uncertainty marker (**[Settled law] / [Official guidance] / [Best practice] / [Open issue]**); nothing
here is legal advice.

---

## User prompt

> "We're an EU-based SaaS company about to launch (September 2026) a customer-facing product with two AI
> features: a conversational support chatbot, and an image generator that creates marketing visuals from
> text prompts. We build and place the product on the market under our own brand. Which Article 50
> transparency duties apply to us, what exactly must we implement, and by when? What's our penalty
> exposure if we get it wrong?"

## Mode

Full assessment (the user wants duties + implementation + deadline + exposure). *Source status (checked
2026-08-04): Guidelines final (20 Jul 2026) · Omnibus in force (Reg. (EU) 2026/1744) · CoP adequacy-assessed · icons published.*

## Phase 1 — Facts I'm relying on

| Field | Value |
|---|---|
| What it does | (a) support chatbot that converses with customers; (b) text→image generator producing marketing visuals |
| Generates content? | Yes — **image** (the generator); the chatbot generates **text** to a human |
| Interacts with people? | Yes — the chatbot interacts directly with customers |
| Role | **Provider** — builds and places the product on the market under its own brand |
| EU market-placement date | **September 2026** (i.e. *after* 2 Aug 2026 → newly-placed, **no legacy grace**) |

## Phase 2 — Role

**Provider.** Art. 50 assigns 50(1) interaction disclosure and 50(2) synthetic-content marking to the
**provider**; 50(3)/(4) bind deployers and are not in issue here. **[Settled law]**

## Phase 3 — Trigger determination

| Duty | Binds | Triggered? | Trigger basis | Obviousness / Exception verdict |
|------|-------|-----------|---------------|---------------------------------|
| 50(1) | Provider | **Yes** | Chatbot interacts directly with natural persons | Not "obvious" for a general-audience support bot — disclose proactively **[Official guidance]** para. 38 |
| 50(2) | Provider | **Yes** | Image generator produces synthetic images | No assistive-function exemption — it *generates*, not trivially edits **[Official guidance]** |
| 50(3) | Deployer | No | No emotion/biometric categorisation | — |
| 50(4) | Deployer | No | Provider role; no deployer deepfake publication here | — |
| 50(5) | Provider | **Yes** | Delivery-quality rules attach to every triggered duty | Clear, distinguishable, timely, accessible |

## Phase 4 — Implementation

**Art. 50(1) — chatbot disclosure.** Disclose, at or before the first interaction, that the user is
interacting with an AI system. A generic "assistant" label, "this uses LLMs", or a line buried in the
T&Cs does **not** satisfy 50(1) (**[Official guidance]** para. 38). Machine-readable signals alone are not
enough for the human-facing duty.

**Art. 50(2) — image marking.** Separate the tiers:
- **Statutory floor [Settled law]:** outputs must be marked in a **machine-readable** format and
  **detectable** as artificially generated/manipulated; the marking must be effective, interoperable,
  robust and reliable *"as far as technically feasible"*. The Regulation mandates **no specific
  technique** and does **not** mandate "two layers".
- **Code route [Best practice]:** the June 2026 Code operationalises this as a **layered** solution —
  signed + time-stamped **metadata** (C2PA de-facto) **plus** an imperceptible **watermark** — and treats
  **detection as half the duty** (offered free of charge, per technique). No single technique meets all
  four criteria. Adherence to the Code is **not conclusive evidence** of compliance.
- If a GPAI model sits under the generator, 50(2) still binds it at the **AI-system** layer; model-level
  marking is *encouraged* best practice, **not** an Art. 53(1)(d) duty.

**Art. 50(5) — delivery.** Disclosures/markings must be clear, distinguishable, timely and accessible
(use WCAG AA as the UI benchmark; assess EAA applicability).

## Phase 5 — Dated roadmap

- **2 Aug 2026** — 50(1) and 50(2) apply to newly-placed systems, **no transition**. **[Settled law]**
- Because the product is placed **Sept 2026** (after 2 Aug 2026), the **legacy 50(2) grace to 2 Dec 2026
  does NOT apply** — you must ship marking at launch. **[Settled law]**
- **2 Feb 2027** — the Code's watermark-**detection interoperability** obligation (distinct from the
  superseded original legacy-marking proposal of the same date). **[Best practice]**
- No retrospective marking of anything generated/published before 2 Aug 2026 (not applicable here). 

## Phase 6 — Output

### 6.0 Bottom line
- **Role:** provider. **Duties triggered:** 50(1) chatbot disclosure + 50(2) image marking (+ 50(5)).
- **Earliest deadline:** **2 Aug 2026**, and since you launch Sept 2026 there is **no legacy grace** —
  marking must be live at launch.
- **Biggest gap:** a compliant 50(2) marking pipeline (machine-readable mark + detectability) for the
  image generator.
- **Load-bearing uncertainty:** the *layered* two-technique expectation is the **Code route [Best
  practice]**, not the statutory floor — do not present it as the black-letter mandate. **[Official guidance]**
- **Exposure:** Tier 2 — up to **EUR 15,000,000 or 3%** of worldwide annual turnover (Art. 99(4)(g)).
  **Not** the €35M / 7% band (that is Art. 5 prohibited practices). **[Settled law]**

### 6.5 Readiness
`Readiness: Low` · `Critical blockers: 1 (50(2) marking pipeline)` · `Must-fix before 2 Aug 2026: 2` ·
`Counsel review needed: yes`

### 6.6 Source status
`Source status (checked 2026-08-04): Guidelines final (20 Jul 2026) · Omnibus in force (Reg. (EU) 2026/1744) · CoP adequacy-assessed · icons published.`

### (c) Portable compliance block

```
ART. 50 TRANSPARENCY COMPLIANCE BLOCK
Role: Provider
50(1) interaction disclosure: TRIGGERED (chatbot) — proactive at-start disclosure required
50(2) synthetic-content marking: TRIGGERED (image generator) — machine-readable mark + detectability
50(3) biometric/emotion notice: n/a
50(4) deepfake/PI-text labelling: n/a
50(5) delivery quality: applies to 50(1) + 50(2)
Any 50 trigger active: true
Earliest deadline: 2 Aug 2026 (no legacy grace — placed Sept 2026)
Penalty band: Tier 2 — EUR 15M / 3% (Art. 99(4)(g))
Code of Practice signatory intent: undecided
Source: ai-act-transparency v<X.Y>
```

---

*This example shows the provider / 50(1)+50(2) path. Deployer cases (deepfake labelling under 50(4),
biometric notices under 50(3)), the legacy-system grace, and the artistic/public-interest exceptions run
through the same six phases with different outputs (see `SKILL.md`).*
