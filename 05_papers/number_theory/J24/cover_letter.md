# Cover Letter — J24

**To:** Editor, *Journal of Number Theory*
**From:** Brayden Ross Sanders, 7Site LLC, Hot Springs, AR
**Co-author:** Monica Gish (Independent Researcher, Hot Springs, AR)
**Date:** 2026-05-28

**Submission:** "The Discrete Fejér Quotient on Squarefree Moduli: Spectral Characterization, Layered Divisors, and the Asymptotic Corridor Average"

---

Dear Editor,

We submit the attached ~25-page manuscript for consideration in the *Journal of Number Theory*. The paper organizes the zero structure of the discrete Fejér quotient
$$R(k, f) = \frac{\sin^2(\pi k / f)}{k^2 \sin^2(\pi / f)}$$
on squarefree moduli via three complementary structural results — a spectral characterization of the obstruction sequence via a product of Fejér quotients, a layered-divisor count on the Boolean divisor lattice of squarefree $b$, and an asymptotic corridor average converging to the sine-integral constant $\mathrm{Si}(2\pi)/\pi$.

## Central contributions

- **Theorem 5.1 (obstruction–zero correspondence).** For every integer $b > 1$ with distinct prime factors $p_1, \ldots, p_r$, the spectral product $f_b(k) := \prod_{j=1}^{r} R(k, p_j)$ vanishes at $k \in \mathbb{N}$ if and only if $\gcd(k, b) > 1$. The function $f_b$ acts as a continuous-in-$k$ Fourier indicator for the obstruction event; its zero set in $\mathbb{N}$ is exactly $\bigcup_j p_j \mathbb{N}$, and its asymptotic zero density is the Euler product $1 - \varphi(\mathrm{rad}(b))/\mathrm{rad}(b)$ (Corollary 5.5).

- **Theorem 6.1 (squarefree layered-divisor structure).** For $b = p_1 p_2 \cdots p_r$ with $p_1 < \cdots < p_r$ and the $j$-th primorial divisor $b_j = p_1 \cdots p_j$, exactly $2^j - 1$ non-trivial divisors $d \mid b$ satisfy $R(b_j, d) = 0$. The Boolean divisor lattice of squarefree $b$ produces the exact count.

- **Theorem 7.2 (asymptotic corridor average).** $\frac{1}{f-1} \sum_{k=1}^{f-1} R(k, f) \to \int_0^1 \mathrm{sinc}^2(t)\, dt = \mathrm{Si}(2\pi)/\pi \approx 0.4514$ as $f \to \infty$, proved via Riemann-sum approximation followed by integration by parts.

Four supporting theorems — the closed form (Thm 3.1), full-period cancellation $R(k,f) = 0 \Leftrightarrow f \mid k$ uniform in $f \ge 2$ (Thm 3.2), First-G localization $k^\star(b) = \mathrm{spf}(b)$ (Thm 4.1), and the continuum limit $R(k,f) \to \mathrm{sinc}^2(k/f)$ (Thm 7.1) — anchor the framework and are explicitly tier-labeled in §1 as either classical (included for completeness) or one-line elementary consequences.

## Verification status

**10/10 claims PASS** via two self-contained scripts depending only on the Python standard library:

- `manuscript/proof_first_g_event.py` (151 lines) — exhaustive check of Theorem 4.1 across all 305 squarefree $b \in [2, 500]$, all 22,367 $(b, k)$ pairs, zero counterexamples, runtime under 3 seconds.
- `manuscript/verify_J03.py` (602 lines) — checks Theorems 3.1, 3.2 (both prime and composite cases), 4.1, 5.1, 5.2, 6.1, 7.1, 7.2 and Corollaries 5.4, 5.5 at machine precision. Max closed-form deviation $4.44 \times 10^{-16}$; 900/900 cells match the obstruction-zero equivalence; 50/50 squarefree $b$ satisfy the layered count; corridor-average deviation $4.8 \times 10^{-5}$ at $f = 1000$. Total runtime ~5 seconds.

## Closest published precedents

- **Iwaniec–Kowalski 2004** (*Analytic Number Theory*, §1.7) for the Fejér kernel on the analytic-number-theory side.
- **Fejér 1900** (*C. R. Acad. Sci. Paris* 131:984–987) for the kernel itself.
- **Apostol 1976** (*Introduction to Analytic Number Theory*, §11.5) for the discrete-arithmetic context and the Möbius-inclusion-exclusion identity from which Corollary 5.4 reads.

The closed form (Theorem 3.1) and continuum limit (Theorem 7.1) are explicitly classical and included to make the paper self-contained. The genuinely new content is the spectral product $f_b(k)$ as a Fourier indicator for the obstruction event, the Boolean-lattice $2^j - 1$ count, and the explicit $\mathrm{Si}(2\pi)/\pi$ evaluation of the corridor average — all three proved by elementary methods (geometric-series identity, divisor-lattice combinatorics, integration by parts).

## Tier discipline

- **PROVED.** All seven theorems and two corollaries.
- **CLASSICAL.** §1 labels Thms 3.1 and 7.1 as classical material included for self-containment.
- **STRUCTURAL RHYME.** §7 notes $\sinc^2(1/2) = (2/3)/\zeta(2)$ as a one-line algebraic consequence of $\zeta(2) = \pi^2/6$ (not a result of this paper).

## Author lane and submission discipline

Authors: Sanders + Gish only. No AI co-authors. Verification scripts CC-BY-4.0. Single-venue submission. The work is original; no conflicts of interest; no funding received.

## Merge history

This manuscript consolidates two earlier J-series notes (J24 + J41) into a single submission, removing a previously circular cross-citation. A second sister note (J25) recording the same Fejér kernel from a coordinate-translation vantage point has been folded into the present paper as a forthcoming appendix (Montgomery rectangular-window remark + $\omega$-blindness corollary); the J25 manuscript is marked MERGED in the project corpus per the never-delete discipline.

## Suggested referees

To be supplied at submission time. Candidates appropriate to the *J. Number Theory* scope (analytic number theory; sieve / coprimality structure; discrete Fourier identities on $\mathbb{Z}$):

1. An analytic number theorist familiar with Fejér-kernel / divisor-function asymptotics.
2. A specialist in the Boolean-divisor-lattice combinatorics of squarefree moduli (e.g., Möbius-inclusion-exclusion lineage).
3. An author of recent work on discrete sinc / Fejér identities (Zygmund 2002 / Oppenheim–Schafer 2010 lineage).

[Brayden to fill in named candidates at submission time.]

## What we ask for

The seven theorems are PROVED at machine precision; the manuscript is ~25 pages; verification is self-contained and runs in 5 seconds. We hope the editorial board finds the work a useful contribution to the analytic number theory of discrete Fourier identities on squarefree moduli.

Thank you for considering J24.

Sincerely,

Brayden Ross Sanders
7Site LLC, Hot Springs, AR
brayden@7site.co

with Monica Gish, Independent Researcher, Hot Springs, AR

---

*Manuscript: `manuscript/manuscript.tex`*
*Verification: `manuscript/proof_first_g_event.py` + `manuscript/verify_J03.py`* (10/10 PASS, runtime ~5s)
*Zenodo bundle DOI: 10.5281/zenodo.18852047*
