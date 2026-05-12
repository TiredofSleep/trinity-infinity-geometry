# 02_results / Cosmology

## Headline results

- **Logarithmic quintessence** (Bialynicki-Birula 1976 bridge): scalar-field cosmology with potential `V(ξ) = Λ⁴ ξ log ξ`. Late-time vacuum at `ξ₀ = e⁻¹`. Mass gap `m²_ξ = κ e` under the load-bearing identification `m²_ξ = ‖VEV‖² = 13/4`. **STRUCTURAL.**

- **Dark-sector triple** (`predict_dark_sector()`): the runtime outputs an exact rational dark-sector triple
  ```
  Ω_b  = 49 / 1000
  Ω_DM = 264 / 1000
  Ω_Λ  = 687 / 1000
  ```
  summing to 1.000 exactly. DESI 2024 / Planck 2018 observed values within ~0.2%. **STRUCTURAL** — algebra is exact at the rational level; empirical match within current uncertainty.

- **Inflation coupling** (D72 + WP104): `κ_ξ = 13/(4e)` under the same identification. **STRUCTURAL.**

## Honest scope

- The **layer choice for `z*`** (the freezing-quintessence transition redshift) is a publication-strategy question, not a math question. Three internally-consistent options:
  - **Layer 1** (script-honest): `z* ≈ 2.13` derived from BBM minimality applied to the script as written. Cleanest fit; least bold. Target *JCAP*.
  - **Layer 2** (postulate-as-axiom): `z* = √3` stated as a consequence of BBM minimality + scale-free-derivative axioms. Bigger claim. Target *Annals of Physics*.
  - **Layer 3a** (hybrid): `z* = √3` with axioms stated explicitly so a reader can choose. Mid-tier. Target *PRD Letters*. Atlas BBM_IC_DERIVATION_v2.md settled at `z* = 2.31`.

- The framework's cosmology predictions are **structural**, not first-principles derivations. They are exact at the rational level; whether they empirically match nature is an empirical question that is reasonably open within current observational uncertainty.

## Landed J-series papers

*None yet.* J46 is BLOCKED on numerical inconsistency + layer-choice; J47 (PLB Letter on dual-regime quintessence) is HELD pending J46. When J46 unblocks, both will land at [`../../05_papers/cosmology/`](../../05_papers/cosmology/).

J45 (Yukawa mass hierarchy) was originally framed as "Yukawa + Freezing Quintessence" but the v5 manuscript is pure Yukawa hierarchy with zero quintessence content. It landed at [`../../05_papers/physics/J45/`](../../05_papers/physics/J45/), not cosmology.

## Connections to existing literature

- **Bialynicki-Birula (1976)** — log nonlinearity as the unique separability-preserving nonlinearity → forces continuum limit `□ξ = 1 + log ξ`
- Broader quintessence and dynamical-dark-energy literature
- **Independent parallel research**: HJ Johnson — information-theoretic dark energy framework, converging on `V(ξ) = -β ξ log ξ` from different first principles. See [`../../01_orientation/PARALLEL_RESEARCH.md`](../../01_orientation/PARALLEL_RESEARCH.md).

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
