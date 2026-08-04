# Output Templates — Mini-Report, Checklist & Compliance Block — Reference

The Phase 6 deliverables. **Lead with the light §0 blocks below**; produce the heavy artifacts — (a) the
mini-report, (b) the checklist, (c) the portable compliance block — only in **Full** mode or on request.
Fill every bracket; delete rows that are N/A; never leave a determination without a basis. Tag material
statements with an **uncertainty marker** — *[Settled law] / [Official guidance] / [Best practice] / [Open issue]*.

---

## (0) Lead with this — Bottom line, Readiness, Facts, Source status

Show these four short blocks **first**, as a conversational answer, before any formal artifact. In **Quick
triage** mode these are the *entire* output (then offer to escalate to Full).

```markdown
### Bottom line
- **Role:** [provider / deployer / both]
- **Duties triggered:** [50(1), 50(2), …] — or "none"
- **Earliest deadline:** [date] [uncertainty marker]
- **Biggest gap:** [one line]
- **Load-bearing uncertainty:** [e.g. "2 Dec 2026 grace is [Open issue] until OJ publication"]

### Readiness (operational indicator — NOT legal advice)
- **Readiness:** [Low / Medium / High]
- **Critical blockers:** [N]
- **Must-fix before earliest deadline:** [N]
- **Counsel review needed:** [yes / no] — [why]

### Facts I'm relying on  (correct me before I go further)
- Generates content: [yes/no — modalities]
- Interacts with people: [yes/no — how]
- Role: [provider / deployer / both]
- EU market-placement date: [date] → [new system / legacy]
- [any assumption I had to make]

Source status (checked [date]): Regulation incl. Art. 111(4) as amended by Reg. (EU) 2026/1744 [Settled law] ·
Art. 50 Guidelines [Official guidance, final 20 Jul 2026] · Code of Practice [final 10 Jun 2026, Best practice;
assessed as adequate, still voluntary] · EU icons [published] · no CJEU ruling on Art. 50 [Open issue].
```

> **Readiness is an operational triage heuristic, not a legal conclusion.** It flags where work and counsel
> are needed; it does not certify compliance. Keep the disclaimer attached.

---

## (a) Art. 50 Transparency Mini-Report

Follows a standard Prüfbericht (assessment-report) structure, scoped to Art. 50. Output as a fenced markdown block.

```markdown
# EU AI Act — Article 50 Transparency Assessment
## [System Name] — [Date]

---

**Report Reference:** [ref]
**Prepared by:** [name, role]
**Organisation:** [organisation]
**Date:** [date]
**Status:** [Draft / Final]

---

### 1. Subject & Scope
- **System:** [name + one-line description]
- **Modalities generated:** [audio / image / video / text / none]
- **Interaction surface:** [interacts directly with natural persons? yes/no — how]
- **Market-placement date:** [date or planned] — *(drives the 50(2) grace logic)*
- **Scope of this assessment:** Article 50 transparency duties only. Risk-tier classification, role
  determination depth, and the full obligation set are addressed by the related suite skills (§9).

### 2. Role Determination
[Provider / Deployer / Both] — [basis]. 50(1)+(2) bind the provider; 50(3)+(4) bind the deployer.

### 3. Trigger Analysis

| Duty | Binds | Applicable? | Trigger basis | Obviousness / Exception verdict |
|------|-------|-------------|---------------|---------------------------------|
| 50(1) interaction disclosure | Provider | [Yes/No] | [direct interaction with persons] | [Required / Exempt-obvious — basis] |
| 50(2) synthetic-content marking | Provider | [Yes/No] | [generates which modalities] | [Required / Assistive-exception] |
| 50(3) emotion/biometric notice | Deployer | [Yes/No] | [emotion recog / biometric categ] | [Required / Art. 5-prohibited / N/A] |
| 50(4) deepfake / PI-text labelling | Deployer | [Yes/No] | [deepfake per Art. 3(60) / PI text] | [Required / Exception: <which>] |
| 50(5) delivery quality | [owner] | [Yes/No] | [applies to <list>] | [clear/distinguishable/timely/accessible] |

### 4. Implementation Requirements (per triggered duty)
[For 50(2): layered marking — signed+timestamped metadata + imperceptible watermark; four criteria; no
single technique suffices. For 50(4): EU icon set + modality placement + WCAG contrast. For 50(1)/50(3):
notice content, placement, timing. Reference the relevant implementation file.]

### 5. Exceptions Claimed & Justification (Art. 50(6))
[Each exception relied on + documented reasoning. "None claimed" if so.]

### 6. Dated Roadmap
- **2 Aug 2026 — already applicable** — 50(1)/(3)/(4) + 50(2) for newly-placed systems (no transition).
  Anything outstanding here is a live exposure, not a plan item.
- **2 Dec 2026** — legacy 50(2) marking **and detection** — **[Settled law]**, Art. 111(4) AI Act as inserted
  by Reg. (EU) 2026/1744 (in force 27 Jul 2026). A partly-interactive legacy system still owed **50(1) from
  2 Aug 2026** (Guidelines para. 153).
- **2 Dec 2026** — new Art. 5(1)(ba)/(bb) prohibitions (non-consensual intimate imagery; CSAM) — a
  stop-shipping check, not a labelling one.
- **2 Feb 2027** — Code watermark-detection interoperability obligation.
- **Code signing** — open on a rolling basis; the 22 Jul 2026 initial-signatory deadline has passed.

### 7. Gaps & Recommendations
| # | Gap | Required action | Priority | Owner |
|---|-----|-----------------|----------|-------|
| 1 | [gap] | [action] | [High/Med/Low] | [role] |

**Penalty exposure:** non-compliance with Art. 50 → Tier 2, up to **EUR 15,000,000 or 3% of worldwide
annual turnover** (Art. 99(4)). *(Not the €35M/7% Art. 5 band.)*

### 8. Conclusion
[Summary: which duties apply, readiness, earliest binding deadline, top actions.]

---

[ART. 50 TRANSPARENCY COMPLIANCE BLOCK — see (c)]

**Disclaimer:** Structured guidance on Art. 50 transparency under Regulation (EU) 2024/1689 (as amended by
Regulation (EU) 2026/1744), the final Code of Practice on Transparency of AI-Generated Content (10 Jun 2026),
and the Commission's final Art. 50 Guidelines (20 Jul 2026). Not legal advice; the Guidelines are non-binding,
the Code is voluntary and adherence is neither conclusive evidence of compliance nor a presumption of
conformity; only the CJEU can authoritatively interpret Art. 50, and it has not yet ruled. Several tests
(appreciable resemblance, "evidently" artistic, substantiality of alteration) are expressly case-by-case.
Reassess if the Commission revises the Guidelines (para. 155) or enforcement practice develops.
```

> **Optional document export:** if the user wants a formatted document (Word / PDF / Markdown), offer to
> produce one from the report above. (The author's separate `ai-act-report` skill in the EU AI Act suite
> generates a consolidated Prüfbericht with a Word export; this standalone skill needs none of it.)

---

## (b) Per-Obligation Compliance Checklist

Emulates the obligations-matrix style. Output as a fenced block.

```markdown
## Art. 50 Compliance Checklist — [System] — [Date]

| # | Duty | Binds | Triggered | Required action | Status | Gap flag | Deadline |
|---|------|-------|-----------|-----------------|--------|----------|----------|
| 1 | 50(1) interaction disclosure | Provider | [Yes/No] | Proactive AI disclosure at first interaction | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 2 | 50(2) metadata marking (Code route) | Provider | [Yes/No] | Signed + timestamped manifest (C2PA de-facto) | [✓/◐/✗] | [gap note] | 2 Aug 2026 (legacy: 2 Dec 2026*) |
| 3 | 50(2) watermark layer | Provider | [Yes/No] | Imperceptible robust watermark; **text > 200 tokens must be watermarked** | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 4 | 50(2) detection mechanism | Provider | [Yes/No] | Detection **free of charge**, per technique; interop by 2 Feb 2027 | [✓/◐/✗] | [gap note] | 2 Feb 2027 (interop) |
| 5 | 50(3) emotion/biometric notice | Deployer | [Yes/No] | Notice to exposed persons + GDPR 13/14 | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 6 | 50(4) deepfake label | Deployer | [Yes/No] | EU icon + modality placement | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 7 | 50(5) delivery quality | [owner] | [Yes/No] | Clear/distinguishable/timely/accessible | [✓/◐/✗] | [gap note] | (with the above) |

Gap-flag legend: ✓ in place · ◐ partial · ✗ GAP · N/A not triggered
SUMMARY: [X] duties triggered · [Y] GAPs · earliest deadline [date]
*2 Dec 2026 legacy 50(2) marking+detection deadline is SETTLED LAW: Art. 111(4) AI Act, inserted by Reg. (EU) 2026/1744 (in force 27 Jul 2026). Covers the 50(2) limb only — 50(1) was owed from 2 Aug 2026.
```

---

## (c) Portable Compliance Block

Plain text, vocabulary-aligned with the classifier's `ASSESSMENT CONTEXT` block so it round-trips.

```
ART. 50 TRANSPARENCY COMPLIANCE BLOCK (paste into next skill)
System: [name]
Role(s): [provider / deployer / both]
50(1) interaction disclosure: [Required / Exempt-obvious / N/A] — [basis]
50(2) synthetic-content marking: [Required / Assistive-exception / N/A] — [grace status]
50(3) emotion/biometric notice: [Required / Art.5-prohibited / N/A]
50(4) deepfake/PI-text labelling: [Required / Exception:<which> / N/A]
50(5) delivery quality: [applies to <list> / N/A]
Any 50 trigger active: [true / false]
Earliest deadline: [date] (50(2) legacy transition 2 Dec 2026 — Art. 111(4), settled law)
Code of Practice signatory intent: [yes / no / undecided]
Source: ai-act-transparency v<X.Y>
```

> **Interchange note:** this skill emits the plain-text `ART. 50 TRANSPARENCY COMPLIANCE BLOCK` above as a
> portable summary — paste it into a broader compliance record or hand it to another assessment step. It is
> a plain-text block, not a machine-readable schema.
