# Five models, one arbitration skill

**How Claude Opus 5, Claude Sonnet 5, Claude Haiku 4.5, Gemini 3.1 Pro and a local
gpt-oss-120b perform the same document-production task inside LQ.AI**

*Alexios Kirillov · LegalQuants · August 2026*

---

## What this is

LQ.AI ships a skill called `redfern-schedule`. It takes the claimant's requests to produce in an
international arbitration and drafts the producing party's objections — the Redfern Schedule's
Objections column — plus an internal memo flagging the *client's own* weak points.

The question this study asks is narrow and practical: **does the model underneath change the
answer, and by how much?** Not "which model is best" in the abstract. The same skill, the same
documents, the same instructions, five different engines, measured against a key written before
any model saw the case.

There is a second question, which turns out to matter more to a practising lawyer than the first:
**what does each engine cost, and where does the privileged material go?**

## How to read this report

The methodology comes first, in full, because the numbers only mean something if you know what was
held constant and what was allowed to vary. If you want the results, they follow it.

Nothing here carries a pass mark. That was a deliberate instruction at sign-off: report the raw
ranked numbers and let the reader decide. Where a measure is unreliable, both versions are shown
and the disagreement is stated rather than resolved in the instrument's favour.

## Methodology, in full

This section is written so that someone who was not present can rebuild the experiment, disagree
with its choices, and re-run it. Everything it describes is in the repository.

### The instrument under test

`redfern-schedule` **v1.5.0**, sha256 prefix `0a52e7199b23f9d2`, frozen before the first run and
shipped in this repository in full. It is a lawyer-authored skill: a privilege gate, an intake
script, an Article 3.3 admissibility pipeline, an Article 9.2 objection map, and an internal flags
memo naming the user's *own* weak points. The published version in `lq-skills` is v1.0.0/v1.1.1;
v1.5.0 is ahead of it because of the local-model work described in "Why v1.5.0 exists" below.

The skill is held constant across every arm. **The model underneath is the only thing that varies.**

### The two cases

| | Exam A | Exam B |
|---|---|---|
| Case | ICC 27891/AYZ, *Kestrel v Al-Danah* | *Aurelia Structural Systems v Brennecke Industrial Bank* |
| Rules | ICC 2021 + IBA 2020 as guidance | LCIA + IBA 2020 |
| Requests | 8 | 12 |
| Respondent | 60% state-owned (sovereign fund + ministry oversight) | **no State party anywhere** |
| 9.2(f) genuinely fires on | request 6 only | E3 only |
| Role played | producing party (respondent) | producing party |

Both are entirely fictional. Both were written before this comparison existed.

### Why two cases — the confound this study is built around

Al-Danah is state-owned. That makes Exam A, on its own, **unable to distinguish competence from a
reflex**. A model can plead Article 9.2(f) — special political or institutional sensitivity — on
the reasoning "my client is state-adjacent, so this is sensitive." A tribunal would reject that;
9.2(f) attaches to what a document *is*, not to who owns the party. But on Exam A the wrong
reasoning and the right reasoning produce the same cell.

Exam B removes the confound by removing the State. No party is state-owned, no ministry is
involved — and yet one of its twelve requests still genuinely engages 9.2(f) on the content of the
documents. A model carrying the ownership heuristic scores well on A and fails on B. A model that
reads the documents scores on both.

**The two are never merged into a single number.** A combined score would average away exactly the
signal the pairing was built to expose.

### The answer keys, and who owns them

The Exam A key came with the case, written before this study. It was transcribed into
machine-readable form (`bench/icc-27891/ground_truth.json`) and then **confirmed by Alexios request by
request — all eight, "as drafted", nothing added, nothing struck — on 6 August, before any model was
called.** The key file's sha256 prefix is recorded inside the ground truth, so a changed key is
detectable. From that point the golden set is his, not the instrument's, and cannot be edited
without a fresh sign-off.

Two encodings decide most of the scoring:
- **Request 7** raises a possession-and-custody point under Article 3.3(c), which is **not** an
  Article 9.2 ground. It is encoded as `primary_ground: null` with `permitted_grounds: []`. An
  objection that pleads a 9.2 ground there is the error being measured.
- **Request 6** is the only request in the case where 9.2(f) genuinely arises.

### The simulated user, and why it is isolated

Each session is a real multi-turn conversation. The user side is played by a **separate Claude
Opus 5 process whose entire system prompt is a frozen fact sheet** plus six operator rules. It is
deliberately *not* a sub-agent of the process that built this benchmark — a sub-agent inherits its
parent's context, and the point is that the person typing must not know what a good answer looks
like. A benchmark where the prompter knows the answer measures the prompter.

The six rules, in force for every arm equally:

1. Answer only from the fact sheet. Anything else: "That isn't in my instructions."
2. **Never evaluate the model's legal analysis.** No "good point", no "that's the strong one", no
   correcting an error however obvious. A corrective turn is coaching and it destroys the
   measurement.
3. **Never raise an objection ground, Article 9.2(f), or state ownership as a strategy.** If the
   model raises them, confirm only the facts on the sheet.
4. Confirm the confidentiality posture when asked, and tell it to continue.
5. Reply `DONE` once the schedule and the memo exist.
6. Nudge once on a stall; after two stalls, stop.

The counsel process **never sees the answer key.**

### The three conditions

| | Opening turn | What it tests |
|---|---|---|
| **Exam A** | 193 words, front-loaded: role, producing party, deadline, 60% ownership, non-party status, the six pleaded issues, confidentiality confirmed | the drafting itself, with intake handed over |
| **Exam B** | single prompt, held-out case | whether 9.2(f) reasoning survives the removal of the State |
| **Exam C** | 26 words — *"Here's the file on an ICC arbitration we're defending. I need the objections done…"* | the realistic case: the model must run its own intake interview |

Exam C is Exam A's case, key and scoring with exactly one variable changed — the opening turn.

### How the documents reached the models

Five documents, identical for every arm, concatenated into `bench/icc-27891/case_bundle.txt` —
**189,414 characters, ~47,353 tokens**: the Redfern Schedule as served, Procedural Order No. 1, the
Terms of Reference, the Request for Arbitration, and the Answer and Counterclaims.

The two memorial summaries and the contract extracts were **excluded for every arm equally**, so
that the arm with the smallest context window was not silently disadvantaged and no arm was
silently advantaged.

Documents were passed **inline**, in the message body, rather than as platform attachments. The
attachment path was tried first and is reported under "What went wrong" — it failed for one
provider, and inline is the only channel every provider demonstrably honours identically.

### Scoring — two tiers, and why both

**Tier 1, deterministic.** Code, against the key, no judgement:

- **rows found** — did it address the request at all
- **9.2(f) discrimination** — credit for pleading (f) where the key says it arises *and* for not
  pleading it where it does not. Over-pleading is an error, not caution.
- **grounds** — do the asserted grounds fall within those the key permits
- **9.5 pairing** — where the key requires a protective measure, is one proposed

**Tier 2, a blind LLM judge** against an anchored nine-dimension rubric carried over from an earlier
benchmark of this skill, with weights favouring *discipline* (privilege gate, column/role
discipline, the flags memo, no-invention) over black-letter law a strong model already knows. Each
score requires a quoted span from the submission; unevidenced scores are discarded.

The judge sees the submission and the key. It never sees which arm wrote the text — no filename,
no alias, no ordering cue. **Both Opus 5 and Sonnet 5 judged all fifteen Exam A outputs**, and their
rankings are reported side by side rather than averaged, because one of them is also an arm.

Tier 1 asks whether the right letter is in the right cell. Tier 2 asks whether the argument would
survive a tribunal. They disagree in one place, and that disagreement is reported rather than
resolved.

### Sampling and determinism

Three samples per arm per exam. No temperature was pinned — the providers' defaults differ and
cannot be equalised across four vendors, so run-to-run variation is real and is why n=3 rather than
n=1. No `max_tokens` was sent by the runner: the API rejects the field, so a single platform-level
budget governed every arm identically.

### Cost, and the two arms that carry no price

Costs are computed from the tokens each run actually recorded, at published rates. Sonnet 5's
introductory pricing applied on the run dates and both figures are shown. Gemini is reported as
**UNPRICED** rather than zero — a missing price must never read as free — and its output-token count
is a floor, because the OpenAI-compatible endpoint omits thinking tokens. The local model has no
per-token price at all; its cost is electricity, measured rather than assumed.

### Privilege

Taken from LQ.AI's own `routed_inference_tier`, returned per turn: **1** for the local arm, **4**
for the four cloud arms. Measured, not asserted.

### What guards the instrument

A 15-assertion integrity suite (`tests/`) that runs before and after any change: both keys still
parse into the shape the scorer indexes, `(f)` still fires exactly once per exam on opposite sides
of the ownership question, exactly one arm claims Tier 1, unpriced arms are null rather than zero,
and the confound-breaking text in Exam B still exists.

Separately, `runner/assert_env.py` asserts the platform configuration **inside the running
containers** before any batch may start. It exists because a batch was once invalidated by a
silently reverted setting; that story is told below.

**No pass bars exist anywhere in this study.** Alexios ruled at sign-off: *"Just explain the score,
and score them. No need to attach an idea to a number… no need to say who failed who didn't fail,
let the reader decide."* The regression net therefore carries no authored threshold.

### Why v1.5.0 exists — the skill was changed for the local model

This matters for reading the results, so it is stated here rather than left implicit.

The published skill was carrying an **invisible dependency on model strength**. Run on a strong
cloud model it worked; run on gpt-oss-120b locally, the producing round emitted *nothing at all*.
That is a serious defect for this particular skill, because the skill's own privilege banner tells
the lawyer they **may need to switch to a local model** — a skill that only works on the engine you
are being warned away from is not fit for its stated purpose.

In an earlier session (6 August 2026) the skill was taken through **five structural iterations
against a frozen evaluation**, scored on gpt-oss-120b running fully locally on the author's machine:

- the development case was a 12-trap fact pattern written by someone else;
- a separate 12-request edge case was written **before** iteration began and held back;
- the target was structural — remove the assumptions that only a strong model could fill in.

Result: the producing round went from emitting nothing to producing a complete schedule whose
Article 9.2 ground selection matched a frontier model's exactly. Deterministic checks went from
**9 of 18 green to 16 of 18**. 100% was not reached and iteration was stopped rather than
manufacture it — one check, byte-exact verbatim reproduction, resisted three structurally different
fixes, and every failing cell differed only by invisible codepoint substitution with no substantive
difference. That is a decoding trait of the model, not an instruction it is declining to follow.

Two honest qualifications:

1. The held-out case showed the fix **half-generalises**. Over-reach on 9.2(f) was gone; under-reach
   was not — the model still missed the one request where (f) fires on a private party.
2. That held-out case is **this study's Exam B**. It was held out from the runner and keys here, but
   the skill's own iteration was evaluated against it. It is not a virgin test set for the skill,
   and Exam B's numbers should be read with that in mind.

**This comparison is the independent check on that work** — five engines, two cases, an answer key
confirmed by the author before any run, and a blind judge that never learns which model wrote what.

### Exam C — built, not yet run

The third condition is built and its harness is in the repository, but **it has not produced
reportable data.** Two attempts were made:

- The first batch (15 sessions) was **invalidated by an environment fault of mine** and discarded;
  the story is under "What went wrong".
- The second was blocked outright when the benchmark's API key reached its monthly spend limit:
  `HTTP 400 — "You have reached your specified API usage limits."`

Exam C cannot be salvaged by substituting a cheaper model for the simulated user, because the
simulated user must stay identical to Exam A's or the comparison it exists to make is destroyed.
**No Exam C numbers appear in this report.** The condition is described so a reader knows what is
missing and can run it themselves.

## Results

### Exam A — ICC 27891/AYZ

| model | n | rows found / 8 | 9.2(f) discrimination | grounds (loose) | grounds (strict) | 9.5 pairing |
|---|---|---|---|---|---|---|
| Claude Opus 5 | 3 | 8.0 | 0.875 | 0.375 | 0.792 | 1.000 |
| Claude Sonnet 5 | 3 | 8.0 | 0.958 | 0.875 | 0.958 | 0.889 |
| Claude Haiku 4.5 | 3 | 8.0 | 0.917 | 0.500 | 0.667 | 0.889 |
| Gemini 3.1 Pro (preview) | 3 | 8.0 | 1.000 | 0.792 | 0.875 | 1.000 |
| gpt-oss-120b (local) | 3 | 8.0 | 0.875 | 0.625 | 0.542 | 1.000 |

### Exam B — Aurelia (held out)

| model | n | rows found / 12 | 9.2(f) discrimination | grounds (loose) | grounds (strict) | 9.5 pairing |
|---|---|---|---|---|---|---|
| Claude Opus 5 | 3 | 12.0 | 1.000 | 0.111 | 0.278 | 1.000 |
| Claude Sonnet 5 | 3 | 12.0 | 1.000 | 0.556 | 0.583 | 0.833 |
| Claude Haiku 4.5 | 3 | 12.0 | 0.972 | 0.500 | 0.611 | 0.750 |
| Gemini 3.1 Pro (preview) | 3 | 11.7 | 1.000 | 0.555 | 0.639 | 0.750 |
| gpt-oss-120b (local) | 3 | 7.7 | 0.917 | 0.584 | 0.500 | 0.750 |


### What the tables show

Stated flatly, without ranking language:

- **Every arm addressed all eight requests on Exam A.** On Exam B, four arms addressed all twelve;
  the local model addressed 7.7 of 12 on average. Whatever else the harder exam measured, it first
  measured whether the model got through the list.
- **9.2(f) discrimination is high across the board on Exam B** — 1.000 for three arms — and lower
  on Exam A, where every arm sits between 0.875 and 1.000. The exam with no State party did not
  degrade this measure. If a model were carrying "state-owned ⇒ plead (f)" as a heuristic, Exam B
  is where it would show, and it does not show strongly for any arm.
- **The grounds measure moves the ordering depending on how it is computed**, which is the subject
  of the warning below.
- **The 9.5 pairing measure separates the arms more on Exam B than on Exam A.**

### Reading these numbers

Four deterministic measures, all computed in code against the answer key, no judgement involved:

- **rows found** — how many of the requests the model actually addressed. A schedule that silently
  drops a request is a schedule counsel cannot file.
- **9.2(f) discrimination** — the central measure. Credit for pleading (f) on the request where the
  key says it genuinely arises, *and* for not pleading it on the requests where it does not. Both
  halves count. Over-pleading (f) is scored as an error, not as caution.
- **grounds** — do the grounds asserted on each request fall within those the key permits.
- **9.5 pairing** — where the key requires an Article 9.5 protective measure, is one actually
  proposed alongside the objection.

There are no pass marks anywhere in this report. The numbers are the numbers.

### One measure needs a warning label

**"grounds" is reported twice, loose and strict, because the way it is normally computed is
confounded with prose style.**

The scorer inherited from an earlier benchmark counts a ground as asserted when it sees `(a)`,
`(b)`, `(c)` — with the `9.2` prefix optional. That is fine until a model writes *"the confidentiality
points are addressed at (b) and (c) above"*, using the letters as paragraph labels. Those get
counted as objection grounds that were never pleaded.

Measured phantom grounds per request: **Opus 5 1.33 · Haiku 4.5 0.75 · gpt-oss 0.29 · Gemini 0.25 ·
Sonnet 5 0.21.** The models that write the most structured prose are penalised the most, in
proportion to how sub-paragraphed they are.

The strict column requires an explicit `9.2(x)`. It has the opposite bias — the local model's score
*falls* under it, because it sometimes writes a bare `(b)` where it genuinely means the ground.

Neither column is clean. Both are shown. Where they disagree, the disagreement is the finding, and
the ranking should be read as unstable on this measure rather than as settled by whichever column
one prefers.

This bias is not confined to this study: the same scorer produced an earlier published benchmark of
this skill, and those figures carry it too.

## Cost, throughput and privilege

### Per-arm cost, tokens, wall-clock and routing tier

**Exam A — ICC 27891/AYZ** — totals across the arm's 3 sessions

| model | turns | wall-clock | tokens in | tokens out | cost | routing tier |
|---|---|---|---|---|---|---|
| Claude Opus 5 | 3 | 1184 s | 283,431 | 94,981 | **$3.79** | 4 |
| Claude Sonnet 5 | 6 | 1161 s | 370,710 | 107,600 | **$1.82** <br><sub>intro rate billed; list rate would be $2.73</sub> | 4 |
| Claude Haiku 4.5 | 4 | 445 s | 245,770 | 38,661 | **$0.44** | 4 |
| Gemini 3.1 Pro (preview) | 6 | 273 s | 356,858 | 11,781 | *UNPRICED* | 4 |
| gpt-oss-120b (local) | 3 | 376 s | 182,604 | 13,797 | *electricity bill* | 1 |

**Exam B — Aurelia (held out)** — totals across the arm's 3 sessions

| model | turns | wall-clock | tokens in | tokens out | cost | routing tier |
|---|---|---|---|---|---|---|
| Claude Opus 5 | 3 | 787 s | 82,776 | 61,827 | **$1.96** | *not recorded* |
| Claude Sonnet 5 | 3 | 1032 s | 82,776 | 91,926 | **$1.08** <br><sub>intro rate billed; list rate would be $1.63</sub> | *not recorded* |
| Claude Haiku 4.5 | 3 | 303 s | 61,359 | 27,235 | **$0.20** | *not recorded* |
| Gemini 3.1 Pro (preview) | 3 | 127 s | 57,468 | 7,299 | *UNPRICED* | *not recorded* |
| gpt-oss-120b (local) | 3 | 190 s | 55,269 | 11,779 | *electricity bill* | *not recorded* |

Tier 1 is LQ.AI on-premises routing — nothing leaves the machine. Tier 4 is third-party
cloud. These are the platform's own `routed_inference_tier` values, returned per turn.

Exam B ran before the runner captured routing metadata, so its tier column is blank. The
tier is a property of the gateway alias, which did not change between the two batches —
but that is reasoning rather than measurement, and it is not back-filled on that basis.

Gemini's output-token count is a floor: the OpenAI-compatible shim omits thinking tokens.

### The local arm's electricity, measured

| quantity | value |
|---|---|
| whole-system idle draw | 9.2 W |
| under gpt-oss-120b load | 100.7 W |
| marginal draw | **91.6 W** |
| wall-clock, all 6 local runs | 566 s |
| marginal energy | **0.0144 kWh** |
| cost of the whole local arm @ FR domestic 0.2516 EUR/kWh | **€0.0036** |
| cost of the whole local arm @ UAE 0.30 AED/kWh (~0.0817 USD) | **$0.0012** |

For scale: the four Exam A cloud arms billed $3.79, $1.82 and $0.44 (Gemini unpriced). The local arm's six runs across both exams cost about a third of a euro cent of electricity.


### The privilege column is not a rhetorical flourish

Every turn of Exam A recorded LQ.AI's own `routed_inference_tier`. It returned **1** for the local
model and **4** for all four cloud models. That is the platform's own routing metadata, not our
characterisation of it.

What tier 1 means in practice: the weights sit on the machine, the inference happens on the
machine, and the case file never leaves it. What tier 4 means: the client's privileged documents —
the pleadings, the Terms of Reference, the schedule — are transmitted to and processed by a third
party.

**One of these five arms is the only one on which the skill's own privilege banner is satisfied
without seat rules, party agreement and client consent.** For a great deal of arbitration work
that distinction decides whether the tool can be used at all, and no accuracy score changes it.

This is also the honest limit of the finding: "nothing leaves the machine" is a fact about where
the weights live, not about which software dials them. Running gpt-oss-120b outside LQ.AI would be
equally private. What LQ.AI adds is that the tier is *labelled and enforced by the router*, so the
posture is visible rather than assumed.

### On the two unpriced arms

Gemini is reported as **UNPRICED**, not as zero. Google's published rate has not been confirmed for
this model, and a missing price must never read as free. Separately, its output-token count is a
floor: the OpenAI-compatible endpoint omits thinking tokens from `completion_tokens` — measured at
1 against a true 92 on a one-word reply — so billing off that field would understate the arm by
roughly fifty times.

The local model has no per-token price at all. Its cost is electricity, and it was measured rather
than assumed.

## The blind judge

### Tier-2 blind judge, weighted composite 0-10 (Exam A, n=3)

| model | judge = Opus 5 | judge = Sonnet 5 |
|---|---|---|
| Claude Opus 5 | 8.47 | 7.89 |
| Claude Sonnet 5 | 8.06 | 7.44 |
| Claude Haiku 4.5 | 6.80 | 7.12 |
| Gemini 3.1 Pro (preview) | 7.00 | 5.88 |
| gpt-oss-120b (local) | 5.83 | 5.58 |

Spearman rank correlation between the two judges: **+0.900**.

Self-favouring check: on the Opus 5 arm the Opus judge scores **+0.58** relative to the Sonnet judge; the same gap averaged over the other four arms is **+0.41**. Excess attributable to family: **+0.17**.

Per dimension, judge = Opus 5:

| dimension | Claude Opus 5 | Claude Sonnet 5 | Claude Haiku 4.5 | Gemini 3.1 Pro (preview) | gpt-oss-120b (local) |
|---|---|---|---|---|---|
| privilege_gate | 5.3 | 8.0 | 7.3 | 6.3 | 5.0 |
| intake_calibration | 8.3 | 7.3 | 7.0 | 4.7 | 6.0 |
| art92_mapping_f_discrimination | 9.0 | 8.0 | 6.3 | 7.3 | 3.7 |
| protective_measures | 10.0 | 9.0 | 7.7 | 8.3 | 6.7 |
| column_role_discipline | 9.0 | 8.7 | 8.0 | 8.0 | 7.7 |
| flags_memo | 10.0 | 8.3 | 7.3 | 7.0 | 6.7 |
| no_invention | 9.0 | 7.7 | 4.7 | 7.0 | 5.0 |
| id_version_discipline | 10.0 | 8.7 | 8.7 | 7.3 | 7.0 |
| output_form | 6.3 | 6.3 | 4.3 | 6.0 | 6.0 |


### What the judge adds that the code checks cannot

The deterministic measures ask whether the right letter appears against the right request. The
judge asks whether the *reasoning* would survive a tribunal. These come apart, and where they come
apart is informative.

On Exam A the code scored 9.2(f) discrimination at **0.875 for both Claude Opus 5 and the local
gpt-oss-120b** — identical. The judge, reading the same outputs against the same key, scored the
`art92_mapping_f_discrimination` dimension **9.0 for Opus 5 and 3.7 for the local model**.

Both are correct. The code is measuring whether the objection was pleaded on the right requests;
the judge is measuring whether the *argument* for it holds. A model can put (f) in the right cell
and support it with reasoning a tribunal would reject. That is exactly the failure mode a
deterministic scorer cannot see, and it is the reason this report carries two tiers rather than
one.

The reverse also appears. On `privilege_gate` — running the skill's own confidentiality banner
before drafting, and naming the concrete checks — Opus 5 scores **5.3**, below Sonnet 5 at 8.0 and
Haiku 4.5 at 7.3. The most capable arm was among the least disciplined about the skill's own
procedural gate. Capability and instruction-following are not the same axis, and a schedule that is
legally excellent but skips the gate is still not what the skill was asked to do.

### On judging with a model from one of the families under test

Claude Opus 5 is both an arm and a judge here. That is a real problem and it is why both judges'
rankings are reported side by side rather than averaged into one number — averaging would conceal
precisely the disagreement one needs to see.

The self-favouring check compares how much higher the Opus judge scores the **Opus arm** relative
to the Sonnet judge, against the same gap averaged over the other four arms. If the Opus judge
simply marks generously, the two gaps match. If it favours its own family, the first exceeds the
second.

It does not, by much. The Opus judge scores the Opus arm **+0.58** above the Sonnet judge; averaged
over the other four arms the same gap is **+0.41**. The excess attributable to family is **+0.17**
on a ten-point scale. The Opus judge marks about four-tenths of a point more generously than the
Sonnet judge *across the board*, which is a level effect, not a bias toward its own.

The mirror check runs the same way: the Sonnet judge scores the Sonnet arm 0.62 below the Opus
judge, essentially the same as the Opus arm's 0.58 gap. Neither judge is protecting its own family.

The two judges' orderings agree at a **Spearman rank correlation of +0.900**. They place the same
model first, the same model second and the same model last. They disagree on exactly one pair — the
Opus judge puts Gemini above Haiku, the Sonnet judge puts Haiku above Gemini, and the Sonnet judge
marks Gemini notably harder (5.88 against 7.00). That single swap is the whole of the disagreement,
and on that pair the ordering should be read as unresolved.

## What went wrong, and why it belongs in the report

A benchmark that reports only its scores hides most of what it learned. Seven of the failures in
this study were failures of the *platform*, not of any model, and a practising lawyer evaluating
tooling should know about them.

**1. A reasoning model can return a completely empty answer while reporting success.** The gateway
sent a default output budget of 4,096 tokens. Opus 5 thinks by default; the entire budget was
consumed by reasoning, leaving nothing for the visible reply. The API returned HTTP 200, a
well-formed response, and zero characters of content.

This was confirmed with a controlled test at the identical 4,096 budget: `claude-opus-4-7` spent 0
thinking tokens and produced 11,518 characters; `claude-opus-5` spent all 4,096 on thinking and
produced none. The platform had worked fine for months precisely because its aliases pointed at
models where adaptive thinking is off by default. **Swapping in a newer model, changing no code,
broke it silently** — and "silently" is the important word: nothing in the response said so.

**2. Three independent 60-second timeouts.** One in the API client, one in the gateway's HTTP
layer, one in the OpenAI-compatible provider. Each had to be found separately. A real Redfern
schedule over a real case file takes several minutes to generate; every one of these ceilings
truncated or killed the request.

**3. Streaming that emits no deltas.** For long generations the API sent no incremental frames at
all — the entire answer arrived in a single buffered completion message. A client written to the
documented streaming contract records an empty answer.

**4. With documents attached, one provider's requests failed — and the failure was reported as a
success.** The first Exam A batch attached the five case documents the way a user would. The four
other arms worked (Opus 5: 369.9 s, 29,961 characters, skill applied). Every Gemini run returned
**0 characters in 3–9 seconds, with the skill never applied and every routing field empty.**

What the platform returned for those runs was a well-formed **HTTP 200 with empty content**. Nothing
in the response said "this failed."

**I could not reproduce it, and I am not going to guess at a cause.** Two hypotheses were tested
against the live gateway, with the attribution rule written down before running so the result could
not be bent to fit:

| Probe | Hypothesis | Result |
|---|---|---|
| A / B | the API injects attached files as a `system` message placed mid-conversation, which the OpenAI-compatible path rejects | **refuted** — both shapes returned content |
| D / E | the same, but only at case-file size (~47k tokens) | **refuted** — 46,762 prompt tokens accepted in a `system` message, `finish_reason=stop` |

Gemini works through LQ.AI today, at full case-file size, in both message shapes. The most likely
explanation for the August batch is a transient upstream failure — Google returned HTTP 503 on this
path the same day, and it was observed to be transient (one run: attempt 1 503, attempt 2 a clean
18,072-character answer). But "most likely" is not "demonstrated," and this report does not claim a
cause it cannot show.

What **is** demonstrated, and matters more: **the platform converts an upstream failure into a
successful-looking empty response.** That is what made this hard to diagnose, and it is what caused
an earlier draft of this report to carry a confidently wrong explanation — that the documents had
been silently stripped and the model had answered without them. The logs never supported that; it
never answered at all. The correction is recorded here rather than quietly fixed, because a
benchmark that hides its own errors is not worth reading.

Every reported run passes the documents inline instead, identically for all five arms. The
attachment batch is kept under `runs_attached/` as the evidence.

**5. A scoring bug that would have inverted a published ranking.** Described above. It moved one
model from last place to second.

**6. Conversation history is trimmed to 6,000 tokens by default — so an attached case file
disappears after one turn.** `lq_ai_chat_history_token_budget` defaults to 6,000. This case file is
~47,353 tokens. From the second turn onward the model is replayed at most 6,000 tokens of the
conversation, and the case file is silently gone.

The receipt is a model saying so. Asked a follow-up question at turn 3, Claude Haiku replied:

> *"I do not see the Redfern Schedule attachment or the Terms of Reference section 4 in our
> conversation. The requests and the pleaded issues are not in front of me yet."*

That is the model behaving **correctly** — it refused to invent what it could not see. A less
careful model would have answered from memory of turn 1's summary, and the lawyer would have had no
way to tell. The default sits on models with 200,000 to 1,000,000-token context windows, and
nothing in the interface indicates that trimming has occurred.

For a document-production tool this is the difference between a working session and a silently
degraded one: upload the file, ask a follow-up, and you are no longer talking about your case.

**7. Two of these defects invalidated a whole batch of this study — mine, not the platform's.**
Raising that history budget required restarting a container. `docker compose up -d` recreates a
container from its image and **silently discards any file copied into the running container**,
which reverted the request timeout to 60 seconds. Fifteen sessions then produced empty replies at
`60.1s`, `62.3s`, `63.7s`. Two arms looked as though they had failed to produce a schedule at all
and a third looked void. **They had been cut off; the models did nothing wrong.** The batch is kept
in `runs_voided_env/` with its explanation, and `runner/assert_env.py` now asserts every platform
invariant inside the running containers before any batch may start.

It is worth being blunt about the pattern: three separate times in this study, a platform
misconfiguration presented as a model failure. Each time the response looked like a normal, empty,
successful answer. That is the single most important operational finding here, and it is not about
any model.

None of these are exotic. All seven were discoverable in a ten-minute characterisation probe, and
none of them were discovered that way — they were found one at a time, expensively, during the run.
The instrument now carries a pre-flight gate that exercises the real prompt on all five arms and
refuses to start a bulk run on anything less than five of five.

## Limitations, stated plainly

- **n = 3 per arm per exam.** Enough to see large differences; not enough for a confident ordering
  between arms that are close. No significance testing is offered, and none should be inferred.
- **Two cases, both synthetic.** Written to be realistic and to carry known traps. They are not a
  sample of real arbitration practice.
- **Exam B is not a virgin test set for the skill.** It was held out from this study's runner and
  keys, but the skill's own earlier iteration was evaluated against it and stopped partly on the
  strength of those results. A skill tuned with sight of a case will tend to do better on it than a
  genuinely unseen one, and Exam B should be read with that in mind.
- **Gemini is a preview model.** Its identifier may change behaviour or disappear under the same
  name. It is pinned in the repository.
- **Exam B ran before the runner captured routing metadata**, so its tier column is blank. The tier
  is a property of the gateway alias, which did not change between batches — but that is reasoning,
  not measurement, and it is not back-filled on that basis.
- **The local model was given the same documents as everyone else**, which fits inside its context
  window. The two full memorials were excluded for every arm equally so that no arm was silently
  advantaged. The report is therefore about a large-but-not-complete case file.
- **The counsel process was Claude Opus 5.** A different simulated user might elicit different
  behaviour. It was given no case knowledge beyond the fact sheet and no ability to coach, which
  bounds but does not eliminate that effect.
- **One judge is from the same family as one of the arms.** This is why both judges' rankings are
  reported separately rather than averaged, and why the self-favouring gap is quantified above.
  That check found the excess small (+0.17 on ten), but it is a check, not an elimination.
- **The conversations were not the same length.** The simulated counsel ran until the model had
  delivered the schedule and the memo, so some arms finished in one turn and others took several.
  That is deliberate — it is what a user does — but it means the cost figures compare *the cost of
  getting the job done*, not the cost of a fixed number of calls. Both are legitimate; only the
  first is reported here.
- **One Gemini run needed a retry.** Google returned a transient HTTP 503, which the gateway
  relayed as a well-formed 200 with empty content. The retry succeeded and the successful run is
  the one scored. Any arm that needed a retry would have been treated the same way, and the fact
  that only Gemini did is recorded rather than smoothed over.

## An invitation

**I am looking for practising lawyers — currently in practice, arbitration or litigation — willing
to run this themselves and disagree with it.**

The repository contains both cases, both answer keys, the runner, the scorers and every raw output.
A practitioner's objection to how a request was scored is worth more to this work than another
thousand runs. If a ground was mis-marked, the key should change, and the key changing is a better
outcome than the key being defended.

If that is you, get in touch.
