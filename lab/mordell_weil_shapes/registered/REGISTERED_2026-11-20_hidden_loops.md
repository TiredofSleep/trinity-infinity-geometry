# Registered before looking: hidden loops

Written 2026-11-20, about 21:20 US Central. The split below has not been computed on any data.

**Statement (Brayden, 21:16):** "Angles don't pack, only curves that can loop."

**Reading (Claude).** A point of infinite order is an angle that never closes. A torsion point is a loop.
The torsion table already shows more loops, better packing. But a curve can carry a loop that is not a
rational point: a rational isogeny is a finite cyclic subgroup that is defined over ℚ as a set although
its points are not rational. A curve has one exactly when its isogeny class has more than one curve.

**Prediction.** Among rank-2 optimal curves with **trivial torsion**, those whose isogeny class has size ≥ 2
have higher mean packing density than those whose class has size 1.

**Pass:** difference positive and more than two standard errors. **Miss:** zero or negative.
**Secondary, recorded:** ordering by class size (1, 2, 3+); the conductor trend within each group.
**Mundane reading to test afterwards if it passes:** a rational ℓ-isogeny means ℓ-torsion over a small
extension field, which may raise the height floor the same way rational torsion does.

---

# Outcome (`scripts/hidden_loops.py`; registration 21:17 CST, computed after)

Torsion-free rank-2 optimal curves, conductor below 500 000:

| isogeny class size | n | mean density | thin share (elongation > 2) |
|---|---|---|---|
| 1 (no rational isogeny) | 223 050 | 0.5434 | 22.4% |
| 2 | 5 186 | 0.5842 | 13.4% |
| 3 | 284 | 0.5717 | 16.2% |
| 4 or more | 11 | 0.5926 | 0% |
| **≥ 2 together** | 5 481 | **0.5835** | |

Difference 0.0401, standard error 0.0021: **pass, 18.7 standard errors.** The secondary ordering (2 against
3) is not monotone; class size 3 has only 284 curves.

**Not predicted.** By conductor band, mean density:
- class size 1: 0.5215, 0.5236, 0.5304, 0.5360, 0.5404, 0.5446, 0.5482, 0.5494 (rising)
- class size ≥ 2: 0.5812, 0.5687, 0.5942, 0.5833, 0.5842, 0.5838, 0.5867, 0.5786 (flat)

So the pattern seen for rational torsion repeats for hidden loops: curves with any loop sit at a higher
density that does not change with conductor, and the whole conductor trend belongs to curves with no loop
of either kind. For comparison, curves with rational torsion sit at 0.60–0.63.

**Open, unregistered:** whether the loop-free curves are rising toward the loop-bearing level (about
0.58–0.60) rather than toward 0.9069. Saturating fits could not separate limits between 0.60 and 0.9069.

**Finer loops to register next.** The degree of the isogeny (compute with `ellisomat`); the image of Galois
on 2-torsion and 3-torsion for curves with no rational isogeny (for example, whether the discriminant is a
square, which makes the 2-torsion field cyclic); torsion gained over quadratic fields. Each is a smaller
"loop" by this reading, and each predicts a smaller density gain. If density tracks the size of the mod-ℓ
image across all of these, the whole effect may be one known mechanism (small-height points are scarcer when
torsion appears in small fields), and should be written up as that.
