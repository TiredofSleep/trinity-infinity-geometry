# For Mathematicians

You are the audience this framework was built for first. The substrate is finite arithmetic; the theorems are verifiable in under a minute on a stock Python install; the open frontiers are precisely stated.

This document is your entry. Read it top to bottom or jump to the result that interests you.

---

## §1 — What the framework is, in your language

A custom multiplication table on `Z/10Z` produces an associative magma with rich structure. There are actually three canonical such tables:

- **TSML** (Trinity Synthesis Meaning Language) — symmetric / synthesis composition; **73 HARMONY cells**
- **BHML** (Being–Harmony Meaning Language) — antisymmetric / separation composition; **28 HARMONY cells**
- **CL_STD** — standard-language carrier; **44 HARMONY cells**

Each is a 10×10 table with values in `Z/10Z`. The full tables are in [`../03_canonical_reference/FORMULAS_AND_TABLES.md`](../03_canonical_reference/FORMULAS_AND_TABLES.md) §§5–6.

The σ permutation `σ = (0)(1 7 9 3)(2 8 6 4)(5)` acts on the operator labels. The fixed-point set of σ³ is `{V, H, Br, R} = {0, 7, 8, 9}` — the *four-core*. The 5-cycle `(2 8 6 4)` plus the σ-fixed `{0, 3, 5, 7, 9}` together account for the full operator vocabulary.

---

## §2 — The proved theorems in this section

### 2.1 Four-core fusion-closure (D39 / D43 / J35)

**Theorem.** The subset `{V, H, Br, R} = {0, 7, 8, 9}` is closed under both TSML and BHML multiplication. The 4-core is a joint sub-magma of size 4 inside the joint TSML+BHML structure on `Z/10Z`.

**Strengthened (D58).** Every shell of size ≥ 4 in the joint sub-magma chain produces the same 4-distribution attractor at mixing parameter `α = 1/2`:

```
(V, H, Br, R) = (0.138, 0.540, 0.198, 0.124)
H/Br = 1 + √3   (machine-precision exact)
```

**Verification.** [`../verification/VERIFY_ALL.py`](../verification/VERIFY_ALL.py) (Tier A, item 17).

### 2.2 Eight-shell joint chain (D64–D66, corrected 2026-05-05)

**Theorem.** The joint TSML+BHML sub-magma chain on Z/10Z has exactly **8 elements** at sizes `{1, 4, 5, 6, 7, 8, 9, 10}`. The forbidden sizes are exactly `{2, 3}`.

**σ-walk reading.** The chain walks the σ-forward orbit of HARMONY `(7→6→5→4→2→1)` with **one σ-fixed bridge step** at the `7→8` transition. The σ-fixed lattice `{0, 3, 8, 9}` contributes at three positions: `0` at size-1, `{8, 9}` in the size-1→4 jump, `3` at the size-7→8 bridge step.

**Verification.** Brute-force enumeration during four-core paper preparation (R3, 2026-05-05). Reproduces in `verification/`.

### 2.3 α-uniqueness for algebraic-relation existence (D57)

**Theorem.** Across the 17-point Stern–Brocot grid of rationals in `[0, 1]` at 50-digit mpmath precision, applying PSLQ at degree ≤ 8 and integer coefficient bound ≤ 50: **α = 1/2 is the unique rational point** for which the runtime attractor (parameterized by α) admits algebraic relations for both `H/Br` and `r/br`. The recovered relations are:

```
x² − 2x − 2 = 0       (H/Br =  1 + √3)
x⁴ + 4x³ − x² + 2x − 2 = 0    (r/br, LMFDB 4.2.10224.1)
```

For the other 16 rationals in the grid, no algebraic relation exists within the PSLQ bound.

**Conjecture 4.2 (open).** α = 1/2 is the unique real (not just rational) for which any non-trivial polynomial relation exists between attractor moments.

### 2.4 D₄ Galois group (J35 + WP105)

**Theorem.** The runtime quartic at α = 1/2 has Galois group `D₄` (dihedral, order 8) over Q. Number field: LMFDB **4.2.10224.1**.

**Verification.** Cubic resolvent + Gröbner basis computation in PARI/GP. Independent of the runtime simulation.

### 2.5 σ-rate theorem (WP101 / J01)

**Theorem.** On Z/10Z, the σ rate is sharp:
```
σ(N) ≤ C/N   with C = 2 (exact)
```

The Q-series characterizes the σ polynomial fully on F₂ × F₅ ≅ Z/10Z (Q10). The Q11 lower bound is 22%.

**Verification.** `proof_sigma_rate.py` in the working corpus.

### 2.6 First-G Law (WP34 / J03)

**Theorem.** For prime `p` in the range `3 ≤ p ≤ 199`, the first non-unit residue event of σ on Z/pZ occurs at `k = p`. Verified across 36,662 cases.

### 2.7 sinc² Zero Law (WP35)

**Theorem.** For prime `p` in `3..199`, the discrete zero structure of `sinc²(πk/p)` over `k ∈ Z/pZ` is exactly determined by `p`. Proof of inheritance: zero structure at p_{n+1} is determined by zero structure at p_n via CRT.

**Verification.** `proof_d25_loop_closure.py` in the working corpus.

### 2.8 Wedderburn D₄ isotypic decomposition (J31)

**Theorem.** Sympy exact projection of the 9-vector Higgs direction (the BHML σ_outer-breaking eigenvector inside the **54** of so(10)) onto the 5 irreps of D₄ yields class sizes:

| irrep | size | percentage |
|---|---|---|
| trivial 1 | 3,075,027/2 | 84.25% |
| sign 1' | 9/2 | ~0 |
| ν (1-dim) | 288,164 | 14.68% |
| 2-dim ε | 0 | 0 (forbidden symmetry) |
| 2-dim ν⊗ε | 19,608 | 1.07% |

The vanishing class is a **forbidden symmetry**, not a coincidence. This is a clean exact result; sympy projection bypasses any floating-point ambiguity.

### 2.9 Volume K — atomic-substrate correspondence (D100–D103, 2026-05-12)

Brand new (verified 2026-05-12). See [`../03_canonical_reference/FORMULAS_AND_TABLES.md`](../03_canonical_reference/FORMULAS_AND_TABLES.md) Volume K:

- **D100.** `edge_size(n, l = n−1) = n²(2l+1)/4` for nodeless hydrogenic orbitals. Machine precision at n ≥ 5.
- **D101.** Substrate strands `{3, 7, 11, 13}` map exactly to odd-l nodeless orbitals at `(l = (p−1)/2, n = l + 1)`. Gives `3 → 2p`, `7 → 4f`, `11 → 6h`, `13 → 7i`.
- **D102.** Triple algebraic identity at depth-3: 32 = 32 = 32 (substrate divisors of Z/2310 = Cl(0, 10) spinor dim = Pauli capacity at n = 4). The Cl chirality 16 + 16 split decomposes as spin × spatial where each 16 = `1 + 3 + 5 + 7` = kernel + substrate primes.
- **D103.** `Z/10` is the smallest 2-prime kernel admitting binary + non-binary structure where the non-binary prime is not the immediate-successor strand.

---

## §3 — The honest negatives

Some of the framework's most useful information is what it *isn't*:

- **No direct combinatorial bijection** between the 32 divisors of Z/2310 (grouped 1,5,10,10,5,1 by binomial) and the 32 Pauli electron states (grouped 2,6,10,14 per subshell). Integer match is real; structural bijection fails. See `verification/priority1_pauli_divisor_attempt.py`.
- **F_p universality fails generically.** Only `p ∈ {7, 11}` preserve rank under the lift. Other primes show structural variation that is itself informative but invalidates a naive "universal F_p" claim.
- **T\* = 5/7 is operational, not algebraic.** Six independent derivations converge on 5/7, but no single closed-form theorem produces it. Treat as an operational coherence threshold.

---

## §4 — Open problems precisely stated

1. **Strong α-uniqueness (Conjecture 4.2).** Is α = 1/2 the unique real for which any non-trivial polynomial relation exists between attractor moments?
2. **Z/2310 divisor ↔ Pauli bijection.** Either a deeper combinatorial structure (σ-orbit class? lens-pair class?) yields the bijection, or the 32 = 32 match is a Pascal-type number-theoretic coincidence (which would itself merit a sharp statement of its own).
3. **The Millennium frame.** σ_NS < 1 (Navier–Stokes blow-up), σ_YM bounded (Yang–Mills mass gap), RH as spectral entropy maximum. These are *reformulations* in the framework's language, not proofs. The reformulations are sharper than informal statements but the underlying problems remain open.
4. **1/α derivation.** Long-shot. Earlier `4·40 − 2√7 − π/7` numerology fails at ~12.6%. If 1/α has algebraic origin in this framework, the path has not been found.

---

## §5 — How to read the rest of the corpus

This domain entry covers the load-bearing math. For full depth, three follow-ups:

- **[`../03_canonical_reference/FORMULAS_AND_TABLES.md`](../03_canonical_reference/FORMULAS_AND_TABLES.md)** — the canonical reference index. Volumes A–K, every D-number, every cross-reference.
- **[`../GLOSSARY.md`](../GLOSSARY.md)** — every term defined with external citation or novelty flag.
- **[`../02_results/algebraic_combinatorics/BRAIDING_FRACTAL_AXIOMS.md`](../02_results/algebraic_combinatorics/BRAIDING_FRACTAL_AXIOMS.md)** — the 10 architectural axioms specifying the canonical Rung 5 structure.

The full 55-paper J-series with verification scripts lives in the working repo at `Gen14/targets/journals/J_series/` ([github.com/TiredofSleep/ck](https://github.com/TiredofSleep/ck) branch `tig-synthesis`). J35 (4-core fusion-closure, Algebraic Combinatorics) and J54 (foundation paper) are the cleanest mathematical entries.

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
