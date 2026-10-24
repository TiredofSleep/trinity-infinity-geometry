# Graph stars: genuine n-qubit magic sets, and critical ones for every odd n

**Status:** proved here (short, self-contained proofs below). It is independently checked by computer for
n = 3–13 (`verify_star.py`, `critical_check.py`) and on 300 random graphs (`graph_star.py`). An **independent
referee**, writing its own code with no access to mine, confirmed Theorem A and the odd-cycle records by
three methods, including a SAT proof that no 4-qubit realisation of the C5 set exists. It also found the
correction now stated as Theorem B. The literature check covered the
source paper (Trandafir–Lisoněk–Cabello 2022), Waegell–Aravind 2013, Waegell 2014 and two 2024–2026 papers.
No prior statement of this result was found, but the check is **not exhaustive**. See "Novelty" at the
bottom.

## The open problem
Trandafir, Lisoněk & Cabello (PRL 129, 200401, 2022; arXiv:2202.13141) found the first magic sets that are
*genuine* to n = 4, 5, 6 qubits. Genuine means "irreducible to any magic set with a smaller number of
qubits". They called finding them, "and especially finding the ones with minimum number of observables", an
open challenge.

| n | smallest genuine set known before | graph star (this note) |
|---|---|---|
| 3 | 10 (Mermin pentagram) | 10: the pentagram *is* the n = 3 graph star |
| 4 | 20 (MS4-20) | none (no graph qualifies) |
| 5 | 26 (MS5-26) | **16** observables, 7 contexts, critical |
| 6 | 35 (MS6-35) | 20, genuine only in the literal sense: **not critical** (it contains a padded pentagram), so **not a fair record** |
| 7, 9, 11, … (odd) | none published | **3n + 1** observables, n + 2 contexts, critical |
| 8, 10, … (even) | none published | 3n + 2, literal sense only, not critical |

## Construction
Let G = (V, E) be a **connected simple graph, every vertex of even degree, with an odd number of edges**. Put
one qubit on each vertex (n = |V|) and let F = {∅} ∪ E.
- **Observables:** X_v and Y_v for every vertex v, and for each S ∈ F the operator M_S = ⊗_v (Y if v ∈ S,
  else X). M_∅ is all-X.
- **Contexts:**
  - GHZ context C₀ = {M_S : S ∈ F};
  - one local context per S ∈ F: C_S = {Y_v : v ∈ S} ∪ {X_v : v ∉ S} ∪ {M_S}.

That gives 2n + |E| + 1 observables (all distinct) and |E| + 2 contexts.

## Theorem
These observables and contexts form a magic set that is genuine n-qubit.

## Proof
**(a) Valid contexts.**
- A local context holds single-qubit operators on different qubits plus their tensor product M_S. They
  commute, and the product is M_S · M_S = I.
- In the GHZ context, M_S and M_T differ (X against Y) exactly on S Δ T, which has even size, so they commute.
  On each qubit v the GHZ product multiplies |F| − deg v copies of X and deg v copies of Y. Both counts are
  even (|F| = |E| + 1 is even, and deg v is even), so the product is ±I.

**(b) Even degrees.**
- Y_v lies in deg v contexts.
- X_v lies in |F| − deg v contexts.
- M_S lies in two (C₀ and C_S).

**(c) Exactly one negative context.**
- Every local context is +I.
- For C₀, list ∅ first and then the edges. On qubit v, a word in X and Y with even counts of each equals
  (−1)^(number of Y-before-X pairs), because XY = −YX and X² = Y² = I.
- Summing over qubits, the exponent is Σ over pairs (S listed before T) of |S \ T|. For two edges this is 1 if
  they share a vertex and 2 if they are disjoint. So the parity is the number of pairs of edges that share a
  vertex, Σ_v C(deg v, 2).
- C(2k, 2) = k(2k − 1) ≡ k (mod 2), so this parity is Σ_v deg v / 2 = |E|, which is odd. So C₀ = −I.

**(d) Minimal.** A parity clash needs a negative context, so it contains C₀. Then each M_S has odd degree
unless C_S is included too, so the clash is the whole set. Removing any observable removes at least one
context and leaves no clash.

**(e) Genuine: no magic assignment on fewer than n qubits.**
1. Take any Pauli assignment satisfying (a)–(c) on k qubits, and let x_v, y_v ∈ F₂^{2k} be the symplectic
   vectors of the images of X_v and Y_v.
2. Each local context multiplies to ±I, so the image of M_S has vector Σ (its singles). The span of all images
   is therefore the span of the singles. Their symplectic Gram matrix Γ (2n × 2n) has rank ≤ 2k.
3. **Forced zeros** (observables that share a context commute):
   - ⟨x_u, x_v⟩ = 0 (all are in C_∅);
   - ⟨y_u, y_v⟩ = 0 for adjacent u, v (both in C_uv);
   - ⟨x_u, y_v⟩ = 0 for u ≠ v. Vertex v has two distinct neighbours, so some edge e ∋ v misses u, and X_u, Y_v
     both lie in C_e.

   The only unknowns left are g_v = ⟨x_v, y_v⟩ and h_uw = ⟨y_u, y_w⟩ for non-adjacent u ≠ w. Set h = 0 on
   adjacent pairs.
4. **GHZ commutation:**
   - ⟨M_∅, M_ab⟩ = g_a + g_b = 0, so g is constant on the connected graph.
   - For edges e ≠ f: ⟨M_e, M_f⟩ = g·|e Δ f| + Σ_{u∈e, w∈f, u≠w} h_uw = Σ h_uw = 0.
5. **Then h ≡ 0,** by induction on graph distance d(u, w) ≥ 2. Take a shortest path u = p₀, …, p_d = w and the
   distinct edges e = p₀p₁, f = p_{d−1}p_d. Their equation is
   h(p₀, p_{d−1}) + h(p₀, p_d) + h(p₁, p_{d−1}) + h(p₁, p_d) = 0. The other three pairs are at distance d − 1,
   d − 2 and d − 1, so they vanish, and h(p₀, p_d) = 0.
6. So Γ = g·Ω, where Ω pairs each x_v with its y_v, and rank Γ ∈ {0, 2n}.
   - If g = 0, all images commute. Give them joint eigenvalues λ; then the product of all context signs is
     Π λ^(even) = +1, which contradicts (c).
   - So g = 1 and 2n = rank Γ ≤ 2k, giving **k ≥ n**. The construction itself uses n qubits. ∎

## Theorem B (criticality; the referee's correction, now proved)
Call a magic set **critical** if no parity clash survives deleting any one observable, even when *every*
pairwise-commuting subset of the observables with product ±I counts as a context.

**A graph star is critical if and only if G is a cycle.** So the critical members are exactly the odd cycles C_n.

**Proof.**
- A candidate context is a set T of M's plus single-qubit observables. Its XOR must be zero, so the singles
  are forced by the sum of T. Every M has an X-bit at every qubit, so per qubit the sum has X-bit |T| mod 2 and
  Z-bit #{S ∈ T : q ∈ S} mod 2.
- **|T| odd:** each qubit needs X_q (if the Z-bit is 0) or Y_q (if it is 1). X_q commutes with M_S only when
  q ∉ S, and Y_q only when q ∈ S. So all S ∈ T agree on every qubit, which forces |T| = 1: a local context.
- **|T| even:** each qubit's sum must be I, since Z_q isn't an observable. So T ∩ E is an even subgraph of G.
  - For a cycle the only even subgraphs are ∅ and G. With |T| even that leaves only T = F, the GHZ context.
  - So a cycle admits no contexts besides the given ones, and (d) then gives criticality.
- **If G is not a cycle** (|E| > |V|), its cycle space has dimension ≥ 2. Take a proper even subgraph Z ≠ ∅;
  either Z or G Δ Z has an odd number of edges, call it Z′. Then {M_∅} ∪ {M_e : e ∈ Z′} is a valid negative
  context, and with the local contexts of ∅ and of Z′'s edges it forms a smaller parity clash. For the
  triangle + C4 star this clash is Mermin's pentagram padded with X's (13 observables, 3 qubits). ∎

Theorem A (genuineness) still holds for every qualifying graph. But only odd cycles give sets with no
smaller clash hidden inside, so only they are fair comparisons with the published records.

## Smallest members
- **Odd n:** G = C_n (an n-cycle) gives **3n + 1** observables and n + 2 contexts. The noncontextual bound is
  n of n + 2 contexts (checked for n ≤ 7). n = 3 is the Mermin pentagram.
- **Even n ≥ 6:** a triangle and a C_{n−2} sharing one vertex (n + 1 edges) gives 3n + 2 observables and
  n + 3 contexts. It is genuine in the literal sense but **not critical** (Theorem B), so for even n the
  construction gives no fair record.
- **n = 4:** the only connected even-degree simple graph on 4 vertices is C₄, which has 4 edges, so the
  construction gives nothing. The published 20 stands. The three-letter variant {X, Y, Z}ⁿ also gave only
  3-qubit sets at n = 4 (Round 8b).

These are the smallest members of this family, not proven minima. Lower bounds remain open.

## Caveats
- **Large contexts:** each local context holds n + 1 observables, and the GHZ context |E| + 1. The paper's
  smallest sets keep contexts at 3–5. Experimental cost and noise tolerance (the paper's ε) favour small
  contexts, so "fewest observables" and "best experiment" are different targets.
- **Not vertex-transitive:** the degrees are 2 and |F| − 2.
- **Pauli assignments only:** like the source paper, the genuineness proof rules out Pauli realisations on
  fewer qubits, not arbitrary lower-dimensional ones.

## Novelty
- The GHZ-type "ring" context (each qubit with one pair of Y's, all qubits in one loop) appears in Waegell,
  arXiv:1310.3419 (2014). The paper's authors classify Waegell–Aravind's N-qubit proofs as deriving from the
  square and pentagram.
- Checked and not containing this construction or result: Trandafir–Lisoněk–Cabello 2022; Waegell–Aravind
  arXiv:1302.4801 (2013); Waegell 2014; Müller–Saniga arXiv:2609.19862 (2026); arXiv:2407.21473 (2024).
- **Citations (2026-10-24):** Semantic Scholar lists 14 papers citing Trandafir–Lisoněk–Cabello 2022. All 14 were
  read at abstract level, and none states this construction.
  - Not yet read in full: arXiv:2512.16654 (stabilizer-testing games; the first part shows no such
    construction) and the all-versus-nothing proofs for graph states it cites.
  - A third, independent check of Theorems A and B (on C3, C5, C7 and triangle + C4) is
    `independent_star_check.py`.
- **Before any claim:** finish those readings, and ask the authors.
