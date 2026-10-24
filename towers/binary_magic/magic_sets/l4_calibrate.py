"""L4 calibration: Waegell's 4-qubit Star with single-qubit factors (13 observables, 6 contexts of
sizes 3-5) is inside L4's class, so the (6, 13) search must have generated it, as 'fewer qubits'."""
import json, sys
from lower_bound4 import canon_fast
from waegell_stars import even_kernel, star

obs, ctxs = star(even_kernel(4), False)
key = canon_fast(len(ctxs), ctxs, len(obs))
path = sys.argv[1] if len(sys.argv) > 1 else "logs/l4_seen_6_13.json"
seen = {json.dumps(k): v for k, v in json.load(open(path, encoding="utf-8"))}
got = seen.get(json.dumps([[list(p), m] for p, m in key]), "NOT FOUND")
print("Waegell 4-qubit Star (13 observables) in the (6,13) survivors:", got)
assert got == "fewer qubits"
