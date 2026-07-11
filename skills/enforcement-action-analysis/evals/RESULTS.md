# Corpus-Grade Eval Results — enforcement-action-analysis

Real-document eval per `skills/CONTRIBUTING.md` (Gold tier). Each run applies the
skill to a **public** enforcement document and scores the output against the
skill's own commitments. No privileged or internal material is used.

## Scoring criteria

| Code | Criterion | Fail condition |
|------|-----------|----------------|
| C1 | All 8 output sections present (or omitted with a stated reason) | Section silently dropped |
| C2 | Every bullet carries a page citation | Uncited factual claim |
| C3 | Alleged / admitted / adjudicated preserved | Characterization upgraded to fact |
| C4 | Confidence bands applied (ambiguity flagged, not guessed) | Silent single reading of an ambiguous item |
| C5 | Genuinely-absent items routed to Open Questions | Invented detail to fill a gap |
| C6 | No hallucinated figure, statute, or party | Any fabricated value (auto-fail overall) |

## Runs

### Run 1 — BIS Order & Settlement Agreement, Applied Materials, Inc. & Applied Materials Korea

- **Source:** Bureau of Industry and Security (Commerce) · public Order + Settlement Agreement under EAR § 766.18(a) · 56-page PDF (19-page Order + Settlement Agreement + Schedule of Violations)
- **Instrument type:** administrative settlement (export controls / EAR Entity List)
- **Date run:** 2026-07-10 · **Skill version:** 1.0.0
- **Model / harness:** Claude Code, Opus 4.8

| C1 | C2 | C3 | C4 | C5 | C6 | Overall |
|----|----|----|----|----|----|---------|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **PASS** |

**Notes:**
- Produced all eight sections; every bullet cited to a page.
- **C3 (hardest test):** correctly captured that AMAT *admits* the conduct under § 766.18(a) (p. 14) while flagging that the matter is settled/admitted, **not adjudicated**. A weaker read would have collapsed "alleged" and "admitted."
- **C5 / mitigating-factors trap:** the document contains no voluntary-self-disclosure or cooperation-credit statement and no formal penalty-factors analysis. The skill **flagged their absence** and routed them to Open Questions rather than inventing them — the key discipline this skill exists to enforce.
- **C4:** aggravating factors and the penalty-composition question were marked Medium confidence (drawn from narrative / not expressly stated) rather than asserted as fact.
- Figures ($252,500,300 penalty; ≈$126,250,150 equipment value; ECCN 3B991) and statutes (§ 764.2(a)/(c)) all traced to the source.
- **Limitation of this run:** self-assessment by the same model that produced the output — a demonstration of the skill's behavior, not an independent audit. A second reviewer or a fresh-session re-run is the stronger check.
- **Skill edits prompted:** none. Output shape and disciplines held on a complex, real multi-part instrument.

---

### Run 2 — Non-Prosecution Agreement, Alibaba Group Holding Limited et al.

- **Source:** DOJ · U.S. Attorney's Office, District of Rhode Island (with DOJ Enforcement & Affirmative Litigation Branch and Money Laundering, Narcotics and Forfeiture Section) · public Non-Prosecution Agreement + Statement of Facts + Corporate Compliance Program attachment · 29-page PDF
- **Instrument type:** Non-Prosecution Agreement (NPA) — misdemeanor FDCA violation + civil forfeiture (first DOJ/NPA instrument in this corpus; Run 1 was a BIS administrative settlement)
- **Date run:** 2026-07-10 · **Skill version:** 1.0.0
- **Model / harness:** Claude Code, Sonnet 5

| C1 | C2 | C3 | C4 | C5 | C6 | Overall |
|----|----|----|----|----|----|---------|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **PASS** |

**Notes:**
- Produced all eight sections; every bullet cited to a page.
- **C3:** correctly held the line between the Statement of Facts, which Alibaba *admits* is true and accurate (p. 18), and the absence of any adjudicated finding — the NPA structure means no court ever reaches the conduct unless Alibaba breaches.
- **C4:** flagged the CSA's role as Medium confidence — it is folded into the "Drug, Device, and Importation Laws" definition and drives the forward-looking compliance program, but the document does not state Alibaba admitted a CSA violation the way it does for the FDCA misdemeanor. Also flagged the Section D aggravating-factors paragraph (lack of voluntary-disclosure credit run together with post-remediation compliance failures) as ambiguously drafted rather than picking one reading.
- **C5 (notable catch):** the letter names four Alibaba entities as parties represented by counsel (p. 2), but the signature pages provided show execution only by Alibaba Group Holding Limited and Alibaba.com Singapore E-Commerce Pte. Ltd. (p. 17) — no signature blocks for AliExpress E-Commerce One Pte. Ltd. or Alibaba.com U.S. LLC appear in the material reviewed. The skill flagged this as an open question about execution rather than assuming all four entities signed. Also routed the undefined "Effective Date" trigger and the unprovided Attachments D/E to Open Questions rather than guessing their contents.
- Figures ($125M penalty, $200M forfeiture, $325M total — reconciled against the Board Minutes' independent $325M reference on p. 21) and statutes (FDCA 21 U.S.C. § 301; 18 U.S.C. § 545; 18 U.S.C. § 981(a)(1)(C)) all traced to the source.
- **Limitation of this run:** self-assessment by the same model that produced the output — a demonstration of the skill's behavior, not an independent audit.
- **Skill edits prompted:** none. Output shape and disciplines held on a second, structurally different instrument type (NPA vs. Run 1's administrative settlement), including catching a signature-page inconsistency the skill was never explicitly instructed to look for.

---

### Run 3 — [document title]

- **Source:** [agency] · [URL] · [instrument type]
- **Date run:** [YYYY-MM-DD] · **Skill version:** 1.0.0
- **Model / harness:** [...]

| C1 | C2 | C3 | C4 | C5 | C6 | Overall |
|----|----|----|----|----|----|---------|
| ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | PASS / FAIL |

**Notes:** [...]

## Summary

- **Documents run:** 2 · **Pass:** 2 · **Fail:** 0
- **Patterns observed:** Across a BIS export-control settlement and a DOJ Non-Prosecution Agreement — two structurally different instrument types — the skill held its core disciplines: page citations, the alleged/admitted/adjudicated distinction, and refusing to invent mitigating factors or resolve genuine gaps (missing signatures, undefined terms, unprovided attachments) by guessing.
- **Eval variable — model:** Run 1 used Opus 4.8; Run 2 used Sonnet 5. Holding the disciplines across two different models (including a smaller one) strengthens the robustness read, but it is an uncontrolled variable — cross-run differences could be model- as well as skill-driven. Future runs should record the model and, where possible, hold it constant to isolate skill behavior.
- **Skill edits prompted by this eval:** none.
