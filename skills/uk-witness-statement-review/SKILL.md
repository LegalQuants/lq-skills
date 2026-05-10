---
name: uk-witness-statement-review
description: Use when users say "review this witness statement", "check this statement before service", "PD 57AC", "statement of truth", "hearsay in this witness evidence", or need England and Wales witness evidence checked for source support, CPR/PD issues, exhibits, chronology conflicts, or argument.
author: AnonLQ
jurisdiction: England and Wales
tags: [litigation, witness-statements, cpr, evidence, england-and-wales, drafting]
---

# uk-witness-statement-review

## When to Use

- A user has a draft witness statement for England and Wales civil proceedings.
- The statement needs checking against documents, chronology, pleadings, or disclosure.
- The user wants issues flagged before signing, service, exchange, or filing.
- The draft may contain argument, speculation, hearsay, unsupported recollection, or inconsistent dates.

This skill is a review workflow. It does not certify truth, settle admissibility, or replace solicitor/counsel sign-off.

## Access Modes

This skill works in three modes:

1. **Live source mode** - use browser, web search, MCP, API, or other configured access to retrieve public rules, orders, filings, or source documents.
2. **User-supplied source mode** - use the draft statement plus uploaded or pasted exhibits, pleadings, correspondence, chronology, disclosure, prior statements, rules, or orders supplied by the user.
3. **No-source mode** - review the statement's internal drafting issues and produce a source-request checklist, but do not mark factual assertions as supported.

If exhibits, documents, rules, or orders cannot be retrieved or supplied, mark the relevant check `source_missing` or `verify_current_rule`. Do not verify facts or procedural compliance from model memory.

## How It Works

### 1. Confirm context

Identify:

- Court or tribunal, claim type, and procedural stage.
- Witness role: party, employee, expert-adjacent fact witness, third party, or litigant in person.
- Purpose: interim application, trial, summary judgment, costs, or pre-action evidence.
- Governing directions, page limits, exhibit rules, or court-specific order.
- Source set: pleadings, chronology, exhibits, correspondence, disclosure, and prior statements.

If the governing order or forum is unknown, flag CPR/PD points as `verify_current_rule`.

If the forum is a tribunal or specialist court not governed by the CPR witness statement regime, identify the applicable procedural rules and mark CPR/PD checks as `not_applicable_or_verify`.

### 2. Build a statement map

For each paragraph, classify:

- `first-hand fact`
- `hearsay or reported fact`
- `belief or inference`
- `argument or submission`
- `legal conclusion`
- `procedural background`
- `exhibit reference`
- `needs_source`

Keep paragraph numbers stable. The output should let a drafter jump straight to the problem paragraph.

### 3. Check source support

For each factual assertion:

- Tie it to a source document, exhibit, correspondence item, chronology entry, or witness knowledge basis.
- Quote or pinpoint the supporting material.
- Mark unsupported assertions as `needs_source`.
- Mark document conflicts as `source_conflict`.
- Preserve uncertainty: a witness can say what they recall, but the review must show where documents differ.

### 4. Check drafting and compliance risks

Flag:

- Argument dressed as evidence.
- Legal submissions or conclusions better left to skeleton argument.
- Speculation about another person's state of mind.
- Hearsay that needs a clear source or notice analysis.
- Collective phrases such as "we knew" without identifying who knew what.
- Dates, amounts, names, and defined terms inconsistent with documents or pleadings.
- Missing or vague exhibit references.
- Overlong narrative, irrelevant background, or duplicated chronology.
- PD 57AC trial witness statement requirements, certificate of compliance, and confirmation of compliance where applicable; otherwise mark `not_applicable_or_verify`.
- Statement of truth, signature, date, interpreter, translation, or exhibit formatting issues where applicable.

Do not invent procedural requirements from memory. If current CPR/PD wording matters, retrieve it or mark `verify_current_rule`.

### 5. Produce a review report

Recommended output:

| Paragraph | Issue | Severity | Source / Pinpoint | Rule / Source Checked | Suggested Fix |
|---|---|---|---|---|

Severity values:

- `critical` - likely service/signing/accuracy problem.
- `major` - material evidential or drafting risk.
- `minor` - clarity, formatting, or housekeeping issue.
- `verify` - rule or source needs checking.

Then include:

- Key inconsistencies with documents.
- Unsupported factual assertions.
- Argument/legal-conclusion paragraphs.
- Exhibit and statement-of-truth checklist.
- Questions for the witness or solicitor.

## Example

```text
Review this draft witness statement against the documents and chronology. Flag unsupported paragraphs, argument, hearsay, date conflicts, and CPR/PD compliance issues. Do not rewrite the statement unless I ask.
```

For a compact output pattern, see `examples/output.md`.
For paragraph classifications and witness-evidence review axes, see `references/witness-review-playbook.md`.

## Limitations

- The witness, not the agent, owns the truth of the evidence.
- Current CPR, Practice Direction, court order, and tribunal rules must be checked where compliance matters.
- Privileged comments and drafts require an approved processing environment.
- This skill flags evidential risk; it does not make final admissibility rulings.
