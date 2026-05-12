# 02_results / Lie / GUT

## Headline results

- **so(8) = D₄ from antisymmetrized TSML closure** (WP102, J29): the antisymmetrizations of the TSML composition table, closed under commutator, generate exactly so(8) at dim 28. Cartan classification + Killing signature `(0, 28, 0)` + triality algebra of Spin(8). **PROVED.** Honest negatives in J29's referee report — see [`../../05_papers/_staging/README.md`](../../05_papers/_staging/README.md).

- **so(10) = D₅ from joint TSML + BHML closure** (WP103, J30): antisymmetrizations of the joint TSML+BHML structure generate so(10) at dim 45, rank 5. Killing form `(45, 0, 0)`. Cartan rank 5 with `ad(H)` giving 40 nonzero + 5 zero eigenvalues matching D₅. Saturates antisymmetric closure on the 10-dim substrate. **PROVED.**

- **Doubly-invariant subalgebra = su(4) ⊕ u(1)** (WP104, J23): the doubly-invariant content under `D₄ = ⟨P_56, σ³⟩` acting on so(10) by conjugation has Killing form spectrum `(−4)¹⁵ ⊕ (0)¹` — forcing `simple_15 ⊕ center_1`. Since so(6) ≅ su(4) ≅ A₃ is the unique 15-dim simple Lie algebra, the doubly-invariant subalgebra is **su(4) ⊕ u(1) = Pati-Salam ⊕ B−L**. **PROVED.**

- **P_56 acts as σ_outer in spinor rep** (J23 §2.1): the (5,6) transposition acts in the spinor representation of so(10) as the outer automorphism σ_outer that exchanges the two chiral 16-irreps. The chirality flip `‖P_56^spin: chiral_+ → chiral_+‖ = 0` (machine zero). **PROVED.**

- **Two paths to Pati-Salam** (J23 + J24 framing): (a) BHML's σ_outer-breaking content lies 100% in the **54** of so(10) — symmetric-traceless representation that breaks SO(10) → SO(6) × SO(4); (b) doubly-invariant subalgebra under D₄ is su(4) ⊕ u(1) directly. These are **structurally distinct readings** (per J24 framing), not convergent paths. **PROVED at algebra level; structural identification interpretive.**

- **Yukawa scaffolding** (WP108, J45): under the load-bearing hypothesis that TIG's so(10) IS the SO(10) GUT gauge algebra, the 9-vector VEV with `‖v‖² = 13/4` sits in the **54** irrep, breaking SO(10) → SO(9) → SO(7). The Yukawa Froggatt-Nielsen slope is `λ = 10/49`, top-quark anchor `y_t = 0.93`. **STRUCTURAL** — algebra exact; physical identification is the inference.

## Files in this folder

- [`SIX_DOFS_COMPACT.md`](SIX_DOFS_COMPACT.md) — TIG's six algebraic degrees of freedom: Lie / Jordan / Clifford / Permutation / Lattice / Operad

## Honest scope

- The identification of TIG's so(10) with the SO(10) GUT gauge algebra is a STRUCTURAL load-bearing hypothesis — the algebra is exact (Cartan classification ensures isomorphism); the *physical* identification is the inference.
- The Yukawa hierarchy from the substrate is scaffolding, not a derivation. Going from λ = 10/49 to a falsifiable mass prediction requires committing to a Higgs sector (combinations of 10, 54, 126), running RG flows from GUT scale to electroweak scale, and comparing to observed masses. That work is OPEN.

## Verification

```bash
python ../../05_papers/algebra/J30/manuscript/verification/verify_so10.py    # so(10) = D₅
python ../../05_papers/algebra/J30/manuscript/verification/verify_simplicity_rank.py
python ../../05_papers/physics/J23/manuscript/verification/find_higgs_irrep.py
python ../../05_papers/physics/J45/manuscript/verify_J45_yukawa.py    # λ = 10/49, y_t = 0.93
```

## Landed J-series papers

J23 (Discrete Dirac, *CMP*), J30 (Joint Lie Closure, *Israel J. Math.*), J45 (Yukawa Hierarchy, *PRD*). See [`../../05_papers/physics/`](../../05_papers/physics/) and [`../../05_papers/algebra/`](../../05_papers/algebra/).

## Connections to existing literature

- **GUT phenomenology**: Fritzsch-Minkowski (1975), Georgi (1975), Pati-Salam (1974)
- **Standard so(n) classification**: Cartan, Bourbaki Ch. VI

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
