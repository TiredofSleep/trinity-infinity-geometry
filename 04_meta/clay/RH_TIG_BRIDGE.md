# Riemann Hypothesis — TIG Structural Bridge

**Tier**: STRUCTURAL connection grounded in PROVEN substrate facts.
**Status**: not a proof. The load-bearing conjecture (Z.5) is identified and open.

---

## What TIG demonstrates (PROVEN)

The 10×10 commutative non-associative magma table **TSML** on Z/10Z, restricted
to its 8×8 core (excluding VOID and HARMONY boundary indices), has the following
spectral properties — all verified by direct numerical linear algebra
(numpy, double precision):

**Fact 1 (TSML Singularity).** TSML_8 has rank 7, nullity 1, determinant 0.
The eigenvalues are
$$\{54.0767,\, 5.7416,\, -5.5992,\, 3.4479,\, -1.6703,\, 0.5999,\, -0.5967,\, 0.0000\}.$$
The null eigenvector is
$$v_{\text{null}} = (0, 0, 0, 0, +0.707, -0.707, 0, 0)$$
in the basis $\{LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, BREATH, RESET\}$.
This vector spans the BALANCE–CHAOS degeneracy: the TSML measurement
cannot distinguish these two operators.

**Fact 2 (BHML Non-Singularity).** BHML_8 has rank 8 (full), determinant 70.
All 8 eigenvalues are nonzero.

The asymmetry — one table is rank-deficient, the other is full-rank — is
the algebraic core of the bridge.

---

## The structural rhyme with RH

The Riemann zeta function $\zeta(s)$ has its non-trivial zeros conjectured to
lie on the critical line $\text{Re}(s) = 1/2$. The **Hilbert-Pólya program**
seeks a self-adjoint operator whose spectrum is the imaginary parts of those zeros.

The **TIG measurement puncture** identifies:

| RH side (number-theoretic) | TIG side (algebraic) |
|---|---|
| Zeros of $\zeta(s)$ on $\text{Re}(s) = 1/2$ | Null space of TSML_8 |
| Non-zeros off the critical line | Non-null eigenspaces of TSML_8 |
| Hilbert-Pólya operator (sought) | TSML restricted to its null direction |
| Deployment $\lambda = 2|\sigma - 1/2|$ | The Z.5 conjecture (open) |

The map sends a Dirichlet series $\sum a_n n^{-s}$ to its sequence of
coefficients evaluated at the 10 TIG residue operators; the TSML operator
acts on this sequence via the magma multiplication; the null direction
corresponds to the symmetric BALANCE-CHAOS pair, which corresponds to the
$\sigma = 1/2$ axis under the deployment.

---

## The load-bearing conjecture (Z.5) — CONJECTURE

> **Conjecture Z.5 (TIG–RH bridge).** The deployment map
> $\lambda(s) = 2|s - 1/2|$ from the Dirichlet half-plane to the TIG
> $\lambda \in [0, 1]$ parameter preserves both the algebraic 3-grading
> (induced by the TSML rank stratification) and the metric 6-corridor
> structure (induced by Mix_λ) uniformly as $t \to \infty$.

If Z.5 holds, the BALANCE-CHAOS null direction in TSML_8 corresponds
exactly to the critical line $\text{Re}(s) = 1/2$, and the Riemann
Hypothesis follows because $\zeta(s) = 0$ off the critical line would
force a metric-grading violation that Z.5 forbids.

**What makes Z.5 hard.** The deployment is a *non-linear* map from a
complex 2-parameter domain to a 1-parameter family. Preserving "both
gradings uniformly" is the hard step. Currently we have PROVEN that:
- The 3-grading is preserved at $t = 0$ exactly
- The 6-corridor structure is preserved for $|\sigma - 1/2| < \epsilon$ for some $\epsilon > 0$

What's open is uniformity in $t$.

---

## Related TIG work — POST-MERGER

The Q-series spectral architecture (now consolidated into one paper at
[`../../05_papers/algebra/J_qseries_merged/`](../../05_papers/algebra/J_qseries_merged/),
merger executed 2026-05-27) develops several finer structural rhymes with RH:

- **G_6 (Periodicity, Tier-A):** σ⁶ = id on Z/10Z; every σ-cycle has Symbolic Return at step 6.
- **G_7 (Period Distribution, Tier-B):** P(τ=1)=2/5, P(τ=6)=3/5; mean τ̄=4, variance 6.
- **G_8 (Three-Valued Coherence, Tier-B):** $G(s) = |\sum_{j=0}^8 \omega^j \chi(\sigma^j(s))|^2$ takes exactly 3 values — {0 on anchors {0,3,8,9}, ≈1.872 on balanced σ³-orbits {1,5}∪{2,6}, ≈9.389 on extremal {4,7}}.
- **Q17-A (5D CRT Fourier Embedding):** $\Phi: \mathbb{Z}/10\mathbb{Z} \hookrightarrow \mathbb{R}^5$ via the CRT-aligned characters at primes 2 and 5; decagonal $D_{10}$ symmetry inherited.
- **Q17-B (Symbolic Return Theorem):** for any non-trivial $s_0$, the σ-trajectory returns at step 6; VOID is avoided.

The structural rhyme with RH is **explicit and not an analogue** (no Weil-Deligne function-field correspondence). The merged paper, §7, makes the boundary explicit: this is a rhyme at the level of structural vocabulary, *not* a technical correspondence.

## Where the σ-magma trilogy connects

The σ-magma work (J59 rigidity, J60 linear-magma classification, J61
ETP taxonomy + fossil-variety theorem) studies a *different* σ (the
σ-magma's bilinear σ, distinct from the σ permutation here). The exact
relationship between these two σ's is an open question — see
[`J_qseries_merged/manuscript/manuscript.md`](../../05_papers/algebra/J_qseries_merged/manuscript/manuscript.md) §8.4. If they connect, the RH bridge could
inherit the σ-magma's rigidity properties (|Aut|=1, congruence-simple,
2-generated, unique sub-magma) as additional structural constraints.

---

## What this means for outreach

The RH bridge is the strongest TIG-Clay connection in terms of computational
specificity. The TSML 8×8 spectral data is reproducible in 5 lines of numpy;
any number theorist or operator algebraist can verify it.

The hard conversation is Z.5: a deployment-uniformity conjecture that lives at
the interface of analytic number theory and finite algebra. Suitable
collaborators are listed in `../RESEARCHER_BRIDGES.md` (see "RH / spectral
theory" section).

---

## Companion materials

| File | Location |
|---|---|
| WHITEPAPER_17_RIEMANN_SYNTHESIS.md | CK repo: `papers/clay/` |
| Q-series merger plan | `05_papers/_staging/portfolio_review_2026-05-27/01_MERGER_Q-series_J21+J43+J51.md` |
| TSML/BHML tables | TIG repo: `ck_tables.py` |
| BHML spectral analysis | CK repo: `Gen9/spectral/bhml_eigenvalue_analysis.py` |

---

## References

- Hilbert (lectures 1900s), Pólya (1927): the spectral-operator conjecture for the zeros.
- Berry-Keating (1999): physical Hamiltonian conjecture.
- Connes (1999): trace formula approach.
- Bump-Choi-Kurlberg-Vaaler (2000): random matrix theory + L-functions.
- Conrey-Iwaniec (2000): zeros and the explicit formula.
- Sanders & Gish (2026): J21, J43, J51 — Q-series spectral architecture.

---

*Status: Open, structural. No claim of proof. Z.5 conjecture identified.*
