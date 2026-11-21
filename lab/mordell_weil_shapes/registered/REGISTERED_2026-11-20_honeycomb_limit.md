# Registered prediction: the honeycomb limit

**Prediction (Brayden, 2026-11-20, 20:52 CST):** "As the honeycomb fractals it extends towards infinitely
better but never reaches 91."

**Operational form (Claude).** For torsion-free rank-2 optimal curves ordered by conductor:
- **H1 (keeps improving):** mean packing density keeps rising in every new band above 500 000.
- **H2 (the limit is the honeycomb):** the mean tends to π/(2√3) = 0.9069. Because no lattice exceeds that
  value, H2 requires the whole distribution to collapse onto the hexagonal shape: the share of lattices with
  density above 0.85 must rise toward 1 and the mean of x must rise toward ½.
- **Rival:** the mean levels off well below 0.9069 (the lower tail thins out, the top does not move).

**What existing data already say (computed after the prediction was made, on data already in hand, so this
is a diagnostic and not a test; `scripts/honeycomb_limit.py`).** Torsion-free curves, eight conductor bands
from 10³ to 5 × 10⁵:

| percentile of density | first band | last band | change |
|---|---|---|---|
| 10th | 0.268 | 0.305 | +0.036 |
| 25th | 0.380 | 0.419 | +0.039 |
| 50th | 0.531 | 0.564 | +0.033 |
| 75th | 0.683 | 0.695 | +0.012 |
| 90th | 0.762 | 0.771 | +0.009 |

- Share with density above 0.85: 0.9% to 1.1% in every band from 10⁴ up, no trend. Above 0.89: 0.05–0.09%.
- Mean of x: 0.2685 falling to 0.2612. It is moving away from ½, toward rectangular shapes.
- The mean rises 0.0082 per e-fold of conductor. A straight line reaches 0.9069 near conductor 10²⁵.
- Saturating fits with any limit from 0.60 to 0.9069 fit equally well (rms residual 0.0004). **The data
  cannot choose the limit.**

**Reading.** H1 is supported. H2 is not: the improvement comes from bad packings becoming rarer, while the
best packings are no more common and the shapes are not drifting toward hexagonal. That is what a rising
floor on the shortest vector would produce. Claude's stated expectation is the rival; Brayden's is H2.

**To test on fresh data (LMFDB above 500 000, or Stein–Watkins), registered in advance:**
1. mean density above 0.550 in the first new band (H1);
2. share above 0.85 significantly above 1.1%, and mean x above 0.2612 (H2). If both stay flat or fall while
   the mean rises, H2 is refuted in this range and the rival stands.

**Extension to register separately:** rank 3. The densest lattice packing there is the face-centred cubic,
density 0.7405. Cremona's tables hold the rank-3 curves below 500 000; compute their mean density against
the uniform null on the space of 3-dimensional shapes before looking at trends.
