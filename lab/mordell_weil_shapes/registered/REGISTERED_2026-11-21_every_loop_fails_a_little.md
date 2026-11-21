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

The registration was committed in `81297a4`, and the run came after it. The logs are
[`../every_loop_compute.log`](../every_loop_compute.log) and [`../every_loop.log`](../every_loop.log). Heights for all
348 672 curves of the rank-2 classes took 99 seconds, with no failures.

**Checks of the pipeline.**
- 42 fresh curves have a BSD quotient exactly 1/4 of their optimal partner's.
- Saturation at every prime up to 100 changed no generator, on either side.
- For all 42, the analytic order of Sha is 1 on the optimal curve and 4 on the fresh one
  ([`../every_loop_after.log`](../every_loop_after.log)). So the quotient is a change of Sha across the isogeny, not a
  fault in the generators.
- 0.06% of the fresh curves were flagged and none failed, so the round is not void.

| | n | above 2 | above 5 | q (bootstrap s.e.) | strict | graded |
|---|---|---|---|---|---|---|
| **fresh curves** (L1, L2) | 69 616 | 0.1267 | 72 | 0.0082 (0.0010) | **miss** | **pass**, 19.7 s.e. |
| **optimal hidden-loop curves** (L3) | 5 481 | 0.1352 | 5 | 0.0068 (0.0031) | **miss** | **pass**, 8.5 s.e. |
| optimal curves with no loop (the reference) | 223 050 | 0.2244 | 1 697 | 0.0339 (0.0008) | | |
| optimal curves with torsion (seen, not scored) | 50 525 | 0.0938 | 3 | 0.0006 | | |

- **L1 misses.** 72 fresh curves fail badly, with elongations from 5.006 to 9.416.
- **L2 passes.** A fresh lattice that fails is about a quarter as likely to fail badly as one with no loop.
- **L3:** the strict form misses (5 curves above 5), and the graded form passes.
- **The rival died.** Its first half held, since L1 missed by 72 curves. Its second half did not: L2 passed.
- **Seen, not scored:** 3 optimal curves with torsion lie above 5.

**Two of four criteria held: the strict sentence died, and its graded form held.** No group of curves with a loop
avoids the bad tail entirely. But a lattice with a loop that fails is far less likely to fail badly.

## Read after the run (not registered; [`../every_loop_after.py`](../every_loop_after.py))

- **Where loops fail badly: a round partner, stretched.**
  - 63 of the 72 fresh curves above 5 have exactly n times the elongation of their optimal partner: n = 2 for 13
    curves, 3 for 34 and 5 for 16. Their partners are round, with elongations from 1.0 to 3.2.
  - 3 more share their partner's shape exactly, because their partners are themselves above 5.
  - The other 6 are neighbours of index 7 or 9, or of none up to 16, and are not exact multiples.
  - The 63 lie in classes of two curves. Such a class is joined by one isogeny of prime degree ℓ, and then the index
    between the two lattices is 1 or ℓ. So n is the isogeny's degree, and the stretch is the neighbour τ ↦ ℓτ of the
    rival's argument.
- **The graded pass comes from rational torsion.**
  - The fresh curves with no rational torsion number 7 970. A 2-isogeny's kernel is a rational point, so these
    carry only isogenies of odd degree. They have q = 0.0360 ± 0.0046, no lower than with no loop (−0.5 s.e.), and
    they hold 59 of the 72.
  - Fresh curves with torsion have q = 0.0018 (+32.7 s.e.), and optimal curves with any loop have q = 0.0015
    (+33.4 s.e.).
  - The optimal hidden-loop curves (L3) are protected, but their stretched partners are not.
- **No optimal curve with a loop fails very badly.**
  - All 63 optimal curves above elongation 8 have no loop.
  - The thinnest optimal curve with a loop is 364560fd1, at 6.19. The thinnest with no loop is at 13.17.
  - Eight optimal curves with a loop lie above 5: five torsion-free, and three with ℤ/2.
- **The fresh curve is more often the thinner member of its pair.** Among fresh curves related to their partner by
  index 2, 3 or 5, the fresh curve is the thinner one in 56%, 61% and 63% of pairs. Nothing registered tested this,
  and its cause is not known here.
- **Across conductor bands,** q stays between 0.007 and 0.011 for the fresh curves, against 0.033–0.035 with no loop.

## What this changes

- **"None fails badly" is false as stated.** 80 curves with a loop (72 fresh, 5 hidden-loop optimal and 3 with
  torsion) pack below a fifth of the honeycomb. It goes to the graveyard with this evidence.
- **What survives is the graded form, with a mechanism for its exceptions.**
  - A rational torsion point protects a lattice from failing badly. Given that the lattice fails, the protection is
    about 20 to 1 against curves with no loop.
  - An isogeny alone does not protect the non-optimal curve, whose lattice is often its round partner's stretched by
    the isogeny's degree.
- **Possible next rounds, if the author wants them:**
  - register that the stretch factor is the isogeny's degree in classes of three or more curves (PARI's `ellisomat`
    gives the degrees);
  - register whether optimality picks the rounder member of a pair.
