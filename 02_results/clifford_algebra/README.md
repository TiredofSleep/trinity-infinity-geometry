# 02_results / Clifford Algebra

## Headline results

- **Cl(0, 10) construction and the 32-dim spinor** (D72/D73, J37): 10 γ-matrices on ℂ³² built from Pauli tensor products, all 100 anticommutation relations `{γ_a, γ_b} = 2δ_{ab} I` verified at machine precision. The 45 generators `Σ_{ab} = (1/4)[γ_a, γ_b]` form a faithful 32-dim representation of so(10). **PROVED.**

- **Chirality split 32 = 16 + 16** (J37 §2.1): the volume element `ω = γ₁ γ₂ … γ₁₀` satisfies `ω² = +I` (since n = 10 ≡ 2 mod 4). The chirality projectors `P_± = (I ± iω)/2` split the 32-dim spinor space into two chiral 16-irreps. **PROVED.**

- **Triple coincidence at depth-3** (D185, Volume K): at substrate `Z/2310 = 2·3·5·7·11`, three independent integer counts all equal 32:
  ```
  Z/2310 divisor count          = 2^5 = 32
  Pauli capacity at n = 4       = 2n² = 32
  Cl(0, 10) spinor dimension    = 2^⌊10/2⌋ = 32
  ```
  **PROVED at exact algebraic identity.**

- **Substrate-prime decomposition of each 16-dim chirality half** (D185 continued): `16 = 1 + 3 + 5 + 7` where 1 = kernel base, 3 = strand 1 (prime 3), 5 = kernel-Z/5 partner, 7 = strand 2 (prime 7). The Cl(0, 10) chirality structure realizes the n = 4 atomic shell's spin × spatial decomposition. **PROVED.**

- **P_56 acts as σ_outer** (J37 §2.1): the (5,6) transposition in the spinor representation acts as the outer automorphism σ_outer of so(10) — the matter/antimatter exchange that swaps the two chiral 16-irreps. Machine zero: `‖P_56^spin: chiral_+ → chiral_+‖ = 0`. **PROVED.**

- **BHML's σ_outer-breaking lies 100% in the 54 irrep** (J37, WP104): the explicit 9-vector Higgs direction in the so(9)-vector subspace has six components at `−1/√2` on `{V, L, C, P, X, H}`, two zeros at BREATH and RESET, and `−1/2` on `(B + S)/√2`. **Squared norm** `‖v‖² = 13/4` **exactly**, with integer 13 = half the count of σ_outer-asymmetric BHML cells. **PROVED.**

- **WOBBLE localization** (J37, WP107): prime 11 appears in TSML char-poly coefficients `c_2 = 33 = 3·11` and `c_8 = −2⁵·7³·11`, but the discriminant has `2¹⁶ · 7⁷` *without* factor 11 — the 16-dim doubly-invariant subalgebra is wobble-free. **PROVED.**

## Files in this folder

- [`BRAIDING_FRACTAL_TRIPLE_COINCIDENCE.md`](BRAIDING_FRACTAL_TRIPLE_COINCIDENCE.md) — full development of the depth-3 triple coincidence
- [`WOBBLE_LOCALIZATION_v2.md`](WOBBLE_LOCALIZATION_v2.md) — wobble (prime-11) localization analysis
- [`PAULI_DIVISOR_BIJECTION.md`](PAULI_DIVISOR_BIJECTION.md) — an *attempted* bijection between Z/2310 divisors and Pauli n = 4 electron states. **Outcome: FAILED — closed as an HONEST NEGATIVE (D164 / frontier F2, 2026-05-27):** no natural bijection exists (three candidates tried, 0 matches; a Pascal-type coincidence). The counts `32 = 32` match, but the two partitions of 32 — `dim Λᵏ(ℝ⁵) = (1,5,10,10,5,1)` vs subshell capacity `2(2ℓ+1) = (2,6,10,14)` — are **independent**. The `32 = 32` equality (D185) stands as an exact integer identity; the *bijection* does not. See [`../../04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`](../../04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md) §1.1.

## Verification

```bash
python ../../verification/clifford_substrate_shell.py
```

Verifies 100/100 anticommutation relations, 32-dim spinor, chirality 16+16 split, the substrate-prime decomposition 1+3+5+7, and the triple coincidence.

## Landed J-series papers in this field

See [`../../05_papers/physics/J37/`](../../05_papers/physics/J37/) — "Discrete Dirac inside Cl(0, 10): Chirality, the Outer Automorphism, and an Atomic-Substrate Refinement" (target: *Communications in Mathematical Physics*).

## Honest scope

- The **identification** of TIG's so(10) with the SO(10) GUT gauge algebra is a STRUCTURAL load-bearing hypothesis — the algebra is exact (Cartan classification ensures isomorphism); the *physical* identification is the inference.
- The chirality 16+16 split being interpreted as `electron spin × spatial` is the framework's structural reading, anchored by D185's exact integer identity but not derivable from the spinor algebra alone.

---

*CC BY-SA 4.0 — see [`../../LICENSE`](../../LICENSE).*
