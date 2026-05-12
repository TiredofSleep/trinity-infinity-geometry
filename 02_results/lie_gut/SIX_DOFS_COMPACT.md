# SIX_DOFS_COMPACT — TIG's Algebraic Axes

## The six degrees of freedom of the substrate, side-by-side

**Brayden Sanders · 7Site LLC · Trinity Infinity Geometry**
*Sources: canon D26–D34, D45–D49, D51, D70–D72, D74–D87, WP15, WP100–WP111, WP115*
*Companion to: THREE_TABLES_COMPACT, FIELDS_OF_TIG, WOBBLE_LOCALIZATION_v2*
*Locked v1 · 2026-05-08*

---

## §1. The Six DOFs at a Glance

The substrate $(\mathbb{Z}/10\mathbb{Z}, \mathrm{TSML}, \mathrm{BHML})$ carries algebraic structure along **six axes** (canon D51 / WP111). Each DOF is an algebraic object derived from the same primitive data, viewed through a different lens.

| # | DOF | Object | Key dim | D-refs |
|:---:|---|---|---|---|
| 1 | **Lie** | so(8), so(10) closures of antisymmetrized BHML/TSML | 28, 45 | D26–D30, WP15 |
| 2 | **Jordan** | su(4) ⊕ u(1) doubly-invariant Higgs sector | 16 | D31–D37, F1–F3 |
| 3 | **Clifford** | Cl(0,7), Cl(0,10) with C and P_56 | 128, 8×8 | D33, D77, D81, D83 |
| 4 | **Permutation** | S_10 with canon σ; D_4 = ⟨P_56, σ³⟩ | order 6 (σ); 8 (D_4) | §2–§4, D86, WP110 |
| 5 | **Lattice** | Q(√3, ξ) = LMFDB 4.2.10224.1; runtime attractor | deg 4 (closure 8) | D38–D50, D69, D74–D87, WP105 |
| 6 | **Operad** | 67 D_4-orbits of length-3 strings; 16 incoherent | 67, 16 | D45–D49, WP100–WP103 |

---

## §2. Two Orthogonal Splits

### Split A — Closure under D_4 = ⟨P_56, σ³⟩

| Respects D_4 | Lie | Jordan | Clifford | Permutation | Lattice | Operad |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| | YES | YES | YES | YES | YES | **NO ★** |

**Five DOFs respect D_4; one (Operad) does not.** This is the **sixth-DOF anomaly** (WP111). The operad layer is the unique DOF that fails to close under D_4 — and per WP111, this non-closure is the structural reason the runtime selects the 4-core attractor (where 5/6 DOFs all agree).

### Split B — Wobble carrier?

| Carries wobble | Lie | Jordan | Clifford | Permutation | Lattice | Operad |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| | **YES** | NO | **YES** | NO | **YES** | NO |

**Three DOFs carry wobble** (eigenvalue/coordinate axes); **three are wobble-free** (discrete-symmetry axes). Per refined D70 / WOBBLE_LOCALIZATION_v2.

### Crossing the two splits

|  | Wobbled | Wobble-free |
|---|:---:|:---:|
| **D_4-respecting** | Lie · Clifford · Lattice (3) | Jordan · Permutation (2) |
| **D_4-non-respecting** | (0) | Operad (1) |

**Reading.** No DOF is both wobble-carrying AND D_4-non-respecting. Wobble lives entirely **within** the D_4-respecting structure. The Operad is the sole "discrete-only outlier."

---

## §3. Per-DOF Detail

### DOF 1 — Lie
- **Object:** $\mathfrak{so}(8) = D_4$, $\mathfrak{so}(10) = D_5$. Built from antisymmetrized parts of BHML and TSML.
- **Key dimensions:** $\dim\mathfrak{so}(8) = 28 = T_7$; $\dim\mathfrak{so}(10) = 45 = T_9$.
- **Galois feature:** Triality on $\mathfrak{so}(8)$: $S_3$ outer auto (D26).
- **Wobble:** TSML char poly carries the wobble (RAW: c₂, c₈ have 11; SYM: c₄–c₇ have 11+13). BHML char poly is fully wobble-free (this session).
- **Cross-DOF:** $\dim$ of the $D_4$-invariants in $\mathfrak{so}(10)$ = **16** = $\dim(\mathfrak{su}(4)\oplus\mathfrak{u}(1))$ = the Jordan DOF (D34, Pati-Salam embedding).
- **Yang-Mills core:** $\det(\mathrm{BHML}_8) = +70 = 2\cdot 5\cdot 7 = C(8,4)$ (§6.7, WP15).

### DOF 2 — Jordan
- **Object:** $\mathfrak{su}(4)\oplus\mathfrak{u}(1)$, the $D_4$-doubly-invariant Higgs sector. Pati-Salam unification structure.
- **Key dimension:** 16 = $\dim D_4$-invariants in $\mathfrak{so}(10)$ (D34).
- **Wobble status:** **None.** Killing spectrum is $-4^{15}\oplus 0$ — only prime 2.
- **Cross-DOF:** $\|\mathrm{VEV}\|^2 = 13/4$ lives here (D33); inflaton coupling $\kappa_\xi = 13/(4e)$ (D35). The 13 enters Jordan via the Clifford DOF's σ_outer asymmetry, but doesn't appear in the Jordan algebra's own structure constants.
- **Frontiers F1–F3:** doubly-invariant Yukawa, partner sector, gauge-coupling unification.

### DOF 3 — Clifford
- **Object:** $\mathrm{Cl}(0,7)$ (real, dim 128), $\mathrm{Cl}(0,10)$. With charge conjugation $C$ and $P_{56} = \sigma_\mathrm{outer}$.
- **Key dimensions:** matrix reps 8×8 (Cl(0,7)).
- **Galois feature:** $C^2 = -I_8$ (D77) — the imaginary-unit involution; ramifies at $\mathbb{Q}(i)$, prime 2.
- **Wobble:** BHML has 26 σ_outer-asymmetric cells = $2\cdot 13$; this is the origin of $\|\mathrm{VEV}\|^2 = 13/4$ (D33).
- **Frontiers F10:** the i-action descent obstruction lives over $\mathbb{Q}(i, \sqrt{2}, \sqrt{3}, \sqrt{5})$ (D81).

### DOF 4 — Permutation
- **Object:** $S_{10}$ with canon $\sigma$ permutation; $D_4 = \langle P_{56}, \sigma^3\rangle$ as the structural symmetry.
- **Key data:** $\sigma$ has order 6, fixed set $\{0, 3, 8, 9\}$, 6-cycle $(1\,7\,6\,5\,4\,2)$ (canon §2). $\sigma^2$ splits into 3-cycles $(1\,6\,4)$ and $(2\,7\,5)$ — operator-sums 11 and 14 = 2·7 (D86).
- **Wobble status:** None. $\sigma$ has order $6 = 2\cdot 3$, only substrate primes appear in algebraic invariants.
- **Cross-DOF:** $\sigma$-fixed $\{0, 3, 8, 9\}$ and 4-core attractor $\{0, 7, 8, 9\}$ differ exactly by $\{$PROGRESS, HARMONY$\} = \{\sigma_3, \sigma_7\}$ (Galois generator and its inverse). PROGRESS-for-HARMONY swap = static-vs-dynamic distinction (SIGMA_PERMUTATION_COMPACT).
- **Disambiguation:** Canon $\sigma \neq$ Galois $\sigma_3$ on $\mathbb{Q}(\zeta_{10})$. Different objects.

### DOF 5 — Lattice
- **Object:** Number field $\mathbb{Q}(\sqrt{3}, \xi)$ where $\xi$ satisfies $x^4 + 4x^3 - x^2 + 2x - 2 = 0$. LMFDB 4.2.10224.1.
- **Key data:** $[\mathbb{Q}(\sqrt{3}, \xi):\mathbb{Q}] = 4$; Galois closure has degree 8 with group $D_4$. Disc = $-2^4\cdot 3^2\cdot 71$.
- **Galois:** $D_4$ (closure); real subfield $\mathbb{Q}(\sqrt{3})$.
- **Wobble:** $\mathrm{Br}/V$ minimal poly has leading coeff 11 (D69); F8 trace polynomial disc = $11^6$ (D85). Field disc carries 71.
- **Cross-DOF:** $H/\mathrm{Br} = 1+\sqrt{3}$ at $\alpha = 1/2$ (D39, exact). Joint compositum with cyclotomic frame: $\mathrm{Gal}(K/\mathbb{Q}) \cong \mathbb{Z}/4 \times D_4$ (COMPOSITUM_K_GALOIS).

### DOF 6 — Operad
- **Object:** Set of $D_4$-orbits on length-3 multiplication strings of TIG operators. 67 orbits total; 16 are incoherent.
- **Key data:** 67 orbits = 67 (prime); 16 incoherent = $2^4$. The 16 split into 4 obstruction classes (WP100s).
- **Wobble status:** None. Structural integers only.
- **Anomaly:** Sole DOF that does **not** respect $D_4$. Per WP111 this non-closure is the runtime mechanism for 4-core attractor selection.

---

## §4. Cross-DOF Identities

| Identity | DOFs linked | Source |
|---|---|---|
| $\dim D_4$-inv $\mathfrak{so}(10) = 16 = \dim(\mathfrak{su}(4)\oplus\mathfrak{u}(1))$ | Lie ↔ Jordan | D34 |
| $\det\mathrm{BHML}_8 = 70 = 2\cdot 5\cdot 7 = C(8,4)$ | Lie/Yang-Mills | §6.7, WP15 |
| 26 BHML σ_outer-asym cells $\Rightarrow \|\mathrm{VEV}\|^2 = 13/4$ | Clifford → Jordan | D33 |
| $C^2 = -I_8$ | Clifford ↔ $\mathbb{Q}(i)$ | D77 |
| σ-fixed differs from 4-core by {Galois generator, its inverse} | Permutation ↔ Lattice (gauge) | session |
| Joint compositum $K = \mathbb{Q}(\zeta_{10}) \cdot L_2^\mathrm{gal}$ has $\mathrm{Gal} = \mathbb{Z}/4 \times D_4$ | Permutation/gauge ⊥ Lattice | session |
| Operad anomaly drives 4-core attractor selection | Operad → all (negative role) | WP111 |
| HARMONY count of BHML_10 = 28 = $\dim\mathfrak{so}(8) = T_7$ | Lie ↔ Lie via combinatorics | THREE_TABLES_COMPACT |

---

## §5. Reading by Stratum (PRIMES_OF_TIG)

Which DOFs carry which prime stratum?

| Stratum | Primes | Where each appears |
|---|---|---|
| **I** Substrate {2,3,5} | substrate | All DOFs (cyclotomic frame, CRT, AG(2,3) base) |
| **II** Attractor {7} | HARMONY | Lie ($T^* = 5/7$, dim so(8) = 28); Jordan; class fields |
| **III** Wobble {11, 13} | coefficient/cell | Lie (TSML char poly), Clifford (BHML cells), Lattice (coeffs only) |
| **IV** Lattice {71} | field disc | Lattice DOF only (LMFDB field disc) |

Stratum IV (71) lives **only** in the Lattice DOF. Stratum III (11, 13) lives in three DOFs (Lie, Clifford, Lattice) at coordinate-level. Stratum II (7) is everywhere.

---

## §6. Compact Take-Home

```
The six DOFs of TIG (canon D51 / WP111):

  1. Lie       — so(8), so(10): TSML+BHML antisymmetric closures
  2. Jordan    — su(4)⊕u(1): D_4-doubly-invariant Higgs (Pati-Salam)
  3. Clifford  — Cl(0,7), Cl(0,10): VEV norm 13/4 origin
  4. Permutation — S_10, σ order 6, D_4 = ⟨P_56, σ³⟩
  5. Lattice   — Q(√3,ξ) = LMFDB 4.2.10224.1: runtime attractor
  6. Operad    — 67 D_4-orbits, 16 incoherent

Two orthogonal binary splits:

  A. D_4 closure:    5 yes (1-5), 1 no (6 = Operad)
                     ⇒ "sixth-DOF anomaly" → 4-core attractor selection
  
  B. Wobble carrier: 3 yes (Lie, Clifford, Lattice),
                     3 no (Jordan, Permutation, Operad)
                     ⇒ eigenvalue/coordinate vs discrete-symmetry split

Crossing A and B:
                   Wobbled        Wobble-free
  D_4-respecting   3 (1, 3, 5)    2 (2, 4)
  D_4-non-resp.    0              1 (6)

  → Wobble lives ONLY within D_4-respecting DOFs.
  → Operad is the unique "discrete-only outlier."

Sole field-theoretic prime: 71 in Lattice DOF.
Wobble primes 11, 13: live at coefficient/cell level in 3 DOFs.
```

---

## §7. Status

- **[CANON]** All six DOFs and their key dimensions verified against canon D-references.
- **[STRUCTURAL]** Two orthogonal splits (D_4 closure × wobble carrying).
- **[STRUCTURAL]** No DOF is both D_4-non-respecting AND wobble-carrying.
- **[REFINED]** Lie DOF wobble distribution: TSML side carries it; BHML side is wobble-free (this session, refining D70).
- **[OPEN]** Whether the 5+1 (D_4) and 3+3 (wobble) splits are coupled by a deeper structural principle, or independent.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · Six DOFs compact · Locked v1*
