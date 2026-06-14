# Two more teaching levers, both measured — both honest negatives (for now)

**2026-06-13.** After Muon won decisively (+2.5×, adopted), the next two named
levers were curriculum and counterpart-distillation. Tested both, full force.
Both came back negative at this scale. Reporting them as plainly as the win,
because that is the discipline — and because an honest negative is a real result.

## Curriculum (easy→hard) — HURTS here (`curriculum_ab.py`)

Competence-based curriculum (Platanios 2019): rank windows by difficulty (mean
token rarity, −log p), and at step t sample only from the easiest competence(t)
fraction, competence growing 0.2→1.0. Same 3-layer model, same Muon, same val;
only data order differs.

| step | curriculum ppl | shuffled ppl |
|---|---|---|
| 450 | 224 | **83** |
| 900 | 125 | **59** |
| 1800 (final) | 53.8 | **48.8** |

**Shuffled wins at every matched step**, and reaches curriculum's *final* (53.8)
by step 1200 — ~1.5× faster *and* a better endpoint. Why: restricting early
training to the easiest (most common-token) windows starves the model of the full
distribution the validation set is drawn from; it overfits easy text early and
never recovers the lead. Honest negative for this difficulty proxy + schedule.
Kept shuffled order. Figure: `curriculum_figure.svg`.

## Counterpart distillation — no gain YET (`counterparts.py`)

Two genuinely different LMs as co-teachers: MiniLM (external) + **CK's own
book-trained GPT** (`ck_grow.pt`), fused by reliability weighting on the 8-way
term task.

| k | MiniLM | CK-GPT | fused (gated) |
|---|---|---|---|
| 1 | 0.596 | 0.145 | 0.596 |
| 3 | 0.784 | 0.167 | 0.773 |
| 5 | 0.832 | 0.174 | 0.832 |

**CK-GPT scores ~0.15 — barely above the 0.125 chance.** At 4 layers / ppl ~65 it
is too early in training to be a useful teacher for this task; its single-term
embeddings carry almost no domain signal (and single terms are out-of-modality for
a model trained on book *sequences*). A reliability gate (drop a teacher below 0.6×
the best) gives no-harm at k=1,5; at k=2,3 tiny-holdout noise occasionally lets it
through, dragging fusion ~1% below MiniLM. So: the society protocol is sound (it
mostly refuses a weak teacher), but **the second teacher does not help yet.**

## The honest scorecard, after testing all three

| lever | verdict |
|---|---|
| **Muon optimizer** | **WIN — +2.5× faster, adopted** |
| curriculum (easy→hard) | negative — shuffled wins; easy-first starves the distribution |
| counterpart distillation | no gain yet — CK-GPT too early; gate protects, re-run as it trains |

One of three landed — and it landed big. That is the truthful picture: the
geometry-aware optimizer is a real, free win; the other two levers, tested fairly,
did not help at this scale, with clear reasons and clear re-test conditions (a
stronger CK-GPT; a better curriculum proxy or none). The broad Muon run continues
to train and grow regardless.

— Claude (Opus 4.8), with Brayden
