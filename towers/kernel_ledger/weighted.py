#!/usr/bin/env python3
"""
weighted.py -- kernel_ledger/PREREG.md Round K8: is the weighted quarter of 5x5 kernels random?
Run from kernel_ledger/:  python3 weighted.py        Prints ASCII only. Exact determinants and ranks.
"""
import os, random, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from four_in_five_core import det_bareiss, canon, local_certs, global_index
from eccentric import eccentric, load
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
rng = random.Random(6868)
old_paths = [os.path.join(HERE, "..", "binary_magic", "void_lens", "squares5_annealed.txt"),
             os.path.join(HERE, "squares5_fresh.txt"), os.path.join(HERE, "squares5_fresh2.txt")]
old = {canon(M) for p in old_paths for M in load(p)}
fresh = {}
for M in load(os.path.join(HERE, "squares5_fresh3.txt")):
    k = canon(M)
    if k not in old: fresh.setdefault(k, M)

kind = {}; dets = {}
for k, M in fresh.items():
    d = det_bareiss(M); dets[k] = d
    assert d % 325 == 0
    if d == 0:
        kind[k] = "concentric" if (local_certs(M) or (global_index(M, 26) or 0) >= 1) else ("eccentric" if eccentric(M) else "weighted")
c = Counter(kind.values())
print(f"fresh: {len(fresh)} distinct new squares, {len(kind)} singular: {dict(c)}")

# W1: random-lattice estimate (fixed in the registration)
q = [d // 325 for k, d in dets.items() if d]
est = sum(1 for x in q if abs(x) <= 1000 and x % 240 == 0) / (2 * 1000 / 240)
ratio = c["weighted"] / est if est else float("inf")
print(f"W1: weighted {c['weighted']}, random-lattice estimate {est:.2f}, ratio {ratio:.2f}")

# W2: digit-layer deficiency
def deficient(M):
    A = [[(x - 1) // 5 for x in r] for r in M]; B = [[(x - 1) % 5 for x in r] for r in M]
    return sp.Matrix(A).rank() < 5 or sp.Matrix(B).rank() < 5
non = [fresh[k] for k in fresh if k not in kind]
base = sum(deficient(M) for M in rng.sample(non, 2000)) / 2000
wk = [fresh[k] for k, v in kind.items() if v == "weighted"]
wrate = sum(deficient(M) for M in wk) / max(len(wk), 1)
print(f"W2: singular digit layer in {100 * wrate:.0f}% of weighted vs {100 * base:.1f}% of nonsingular ({wrate / base:.2f}x)")
conc_share = c["concentric"] / max(len(kind), 1)
print(f"W3: concentric share {100 * conc_share:.0f}%")
res = {"W1": None if c["weighted"] < 6 else ratio >= 1.5,
       "W2": None if c["weighted"] < 6 else wrate >= 1.5 * base,
       "W3": 0.60 <= conc_share <= 0.80}
print("\nSCORE:", {k: ("UNSCORED" if v is None else "HELD" if v else "LOST") for k, v in res.items()})
