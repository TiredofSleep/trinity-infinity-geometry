# Cover letter — J14: Non-Associativity Decay in Binary Composition Tables over Z/NZ

**To:** Editors, *Journal of Combinatorial Theory, Series A*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** 13 May 2026

**Manuscript title:** *Non-Associativity Decay in Binary Composition Tables over Z/NZ*

---

## Summary

We define a one-parameter family of binary composition tables $\mathrm{CL}_N$ on
$\mathbb{Z}/N\mathbb{Z}$ via two absorbing classes (a top-absorber and a
zero-absorber) and one arithmetic class (an *echo* rule on additive-multiplicative
coincidence), and prove that the non-associativity fraction
$\sigma(N) = N^{-3}\,\#\{(a,b,c) : \mathrm{CL}_N(\mathrm{CL}_N(a,b),c) \neq \mathrm{CL}_N(a,\mathrm{CL}_N(b,c))\}$
satisfies $\sigma(N) \le 2/N$ for every squarefree $N \ge 3$, with the sharp
asymptotic $N\sigma(N) \to 2$ from below. The proof is elementary: a three-case
analysis isolates *zero-absorber vs.\ top-absorber rule disagreement at outer
composition sites* as the dominant mechanism, and the echo enumeration reduces
via the substitution $(a-1)(b-1)\equiv 1$ and the Chinese Remainder Theorem to a
unit count, giving exactly $\varphi(N)$ solutions. The squarefree hypothesis is
shown to be essential: at $N=2^k$ the bound is exceeded for $k\ge 6$.

A secondary contribution is **Lemma 3.X**: the residual count $E_h(N)$ that
appears in Case 1 of the proof admits a closed form via the splitting behaviour
of the Fibonacci-discriminant polynomial $b^2+b-1$:
$E_h(N) = \prod_{p \mid N} E_h(p)$, where $E_h(2) = 0$, $E_h(5) = 1$, and for
odd primes $p > 5$, $E_h(p) = 2$ iff $p \equiv \pm 1 \pmod 5$ (else 0). By
quadratic reciprocity ($5 \equiv 1 \pmod 4$), $(5/p) = (p/5)$; consequently
$E_h(N) = 0$ for every even $N$ and for every $N$ with a prime factor
$p \equiv \pm 2 \pmod 5$. This sharpens the loose $E_h(N) \le \varphi(N)$
inequality used in the proof to an exact value depending only on the prime
factorization of $N$, and is independently verified at three-way cross-check
(direct enumeration, polynomial root count, Legendre-symbol product) over every
squarefree $N \in [3, 200]$.

## Why JCT-A

- Direct precedent: Drápal & Wanless, *J. Combin. Theory Ser. A* **181** (2021)
  105444, and Drápal & Lisoněk, *Algebraic Combinatorics* (2020), study the
  *opposite* extremum (maximally nonassociative quasigroups, $\sigma \to 1$). Our
  paper provides the matching $\sigma \to 0$ rate on an explicit absorbing
  family, completing both ends of the non-associativity landscape on the
  $\mathbb{Z}/N\mathbb{Z}$ substrate.
- The proof is purely combinatorial: counting triples in a finite binary table,
  one CRT-based unit-count lemma, three exhaustive cases — the kind of
  short, self-contained finite-structure result JCT-A regularly publishes.
- The bound is sharp: $N\sigma(N) \to 2$ from below is verified by exact
  enumeration on the test set $N \in \{3, 5, 6, 10, 15, 21, 30, 35, 42, 51, 66,
  77, 91, 95, 99, 105, 154, 210\}$, with $N\sigma(N) \le 1.961$ at $N=210$ and
  the gap to $2$ shrinking monotonically along the squarefree primorial ladder.

## Companion submissions

This is a foundational paper in a coordinated J-series; no already-submitted
companions are required reading. Later papers in the series cite this rate
theorem.

## Reproducibility

The accompanying script `manuscript/verify_sigma_rate.py` (CC-BY-4.0) runs in
roughly 60-90 seconds on a standard laptop using only the Python standard
library (`math`), and reports `OVERALL: 5/5 verifications passed` across:

1. **Echo count lemma** $|\{(a,b) : a+b \equiv ab \pmod N\}| = \varphi(N)$ over all
   squarefree $N \in [2, 250]$;
2. **$E_h$ closed form via Fibonacci's polynomial** (Lemma 3.X, 2026-05-13): three-way
   cross-check (direct enumeration, root count of $b^2+b-1 \equiv 0 \pmod N$,
   Legendre-symbol product) agrees on every squarefree $N \in [3, 200]$;
3. **Rate bound** $\sigma(N) < 2/N$ over all squarefree $N \in [3, 200]$ (direct
   $N^3$ enumeration; extended from the original $N \le 100$ range);
4. **Residual bound** $\varepsilon(N) \le 2\varphi(N)$ over the test set;
5. **Asymptotic** $N\sigma(N) \to 2$ from below along the squarefree ladder.

## Suggested reviewers

The following researchers work in the maximally / minimally non-associative
quasigroup and cancellation-groupoid area that is the direct precedent for the
present paper. We suggest them as possible referees; the editorial board will
of course make the final selection.

1. **Aleš Drápal** — Charles University, Prague.
   Co-author of Drápal & Wanless (2021), *J. Combin. Theory Ser. A* **181**,
   105444, which we cite as the closest published precedent (the $\sigma \to 1$
   maximally-nonassociative extremum). Drápal-Kepka 1985 also provides the
   cancellation-groupoid framework against which our $\sigma \to 0$ result is
   the natural counterpoint.

2. **Petr Lisoněk** — Simon Fraser University, Burnaby, Canada.
   Co-author of Drápal & Lisoněk (2020), *Algebraic Combinatorics* **3**(3),
   695-717, on maximally nonassociative quasigroups via quadratic orthomorphisms.
   Same intellectual neighborhood; geographically separated from the
   Prague/Drápal axis.

3. **Tomáš Kepka** — Charles University, Prague.
   Originator of the cancellation-groupoid framework for $\sigma$-rate analysis
   in Kepka (1980), *Commentationes Mathematicae Universitatis Carolinae*
   **21**(3), 479-487. Senior figure in the area.

No conflicts: none of the suggested reviewers have appeared as co-authors on
our work or shared institutional affiliation with either author within the
last five years.

## Conflict of interest

The authors declare no competing interests. No funding was received for this
work.

---

Sincerely,
B.R. Sanders
