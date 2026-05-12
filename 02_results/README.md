# 02 — Results, Field-Organized

The framework's load-bearing results, organized by the mathematical / physical field they live in. Pick your field; each subdirectory has a `README.md` with claim statements, status flags, and links to verification scripts and published papers in `05_papers/`.

---

## Fields

| Field | Folder | Headline results |
|---|---|---|
| **Algebraic Combinatorics** | [`algebraic_combinatorics/`](algebraic_combinatorics/) | Z/10Z operator algebra; TSML+BHML composition tables; 4-core fusion-closure `{V, H, Br, R}`; 8-shell joint sub-magma chain `{1, 4, 5, 6, 7, 8, 9, 10}`; σ-rate theorem `σ(N) ≤ C/N` with C = 2 |
| **Atomic Physics** | [`atomic_physics/`](atomic_physics/) | D2/D1 = (2l+1)/(8π) closed form for nodeless hydrogenic orbitals; substrate-prime → orbital-multiplicity correspondence (strands {3, 7, 11, 13} → 2p, 4f, 6h, 7i) |
| **Clifford Algebra** | [`clifford_algebra/`](clifford_algebra/) | Cl(0, 10) 32-dim spinor; chirality 16+16 split = spin × spatial; triple coincidence at depth-3 (32 divisors of Z/2310 = Pauli n=4 = Cl(0,10) spinor dim); WOBBLE localization at prime 11 |
| **Number Theory** | [`number_theory/`](number_theory/) | First-G Law (squarefree stability of smallest-prime-factor coprime window); sinc² zero law for squarefree moduli; cyclotomic Q(ζ₁₀) tower; cyclotomic forcing of T*=5/7 under D₄ Galois |
| **Dynamics** | [`dynamics/`](dynamics/) | α = 1/2 universal attractor `(V, H, Br, R) = (0.138, 0.540, 0.198, 0.124)` with `H/Br = 1 + √3` exactly; closed-form algebraic attractor and lattice-cache fixed-point arithmetic |
| **Cosmology** | [`cosmology/`](cosmology/) | Logarithmic quintessence V(ξ) = Λ⁴ξ log ξ from Bialynicki-Birula 1976 separability; late-time vacuum ξ₀ = e⁻¹; dark-sector triple Ω = (49, 264, 687)/1000; J46/J47 layer choice pending |
| **Lie / GUT** | [`lie_gut/`](lie_gut/) | so(8) = D₄ from antisymmetrized TSML closure; so(10) = D₅ from joint TSML+BHML closure; doubly-invariant subalgebra su(4) ⊕ u(1) = Pati-Salam ⊕ B−L; two paths to Pati-Salam; 9-vector Higgs scaffolding |

---

## Claim status flags

Every result in `02_results/` carries an explicit status flag — see [`../01_orientation/README.md`](../01_orientation/README.md) for the discipline:

- **PROVED** — formal proof + numerical verification at the precision noted
- **STRUCTURAL** — rigorous derivation grounded in proved claims, with the load-bearing identification named explicitly (not assumed)
- **EMPIRICAL** — observed in computational experiments at the scale noted
- **OPEN** — research-direction hypothesis, precisely stated

For the master proof spine with D-numbered theorems and Volumes A through K, see [`../03_canonical_reference/FORMULAS_AND_TABLES.md`](../03_canonical_reference/FORMULAS_AND_TABLES.md).

---

## How fields connect

The strongest cross-field result is the **substrate-atomic correspondence (Volume K, D100–D103)**: a finite-arithmetic substrate on Z/10Z with three prime strands wrapping (3, 7, 11) up to depth 3 → Z/2310 with 32 divisors = Cl(0, 10) spinor dim = atomic Pauli capacity at n = 4. The Cl(0, 10) chirality split realizes the n = 4 shell's spin × spatial structure exactly, with the spatial part `1 + 3 + 5 + 7` = kernel + substrate primes. This connects **Algebraic Combinatorics** ↔ **Clifford Algebra** ↔ **Atomic Physics** through exact integer identities.

For the speculative / Tier C interpretation of why these connections exist, see [`../04_meta/META_TIG_AS_PREPHYSICAL_SUBSTRATE.md`](../04_meta/META_TIG_AS_PREPHYSICAL_SUBSTRATE.md). For the formal architecture, see [`algebraic_combinatorics/BRAIDING_FRACTAL_AXIOMS.md`](algebraic_combinatorics/BRAIDING_FRACTAL_AXIOMS.md).

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
