# Prediction ledger

Dated bets on physics experiments, written down before the deciding data arrives. Each bet names the result that would
kill it and the experiment that will decide it. Status changes only when that experiment reports.
User quotes are marked with their Central Time timestamp and the word "verbatim".

---

## P1. Tau mass from Koide's relation (registered 2026-10-29)
**Basis.** Q = (m_e + m_mu + m_tau) / (sqrt m_e + sqrt m_mu + sqrt m_tau)^2 = 2/3 exactly, using pole masses.
Geometrically, the vector (sqrt m_e, sqrt m_mu, sqrt m_tau) sits at exactly 45 deg to the cube diagonal (1,1,1).
In circulant-matrix form, the "still" (diagonal) part and the "turning" (120 deg cycle) part carry equal weight.
Context from the user: "Intrinsic spin" (2026-10-29 09:06, verbatim).

**Prediction.** m_tau = 1776.969 MeV.

**Now.** Q = 0.6666645 +- 0.0000051 (0.4 sigma from 2/3). The PDG average is 1776.93 +- 0.09 MeV. Belle II (2023)
measured 1777.09 +- 0.08 (stat) +- 0.11 (syst) MeV.

**Kill.** The world-average tau mass excludes 1776.969 MeV at more than 3 sigma.
**Decided by.** Belle II, BESIII, and a future tau-charm factory.

**Side note (measured, not a bet).** In Brannen's form, sqrt m_n = A (1 + sqrt2 cos(delta + 2 pi n/3)), the start
angle is delta = 0.2222220471 if the electron and muon masses fix it. That is 1.75e-7 short of 2/9, which is
excluded at 452 sigma by the muon-mass precision. So sqrt2 and 2/9 cannot both be exact.

---

## P2. Neutrino masses from the same rule (registered 2026-10-29)
**Source.**
- "Intrinsic spin" (09:06, verbatim).
- "One has an exact opposite, the other does not" (09:39, verbatim). This was the user's account of why leptons
  balance stillness and turning while quarks do not: electric charge cancels only against an exact opposite, while
  color can also cancel in thirds at 120 deg.
- Asked whether a particle that is its own opposite counts as having an exact opposite, the user answered "Yes"
  (10:05, verbatim).

**Consequence.** The rule applies to neutrinos whether they are Dirac (a separate antineutrino) or Majorana (their
own antiparticle). Neutrino masses should therefore satisfy Q = 2/3.

**Fix used (not derived).** The lightest neutrino's square root enters with a reversed sign ("spins the other way").
With all roots positive there is no solution: Q tops out at 0.586 in normal ordering. Brannen proposed this sign
choice in 2006. A scan of every single-sign reversal in both orderings finds only the lightest-reversed solutions.

**Predictions.**

| | normal ordering (main branch) | inverted ordering (fallback) |
|---|---|---|
| masses (meV) | m1 = 0.360, m2 = 8.62, m3 = 50.11 | m1 = 49.32, m2 = 50.07, m3 = 2.93 |
| sum | **59.1 meV** | 102.3 meV, already disfavored by DESI DR2 + CMB (< 64 meV at 95%) |

For the main branch:
- The beta-decay (KATRIN-type) mass is 8.8 meV, so KATRIN and Project 8 should see no mass signal.
- If neutrinos are Majorana, the neutrinoless double-beta effective mass m_bb lies between 1.2 and 3.9 meV,
  depending on the unknown Majorana phases. That is below the planned reach of LEGEND-1000 and nEXO.

**Inputs.** NuFIT: dm21^2 = 7.42e-5 eV^2, dm31^2 = 2.511e-3 eV^2, sin^2 theta12 = 0.307, sin^2 theta13 = 0.0222.
If these move, the procedure (Q = 2/3 with the lightest root reversed) is fixed and the digits are recomputed.
**Recomputed 2026-10-30 with newer inputs.**
- dm21^2 = 7.50 +- 0.12 e-5 eV^2 (JUNO, first result, arXiv:2511.14593).
- dm31^2 = 2.529 +- 0.021 e-3 eV^2 (NuFIT 6.1, normal ordering, as quoted in arXiv:2601.18781; not read at the
  source).
- Result: 0.363, 8.67 and 50.29 meV, sum 59.3 meV. The bet is unchanged in substance.
- *Added 2026-10-31, on review:* with these inputs the beta-decay mass is 8.9 meV and m_bb is 1.2 to 4.0 meV
  (`ledger_math.py`). The 8.8 meV and 1.2 to 3.9 meV above come from the original inputs.

**Kill (main branch), any one of:**
- Inverted ordering is established (JUNO, DUNE, KM3NeT/ORCA).
- Cosmology measures the sum below 58.7 meV, the oscillation minimum. This would also rule out every
  normal-ordering model.
- Cosmology measures the sum clearly above about 70 meV.
- A neutrinoless double-beta signal implies m_bb > 4 meV.
- A beta-decay mass above about 10 meV is measured.

**Decided by.** JUNO (running) for the ordering. DESI, Euclid, CMB-S4 and the Simons Observatory for the sum.
LEGEND and nEXO for m_bb.

---

## P3. Quark unitarity-triangle angle alpha >= 90 deg (stated in chat 2026-10-27, written here 2026-10-29)
**Source.** "the bend between 90 and 120?" (2026-10-27 20:42, verbatim). The global fit already excludes values above
about 96 deg at 3 sigma, so the effective bet is alpha >= 90 deg.

**Now.**
- UTfit global fit: 91.7 +- 1.4 deg.
- Direct measurement: 88.5 +- 3.1 deg (UTfit) and 84.1 (+3.7 / -3.0) deg (PDG/HFLAV).

No new data has arrived between the statement in chat and this write-up.

**Kill.** The direct world average excludes alpha >= 90 deg at more than 3 sigma.
**Decided by.** Belle II and LHCb, aiming for about 1 deg precision.
**Open.** The user has not yet given the size and sign of the "stray" from 90 deg ("another reduction from crossing
scales", 2026-10-27 21:13, verbatim). It is not registered.

---

## P4. A lumpier universe: the matter dipole stays at least 2x the kinematic value (stated in chat 2026-10-27, written here 2026-10-29)
**Source.** "I think you are imagining too smooth a universe and our ability to see the layers and exchanges is still
currently too shallow." (2026-10-27 19:53, verbatim)

**Prediction.** As surveys reach deeper sources, the number-count dipole of distant radio galaxies and quasars stays
at least 2x the amplitude expected from our 370 km/s motion. The Giant Arc and the Big Ring also stay statistically
significant.

**Now.**
- CatWISE quasars: about 2x expected, 3.3-3.6 sigma after a 2025 reassessment (originally 4.9 sigma).
- DESI DR1 quasars: the right speed but the wrong direction, at 3.45 sigma.

**Kill.** A deeper survey measures a dipole consistent with the kinematic expectation (ratio below 1.5, excluding 2x at
more than 3 sigma).
**Decided by.** Euclid, SPHEREx, Rubin LSST and SKA.

---

## P5. The neutron lifetime gap is outside breaking, and the beam is right (registered 2026-10-30)
**Source.**
- "It depends on what breaks the neutron... a cosmic ray breaking a neutron produces a different result than a pure
  fission" (14:06, verbatim).
- Asked whether the gap comes from something outside breaking bottled neutrons or from a second internal decay
  channel, the user answered "Something outside....  built up higgs possibly?" (14:52, verbatim).

**Prediction (outcome).** The true free-neutron lifetime is the beam value, near 888 s. Bottle experiments lose about
1.2% of their neutrons to something other than beta decay.

**Now.** Beam: 888.1 +- 2.0 s. Bottle: 877.8 +- 0.3 s. The gap is about 10 s, roughly 5 sigma.

**Kill.**
- J-PARC, whose time-projection chamber counts decay electrons and so depends on neither proton counting nor
  storage, lands near 878 s and more than 3 sigma below 888 s.
- Or a new beam measurement (BL3 at NIST) also lands near 878 s.

**Holds if.** New bottle results (UCNtau+, tauSPECT) drift up toward 888 s, or a storage-loss mechanism is identified
that accounts for the gap.

**Mechanisms checked at registration (2026-10-30). These are separate from the outcome bet.**
- Cosmic rays: they break stored neutrons at about 4e-27 per second against a decay rate of 1.1e-3 per second.
  That is 1e-24 of the effect needed. Ruled out.
- Built-up Higgs: ruled out on two counts.
  - A local Higgs field raised by 0.10% would make neutrons decay 1.17% faster (from phase space, with the
    quark-mass part of the n-p split scaled). But it would also shift the electron mass, and with it every
    electron-based atomic clock, by 0.10%, and clocks agree to about 1e-18.
  - The stored neutrons themselves push the Higgs field by about 2e-49, far short of the 1e-3 needed. Higgs bosons
    live 1.6e-22 s, so they cannot accumulate.
- Still open: material-wall or residual-gas losses. A magnetic, wall-free bottle (UCNtau) still gets 877.8 s.

---

## P6. Up-type quarks turn exactly 1/3 more than down-type (registered 2026-10-30)
**Source.**
- "Down type quarks subtracted from up type quarks is eerily close to 1/3" (17:38, verbatim).
- "Yes ill commit" (17:50, verbatim), committing to the convention below.

**Statement.** turning = 3Q - 1 for each three-quark family, where Q is Koide's ratio and 1 means stillness and
turning balance. The bet is turning(u, c, t) - turning(d, s, b) = 1/3 exactly.
**Convention (part of the bet).** MS-bar masses: u, d and s at 2 GeV, and c, b and t each at its own mass.

**Inputs.** FLAG 2024: m_u = 2.14, m_d = 4.70, m_s = 93.46 MeV, m_c(m_c) = 1.278 GeV, m_b(m_b) = 4.200 GeV.

**Prediction.** m_t(m_t) = 157.8 GeV, which is a pole mass of about 167.6 GeV using the 4-loop conversion.
The conversion is checked against the measurements: 162.5 GeV converts to 172.5 GeV.

**Status at registration: disfavored.**
- Against the cross-section MS-bar value of 162.5 (+2.1 / -1.5) GeV it is about 2-3 sigma off.
- Against the direct top mass from ATLAS+CMS, 172.52 +- 0.33 GeV, it is 4.6-7.8 sigma off. The range depends on
  whether the ambiguity between the reconstructed mass and the pole mass is taken as 1.0 or 0.5 GeV.
- Under the same convention, the difference with today's masses is 0.339.

**Fallout if true.**
- The Standard Model W mass would be 80.327 GeV, against a measured value of about 80.365 +- 0.010.
- The Higgs vacuum would be absolutely stable up to the Planck scale, which needs a pole mass below about 171.5 GeV.

**Kill.** A top-threshold scan at FCC-ee or a similar machine measures m_t(m_t) above 160 GeV to +-0.1 GeV. Or the
direct-mass interpretation is confirmed to within 1 GeV of the pole mass. The second condition is close to holding
already.

**Recompute.** Run `ledger_math.py` (P6 block).

---

## P7. Neutrinos sit exactly half a window past the charged leptons (registered 2026-10-30)
**Source.**
- The user asked to register it: "Yes and check literature" (2026-10-30 18:48, verbatim).
- The geometric reading came from the user's "the 45 degree cone has to be a cone and two half cones" (18:35,
  verbatim).
- The relation is **Brannen's 2006 prediction**, delta_nu = delta_e + pi/12. Brannen, "Koide Mass Formula for
  Neutrinos", brannenworks.com/MASSES.pdf. Brannen predicted m = 0.383, 8.91 and 50.7 meV.

**Statement.** Both families lie on Koide's cone: Q = 2/3, with the lightest neutrino root reversed (as in P2). The
neutrino angle is the charged-lepton angle plus exactly 15 deg: delta_nu - delta_e = pi/12. On the cone, the
all-positive region comes in 30 deg windows. The charged leptons sit 2.27 deg inside the edge of one window, and
the neutrinos sit half a window further around.

**Prediction.** dm21^2 / dm31^2 = **0.03084**. Masses, scaled by dm31^2 = 2.529e-3 eV^2: 0.380, 8.84 and 50.29 meV;
sum 59.5 meV; normal ordering.

**Status at registration.**
- Against NuFIT 5 (the P2 inputs): measured ratio 0.02955 +- 0.00089, +1.44 sigma. This matches Round G5 in
  generation_loop/.
- Against JUNO 2025 (dm21^2 = 7.50 +- 0.12 e-5) with NuFIT 6.1 dm31^2 = 2.529 +- 0.021 e-3: measured
  0.02966 +- 0.00053, **+2.21 sigma**. That is mild tension, under the kill line.

**Rival on record.** The "Alikhanov relation" (arXiv:2601.18781, 2026; textures in Strumia, arXiv:2610.10696) has
the lightest neutrino massless. It predicts a ratio of (3 - 2 sqrt2)^2 = 0.02944, which is -0.41 sigma against the
same data. The two predictions differ by 0.0014. JUNO's design precision (about 0.3% on dm21^2, about 0.2% on
dm31^2) would separate them by roughly 10 sigma.

**Kill.** The measured dm21^2/dm31^2 excludes 0.03084 at more than 3 sigma. P7 also inherits P2's kills: inverted
ordering, or a cosmological sum below 58.7 meV.
**Decided by.** JUNO (dm21^2, and later dm31^2), with dm31^2 also from T2K, NOvA, DUNE and Hyper-K.
**Recompute.** Run `ledger_math.py` (P7 block).

---

## P8. The angle is exactly 2/9, set by color, and Koide's cone gives way (registered 2026-10-30)
**Source.**
- "a half cone is 2/3 force color... so the whole picture of cones fillings cubes leaves 1/3 leftover... that
  might be the -2/9" (18:53, verbatim).
- "The reason is color.. A cone carries 3 colors but a half cone carries two" (19:17, verbatim).

**Statement.** Brannen's angle is exactly delta = (2/3) x (1/3) = 2/9 rad.
- **The charge reading.** 2/3 and 1/3 are the up and down quark charges, which anomaly cancellation ties to the
  electron's charge: -1 + 3(2/3 - 1/3) = 0 per generation. So delta = |Q_u Q_d|. With N_c colors this is
  (N_c^2 - 1)/(4 N_c^2), which is 8/36 at N_c = 3 (8 = the number of gluons).
- **Caveat.** The plain count (N-1)/N^2 also gives 2/9 at N = 3. So 2/9 has more than one color reading.
- **What gives way.** Exact 2/9 and an exact Koide 2/3 are incompatible, so the cone gives way.

**Prediction.** With the amplitude fixed by the electron and muon masses:
- Q = 0.66666652, about 2.1e-7 below 2/3;
- m_tau = **1776.96651 MeV**, against 1776.969 MeV if Koide is exact (P1).

**Status.** Consistent: PDG m_tau = 1776.93 +- 0.09 MeV. Measured Q = 0.6666645 +- 0.0000051.

**Kill.** A tau mass measured to about 1 keV that excludes 1776.9665 MeV at 3 sigma. P1 and P8 differ by only
2.5 keV, about 35x below today's error, and no planned experiment reaches that. This is a standing fork, not a
near-term bet.

**Open (the gap in the mechanism).** A count gives a pure number. For it to be an angle in radians, something must
produce a phase equal to the count with coefficient exactly 1. That is Shulga's underived lambda_B
(arXiv:2605.10245). Read as a fraction of a full turn, 2/9 would be 80 deg, not 12.7 deg.

**Third-layer search (G10, 2026-10-30).** The search tried to fill the gap with a small correction term.
- The gap is eps = 7.8806e-7 +- 0.0017e-7 in the angle form, and eta = 2.1319e-7 in the cone form.
- No bare power of alpha, mass ratio or log term hits it.
- Richer grammars hit it exactly at the chance rate (6 hits against 5.6 expected).
- So the gap cannot be identified by search; it needs a theory that fixes one term in advance. See
  generation_loop/PREREG.md G10.

**Recompute.** Run `ledger_math.py` (P8 block).
