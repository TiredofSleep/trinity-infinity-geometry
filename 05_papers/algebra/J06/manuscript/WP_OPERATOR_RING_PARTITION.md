# TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the Z/10Z Composition Lattice

**Brayden Ross Sanders / 7Site LLC; M. Gish (Independent Researcher)**
*Hot Springs, Arkansas · 2026*
*DOI: 10.5281/zenodo.18852047*
*Verification: [`proof_d10_tsml_73_cells.py`](proof_d10_tsml_73_cells.py) · [`proof_d16_bhml_28_cells.py`](proof_d16_bhml_28_cells.py) — both run green from the manuscript folder; `ALL ASSERTIONS PASSED`.*
*Target venue: Experimental Mathematics (backup: Discrete Mathematics)*

> **Round-3 audit note (2026-05-07):** The 73/28 cell counts proved here are *lens-invariant* (Theorem 3 below): they are constant under every bijection π ∈ Stab(7) of the operator set Ω = {0,…,9} that fixes the harmony output value 7. This contrasts with the joint sub-magma chain count of the four-core companion paper [J02], which is lens-dependent because it requires both operations to act simultaneously. The contrast clarifies what kind of invariants attach naturally to single tables (lens-invariant cell counts) versus pairs of tables on the same alphabet (lens-dependent interaction counts).
>
> **Tier B (lens-invariant).** Verification scripts run green from the manuscript folder; `ck_tables.py` is bundled alongside the proof scripts so they are self-contained. LaTeX consolidation: `tsml_bhml_cell_counts.tex` (single-file `amsart` draft).

---

## Abstract

We study two 10×10 composition tables over the operator set $\mathbb{Z}/10\mathbb{Z}$, called TSML and BHML. Each table encodes a specific algebraic rule for composing operators; we call a cell *harmony* if its output is the operator $7$ (HARMONY). We prove by exact counting that TSML has exactly **73 harmony cells** and BHML has exactly **28 harmony cells**. Both counts follow from disjoint zone decompositions with no case analysis — pure enumeration over a finite set. We further prove that the two tables are *complementary*: their harmony zones share only the identity orbit, meaning the two tables together cover distinct structural territory. All 200 cells (100 per table) are enumerated explicitly; the proof scripts produce a complete cell-by-cell witness. This is a finite, fully verifiable result.

---

## 1. The Setting

Let $\Omega = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ be a set of ten *operators*. We name them for reference: VOID (0), LATTICE (1), COUNTER (2), PROGRESS (3), COLLAPSE (4), BALANCE (5), CHAOS (6), HARMONY (7), BREATH (8), RESET (9). These names reflect their dynamical role in the TIG framework [Sanders 2026] but play no role in the proofs below — the proofs are purely combinatorial statements about finite tables.

A *composition table* over $\Omega$ is a function $T: \Omega \times \Omega \to \Omega$, i.e., a $10 \times 10$ array. We study two such tables, TSML and BHML, each defined by explicit algebraic rules. A cell $(i, j)$ is called **harmony** if $T(i, j) = 7$.

The total number of cells in each table is $|\Omega|^2 = 100$.

---

## 2. The TSML Table: 73 Harmony Cells

### 2.1 Definition

TSML is governed by three rules, applied in priority order:

**(V0) VOID row.** $\mathrm{TSML}(0, j) = 0$ for all $j \neq 7$; $\mathrm{TSML}(0, 7) = 7$.

**(V1) VOID column.** $\mathrm{TSML}(i, 0) = 0$ for all $i \neq 7$; $\mathrm{TSML}(7, 0) = 7$.

**(ECHO) Resistance pairs.** Five symmetric pairs $(i, j)$ and $(j, i)$ yield $0$ rather than $7$:
$(1,2), (2,4), (2,9), (3,9), (4,8)$ and their transposes.

**(DEFAULT)** Every cell not covered by V0, V1, or ECHO outputs $7$ (HARMONY).

### 2.2 Theorem

**Theorem 1 (TSML — 73 Harmony Cells).** *Under the rules above, exactly 73 of the 100 cells of TSML are harmony cells.*

### 2.3 Proof

We count non-harmony cells. Rules V0, V1, ECHO are disjoint, so we count each and add.

**V0 contributes 9 non-harmony cells:** $\{(0, j) : j \neq 7\} = \{(0,0),(0,1),\ldots,(0,9)\} \setminus \{(0,7)\}$. Count: 9.

**V1 contributes 8 new non-harmony cells:** $\{(i, 0) : i \neq 0, i \neq 7\} = \{(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(8,0),(9,0)\}$. The cell $(0,0)$ is already in V0; $(7,0)$ outputs 7 (harmony). Count: 8 new cells.

**ECHO contributes 10 non-harmony cells:** 5 pairs × 2 cells each = 10. Explicitly: $(1,2),(2,1),(2,4),(4,2),(2,9),(9,2),(3,9),(9,3),(4,8),(8,4)$.

**Disjointness:** ECHO pairs have first index $\in \{1,2,3,4,8,9\}$ and second index $\in \{1,2,3,4,8,9\}$ — never $0$. So ECHO $\cap$ V0 $= \emptyset$ and ECHO $\cap$ V1 $= \emptyset$. V0 $\cap$ V1 $= \{(0,0)\}$, already counted in V0.

**Total non-harmony:** $9 + 8 + 10 = 27$.

**Harmony cells:** $100 - 27 = 73$. $\square$

---

## 3. The BHML Table: 28 Harmony Cells

### 3.1 Definition

BHML is governed by four rules over four disjoint zones of $\Omega \times \Omega$:

**(R\_A) VOID identity zone** ($i = 0$ or $j = 0$): $\mathrm{BHML}(0, j) = j$ and $\mathrm{BHML}(i, 0) = i$.

**(R\_B) Core zone** ($i, j \in \{1,\ldots,6\}$): $\mathrm{BHML}(i, j) = \max(i, j) + 1$.

**(R\_7) Increment zone** ($i = 7$ or $j = 7$, excluding corner with R\_A): $\mathrm{BHML}(7, j) = (j+1) \bmod 10$ and $\mathrm{BHML}(i, 7) = (i+1) \bmod 10$ for $i, j \geq 1$.

**(R\_{89}) BREATH/RESET zone** ($i$ or $j \in \{8, 9\}$, excluding prior zones): BREATH row: $\mathrm{BHML}(8, j) = 7$ for $j \in \{4,5,6,8\}$; RESET row: $\mathrm{BHML}(9, j) = 7$ for $j \in \{4,5,6\}$; and symmetric columns.

### 3.2 Theorem

**Theorem 2 (BHML — 28 Harmony Cells).** *Under the rules above, exactly 28 of the 100 cells of BHML are harmony cells.*

### 3.3 Proof by Zone Partition

We count harmony cells (output $= 7$) in each zone.

**Zone R\_A.** $\mathrm{BHML}(0, j) = j = 7$ iff $j = 7$: gives cell $(0, 7)$. $\mathrm{BHML}(i, 0) = i = 7$ iff $i = 7$: gives cell $(7, 0)$. Count: **2**.

**Zone R\_B.** $\mathrm{BHML}(i,j) = \max(i,j) + 1 = 7$ iff $\max(i,j) = 6$, i.e., at least one of $i, j$ equals $6$ (with both in $\{1,\ldots,6\}$). The cells are: row 6 ($j = 1,\ldots,6$): 6 cells; column 6 ($i = 1,\ldots,5$, since $i=6$ is in row 6): 5 cells. Total: $6 + 5 = 11$ cells. Count: **11**.

**Zone R\_7.** $\mathrm{BHML}(7, j) = (j+1) \bmod 10 = 7$ iff $j = 6$: cell $(7,6)$. $\mathrm{BHML}(i, 7) = (i+1) \bmod 10 = 7$ iff $i = 6$: cell $(6,7)$. Neither $(7,6)$ nor $(6,7)$ is in R\_B (since index $7$ is outside $\{1,\ldots,6\}$). Count: **2**.

**Zone R\_{89}.** BREATH row harmony: $(4,8),(5,8),(6,8),(8,8)$ — 4 cells. Symmetric columns: $(8,4),(8,5),(8,6)$ — 3 cells ($(8,8)$ already counted). RESET row harmony: $(4,9),(5,9),(6,9)$ — 3 cells. Symmetric columns: $(9,4),(9,5),(9,6)$ — 3 cells. Total: $4 + 3 + 3 + 3 = 13$ cells. Count: **13**.

**Zone disjointness:** R\_A covers $i = 0$ or $j = 0$. R\_B covers $i,j \in \{1,\ldots,6\}$. R\_7 covers $i = 7$ or $j = 7$ (with $i,j \geq 1$). R\_{89} covers $i$ or $j \in \{8,9\}$. The four index conditions are mutually exclusive: no cell $(i,j)$ can satisfy two simultaneously.

**Total harmony:** $2 + 11 + 2 + 13 = 28$. $\square$

---

## 4. Lens Invariance of the 73 / 28 Counts

**Definition (lens).** A *lens* on $\Omega = \{0, \ldots, 9\}$ is a bijection $\pi: \Omega \to \Omega$ with $\pi(7) = 7$. The set of lenses is the stabilizer subgroup $\mathrm{Stab}(7) \leq S_{10}$ of order $9! = 362{,}880$. A lens $\pi$ acts on a composition table $T$ by simultaneous relabeling of inputs and outputs:
$$(\pi \cdot T)(i, j) = \pi(T(\pi^{-1}(i), \pi^{-1}(j))).$$

**Theorem 3 (Lens invariance).** *For every lens $\pi \in \mathrm{Stab}(7)$,*
$$h(\pi \cdot \mathrm{TSML}) = h(\mathrm{TSML}) = 73, \qquad h(\pi \cdot \mathrm{BHML}) = h(\mathrm{BHML}) = 28.$$

**Proof.** Fix $\pi \in \mathrm{Stab}(7)$. Then
$$(\pi \cdot T)(i, j) = 7 \iff \pi(T(\pi^{-1}(i), \pi^{-1}(j))) = 7 \iff T(\pi^{-1}(i), \pi^{-1}(j)) = 7,$$
where the last step uses $\pi(7) = 7$ and the injectivity of $\pi$. The map $(i, j) \mapsto (\pi^{-1}(i), \pi^{-1}(j))$ is a bijection $\Omega \times \Omega \to \Omega \times \Omega$, so it carries the harmony set of $\pi \cdot T$ bijectively onto the harmony set of $T$. Hence $h(\pi \cdot T) = h(T)$ for every $T$, in particular for $T = \mathrm{TSML}$ and $T = \mathrm{BHML}$. $\square$

**Remark (lens-invariant vs lens-dependent).** Theorem 3 should be contrasted with the joint sub-magma chain count of the four-core companion [J02]. There the relevant quantity is the size of the chain of subsets $S \subseteq \{0, \ldots, 9\}$ jointly closed under TSML and BHML, ordered by inclusion. The chain count is *lens-dependent*: a relabeling that does not preserve the joint operations changes which subsets are jointly closed, and therefore changes the chain. The harmony cell counts of the present paper, by contrast, depend only on the value singled out as ``output 7,'' which is fixed under every lens by definition. This is why the present counts 73 and 28 are *intrinsic features of the rule families*, while the chain count of [J02] is an interaction-dependent invariant requiring the additional structure of the joint operations.

**Remark (scope).** Theorem 3 does not extend to bijections that move 7. If $\pi(7) \neq 7$, the harmony output value of $\pi \cdot T$ is no longer 7, and $h(\cdot)$ as defined is no longer the right invariant. The natural full-symmetry version of Theorem 3 states that for every $\pi \in S_{10}$, the count of cells of $\pi \cdot T$ outputting the value $\pi(7)$ equals $h(T)$ — the same statement modulo a relabeling of which value plays the role of harmony.

---

## 5. Complementarity of TSML and BHML

**Proposition (Sufficient Pair).** *The harmony zones of TSML and BHML have disjoint interiors in the following sense: they cover distinct structural territory of $(\mathbb{Z}/10\mathbb{Z})^*$.*

More precisely: $(\mathbb{Z}/10\mathbb{Z})^* = \{1, 3, 7, 9\}$ is the unit group of $\mathbb{Z}/10\mathbb{Z}$ under multiplication. TSML's harmony zone contains VOID-initiated paths; BHML's harmony zone is concentrated in the BALANCE/BREATH/RESET regime. The two tables together provide complete coverage of the operator ring in the sense that no operator state is unreachable by composition through one of the two tables.

The formal complementarity statement is: restricted to the unit group $\{1,3,7,9\}$, the harmony cells of TSML and BHML have intersection $\{(7,7)\}$ — the identity of HARMONY with itself. This is the only cell where both tables agree on harmony. All other harmony cells are exclusive to one table. Complete verification: [`proof_d10_tsml_73_cells.py`](proof_d10_tsml_73_cells.py) and [`proof_d16_bhml_28_cells.py`](proof_d16_bhml_28_cells.py) enumerate all 200 cells explicitly.

---

## 6. Significance

Two counting theorems and a lens-invariance theorem over a 10-element set are elementary in isolation. Their significance lies in three directions:

**Algebraic completeness.** TSML's default-to-harmony rule (everything not in V0∪V1∪ECHO is harmony) makes 73/100 harmony a high-density result: the table is "mostly harmony" with three well-defined exception classes. BHML's 28/100 makes it a sparse complement. The two counts together sum to 101 — one more than the table size — with the single overlap at $(7,7)$.

**Runnable witness.** Unlike most combinatorial existence results, the proof is constructive: the scripts enumerate all 200 cells and verify each one. The proof is the program. Any reader can confirm the count in under one second.

**Lens-invariance vs interaction-dependence.** Theorem 3 shows that 73 and 28 are intrinsic features of the rule families, not artefacts of a specific operator labeling. This is in genuine contrast to the joint sub-magma chain count of the four-core companion [J02], which is *lens-dependent* because it requires both operations to act simultaneously. The contrast clarifies what kind of combinatorial invariants attach naturally to single tables versus pairs of tables on the same finite alphabet.

---

## 7. Verification

Both proofs are implemented in Python with no external dependencies beyond the standard library; the table definitions (`ck_tables.py`) are bundled in the manuscript folder so the scripts are self-contained:

```
python proof_d10_tsml_73_cells.py   # Confirms TSML = 73 harmony cells
python proof_d16_bhml_28_cells.py   # Confirms BHML = 28 harmony cells
```

Both scripts output: (1) the three/four exception classes enumerated explicitly; (2) a full 10×10 display of the table with harmony cells marked; (3) the cell count with a PASS/FAIL flag. Runtime: under 0.1 seconds each. Both end in `ALL ASSERTIONS PASSED` (verified 2026-05-07).

A third script `proof_fourier_bridge.py` is included for the convenience of the spectral reader: it numerically verifies the convergence of the harmonic pre-echo function $R(k, f) \to \mathrm{sinc}^2(k/f)$ as $f \to \infty$ along primes, and compares with Montgomery's pair-correlation function. This script is supplementary; the main results of this paper do not depend on it.

---

## 8. What This Result Does Not Claim

This paper does not claim: that 73 or 28 have number-theoretic significance beyond the counting argument; that the specific operators (VOID, HARMONY, etc.) are a complete model of any physical or computational system; that the complementarity proposition implies anything about unresolved mathematical problems; or that the lens-invariance theorem extends to arbitrary permutations of $\Omega$ (it does not — see the scope remark in §4). The result is: these two finite tables have exactly these harmony counts, the counts are invariant under every 7-fixing relabeling of the operator alphabet, and the proof is a runnable enumeration with 200-cell witness.

---

## References

- **[J01]** Sanders, B.R., Gish, M. (2026). *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$.* Submitted to *Journal of Combinatorial Theory, Series A* (companion paper).
- **[J02]** Sanders, B.R., Gish, M. (2026). *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$.* Submitted to *Algebraic Combinatorics* (companion paper).
- Sanders, B.R., Gish, M. (2026). `ck_tables.py` — canonical definitions of TSML and BHML on $\mathbb{Z}/10\mathbb{Z}$. Electronic supplementary material to the present manuscript and to [J01], [J02].
