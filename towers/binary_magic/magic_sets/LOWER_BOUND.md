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
At n = 5 with d = V − C + 1 this gives |c| ≤ V − C − 4 + dim R_c. For general n it reads
|c| ≤ V − C + 1 − n + dim R_c, which is what `lower_bound4.py` uses.

## Lemma 5: the noncontextual bound of a context-minimal clash is C − 2
The paper's Theorem 2 gives b = C − 2·w_min, where w_min is the least weight in s + (column space of the
incidence matrix), and s marks the negative contexts. In a context-minimal clash the only dependency among
the contexts is their total (Lemma 2). So the column space is every even-weight vector, s + it is every
odd-weight vector, and w_min = 1. Hence **b = C − 2 and the noise tolerance is exactly 2/C**, with any one
context the one left unsatisfied.

**Corollary.** If w_min > 1, or if a genuine n-qubit set has C − 1 > V − 2n (Lemma 1 gives r ≤ V − 2n), then the
contexts have a second dependency T. Then T or its complement is a smaller parity clash made of the set's
own contexts.
- The paper's tables: w_min > 1 for 13 of the 18 sets, and C − 1 > V − 2n for 16 of them, all but the square
  and the pentagram (`tolerance_check.py`).
- So the published sets are not context-minimal. Their minimality is a different notion: the paper's
  Appendix B asks that every Pauli assignment be injective and avoid the identity.
- The search below is about **context-minimal** sets, the definition in `PREREG.md`. Sets that hide a
  smaller clash among their contexts, like the published ones, are outside its scope.

## L4: no genuine 4-qubit set with at most 6 contexts of 3–5 observables (2026-10-24)
For n = 4, Lemmas 2–3 and the size cap leave (C, V) ∈ {(5, 12), (6, 13), (6, 14), (6, 15)}:
- C ≥ 5;
- V ≥ C + 7;
- 2V ≤ 5C, since every degree is even and every context has at most 5 observables.

The cap 5 never exceeds the Lemma-4 cap V − C − 2, so only regime A is needed. `lower_bound4.py C V 8 4 5`:

| (C, V) | hypergraphs built | distinct survivors | no magic assignment | fewer qubits | genuine | unresolved |
|---|---|---|---|---|---|---|
| (5, 12) | 1,395 | 20 | 19 | 1 | 0 | 0 |
| (6, 13) | 1,341,370 | 2,369 | 2,278 | 91 | 0 | 0 |
| (6, 14) | 215,790 | 454 | 413 | 41 | 0 | 0 |
| (6, 15) | 12,043 | 49 | 39 | 10 | 0 | 0 |

**Calibration:** Waegell's 4-qubit Star with single-qubit factors lies in this class: 13 observables, 6 contexts
of 3–5. The (6, 13) search generates it and finds that it fits on fewer qubits (`l4_calibrate.py`), as
`waegell_stars.py` finds directly (2 qubits). The (5, 14) case at n = 5 reproduces lower_bound3's 216 survivors
exactly (`lower_bound4.py 5 14`, in `run_all.py`). Log: `logs/lower_bound4_L4_n4_2026-10-24.log`.

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

**The generator that does it (`lower_bound5.py`, Claude Code, 2026-10-24).**
- **Regime A** is `lower_bound4.py`'s: every context within the cap V − C + 2 − n. At (6, 15) that is
  23,281,793 hypergraphs, counted exactly (`count_jobs.py`).
- **Regime B:** relabel a *largest* context as c₀, of exact size s₀, so no other context is bigger. Let S be the
  set of T ⊆ {1, …, C − 1} whose contexts sum to a vector inside c₀.
  - The other contexts are independent (Lemma 2), so S is a subspace, it contains {1, …, C − 1}, and dim S =
    dim R_{c₀} ≥ s₀ − (V − C + 1 − n) (Lemma 4).
  - Every observable outside c₀ has an even T-degree for every T in S, so its pattern lies in S^⊥. Every
    observable inside c₀ has a pattern {0} ∪ D with |D| odd.
- **At (6, 15):**
  - s₀ = 7 needs dim S ≥ 2, so 7 possible outside patterns (one split T, as before);
  - s₀ = 8 needs dim S ≥ 3, so only 3;
  - s₀ = 9 needs dim S ≥ 4, so only 1.
- One S is taken from each orbit under relabelling, and the outside multiset once per orbit of its stabilizer.
  Every hypergraph then goes through the same exact filters.
- **Calibration:** it reproduces `lower_bound4.py` exactly. (5, 14) gives 216 (210 + 6) and (5, 15) gives 2,327
  (2,289 + 38). It builds 1,614 and 7,664 regime-B hypergraphs, where `lower_bound4.py` builds 50,263 and
  158,082 (31 and 21 times more).

If both searches come back empty, then:
- **16 is the exact minimum at n = 5;**
- the C5 graph star is optimal;
- the general bound V ≥ 2n + C − 1 shows that any odd-n improvement on 3n + 1 must use fewer than n + 2 contexts.
