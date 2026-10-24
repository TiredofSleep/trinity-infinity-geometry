# magic_sets/: the lens on an open problem

**The problem:** the smallest genuine n-qubit magic sets (Trandafir–Lisoněk–Cabello, PRL 2022). Read
`PREREG.md` (every prediction written before its run, scores after), then `THEOREM.md` (the result and its
proof).

**The result:** graph stars. Any connected even-degree graph with an odd number of edges gives a genuine
|V|-qubit magic set (Theorem A). The set is critical (no smaller clash hidden inside) exactly when the graph
is a cycle (Theorem B). So odd cycles give critical genuine n-qubit sets with 3n + 1 observables for every odd
n: 16 at n = 5 (published 26), and new for n ≥ 7. The n = 3 member is the Mermin pentagram. The even-n
members (e.g. 20 at n = 6) aren't critical, so they aren't fair records.

| script | what it does |
|---|---|
| `ms_core.py` | Pauli arithmetic, context signs, Gram-space minimum rank (the paper's Corollary 10) |
| `validate.py` | W1–W3: square, pentagram, padded square |
| `search.py` | the random-pool search (weak; W4 lost); kept for the record |
| `stars.py` | Round 8a: the binary-code construction; 672 genuine 5-qubit members |
| `verify_ms5_16.py`, `verify_star.py` | independent verification (explicit realisations and matrices, no shared code with the Gram-space method) |
| `graph_star.py` | Round 8c: the theorem tested on 300 random graphs, plus the even-edge controls |
| `critical_check.py` | Theorem B: odd cycles critical through n = 13; non-cycles hide a smaller clash (the referee's correction) |
| `export_sets.py` | writes `graph_star_sets.json` (the n = 5, 6, 7 records as Pauli strings) |
| `independent_star_check.py` | a third, independent check (Claude Code, 2026-10-24). It shares no code with the files above or `referee/`, enumerates every possible context, and solves for the whole Gram space |
| `lower_bound4.py` | the lower-bound search, generating only what Lemma 4 allows (regime A: every context within the dim R_c = 1 cap; regime B: a bigger context with its split T). Any n, with an optional cap on context size. Gentle: 6 workers at low priority by default |
| `lower_bound5.py` | the same search with a sharper regime B. A largest context of exact size s0 forces dim R ≥ s0 − (V − C + 1 − n), so every observable outside it has its pattern in S^⊥ for a subspace S of that dimension: 7, 3 or 1 possible patterns at (6, 15). Each S is taken once per symmetry orbit. It reproduces `lower_bound4.py` on (5, 14) and (5, 15) exactly, building about 30 times fewer regime-B hypergraphs |
| `gram_np.py` | the minimum magic Gram rank, vectorized with numpy (batched GF(2) ranks). It agrees with `ms_core.py` exactly on 45 test sets, and is fast enough to exhaust Gram spaces of dimension 24 |
| `count_jobs.py` | counts exactly how many hypergraphs each `lower_bound4.py` job would build, without building them (and the symmetry-broken regime-B counts) |
| `l4_calibrate.py` | L4's calibration: the search's (6, 13) survivors include Waegell's 4-qubit Star, as "fewer qubits" |
| `waegell_stars.py`, `waegell_realize.py` | the literature gate: Waegell's Star families from his thesis's Tables 26–27, tested by the same criteria (magic, minimal, Gram rank, bound), then realized on fewer qubits and checked with explicit matrices |
| `tlc_hidden.py` | the published MS5-26, rebuilt from its printed Pauli strings and checked with explicit matrices (genuine 5-qubit, b = 24/30); its incidence rank is 16, so 8,191 sub-collections of its own contexts are clashes, and each is tested for how many qubits it needs |
| `tolerance_check.py` | Lemma 5 (b = C − 2 for context-minimal clashes) by brute force, and what the published tables imply: 13 of 18 with w_min > 1, and 16 of 18 that must hide a smaller clash |
| `run_all.py` | all of the above except the long searches (ALL GREEN) |

**Status:**
- **Proved, computer-checked and independently refereed.** The even-n correction is built in.
- **Lower bound:** at n = 5, **16 is the exact minimum**: all three cases with V ≤ 15 are empty, and the last,
  (6, 15), took 24.7 million hypergraphs and 28 minutes (`lower_bound5.py`). At n = 4, the search with at most 6
  contexts of 3–5 (L4) found none at any size. Both cover context-minimal sets (`LOWER_BOUND.md`).
- **Literature:**
  - The ring context is in Waegell 2014.
  - Waegell's thesis Stars are degree-2 sets that reduce to the square or the pentagram, not genuine.
  - The completion and the genuineness proof were not found.
- **Ask the authors before claiming.**
