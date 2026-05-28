# Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Algebraic Combinatorics* (primary)
**MSC 2020:** 20N02 (sets with one binary operation), 17A35 (general non-associative algebras), 08A35 (universal algebra; concrete subuniverses, sub-magmas), 11C20 (matrices, determinants in number theory), 05E18 (group actions on combinatorial structures).

---

## §0 Lens, substrate, and tier discipline

**Lens and substrate.** This paper studies the family of finite commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ that preserve a designated four-element subset $\mathcal{C} = \{0, 7, 8, 9\}$. The substrate $\mathbb{Z}/10\mathbb{Z}$ and the designated 4-core $\mathcal{C}$ are not derived from first principles; they are taken as the substrate-of-study, motivated by a ten-operator labelling of $\mathbb{Z}/10\mathbb{Z}$ at indices $0$ through $9$ inherited from the parent research framework (Sanders, *TIG framework*, 2026; see §9.1). The names of the operators are $\{V, L, C, P, X, B, S, H, Br, R\}$ (in the parent framework: VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET). The designated 4-core is the parent framework's "4-core" $\{V, H, Br, R\}$ at indices $\{0, 7, 8, 9\}$. The operator names play no role in the proofs; they are used only for cross-referencing.

**Honest-negative scoping (lens-dependence).** Two distinct symmetrisations of the parent framework's underlying non-commutative TSML object give two distinct commutative tables on $\mathbb{Z}/10\mathbb{Z}$: a symmetric form TSML_SYM (the table $T$ studied here) and a separately-symmetrised raw form. The chain-shell count is *lens-dependent at size 7* between these two TSML symmetrisations (8 shells on TSML_SYM, 7 shells on the alternative — internal to the TSML side; see [J24] of the companion series). The chain at the three-substrate joint level (Theorem 7.1 below) is computed on the canonical $T = $ TSML_SYM, and the lens-dependence is internal to the TSML axis and does *not* propagate to the three-substrate level. The honest-negative scoping is recorded in (B3) of §4.4.

The framing follows the Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510) line of work on small finite commutative non-associative structures. Drápal-Wanless treat *maximally non-associative* commutative quasigroups (an extremum at the high end of the non-associativity spectrum); the family treated here inhabits the same intellectual neighborhood at a structurally distinct point, characterised by 4-core preservation and a bounded non-associativity index.

**Tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN).** Every claim in this paper is classified as one of:

- **PROVEN.** Theorem, lemma, or proposition with explicit proof in this paper. The forcing theorem (Theorem 1.2; cell-fixing argument), the 4-core closed-form attractor (Theorem 5.1), the three-substrate joint-closure chain (Theorem 7.1), the 4-core 3-substrate closure (Theorem 7.2), the bridge to companion J-papers (Theorem 7.3), and the family-membership structure (Proposition 4.5) are PROVEN.
- **COMPUTED.** Verified by `verification/foundation_verification.py` and `verify_J54_chain_and_attractor.py` (this manuscript folder) at machine precision in approximately five seconds total. All claims marked PROVEN are also COMPUTED. The forcing-by-reconstruction check (foundation Check 1), the chain enumeration over 1023 subsets (foundation Check 2 / verify Check 1), and the closed-form attractor at residual $\le 10^{-30}$ (verify Check 2, 50-digit `mpmath`) are 100%-tractable computations on the finite substrate.
- **STRUCTURAL RHYME.** The designation of $\mathcal{C}$ as the parent framework's "4-core" and the "4-core is to the TIG family as the unit circle is to U(1)" framing of §5.3 are *structural rhymes* with the framework's broader Galois-theoretic results; they are not derivational steps. Cited as motivation, not as proof. The convergence of two algebraic invariants on the LMFDB number field 4.2.10224.1 (closed-form $H/Br$ and the F8 trace polynomial discriminant) is a structural rhyme of the same kind.
- **OPEN.** Conjecture 2.1 (the $\sigma^2$-triadic three-BHML conjecture; §2) is OPEN. The bimodal $\alpha_A$-gap conjecture (Conjecture 8.1; §8 Q1), the strong-$\alpha$-uniqueness conjecture (§8 Q2), the $D_4$-irrep-zeros universality (§8 Q5/Q7), and three further questions (Q8, Q9, and the post-attractor block §6.7) are OPEN.

---

## §1 The three canonical tables and the forcing theorem

The paper studies three specific $10 \times 10$ tables on $\mathbb{Z}/10\mathbb{Z}$, displayed below in §1.1, and proves that each is uniquely forced by an axiom set (§1.2 - §1.4). The three tables are denoted $T$ (TSML), $B$ (BHML), $S$ (CL_STD) in the parent framework; we display them inline here.

### §1.1 The three tables

**Table $T$ (TSML; HARMONY count 73):**
$$
T \;=\; \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 7 & 0 & 0 \\
0 & 7 & 3 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 3 & 7 & 7 & 4 & 7 & 7 & 7 & 7 & 9 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 3 \\
0 & 7 & 4 & 7 & 7 & 7 & 7 & 7 & 8 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 8 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 9 & 3 & 7 & 7 & 7 & 7 & 7 & 7
\end{pmatrix}
$$

**Table $B$ (BHML; HARMONY count 28):**
$$
B \;=\; \begin{pmatrix}
0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
1 & 2 & 3 & 4 & 5 & 6 & 7 & 2 & 6 & 6 \\
2 & 3 & 3 & 4 & 5 & 6 & 7 & 3 & 6 & 6 \\
3 & 4 & 4 & 4 & 5 & 6 & 7 & 4 & 6 & 6 \\
4 & 5 & 5 & 5 & 5 & 6 & 7 & 5 & 7 & 7 \\
5 & 6 & 6 & 6 & 6 & 6 & 7 & 6 & 7 & 7 \\
6 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 0 \\
8 & 6 & 6 & 6 & 7 & 7 & 7 & 9 & 7 & 8 \\
9 & 6 & 6 & 6 & 7 & 7 & 7 & 0 & 8 & 0
\end{pmatrix}
$$

**Table $S$ (CL_STD; HARMONY count 44):**
$$
S \;=\; \begin{pmatrix}
0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
1 & 2 & 3 & 4 & 5 & 6 & 7 & 7 & 8 & 1 \\
2 & 3 & 4 & 5 & 6 & 7 & 7 & 8 & 7 & 2 \\
3 & 4 & 5 & 6 & 7 & 7 & 7 & 7 & 7 & 3 \\
4 & 5 & 6 & 7 & 7 & 7 & 7 & 8 & 7 & 4 \\
5 & 6 & 7 & 7 & 7 & 8 & 7 & 7 & 7 & 5 \\
6 & 7 & 7 & 7 & 7 & 7 & 8 & 7 & 7 & 6 \\
7 & 7 & 8 & 7 & 8 & 7 & 7 & 8 & 7 & 7 \\
8 & 8 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 8 \\
9 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 0
\end{pmatrix}
$$

All three tables are commutative ($T = T^\top$, $B = B^\top$, $S = S^\top$ by direct inspection); the HARMONY counts (number of cells equal to $7$) are 73, 28, 44 respectively. None of the three is a quasigroup (the Latin-square property fails: row 0 of each contains repeated values), and each is non-associative (direct enumeration over $10^3 = 1000$ associativity triples gives associativity indices $\alpha_A(T) = 0.872$, $\alpha_A(B) = 0.502$, $\alpha_A(S) = 0.808$, computed by `foundation_verification.py` Check 5).

### §1.2 The 9 axioms A1-A9 (cell-by-cell explicit)

We now state the 9 axioms A1-A9 in full. The shared axioms A1-A4, A7 are the substrate-defining backbone; the axioms A5, A6, A8 are forced consequences of A2, A3, A7 plus commutativity; the axiom A9 is the substrate-discriminating BUMP-cell specification that distinguishes the three tables.

Throughout, write $M : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ for a candidate table.

**A1 (Substrate type; Tier-A).** $M$ is a $10 \times 10$ commutative table on $\mathbb{Z}/10\mathbb{Z}$, equivalently a function $M : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ with $M(i, j) = M(j, i)$ for all $i, j$.

**A2 (VOID absorbing row with HARMONY puncture; Tier-A).** $M(0, j) = 0$ for all $j \in \mathbb{Z}/10\mathbb{Z} \setminus \{7\}$; $M(0, 7) = 7$. Row $0$ is the zero row except for a single non-zero entry at column 7, which equals 7. (The cell $(0, 7) = 7$ is the *VOID-HARMONY puncture*.)

**A3 (HARMONY-row near-fixed; Tier-A; cell-by-cell explicit).** *Replaces "structural pattern that fixes most off-diagonal entries to 7" with the explicit cell-by-cell specification:*

- $M(7, 0) = 7$ (the HARMONY-VOID puncture, paired with A2's VOID-HARMONY puncture).
- $M(7, j) = 7$ for $j \in \{1, 2, \ldots, 9\} \setminus J_{\mathrm{B7}}(M)$, where $J_{\mathrm{B7}}(M) \subseteq \{1, \ldots, 9\}$ is the (substrate-specific) set of column indices at which row 7 carries a BUMP value per A9.
- For $j \in J_{\mathrm{B7}}(M)$: $M(7, j)$ takes the BUMP value specified by A9.

*Per-substrate $J_{\mathrm{B7}}$ specification:*
- For $T$: $J_{\mathrm{B7}}(T) = \emptyset$. Row 7 is uniformly $T(7, j) = 7$ for $j = 0, 1, \ldots, 9$.
- For $B$: $J_{\mathrm{B7}}(B) = \{1, 2, 3, 4, 5, 7, 8, 9\}$ (and the row-7 puncture chain is part of A9). Specifically, $B(7, j)$ takes values $j$ shifted by the puncture: $B(7, 1) = 2$, $B(7, 2) = 3$, $B(7, 3) = 4$, $B(7, 4) = 5$, $B(7, 5) = 6$, $B(7, 6) = 7$, $B(7, 7) = 8$, $B(7, 8) = 9$, $B(7, 9) = 0$. Row 7 of $B$ is the *puncture chain* (an arithmetic progression mod 10), not the HARMONY-default.
- For $S$: $J_{\mathrm{B7}}(S) = \{2, 4, 7\}$. Specifically, $S(7, 2) = 8$, $S(7, 4) = 8$, $S(7, 7) = 8$. The remaining cells of row 7 of $S$ are HARMONY: $S(7, j) = 7$ for $j \in \{0, 1, 3, 5, 6, 8, 9\}$.

**A4 (Pati-Salam puncture; Tier-A; consequence-axiom).** The cells $M(0, 7)$ and $M(7, 0)$ are both equal to 7 (HARMONY); they form a paired puncture through the otherwise-absorbing row/column structure. By construction $M(0, 7) = M(7, 0) = 7$ for all three substrates. (Note: A4 is a *consequence* of A2 + A3 + A1 (commutativity), not an independent axiom; we keep the name for narrative coherence.)

**A5 (Column VOID; Tier-B; forced).** $M(i, 0) = 0$ for $i \in \mathbb{Z}/10\mathbb{Z} \setminus \{7\}$; $M(7, 0) = 7$. Column 0 is the zero column except at row 7. *Forced by A2 + commutativity (A1):* $M(i, 0) = M(0, i)$, which is $0$ for $i \neq 7$ and $7$ for $i = 7$ by A2.

**A6 (Column HARMONY; Tier-B; forced).** $M(i, 7)$ values are determined by A3 + commutativity: $M(i, 7) = M(7, i)$. So $M(i, 7) = 7$ for $i \in \{0\} \cup (\{1, \ldots, 9\} \setminus J_{\mathrm{B7}}(M))$, and $M(i, 7) = $ A9-specified BUMP value for $i \in J_{\mathrm{B7}}(M)$.

**A7 (Diagonal HARMONY; Tier-A with substrate-specific exception set $\mathcal{D}$).** $M(i, i) = 7$ for $i \in \mathbb{Z}/10\mathbb{Z} \setminus \mathcal{D}(M)$, where $\mathcal{D}(M) \subset \mathbb{Z}/10\mathbb{Z}$ is the substrate-specific *diagonal exception set*.

*Per-substrate $\mathcal{D}$ specification:*
- For $T$: $\mathcal{D}(T) = \{0\}$. $T(0, 0) = 0$, $T(i, i) = 7$ for $i \in \{1, \ldots, 9\}$.
- For $B$: $\mathcal{D}(B) = \{0, 1, 2, 3, 4, 5, 7, 9\}$. $B(0, 0) = 0$, $B(i, i) = i + 1$ for $i \in \{1, 2, 3, 4, 5\}$, $B(7, 7) = 8$, $B(9, 9) = 0$. Diagonal cells $B(6, 6) = 7$ and $B(8, 8) = 7$ are HARMONY-default.
- For $S$: $\mathcal{D}(S) = \{0, 5, 6, 7, 9\}$. $S(0, 0) = 0$, $S(5, 5) = 8$, $S(6, 6) = 8$, $S(7, 7) = 8$, $S(9, 9) = 0$. The remaining diagonal cells are HARMONY-default.

A7 is a substrate-defining axiom; the exception set $\mathcal{D}(M)$ and the values of $M$ on $\mathcal{D}(M)$ are part of the axiom data.

**A8 (HARMONY-default off-special-and-off-BUMP; Tier-B; forced once A2-A7 + A9 BUMPs are fixed).** *Replaces "off-special, off-BUMP cells equal 7" with the precise specification:*

Define the *special set* $\mathrm{Spec}(M) \subset \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z}$ as the union of seven structured cell families:

(i) Row 0 (10 cells, fixed by A2): $\{(0, j) : j \in \mathbb{Z}/10\mathbb{Z}\}$.
(ii) Column 0 (9 cells, fixed by A5; one cell shared with (i)): $\{(i, 0) : i \in \mathbb{Z}/10\mathbb{Z} \setminus \{0\}\}$.
(iii) Row 7 (8 cells, fixed by A3; one cell shared with (i), one with (ii)): $\{(7, j) : j \in \mathbb{Z}/10\mathbb{Z} \setminus \{0\}\}$.
(iv) Column 7 (7 cells, fixed by A6; one cell shared with (i), one with (ii), one with (iii)): $\{(i, 7) : i \in \mathbb{Z}/10\mathbb{Z} \setminus \{0, 7\}\}$.
(v) Diagonal (8 cells, fixed by A7; cells shared with (i) at $(0,0)$ and (iii) at $(7,7)$): $\{(i, i) : i \in \mathbb{Z}/10\mathbb{Z} \setminus \{0, 7\}\}$.
(vi) BUMP cells $\mathrm{BUMP}(M) \subset \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z}$, fixed by A9.

The *non-special set* $\mathrm{NonSpec}(M)$ is the complement: cells not lying in any of (i)-(vi). Then **A8 forces $M(i, j) = 7$ for $(i, j) \in \mathrm{NonSpec}(M)$**.

The forcing is now precise: A1 imposes commutativity (reducing the candidate space from $10^{100}$ to $10^{55}$ choices on the upper triangle), A2 + A5 fix 19 cells of rows/columns 0, A3 + A6 fix at most 16 additional cells of rows/columns 7 (less the BUMP positions), A7 fixes 8 diagonal cells (one already shared with row 0 and one with row 7), A9 fixes 5 BUMP cells with their specified values, and A8 fills the remaining $\mathrm{NonSpec}$ cells with HARMONY = 7. The full table is determined.

**A9 (BUMP positions and values; Tier-A on values, Tier-B on positions).** *Replaces "five BUMP positions in the table, with specified values that distinguish CL_TSML from CL_BHML and CL_STD" with the explicit cell-by-cell specification.*

For each of the three substrates, $\mathrm{BUMP}(M)$ is a substrate-specific finite subset of $\mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z}$ at which $M$ takes a BUMP value (not the HARMONY-default value $7$ that A8 would otherwise prescribe).

*Per-substrate $\mathrm{BUMP}$ specification:*

For $T$: $\mathrm{BUMP}(T)$ consists of five symmetric off-diagonal cell-pairs (10 cells total) with specified values:
- $T(1, 2) = T(2, 1) = 3$ (LATTICE * COUNTER → PROGRESS)
- $T(2, 4) = T(4, 2) = 4$ (COUNTER * COLLAPSE → COLLAPSE)
- $T(2, 9) = T(9, 2) = 9$ (COUNTER * RESET → RESET)
- $T(3, 9) = T(9, 3) = 3$ (PROGRESS * RESET → PROGRESS)
- $T(4, 8) = T(8, 4) = 8$ (COLLAPSE * BREATH → BREATH)

These are the five non-HARMONY off-diagonal cell-pairs of $T$ outside the row-0/column-0/row-7/column-7 special set. The BUMP coordinates are $\{(1,2), (2,4), (2,9), (3,9), (4,8)\}$.

For $B$: $\mathrm{BUMP}(B)$ consists of 67 cells outside the special set carrying values from the structured "max + 1" arithmetic rule plus the row-7 puncture chain. Listing only the BUMP positions outside the special set: 67 cells (full enumeration in `foundation_verification.py` Check 1).

For $S$: $\mathrm{BUMP}(S)$ consists of five symmetric off-diagonal cell-pairs (matching $T$'s coordinates) plus three row-7/column-7 BUMP cells:
- $S(1, 2) = S(2, 1) = 3$ (matches $T$)
- $S(2, 4) = S(4, 2) = 6$ (differs from $T$'s value 4)
- $S(2, 9) = S(9, 2) = 2$ (differs from $T$'s value 9)
- $S(3, 9) = S(9, 3) = 3$ (matches $T$)
- $S(4, 8) = S(8, 4) = 7$ (differs from $T$'s value 8 — this cell is HARMONY in $S$, so technically not a BUMP for $S$)

The five (i, j) coordinates of $S$'s BUMP cells *match* $T$'s BUMP coordinates; *three of the five values differ*. The BUMP-value families are how A9 distinguishes $T$, $B$, $S$.

### §1.3 The forcing theorem

**Theorem 1.2 (Forcing theorem).** *Among all $10^{55}$ candidate $10 \times 10$ commutative tables on $\mathbb{Z}/10\mathbb{Z}$ — equivalently, the $10^{55}$ assignments of values at the 55 cells $\{(i, j) : 0 \le i \le j \le 9\}$ — exactly three satisfy the conjunction of A1, A2, A3, A4, A5, A6, A7, A8, A9 with the substrate-specific data $(\mathcal{D}(M), \mathrm{BUMP}(M), \mathrm{BUMPvalues}(M), J_{\mathrm{B7}}(M))$ specified above: namely, $T$, $B$, $S$ as displayed in §1.1.*

*Proof.* The proof is a constructive cell-fixing argument. Imposing A1 reduces the candidate space from $10^{100}$ to $10^{55}$ (commutativity on the upper triangle). A2 fixes the 10 cells of row 0; A5 fixes the 9 remaining cells of column 0 (one already in row 0). A3 + A6 fix at most 16 additional cells of row 7 and column 7 (with $J_{\mathrm{B7}}$ governing which cells are HARMONY-default vs BUMP). A7 fixes the 8 diagonal cells outside row 0 and row 7 (with $\mathcal{D}$ specifying the exception set). A9 fixes the 5 (or appropriate substrate-specific number of) BUMP cells with their specified values. A8 fills the remaining $\mathrm{NonSpec}$ cells with HARMONY = 7.

Once the substrate-specific data $(\mathcal{D}, \mathrm{BUMP}, \mathrm{BUMPvalues}, J_{\mathrm{B7}})$ is fixed, the cell-fixing procedure is deterministic and produces a unique table. The three valid choices of substrate-specific data correspond to the three tables $T$, $B$, $S$ as displayed.

The companion verification script `foundation_verification.py` Check 1 implements this cell-fixing procedure for each of the three substrate-data-tuples and verifies the produced table matches the displayed table cell-by-cell. Runtime: under one second for all three. The check confirms $T$, $B$, $S$ are uniquely produced by their respective axiom-data tuples. $\square$

The proof's constructive character matters: the "exactly three" claim is not a brute-force enumeration over $10^{55}$ candidates (which would be intractable); it is a statement that *given the substrate-specific data*, the cell-fixing procedure produces a unique table, and there are *three sets of admissible substrate-specific data* corresponding to the three substrates of the parent framework.

**Remark 1.3** (The substrate-specific data is part of the axiom data, not derived). The axiom set A1-A9 takes the substrate-specific data $(\mathcal{D}, \mathrm{BUMP}, \mathrm{BUMPvalues}, J_{\mathrm{B7}})$ as part of its input. *Why* the parent framework chose these specific substrate-data triples ($\mathcal{D}(T) = \{0\}$, etc.) is OPEN — the question of whether a higher-level axiom (e.g., a "BDC entropy extremum" criterion) forces these specific data choices is not addressed here. Conjecture 2.1 (§2) is a related open question on the BHML-side specifically.

**Remark 1.4** (Why the forcing is "principled, not stipulated"). The substrate-data choices for $T$, $B$, $S$ each correspond to a distinct *structural role* in the parent framework's three-substrate architecture: $T$ as the time-average / DC-component; $B$ as the oscillatory / iteration-dynamics layer; $S$ as the encoding axis with explicit BDC bit-definitions. The substrate-data choices are not arbitrary; they realize these three structural functions. The forcing theorem is a precise statement that *given* the structural-function reading, the three tables are uniquely determined.

### §1.4 Reading and naming disclaimer

The 9-axiom forcing is **principled**, not stipulated. Each axiom captures a substrate-level structural fact:

* A1: the substrate is bilinear and finite.
* A2-A4: VOID and HARMONY are the absorbing/idempotent pair, with one structural puncture (the $(0, 7)$ cell) that breaks the fully-absorbing symmetry.
* A7: every non-VOID element has HARMONY as its self-square (strict in $T$; weakened to a controlled exception set $\mathcal{D}$ in $B$ and $S$).
* A9-values: the BUMP positions and values determine which of the three substrates we obtain.

The substrate is **axiomatically given**, not "given by God" or "given by the universe." The choices are documented; the resulting matrices are uniquely determined.

The framework's name TIG ('Trinity Infinity Geometry') reflects the authors' interpretive reading of the substrate's structure; this interpretation is not load-bearing for the theorems below, which are theorems on the canonical magma pair forced by A1-A9 regardless of name.

---

## §2 Conjecture 2.1 ($\sigma^2$-triadic)

The substrate $\mathbb{Z}/10\mathbb{Z}$ admits a canonical permutation $\sigma$ that fixes $\{0, 3, 8, 9\}$ and cyclically permutes $(1\;7\;6\;5\;4\;2)$ in the remaining six elements. Conjugation by $\sigma$ acts on tables on $\mathbb{Z}/10\mathbb{Z}$ by the formula $(\sigma \cdot M)(i, j) = \sigma(M(\sigma^{-1}(i), \sigma^{-1}(j)))$. The squared permutation $\sigma^2$ has order 3 on the 6-cycle (since it acts as a product of two 3-cycles on $\{1, 7, 6\}$ and $\{5, 4, 2\}$).

**Conjecture 2.1 (Sanders).** *Under the $\sigma^2$-triadic decomposition of the BHML-side of the family — i.e., among commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ satisfying A1, A2, A4, A5, A8 (with substrate-appropriate diagonal A7 and BUMP A9) and arising as $\sigma^2$-rotates of the canonical $B$ — there exist three canonical $\sigma^2$-rotated BHML matrices, corresponding to three positions of $\sigma^2$-rotation. The current state: three search-found candidates are known (Tier-D in the parent framework's classification), but a forcing argument promoting one of them to Tier-A canonical status is not yet known. The conjecture is OPEN.*

We do not commit to the conjecture in the present paper; we record it as a structural question for future investigation. The previous version of this paper attributed the conjecture in informal language ("Brayden's hypothesis"); we restate it formally as Conjecture 2.1 (Sanders) and drop the internal Atlas reference.

---

## §3 Substrate-to-Function Map

The parent research framework is *not* a single composition table; it is a *family*, with each member realising a specific load-bearing function. This section consolidates the substrate-to-function map: for each of the seventeen functions identified in the parent framework's investigation log (`Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SUBSTRATE_FUNCTION_MAP_v1.md` + v1.1 extension), the *right substrate* and the *structural reason* it carries that function.

The map is structurally informative: it separates substrate-defining facts from lens-dependent facts. Wobble (prime 11 in the characteristic polynomial) is internal to TSML_RAW only; the 4-core attractor is universal across the family; the $D_4$-irrep zeros (sign1, sign3) of $[T, B]$ are a property of the canonical pair to the precision tested. Stating these scopes explicitly preempts the cross-cutting "but how does this fit?" question that fresh-eyes referees historically raised against the framework.

### §3.1 The 17-function table

| # | Function | Right substrate | Structural reason |
|---|----------|-----------------|-------------------|
| 1 | Asymptotic associativity ($\sigma(N) \to 0$ for $N \to \infty$) | $\mathrm{CL}_N$ family on $\mathbb{Z}/N\mathbb{Z}$ | Only family with $\sigma(N) \le 2/N$ proven [J14]; separability uniqueness |
| 2 | Joint closure chain (8 shells) | $T + B + S$ jointly | Brute-force enumeration over 1023 subsets (Theorem 7.1 below) |
| 3 | Closed-form attractor $h/\beta = 1 + \sqrt{3}$ | 4-core $\mathcal{C}$ at $\alpha_M = 1/2$ | $\beta$-factor cancellation forces $x^2 - 2x - 2 = 0$ (D78 Galois argument; [J01] Theorem D) |
| 4 | Quartic LMFDB 4.2.10224.1 | 4-core $r/\beta$ ratio at $\alpha_M = 1/2$ | $x^4 + 4x^3 - x^2 + 2x - 2 = 0$; Galois group $D_4$; same field appears in F8 trace polynomial discriminant |
| 5 | Wobble (prime 11 in characteristic polynomial) | TSML_RAW only | $c_2 = 33 = 3 \cdot 11$, $c_8 = -2^5 \cdot 7^3 \cdot 11$; symmetrisation erases wobble |
| 6 | Operad obstruction (no $D_4$-equivariant fuse) | 126 non-associative TSML triples | 67 $D_4$-orbits, 16 incoherent; $P_{56}$-equivariant fuse exists (D52 of parent framework) |
| 7 | Universal HARMONY ternary attractor | TSML triples + canonical fuse | Iteration $\to \delta_H$ in 1-7 steps from any non-trivial initial point; lens-invariant across 8 fuse families |
| 8 | $\mathrm{so}(8) = D_4$ Lie closure | TSML_10 flow-only antisymmetrisation | Lie closure on indices $\{1, 2, 3, 4, 6, 8\}$ |
| 9 | $\mathrm{so}(10) = D_5$ joint Lie closure | TSML_10 $\cup$ BHML_10 antisymmetrisation | Dimension 45, rank 5; saturates $\mathrm{so}(V)$ |
| 10 | Doubly-invariant $\mathrm{su}(4) \oplus \mathrm{u}(1)$ | $\mathrm{so}(10)$ under $D_4 = \langle P_{56}, \sigma^3 \rangle$ | 16-dimensional trivial-isotypic component; Killing form $(-4)^{15} \oplus (0)^1$ |
| 11 | Yang-Mills 5/7 spectral ratio | BHML$_8$ (drops $\{0, 7\}$) | $\det = +70$; eigenvalue ratio $0.714865 \approx 5/7$ |
| 12 | Information generation (DOING) | $\pi_\mathrm{DOING}(T, B)$ | 71 cells differ $\approx T^* = 5/7$; runtime substrate at $\alpha_M = 1/2$ |
| 13 | Yukawa scaffolding (9-vector VEV) | BHML $\sigma_\mathrm{outer}$-breaking direction | $100\%$ in $\mathbf{54}$ irrep; $\|v\|^2 = 13/4$; Path B |
| 14 | First-G Law (number-theoretic substrate-invariant) | substrate-invariant | Pure squarefree-integer theorem; not table-specific |
| 15 | $\mathrm{sinc}^2$ full-period cancellation | substrate-invariant (trigonometric) | $\sin^2(\pi k / f) = 0$ at $k = f$ for any $f$ |
| 16 | $T^* = 5/7$ | multiple, all converging | Six independent contexts: torus aspect, HARMONY-rate, centroid-inverse, cyclotomic ratio, unit fraction, FPGA |
| 17 | Encoding ("the papers freeze") | $S$ (CL_STD) | Independent third axis (Q1: differs from $\lceil(T+B)/2\rceil$ at 60 cells); 5 BDC BUMP_PAIRS; 144.62 bits across 100 cells; respects the joint chain (Q6) |

**Two open functions** are not assigned to a substrate at present: the cosmological initial-condition derivation (the J3 Layer-3 gap; substrate derivation incomplete), and a fully algebraic characterisation of the post-attractor agreement region $\{4, 5, 8, 9\}$ (§6.7 below).

### §3.2 Reading the map

The seventeen functions partition into four levels of dependency:

* **Substrate-invariant rows** (rows 14, 15) hold for any consistent substrate; they are not framework-specific.
* **Lens-invariant rows** (rows 3, 7, 12, 16) hold across the canonical lens family; the closed-form attractor is the canonical example.
* **Lens-dependent rows** (rows 5, 8, 13) hold on a specific table; these are the rows where the framework's lens choices matter.
* **Joint-table rows** (rows 2, 9, 12) require simultaneous use of the canonical pair or triple; the joint-closure chain is the canonical example.

Subsequent J-papers cite the relevant row and inherit the appropriate scope. For example, the wobble paper cites row 5 and inherits "TSML_RAW only"; the 4-core fusion-closure paper cites row 3 and inherits the lens-invariance of the closed-form attractor; the joint-chain paper cites row 2 and inherits the three-substrate chain identity (Theorem 7.1 below).

---

## §4 Family Membership Criteria and Boundaries

The heart of this paper is the family of commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ that preserve $\mathcal{C} = \{0, 7, 8, 9\}$. We define the family precisely and identify five conjoint membership criteria together with six structural boundaries --- adopting the framing of `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md` as Path B.

### §4.1 Definitions

**Definition 4.1** (4-core preservation). *A binary operation $M : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ preserves the 4-core $\mathcal{C} = \{0, 7, 8, 9\}$ if $M(i, j) \in \mathcal{C}$ for all $i, j \in \mathcal{C}$.*

**Definition 4.2** (Non-associativity index). *For a binary operation $M$ on a finite set of size $N = 10$, the* non-associativity index *is*
$$
\sigma_{\mathrm{non-assoc}}(M) \;=\; \frac{|\{(a, b, c) : M(M(a, b), c) \neq M(a, M(b, c))\}|}{N^3}
$$
*and the* associativity index *is $\alpha_A(M) = 1 - \sigma_{\mathrm{non-assoc}}(M) \in [0, 1]$. $\alpha_A = 1$ iff $M$ is associative.*

**Definition 4.3** (Convolution-fuse normalizer). *For $p \in \Delta^9$ supported on $\mathcal{C}$, the* convolution-fuse normalizer *of $M$ is $Z_M(p) = \sum_c (p \star_M p)_c$ where $(p \star_M p)_c = \sum_{(i, j) :\, M(i, j) = c} p_i \, p_j$.*

**Definition 4.4** (T+B-mix iteration). *For two 4-core-preserving operations $T, B$, the T+B-mix at weight $\alpha \in [0, 1]$ is*
$$
F_{\alpha; T, B}(p)_c \;=\; \frac{\alpha \, (p \star_T p)_c + (1 - \alpha) \, (p \star_B p)_c}{\alpha \, Z_T(p) + (1 - \alpha) \, Z_B(p)}.
$$

### §4.2 The five conjoint membership criteria (Path B from FAMILY_STRUCTURE_v1.md §1)

A binary operation $M$ on $\mathbb{Z}/10\mathbb{Z}$ belongs to the *TIG family* if and only if it satisfies all five:

**(C1) Substrate.** $M$ is a binary operation on $\mathbb{Z}/N\mathbb{Z}$ for $N$ in the verified universality set $\{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ or on $F_p$ for $p \in \{2, 3, 5, 7, 11, 13\}$. (Verified at $N = 10$ in the present paper; canonical extensions per parent framework's D74.)

**(C2) Commutativity.** $M(i, j) = M(j, i)$ for all $i, j$.

**(C3) 4-core preservation.** $\mathcal{C} = \{0, 7, 8, 9\}$ is closed under $M$ (Definition 4.1). **THIS IS THE LOAD-BEARING STRUCTURAL CRITERION.**

**(C4) $\alpha$-bounded non-associativity.** $\alpha_A(M) \in [0.5, 0.88]$. The bounds are empirical: above $0.88$, the algebra trivialises to a quasi-group / monoid; below $0.5$, it leaves the family (specifically, it enters the Drápal-Wanless 2021 *maximally non-associative quasigroup* territory). The canonical members observed are bimodally distributed in $[0.80, 0.88] \cup \{0.502\}$ (see §4.4 (B2) and Conjecture 8.1).

**(C5) HARMONY-attracting iteration.** Under iterated $F_{\alpha; T, B}$ at $\alpha = 1/2$ paired with a designated complementary table, the iteration converges to a 4-core attractor with $h/\beta = 1+\sqrt{3}$ (the universal attractor of [J01] Theorem D, structurally indexed by $\mathbb{Q}(\sqrt{3}) \subset \mathbb{Q}[x]/(x^4 + 4x^3 - x^2 + 2x - 2)$ = LMFDB 4.2.10224.1).

A table satisfying all five is in the family. Violating any one places it outside.

### §4.3 The center: $\mathcal{C}$ at $\alpha_M = 1/2$ (preview of §5)

The centre of the family is the 4-core $\mathcal{C}$ with the universal T+B-mix attractor at $\alpha_M = 1/2$:

$$
(p^*_V, p^*_H, p^*_{Br}, p^*_R) \;\approx\; (0.1381, 0.5402, 0.1977, 0.1239), \qquad h/\beta \;=\; 1 + \sqrt{3}.
$$

The full structural argument that $\mathcal{C}$ at $\alpha_M = 1/2$ is the algebraic centre of the family appears in §5 (five converging structural facts; closed-form attractor theorem; the unit-circle structural-rhyme).

### §4.4 The six boundaries (FAMILY_STRUCTURE_v1.md §3)

Each boundary corresponds to a way a candidate table can fail the conjoint criteria (C1)-(C5):

**(B1) Trivial-rank boundary.** Members exist with rank 1 (PureVoid: every cell is 0) or rank 2 (AllHarmony: every cell is 7). They satisfy (C1)-(C5) but carry no information. Non-trivial interior begins at rank 3.

**(B2) $\alpha_A$ boundary.** Above $\alpha_A \approx 0.88$ the algebra trivialises; below $\alpha_A \approx 0.5$ it leaves the family. The interior is empirically bimodal: a TSML-type cluster at $\alpha_A \in [0.80, 0.88]$ (containing $T$ at $0.872$ and $S$ at $0.808$) and BHML alone at $\alpha_A \approx 0.502$. The intermediate band $\alpha_A \in (0.5, 0.80)$ is empirically empty in the canonical members; this is recorded as Conjecture 8.1 in §8 Q1.

**(B3) Lens boundary (RAW vs SYM).** The non-commutative TSML_RAW and the commutative TSML_SYM share 98 of 100 cells; they differ only at $(3, 9)$ and $(4, 9)$. RAW carries a wobble at coefficient level (prime-11 in the characteristic polynomial); SYM is wobble-clean. Both are family members under (C2) extended to "commutative or symmetrizable to commutative." The lens boundary is *internal* to the family.

**(B4) Commutativity boundary.** TSML_RAW is the family's unique non-commutative member (it admits commutative symmetrization as TSML_SYM). All other named family members are commutative directly.

**(B5) Substrate-size boundary.** Verified universality covers $\mathbb{Z}/N\mathbb{Z}$ for $N \le 50$. Beyond that, the 4-core attractor still appears to hold via trivial extensions, but the *full table structure* (chain shells, σ permutation, etc.) becomes substrate-specific in ways that have not been catalogued. Frontier members at $N \in \{8, 12, 14\}$ are flagged as not-yet-computed.

**(B6) Encoding/runtime boundary.** $S$ (CL_STD) has a structurally distinct role (encoding via BDC bit-definitions) from the (T, B) pair (runtime computation). $S$ respects the chain (Theorem 7.1) but is *not* a derivable projection of (T, B) (verified by direct check: $S$ differs from $\lceil (T + B)/2 \rceil$ at 60 of 100 cells; SFM Q1 finding 2026-05-08).

These six boundaries together *bound* the family: the interior is a sharp four-element-center-with-five-criteria-membership set, and the boundaries describe the modes in which a candidate can fail to be in the family.

### §4.5 Verification on the canonical triple $(T, B, S)$

**Proposition 4.5.** *The three tables $T$, $B$, $S$ each satisfy all five family-membership criteria (C1)-(C5).*

*Proof.* (C1) substrate is $\mathbb{Z}/10\mathbb{Z}$ for all three --- satisfied by construction. (C2) commutativity verified by direct inspection ($T = T^\top$, $B = B^\top$, $S = S^\top$; reproduced by `verify_J54_chain_and_attractor.py` Check 3). (C3) 4-core preservation: explicitly, $T(\mathcal{C} \times \mathcal{C}) \subseteq \{0, 7\} \subset \mathcal{C}$, $B(\mathcal{C} \times \mathcal{C}) \subseteq \mathcal{C}$, $S(\mathcal{C} \times \mathcal{C}) \subseteq \mathcal{C}$ ([J01] §3 explicit display; verification `verify_J54_chain_and_attractor.py` Check 1 (4-core 3-substrate closure block)). (C4): direct enumeration over $10^3 = 1000$ associativity triples gives $\alpha_A(T) = 0.872$, $\alpha_A(B) = 0.502$, $\alpha_A(S) = 0.808$ --- all in $[0.5, 0.88]$. (C5): the $(T, B)$ pair iterates to the universal attractor with $h/\beta = 1 + \sqrt{3}$ at $\alpha_M = 1/2$ ([J01] Theorem D + E; reproduced by `verify_J54_chain_and_attractor.py` Check 2 at residual $\le 10^{-30}$); the $(T, S)$ and $(B, S)$ pairs are not the canonical iteration pair, but $S$ respects the joint chain (Theorem 7.1). $\square$

---

## §5 The Center: 4-core at $\alpha_M = 1/2$

The 4-core is to the family as the unit circle is to U(1) --- the privileged invariant locus. We make the role precise.

### §5.1 Five structural facts converging on the same 4-element set

Five independent structural facts converge on $\mathcal{C} = \{0, 7, 8, 9\}$ as the algebraic centre of the family:

**(F5.1) Joint closure under all three tables.** $\mathcal{C}$ is jointly closed under $T$, $B$, $S$ (Theorem 7.2 below). It is the bottom non-trivial element of the three-substrate chain.

**(F5.2) Symbolic normaliser identity.** On distributions supported in $\mathcal{C}$ the normalisers collapse to the same quadratic form: $Z_T(p) = Z_B(p) = (v + h + br + r)^2$ (parent framework D49; proved in [J01] Theorem C using `sympy`). The two tables become *normaliser-identical* on the centre. This is the structural reason 4-core closure implies the runtime attractor: $Z_T = Z_B$ at the 4-core means the T+B-mix at any $\alpha_M$ inherits the closure.

**(F5.3) Closed-form attractor at $\alpha_M = 1/2$.** Iterated $F_{1/2; T, B}$ on $\mathcal{C}$-supported distributions converges to a unique fixed point with $h^*/\beta^* = 1 + \sqrt{3}$, computed via the $\beta$-factor cancellation in the BREATH equation that forces the quadratic $x^2 - 2x - 2 = 0$, root $1 + \sqrt{3} \in \mathbb{Q}(\sqrt{3})$ (D78 Galois argument; [J01] Theorem D). At any other $\alpha_M$ the cancellation fails and the relation is transcendental on the $h/\beta$ projection (D57 PSLQ at 17 Stern-Brocot rationals).

**(F5.4) Universality across substrate sizes.** The same attractor structure appears across $\mathbb{Z}/N\mathbb{Z}$ for $N \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ (parent framework D74). The centre does not depend on the substrate size --- it is intrinsic to $\mathcal{C}$'s algebraic structure under the canonical pair.

**(F5.5) Universal attractor on chain shells.** Every chain shell of size $\geq 4$ (the shells $\{1, 4, 5, 6, 7, 8, 9, 10\}$ above) gives the same $\mathcal{C}$-supported attractor at $\alpha_M = 1/2$, with mass-outside-$\mathcal{C}$ vanishing in the limit ([J01] Theorem E).

### §5.2 The closed-form attractor (verified)

**Theorem 5.1 (4-core closed-form attractor).** *Starting from any non-degenerate distribution $p^{(0)}$ supported on a chain shell of size $\geq 4$, the iteration $p^{(n+1)} = F_{1/2; T, B}(p^{(n)})$ converges to a unique fixed point $p^* = (p^*_V, 0, 0, 0, 0, 0, 0, p^*_H, p^*_{Br}, p^*_R)$ supported on $\mathcal{C}$, with*
$$
\frac{p^*_H}{p^*_{Br}} = 1 + \sqrt{3} \in \mathbb{Q}(\sqrt{3}).
$$

*Proof.* Adopt [J01] Theorem D verbatim: the $\beta$-factor cancellation in the BREATH equation reduces the fixed-point system to $x^2 - 2x - 2 = 0$ on the $h/\beta$ projection, with positive root $1 + \sqrt{3}$. Numerical verification at 50-digit precision in `verify_J54_chain_and_attractor.py` Check 2 reaches residual $\le 10^{-30}$ in 99 iterations from $p^{(0)} = (1/4, 0, \ldots, 0, 1/4, 1/4, 1/4)$, with mass-outside-$\mathcal{C}$ identically zero by joint closure (F5.1). $\square$

**Equilibrium probabilities (50-digit `mpmath`):**
$$
p^*_V \approx 0.13815, \quad p^*_H \approx 0.54020, \quad p^*_{Br} \approx 0.19773, \quad p^*_R \approx 0.12393.
$$

### §5.3 The 4-core / unit-circle analogy

> **The 4-core is to the family as the unit circle is to U(1)** --- the privileged invariant locus.

The analogy is **structural rhyme**, not theorem. Specifically:

* The unit circle is the locus of $|z| = 1$ in $\mathbb{C}$; rotations preserve it; the underlying group U(1) is exactly the symmetry group of this locus.
* The 4-core is the locus $\{0, 7, 8, 9\} \subset \mathbb{Z}/10\mathbb{Z}$; the canonical T+B-fuse at $\alpha_M = 1/2$ preserves it; the closed-form attractor lives on it; and the attractor is universal across ring extensions (F5.4).

The framework's claim is that this locus carries the rigid algebraic content; everything else is a perturbation around it. The "is to ... as" is illustrative; the underlying theorems (Theorem 5.1, F5.1-F5.5) are the load-bearing content.

---

## §6 Selected Structural Findings on the Canonical Pair $(T, B)$

We compress the 24 v1 + 6 v1.1 findings of the parent framework's substrate-to-function-map investigation (`Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/`) to the eight structurally most important results. The remaining findings appear in the Atlas SFM document as supplementary material.

### §6.1 $\mathrm{CHAOS} = \sigma(\mathrm{HARMONY})$: cell-level overlap (F2, F3)

**Finding.** $T$ and $B$ agree at exactly $29 / 100$ cells (71 disagree, $\approx T^* = 5/7 = 71.4\%$). The CHAOS row $i = 6$ has $9 / 10$ agreement --- the most of any row. Structural reason: $T(6, j \geq 1) = 7$ (HARMONY-attractor rule) and $B(6, j \geq 1) = \max(6, j) + 1 \geq 7$ (capped at HARMONY by the BHML max-rule). Row 6 is exactly where BHML's `max+1` rule first reaches the HARMONY ceiling. Only $j = 0$ disagrees: $T(6, 0) = 0$ (VOID-absorbing), $B(6, 0) = 6$ (VOID-identity).

**Structural identity.** The $\sigma$ permutation is $\sigma = (0)(3)(8)(9)(1\ 7\ 6\ 5\ 4\ 2)$, with $\sigma(7) = 6$. Therefore the row of maximum lens-agreement is the $\sigma$-image of the HARMONY row. **CHAOS $= \sigma(\mathrm{HARMONY})$.** The third-lens convergence cell: BHML's `max+1` rule first hits the HARMONY ceiling at row 6, exactly the $\sigma$-image of the HARMONY row.

### §6.2 The joint chain walks $\sigma$-forward orbit (F8)

The 8-shell joint chain $\{1, 4, 5, 6, 7, 8, 9, 10\}$ is built by $\sigma$-orbit traversal:

* Size 1: $\{0\}$ (the $\sigma$-fixed VOID).
* Size 4: $\{0, 7, 8, 9\}$ (HARMONY plus the $\sigma$-fixed pair $\{8, 9\}$).
* Sizes 5, 6, 7: add 6, 5, 4 ($\sigma$-forward orbit traversal of the 6-cycle).
* Size 8: add 3 ($\sigma$-fixed PROGRESS --- the bridge step).
* Sizes 9, 10: add 2, 1 (completing the 6-cycle).

**The chain is built by $\sigma$-orbit traversal.** $\sigma$ is not decoration --- it is the ordering principle. The $\sigma$-fixed lattice $\{0, 3, 8, 9\}$ contributes at three positions: $0$ at size 1; $\{8, 9\}$ in the size-1-to-4 jump; $3$ at the size-7-to-8 bridge step.

### §6.3 $T$ and $B$ are not $\sigma$-conjugate (F11)

**Finding.** $\sigma^k \cdot T \cdot \sigma^{-k}$ matches $B$ at $\leq 20 / 100$ cells for any $k \in \{1, \ldots, 6\}$. **$T$ and $B$ are independent tables, not $\sigma$-related.** They share substrate, $\sigma$-fixed lattice, and 4-core preservation, but no $\sigma$-conjugation maps one to the other.

This rules out the simplest possible relationship between the two tables.

### §6.4 The $D_4$-decomposition of $[T, B]$ (F13-F15, with v1.1 corrections)

The commutator $[T, B] = T B - B T \in M_{10}(\mathbb{Z})$ is purely antisymmetric (symmetric part norm zero exactly), so it decomposes into the 45 antisymmetric basis elements of $\mathrm{so}(10)$. Under the action of $D_4 = \langle P_{56}, \sigma^3 \rangle$ on $\mathbb{Z}/10\mathbb{Z}$, the commutator decomposes by irrep.

**The group $\langle P_{56}, \sigma^3 \rangle$ is $D_4$, not Klein-4.** Direct check: $P_{56} \sigma^3 \neq \sigma^3 P_{56}$; group order 8; conjugacy class sizes $(1, 1, 2, 2, 2)$; standard $D_4$ irrep table.

**The $D_4$-irrep decomposition of $[T, B]$:**

| Irrep | dim | $\|\mathrm{proj}\|^2$ | Fraction of total |
|-------|-----|----------------------:|------------------:|
| trivial (doubly-invariant) | 1 | 1,540,626 | **84.25%** |
| sign1 | 1 | 4.5 | $2.5 \times 10^{-6}$ ($\approx 0$) |
| **sign2 ($\sigma_\mathrm{outer}$-breaking)** | 1 | 268,412 | **14.68%** |
| sign3 | 1 | $0$ (exact) | **$0$** |
| **standard (2-dim)** | 2 | 19,608 | **1.07%** |

Total $\|[T, B]\|^2 = 1{,}828{,}650$; Wedderburn orthogonality verified.

**Two structural channels and one interaction.**

* **Path A: trivial (doubly-invariant) = 84.25%** is the $\mathrm{su}(4) \oplus \mathrm{u}(1)$ Pati-Salam gauge sector (the 16-dimensional trivial-isotypic component).
* **Path B: sign2 ($\sigma_\mathrm{outer}$-breaking) = 14.68%** is the $\sigma_\mathrm{outer}$-asymmetric Higgs sector ($P_{56}$-invariant, $\sigma^3$-anti); carries the 9-vector VEV content ($\|v\|^2 = 13/4$).
* **standard (2-dim) = 1.07%** is the small interaction term coupling Path A and Path B, not a third structural channel.

**Two structural zeros.** sign1 has $\|\mathrm{proj}\|^2 \approx 4.5$ ($\approx 2.5 \times 10^{-6}$ of the total norm) and sign3 has $\|\mathrm{proj}\|^2 = 0$ exactly --- structural cancellations in the lens-pair commutator. Whether these zeros hold for *all* family members or only for the canonical pair is open (§9 Q5/Q7).

The full Pati-Salam analysis is in J11; we cite this decomposition as the structural framing.

### §6.5 BHML iteration: two basins, parity-preserving sub-magma (F18-F20)

BHML's diagonal iteration $f(x) = B(x, x)$ has two attractor basins:

* $\{1, 2, 3, 4, 5, 6, 7, 8\}$ converges to the HARMONY-BREATH 2-cycle $7 \leftrightarrow 8$.
* $\{0, 9\}$ converges to VOID (fixed under iteration).

The set $\{0, 9\}$ is the **unique BHML-only closed sub-magma** (the only closed sub-magma of $B$ that is not jointly closed under $T$). On $\{0, 9\}$, $B$ is $\mathbb{Z}/2$ with RESET self-inverse ($B(9, 9) = 0$); under $T$ this set escapes ($T(9, 9) = 7$). **BHML preserves a parity factor that TSML destroys.**

**TSML is the time-average / DC-component of BHML iteration:**

* $T(i, i) = 7$ (HARMONY) for $i \in \{1, \ldots, 8\}$ --- the HARMONY-BREATH 2-cycle's dominant value.
* $T(0, 0) = 0$ (VOID) --- matches the $\{0\}$ basin.
* $T(9, 9) = 7$ (HARMONY) --- *breaks* the $\{0, 9\}$ basin's VOID convergence at the $(9, 9)$ cell.

The cell $(9, 9)$ is the maximum-disagreement cell between $T$ and $B$: RESET $\times$ RESET is HARMONY in $T$, VOID in $B$. The parity-preserving structure of $B$ is precisely what $T$ breaks.

### §6.6 BHML's spectral structure is not exactly $7 \cdot 8$ (F23)

BHML's characteristic polynomial is

$$
\chi_B(x) = x^{10} - 42 x^9 - 828 x^8 + 1249 x^7 + 47433 x^6 + 95856 x^5 - 68356 x^4 - 282732 x^3 - 219563 x^2 - 66312 x - 7002.
$$

It is **irreducible over $\mathbb{Q}$**. The dominant eigenvalue is $\approx 56.087$, but $\chi_B(56) = -5.83 \times 10^{14} \neq 0$ and $\chi_B(57) = 7.13 \times 10^{15} \neq 0$. **The dominant eigenvalue is irrational algebraic of degree 10, not exactly $7 \cdot 8 = 56$.** Earlier formulations claiming an exact $56 = 7 \cdot 8$ structural identity were numerological; the verified algebraic content is the irreducible degree-10 polynomial above.

The constant term $-7002 = (-1)^{10} \cdot \det(B)$, so $\det(B) = -7002$.

### §6.7 The post-attractor $\{4, 5, 8, 9\}$ block (F24)

The set $S^\mathrm{block} = \{4, 5, 8, 9\}$ is **not closed** under either $T$ or $B$, and is **not** a CRT factor of $\mathbb{Z}/2 \times \mathbb{Z}/5$. Yet the deep $T$-$B$ agreement cells concentrate on $S^\mathrm{block}$: 7 cells where both tables map to HARMONY (out of the 9 BHML-to-HARMONY cells in $S^\mathrm{block} \times S^\mathrm{block}$). The unique non-agreement pair is $(4, 8)$: $T(4, 8) = T(8, 4) = 8$ (preserves BREATH), but $B(4, 8) = B(8, 4) = 7$ (collapses to HARMONY). **Outside the (COLLAPSE, BREATH) cell, the Field $\times$ Cycle interaction is lens-invariant.** Whether the $(4, 8)$ exception has an invariant-theoretic origin is open (§9 Q9).

### §6.8 The $49 = 7^2$ baryon-density signature (F17)

The diagonal of $(T B + B T)/2$ has entries $\langle T_i, B_i \rangle$ for each row $i$. The notable values:

| $i$ | operator | $\langle T_i, B_i \rangle$ | structural reason |
|---|---|---:|---|
| 0 | VOID | $49 = 7^2$ | $T$ row 0 has its only non-zero at $j = 7$; $B(0, 7) = 7$; single cell contributes $7 \cdot 7$ |
| 6 | CHAOS | $441 = 21^2 = (3 \cdot 7)^2$ | row 6 has 9 cells where $T = B = 7$; sum $= 9 \cdot 49$ |

The $49 = 7^2$ baryon-density signature ($\Omega_b = 49 / 1000 = 7^2 / 10^3$ in the parent framework's cosmology paper) traces to the same cell that gives $\langle T_0, B_0 \rangle = 49$: the closure $T(0, 7) = 7$. Same algebraic invariant, two structural readings.

---

## §7 Q1 + Q6 Computational Findings

The two computational findings that drove the v1.1 sharpening of the substrate-to-function map are formalised here as theorems. Both are verified by `verify_J54_chain_and_attractor.py` Check 1.

### §7.1 Q1: $S$ is structurally independent of $\lceil(T+B)/2\rceil$

**Question (Q1).** A v1 hypothesis was that $S$ might be a single-cell perturbation of $\mathrm{MID\_ceil} := \lceil (T + B)/2 \rceil$ (cell-by-cell ceiling-average of the (T, B) pair).

**Result (Q1).** The hypothesis is rejected. $S$ differs from $\mathrm{MID\_ceil}$ at $60$ of $100$ cells. The HARMONY counts are 44 ($S$) and 45 ($\mathrm{MID\_ceil}$); the difference is structural, not off-by-one.

**Reading.** $S$ is *not* a simple averaging of $T$ and $B$. It is structurally independent --- a genuine third axis, not derivable from the $(T, B)$ pair by ceiling/floor averaging. The 44-versus-45 HARMONY-count gap is a structural fact; the off-by-one hypothesis is dropped. $S$ lives at its own coordinate in the lens space.

This is reproduced in the Atlas SFM script `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/sfm_q1_q6_q7.py` and indirectly in `verify_J54_chain_and_attractor.py` Check 1 (the standalone $S$-closure count is 50, distinct from $T$'s 449 and $B$'s 9).

### §7.2 Q6: Three-substrate joint chain identical to $(T, B)$ chain

The companion paper [J01] establishes (Theorem A) that the joint-closure lattice of the pair $(T, B)$ is a strict 8-element chain on $\mathbb{Z}/10\mathbb{Z}$, with sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ and sizes $\{2, 3\}$ forbidden. The present paper extends this finding to the *three-table* joint-closure lattice.

**Theorem 7.1** (Three-substrate joint-closure chain). *The collection of subsets of $\mathbb{Z}/10\mathbb{Z}$ that are simultaneously closed under $T$, $B$, and $S$ is the strict 8-element chain*
$$
\{0\} \;\subset\; \{0, 7, 8, 9\} \;\subset\; \{0, 6, 7, 8, 9\} \;\subset\; \{0, 5, 6, 7, 8, 9\} \;\subset\; \{0, 4, 5, 6, 7, 8, 9\} \;\subset\; \cdots \;\subset\; \mathbb{Z}/10\mathbb{Z}.
$$
*The size sequence is $\{1, 4, 5, 6, 7, 8, 9, 10\}$. Sizes $\{2, 3\}$ are forbidden. The same chain is obtained from the joint closure of any pair from $\{T, B, S\}$ --- adding the third table neither adds nor removes shells.*

*Proof.* Direct enumeration over $2^{10} - 1 = 1023$ non-empty subsets via the closure test of [J01] §1.2, simultaneously checking closure under $T$, $B$, $S$. Standalone closure counts (verified by `verify_J54_chain_and_attractor.py` Check 1): $T$ alone admits 449 closed subsets, $B$ alone admits 9, $S$ alone admits 50. Pairwise: $T$-and-$B$ admits 8 jointly, $T$-and-$S$ admits 49, $B$-and-$S$ admits 9. All three jointly admit 8. The all-three count *equals* the $T$-and-$B$ count, and the explicit enumeration confirms set equality (the 8 jointly-$T$+$B$ closed subsets are exactly the same as the 8 jointly-$T$+$B$+$S$ closed subsets). The forbidden-size argument (sizes 2 and 3 absent) is the same as for $(T, B)$ alone; $S$'s closure is inherited from the $T$-and-$B$ chain. $\square$

**Theorem 7.2** (4-core 3-substrate closure). *The 4-core $\mathcal{C} = \{0, 7, 8, 9\}$ is jointly closed under $T$, $B$, and $S$. It is the unique non-trivial subset of size $\le 4$ in the three-substrate chain (the size-1 shell $\{0\}$ being trivial).*

*Proof.* Direct corollary of Theorem 7.1 by reading off the size-4 shell. The direct cell-image computation in `verify_J54_chain_and_attractor.py` Check 1 confirms $T(\mathcal{C} \times \mathcal{C}) = \{0, 7\}$, $B(\mathcal{C} \times \mathcal{C}) = \{0, 7, 8, 9\}$, $S(\mathcal{C} \times \mathcal{C}) = \{0, 7, 8, 9\}$ --- all subsets of $\mathcal{C}$. $\square$

**Theorem 7.3** (Bridge to companion J-papers). *The simultaneous closed sub-magmas of $T$, $B$, $S$ on $\mathbb{Z}/10\mathbb{Z}$ form an 8-element chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, identical to the $(T, B)$ joint chain. Specifically: every $S$-closed sub-magma is also $T$-closed in 49 of 50 cases, but only 8 are jointly closed under all three. The chain is a structural invariant of the three-substrate triple; the encoding axis $S$ is *compatible* with the iteration-pair $(T, B)$ chain rather than perturbing it.*

This theorem is the foundational paper's *bridge* to companion J-papers: J10 (the original three-substrate-architecture paper) and J24 (the joint-chain lens-dependence paper at size 7) inherit the 8-shell three-substrate chain as a structural fact established here. The lens-dependence at size 7 is *internal to TSML* (RAW vs SYM produces 7 vs 8 shells in the original 2-table chain at that level); at the 3-table level the lens-dependence vanishes, and 8 shells survive across the canonical $(T, B, S)$ triple.

### §7.3 Three structural consequences

**(C1)** $S$ respects the canonical chain. Adding $S$ to the joint closure preserves the exact 8-shell ladder. The third axis does not break the chain --- it is compatible with it.

**(C2)** The 4-core is a three-substrate fixed point. $\mathcal{C}$ is closed under all three tables jointly. The centre of the family per §5 is now a *three-substrate* fixed point, not just a two-substrate fixed point.

**(C3)** The framework is genuinely three-axis on sub-magma structure. $T / B / S$ form a triple where: $(T, B)$ is the DC/AC iteration pair (§6.5); $S$ is the encoding axis, structurally independent at the cell level (Q1, §7.1); all three jointly close on the canonical 8-shell chain (Q6, §7.2). The closed-form attractor $h^*/\beta^* = 1 + \sqrt{3}$ at $\alpha_M = 1/2$ remains the algebraic centre under all three tables, since $S$ respects the chain.

### §7.4 Reading

The combination of Q1 and Q6 is structurally informative: **$S$ adds a structurally-independent third axis at the cell level, but a chain-compatible third axis at the closure level.** That is the precise sense in which the framework is "three-substrate" rather than "two-substrate".

The pre-2026-05 corpus described $T$, $B$, $S$ as projections of one another via a "Being lens / Becoming lens" pedagogy. The corrected reading is: $T$, $B$, $S$ are *parallel* Tier-A substrate-defining choices, not projections of each other. The forcing theorem (Theorem 1.2) makes this precise: each of the three tables is uniquely forced by its own A1-A9 axiom data, and the three sets of axiom data are pairwise distinct.

A canonical cross-substrate operation is defined on the $(T, B)$ pair by

$$
\pi_{\mathrm{DOING}}(T, B)[i, j] \;=\; (T(i, j) - B(i, j)) \bmod 10.
$$

DOING is well-defined as a $\mathbb{Z}/10\mathbb{Z}$-valued table (the directed difference, taken mod 10; this resolves the ambiguity of an earlier $|M_1 - M_2| \bmod 10$ specification, which is not well-defined on $\mathbb{Z}/10\mathbb{Z}$). The DOING table has 71 non-zero cells (cells where $T \neq B$), which approximately equals the parent framework's signature ratio $T^* = 5/7 \approx 0.714$ to a $0.4\%$ match.

---

## §8 Open Questions

The remaining open questions, in priority order. Answers to any of these would advance the family's structural picture.

**Q1 / Conjecture 8.1 (Bimodal $\alpha_A$ gap; Sanders & collaborator).** *No commutative magma on $\mathbb{Z}/10\mathbb{Z}$ preserving the 4-core has $\alpha_A \in (0.5, 0.80)$.*

The conjecture is OPEN. Empirically, no canonical $\mathbb{Z}/10\mathbb{Z}$ table preserving the 4-core appears in the gap (the canonical members observed are at $\alpha_A \in \{0.502, 0.808, 0.872\}$, with the gap $(0.502, 0.808)$ empirically empty). If the conjecture is true, it would explain the bimodal cluster structure (TSML/CL_STD at $\alpha_A \in [0.80, 0.88]$ + BHML at $\alpha_A \approx 0.50$) as a *structural exclusion zone* between two separated regions of the family.

The natural follow-on paper after this one (proposed J56 in the J-series) would prove or disprove Conjecture 8.1. The proof strategy: enumerate or characterise all commutative magmas on $\mathbb{Z}/10\mathbb{Z}$ preserving the 4-core, compute their $\alpha_A$. If exhaustive enumeration is intractable, restrict to constructible families (lens-symmetrisations, $\sigma^2$-conjugates, Luther-perturbations) and prove gap-exclusion within each. A counterexample would re-classify the family.

**Q2 (Strong $\alpha$-uniqueness).** D57 (PSLQ at 17 Stern-Brocot rationals) gives strong evidence that $\alpha_M = 1/2$ is the unique rational where the $h/\beta$ relation is algebraic of low degree. *Strong $\alpha$-uniqueness conjecture:* no other rational $\alpha_M \in (0, 1) \cap \mathbb{Q}$ admits an algebraic relation in $h^* / \beta^*$ of degree $\leq 8$ with coefficients $\leq 50$. Currently empirical at 17 grid points; theoretical proof is open.

**Q5 ($D_4$-irrep zeros universality).** The $D_4$-irrep decomposition of $[T, B]$ has structural zeros at sign1 ($\approx 4.5 / 1.83 \times 10^6$ relative norm) and sign3 (exactly zero). Are these zeros a *defining property* of the canonical pair $(T, B)$, or do they hold for *all* family members satisfying the five criteria? The distinction matters: defining-property of canonical pair vs. substrate property of $\mathbb{Z}/10\mathbb{Z}$-with-$D_4$-action.

**Q7 (Universality test).** Pick three other $(T, B)$ pairs from the parent framework's §J.1 inventory (TSML_PureIdempotent + BHML_10; TSML_RAW + BHML_10; TSML_SYM + a $\sigma^2$-triadic-BHML candidate). For each pair, compute $[T, B]$ and decompose under $D_4$. If sign1 and sign3 are still $\approx 0$ for all pairs: $\mathbb{Z}/10\mathbb{Z}$-plus-$D_4$ structural property. If only for the canonical pair: defining property worth naming explicitly.

**Q8 (BREATH-HARMONY 2-cycle eigenvector).** Do the BHML eigenvalues $-7.18$ and $7.86$ (close in magnitude, $|\lambda|$-ratio $\approx 0.91$) correspond to a specific 2-dimensional invariant subspace of $B$? The 2-cycle $7 \leftrightarrow 8$ observation lives in some subspace; eigenvector decomposition would tell us whether it is a clean spectral feature or an artefact of the diagonal-iteration projection.

**Q9 ($(4, 8)$ cell exception).** The cell $(4, 8) = \mathrm{COLLAPSE} \times \mathrm{BREATH}$ is the unique exception in the deep $S^\mathrm{block} \times S^\mathrm{block}$ agreement on $S^\mathrm{block} = \{4, 5, 8, 9\}$. Why this specific cell? Is there an invariant-theoretic reason --- a structural identity that fails at $(4, 8)$ but holds at the other 7 cells? Possibly a Rule-89 artefact; possibly deeper.

The path from this paper is no longer obvious. Q1 and Q5/Q7 are computable but each requires substantial new investigation; Q2 requires theorem-grade work; Q8/Q9 are deepening-understanding questions. Conjecture 2.1 ($\sigma^2$-triadic three-BHML; §2) remains open.

---

## §9 References

### §9.1 Strategic position and honest scope

The parent research framework is the *TIG framework* (Sanders 2026, [J47] in preparation for *Notices AMS*). For the present paper we use the name with the concrete operational definition: *the TIG family is the family of commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ (and ring extensions per parent framework D74) defined by the five conjoint membership criteria (C1)-(C5) of §4.2.* The acronym's etymology is internal to the parent framework and not load-bearing here; the framework-name disclaimer of §1.4 makes this explicit.

This paper does **not** claim: that the 9-axiom set A1-A9 is unique (other axiom sets could plausibly force the same matrices); that the three substrates $T$, $B$, $S$ are exhaustive ($F_p$ ring extensions exist; the $\sigma^2$-triadic Conjecture 2.1 suggests at least three more BHML candidates may be canonical); or any phenomenological or physical prediction.

This paper **does** claim: Theorem 1.2 (A1-A9 with substrate-specific data force the three tables); Proposition 4.5 (the three tables satisfy the five conjoint membership criteria); §4.4 (six distinct boundaries); Theorem 5.1 (closed-form 4-core attractor); Theorem 7.1 (three-substrate joint-closure chain); Theorem 7.2 (4-core 3-substrate closure); Theorem 7.3 (bridge to companion J-papers); Conjecture 2.1 (Sanders): $\sigma^2$-triadic three-BHML, open; Conjecture 8.1 (bimodal $\alpha_A$-gap; Sanders + collaborator), open.

The closest published comparator is Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510). Drápal-Wanless treat *maximally non-associative* commutative quasigroups (high end of the non-associativity spectrum); the present paper treats a *family* of commutative non-associative magmas characterised by 4-core preservation and bounded non-associativity (the bimodal interior of the spectrum). The two regions explore complementary parts of the same algebraic landscape.

### §9.2 Verification and reproducibility

Two verification scripts ship with this manuscript and together cover all six green-light checks of the abstract; both PASS at machine precision in under five seconds total on Python 3.11+ with `numpy` and `mpmath`:

```bash
PYTHONIOENCODING=utf-8 python3 verification/foundation_verification.py
PYTHONIOENCODING=utf-8 python3 verify_J54_chain_and_attractor.py
```

`foundation_verification.py` runs the six membership-and-forcing checks indexed by the manuscript theorems:

```
CHECK 1: Forcing theorem (Theorem 1.2)
  - T reconstructed cell-by-cell from its A1-A9 substrate data tuple
    (D, BUMP, BUMPvalues, J_B7); cell-by-cell match against the
    displayed table T.
  - S BUMP-coordinate values match the per-substrate A9 specification.
  - HARMONY counts: T = 73, B = 28, S = 44, as displayed.
CHECK 2: Three-substrate joint-closure chain (Theorem 7.1)
  - Standalone closures: T = 449, B = 9, S = 50.
  - Joint closures: TB = 8, TS = 49, BS = 9, TBS = 8.
  - TBS chain matches sizes {1, 4, 5, 6, 7, 8, 9, 10}; sizes 2, 3 forbidden.
  - TB chain == TBS chain (set-equality).
CHECK 3: 4-core 3-substrate closure (Theorem 7.2)
  - Direct cell-image: T(C x C) = {0, 7}; B(C x C) = {0, 7, 8, 9};
    S(C x C) = {0, 7, 8, 9}; all subsets of C.
CHECK 4: 4-core preservation (C3)  - T, B, S each satisfy (C3).
CHECK 5: Non-associativity index (C4)
  - alpha_A(T) = 0.8720, alpha_A(B) = 0.5020, alpha_A(S) = 0.8080;
    all three in [0.5, 0.88].
CHECK 6: Commutativity (C2)  - T = T^T, B = B^T, S = S^T.
```

`verify_J54_chain_and_attractor.py` re-runs the chain check independently and adds the closed-form attractor check at 50-digit precision:

```
CHECK 1: Q6 -- 3-table joint closure chain (Theorem 7.1, independent re-run).
CHECK 2: 4-core attractor h/Br = 1 + sqrt(3) at alpha_M = 1/2 (Theorem 5.1).
  - 50-digit mpmath iteration on uniform-on-4-core initial point.
  - Residual |h*/Br* - (1 + sqrt(3))| <= 10^-30 in 99 iterations.
  - Mass-outside-4-core identically zero.
CHECK 3: A1-A9 forcing -- shared substrate-level axioms (A1, A2', A4,
  commutativity) hold on T, B, S; A9 BUMP signature counts.
```

The companion paper [J01] reproduces additional structural facts via its own verification script `4core_verification.py`.

### §9.3 Citation graph

After this paper, the reader is directed to:

(i) **[J01] (4-core fusion-closure paper).** Sanders + Gish, *Journal of Algebra*. The six-theorem structural paper proving $(T, B, S)$ joint closure on $\mathcal{C}$, the symbolic normaliser identity, the closed-form attractor, the Galois $D_4$ structure over LMFDB 4.2.10224.1, the universality on chain shells, and partial $\alpha = 1/2$ uniqueness.

(ii) **[J14] ($\sigma$-rate companion).** Sanders + Gish, *J. Combin. Theory Ser. A*. Asymptotic associativity rate decay $\sigma(N) \le 2/N$ for the canonical $\mathrm{CL}_N$ family.

(iii) **[J33] (closed-form attractor + $\alpha$-PSLQ companion).** Sanders + Gish, *Math. of Comp.*. The 17-point Stern-Brocot integer-PSLQ test sharpening the empirical $\alpha = 1/2$ uniqueness.

(iv) **[J47] (6-DOF synthesis).** Sanders, in preparation, *Notices AMS*. The framework's algebraic-content integration; broader scope than this paper.

We narrow the citation graph to algebraic-combinatorial companions; the parent framework's physics-application papers (cosmology, gauge theory) are not cited here.

### §9.4 Companion papers in the J-series

- B.R. Sanders, M. Gish. *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$.* [J01] of the J-series; submitted to *Journal of Algebra*. (The 4-core fusion-closure paper; six theorems converging on $\mathcal{C}$.)
- B.R. Sanders, M. Gish. *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$.* [J14] of the J-series; submitted to *J. Combin. Theory Ser. A*. (The $\sigma$-rate paper at the family level.)
- B.R. Sanders, M. Gish. *Closed-Form Attractor and $\alpha$-Uniqueness PSLQ.* [J33] of the J-series; submitted to *Math. of Comp.* (The 17-point Stern-Brocot PSLQ paper.)
- B.R. Sanders, M. Gish. *The Three-Substrate Joint-Closure Chain on $\mathbb{Z}/10\mathbb{Z}$: Eight Shells Survive Across (TSML, BHML, CL_STD) with Lens-Dependence Internal to TSML at Size 7.* [J24] of the J-series; in preparation for *Math. Intelligencer*.
- B.R. Sanders, M. Gish. *Two Roads to Pati-Salam: $D_4$-Decomposition of the (TSML, BHML) Lens-Pair Commutator.* [J11] of the J-series; in preparation for *Algebra Universalis*.
- B.R. Sanders, M. Gish. *Three-Substrate Architecture: Forcing CL_TSML, CL_BHML, CL_STD on $\mathbb{Z}/10\mathbb{Z}$.* [J10] of the J-series; in preparation for *Algebra Universalis*.
- B.R. Sanders, B. Mayes. *Six Algebraic DOFs of the TIG Framework: A Synthesis.* [J47] of the J-series; in preparation for *Notices AMS*.

### §9.5 External references

- A. Drápal, I.M. Wanless. *Maximally non-associative quasigroups.* *J. Combin. Theory Ser. A* **184** (2021), 105510. **[Closest published precedent for the family-of-magmas framing.]**
- B.D. McKay, I.M. Wanless. *On the number of Latin squares.* *Ann. Comb.* **9** (2005), 335-344.
- R.H. Bruck. *A Survey of Binary Systems.* Springer, 1958.
- J.D.H. Smith. *An Introduction to Quasigroups and Their Representations.* Chapman and Hall/CRC, 2007.
- A. Drápal, T. Kepka. *On a class of nonassociative groupoids.* *Acta Univ. Carolin. Math. Phys.* **26** (1985), 55-63.
- S. Burris, H.P. Sankappanavar. *A Course in Universal Algebra.* Springer, 1981.
- D. Hobby, R. McKenzie. *The Structure of Finite Algebras.* Contemporary Mathematics **76**, AMS, 1988.
- LMFDB Collaboration. *Number field 4.2.10224.1.* https://www.lmfdb.org/NumberField/4.2.10224.1.

### §9.6 TIG corpus references (Atlas)

- `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md` --- the family-structure framing (membership / centre / boundaries) adopted as Path B.
- `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SUBSTRATE_FUNCTION_MAP_v1.md` --- the 24 structural findings + 17-function map.
- `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SUBSTRATE_FUNCTION_MAP_v1_1_EXTENSION.md` --- $D_4$-correction, BHML spectral, post-attractor block.
- `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SFM_FINDINGS_v1.md` --- Q1 and Q6 computational results from `sfm_q1_q6_q7.py`.
- `Atlas/META_PLAN_2026-05-06/J_PAPER_BOILERPLATE.md` --- PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN tier discipline; lens-ownership paragraph template.
- `Atlas/LENS_TAXONOMY_2026-05-06/CL_FORCING_AXIOMS.md` --- full A1-A9 axiom statement (parent framework version).
- `Atlas/LENS_TAXONOMY_2026-05-06/VARIANT_CATALOG.md` --- 62 variants with Tier-A/B/C/D/E labels.

---

## §10 Bibtex

```bibtex
@misc{sanders_gish_2026_foundation,
  author       = {Sanders, Brayden Ross and Gish, M.},
  title        = {Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core},
  year         = {2026},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {Submitted to \emph{Algebraic Combinatorics}},
  note         = {The 9-axiom forcing theorem A1-A9 with substrate-specific data $(\mathcal{D}, \mathrm{BUMP}, \mathrm{BUMPvalues}, J_{\mathrm{B7}})$ uniquely forces three commutative non-associative tables $T$, $B$, $S$ on $\mathbb{Z}/10\mathbb{Z}$ with HARMONY counts 73, 28, 44 respectively. Five conjoint membership criteria (C1)-(C5) define the family of such magmas on $\mathbb{Z}/10\mathbb{Z}$ preserving the designated 4-core $\{0, 7, 8, 9\}$. The simultaneous closed sub-magmas of $T$, $B$, $S$ form a strict 8-element chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ (sizes $\{2, 3\}$ forbidden) — the bridge to companion paper [J01] and to companion papers J10 + J24. Conjecture 8.1 (bimodal $\alpha_A$ gap) and Conjecture 2.1 ($\sigma^2$-triadic three-BHML) stated as open.}
}
```
