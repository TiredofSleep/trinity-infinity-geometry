"""export_sets.py — writes the record sets (n = 5, 6, 7) as explicit Pauli strings and contexts, re-verified
with explicit matrices, to graph_star_sets.json for anyone to check."""
import json
from graph_star import graph_star
from ms_core import verify_with_matrices, parse, check_magic
from critical_check import critical
out = {}
for name, n, E in (("C5 (n=5)", 5, [(q, (q + 1) % 5) for q in range(5)]),
                   ("triangle+C4 (n=6)", 6, [(0, 1), (1, 2), (0, 2), (0, 3), (3, 4), (4, 5), (5, 0)]),
                   ("C7 (n=7)", 7, [(q, (q + 1) % 7) for q in range(7)])):
    labels, ctxs = graph_star(n, E)
    signs = verify_with_matrices(labels, ctxs)
    assert signs.count(-1) == 1 and check_magic([parse(l) for l in labels], ctxs)[0]
    crit = not critical(labels, ctxs)[2]
    out[name] = dict(qubits=n, observables=len(labels), contexts=[[labels[v] for v in c] for c in ctxs],
                     negative_context=signs.index(-1), critical=crit,
                     note="critical: no smaller parity clash under any choice of contexts" if crit else
                          "genuine in the literal sense only; contains a padded pentagram (not a fair record)")
    print(f"{name}: {len(labels)} observables, {len(ctxs)} contexts, verified with {2**n}x{2**n} matrices")
json.dump(out, open("graph_star_sets.json", "w"), indent=1)
