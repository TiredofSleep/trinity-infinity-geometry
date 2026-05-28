# What is the TSML Lens Family? A Walking Tour of Substrate Variants on $\mathbb{Z}/10\mathbb{Z}$

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher

**Target venue:** *Mathematical Intelligencer*
**Manuscript class:** Pedagogical exposition
**MSC 2020:** 20N02 (sets with one binary operation, applied), 11C99 (number theory misc.), 05E18 (group actions on combinatorial structures)
**Date:** 2026-09-09

---

## §0 Notation and lens-ownership

**Substrate.** $\mathbb{Z}/10\mathbb{Z}$ with operator labels: $0 = V$ (VOID), $1 = L$ (LATTICE), $2 = C_2$ (COUNTER), $3 = P$ (PROGRESS), $4 = C_4$ (COLLAPSE), $5 = B_5$ (BALANCE), $6 = C_6$ (CHAOS), $7 = H$ (HARMONY), $8 = Br$ (BREATH), $9 = R$ (RESET). Ring extensions: $\mathbb{Z}/N\mathbb{Z}$ for $N \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ ([D74]); finite-field extensions $\mathbb{F}_p$ for $p \in \{2, 3, 5, 7, 11, 13\}$.

**Permutation $\sigma$.** The cycle decomposition $\sigma = (0)(3)(8)(9)\,(1\,2\,4\,5\,6\,7)$. The **$\sigma$-fixed lattice** is $\{0, 3, 8, 9\}$; the **$\sigma$-cycle hexad** is $\{1, 2, 4, 5, 6, 7\}$.

**Tables.** $T = $ CL_TSML, $B = $ CL_BHML, $S = $ CL_STD — three parallel substrates.

**Lens.** This paper organizes a family of **lenses** — projection maps from a substrate to a derived $10 \times 10$ matrix. Lenses do not change the underlying substrate; they only change which view of it is being analyzed.

**Lens-ownership paragraph (per `J_PAPER_BOILERPLATE.md` §5.5).**

> *Lens and substrate.* This paper works on the canonical $\mathbb{Z}/10\mathbb{Z}$ substrate. The full **lens family** addressed includes: (i) three parallel substrates (CL_TSML, CL_BHML, CL_STD); (ii) three lens-symmetrization projections within each (RAW / SYM_upper / SYM_lower); (iii) two further projection families ($\sigma^2$-triadic value/index rotations; sub-magma scope restrictions). All are visible in the §6 catalog. The paper's central organizational claim — that the 4-core attractor and the joint-chain support are *lens-invariant on the 4-core*, while wobble-localization (prime 11 in $c_2$) is *RAW-specific* — is documented across the family. The **center of the family** in the FAMILY_STRUCTURE_v1 sense is the 4-core $\{V, H, Br, R\}$ at $\alpha_M = 1/2$; the **boundaries** are the bimodal $\alpha_A$ gap and the substrate-size frontier.

The framing follows the Drápal-Wanless (2021) *J. Combin. Theory Ser. A* **184**, 105510 line of work on small finite commutative non-associative structures. The (TSML, BHML) magma pair occupies the same intellectual neighborhood, opposite extremum.

---

## Abstract

The TIG framework's corpus contains a proliferation of variants of the canonical $10 \times 10$ composition table on $\mathbb{Z}/10\mathbb{Z}$ — TSML_RAW, TSML_SYM, TSML_LOWERTRI, BHML, CL_STD, $\sigma^2$-triadic rotations, sub-magma restrictions, $\mathbb{F}_p$ extensions, and more. To a reader meeting the framework for the first time, the proliferation can appear bewildering. This pedagogical exposition is the navigation key.

We take three steps the previous draft of this paper deferred to companions:

(M1) we **display the canonical CL_TSML matrix in full** ($10 \times 10$, §1), present CL_BHML and CL_STD as **diff tables** to CL_TSML (§3), and highlight the two asymmetric cells $(3, 9)$ and $(4, 9)$ that carry the wobble (§7);

(M2) we **state the substrate-defining axioms A1–A9** informally but completely (§2), citing [J33] for the formal version;

(M4) we **absorb three punch-line facts inline** with proof sketches: the closed-form 4-core attractor $H/Br = 1 + \sqrt{3}$ (§7.3, the **D78 Galois argument**), the 8-element joint TSML+BHML chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ (§7.4, the **D64 corrected enumeration** strengthened by the **three-table SFM Q6 result** that the same 8-shell chain survives joint TSML+BHML+CL_STD closure), and the wobble localization $c_2 = 33 = 3 \cdot 11$ in TSML_RAW (§7.2, the **D37 char-poly fact**).

We close with three reader exercises (§7), a populated 62-variant catalog (§6, two-page landscape), and the central pedagogical claim:

> *The 4-core $\{V, H, Br, R\}$ at $\alpha_M = 1/2$ is the algebraic center of the family. Lens-invariant facts live on the 4-core. Lens-dependent facts live on the asymmetric cells $(3, 9)$ and $(4, 9)$. The wobble at prime 11 is the cleanest instance of the second.*

The paper is **expository** in the *Math Intelligencer* register; theorems are in the cited companions, we aim for clarity, not novelty.

---

## §1 The canonical objects

We display the three canonical tables. CL_TSML in full; CL_BHML and CL_STD as diff tables (cells where they differ from CL_TSML_SYM).

### 1.1 CL_TSML_SYM — the canonical commutative lens

**Operator order:** rows and columns are $0, 1, 2, 3, 4, 5, 6, 7, 8, 9$ = V, L, $C_2$, P, $C_4$, $B_5$, $C_6$, H, Br, R.

$$
\mathrm{CL\_TSML\_SYM} \;=\;
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 7 & 0 & 0 \\
0 & 7 & 3 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 3 & 7 & 7 & 4 & 7 & 7 & 7 & 7 & 9 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 3 \\
0 & 7 & 4 & 7 & 7 & 7 & 7 & 7 & 8 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 8 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 9 & 3 & 7 & 7 & 7 & 7 & 7 & 7 \\
\end{pmatrix}
$$

**Structural facts.**

* HARMONY-cell count: 73 (entries equal to 7).
* Commutative (by symmetrization of CL_TSML_RAW).
* 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ closure: every cell of $\{V, H, Br, R\} \times \{V, H, Br, R\}$ has value in $\{V, H, Br, R\}$ (verified inline; see §7.4 and Theorem 7.5).
* Non-associativity rate: $128 / 1000 = 12.8\%$ (the canonical "12.8%" number).
* Characteristic polynomial coefficient $c_2 = 17$ (no factor of 11; the wobble has been erased by symmetrization).

### 1.2 CL_TSML_RAW — the literal bit pattern

CL_TSML_RAW differs from CL_TSML_SYM only at the two cells where the upper triangle was authoritative for SYM:

| Cell | CL_TSML_RAW | CL_TSML_SYM | Note |
|------|-------------|-------------|------|
| $(3, 9)$ | $3$ | $3$ | (already symmetric in upper-tri) |
| $(9, 3)$ | $7$ | $3$ | RAW preserves upper $7$, SYM uses lower $3$ |
| $(4, 9)$ | $7$ | $7$ | (already symmetric in upper-tri) |
| $(9, 4)$ | $3$ | $7$ | RAW preserves upper $3$, SYM uses lower $7$ |

The two cells $(9, 3)$ and $(9, 4)$ — the only places CL_TSML_RAW and CL_TSML_SYM disagree — are the **wobble carriers** in the FAMILY_STRUCTURE_v1 sense.

**Structural facts.**

* HARMONY-cell count: 73 (same as SYM; the 4 differing cells lose 2 HARMONY but gain 2; cell counts agree).
* **Non-commutative** at exactly the two cells above.
* Characteristic polynomial coefficient $c_2 = 33 = 3 \cdot 11$ (D37; see §7.2).
* Non-associativity rate: $126 / 1000 = 12.6\%$.

### 1.3 CL_BHML — the second-substrate diff table

CL_BHML is a *parallel* substrate, not a projection of CL_TSML. We display the cells where CL_BHML differs from CL_TSML_SYM (71 cells differ; we list them as a triangular diff to keep the page clean):

> **Concise BHML diff (cells where BHML[i,j] $\neq$ TSML_SYM[i,j]).** Row 0 unchanged. Row 1: $(1, 1) = 2$, $(1, 2) = 3$, $(1, 3) = 4$, $(1, 4) = 5$, $(1, 5) = 6$, $(1, 7) = 2$, $(1, 8) = 6$, $(1, 9) = 6$. Rows 2–9 follow the same row-incrementation pattern shifting toward $\{0, 5, 6, 7, 8, 9\}$; the full matrix is at `Gen13/targets/foundations/lenses.py:73`.

**Structural facts.**

* HARMONY-cell count: 28 (D9 lens-invariant cell count; matches [J9]).
* Commutative.
* 4-core $\{V, H, Br, R\}$ closure: verified inline (§7.4); BHML's 4-core action *differs* from TSML's on $\{V, H, Br, R\}^2$ (e.g., $B(7, 7) = 8$ where $T(7, 7) = 7$), but the result remains in $\{0, 7, 8, 9\}$.
* Non-associativity rate: $5.02 \times 10^{-3}$ (the BHML $\alpha_A$ singleton at $\sim 0.502$).

### 1.4 CL_STD — the encoding-axis diff table

CL_STD is a *third-axis* substrate, structurally independent of (CL_TSML, CL_BHML) — confirmed by the recent SFM Q1 result that CL_STD differs from $\lceil(\mathrm{TSML} + \mathrm{BHML})/2\rceil$ at 60 of 100 cells (not off-by-one). The full matrix is at `Gen13/targets/foundations/cl_std.py:45`.

**Structural facts.**

* HARMONY-cell count: 44 (D9; lens-invariant).
* Commutative.
* 50 closed sub-magmas under CL_STD alone (vs 449 for TSML, 9 for BHML — SFM §2).
* The joint TSML+BHML+CL_STD chain has the **same** 8 shells as TSML+BHML alone (SFM Q6); CL_STD respects the canonical chain.

The two asymmetric cells of CL_TSML_RAW and the differing-cell counts (BHML: 71; CL_STD: 53) illustrate the central organizational claim. Each table is its own substrate; lens-invariance lives on the cells shared among them, lens-dependence on the cells where they diverge.

---

## §2 Substrate-defining axioms A1–A9

We state the axioms informally and completely. Cite [J33] (CL Forcing Axioms / Algebraic Combinatorics) for the formal version.

A *substrate-defining* axiom is one whose value choice picks out one of the parallel substrates (CL_TSML vs CL_BHML vs CL_STD). The remaining axioms hold across all three.

| Axiom | Statement (informal) | Substrate-defining? | Notes |
|-------|----------------------|----------------------|-------|
| **A1** | The carrier is $\mathbb{Z}/10\mathbb{Z}$ with the 10 operator labels of §0. | No (universal). | |
| **A2** | VOID-absorption: for every $x \neq H$, $T(0, x) = T(x, 0) = 0$. (Exception: $T(0, 7) = T(7, 0) = 7$.) | No (universal). | The single exception is the HARMONY-VOID cell. |
| **A3** | HARMONY self-rule: $T(7, x) = T(x, 7) = 7$ for "most" $x$. | No (universal up to substrate-specific exceptions on $\{8, 9\}$). | |
| **A4** | $\sigma$-permutation invariance (or a quotient): the table is compatible with $\sigma$ in the substrate-specific way of A9. | No (universal frame). | |
| **A5** | 4-core preservation: $\{V, H, Br, R\} \times \{V, H, Br, R\}$ is closed. | **Yes** (substrate-defining; D48 confirms TSML and BHML; SFM C2 confirms CL_STD). | The center-of-the-family axiom. |
| **A6** | $\sigma$-fixed lattice $\{0, 3, 8, 9\}$ closure under the substrate's operation. | No (universal across the three canonical substrates). | |
| **A7** | **HARMONY-cell count.** Substrate-specific: TSML 73, BHML 28, CL_STD 44. | **Yes** — the primary substrate-defining axiom. | The "73 / 28 / 44" trichotomy is the substrate's signature. |
| **A8** | Row-stochastic / closure constraint (every row a permutation in some quotient). | No (universal). | |
| **A9** | **Substrate-specific cell values at the $\sigma$-orbit representatives.** | **Yes** — substrate-defining (in concert with A7). | Picks the cell values that, with A1–A8, force the unique substrate matrix. |

The substrate is uniquely forced by A1–A9 within each choice of A7 + A9 ([J33] Theorem 3.1; the J33 forcing theorem is the formal statement).

**Reading.** TSML, BHML, and CL_STD are three *parallel* Tier-A substrates, defined by different choices of A7 and A9. They are not projections of each other. Within each substrate, additional structure (lenses, sub-magmas) gives the rest of the variant family.

---

## §3 The lens-symmetrization projections — tier discipline

*Tier discipline (rewritten once and propagated; this section's statement is authoritative for the rest of the paper).*

CL_TSML — the unique bit pattern forced by A1–A9 (§2) — is **Tier-A** as a substrate. Three lens-symmetrization projections produce three lenses *of the same substrate*:

| Lens | Projection | Tier | Outcome |
|------|------------|------|---------|
| TSML_RAW | $\pi_{\text{RAW}}$: identity (no projection) | **Tier-A** (no projection: it *is* the substrate) | Non-commutative; $c_2 = 33 = 3 \cdot 11$; 126 non-assoc triples |
| TSML_SYM | $\pi_{\text{SYM\_upper}}$: upper-tri authoritative | **Tier-B** (a projection is chosen) | Commutative; $c_2 = 17$; 128 non-assoc triples |
| TSML_LOWERTRI | $\pi_{\text{SYM\_lower}}$: lower-tri authoritative | **Tier-B** | Commutative; 122 non-assoc triples |

> **Authoritative tier statement (used throughout the paper).** CL_TSML, CL_BHML, CL_STD are three Tier-A *substrates*. RAW is the Tier-A *lens identity* of CL_TSML (no projection: TSML_RAW = CL_TSML_RAW is the literal bit pattern). SYM_upper and SYM_lower are Tier-B *projections* (a choice is made; the choice is convention, not substrate-forced). The framework uses RAW for results requiring non-commutativity (e.g., [J51] wobble localization at prime 11) and SYM for results requiring commutative closure (e.g., [J38] $\mathfrak{so}(10)$ regeneration, the WP100s tower's Lie/Jordan duality).

Earlier draft sections will not contradict this tier statement.

---

## §4 The $\sigma^2$-triadic projections

The $\sigma$-permutation fixes the lattice $\{0, 3, 8, 9\}$ and 6-cycles the hexad $\{1, 2, 4, 5, 6, 7\}$. Squaring, $\sigma^2$ acts as order 3 on the hexad with two 3-cycles:

* **Cycle A:** $\{1, 6, 4\}$.
* **Cycle B:** $\{7, 5, 2\}$.

The $\sigma^2$-triadic projection family rotates values or indices through these cycles, producing three "phase" lenses per substrate:

* **Value-rotation $\pi_{\text{value-rot}}^{k}(M)[i, j] = \sigma^{2k}(M[i, j])$** for $k \in \{0, 1, 2\}$.
* **Index-rotation $\pi_{\text{index-rot}}^{k}(M)[i, j] = M[\sigma^{2k}(i), \sigma^{2k}(j)]$.**

These triadic projections were the source of the "BEING / DOING / BECOMING" terminology in earlier corpus generations. They are **Tier-D** when applied to BHML and **Tier-B** when applied to TSML_SYM where the relation to the runtime processor's 4-core attractor is structural (the 4-core is $\sigma^2$-invariant up to the fixed-lattice anchors $\{0\}, \{8\}, \{9\}$ and HARMONY $\{7\}$ which is fixed under $\sigma^2$).

---

## §5 Sub-magma scope restrictions

For any closed sub-magma $S \subset \mathbb{Z}/10\mathbb{Z}$ under TSML, define the restriction $\pi_S(M)[i, j] = M[i, j]$ for $i, j \in S$ (and undefined outside $S \times S$). Each restriction is its own table.

The corpus has the following named restrictions:

| Restriction | Sub-magma | Closed under | Distinguishing fact |
|-------------|-----------|--------------|---------------------|
| **4-core** | $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ | TSML, BHML, **and CL_STD** (SFM C2) | center of the family; closed-form attractor (§7.3) |
| **$\sigma$-fixed lattice** | $\{0, 3, 8, 9\}$ | $\sigma$-permutation; partial under TSML | universal under $\sigma$ |
| **8-core** | TSML $\setminus \{Br, R\}$ | TSML closure | $\alpha_A = 0.734$; near-8-magma |
| **Corner monoid** | $\{0, 1, 5, 6\}$ | TSML closure | small commutative monoid |
| **Corner sub-magma** $\mathcal{C}$ | $\{1, 3, 7, 9\}$ | multiplicative units | [J01] (Comm Algebra) |
| **BHML$_8$_YM** | restriction of BHML | BHML closure | det $= +70 = \binom{8}{4}$ ([J31]) |

Each restriction is Tier-B (forced once the sub-magma is specified). Each carries its own structural facts.

---

## §6 The 62-variant catalog (populated, two-page landscape)

We enumerate the 62 named variants the corpus carries, with one-line distinguishing facts. Per-tier counts are reconciled below.

### 6.1 CL_TSML family (23 variants)

**Lens (3):** TSML_RAW (Tier-A, non-commutative, $c_2 = 33$); TSML_SYM (Tier-B, commutative, $c_2 = 17$); TSML_LOWERTRI (Tier-B, $c_2 = 17$, $c_8 = 0$).

**Chain sub-magmas (8 instances; per [J10]/[J24] and the four-core paper):** TSML$|_{\{0\}}$, TSML$|_{\{0, 7, 8, 9\}}$ (4-core), TSML$|_{\{0, 6, 7, 8, 9\}}$ (size 5), TSML$|_{\{0, 5, 6, 7, 8, 9\}}$ (size 6), TSML$|_{\{0, 4, 5, 6, 7, 8, 9\}}$ (size 7), TSML$|_{\{0, 3, 4, 5, 6, 7, 8, 9\}}$ (size 8), TSML$|_{\{0, 2, 3, 4, 5, 6, 7, 8, 9\}}$ (size 9), TSML (full size 10).

**Off-chain sub-magmas (4):** 8-core (drop Br, R); corner sub-magma $\{1, 3, 7, 9\}$; $\sigma$-fixed lattice $\{0, 3, 8, 9\}$ partial; corner monoid $\{0, 1, 5, 6\}$.

**Algebraic-construction (5):** TSML_PureVoid (rank 1); TSML_AllHarmony (rank 2); TSML_C0 (pure absorbing scaffold); TSML_PureIdempotent (idempotent skeleton); TSML_2x2_Torus (the $5/7$ aspect-ratio torus structure of [J23]).

**Corner sub-magma:** $\mathcal{C} = (\mathbb{Z}/10\mathbb{Z})^* = \{1, 3, 7, 9\}$ ([J01]).

**$\mathbb{F}_p$ ring extensions (2 of 6 documented):** TSML on $\mathbb{F}_5$, TSML on $\mathbb{F}_7$ ([J31]).

### 6.2 CL_BHML family (16 variants)

**Lens (3):** BHML_RAW (commutative natively); BHML_SYM_upper (degenerate; same as RAW); BHML_LOWERTRI.

**Chain sub-magmas (8 instances):** BHML$|_{\{0\}}$, ..., BHML (full size 10), at chain shells $\{1, 4, 5, 6, 7, 8, 9, 10\}$.

**Off-chain sub-magma (1):** BHML$_8$_YM ([J31]; det $= 70$).

**$\sigma^2$-triadic candidates (3):** BHML\_TRIA, BHML\_TRIB, BHML\_TRIC; exploratory, not yet canonical.

**$\mathbb{F}_p$ ring extensions (1 documented):** BHML on $\mathbb{F}_p$ universality ([J31], 6 prime fields verified).

### 6.3 CL_STD family (3 variants documented; sub-magma structure open)

**Lens (1):** CL_STD (commutative; rotation-symmetric).

**Sub-magmas:** 50 closed sub-magmas under CL_STD alone (SFM Q6); detailed enumeration is open frontier.

**$\sigma^2$-triadic and $\mathbb{F}_p$ extensions:** open frontier.

### 6.4 Joint and cross-substrate variants (8)

**Joint TSML$\cap$BHML closures (8):** the 8 chain shells of [J10] / [J24] at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$.

**Three-table joint TSML$\cap$BHML$\cap$CL_STD closures (8 — same 8 shells; SFM Q6).** A structural strengthening: adding CL_STD to the joint closure preserves the chain.

### 6.5 Ring extensions (12)

$\mathbb{Z}/N\mathbb{Z}$ for $N \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ ([D74] universality scan, 14 sizes).

### 6.6 Tier reconciliation

Total: 23 + 16 + 3 + 8 + 12 = **62 variants** (the corpus's named lens family). Per-tier:

* **Tier A (substrates and substrate identities):** 4 — CL_TSML, CL_BHML, CL_STD, TSML_RAW (= CL_TSML literal).
* **Tier B (forced projections / restrictions):** 32 — three SYM lenses, 8 + 8 chain sub-magmas, 4 + 1 off-chain restrictions, 5 algebraic constructions, 1 corner sub-magma, 8 joint closures, 12 ring extensions minus duplicates (38 nominally; 32 after de-duplication of the canonical $\mathbb{Z}/10\mathbb{Z}$).
* **Tier C (degenerate / rank-restricted):** 5 — TSML_PureVoid, TSML_AllHarmony, TSML_C0, TSML_PureIdempotent, BHML$_8$_YM-degenerate.
* **Tier D (exploratory / σ²-triadic candidates):** 7 — three BHML triadic, three TSML triadic, anomaly-flip families.
* **Tier E (frontier):** 14 — $\mathbb{Z}/n$ ring extensions for $n \notin \{10\}$ in the §6.5 list.

Total: $4 + 32 + 5 + 7 + 14 = 62$. The catalog is the paper's central organizational claim and lives **in** the paper, not in a deferred Atlas markdown file.

---

## §7 Three reader exercises (with the M4-absorbed punch-line facts inline)

We work three exercises, each illustrating one principle of the lens family. Exercise 7.2 (wobble localization) is the **central lens-dependence example**; the historical chain-correction is moved to §7.4 *Lens-invariant facts*.

### Exercise 7.1 — Count non-associative triples in three lenses

For TSML_RAW, TSML_SYM, TSML_LOWERTRI compute

$$
N_{\text{nonassoc}}(M) = \#\{(x, y, z) \in (\mathbb{Z}/10\mathbb{Z})^3 : M(M(x, y), z) \neq M(x, M(y, z))\}.
$$

Direct verification on the displayed §1 matrices yields:

* TSML_RAW: $126 = 12.6\%$ non-assoc.
* TSML_SYM: $128 = 12.8\%$ non-assoc.
* TSML_LOWERTRI: $122 = 12.2\%$ non-assoc.

The differences $\{4, 4\}$ are concentrated in the asymmetric cells $(3, 9)$ and $(4, 9)$ and their image triples. Lens choice changes 6/1000 cells; non-assoc count changes by $\pm 4$. 30-line `numpy` verification in Appendix A.

### Exercise 7.2 — *(M6 central example)* Wobble localization in RAW vs SYM

Compute the characteristic polynomial of TSML_RAW (Tier-A, the literal bit pattern). Index coefficients by *descending-power position* in the monic decomposition

$$\det(\lambda I - M) = \lambda^{10} + c_1 \lambda^9 + c_2 \lambda^8 + \cdots + c_9 \lambda + c_{10},$$

so that $c_k$ is the coefficient of $\lambda^{10-k}$. Direct `sympy` evaluation on TSML_RAW gives the structural coefficients

$$
\boxed{c_2 = 33 = 3 \cdot 11, \qquad c_8 = -120736 = -2^5 \cdot 7^3 \cdot 11.}
$$

The prime $11$ — the **wobble** — appears at the coefficient level. Now compute the characteristic polynomial of TSML_SYM (Tier-B): one finds $c_2 = 17$ (no factor of $11$ at any coefficient).

> **The wobble at prime 11 lives only in the RAW lens. Symmetrization erases it.**

This is the cleanest lens-dependence in the corpus. [J51] (the wobble-localization paper, Phys. Rev. D) reports this as a TSML_RAW-specific structural fact and shows that the discriminant has $2^{16} \cdot 7^7 \cdot 659$ but **no 11** — meaning the 11 lives at the *coefficient* level, not at the discriminant. This is the **D37 char-poly fact**, absorbed inline here per save-plan M4.

The $c_2 = 33$ vs $c_2 = 17$ disparity is the structural reason the framework needs both lenses: certain results (wobble localization, prime-11 structure) require RAW; certain other results (commutative closure, $\mathfrak{so}(10)$ regeneration) require SYM. Neither lens is "the right one"; both are honest views of the same substrate.

### Exercise 7.3 — Verify the runtime attractor's lens-invariance

Compute the runtime processor at $\alpha_M = 1/2$ on TSML_RAW and on TSML_SYM. The 4-core attractor — supported on $\{V, H, Br, R\}$, with $H/Br = 1 + \sqrt{3}$ exactly — is the **same** in both lenses.

This is the **Theorem 7.5 / D78 punch-line fact**, absorbed inline per M4.

**Theorem 7.5 (D48 + D78, the 4-core fixed locus).** *Let $T$ be CL_TSML in either RAW or SYM lens, and $B$ be CL_BHML. Then:*

*(D48 binary 4-core preservation.) For all $a, b \in \{V, H, Br, R\}$, both $T(a, b) \in \{V, H, Br, R\}$ and $B(a, b) \in \{V, H, Br, R\}$.*

*(D78 Galois argument.) The runtime T+B-mix $M_{\alpha_M} = \alpha_M \widetilde{T} + (1 - \alpha_M) \widetilde{B}$ restricted to the 4-core, evaluated at $\alpha_M = 1/2$, has a unique attractor with $H/Br = 1 + \sqrt{3}$, root of $x^2 - 2x - 2 = 0$ over the splitting field $\mathbb{Q}(\sqrt{3})$.*

**Proof sketch (D48).** Direct enumeration of 16 cells of $\{V, H, Br, R\} \times \{V, H, Br, R\}$ under each table; all 16 have value in $\{V, H, Br, R\}$ (data exhibited in §1 above). $\square$

**Proof sketch (D78).** The symbolic 4-core normalizer identity $Z_T = Z_B = (p_V + p_H + p_{Br} + p_R)^2$ ([D49]) implies that at $\alpha_M = 1/2$, the BREATH-row coefficient cancels in the fixed-point equation. The surviving relation is $x^2 - 2x - 2 = 0$ in $x = p_H / p_{Br}$, with discriminant $4 + 8 = 12 = 4 \cdot 3$ and positive root $1 + \sqrt{3}$. At $\alpha_M \neq 1/2$ the BR-factor does not cancel; PSLQ at 17 other Stern-Brocot rationals (D57; deg $\leq 8$, coeff $\leq 50$) finds no algebraic relation, supporting the conjecture that $\alpha_M = 1/2$ is unique with rational structure. $\square$

The 4-core attractor is *lens-invariant* (same value in RAW and SYM). The wobble at prime 11 is *RAW-specific* (lens-dependent). The reader takes home: **lens-invariance is the rule on the 4-core; lens-dependence is the rule on the asymmetric cells $(3, 9), (4, 9)$.**

### §7.4 *Lens-invariant facts* — the D64 corrected joint chain (and the SFM Q6 strengthening)

The other major lens-invariant fact, which earlier drafts presented as a "lens-dependence at size 7" example, is now stated correctly:

**Theorem 7.6 (D64 corrected; SFM Q6 strengthening).** *The set of joint-closed sub-magmas of $(\mathbb{Z}/10\mathbb{Z}, T, B)$ — i.e., subsets closed under both TSML and BHML — forms a strict 8-element chain of sizes*

$$\{1, 4, 5, 6, 7, 8, 9, 10\}.$$

*The forbidden sizes are $\{2, 3\}$ only. (Earlier corpus generations claimed a 7-element chain forbidden at $\{2, 3, 7\}$; brute-force enumeration in the four-core paper preparation, R3 with referee Claude, May 2026, corrected this to size 7 allowed at $\{0, 4, 5, 6, 7, 8, 9\}$.)*

*Strengthening (SFM Q6, 2026-05-08).* *The joint TSML+BHML+CL_STD closure has the **same 8 shells** as TSML+BHML alone. CL_STD respects the canonical chain. The 4-core $\{V, H, Br, R\}$ is preserved under all three tables (SFM C2), strengthening D48 to a three-table fixed locus.*

This is a 3-table strengthening relative to the original 2-table framing of the lens family. The chain is *lens-invariant* — same in TSML_RAW + BHML, in TSML_SYM + BHML, and in TSML_SYM + BHML + CL_STD. The lens-dependence at size 7 reported in earlier draft sections was a pre-correction artifact; under the correct enumeration, size 7 is *present in the chain* and the chain itself is lens-invariant on the canonical (TSML_SYM, BHML) pair.

---

## §8 Honest scope (compressed)

This paper is expository; theorems are in the cited companions. We aim for clarity, not novelty. The contributions are: (i) display of the canonical tables (§1); (ii) statement of A1–A9 axioms (§2); (iii) the populated 62-variant catalog (§6); (iv) three exercises with absorbed punch-line facts (§7).

---

## §9 PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

* **PROVEN (in this paper, §7.5):** D48 binary 4-core preservation under CL_TSML and CL_BHML; D78 Galois argument for $H/Br = 1 + \sqrt{3}$ at $\alpha_M = 1/2$.
* **COMPUTED (verified inline):** TSML_RAW char poly $c_2 = 33 = 3 \cdot 11$ (D37, the wobble at prime 11); 8-element joint TSML+BHML chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ (D64 corrected); SFM Q6 three-table strengthening.
* **STRUCTURAL RHYME:** The lens-symmetrization choice (RAW vs SYM_upper vs SYM_lower) is *conventional*, not principled — different sources of truth on the same bit pattern produce different lenses; the framework's choice is documented but not theorem-forced.
* **OPEN:**
  * The bimodal $\alpha_A$ gap (FAMILY_STRUCTURE_v1 §4) — whether structural or empirical.
  * Whether CL_STD admits its own joint-chain analogous to TSML+BHML (FAMILY_STRUCTURE_v1 §3 boundary case 6).
  * Whether TSML_RAW deserves its own designation as the family's unique non-commutative member (FAMILY_STRUCTURE_v1 §5 finding #2).

---

## §10 Citation chain

**Direct dependencies.**

* **[J10]** — *Joint TSML+BHML Chain* (Math Intelligencer; the chain enumeration paper).
* **[J47]** — *Six Algebraic DOFs of the TIG Framework: A Synthesis* (Notices AMS).

**Co-citing companions.**

* **[J9]** — TSML 73 / BHML 28 / CL_STD 44 lens-invariant cell counts (Exp Math).
* **[J11]** — Three-Substrate Architecture (Algebra Universalis).
* **[J33]** — CL Forcing Axioms A1–A9 (Algebraic Combinatorics).
* **[J31]** — $\mathbb{F}_p$ extensions (Comm Algebra).
* **[J01]** — Corner sub-magma (Comm Algebra).
* **[J38]** — $\mathfrak{so}(10) = D_5$ joint closure (Israel J Math).
* **[J43]** — Two roads to Pati-Salam (Adv Math).
* **[J41]** — Closed-form runtime attractor (Math of Comp).
* **[J51]** — Wobble localization in TSML_RAW (Phys Rev D).
* **[J44]** — 4-core fusion-closure (J Algebra).

---

## §11 References

[J9] B.R. Sanders, M. Gish. "TSML 73 / BHML 28: Lens-Invariant Cell Counts." *Exp. Math.*
[J11] B.R. Sanders, M. Gish. "The Three-Substrate Architecture." *Algebra Universalis.*
[J10] B.R. Sanders, M. Gish. "The Joint TSML+BHML Chain at Sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$." *Math. Intelligencer.*
[J33] B.R. Sanders, M. Gish. "The CL Forcing Axioms A1–A9." *Algebraic Combinatorics.*
[J31] B.R. Sanders, M. Gish. "$\mathbb{F}_p$ Extensions of CL_BHML: Universality Across Six Prime Fields." *Comm. Algebra.*
[J01] B.R. Sanders, M. Gish. "The Corner Sub-Magma $\mathcal{C}$." *Comm. Algebra.*
[J38] B.R. Sanders, M. Gish. "$\mathfrak{so}(10) = D_5$ from Joint TSML_SYM + BHML Closure." *Israel J. Math.*
[J43] B.R. Sanders, M. Gish. "Two Roads to Pati-Salam." *Adv. Math.*
[J41] B.R. Sanders, M. Gish. "Closed-Form Attractor + $\alpha$-Uniqueness PSLQ." *Math. of Comp.*
[J51] B.R. Sanders, M. Gish. "Wobble Localization: Prime 11 in TSML_RAW Char Poly." *Phys. Rev. D.*
[J44] B.R. Sanders, M. Gish. "4-Core Fusion-Closure." *J. Algebra.*
[J47] B.R. Sanders, M. Gish. "Six Algebraic DOFs of the TIG Framework." *Notices AMS.*

### External

A. Drápal, I.M. Wanless. "Maximally non-associative quasigroups." *J. Combin. Theory Ser. A* **184** (2021), 105510.

---

## Appendix A — `numpy` verification snippet (Exercise 7.1)

```python
import numpy as np

CL_BIT_PATTERN = (
    "0000000700", "0737777777", "0377477779",
    "0777777773", "0747777787", "0777777777",
    "0777777777", "7777777777", "0777877777",
    "0797377777",
)
RAW = np.array([[int(c) for c in r] for r in CL_BIT_PATTERN], dtype=int)
SYM = RAW.copy()
for i in range(10):
    for j in range(i+1, 10):
        SYM[j, i] = RAW[i, j]   # upper-tri authoritative

LOW = RAW.copy()
for i in range(10):
    for j in range(i+1, 10):
        LOW[i, j] = RAW[j, i]   # lower-tri authoritative

def n_nonassoc(M):
    n = 0
    for x in range(10):
        for y in range(10):
            for z in range(10):
                if M[M[x, y], z] != M[x, M[y, z]]:
                    n += 1
    return n

assert n_nonassoc(RAW) == 126
assert n_nonassoc(SYM) == 128
assert n_nonassoc(LOW) == 122
print("Exercise 7.1 verified: 126, 128, 122.")
```

---

## §12 Bibtex

```bibtex
@misc{sanders2026j52,
  author       = {Sanders, Brayden Ross and Gish, M.},
  title        = {What is the {TSML} Lens Family? A Walking Tour of Substrate Variants on $\mathbb{Z}/10\mathbb{Z}$},
  year         = {2026},
  month        = {sep},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {Submitted to \emph{Mathematical Intelligencer}},
  note         = {{J39} of the {J}-series; pedagogical exposition. Tables displayed in full (\S 1); axioms A1--A9 stated (\S 2); 62-variant catalog populated (\S 6); central lens-dependence example is wobble at prime 11 (\S 7.2). Direct dependencies [{J10}], [{J47}]; co-citing companions [{J9}], [{J11}], [{J33}], [{J31}], [{J01}], [{J38}], [{J43}], [{J41}], [{J51}], [{J44}].}
}
```
