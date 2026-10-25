#!/usr/bin/env python3
"""
eccentric.py -- kernel_ledger/PREREG.md Round K7: concentric vs eccentric certificates for 5x5 kernels.
  concentric: a proper set of lines summing to a constant vector (a complementary pair: midpoint = the void
              center), or a factorised complement map of void index >= 1;
  eccentric:  two disjoint pairs of parallel lines with equal sums (a shared midpoint off the center), or one
              line equal to the average of two others.
Run from kernel_ledger/:  python3 eccentric.py        Prints ASCII only.
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from four_in_five_core import det_bareiss, canon, local_certs, global_index

HERE = os.path.dirname(os.path.abspath(__file__))

def eccentric(M):
    n = len(M); out = []
    for name, L in (("rows", [tuple(r) for r in M]), ("cols", [tuple(c) for c in zip(*M)])):
        add = lambda a, b: tuple(x + y for x, y in zip(L[a], L[b]))
        for (a, b), (c, d) in itertools.combinations(itertools.combinations(range(n), 2), 2):
            if len({a, b, c, d}) == 4 and add(a, b) == add(c, d): out.append((name, "pair", (a, b), (c, d)))
        for c in range(n):
            for a, b in itertools.combinations([x for x in range(n) if x != c], 2):
                if add(a, b) == tuple(2 * x for x in L[c]): out.append((name, "mid", c, (a, b)))
    return out

def load(path):
    out = []
    for l in open(path):
        r = list(map(int, l.split())); M = [r[5 * i:5 * i + 5] for i in range(5)]
        assert sorted(r) == list(range(1, 26)); out.append(M)
    return out

def main():
    global final
    old = {canon(M) for p in (os.path.join(HERE, "..", "binary_magic", "void_lens", "squares5_annealed.txt"),
                              os.path.join(HERE, "squares5_fresh.txt")) for M in load(p)}
    new = {}
    for M in load(os.path.join(HERE, "squares5_fresh2.txt")):
        k = canon(M)
        if k not in old: new.setdefault(k, M)

    def classify(sample):
        stats = {"n": 0, "sing": 0, "forced": 0, "acc": 0, "acc_ecc": 0, "acc_none": 0, "ecc_nonsing": 0}
        ex = []
        for M in sample:
            stats["n"] += 1; s = det_bareiss(M) == 0; e = eccentric(M)
            if e and not s: stats["ecc_nonsing"] += 1
            if not s: continue
            stats["sing"] += 1
            forced = bool(local_certs(M)) or (global_index(M, 26) or 0) >= 1
            if forced: stats["forced"] += 1; continue
            stats["acc"] += 1
            if e: stats["acc_ecc"] += 1; ex.append((M, e[0]))
            else: stats["acc_none"] += 1
        return stats, ex

    for label, sample in (("seen (Round 8c + K6)", [M for p in (os.path.join(HERE, "..", "binary_magic", "void_lens", "squares5_annealed.txt"),
                                                                os.path.join(HERE, "squares5_fresh.txt")) for M in load(p)]),
                          ("new (K7)", list(new.values()))):
        st, ex = classify(sample)
        print(f"{label}: {st}")
        for M, e in ex[:3]: print("   eccentric example:", e, M)
        if label.startswith("new"): final = st

    res = {"E1": final["ecc_nonsing"] == 0}
    res["E2"] = None if final["acc"] < 8 else 0.05 <= final["acc_ecc"] / final["acc"] <= 0.40
    res["E3"] = None if final["acc"] < 8 else final["acc_none"] / final["acc"] > 0.5
    print("\nSCORE:", {k: ("UNSCORED" if v is None else "HELD" if v else "LOST") for k, v in res.items()})

if __name__ == "__main__":
    main()
