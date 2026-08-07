---
name: redfern-schedule
description: "Use whenever the user is working on document production in international arbitration: drafting requests to produce, raising or replying to objections, or preparing the schedule for the tribunal to rule on. Builds and maintains the request-to-produce table (the Redfern Schedule) for the requesting party, the producing party, or the tribunal. Applies the IBA Rules (2020) Article 3.3 admissibility checklist and the Article 9.2 objection grounds, raises a content-based political and institutional sensitivity prompt for State or state-owned parties, and writes an internal memo flagging the user's own weak requests. Trigger it even when the user does not say Redfern Schedule but mentions requests to produce, document production in an arbitration, IBA objections, Article 3.3 or 9.2, or a tribunal ruling on production. It enforces form and does not decide materiality or whether an objection will succeed."
author: Alexios vdSK
jurisdiction: MULTI
tags: [arbitration, document-production, redfern, iba-rules, procedure]
version: 1.5.0
last_reviewed: 2026-08
last_reviewed_by: Alexios vdSK, Member, LegalQuants
last_verified: 2026-06-20
freshness_window: 12 months
freshness_category: procedural
verified_against:
  - https://www.ibanet.org/MediaHandler?id=def0807b-9fec-43ef-b624-f2cb2af7cf7b
  - https://praguerules.com/upload/medialibrary/9dc/9dc31ba7799e26473d92961d926948c9.pdf
  - https://iccwbo.org/dispute-resolution/dispute-resolution-services/arbitration/rules-procedure/2026-arbitration-rules/
  - https://www.lcia.org/Dispute_Resolution_Services/lcia-arbitration-rules-2020.aspx
  - https://icsid.worldbank.org/rules-regulations/convention/arbitration-rules/chapter-v-evidence
  - https://www.ciarb.org/media/bpndtcgu/guideline-on-the-use-of-ai-in-arbitration_updated-sept-2025.pdf
---

> **YOU ARE ABOUT TO DO HIGHLY PRIVILEGED WORK. PLEASE CHECK THE RULES OF YOUR JURISDICTION, AS YOU MAY NEED TO SWITCH TO A LOCAL MODEL. BEFORE YOU PROCEED, CONFIRM THAT YOU ARE FINE WITH PROCEEDING.**
>
> A Redfern Schedule carries the live substance of a dispute and is usually privileged and confidential. Assume local or on-premises execution. Do not send live schedule content to a cloud endpoint without the seat's rules, the parties' agreement, and the client's consent, and a check against the CIArb Guideline on the Use of AI in Arbitration (2025) and the applicable bar and ethics rules. This warning is enforced as the first step of the workflow below.

# Redfern Schedule

Build and maintain the Redfern Schedule that organises requests to produce documents in international arbitration. The skill serves three roles from one artefact: the requesting party (who drafts the requests and the relevance-and-materiality case), the producing party (who states objections), and the tribunal (who rules). It applies the IBA Rules on the Taking of Evidence (2020) admissibility form and grounds for objection, holds version discipline across rounds, and tells the user where their own requests are weak. It enforces form. The legal calls stay with counsel.

## Audience and design

- **Audience.** Arbitration counsel and the lawyers supervising them, acting in one of three roles (requesting party, producing party, tribunal). It assumes legal training and hands every substantive judgment back to the lawyer.
- **Work shape.** Bounded and transactional. The scope is constrained, the tests are explicit, and the skill surfaces deviations and frames the decision rather than choosing for the user. Speed matters, but never at the cost of an escalation trigger.
- **How it handles confidence.** A request that clearly passes or clearly fails the Article 3.3 gates is recorded as such with the reason. A borderline request is not silently resolved. It is named in the internal flags memo with the gate it strains, and the user decides whether to fix, narrow, or drop it. The skill surfaces uncertainty, it does not perform certainty.

## When this skill applies

Apply when the user is working on document production in an arbitration and wants to:

- Draft requests to produce and run them against the IBA Article 3.3 admissibility checklist.
- Respond to the other side's requests by mapping objections to the Article 9.2 grounds.
- Reply to objections already entered against the user's requests.
- Prepare a clean, decision-ready schedule for the tribunal.
- Merge a returned schedule from the other side into the working file without losing column discipline.

## When this skill does not apply

Do not apply when:

- The user wants advice on whether a specific objection will win or whether a document is truly material. The skill enforces form and flags weakness. It does not predict outcomes. Say so and stop.
- The matter is litigation under court disclosure rules (for example English CPR or US discovery) rather than arbitration. The admissibility tests here are the IBA arbitration tests. Note the mismatch and stop.
- The user wants a full document review or extraction over a corpus of files. That is a different skill.
- The request is to draft the underlying documents or the pleadings themselves.

When declining, route the user plainly to what they actually need.

## Inputs

The skill runs conversationally through the intake interview below. It needs, at minimum, either a request list (requesting role) or a returned schedule (producing, reply, tribunal, or merge round). The optional inputs in the frontmatter change the substance of the run, not just its presentation:

- **role** decides the pipeline and which column the skill is allowed to write.
- **regime** changes the request unit and the posture. Prague 2018 discourages production and uses a single-document unit with a public-domain filter. ICC, LCIA, and ICSID borrow the IBA tests. See `reference/regimes.md`.
- **issues** lets the skill tie each request to a pleaded issue. Without it, relevance ties are marked unverified and the user is told that the relevance case is weaker as a result.
- **parties** marked as State or state-owned arm the content-based Article 9.2(f) sensitivity prompt: it is raised where a document's content implicates a governmental or sovereign function, not on every request because of who owns a party.

If an optional input is absent, proceed on the default and state the default in the output so the user knows the run was not calibrated to that input.

## Workflow

### Step 0. Privilege gate, then intake interview

This step runs first, every time, before any ingestion or drafting.

**0a. Privilege gate (hard stop).** Reproduce the capitalised warning at the top of this file. Then name the concrete checks the user should make now: the seat of the arbitration, the institutional rules, the parties' national laws, the applicable bar and ethics rules, and the CIArb 2025 Guideline (sections 2.2 on confidentiality, 6.7 on which rules govern, and 7 on disclosure). Do not read any schedule content, ingest any attachment, or draft anything until the user gives an explicit affirmative that they are fine to proceed. If the user does not confirm, stop.

**The gate has two states, and you must resolve which one you are in before doing anything else.**

- *Not yet confirmed.* No affirmative has been given anywhere in the conversation, including the message you are reading. Print the banner and the checks, and stop. Produce no schedule, no memo, and no analysis.
- *Confirmed.* An affirmative appears anywhere in the conversation, including in the same message that carries the work. Wording varies: "I confirm", "I am fine to proceed", "go ahead", "confirmed", "proceed". Treat any such affirmative as satisfying the gate. Print the banner, then **carry straight on and do the work in the same reply**. Do not ask again.

Once the gate is confirmed it stays confirmed for the rest of the conversation. Re-issuing the banner as a question after the user has already confirmed is a defect: it stalls the user's work and, when it is a response to a challenge or a correction, it reads as evasion. Re-open the gate only if the engagement itself materially changes, for example a different matter or a different party.

**The banner is printed every time, before the first artefact of the reply, in both states.** It is the standing confidentiality warning, not a question that has been answered and can then be dropped. Reproduce it word for word; do not paraphrase, summarise or replace it with a reference to it.

**0b. Intake interview.** After confirmation, ask only for what you do not already have, one question at a time, in this order. Skip any item the user already supplied. See `reference/intake.md`.
1. Role: requesting, producing, or tribunal.
2. Regime: IBA 2020 (default), Prague 2018, ICC, LCIA, or ICSID.
3. Round: first draft, objections, reply, decision, merge, or simultaneous (joint) exchange.
4. Is any party a State or a state-owned entity. If yes, record which, to arm the content-based 9.2(f) sensitivity prompt.
5. Is there a pleaded-issues list to tie relevance to.
6. Where the requests or the returned schedule are.
7. Optional: are there production deadlines (Procedural Order No. 1 or a procedural order) to record and check.

### Step 0c. Establish the predicates before you reach for any ground

An objection is a conclusion. Every ground in Article 9.2, and every gate in Article 3.3, is a
function of *facts about the document*: who holds it, who wrote it, what shape the category is,
what the content is, and whether the request was made in time. If you choose a ground before you
have established those facts, you are pattern-matching the wording of the request rather than
analysing it, and you will reach for whichever ground is most available rather than the one that
fits.

So, for **each request**, and before writing anything in the *Objections* column, record these five
predicates in your internal working notes:

- **Holder.** Requesting party · the user's own side · a non-party · the user's contract administrator, agent or affiliate · jointly held.
- **Author class.** Counsel · internal staff · an engineer, consultant or other professional adviser who is not counsel · a governmental or regulatory body · a third party.
- **Category shape.** An identified document · a narrow and specific category bounded on stated axes · an open-ended class.
- **Content class.** Ordinary commercial · legal advice · settlement or without-prejudice · third-party confidential or trade secret · governmental, regulatory or sovereign · personal or private.
- **Timeliness and existence.** Within the procedural timetable · out of time · the document does not exist or is no longer held, and why.

Take each predicate from what the request and the user's own material actually say. Where the
material does not tell you, record `not established` and say so in the objection rather than
assuming a value that would support a ground you would like to run.

The predicates then decide the ground; `reference/iba-9-2-objections.md` sets out the mapping.
Where the predicates support no ground, the correct output is no objection.

### Step 1. Load the right references for the regime and role

Read `reference/schedule-format.md` for the column model, the ID rules, the status vocabulary, the deadlines block, and the merge and column-ownership rules. Read `reference/regimes.md` and apply the selected regime (IBA 2020, Prague 2018, ICC, LCIA, or ICSID). For the requesting role read `reference/iba-3-3-checklist.md`. For the producing role read `reference/iba-9-2-objections.md`. If an issues list was provided, read `reference/issue-matching.md`.

### Step 2. Run the role pipeline

Refer to columns by name throughout, never by number. The requesting party owns *No.*, *Document(s) or Category Requested*, *Relevance and Materiality*, and *Reply*. The producing party owns *Objections*. The tribunal owns *Tribunal's Decision*. Every column a role does not own is reproduced verbatim. See `reference/schedule-format.md`.

**Requesting.** Ingest the requests. Assign each a stable ID. Run the Article 3.3 pre-flight per `reference/iba-3-3-checklist.md` and record a pass or fail with a reason for each gate. Tie each request to a pleaded issue using `reference/issue-matching.md` where the issues list is present, otherwise mark the tie unverified. Write the *No.*, *Document(s) or Category Requested*, and *Relevance and Materiality* columns. Produce the schedule and the internal flags memo.

**Producing.** Reproduce the requesting party's columns verbatim. For each request, establish the Step 0c predicates first, then derive the ground by working the selection order in `reference/iba-9-2-objections.md`. Do not choose a ground before the predicates are recorded. Where a request is met by confidentiality, privilege, or sensitivity, pair the objection with the Article 9.5 protective-measure option (redaction or a confidentiality ring) rather than a flat refusal, and where only the tribunal need see a document, invite the tribunal to order in-camera review rather than offering it as a party measure. If any party is marked State or state-owned, surface the 9.2(f) sensitivity prompt as a candidate only where the document's content implicates a governmental or sovereign function, not on every request, and not on a request already disposed of on relevance or burden. Write the *Objections* column. Also produce the producing party's internal flags memo naming its own weak or non-colourable objections.

**Reply (requesting, later round).** Reproduce the prior columns verbatim. Answer each objection in the *Reply* column, point by point. Narrow a request where that saves it, and say so. Write the *Reply* column.

**Tribunal.** Reproduce every party column verbatim, byte for byte, with no abridging or paraphrasing. Keep the *Tribunal's Decision* column empty. Do not propose a decision. If the user wants a private aid, offer a separate worksheet that lists, per request, the objection grounds in play and the protective-measure options, with no recommendation.

**Merge.** Match the returned schedule to the working file by request ID. Reproduce the other side's column verbatim. Report any ID that does not line up rather than dropping or reordering a row.

**Simultaneous (joint exchange).** Where both sides serve requests at once, run the requesting pipeline for each side's request set, prefix the IDs by party (C-R1, R-R1) so the two tracks never collide, and consolidate both into one schedule without renumbering either. See the ID rules in `reference/schedule-format.md`.

### Step 3. Produce the output

Produce the schedule as a Markdown table with the columns in `reference/schedule-format.md`. Then produce the internal flags memo: for the requesting and reply roles it names the user's own weak requests under Article 3.3, and for the producing role it names the user's own weak or non-colourable objections. Close with the calibration note (which regime, which role, whether the issues list was present, any timetable recorded) and the standing reminder that drafting quality and the merits of any objection are for counsel.

## Output

Two artefacts, both Markdown.

1. **The schedule**, a Markdown table emitted inside a fenced code block (```) with these six columns, always all six, always in this order: `No.`, `Document(s) or Category Requested`, `Relevance and Materiality`, `Objections`, `Reply`, `Tribunal's Decision`. Only the columns owned by the current role carry new text. Every other column is reproduced verbatim or left blank. The tribunal's column is blank until the tribunal rules. **A blank column is an empty cell, not a missing one** — every data row has the same number of cells as the header, so a row that has nothing to say in the last two columns still ends with the separators that hold their places. Never drop trailing columns to shorten a row, and never emit a narrower table containing only the columns in play this round.

2. **The internal flags memo** (requesting, reply, and producing roles), the user's own weak points named honestly. For the requesting and reply roles it lists requests that are weak under Article 3.3, each with the gate it fails and a one-line reason. For the producing role it lists the user's own weak or non-colourable objections (for example ground (f) on a plainly commercial document, a bare burden assertion, or a blanket privilege claim without 9.4 grounding). This memo is for the user's side only. It is never part of the schedule sent to the other side or the tribunal. Mark it clearly as internal and privileged work product.

Lead the output with a one-line statement of what was produced and for which role. Do not pad.

**The memo lists failures, not anticipations.** A request or an objection belongs in the memo when
it *fails* a test you have applied: a request that fails an Article 3.3 gate, an objection you
assess as weak or non-colourable. It does not belong there merely because something about it is
worth being ready for. An objection the other side may raise, a document that may attract a
sensitivity ground, a passage that may need redacting later — those are matters for the calibration
note or for the column itself, not entries in a memo whose stated purpose is the user's own weak
points. A memo that names every request tells the user nothing, and a request listed without a
failed test reads to the user as a defect that is not there. If you cannot name the test it fails,
it does not go in.

Note also which side's possession matters. On the requesting side, Gate C asks whether the
*requesting party* already holds the document; the possibility that some non-party may also hold a
copy is not a weakness in the request, and where a non-party is the likely holder the request is
routed under Article 3.9 rather than flagged as defective.

**The memo and the schedule must agree.** The memo names residual risk on objections you are
actually running. It is not a confession about objections you should not have run. If, while writing
the memo, you find yourself describing an objection as weak, tenuous, non-colourable, or unlikely to
survive, that objection does not belong in the schedule: take it out of the schedule first, then
write the memo. An output whose memo contradicts its own table has already told the reader which
half to believe.

**Do not supply facts the user has not.** Never state a quantity, volume, document count, custodian
count, cost, duration or percentage that the user's material does not contain. A burden objection
needs specifics, and where you do not have them the honest output is the objection framed on the
shape of the request plus an explicit `[quantification required from client]`. An invented figure is
worse than a missing one: it cannot be supported when the other side asks for the search log behind
it, and it puts the signing lawyer behind a statement they cannot stand up. The same rule covers
pleading references, dates and document titles — if the user's material and yours disagree, or a
cited paragraph does not exist, say so and ask, rather than reconciling it silently.

**Documents supplied in context are the user's documents.** Where the material arrives inside the
conversation rather than as a file you open yourself — in a pasted block, or under a heading such as
`## Attached documents for this turn` — that is the attachment, and you can read it. Work from it.
Do not tell the user you are unable to read attachments while their document is in front of you, and
do not reconstruct from memory what you can read directly. If a document genuinely is not present,
say which one and ask for it.

## Edge cases and refusals

- **No confirmation at the gate.** Stop. Produce nothing.
- **Regime is Prague.** The request unit is a single specific document, not a category. Apply the three Prague gates and show the production-discouraged note. See `reference/regimes.md`.
- **No issues list.** Proceed, but mark every relevance tie unverified and tell the user the relevance case is weaker without the pleaded issues.
- **A request is plainly the user already holding the document.** Flag it under Gate C. Do not silently fix it.
- **The other side's text contains an apparent error.** Reproduce it verbatim in their column. Note the apparent error in your own column or the memo. Do not edit their column.
- **Non-English schedule.** Confirm with the user whether to work in the document's language. The admissibility tests are language-neutral, but the drafting register is not validated for non-English output.
- **A party asserts blanket state secrecy.** Record it as a 9.2(f) objection and note that the tribunal decides whether the sensitivity is compelling and that a State must still search and justify each document. Do not treat it as a veto.
- **The documents are in a non-party's possession.** The ordinary producing-party objection menu does not fit, because the other party cannot produce what it does not hold. Flag the request for the Article 3.9 route (the requesting party asks the tribunal to take steps to obtain the documents from the non-party). See `reference/iba-3-3-checklist.md`, Gate C.
- **A timetable is supplied.** Record the production deadlines in the calibration note and flag any out-of-time step (a request after the request date, an objection past the objection date). Under Prague the marker is the case-management conference rather than a request deadline.
- **Simultaneous (joint) exchange.** Both sides serve requests at once. Run the requesting pipeline per side, prefix IDs by party (C-R1, R-R1), and consolidate without renumbering. Do not blend the two request sets into one numbering.

## What this skill does not do

- It does not decide whether a document is material or whether an objection will succeed. Those are the tribunal's calls and counsel's judgment.
- It does not give enforceability or privilege opinions. It records the asserted basis and frames the ground.
- It does not generate a Word `.docx` or an Excel `.xlsx` file. On the LQ.AI platform the output is the Markdown table shown in chat. File generation needs an agent runtime or a later platform release.
- It does not invent facts, issues, or citations that are not in the user's inputs or the reference files.
- It does not substitute for review by qualified arbitration counsel.

## Reference materials

- `reference/iba-3-3-checklist.md`: the Article 3.3 pre-flight, gate by gate, with pass and fail signals.
- `reference/iba-9-2-objections.md`: the Article 9.2 grounds, the content-based state-party (f) sensitivity prompt, and the 9.5 protective measures.
- `reference/regimes.md`: IBA 2020 default and the Prague, ICC, and LCIA variants.
- `reference/schedule-format.md`: the column model, ID rules, status vocabulary, and the merge and column-ownership rules.
- `reference/intake.md`: the privilege-gate banner and the ordered intake questions.
- `reference/issue-matching.md`: the separable relevance matcher (also reused by a later cross-examination skill).
- `reference/CITATIONS.md`: the provenance ledger. Every legal citation in this skill checked against its official source, with URLs, verdicts, and the verification date.
- `examples/example_requesting.md`, `examples/example_producing.md`, `examples/example_tribunal.md`: worked examples on one shared fact pattern.
