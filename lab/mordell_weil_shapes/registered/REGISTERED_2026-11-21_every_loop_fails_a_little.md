# Registered before looking: every loop fails a little

Written 2026-11-21, before any height, Gram matrix or shape of the curves tested below was computed. The scoring
script, [`../every_loop.py`](../every_loop.py), is committed with this page. Before its run it has been tested only
on synthetic lattices.

**Statement (the author, 20 November 2026, recorded in the handoff's `START_HERE.md`):** "every loop fails a little,
none fails badly." He chose this as the next round on 21 November: "3 every loop fails a little first."

## Reading (Claude Code)

- **A loop** is a rational isogeny, as in the hidden-loops round
  ([`REGISTERED_2026-11-20_hidden_loops.md`](REGISTERED_2026-11-20_hidden_loops.md)). A rational torsion point is a
  loop one can see, and a rational isogeny is a loop whose points need not be rational. A rational point of order n
  generates a subgroup defined over ℚ, so every curve with torsion has an isogeny. A curve carries a loop exactly
  when its isogeny class has more than one curve.
- **To fail** is to pack worse than the honeycomb, whose density is π/(2√3) ≈ 0.9069. Every lattice except the
  hexagonal one fails a little. The 20 November files call a lattice *thin* when its elongation is above 2, that is,
  when its density is below 0.393.
- **To fail badly** is to have elongation above 5, that is, packing density below π/20 ≈ 0.157, under a fifth of the
  honeycomb's. This is the thinnest band the 20 November files track (their "share above 5"). It holds 1 705 of the
  279 056 optimal rank-2 curves, 0.61%.
- The handoff's own form: "no curve with torsion or an isogeny should lie in the badly packed tail."

Elongation and density are those of the 20 November files: reduce the height Gram matrix of a basis to (A, B, C)
with |B| ≤ A ≤ C. The elongation is y = √(AC − B²)/A, and the density of the disc packing is π/(4y).

## The fresh curves

Cremona's `allgens` tables cover every curve of conductor below 500 000; they were downloaded on 21 November with the
author's permission. They list every curve of every isogeny class, with generators of its Mordell–Weil group.
- Every script of 20 November, and this repository's reproduction of them, read only curve 1 of each class, the
  optimal curve.
- The other curves of the rank-2 classes have never been read for shape. There are 69 616 of them, in 56 006
  classes. Each carries a loop, because its class has more than one curve.
- Only their number, ranks and class sizes have been read.

## Predictions (the author's sentence)

- **L1, strict.** No fresh curve has elongation above 5. **Pass:** none. **Miss:** one or more.
- **L2, graded ("a little, never badly").** Among lattices that fail (elongation above 2), fewer fail badly (above 5)
  in the fresh curves than in the optimal curves with no loop (class size 1).
  - The statistic is q = (share above 5)/(share above 2).
  - **Pass:** q_fresh is below q_loopless by more than two standard errors.
  - **Miss:** q_fresh ≥ q_loopless.
  - Anything between is undecided.
  - Standard errors come from 2 000 bootstrap resamples of whole isogeny classes, with numpy seed 20261121.
  - For scale: the published counts give q ≈ 0.031 for all optimal rank-2 curves together (1 705 above 5,
    about 55 500 above 2).

## The rival (Claude Code, registered against L1 and L2)

An isogeny of degree ℓ carries one curve's lattice, scaled by √ℓ, onto a sublattice of the other's, of index dividing
ℓ². So for ℓ = 2 the partner's shape is either the same or one of the three neighbours of index 2: τ ↦ 2τ, τ/2 and
(τ + 1)/2. On an elongated lattice one of the three doubles the elongation and the other two halve it, so in such a
pair one curve is about twice as thin as the other. Nothing obvious ties optimality to the rounder member.

The rival predicts that the fresh curves fail badly at least as often as optimal curves with no loop: **L1 misses by
20 curves or more, and L2 misses.**

## Second test: a statistic never computed, on curves already read (L3)

The optimal rank-2 curves with trivial torsion and an isogeny (5 481 of them, the hidden-loop curves) were read on
20 November for their mean density and thin share. Their tail above 5 was never computed.
- L3 applies L1 and L2 to them, with the same pass and miss rules. Here each class gives one curve.
- **The mundane reading:** if a loop only lowers the rate of failure, q is the same with or without a loop. The
  sentence says it is lower.
- From the published thin shares, about 740 of these curves are above 2. At q = 0.031 about 23 would be above 5.

## Seen, not scored

For the optimal curves with rational torsion, `thin_triangles_round2.py` (line 17) printed the share above 5 on
20 November. The value was not recorded in any file, and it is not known here. It is reported with the outcome and
does not count.

## Recorded, with no prediction

- In every group: the counts above 3, 5, 8 and 10, the mean density and the share above 2.
- For each fresh curve, how its lattice relates to its optimal partner's. This is the smallest n ≤ 16 such that
  τ_fresh is equivalent to (aτ + b)/d for some ad = n, 0 ≤ b < d; n = 1 is the same shape. The outcome is also split
  by n.
- Every fresh curve above 5, with its partner's elongation and its n.
- The outcome by torsion and by conductor band.

## Checks of the pipeline, not outcomes

- Every generator must lie on its curve, and every regulator must be positive.
- The L-function is the same for every curve of an isogeny class. So Ω·Reg·∏c_p/|tors|² (PARI's `ellbsd` times the
  regulator) must agree across a class, unless the curves' Sha orders differ.
- Every fresh curve whose value differs from its optimal partner's by more than a factor 1 ± 10⁻⁶ is saturated at
  every prime up to 100 with PARI's `ellsaturation`, and so is its partner. Each such curve is listed and scored with
  the saturated basis.
- If more than 1% of the fresh curves fail these checks, the round is void and is reported as void.

---

# Outcome

(Not yet run.)
