# Generation loop: pre-registration

Every prediction below was written before any code for that round was run. Output is ASCII. Run from this folder.

## The question
The charged-lepton masses obey Koide's relation, Q = (sum m) / (sum sqrt m)^2 = 2/3, to 0.4 sigma. Earlier work in
this project (predictions/PREDICTIONS.md, P1 and P2) established three equivalent forms:
- **Cone form:** the vector (sqrt m_e, sqrt m_mu, sqrt m_tau) makes exactly 45 deg with the cube diagonal (1,1,1).
  (Foot, hep-ph/9402242, 1994, noticed this.)
- **Matrix form:** for any Hermitian matrix S whose eigenvalues are the sqrt m, Q = 2/3 holds exactly when the
  traceless part of S and its scalar part have equal norm. This is "stillness = turning". Equivalently, S sits at
  45 deg from the identity in matrix space.
- **Azimuth form:** with Q = 2/3 exact, sqrt m_n = A (1 + sqrt2 cos(delta + 2 pi n / 3)), and the electron and muon
  masses fix delta = 0.2222204717 (+- 4e-10). The near-miss delta ~ 2/9 is Brannen's (2006). In this project, 2/9
  is excluded at 452 sigma by the muon-mass precision.

So the cone (Q = 2/3) and the hierarchy (delta) are separate questions. G1 asks whether the cube supplies the cone.
G2 asks whether simple geometry supplies delta.

## Round G1 (registered 2026-10-30 18:20 CT)
**Space.** Real symmetric 3x3 matrices S = sum over g in T of eps_g (g + g^T)/2, where:
- T is a subset of the 24 proper rotations of the cube, with |T| = 1, 2 or 3;
- eps_g = +1 or -1;
- the eigenvalues of S are read as signed sqrt-masses.

**Measures.** Q = tr(S^2) / (tr S)^2 when tr S != 0. A spectrum counts as "exact Koide" if |Q - 2/3| < 1e-12.
Hierarchy is measured by the sorted absolute eigenvalue ratios against the lepton values
sqrt(m_mu/m_e) = 14.38 and sqrt(m_tau/m_e) = 58.97.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G1a | real | Exact-Koide spectra exist in this space: the cube can produce the 45 deg cone. | None found. |
| G1b | real | No exact-Koide spectrum reproduces both lepton ratios to within 1%. The cube alone cannot make the hierarchy, because eigenvalues of sums of at most 3 rotations are bounded small numbers. | Any spectrum within 1% on both ratios. |

## Round G2 (registered 2026-10-30 18:20 CT)
**Targets.** delta is defined only up to the symmetries delta -> -delta and delta -> delta + 2 pi/3. The six
representatives in [0, 2 pi) are all targets: delta, 2pi/3 - delta, 2pi/3 + delta, 4pi/3 - delta, 4pi/3 + delta,
2pi - delta. The tolerance is 1.2e-9, which is 3 sigma.

**Grammar, fixed now.**
- Atoms: pi; arctan(1/sqrt2) (body diagonal to face diagonal); arctan(sqrt2) (body diagonal to edge, 54.7356 deg);
  arccos(1/3) (tetrahedral angle); arctan(1/2); arctan(1/3).
- Candidates are of two kinds:
  - pure rationals p/q, with 1 <= q <= 1000 and 0 < p/q < 2 pi;
  - q1 * x + q2 * y, where x and y are atoms (x != y, or y absent) and q1, q2 are rationals with numerator
    |p| <= 12 and denominator 1-36.
- Only candidates in (0, 2 pi) are kept.

**Chance rate.** The expected number of random hits is N_candidates x 6 targets x 2.4e-9 / (2 pi). It is computed
and printed.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G2a | real | No candidate hits any target within 3 sigma. delta is not a simple geometric angle at the 1e-9 level. | Any hit. A hit is then reported with its chance probability. |
| G2b | translation | 2/9 misses the nearest target by more than 1e-7, confirming the earlier 452-sigma exclusion inside this pipeline. | Miss below 1e-7. |

## Scores, Rounds G1-G2 (`search.py`, `search.log`; run 2026-10-30 after registration)
**Erratum, left unedited above.** The registration text gives delta as "0.2222204717". That is a transposition
typo. The value the code computes from the stated method (electron and muon masses, Koide exact) is
0.2222220471 +- 3.9e-10, the same value recorded in predictions/PREDICTIONS.md (P1). The targets were computed by
the registered method, not from the typed number.

| id | result | outcome |
|---|---|---|
| G1a | 17,344 cube-rotation matrices (all subsets of 1-3 rotations, with signs): **0** exact-Koide spectra | **lost**. The 45 deg cone is not native to small sums of cube rotations. |
| G1b | no exact-Koide spectrum, so none near the lepton ratios | held (vacuously) |
| G2a | 7,275,871 candidates (3,144,230 rationals p/q with q <= 1000, plus 4,131,641 rational combinations of cube and tetrahedral angles); 0 hits within 1.2e-9; 0.016 expected by chance | **held**: delta is not a simple geometric angle at the 1e-9 level |
| G2b | 2/9 misses by 1.75e-7 (452 sigma) | held |

**What this leaves.** A mechanism has to supply two independent things:
- the cone, Q = 2/3. Small cube constructions do not give it.
- the azimuth, delta = 0.2222220471. It is not a simple angle.

**A restatement to pursue next (not yet a prediction).** Divide the sqrt-mass matrix S by its trace to get
rho = S / tr S. Then Q = tr(rho^2), so Koide's 2/3 says this "state" has purity exactly 2/3. That is the midpoint
between the maximally mixed value (1/3) and a pure state (1). For a two-level system, 45 deg from the identity
means a pure state; for three levels it means exactly halfway.

## Rounds G3-G5 (registered 2026-10-30 18:45 CT, before any G3-G5 code was written)
**Source.** The user, 2026-10-30 18:35 CT, verbatim: "G1, the 45 degree cone has to be a cone and two half cones..
G2 is a figure of the loop plus the angle  Also, follow the new lead".

**Shared definitions.**
- The cube's 13 rotation axes, as unit vectors, serve as pure "states": 3 edge-direction axes (1,0,0), 6
  face-diagonal axes (1,1,0)/sqrt2 and 4 body-diagonal axes (1,1,1)/sqrt3, with all sign variants up to overall
  sign.
- P_a is the projector onto axis a.
- A mixture is rho = (sum w_i P_i) / (sum w_i). Its purity is tr(rho^2), and Koide's 2/3 is purity exactly 2/3
  (the lead from G1-G2). Purity is an exact rational here, because every projector entry is rational.
- The eigenvalues of rho are read as sqrt-masses, so the angle delta is defined as before, and so are its targets.
  delta_e = 0.2222220471 rad (12.7324 deg). The window edge, where one mass vanishes, is pi/12 = 15 deg.

### G3: "a cone and two half cones" as weights (1, 1/2, 1/2), plus the plain halfway lead
Space:
- every pair (a, b) of distinct axes with weights (1/2, 1/2);
- every ordered triple (a; b, c) with weight 1 on a and 1/2 on each of b and c;
- every triple with equal weights.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G3a | translation | Equal pairs reach purity exactly 2/3 precisely when the two axes meet at the magic angle, arccos(1/sqrt3) = 54.7356 deg (edge to body diagonal). Derived by hand before this round: purity = (1 + cos^2)/2. Every such pair sits at the window edge, delta = 15 deg, with one mass exactly zero. | Any pair purity-2/3 case at another angle, or not at 15 deg. |
| G3b | real | Some (1, 1/2, 1/2) triples reach purity exactly 2/3 with all three eigenvalues nonzero. | None. |
| G3c | real | No exact purity-2/3 mixture in G3 lands within 1e-6 of delta_e. The lepton angle is not a cube mixture. | Any within 1e-6. |

### G4: "a figure of the loop plus the angle" as the unrolled cone
Unrolling a 45 deg cone turns an azimuth delta into a sector angle delta / sqrt2, since sin 45 deg = 1/sqrt2. The
rolled-up direction gives delta * sqrt2. G4 reruns the G2 grammar (unchanged) against the six G2 targets, each
divided by sqrt2 and multiplied by sqrt2. That makes 12 targets, at the same 3-sigma tolerance scaled by the same
factor. The chance rate is printed.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G4a | real | No hit. | Any hit, reported with its chance probability. |

### G5: neutrinos half a window further around (Brannen 2006: delta_nu = delta_e + pi/12)
Use P2's neutrino solution: Q = 2/3, the lightest root reversed, normal ordering, NuFIT splittings
dm21^2 = 7.42e-5 (+- 0.21e-5) and dm31^2 = 2.511e-3 (+- 0.027e-3) eV^2. Fit its angle delta_nu with the same labels
as the charged leptons (lightest at n = 1, middle at n = 2, heaviest at n = 0). Propagate the splitting errors by
Monte Carlo.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G5a | real | delta_nu - delta_e = pi/12 (15 deg) within 3 sigma of the oscillation-data uncertainty. That is, the neutrinos sit exactly half a 30 deg window beyond the leptons. | Off by more than 3 sigma. |

### Scores, Rounds G3-G5 (`rounds3.py`, `rounds3.log`)
| id | result | outcome |
|---|---|---|
| G3a | 12 pairs reach purity 2/3, all edge + body diagonal (magic angle), all at delta = 15 deg (one mass zero) | held |
| G3b | (1, 1/2, 1/2): 24 of 858 reach purity 2/3 **exactly**, all with three nonzero masses, all at delta = 8.3481 deg, sqrt-mass ratios 1 : 3.90 : 19.57 | **held** |
| G3c | the closest purity-2/3 mixture is 4.38 deg from delta_e | held |
| G4a | 7,275,871 candidates against 11 unrolled-cone targets; 0 hits; 0.030 expected | held |
| G5a | delta_nu - delta_e = 14.66 +- 0.24 deg vs pi/12 = 15 deg: -1.41 sigma | **held** |

**The structure behind G3, found after scoring and checked by hand.**
- Every exact hit uses the cube's flag at one vertex: an edge axis e = (1,0,0), the face diagonal through it,
  f = (1,1,0)/sqrt2, and the body diagonal through that, b = (1,1,1)/sqrt3. Their pairwise angles are the cube's
  three angles: 45, 54.74 and 35.26 deg.
- For rho = (w_e P_e + w_f P_f + w_b P_b)/W, purity 2/3 is the quadric w_e^2 + w_f^2 + w_b^2 - w_e w_f - 2 w_e w_b = 0.
  Fixing w_e = 1 turns it into a **circle** in (w_f, w_b): center (1/2, 1), radius 1/2. Write
  w_f = 1/2 + 1/2 cos(phi) and w_b = 1 + 1/2 sin(phi).
  - phi = 0 is equal weights (6.49 deg).
  - phi = -90 deg is "a cone and two half cones", (1, 1/2, 1/2) (8.35 deg).
  - phi = 180 deg is the edge + body pair (15 deg, the window edge).
- So the Koide mixtures of the cube flag form a loop in weight space, and each point on the loop has an angle phi.

## Round G6 (registered 2026-10-30 19:00 CT, before phi_e was computed): "a figure of the loop plus the angle"
Find the point(s) phi_e on the flag circle whose mixture has delta = delta_e. phi_e is taken modulo 2 pi, and both
solutions count if there are two. Propagate delta_e's uncertainty into phi using the derivative. Test phi_e against
the G2 grammar (unchanged) at 3 sigma.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G6a | real | The lepton angle lies on the flag circle, so a solution phi_e exists in (90 deg, 180 deg). | No solution. |
| G6b | real | phi_e is not a grammar angle: no hit at 3 sigma. The chance rate is printed. | Any hit, reported with its chance probability. |
| G6c | translation | Neutrinos, which need one reversed root, cannot be a flag mixture, because mixtures have no negative eigenvalues. | (Logical; recorded for completeness.) |

### Scores, Round G6 (`round6.py`, `round6.log`)
| id | result | outcome |
|---|---|---|
| G6a | The whole flag circle has purity 2/3, to 3e-41. The lepton angle is hit at phi_e = 135.758749 deg (weights 1 : 0.141796 : 1.348841) and at 217.561349 deg (1 : 0.103649 : 0.695195). | held |
| G6b | 7,275,871 grammar candidates; 0 hits; 0.059 expected. 135.7587 deg is 0.76 deg from 135 deg, at a precision of about 3e-7 deg. | held: phi_e is not a simple angle |

**The 15 deg step as a sharper test (not registered as a bet).** If delta_nu - delta_e = pi/12 exactly, then:
- dm21^2/dm31^2 = 0.03084, against a measured 0.02955 +- 0.00089 (+1.44 sigma);
- the masses are 0.379, 8.81 and 50.11 meV (sum 59.3 meV).

JUNO's precision on dm21^2 will decide it.

## Literature check (2026-10-30, after G1-G6; not exhaustive)
| idea in this folder | status | source |
|---|---|---|
| Koide = 45 deg between (sqrt m) and (1,1,1) | known since 1994 | Foot, "A note on Koide's lepton mass relation", hep-ph/9402242 |
| Q = 2/3 <=> circulant amplitude eta^2 = 1/2; the angle delta ~ 2/9 | known | Brannen 2006 (brannenworks.com/MASSES2.pdf); Strumia 2026, cyclic texture K1 with phase ~ 2/9 (arXiv:2610.10696) |
| "purity exactly 2/3" (G1-G2 restatement) | a rewording of eta^2 = 1/2, not new content | as above |
| neutrinos: lightest root reversed, delta_nu = delta_e + pi/12 (G5) | Brannen's 2006 prediction | Brannen, "Koide Mass Formula for Neutrinos" (brannenworks.com/MASSES.pdf); 2006 APS NW meeting |
| "stillness = turning" as equal singlet and doublet norms; "a loop plus an angle" | close published analog | Shulga 2026 (arXiv:2605.10245). An internal circle carries an antiperiodic (half-angle) doublet; equal norms give the 45 deg cone; the angle on the cone is -2 lambda_B/9 with lambda_B *not derived* |
| cube-flag mixtures (edge, face diagonal, body diagonal) and the Koide circle in weight space (G3, G6) | **not found** in the sources checked | closest: Brannen's density-matrix talk (2006), which builds projectors along +-x, +-y, +-z (the cube's edge axes), with eta = sqrt(1/2) and phase pi/4 |

**Update with newer data, after G5 was scored.** JUNO's first result (dm21^2 = 7.50 +- 0.12 e-5 eV^2,
arXiv:2511.14593), with NuFIT 6.1 dm31^2, moves the pi/12 test from -1.41 sigma to about 2.2 sigma off. This is
now tracked as P7 in predictions/PREDICTIONS.md. A 2026 rival, the "Alikhanov relation" (massless lightest
neutrino, arXiv:2601.18781), sits at -0.41 sigma on the same data.

## Round G7 (registered 2026-10-30 19:35 CT, before any quark angle was computed): mechanisms on separate objects
**Source.** The user, 19:25 CT, verbatim: "Assuming all working mechanism are right with different instances.. and
maybe all the mechanism work together for a full picture". Then 19:27 CT, verbatim: "Not the same layer on the same
object, same layers on multiple separate objects in the same system".

**Assignment rule, fixed now from the user's color principle (19:17 CT).**
- The colorless object (charged leptons) carries the exact cone, Q = 2/3. That is P1, already consistent.
- The colored objects (the up-type family u, c, t and the down-type family d, s, b) carry the exact color angle,
  delta = 2/9 rad, with their own amplitude b. Their cone is not required, because color breaks it.

**Method.**
- Write sqrt m_n = A (1 + b cos(delta + 2 pi n / 3)), with labels fixed by mass order: heaviest n = 0, lightest
  n = 1, middle n = 2.
- Get (A, b, delta) exactly from the three masses via the discrete Fourier coefficient,
  c1 = (1/3) sum_n sqrt(m_n) e^(-2 pi i n/3) = (A b / 2) e^(i delta).
- Check: this labeling returns delta_e = 0.22222 for the charged leptons.
- Scored convention: the P6 convention the user committed to. That is u, d and s at 2 GeV (FLAG 2024), and c, b and
  t each at its own mass (m_c 1278 +- 13 MeV, m_b 4200 +- 14 MeV, m_t(m_t) 162.5 +- 1.8 GeV).
- Errors by Monte Carlo.
- Two other conventions are reported but not scored: all six run to one common scale, and pole masses for c, b and
  t.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G7a | real | up-type angle delta_u = 2/9 within 2 sigma | off by more than 2 sigma |
| G7b | real | down-type angle delta_d = 2/9 within 2 sigma | off by more than 2 sigma |

The chance rate, the probability that a uniformly random angle lands within 2 sigma of 2/9 on the delta circle, is
printed for each.

### G7 scores (run 2026-10-30, round7.py, round7.log)
Check: charged leptons give b = 1.414209 and delta = 0.222225, so the fit reproduces the lepton angle.

| id | result | score |
|---|---|---|
| G7a | up-type delta_u = 0.07707 +- 0.00062 rad (4.42 deg), b^2 = 3.07; -235.7 sigma from 2/9 | **LOST** |
| G7b | down-type delta_d = 0.10984 +- 0.00052 rad (6.29 deg), b^2 = 2.39; -214.1 sigma from 2/9 | **LOST** |

**Unscored conventions.** No convention rescues either family.
- One common scale: up 0.0519, down 0.1037.
- Pole masses for c, b, t: up 0.0864, down 0.1024.

**Correction to the chance rate, made after scoring; the scores are unaffected.**
- The first run computed the chance on the full 2 pi circle. With mass-order labels, delta can only lie in (0, pi/3).
- Corrected: up 0.24%, down 0.20% (previously 0.04% and 0.03%). Fixed in round7.py and rerun.

**Post hoc, not evidence.**
- Down-type delta 0.1098 lies near 1/9 = 0.1111. That is still -2.5 sigma in the scored convention, and it drifts to
  0.102-0.104 in the other conventions.
- Up-type b^2 = 3.07 lies near 3. It moves 2.99 -> 3.32 across conventions.
- In both cases the spread across conventions is larger than the gap to the round number, so neither can be scored
  until theory fixes the convention.

**Verdict.** Under the color-based assignment, the exact 2/9 angle belongs only to the colorless leptons. The colored
families do not carry it.

## Round G8 (registered 2026-10-30, before computing): the literature's version of separate objects
**Source.** Same user statement as G7: same layer, separate objects.
- The published instance is the exact cone (Q = 2/3) on quark triplets that cut across up and down type.
- Rodejohann and Zhang (2011) fit c-b-t.
- Rivero (arXiv:1111.7232) found s-c-b with a negative sqrt(m_s).
- These are their claims, not ours. G8 tests them under the convention already fixed for G6 and G7.

**Scored convention.** P6 own-mass: m_s(2 GeV) = 93.46 +- 0.58 MeV; m_c(m_c) = 1278 +- 13 MeV;
m_b(m_b) = 4200 +- 14 MeV; m_t(m_t) = 162.5 +- 1.8 GeV. Errors by Monte Carlo.

**Unscored, reported.** The authors' mixed convention, with the direct top 172.52 +- 0.33 GeV in place of m_t(m_t),
and all at one common scale.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G8a | real | Q(-s, c, b) = 2/3 within 2 sigma | off by more than 2 sigma |
| G8b | real | Q(c, b, t) = 2/3 within 2 sigma | off by more than 2 sigma |

### G8 scores (run 2026-10-30, round8.py, round8.log)

| id | scored result (P6 own-mass) | score |
|---|---|---|
| G8a | Q(-s, c, b) = 0.67444 +- 0.00124, +6.3 sigma | **LOST** |
| G8b | Q(c, b, t) = 0.66216 +- 0.00132, -3.4 sigma | **LOST** |

**Unscored.**
- (-s, c, b) at one common scale: 0.7015, +25 sigma.
- (c, b, t) with the direct top: 0.66875, +4.0 sigma.
- (c, b, t) at one common scale: 0.7208, +48 sigma.

**Note.** Q(c, b, t) crosses 2/3 between m_t(m_t) and the pole mass. So some top definition near 167 GeV makes it
exact. That is a convention being chosen to fit, not evidence.

**Verdict.** Neither the color-based assignment (G7) nor the published cross-family triplets (G8) puts an exact
lepton mechanism on a quark object in any fixed convention. Quark masses depend on convention at the 5-30% level,
so any exact quark claim needs theory to choose the convention first.

## Round G9 (registered 2026-10-30 19:45 CT, before running): the families read where color locks
**Source.** The user, 19:39 CT, verbatim: "Where color locks". This was his pick among three options: each quark's
own mass, one common scale, or where color locks (about 1 GeV).

**The rule is unchanged from G7.** Each colored family carries delta = 2/9 rad with its own amplitude b. The phrase
"where color locks" has two readings, and both are fixed now.

### Reading A: masses run to mu = 1 GeV in MS-bar
**Method.**
- Run all six masses to 1 GeV with 4-loop QCD running.
- alpha_s matching at the b and c thresholds is 11/72 a^2. The mass decoupling factor is 89/432 a^2.
- Inputs: the G7 values, plus alpha_s(M_Z) = 0.1180 +- 0.0009.
- The top's value at 1 GeV is a formal continuation.
- Also report delta at mu = 2 GeV, 3 GeV and M_Z.

**Not blind.** Last turn I showed approximate common-scale numbers: up 0.052, down 0.104. QCD running multiplies
every quark mass by the same factor, so ratios, and with them delta and Q, are the same at every common scale. Reading
A is that convention recomputed properly. Its score counts as a confirmation, not an independent test.

### Reading B: the masses the quarks carry once color has locked them inside hadrons
**Inputs.** Constituent masses fixed from a published set (Griffiths, Introduction to Elementary Particles 2008,
p. 135, as tabulated on Wikipedia "Constituent quark"): u 336, d 340, s 486, c 1550, b 4730 MeV.

**Uncertainty.** These masses are model-dependent, so each gets an independent 1-sigma model uncertainty of +-10%.
That is generous, and it biases the test toward holding. The chance rate is printed so that a cheap hold is not
oversold.

**Blind.** I have not computed the delta of any constituent family.

**The up-type family is undefined in this reading.** The top decays before color can lock it:
- tau_t = hbar / Gamma_t, about 4.6e-25 s, with Gamma_t about 1.42 GeV.
- The locking time is about hbar / Lambda_QCD, about 3e-24 s.
- Griffiths' 177 GeV top entry is only a stand-in for its free mass.
- So (u, c, t) is reported but not scored.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G9a | confirmation (not blind) | Reading A, up-type delta_u(1 GeV) = 2/9 within 2 sigma | off by more than 2 sigma |
| G9b | confirmation (not blind) | Reading A, down-type delta_d(1 GeV) = 2/9 within 2 sigma | off by more than 2 sigma |
| G9c | real (blind) | Reading B, down-type delta_d(constituent) = 2/9 within 2 sigma, at +-10% model uncertainty | off by more than 2 sigma |

### G9 scores (run 2026-10-30, round9.py, round9.log)
**Checks on the running.** All three match the literature, so the running is sound.
- alpha_s(1 GeV) = 0.476.
- m_b(M_Z) = 2.879 GeV, against the literature 2.86-2.87.
- m_c(3 GeV) = 0.994 GeV, against FLAG 0.988.
- m_c/m_s at 2 GeV = 11.77, against the FLAG lattice ratio 11.77.

At mu = 1 GeV, 2 GeV, 3 GeV and M_Z, delta comes out identical to 5 digits: up 0.05218, down 0.10010. Running is
blind to flavor, so the choice of scale cannot move any family's angle.

| id | result | score |
|---|---|---|
| G9a | Reading A, up: delta = 0.05218 +- 0.00067 rad (2.99 deg), b^2 = 3.32, Q = 0.887; -254.6 sigma | **LOST** (confirmation) |
| G9b | Reading A, down: delta = 0.10010 +- 0.00055 rad (5.74 deg), b^2 = 2.49, Q = 0.748; -221.8 sigma | **LOST** (confirmation) |
| G9c | Reading B, down constituent (340, 486, 4730): delta = 0.0643 +- 0.0265 rad (3.68 deg), b = 0.89, Q = 0.465; -6.0 sigma. Checked by percentile: 0 of 200,000 draws at +-10% reach 2/9 (the largest is 0.214) | **LOST** |

**Robustness, unscored.** 2/9 only comes within reach if the model spread on the constituent masses is widened:
0.55% of draws at +-20%, and 4.9% at +-30%. At that width, a hit would mean nothing.

**The top never locks.** hbar/Gamma_t = 4.6e-25 s, against a locking time of about 3.1e-24 s, so the top decays 6.8
times faster than color can lock it. Read where color locks, the up family has only two members.

**Tally for quark families carrying 2/9 (G7-G9).** 7 scored, 0 held.
- In every reading tried (own mass, any common scale, pole masses, constituent masses, and the published
  cross-family triplets), no quark object carries the lepton angle or the exact cone.
- The 2/9 appears on the quark side only in the charges, |Q_u Q_d| = 2/9, not in their masses.

## Round G10 (registered 2026-10-30 21:20 CT, before running): the third layer
**Source.** The user, 21:11 CT, verbatim: "Run it". That answers my offer of a pre-registered search for what fills the
gap between the exact cone and the exact 2/9 angle on the charged leptons.

**Literature.** I checked for a published correction formula before registering.
- Zenczykowski (Open Physics 16, 2018, 427) states the incompatibility and calls it "extremely small".
- He attributes it to "higher order corrections of the underlying scheme" and gives no formula.
- So there is no published candidate to test blind (no tier 0).

**Targets.** Two, computed in round10.py from m_e and m_mu (PDG/CODATA, m_mu +- 2.3e-6 MeV).
- eps, the angle form: Koide held exact, delta_K = (2/9)(1 - eps). Expected about 7.88e-7.
- eta, the cone form: delta = 2/9 held exact with free amplitude, Q = (2/3)(1 - eta). Expected about 2.1e-7.
- The absolute forms (2/9 - delta, 2/3 - Q) differ from these by the rational factors 2/9 and 2/3, which the
  coefficient sets already contain. So only eps and eta are independent.
- Tolerance: 2 sigma, where sigma comes from m_mu.

**Grammar: candidate = c * S, positive values only.**
Small factors S, 69 in total:

| Group | Form | Ranges | Count |
|---|---|---|---|
| (i) | x^k | x in {alpha, alpha/pi, alpha/(4pi)}; k = 1..4 | 12 |
| (ii) | rho^k | rho in {m_e/m_mu, m_e/m_tau, m_mu/m_tau}; k in {1/2, 1, 3/2, 2, 5/2, 3, 4} | 21 |
| (iii) | x * rho^k | x in {alpha, alpha/pi}; k in {1/2, 1, 3/2, 2} | 24 |
| (iv) | (alpha/pi)^k * L^j | L in {ln(m_mu/m_e), ln(m_tau/m_e), ln(m_tau/m_mu)}; k in {2, 3}; j in {1, 2} | 12 |

Pure rationals are excluded, because any target lies near some rational.

Coefficient tiers:

| Tier | Coefficients c | Count |
|---|---|---|
| T1 | {1} | 1 |
| T2 | color and cone numbers: {1, 1/2, 2, 1/3, 2/3, 3/2, 3, 4/3, 2/9, 9/2, 8, 1/8, 1/9, 9} | 14 |
| T3 | every reduced p/q with 1 <= p, q <= 12 | 91 |

**Chance calibration.**
- Replace each real target with random targets, log-uniform within +-1 decade of it, at the same relative tolerance.
- 20,000 trials.
- Expected chance hits for a tier = the mean number of hits over these random target pairs.

**Scoring.** A tier HOLDS only if it has at least one hit AND P(at least that many hits | Poisson with the calibrated
expected count) < 0.01. Otherwise it is LOST, meaning no third layer is identifiable in that tier beyond what chance
supplies.

**Disclosure.** Before registering, I looked at exactly one candidate: 2 alpha^3 = 7.77e-7 against eps of about 7.88e-7.
That is 1.4% off, outside the window. It sits in T2 and will be scored like everything else.

| id | kind | prediction | kill condition |
|---|---|---|---|
| G10a | real | T1 identifies the gap (hits beyond chance, p < 0.01) | no hit, or hits consistent with chance |
| G10b | real | T2 identifies the gap | same |
| G10c | real | T3 identifies the gap | same |

### G10 scores (run 2026-10-30, round10.py, round10.log)
**Targets.** eps = 7.880596e-7 +- 1.74e-9; eta = 2.131894e-7 +- 4.72e-10. Both are measured to 0.22%.

| id | candidates per target | hits | expected by chance | P(at least that many) | score |
|---|---|---|---|---|---|
| G10a T1 | 69 | 0 | 0.061 | 1 | **LOST** |
| G10b T2 | 966 | 0 | 0.879 | 1 | **LOST** |
| G10c T3 | 6279 | 6 | 5.614 | 0.49 | **LOST** (hits at exactly the chance rate) |

**Nearest misses.**
- T1, eps: alpha/pi * (m_e/m_mu)^(3/2) = 7.8125e-7, -0.86% (-3.9 sigma).
- T2, eta: 2 (alpha/pi)^3 ln(m_tau/m_e), -4.1%. The disclosed 2 alpha^3 also misses.

**The six T3 hits, all at the chance rate.**
- eps: 3/8 alpha (m_e/m_tau) at -0.64 sigma; 7/3 (alpha/4pi)^2 at -0.70 sigma.
- eta: 3/11 (alpha/pi)(m_e/m_mu)^(3/2) at -0.26 sigma; 3/5 (alpha/pi)^3 ln^2(m_mu/m_e) at +1.19 sigma;
  5/4 alpha (m_e/m_mu)^2 at +0.36 sigma; 6 alpha (m_e/m_tau)^(3/2) at +0.70 sigma.

Each looks like physics, and as a set they are what the grammar's size produces by chance.

**Verdict.**
- At 0.22% precision on the gap, a correction search can only be informative with about 70 or fewer candidates,
  which is T1 size. T1 has no hit.
- Any richer grammar finds formulas at the chance rate.
- The third layer can only come from a theory that fixes one term in advance, or from a tau mass measured to about
  2.5 keV. The second is beyond any planned experiment (P8).

## Review (Claude Code, 2026-10-31; appended, nothing above edited)

- **Every round reproduces.** All seven scripts rerun to their logs byte for byte. `test_scores.py` checks each
  script's SCORE line against the score tables above (21 ids), and a deliberately flipped table entry makes it fail.
- **G9's running, refereed on the code.** `qcd_running_check.py` is an independent implementation: the coefficients
  in the alpha_s/(4 pi) normalization of the four-loop papers, a hand-written RK4, and the mass factor as an integral
  over the coupling.
  - The beta and gamma_m coefficients in `round9.py` are the four-loop ones (van Ritbergen, Vermaseren and Larin
    1997; Chetyrkin 1997; Vermaseren, Larin and van Ritbergen 1997), correctly rescaled to alpha_s/pi. For nf = 5
    they give 1.9167, 2.4167, 2.8268, 18.852 (beta) and 1, 3.5139, 7.4199, 11.034 (gamma_m).
  - The decoupling constants are right for matching at mu = m_h(m_h) in MS-bar, and applied in the right
    direction: 11/72 a^2 for alpha_s and 89/432 a^2 for the masses (Chetyrkin, Kniehl and Steinhauser).
  - The independent run reproduces every printed number: alpha_s(m_b) = 0.2243, alpha_s(2 GeV) = 0.3015,
    alpha_s(1 GeV) = 0.4760, m_b(M_Z) = 2.879 GeV, m_c(3 GeV) = 0.994 GeV, m_c/m_s = 11.77, the six masses at 1 GeV,
    and delta_up = 0.05218, delta_down = 0.10010.
  - That the ratios are the same at every common scale holds by construction: the running factor, and at this
    order the decoupling jump, are the same for every flavor. It is a consistency check, not evidence.
  - One small inconsistency, without effect: the b and c thresholds get a decoupling jump and the top's does not.
    The jump would move the top's continued mass by about 0.03%, far too little to move delta.
- **G10's chance calibration, reviewed.** `g10_calibration_check.py` rebuilds the targets and the grammar from this
  file, without importing `round10.py`. It reproduces the targets, the 0, 0 and 6 hits, and the registered
  expectations (0.064, 0.877 and 5.616, against 0.061, 0.879 and 5.614: Monte Carlo noise). Two other calibrations:
  - random targets within +-0.3 and +-0.1 decade: T3 expects 5.74 and 5.49;
  - random constants, with alpha and the three masses each scaled by a log-uniform factor in [1/2, 2] and the
    grammar recomputed: T3 expects 5.66.

  No tier's verdict changes. T1 and T2 have no hits, and T3's six stay at P of about 0.5 under every calibration.
  The grammar's density near the targets is close to its two-decade average, so the registered calibration does
  not miscount.
- **The flag circle, checked symbolically.** `flag_circle_check.py`: for any lines, purity 2/3 of
  (sum w_i P_i)/(sum w_i) is the quadric sum w_i^2 + 6 sum_{i<j} (c_ij - 2/3) w_i w_j = 0, where c_ij is the pair's
  squared cosine. So a cross term vanishes exactly when that squared cosine is 2/3. On the cube's flag the squared
  cosines are 1/2 (edge and face diagonal), 1/3 (edge and body diagonal: the magic angle of
  `towers/THE_ONE_THIRD_AND_THE_FOLD.md`) and 2/3 (face and body diagonal). That is why the purity-2/3 set is a
  circle, and both G6 points lie on it.
- **Yield.** Of the 21 scored ids, the holds in G1-G6 are mostly null results (no hit, no cube origin) or
  translations. The positive ones, G3b and G6a, are existence statements on the flag circle, and G5a is Brannen's
  2006 relation, now at about +2.2 sigma with JUNO (P7). G7-G10 lost all ten. The one new piece of mathematics is
  the flag circle, an elementary identity.
