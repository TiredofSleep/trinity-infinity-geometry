# Registered before data: thin triangles and conductor

Written 2026-11-20, about 19:55 US Central, before any curve of conductor above 99 999 was downloaded.

**Prediction (Brayden, 19:51):** "Larger numbers make a long thin triangle less and less likely."

**Operational form (Claude):** among rank-2 optimal curves in Cremona's tables,
1. the share with elongation > 2 in the band 100 000–199 999 is below the 60 000–99 999 value, 0.212;
2. the share in 200 000–299 999 is below the share in 100 000–199 999;
3. the Spearman correlation of elongation with conductor over 100 000–299 999 is negative.

**Noise:** about 50 000 curves per band gives a standard error near 0.002 on a share.
**Miss:** share in 100 000–199 999 at or above 0.212, or (2) reversed by more than two standard errors.
**Known in advance:** the four bands below 100 000 already run 0.243, 0.232, 0.217, 0.212, and Brayden had
seen the falling medians. So this tests whether the trend continues, not whether it exists.
**Also recorded, no prediction made:** share with elongation > 5; median elongation; the size-only model's
share for each band (does the fall come only from the two sides growing more alike?).

---

# Outcome (same evening; `scripts/thin_triangles_registered_test.py`)

Fresh data: 114 198 rank-2 optimal curves, conductors 100 000–299 999, downloaded after the text above was
written (file timestamp 19:52 CST; data computed 19:56).

| band | n | share elongation > 2 | s.e. | share > 5 | median | size-only model, share > 2 |
|---|---|---|---|---|---|---|
| 1 000–9 999 | 1 951 | 0.2430 | 0.0097 | 0.0046 | 1.432 | 0.197 |
| 10 000–29 999 | 7 673 | 0.2324 | 0.0048 | 0.0069 | 1.430 | 0.203 |
| 30 000–59 999 | 14 370 | 0.2175 | 0.0034 | 0.0072 | 1.411 | 0.206 |
| 60 000–99 999 | 21 484 | 0.2124 | 0.0028 | 0.0068 | 1.391 | 0.204 |
| **100 000–199 999** | 55 813 | **0.2040** | 0.0017 | 0.0062 | 1.383 | 0.208 |
| **200 000–299 999** | 58 385 | **0.1980** | 0.0016 | 0.0062 | 1.371 | 0.206 |

1. 0.2040 < 0.212: **pass**, by about five standard errors.
2. 0.1980 < 0.2040: **pass**, by about 2.6 standard errors of the difference.
3. Spearman, fresh data only: −0.0134 (p = 6 × 10⁻⁶): **pass**.

**Not predicted, and the more interesting result.** The size-only model stays flat (0.197 to 0.208) while
the data fall from 0.243 to 0.198 and cross below it. So the trend is not produced by the two sides growing
more alike: the spread of the shortest side actually widens (sd of its log 0.66 → 0.76). The share above 5
shows no trend (0.006–0.007 throughout).

**Limits.** The effect is small: four points of share over two and a half decades of conductor. The
size-only model is crude and partly circular. Where the share is heading (a positive limit, or zero) is not
determined by this range. Possible mundane causes not yet excluded: the choice of optimal curve in each
isogeny class; ordering by conductor rather than height; how the tables' generators were reduced (shape is
basis-independent, so this last should not matter, but check).
