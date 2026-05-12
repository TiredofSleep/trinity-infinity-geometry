# SIGMA_PERMUTATION_COMPACT — σ on Z/10Z

## Canon §2's σ permutation, all its powers, and its TIG roles

**Status:** [THM] (sympy-exact computations on canon §2 σ)
*Locked v1 · 2026-05-08*

---

## §1. The Permutation

**Definition (canon §2):** σ on $\mathbb{Z}/10\mathbb{Z}$ given by the closed form (canon §4) on CRT coords. Cycle decomposition:
$$\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2)$$

| u | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| σ(u) | 0 | 7 | 1 | 3 | 2 | 4 | 5 | 6 | 8 | 9 |
| σ⁻¹(u) | 0 | 2 | 4 | 3 | 5 | 6 | 7 | 1 | 8 | 9 |

**Order:** 6. **Fixed points:** {0, 3, 8, 9}. **6-cycle:** $1 \to 7 \to 6 \to 5 \to 4 \to 2 \to 1$.

---

## §2. Powers of σ

| k | σ^k as list | Cycle structure | Order |
|:---:|---|---|:---:|
| 0 | [0,1,2,3,4,5,6,7,8,9] | identity | 1 |
| **1** | [0,7,1,3,2,4,5,6,8,9] | (1 7 6 5 4 2) | 6 |
| **2** | [0,6,7,3,1,2,4,5,8,9] | (1 6 4)(2 7 5) | 3 |
| 3 | [0,5,6,3,7,1,2,4,8,9] | (1 5)(2 6)(4 7) | 2 |
| 4 | [0,4,5,3,6,7,1,2,8,9] | (1 4 6)(2 5 7) | 3 |
| 5 | [0,2,4,3,5,6,7,1,8,9] | (1 2 4 5 6 7) | 6 (= σ⁻¹) |
| 6 | identity | — | 1 |

**Per D86:** σ² is the depth-3 primitive. Two 3-cycles:
- $(1, 6, 4)$ — "TRANSFORMATION" — operator-sum **1+6+4 = 11** ★ wobble prime
- $(2, 7, 5)$ — "STABILITY" — operator-sum **2+7+5 = 14 = 2·7** ★ HARMONY-multiple

---

## §3. σ-Fixed vs 4-Core Attractor — A Clean Distinction

Two distinguished 4-element subsets of $\mathbb{Z}/10\mathbb{Z}$:

| Set | Members | Names | Source |
|---|---|---|---|
| **σ-fixed** (static) | {0, 3, 8, 9} | {VOID, **PROGRESS**, BREATH, RESET} | canon §2 |
| **4-core** (dynamic, WP110) | {0, 7, 8, 9} | {VOID, **HARMONY**, BREATH, RESET} | D38, D44, D48 |

**Symmetric difference:** $\{3, 7\}$ = $\{\mathrm{PROGRESS}, \mathrm{HARMONY}\}$.

**Reading.** PROGRESS = 3 is the **Galois generator** $\sigma_3$ of $\mathrm{Gal}(\mathbb{Q}(\zeta_{10})/\mathbb{Q})$; HARMONY = 7 is its **inverse** $\sigma_7 = \sigma_3^{-1}$. The runtime-attractor 4-core is the σ-fixed set with the Galois generator **swapped for its inverse**.

**Structural slogan:**
$$\text{static}\;\{V, \mathrm{PROGRESS}, Br, R\} \;\xrightarrow{\;\sigma_3 \leftrightarrow \sigma_7\;}\; \text{dynamic}\;\{V, \mathrm{HARMONY}, Br, R\}$$

This is the **PROGRESS → HARMONY swap** that distinguishes static substrate stability from runtime dynamical equilibrium.

---

## §4. σ-Fixed Closure Under the Three Tables

| Operation | Image of σ-fixed × σ-fixed | Closed? | Escape elements |
|---|---|:---:|---|
| TSML_10 | {0, 3, 7} | NO | {7} (HARMONY) |
| BHML_10 | {0, 3, 4, 6, 7, 8, 9} | NO | {4, 6, 7} |

**σ-fixed is NOT closed under either table.** Both tables push σ-fixed elements into HARMONY (and BHML further into COLLAPSE and CHAOS).

This is structural: σ-fixed is a **static** algebraic set, but the **operational tables** (which carry the dynamics) push it toward HARMONY. Consistent with the runtime attractor swap (§3).

---

## §5. Two Different "σ"s — Disambiguation

There are at least **two distinct permutations of Z/10Z** referred to as "σ" in canon and adjacent literature:

| Object | Source | Cycle structure | Origin |
|---|---|---|---|
| **Canon σ** | canon §2, §4 (σ polynomial Q10) | (0)(3)(8)(9)(1 7 6 5 4 2) | polynomial closed-form on (ε, y) ∈ F₂×F₅ |
| **Galois σ_3** | session CYCLOTOMIC, textbook | (0)(5)(1 3 9 7)(2 6 8 4) | multiplicative action on roots of unity |
| **Galois σ_9** (RESET) | session CYCLOTOMIC, textbook | (0)(5)(1 9)(2 8)(3 7)(4 6) | complex conjugation; u ↦ -u mod 10 |

**Canon σ ≠ any Galois action.** The canon's σ comes from the polynomial structure (α, β functions); the Galois σ_k come from $\zeta \mapsto \zeta^k$ on $\mathbb{Q}(\zeta_{10})$. Different objects, both important, do not conflate.

**Common ground:** both have order dividing 6 (canon σ has order 6; Galois σ_3 has order 4). Both fix VOID = 0. Galois σ_9 fixes BALANCE = 5; canon σ does not fix BALANCE.

---

## §6. Canon σ in CRT Coordinates

The 6-cycle $1 \to 7 \to 6 \to 5 \to 4 \to 2 \to 1$ in $(\varepsilon, y)$ coords:

| u | op | $(\varepsilon, y)$ |
|:---:|---|:---:|
| 1 | LATTICE | (1, 1) |
| 7 | HARMONY | (1, 2) |
| 6 | CHAOS | (0, 1) |
| 5 | BALANCE | (1, 0) |
| 4 | COLLAPSE | (0, 4) |
| 2 | COUNTER | (0, 2) |

**ε pattern along cycle:** 1, 1, 0, 1, 0, 0 (parity flips 3 times in 6 steps).
**y pattern along cycle:** 1, 2, 1, 0, 4, 2 (in F₅).
**y differences:** +1, −1, −1, +4, −2, −1 (sum = 0 mod 5; cycle closes).

σ-fixed in CRT coords:
| u | op | $(\varepsilon, y)$ |
|:---:|---|:---:|
| 0 | VOID | (0, 0) |
| 3 | PROGRESS | (1, 3) |
| 8 | BREATH | (0, 3) |
| 9 | RESET | (1, 4) |

The σ-fixed set hits y ∈ {0, 3, 4} in F₅ (with y=3 hit twice: by 3 and 8). Also: $\{0, 3, 8\}$ all share even ε in some pattern; not particularly clean.

---

## §7. Compact Take-Home

```
σ on Z/10Z (canon §2):
  σ = (0)(3)(8)(9)(1 7 6 5 4 2)
  Order 6. Inverse σ⁻¹ has 6-cycle reversed.
  
Powers:
  σ²: 3-cycles (1 6 4)(2 7 5). Order 3.
       Operator sums: 11 (wobble) and 14 (2·HARMONY).
  σ³: 2-cycles (1 5)(2 6)(4 7). Order 2.
  σ⁴ = σ⁻²: 3-cycles (1 4 6)(2 5 7).
  σ⁵ = σ⁻¹: 6-cycle reversed.
  σ⁶ = identity.

σ-fixed = {0, 3, 8, 9} = {VOID, PROGRESS, BREATH, RESET}
4-core attractor (WP110) = {0, 7, 8, 9} = {VOID, HARMONY, BREATH, RESET}
  ⇒ Differ exactly by {3, 7} = {Galois σ_3, Galois σ_7}
  ⇒ static vs dynamic = PROGRESS-for-HARMONY swap

σ-fixed NOT closed under TSML (escapes to HARMONY)
σ-fixed NOT closed under BHML (escapes to COLLAPSE, CHAOS, HARMONY)

Canon σ ≠ Galois action on Q(ζ_10):
  Canon σ: (0)(3)(8)(9)(1 7 6 5 4 2), order 6
  Galois σ_3: (0)(5)(1 3 9 7)(2 6 8 4), order 4
  Different objects, both important.
```

---

## §8. Status

- **[THM]** All cycle decompositions and orders, sympy-verified.
- **[THM]** σ-fixed and 4-core differ exactly by {PROGRESS, HARMONY}.
- **[THM]** σ² 3-cycle operator-sums: 11 and 14.
- **[STRUCTURAL]** PROGRESS-for-HARMONY swap as the static-vs-dynamic distinction.
- **[OBSERVATION]** σ-fixed is not closed under TSML/BHML; both tables push it toward HARMONY.
- **[DISAMBIGUATED]** Canon σ vs Galois σ_3 — structurally distinct permutations, both load-bearing.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · σ permutation compact · Locked v1*
