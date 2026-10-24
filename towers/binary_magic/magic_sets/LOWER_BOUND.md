# Lower bounds for genuine n-qubit magic sets

Notation:
- V observables and C contexts;
- r = F₂-rank of the incidence matrix;
- W = F₂^V / R, the observable space modulo the context relations, with d = dim W = V − r.

A Pauli assignment is a list of symplectic vectors; "genuine n-qubit" means every magic Gram matrix has rank
≥ 2n (Trandafir–Lisoněk–Cabello, Cor. 10).

## Lemma 1: V ≥ 2n + r
Each context multiplies to ±I, so its vectors sum to 0. The r independent context relations are therefore
linear dependencies among the V vectors. So dim span ≤ V − r, and the Gram matrix's rank is at most that.
Genuineness needs rank ≥ 2n. ∎

## Lemma 2: a minimal magic set has r = C − 1
The sum of all contexts is 0 (even degrees). Any other dependency is a proper, nonempty sub-collection T whose
observables all have even T-degree; its complement is the same. One of the two carries an odd number of
negative contexts, which would be a smaller clash. ∎

**Corollary.** V ≥ 2n + C − 1. Every known minimal set meets it with equality:

| set | V | 2n + C − 1 |
|---|---|---|
| square | 9 | 4 + 6 − 1 = 9 |
| pentagram | 10 | 6 + 5 − 1 = 10 |
| C_n star | 3n + 1 | 2n + (n + 2) − 1 = 3n + 1 |

## Lemma 3: a magic set has at least 5 contexts
Write P_X for the product of the observables in a set X.
- **C = 3:** the observables split into pieces A (in c₁, c₂), B (in c₁, c₃) and D (in c₂, c₃). P_A, P_B and P_D
  pairwise commute, since each pair shares a context. So the product of the three context equations is
  P_A² P_B² P_D² = I, which means an even number of negatives.
- **C = 4:** observables in all four contexts commute with everything and drop out of the parity. Of the rest,
  let X_ij hold the observables in contexts i and j. Multiplying the four context equations, the parity of
  negatives equals ω(P_X13, P_X24), the symplectic product: it is 1 when the two anticommute. But the context
  equations force P_X24 ∝ P_X12 P_X23, and P_X13 commutes with both P_X12 (context 1) and P_X23 (context 3). So
  the parity is 0. ∎

## Lemma 4: a cap on context size
A magic form B of rank ≥ 2n on W makes each context's span in W isotropic, so of dimension ≤ d − n.
Hence |c| ≤ d − n + dim R_c, where R_c = the relations supported inside c (always ≥ 1, from c itself).
At n = 5 with d = V − C + 1 this gives |c| ≤ V − C − 4 + dim R_c.

## Theorem (target): no genuine 5-qubit magic set has 15 or fewer observables
By Lemmas 2 and 3, V ≤ 15 forces C ∈ {5, 6}:
- C = 6 needs V = 15, so d = 10;
- C = 5 has V = 14 (d = 10) or V = 15 (d = 11).

By Lemma 4:
- with dim R_c = 1, every context has ≤ 6 observables, except when C = 5 and V = 15, where 7 is possible;
- larger contexts need dim R_c ≥ 2.

The exhaustive search (`lower_bound2.py`) covers contexts of ≤ 6 observables, calibrated at n = 2 and 3 and
cross-checked against a brute-force enumerator. The remaining cases are covered by `lower_bound3.py`: C = 5
with V = 15 and contexts up to the Lemma-4 cap, plus every case with dim R_c ≥ 2. **Status: see the scores in
PREREG.md (Round 11).**

**Size of the remaining case (counted 2026-10-24, in Claude Code).** For (C, V) = (6, 15), the generator in
`lower_bound2.py`, called with context sizes up to 9, yields the following number of hypergraphs to filter
(counted exactly, by dynamic programming over the multigraph part; no hypergraph was built):
- 19.9 million with no high-degree observable;
- 239 million with at most one;
- 1.25 billion with at most two;
- 3.89 billion with at most three, and more beyond (the count stopped there).

At the measured 6,700 hypergraphs per second, that is days even on 32 cores, so the run cannot finish as
written.
- Lemma 4 caps the contexts at 6 whenever dim R_c = 1, which forces 2a₄ + 4a₆ ≤ 6 (at most three
  high-degree observables). So the dim R_c = 1 regime is small if generated with that cap.
- A context of 7 to 9 observables needs dim R_c ≥ 2. Then the other five contexts split into two groups that
  no degree-2 observable outside c joins, which is a structural condition to enumerate directly.

If both searches come back empty, then:
- **16 is the exact minimum at n = 5;**
- the C5 graph star is optimal;
- the general bound V ≥ 2n + C − 1 shows that any odd-n improvement on 3n + 1 must use fewer than n + 2 contexts.
