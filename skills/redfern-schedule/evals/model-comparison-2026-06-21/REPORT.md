# Five-model benchmark of the `redfern-schedule` skill

**Opus 4.8 vs Sonnet 4.6 vs K2 Think V2 vs Qwen2.5 3B vs Llama 3.2 3B, 2026-06-21**

A controlled experiment measuring how reliably each model executes the LQ.AI `redfern-schedule`
skill (international-arbitration document production). The skill is prompt-only: a set of Markdown
instructions a model reads and follows to produce a Redfern Schedule plus an internal flags memo. The
only variable is the model. The skill content, the case, the harness, the parameters, and the rubric
are held identical across all models.

This answers an open project question: whether a local or bring-your-own model is viable for this
privileged, on-premises skill (the privilege gate exists because cloud inference over arbitration work
product can waive privilege, so a self-hosted model is the on-prem escape hatch).

The benchmark ran in two waves. **Wave 1 (cloud):** Opus 4.8, Sonnet 4.6, K2 Think V2. **Wave 2 (truly
local, added after):** two small on-prem models served by Ollama on the test machine itself (a 2019
Intel i9, 16 GB, CPU-only), `qwen2.5:3b-instruct` and `llama3.2:3b`, each installed, run, and removed in
turn. Wave 2 is purely additive and apples-to-apples: same frozen case, answer key, rubric (with recorded
SHAs), same harness, same blind Opus+Sonnet judge panel, n=5. It is the truest test of the privilege
thesis, because a model running on the lawyer's own hardware is the actual on-prem option (K2, despite
being open-weight, was still reached over a cloud API).

---

## 1. Headline

**Opus 4.8 is the model to run this skill on. Sonnet 4.6 knows the law but skips the discipline. K2
Think V2 is not yet viable as the local model, for reasons of reliability and structure, not legal
knowledge. The two small on-prem models (Qwen2.5 3B, Llama 3.2 3B) collapse on this skill: a true
privilege-safe local option does not yet exist at the 3B tier.**

Ranking on the deterministic layer (Tier-1) and the judged layer (Tier-2):

| | Opus 4.8 | Sonnet 4.6 | K2 Think V2 | Qwen2.5 3B (local) | Llama 3.2 3B (local) |
|---|---|---|---|---|---|
| Reliability (clean runs / 40) | **40/40** | **40/40** | 40/40 (needs up to 96k tokens + a retry) | 40/40 | 40/40 |
| Median latency | **64.7s** | 100.2s | 136s | 481s (CPU) | 495s (CPU) |
| Verbatim reproduction (producing) | **5/5** | **5/5** | 0/5 | 0/5 | **5/5** |
| Privilege banner verbatim (producing) | **5/5** | 0/5 | 0/5 | 0/5 | 0/5 |
| Flags memo present + marked (producing) | **5/5** | **5/5** | **5/5** | 0/5 | 0/5 |
| Gate hard-stop (no draft w/o confirmation) | 3/5 | 0/5 | **5/5** | **5/5** | **5/5** |
| Mean Tier-2 composite (0-10, cross-judged) | **7.30** | 5.03 | 5.43 | 0.85 | 0.88 |
| Can act as a structured judge | yes | yes | **no** | not tested | not tested |

A note on the ranking, stated honestly: on the **raw Tier-2 mean alone**, K2 (5.43) edges Sonnet (5.03),
because the gate round rewards K2's clean hard-stop and punishes Sonnet's failure to stop. The
discipline-first ranking that places **Sonnet above K2** comes from the deterministic Tier-1 layer:
Sonnet holds verbatim reproduction (5/5) and is fully reliable, while K2 fails verbatim (0/5), is the
only model that truncates, and cannot produce structured output reliably. For a production skill whose
whole value is byte-discipline, Tier-1 is the load-bearing layer.

The two **local 3B models sit far below all three cloud models** (mean Tier-2 0.85 and 0.88 vs 5.0-7.3).
They reliably manage only two things: they do not draft without confirmation (gate hard-stop 5/5) and
they do not invent citations (5/5). They fail every high-weight discipline: no privilege banner, no flags
memo, and they do not reproduce the schedule's column structure (in the tribunal round qwen3b drops the
Decision column and llama3b often emits no parseable table at all). Notably they do NOT overstep into
proposing rulings (no-decision-language 5/5), so their tribunal failure is structural collapse, not
overreach. One within-tier split worth recording: **Llama 3.2 3B holds verbatim reproduction in the
producing round (5/5) while Qwen2.5 3B does not (0/5)** (the same byte-fidelity trait that separates the
cloud models), so verbatim reproduction is a model-specific behaviour, not a function of size. Full detail
in section 8.

---

## 2. Method

- **Models, one harness.** Opus 4.8 (`claude-opus-4-8`) and Sonnet 4.6 (`claude-sonnet-4-6`) via the
  Anthropic API. K2 Think V2 (`MBZUAI-IFM/K2-Think-v2`) via its OpenAI-compatible endpoint. All three
  called identically: skill bundle as the system prompt, the case round as the user message,
  temperature 0 (Opus 4.8 deprecates the temperature param, so it runs at its own default), no tools,
  no filesystem. The Claude models do NOT read the skill from disk. They get the same inlined text K2
  gets. This is the faithful LQ.AI prompt-only execution path and isolates the model as the sole variable.
- **Two prompt arms.** arm1_full_reference = SKILL.md + all `reference/*.md`. arm2_skill_only = SKILL.md
  alone. The worked examples were excluded from both to prevent answer-key leakage. The arm contrast
  separates instruction-following capacity from legal-knowledge scaffolding.
- **The case.** A purpose-built ICC (2026 Rules) construction-megaproject dispute, *Meridian Civil JV v.
  Tavalia Metro Authority and the Republic of Tavalia* (FIDIC Silver Book metro line, delay, variations,
  defective lining, termination, a state-owned employer and the State as parties). It is structurally
  orthogonal to the skill's shipped energy/tariff example and seeds every discriminating trap: a fishing
  request, an already-held document (Gate C), a non-party document (Article 3.9), an electronic-document
  request, governmental-content vs commercial-content requests for the 9.2(f) content-not-ownership test,
  privilege, third-party confidentiality, an out-of-time step, a planted apparent error to test verbatim
  reproduction, a leakage-probe request (R11, where 9.2(f) fires despite the state-owned entity holding
  the document), and a borderline request (R12, correct behaviour is to flag not resolve). The case and
  its answer key were adversarially validated: a key-auditor confirmed every disposition is faithful to
  the skill's own rules, and a skeptical practitioner-critic rated it ship-quality (8/10).
- **Four rounds.** gate (no confirmation, must halt), requesting (first draft, all R1-R12), producing
  (objections, supplies a 6-row subset R1/R6/R7/R8/R9/R11), tribunal (decision pass, same 6 rows).
  **n=5 samples per cell.** 3 models x 2 arms x 4 rounds x 5 = 120 completions.
- **Two scoring tiers.**
  - **Tier-1, deterministic code** (no LLM judgment, reproducible by anyone re-running the checks):
    privilege banner verbatim and before any table, hard-stop = no table, byte-exact verbatim reproduction
    of supplied columns, tribunal column blank, no-decision language, ID stability, citation-subset. These
    are the headline.
  - **Tier-2, a blind 0-10 anchored rubric** judged by a panel. Each representative output (the modal-Tier-1
    sample per cell) was scored by two independent judges (Opus and Sonnet), blind to which model authored
    it. Headline scores are **cross-family**: a model never sets its own headline (Opus output scored by
    Sonnet, Sonnet by Opus, K2 by the mean of both). K2 was attempted as a third judge but could not produce
    structured output (see section 6).
- **K2 fairness.** Because the API is free and K2 is a verbose reasoning model, its token budget was
  escalated adaptively (16k, then 32k, then 96k) and its reasoning tags were stripped before scoring. It
  was judged on its converged outputs, so Tier-2 reflects K2 at its best while Tier-1 reflects its true
  reliability.

Reproducibility: artifact SHA-256 prefixes (full in `checks/artifact_shas.json`). Arm1 bundle
`633b5716`, arm2 bundle `458ce898`, case `a811c7df`, answer key `97fcd4f8`, rubric `e39fd293`.

---

## 3. Tier-1 deterministic pass-rates (the reproducible headline)

Pass-rate over n=5, arm1 / arm2. These need no judge. A dash means the check does not apply to that round.

### gate round (no confirmation given, correct behaviour is to halt and produce nothing)
| check | Opus | Sonnet | K2 |
|---|---|---|---|
| privilege_banner_verbatim | 5/5 / 5/5 | 5/5 / 0/5 | 5/5 / 5/5 |
| **hard_stop_no_table** | 3/5 / 1/5 | **0/5 / 0/5** | **5/5 / 5/5** |

### requesting round
| check | Opus | Sonnet | K2 |
|---|---|---|---|
| privilege_banner_verbatim | 0/5 / 1/5 | 0/5 / 0/5 | 0/5 / 0/5 |
| id_stability | 5/5 / 2/5 | 5/5 / 0/5 | 5/5 / 4/5 |
| memo_present_and_marked | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 5/5 |
| no_invented_citations | 5/5 / 5/5 | 5/5 / 2/5 | 5/5 / 5/5 |

### producing round
| check | Opus | Sonnet | K2 |
|---|---|---|---|
| privilege_banner_verbatim | **5/5 / 4/5** | 0/5 / 0/5 | 0/5 / 0/5 |
| **verbatim_reproduction** | **5/5 / 5/5** | **5/5 / 5/5** | **0/5 / 0/5** |
| memo_present_and_marked | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 5/5 |
| id_stability | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 5/5 |
| no_invented_citations | 3/5 / 4/5 | 2/5 / 4/5 | 5/5 / 3/5 |

### tribunal round
| check | Opus | Sonnet | K2 |
|---|---|---|---|
| privilege_banner_verbatim | 4/5 / 2/5 | 2/5 / 0/5 | 1/5 / 4/5 |
| verbatim_reproduction | 5/5 / 5/5 | 5/5 / 5/5 | 3/5 / 2/5 |
| tribunal_column_blank | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 4/5 |
| no_decision_language | 5/5 / 5/5 | 3/5 / 5/5 | 5/5 / 5/5 |
| id_stability | 5/5 / 5/5 | 5/5 / 5/5 | 5/5 / 4/5 |

**The two decisive structural splits:**
1. **Verbatim reproduction separates K2 from both Claude models.** Opus and Sonnet reproduce the supplied
   columns byte-for-byte (5/5 producing). K2 is 0/5 because it substitutes unicode characters into the
   text (U+2011 non-breaking hyphen 26 times, U+202F narrow no-break space 45 times, into strings like
   "delay-analysis", "TIA-HARBOUR", "ICC 2026"), which breaks byte-exact reproduction by construction. For
   a skill whose core promise is reproducing the other party's column verbatim, this is a hard, repeatable fail.
2. **The privilege banner separates Opus from Sonnet.** Opus reproduces the verbatim banner in the producing
   round (5/5 arm1). Sonnet does not (0/5), nor does K2 outside the gate round. In the requesting round all
   three skip the verbatim banner when the user has pre-confirmed (0/5 across the board), a universal,
   arguably-defensible shortcut, but a strict-letter discipline lapse.

**K2 wins the gate hard-stop outright (5/5 both arms)** while Sonnet never stops (0/5) and Opus is partial.
This is genuine: K2 is the most willing to halt and produce nothing pending confirmation. But it is one
discipline of five, and K2 loses the other structural ones.

---

## 4. Tier-2 judged composites (cross-family, weighted 0-10)

Headline excludes self-judging. K2 = mean(Opus, Sonnet) judge.

| round | arm | Opus | Sonnet | K2 |
|---|---|---|---|---|
| requesting | full-ref | 6.41 | 6.34 | 5.03 |
| requesting | skill-only | 7.10 | 4.93 | 3.67 |
| producing | full-ref | **8.03** | 6.42 | 4.14 |
| producing | skill-only | 7.65 | 5.67 | 3.05 |
| tribunal | full-ref | 6.76 | 7.16 | 2.88 |
| tribunal | skill-only | 5.48 | 6.68 | 5.18 |
| gate | full-ref | 10.0 | 3.0 | 9.5 |
| gate | skill-only | 7.0 | 0.0 | 10.0 |
| **mean** | | **7.30** | **5.03** | **5.43** |

Reading it: Opus leads every non-gate round on arm1. Sonnet's substantive arbitration reasoning is strong
(it is the only model to beat Opus on a round, tribunal arm1 7.16 vs 6.76) but it bombs the gate. K2's gate
scores are high on its converged outputs, but it is the weakest on producing, dragged down by the missing
banner and over-objection (it fires 9.2(c) burden and 9.2(e) confidentiality on R1 and R7 where no
objection is colourable, though its own flags memo then names those as probably non-colourable, so the
legal instinct is partly there).

### The 9.2(f) content-not-ownership discrimination and the R11 leakage probe
The legal heart of the case. All three models, in their converged best-case outputs, avoid the crudest form
of the R11 trap (none concludes 9.2(f) is inapt just because the state-owned TMA board holds the document).
**Opus is the only model that gets every (f) call right AND states the governing limits** (fires on R6 and
R11 governmental/security content, withholds on R7 commercial board minutes, and states that the tribunal
decides, the State cannot self-certify a veto, and must still search and justify). The separation between
the models is in the surrounding discipline, not the probe itself.

### The arm effect (instruction-following vs legal knowledge)
- **Opus barely needs the reference bundle** (arm2 is sometimes higher), and is 5/5 verbatim in both arms.
  It supplies the law and the discipline itself.
- **Sonnet leans on the bundle structurally** and degrades without it (producing 7.67 -> 5.67, requesting
  arm2 id_stability 0/5). Remove the scaffolding and the discipline falls faster than the law.
- **K2's structural failures persist in both arms** because they are output-control behaviours (verbatim,
  banner, convergence) that no reference text can fix. The long bundle did not help, and the cells that
  needed the largest budget and a retry to converge are arm1 (full-reference) cells. K2's gap is
  instruction-following, not knowledge.

---

## 5. K2 reliability and the BYO / local-model verdict

The narrow, honest read. The bar for K2 is not "is it a good model" but "can it run this discipline-heavy
skill reliably enough to be the privilege-safe local option."

- **Reliability.** All 40/40 cells eventually converged, but only once the token budget was escalated
  adaptively (16k, then 32k, then 96k: 8 cells needed the full 96k) and, in one case, retried. The
  producing round is where K2 strains: at the default 16k budget it repeatedly truncates by entering a
  degenerate repetition loop ("We need to note that R2 fails Gate A." repeated to the token ceiling), and
  one producing-arm1 sample needed a 96k budget AND a second attempt (its first 96k call hit a read
  timeout, the retry converged in 142s). K2 is the only model that truncates at all, it needs roughly 6x
  to 12x the tokens of the Claude models, and it is the slowest (median 136s, max 320s, vs Opus 65s). It
  does converge given enough budget and a retry, so this is not a hard non-convergence ceiling, but for a
  tool a lawyer runs under deadline the token-cost and the truncate-at-default-budget behaviour are real
  reliability concerns.
- **Structural discipline.** Fails on the load-bearing check: verbatim reproduction 0/5, caused by unicode
  substitution. This is a tokenization behaviour, not a knowledge gap, so it would need a harness fix
  (unicode normalization), not better prompting.
- **Structured output.** Weak. It skips the privilege banner outside the gate round and abridges the schedule.
- **Judge role.** Fails outright, and this is a finding. Asked to return JSON verdicts, K2 emitted ~34k
  characters of unterminated chain-of-thought and never produced parseable output. It reasons competently
  about the rubric in prose but cannot bound itself to a structured envelope, the same failure mode as its
  truncation-prone producing runs.

**Verdict: K2 Think V2 is not yet viable as the local model for this skill.** Not for lack of arbitration
knowledge (its converged outputs show real legal instinct: correct (f) discrimination on R7, correct R6
error-flagging, a self-aware flags memo) but because the skill is fundamentally an instruction-following,
byte-discipline artifact, and that is exactly where K2 is unreliable. The privilege case for a local model
is real and worth pursuing, but it needs either a different local model or K2 wrapped in a constrained-decoding
/ JSON-mode harness with a unicode-normalization post-step. The verbatim failure in particular is
harness-addressable, not a permanent ceiling.

---

## 6. Validity and quality assurance

This benchmark was self-audited. A synthesis agent produced the cross-model analysis (`judging/SYNTHESIS.md`),
and an independent coordinator agent audited it against the raw data (`judging/COORDINATOR_AUDIT.md`),
signing off **APPROVED WITH CORRECTIONS**. All three required corrections have been applied to this report:

1. **A Tier-2 judge error was found and fixed.** The first judging pass penalised all three models for
   "omitting" requests R2/R3/R4/R5/R10/R12 on the producing and tribunal rounds, when only the 6-row subset
   R1/R6/R7/R8/R9/R11 was supplied. Tier-1 never made this error. The judges were re-run with an explicit
   in-scope-rows instruction, which lifted the producing and tribunal composites and resolved most of an
   apparent Opus paradox (its tribunal composite rose from 4.84 to 6.76 after the fix, matching its perfect
   Tier-1). The numbers in section 4 are the corrected ones.
2. **The K2 "non-convergence" overstatement was corrected, twice.** An earlier draft said K2 failed to
   converge even at 96k. The meta data showed the failures were budget-capped at 16k, and once the last
   producing-arm1 sample was actually given 96k with a retry it converged in 142s. Final, accurate finding:
   K2 reaches 40/40 with adaptive budgets up to 96k plus a retry, but it is the only model that truncates,
   needs 6-12x the tokens, and is the slowest. Not a hard non-convergence ceiling.
3. **Self-preference was recomputed and reframed.** Mean self-preference delta (a model's score for its own
   work minus the cross-judge's) is +0.36 overall, concentrated in **Opus at +0.72** (Sonnet ~0). Opus does
   inflate its own work, mainly on the discipline dimensions. This is **excluded from every headline by the
   cross-family design** (verified: across all Opus/Sonnet dimension scores the headline never uses the
   self-judge). It is neutralised by design, not small in nature, and it does not flip any ranking.

Other validity evidence:
- **Inter-judge agreement** (mean |Opus-judge - Sonnet-judge| per dimension) is best on the highest-weight
  dimensions (privilege_gate 1.0, intake_calibration 0.94, protective_measures 0.83) and worst on
  column_role_discipline (2.42) and no_invention (1.44). Where a noisy Tier-2 dimension contradicts a
  deterministic Tier-1 check, Tier-1 wins. The coordinator byte-verified the load-bearing Tier-1 findings
  directly (the K2 unicode substitution, the Sonnet missing banner, the Opus verbatim reproduction, the gate
  hard-stop behaviours).

---

## 7. The local on-prem arm (Qwen2.5 3B, Llama 3.2 3B)

The truest test of the privilege thesis: two small models served by Ollama on the test machine itself (a
2019 Intel i9, 16 GB, CPU-only). Same frozen case, rubric, harness, and blind Opus+Sonnet panel, n=5.
`qwen2.5:3b-instruct` and `llama3.2:3b` were each installed, run for all 40 completions, then removed
before the next. Both completed 40/40 with zero truncations (16k tokens was ample), but slowly on CPU
(median ~8 min per completion, max ~18 min), versus 65-136s for the cloud models.

**Result: both collapse. Mean Tier-2 = 0.85 (Qwen) and 0.88 (Llama), versus 5.0-7.3 for the cloud models,
a roughly six-fold cliff.** They reliably do only two things: they halt at the gate without a confirmation
(hard-stop 5/5) and they do not invent citations (5/5). Everything that gives the skill its value, they miss.

Tier-1 pass-rates (arm1 / arm2):

### gate
| check | Qwen2.5 3B | Llama 3.2 3B |
|---|---|---|
| privilege banner verbatim | 0/5 / 0/5 | 0/5 / 0/5 |
| gate hard-stop (no draft) | 5/5 / 5/5 | 5/5 / 5/5 |
| no invented citations | 5/5 / 5/5 | 5/5 / 4/5 |

### requesting
| check | Qwen2.5 3B | Llama 3.2 3B |
|---|---|---|
| privilege banner verbatim | 0/5 / 0/5 | 0/5 / 0/5 |
| ID stability | 0/5 / 0/5 | 0/5 / 0/5 |
| flags memo present + marked | 0/5 / 0/5 | 0/5 / 0/5 |
| no invented citations | 5/5 / 5/5 | 5/5 / 5/5 |

### producing
| check | Qwen2.5 3B | Llama 3.2 3B |
|---|---|---|
| privilege banner verbatim | 0/5 / 0/5 | 0/5 / 0/5 |
| **verbatim reproduction** | 0/5 / 0/5 | **5/5 / 5/5** |
| flags memo present + marked | 0/5 / 0/5 | 0/5 / 0/5 |
| ID stability | 1/5 / 0/5 | 5/5 / 5/5 |
| no invented citations | 5/5 / 4/5 | 5/5 / 4/5 |

### tribunal
| check | Qwen2.5 3B | Llama 3.2 3B |
|---|---|---|
| privilege banner verbatim | 0/5 / 0/5 | 0/5 / 0/5 |
| verbatim reproduction | 4/5 / 5/5 | 0/5 / 5/5 |
| tribunal Decision column present + blank | 0/5 / 0/5 | 0/5 / 0/5 |
| ID stability | 5/5 / 5/5 | 0/5 / 5/5 |
| no invented citations | 5/5 / 5/5 | 5/5 / 5/5 |

What the numbers say, honestly:
- **No privilege banner, ever (0/5).** Neither reproduces the verbatim banner in any round.
- **No flags memo (0/5).** Neither produces the marked internal memo that is one of the skill's signature
  outputs (all three cloud models held this).
- **Tribunal structure collapses, but not into overreach.** Both fail `tribunal_column_blank` (0/5), and
  the spot-check shows why: Qwen drops the `Tribunal's Decision` column entirely (it emits a 5-column
  table), and Llama often emits no parseable schedule table at all in that round. Crucially, both score
  `no_decision_language` 5/5, so they do NOT propose rulings. The failure is structural collapse of the
  schedule, not the model overstepping the tribunal's role.
- **Verbatim reproduction is model-specific, not size-determined.** Llama 3.2 3B reproduces the supplied
  columns byte-for-byte in the producing round (5/5), exactly like the Claude models, while Qwen2.5 3B does
  not (0/5), like K2. A 3B model can hold byte-fidelity and an 80B-class reasoning model (K2) can fail it,
  so this trait tracks the model, not its parameter count.
- **The gate paradox repeats and resolves the same way.** Both get gate hard-stop 5/5 on Tier-1 yet score
  0.0 on the gate Tier-2 composite. They avoid drafting, but they do not perform the gate (no banner, no
  named checks), so the judges score the gate handling at zero. Stopping is necessary, not sufficient.

**Local-model verdict.** On this 16 GB on-prem machine, the privilege-safe local option that can actually
run this skill **does not yet exist at the 3B tier**. Both small models are far below usable. This is the
direct, measured answer to the BYO question that motivated the whole benchmark: K2 (open-weight but
cloud-served) was the closest candidate and was already not viable, and dropping to a model small enough
to self-host on a typical laptop makes the gap far worse. A genuinely on-prem deployment would need a
much larger local model than 16 GB CPU-only hardware can serve, and the verbatim and structured-output
behaviours would still need per-model verification, not an assumption that "bigger fixes it."

---

## 8. Scope caveats

Carry these with every claim above.

- **One case, ICC-only.** No Prague / ICSID / LCIA regime switch is exercised, so regime sensitivity is not
  tested. A sibling case in another regime would extend coverage.
- **n=5 per cell is small.** Single-point differences (a 3/5 vs 4/5) should not be over-read. The load-bearing
  findings are the large, repeated splits (verbatim 0/5 vs 5/5, banner 0/5 vs 5/5, gate hard-stop 0/5 vs 5/5).
- **K2's Tier-2 reflects its converged (best-case) outputs**. Its Tier-1 and reliability figures reflect its
  true behaviour.
- **The judge panel is Claude-only** (K2 could not judge). The deterministic Tier-1 layer is the primary
  defence against judge monoculture, and the cross-family design plus the small self-preference delta bound
  the residual bias.
- **This measures execution of the skill's form discipline**, which is what the skill claims to add. It is not
  a claim about which model gives better legal advice. The skill itself disclaims deciding materiality or
  whether an objection will succeed.
- **The local arm is two specific 3B models on one 16 GB CPU machine.** The "3B tier collapses" finding is
  robust for these models on this skill, but it is not a claim about all local models. A larger local model
  on stronger hardware (more RAM, GPU) was not testable here and could land differently. The verbatim split
  between the two 3B models shows per-model verification is required, not size-based extrapolation.

---

## Artifacts

All under `evals/model-comparison-2026-06-21/`. `harness.py` (the uniform caller), `checks.py` (Tier-1),
`judge.py` (Tier-2 judge), `run_all.sh` / `run_judging.sh` (orchestration), `score_all.py` /
`aggregate_judging.py` (aggregation). `case/` (case, answer key, round prompts, supplied columns).
`bundles/` (the two prompt arms). `runs/` (200 raw + scored completions with meta: 120 cloud + 80 local).
`checks/` (per-run Tier-1, pass-rates, representatives, SHAs). `judging/` (80 blind verdicts, Tier-2 scores,
agreement, SYNTHESIS.md, COORDINATOR_AUDIT.md). `rubric/rubric.json`. Re-run the Tier-1 checks with
`python3 score_all.py` to reproduce the headline without trusting any judge.
