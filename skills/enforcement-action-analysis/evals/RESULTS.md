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

### Run 2 — [document title]

- **Source:** [agency] · [URL] · [instrument type]
- **Date run:** [YYYY-MM-DD] · **Skill version:** 1.0.0
- **Model / harness:** [...]

| C1 | C2 | C3 | C4 | C5 | C6 | Overall |
|----|----|----|----|----|----|---------|
| ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | PASS / FAIL |

**Notes:** [suggest a different instrument type — e.g., an OFAC settlement or DOJ DPA — to test the template across agencies]

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

- **Documents run:** 1 · **Pass:** 1 · **Fail:** 0
- **Patterns observed:** On a complex real BIS export-control matter, the skill held its core disciplines — page citations, the alleged/admitted/adjudicated distinction, and (critically) refusing to invent mitigating factors that a typical enforcement action would contain but this one did not.
- **Skill edits prompted by this eval:** none.
