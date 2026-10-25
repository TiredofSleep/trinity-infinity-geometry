# Robustness: forced zeros survive, bought zeros split (pre-registration, 2026-10-24 23:50, before any run)

**The design rule under test.** A zero is exactly as robust as what pays for it:
- **paid for by a count** (sublattice imbalance; missing perfect pairing; too few bars): survives any
  perturbation that keeps the count;
- **paid for by a symmetry:** survives perturbations that keep the symmetry, and splits under the rest;
- **bought** (equal values, special geometry): splits under any generic perturbation, at first order.

**Systems.** Hueckel (tight-binding) carbon graphs, with exact zero counts by integer rank:
- [3]triangulene, C22, imbalance 2;
- a balanced phenalenyl dimer joined minority-to-minority (13/13). Two zero modes, paid for by a missing
  pairing: Clar's-goblet mechanism;
- cyclobutadiene C4 and [12]annulene C12, each with two zero modes bought by ring symmetry;
- 2D frames from applications/A3: the mirror frame (symmetry-paid) and an under-braced frame (count-paid).

**Perturbations.**
- **Bond disorder:** each bond's strength becomes 1 + delta * u, u uniform on [-1, 1]. Bipartite (chiral)
  structure is kept.
- **On-site disorder:** each atom gets energy delta * u. Chiral symmetry is broken.
- **Frames:** joint positions are moved by delta * (random unit vector), either mirror-symmetrically or
  generically.
- delta takes 8 values from 1e-4 to 1e-1; 50 trials each.

| id | kind | prediction | kill condition |
|---|---|---|---|
| R1 | translation | Bond disorder: triangulene and the balanced dimer keep exactly 2 zero modes in every trial (integer-free check: the 2 smallest \|E\| < 1e-10 while the 3rd > 1e-6) | Any trial losing them |
| R2 | real | Bond disorder: the bought modes of C4 and C12 split linearly; the median log-log slope of the smallest \|E\| against delta is in [0.8, 1.2] for each | Slope outside |
| R3 | real | On-site disorder splits even the count-paid modes of triangulene linearly: median slope in [0.8, 1.2] | Slope outside |
| R4 | translation | Frames: the count-paid mechanism survives any geometric perturbation (rank stays below 2j - 3); the symmetry-paid mechanism survives symmetric perturbations and vanishes under generic ones | Any exception |
| R5 | real | The symmetry-paid frame mechanism stiffens linearly under symmetry breaking: the median slope of sigma_min(R) against delta is in [0.8, 1.2] | Slope outside |
| R6 | translation | Chemistry check against the literature: the same audit labels cyclobutadiene's two zero modes "bought" (Jahn-Teller distortion lifts them) and Clar's-goblet-type modes "paid for" (robust to such distortions; Ortiz et al., arXiv:1906.08544) | The audit labels them the other way |

## Scores (`run.log`; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| R1 | triangulene and the goblet-type dimer keep exactly 2 zero modes in all 400 bond-disorder trials each | **held** |
| R2 | bought modes split linearly: slope C4 0.96, C12 1.00 | **held** |
| R3 | on-site disorder splits triangulene's count-paid modes linearly: slope 1.00 | **held** |
| R4 | count-paid frame mechanism survives every perturbation; symmetry-paid survives symmetric ones only | **held** |
| R5 | symmetry-paid mechanism stiffens linearly when the mirror breaks: slope 0.99 | **held** |
| R6 | the audit labels cyclobutadiene's modes bought (2) and the goblet-type modes paid by pairing (2), matching the literature | **held** |

**Tally:** 3 of 3 real (R2, R3, R5). Running record: **44 of 71**.
