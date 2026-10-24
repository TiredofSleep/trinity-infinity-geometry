# Pre-registration: the lens on an open problem (written 2026-10-23, before any search ran)

## The problem
Trandafir, Lisoněk & Cabello, "Irreducible magic sets for n-qubit systems", PRL 129, 200401 (2022),
arXiv:2202.13141. They close by calling it "an interesting challenge" to find genuine n-qubit magic sets,
"and especially … the ones with minimum number of observables".

**A magic set** is a set of Pauli observables and contexts. Each context is a set of commuting observables
whose product is +I or −I; it is negative when the product is −I. Three conditions:
1. every observable lies in an even number of contexts;
2. an odd number of contexts are negative;
3. it is minimal.

That is exactly a parity clash: the F2 antinomy detector's job. A set is **genuine n-qubit** when its
context structure can't be realized with Pauli observables on fewer qubits. By their Corollary 10, the
minimum qubit count is half the minimum binary rank of a "magic Gram matrix" in the structure's valid Gram
space.

**Smallest known (their Table II and main text):**

| qubits | smallest set | observables |
|---|---|---|
| 2 | Mermin square | 9 |
| 3 | pentagram | 10 |
| 4 | MS4-20 | 20 |
| 5 | MS5-26 | 26 |
| 6 | MS6-35 | 35 |

They also report an exhaustive search showing "no magic sets with fewer than 19 vertices". The paper
doesn't make clear which class that covers.

## What the lens adds
Their search went hypergraph-first: enumerate context structures, then test whether Pauli operators fit.
The main search was restricted to observables in four contexts and contexts of four or five observables.
This attempt goes **operator-first**, along the XOR skeleton:
1. grow pools of Pauli operators along commuting XOR lines {a, b, a⊕b};
2. list every context inside the pool (commuting sets of 3–5 operators that XOR to zero);
3. use integer programming to find the parity clash that uses the fewest observables;
4. shrink it to a minimal set;
5. compute the genuine qubit count from the Gram space.

This reaches structures their restricted search didn't cover (any mix of degrees and context sizes 3–5).

## Definitions used (where the paper is ambiguous)
- **Minimal:** no proper subset of the contexts is itself a parity clash, and all observables are distinct
  and not the identity. The paper's word "irreducible" may mean more than this; any result gets flagged
  with that gap.
- **Genuine n-qubit:** the minimum binary rank over magic Gram matrices is exactly 2n.

## Predictions
| id | kind | prediction | kill condition |
|---|---|---|---|
| W1 | validation | Mermin square: a parity clash, genuine 2-qubit (minimum rank 4), noncontextual bound 4 of 6 contexts. | Any mismatch. |
| W2 | validation | Pentagram: genuine 3-qubit (minimum rank 6), bound 3 of 5. | Any mismatch. |
| W3 | validation | The Mermin square padded with an idle third qubit still reads as 2-qubit (minimum rank 4). This is the test that the genuineness check isn't fooled by spare qubits. | It reads as 3. |
| T4 | real | **No** genuine 4-qubit minimal set with 19 or fewer observables is found. Guess: the true minimum is 20, or the search is too weak. | One is found, which would beat the published 20. |
| T5 | real | **No** genuine 5-qubit set with 25 or fewer is found. | One is found (beats 26). |
| T6 | real | A genuine 6-qubit set with **34 or fewer** observables **is** found. Six qubits is where the published search is thinnest. | None found (35 stands). |

**Budget:** about 2 hours of compute in total, over at most 3 pool-growth strategies. A negative result
means "not found by this method within this budget", never "doesn't exist".

**Before claiming any record:** rebuild the operators as explicit matrices in numpy; check commutation,
products and signs independently of the bit arithmetic; recheck minimality by brute force over context
subsets; and recompute the qubit count with a second method where the Gram space allows.

*Added before the search ran:* **W4 (method calibration).** Run on 3 qubits, the search should rediscover a
genuine 3-qubit minimal set with 10 observables (the pentagram's size). If it can't find the known minimum
at n = 3, its results at n ≥ 4 mean little.

## Round 8a: the code construction (written before `stars.py` ran)
**Calibration status, before this round:** the random-pool search (90 s at n = 3) found only 2-qubit-realizable
clashes of 11–12 observables, not the pentagram. W4 is unresolved, and the pool method looks too weak to
trust at n ≥ 4.

**The lens construction.** The pentagram is built from a binary code. Take a family F of even-weight
subsets S of the n qubits. Let M_S be the operator with Y on S and X elsewhere; any two M_S commute because
|S Δ T| is even. The contexts are:
- the "GHZ" context {M_S : S ∈ F};
- for each S, a local context {Y_i for i ∈ S, X_j for j ∉ S, M_S}.

Degrees are even exactly when |F| is even and every qubit lies in an even number of the S. Only the GHZ
context can be negative, so a clash needs a GHZ product of −I. And any clash must use the GHZ context, then
every local context, so **minimality is automatic**. The pentagram is n = 3, F = {∅, 12, 13, 23}. Observables:
|F| plus the single-qubit operators used (at most 2n).

| id | kind | prediction | kill condition |
|---|---|---|---|
| M1 | translation | n = 3 with the pentagram's F gives a genuine 3-qubit clash with 10 observables. | Anything else. |
| M2 | real | At n = 4, **no** member of the family is genuine 4-qubit: every magic one is realizable on 3 qubits. Reasoning: otherwise the paper's "no magic sets under 19 vertices" would be contradicted by a roughly 12-observable set. | A genuine 4-qubit member exists. That would beat the published 20 by a wide margin, so it would need the strongest verification. |
| M3 | real | Exhaustively for n = 4 and 5, and for |F| ≤ 8 at n = 6, the X/Y star family never goes beyond 3 genuine qubits. | Some member is genuine n-qubit for n ≥ 4. |

### Round 8a scores
| id | result | outcome |
|---|---|---|
| M1 | the pentagram's code gives the pentagram (10 observables, 3 qubits) | **held** |
| M2 | n = 4: 8 magic members, all realizable on 3 qubits | **held** |
| M3 | n = 5: **672 genuine 5-qubit members**; the smallest has 16 observables | **lost**, in the useful direction |
| T5 | a genuine 5-qubit set with ≤ 25 observables was found (16) | **lost**, in the useful direction |

**The candidate record: MS5-16.** F = {∅, 01, 02, 13, 24, 34}, the all-X operator plus the five edges of a
5-cycle. That gives 16 observables (X_q and Y_q for each qubit, plus six GHZ-type M_S) and 7 contexts, each of
6 observables, exactly one of them negative. The published smallest genuine 5-qubit set has 26 (MS5-26).

**Independent verification (`verify_ms5_16.py`, no shared code path with `min_magic_rank`):**
- explicit 32×32 matrices confirm commutation, products and signs;
- brute force over all 126 proper context subsets confirms minimality;
- every Gram matrix of the 10 single-qubit observables allowed by the commutation constraints was
  enumerated (2¹⁰), each was realised as explicit Pauli operators, and every context was multiplied out.
  Only two are allowed: rank 0 (even number of negatives) and the actual one, rank 10 (odd). So no
  assignment on ≤ 4 qubits exists, and the set is genuine 5-qubit in the paper's sense ("irreducible to any
  magic set with a smaller number of qubits").

**Why it doesn't contradict the paper's "no magic sets under 19 vertices":** that exhaustive search assumed
every observable sits in four contexts and every context has 4 or 5 observables. MS5-16 has degrees 2 and 4,
and contexts of 6.

**Literature gate, still open:** the paper says earlier N-qubit parity proofs (Waegell–Aravind) "derive from
the square and the pentagram". Whether this code family appears there has to be checked before claiming
novelty.

## Round 8b (written before running)
| id | kind | prediction | kill condition |
|---|---|---|---|
| N6 | real | The X/Y family at n = 6 with |F| ≤ 8 still tops out at 5 genuine qubits. Even n seems capped at n − 1 (n = 4 → 3; n = 6, |F| ≤ 6 → 5). | A genuine 6-qubit member. |
| N7 | real | The X/Y family at n = 7 with |F| ≤ 8 has genuine 7-qubit members, which would be the first genuine 7-qubit magic sets known. | None. |
| NZ | real | Allowing Z as a third letter (operators from {X, Y, Z}ⁿ with pairwise even distance) breaks the even-n cap: a genuine 4-qubit member exists with ≤ 20 observables. | None with |F| ≤ 8. |

### Round 8b scores
| id | result | outcome |
|---|---|---|
| N6 | 34,560 genuine 6-qubit X/Y members at |F| = 8; the smallest has 20 observables | **lost**, in the useful direction |
| N7 | all-X + 7-cycle: genuine 7-qubit, 22 observables | **held** |
| NZ | the three-letter family at n = 4: 32 magic members, all on 3 qubits | **lost** |
| T4 | no genuine 4-qubit set with ≤ 19 observables found | **held** |
| T6 | a genuine 6-qubit set with 20 observables (published: 35) | **held** |
| W4 | the random-pool search never found the pentagram | **lost**. The pool method was weak; the code construction replaced it. |

`verify_star.py` independently confirms the odd cycles for n = 3 to 13 and triangle + C_(n−2) for n = 6 to 12.
Every one is rigid: the only allowed Gram matrices are 0 and the actual one.

## Round 8c: a theorem, and its test (written before `graph_star.py` ran)
**Theorem (proof in THEOREM.md).** Let G be a connected simple graph with every degree even and an odd
number of edges. Take observables X_v and Y_v for each vertex, M_∅ = all-X, and for each edge e, M_e = Y on
e and X elsewhere. Take contexts: the GHZ context {M_∅} ∪ {M_e}, plus one local context per element of
F = {∅} ∪ E. This is a magic set that is **genuine |V|-qubit**, with 2|V| + |E| + 1 observables and
|E| + 2 contexts.

| id | kind | prediction | kill condition |
|---|---|---|---|
| TH1 | translation of the proof | 300 random connected even-degree graphs with an odd number of edges (5–9 vertices) are all magic, minimal and genuine |V|-qubit, with valid Gram space {0, actual}. | Any exception: the proof is wrong. |
| TH2 | translation | With an even number of edges, the set is never magic (degrees fail or the GHZ product is +I). | A magic one. |
| TH3 | translation | GHZ sign: the product of the M's is (−1)^(Σ_v C(deg v, 2)) and Σ_v C(deg v, 2) ≡ \|E\| mod 2, checked by explicit multiplication on every TH1 graph. | Any mismatch. |

### Round 8c scores
| id | result | outcome |
|---|---|---|
| TH1 | 300 random graphs (5–9 vertices): all magic, minimal, rigid, genuine \|V\|-qubit | **held** |
| TH2 | 200 even-edge graphs: none magic (the GHZ "context" doesn't even multiply to ±I) | **held** |
| TH3 | the GHZ sign matches (−1)^(Σ C(deg,2)), and Σ C(deg,2) ≡ \|E\| | **held** |

## Final tally for this attempt
- **Validations:** W1–W3 held. W4 lost (the random-pool search was too weak).
- **Real predictions:** 4 of 8 held (corrected at handoff from "4 of 10", a miscount). T4, T6, M2 and N7 held. T5, M3, N6 and NZ lost. Three of those four losses
  (T5, M3, N6) were in the useful direction: sets I predicted wouldn't be found were found.
- **Theorem translation checks:** TH1–TH3 held.

**The result:** graph stars give genuine n-qubit magic sets for every n ≥ 5: 3n + 1 observables for odd n,
3n + 2 for even n. That's 16 against 26 at n = 5, 20 against 35 at n = 6, and the first known for n ≥ 7. The
proof is in `THEOREM.md`.

## Round 9: can the big contexts be shrunk? (written before `split_test.py` ran)
Graph stars have contexts of n + 1 (local) and |E| + 1 (GHZ). The standard way to shrink a context is to
**chain-split** it. Replace {s₁, …, s_k} by {s₁, s₂, P₂}, {P₂, s₃, P₃}, …, {P_{k−1}, s_k} with intermediate
products P_j as new observables. Each P_j sits in two contexts, so degrees stay even, and the sign product is
unchanged, so it stays a parity clash. But commutation constraints are lost: s₃ only has to commute with s₁s₂,
not with s₁ and s₂ separately.

**Comparison on the paper's noise measure** (ε = 1 − b/Q, b = noncontextual bound, Q = number of contexts):

| set | ε |
|---|---|
| C5 graph star | 2/7 = 0.286 |
| MS5-27 | 0.37 |
| MS5-26 | 0.2 |
| triangle + C4 graph star (n = 6) | 2/9 = 0.222 |
| MS6-35 | 0.167 |

So graph stars lead on observable count, not on noise tolerance at n = 5.

| id | kind | prediction | kill condition |
|---|---|---|---|
| Q1 | real | Chain-splitting every local context of the C5 star (to size 3) keeps a parity clash but **drops genuineness** below 5 qubits. | Still genuine 5-qubit. |
| Q2 | real | Chain-splitting only the GHZ context also drops genuineness. | Still genuine 5-qubit. |

### Round 9 scores
| id | result | outcome |
|---|---|---|
| Q1 | locals split: 31 observables, 25 contexts, still a parity clash, but realizable on **4** qubits | **held** |
| Q2 | GHZ split: 19 observables, 10 contexts, still a clash, but realizable on **2** qubits | **held** |

**What it means:** in graph stars the big contexts *are* the genuineness. The rigidity proof uses the
commutation constraints those contexts impose, and splitting them hands back the freedom to live on fewer qubits.
So there's a real trade-off between observable count and context size:
- graph stars: few observables, big contexts;
- the paper's sets: small contexts, more observables.

A new open question: what is the fewest observables for a genuine n-qubit set whose contexts have at most k
observables?

## Independent referee (separate agent, own code, no access to mine)
- **Confirmed:** Theorem A's proof (step by step); the C5 set (16 observables) and C7 set (22) as genuine,
  by three methods:
  - the full Gram space over all observables: exactly {0, actual} for every set;
  - SAT with justified symmetry breaking: all 373 four-qubit patterns UNSAT for C5;
  - an incomplete constructive search: 33 million leaves, no magic assignment found.
- Both are **critical**: the only commuting ±I subsets are the given contexts.
- **Corrected:** for any non-cycle graph the GHZ context splits, so a smaller parity clash hides inside. The
  6-qubit set contains a padded pentagram (13 observables, 3 qubits). The "20 vs 35" comparison is withdrawn
  as unfair. This is now Theorem B, proved in THEOREM.md and reproduced in `critical_check.py`, which shows
  odd cycles critical through n = 13 and non-cycles not.
- **Rescored:** T6 held only in the literal sense; as a fair record it is **withdrawn**.

**Corrected result:** critical, genuine n-qubit magic sets for every odd n, with 3n + 1 observables. At n = 5 that
is 16 against the published 26, and n ≥ 7 is new. Even n remains open via this route.

## Round 10: what is a small genuine magic set good for? (written before `game_use.py` ran)
The cleanest use is a **nonlocal game**. Alice receives a context and outputs ±1 values for its observables,
whose product must equal the context's sign. Bob receives one observable from that context and outputs ±1.
They win if Bob's value matches Alice's value for that observable. There is no compatibility loophole
because Alice and Bob are separated, unlike single-device contextuality tests.
- **Quantum strategy:** share n EPR pairs (2n qubits). Alice measures the context; Bob measures the transpose
  of his observable.
- **Genuine n-qubit:** any perfect Pauli strategy needs all n pairs. So it's a Pauli-world certificate of
  n EPR pairs.

| id | kind | prediction | kill condition |
|---|---|---|---|
| U1 | translation | Exact classical value = 1 − w_min / (contexts × context size) when all contexts have equal size: square 17/18, pentagram 19/20, C5 star 41/42, C7 star 71/72. Brute force over every deterministic strategy for square, pentagram and C5. | Any mismatch. |
| U2 | translation | The explicit EPR strategy wins with probability exactly 1, by simulation with 2n-qubit state vectors (C5: 10 qubits). | Anything below 1. |
| U3 | translation | Under white noise of visibility η the quantum win rate is (1 + η)/2, so the needed visibility is η* = 2·(classical value) − 1: 0.889, 0.900, 0.952, 0.972. | Simulation disagrees. |
| U4 | real | The cost of minimality: within these sets, **the higher the qubit count, the higher η*.** And graph stars need **one** entangling measurement in total (Alice's GHZ context); every other setting on both sides is a product of single-qubit X/Y measurements. | η* not increasing, or more than one entangling setting. |

### Round 10 scores
| id | result | outcome |
|---|---|---|
| U1 | classical values 17/18, 19/20, 41/42, 71/72 (brute force for the first three) | **held** |
| U2 | the EPR strategy wins with probability 1 (simulated up to C5, 10 qubits; C7's 14 qubits not simulated) | **held** |
| U3 | win rate (1 + η)/2; visibility needed 0.889, 0.900, 0.952, 0.972 | **held** |
| U4 | η* rises with qubit count; graph stars need exactly one entangling setting (the square needs two) | **held** |

---
## Round 11: is 16 the minimum at 5 qubits? (written before `lower_bound.py` ran)
**Lemma (proof in the script header).** A genuine n-qubit magic set with V observables and context incidence
matrix of F2-rank r has **V ≥ 2n + r**. Its observables must span ≥ 2n symplectic dimensions, and the r
independent context relations are linear dependencies among them.

**Exhaustive search class.** Hypergraph-first, with the qubit count decided by the paper's own test (the minimum
magic Gram rank). Every hypergraph with:
- at most 6 contexts, each of 3 to n + 1 observables;
- every observable in an even number of contexts;
- V ≤ (current record − 1) observables.

Each one is tested for a magic Pauli assignment and its minimum qubit count. Contexts of n + 1 are the largest
whose observables can be independent apart from their own relation (a maximal isotropic set in n qubits).

| id | kind | prediction | kill condition |
|---|---|---|---|
| L0 | translation | V = 2n + r exactly for the square, the pentagram and the C5/C7 stars. | Any set with V < 2n + r (lemma wrong) or a strict gap. |
| L1 | calibration | n = 2, up to 6 contexts of size 3: the minimum genuine 2-qubit set has 9 observables (the square). | Anything else. |
| L2 | calibration | n = 3, up to 6 contexts of size 3–4: the minimum genuine 3-qubit set has 10 (the pentagram). | Anything else. |
| L3 | real | n = 5, up to 6 contexts of size 3–6, V ≤ 15: **no** genuine 5-qubit set. Within the class, 16 is optimal. | One exists. That would be a new record, verified independently before any claim. |
| L4 | real | n = 4, up to 6 contexts of size 3–5: **no** genuine 4-qubit set at any size. | One exists. Anything under 20 would beat the published MS4-20. |

*Amendment before any n ≥ 3 result (the first, generic enumerator was too slow and was stopped; only L1 had
finished: the square, 9, the unique genuine 2-qubit set with ≤ 9 observables. **L1 held.**)*

**Lemma 2.** In a minimal magic set the contexts have exactly one linear dependency (their sum), so r = C − 1.
Proof: another dependency gives a proper, nonempty sub-collection T with every observable of even T-degree. Its
complement is even too. One of the two carries an odd number of negative contexts, so it is a smaller parity
clash, contradicting minimality.

**Corollary.** A minimal genuine n-qubit set has **V ≥ 2n + C − 1**. At n = 5 with V ≤ 15 that forces
**C ≤ 6**. The context-count limit in L3 is therefore proved, not assumed. The only remaining restriction is
context size ≤ 6. A faster enumerator (`lower_bound2.py`) builds the hypergraphs directly: high-degree
observables first, then multigraphs of degree-2 observables, with canonical deduplication.

**L2 restated:** n = 3, every minimal hypergraph with V ≤ 10 (so C ≤ 5) and contexts of size 3–4: the only
genuine 3-qubit sets have 10 observables. **L3 restated:** n = 5, every minimal hypergraph with V ≤ 15
(so C ≤ 6) and contexts of size 3–6: no genuine 5-qubit set. **L4** unchanged (C ≤ 6, sizes 3–5).

*Added while L3 was running, before any n = 5 output existed:*
- **Calibrations:** L2 held (the pentagram is the unique genuine minimal 3-qubit set with ≤ 10 observables). The
  fast enumerator matches the brute-force one exactly on 5 classes (`enum_crosscheck.py`).
- **Lemma 3** (≥ 5 contexts) and **Lemma 4** (|c| ≤ V − C − 4 + dim R_c, and dim R_c ≤ C − 2) are in LOWER_BOUND.md.
  Together they make the n = 5 question finite: (C, V) ∈ {(5,14), (5,15), (6,15)}, with contexts of ≤ 9
  observables.

| id | kind | prediction | kill condition |
|---|---|---|---|
| L3-full | real | `lower_bound3.py` (every case, every allowed context size) finds **no** genuine 5-qubit magic set with ≤ 15 observables, so **16 is the exact minimum**. | Any genuine hit, which would be a new record and need independent verification. Or any "unresolved" case, which would make the result incomplete. |

### Round 11 status at handoff (2026-10-24, about 50 CPU-minutes into `lower_bound3.py`)
| case | result |
|---|---|
| C = 5, V = 14 | done: 216 distinct minimal hypergraphs tested. 210 have no magic Pauli assignment; 6 fit on < 5 qubits. **No genuine 5-qubit set.** |
| C = 5, V = 15 | done: 2,327 more distinct. Cumulative: 2,499 with no magic assignment, 44 fitting on < 5 qubits. **None genuine, none unresolved.** |
| C = 6, V = 15 | **still running at handoff**; this is the largest case. |
| L4 (`lower_bound2.py n4`) | still running at handoff; no output yet. |

So no genuine 5-qubit magic set with ≤ 15 observables uses 5 contexts. **L3-full stays unscored until the
C = 6, V = 15 case finishes.** Partial logs are in `logs/`.

### Round 11 scores, continued (Claude Code, 2026-10-24; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| L4 | n = 4, at most 6 contexts of 3-5 observables, every size: (C, V) in {(5,12), (6,13), (6,14), (6,15)} give 20 / 2,369 / 454 / 49 distinct context-minimal survivors, none genuine, none unresolved (`lower_bound4.py`, n = 4; `LOWER_BOUND.md`) | **held** |
| L3-full | (5,14) and (5,15) empty, as before. (6,15), by `lower_bound5.py`: 23,281,793 + 1,444,341 hypergraphs, 81,246 distinct context-minimal survivors (79,670 with no magic assignment, 1,576 on fewer qubits), none genuine, none unresolved. So **16 is the exact minimum** for context-minimal genuine 5-qubit sets (`LOWER_BOUND.md`) | **held** |

**Calibration of L4.** Waegell's 4-qubit Star with single-qubit factors (13 observables, 6 contexts of 3-5)
is inside the class. The search generates it and classes it "fewer qubits" (`l4_calibrate.py`); directly
it fits on 2 qubits.

**Literature gate: Waegell's thesis (arXiv:1307.6264), read from the PDF.** Its Star families (Tables 26-27)
put every observable in exactly two IDs, so they fall under Arkhipov's theorem. Computed, each with N >= 4
fits on fewer than N qubits, and the 5-qubit Star fits on 2 (`waegell_stars.py`, `waegell_realize.py`, with
explicit matrices). The odd-N Star shares the graph star's counts, 3N + 1 and N + 2, but not its hypergraph,
and it is not genuine. This was the reading the chat asked for before anything is sent (THEOREM.md, Novelty).

**Lemma 5 (added, from TLC's Theorem 2).** A context-minimal clash has b = C - 2 exactly, so its tolerance is
2/C. The definitions matter:
- The published sets are not context-minimal: 16 of the 18 tabled sets must hide a smaller clash among their
  own contexts (`tolerance_check.py`). TLC's "minimal" is a different notion, injective assignments.
- So T4-T6 and L3-L4 compare our context-minimal sets with sets from a wider class.
- The C_5 graph star belongs to both classes, so "16 vs 26" stands inside theirs. A lower bound for their wider
  class is not attempted.

**The chat's next test, run 2026-10-24: do the hidden clashes still need all n qubits?** This was asked after
Lemma 5 as an open question, with no prediction registered. On MS5-26, no:
- all 3,051 context-minimal sub-clashes fit on at most 4 qubits;
- 105 larger sub-collections need 5, and every one of them uses all 26 observables and at least 18 of the 30
  contexts (`tlc_hidden.py`; `gram_np.py` is exhaustive up to Gram dimension 24, and none was left unresolved).
Its genuineness lives in the near-whole set, not in any minimal contradiction inside it.
