# Registered before data: does the thinning continue? (round 2)

Written 2026-11-20, about 20:25 US Central, before any curve of conductor above 299 999 was downloaded.

**Prediction (Brayden, 20:21):** "It keeps getting more rare."

**Operational form (Claude).** Share of rank-2 optimal curves with elongation > 2, by band so far:
0.2430, 0.2324, 0.2175, 0.2124, 0.2040, 0.1980 at median log-conductors near 8.5, 9.9, 10.7, 11.3, 11.9, 12.4.
A straight line in log conductor has slope about −0.0115 per e-fold; a power law has exponent about −0.053.
Both forms predict, to within noise:

- 300 000–399 999: **0.193** (pass if between 0.188 and 0.198 and below 0.1980)
- 400 000–499 999: **0.190** (pass if below the 300 000–399 999 value, or within one standard error of it)

**Miss:** either band at or above 0.1980.
**Stated limit of this round:** the two forms cannot be told apart in this range, so this round cannot say
whether the share goes to zero. It only tests continued decline at the fitted rate.

**Also recorded, no prediction:** the share above 5 (flat at 0.006–0.007 so far), and for the curves above 5
whether the short side is unusually short or the long side unusually long relative to their band
(Brayden, on the tail: "same thing, intrinsic vs extrinsic").

---

# Outcome (`scripts/thin_triangles_round2.py`)

Fresh data: 119 362 rank-2 optimal curves, conductors 300 000–499 999 (registration 20:22 CST; data 20:26).

| band | n | share elongation > 2 | s.e. | predicted |
|---|---|---|---|---|
| 300 000–399 999 | 59 814 | **0.1922** | 0.0016 | 0.193 (window 0.188–0.198) |
| 400 000–499 999 | 59 548 | **0.1870** | 0.0016 | 0.190, below the previous band |

Both **pass**. Across all eight bands the share falls monotonically: 0.2430, 0.2324, 0.2175, 0.2124, 0.2040,
0.1980, 0.1922, 0.1870. The share above 5 is 0.0057 and 0.0058 (earlier bands 0.0046–0.0072).

# Not registered: what the same data showed when split by torsion

Total sample 279 056 curves (conductor 389–499 999). The tables are now used up to their end, so none of
this can be tested on fresh Cremona data; it needs another source (LMFDB above 500 000, or the
Stein–Watkins tables) and a registration first.

| torsion | n | share elongation > 2 | median elongation |
|---|---|---|---|
| trivial | 228 531 | 0.2222 | 1.411 |
| ℤ/2 | 46 462 | 0.0982 | 1.268 |
| ℤ/3 | 2 779 | 0.0583 | 1.235 |
| ℤ/4 | 800 | 0.0175 | 1.163 |
| ℤ/2 × ℤ/2 | 312 | 0.0032 | 1.153 |

- More torsion, rounder lattice, in order.
- **The registered trend lives entirely in the torsion-free curves:** 0.2735, 0.2621, 0.2444, 0.2384, 0.2275,
  0.2212, 0.2133, 0.2092 by band. Among curves with torsion the share is flat near 0.09–0.10 in every band.
  The torsion mix is steady (15.5% in the first band, 17.6–18.3% after), so the trend is not a change of mix.
- The thinnest lattices (elongation > 5) are thin at both ends: short side 0.13× its band's median, long
  side about 2×. The merely thin (2 to 5) are 0.44× and 1.36×. Same mechanism, further along.
- The shortest side grows with conductor at every quantile (median 0.40 → 0.95; first percentile 0.078 →
  0.134).

**Candidate mundane explanation to test first:** torsion raises the floor on the height of a
non-torsion point (points of very small height come from small integral points, and translation by torsion
constrains those). A higher floor means fewer very short sides and so rounder lattices. If the shape
distribution, conditioned on the shortest side measured against that floor, no longer depends on torsion,
this is a restatement of known height bounds (Hindry–Silverman and successors) and should be filed as such.
