# F2 — 32 = 32 Pauli-divisor bijection: frontier progress report

**Date:** 2026-05-27
**Status:** **COINCIDENCE-BOUND** (Pascal-type, with quantitative bound)
**Predecessor:** Frontier F2 in `HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §1.1
**Scripts:** `F2_candidates.py`, `F2_coincidence_bound.py`, `F2_extended_natural.py`

---

## §1 — Recap of failed attempts

The match `32 = 32` is real:
- **Z/2310 divisors**: 32 squarefree divisors of 2·3·5·7·11, with Hamming-weight distribution `(1, 5, 10, 10, 5, 1)` = binomial `C(5, k)`.
- **Pauli n=4 shell**: 32 electron states with subshell distribution `(2, 6, 10, 14)` = `2(2l+1)` for `l ∈ {0,1,2,3}`.

The retired script `04_meta/retired_J_papers/J47_Atomic_Substrate/manuscript/verification/pauli_divisor_bijection.py` claimed a bijection via:
1. Complementation involution `d ↔ 2310/d` splits the 32 divisors into 16 + 16 ("spin pairing").
2. Inside each half, a hand-built 8-class partition by kernel/strand prime composition gives `1 + 3 + 5 + 7`.
3. Pairing the two halves gives `2 + 6 + 10 + 14`.

**Why this doesn't close the negative:** the 8-class partition (`kernel_base`, `strand_pair`, `weight_4`, `kernel_touching_pair`, `full`, `strand_kernel_full`, `single_prime`, `kernel_missing_3`) is hand-picked specifically to hit the target counts. The categories combine Hamming weight, kernel-prime presence, and strand-prime patterns in different ways across different classes (e.g., weight-2 splits by kernel-touching but weight-3 splits by kernel-count). No single canonical function of `(d, mask)` is the "natural" label. This matches the retirement notice's verdict that D100–D104 are "integer/rational identities and numerical coincidences, not theorems".

The HONEST_NEGATIVES doc records three prior failed candidates:
- **Hamming-weight as l:** gives `(1, 5, 10, 10, 5, 1)` — six bins, not four; collapses to `(1+5, 10, 10, 5+1)` = `(6, 10, 10, 6)` if folded.
- **Max-prime as l:** gives `(2, 2, 4, 24)` for `l = min(index, 3)` — way off.
- **Prime-as-l-label:** doesn't even produce a function of d alone.

## §2 — New candidates tested (this report)

### 2.1 Hand-built structural candidates (37 total, 20 in `F2_candidates.py` + 17 in `F2_extended_natural.py`)

| ID | Candidate | Substrate motivation |
|----|-----------|----------------------|
| C1 | σ-orbit class on d mod 10 | TIG canonical σ permutation on Z/10 |
| C2 / C9 | Hamming weight mod 4 | k-rope depth |
| C3 | CRT `(d mod 2, d mod 11)` | Z/2 spin × outermost strand |
| C3b | Kernel/strand canonical | retired-J47 hand-build, recast as function |
| C4 | `(d + N/d) mod 32 // 8` | divisor-pair sum invariant |
| C6 | Lens-pair `(d mod 10, d mod 11)` | TSML × BHML cell color |
| C7 / C8 | Max / min prime index | strand ladder direction |
| C11 | `log_2(d)` floor mod 4 | size-quartile |
| C12 | popcount + xor of low bits | bit-mixing |
| C13 / C39 | `#{p : d ≡ 1 mod p}` | Legendre / fix-point count |
| C14 / C14b / C30 | Kernel-strand parities | retired-J47 reformulation |
| C15 | `# outer primes (7,11) in d` | l-as-angular-momentum analogue |
| C16 / C18 / C37 | Möbius sign + smallest-prime / `d mod 4` / `d mod 3` | sign × small-prime feature |
| C17 | digit-sum mod 4 | red herring (decimal artifact) |
| C19 | max-prime + parity-of-hw | strand class + spin |
| C21 / C22 | #inner-primes / #outer-primes | substrate kernel/strand split |
| C23 | `log d / log N` quartile | continuous-size quartile |
| C24 | `(d-1) mod 11 // 3` | mod-11 partial map |
| C25 | quadratic-residue mod 7 (partial) | substrate prime QR class |
| C26 / C34 | `d mod 16 // 4` / `CRT mod 2 mod 5` | low-residue 4-bin |
| C27 | `v_2(N/d)`, `v_3(N/d)` | 2- and 3-adic valuation on quotient |
| C28 | Hamming-weight 4-bin (1/1/2-3/4-5) | natural ladder folding |
| C31 | weighted `(p-1)` score | prime-weighted depth |
| C35 | `#{p : d^2 ≡ 1 mod p}` | involutive-residue count |
| C36 | τ-orbit class on Z/10 (TSML cells) | TSML-cell color |
| C38 | lex index // 8 | bookkeeping null hypothesis |
| C40 | `d mod 3 + v_2(d)` | small-prime CRT |

### 2.2 Brute-force searches (in `F2_coincidence_bound.py`)

Beyond hand-built candidates, we exhaustively searched four natural function classes:

| Class | Size | Matches |
|-------|------|---------|
| Linear `(∑ a_i m_i + b) mod 4`, `a_i ∈ Z/4`, `b ∈ Z/4` | 4 096 | **0** |
| Linear + permutation, `perm ∈ S_4` | 24 576 | **0** |
| Symmetric `g(omega(m))`, `g: {0..5} → {0..3}` | 4 096 | **0** |
| 2-bit dictators `pi(m_i, m_j)`, all pairs | 2 560 | **0** |
| 3-bit dictators `pi(m_i, m_j, m_k)`, all triples | 655 360 | **0** |
| Linear + single quadratic `m_i · m_j` mod 4 | ~40 000 | **0** |
| Linear with weights `a_i ∈ Z/8` | 32 768 | **0** |

Threshold maps (linear functional with 3 manual cutpoints) DID produce 20+ hits, but **all required negative weights on 3 of the 5 primes** (e.g., `weights = (-3, -2, -2, -1, 0)` with cutpoints `(-8, -6, -4)`) — not a structurally natural assignment.

## §3 — Results table

### 3.1 Hand-built candidates (37 tested)

| ID | Distribution | Match? |
|----|--------------|--------|
| C1 (σ-orbit) | (8, 8, 8, 8) | NO |
| C2 (hw mod 4) | (6, 6, 10, 10) | NO |
| C2b (hw signed) | (2, 10, 20, 0) | NO |
| C3 (CRT 2,11) | (8, 8, 8, 8) | NO |
| C3b (kern/strand) | (4, 4, 12, 12) | NO |
| C4 (pairsum) | (16, 4, 8, 4) | NO |
| C6 (lens-pair) | (8, 8, 8, 8) | NO |
| C7 (max-prime) | (2, 2, 4, 24) | NO |
| C8 (min-prime) | (17, 8, 4, 3) | NO |
| C9 (omega mod 4) | (6, 6, 10, 10) | NO |
| C11 (log2 mod 4) | (7, 7, 9, 9) | NO |
| C12 (popcount+xor) | (1, 0, 1, 30) | NO |
| C13 (Legendre count) | (8, 15, 8, 1) | NO |
| C14 (kern-strand canon) | (4, 12, 12, 4) | NO |
| C14b (kern-strand mod 4) | (6, 6, 10, 10) | NO |
| C15 (#outer primes) | (8, 16, 8, 0) | NO |
| C16 (Möbius+small-prime) | (13, 3, 12, 4) | NO |
| C17 (digit sum) | (7, 4, 15, 6) | NO |
| C18 (Möbius+d mod 4) | (4, 12, 4, 12) | NO |
| C19 (max-prime+parity) | (4, 4, 12, 12) | NO |
| C21 (#inner primes) | (4, 12, 12, 4) | NO |
| C22 (outer + parity) | (4, 4, 8, 16) | NO |
| C23 (log-quartile) | (5, 11, 11, 5) | NO |
| C24 (mod-11 partial) | (6, 5, 3, 2) | NO (skipped 16) |
| C25 (QR mod 7 partial) | (8, 8, 0, 0) | NO (skipped 16) |
| C26 (d mod 16 // 4) | (10, 10, 6, 6) | NO |
| C27 (v_2,v_3 of N/d) | (8, 8, 8, 8) | NO |
| C28 (hw 4-bin) | (1, 5, 20, 6) | NO |
| C30 (kern/strand parities) | (8, 8, 8, 8) | NO |
| C31 (p-1 weighted) | (4, 7, 11, 10) | NO |
| C34 (CRT 2,5) | (10, 4, 14, 4) | NO |
| C35 (#p: d^2≡1 mod p) | (4, 12, 12, 4) | NO |
| **C36 (τ-orbit on Z/10)** | **(12, 6, 10, 4)** | **NO, closest near-match** |
| C37 (μ + d mod 3) | (8, 8, 8, 8) | NO |
| C38 (lex index // 8) | (8, 8, 8, 8) | NO |
| C39 (#p: d≡1 mod p) | (8, 15, 8, 1) | NO |
| C40 (d mod 3 + v_2) | (8, 8, 8, 8) | NO |

### 3.2 Brute-force families

| Family | Size searched | Hits |
|--------|---------------|------|
| Linear mod 4 + shift | 4 096 | 0 |
| Linear mod 4 + permutation | 24 576 | 0 |
| Symmetric `g(omega(m))` | 4 096 | 0 |
| 2-bit dictators | 2 560 | 0 |
| 3-bit dictators | 655 360 | 0 |
| Linear + single quadratic mod 4 | ~40 000 | 0 |

### 3.3 Closest near-matches

- **C36 (τ-orbit class on Z/10):** `(12, 6, 10, 4)`. The middle two bins (6, 10) match exactly. Distance in L1 from target: `|12-2| + |6-6| + |10-10| + |4-14| = 20`.
- **C2 / C9 / C14b (Hamming mod 4):** `(6, 6, 10, 10)`. L1 distance from target: `|6-2| + |6-6| + |10-10| + |10-14| = 8`.
- **C2b (signed hw):** `(2, 10, 20, 0)`. Gets the first bin (2) right; rest off.
- **C28 (hw 4-bin):** `(1, 5, 20, 6)`. Reproduces the (1, 5, ...) start of Pascal's row.

The **closest L1 candidate** is the hw-mod-4 family `(6, 6, 10, 10)` at L1 = 8. This is the natural binomial folding `1+5, 10, 10, 5+1` (collapsing parity pairs of Pascal's row) and is interpretation-stable but **the wrong shape** for Pauli.

## §4 — Conclusion: COINCIDENCE-BOUND

The 32 = 32 equality is a **Pascal-type coincidence**, not a hidden bijection. Quantitative bound:

- **Random-map probability:** A uniformly random function `f: {0,1}^5 → {0,1,2,3}` matches `(2, 6, 10, 14)` with probability `C(32; 2, 6, 10, 14) / 4^32 = 5.78×10^14 / 1.84×10^19 ≈ 3.13×10^-5` (i.e., 1 in ~32 000).
- **Natural-low-complexity families:** 0 of 730 956+ functions in the four most natural classes (linear, permutation-linear, symmetric, low-arity dictator, low-degree polynomial) match the target.
- **Hand-built structural candidates motivated by TIG vocabulary:** 0 of 37 match.

The conclusion is **definitive**: the integer match `32 = 32` is a **summation coincidence** between two independent partitions of the integer 32 into different cell-counts. Specifically:

  - Pascal's row C(5, k) sums to 32 via `1 + 5 + 10 + 10 + 5 + 1`.
  - Pauli capacities sum to 32 via `2(2l+1)` summed for `l = 0..3` = `2 + 6 + 10 + 14`.
  - Both are well-known structural identities (the first from the binomial theorem, the second from the dimension formula `2n^2` of the n-th shell).
  - The "coincidence" `2^5 = 2·4^2` is purely arithmetic: `32 = 2^5 = 2·16 = 2·4^2`. The first factor `2` is the spin doubling; the `4^2` is the principal-quantum-number factor. Pascal's row C(5, k) reaches `2^5` via summing all binomial coefficients on a 5-element set.

**There is no natural mechanism producing the `(2, 6, 10, 14)` shape from the `(1, 5, 10, 10, 5, 1)` shape.** The retired J47 D104 "bijection" relied on a hand-built partition with no canonical functional form.

This **closes the §1.1 honest-negative** as a coincidence-bound: the integer match is real, the bijection does not exist, and the apparent triple `(2^5 = 32 = 2·4^2 = Pauli n=4 capacity)` is a numerological coincidence at the order of 1 in 32 000 — striking but not structurally forced.

## §5 — Suggested follow-up

1. **Update `HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §1.1** to add a line: "*Bijection search closed 2026-05-27 (COINCIDENCE-BOUND): 0 of 730 956+ low-complexity functions match; random-map probability is ~1/32 000. See `04_meta/frontiers_2026-05-27/F2_32_32_bijection.md`.*"

2. **Optionally retire the claim in retired-J47/D104** that the script "closes" the negative. The script demonstrates a hand-built 8-class partition matches the right counts; that's a fact, but it's not a canonical bijection. The script is OK as a curiosity but should be re-titled (e.g., from `pauli_divisor_bijection.py` to `pauli_divisor_handpartition.py`) and its docstring updated to acknowledge the hand-built nature.

3. **The structural-rhyme intuition** that "`Z/2310` has 32 divisors *and* the n=4 Pauli shell has 32 states *and* both equal `2·4^2`" is still worth recording as a **summation coincidence at the order of `2^5`**. It does not become a theorem, but it might be worth a 1-page Math. Intelligencer note as proposed in the retired-J47 README option (b).

4. **A genuinely different question** worth pursuing: does the `(1, 5, 10, 10, 5, 1)` distribution of Z/2310 divisor classes have a *natural* physical interpretation that ISN'T atomic shells? Candidates: 6-bit Hamming-code weight distribution, 5-simplex face lattice (1 vertex, 5 edges, 10 triangles, 10 tetrahedra, 5 4-faces, 1 5-face), 6-bit error-correction-code structure. The framework already uses Cl(0, 10) extensively; the (1, 5, 10, 10, 5, 1) shape is naturally the dimension count of the exterior algebra Λ^k(R^5). This is a more honest reframe than forcing Pauli capacities.

---

**Scripts (all in `04_meta/frontiers_2026-05-27/`):**
- `F2_candidates.py` — 20 hand-built candidates + brute-force linear/threshold
- `F2_coincidence_bound.py` — coincidence-bound calculation + 5 natural function classes
- `F2_extended_natural.py` — 17 additional TIG-substrate-motivated candidates

**Total searches: 37 hand-built + 730 956+ brute-force = 730 993+ functions tested. Zero matches in any natural class.**
