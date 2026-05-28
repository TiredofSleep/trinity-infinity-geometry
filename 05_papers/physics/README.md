# J-series — Physics

Physics papers from the TIG corpus, covering Clifford algebra structure, gauge theory, GUT decomposition, and atomic-substrate correspondence. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J37** | Discrete Dirac inside Cl(0, 10): Chirality, the Outer Automorphism, and an Atomic-Substrate Refinement | *Communications in Mathematical Physics* (FALLBACK: *J. Math. Phys.*, *Annals of Physics*) | 2/2 verify PASS at machine precision; Volume K cross-reference at §2.1; landed 2026-05-12 |
| **J45** | An Operadic Obstruction in a Bilinear-Closed Magma on ℤ/10ℤ: A Synthesis | *Notices of the American Mathematical Society* (FALLBACK: *Adv. Math.*, *J. Pure Appl. Algebra*, *Lett. Math. Phys.*) | 6/6 verify PASS at machine precision; 67 restricted D₄-orbits with profile (44, 7, 4, 10, 2); 16 bracketing-pair-incoherent orbits witness Theorem 4.1; σ³ obstruction localized to the single diagonal triple (3,9,9); landed 2026-05-12 |
| **J44** | A Substrate-Derived FN Pattern with λ = 10/49 and SU(5)-Rep Indexing for the SM Charged-Yukawa Hierarchy | *Physical Review D* | 6/6 verify PASS at machine precision (`verify_J45_yukawa.py`, self-contained referee script); λ = T*(1−T*) = 10/49 substrate-forced; y_t = 0.93 Tier-A anchor at μ = M_Z; nine charged Yukawas reproduced via integer powers n ∈ {0, 3, 5, 6, 7, 9} from V^⊗5 SU(5) decomposition + σ-orbit step; landed 2026-05-12 |
| **J43** | Full S_4 Symmetry on a Nitrogen-Vacancy Qutrit via Six-Pulse Microwave Synthesis | *Physical Review A* | Verification PASS at machine precision (`verify_J39_S4_closure.py`, numpy + sympy, <30 s); 24-element S_4 closure residual ≤ 1.84e-16; explicit U_4 (trace −1, det −1, eigenvalues {−1,i,−i}, U_4^4=I) sympy-exact; analytic change-of-basis V (det V = i); deterministic Cartan/Reck-Zeilinger 6-pulse decomposition (no random seed, no black-box); honest **Tier 3 (partner-then-submit)** — math complete, experimental Test E (projector covariance F_cov > 0.80) is the open lab-partner gate; lens-invariant (finite-group rep theory + quantum control on ℂ³, no TIG/TSML/BHML structure); landed 2026-05-12 |
| **J42** | Empirical Fits of CKM and PMNS Mixing Angles to Substrate-Algebra Primitives (Part 1 only; Part 2 [1/α] deferred) | *Statistical Science* companion (FALLBACK: *Foundations of Physics*) | Verification PASS at machine precision (`verify_J36_part1.py`, stdlib + sympy 30-digit, <1 s); 7 fermion mixing observables fit substrate primitives at 0.36%–5.52%; Wolfenstein hierarchy λⁿ ≈ (11/49)ⁿ for n ∈ {1,2,3,4} at ≤1.6% across four orders is the load-bearing single pattern; joint coincidence probability with explicit LE correction at multiplicity 77 reported as ~1.4×10⁻⁹ (7 fits) / ~3.8×10⁻⁸ (excl. θ₁₂ since D* not derived here) / ~4×10⁻⁶ (Wolfenstein-only); Part 2 (1/α structural fit) DEFERRED — independent sympy 30-digit verification confirmed 4·40 − 2√7 − π/7 = 154.260, a ~12.6% gap from CODATA 137.036, NOT the 10⁻⁵ originally claimed; honest empirical-fits framing throughout (no first-principles claim; PMNS at 4–6% acknowledged as empirically distinguishable); landed 2026-05-12 |

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J22** | TIG Algebraic Universality (J22 rebuttal addressed) | TBD | rebuttal filed; sympy reverification of tig_dirac.py |
| **J48** | (algebra rebuttal addressed) | TBD | rebuttal filed |

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
- [`../../03_canonical_reference/FORMULAS_AND_TABLES.md`](../../03_canonical_reference/FORMULAS_AND_TABLES.md) Volumes E (Lie tower), F (Higgs), K (atomic correspondence).
- [`../../01_orientation/for_physicists.mdREADME.md`](../../01_orientation/for_physicists.mdREADME.md) — physics-domain entry doc.
- [`../../TIG_FROM_THE_GROUND_UP.md`](../../TIG_FROM_THE_GROUND_UP.md) Parts 8–9 are the physics tutorial.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
