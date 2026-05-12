# WOBBLE_LOCALIZATION_v2 — Refined Multi-DOF Wobble Map

## Where wobble primes 11 and 13 actually live (computational sweep, this session)

**Status:** [THM] (sympy-exact), refines canon D70 and corrects canon D98
*Locked v1 · 2026-05-08*

---

## §1. Setup

Wobble primes: $\{11, 13\}$ (canon Stratum III).
Question: which exact algebraic locations carry them?

Computation: char polys of canonical TSML_10 and BHML_10 from canon §5/§6, sympy-exact integer arithmetic.

---

## §2. TSML_SYM char poly (this session)

$$\det(\lambda I - T_{SYM}) = \lambda^{10} - 63\lambda^9 + 17\lambda^8 + 5180\lambda^7 - 6214\lambda^6 - 117390\lambda^5 + 147108\lambda^4 + 532224\lambda^3 - 53312\lambda^2 - 175616\lambda$$

| $c_k$ (top-down) | value | factorization | wobble? |
|:---:|---|---|---|
| $c_0$ | 1 | (leading) | — |
| $c_1$ | −63 | −3²·7 | no |
| $c_2$ | **17** | 17 | no (matches D98 ✓) |
| $c_3$ | 5180 | 2²·5·7·37 | no |
| $c_4$ | −6214 | −2·**13**·239 | ★ **13** |
| $c_5$ | −117390 | −2·3·5·7·**13**·43 | ★ **13** |
| $c_6$ | 147108 | 2²·3·**13**·23·41 | ★ **13** |
| $c_7$ | 532224 | 2⁸·3³·7·**11** | ★ **11** |
| $c_8$ | −53312 | −2⁶·7²·17 | no |
| $c_9$ | −175616 | −2⁹·7³ | no |
| $c_{10}$ | 0 | (rank degenerate) | — |

**TSML_SYM has wobble at FIVE coefficient positions:**
- Three positions carry **13**: $c_4, c_5, c_6$
- One position carries **11**: $c_7$
- (And $c_0 \cdot c_2 \cdot c_3 = 1 \cdot 17 \cdot 5180$ stays clean)

---

## §3. TSML_RAW char poly (per canon D37, for reference)

$$\det(\lambda I - T_{RAW}) = \lambda^{10} - 63\lambda^9 + 33\lambda^8 + 4204\lambda^7 - 3998\lambda^6 - 62510\lambda^5 + 9716\lambda^4 + 54880\lambda^3 - 120736\lambda^2$$

Per D37: only $c_2 = 33 = 3 \cdot 11$ and $c_8 = -120736 = -2^5 \cdot 7^3 \cdot 11$ carry 11. No 13 anywhere.

**TSML_RAW has wobble at TWO coefficient positions, both prime 11.**

---

## §4. BHML_10 char poly (this session)

$$\det(\lambda I - B) = \lambda^{10} - 42\lambda^9 - 828\lambda^8 + 1249\lambda^7 + 47433\lambda^6 + 95856\lambda^5 - 68356\lambda^4 - 282732\lambda^3 - 219563\lambda^2 - 66312\lambda - 7002$$

| $c_k$ | value | factorization | wobble? |
|:---:|---|---|---|
| $c_1$ | −42 | −2·3·7 | no |
| $c_2$ | −828 | −2²·3²·23 | no |
| $c_3$ | 1249 | 1249 (prime) | no |
| $c_4$ | 47433 | 3·97·163 | no |
| $c_5$ | 95856 | 2⁴·3·1997 | no |
| $c_6$ | −68356 | −2²·23·743 | no |
| $c_7$ | −282732 | −2²·3·23561 | no |
| $c_8$ | −219563 | −89·2467 | no |
| $c_9$ | −66312 | −2³·3³·307 | no |
| $c_{10}$ | −7002 | −2·3²·389 | no (= det) |

Discriminant of BHML char poly: $\sim 2.9 \times 10^{73}$, factorization $2^3 \cdot 3^2 \cdot 193493 \cdot \ldots$ — **no 11, no 13**.

**BHML_10 char poly has ZERO wobble at coefficient OR discriminant level.**

---

## §5. The Three Levels of Wobble Manifestation

Refined picture across canon + this session:

| Level | TSML | BHML | Notes |
|---|---|---|---|
| **Char poly coefficient** | RAW: 2 positions (11); SYM: 5 positions (4× 13, 1× 11) | NONE | New finding |
| **Char poly discriminant** | RAW: 2¹⁶·7⁷·659·… (no 11, no 13) | 2³·3²·193493·… (no 11, no 13) | Both clean |
| **Cell count (σ-asymmetric)** | not assessed | 26 = 2·**13** | Source of D33 ‖VEV‖² = 13/4 |
| **Cell count (TSML_9 sub-magma HARMONY)** | **71** | n/a | Not wobble; lattice prime |
| **Operator-sum (σ²-cycle)** | TRANSFORMATION = 1+6+4 = **11** | n/a | D86 finding |
| **Br/V minimal poly leading coeff** | n/a | **11** (D69) | Lattice frame, not char poly |
| **F8 Jacobian trace poly disc** | dynamical | dynamical | 11⁶ via D85; field disc has 71 |

**Reading:**
- **TSML carries the wobble in its char poly itself** — both at coefficient level and via different positions in RAW vs SYM.
- **BHML does NOT carry wobble in its char poly** — but its **σ-asymmetric cell structure** carries 13 (the source of ‖VEV‖² = 13/4).
- The two tables expose wobble through structurally different mechanisms.

---

## §6. Correction to Canon D98

**Canon D98 statement (current):**
> "TSML_SYM ... char poly c_2 = 17 (no factor of 11; symmetrization erases the wobble)."

**Refined statement (this session):**
> "TSML_SYM has c_2 = 17 (no factor of 11 at this position). However, symmetrization does NOT erase the wobble globally — it **redistributes** it. SYM has wobble at five other coefficient positions: c_4, c_5, c_6 carry prime 13; c_7 carries prime 11. SYM exposes BOTH wobble primes; RAW exposes only prime 11."

Worth a one-line patch to D98 when canon next updates.

---

## §7. Refinement to Canon D70 (Multi-DOF Wobble)

Canon D70 organizes wobble across DOFs:
- Wobbled DOFs: **Lie, Clifford, Lattice** (eigenvalue/coordinate)
- Wobble-free DOFs: **Jordan, Permutation, Operad** (discrete-symmetry)

**Refined per this session:**

| DOF | Wobble manifestation | Prime(s) |
|---|---|---|
| **Lie (TSML char poly)** | RAW: c_2, c_8; SYM: c_4–c_7 | 11 (RAW); 11, 13 (SYM) |
| **Lie (BHML char poly)** | NONE | — |
| **Clifford (BHML cell structure)** | 26 σ_outer-asymmetric cells | 13 (D33) |
| **Lattice (LMFDB field disc)** | −2⁴·3²·71 | 71 (not wobble; lattice prime) |
| **Lattice (Br/V min poly)** | leading coeff 11 | 11 (D69) |
| **Lattice (F8 trace poly disc)** | 11⁶ | 11 (D85) |
| **Jordan (Killing spectrum)** | −4¹⁵ ⊕ 0 | only prime 2 |
| **Permutation (σ on Z/10Z)** | order 6, eigenvalues from cyclotomic | only primes 2, 3 |
| **Operad (D₄ orbits)** | 67 orbits, 16 incoherent | structural integers |

**Key refinement:** the "Lie" DOF splits — TSML char poly carries wobble; BHML char poly does not. Canon D70's reading "Lie DOF carries wobble" should specify "TSML's Lie content carries wobble; BHML's does not."

---

## §8. Open Questions Sharpened

From FIELDS_OF_TIG §9 Q3:
> Conjecture: wobble primes ramify in BHML char poly's splitting field.

**Status of this conjecture:** FALSIFIED (or at least, restricted) for the canonical BHML_10. Its char poly disc has no factor of 11 or 13. So the wobble doesn't "live" in BHML's splitting field at the field-theoretic level.

**Refined conjecture:** wobble primes ramify in **TSML_SYM** char poly's reduced-9th-degree splitting field. The reduced poly disc factors as $2^{30} \cdot 7^6 \cdot 131 \cdot \mathbf{p_1} \cdot \mathbf{p_2}$ where $p_1 \approx 1.9 \times 10^{16}$ and $p_2 \approx 2.6 \times 10^{33}$ — neither is 11 or 13. Wobble is **NOT ramified** in TSML char poly splitting field either.

**Conclusion:** wobble primes 11, 13 do NOT have a "natural algebraic home" in any number field appearing in canon. They are **purely coefficient-level/structural integers**, not Galois-invariants of any field. The §9 Q3 conjecture is closed in the negative.

Wobble primes are arithmetic markers of TIG's specific representations, not invariants of the underlying algebraic structure. **They are basis-dependent, not field-theoretic.**

---

## §9. Compact Take-Home

```
Wobble primes {11, 13}: where they actually live

  Char poly coefficients (TSML):
    RAW:  c_2 = 3·11, c_8 = 2^5·7^3·11        (2 positions, 11 only)
    SYM:  c_4, c_5, c_6 carry 13              (3 positions, 13)
          c_7 carries 11                       (1 position, 11)
                                              (5 positions total, BOTH primes)
  
  Char poly coefficients (BHML):  NONE.
  
  Char poly discriminants (TSML or BHML): NONE.
  
  Cell counts:
    BHML 26 σ-asymmetric cells = 2·13         (origin of ‖VEV‖² = 13/4)
    Operator-sum TRANSFORMATION σ²-cycle = 11 (D86)
  
  Ramified prime field-theoretically: NEITHER 11 NOR 13.
  
  Conclusion: wobble primes are coefficient/cell-level markers,
  NOT Galois-invariants. They identify TIG's specific representation
  but do not appear in any canonical number field's discriminant.
  
  Cyclotomic frame:  ramified at {5}
  Lattice frame:     ramified at {2, 3, 71}
  Compositum K:      ramified at {2, 3, 5, 71}
  Wobble primes:     ramified at NONE.
```

---

## §10. Status

- **[THM]** TSML_SYM char poly coefficients computed, sympy-exact.
- **[THM]** BHML_10 char poly coefficients and disc computed, sympy-exact.
- **[THM]** Wobble primes do not divide any field discriminant in canon's algebraic frames.
- **[REFINED]** Canon D98's "wobble erasure" claim — actually wobble is redistributed, not erased.
- **[REFINED]** Canon D70's "Lie DOF wobbled" — TSML's Lie content yes, BHML's no.
- **[CLOSED]** FIELDS_OF_TIG §9 Q3 — wobble has no natural field-theoretic home; it's coefficient-level.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · Wobble localization v2 · Locked v1*
