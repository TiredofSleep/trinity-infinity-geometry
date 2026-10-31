# kernel_ledger: pre-registration (2026-10-24, written before `ledger_tests.py` ran)

Rules as in the other folders: predictions are never edited; scores are appended; *translation* = forced by a
known theorem or derivation; *real* = a guess that can lose.

| id | domain | kind | prediction | kill condition |
|---|---|---|---|---|
| K1 | molecules | translation | 300 random benzenoids (4-12 hexagons): nullity of the adjacency = n - 2nu (Level 2 exact; Fajtlowicz-John-Sachs). | Any mismatch. |
| K2a | molecules | real | Site-diluted square-lattice clusters (300; >= 12 sites): unweighted nullity exceeds n - 2nu in at least 5% of clusters. That is a Level 3 residue; on a square lattice it comes from 4-cycles. | Excess in fewer than 5%. |
| K2b | molecules | translation | With random integer weights (1..10^6) on the same bonds, nullity = n - 2nu in every cluster: the residue is value-forced and disappears. | Any cluster with excess. |
| K3a | Fourier | real | Every singular square minor of DFT_9 has a single-subgroup coset certificate (definition in `ledger_tests.py`, recursive on the quotient), in rows-to-columns or columns-to-rows form. | An uncertified singular minor. |
| K3b | Fourier | real | The same at n = 8. | An uncertified singular minor. |
| K3c | Fourier | real | At n = 6 or n = 10, which have two incomparable subgroups, some singular minor has **no** single-subgroup certificate: mixed-subgroup cancellations exist. | All certified at both. |
| K4a | frameworks | translation | 300 random mirror-symmetric 2D frameworks: j = 2m joints (m = 3..5 mirror pairs), b = 2j - 3 bars, b_sigma in {1, 3, 5} cross bars. There are at least (b_sigma - 1)/2 antisymmetric mechanisms (Level 1, Fowler-Guest). | Fewer. |
| K4b | frameworks | real | Among those whose graph is generically rigid (rank 2j - 3 in a random asymmetric realization), the symmetric realization has **exactly** (b_sigma - 1)/2 mechanisms in at least 90%. | Below 90%. |
| K5a | magic squares | real | Natural 6x6 squares (C annealer, 5 CPU-min): singular fraction below order 5's 0.19%. | 0.19% or more. |
| K5b | magic squares | real | Among the singular 6x6 squares, the share with no void certificate (no factorised complement map of index >= 1, no constant-sum line subset) exceeds order 5's 5/19 = 26%. | 26% or less, or fewer than 5 singular squares (then unscored). |

## Scores (`run.log`; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| K1 | 300 benzenoids: nullity = n - 2nu in all (nullities 0: 124, 1: 154, 2: 22) | **held** |
| K2a | unweighted excess over n - 2nu in 131 of 300 clusters (43.7%) | **held** |
| K2b | random integer weights: nullity = n - 2nu in all 300 | **held** |
| K3a | DFT_9: 3,420 singular minors, **2,066 without** a single-subgroup coset certificate. Example: rows {0,3}, columns {0,3}, where the rows sit inside a subgroup and two columns alias. | **lost** |
| K3b | DFT_8: 1,396 singular, 585 uncertified | **lost** |
| K3c | uncertified singular minors at n = 6 (46 of 120) and 10 (10,068 of 20,480) | **held as registered, but uninformative**: the certificate was too narrow (K3a and K3b lost), so this says nothing about mixed subgroups |
| K4a | 300 symmetric frameworks: antisymmetric mechanisms >= (b_sigma - 1)/2 always | **held** |
| K4b | 167 generically rigid graphs: exactly the forced count in 164 (98.2%) | **held** |
| K5a | 2,851 distinct order-6 squares: **0 singular** (order 5: 0.19%) | **held** |
| K5b | fewer than 5 singular squares | **unscored** |

**Tally:** 4 of 6 scored real predictions held. Running record (all folders): **33 of 55**.

**What K3 got wrong.** I registered only one mechanism: support on full cosets of a subgroup H. The dominant
mechanism is the dual one, *aliasing*: if the rows lie in a coset of a subgroup K, then columns in the same
class mod the annihilator K-perp become proportional.

## Round K3' (post hoc exploration first, then a fresh registered test)
**Exploration on the same data (n = 6, 8, 9, 10), labelled post hoc.** A product bound (cosets of K meeting R,
times classes of K-perp meeting C, < |R|) plus the coset-support certificate still leaves 10-47% of the
singular minors uncovered.
- **Class pigeonhole:** a subgroup K and one class b of K-perp with |C cap (b + K-perp)| > #(cosets of K meeting R).
  It is sound by construction (`fourier_certs.py`).
- It covers 120/120 at n = 6, 1,268/1,396 at n = 8, 3,339/3,420 at n = 9 and 19,680/20,480 at n = 10.
  The remainder needs two levels of the subgroup chain: the Cooley-Tukey factorization applied twice.

**Fresh test (written before running; n = 12 and n = 16 were not looked at):**
| id | kind | prediction | kill condition |
|---|---|---|---|
| F1 | translation | Class-pigeonhole certificates are sound: every certified minor is singular. Exhaustive at n = 12; 300,000 random minors at n = 16. | Any certified nonsingular minor. |
| F2 | real | Class pigeonhole covers at least 85% of singular minors at n = 12 (exhaustive) and at n = 16 (sampled). | Below 85% at either. |
| F3 | translation | n = 11 and 13 (prime): no singular minor in 300,000 random minors each (Chebotarev). | Any. |

### Round K3': measurement history (predictions F1-F3 unchanged)
- **Run 1** (`fourier_fresh_firstrun.log`) decided singularity by |det| < 1e-7. It flagged 72 certified minors
  at n = 16 as nonsingular. All 72 were 14x14 minors with |det| about 1.5e-7, and SVD showed them rank-deficient.
  An absolute threshold is wrong at the Hadamard scale 14^7 ~ 1e8.
- **Run 2** (`fourier_fresh_secondrun.log`) used numpy's default `matrix_rank`. It disagreed with an exact recheck
  4,349 times at n = 12 and 2,000 at n = 16, always on certified minors that exact arithmetic says are singular.
  The default SVD tolerance (max(M,N) * eps * sigma_max) is too strict for these.
- **Run 3** (`fourier_fresh.log`) is the scored run. Every certified minor, and every minor with
  sigma_min / sigma_max < 1e-5, is decided exactly: determinant mod two primes p = 1 mod n, via the ring map
  Z[zeta_n] -> F_p. Every other minor is nonsingular. A container restart killed the first attempt at run 3;
  it was rerun as two parallel halves with the same code.

### Round K3' scores (run 3, exact)
| id | result | outcome |
|---|---|---|
| F1 | 0 unsound certificates: all 424,696 certified minors at n = 12 and 23,263 at n = 16 are exactly singular | **held** |
| F2 | class pigeonhole covers 88.9% of the 477,688 singular minors at n = 12 (exhaustive) and 86.7% of 26,827 at n = 16 (sampled) | **held** |
| F3 | n = 11, 13: no singular minor among 300,000 each; none even below sigma ratio 1e-5 | **held** |

**Tally:** F2 held (1 of 1 real). Running record (all folders): **34 of 56**.

## Round K6: "4 seen as 5" (written 2026-10-24 22:45, before `four_in_five.py` ran)
**Prompt (from the user).** Order-5 kernels sit in the concentric and eccentric spheres around the cube's
motion: how can 4 be seen as 5?

**Geometry.** Centered at the void, an n x n magic square acts on the (n-1)-dimensional space orthogonal to 1.
There the n line positions are the vertices of a regular simplex.
- **n = 4:** the simplex is a tetrahedron inscribed in a cube. The forced kernels chi_01, chi_10 and chi_11 are
  the cube's three axes (each perpendicular to a pair of opposite tetrahedron edges), or combinations of them.
- **n = 5:** the simplex is a 4-simplex, which has no cube. A kernel vector perpendicular to the edge (a, b) has
  v_a = v_b: lines a and b enter merged, and the square acts like a 4-line system. A kernel vector inside the
  facet opposite a has v_a = 0: line a drops out.

**Seen so far (post hoc).** All 5 accidental squares from Round 8c have a primitive integer kernel vector, right
or left, with a repeated entry or a zero entry. All 14 complementary-pair squares do too, by construction.

| id | kind | prediction | kill condition |
|---|---|---|---|
| M0 | translation | Every one of the 640 singular 4x4 squares has a kernel vector with \|v_a\| = \|v_b\| for some a != b (a cube axis, or a sum of two). | Any exception. |
| M1 | real | In a **fresh** sample of singular natural 5x5 squares, every singular square has a primitive integer kernel vector (right or left) with a repeated entry (v_a = v_b) or a zero entry. Squares already seen in Round 8c are excluded. Fresh annealing: seeds 31-34, 150 CPU-s each. | Any fresh singular square with neither. Unscored if fewer than 10 fresh singular squares. |
| M2 | real | The rate in M1 is at least 3x a chance baseline: for each square, the probability that a random integer vector with the same entry range (max \|v_i\|) and zero sum has a repeat or a zero. Estimated by Monte Carlo and averaged over the sample, for right and left kernels combined. | Observed rate below 3x baseline. |
| M3 | real | Among the fresh **accidental** singular squares (no void certificate), the merge or drop property still holds for all, so 4-line reduction explains even the kernels that no symmetry forces. | An accidental fresh square without it. Unscored if fewer than 3 accidental. |

### Round K6 scores (`four_in_five.log`; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| M0 | all 640 singular 4x4 squares have a kernel vector with \|v_a\| = \|v_b\| (a cube axis or a sum of two) | **held** |
| M1 | 18,847 fresh squares, 28 singular: 3 of them have no repeated or zero kernel entry | **lost** |
| M2 | observed 0.89 vs a chance baseline of 0.845 (1.1x). Small-integer kernels repeat by pigeonhole. | **lost** |
| M3 | fresh accidental squares: 7 of 10 merge or drop, and their chance rates are 0.28-0.80 each | **lost** |

**Tally:** 0 of 3 real. Running record: **34 of 59**. "Merged or dropped lines" is not the mechanism; it is
small-number pigeonhole.

**What the fresh data did show (post hoc, labelled).** Two fresh accidental squares have tiny left kernels:
- (1, -1, -1, 1, 0): r0 + r3 = r1 + r2. Two row pairs share a midpoint that is *not* the center. This is the
  order-4 cube axis (1, -1, -1, 1) on four of the five rows.
- (0, 0, -2, 1, 1): row 2 is the midpoint of rows 3 and 4.

That fits the user's "concentric / eccentric" language exactly:
- **concentric:** a pair of lines whose midpoint *is* the void center (a complementary pair, the forced
  certificate);
- **eccentric:** two pairs of lines sharing an off-center midpoint, or one line at the midpoint of two others.

Each eccentric relation is itself a kernel vector, so it forces singularity. I had not tested this certificate
class.

## Round K7: eccentric certificates (written before `eccentric.py` ran, on a new sample)
**New sample:** seeds 41-44, 150 CPU-s each; squares seen in Round 8c or K6 are excluded.

| id | kind | prediction | kill condition |
|---|---|---|---|
| E1 | translation | Every square with an eccentric certificate (rows or columns: l_a + l_b = l_c + l_d, or 2 l_c = l_a + l_b) is singular. | A nonsingular one. |
| E2 | real | Eccentric certificates explain between 5% and 40% of the new sample's accidental singular squares (seen so far: 2 of 15, 13%). | Outside 5-40%. Unscored if fewer than 8 accidental. |
| E3 | real | Concentric + eccentric together still leave most accidental kernels unexplained: more than half have no certificate of either kind. | Half or fewer unexplained. |

### Round K7 scores (`eccentric.log`)
| id | result | outcome |
|---|---|---|
| E1 | 18,657 new squares: no nonsingular square has an eccentric certificate | **held** |
| E2 | 38 singular: 28 concentric (forced), 10 accidental, of which 2 eccentric (20%) | **held** |
| E3 | 8 of 10 accidental have no certificate of either kind (80%) | **held** |

**Tally:** 2 of 2 real. Running record: **36 of 61**.

**Order 5, all three samples (85 singular squares):**
- 60 concentric (71%): a pair of lines centered on the void;
- 4 eccentric (5%): two equal-weight pairs sharing an off-center midpoint, or a line at the midpoint of two
  others;
- 21 neither (25%).

**A definitional remark, not a finding.** Every kernel vector v of a magic square has sum 0. So the lines with
positive coefficients and the lines with negative coefficients have the same weighted barycenter: every kernel
is two clouds of lines sharing a center. Concentric means equal weights centered on the void. Eccentric means
equal weights centered elsewhere. The remaining 25% share a center only with unequal weights, e.g.
3 r0 + 2 r1 = 4 r2 + r3.

## Round K8: is the weighted quarter random? (written 2026-10-24 23:05, before `weighted.py` ran)
**Exploration on the 47,538 squares already seen (post hoc, labelled).**
- **Determinant lattice.** Every 5x5 det is a multiple of 325 = 5^2 * 13. Near zero, nonsingular dets land on
  highly divisible multiples (L = 60-240) at about 8 squares per lattice point. 0 is the most divisible point,
  so a "random lattice" model predicts roughly 8 accidental zeros. 21 weighted kernels were seen, about 2.5x
  that.
- **Digit layers.** Write M - 1 = 5A + B (base 5). Among nonsingular squares, 23.5% have a singular digit layer
  (A or B). Among weighted-singular squares it is 12 of 21 (57%), about 2.4x.

**Fresh sample:** seeds 61-68, 150 CPU-s each; squares seen in any earlier round are excluded.

| id | kind | prediction | kill condition |
|---|---|---|---|
| W1 | real | The weighted quarter is *not* pure arithmetic noise: #weighted-singular / (random-lattice estimate) >= 1.5. The estimate is fixed in advance: on the fresh nonsingular squares, the count of det/325 values with 0 < \|q\| <= 1000 and q divisible by 240, divided by (2 * 1000 / 240). | Ratio below 1.5. Unscored if fewer than 6 weighted. |
| W2 | real | Weighted-singular squares have a singular digit layer at least 1.5x as often as 2,000 random fresh nonsingular squares. | Below 1.5x. Unscored if fewer than 6 weighted. |
| W3 | real | Concentric squares are 60-80% of the fresh singular squares (seen so far: 71%). | Outside 60-80%. |

### Round K8 scores (`weighted.log`)
| id | result | outcome |
|---|---|---|
| W1 | 39,831 fresh squares, 76 singular (48 concentric, 3 eccentric, 25 weighted). Random-lattice estimate 8.16, so the ratio is **3.06** | **held** |
| W2 | singular digit layer in 48% of weighted vs 24.8% of nonsingular (1.94x) | **held** |
| W3 | concentric share 63% | **held** |

**Tally:** 3 of 3 real. Running record: **39 of 64**. The weighted quarter is not arithmetic noise: zero comes
up about 3x as often as an equally divisible nonzero determinant.

## Round K8b: a proved filter (derivation, then a translation check; written before `digit_filter.py` ran)
Write M = 5A + B + E, with E the all-ones matrix, A the high base-5 digits and B the low ones. If Mv = 0 then
sum(v) = 0, because every column sums to 65. So Ev = 0, Bv = -5Av, and Bv = 0 mod 5. A primitive integer v is not
0 mod 5, so **M singular => B singular mod 5**. Equivalently, if the low digit layer is invertible mod 5, the
square is invertible: infinite descent at the prime 5, the same engine as Round 8b.

| id | kind | prediction | kill condition |
|---|---|---|---|
| T1 | translation | Every singular square in all four 5x5 samples (161) has det(B) = 0 mod 5, and therefore none has an invertible B mod 5. | Any exception. |
| T2 | exploratory | P(singular \| B singular mod 5) and the share of squares with B singular mod 5. Not a prediction. | -- |

### Round K8b score (`digit_filter.log`)
| id | result | outcome |
|---|---|---|
| T1 | 87,369 distinct squares: no singular square has B invertible mod 5. But B is singular mod 5 in **100%** of squares. | **held but vacuous.** Every row of B sums to 0 mod 5, so the constant vector 1 is always in B's kernel mod 5. The void direction defeats the naive descent. |

**Refined picture (exploration on the same 87,369 squares; post hoc, needs a fresh test):**
- **rank over F5 of B:** 4 in 65,905 squares, 3 in 21,130, 2 in 334.
- **P(singular) by that rank:** 0.14% at rank 4, 0.27% at rank 3, **2.7%** at rank 2 (about 19x the base rate).
- **Kernels mod 5:** 126 of 161 singular kernels are congruent to a constant vector mod 5. Reduced mod 5, the
  kernel *is* the void direction.
- **The other 35** force rank_F5(B) <= 3, since the mod-5 kernel then contains 1 and v.

**Next, registered but not yet run:**
- **T3 (real):** on a fresh sample, P(singular | rank_F5(B) = 2) >= 10x the base rate.
- **T4 (translation):** every singular square whose kernel is not constant mod 5 has rank_F5(B) <= 3.
- **T5 (real):** the weighted kernels concentrate at rank_F5(B) <= 3 more than the concentric ones do.

## Round K9: running T3-T5 (amendment written before any sample was drawn, 2026-10-24 23:14)
**Sample:** seeds 71-78, 240 CPU-s each, from a C annealer. Squares seen in any earlier round are excluded.

**Scoring details added before running:**
- T3 is unscored if the sample has fewer than 100 squares with rank_F5(B) = 2.
- T5 compares the share of kernels with rank_F5(B) <= 3 among weighted vs concentric singular squares.
  It holds if weighted > concentric, and is unscored if there are fewer than 6 weighted.

**T6, added before the K9 sample finished annealing (no K9 data seen).**
Hypothesis: the weighted excess (W1) is 5-adic. Low-rank digit layers push det M toward high powers of 5, and 0 is
the most 5-divisible point. W1's estimator used L = 240, which has only one extra factor of 5.

| id | kind | prediction | kill condition |
|---|---|---|---|
| T6 | real | The lattice estimator recomputed with L = 48 * 5^3 = 6000 and T = 30,000 (ten multiples each side), on the K9 fresh sample, predicts at least 0.7x the observed number of weighted zeros. | Estimate below 0.7x observed. Unscored if fewer than 6 weighted. |
| T7 | real | Among nonsingular K9 squares, the mean 5-adic valuation of det/325 strictly increases as rank_F5(B) falls from 4 to 3 to 2. | Not strictly increasing. |

### Round K9 scores (`digit_rank.log`; 64,680 fresh squares, 103 singular)
| id | result | outcome |
|---|---|---|
| T3 | rank_F5(B) = 2: 3 of 215 singular (1.40%), **8.8x** base (needed 10x) | **lost** (narrowly; 3 events) |
| T4 | every kernel not constant mod 5 comes with rank_F5(B) <= 3 | **held** |
| T5 | share with rank_F5(B) <= 3: weighted 41% (9/22) vs concentric 41% (32/79) | **held as registered by 0.4 points: no real difference** |
| T6 | 5-adic lattice estimate with L = 6000: 1.80 vs 22 weighted zeros (0.08x) | **lost**. Partly a design flaw: a +-30,000 window is mostly tail when the median \|det/325\| is about 3,300, so a coarse lattice reads low. The question "is the excess 5-adic?" stays open. |
| T7 | mean 5-adic valuation of det/325: rank 4: 0.25, rank 3: 0.52, rank 2: 1.90 | **held** |

**Tally:** 2 of 4 real (T5 only nominally). Running record: **41 of 68**.

**Where the weighted quarter stands:**
- It is real structure (W1, 3x chance).
- Low digit rank mod 5 raises both the singular rate (about 9x at rank 2, 1.6x at rank 3) and the 5-adic
  divisibility of det (T7).
- Weighted kernels are *not* more digit-degenerate than concentric ones (T5).
- No properly scaled test yet says the excess is 5-adic. The next estimator should work per valuation class:
  write det/325 = 5^k u and estimate the density of u near 0 within each k.

## Round K10: a hidden quarter-turn symmetry behind the weighted quarter? (registered 2026-10-27 20:50 CT, before any K10 computation)
**Source:** the user, 2026-10-27 20:42 CT, verbatim: "3 times more than chance a 90 degree symmetry appears inside a cube?"
**Sample:** every distinct 5x5 square in squares5_annealed.txt and squares5_fresh{,2,3,4}.txt, deduplicated by `canon`.
These were all seen in earlier rounds, but no quarter-turn statistic was ever computed on them.
Classes as in K7/K8: concentric (`local_certs` or void index >= 1), eccentric (`eccentric`), weighted (neither).

**Measures:**
- q90(M) is the number of the 24 off-center cells with M[i][j] + M[4-j][i] = 26. That counts cells where turning the
  square a quarter-turn gives the complement.
- A lever match means the row kernel u (u^T M = 0) and the column kernel v (M v = 0) satisfy v || u or
  v || reverse(u). The same lever balances the rows and the columns, as a quarter-turn or transpose symmetry would force.

| id | kind | prediction | kill condition |
|---|---|---|---|
| K10a | real | Mean q90 over weighted-singular squares is at least 1.5x the mean over 5,000 random nonsingular squares (seed 1010). | Ratio below 1.5. Unscored if fewer than 15 weighted. |
| K10b | real | A lever match occurs in at least 25% of weighted-singular squares. | Below 25%. Unscored if fewer than 15 weighted. |

### Round K10 scores (`quarter_turn.py`, `quarter_turn.log`; 152,049 distinct squares, 264 singular)
| id | result | outcome |
|---|---|---|
| K10a | mean q90: weighted 1.074 vs nonsingular 0.897 (1.20x; needed 1.5x). Concentric 1.12x, eccentric 0.74x. | **lost** |
| K10b | lever match in 0 of 68 weighted (also 0 of 187 concentric and 0 of 9 eccentric). The detector was checked on built-to-match matrices and returned True. | **lost** |

Row levers and column levers are never the same lever in any class. No quarter-turn or transpose symmetry is behind
the weighted quarter. **Tally:** 0 of 2. Running record: **41 of 70**.
