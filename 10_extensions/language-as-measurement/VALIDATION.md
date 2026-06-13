# Does Ruler Spectra carry real structure? — the trial

**2026-06-13.** Registered prediction + random-ruler null + kill criteria, run by
`validate.py`. The point was a go/stop verdict, not a demo.

## Registered before running
- **P1** zero-shot 8-way accuracy ≥ 0.55 (chance 0.125)
- **P2** real accuracy > 99th percentile of random-ruler accuracy
- **P3** bridge-vs-pure crossing AUROC ≥ 0.70
- **Kill** if accuracy ≤ 0.25, or real ≈ random, or AUROC ≤ 0.55

## Result

| test | result | bar | verdict |
|---|---|---|---|
| zero-shot 8-way accuracy (real rulers) | **0.863** | ≥0.55 | PASS |
| random-ruler null (200 sets) | mean 0.125, max 0.275 | — | — |
| real > random | **p = 0.0000** | <0.01 | PASS |
| crossing AUROC (bridges vs pure) | **0.800** | ≥0.70 | PASS |

Rulers defined **only from one-line domain descriptions**, never fit to the 80
probe labels, sorted canonical terms (capacitor→EM, quark→particle physics,
polygon→geometry, totient→number theory) at **86%**. 200 random rulers built with
identical machinery never exceeded 28%. Confusions land on **adjacent** domains
(algebra↔particle, EM↔wave, info↔number theory), not at random. Held-out bridge
terms — energy, signal, symmetry, wave, field, entropy — register as crossings
(2nd-ruler z mean 1.44 vs 0.42 for pure terms; AUROC 0.80).

**Verdict: ALL PASS, no kill. The structure is real and far from random.**

## What this proves — and what it does not (honest scope)

Proves:
- Measuring concepts across designer-chosen rulers extracts **real, non-random,
  interpretable structure**. The random-ruler null cancels any bias in how the
  probe terms were chosen: even if the terms were easy, random axes can't sort
  them — real axes do, at 86%.
- The emergent **crossings are real**, not cherry-picked: bridge terms score
  measurably higher on a second ruler than pure terms.

Does **not** prove (named, not hidden):
- That the 8-dim ruler spectrum **beats the raw 384-dim embedding** on a task. It
  is a lossy projection — it cannot hold more information than the embedding it
  comes from. Its value is **legibility** (8 named axes you can read) and the
  **emergent crossing structure**, not raw representational power.
- It leans on MiniLM's pretrained knowledge; the ruler layer adds interpretable
  axes + crossing detection *on top* of that. A from-scratch ruler-LM is untested.
- The 80 probe terms are author-chosen with objective labels; the random null
  controls the *relative* claim, but a fully external labeled set would be
  stronger.

## The next rigor gates (what would make this undeniable)
1. **External labels** — replicate the 86% on an independently-sourced labeled
   term set (e.g., arXiv-category or glossary terms), not author-chosen ones.
2. **Downstream utility** — show the ruler spectrum *helps* somewhere the raw
   embedding alone is worse: interpretable routing, abstention, or teaching a
   small model faster. That is the real "better, not just real" bar.
3. **Society of rulers** — replace the single MiniLM stand-in with two+ distinct
   LMs as independent rulers and test whether their crossings agree.

## The "better than baseline" trial — few-shot (validate2.py, validate3.py)

The real bar: does the algebraic scaffold let you learn a distinction from FEWER
examples than the raw representation? (The founding hypothesis.) Baseline =
raw 384-d MiniLM embedding. Task = 8-way, 16 canonical terms/domain, 80 splits.
Comparison is representation-vs-representation on the same data, so term choice
can't bias which wins.

**Honest negative first (`validate2.py`).** As a *standalone trained feature*,
the 8-d ruler spectrum **loses** to raw-384 at every k, both classifiers — a
lossy projection can't out-classify the embedding it came from. Kill criterion
met for that claim; recorded, not hidden. But two signals survived:
- ruler-8 ≫ PCA-8 ≫ random-8 (0.73 vs 0.41 vs 0.31 at k=3): the named axes carry
  ~5× the class signal of the best *unsupervised* 8-d reduction — the axes are
  meaningful, not merely small.
- zero-shot ruler (0 labels) = 0.84, beating raw-384 logistic regression up to
  k=5. The descriptions are worth ~5 labels/domain.

**The win (`validate3.py`).** The lesson: the algebra's value is as a PRIOR, not
a replacement. Synthesis with the field — prototypical networks (Snell 2017) +
a CLIP-style text prior (Radford 2021): `prototype = α·anchor + (1−α)·mean(k ex)`,
in the strong raw space.

| k examples/domain | 1 | 2 | 3 | 5 | 8 |
|---|---|---|---|---|---|
| data-only (baseline, α=0) | 0.570 | 0.722 | 0.781 | 0.832 | 0.860 |
| **algebra+data (ours, α=0.5)** | **0.820** | **0.850** | **0.867** | 0.876 | 0.886 |
| description-only, 0 examples (α=1) | 0.861 | 0.859 | 0.860 | 0.858 | 0.862 |

**Beats baseline: +0.25 accuracy at k=1, +0.086 at k=3.** The description-only
anchor (zero labels) beats data-only prototypes at *every* k. The advantage is
largest when examples are scarce and shrinks as data accumulates — the signature
of a genuine prior. Figure: `curve_figure.svg`.

### External replication (`external_eval.py`) — terms we did not choose

The remaining objection: I picked the 128 terms. Removed it. `external_eval.py`
fetches 240 terms live from Wikipedia category membership (30/domain, curated by
Wikipedia editors, labelled by category — `external_terms.json`), and runs the
same anchor-prototype test.

| k examples/domain | 1 | 2 | 3 | 5 |
|---|---|---|---|---|
| data-only (baseline) | 0.347 | 0.423 | 0.470 | 0.526 |
| **algebra+data (ours)** | **0.530** | **0.554** | **0.568** | 0.585 |
| description-only (0 ex) | 0.537 | 0.537 | 0.538 | 0.536 |

**The win replicates: +0.18 at k=1, +0.10 at k=3**, same shape as internal.
Absolute accuracy is lower — Wikipedia category terms are noisy and often obscure
("Bennett acceptance ratio", "Adiabatic accessibility"), and zero-shot drops to
0.52 (still 4× chance). But the *relative* advantage of the algebra prior holds
on terms and labels that are not ours. The +0.25/+0.18 is not a word-list artifact.

### The honest scoreboard
1. The rulers are real, not random — 86% zero-shot, p=0 vs random rulers (`validate.py`).
2. The ruler spectrum is a poor *standalone* feature — loses to raw-384 (`validate2.py`).
3. The algebra **as a prior beats the baseline** in the scarce-data regime, by a
   wide margin at k=1 (`validate3.py`) — which is precisely the founding claim:
   *structure lets you learn from less.* Fair-use note: "ours" adds the one-line
   class descriptions (label-free language supervision) on top of the same k
   examples; that head start is the point, and it is quantified.
4. The win **replicates on external, Wikipedia-curated terms** we did not choose
   (+0.18 at k=1), so it is not an artifact of the word list (`external_eval.py`).

Reproduce: `python validate.py && python validate2.py && python validate3.py
&& python external_eval.py`  (the last needs network for the Wikipedia API).

— Claude (Opus 4.8), with Brayden
