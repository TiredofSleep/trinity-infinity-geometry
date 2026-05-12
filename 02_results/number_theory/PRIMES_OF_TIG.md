# PRIMES_OF_TIG — Compact Synthesis

## Every prime appearing in canon D1–D99, organized into four strata

**Brayden Sanders · 7Site LLC · Trinity Infinity Geometry**
*Synthesis output: condensed prime spectrum table with cross-stratum bridges*
*Status: locked v1 · 2026-05-08*

---

## §1. The Four Strata

| Stratum | Primes | Role |
|---|---|---|
| **I** Substrate | {2, 3, 5} | CRT decomposition Z/2 × Z/5; AG(2,3) base F₃; cyclotomic ramification |
| **II** Attractor | {7} | HARMONY operator; T* = 5/7; class numbers; BHML_8 det 2·5·7 |
| **III** Wobble | {11, 13} | Coordinate/eigenvalue axes; basis-dependent locations |
| **IV** Lattice | {71} | Field-theoretic invariant; runtime-attractor field disc |
| **Outliers** | {113, 191, 229, 313, 389, 659} | Single-occurrence in dets/residues; no cross-DOF role |

---

## §2. The Stratum Bridge: 2·71 + 1 = 11·13

**Key structural identity.** The Sophie-Germain step on 71 produces exactly the two wobble primes:

$$2 \cdot 71 + 1 \;=\; 143 \;=\; 11 \cdot 13$$

This ties Stratum IV (71, lattice) to Stratum III (11, 13, wobble) through a single integer step. Not a coincidence dependent on choosing 71 — it's the unique integer relation linking the three primes that already appear in canon's WOBBLE structure.

**Implication for TIG:** the lattice prime 71 is the "germ" whose Sophie-Germain doubling produces the wobble pair (11, 13). One generator, two manifestations.

---

## §3. Per-Prime Summary

### Prime 2 (Stratum I)
- Z/2Z factor of CRT decomposition Z/10 ≅ Z/2 × Z/5
- BALANCE = (1, 0) ∈ Z/2 × Z/5; the Z/2 idempotent
- Even non-units {2, 4, 6, 8} multiplicative Z/4Z (session, identity 6)
- disc Q(√3) = 12 = 4·3 = 2²·3
- disc LMFDB 4.2.10224.1 = −2⁴·3²·71 (D41)

### Prime 3 (Stratum I)
- AG(2,3) base field F₃; the affine plane
- PROGRESS = 3 = generator of U(10) = C corners (Plichta cross)
- σ₃: ζ ↦ ζ³ generator of Gal(Q(ζ₁₀)/Q) (session)
- disc Q(√3) = 12 = 4·3
- 3² in disc LMFDB 4.2.10224.1 (D41)
- 3 = "every one is three" L0 triadic principle

### Prime 5 (Stratum I)
- BALANCE operator = 5 in Z/10Z
- T* = **5**/7 numerator (six derivations)
- disc Q(ζ_10) = +**5**³ = 125 — UNIQUE ramified prime in cyclotomic frame
- α⁻¹ = 22·6 + 5 = 137 (canonical decomposition)
- α⁻¹ = **5**³ + 12 (session decomposition)
- Z/5Z factor of CRT; CHAOS = 6 is its idempotent

### Prime 7 (Stratum II)
- HARMONY operator = 7 in Z/10Z
- T* = 5/**7** denominator
- BHML_8 det = **70** = 2·5·**7** (Yang-Mills core, WP15)
- BHML_10 cells with HARMONY: 28, TSML_10: 73, CL_STD: 44 — varying counts
- 7² in det(TSML_PureIdempotent) = 398664 = 2³·3·**7²**·113 (§6.4)
- Class number Q(√−71) = **7**
- Fine structure: T* = 7/10 + 1/(**7**·10) (D22)
- 7³ in the discriminant of TSML char poly (D37): 2¹⁶·**7⁷**·…

### Prime 11 (Stratum III, wobble)
**Five distinct locations** (D70, D85, D86, +session):
1. TSML_RAW char poly coefficient c_2 = 33 = 3·**11** (D37)
2. TSML_RAW char poly coefficient c_8 = −120736 has factor **11** (D37)
3. Br/V denominator: minimal poly leading coeff **11** (D69)
4. F8 simplex Jacobian trace polynomial disc **11⁶** (D85)
5. Operator-sum of TRANSFORMATION σ²-cycle: 1+6+4 = **11** (D86)

**Cross-bridge:** 11 = (2·71+1)/13. Tied to lattice prime via Sophie Germain step.

### Prime 13 (Stratum III, wobble)
- ‖VEV‖² = **13**/4 (D33), origin: 26 σ_outer-asymmetric BHML cells / 2
- κ_ξ = **13**/(4e) inflaton coupling (D35)
- **Cross-bridge:** 13 = (2·71+1)/11. Tied to lattice prime via Sophie Germain step.

### Prime 71 (Stratum IV, lattice)
**Three structural roles in canon (D97):**
1. TSML_9 sub-magma HARMONY count = **71**
2. |TSML XOR BHML| lens-disagreement count = **71** (SYM lens)
3. LMFDB 4.2.10224.1 field disc squarefree part = −**71**

**Three more in adjacent results:**
4. F8 simplex Jacobian trace polynomial field disc = −10224 also has −**71** (D87)
5. Q(√−71) class number = 7 = HARMONY (textbook)
6. φ(71) = **70** = BHML_8 det = C(8,4) (textbook)

**Cross-bridge:** 2·**71** + 1 = 11·13. Tied to wobble pair via Sophie Germain step.

### Outlier Primes (single-occurrence)

| Prime | Location | Notes |
|---|---|---|
| 113 | det(TSML_PureIdempotent) = 2³·3·7²·**113** | Variant table |
| 191 | T* − DE = **191**/7000 (session Sprint A) | Cosmological residue |
| 229 | DE = (3·**229**)/1000 (session) | Cosmological residue |
| 313 | DM + VM = **313**/1000 (session) | Cosmological residue |
| 389 | det(BHML_10) = −2·3²·**389** | Canonical BHML det |
| 659 | TSML char poly disc factor (D37) | Char-poly factor |

These appear in exactly one location each. No cross-DOF or cross-stratum role established.

---

## §4. Returns and Reflections

Three primes "return" — they appear in multiple strata or in textbook properties that map back to TIG operators:

| Prime | Returns |
|---|---|
| **7** | HARMONY operator; T* denominator; class h(Q(√−71)) = 7; 7² in TSML_Idem det; 7³ in TSML char poly disc |
| **70 = 2·5·7** | BHML_8 det; φ(71); HARMONY ladder bottom rung (D97) |
| **71** | Three roles in D97 + class h connection + φ(71) connection |

The structure: HARMONY (7) is the attractor not just operationally but **arithmetically** — class numbers, totients, and discriminants of nearby fields all return to it.

---

## §5. The HARMONY Count Ladder (D97 + extended)

Synthesis: every HARMONY count integer in canon, with structural reading.

| # | Source | Decomposition | Reading |
|---|---|---|---|
| **28** | BHML_10 HARMONY | T₇ (7th triangular) = dim **so(8) = D₄** (D26) | The Becoming-lens HARMONY count IS the dim of the Lie algebra of triality |
| **36** | TSML_7 HARMONY | T₈ (8th triangular) = sum 1..8 | One triangular step beyond BHML; chain rung 7 |
| **44** | CL_STD HARMONY | 4·**11** (Stratum-III wobble factor) | Standard encoding HARMONY uses wobble prime |
| **45** | dim **so(10) = D₅** (D27) | T₉ (9th triangular) | The Lie algebra dim, NOT a HARMONY count |
| **70** | det(BHML_8) | 2·5·7 = C(8,4) = φ(71) | Yang-Mills core determinant |
| **71** | TSML_9 HARMONY | prime; lattice prime | Three roles per D97 |
| **72** | TSML_10 − apex | 8·9 (active operators × RESET) | Drop the (7,7) self-cell |
| **73** | TSML_10 HARMONY | 72 + 1 (one beyond Being) | The full prescribed view |

**Triangular sub-spine.** T₇ = 28, T₈ = 36, T₉ = 45 — three sequential triangulars. The first two are HARMONY counts (BHML_10, TSML_7); the third is dim so(10). The Lie-algebra dimension lives one triangular step beyond the largest HARMONY count in the chain.

**Wobble interpolation.** 44 = CL_STD HARMONY = 4·11 sits between T₇ = 28 and T₉ = 45 but is **not triangular**. It uses the wobble prime, breaking the triangular sub-spine. CL_STD ("the papers freeze," D95) is structurally distinct from the chain-wise HARMONY counts.

---

## §6. Cyclotomic vs Lattice Frame

Two number fields appear in TIG with disjoint ramification:

| Field | Discriminant | Ramified primes | Carrier |
|---|---|---|---|
| **Q(ζ₁₀)** (cyclotomic) | +5³ = 125 | {5} | C corners = U(10) |
| **Q(√3)** (real subfield, lattice) | 12 = 2²·3 | {2, 3} | runtime mid-tower |
| **LMFDB 4.2.10224.1** (full lattice) | −2⁴·3²·71 | {2, 3, 71} | full runtime attractor |

**No prime overlap:** {5} (cyclotomic) ∩ {2, 3, 71} (lattice) = ∅.

The cyclotomic frame ramifies only at BALANCE-prime; the lattice frame ramifies at substrate primes 2, 3 plus the lattice prime 71. Wobble primes (11, 13) appear in **neither** discriminant — they live at coefficient/coordinate level, not as ramification data.

---

## §7. Compact Take-Home

```
TIG prime spectrum (canon D1-D99):

  Stratum I (substrate, ≤5):    2, 3, 5     CRT + cyclotomic frame
  Stratum II (HARMONY):         7           T* denominator + class h(-71)
  Stratum III (wobble):         11, 13      coefficient/eigenvalue layer
  Stratum IV (lattice):         71          runtime field disc

Key bridge:
  2·71 + 1 = 11·13              III ↔ IV via Sophie Germain step

Returns to HARMONY (prime 7):
  T* = 5/7                      operator-level
  BHML_8 det = 70 = 2·5·7       structural det
  φ(71) = 70                    totient of lattice prime
  Q(√-71) class number = 7      adjacent quadratic field
  TSML char poly disc has 7^7   variant signature

HARMONY counts ladder (T_n = triangular):
  28 = T_7 = dim so(8)          BHML_10 HARMONY
  36 = T_8                      TSML_7 HARMONY
  44 = 4·11                     CL_STD (wobble interpolation)
  45 = T_9 = dim so(10)         (Lie dim, not HARMONY)
  70 = 2·5·7 = C(8,4) = φ(71)   BHML_8 det
  71                            TSML_9 HARMONY (3 roles, D97)
  72 = 8·9                      TSML_10 minus apex
  73                            TSML_10 HARMONY (canonical)

No prime overlap between cyclotomic disc (5³) and lattice disc
(2^4·3^2·71). Wobble primes 11, 13 in neither.
```

---

## §8. New Observations from this Synthesis

- **2·71+1 = 11·13** ties strata III and IV through Sophie Germain step. Worth recording as a TIG-structural arithmetic identity. **[NEW from this synthesis]**
- **Q(√−71) class number = 7** is textbook; its identification with HARMONY is structural. **[Consequence of canon + textbook]**
- **φ(71) = 70 = det(BHML_8)** ties the totient of the lattice prime to the Yang-Mills core determinant. **[Consequence of canon + textbook]**
- **T₇ = 28 = dim so(8) = BHML_10 HARMONY** is one triangular step. T₉ = 45 = dim so(10). **[Consequence of canon + arithmetic]**
- **CL_STD HARMONY = 44 = 4·11** sits off the triangular sub-spine, using wobble prime. **[Reading of D97]**

---

## §9. Status

- **[THM]** The Sophie Germain identity 2·71+1 = 11·13 (trivial verification).
- **[THM]** Q(√−71) class h = 7 (textbook).
- **[THM]** φ(71) = 70 (textbook).
- **[THM]** T₇ = 28 = dim so(8); T₉ = 45 = dim so(10) (textbook + canon D26, D27).
- **[STRUCTURAL]** The four-strata classification of TIG primes.
- **[STRUCTURAL]** The ladder/triangular reading of HARMONY counts.
- **[OPEN]** Whether the III↔IV bridge 2·71+1 = 11·13 is the unique such relation, or whether other primes p admit 2p+1 factoring as TIG-structural prime products.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · Primes of TIG synthesis · Locked v1*
