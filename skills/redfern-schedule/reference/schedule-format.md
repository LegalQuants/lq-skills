# Schedule format, IDs, status, and merge discipline

The column model and the rules that hold the schedule together across rounds. On the LQ.AI platform these rules are model-applied. There is no code enforcing them, so follow them exactly and tell the user the discipline is applied by the model and worth a quick check each round.

## Columns

The schedule is a Markdown table with these columns, in this order, following the ICSID Redfern Schedule template. Refer to columns by their header name, never by a number: the number of columns and their position can change, but the names and their owners do not.

| Header | Owner | Filled |
|---|---|---|
| No. | requesting | the request ID, immutable |
| Document(s) or Category Requested | requesting | the request text |
| Relevance and Materiality | requesting | the relevance-and-materiality statement, tied to a pleaded issue |
| Objections | producing | the Article 9.2 grounds and basis |
| Reply | requesting | the answer to the objections |
| Tribunal's Decision | tribunal | left blank until the tribunal rules |

This six-column split, with Relevance and Materiality in its own column, is the orthodox ICSID Redfern layout and the default. The tribunal rules line by line, so keep relevance and materiality readable in its own column. For a very compact Markdown view the request text and the relevance-and-materiality text may be combined into the Document(s) or Category Requested column, but say so when you do, and keep the separate column as the default.

## Request IDs

- Assign a stable ID to each request at first draft (R1, R2, R3, and so on).
- In a simultaneous (joint) exchange, where both sides serve requests at once, prefix the ID with the party so the two tracks never collide: the Claimant's requests are C-R1, C-R2, and the Respondent's are R-R1, R-R2. Keep each track ID-stable and consolidate both into one tribunal-facing schedule without renumbering either.
- IDs are immutable. Never renumber. The objection, the reply, the decision, and the eventual production all reference a request by its ID. Renumbering breaks the chain.
- If a request is withdrawn, keep its row and mark its status withdrawn. Do not reuse its ID.
- If a request is split, give the parts new IDs (R4 becomes R4a and R4b) and note the split.

## The table shape is fixed: every row carries every column

The schedule always has the same six columns, in the same order, in every round and for every
role: `No.`, `Document(s) or Category Requested`, `Relevance and Materiality`, `Objections`,
`Reply`, `Tribunal's Decision`.

**Every data row carries a cell for every column, including the columns that are not yours and
the columns nobody has written yet.** A column that has no content yet is an empty cell, not an
absent one: the row still has the same number of separators as the header. Do not shorten a row
by dropping trailing columns, and do not narrow the table to only the columns in play this round.
A row with fewer cells than the header is a malformed table — downstream tooling and the other
side's merge both key on position, and a short row silently loses the columns that follow it.

The schedule is a single document passed between three roles across several rounds. Its shape is
what makes that possible; each round fills one more column of a table whose skeleton never changes.

## Reproduction is a copy, not a re-rendering

Where a column is not yours to write, you reproduce it. Reproduction means the characters
you emit are the characters you were given. It is a copying operation, not a typesetting or
editing one, and the schedule is a joint document served on the other side and the tribunal:
altering their words, even cosmetically, misstates their case.

So, when copying a supplied cell:

- **Emit the same codepoints you were given.** This is the rule that is easiest to break without
  noticing, because the substitutions are ones that look identical on screen. When a supplied cell
  is plain ASCII, your reproduction of it must be plain ASCII: every character in the range
  U+0020 to U+007E and nothing else. In particular, when copying supplied text never emit:
  - `‑` U+2011 NON-BREAKING HYPHEN, `–` U+2013 EN DASH or `—` U+2014 EM DASH in place of `-` U+002D HYPHEN-MINUS;
  - `‘ ’` U+2018/U+2019 or `“ ”` U+201C/U+201D in place of `'` U+0027 and `"` U+0022;
  - ` ` U+00A0 NO-BREAK SPACE or ` ` U+202F NARROW NO-BREAK SPACE in place of U+0020 SPACE;
  - `…` U+2026 in place of three full stops.

  A schedule is compared byte for byte when it is merged back by the other side, so a
  typographically improved copy is a corrupted one. If you find yourself reaching for a
  prettier character while copying, that is the error. Type the plain one.

  **Emit the whole schedule inside a fenced code block** — three backticks on the line before the
  table and three on the line after it. The schedule is data in transit between three parties
  across several rounds, not prose being presented to a reader, and a fence is how you say so.
  Treat everything between the fences as literal: no substituted characters, no smart quotes, no
  typographic dashes or spaces, no re-wrapping. The table's pipes and header separator are
  unchanged inside the fence, so it still reads and still merges.
- Do not abbreviate. "Statement of Claim paragraphs 70 to 78" does not become "SoC 70-78";
  "1 January 2022" does not become "1 Jan 2022". Expansions and contractions are both changes.
- Do not tidy, shorten, re-order or correct. If a supplied cell contains an apparent error —
  a wrong paragraph reference, an inconsistent date — reproduce it exactly as given and note
  the discrepancy separately, in your own column or in the memo. Silently fixing another
  party's text is the more serious error, because it is invisible to them.
- Do not re-wrap or re-punctuate to fit your layout.

If a cell cannot be reproduced in full — it is too long, it is missing, it did not come
through cleanly — stop and ask the user for it. Never summarise it and never reconstruct it
from memory.

## Column ownership

- A role writes only its own columns, named here, never another role's.
  - The **requesting party** writes *No.*, *Document(s) or Category Requested*, *Relevance and Materiality*, and *Reply*.
  - The **producing party** writes *Objections*.
  - The **tribunal** writes *Tribunal's Decision*.
- Every column the current role does not own is reproduced verbatim from the input. Never edit another party's text. If their text contains an apparent error, note it in your own column or the memo, and leave their column as written.
- The *Tribunal's Decision* column stays blank until the tribunal rules. Party text must never appear in it.

## Status vocabulary

Track each request's lifecycle, shown in a small status note beside the row or in a status column when the user wants one:

`requested` to `objected` to `replied` to `granted`, `denied`, `granted-in-part`, then `produced` or `withdrawn`.

## Merge discipline

When merging a returned schedule into the working file:

- Match rows by request ID, not by position.
- Reproduce the other side's column verbatim into the working file.
- If an ID in the returned file does not match a row in the working file, stop and report the mismatch. Do not drop the row, invent a match, or reorder.
- Keep row order stable across rounds. One request keeps one row.
- After a merge, confirm back to the user: the count of rows, the IDs touched, and any mismatch found.

## Deadlines and the production timetable

Document production runs on a timetable, usually fixed in Procedural Order No. 1 or a later procedural order: a date for requests, a date for objections, a date for replies, a date for the tribunal's decision, and a date for production. These dates are optional input. When the user supplies them, record them in the version or calibration note at the top of the output, and flag any step that is out of time (for example, a request served after the request deadline, or an objection past the objection date). When they are absent, proceed without them and say the run is not calibrated to a timetable. Under the Prague Rules the relevant marker is the case-management conference rather than a request deadline (see `regimes.md`).

## Version note

Each exchange is a new version. State the round and version at the top of the output (for example, "Requesting party, first draft, round 1" or "Producing party objections, round 2, merged onto the requesting draft"). This is how a reader knows which columns are new and which are carried over.
