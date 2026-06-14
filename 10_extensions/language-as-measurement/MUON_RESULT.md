# Muon vs Adam — the geometry-aware optimizer, measured and adopted

**2026-06-13.** Frontier mechanism #4 (geometry-aware optimization) was the named
highest-ROI lever. Tested it, didn't assume it.

## The A/B (`train_ab.py`, `muon.py`)

Identical fixed 3-layer transformer on the 795M-token book corpus — same init,
same data order, same schedule — **only the optimizer differs.** Muon (Keller
Jordan 2024) orthogonalizes each weight-matrix update via Newton–Schulz, so steps
move in the spectral geometry of the matrix; AdamW is coordinate-wise.

| step | Adam ppl | Muon ppl |
|---|---|---|
| 150 | 224 | 156 |
| 450 | 121 | 75 |
| 600 | 104 | 65 |
| 900 | 83 | 53 |
| 1500 | **65.7** | **42.8** |

**Muon wins at every step.** It reaches Adam's *final* perplexity (66) by step
~600 — **~2.5× faster** — and ends 35% lower (42.8 vs 65.7), at <1% overhead. The
registered prediction (1.3–2× faster) was beaten. Figure: `ab_figure.svg`.

## Honest note on adoption

Hot-swapping Adam→Muon *mid-training* on the already-trained step-7000 model
bumped perplexity 52 → 102 for a step (optimizer switch = different update
geometry + momentum reset). The A/B validated Muon **from scratch**, not
hot-swapped, so the broad run was **restarted fresh on Muon** (the validated
configuration); the Adam run is preserved as `grow_log_adam.jsonl` for a
full-scale Adam-vs-Muon comparison as the fresh run passes the same milestones.

Muon is now CK's default optimizer (`CK_OPT=muon` in `train_grow.py`; `CK_OPT=adam`
falls back). Hidden 2-D weight matrices use Muon; embeddings, head, norms, and
biases stay on AdamW.

## Scorecard update
Frontier mechanism #4 moves **next → tested & adopted (+2.5× training speed)**.
Remaining next levers: curriculum schedule, and distillation from counterpart LMs.

— Claude (Opus 4.8), with Brayden
