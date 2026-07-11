# Worked Example — Non-Prosecution Agreement, Alibaba Group Holding Limited et al.

This example applies `enforcement-action-analysis` end-to-end to a **public** U.S.
enforcement document: a DOJ Non-Prosecution Agreement (NPA) for misdemeanor
violations of the Federal Food, Drug, and Cosmetic Act, paired with a civil
forfeiture. It demonstrates the skill's output shape on a DOJ instrument (as
opposed to Run 1's BIS administrative settlement), the alleged/admitted/adjudicated
distinction under an NPA structure, and the skill catching a document-internal
inconsistency (an apparent signature-page gap) rather than assuming it away.

All page citations refer to the source Agreement. Privilege: none — the analysis is
based solely on a public document and is a draft for attorney review.

---

## Input

A 29-page PDF: a DOJ letter agreement (U.S. Attorney's Office, District of Rhode
Island, with the DOJ Enforcement & Affirmative Litigation Branch and the Money
Laundering, Narcotics and Forfeiture Section) captioned "Alibaba.com U.S. LLC et al.
Non-Prosecution Agreement," plus Attachment A (Statement of Facts), a partial
Attachment B (Certificate of Corporate Resolutions), and Attachment C (Corporate
Compliance Program). Attachments D and E (certifications) are referenced but not
included in the provided pages. User prompt: *"Apply the skill to this enforcement
action."*

---

## Output

### At a Glance
- **Entity:** Alibaba Group Holding Limited and subsidiaries (Alibaba.com Singapore E-Commerce Pte. Limited, AliExpress E-Commerce One Pte. Ltd., Alibaba Group (U.S.) Inc., Alibaba.com U.S. LLC) — collectively "Alibaba" · **Agency:** DOJ (USAO District of Rhode Island; Enforcement & Affirmative Litigation Branch; Money Laundering, Narcotics and Forfeiture Section) · **Instrument:** Non-Prosecution Agreement · **Penalty:** $125,000,000 monetary penalty + $200,000,000 civil forfeiture = $325,000,000 (pp. 4–7)

### Parties & Instrument
- Subject entity defined broadly: Alibaba Group Holding Limited (Cayman Islands, NYSE-listed) and all subsidiaries/officers/directors/employees/agents acting within scope, expressly naming Alibaba.com Singapore E-Commerce Pte. Limited, AliExpress E-Commerce One Pte. Ltd., Alibaba Group (U.S.) Inc., and Alibaba.com U.S. LLC (p. 2).
- Instrument expressly labeled a **Non-Prosecution Agreement** for misdemeanor FDCA violations (p. 2).
- **Execution gap flagged, not assumed:** the letter names four entities as represented parties (p. 2), but the signature pages provided show execution only by Alibaba Group Holding Limited and Alibaba.com Singapore E-Commerce Pte. Ltd. (p. 17). No signature blocks for AliExpress E-Commerce One Pte. Ltd. or Alibaba.com U.S. LLC appear in the material reviewed.

### Conduct & Allegations
- **Admitted** (Statement of Facts, Attachment A, which Alibaba "agrees and stipulates ... is true and accurate," p. 18): during January 2016–December 2024, third-party sellers used the Alibaba.com (ICBU, B2B) and AliExpress (B2C) platforms to advertise, sell, and import Subject Merchandise — unapproved drugs, devices, pill-press equipment, controlled substances, listed chemicals — into the U.S. in violation of the FDCA and other Drug, Device, and Importation Laws (pp. 18–19).
- ICBU had published rules prohibiting this conduct and contractual authority to bar noncompliant sellers, but "failed to prevent some third-party sellers from circumventing controls" (p. 19).
- Some merchants used ICBU's private messaging tools to evade U.S. customs law or redirect buyers to encrypted channels; ICBU had monitoring capability but "generally did not penalize merchants unless they publicly posted prohibited goods" (p. 19).
- Government conducted 40+ undercover purchases of illegally importable goods shipped to Rhode Island (pp. 19–20). Approximately **80,000 product sales** lacked required approvals, combined gross merchandise value **greater than $200 million** (p. 20).
- **Alleged vs. admitted vs. adjudicated:** the entire factual predicate is *admitted* by stipulation (p. 18), not litigated. Nothing in the document is *adjudicated* — under the NPA structure, no court reaches the conduct unless Alibaba later breaches (pp. 9–11).

### Statutory & Regulatory Basis
| Basis | Provision | Conduct | Civil/Criminal | Status |
|---|---|---|---|---|
| FDCA | 21 U.S.C. § 301 *et seq.* | Advertisements and sales of Subject Merchandise (unapproved drugs, devices, pill-press equipment) on Alibaba Platforms; basis for the $125M monetary penalty (pp. 2, 5) | Criminal (misdemeanor) | Admitted |
| Smuggling | 18 U.S.C. § 545 | Third-party sellers' smuggling of Subject Merchandise via Alibaba Platforms; basis for the $200M forfeiture (p. 6) | Civil (forfeiture predicate) | Admitted |
| Civil forfeiture | 18 U.S.C. § 981(a)(1)(C) | Proceeds traceable to § 545 smuggling (p. 6) | Civil | Consented |
| CSA | 21 U.S.C. § 801 *et seq.* | Embedded in the "Drug, Device, and Importation Laws" definition; drives forward-looking compliance-program obligations, not charged as a violation (p. 3) | — | Neither |

### Penalties & Resolution
- **Monetary penalty:** $125,000,000 to U.S. Treasury within 30 Business Days of the Effective Date; final, non-refundable, no tax deduction, no reimbursement/indemnification (pp. 5–6).
- **Civil forfeiture:** $200,000,000 plus transfer fees, same 30-day deadline; forfeiture-procedure rights waived (pp. 6–8).
- **Total: $325,000,000** — independently corroborated by the Board Minutes' reference to a "Proposed Settlement" penalty of "US$325 million" (p. 21); the two figures reconcile.
- **Monitor:** none imposed. Oversight instead runs through a mandated Attachment C compliance program, Government-initiated compliance-monitoring requests (p. 9), and two separate rounds of executive self-certification — CEO/CCO certification within 30 days after the Term expires (p. 9) and CEO/CFO certification at expiration of the non-prosecution period (p. 11) — both deemed material statements under 18 U.S.C. §§ 1001/1519.
- **Term:** 3 years from execution, extendable up to 1 additional year for a knowing/material breach, with 30-day notice and cure (p. 4).
- **Compliance program (Attachment C):** risk assessment, enhanced Prohibited/Restricted Items policy, risk-based transaction monitoring, permanent-ban procedures, AI-based detection, a 90-day "Law Enforcement Green Channel" for expedited subpoena/warrant processing, training, confidential reporting, M&A due diligence, root-cause remediation (pp. 24–29).
- **Successor liability:** any sale/merger/corporate-form change materially affecting the Alibaba Platforms during the Term must bind the purchaser to the Agreement's obligations; noncompliant transactions are void (pp. 11–12).
- **No protection for individuals:** the Agreement expressly does not protect any individual from prosecution regardless of Alibaba affiliation (p. 9).

### Compliance Observations *(what the document itself states)*
- ICBU had written policies against the conduct and enforcement authority, but its systems "failed to prevent" circumvention (p. 19).
- Enforcement was narrower than the written policy in practice: sellers were "generally" penalized only for **publicly posted** violations, leaving private-channel conduct largely unaddressed despite monitoring capability (p. 19).
- Alibaba employees internally raised concerns about inadequate filtering; the company is described as "not sufficiently reactive or proactive" in response (p. 20).
- ICBU derived indirect profit (marketplace fees) from the activity connected to the violations, though not from the underlying goods (p. 19).

### Aggravating / Mitigating Factors
- **Aggravating:** no voluntary-self-disclosure credit — Alibaba did not timely/voluntarily disclose the conduct (p. 3); compliance failures "contributed to the offense conduct," including failures that persisted after remedial measures were already implemented (p. 3) — **Medium confidence** on the precise boundary between these two points, as both are compressed into the same sub-paragraph without a clean break in the source text.
- **Mitigating:** substantial investigative cooperation (document production, employee interviews, factual presentations, separate witness counsel) (pp. 3–4); good-faith remedial measures already taken (terminating bad-actor relationships, closing high-risk categories, compliance staffing, policy updates, training) (p. 4); forward commitment to the Attachment C program (p. 4); continued-cooperation agreement (p. 4); no prior criminal history (p. 4).

### Open Questions / Not Addressed
- **Execution of all named parties:** no signature blocks for AliExpress E-Commerce One Pte. Ltd. or Alibaba.com U.S. LLC appear despite both being named as represented parties (pp. 2, 17).
- **"Effective Date":** used repeatedly to trigger payment and notice deadlines but not expressly defined in the Definitions section as provided (p. 2).
- **Attachments D and E:** referenced (certifications) but not included in the material reviewed — their specific content is unavailable.
- **Transaction breakdown:** the $200M+ combined gross merchandise value is not split between ICBU (B2B) and AliExpress (B2C) (p. 20).
- **Parallel proceedings:** no mention of SEC, FDA, CBP, or state-regulator action; cannot be assessed from this document alone.
- **Individual liability:** the Agreement reserves the Government's ability to prosecute individuals (p. 9) but names none.

---

## What this example demonstrates

- **Alleged vs. admitted vs. adjudicated (NPA structure):** the skill held the line between Alibaba's stipulated admission of the Statement of Facts and the absence of any adjudicated finding — an NPA, unlike a litigated settlement, never puts the conduct before a court unless breach occurs.
- **Confidence bands on a compressed source paragraph:** the merged aggravating-factors sub-paragraph was marked Medium confidence rather than resolved by picking one reading.
- **Catching an inconsistency instead of smoothing it over:** four entities are named as represented parties, but only two appear on the signature pages provided. The skill flagged this as an open question about execution rather than assuming the missing entities signed — the same discipline that, in Run 1, refused to invent absent mitigating factors.
