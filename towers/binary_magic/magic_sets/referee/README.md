# referee/: independent verification code

Written by a separate agent that had no access to the code in `../`. It wrote everything from scratch and
read only THEOREM.md and `graph_star_sets.json`. Paths have been made relative (they read
`../graph_star_sets.json`).

Needs `pip install python-sat networkx`.

| script | what it checks |
|---|---|
| `verify_sets.py` | explicit matrices, signs, (i)–(iii) |
| `gram.py` | full Gram space over all observables: exactly {0, actual} for each set |
| `sat_search.py`, `sat_canon.py` | SAT, with symmetry breaking: no 4-qubit realisation of the C5 set (373 patterns UNSAT) |
| `canon_search.py`, `run_c5.py` | constructive search over Clifford orbits; signs from explicit multiplication |
| `critical.py`, `crit_all.py` | criticality: odd cycles critical; non-cycles hide a padded pentagram |
| `general_check.py`, `calibrate.py` | the theorem on all small qualifying graphs; calibration on the square and pentagram |

**Verdict** (summarised in `../PREREG.md`): Theorem A confirmed; C5 and C7 confirmed and critical. The even-n
"20 vs 35" was corrected to literal-sense only, which is now Theorem B.
