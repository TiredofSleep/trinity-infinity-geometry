# Registered before looking: "the curve of the curve"

Written 2026-11-20, about 22:47 US Central. Neither split below has been computed on any data.

**Statement (Brayden, 22:43):** "If an area is definable but infinitely measurable, it is the same as
infinitely immeasurable. So the amount of the curve, the curve of the curve shows why it pools."
Earlier (21:16): "Angles don't pack, only curves that can loop."

**Two readings (Claude), each of the curve's own geometry rather than of its points.**

*Reading A, the real loop.* Over the real numbers a curve y² = cubic has either one piece or two. It has two
exactly when its discriminant is positive, and the second piece is a closed loop (the "egg"). A curve
"that can loop", literally.
- **A1.** Among loop-free curves in the arithmetic sense (trivial torsion, isogeny class of size 1),
  curves with positive discriminant have higher mean packing density than curves with negative discriminant.
  Pass: positive difference above three standard errors. Miss: zero or negative.

*Reading B, the curve's own shape.* Every curve is itself a torus with a shape: its period lattice, a point
τ on the same modular surface where the Mordell–Weil shapes live. "The curve of the curve."
- **B1.** Within each discriminant sign, the Mordell–Weil packing density is correlated with the elongation
  Im τ of the curve's own period lattice. No direction was stated, so the test is two-sided: |Spearman|
  above five standard errors (about 0.011 for 200 000 curves). Miss: smaller than that.
- **B2 (recorded, no prediction):** whether the conductor trend differs by discriminant sign; whether the
  pooling density near 0.61 corresponds to the uniform measure on the modular surface cut off at some
  elongation.

**Mundane expectations, stated now.** Canonical heights have an archimedean part computed from the real
period lattice, and a point on the egg has a different local height from a point on the unbounded piece. So
some dependence of the height pairing on both A and B would not be surprising. What would be worth
reporting is its size and direction.

---

# Outcome (`scripts/periods.py`, `scripts/curve_of_curve.py`; registered 22:44 CST, computed after)

All 279 056 curves. Check on the pipeline: the reduced τ has real part 0 for every curve with positive
discriminant, as it must.

**A1, the real loop: pass, small.** Loop-free curves (trivial torsion, class size 1):

| | n | mean density | thin share |
|---|---|---|---|
| positive discriminant (has the egg) | 75 482 | 0.5474 | 21.3% |
| negative discriminant | 147 568 | 0.5414 | 23.0% |

Difference +0.0061, 7.8 standard errors. In the groups that already have an arithmetic loop the sign makes
no visible difference (isogeny-only 0.5829 / 0.5838; ℤ/2 0.6022 / 0.6040; ℤ/3 0.6245 / 0.6220).

**B1, the curve's own shape: pass, large.** Loop-free curves, Spearman correlation of Mordell–Weil packing
density with Im τ of the curve's period lattice:

| | n | Spearman | density by fifths of Im τ (round → elongated) |
|---|---|---|---|
| positive discriminant | 75 482 | −0.128 (35 s.e.) | 0.573, 0.564, 0.555, 0.536, 0.509 |
| negative discriminant | 147 568 | −0.032 (12 s.e.) | 0.546, 0.543, 0.547, 0.548, 0.523 |

The rounder the curve's own torus, the better its points pack. For positive discriminant the spread between
the extreme fifths (0.064) is more than twice the whole conductor trend over the tables (0.028).

**B2, recorded.** Conductor slope: +0.0067 (positive discriminant) and +0.0087 (negative); the share of
positive discriminant is steady at about 34% from 10⁴ up, so sign does not drive the trend.
The uniform measure on the modular surface cut off at elongation Y has mean density 0.675, 0.609, 0.569,
0.543 for Y = 1.5, 2, 2.5, 3. The pooling density estimated earlier, 0.614 (95% range 0.602–0.634),
matches a cutoff near Y = 2. That is one free parameter fitted to one number: a coincidence until a cutoff
of 2 is derived from something or the *whole* shape distribution of a group near the pooling level is shown
to match the cut-off uniform one. Register that comparison before making it.

**Not yet excluded.** Im τ is large when the curve is close to degenerate, which goes with a large
discriminant for its conductor. B1 may therefore be partly a relation between discriminant size and
heights. Next: repeat B1 within narrow bands of conductor and of log|Δ|, and against the Faltings height.
Canonical heights include an archimedean term built from the period lattice, so some dependence is expected
on general grounds; the question for the literature is whether its size and sign are known.
