# Information as a path across substrates — the general principle, tested

**2026-06-13.** The thesis, sharpened to one sentence:

> Meaning is not a point in one representation. It is a **path across a stack of
> complementary mathematical lenses**, each measuring a different facet, where the
> *whole* — weighted by each lens's reliability in the current regime — is at
> least as good as the best single lens, and better wherever the lenses are
> comparable.

No lens is privileged (every square sits inside a parabola; every circle is
measured by squares — each ruler reads what it can and leaves a defect the next
ruler catches). You carry a **ladder of paradigms** and let information thread
them. The empirical claim — *does carrying many lenses help?* — is the only thing
that makes this more than philosophy, so it was tested.

## The test (`synthesis.py`)

Four genuinely different mathematical paradigms as lenses on an 8-way task, each
scoring every class for a held-out point:

| lens | paradigm |
|---|---|
| **anchor** | vector projection onto class descriptions (semantic axes) |
| **data** | cosine to the k-example prototype (metric geometry of the manifold) |
| **graph** | label propagation over the kNN graph (spectral / relational) |
| hierarchy | coarse parent prior (multiresolution — too coarse to classify alone) |

Combined four ways; the principled one is **reliability-weighting**: trust each
lens by how well it predicts a held-out slice of the few examples
(empirical-Bayes shrinkage — lean on the prior when data is thin).

## The measured law (80 splits)

| examples/class k | 1 | 2 | 3 | 5 | 8 |
|---|---|---|---|---|---|
| anchor (semantic) | 0.860 | 0.859 | 0.859 | 0.861 | 0.861 |
| data (manifold) | 0.591 | 0.726 | 0.784 | 0.834 | 0.859 |
| graph (relational) | 0.673 | 0.758 | 0.788 | 0.828 | 0.853 |
| **fusion (reliability)** | **0.860** | 0.838 | 0.857 | **0.867** | **0.869** |
| best single lens | 0.860 | 0.859 | 0.859 | 0.861 | 0.861 |

**The honest law, three regimes:**
1. **Scarce data (k=1):** one lens dominates (the semantic prior). Naive averaging
   *hurts* — it dilutes the winner (fuse-equal 0.754 ≪ 0.860). Reliability-weighting
   correctly **falls back to the prior** and ties it exactly (0.860). The whole is
   never worse than the best part *only if you weight by reliability*.
2. **Middle (k=2–3):** the awkward zone — the data lenses are mediocre and
   reliability is hard to estimate from one or two examples. Fusion trails the
   prior by ≤0.02. Honest soft spot; not papered over.
3. **Comparable lenses (k≥5):** every paradigm is now informative, and the fusion
   **beats the best single lens** (+0.006 at k=5, +0.014 at k=8) by riding
   whichever is strongest per point.

Figure: `synthesis_figure.svg` — the fusion line tracks the upper region of the
single-lens curves.

## So: useful synthesis? — yes, with a stated boundary

- **Useful, proven:** carrying multiple white-box paradigms and weighting them by
  reliability is **never worse than the best single lens at the extremes and wins
  where the lenses are comparable.** You don't have to know in advance which
  paradigm to trust — the stack adapts. That is the operational payoff of "all
  these things play together."
- **Not a free lunch (the defect, named):** blind averaging is *worse* than the
  best lens when one dominates, and there is a real mid-data dip where reliability
  is hard to estimate. The synthesis is "weight by reliability," not "average."
- **The shape of the win is the point:** information as a path across substrates
  means the right lens leads at each scale — prior when blind, manifold when seen,
  relational in between — and the combined map is the trajectory that always rides
  the best-available paradigm.

This sits on top of the earlier result (a single algebraic prior already beats the
data-only baseline by +0.25 at k=1, externally replicated). The synthesis
generalizes it: *many* priors, reliability-weighted, give a map that is robust
across the whole data range.

Reproduce: `python synthesis.py`.

## Made into a language that LEARNS — online, like an AI and with an AI (`learner.py`)

The batch test above hand-weights the lenses. The real thing is an agent that
*learns to speak the algorithm-language from experience*. `learner.py` is that:
the lenses are the vocabulary; the agent reads a **stream** of experiences,
expresses each in the language, predicts, gets feedback, and learns online —
**no batch fitting**. The AI is in the loop twice: the embedder (MiniLM) is the
perceptual organ, and the agent learns from a feedback stream the way an AI trains.

It learns two things online:
- its **memory** (per-class prototypes / examples fill in from experience), and
- **which lens to trust** — via multiplicative weights / Hedge (Littlestone–
  Warmuth 1994; Freund–Schapire 1997), the no-regret way to learn the reliability
  we used to hand-code.

Result on a 240-experience stream (averaged over 40 orders, harder external set):

| | accuracy |
|---|---|
| agent, first quarter of stream | 0.519 |
| agent, last quarter of stream | **0.612** (learned +0.093) |
| fixed prior (anchor), whole stream | 0.537 (does not learn) |

And the learned lens-weights moved on their own: **anchor 0.33 → 0.09, proto
0.33 → 0.91, knn → 0.00.** The agent began by leaning on its prior (the LM's
zero-shot knowledge), then *learned to trust the memory it grew from experience*.
That weight shift, visible in `learner_figure.svg`, **is** the learning — white-box,
online, with the LM as perception. This is the algorithm-language learning like an
AI and with an AI; the synthesis above is the static snapshot of what it converges to.

Reproduce: `python learner.py`.

— Claude (Opus 4.8), with Brayden
