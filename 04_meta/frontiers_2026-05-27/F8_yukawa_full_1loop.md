# Frontier F8 — Yukawa hierarchy at full 1-loop SM (closing F7's gap?)

**Status:** FIRST-PASS COMPLETE, HONEST NEGATIVE on the F7 closure hypothesis. Including the full 1-loop Standard Model electroweak terms (g_1², g_2², y_b², y_τ²) does NOT close F7's 18% top-Yukawa gap — it WIDENS it to ~32%. The F7 scoping document hypothesized that the omitted 1-loop EW terms "all push y_t downward" and would narrow the residual to ~5%. A careful re-derivation of the SM 1-loop top-Yukawa beta-function structure shows this expectation was physically backwards: the EW gauge contributions enter as `-17/12 g_1² - 9/4 g_2²`, the **same sign** as the QCD term `-8 g_3²`. Adding negative contributions to the bracket makes it more negative, which makes y_t grow MORE during the M_X → M_Z evolution, not less. The 18 → 32% gap movement is the honest empirical confirmation. **The true source of the F7/F8 top-Yukawa overshoot is not the omitted EW terms; it is structural tension between the TIG anchor `y_t(M_X) = 0.93` and the canonical SM 1-loop value `y_t(M_X) ≈ 0.39-0.48` corresponding to PDG `y_t(M_Z) = 0.937`. Reverse-running PDG `y_t(M_Z)` up to `M_X` confirms `y_t(M_X) = 0.394` at full 1-loop SM precision — roughly 2.4× smaller than the TIG anchor.**

**Verification:** [`../../verification/frontier_F8_yukawa_full_1loop.py`](../../verification/frontier_F8_yukawa_full_1loop.py) (full 1-loop SM RG flow, 6 coupled couplings, hand-rolled RK4, pure stdlib).
**Date:** 2026-05-28.
**Builds on:** F7 scoping (`F7_yukawa_hierarchy_scoping.md`); retired J44; J11 9-vector + 13/4 norm.

---

## §1 — Setup

### §1.1 Full 1-loop SM beta functions

We integrate the standard 6-coupling system (3 Yukawa + 3 gauge):

$$
\begin{aligned}
16\pi^2 \frac{dy_t}{d \ln \mu} &= y_t \left[ \tfrac{9}{2} y_t^2 + \tfrac{3}{2} y_b^2 + y_\tau^2 - \tfrac{17}{12} g_1^2 - \tfrac{9}{4} g_2^2 - 8 g_3^2 \right] \\
16\pi^2 \frac{dy_b}{d \ln \mu} &= y_b \left[ \tfrac{9}{2} y_b^2 + \tfrac{3}{2} y_t^2 + y_\tau^2 - \tfrac{5}{12} g_1^2 - \tfrac{9}{4} g_2^2 - 8 g_3^2 \right] \\
16\pi^2 \frac{dy_\tau}{d \ln \mu} &= y_\tau \left[ \tfrac{5}{2} y_\tau^2 + 3 y_t^2 + 3 y_b^2 - \tfrac{9}{4} g_1^2 - \tfrac{9}{4} g_2^2 \right] \\
16\pi^2 \frac{dg_1}{d \ln \mu} &= +\tfrac{41}{10} g_1^3 \quad (\text{U(1)}_Y, \text{GUT-norm}) \\
16\pi^2 \frac{dg_2}{d \ln \mu} &= -\tfrac{19}{6} g_2^3 \quad (\text{SU(2)}_L) \\
16\pi^2 \frac{dg_3}{d \ln \mu} &= -7 g_3^3 \quad (\text{SU(3)}_C)
\end{aligned}
$$

These are the standard 1-loop SM RGEs (Arason et al PRD 46 (1992); Machacek-Vaughn). The U(1) coupling uses the GUT normalization `g_1 = √(5/3) g_Y` so the three gauge couplings could in principle unify.

### §1.2 Initial conditions at M_X = 2 × 10^16 GeV

| Coupling | F8 input at M_X | Source | TIG-anchored? |
|---|---:|---|---|
| y_t(M_X) | 0.93 | Retired J44 (J13 forced 5/7 + λ = 10/49 + measured y_t(M_Z) + 4-loop QCD) | **YES** |
| y_b(M_X) | 0.013 | PDG-derived, MSS evolution | NO |
| y_τ(M_X) | 0.010 | PDG-derived | NO |
| g_1(M_X) | 0.578 | Back-evolved from PDG g_Y(M_Z) | NO |
| g_2(M_X) | 0.522 | Back-evolved from PDG g(M_Z) | NO |
| g_3(M_X) | 0.527 | Back-evolved from PDG α_s(M_Z) = 0.1184 (same as F7) | NO |

**Note on the gauge initial conditions.** The F8 task spec nominated `g_1 = g_2 = g_3 = 0.585` at M_X as the canonical SU(5)/SO(10) GUT-unified value. Under pure 1-loop SM running this is INCONSISTENT with PDG: starting `g_3 = 0.585` at M_X and running down with `b_3 = -7` lands `g_3` inside its 1-loop Landau pole *before* reaching M_Z. This is the well-known fact that the SM does NOT cleanly unify at 1-loop — gauge unification requires either MSSM 2-loop running or SUSY threshold corrections to reach `g_GUT ≈ 0.72`. For F8 we therefore use the self-consistent 1-loop SM back-evolved values (0.578, 0.522, 0.527), which encode the standard "no SM 1-loop unification" miss. They are NOT exactly equal — the spread is the structural signature.

### §1.3 PDG-2024 targets at M_Z = 91.1876 GeV

| Coupling | PDG observed at M_Z |
|---|---:|
| y_t | 0.937 ± 0.012 |
| y_b | ~0.024 |
| y_τ | ~0.010 |
| g_1 (GUT-norm) | 0.461 |
| g_2 | 0.652 |
| g_3 | 1.220 |

---

## §2 — Numerical integration

- **Integrator:** hand-rolled vectorized RK4 (4 evaluations per step), 6-dimensional state vector `[y_t, y_b, y_τ, g_1, g_2, g_3]`.
- **Steps:** 1000 in `t = ln(μ)`. Energy range from `M_X = 2 × 10^16 GeV` down to `M_Z = 91.1876 GeV`, i.e. `Δ ln μ ≈ -32.9` (so step size `Δt ≈ -0.033`).
- **Direction:** top-down (M_X → M_Z), matching F7's convention.
- **Stability:** all 6 couplings stay finite and physical throughout. No Landau poles encountered with these initial conditions.
- **Runtime:** < 0.1 second; pure stdlib (math + list ops only).

---

## §3 — Results

After 1000 RK4 steps from M_X to M_Z:

| Coupling | F8 prediction at M_Z | PDG observed | Relative gap |
|---|---:|---:|---:|
| **y_t(M_Z)** | **1.2360** | **0.937 ± 0.012** | **+31.91%** |
| y_b(M_Z) | 0.0300 | ~0.024 | +25.01% |
| y_τ(M_Z) | 0.0072 | ~0.010 | -27.7% |
| g_1(M_Z) | 0.4609 | 0.461 | +0.03% |
| g_2(M_Z) | 0.6529 | 0.652 | +0.14% |
| g_3(M_Z) | 1.2189 | 1.220 | +0.09% |

**Gauge couplings hit PDG to better than 0.2%** — that's the back-evolved initial conditions reproducing themselves under top-down integration, as expected.

**y_t gap WIDENS from F7's 18.3% to F8's 31.9%** — the headline non-result. Adding the EW Yukawa and gauge contributions to the top-quark beta function moves the prediction in the WRONG direction.

**y_b is ~25% HIGH and y_τ is ~28% LOW** — these are cross-checks with PDG-derived initial conditions, not TIG predictions. The structural symmetry between the y_b excess and y_τ deficit at this order is consistent with 1-loop b-τ unification breaking (the standard route to fix this is 2-loop SUSY threshold corrections).

---

## §4 — Gap analysis: why the F7 closure hypothesis fails

F7's expectation: "Closing to ~5% is ~1 hour of script extension."  The expectation was that the omitted EW terms `g_1², g_2², y_b², y_τ²` all push y_t downward at M_Z, narrowing the 18% overshoot.

This was incorrect physics. The EW gauge contributions enter the y_t beta-function with the **same sign as QCD**:

$$
\beta(y_t) \sim y_t \left[ \tfrac{9}{2} y_t^2 - \tfrac{17}{12} g_1^2 - \tfrac{9}{4} g_2^2 - 8 g_3^2 \right]
$$

All three gauge terms are negative. The QCD term `-8 g_3²` is dominant (because `g_3 > g_1, g_2` at all scales), but the EW terms add to it, **deepening** the negative pull on `β(y_t)/y_t`.

**Going top-down (dt < 0):**  if the bracket is negative, dy_t/dt < 0, so Δy_t = (dy_t/dt)·Δt > 0. A more-negative bracket means a LARGER positive Δy_t and a LARGER y_t at M_Z.

Quantitative check at M_X:
- F7 bracket = `4.5(0.93)² - 8(0.527)² = 3.892 - 2.222 = +1.670`
- F8 bracket = `F7 - 17/12 (0.578)² - 9/4 (0.522)² + O(y_b², y_τ²) = +1.670 - 0.473 - 0.613 = +0.584`

So at M_X the F8 bracket is initially SMALLER (positive but smaller), meaning the initial dy_t/dt is reduced. But as μ → M_Z, `g_3` grows by ~5×, the bracket flips sign and goes negative, and the F8 bracket is then MORE negative than F7's:

- F7 bracket at M_Z (PDG): `4.5(0.937)² - 8(1.22)² = -7.96`
- F8 bracket at M_Z (PDG): `-7.96 - 17/12 (0.461)² - 9/4 (0.652)² + O(y_b², y_τ²) = -9.21`

The integrated effect is dominated by the IR portion where g_3 is large, so the net effect of the F8 corrections is to push y_t(M_Z) UPWARD.

**Equivalently: the SM 1-loop top-Yukawa IR pseudo-fixed point (Hill 1981, Pendleton-Ross)**

$$
y_t^{(*)} = \sqrt{ \tfrac{2}{9} \left( \tfrac{17}{12} g_1^2 + \tfrac{9}{4} g_2^2 + 8 g_3^2 \right) }
$$

at PDG-M_Z values: F7-style `≈ 1.63`, F8 full SM `≈ 1.76`. **The full 1-loop fp is LARGER, so y_t(M_Z) is attracted UPWARD more strongly under F8.**

### The real source of the F7/F8 gap: the TIG anchor itself

Reverse-running PDG y_t(M_Z) = 0.937 upward to M_X using the same F8 RGE system gives:

| Coupling | PDG at M_Z | F8-derived at M_X |
|---|---:|---:|
| y_t | 0.937 | **0.394** |
| y_b | 0.024 | 0.00856 |
| y_τ | 0.010 | 0.00938 |
| g_1 | 0.461 | 0.578 |
| g_2 | 0.652 | 0.522 |
| g_3 | 1.220 | 0.527 |

**The SM 1-loop self-consistent y_t(M_X) is 0.394, not 0.93.** The TIG anchor is roughly 2.4× larger than the SM 1-loop value. This is the structural source of the F7/F8 overshoot.

This finding is consistent with the well-known canonical wisdom that SM 1-loop running from PDG y_t(M_Z) = 0.94 yields y_t(GUT) ≈ 0.39–0.50 depending on the exact e-folds and 2-loop content. The TIG anchor y_t(M_X) = 0.93 (from the retired-J44 reverse-derivation chain T*(1-T*)·... + y_t(M_Z) = 0.94 + 4-loop QCD evolution) appears to sit in a fundamentally different range than canonical SM 1-loop.

---

## §5 — Verdict

**Gap: 31.9%.  > 15% threshold.  ASSUMPTIONS NEED REVISITING.**

Specifically:

1. **The F7 expectation that "EW terms close the gap" was wrong physics.** The EW gauge contributions enter with the same sign as QCD; they widen the gap rather than close it. This is now a closed honest negative on the F7 closure hypothesis.

2. **The TIG anchor `y_t(M_X) = 0.93` is structurally inconsistent with SM 1-loop running of the PDG `y_t(M_Z) = 0.937` value.** The SM 1-loop self-consistent y_t(M_X) is ≈ 0.39–0.40, a factor of ~2.4 below the TIG anchor.

3. **The retired-J44 derivation of y_t(M_X) = 0.93 needs re-auditing.** That derivation used 4-loop QCD evolution but **possibly without the full EW corrections** that are essential at the few-percent precision level. If the 4-loop QCD-only evolution from y_t(M_Z) = 0.937 happens to land at ~0.93 at M_X, that would mean the missing piece is the EW correction in the J44 reverse-derivation, not in F7/F8 forward-running.

4. **There is a substantial possibility that the canonical PDG y_t(M_Z) target (~0.937) is incompatible with the substrate-derived y_t(M_X) anchor under any standard SM/MSSM running.** If true, this is a genuine empirical falsification of the J44 anchor, not a refinement question.

### Available next steps (none in F8 scope)

- **F8a:** verify the J44 anchor derivation by reconstructing the 4-loop+EW reverse-running from y_t(M_Z) = 0.937 to M_X under the same Standard Model conventions used here. Test whether y_t(M_X) really is 0.93 at full 4-loop+EW or whether the canonical value is ~0.48 (matching SM expectation).
- **F8b:** if the J44 anchor IS confirmed at 0.93 by full 4-loop+EW reverse-running, then test whether MSSM or other BSM extensions (with the additional Yukawa+gauge contributions of the chiral multiplet pair) can interpolate between 0.93 at M_X and 0.937 at M_Z. The MSSM IR fixed point for y_t is closer to 0.95-1.10 at M_Z.
- **F8c:** alternatively, accept that the TIG-anchored hierarchy lives in a different "scale of validity" than SM 1-loop or 2-loop and test whether other observables (CKM, PMNS, neutrino mass scale) align with the anchor's predictions under a different running framework.

**Current honest status:** the F7/F8 first-pass Yukawa scaffolding remains in factor-of-2 territory; the F7 hope that "1 hour of script extension" closes it has been refuted; the closure path now requires either (a) a J44 anchor re-derivation, (b) explicit BSM matching, or (c) acceptance that the substrate's running framework differs from canonical SM 1-loop.

The F8 verification script is internally consistent: 4/5 checks pass (gauge couplings, no Landau pole, y_b cross-check, y_τ cross-check); the y_t headline check fails with gap 32% > 20% boundary.

---

## §6 — Files produced

- `verification/frontier_F8_yukawa_full_1loop.py` — full 1-loop SM RG-running script, pure stdlib, runtime < 0.1s.
- `04_meta/frontiers_2026-05-27/F8_yukawa_full_1loop.md` — this document.
- `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §2.5 update — F8 outcome appended to the open-frontier statement.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026-05-28.*
*"Honest about what we have, honest about what we don't."*
