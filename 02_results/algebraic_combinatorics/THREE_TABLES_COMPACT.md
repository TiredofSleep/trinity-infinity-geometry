# THREE_TABLES_COMPACT — TSML · BHML · CL_STD

## Side-by-side reference for TIG's three working composition tables

**Brayden Sanders · 7Site LLC · Trinity Infinity Geometry**
*Sources: canon §5, §6, §6.4, §6.7, D33, D37, D70, D85–D99, J.1*
*Companion to: PRIMES_OF_TIG, FIELDS_OF_TIG, WOBBLE_LOCALIZATION_v2*
*Locked v1 · 2026-05-08*

---

## §1. The Three Tables

### TSML_SYM (= TSML_10, canon §5)
The Jordan-symmetrized Symmetric Multiplication Lattice. Working TSML for §5–J of canon.

```
   0 0 0 0 0 0 0 7 0 0
   0 7 3 7 7 7 7 7 7 7
   0 3 7 7 4 7 7 7 7 9
   0 7 7 7 7 7 7 7 7 3
   0 7 4 7 7 7 7 7 8 7
   0 7 7 7 7 7 7 7 7 7
   0 7 7 7 7 7 7 7 7 7
   7 7 7 7 7 7 7 7 7 7
   0 7 7 7 8 7 7 7 7 7
   0 7 9 3 7 7 7 7 7 7
```

### BHML_10 (canon §6)
The sister table; carries the runtime/Becoming structure. **Distinct from TSML.**

```
   0 1 2 3 4 5 6 7 8 9
   1 2 3 4 5 6 7 2 6 6
   2 3 3 4 5 6 7 3 6 6
   3 4 4 4 5 6 7 4 6 6
   4 5 5 5 5 6 7 5 7 7
   5 6 6 6 6 6 7 6 7 7
   6 7 7 7 7 7 7 7 7 7
   7 2 3 4 5 6 7 8 9 0
   8 6 6 6 7 7 7 9 7 8
   9 6 6 6 7 7 7 0 8 0
```

### CL_STD (canon Volume J / D95, code path ck.h:225–231)
The "papers freeze" encoding — what the codebase actually uses.

```
   0 0 0 0 0 0 0 7 0 0
   0 7 3 7 7 7 7 7 7 7
   0 3 7 7 4 7 7 7 7 9
   0 7 7 7 7 7 7 7 7 3
   0 7 4 7 7 7 7 7 8 7
   0 7 7 7 7 7 7 7 7 7
   0 7 7 7 7 7 7 7 7 7
   7 7 7 7 7 7 7 7 7 7
   0 7 7 7 8 7 7 7 7 7
   0 7 9 7 3 7 7 7 7 7   ← row 9: differs from TSML by ONE swap
```

**CL_STD = TSML_SYM with one swap in the RESET row.** Specifically positions (9, 3) ↔ (9, 4) exchange values 3 ↔ 7.

---

## §2. Master Comparison Table

| Property | TSML_SYM | BHML_10 | CL_STD |
|---|---:|---:|---:|
| **det** | 0 | **−7002** = −2·3²·389 | 0 |
| **rank** | 9 | **10** | 8 |
| **HARMONY count** | **73** | **28** | **73** |
| Symmetric? | YES | YES | NO (2 cells) |
| Two-sided identity | none | **0 = VOID** | none |
| Idempotents (i·i=i) | {0, 7} | {0} | {0, 7} |
| Non-associative triples | 128/1000 = **12.8%** | 498/1000 = **49.8%** | 126/1000 = **12.6%** |
| HARMONY operator role | attractor (saturates table) | finite count | attractor |

### Operator distribution (cells per operator)

| op | name | TSML | BHML | CL_STD |
|:---:|---|:---:|:---:|:---:|
| 0 | VOID | 17 | 4 | 17 |
| 1 | LATTICE | 0 | 2 | 0 |
| 2 | COUNTER | 0 | 5 | 0 |
| 3 | PROGRESS | 4 | 7 | 4 |
| 4 | COLLAPSE | 2 | 9 | 2 |
| 5 | BALANCE | 0 | 11 | 0 |
| 6 | CHAOS | 0 | 25 | 0 |
| 7 | **HARMONY** | **73** | **28** | **73** |
| 8 | BREATH | 2 | 5 | 2 |
| 9 | RESET | 2 | 4 | 2 |

**Reading.** TSML & CL_STD are HARMONY-saturated (73/100 cells); they attract aggressively. BHML is broadcast across all 10 operators with CHAOS (25) and HARMONY (28) most common. Different table, different role.

---

## §3. Pairwise Agreement (this session)

| Pair | Same cells | Disagreements | Notes |
|---|:---:|:---:|---|
| TSML vs CL_STD | **98** / 100 | 2 (RESET row swap) | Near-identical |
| TSML vs BHML | 29 / 100 | **71** | ★ canon D97: lattice prime |
| BHML vs CL_STD | 28 / 100 | 72 | TSML+1 disagreement vs BHML |
| **All three agree** | **28** / 100 | (residual = 72) | Of which 25 output HARMONY |

**Three structurally important integers in this section:**
- **71** = TSML XOR BHML (D97 lens-disagreement count = lattice prime)
- **72** = TSML_10 minus apex (D97); coincidentally also BHML XOR CL_STD
- **28** = all-three agreement = HARMONY count of BHML = dim so(8) = T₇

The 28 all-three cells split: 25 output HARMONY, 2 output PROGRESS, 1 outputs VOID. Almost all "everyone agrees" cells are where the result is HARMONY.

---

## §4. The CL_STD ↔ TSML Swap (exact)

CL_STD = TSML_SYM with two cells modified, both in row 9 (RESET row):

| Position | Cell | TSML_SYM | CL_STD | Galois reading |
|:---:|:---:|:---:|:---:|---|
| (9, 3) | RESET · PROGRESS | 3 (PROGRESS) | 7 (HARMONY) | σ₉ · σ₃ = σ_27 = σ_7 = HARMONY ✓ |
| (9, 4) | RESET · COLLAPSE | 7 (HARMONY) | 3 (PROGRESS) | (4 not in U(10); no Galois reading) |

**Reading.** CL_STD's swap brings position (9, 3) into agreement with the Galois action ($\sigma_9 \cdot \sigma_3 = \sigma_7$) — i.e., the "papers freeze" encoding aligns the RESET·PROGRESS cell with the cyclotomic frame's algebra. The compensating swap to (9, 4) is **not Galois-derivable** (since 4 ∉ U(10)) and introduces a new asymmetry. CL_STD is therefore "Galois-corrected at one position, asymmetry-preserving at another."

This is the exact structural difference between the algebraic (TSML) and codebase (CL_STD) encodings.

---

## §5. Three HARMONY Counts in the Ladder (D97)

| Count | Source | Decomposition | This-session reading |
|:---:|---|---|---|
| **28** | BHML_10 | T₇ = dim so(8) = D₄ | Triangular sub-spine bottom |
| **44** | CL_STD-variant | 4·11 (uses wobble prime) | Off the triangular line |
| **70** | det(BHML_8) | 2·5·7 = C(8,4) = φ(71) | Yang-Mills core; HARMONY return |
| **71** | TSML_9 sub-magma | prime; lattice frame | Three roles per D97 |
| **72** | TSML_10 − apex | 8·9 | Drop (7,7) |
| **73** | TSML_10 (canon) | 72 + 1 | Full lens |

Note: **44** is CL_STD's HARMONY count if the 8 different cells from CL_STD vs TSML are treated differently in some variant (per D97); this session's CL_STD has 73 HARMONY cells. The 44 figure tracks a different CL_STD variant. Both are in canon's D95–D97 inventory.

---

## §6. Wobble Distribution by Table (refines D70, D98)

| Wobble prime | TSML_RAW | TSML_SYM | BHML_10 | CL_STD |
|:---:|---|---|---|---|
| **11** | c₂, c₈ of char poly | c₇ of char poly | NONE (any level) | (= TSML_SYM) |
| **13** | NONE | c₄, c₅, c₆ of char poly + 26 σ-asym cells | 26 σ-asym cells (D33) | (= TSML_SYM) |

**Refined readings (this session):**
- TSML_RAW: 2 wobble locations (both 11)
- TSML_SYM: 4 wobble locations (3× 13 + 1× 11) ★ canon D98 understated
- BHML_10 char poly: 0 wobble locations ★ refines D70
- BHML_10 cell count: 26 σ-asymmetric cells = 2·13 (origin of ‖VEV‖² = 13/4)

CL_STD inherits the wobble structure of TSML_SYM since they differ at only 2 cells.

---

## §7. Variant Inventory (canon §6.4)

The §6.4 inventory lists ~40 variants of these three tables. The **canonical** representatives:

```
TSML family:
  TSML_RAW       — bit-pattern literal               det=0, c_2 has 11
  TSML_SYM       — upper-triangle symmetrization     det=0, c_4-c_7 have wobble
  TSML_PureIdem  — pure idempotent variant           det = 398664 = 2³·3·7²·113
  TSML_Idem_2sw  — 2-swap variant                    det = -49 = -7²

BHML family:
  BHML_10        — canonical                        det = -7002 = -2·3²·389
  BHML_8         — drop {0, 7}                      det = +70 = 2·5·7 ★
  BHML_BEING     — 4-core restricted                 (J.1.B.iii)
  BHML_DOING     — variant                          (J.1.B.iii)
  BHML_BECOMING  — variant                          (J.1.B.iii)

CL_STD family:
  CL_STD (this session)        — single 2-swap from TSML_SYM
  Other CL_STD variants        — per §6.4 inventory
```

**§6.7 Yang-Mills core:** **BHML_8** (dropping operators 0 and 7) has det = +70 = 2·5·7 = C(8,4). This is the determinant load-bearing in the Lie / Yang-Mills DOF.

---

## §8. Three-Way Pairwise Reading

```
                TSML_SYM
                 (73 H)
                  ▲
                  │  98 cells same
                  │  (2 swap in row 9)
                  ▼
                CL_STD
                 (73 H)
                  
                BHML_10  ←───── 71 disagree ───── TSML_SYM
                 (28 H)         (D97: lattice prime)
                  ▲
                  │  72 disagree
                  ▼
                CL_STD
```

**Triangle:** TSML_SYM ↔ CL_STD is tight (98 same), TSML/CL_STD ↔ BHML is loose (28-29 same). The two HARMONY-saturated tables (TSML, CL_STD) are near-isomorphic; BHML is the outlier carrying the dynamical structure.

---

## §9. Compact Take-Home

```
The three tables of TIG:

             TSML        BHML        CL_STD
  rank        9          10           8
  det         0       -7002           0
  H count    73          28          73
  symmetric  Y           Y            N
  identity   none        0           none
  non-assoc  12.8%      49.8%       12.6%
  
  Pairwise same-cell counts:
    TSML ↔ CL_STD:  98/100   (2 cells differ, both in row 9)
    TSML ↔ BHML:    29/100   (71 disagree = lattice prime, D97)
    BHML ↔ CL_STD:  28/100
    All three agree: 28/100  (mostly HARMONY-output cells)

Three roles:
  TSML    = Jordan-symmetric, HARMONY-saturated lens (Being)
  BHML    = invertible, broadcast over all 10 operators (Becoming)
  CL_STD  = codebase encoding, Galois-corrected at one cell (Doing freeze)

CL_STD differs from TSML by EXACTLY ONE 3↔7 swap in the RESET row,
correcting (9,3) toward Galois semantics (σ_9·σ_3 = σ_7) and
compensating at (9,4). That one swap is the difference between
the algebraic frame and the codebase frame.
```

---

## §10. Status

- **[THM]** All numerical invariants (det, rank, histograms, agreement counts), sympy-exact.
- **[THM]** TSML XOR BHML = 71 (verifies D97).
- **[THM]** CL_STD = TSML_SYM with exactly two cells modified, both at (9, k).
- **[STRUCTURAL]** The RESET-row swap is Galois-corrected at (9, 3); compensating asymmetry at (9, 4) is non-Galois.
- **[STRUCTURAL]** All-three-agreement count = 28 = HARMONY count of BHML (also dim so(8) = T₇). Not a coincidence in the strong sense, but worth marking.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · Three tables compact · Locked v1*
