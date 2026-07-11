# Worked Example — BIS Order, Applied Materials, Inc. & Applied Materials Korea

This example applies `enforcement-action-analysis` end-to-end to a **public** U.S.
enforcement document: a Bureau of Industry and Security (BIS) Order and Settlement
Agreement under EAR § 766.18(a). It demonstrates the skill's output shape, its page-
citation discipline, the alleged/admitted/adjudicated distinction, and — most
importantly — its refusal to invent factors the source does not contain.

All page citations refer to the source Order/Settlement Agreement. Privilege: none —
the analysis is based solely on a public document and is a draft for attorney review.

---

## Input

A 56-page BIS PDF comprising a 19-page Order, the Settlement Agreement, and a
Schedule of Violations. The respondents are Applied Materials, Inc. (Santa Clara, CA)
and Applied Materials Korea, Ltd. The matter concerns reexports of ion-implanting
equipment (ECCN 3B991) to SMIC in China via South Korea. User prompt: *"Apply the
skill to this PDF enforcement action."*

---

## Output

### At a Glance
- **Entity:** Applied Materials, Inc. (Santa Clara, CA) & Applied Materials Korea, Ltd. — collectively "AMAT" · **Agency:** BIS (Commerce) · **Instrument:** Settlement Agreement + Order under EAR § 766.18(a) · **Penalty:** $252,500,300 civil penalty (p. 14)

### Parties & Instrument
- **Respondents:** Applied Materials, Inc. (Delaware-incorporated, Santa Clara HQ) and Applied Materials Korea, Ltd. (AMK, South Korea) (pp. 1–2).
- **Related entities named:** Varian Semiconductor Equipment ("VSE"), AMAT subsidiary operating the Gloucester, MA plant (acquired 2011); AMK, the South Korea subsidiary; Global Engineering, a South-Korean third-party contractor supplying assembly/testing labor (pp. 2–3).
- **Entity-List counterparties:** SMIC and six named subsidiaries (SMSC, SMNC, SMIC-TJ, SMIC-BJ, SMIC-SZ, SMIC-SH), added to the Entity List Dec. 18, 2020 (pp. 3–4).
- **Instrument:** Settlement Agreement under § 766.18(a); AMAT **admits** committing the alleged conduct (p. 14). A settled, admitted matter — not adjudicated after contest.

### Conduct & Allegations
- **Admitted conduct:** 56 violations of the EAR between Nov. 8, 2020 and July 18, 2022 — reexport or attempted reexport of ion-implanting equipment (ECCN 3B991) from AMK in South Korea to SMIC in China without required licenses (pp. 2, 14). Total equipment value ≈ $126,250,150 (p. 2).
- **Mechanism ("dual-build"):** After a Sept. 25, 2020 BIS "is-informed" letter and SMIC's Dec. 18, 2020 Entity-List addition, AMAT shifted part of its Gloucester production to South Korea — partially building equipment in the U.S. on a SMIC order, shipping all U.S.- and foreign-origin parts to AMK for final assembly/testing, then reexporting to SMIC — on the theory that "substantial transformation" in Korea rendered the goods foreign-made (pp. 7–11).
- **Alleged vs. admitted vs. adjudicated:** framed throughout as *alleged* in the Proposed Charging Letter, but AMAT **expressly admits** the conduct in the Settlement Agreement (p. 14). **Not adjudicated** — no contested finding by a tribunal.

### Statutory & Regulatory Basis
| Charges | Provision | Conduct | Civil/Criminal | Status |
|---|---|---|---|---|
| 1–54 | 15 C.F.R. § 764.2(a) — engaging in prohibited conduct | Caused reexport of ion-implanting equipment of 54 implanters (≈ $118,450,150) from AMK to SMIC without a license (pp. 5–6) | Civil (administrative) | Admitted |
| 55–56 | 15 C.F.R. § 764.2(c) — attempting prohibited conduct | Two attempted reexports (≈ $3,900,000 each) to SMNC (Nov. 8, 2020) and SMIC-SZ (July 18, 2022) (p. 6) | Civil (administrative) | Admitted |

- Underlying licensing bases: EAR Entity-List controls, 15 C.F.R. § 744.11; military-end-use "is-informed" authority, § 744.21(b) (pp. 3–5).

### Penalties & Resolution
- **Civil penalty:** $252,500,300, due within 30 days (p. 14).
- **Compliance audits:** Two annual internal audits of AMAT's export-controls compliance program (covering semiconductor-equipment exports to/within China), reports due to the BIS Boston Field Office by July 1, 2027 and July 1, 2028 (pp. 14–15).
- **Denial of export privileges:** Three-year denial, **suspended** and thereafter **waived**, conditioned on full/timely penalty payment and timely audit completion; may be activated on non-compliance (pp. 15–16).
- **Ongoing undertakings:** Continue export-control training, maintain internal/external non-compliance notification procedures, and maintain an anonymous reporting hotline (p. 18, NINTH).
- **Conditions on licenses:** Compliance made a condition of any AMAT export license/privilege (p. 17, SIXTH).
- **Publicity:** Charging Letter, Settlement Agreement, and Order made public (p. 18, TENTH).

### Compliance Observations *(what the document itself states)*
- AMAT maintained an export-compliance program "tailored to its risk profile" and had applied for 1,100+ BIS licenses overall, 100+ for SMIC (pp. 2–3).
- **Root cause per the Order:** AMAT's Global Trade Group applied a "substantial transformation" test — a Customs concept that "does not appear anywhere in the EAR" — to conclude the Korea-assembled equipment was foreign-made (pp. 10–11).
- AMAT built a "substantial transformation" checklist, ran automated system blocks on SMIC shipments, then **manually overrode** those blocks when a shipment met the checklist (p. 11).

### Aggravating / Mitigating Factors
- **Aggravating (Medium confidence — drawn from the narrative; the Order does not include a formal penalty-factors analysis in the reviewed pages):** conduct continued *after* the is-informed letter and Entity-List addition; internal urgency to "go into hyper drive on [South] Korea" (p. 8); senior-leadership engagement; revenue motive (SMIC business valued at $112–150M/yr, >$1B total impact) (p. 10).
- **Mitigating:** **Not expressly stated.** The Order describes AMAT's mistaken "substantial transformation" belief (pp. 10–12) but does **not** characterize it as good-faith mitigation, and there is **no** mention of voluntary self-disclosure or cooperation credit in the reviewed pages. Flagged rather than inferred.

### Open Questions / Not Addressed
- **Penalty composition:** the $252,500,300 figure is not broken into components, and its relationship (if any) to the ≈$126M equipment value is not explained (p. 14). *(Medium confidence the two are related; not stated.)*
- **Voluntary self-disclosure / cooperation credit:** not addressed — unclear whether either applied.
- **Parallel proceedings:** the Order does not reference any concurrent DOJ, OFAC, or other-agency action, so cross-agency credit cannot be assessed from this document alone.
- **Individual liability:** no individuals are charged; the Order addresses the entities only.
- **Schedule of Violations detail:** the per-shipment Schedule is referenced but was not part of the reviewed pages.

---

## What this example demonstrates

- **Alleged vs. admitted vs. adjudicated (§ 766.18 settlement):** the skill captured the express admission (p. 14) without upgrading it to an adjudicated finding.
- **Confidence bands in practice:** aggravating factors and penalty composition were marked Medium (narrative-derived / not expressly stated), not asserted as fact.
- **Refusing the mitigating-factors trap:** most enforcement actions recite voluntary self-disclosure or cooperation credit. This one does not. The skill flagged their absence and routed them to Open Questions instead of inventing them — the core discipline the skill enforces.
