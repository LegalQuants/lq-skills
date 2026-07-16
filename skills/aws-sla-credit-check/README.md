# aws-sla-credit-check

Analyze AWS operational incidents against AWS's published Service Level Agreements to identify potential service credit eligibility and generate an action-item memo with claim deadlines.

## The problem

AWS SLA credits are claim-based: the customer must detect the incident, connect it to the correct published SLA, and file a support case before a deadline. The detection lives with operations, the contract knowledge lives with legal, and the deadline belongs to nobody. Credits routinely expire unclaimed, not because the analysis is hard, but because no one performs it in time.

## What this skill does

Given an AWS incident (or a lookback window), the agent:

1. Establishes the incident facts from the public AWS Health Dashboard status history
2. Fetches the current published SLA for each affected service
3. Extracts the credit mechanics (commitment definitions, credit tiers, exclusions, claim procedure, deadline) with a citation for every value
4. Computes potential credit eligibility, showing the arithmetic
5. Produces a memo with the claim deadline as a date and a checklist of the internal facts to verify before filing

Everything is public-data-only and descriptive. The skill never asserts that credits are owed; actual eligibility depends on the customer's usage, architecture, and any negotiated agreement, which the skill explicitly routes to human verification.

## Installation

### Claude Code / Codex CLI

Clone or copy the `aws-sla-credit-check` folder into your skills directory. The skill needs no dependencies beyond the harness's ability to fetch public web pages.

### Other harnesses

The skill is a methodology document (SKILL.md). Any harness that loads agent skills and can fetch URLs can run it.

## Example usage

> "AWS had an incident in us-east-1 yesterday affecting EC2 and EBS. Check whether we might be owed SLA credits and what the deadline is."

> "Sweep the last 45 days of AWS incidents for anything potentially claimable, ranked by how soon the claim window closes."

> "Explain the current S3 SLA credit tiers with citations."

## How it was tested

Run against historical AWS incidents with publicly documented durations, checked against the current published SLAs for EC2, EBS, S3, Lambda, and RDS. The citation-per-value extraction discipline mirrors the author's Compute Terms Observatory (https://github.com/erinecrum/compute-terms-observatory), a public archive and comparison of cloud providers' published legal terms, and a continuously running SLA event radar built on the same public sources.

## Limitations

Public data only; conditional output; SLA definitions and deadlines controlled by the current published text, which the skill fetches fresh rather than remembering; AWS-scoped in v1 (the methodology extends to other providers' published SLAs and extensions are welcome). Not legal advice.

## Author

Erin Crum. California-licensed technology transactions attorney; in-house counsel leading cloud infrastructure and AI commercial work, including serving as legal lead on a multi-billion dollar hyperscaler agreement.

## License

MIT
