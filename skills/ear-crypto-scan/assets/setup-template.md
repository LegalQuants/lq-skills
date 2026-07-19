Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Export Control Crypto Scan — Setup

Run this setup once before your first scan. It will ask 6 questions and produce a
configured, ready-to-run version of the scan prompt for your organization.

## How to Run

Paste this entire document into a Claude session (any model). Answer the 6 questions
when prompted. Claude will produce `export-control-crypto-scan-CONFIGURED.md` — a
version of the scan prompt pre-filled with your organization's details.

Save the configured file. Use it (not this setup script) when running actual scans.

You can re-run setup at any time to update your configuration.

---

## Setup Questions

Please answer the following 6 questions. Claude will use your answers to configure
the scan prompt.

**Q1 — Organization name:** What is your organization's name? This appears in report
headers.

[Your answer here]

**Q2 — Legal contact:** Who should scan output be delivered to? (e.g., "General
Counsel", "Legal Team", "VP Legal", a specific name+title)

[Your answer here]

**Q3 — Distribution restriction:** Who is authorized to receive the scan report
beyond legal counsel? (e.g., "Legal and Security Engineering only", "Legal and R&D
leadership only", "Legal counsel only")

[Your answer here]

**Q4 — Outside counsel:** Has your organization engaged outside export control counsel?

* Option A: Yes — [counsel name/firm if you want it in the report, or just "Yes"]
* Option B: Not yet — findings will be used to select and brief outside counsel
* Option C: Findings will be reviewed internally by [role]

[Your answer here]

**Q5 — Privilege label:** What privilege designation does your organization use for
attorney work product? (Standard options: "Attorney-Client Privileged / Attorney Work
Product / Confidential", or your organization's specific label. If unsure, use the
standard.)

[Your answer here]

**Q6 — Repository languages:** Which languages are present in the codebase you will
scan? Select all that apply: Go / Python / JavaScript / TypeScript / Java / Other: ____
(This determines which appendices to include in your configured prompt)

[Your answer here]

---

## Instructions for Claude (running this setup)

When the user has answered all 6 questions above, do the following:

1. Load the skill files from `ear-crypto-scan/` (the user should confirm the skill
   folder is in context — specifically `SKILL.md` and the relevant language appendices
   from `references/`)

2. Substitute the user's answers into the template as follows:

| Placeholder | Substitute with |
| ----------- | --------------- |
| `[YOUR_ORG]` | Answer to Q1 |
| `[LEGAL_CONTACT]` | Answer to Q2 |
| `[DISTRIBUTION_LIST]` | Answer to Q3 |
| `[OUTSIDE_COUNSEL_DESCRIPTION]` | Answer to Q4 |
| `[PRIVILEGE_LABEL]` | Answer to Q5 |
| `[MODEL_USED]` | Leave as `[MODEL_USED]` — filled in at scan time |

3. Include only the appendices relevant to Q6:

   * Go selected → include `references/appendix-go.md`
   * Python selected → include `references/appendix-python.md`
   * JavaScript or TypeScript selected → include `references/appendix-js-ts.md`
   * Java selected → include `references/appendix-java-stub.md`
   * Other → include a note: "Appendix for [language] not yet available — flag crypto
     API calls in this language as Unknown confidence for manual review"
   * Omit appendices for languages NOT selected

4. Save the result as `export-control-crypto-scan-CONFIGURED.md`

5. Confirm to the user: "Setup complete. Your configured scan prompt has been saved
   as `export-control-crypto-scan-CONFIGURED.md`. Use this file when running scans —
   paste its contents into a Claude Code session pointed at your repository root."

6. Remind the user: "If your configuration changes (new legal contact, new outside
   counsel, additional languages added to the codebase), re-run this setup to generate
   an updated configured file."
