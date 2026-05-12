# LQ Skills

Legal Quants — agent skills for legal work.

A curated collection of skills built by the [Legal Quants](https://legalquants.com) community (~100 lawyer-builders across 17+ jurisdictions). These skills are harness-agnostic: install once, use across Claude Code, Codex CLI, Gemini CLI, OpenCode, Cursor, and OpenClaw.

## Why

Most legal AI tools are black boxes. LQ skills are transparent, version-controlled, and practitioner-built — by lawyers who actually use them in production.

## Skills

| Skill | Author | Jurisdiction | Description |
|-------|--------|--------------|-------------|
| [statutory-analysis](skills/statutory-analysis/) | Rafal Stanislaw Fryc | US | Guide for reading, interpreting, and applying statutes |
| [customs-trade-law](skills/customs-trade-law/) | M. Onur Kafkas | US | HTS classification, CROSS ruling research, CIT/CAFC case mapping |
| [us-state-privacy-navigator](skills/us-state-privacy-navigator/) | Zachary Brenner | US | Cross-jurisdictional analysis of the US state consumer privacy patchwork. Applicability triage, gap analysis, DSAR routing, conflict-of-laws synthesis, and federal sectoral overlay analysis across all 20 comprehensive state privacy laws. Includes structured precedent corpus (82 enforcement actions), per-state AG enforcement priorities, citation discipline auditor, and DOCX deliverable generation. |
| [sgcite](skills/sgcite/) | Yu Chou Teo | SG | Verify Singapore court citations and detect hallucinated cases |
| [license-comply](skills/license-comply/) | Sam Clearwater | US | Audit open-source dependency licenses in Python projects |
| [redlines](skills/redlines/) | Hou Fu Ang | SG | Generate tracked changes in Word documents from diff output |
| [text-provenance](skills/text-provenance/) | Yu Chou Teo | SG | Identify text sources, attribute clauses, detect plagiarism |
| [office-word-diff](skills/office-word-diff/) | Yu Chou Teo | SG | Word-level tracked changes via Office.js |
| [superdoc-redlines](skills/superdoc-redlines/) | Yu Chou Teo | SG | Multi-agent DOCX redlining with conflict resolution |
| [nzbn-word-addin](skills/nzbn-word-addin/) | Joshua Wong | NZ | Validate NZ companies via NZBN register from Word |
| [bart-statutory-reference-checker](skills/bart-statutory-reference-checker/) | Kevan Wee | SG | Check statutory citations against Singapore statutes |
| [nda-review](skills/nda-review/) | Jamie Tso | Agnostic | One-way commercial NDA review with clause-by-clause issue logs |
| [vibe-legal-batch-redliner](skills/vibe-legal-batch-redliner/) | Artur Serov | UK | Batch contract redlining with playbook-driven AI |
| [lq-board-document-review](skills/lq-board-document-review/) | Alexios vdSK | MULTI | Four-category governance review: defined terms, cross-refs, matrix consistency, red flags |
| [lq-governance-playbook-benchmark](skills/lq-governance-playbook-benchmark/) | Alexios vdSK | MULTI | Benchmark governance docs against LQ Playbook with five-tier classification |
| [classify-ccp](skills/classify-ccp/) | Leona Zhang | Agnostic | Classify treatment of Competition Compliance Programmes (CCPs) in competition-law enforcement documents — offence, defence, remedy, or irrelevant |
| [adversarial-qc](skills/adversarial-qc/) | Alexios vdSK | Agnostic | Adversarial quality control for AI deliverables — two-agent parallel verification with checklist, agreements/disagreements flagged for human review |
| [collating-reviewer-feedback](skills/collating-reviewer-feedback/) | AnonLQ | Agnostic | Compile DOCX comments and tracked changes into a lawyer-controlled resolution checklist |
| [uk-citation-verification](skills/uk-citation-verification/) | AnonLQ | UK | Verify UK citations against public authority sources and flag hallucinated or mismatched authorities |
| [proposition-checking](skills/proposition-checking/) | AnonLQ | Agnostic | Check whether cited materials actually support legal and factual propositions |
| [building-chronologies](skills/building-chronologies/) | AnonLQ | Agnostic | Build sourced chronologies from legal documents, correspondence, disclosure, and pleadings |
| [uk-witness-statement-review](skills/uk-witness-statement-review/) | AnonLQ | England and Wales | Review witness statements for source support, CPR compliance, and evidential risk |
| [uk-particulars-of-claim-review](skills/uk-particulars-of-claim-review/) | AnonLQ | England and Wales | Review draft Particulars of Claim for pleaded elements, CPR/PD16 structure, remedies, and gaps |
| [uk-disclosure-list-review](skills/uk-disclosure-list-review/) | AnonLQ | England and Wales | Review disclosure lists for document coverage, inspection objections, privilege flags, and adverse documents |
| [uk-court-of-appeal-judicial-preference-check](skills/uk-court-of-appeal-judicial-preference-check/) | AnonLQ | England and Wales | Check appellate drafts against public-source Court of Appeal judicial preference signals |
| [local-first-legal-workspace](skills/local-first-legal-workspace/) | AnonLQ | Agnostic | Audit privacy boundaries for local-first legal AI workspaces and BYOK workflows |
| [legal-claim-economics](skills/legal-claim-economics/) | AnonLQ | Agnostic | Model claim economics, funding structures, fee arrangements, and recovery waterfalls |
| [corporate-registry-investigation](skills/corporate-registry-investigation/) | AnonLQ | UK | Investigate UK companies using Companies House officers, PSCs, charges, and filings |
| [action-items-from-client-alert](skills/action-items-from-client-alert/) | Kevin Keller | Agnostic | Extract time-sensitive action items, deadlines, and obligations from client alerts/bulletins into a deadline-organized checklist |
| [comms-improver](skills/comms-improver/) | Kevin Keller | Agnostic | Rewrite legal-jargon-heavy text into plain language for a specified non-legal audience |
| [contract-qa](skills/contract-qa/) | Kevin Keller | Agnostic | Answer specific questions about a loaded contract — meaning, location, unusualness, comparison, scenario analysis — with verbatim citations |
| [dpa-checklist-review](skills/dpa-checklist-review/) | Kevin Keller | Multi-regime | Score a DPA/BAA against required terms under GDPR Art 28, US state privacy laws, or HIPAA |
| [enhance-prompt](skills/enhance-prompt/) | Kevin Keller | Agnostic | Rewrite a short/vague prompt into a structured legal prompt with role, jurisdiction, task, constraints, and output format |
| [msa-review-commercial-purchase](skills/msa-review-commercial-purchase/) | Kevin Keller | US | Review Master Purchase/Supply/Goods Agreements with severity-rated findings, redlines, and buyer/supplier-calibrated assessment |
| [msa-review-saas](skills/msa-review-saas/) | Kevin Keller | US | Review SaaS MSAs/Subscription Agreements with severity-rated findings, redlines, and vendor/customer-calibrated assessment |
| [skill-creator](skills/skill-creator/) | Kevin Keller | Meta | Conduct focused conversation to elicit a skill's behaviour and produce a complete skill folder ready to save |
| [vendor-privacy-policy-first-pass](skills/vendor-privacy-policy-first-pass/) | Kevin Keller | Multi-regime | Fast triage of a vendor privacy policy — what it says, red flags warranting escalation |
| [coquill](skills/coquill/) | Hou Fu Ang | Agnostic | Document assembly orchestrator — matches user requests to docx/HTML templates, interviews for variables, renders documents. Bundles three internal sub-skills (`coquill-analyzer`, `coquill-renderer`, `coquill-transcriber`) used by the orchestrator |
| [foreign-law-research](skills/foreign-law-research/) | Chong Liu | Multi-jurisdiction | Researching foreign law questions with structured workflow, source authority hierarchy, timeliness grading, and smart navigation |
| [legal-translation](skills/legal-translation/) | Arjun Singh Chouhan | Agnostic | Legal document translation that understands law, not just language — covers all language pairs, transliteration, bilingual documents, and legal terminology lookups |
| [california-property-tax](skills/california-property-tax/) | Legal Quants community | US-CA | California property tax research workflow using BOE Property Tax Rules (462.* change of ownership) and PTLG annotations (220.*); rule/annotation synthesis applied to user facts |
| [case-file-analyzer](skills/case-file-analyzer/) | Dennis G. Jansen | Agnostic | Stateless R.A.L.P.H.-pattern agent for adversarial case-file analysis — extracts facts/claims/legal views into XML metadata across large directories, then synthesizes contradictions and timeline. Proof of concept |

See [ACCESS-MODES.md](ACCESS-MODES.md) for source-handling conventions, [PR-READINESS.md](PR-READINESS.md) for the AnonLQ-attributed contribution checklist, and [skills/CONTRIBUTING.md](skills/CONTRIBUTING.md) for the higher-bar process applied to skills carrying legal substance.

## Installation

### OpenClaw
```bash
clawhub install lq-skills --registry https://github.com/LegalQuants/lq-skills
```

### Claude Code / Codex CLI
```bash
git clone https://github.com/LegalQuants/lq-skills.git
```

### Gemini CLI
```bash
gemini extensions install https://github.com/LegalQuants/lq-skills
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache License 2.0 for the project and AnonLQ-attributed skills (see [LICENSE](LICENSE)).

Several community skills imported from their authors' own GitHub repos retain their original MIT licenses, which are compatible with Apache 2.0:

- `skills/classify-ccp/` — MIT, Copyright Leona Zhang
- `skills/adversarial-qc/` — MIT, Copyright Alexios van der Slikke-Kirillov
- `skills/coquill/` (and `coquill-analyzer`, `coquill-renderer`, `coquill-transcriber`) — MIT, Copyright Ang Hou Fu
- `skills/foreign-law-research/` — MIT, Copyright Chong Liu
- `skills/legal-translation/` — MIT, Copyright Arjun Singh Chouhan

Other community skills inherit the project-level Apache 2.0 license unless they include their own `LICENSE` file.
