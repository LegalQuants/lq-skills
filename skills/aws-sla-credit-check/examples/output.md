# Worked example — AWS SLA credit check

**Input prompt:**
> "AWS had the us-east-1 event on May 7–8 affecting EC2 (and reportedly EBS). Check whether we might be owed SLA credits and what the deadline is."

**Run date:** 2026-07-15. All SLA values and incident facts were fetched fresh on this date; because AWS revises SLAs and the Health Dashboard is a live source, re-running later may produce different values.

---

# Action-Item Memo — Potential AWS SLA Credit (us-east-1 EC2, May 7–8 2026)

**Status: POTENTIAL eligibility only — conditional on your usage. Not legal advice.**

## 1. Incident summary (sourced)

Read directly from the AWS Health Dashboard **Service history** tab (https://health.aws.amazon.com/health/status, viewed 2026-07-15):

| Fact | Value | Source |
|---|---|---|
| AWS event label | Amazon Elastic Compute Cloud — **"Increased Error Rate and Latency"** | Health Dashboard Service history |
| Region | us-east-1 | Health Dashboard Service history |
| Start time | **May 7, 2026, 5:25:26 PM PDT** | Health Dashboard Service history |
| Last update time | **May 8, 2026, 8:04:07 PM PDT** | Health Dashboard Service history |
| Event envelope | ≈ **26.6 hours** (start → last update) | computed from the two timestamps above |
| Availability Zone / cause | Single AZ **`use1-az4`**; cooling/thermal failure caused power loss to EC2 instances and EBS volumes; cooling restored ~1:50 PM PDT May 8 | Network World (secondary reporting), fetched 2026-07-15 |

**⚠️ Two facts to pin down before relying on this.**
1. **The 26.6-hour figure is the event *envelope*, not confirmed continuous unavailability.** AWS labeled this "Increased Error Rate and Latency," which is softer than the SLA's defined term "Unavailable." How much of the window your resources actually had *no external connectivity* (EC2) or *zero read/write IO* (EBS) must be measured from your own CloudWatch data.
2. **EBS is not a separate line in the Health Dashboard history for this event** — the history entry is filed under EC2. EBS impact comes from secondary reporting. Confirm any EBS impact against your own monitoring before claiming under the EBS SLA.

## 2. Credit mechanics (fetched 2026-07-15)

**Amazon EC2 SLA** — https://aws.amazon.com/compute/sla/ · **Amazon EBS SLA** — https://aws.amazon.com/ebs/sla/

| SLA / commitment | Monthly Uptime threshold | Credit tiers | Defined "Unavailable" |
|---|---|---|---|
| EC2 Region-Level (multi-AZ) | 99.99% | <99.99%→10% · <99.0%→30% · <95.0%→100% | all instances across multiple AZs "concurrently have no external connectivity" |
| EC2 Instance-Level | 99.5% | <99.5%→10% · <99.0%→30% · <95.0%→100% | "your Single EC2 Instance has no external connectivity" |
| EBS Region-Level (multi-AZ) | 99.99% | <99.99%→10% · <99.0%→30% · <95.0%→100% | all attached volumes across 2+ AZs "perform zero read write IO, with pending IO in the queue" |
| EBS Volume-Level | 99.9% | <99.9%→10% · <99.0%→30% · <95.0%→100% | a "Single EBS Volume performs zero read write IO, with pending IO in the queue" |

**Architectural precondition (decisive here):** this was a **single-AZ** event (`use1-az4`). The Region-Level commitments require *concurrent multi-AZ* failure, so they **do not apply**. The commitments to test are **EC2 Instance-Level (99.5%)** and, if EBS impact is confirmed, **EBS Volume-Level (99.9%)**.

**Claim deadline language (both SLAs, verbatim):** *"must be received by us by the end of the second billing cycle after which the incident occurred."*
**Exclusions (both):** factors outside AWS's reasonable control, customer actions/inactions, customer equipment/software, or AWS suspension rights.

## 3. Potential eligibility (May 2026 = 31 days = 44,640 minutes)

*Qualifying-downtime % = qualifying downtime minutes ÷ 44,640.* Because the qualifying portion of the 26.6-hour envelope is not established from public data, this is the **tier ladder** to place your verified downtime against:

| Verified qualifying downtime | EC2 Instance-Level (99.5%) | EBS Volume-Level (99.9%) |
|---|---|---|
| ≤ 44.6 min | no credit | no credit |
| 44.6 min – 223 min | no credit | **10%** |
| 223 min – 446 min (≈3.7–7.4 hrs) | **10%** | **10%** |
| 446 min – 2,232 min (≈7.4–37.2 hrs) | **30%** | **30%** |
| > 2,232 min (> 37.2 hrs) | **100%** | **100%** |

*Arithmetic:* threshold minutes = (1 − uptime%) × 44,640. E.g. EC2 Instance-Level 99.5% → 0.005 × 44,640 = 223.2 min; 99.0% → 446.4 min; 95.0% → 2,232 min.

> **Conditional:** IF your EC2 instances in `use1-az4` had no external connectivity (or your EBS volumes did zero IO with pending IO) for a verified duration, the published tiers indicate the credit above, as a percentage of your May 2026 monthly charges for that service in us-east-1. For reference, if the *entire* 26.6-hour envelope (≈1,599 min) qualified, both commitments would land in the **30% tier** — but the "Increased Error Rate and Latency" label means the qualifying portion is likely less, so do not assume the full envelope.

## 4. ⏰ Claim deadline

Incident month = **May 2026**. "End of the second billing cycle after" → **July 31, 2026** (AWS billing cycle = calendar month: June is the first cycle after, July the second). **As of the 2026-07-15 run date, that is ~2 weeks away.** Confirm the interpretation against the live SLA before relying on it.

## 5. Next steps (who verifies what)

1. **Cloud platform / FinOps** — from CloudWatch, measure the actual per-resource windows in `use1-az4` on May 7–8 where EC2 instances had no external connectivity and/or EBS volumes did zero IO. This produces the *qualifying* downtime, which is what Section 3 needs (not the 26.6-hour envelope).
2. **Cloud platform** — confirm affected resources were in `use1-az4` (Region-Level does not apply to a single-AZ event) and whether any EBS volumes were actually impacted.
3. **FinOps** — pull **May 2026** EC2 (and, if applicable, EBS) charges for us-east-1 — the credit base.
4. **Legal** — confirm no enterprise agreement supersedes the published SLA, and that the deadline wording above still matches the live SLA.
5. **File** the AWS Support case before **July 31, 2026** with affected resource IDs, the verified downtime window, and the specific SLA section relied on.

## 6. Contrast — a more recent event that likely does NOT qualify

The **most recent** us-east-1 event in the Service history is **July 6, 2026 — EC2 "Increased Launch Template API Error Rates"** (5:45–7:53 AM PDT, ~2 hrs). This is elevated errors on a single EC2 *API*, not a loss of connectivity to running instances, so it almost certainly does **not** meet the EC2 SLA's "Unavailable" definition. Recency does not equal claimability — the defined term controls.

## 7. Disclaimer

This memo reads published AWS documents and the public Health Dashboard only, as of the fetch dates shown, and computes what their arithmetic implies. It is **not legal advice** and does **not** assert any credit is owed. Actual eligibility depends on your usage, architecture, and any negotiated agreement that may modify or replace the published SLA. Verify every value against current source documents before filing.
