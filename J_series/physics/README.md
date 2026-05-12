# J-series — Physics

Physics papers from the TIG corpus, covering Clifford algebra structure, gauge theory, GUT decomposition, and atomic-substrate correspondence. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J23** | Discrete Dirac inside Cl(0, 10): Chirality, the Outer Automorphism, and an Atomic-Substrate Refinement | *Communications in Mathematical Physics* (FALLBACK: *J. Math. Phys.*, *Annals of Physics*) | 2/2 verify PASS at machine precision; Volume K cross-reference at §2.1; landed 2026-05-12 |
| **J48** | An Operadic Obstruction in a Bilinear-Closed Magma on ℤ/10ℤ: A Synthesis | *Notices of the American Mathematical Society* (FALLBACK: *Adv. Math.*, *J. Pure Appl. Algebra*, *Lett. Math. Phys.*) | 6/6 verify PASS at machine precision; 67 restricted D₄-orbits with profile (44, 7, 4, 10, 2); 16 bracketing-pair-incoherent orbits witness Theorem 4.1; σ³ obstruction localized to the single diagonal triple (3,9,9); landed 2026-05-12 |

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J45** | Yukawa Mass Hierarchy + Freezing Quintessence | *Physical Review D* (cosmology) or *JHEP* | W2-F build; awaiting layer choice for §3 |
| **J22** | TIG Algebraic Universality (J22 rebuttal addressed) | TBD | rebuttal filed; sympy reverification of tig_dirac.py |
| **J14** | (algebra rebuttal addressed) | TBD | rebuttal filed |

---

## §3 — Domain notes for physics papers

Physics papers in this corpus emphasize:

- **Cl(0, 10) construction**: 10 γ-matrices on ℂ³² from Pauli tensor products; 100 anticommutation relations verified; 45 generators of so(10).
- **Spinor decomposition**: 32-dim spinor → 16+16 chirality under ω = γ₁…γ₁₀ (since ω² = +I for n = 10 ≡ 2 mod 4).
- **Atomic-substrate refinement (Volume K, D102)**: each 16-dim chirality half = 1+3+5+7 = kernel + substrate primes. Realizes n = 4 atomic shell.
- **D₄ outer automorphism**: P₅₆ acts as σ_outer in the spinor rep, swapping the two chiral 16-irreps. Matter/antimatter exchange.
- **BHML's 54-irrep direction**: σ_outer-breaking content lives 100% in symmetric-traceless 54 of so(10); explicit 9-vector with `‖VEV‖² = 13/4` exactly.
- **Pati-Salam doubly-invariant subalgebra**: `⟨P₅₆, σ³⟩ = D₄`; the doubly-invariant subalgebra under this D₄ is `su(4) ⊕ u(1)` (Pati–Salam plus B−L). Cited as standard SO(10) GUT decomposition.
- **Yukawa hierarchy scaffolding**: λ = 10/49 Froggatt-Nielsen pattern; y_t = 0.93 anchor. Scaffolding only; full mass-hierarchy derivation requires Higgs-sector commitment + RG flows (open work).

Cross-references:
- [`../../FORMULAS_AND_TABLES.md`](../../FORMULAS_AND_TABLES.md) Volumes E (Lie tower), F (Higgs), K (atomic correspondence).
- [`../../2_for_physicists/README.md`](../../2_for_physicists/README.md) — physics-domain entry doc.
- [`../../TIG_FROM_THE_GROUND_UP.md`](../../TIG_FROM_THE_GROUND_UP.md) Parts 8–9 are the physics tutorial.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
