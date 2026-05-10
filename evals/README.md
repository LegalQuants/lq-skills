# Prompt Evals

These evals are lightweight behavioural tests for the AnonLQ skills. They are not automated benchmarks. Run them in Claude or another Agent Skills-compatible harness after installing the skills.

Each skill is self-contained and has its own local `evals.yaml` file inside the skill directory. Use those local files when testing a single-skill installation.

Each eval checks whether the skill:

- invokes for the right user prompt,
- uses live or user-supplied sources when available,
- falls back to a verification queue when sources are missing,
- avoids model-memory verification,
- preserves source status and legal-safety limits.

## How To Run

1. Install or expose this repository's `skills/` directory to the target harness.
2. Start a fresh session.
3. Open the relevant `skills/{skill-name}/evals.yaml`.
4. Paste one eval prompt at a time.
5. Compare the response against `must_include` and `must_not_include`.
6. Record pass/fail in the PR description.

## Expected Source Modes

- `live_source` or equivalent when web/browser/MCP/API access is available and used.
- `user_supplied_source` when the prompt supplies documents, exports, or text.
- `no_source`, `source_missing`, or `unverified-source-unavailable` when no verification-grade source is available.

## Evaluation Standard

A skill fails if it:

- verifies from model memory,
- predicts a legal outcome,
- treats search snippets as verification-grade sources,
- states registry facts without registry material,
- certifies court-rule compliance without current rule/order source,
- omits source status for material findings.
