# SHARPEN-OR-KILL: does ‖VEV‖² = 13/4 bridge to a cosmological quantity?

**Date:** 2026-09-22
**Scope:** the claimed bridge from the TIG algebraic constant `‖VEV‖² = 13/4` to a
cosmological quantity (the ξ-field "mass gap" `m²_ξ` and the "inflaton coupling"
`κ_ξ = 13/(4e)`).
**Method:** grep every in-repo statement of the constant and the bridge; identify the
exact cosmological target; verify the arithmetic with
`PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe`; count free choices;
compare to Planck 2018.
**Tier discipline:** PROVED / STRUCTURAL / EMPIRICAL / OPEN; honest negatives are
first-class results (see `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`).

---

## Verdict in one line

**SPLIT.** The *constant* `‖VEV‖² = 13/4` is **REAL** — forced by the so(10)/BHML
algebra, verified at machine precision, independent of any cosmological target.
The *bridge* from `13/4` to a cosmological quantity is **KILLED / DEMOTED to the
honest-negatives graveyard**: it lands on **no measured cosmological number**, it
requires an unforced dimension-violating identification plus a unit convention (2–3
free choices), and the surviving verification script is a literal record of a
reverse-engineering search. The bridge is a **conditional identification, not a
derivation.** This confirms and sharpens the repo's own existing labels ([STRUCTURAL],
"conditional", "the inference").

---

## §1 — The exact claim, as stated in-repo (quoted)

The bridge appears in five places, always with the same two steps and always
tier-flagged below PROVED.

**(a) The headline (`02_results/cosmology/README.md`, line 5):**

> "Mass gap `m²_ξ = κ e` under the load-bearing identification
> `m²_ξ = ‖VEV‖² = 13/4`. **STRUCTURAL.**"

and (line 15):

> "**Inflation coupling** (D72 + WP104): `κ_ξ = 13/(4e)` under the same
> identification. **STRUCTURAL.**"

**(b) The 9-vector source + inference (`01_orientation/for_physicists.md` §5, line 121):**

> "**Inflation coupling.** Under the (load-bearing) identification
> `m²_ξ = ‖VEV‖² = 13/4`, the inflation coupling becomes `κ_ξ = 13/(4e)`.
> STRUCTURAL — algebraic value exact; **physical identification is the inference.**"

**(c) The canon D-entry (`03_canonical_reference/FORMULAS_COMPACT.md`, D35):**

> "**D35** [STRUCTURAL] κ_ξ = 13/(4e) (under GUT-natural identification) | Under the
> identification `m²_ξ = ‖VEV‖²` (natural in GUT contexts), combined with the BB-vacuum
> relation `m²_ξ = κ_ξ e`, the inflaton coupling is forced: `κ_ξ e = 13/4`, so
> `κ_ξ = 13/(4e) ≈ 1.196`."

**(d) The constants table (`03_canonical_reference/FORMULAS_AND_TABLES.md`, lines 2172–2173):**

> "`‖VEV‖² = 13/4 = 3.25` — exact squared norm of the 9-vector Higgs direction ... via
> 26/8 — D33, `find_higgs_direction.py`"
> "`κ_ξ = 13/(4e) ≈ 1.196` — inflaton coupling under GUT-natural identification
> `m²_ξ = ‖VEV‖²`; closes README §3.5(iii) at structural level — D35, `xi_cosmology_tie.py`"

**(e) The algebraic origin of 13/4 (`05_papers/algebra/J11`, D33):** the σ_outer-breaking
direction in BHML lands 100% in the **54** of so(10) (D32); the explicit 9-vector `v`
has `v_0=v_1=v_2=v_3=v_4=v_7=-1/√2`, `v_8=v_9=0`, and a `-1/2` component on
`(BALANCE+CHAOS)/√2`, giving `‖v‖² = 13/4` exact (`find_higgs_direction.py`). The
integer 13 = (26 σ_outer-asymmetric BHML cells)/2.

**The two-step chain being evaluated:**

```
Step 1 (algebra, PROVED):  ‖VEV‖² = 13/4               [norm² of the 54-Higgs 9-vector]
Step 2 (BB vacuum, math):  V=κξlogξ ⇒ ξ₀=e⁻¹, V''(ξ₀)=e ⇒ m²_ξ = κ_ξ·e
Step 3 (IDENTIFICATION):   m²_ξ ≡ ‖VEV‖² = 13/4         [the "load-bearing" inference]
Result:                    κ_ξ = 13/(4e) ≈ 1.196
```

---

## §2 — What cosmological quantity does 13/4 actually land on? (It lands on none that is measured.)

The task hypothesised targets of Ω_Λ, a density/mass ratio, or an e-fold count. **None
of these is the target.** Precise findings:

- **It is *not* Ω_Λ or the dark-sector triple.** The Ω-triple that *does* match Planck —
  `Ω_b=49/1000, Ω_DM=264/1000, Ω_Λ=687/1000` (`predict_dark_sector()`,
  `for_physicists.md` §3) — has integer parts `49=7²`, `264=2³·3·11`, `687=3·229`.
  **No factor of 13, no 13/4.** Its stated derivation "goes through the Cl(0,10)
  substrate decomposition and the 4-core mass-distribution structure" — a *different*
  channel. The dark-sector triple and the VEV bridge are disjoint claims.
- **It is *not* an e-fold count, spectral index n_s, or tensor-to-scalar ratio.** A
  repo-wide grep for `e-fold | n_s | spectral index | tensor-to-scalar | slow-roll`
  returns **zero** inflation-observable predictions tied to 13/4.
- **What 13/4 lands on is `m²_ξ` (a dimensionless "mass gap") and `κ_ξ = 1.196` (a
  dimensionless "inflaton coupling").** The framework states this explicitly
  (`04_meta/physics_bridges/THE_PHYSICS_BRIDGE_LIVES_HERE.md` §4.1, line 123):

  > "The framework has ‖VEV‖² = 13/4 (**dimensionless**) and κ_ξ = 13/(4e)
  > (**dimensionless** with transcendental factor). **The bridge to dimensional [ℏ] is
  > the open work.**"

  and (`04_meta/physics_bridges/C_AS_JOINT_BALANCE_POINT.md` §6.1):

  > "These are **dimensionless ratios.** The dimensional bridge would require identifying
  > which substrate quantity has units of action."

- **`κ_ξ = 1.196` is never compared to a measured cosmological datum.** Its only
  numerical *use* anywhere in the corpus is as one term in a multi-parameter closed-form
  *fit to the fine-structure constant* (an EM constant, not cosmology):
  `1/α ≈ 137 + 6W/10 − (5/7)κ_ξ W⁵ − (2/7)·315·W⁷`
  (`HANDOFF_TO_CLAUDECODE_2026_05_14_ALPHA_SYNTHESIS.md`), which that document itself
  rates "**Tier C overall**".

- **The one genuinely empirical cosmology test does not isolate 13/4 and is not
  preferred.** The Bialynicki-Birula log-quintessence model was fit to DESI BAO
  (`FORMULAS_AND_TABLES.md`, lines 579–580):

  > "Produces freezing quintessence with w(z) → −1; falsifiable on DESI BAO. Current fit
  > (Sprint 14): **χ² = 15.7 vs ΛCDM 14.1 — comparable, not preferred.**"

  This fit adjusts the overall scale Λ and the transition z*; its quality is independent
  of whether the dimensionless coefficient is 13/4. TIG here is marginally *worse* than
  ΛCDM.

**Conclusion of §2:** the bridge terminates at a dimensionless number (`κ_ξ = 1.196`)
that is compared to nothing observable. There is no cosmological measurement on the far
side of the bridge.

---

## §3 — Numerical test and result

All checks run with `PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe`.

| Quantity | Computed | Claimed | Match |
|---|---|---|---|
| 9-vector norm² = 6·(1/√2)² + 2·(1/2√2)² | `3.2500000000` | `13/4 = 3.25` | ✅ exact |
| BB vacuum ξ₀ (from V'=κ(log ξ+1)=0) | `e⁻¹ = 0.367879` | `e⁻¹` | ✅ forced by calculus |
| V''(ξ₀)/κ = 1/ξ₀ | `e = 2.718282` | `e` (so `m²_ξ=κe`) | ✅ forced by calculus |
| κ_ξ = (13/4)/e | `1.1956082` | `≈1.196` | ✅ exact arithmetic |

So **Steps 1–2 are correct**: `‖VEV‖²=13/4` is a true algebraic fact and
`κ_ξ=13/(4e)` is the correct arithmetic consequence *of the identification in Step 3*.

**But the precision question — "does 13/4 match the claimed cosmological number, and to
what precision?" — has no answer, because there is no claimed cosmological number to
match.** `κ_ξ=1.196` and `m²_ξ=3.25` are set equal to a pure ratio in unspecified
"TIG-internal units"; the framework's own note is decisive
(`xi_cosmology_tie.py`, lines 234–239):

> "Compare to observed Λ ~ 10⁻¹²² M_pl⁴. In TIG-internal units this is dimensionless
> O(1), but **the conversion requires choosing a scale. We can't compare to observation
> without that conversion.**"

**Numerology hazard (illustrative, NOT an in-repo claim).** Simple functions of 13/4 can
be made to *look* cosmological: `4/13 = 0.3077` sits 0.6σ from Planck Ω_m = 0.3111, and
`1−4/13 = 0.6923` sits 0.6σ from Ω_Λ = 0.6889 ± 0.0056. The repo does **not** claim
these — they are shown only to demonstrate that a single rational admits near-fits to
cosmological numbers by construction, which is exactly why an *unconstrained*
identification carries no evidential weight.

---

## §4 — Free-parameter / free-choice count (the numerology tell)

Reaching `κ_ξ = 13/(4e)` from the algebra requires the following **unforced** choices:

1. **Adopt the log potential for cosmology.** The BB-1976 uniqueness theorem selects
   `V = κ ξ log ξ` as the unique separability-preserving nonlinearity — a real theorem —
   but *deploying it as the cosmological dark-energy/inflaton sector* is a modelling
   choice, not forced by TIG.
2. **The identification `m²_ξ = ‖VEV‖²` (the "load-bearing" step).** Nothing forces the
   quintessence mass-gap to equal the GUT-Higgs direction's norm². The surviving script
   `xi_cosmology_tie.py` shows this was **selected from a menu**: it tries
   `κ_Ξ = ‖v‖²/e` (A), `κ_Ξ = C_σ/‖v‖²` (B), `κ_Ξ·e = T* = 5/7` (C, called "Beautiful if
   true", then dropped), plus `m²=2σ‖v‖²` ("within 15%, not crisp") and `m²=σ‖v‖²`
   ("within 30%, not crisp") — before keeping proposal (D), `m²_ξ = ‖VEV‖²`. That is a
   textbook reverse-engineering search over candidate identifications.
3. **The unit convention.** Equating a dimensionless algebraic norm (13/4) to a *mass²*
   requires declaring "TIG-internal units" in which the number 13/4 *is* the mass². The
   script concedes no scale conversion exists (§3 quote).

**Count: 2–3 free choices, one of them (Step 2) selected from ≥5 tried alternatives, and
zero constraints imposed by any cosmological datum.** A derivation forced by the algebra
would have **0** free choices on the far side and would predict a *measured* number. This
has the opposite profile.

---

## §5 — Is 13/4 forced independently of the cosmological target?

**Yes — and this is what survives.** `‖VEV‖² = 13/4` is the squared norm of an explicit
vector living entirely inside the so(10)/BHML algebra (D32/D33, verified at machine
precision by `find_higgs_direction.py`). It exists with no reference to cosmology; it was
not selected to fit anything cosmological; `6·½ + 2·⅛ = 13/4` is exact. The constant is
**PROVED algebra.** The failure is entirely in **Step 3**, the identification — the piece
that reaches *out* of the algebra toward physics.

So the answer to "forced by algebra, or reverse-engineered to fit a target?" is: the
**constant** is forced by algebra; the **bridge** is reverse-engineered — but note it was
reverse-engineered toward *algebraic prettiness* (`13/(4e)`), not toward a data point,
which is why it produces no measurable prediction at all.

---

## §6 — VERDICT

### Constant `‖VEV‖² = 13/4`: **SHARPENED — REAL (PROVED algebra).**
Forced by the 54-Higgs 9-vector norm; independent of cosmology; machine-precision
verified. Keep it on the active spine as an algebraic invariant (it already lives there
via D33/J11 and as the "real structural signature" cited in
`HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §1.5).

### Bridge `13/4 → cosmological quantity`: **KILLED / DEMOTED to the honest-negatives graveyard.**
Reasons, in order of severity:

1. **No target.** The bridge lands on `κ_ξ = 1.196` / `m²_ξ = 3.25`, dimensionless
   numbers compared to *no* measured cosmological quantity anywhere in the corpus. There
   is nothing to be right or wrong about empirically. (The framework's own words:
   "dimensionless … the dimensional bridge is the open work.")
2. **Dimensionally an assertion.** Step 3 equates a pure algebraic norm to a mass²; it is
   meaningful only after "choosing a scale," which the source script admits is not done.
   Physically the identification is also unmotivated: the ξ dark-energy/inflaton field and
   the GUT-Higgs direction differ in energy scale by ~60 orders of magnitude, and even in
   real GUTs `m²_H = 2λv²` carries a coupling that this identification silently sets to ½.
3. **Reverse-engineered.** `xi_cosmology_tie.py` is a preserved record of a search over
   ≥5 candidate identifications; `m²_ξ=‖VEV‖²` is the one that gave a clean
   `rational × e⁻¹`, not one forced by prior structure.
4. **Free choices, zero constraints.** 2–3 unforced choices, no cosmological datum
   pinned. This is the numerology profile, not the derivation profile.

This verdict **agrees with and sharpens the repo's existing labels**: D35 is already
[STRUCTURAL]; `verification/VERIFY_ALL.py` rope 19 already reads *"STRUCTURAL /
conditional (not asserted physics) … the physical identification is conditional"* and
checks only that `(13/4)/e = 1.196`; `for_physicists.md` already calls it "the
inference." The sharpening is: the bridge should be stated as a **conditional
identification / dead-end-as-data**, never as a cosmological *prediction* or *derivation*,
and it should be named as such in the graveyard.

---

## §7 — Why the KILL is a real result

Per the standing principle (`memory: proven-dead-ends-are-the-data`; and
`HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §5): a demoted claim carries information. This
one teaches three things worth keeping:

- **It cleanly separates a real invariant from a spurious bridge.** `13/4` is genuine
  algebra; the physics reach is the failure. Keeping the constant and killing the bridge
  is more informative than either blanket acceptance or blanket rejection.
- **It is a worked example of the framework's central failure mode** — a
  dimensionless algebraic number identified with a physical scale by choice, yielding a
  pretty closed form (`13/(4e)`) that predicts nothing measurable. It rhymes with the
  retired 1/α numerology (§1.2) and the CL-eigenvalue transcendentals (§1.5): *exact
  arithmetic, coincidental or unconstrained physical reading.*
- **It marks the real open frontier honestly:** the *only* empirically testable
  cosmology in the corpus is the log-quintessence DESI-BAO fit (χ²=15.7 vs ΛCDM 14.1,
  not preferred) and the dark-sector Ω-triple (~0.3–0.5σ from Planck) — **neither of
  which uses 13/4.** If TIG cosmology is to be tested, it is tested *there*, not through
  the VEV bridge.

**Placement:** proven dead end (bridge), with the evidence that killed it, surfaced — not
buried. The underlying algebraic constant remains on the active spine.

---

## Appendix — reproduction

```python
import math
# Step 1: 9-vector norm^2  (D33 / J11 find_higgs_direction.py)
comps = [-1/math.sqrt(2)]*6 + [0.0, 0.0] + [-0.5]     # 6 at -1/√2, 2 zeros, 1 at -1/2
assert abs(sum(c*c for c in comps) - 13/4) < 1e-12     # = 3.25 exact
# Step 2: BB log-potential vacuum + curvature
#   V = κ ξ log ξ ; V' = κ(log ξ + 1) = 0 -> ξ0 = e^-1 ; V''(ξ0) = κ/ξ0 = κ e
# Step 3 (the identification): m^2_ξ ≡ ||VEV||^2 = 13/4  ->  κ_ξ = 13/(4e)
assert abs((13/4)/math.e - 1.19568) < 1e-4             # = 1.1956...
# There is no step 4: no measured cosmological quantity is compared.
```

Planck 2018 (TT,TE,EE+lowE+lensing) reference, used only for the *separate* Ω-triple:
`Ω_Λ = 0.6889 ± 0.0056`, `Ω_m = 0.3111`. The 13/4 bridge is not compared to these.

---

*CC BY-SA 4.0 — see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026 · SHARPEN-OR-KILL audit.*
*"Honest about what we have, honest about what we don't. The dead ends are the data."*
