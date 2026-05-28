# Q17-B Clay Bridge: A Finite Gauss Sum (Trajectory Coherence Integral) and the Symbolic Return Theorem on $\mathbb{Z}/10\mathbb{Z}$

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher

**Target venue:** *L'Enseignement Mathématique*
**Manuscript class:** Structural / pedagogical bridge (not a Millennium-Problem proof)
**MSC 2020:** 11M99 (zeta and L-functions, miscellaneous), 11T22 (cyclotomy), 20B25 (permutation groups), 11C99 (number theory misc.)
**Date:** 2026-09-03 (Phase 5)
**WP source:** Q17 bundle (`papers/Q17_*.md` — six papers)

---

## Abstract

The TIG framework on $\mathbb{Z}/10\mathbb{Z}$ produces, in its spectral layer ($G_6$–$G_8$ results consolidated in [J51]), a **finite Gauss sum** (which we call the **trajectory coherence integral**) $G(s)$ — a 9-term discrete Fourier coefficient of a $\{-1, 0, +1\}$-valued function $\chi$ along the σ-orbit, weighted by a primitive 9th root of unity $\omega = e^{2\pi i / 9}$. (The object is structurally a finite character sum; per Remark 4.4 we drop the misleading "finite $L$-function" label used in earlier corpus material — there is no analytic continuation, no Euler product, only 9 terms.) This object takes exactly three values across the substrate's 10 operators: zero at the four anchors $\{0, 3, 8, 9\}$, $G_\mathrm{low} \approx 1.872$ on the σ³-orbits $\{1, 5\} \cup \{2, 6\}$, and $G_\mathrm{high} \approx 9.389$ on the σ³-orbit $\{4, 7\}$. The associated **Symbolic Return Theorem** (a direct consequence of $\sigma^6 = \mathrm{id}$, [J51]) establishes that every cycle-element trajectory $s_n = \sigma^n(s_0)$ returns to $s_0$ in 6 steps; every anchor is fixed.

This paper is the **Q17-B Clay bridge**: the structural connection between the finite $G(s)$ and the analytic structure that the Riemann Hypothesis demands of $\zeta(s)$. We do not prove RH; we make precise the sense in which the 6-layer Q-series architecture is a **finite, completely characterized model** of the same structural phenomena RH describes in an infinite setting. The model is an instance; the Millennium Problem asks whether instances can be infinite.

The contribution is in three theorems:

1. **Finite Gauss-Sum Theorem (Trajectory Coherence Integral).** $G(s)$ is a finite character sum (a discrete Fourier coefficient of $\chi$ at frequency $1/9$) along the 9-step $\sigma$-orbit, with explicit three-valued image. We adopt the name *trajectory coherence integral* throughout; the colloquial "finite $L$-function" language used in earlier corpus material is misleading (no analytic continuation, no Euler product) and is dropped — see Remark 4.4.
2. **Symbolic Return Theorem (Q17-A → Q17-B).** Every $\sigma$-orbit on the 6-cycle returns at step 6; every anchor is $\sigma$-fixed; VOID is avoided whenever $s_0 \neq 0$. This is the algebraic kernel underlying Q17.C2's Navier-Stokes target.
3. **Bridge Statement (Q17-B).** The three-valued structure of $G(s)$ — zero at anchors, $G_\mathrm{low}$ on most cycle elements, $G_\mathrm{high}$ on the σ³-orbit $\{4, 7\}$ — *rhymes* with the structure RH requires of $\zeta(s)$: zeros in predictable locations with spectral concentration at the critical line. The rhyme is at the level of structural vocabulary, not function-field analogue (Weil-Deligne); we make the boundary between the finite analogue and the infinite problem explicit.

This paper is the natural sequel to **[J29]** (Q17-A: 5D Force Vector as CRT Fourier Embedding), the proved-algebra companion in the Q17 program, and a co-citing companion to **[J51]** (G6+G7+G8 spectral consolidation).

**Lens and substrate.** This paper works on $\mathbb{Z}/10\mathbb{Z}$ with the canonical $\sigma$-permutation $\sigma = (1\;7\;6\;5\;4\;2)(0)(3)(8)(9)$ and the $\beta$-exception character $\chi$ defined in §3. These choices reflect the structural reading of the substrate developed in the broader Q-series corpus and the [J29] (Q17-A) proved-algebra companion; they are not derived from first principles. The theorems below are theorems on this specific (substrate, $\sigma$, $\chi$) triple. The bridge claim of §5 is explicitly a *structural rhyme* — a vocabulary correspondence between this finite setting and the analytic structure of $\zeta(s)$ — not a function-field analogue.

---

## §1 The Q17 program in context

The Q-series builds, in six layers, a structural characterization of the $\sigma$-permutation on $\mathbb{Z}/10\mathbb{Z}$ and its companion gate score:

* **Layer 1 (polynomial).** $\sigma^6 = \mathrm{id}$ on all of $\mathbb{Z}/10\mathbb{Z}$. Proved by direct polynomial check ($G_6$, [J51]).
* **Layer 2 (braid).** The conjugacy class of $\sigma$ in $S_{10}$ is determined by its cycle type $(6, 1, 1, 1, 1)$. Trivial.
* **Layer 3 (period).** The period distribution on $\mathbb{Z}/10\mathbb{Z}$ is bimodal: $P(\tau = 1) = 2/5$ (anchors) and $P(\tau = 6) = 3/5$ (cycle elements). Mean $\tau = 4$; variance 6 ($G_7$, [J51]).
* **Layer 4 (spectral).** The trajectory coherence integral $G(s) = |\sum_{j=0}^{8} \omega^j \chi(\sigma^j(s))|^2$ is three-valued ($G_8$, [J51]).
* **Layer 5 (optimal table).** TSML and BHML are the two canonical $10 \times 10$ tables on $\mathbb{Z}/10\mathbb{Z}$ with maximal HARMONY counts (73 and 28).
* **Layer 6 (search dynamics).** The runtime processor's 4-core attractor at $\alpha = 1/2$ ([J41], LMFDB 4.2.10224.1).

Q17 is the program that asks: **what is the analytic content of the spectral layer (Layer 4)?** The answer, developed across `Q17_CLAY_SPECTRAL_BRIDGE.md`, `Q17_FINITE_L_FUNCTION_NOTE.md`, `Q17_SYMBOLIC_RETURN_THEOREM.md`, `Q17_NS_TARGET_REFORMULATION.md`, `Q17_5D_RIGOROUS.md`, and `Q17_C2_FORMAL_STATEMENT.md`, is:

* **Q17-A.** The proved algebra — 5D Fourier embedding of $\mathbb{Z}/10\mathbb{Z}$ into $\mathbb{R}^5$ via CRT (Tier-A, [J29]).
* **Q17-B.** The bridge — the finite $L$-function and Symbolic Return Theorem (Tier-B, **this paper**).
* **Q17-C.** The conjectured physics — the Navier-Stokes target reformulation (Tier-D / open).

This paper is Q17-B in isolation: the finite-Gauss-sum / trajectory-coherence content and Symbolic-Return content, proved fully, scoped honestly, and connected to the Clay-RH structural picture *without* claiming any portion of RH itself.

---

## §2 The Symbolic Return Theorem

**Setup.** Let $G = (\mathbb{Z}/10\mathbb{Z}, \sigma)$ where $\sigma = (1\;7\;6\;5\;4\;2)(0)(3)(8)(9)$. From Layer 1: $\sigma^6 = \mathrm{id}$.

**Theorem 2.1 (Symbolic Return).** *Let $\{s_n\}_{n \geq 0}$ be any sequence in $\mathbb{Z}/10\mathbb{Z}$ satisfying $s_{n+1} = \sigma(s_n)$. Then:*

1. **Periodic return on the 6-cycle.** *For any $s_0 \in \{1, 2, 4, 5, 6, 7\}$:* $s_{n+6} = s_n$ *for all $n \geq 0$.*
2. **Fixed behavior at anchors.** *For any $s_0 \in \{0, 3, 8, 9\}$:* $s_n = s_0$ *for all $n \geq 0$.*
3. **VOID avoidance.** *If $s_0 \neq 0$, then $s_n \neq 0$ for all $n \geq 0$.*

*Proof.*

(1) For $s_0$ in the 6-cycle, $\sigma^6(s_0) = s_0$ by Layer 1, so $s_{n+6} = \sigma^{n+6}(s_0) = \sigma^n(\sigma^6(s_0)) = \sigma^n(s_0) = s_n$. $\square$

(2) For $s_0 \in \{0, 3, 8, 9\}$, $\sigma(s_0) = s_0$, so $s_n = s_0$ by induction. $\square$

(3) The orbit of $s_0$ under $\sigma$ is either the 6-cycle (if $s_0 \in \{1, 2, 4, 5, 6, 7\}$) or $\{s_0\}$ (if $s_0$ is an anchor with $s_0 \neq 0$). In both cases, $0 \notin \mathrm{orbit}(s_0)$. $\square$

**Corollary 2.2 (Identical to Q17-A in the proved-algebra register).** The Symbolic Return Theorem is a direct consequence of $G_6$ ($\sigma^6 = \mathrm{id}$). It is **Tier-A** (proved, lens-invariant, no choice of TSML lens or runtime parameter required).

---

## §3 The character $\chi$ and the conductor

**Definition 3.1.** The finite character $\chi : \mathbb{Z}/10\mathbb{Z} \to \{-1, 0, +1\}$ is:

* $\chi(s) = +1$ for $s \in \{1, 4\}$ — the $\beta$-exception pair (states where the gate score matches $T^* = 5/7$ exactly).
* $\chi(s) = -1$ for $s \in \{2, 5, 6, 7\}$ — the $\alpha = 1$ flip nodes (states where the gate score equals 1 exactly).
* $\chi(s) = 0$ for $s \in \{0, 3, 8, 9\}$ — the anchors.

**Total sum.** $\sum_{s \in \mathbb{Z}/10\mathbb{Z}} \chi(s) = (+1+1) + (-1-1-1-1) + 0 = -2$. The non-zero sum reflects the asymmetry between $\beta$-exceptions and flip nodes. (The character is *not* a multiplicative Dirichlet character on a unit group; it is a function on a permutation orbit.)

**Conductor.** The relevant algebraic structure is the cyclic group $\mathbb{Z}/6\mathbb{Z}$ generated by $\sigma$ on the 6-cycle. The DFT period is **9** (not 6): the sum $G(s)$ runs over 9 steps, $j = 0, \ldots, 8$, which wraps the 6-cycle once with 3 overlap steps. The "9" is the conductor in the informal $G_8$ sense: the period of the DFT basis.

---

## §4 The trajectory coherence integral $G(s)$ (a finite Gauss sum)

**Definition 4.1.** For each $s \in \mathbb{Z}/10\mathbb{Z}$:

$$
G(s) \;=\; \left|\sum_{j=0}^{8} \omega^j\, \chi\bigl(\sigma^j(s)\bigr)\right|^2, \qquad \omega = e^{2\pi i / 9}.
$$

**Theorem 4.2 (Three-Valued Trajectory Coherence Integral).** *$G(s)$ takes exactly three values on $\mathbb{Z}/10\mathbb{Z}$:*

| State $s$ | $G(s)$ | Algebraic role |
|-----------|--------|----------------|
| $\{0, 3, 8, 9\}$ (anchors) | $0$ exactly | $\chi(s) = 0$ and $\sigma^j(s) = s$ for all $j$, so the sum is identically zero. |
| $\{1, 2, 5, 6\}$ ($\sigma^3$-orbits $\{1,5\} \cup \{2,6\}$) | $G_\mathrm{low} \approx 1.872$ | Interleaved $\chi$-content along the 6-cycle; partial cancellation under $\omega^j$ weights. |
| $\{4, 7\}$ ($\sigma^3$-orbit) | $G_\mathrm{high} \approx 9.389$ | Imbalanced $\chi$-content in the orbit's first three positions ($\nu_+(s_0) \in \{0, 2\}$ rather than $\nu_+ = 1$); constructive interference under $\omega^j$ weights. |

*Proof sketch.* (i) Anchors contribute zero by direct computation: $\chi(s) = 0$ and $\sigma^j(s) = s$, so every term in the sum vanishes.

(ii)–(iii) For 6-cycle elements, the orbit visits all six elements of $\{1, 2, 4, 5, 6, 7\}$ in $j = 0, \ldots, 5$, then re-visits $s_0, s_1, s_2$ at $j = 6, 7, 8$ (since $\sigma^6 = \mathrm{id}$). Hence the 9-step character content depends on the $\chi$-values at the *first three* orbit positions.

The pairwise equalities $G(1) = G(5)$, $G(2) = G(6)$, $G(4) = G(7)$ follow from the σ³-action: σ³ has order 2 on the 6-cycle, partitioning $\{1, 2, 4, 5, 6, 7\}$ into the three 2-cycles $\{1, 5\}$, $\{2, 6\}$, $\{4, 7\}$. For any 6-cycle element $s$, the orbit at $\sigma^3(s)$ is the same six-element cycle traversed with a 3-step offset; combined with $\omega^9 = 1$ and 6-periodic $\chi$ along the orbit, this forces $|G(s)|^2 = |G(\sigma^3(s))|^2$ (in fact the complex amplitudes satisfy $G_\mathrm{cplx}(\sigma^3(s)) = -\,G_\mathrm{cplx}(s)$, so the squared modulus is preserved exactly).

The further split into $G_\mathrm{low}$ on $\{1, 5\} \cup \{2, 6\}$ and $G_\mathrm{high}$ on $\{4, 7\}$ reflects the χ-content of the first three positions of the orbit. The character $\chi$ takes value $+1$ on $\{1, 4\}$ and $-1$ on $\{2, 5, 6, 7\}$. Let $\nu_+(s_0) := \#\{j \in \{0, 1, 2\} : \chi(\sigma^j(s_0)) = +1\}$. For $s_0 = 4$: orbit $(4, 2, 1)$, $\chi$-values $(+1, -1, +1)$, $\nu_+ = 2$. For $s_0 = 7$: orbit $(7, 6, 5)$, $\chi$-values $(-1, -1, -1)$, $\nu_+ = 0$. For $s_0 \in \{1, 2, 5, 6\}$: $\nu_+ = 1$. The high-locus σ³-orbit $\{4, 7\}$ is therefore the unique σ³-orbit where the first-three-positions $\chi$-content is *imbalanced* ($\nu_+ \in \{0, 2\}$), and the imbalance breaks the cancellation that suppresses $|G|^2$ on the balanced orbits ($\nu_+ = 1$).

Direct evaluation gives $G_\mathrm{low} \approx 1.872$, $G_\mathrm{high} \approx 9.389$. $\square$

**Remark 4.3 (Numerical structure of the three values).** The exact values of $G_\mathrm{low}$ and $G_\mathrm{high}$ are algebraic in $\mathbb{Q}(\omega)$, the cyclotomic field $\mathbb{Q}(\zeta_9)$. The closed-form expressions involve sums of cyclotomic units; the ratio $G_\mathrm{high} / G_\mathrm{low} \approx 5.014$ is itself algebraic. We do not pursue the closed-form here; it is computational.

**Remark 4.4 (Terminology — finite Gauss sum, not an L-function).** Earlier corpus material referred to $G(s)$ informally as a "finite $L$-function." This terminology is misleading: a Dirichlet $L$-function is an *infinite* series $L(s, \chi) = \sum_{n \geq 1} \chi(n)/n^s$ with a multiplicative character $\chi$ on $(\mathbb{Z}/N)^\times$, an Euler product over primes, and analytic continuation; none of these structural features hold for $G(s)$, which is a sum of 9 terms with a $\{-1,0,+1\}$-valued non-multiplicative character $\chi$ on $\mathbb{Z}/10\mathbb{Z}$. The honest name is **finite Gauss sum** (or, with the orbit-iteration emphasis, **trajectory coherence integral**) — a discrete Fourier coefficient of $\chi$ along the $\sigma$-orbit at frequency $1/9$. We use "trajectory coherence integral" throughout this paper; the analogy with $L$-functions is a *vocabulary rhyme* (§5), not a technical correspondence.

---

## §5 The Q17-B Clay bridge

We now state precisely what the finite $L$-function says about the Clay-RH problem — and what it does not.

### 5.1 The structural mirror

The Riemann Hypothesis demands of $\zeta(s)$:

(R1) Zeros located on the critical line $\mathrm{Re}(s) = 1/2$.
(R2) Spectral concentration — the pair correlation of zeros (Montgomery 1973) takes the universal sinc² form $1 - \mathrm{sinc}^2(u)$.
(R3) A duality between the multiplicative Euler product and the additive Dirichlet series.

The finite character sum $G(s)$ exhibits (R1') zeros at the anchors $\{0, 3, 8, 9\}$ — the four $\sigma$-fixed points, exactly the "predictable locations"; (R2') spectral concentration on the σ³-orbit $\{4, 7\}$, where $G_\mathrm{high}$ is approximately $5.0\times$ the value on the other σ³-orbits, with the concentration driven by imbalanced χ-content in the orbit's first three positions ($\nu_+ \in \{0, 2\}$ versus $\nu_+ = 1$); (R3') a transverse pairing between the multiplicative orbit structure ($\sigma$-cycle) and the additive character $\chi$ (which sums to $-2$ across the substrate).

This is the **structural rhyme** with RH: the same three structural ingredients (zeros at predictable locations, spectral concentration, a multiplicative-additive interplay) appear in a finite, completely characterized setting. We emphasize that this is *not* a function-field analogue in the technical sense (Weil 1949, Deligne 1974). The genuine finite analogue of RH is the Weil zeta function of a curve over $\mathbb{F}_p$, proved by Deligne; that machinery is not engaged here. We register only that the finite-arithmetic *shadow* of "zeros at predictable locations + spectral concentration" is realized in $G(s)$, and leave the question of whether a Weil-Deligne-style analogue exists for the σ-permutation as an open problem (§7).

### 5.2 What the bridge does NOT claim

We do not claim:

* **That $G(s)$ proves RH.** $G(s)$ is finite and bounded; $\zeta(s)$ is infinite and analytic. The structural mirror is **not** an analytic continuation argument.
* **That the three-valued structure of $G(s)$ "predicts" the location of $\zeta$-zeros.** The 10-element substrate is too small to force any constraint on $\zeta$.
* **That the $\sigma$-permutation extends to the integers.** The rate theorem [J14] shows $\sigma(\mathbb{Z}/N\mathbb{Z}) \to 0$ as $N \to \infty$ on the squarefree-modular family — i.e., the finite analogue *flattens* in the continuum limit, exactly as the BB Bridge requires ([J13]). The $G(s)$ structure does not survive the continuum limit; it is a feature of finite arithmetic.

### 5.3 What the bridge DOES claim

* **The 6-layer Q-series architecture is a finite, completely characterized model of the same structural phenomena RH describes in an infinite setting.** The model is an instance; the Millennium Problem asks whether instances can be infinite.
* **The Symbolic Return Theorem (Theorem 2.1) is the algebraic kernel of Q17-C2** — the conjectured Navier-Stokes target (`Q17_NS_TARGET_REFORMULATION.md`, treated separately as Tier-D conjecture and not claimed here).
* **The boundary between Q17-A (proved algebra), Q17-B (this paper, structural bridge), and Q17-C (conjectured physics) is sharp.** The proofs in §§2–4 are Tier-A; the bridge statement of §5.1 is Tier-B (structural conjecture, computationally motivated); Q17-C is Tier-D (conjectured).

---

## §6 Companion connections in the J-series

**Direct dependencies (already-submitted companions).**

* **[J29]** — Q17-A: 5D Force Vector as CRT Fourier Embedding of $\mathbb{Z}/10\mathbb{Z}$ into $\mathbb{R}^5$ (AMM). The Tier-A proved-algebra companion. This paper's $\chi$ and $\sigma$-orbit data come from the same underlying CRT decomposition.

**Co-citing companions (parallel-track submissions).**

* **[J51]** — G6+G7+G8 spectral consolidation (European J Combin, Sanders + Gish). Layer-1, Layer-3, Layer-4 polynomial / period / spectral results that this paper builds on.
* **[J5]** — Crossing Lemma (JCT-A or JPAA, Sanders + Gish). The information-generation framing of $\sigma$-non-associativity that gives the 6-cycle its structural meaning.
* **[J20]** — Universal Orthogonality Principle (UOP) (JNT). The orthogonality framing of the $\sigma$-permutation and gate score.

**Successor connections.**

* **[J10]** — Joint TSML + BHML chain (Math Intelligencer). The 8-element chain on which $G(s)$ takes its values.
* **[J47]** — 6-DOF synthesis (this Phase 5 cluster opener). $G(s)$ lives in the Lattice DOF (anchor structure) intersected with the Permutation DOF ($\sigma$-orbit).

---

## §7 Open problems

1. **Closed-form $G_\mathrm{low}$ and $G_\mathrm{high}$ in $\mathbb{Q}(\zeta_9)$.** The numerical values $G_\mathrm{low} \approx 1.872$, $G_\mathrm{high} \approx 9.389$ are algebraic; we do not provide the closed forms in cyclotomic units. **Open.**
2. **Higher-$N$ generalization.** Does $\sigma_N$ on $\mathbb{Z}/N\mathbb{Z}$ (for $N$ squarefree, $N \neq 10$) admit a comparable three-valued $G$-function? The rate theorem [J14] suggests the structure flattens for large $N$. **Partial — Tier-C.**
3. **Why is $\{4, 7\}$ the high-locus σ³-orbit?** The σ³-action partitions the 6-cycle into three 2-cycles $\{1, 5\}$, $\{2, 6\}$, $\{4, 7\}$, and the σ³-orbit on which $\chi$-content of the first three orbit positions is imbalanced ($\nu_+ \in \{0, 2\}$) is uniquely $\{4, 7\}$. The combinatorial fact — *which* σ³-orbit carries the imbalance — depends on the specific σ-orbit ordering and the specific assignment of $\chi$. The structural reason this particular σ³-orbit is the "imbalance carrier" (rather than $\{1, 5\}$ or $\{2, 6\}$) is open: it presumably reflects deeper interplay between the σ permutation's cycle structure and the placement of $\chi^{-1}(+1) = \{1, 4\}$ relative to that cycle. **Open.**
4. **Q17-C (Navier-Stokes).** The Symbolic Return Theorem's continuum lift to NS regularity is the Q17-C target (Tier-D). The bridge premise — that any continuum lift preserving CRT separability is forced to logarithmic nonlinearity (BB theorem) — is treated in [J13]. **Open.**
5. **Weil-Deligne-style analogue.** Whether a genuine function-field zeta function (in the sense of Weil 1949 and Deligne 1974) can be associated with the σ-permutation, so that the structural rhyme of §5 lifts to a mathematical correspondence rather than a vocabulary correspondence, is the deepest open problem in the Q17-B program. **Open.**

---

## §8 Honest scope

This paper is **structural / pedagogical**, not a Millennium-Problem proof. The contributions are:

* Theorem 2.1 (Symbolic Return) — Tier-A, proved.
* Theorem 4.2 (three-valued $G(s)$) — Tier-A, proved.
* §5 bridge statement — Tier-B (structural conjecture, computationally motivated). The boundary between proved algebra (§§2–4) and bridge claim (§5) is sharp.

The paper does not:

* Prove RH or any portion of it.
* Claim that the finite analogue extends to the integers.
* Claim that the conjectured Q17-C NS target is settled.

The paper explicitly:

* Identifies the finite $L$-function $G(s)$ as a Dirichlet character sum on a 9-step orbit.
* Establishes the Symbolic Return Theorem as a direct corollary of $\sigma^6 = \mathrm{id}$.
* Maps the three-valued structure of $G(s)$ onto the three structural features RH demands of $\zeta(s)$.
* Cites the proved-algebra companion [J29] and the spectral-layer companion [J51] as the foundation.

---

## §9 References

### Direct dependencies (already-submitted J-companions)

[J29] B.R. Sanders, M. Gish. "Q17-A: 5D Force Vector as CRT Fourier Embedding of $\mathbb{Z}/10\mathbb{Z}$ into $\mathbb{R}^5$." Submitted to *Amer. Math. Monthly*, Phase 3.
[J51] B.R. Sanders, M. Gish. "Spectral Layer Consolidation: G6 + G7 + G8 from the Q-Series Architecture on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *European J. Combin.*, Phase 5 (parallel submission).

### Co-citing J-companions

[J14] B.R. Sanders, M. Gish. "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$." JCT-A, Phase 1.
[J32] B.R. Sanders, B. Mayes. "Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas." JCT-A or JPAA, Phase 1.
[J13] B.R. Sanders, H.J. Johnson. "The Bialynicki-Birula Bridge: Logarithmic Nonlinearity Forced by Separability." JMP, Phase 2.
[J20] B.R. Sanders, B. Mayes. "Universal Orthogonality Principle (UOP): Theorem 0." JNT, Phase 3.
[J10] B.R. Sanders, M. Gish. "Joint TSML+BHML Chain: Lens-Dependence at Size 7." Math. Intelligencer, Phase 3.
[J47] B.R. Sanders, B. Mayes. "Six Algebraic DOFs of the TIG Framework: A Synthesis." Notices AMS, Phase 5.

### External background

* H. Davenport. *Multiplicative Number Theory.* GTM 74, 3rd ed., Springer, 2000.
* A. Drápal, I.M. Wanless. "Maximally nonassociative quasigroups." *J. Combin. Theory Ser. A* **184** (2021), 105510. (Domain precedent: small finite commutative non-associative structures; opposite extremum to the present family.)
* H.L. Montgomery. "The pair correlation of zeros of the zeta function." *Proc. Sympos. Pure Math.* 24 (1973), 181–193.
* H. Iwaniec, E. Kowalski. *Analytic Number Theory.* AMS Coll. Publ. 53, 2004.
* C. Bombieri. *The Riemann Hypothesis (Clay description).* Clay Mathematics Institute, 2000.
* LMFDB Collaboration. *Number field 4.2.10224.1.* https://www.lmfdb.org/NumberField/4.2.10224.1.

### Q17 corpus references

* `papers/Q17_CLAY_SPECTRAL_BRIDGE.md` (2026-04-02; Tier-B structural).
* `papers/Q17_FINITE_L_FUNCTION_NOTE.md` (2026-04-02; companion).
* `papers/Q17_SYMBOLIC_RETURN_THEOREM.md` (2026-04-02; Tier-A proved).
* `papers/Q17_5D_RIGOROUS.md` (2026-04-02; J29 source).
* `papers/Q17_NS_TARGET_REFORMULATION.md` (Q17-C; not claimed here).
* `papers/G6_PERIODICITY_THEOREM.md`, `papers/G7_GATE_RATE_DISTRIBUTION.md`, `papers/G8_TRAJECTORY_COHERENCE_INTEGRAL.md`.

---

## §10 Bibtex

```bibtex
@misc{sanders2026j51,
  author       = {Sanders, Brayden Ross and Gish, M.},
  title        = {Q17-B Clay Bridge: A Finite Gauss Sum (Trajectory Coherence Integral) and the Symbolic Return Theorem on $\mathbb{Z}/10\mathbb{Z}$},
  year         = {2026},
  month        = {sep},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {Submitted to \emph{L'Enseignement Math\'ematique}},
  note         = {{J52} of the {J}-series; Phase 5; cites [{J29}] (Q17-A proved-algebra companion) and [{J51}] (G6+G7+G8 spectral-layer companion). The structural bridge between the finite Gauss sum $G(s)$ and the analytic structure of $\zeta(s)$, with sharp boundary between proved algebra (Tier-A) and bridge rhyme (Tier-B). The boundary between the structural rhyme of \S5 and a genuine function-field analogue (Weil-Deligne) is made explicit.}
}
```
