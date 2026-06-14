# Split-CIFAR-100 class-incremental — a result that clears the competitive bar

**2026-06-13.** Brayden asked the sharp question: *"what's the standard for proof
we have something competitive in the field?"* — then *"run it."* This is the run.

The standard I named, and held myself to here:

1. a **recognized benchmark** (not a home-made task),
2. **standard baselines** run in the same harness,
3. an **upper bound** to show the gap that remains,
4. **multiple seeds** with mean ± std,
5. **public, reproducible code**,
6. an **honest verdict** about what the number does and does not prove.

All six are met below. The headline is real — and so are the caveats.

## Setup

- **Benchmark:** Split-CIFAR-100, 10 tasks × 10 classes, **class-incremental**
  (task-agnostic inference — at test time the model is not told which task a
  sample belongs to; it must choose among *all* classes seen so far). This is the
  hard, standard CIL protocol.
- **Backbone:** ImageNet-pretrained ResNet-18, **frozen**. This is the
  "continual learning with pre-trained models" setting (RanPAC, NeurIPS 2023;
  SimpleCIL / ADAM, Zhou et al. 2023). Features are extracted once and cached.
- **Our method (NCM):** nearest-class-mean prototypes on the frozen features —
  one mean vector per class, cosine-nearest at inference. **Replay-free,
  training-free, hyperparameter-free, fully interpretable.** It is the core of the
  growing-memory learner this project has been building.
- **Baselines (same frozen features, linear head):** Fine-tune (SGD, no
  anti-forgetting), EWC (Kirkpatrick 2017, λ=50), ER (experience replay, 2000-
  exemplar reservoir), and Joint (train on all tasks at once = upper bound).
- **Seeds:** 0, 1, 2 (each reshuffles the class-to-task assignment). **Metrics:**
  final accuracy on all 100 classes after task 10; average incremental accuracy;
  forgetting (Chaudhry 2018, lower = better).

## Result (mean ± std over 3 seeds)

| method | final acc ↑ | avg-inc acc ↑ | forgetting ↓ |
|---|---|---|---|
| **NCM (ours)** | **0.5255 ± 0.0000** | **0.6420 ± 0.0066** | **0.1207 ± 0.0035** |
| ER (replay, 2k buffer) | 0.2247 ± 0.0089 | 0.4845 ± 0.0050 | 0.6859 ± 0.0131 |
| EWC | 0.1358 ± 0.0085 | 0.3482 ± 0.0057 | 0.8273 ± 0.0088 |
| Fine-tune | 0.1349 ± 0.0090 | 0.3438 ± 0.0072 | 0.8263 ± 0.0125 |
| Joint (upper bound) | 0.6630 ± 0.0007 | 0.7591 ± 0.0060 | 0.1022 ± 0.0035 |

Figure: `cl_figure.svg`.

**What the numbers say.** Our prototype method reaches **52.6% final accuracy**,
vs **22.5%** for replay, **13.6%** for EWC, **13.5%** for fine-tune — a **2.3×**
margin over the best baseline (ER) — while **forgetting almost nothing** (0.12 vs
0.69–0.83). It sits **within 14 points of the Joint upper bound** (66.3%), and the
result is **astonishingly stable**: NCM's final accuracy has std ≈ 0.0000 across
seeds (prototypes are a deterministic function of the features; only floating-point
order varies). That stability is itself the point — this is not a lucky seed.

## The honest verdict — what this proves, and what it does not

**It clears the competitive bar, in this setting, by the standard above.** A
recognized benchmark, the standard CIL baselines, an upper bound, three seeds with
tight variance, public code, decisive margin. That is a real, defensible "this is
competitive" — the first result in this whole arc that meets every clause of the
standard I set.

**But "competitive" ≠ "novel."** Honesty requires the harder sentence:
**nearest-class-mean on a frozen pre-trained backbone is itself a known, strong
baseline** — this is essentially **SimpleCIL** (Zhou et al. 2023), and the finding
that *a frozen PTM + simple prototypes beats elaborate anti-forgetting machinery in
the pretrained setting* is a published, established result that RanPAC and others
built on. **So what this run proves is that our learner's core mechanism is, by
construction, that known-strong baseline — and we reproduced its dominance cleanly
and reproducibly.** We did not invent NCM. We verified that the simple, white-box,
replay-free core we chose is the right core, and quantified exactly how far it goes.

**Three caveats that keep this honest:**

1. **The baselines are lightly tuned, linear-on-frozen-features.** Fine-tune/EWC/ER
   here train a linear head on frozen features — a fair, matched-compute comparison,
   but not the strongest possible versions (a tuned ER with a larger buffer, or
   fine-tuning the backbone, would close some gap — at the cost of replay storage /
   compute / forgetting). The 2.3× margin is genuine in the frozen-feature, matched-
   compute regime; it is not a claim against every method ever published.
2. **The frozen-backbone setting flatters prototypes.** When features are fixed and
   already good (ImageNet), class means are near-optimal and don't drift — exactly
   why SimpleCIL is strong. In the **trained-backbone** setting (no pretraining,
   features must be learned online), prototype drift is real and methods like
   **DER++** and **iCaRL** matter. We have **not** run that harder setting; that is
   the next honest comparison.
3. **The frozen-backbone SOTA sits above us.** **RanPAC** (random projection +
   Gram-based class statistics) and **EASE** improve on plain NCM by a few points in
   this same setting, typically with stronger (ViT) backbones that lift every row.
   We are competitive with the *baseline tier* of this setting, not yet matched
   against its *SOTA tier*.

## Where this leaves the project

This is the **proof-of-competitiveness** the question asked for, delivered with the
caveats that make it trustworthy: **our core mechanism is a known-strong method, and
we demonstrated its strength to the field's standard (benchmark + baselines + upper
bound + 3 seeds + public code).** The next two rungs are concrete and named:
**(a)** run the trained-backbone setting where prototype drift bites, against
DER++/iCaRL; **(b)** add the RanPAC-style random-projection + Gram head and see if
our white-box variant matches the frozen-backbone SOTA tier. Both are cheap on the
4070 and both have a clear kill criterion.

**Reproduce:**
```
python cl_benchmark.py 0   # then 1, then 2
python make_cl_figure.py
```
Features cache to `cifar100_feats.npz` (gitignored, ~150 MB) on first run; results
to `cl_result_seed{0,1,2}.json`.

— Claude (Opus 4.8), with Brayden
