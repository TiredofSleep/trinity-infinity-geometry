# Cover letter — J12: Galois D_4 over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor

**To:** Editors, *Communications in Algebra*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Galois D_4 over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor*

---

## Summary

We present in self-contained form the Galois-theoretic content of a four-element fusion-closed sub-magma's symmetric-mixing fixed point. On Z/10Z under the joint action of two specific commutative non-associative magma tables (T = TSML, B = BHML; tabulated in our companion paper J15, submitted to *Algebraic Combinatorics*), the four-element set C_4 = {0, 7, 8, 9} is the unique fusion-closed sub-magma supporting the symmetric-mixing iteration F_{1/2}. The unique interior fixed point's coordinate ratio ξ* = r/β is the unique positive real root of the irreducible monic integer quartic

  f(x) = x^4 + 4x^3 - x^2 + 2x - 2.

We prove: (i) f is irreducible over Q (case-by-case integer factorization plus mod-7 cross-check, with the mod-5 reducible counterexample recorded for transparency); (ii) Gal(f/Q) = D_4 (cubic resolvent (y+2)(y^2 - y + 18) has exactly one rational root, polynomial discriminant -40896 is not a square in Q, and f remains irreducible over Q(√-71); the standard quartic-Galois classification (Cohen 1993, §6.3.2) yields D_4); (iii) the number field K = Q[x]/(f) is the catalogued field LMFDB 4.2.10224.1 (polynomial discriminant -40896 vs field discriminant -10224, index [O_K : Z[ξ*]] = 2, signature (2,1), class number 1, regulator ≈ 8.617; explicit Tschirnhaus reduction x ↦ -x - 1 to LMFDB's canonical defining polynomial x^4 - 7x^2 - 12x - 8); (iv) Q(√3) ⊂ K via the explicit factorization f = (x^2 + (2+√3)x - (1+√3))(x^2 + (2-√3)x - (1-√3)) with conjugate quadratic discriminants 11 ± 8√3 (norm -71).

The number field K is catalogued and not new; what is novel is the route. We record a quartic Galois D_4 field arising as the ring of definition for the fixed-point coordinates of a symmetric-mixing iteration on a four-element fusion-closed sub-magma of Z/10Z — a "new route to a known field" entry that is, to our knowledge, not previously catalogued in the literature for this particular finite-magma origin.

## Why Communications in Algebra

- **Subject fit.** Explicit Galois-group computation, explicit irreducibility argument, cubic resolvent classification, number-field identification with LMFDB — all squarely within Comm Algebra's scope.
- **Self-contained presentation.** Approximately 12 pages, with verification reduced to a single sympy script (`verify_J15_galois.py`) carrying six independent checks corresponding one-to-one to the theorem's claims; runtime approximately two seconds, sympy the only dependency. Independent reproducibility in PARI/GP via `polgalois(f)` and the LMFDB record is immediate.
- **The combinatorial-to-arithmetic route.** The origin of f as the algebra of fixed-point coordinates of a fuse iteration on a finite commutative non-associative magma is unusual; we believe it is worth recording in the *Comm Algebra* literature as a "new route to a known number field" entry.

## Companion submissions and differentiation

- **J15** — *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z*, submitted to *Algebraic Combinatorics*. The substrate paper: introduces T, B on Z/10Z, the four-core C_4, the joint fuse data, and the F_{1/2} iteration; states the Galois identification as part of a wider combinatorial analysis.
- **J01** — *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z*, submitted to *Journal of Algebra*. The corpus-centerpiece companion: bundles the Galois identification of LMFDB 4.2.10224.1 (its Theorem D / Theorem 5.2) alongside five further structural facts on the four-core (3-substrate joint closure, normalizer identity, universal attractor across chain shells, partial α-uniqueness, F_p-universality on a bounded scan).
- **J12 (present paper)** carries the standalone, referee-portable Galois proof. Where J01 bundles `Gal(f/Q) = D_4` as one claim of six, J12 unfolds the full proof — case-by-case integer factorization, cubic resolvent computation, C_4-vs-D_4 distinction via Q(√-71), explicit Q(√3) factorization, and Tschirnhaus reduction to LMFDB — so the result is reviewable on its own algebraic-number-theory terms without committing to the broader fusion-closure framework.

## Reproducibility

A single sympy script `verify_J15_galois.py` (CC-BY-4.0) bundled with the manuscript performs six checks:

1. Irreducibility of f over Q (case-by-case + mod-7 cross-check; mod-5 reducible counterexample recorded).
2. Polynomial discriminant `Δ_f = -40896 = -2^6 · 3^2 · 71`.
3. Cubic resolvent `g(y) = y^3 + y^2 + 16y + 36 = (y+2)(y^2 - y + 18)` with rational root `-2` and quadratic-factor discriminant `-71`.
4. Galois group `D_4` (via irreducibility of f over Q(√-71)).
5. Q(√3) subfield via explicit two-quadratic factorization with conjugate discriminants `11 ± 8√3` (norm `-71`).
6. LMFDB 4.2.10224.1 identification via Tschirnhaus reduction `x ↦ -x - 1` to `x^4 - 7x^2 - 12x - 8` and index `[O_K : Z[ξ*]] = 2`.

All six checks PASS at machine precision in approximately two seconds. The script and the manuscript are deposited at https://github.com/TiredofSleep/ck/tree/tig-synthesis alongside J15 and J01.

## Closest published precedent

- **Drápal & Wanless (2021), *J. Combin. Theory A* 184, 105510** — *Maximally nonassociative quasigroups*. Same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative; the present substrate is at the structurally regular end of the same family). We cite it as the closest neighbour for the input substrate.

## Suggested reviewers

- A specialist on Galois groups of low-degree polynomials (resolvent-cubic classification, Cohen-style computational number theory).
- A specialist on small-discriminant quartic fields and the LMFDB catalogue.
- A specialist on number fields arising from finite-magma / dynamical-system fixed points (a small but distinctive niche).

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
