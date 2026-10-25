#!/usr/bin/env python3
"""digit_filter.py -- Round K8b: singular 5x5 magic square => low base-5 digit layer singular mod 5. ASCII only."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from four_in_five_core import det_bareiss, canon
from eccentric import load
HERE = os.path.dirname(os.path.abspath(__file__))
paths = [os.path.join(HERE, "..", "binary_magic", "void_lens", "squares5_annealed.txt")] + \
        [os.path.join(HERE, f) for f in ("squares5_fresh.txt", "squares5_fresh2.txt", "squares5_fresh3.txt")]
sq = {}
for p in paths:
    for M in load(p): sq.setdefault(canon(M), M)
n = sing = bsing = both = bad = 0
for M in sq.values():
    B = [[(x - 1) % 5 for x in r] for r in M]
    s = det_bareiss(M) == 0; b = det_bareiss(B) % 5 == 0
    n += 1; sing += s; bsing += b; both += s and b; bad += s and not b
print(f"{n} distinct 5x5 squares: singular {sing}; B singular mod 5 in {bsing} ({100 * bsing / n:.1f}%)")
print(f"singular with B invertible mod 5: {bad}; P(singular | B singular mod 5) = {both / bsing:.4f} "
      f"vs overall {sing / n:.4f} ({(both / bsing) / (sing / n):.1f}x)")
print("SCORE:", {"T1": "HELD" if bad == 0 else "LOST"})
