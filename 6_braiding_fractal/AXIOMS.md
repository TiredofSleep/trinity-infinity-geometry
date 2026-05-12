# The Braiding Fractal — 10 Architectural Axioms

The framework's architecture is fixed by ten axioms specifying a **canonical Rung 5** of a tower of finite-arithmetic carriers. The architecture is invariant; the parameters are minimality-forced. This document states the axioms.

**Status:** locked 2026-05-10 (the architecture name "Braiding Fractal" supersedes the earlier draft name "Brayden Fractal").

---

## Axiom 1 — Kernel of size 2

The carrier's kernel is **Z/2**: the smallest nontrivial cyclic group. The Z/2 factor encodes binary distinction — equivalently, spin under D102's identification. Without binary distinction the framework cannot host fermionic structure.

## Axiom 2 — Smallest non-binary partner

The kernel pairs with the smallest prime that is **not** the immediate-successor strand to {2}. Since 3 is the immediate-successor strand (and is reserved for strand-1 wrapping per Axiom 5), the next-eligible prime is 5. Therefore:

```
kernel = Z/2 × Z/5 = Z/10
```

This is `D103` — Z/10 as the minimal kernel admitting binary + non-binary structure with the non-binary prime not adjacent to the binary.

## Axiom 3 — Dual composition lens

The 10 operators carry two natural multiplication tables — one symmetric (TSML, "Trinity Synthesis Meaning Language", 73 HARMONY cells) and one antisymmetric (BHML, "Being-Harmony Meaning Language", 28 HARMONY cells). The pair is required: neither alone is sufficient to constrain the four-core, the eight-shell chain, or the α = 1/2 attractor.

A third table, **CL_STD** (44 HARMONY cells), serves as the standard-language carrier. The three together form a `(73, 28, 44)` HARMONY signature.

## Axiom 4 — Three-strand wrap depth (depth-3 ceiling)

The kernel is wrapped by exactly **3 additional substrate primes** to form the canonical substrate:

```
Z/10 → Z/30 (×3) → Z/210 (×7) → Z/2310 (×11)
```

This is the depth-3 ceiling — extending further (×13 → Z/30030, ×17 → Z/510510) is allowed but is **post-canonical**. The canonical Braiding Fractal stops at Z/2310 because:

- Z/2310 has 32 divisors (2⁵)
- The atomic shell n = 4 has Pauli capacity 32
- The Clifford algebra Cl(0, 10) has spinor representation dimension 32

These three independent integer counts equal 32 at depth-3 (Axiom 4 corollary, D102 triple coincidence). The fourth strand (13) extends the substrate but no longer aligns with a "simplest whole" count of 32.

## Axiom 5 — Substrate primes are odd

The three wrap strands are exactly the next three primes after 5: **{3, 7, 11}**. They wrap the kernel `{2, 5}`. The full strand set is `{3, 7, 11}` (canonical) extended by `{13, 17, 19, ...}` (post-canonical). Substrate primes are by definition odd; even-prime structure lives entirely in the Z/2 kernel.

## Axiom 6 — Quadratic operator at the midpoint

The mixing parameter `α ∈ [0, 1]` between TSML and BHML carries a quadratic operator that **uniquely admits algebraic-relation closure at α = 1/2** (D57). At α = 1, the attractor collapses to δ_H (full HARMONY). At α = 0, the attractor is a transcendental 4-distribution. At α = 1/2, the attractor is the unique *algebraic interior point* with:

```
H/Br = 1 + √3   (deg 2, x² − 2x − 2 = 0)
r/br : x⁴ + 4x³ − x² + 2x − 2 = 0   (LMFDB 4.2.10224.1, Galois D₄)
```

## Axiom 7 — Four-core attractor

The fixed set of σ³ under the cyclic permutation `σ = (0)(1 7 9 3)(2 8 6 4)(5)` is the four-core `{V, H, Br, R} = {0, 7, 8, 9}`. This is closed under both TSML and BHML multiplication (D39). At α = 1/2 it carries the universal attractor `(V, H, Br, R) = (0.138, 0.540, 0.198, 0.124)` with `H/Br = 1 + √3` (D43, residual 4.23 × 10⁻¹²).

The four-core is the architectural center: every shell of size ≥ 4 in the joint sub-magma chain produces the *same* 4-distribution (D58, robustness audit 2026-04-26).

## Axiom 8 — Strata via substrate primes {3, 7, 11}

The substrate decomposes into three strata:

- **Stratum I**: lives at primes {3, 7, 11}. HARMONY (= 7) is the σ-fixed attractor; wobble (= 11) is localized to specific char-poly coefficients but absent from the discriminant (the 16-dim doubly-invariant subalgebra is wobble-free).
- **Stratum II**: lives at composite-prime products (e.g., 3·7 = 21, 3·11 = 33, 7·11 = 77).
- **Stratum III**: post-canonical extensions to strands 13, 17, 19 etc.

The structural primes are 7 (HARMONY) and 11 (wobble), not the rationals or transcendentals. Coincidences with transcendentals (e, π, φ, ζ(3), Catalan G) at the 1% level are **not** algebraic identities and should not be cited as such; see the `CL_EIGENVALUES_AUDIT_2026_04_25` in the working corpus.

## Axiom 9 — Clifford carrier Cl(0, 10)

The 10 substrate operators embed into the Clifford algebra **Cl(0, 10)** over ℝ. The 32-dim spinor representation decomposes under the chirality involution ω = γ₁ γ₂ … γ₁₀ as `16 + 16` (positive + negative chirality, since `ω² = +I` for n = 10 ≡ 2 mod 4).

Each 16-dim chirality half decomposes as `16 = 1 + 3 + 5 + 7`:
- `1` = kernel base (l = 0, the s-orbital position)
- `3` = strand 1 (l = 1, the p-orbital multiplicity)
- `5` = kernel-Z/5 partner (l = 2, the d-orbital multiplicity)
- `7` = strand 2 (l = 3, the f-orbital multiplicity)

This is **D102**: the Cl(0, 10) chirality decomposition realizes the n = 4 atomic shell's `(spin) × (spatial)` structure exactly. The substrate primes (kernel + strands) are the spatial-orbital multiplicities of the n = 4 shell at fixed spin.

## Axiom 10 — Architectural self-similarity (with caveats)

The architecture **template** — `kernel of 2 primes + 3-strand wrap + dual lens + quadratic operator + four-core` — is invariant across rungs of the tower:

- Rung 5 (canonical, this framework): kernel `{2, 5}`, strands `{3, 7, 11}`, Cl(0, 10), 32 = simplest whole.
- Rung 7: kernel `{2, 5}`, strands `{3, 7, 11, 13, 17}`, Cl(0, 14), 128.
- Lower rungs: smaller substrates, smaller wholes.

Importantly, the template does **not** trivially recurse: at the meta-level (treating Z/2310 itself as a "kernel" for a meta-substrate), the next-strand structure (13, 17, 19) does not produce an integer Pauli shell `n` because `2n² = 256` requires `n = √128`, which is not integer. **Higher meta-rungs exist** but follow modified parameter rules, not the canonical Rung-5 template.

The Braiding Fractal is therefore **the canonical depth-3 architecture**, not a fractal whose recursion structure is identical at every scale. It is "fractal" in the architectural-template sense (the *form* repeats across rungs), not in the parameter-recursion sense (the specific numbers do not).

---

## Summary

The Braiding Fractal is the minimal finite-arithmetic architecture satisfying:

1. carries binary distinction (Z/2 kernel)
2. carries non-binary distinction with non-adjacent prime (Z/5 partner) → kernel = Z/10
3. carries dual symmetric/antisymmetric lens (TSML + BHML)
4. wraps to depth 3 via the next three primes (3, 7, 11)
5. carries a quadratic mixing operator with unique algebraic-interior point at α = 1/2
6. preserves a four-element center under both lenses
7. stratifies via Stratum I structural primes {3, 7, 11}
8. embeds into the Clifford carrier Cl(0, 10)
9. realizes the atomic shell n = 4 in its 32-dim spinor decomposition (1 + 3 + 5 + 7)
10. instantiates an invariant template that can be specified at higher rungs with modified parameters

All ten axioms are verifiable from the substrate. None is an external assumption.

---

## Verification cross-reference

- **Axioms 1–3 + 7**: `_verification_scripts/VERIFY_ALL.py` (Tier A, 14/14)
- **Axiom 4 (depth-3 + triple identity)**: `_verification_scripts/clifford_substrate_shell.py`
- **Axiom 5 (substrate primes)**: implicit in the strand-orbital mapping
- **Axiom 6 (α uniqueness)**: D57 — sharpened via Stern-Brocot grid + PSLQ
- **Axiom 7 (four-core attractor)**: D58 — robustness across non-degenerate inits
- **Axiom 9 (Cl(0, 10))**: `_verification_scripts/clifford_substrate_shell.py` and J23 §2.1
- **Axiom 10 (self-similarity caveats)**: `_verification_scripts/meta_extension.py`

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
*The architecture is locked. The arithmetic is the field. The substrate is enough.*
