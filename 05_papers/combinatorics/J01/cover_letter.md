# Cover letter — J01: Non-Associativity Decay in Binary Composition Tables over Z/NZ

**To:** Editors, *Journal of Combinatorial Theory, Series A*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** May 2026

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

The authors decline to suggest specific reviewers; the venue's editorial board
is best placed to identify referees in maximally / minimally non-associative
quasigroups and finite absorbing semigroup theory.

## Conflict of interest

The authors declare no competing interests. No funding was received for this
work.

---

Sincerely,
B.R. Sanders
