# Frontier F15 — Yukawa with proper M_Z anchor (M_Z → M_X upward running)

**Status:** RG-RUNNING COMPLETE. **Verdict: SUBSTRATE INDEPENDENT (leaning), formally INDETERMINATE.** Anchoring `y_t(M_Z) = 0.93` correctly at M_Z (per F11 audit) and integrating the full 1-loop SM RGE system UPWARD via RK4 yields `y_t(M_X) = 0.3874` at canonical GUT-norm initial conditions (matching F8's reverse-run `0.394` to within 1.67% — the standard SM 1-loop canonical value). The closest substrate-derived candidate is `g_GUT/sqrt(2) ~ 0.4101` at 5.86% gap, but this is a *standard physics* anchor (using the canonical `g_GUT = 0.58` from 1-loop gauge-coupling near-unification), not a substrate-distinguished value. The two cleanest substrate-distinguished candidates — `sqrt(10/49) = sqrt(10)/7 ~ 0.4518` (gap 16.6%) and `(10/49)^(2/3) ~ 0.3466` (gap 10.5%) — both miss by >10%. **No clean substrate first-principles value matches y_t(M_X) within the 5% precision target.** The TIG framework's substrate-derived FN-slope `lambda = 10/49` and 9-vector norm `||v||^2 = 13/4` describe the M_Z-scale FN ladder (per retired-J44) and the SO(10) Higgs sector (per J11); the GUT-scale top-Yukawa value is **RG-determined from the measured M_Z anchor**, not substrate-determined. This closes the F7/F8/F11/F15 Yukawa-RG arc as **honest scoping with no GUT-scale substrate prediction**.

**Verification:** [`../../verification/frontier_F15_yukawa_upward.py`](../../verification/frontier_F15_yukawa_upward.py) (full 1-loop SM RG flow, 6 coupled couplings, hand-rolled RK4, pure stdlib).
**Date:** 2026-05-29.
**Builds on:** F7 scoping (`F7_yukawa_hierarchy_scoping.md`); F8 1-loop SM RGE (`F8_yukawa_full_1loop.md`); F11 audit (`F11_J44_yt_anchor_audit.md`); retired J44; J11 9-vector + 13/4 norm.

---

## §1 — Setup (M_Z anchor + canonical SM RGEs)

### §1.1 Per F11 audit: anchor lives at M_Z, not M_X

The F11 audit established that:
1. The retired-J44 manuscript anchors `y_t(M_Z) ~= 0.93` (Tier-A measured, PDG-derived `y_t(M_Z) = 0.937` rounded to 0.93 — match at 0.75%).
2. J44 makes **no M_X commitment**; all 9 charged Yukawas live at M_Z via the FN ladder `y_X(M_Z) = y_t(M_Z) * lambda^{n_X}`.
3. F7/F8's "GUT-scale 0.93 anchor" was an unforced category error introduced by F7's misreading "evolved to GUT scale" without actually performing the evolution.

**The natural question that survives F11 is:** what is `y_t(M_X)` under standard SM RG running of the TIG anchor? Does the substrate framework predict that GUT-scale value, or is it RG-determined and independent of substrate first principles?

F15 is the corresponding upward-run RG computation.

### §1.2 Initial conditions at M_Z = 91.1876 GeV

All values from PDG 2024 except `y_t(M_Z) = 0.93` which is the TIG Tier-A rounded anchor:

| Coupling | Value | Source |
|---|---:|---|
| `y_t(M_Z)` | 0.93 | TIG Tier-A; retired J44 (= PDG 0.937 to 0.75%) |
| `y_b(M_Z)` | 0.024 | PDG (m_b(M_Z) running mass / v) |
| `y_tau(M_Z)` | 0.010 | PDG (m_tau / v with v = 246 GeV) |
| `g_3(M_Z)` | 1.221 | PDG (alpha_s(M_Z) = 0.1184) |
| `g_2(M_Z)` | 0.652 | PDG (SU(2)_L) |
| `g_1(M_Z)` | 0.461 | GUT-norm sqrt(5/3) g_Y; sin^2 theta_W = 0.231 |

**Note on g_1 normalization:** The F15 task prompt nominated `g_1 = 0.358`, which is the *un-normalized* `g_Y` (hypercharge in SM convention without GUT-norm rescaling). The canonical 1-loop SM RGE for `beta(y_t)` uses the GUT-normalized `g_1 = sqrt(5/3) g_Y ~ 0.461`, so that the U(1)_Y contribution `-17/12 g_1^2` is the standard form (matching F8). We ran BOTH conventions:

- **Run A (prompt-nominal g_1 = 0.358):** y_t(M_X) = 0.4049, g_1(M_X) = 0.4053. The U(1)_Y running is suppressed because g_1 starts smaller, so y_t is pulled less strongly downward through the EW terms; but g_1 also doesn't grow as much (the b_1 = 41/10 self-coupling is g_1^3 driven), so the net effect is a slightly higher y_t(M_X) under this convention.
- **Run B (GUT-norm g_1 = 0.461):** y_t(M_X) = 0.3874, g_1(M_X) = 0.5782. **This is the canonical convention** and matches F8's reverse-run within 1.67% (F8 reported 0.394 for the same direction starting from PDG 0.937; F15 starts from rounded 0.93).

We treat **Run B as primary** because it uses the canonical GUT-normalized U(1) and matches F8's standard 1-loop SM result. Run A is reported for completeness because the prompt nominated it.

### §1.3 1-loop SM beta functions (full 6-coupling system)

Same as F8 (Arason et al PRD 46 (1992); Machacek-Vaughn):

$$
\begin{aligned}
16\pi^2 \frac{dy_t}{d \ln \mu} &= y_t \left[ \tfrac{9}{2} y_t^2 + \tfrac{3}{2} y_b^2 + y_\tau^2 - \tfrac{17}{12} g_1^2 - \tfrac{9}{4} g_2^2 - 8 g_3^2 \right] \\
16\pi^2 \frac{dy_b}{d \ln \mu} &= y_b \left[ \tfrac{9}{2} y_b^2 + \tfrac{3}{2} y_t^2 + y_\tau^2 - \tfrac{5}{12} g_1^2 - \tfrac{9}{4} g_2^2 - 8 g_3^2 \right] \\
16\pi^2 \frac{dy_\tau}{d \ln \mu} &= y_\tau \left[ \tfrac{5}{2} y_\tau^2 + 3 y_t^2 + 3 y_b^2 - \tfrac{9}{4} g_1^2 - \tfrac{9}{4} g_2^2 \right] \\
16\pi^2 \frac{dg_1}{d \ln \mu} &= +\tfrac{41}{10} g_1^3 \\
16\pi^2 \frac{dg_2}{d \ln \mu} &= -\tfrac{19}{6} g_2^3 \\
16\pi^2 \frac{dg_3}{d \ln \mu} &= -7 g_3^3
\end{aligned}
$$

`g_1` is in GUT-norm (`g_1 = sqrt(5/3) g_Y`).

### §1.4 Integrator

Hand-rolled vectorized RK4 (4 evaluations per step) on the 6-dim state vector `[y_t, y_b, y_tau, g_1, g_2, g_3]`, 1000 log-mu steps, `t = ln(mu)` from `ln M_Z` UP to `ln M_X` (so `dt > 0`). Runtime < 0.1s, pure stdlib (math + list ops only).

---

## §2 — Numerical M_Z → M_X result

After 1000 RK4 steps from M_Z to M_X:

### Run B (canonical GUT-norm; primary)

| Coupling | Value at M_Z | Value at M_X | Standard SM expectation at M_X |
|---|---:|---:|---|
| **y_t** | **0.93 (TIG Tier-A)** | **0.3874** | ~0.39 (canonical 1-loop) |
| y_b | 0.024 | 0.00853 | ~0.0085 |
| y_tau | 0.010 | 0.00934 | ~0.0094 |
| g_1 (GUT-norm) | 0.461 | 0.5782 | ~0.58 |
| g_2 | 0.652 | 0.5215 | ~0.52 |
| g_3 | 1.221 | 0.5272 | ~0.53 |

**y_t(M_X) = 0.3874 under canonical SM 1-loop running of the TIG M_Z anchor.**

### Run A (prompt-nominal g_1 = 0.358; secondary)

| Coupling | Value at M_Z | Value at M_X |
|---|---:|---:|
| y_t | 0.93 | 0.4049 |
| g_1 | 0.358 | 0.4053 |
| (g_2, g_3) | (0.652, 1.221) | (0.5215, 0.5272) |

Run A's y_t(M_X) is slightly higher because the smaller g_1 throughout the run gives less U(1)_Y contribution to beta(y_t), suppressing the downward pull less strongly.

### Cross-check: F8 reverse-run consistency

F8's reverse integration of PDG `y_t(M_Z) = 0.937` to M_X gave `y_t(M_X) = 0.394`. F15 Run B starts from the rounded TIG value `0.93` (a 0.75% drop from PDG) and gives `0.3874` — a 1.67% match to F8 (the small difference is the 0.937 vs 0.93 starting value compounding through the run). **F15 Run B is consistent with the standard SM 1-loop canonical wisdom that `y_t(M_X) ~ 0.39 - 0.40`.**

---

## §3 — Substrate predictions to compare

The TIG framework provides three load-bearing substrate ingredients (per F7 §1 + retired J44):

1. **FN slope `lambda = T*(1 - T*) = (5/7)(2/7) = 10/49 ~ 0.2041`** (Tier-B substrate-forced; retired J44).
2. **9-vector norm `||v||^2 = 13/4 = 3.25`** exact (Tier-A; J11 Theorem 4.1).
3. **Joint coherence threshold `T* = 5/7`** (Tier-B; J13 Forced 5/7).

Plus the standard FN powers `n_X ∈ {0, 3, 5, 6, 7, 9}` from the V^⊗5 SU(5)-rep + sigma-orbit indexing of retired J44 Table 4.1.

### §3.1 Candidate values for y_t(M_X)

From these ingredients, the natural candidate values to test are:

| Candidate | Value | Source |
|---|---:|---|
| `lambda = 10/49` | 0.2041 | FN slope |
| `sqrt(10/49) = sqrt(10)/7` | 0.4518 | sqrt of FN slope |
| `(10/49)^(1/3)` | 0.5888 | cube root of FN slope |
| `(10/49)^(2/3)` | 0.3466 | two-thirds power |
| `10/(49^(2/3))` | 0.7383 | alt parsing |
| `1 - 10/49 = 39/49` | 0.7959 | complement |
| `||v||^2 = 13/4` | 3.250 | J11 norm-squared |
| `sqrt(13/4) = sqrt(13)/2` | 1.803 | J11 norm |
| `sqrt(13/4)/2 = sqrt(13)/4` | 0.9014 | half-norm |
| `1/sqrt(13/4) = 2/sqrt(13)` | 0.5547 | reciprocal |
| `4/13` | 0.3077 | reciprocal of norm-sq |
| `T* = 5/7` | 0.7143 | joint coherence |
| `1 - T* = 2/7` | 0.2857 | complement of T* |
| `sqrt(T*) = sqrt(5/7)` | 0.8452 | sqrt |
| `T*^2 = 25/49` | 0.5102 | T* squared |
| `(1-T*)^2 = 4/49` | 0.0816 | (1-T*) squared |

Plus two *standard physics* (not substrate-distinguished) anchors:
- `g_GUT/sqrt(2)` at `g_GUT = 0.58`: 0.4101 (the canonical "1-loop near-unification" gauge coupling divided by sqrt(2))
- `sqrt(4 pi / 40)` at `1/alpha_GUT = 40`: 0.5605 (canonical GUT coupling-strength normalization)

---

## §4 — Compatibility analysis

### §4.1 Closest matches (Run B, canonical GUT-norm)

Sorted by % gap from y_t(M_X) = 0.3874:

| Rank | Candidate | Value | Gap | Substrate-distinguished? |
|---:|---|---:|---:|---|
| 1 | `g_GUT/sqrt(2) [g_GUT = 0.58]` | 0.4101 | **5.86%** | NO (standard physics) |
| 2 | `(10/49)^(2/3)` | 0.3466 | 10.53% | YES (FN slope power) |
| 3 | `sqrt(10/49) = sqrt(10)/7` | 0.4518 | 16.61% | YES (sqrt FN slope) |
| 4 | `4/13` | 0.3077 | 20.58% | YES (1/||v||^2) |
| 5 | `1 - T* = 2/7` | 0.2857 | 26.25% | YES |
| 6 | `T*^2 = 25/49` | 0.5102 | 31.70% | YES |
| 7 | `1/sqrt(13/4)` | 0.5547 | 43.18% | YES |
| 8 | `sqrt(4 pi / 40)` | 0.5605 | 44.68% | NO (standard physics) |
| 9 | `lambda = 10/49` | 0.2041 | **47.32%** | YES (FN slope itself) |

### §4.2 Honest assessment

- The **closest match (5.86%)** is `g_GUT/sqrt(2)` — but this is **not a substrate-distinguished value**, it's the standard "canonical 1-loop near-unified gauge coupling" expression. Matching it is a tautology: F15's RG run reproduces standard SM 1-loop physics.
- The **closest substrate-distinguished candidate is `(10/49)^(2/3) = 0.3466` at 10.53%**. This is not a clean match: a 10% gap on a 0.04-magnitude quantity is dimensionally substantial.
- The **next-closest substrate-distinguished candidate is `sqrt(10/49) = sqrt(10)/7 = 0.4518` at 16.61%**. This is a clean rational-substrate value (just the square root of the FN slope) but the gap is too large.
- **`lambda = 10/49 = 0.2041` itself sits at 47% gap** — half the y_t(M_X) value, not a match.

### §4.3 Why no clean substrate match should be expected

The TIG framework's substrate ingredients (lambda, T*, ||v||^2) live in *dimensionless rational/algebraic-number space*. The top-Yukawa value at M_X is determined by:

1. The IR boundary condition `y_t(M_Z)` (set by PDG measurement, anchored to substrate via Tier-A rounding).
2. The full 1-loop SM RG running between M_Z and M_X — which depends on **g_1, g_2, g_3 at all scales, plus y_b and y_tau** as cross-coupling sources in beta(y_t).
3. The 32.9 e-folds of RG drift between scales — a large multiplicative factor.

For y_t(M_X) to *equal* a clean substrate-derived rational, the cumulative RG drift would have to land on that rational. There's no structural reason for this to happen: the substrate doesn't constrain the SM gauge couplings at M_X, doesn't constrain the alpha_s value at M_Z, doesn't constrain v_EW = 246 GeV. **Standard SM physics determines y_t(M_X) from y_t(M_Z), and the substrate is silent about that determination.**

### §4.4 Run A (g_1 = 0.358) result

For Run A, y_t(M_X) = 0.4049 and the closest substrate-derived value is again `g_GUT/sqrt(2) = 0.4101` at 1.30% gap. This is a coincidentally tight match — but the prompt's `g_1 = 0.358` is the un-normalized hypercharge, NOT the canonical GUT-norm. Run A is a numerical artifact of the non-canonical g_1 normalization, not a real substrate prediction. Run B is the physically correct comparison.

---

## §5 — Conclusion

**Verdict: SUBSTRATE INDEPENDENT (leaning), formally INDETERMINATE at the literal threshold.**

The verification script tags the verdict as `INDETERMINATE` because Run B's closest substrate candidate (`(10/49)^(2/3) ~ 0.3466`) sits at 10.5% gap — just inside the script's 15% INDETERMINATE band but well outside any 5% or 1% substrate-match threshold. Substantively, however:

1. **The closest match (5.86%) is `g_GUT/sqrt(2)`, a *standard physics* anchor.** Matching it is just F15 reproducing canonical SM 1-loop running of the M_Z anchor — i.e. reproducing F8's reverse-run result. This is sanity-check confirmation, not substrate explanation.

2. **No substrate-distinguished value matches y_t(M_X) within 10%.** The closest substrate-distinguished candidates are `(10/49)^(2/3)` (10.5%) and `sqrt(10)/7` (16.6%) — both too far for any first-principles claim.

3. **The substrate's load-bearing rational ingredients (lambda = 10/49, T* = 5/7, ||v||^2 = 13/4) describe phenomena at M_Z** (the FN ladder per retired J44) and **structural Higgs-sector content** (J11's 9-vector inside the 54). They do not constrain or predict the GUT-scale top-Yukawa value, which is RG-determined from the M_Z anchor under canonical SM running.

4. **There is no F7-style hope that "1 hour of script extension" would close to a substrate match.** The cumulative RG drift between M_Z and M_X is determined by the standard SM gauge sector and the cross-coupling Yukawas, none of which are substrate-distinguished. The 0.39 → 0.41 region is where canonical SM physics lands; whether that region "rhymes" with `g_GUT/sqrt(2)` is a question for canonical GUT phenomenology, not for the TIG framework.

### §5.1 What F15 closes

- **The proper M_Z → M_X upward RG run with the correctly-anchored Tier-A `y_t(M_Z) = 0.93`** produces `y_t(M_X) = 0.3874` under canonical 1-loop SM running.
- **This value matches F8's reverse-run within 1.67%**, confirming F11's audit conclusion that F8's "32% overshoot" was an anchor mislabel and the actual SM 1-loop result is uncontroversial.
- **No substrate-derived first-principles value matches y_t(M_X) to better than 10%.** The substrate explains the M_Z-scale FN-ladder structure (per J44); it does not predict the GUT-scale top-Yukawa value.

### §5.2 What F15 leaves open

- **The substrate-origin of the FN-power assignments `n_X`** (retired J44's Tier-B SU(5)-rep + sigma-orbit indexing) — open since F7 §7 #1.
- **The C_p residual multipliers** (retired J44; Tier-C empirical) — open since F7 §7 #2.
- **The right-handed neutrino sector / 126-Higgs** (deferred per retired-J44 save plan) — open since F7 §7 #3.
- **The two-scale `lambda = 10/49` vs `lambda_ref = 11/49` unification** (open since F7 §7 #4).
- **The 2-loop SO(10) RGE with SARAH + SPheno** — multi-year SARAH/SPheno work, still required for a publishable hierarchy completion.

### §5.3 The Yukawa-RG arc closes

F7 → F8 → F11 → F15 is now a closed arc. The arc establishes:

- The TIG anchor `y_t(M_Z) = 0.93` matches PDG `y_t(M_Z) = 0.937` at 0.75%.
- The substrate-derived `lambda = 10/49` populates the M_Z FN ladder per retired-J44 (Tier-B).
- The GUT-scale value `y_t(M_X) ~= 0.39` is RG-determined by canonical SM 1-loop running, independent of substrate first principles.
- F7/F8's earlier "GUT-scale overshoot" was an anchor mislabel (F11 audit) and not a substrate-vs-SM tension.

**The Yukawa hierarchy frontier remains open at the full hierarchy completion level** (per F7 §7), but the M_X anchor question is honestly scoped: it's *standard SM RG result from a Tier-A measured M_Z anchor*, not a substrate prediction.

---

## §6 — Files produced

- `verification/frontier_F15_yukawa_upward.py` — full 1-loop SM RG flow, M_Z → M_X upward integration, dual gauge-norm runs, substrate candidate comparison, pure stdlib (runtime < 0.1s).
- `04_meta/frontiers_2026-05-27/F15_yukawa_proper_anchor.md` — this document.
- `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §2.5 — append F15 outcome to the Yukawa-frontier open-statement.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026-05-29.*
*"Honest about what we have, honest about what we don't — and honest about which scale the substrate constrains."*
