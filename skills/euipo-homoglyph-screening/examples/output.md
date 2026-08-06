# Example: watch screening of AURORA (class 32)

> **Note.** This is an illustrative example with invented register data, to show the output shape. It will be replaced/supplemented with a real (anonymised) case from practice.

## Input

- **Mark screened:** AURORA
- **Mode:** watch
- **Classes:** 32
- **Reputed:** no

## Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EUIPO HOMOGLYPH / LOOK-ALIKE SCREENING
  Mark screened: AURORA   Mode: watch
  Classes: 32             Date: 2026-06-25
  DRAFT — qualified counsel review required before use
  Reviewing attorney: ___________________________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONFUSABLE VARIANTS SEARCHED
АURORA (Cyrillic А) · AURОRA (Cyrillic О) · AURORА (Cyrillic А, final) ·
AUR0RA (zero for O) · AURÓRA (accent) · A U R O R A (spaced)
[Not searchable by connector: zero-width-character variants]

LOOK-ALIKES FOUND
| Look-alike | How it diverges | Owner | Classes | Status |
|---|---|---|---|---|
| АURORA | 1st char Cyrillic А (U+0410) | Eastbridge Trading | 32 | Registered |
| AUR0RA | "O" replaced by digit 0 | (individual) | 32, 33 | Application published |

PER-CONFLICT ASSESSMENT

## АURORA — Eastbridge Trading
- Divergence: first character is Cyrillic А (U+0410); reads and looks identical to Latin AURORA
- Art. 8(1)(b): visual High + phonetic High (pronounced identically) + goods Identical (class 32) → strong confusion signal
- Bad faith: single cross-script swap of an existing mark is a classic imitation pattern → supports invalidity on bad faith
- Art. 8(5): N/A (mark not flagged as reputed)

## AUR0RA — (individual applicant)
- Divergence: letter O replaced by digit 0; visually near-identical
- Art. 8(1)(b): visual High + phonetic High + goods Identical/closely similar → strong confusion signal
- Bad faith: digit-for-letter swap on an application; timing/owner to investigate

FACTORS FOR COUNSEL TO WEIGH
- АURORA (registered): Art. 8(1)(b) strong + bad-faith invalidity available.
- AUR0RA (pending application): Art. 8(1)(b) strong → opposition window open.

WHAT THE ATTORNEY MUST DECIDE
Oppose AUR0RA (application still opposable) and/or seek a declaration of invalidity
against АURORA on bad faith; or send a demand; or monitor. Open unknowns: genuine use,
true owner identity behind the individual applicant, whether AURORA has acquired a
reputation (which would open Art. 8(5)). The enforcement decision is for the reviewing attorney.

LIMITATIONS
This screening searches the EUTM register only, via the configured connector, for the
confusable set generated. It does not cover national registers, domains, or unregistered
use, and the connector's handling of non-Latin characters bounds what can be searched.
This report does not constitute an enforcement recommendation.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
