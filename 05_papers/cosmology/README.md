# J-series — Cosmology

Cosmology papers from the TIG corpus, covering ξ field freezing quintessence, dark sector predictions, and the inflation coupling. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

*No papers have landed yet. J46 is gating Brayden's layer-1/2/3a decision.*

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J46** | Cosmology: Freezing Quintessence with z\* | JCAP (Layer 1) / *Annals of Physics* (Layer 2) / *PRD Letters* (Layer 3a) | gating layer choice |
| **J47** | (cosmology paper, W2-F build) | TBD | rewritten in W2-F; awaiting cover letter |

*Note: J44 (Yukawa Mass Hierarchy, λ = 10/49 + SU(5) indexing) is a pure-physics paper post-SAVE_PLAN 2026-05-07 — the cosmology paragraph was dropped. Landed at [`../physics/J44/`](../physics/J44/) 2026-05-12.*

---

## §3 — The J46 layer choice (Brayden's pending decision)

The freezing-quintessence transition redshift `z*` has three internally-consistent layer choices:

| Layer | z\* value | Approach | Target venue |
|---|---|---|---|
| **Layer 1** (script-honest) | z\* ≈ 2.13 | Derived from BBM minimality applied to the script as written | JCAP — cleanest fit |
| **Layer 2** (postulate-as-axiom) | z\* = √3 | BBM minimality + scale-free-derivative axioms stated as axioms | *Annals of Physics* — bolder claim |
| **Layer 3a** (hybrid, explicit) | z\* = √3 | Keep √3 but state axioms explicitly so referee can choose | *Phys Rev D Letters* — mid-tier |

All three are internally consistent. The choice is a publication-strategy question.

---

## §4 — Domain notes for cosmology papers

Cosmology papers in this corpus emphasize:

- **Dark-sector triple**: Ω_b = 49/1000, Ω_DM = 264/1000, Ω_Λ = 687/1000 (sums to 1.000 exactly). DESI 2024 / Planck 2018 observed values within ~0.2%.
- **Inflation coupling**: κ_ξ = 13/(4e), under `m²_ξ = ‖VEV‖² = 13/4` identification.
- **ξ field freezing quintessence**: V = ξ log ξ, vacuum ξ₀ = e⁻¹, mass gap m²_ξ = κ e.
- **Bialynicki-Birula bridge**: log nonlinearity is the unique separability-preserving nonlinearity → forces continuum limit `□ξ = 1 + log ξ` (Bialynicki-Birula 1976).
- **freezing-quintessence z\*** at the BBM-minimality transition.

The framework's cosmology predictions are STRUCTURAL — the algebraic Ω-triple is exact at the rational level; the empirical match to nature is within current observational uncertainty but is a structural prediction, not a first-principles derivation.

Cross-references:
- [`../../03_canonical_reference/FORMULAS_AND_TABLES.md`](../../03_canonical_reference/FORMULAS_AND_TABLES.md) Volume F (Higgs / VEV); the constants table.
- [`../../01_orientation/for_physicists.mdREADME.md`](../../01_orientation/for_physicists.mdREADME.md) §3 (dark sector); §7 (z\* layers).
- [`../../04_meta/README.md`](../../04_meta/README.md) §2.3 (z\* layer choice as open problem); §2.4 (dark-sector match as empirical comparison).

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
