# AnonLQ Skills

Legal workflow skills contributed under the AnonLQ banner.

These skills are written to be harness-agnostic. They are intended for use in Claude Code, Claude Desktop/API environments with skill support, and other Agent Skills-compatible tools, subject to each harness's installation, skill-loading, file-access, web-search, and MCP support.

## Skills

| Skill | Jurisdiction | Description |
|---|---|---|
| [collating-reviewer-feedback](skills/collating-reviewer-feedback/) | Agnostic | Compile DOCX comments and tracked changes into a lawyer-controlled resolution checklist |
| [uk-citation-verification](skills/uk-citation-verification/) | UK | Verify UK citations against public authority sources and flag hallucinated or mismatched authorities |
| [proposition-checking](skills/proposition-checking/) | Agnostic | Check whether cited materials actually support legal and factual propositions |
| [building-chronologies](skills/building-chronologies/) | Agnostic | Build sourced chronologies from legal documents, correspondence, disclosure, and pleadings |
| [uk-witness-statement-review](skills/uk-witness-statement-review/) | England and Wales | Review witness statements for source support, CPR compliance, and evidential risk |
| [uk-particulars-of-claim-review](skills/uk-particulars-of-claim-review/) | England and Wales | Review draft Particulars of Claim for pleaded elements, CPR/PD16 structure, remedies, and gaps |
| [uk-disclosure-list-review](skills/uk-disclosure-list-review/) | England and Wales | Review disclosure lists for document coverage, inspection objections, privilege flags, and adverse documents |
| [uk-court-of-appeal-judicial-preference-check](skills/uk-court-of-appeal-judicial-preference-check/) | England and Wales | Check appellate drafts against public-source Court of Appeal judicial preference signals |
| [local-first-legal-workspace](skills/local-first-legal-workspace/) | Agnostic | Audit privacy boundaries for local-first legal AI workspaces and BYOK workflows |
| [legal-claim-economics](skills/legal-claim-economics/) | Agnostic | Model claim economics, funding structures, fee arrangements, and recovery waterfalls |
| [corporate-registry-investigation](skills/corporate-registry-investigation/) | UK | Investigate UK companies using Companies House officers, PSCs, charges, and filings |

## Source Access

Skills that check citations, filings, judgments, registry records, procedural rules, or calculations do not bundle API keys or tool access. They work from live web/browser/MCP/custom tools when configured, or from user-supplied documents and exports. See [ACCESS-MODES.md](ACCESS-MODES.md) for the standard fallback behaviour when sources are unavailable.

## Examples

Each skill is self-contained and includes a compact local example in its own `examples/output.md` file.

## Evals and PR Readiness

Each skill includes its own local `evals.yaml`, so a single-skill installation can still be tested without repository-level files. See [evals/README.md](evals/README.md) for how to run them. Use [PR-READINESS.md](PR-READINESS.md) before submitting these skills to another public repository.

## License

MIT. Each skill also includes its own `LICENSE` file.
