# Five-model comparison, 7 August 2026

The independent check on the v1.5.0 changes. `REPORT.md` is the full write-up, including the
complete methodology.

**What was run.** The same skill on five engines — Claude Opus 5, Claude Sonnet 5, Claude Haiku 4.5,
Gemini 3.1 Pro and a local gpt-oss-120b — over two arbitration cases, three samples each, driven
through a real multi-turn conversation whose user side was played by an isolated model that never
saw the answer key. Scored in code against a key confirmed request-by-request before any run, then
independently by two blind LLM judges.

**Why two cases.** The ICC case's respondent is 60% state-owned, so on that case alone a model can
plead Article 9.2(f) for the wrong reason and be indistinguishable from one that read the documents.
The second case has no State party at all, yet one of its twelve requests still genuinely engages
9.2(f) on content. The pairing is the instrument; the two are never merged into one score.

**Files.** `_judge_summary.json` (both judges, per-dimension) · `_grounds_strict.json` (the loose vs
strict grounds metric — see the report's warning about it) · `_electricity.json` (measured local
power draw) · `ARMS.json` (the five arms, rates and privilege posture as declared before the runs).

Raw transcripts, per-run scores and the runner live in the study's own repository, which is private
because it carries the answer keys in full.

**Both cases are entirely fictional.**
