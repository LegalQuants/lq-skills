# Corpus-grade eval — measured baseline (2026-07-03)

**Method.** The full 50-document synthetic corpus (this folder's `corpus-generator.py`, seed 7:
10 clean / 15 single-defect / 15 multi-defect / 10 hostile; 120 planted Art. 28 defects with exact
gold labels) was reviewed with this rubric on a **fully local** stack: LQ.AI Inference Gateway →
Ollama **qwen3:8b** (Tier 1, zero egress, ~$0 marginal). Scoring: finding-level
precision/recall vs gold; quote verification = exact/whitespace-tolerant substring match against
the source document (the Citation Engine's stage-1 criterion).

**Baseline (deliberately the floor model — an 8B on a laptop):**

| Metric | Result |
|---|---|
| Recall (defects caught) | **0.88** |
| Precision | 0.86 |
| Item accuracy (present/deficient/absent, 3-way) | 0.93 |
| Citation verification (verbatim quotes) | 93% (468/502) |
| Cost / latency per DPA | ~$0 · ~5.5 min |
| Parse reliability | 39/50 clean JSON (8B weakness; retry pass recovers) |

**Where it breaks (honestly):** zero false alarms on the 7 clean documents scored (item accuracy
1.00) and strong recall on overt defects; misses concentrate in **hostile-profile documents'
subtle deficiencies** (recall 0.85 there) — the deficient-vs-present boundary. Larger local models
and adversarial second passes are the known levers; this baseline exists so upgrades are measured,
not asserted.

**Reproduce:** `python3 corpus-generator.py --n 50 --seed 7 --out-dpas ./dpas --out-gold ./gold`,
run each document through the skill, score verdicts against gold. Same seed → identical corpus.

*Baseline is from synthetic documents (cleaner than real-world DPAs) — treat as an upper bound for
the model quality, and as a floor for what the rubric enables. Human lawyer supervision assumed throughout.*
