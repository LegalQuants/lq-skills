# lq-dpa-art28-review

Deep **GDPR Article 28** review of Data Processing Agreements: all eight Art. 28(3) mandatory terms
plus six commercial checks, through an explicit **controller/processor party lens**, with
**verbatim-quote citations** (machine-verifiable), severity grading, and proposed redlines.
Spain/EU depth (LOPDGDD, AEPD practice, SCCs/TIA, AI Act Art. 50 flag). Bilingual EN/ES.

**Relationship to the built-in `dpa-checklist-review`:** complementary, not competing. Use the
built-in for **regime triage** (GDPR / US-state / HIPAA BAA / general commercial). Use this skill
when the regime is GDPR and you need the **exhaustive, machine-scorable specialist pass** — fixed
14-item rubric, three-verdict discipline, quotes verified character-for-character.

## What makes this contribution unusual: it ships with its own benchmark

- `evals/corpus-generator.py` — a **deterministic 50-DPA synthetic corpus generator** (10 clean /
  15 single-defect / 15 multi-defect / 10 hostile; ~120 planted Art. 28 defects with exact gold
  labels, because the label is decided before the text is emitted). Same seed → same corpus.
- `evals/RESULTS.md` — a **measured baseline** from running this rubric over the full corpus on a
  fully local model (LQ.AI gateway → qwen3:8b, Tier 1). Upgrade your model, rerun, compare.
- Fixtures: one clean and one hostile corpus document (with its gold file) power the evals.

## Installation

Standard agentskills / Claude Skills format: drop the folder into your LQ.AI deployment's `skills/`
directory (appears in the Skill Library), or use per the Anthropic skills conventions.

## Usage

> "Review this DPA — we are the **controller**." · "Revisa este contrato de encargo de tratamiento —
> somos el **encargado**." · "Score this vendor DPA against Article 28; transfers to the US expected."

The skill asks for the party lens if missing, and will not guess. Output: 14-row findings table,
redlines per deficiency, three-point negotiation summary, open questions.

## Scope & limits

GDPR-specialist by design (other regimes → the built-in checklist skill). Statutory items are
labelled as law; commercial checks as craft — the skill never presents preference as requirement.
**Software, not legal advice** — a licensed lawyer supervises and signs all output.

## Provenance & attestation

Distilled from North End Law's GDPR Art. 28 review practice and its DPA benchmark programme. No
client data or firm-confidential positions. Author + practicing-attorney attestation:
**Sergio Maldonado** (admitted California + Spain).
