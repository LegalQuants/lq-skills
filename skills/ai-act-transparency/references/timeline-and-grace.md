# Timeline, Grace Period & the Digital Omnibus — Reference

The dated anchors a provider/deployer needs to plan Art. 50 implementation.

> **Statutory dates — self-contained; verify on activation.** This file states the Art. 50 dates
> directly. **As of 4 August 2026 the legislative picture is closed:** the Digital Omnibus is
> **Regulation (EU) 2026/1744**, published in the OJ on **24 July 2026** and **in force since 27 July
> 2026**, inserting **Art. 111(4)** AI Act. No OJ watch is needed any more. Web-check on activation only
> for later developments (a revision of the Commission Guidelines, or enforcement practice).

---

## The dates at a glance

| Date | Event | Firm? |
|------|-------|-------|
| ~~22 Jul 2026~~ | **PASSED.** Code of Practice *initial*-signatory form deadline (for the list published before 2 Aug 2026). **Signing remains open**; ~190 organisations signed by end-Jul 2026 | Historic — do not present as a live deadline |
| **2 Aug 2026** | Art. 50(1), 50(3), 50(4) apply — **no transition**. Art. 50(2) applies to systems placed on the market **on/after** this date | Firm (statutory general-application date, Art. 113) |
| **2 Dec 2026** | Art. 50(2) marking deadline for **legacy** generative systems (placed on the market **before** 2 Aug 2026) | **Settled law** — Art. 111(4) AI Act, inserted by Reg. (EU) 2026/1744 |
| **2 Dec 2026** | New **Art. 5(1)(ba)/(bb)** prohibitions (non-consensual intimate imagery; CSAM) begin to apply | Settled law — Reg. (EU) 2026/1744 |
| **2 Feb 2027** | The **Code's interoperability obligation for watermark detection** begins to bite (a *Code-specific* milestone) | Firm (Code milestone, not statutory) |

---

## Statutory baseline — 2 August 2026

Art. 50 (Chapter IV transparency) is **not** a high-risk obligation and is **not** postponed by the
Digital Omnibus. It runs on the Art. 113 **general application date of 2 August 2026**.

Two common misfilings to avoid:
- filing Art. 50 under the postponed Annex III high-risk date (2 Dec 2027) — **wrong**, Art. 50 is not high-risk;
- filing it under the 2 Aug 2025 GPAI/governance tranche (Art. 113(b)) — **wrong**, Art. 50 is not in that tranche.

From 2 Aug 2026, with **no transition**: 50(1) interaction disclosure, 50(3) emotion/biometric notice,
50(4) deepfake/public-interest-text labelling, and 50(2) marking for any system **newly placed on the
market** on/after that date.

---

## The one Omnibus relief — legacy 50(2) marking → 2 December 2026 (SETTLED LAW)

The **only** Digital Omnibus relief touching Art. 50 is a transition for **legacy** generative-AI marking
under 50(2): systems placed on the market or put into service **before** 2 Aug 2026 get until
**2 December 2026** to implement machine-readable marking and detection. The Omnibus **cut the grace from six
months to three** (the Commission had originally proposed 2 Feb 2027; the co-legislators settled on
2 Dec 2026).

**Legal basis — cite this, not a press release:** **Art. 111(4)** AI Act, inserted by **Article 1(37) of
Regulation (EU) 2026/1744** (Digital Omnibus on AI), **published in OJ L 2026/1744 on 24 July 2026** and
**in force since 27 July 2026** (third day after publication, chosen for urgency ahead of 2 Aug 2026).

> **Do not conflate the two "2 Feb 2027"s.** 2 Feb 2027 is *not* the legacy-marking date (that is
> 2 Dec 2026). 2 Feb 2027 is separately the *Code's watermark-detection interoperability* milestone, and
> was also the Commission's *superseded original* legacy-marking proposal — two different things that share a date.

**The limit practitioners miss (Guidelines para. 153):** systems that are **partly interactive and partly
generative** benefit from the transition **only** for the Art. 50(2) marking limb. The **50(1)** disclosure
duty for direct interaction with natural persons is owed **from 2 August 2026** with no transition. A legacy
chatbot that also generates images therefore has *two different deadlines*.

**Planning rule for the skill:** present 2 Dec 2026 as **[Settled law]**. Do **not** hedge it as "adopted",
"awaiting OJ", "near-settled", "politically agreed" or "conditional" — all of those framings are superseded,
and repeating them now understates the user's obligation.

---

## Other Digital Omnibus changes (boundary awareness)

The Omnibus does more than the 50(2) grace. These do **not** change Art. 50 itself but a user may raise them:

- **High-risk application deferred:** stand-alone Annex III high-risk → **2 Dec 2027**; high-risk embedded in
  products → **2 Aug 2028**. (Art. 50 is **not** high-risk and is **not** deferred — it still runs on 2 Aug 2026.)
- **New Art. 5 prohibitions**, applying from **2 December 2026**: **Art. 5(1)(ba)** — AI systems that generate
  or manipulate realistic material depicting the intimate parts of an identifiable natural person, or sexually
  explicit activities, **without freely-given, specific, informed, unambiguous and explicit consent**; and
  **Art. 5(1)(bb)** — **CSAM** as defined in Directive 2011/93/EU, subject to the "without right" defence in
  national law (e.g. legitimate use by authorities in criminal proceedings). **Art. 5(1a)** splits the
  standard: **providers** may not place such systems on the market where that generation is the intended
  purpose or is **reasonably foreseeable and reproducible** without adequate safeguards; **deployers** are
  prohibited from use that **actually generates** such material. This is an Art. 5 *prohibition*, not an
  Art. 50 transparency duty — if a use falls here, the prohibition governs, the **€35M / 7%** band applies,
  and a 50(4) label cannot cure it (mirrors the 50(3) ↔ Art. 5 logic).
- **Sandbox deadline** for national authorities postponed to **2 Aug 2027**.
- **Adequacy-assessment procedure** simplified: a single adequacy assessment with a Commission opinion after
  consulting the AI Board. The Code of Practice has since **been assessed as adequate** under it.

---

## No retrospective marking — keyed on the date of **generation**

Final Commission Guidelines **para. 154**:

- **50(2) outputs** and **50(4) first-subparagraph deepfakes** that were **generated or manipulated before
  2 August 2026** do **not** need to be marked or labelled retroactively — *even if they are published later*.
- **Public-interest text under 50(4) second subparagraph is stricter**: it escapes only if it was **both
  AI-generated/manipulated *and* published** before 2 Aug 2026. Text **generated before** but **published on or
  after** 2 Aug 2026 **must be labelled**.
- Deployers and others holding or disseminating **pre-existing unlabelled deepfakes** are **encouraged** to
  label them, but are **not expected to make disproportionate efforts** — the Guidelines expressly name
  auditing pre-existing content databases and modifying already-printed product packaging as beyond what is
  required.

> **Common error to correct:** phrasing this as "content already *published* before 2 Aug 2026". That
> mis-states the rule for image/audio/video and only coincidentally matches the text rule.

---

## Roadmap shape (use in Phase 5 output)

1. **Immediately** — 50(1) disclosure, 50(3) notices, 50(4) labelling, and 50(2) marking + detection for
   newly-placed systems are **already applicable** (2 Aug 2026, no transition). Anything missing is a live
   exposure, not a plan item.
2. **By 2 Dec 2026** — complete 50(2) marking **and detection** for legacy generative systems (Art. 111(4)).
   Remember: a partly-interactive legacy system still owed **50(1) from 2 Aug 2026**.
3. **By 2 Dec 2026** — confirm nothing in the portfolio falls under the new Art. 5(1)(ba)/(bb) prohibitions;
   this is a **stop-shipping** question, not a labelling question.
4. **By 2 Feb 2027** — meet the Code's watermark-detection interoperability obligation (if a signatory /
   relying on the Code as the compliance route for 50(2)).
5. **Ongoing** — Code signing remains open; check the published signatory list rather than a deadline.
