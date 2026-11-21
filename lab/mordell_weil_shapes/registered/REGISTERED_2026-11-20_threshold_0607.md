# Registered before looking: a threshold at 0.607

Written 2026-11-20, about 21:25 US Central.

**Statement (Brayden, 21:21):** ".607 is a transition point in dynamic space, so yes grows log towards that
threshold, but if achieved beyond, growth toward the honeycomb limit."

**Provenance, recorded honestly.** The number was named after Brayden had been told that curves with loops
sit at "0.58 to 0.60" and (earlier the same day) that a different quantity has average slope "about 0.61".
Two familiar constants are near it: e^(−1/2) = 0.60653 and 6/π² = 0.60793. Which is meant has not been
said, and they differ by 0.0014, less than this data can resolve. A constant chosen after seeing nearby
values is a hypothesis to test, not a finding.

**Operational form (Claude).**
- **T1 (below the threshold: approach, no crossing).** Loop-free curves rise toward 0.607 and level off
  there. Not testable in this range: fits with limits from 0.60 to 0.9069 are indistinguishable.
- **T2 (above the threshold: growth).** Groups whose mean density is already above 0.607, namely the
  torsion classes ℤ/3, ℤ/4, ℤ/6 and ℤ/2 × ℤ/2 (pooled, about 4 000 curves), show density **rising** with
  conductor. Test: least-squares slope of density on ln(conductor) is positive by more than two standard
  errors.
- **T3 (just below: flat).** ℤ/2 (mean 0.603) and isogeny-only curves (0.584) have slope not
  distinguishable from zero, and smaller than the loop-free slope of about 0.008 per e-fold.

**Already known, so not a test:** thin share for all torsion curves together is flat by band (dominated
by ℤ/2); isogeny-only means are flat by band.
**Power warning:** with about 4 000 curves the slope's standard error will be near 0.003–0.004, so a true
slope of 0.008 would be detected at only about two standard errors. A null result here is weak evidence.
**Miss for T2:** slope zero or negative.

---

# Outcome (`scripts/threshold_0607.py`; registered 21:22 CST, computed after)

Slope of packing density against ln(conductor), by group:

| group | n | mean density | slope per e-fold | s.e. | slope ÷ s.e. |
|---|---|---|---|---|---|
| no loop at all | 223 050 | 0.5434 | +0.00800 | 0.00045 | +17.7 |
| isogeny only | 5 481 | 0.5835 | −0.00128 | 0.00246 | −0.5 |
| ℤ/2 | 46 462 | 0.6028 | +0.00223 | 0.00085 | +2.6 |
| ℤ/3 | 2 779 | 0.6228 | −0.00296 | 0.00289 | −1.0 |
| ℤ/4 | 800 | 0.6592 | −0.00863 | 0.00460 | −1.9 |
| ℤ/2 × ℤ/2 | 312 | 0.6700 | −0.00933 | 0.00774 | −1.2 |
| **all above 0.607, pooled** | 4 063 | 0.6363 | **−0.00495** | 0.00229 | **−2.2** |

- **T2: miss.** Groups above 0.607 are not rising toward the honeycomb. Their pooled slope is negative, by
  2.2 standard errors. "If achieved beyond, growth toward the honeycomb limit" is not supported and is
  contradicted at the two-sigma level.
- **T3: mixed.** Isogeny-only is flat as stated. ℤ/2 is not flat: it rises, slowly (2.6 standard errors),
  at about a quarter of the loop-free rate.
- **T1: untested**, as registered.
- The density histogram of loop-free curves is smooth through 0.607: no feature there.

# Not registered: what the slopes look like together

Low groups rise, high groups fall. A weighted straight line through the six (level, slope) points has
slope −0.113 and crosses zero at density **0.614** (68% range 0.607 to 0.623; 95% range 0.602 to 0.634).
No group misses the line by more than 1.9 standard errors.

So the data are consistent with every group drifting toward one common density a little above 0.6, from
both sides: a fixed point, not a threshold. Brayden's 0.607 lies at the edge of the 68% range; so do
e^(−1/2) and 6/π². The range is far too wide to pick out any constant, and this reading was formed after
seeing the slopes. It is the thing to register next, on fresh data:
1. curves below the crossing rise and curves above it fall, in a new sample;
2. the crossing estimated from the new sample alone lies in 0.602–0.634;
3. as a guard against regression to the mean being built in: the groups are defined by torsion and isogeny,
   not by density, so selection on the outcome is not the cause, but check by simulation that a common
   noise model does not manufacture the pattern.
