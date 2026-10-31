#!/usr/bin/env python3
"""
quarter_turn.py -- kernel_ledger/PREREG.md Round K10: is a hidden quarter-turn (90 degree) symmetry behind the
weighted quarter of singular 5x5 squares? Run from kernel_ledger/:  python3 quarter_turn.py   ASCII only.
"""
import os, sys, random
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from four_in_five_core import det_bareiss, canon, local_certs, global_index
from eccentric import eccentric, load
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
paths = [os.path.join(HERE, "..", "binary_magic", "void_lens", "squares5_annealed.txt")] + \
        [os.path.join(HERE, f) for f in ("squares5_fresh.txt", "squares5_fresh2.txt", "squares5_fresh3.txt", "squares5_fresh4.txt")]
uniq = {}
for p in paths:
    for M in load(p): uniq.setdefault(canon(M), M)

def q90(M):
    return sum(1 for i in range(5) for j in range(5) if (i, j) != (2, 2) and M[i][j] + M[4 - j][i] == 26)

def parallel(a, b):
    if not any(a) or not any(b): return False
    i = next(k for k in range(5) if a[k]); r = Fraction(b[i]) / Fraction(a[i])
    return all(Fraction(b[k]) == r * Fraction(a[k]) for k in range(5))

def lever_match(M):
    A = sp.Matrix(M)
    u = A.T.nullspace(); v = A.nullspace()
    if len(u) != 1 or len(v) != 1: return None
    fr = lambda x: Fraction(int(sp.Rational(x).p), int(sp.Rational(x).q))
    u = [fr(x) for x in u[0]]; v = [fr(x) for x in v[0]]
    return parallel(u, v) or parallel(u[::-1], v)

cls = {"concentric": [], "eccentric": [], "weighted": []}; non = []
for M in uniq.values():
    if det_bareiss(M) != 0: non.append(M); continue
    k = "concentric" if (local_certs(M) or (global_index(M, 26) or 0) >= 1) else ("eccentric" if eccentric(M) else "weighted")
    cls[k].append(M)
rng = random.Random(1010); base = rng.sample(non, 5000)
mb = sum(q90(M) for M in base) / len(base)
print(f"distinct squares: {len(uniq)}; singular: " + ", ".join(f"{k} {len(v)}" for k, v in cls.items()))
print(f"nonsingular baseline (5000): mean q90 = {mb:.3f} of 24")
stats = {}
for k, Ms in cls.items():
    q = sum(q90(M) for M in Ms) / max(1, len(Ms))
    lm = [lever_match(M) for M in Ms]; lm = [x for x in lm if x is not None]
    stats[k] = (q, sum(lm) / max(1, len(lm)), len(lm))
    print(f"{k:10s}: mean q90 = {q:.3f} ({q / mb:.2f}x baseline); lever match {sum(lm)}/{len(lm)} = {100 * sum(lm) / max(1, len(lm)):.0f}%")
nw = len(cls["weighted"])
res = {"K10a": None if nw < 15 else stats["weighted"][0] >= 1.5 * mb,
       "K10b": None if nw < 15 else stats["weighted"][1] >= 0.25}
print("\nSCORE:", {k: ("UNSCORED" if v is None else "HELD" if v else "LOST") for k, v in res.items()})
