---
name: aws-sla-credit-check
description: Analyze AWS operational incidents against AWS's published Service Level Agreements to identify potential service credit eligibility, calculate the applicable credit tier, and generate an action-item memo with claim deadlines. Use when an AWS incident has occurred or when doing a periodic sweep for unclaimed credits.
author: Erin Crum
version: 1.0.0
last_reviewed: 2026-07-15
review_cadence: At least every 6 months, and on any structural change to AWS's SLA index or claim-window language.
jurisdiction: Agnostic
tags: [cloud-infrastructure, sla-review, incident-response, contract-review]
---

# AWS SLA Credit Check

Cloud providers do not pay SLA credits automatically. AWS requires the customer to detect the incident, connect it to the correct published SLA, and submit a claim within a deadline. In practice this chain breaks constantly: the operations team sees the outage, the legal team owns the contract, and nobody owns the join. Credits expire unclaimed.

This skill teaches the agent to perform that join using only public documents: the AWS Health Dashboard status history and AWS's published per-service SLAs. The output is a memo a lawyer or FinOps owner can act on, never a legal conclusion.

## When to Use

- An AWS incident just happened and you want to know within the claim window whether a credit claim may be available.
- Periodic sweep: reviewing the last 30 to 60 days of AWS incidents for potentially claimable events before claim windows close.
- Drafting the internal action item or the support case that starts a credit claim.
- Explaining to a stakeholder how a specific AWS service's credit mechanics work, with citations to the current SLA.

Do NOT use this skill to state that credits are actually owed. Actual eligibility depends on facts the public record cannot show: whether the customer ran affected resources in the affected region during the incident window, the customer's architecture (some SLAs require multi-AZ deployment for the commitment to apply), and any negotiated agreement that modifies the published SLA. The skill's output is always "potential eligibility, verify against your usage."

## How It Works

The agent works through five steps. Every extracted value must carry a citation to its source URL and the date fetched. If a value cannot be confidently located, record it as "not specified" and flag it. Never guess a commitment percentage, credit tier, or deadline.

### Step 1: Establish the incident facts

Identify from public sources:

- Affected service(s) and region(s)
- Incident start and end time (or best public approximation)
- Nature of the event, capturing AWS's exact event label verbatim (for example, "Increased Launch Template API Error Rates" versus "Increased Error Rate and Latency" versus a connectivity/power loss). The label matters: an API-error event is not the same as instances losing external connectivity, and it determines whether the event can meet an SLA's defined "Unavailable" threshold in Step 3.

Sources: the AWS Health Dashboard public status history (https://health.aws.amazon.com/health/status), AWS post-event summaries when published, and reputable secondary reporting only to corroborate timing. Record which source supports each fact. If the public record does not establish duration, say so; duration drives everything downstream.

**Reading the Health Dashboard correctly.** The status page is a JavaScript-rendered application: a plain URL fetch returns an essentially empty page and will silently miss every event. Use a browser tool that executes JavaScript. Once it loads, the default **"Open and recent issues"** view shows only currently open or very recent events — it will not show a resolved incident from days or weeks ago. Resolved incidents live under the separate **"Service history"** tab, a running 12-month log of interruptions listed by service, region, and start/last-update time (all times in Pacific Time). Open Service history, then locate the specific event by region and date. Do not rely on the default view, and do not rely on web search alone — search surfaces news coverage of large outages but misses smaller resolved events (and can mislead you with a dashboard page's current-day header date). When an event's detail page or duration cannot be read from public sources, record that explicitly rather than inferring a duration.

### Step 2: Fetch the current published SLA for each affected service

AWS maintains per-service SLAs indexed at https://aws.amazon.com/legal/service-level-agreements/. Fetch the current SLA page for each affected service at analysis time. Do not rely on remembered values: AWS revises SLAs, and the version in force matters. Record the URL and fetch date.

If a service has no published SLA, record that finding explicitly. It is a materially useful answer.

### Step 3: Extract the credit mechanics

From each fetched SLA, extract into a structured table:

- The commitment metric and threshold(s) (for example, Monthly Uptime Percentage of 99.99%), including how the SLA defines the metric, since definitions differ by service (per-region, per-AZ, per-instance, request-error-rate based)
- The credit tiers (which percentage band triggers which credit percentage)
- What the credit applies to (usually the monthly charges for the affected service in the affected region)
- Architectural preconditions, if any (for example, instance-level versus region-level commitments, multi-AZ requirements)
- Exclusions that could defeat the claim
- The claim procedure: where the claim is submitted (typically an AWS Support case), what evidence the SLA requires the customer to include, and the claim deadline, quoted exactly as the SLA states it

Every row cites the SLA section it came from.

### Step 4: Compute potential eligibility

Convert incident duration into the SLA's metric. For a Monthly Uptime Percentage SLA, downtime minutes divide by total minutes in the billing month; state the arithmetic explicitly so a reviewer can check it. Map the result against the credit tiers from Step 3 and state which tier the public facts are consistent with.

Present this as a conditional: "IF you ran [service] in [region] during the incident window and meet the SLA's architectural preconditions, the published tiers indicate a potential credit of [X]% of the monthly charges for that service in that region." Show the sensitivity where duration is uncertain (for example, the tier at 45 minutes of downtime versus 90).

### Step 5: Generate the action-item memo

Produce a short memo containing:

1. Incident summary with sourced facts
2. Per-service table of credit mechanics with citations
3. Potential eligibility calculation with the arithmetic shown
4. The claim deadline, stated as a date, computed from the SLA's deadline language and the incident date, flagged prominently
5. Concrete next steps: what internal usage facts must be verified, who verifies them (FinOps or the cloud platform team), and what goes in the support case
6. A standing disclaimer: this analysis reads published documents only, is not legal advice, and must be verified against current source documents and the customer's own agreement, which may replace or modify the published SLA

## Confidence bands

Every output states its confidence, and low confidence is never suppressed to make the memo look finished.

- **High** — the incident facts (service, region, window) and the current SLA text are each read directly from the cited public sources, and the duration clears or misses a tier threshold by a wide margin. Proceed and present the memo as described above.
- **Medium** — a material fact is only partially established: duration is an event *envelope* rather than confirmed continuous unavailability, or a service's impact comes only from secondary reporting. Proceed, but flag the fact, show tier sensitivity across the plausible range, and state in the memo exactly what verification would move it to High.
- **Low** — a value required for the tier call cannot be located, the SLA has been restructured so the mapping is unclear, or the event label does not map to the SLA's defined "Unavailable." Do **not** compute a tier. Name the uncertainty explicitly and hand the question back to the human. A blank is a valid, useful answer; a guessed tier is not.

## Escalation triggers

Stop the affected branch cleanly, state which trigger fired and why, and route the open question to the named human owner (FinOps, cloud platform, or counsel) when any of these fire — rather than proceeding past the skill's limits:

- **No published SLA** for an affected service, or the SLA index no longer resolves to a per-service page. Record the finding; never substitute a remembered value.
- **Event label does not map** to the SLA's defined "Unavailable" (for example, an API-error-rate event measured against a connectivity-based commitment). Surface the mismatch instead of forcing the mapping.
- **Duration cannot be established** from the public record. Flag it; do not infer a duration to complete the arithmetic.
- **Negotiated or enterprise agreement suspected** (EDP, PPA, custom MSA). The published SLA may be modified or superseded — route to counsel with the full contract before any reliance.
- **Non-AWS provider, or an AWS service outside the tested set.** Out of scope for v1; say so and stop rather than generalizing the methodology silently.
- **Conflicting signals** across the Health Dashboard, an AWS post-event summary, and secondary reporting. Present the conflict; do not silently select one source.

## Examples

Example prompt:

> "AWS had an incident in us-east-1 yesterday affecting EC2 and EBS. Check whether we might be owed SLA credits and what the deadline is."

Expected agent behavior: fetch the Health Dashboard history to establish scope and duration; fetch the current EC2 SLA (noting it contains both a region-level and an instance-level commitment with different tiers) and the EBS SLA; build the credit-mechanics table with citations; compute the potential tier from the public duration; produce the memo with the claim deadline as a date and the verification checklist.

Example prompt:

> "Sweep the last 45 days of AWS incidents for anything potentially claimable."

Expected agent behavior: enumerate incidents from the status history in the window; triage out incidents too short to cross any published threshold (showing the threshold math for the triage decision); run Steps 2 through 5 on the survivors; rank by claim deadline proximity.

A complete worked example — the full memo produced for the May 7–8 2026 us-east-1 EC2 event, with the credit-tier ladder, the deadline computation, and a contrasting non-qualifying event — is in [examples/output.md](examples/output.md).

## Limitations

- **Public data only.** The skill cannot see the customer's usage, spend, architecture, or negotiated agreement. Everything it produces is conditional on facts the customer must verify. Enterprise agreements may modify or supersede published SLAs entirely.
- **Duration is often the weakest fact.** AWS's public status history describes incidents conservatively and sometimes without precise timestamps. The skill flags duration uncertainty rather than resolving it, and shows tier sensitivity to the uncertainty.
- **SLA definitions are service-specific and adversarially precise.** "Unavailable" in an SLA is a defined term that may not match what an operations team means by the same word. The skill must apply the SLA's definition, quoted, not the colloquial one.
- **Deadlines are the point of the tool but the SLA's language controls.** Claim deadline language varies (for example, by the end of the second billing cycle after the incident month). Quote it exactly and compute the date, but tell the reader to confirm against the current SLA.
- **Not legal advice.** The output describes what published documents say and what arithmetic they imply. The decision to claim, and any dispute about eligibility, belongs to counsel with the full facts.
- **AWS-scoped for v1.** The methodology generalizes to other providers' published SLAs (Azure, GCP, GPU clouds), but the source registry in this skill covers AWS. Extending it is a welcome follow-on contribution.
- **Handling of the output.** When this memo is prepared by or at the direction of counsel, it may constitute attorney work product; store and share it accordingly. The skill does not manage privilege — it flags the consideration and leaves the call to counsel.

## Maintenance and ownership

- **Owner:** Erin Crum (author). Substantive review of the credit-mechanics framework and the conservative "potential eligibility only / not legal advice" posture rests with the owner.
- **Version:** 1.0.0. Material changes — to the delegation threshold, the escalation triggers, or the AWS-scope boundary — are versioned and called out in the PR/changelog so downstream users can see what moved.
- **Review cadence:** re-review at least every six months, and on any of these triggers: AWS restructures its SLA index, changes claim-window language, or adds or removes a per-service SLA. Because the skill fetches SLA text live at run time, it does not go stale on the numbers; this cadence covers the methodology and the source map.

## Testing

Tested against the public AWS status history and current published SLAs for EC2, EBS, S3, Lambda, and RDS, using historical incidents where duration is publicly documented. The extraction methodology (citation-per-value, "not specified" over guessing) follows the same discipline as the author's Compute Terms Observatory (https://github.com/erinecrum/compute-terms-observatory), a public archive of cloud providers' published legal terms, and an SLA event radar the author runs continuously against AWS public feeds. Works in Claude Code and any harness that can fetch public web pages; no OpenClaw-specific tooling.
