---
name: euipo-homoglyph-screening
description: Use when a user needs to detect homoglyph / look-alike trademark conflicts that a standard register search misses — marks that look (and often sound) identical to a human but are a different character string to a machine (e.g. Cyrillic "А" for Latin "A", "0" for "O", case tricks). Generates the set of confusable variants of a mark using the Unicode confusables standard, searches the EUTM register for each via a configured EUIPO connector, and assesses any hits under Art. 8(1)(b) (visual + phonetic confusion), bad faith, and Art. 8(5) (reputation / unfair advantage). Two modes: a defensive watch over an owned mark, and a clearance blind-spot check before filing. Outputs a draft conflict report with a recommended action for attorney review. Requires a configured EUIPO connector.
author: Jatocao
jurisdiction: EU
tags: [trademark, euipo, homoglyph, look-alike, knowledge-security, clearance, watch, ip, eu-trademark, unicode]
version: 1.0.0
last_reviewed: 2026-06
lq_ai:
  title: EUIPO Homoglyph / Look-alike Screening
  version: 1.0.0
  author: Jatocao
  tags: [trademark, euipo, homoglyph, look-alike, knowledge-security]
  jurisdiction: EU
  trigger_examples:
    - "Check if anyone has registered a look-alike of our trademark"
    - "Is there a Cyrillic or zero-for-O copy of this brand on the register?"
    - "Run a homoglyph check before we file"
    - "Find confusable variants of this mark in the EUTM register"
    - "Has someone squatted a homoglyph version of our brand?"
  inputs:
    required:
      - name: mark_name
        type: text
        description: The trademark to screen (an owned mark in watch mode, or a proposed mark in clearance mode)
    optional:
      - name: mode
        type: text
        description: "watch (find look-alikes of an owned mark) or clearance (find earlier confusable marks before filing). If omitted, the skill asks."
      - name: nice_classes
        type: text
        description: Nice classes to scope the search (recommended — narrows noise)
      - name: reputed
        type: text
        description: "yes/no — whether the owned mark has a reputation (changes the legal angle to Art. 8(5))"
  output_format: markdown
  self_improvement: false
---

# EUIPO Homoglyph / Look-alike Screening

This skill detects **homoglyph and look-alike** trademark conflicts — marks that are visually (and usually phonetically) identical to a human but are a **different character string** to a machine, so a normal exact/fuzzy register search does not surface them. It generates the confusable variants of a mark, searches the EUTM register for each via a configured EUIPO connector, and assesses any hits under EU trademark law.

It is a **knowledge-security** tool for brands: it closes the gap between *what a human sees* and *what a database matches on* — the same divergence that drives IDN homograph attacks and brand squatting.

Coverage and freshness of the search depend entirely on the connector configured by the user. All outputs are a first-line draft for attorney review — not a legal opinion, an enforcement decision, or advice to act.

> **Scope and Legal Use**
> This skill processes information that may relate to client matters and pending enforcement decisions. Treat all outputs as privileged work product unless the supervising attorney has decided otherwise. The conflict report is a draft for qualified-counsel review — it does not constitute a legal opinion or an enforcement recommendation. The decision to oppose, seek a declaration of invalidity, send a demand, or take no action is for a named responsible attorney.

---

## How this skill behaves

**Work shape — bounded transactional / pattern-matched review.** Screening for a known attack pattern (character-swap look-alikes) is a constrained-scope task with clear gates: variants are generated from a defined confusable set, searched, and any hit is confirmed and assessed against fixed legal grounds. The skill escalates anything outside the pattern (non-searchable characters, domain/online-only use, the enforcement decision) to counsel.

**Confidence bands.** The skill operationalises three levels and behaves accordingly:
- **High** — a register hit that is a clear single-character cross-script or digit-for-letter swap of the screened mark on identical/similar goods: report as a strong look-alike signal.
- **Medium** — a partial or multi-change divergence, or a hit on more distant goods: report with the specific divergence and let counsel weigh it.
- **Low / discard** — a coincidental match that is not genuinely confusable: note why it was excluded rather than padding the report.

---

## When this skill applies

- **Watch / defensive** — periodically check whether a third party has registered a homoglyph or look-alike version of a client's mark (squatting, free-riding, counterfeiting set-up).
- **Clearance blind-spot** — before filing, surface earlier confusable marks that a standard clearance would miss because they are a different string.

This skill complements, it does not replace, a standard clearance (`euipo-trademark-clearance`): a normal search catches similar *strings*; this one catches strings that are *different but look the same*.

---

## The legal angle (how a look-alike is attacked)

A homoglyph/look-alike mark is typically challenged on one or more of three grounds. The skill assesses each hit against all three:

1. **Likelihood of confusion — Art. 8(1)(b) EUTMR.** This is the primary route. A homoglyph is, by construction, **visually near-identical** and very often **phonetically identical** (a reader pronounces "АURORA" exactly like "AURORA"; "0" reads as "O"). High visual + high phonetic similarity, on identical/similar goods, points to confusion. (See `euipo-trademark-clearance` and its CJEU corpus for the full Art. 8(1)(b) analysis.)

2. **Bad faith — invalidity.** A character-swap copy of an existing mark is strong evidence of an **intention to imitate**; it supports an application/action for a **declaration of invalidity on the ground of bad faith**, independently of confusion.

3. **Reputation — Art. 8(5) EUTMR.** Where the earlier mark is **reputed**, confusion is **not required**: it is enough that the look-alike takes **unfair advantage** of, or is detrimental to, the reputation or distinctive character of the mark. For reputed marks this is often the cleanest route.

The skill flags which ground(s) fit each hit and feeds them into the recommended action.

---

## Inputs

**Required:**
- `mark_name` — the mark to screen.

**Optional:**
- `mode` — `watch` or `clearance`. If not given, ask which.
- `nice_classes` — strongly recommended; narrows the search and cuts noise.
- `reputed` — `yes`/`no`. If `yes`, prioritise the Art. 8(5) analysis.

If `mode` is missing, ask: *"Are we watching an existing mark for look-alikes (watch), or checking a proposed mark before filing (clearance)?"*

---

## Workflow

### Step 1 — Build the confusable set

Reduce the mark to its **skeleton** and generate its plausible **confusable variants**, using the mapping in `references/confusables.md` (derived from the Unicode confusables standard, UTS #39). Cover at least:

- **Cross-script homoglyphs** — Cyrillic / Greek letters that look like Latin ones (А, Е, О, Р, С, Х, Ѕ; ο, ν, …).
- **Digit-for-letter** — 0↔O, 1↔l↔I, 5↔S, etc.
- **Case / shape tricks** — uppercase/lowercase that imitate other letters (rn→m, vv→w, cl→d, lI/Il ambiguity).
- **Diacritics and spacing** — accented variants (AURÓRA), inserted spaces/hyphens/zero-width characters.

Prioritise high-probability variants (the patterns seen in real squatting — cross-script, zero-for-O, case tricks) and cap the set to keep the search tractable. Note any variant the connector cannot search.

### Step 2 — Search the EUTM register

Using the configured EUIPO connector (`search_trademarks`), search each variant against the register, scoped to `nice_classes` where given. Collect, per hit: mark, owner, status, classes, filing date.

### Step 3 — Confirm the look-alike

For each hit, confirm it is a genuine look-alike (visually and/or phonetically confusable with `mark_name`) rather than a coincidence, and record **how** it diverges (which character was swapped, which script).

### Step 4 — Assess the legal angle

For each confirmed look-alike, assess the three grounds above:
- **Art. 8(1)(b)** — rate the visual and phonetic similarity (homoglyphs are typically high on both) and goods/services similarity.
- **Bad faith** — note whether the character-swap pattern, owner, and timing suggest deliberate imitation.
- **Art. 8(5)** — if the screened mark is reputed, assess unfair advantage / detriment (confusion not required).

### Step 5 — Recommend an action (draft)

Map the assessment to a **recommended action for counsel to weigh**, not a decision:
- Strong Art. 8(1)(b) on a pending application → **opposition**.
- Reputed mark → **opposition / action on Art. 8(5)** (unfair advantage; no confusion needed).
- Registered look-alike + imitation signals → **declaration of invalidity (bad faith)**.
- Domain/online use rather than a registration → flag as a likely **UDRP / online-enforcement** matter, outside this skill's register scope.
- Always leave the choice (oppose / cancel / demand / monitor / take no action) to the reviewing attorney.

---

## Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EUIPO HOMOGLYPH / LOOK-ALIKE SCREENING
  Mark screened: [MARK]   Mode: [watch / clearance]
  Classes: [CLASSES]      Date: [DATE]
  DRAFT — qualified counsel review required before use
  Reviewing attorney: ___________________________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONFUSABLE VARIANTS SEARCHED
[list of variants generated + any the connector could not search]

LOOK-ALIKES FOUND
| Look-alike | How it diverges | Owner | Classes | Status |
|---|---|---|---|---|
| АURORA (Cyrillic А) | 1st char Cyrillic | ... | 32 | Registered |

PER-CONFLICT ASSESSMENT
## [look-alike] — [owner]
- Divergence: [which character / script]
- Art. 8(1)(b): visual [rating] + phonetic [rating] + goods [rating] → [signal]
- Bad faith: [imitation signals, or "not assessed"]
- Art. 8(5): [if reputed — unfair advantage signal, or "N/A"]

FACTORS FOR COUNSEL TO WEIGH
[one line per look-alike: which ground(s) fit and why]

WHAT THE ATTORNEY MUST DECIDE
[oppose / seek invalidity (bad faith) / demand / monitor / no action — explicitly left to counsel,
 plus open unknowns: genuine use, reputation evidence, owner identity, domain vs register scope]

LIMITATIONS
This screening searches the EUTM register only, via the configured connector, for the
confusable set generated. It does not cover national registers, domains, or unregistered
use, and the connector's handling of non-Latin characters bounds what can be searched.
This report does not constitute an enforcement recommendation.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Edge cases and refusals

- **No EUIPO connector available:** explain the register cannot be searched; offer to generate the confusable set only, clearly marked "no register search performed."
- **Connector cannot search non-Latin characters:** report this honestly and list the variants that could not be checked — do not imply a clean result.
- **Very short marks / common words:** flag that the confusable set explodes and noise rises; recommend scoping by class and owner.
- **Use is online/domain only, not a registration:** flag as an online-enforcement / UDRP matter outside this skill's register scope.
- **User asks whether to oppose / sue:** this skill surfaces conflicts and grounds; the enforcement decision is for qualified counsel. Redirect.

---

## Scope and Legal Use

This skill is intended for use by qualified IP professionals as a first-line look-alike screening tool. All outputs are privileged work product unless the supervising attorney decides otherwise.

- Outputs are confidential and matter-specific drafts.
- The reviewing-attorney line must be completed by a named qualified attorney before any output is acted on or shared.
- This skill does not constitute legal advice and does not create an attorney-client relationship.
- This skill does not decide enforcement. It surfaces look-alike conflicts and the grounds that may apply; the choice to oppose, seek invalidity, demand, monitor, or take no action is for the reviewing attorney, weighing factors outside this skill's scope (genuine use, reputation evidence, commercial priorities).
- Register coverage and non-Latin-character handling depend on the connector configured by the user.
