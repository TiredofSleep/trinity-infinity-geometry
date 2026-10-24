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
| `run_all.py` | all of the above (ALL GREEN) |

**Status:** proved; computer-checked; independently refereed (confirmed, with the even-n correction now built in). The literature check
is partial: the ring context is in Waegell 2014; the completion and genuineness proof weren't found.
Ask the authors before claiming.
