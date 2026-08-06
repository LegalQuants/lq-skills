---
last_verified: 2026-06
freshness_window: 12 months
freshness_category: review-required
verified_against: Unicode Technical Standard #39 (Unicode Security Mechanisms) — confusables.txt data file
---

> **Freshness / completeness.** This is a **curated practitioner subset** of the Unicode confusables data (UTS #39, `confusables.txt`) — the most common, high-probability look-alikes seen in trademark squatting. The full Unicode confusables set is much larger and is updated with each Unicode version; for production-grade generation, pull the current `confusables.txt` and apply the UTS #39 **skeleton** algorithm. Treat this table as a prioritised starting set, not an exhaustive one.

# Confusable characters — look-alike generation set

## How to use this (the "skeleton" idea)

Two strings are **confusable** when, after each character is replaced by its prototype, they reduce to the **same skeleton**. To generate the variants of a mark, substitute each Latin character with the look-alikes below (and vice versa) and search each resulting string. Prioritise cross-script and digit-for-letter swaps — those are the highest-probability attacks.

## 1. Cyrillic letters that look like Latin

| Looks like | Cyrillic | Code point |
|---|---|---|
| A / a | А / а | U+0410 / U+0430 |
| B | В | U+0412 |
| C / c | С / с | U+0421 / U+0441 |
| E / e | Е / е | U+0415 / U+0435 |
| H | Н | U+041D |
| I | І | U+0406 |
| J | Ј | U+0408 |
| K | К | U+041A |
| M | М | U+041C |
| O / o | О / о | U+041E / U+043E |
| P / p | Р / р | U+0420 / U+0440 |
| S | Ѕ | U+0405 |
| T | Т | U+0422 |
| X / x | Х / х | U+0425 / U+0445 |
| Y | У | U+0423 |

## 2. Greek letters that look like Latin

| Looks like | Greek | Code point |
|---|---|---|
| A | Α | U+0391 |
| B | Β | U+0392 |
| E | Ε | U+0395 |
| H | Η | U+0397 |
| I | Ι | U+0399 |
| K | Κ | U+039A |
| M | Μ | U+039C |
| N | Ν | U+039D |
| O / o | Ο / ο | U+039F / U+03BF |
| P | Ρ | U+03A1 |
| T | Τ | U+03A4 |
| X | Χ | U+03A7 |
| Y | Υ | U+03A5 |
| v | ν | U+03BD |

## 3. Digits that look like letters (and vice versa)

| Letter | Digit look-alike |
|---|---|
| O / o | 0 |
| l / I | 1 |
| S | 5 |
| B | 8 |
| G | 6 |
| Z | 2 |
| E | 3 (mirrored) |

## 4. Shape / case / multigraph tricks

| Target | Imitated by |
|---|---|
| m | rn |
| w | vv |
| d | cl |
| I / l / pipe | l, I, \| (U+007C), ı (dotless i, U+0131) |
| nn | m (loose) |

## 5. Diacritics (look-alike by accenting)

Accented Latin variants read as the base letter to many consumers and are a common evasion:
- A → Á À Â Ä Å Ā Ã
- E → É È Ê Ë Ē
- I → Í Ì Î Ï Ī
- O → Ó Ò Ô Ö Õ Ō
- U → Ú Ù Û Ü Ū
- N → Ñ
- C → Ç

## 6. Invisible / spacing manipulations

These do not change appearance but change the string a machine matches on:
- Zero-width space U+200B, zero-width non-joiner U+200C, zero-width joiner U+200D
- Inserted ordinary space, hyphen (-), non-breaking space U+00A0
- Repeated/leading/trailing spaces

## Priority order for generation

1. **Cross-script single-character swaps** (Cyrillic/Greek for one Latin letter) — the most common real attack.
2. **Digit-for-letter** (0↔O, 1↔l) — extremely common.
3. **Case / shape tricks** (rn→m, vv→w).
4. **Diacritics**.
5. **Invisible characters** — only when the connector preserves them in the query.

Cap the generated set to keep the register search tractable, and record any variant the connector cannot search rather than silently dropping it.
