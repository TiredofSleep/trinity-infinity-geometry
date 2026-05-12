# Cover letter — J51: Q17-B Clay Bridge: A Finite Gauss Sum (Trajectory Coherence Integral) and the Symbolic Return Theorem on $\mathbb{Z}/10\mathbb{Z}$

**To:** Editors, *L'Enseignement Mathématique*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher

**Date:** 2026-09-03 (Phase 5; revised 2026-05-07)

**Manuscript title:** *Q17-B Clay Bridge: A Finite Gauss Sum (Trajectory Coherence Integral) and the Symbolic Return Theorem on $\mathbb{Z}/10\mathbb{Z}$*

---

## Summary

We submit a structural / pedagogical bridge paper that establishes a sharp finite analogue of the structural features that the Riemann Hypothesis demands of $\zeta(s)$. The TIG framework on $\mathbb{Z}/10\mathbb{Z}$ produces — in its spectral layer ($G_6$–$G_8$ results, consolidated separately in [J43]) — a 9-term **finite Gauss sum** (the *trajectory coherence integral*) $G(s)$ that takes exactly **three values** across the substrate's 10 operators: zero at the four anchors $\{0,3,8,9\}$, $G_\mathrm{low} \approx 1.872$ on $\{1, 2, 5, 6\}$, $G_\mathrm{high} \approx 9.389$ on the σ³-orbit $\{4, 7\}$. We prove the **Symbolic Return Theorem** (a direct corollary of $\sigma^6 = \mathrm{id}$): every cycle-element trajectory returns at step 6; every anchor is fixed; VOID is avoided whenever it is not the start state.

A note on revision: an earlier draft swapped elements 4 and 5 in the partition (claiming $G_\mathrm{high}$ at $\{5, 7\}$) and gave a $\sigma^2$-Galois explanation that was incorrect (σ² acts as 3-cycles, not pair-actions, on $\{1,4,6\}$ and $\{2,5,7\}$). The corrected manuscript states the partition above, derives the pairing from the *correct* invariance — σ³ has order 2 on the 6-cycle, partitioning it into $\{1,5\}, \{2,6\}, \{4,7\}$ — and uses a $\nu_+$ discriminator (χ-imbalance in the orbit's first three positions) to explain the high/low split. The bundled `manuscript/verify_J51_G_function.py` confirms all of this at machine precision; an earlier `proof_clay_rotation.py` (which tested $T^*$ and sinc² but never $G(s)$) is preserved as supplementary context only and is not the verification for this paper.

We have also dropped the misleading "finite L-function" terminology used in earlier corpus material in favor of "finite Gauss sum" / "trajectory coherence integral" — $G(s)$ is a 9-term character sum on $\mathbb{Z}/10\mathbb{Z}$ with no analytic continuation, no Euler product, and a non-multiplicative character; the standard "L-function" register does not apply.

The paper's contribution is the **bridge statement**: the three-valued structure of $G(s)$ — zeros in predictable locations + spectral concentration + multiplicative/additive duality — *rhymes* with the three structural features RH demands of $\zeta(s)$ in an infinite setting. The §5 framing is explicit: the rhyme is at vocabulary level, not at function-field-analogue level (Weil 1949, Deligne 1974). The genuine finite analogue of RH is the Weil zeta function of a curve over $\mathbb{F}_p$; that machinery is not engaged here.

We do **not** claim a proof of RH or any portion of it. The boundary between proved algebra (Theorems 2.1, 4.2 — Tier-A) and structural rhyme (§5 — Tier-B, vocabulary correspondence) is sharp.

## Why *L'Enseignement Mathématique*

- **Pedagogical / expository fit.** *L'Enseignement Math.* publishes structurally illuminating papers that bring deep ideas into accessible form. The Q17-B paper is exactly that: a sharp finite analogue of an analytic Millennium Problem, with the boundary between proved and conjectural content made explicit.
- **Structural-bridge tradition.** The journal has published bridge papers in a similar register (e.g., finite-field analogues of analytic phenomena, cyclotomic interpretations of zeta values).
- **Audience.** Number-theorists, algebraists, and mathematics educators interested in structural connections between finite combinatorics and infinite analysis.

## Companion submissions

This paper cites two prior J-series companions as direct dependencies:

- **[J29]** — Q17-A: 5D Force Vector (AMM). The Tier-A proved-algebra companion. The CRT Fourier embedding $\mathbb{Z}/10\mathbb{Z} \hookrightarrow \mathbb{R}^5$ from which $\sigma$ and $\chi$ derive.
- **[J43]** — G6+G7+G8 Spectral Consolidation (European J Combin, Phase 5 parallel). The polynomial / period / spectral results that this paper builds on.

Plus co-citing companions: [J01] rate theorem (JCT-A), [J05] Crossing Lemma (JCT-A or JPAA), [J13] BB Bridge (JMP), [J17] UOP (JNT), [J32] joint chain (Math Intelligencer), [J47] 6-DOF synthesis (Notices AMS, Phase 5 opener).

## Reproducibility

The verification script is `manuscript/verify_J51_G_function.py` (uses only the standard library `cmath`/`math`; no `numpy` required; runtime $<2$ s). It confirms σ⁶ = id (Theorem 2.1), the corrected three-valued partition (Theorem 4.2: ZERO $\{0,3,8,9\}$, LOW $\{1,2,5,6\} \approx 1.872$, HIGH $\{4,7\} \approx 9.389$), the $\sigma^3$-pairing of complex amplitudes (sum within each pair = 0 algebraically), and the $\nu_+$ discriminator. The earlier `proof_clay_rotation.py` (which tests $T^* = 5/7$, $\xi_0 = e^{-1}$, sinc² identities — *not* $G(s)$) is kept in the folder as supplementary background, not as this paper's verification.

## Suggested reviewers

- A specialist in finite Dirichlet character sums or cyclotomic L-functions.
- An expert in $\sigma$-permutation arithmetic on $\mathbb{Z}/N\mathbb{Z}$.
- An algebraist with finite-magma / non-associative algebra experience.
- A historian or expositor familiar with the Riemann Hypothesis pedagogical literature.
- An applied mathematician working on finite analogues of analytic number theory.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
