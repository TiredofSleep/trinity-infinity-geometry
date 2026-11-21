"""every_loop_after.py -- read after the run of every_loop.py (not registered; description only).

  python -I every_loop_after.py PARTS_DIR

1. For every fresh curve above 5: is it the neighbour tau -> n tau, which multiplies its optimal partner's elongation
   by n exactly?
2. The optimal curves with a loop that lie above 5, and the largest elongation of an optimal curve with a loop.
3. The graded statistic q = (share above 5)/(share above 2), split by whether the fresh curve has rational torsion,
   with bootstrap standard errors over isogeny classes (as in the registered L2).
4. The 42 fresh curves whose BSD quotient is 1/4 of their partner's: the analytic order of Sha of both curves, from
   L''(1)/2! = Omega * Reg * prod(c_p) * Sha / |tors|^2. PARI's ellanalyticrank returns the derivative L^(r)(1)
   itself, so it is divided by r! here; ellbsd gives Omega * prod(c_p) / |tors|^2.
"""
import glob
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from every_loop import (BAD, FAIL, NBOOT, SEED, boot_q, clusters, get_pari, low_priority, reduce_forms,  # noqa: E402
                        relation_index, tau_of)


def main(parts):
    low_priority()
    rows = []
    for fn in sorted(glob.glob(os.path.join(parts, '*.json'))):
        rows += json.load(open(fn))['rows']
    G = np.array([r['G'] for r in rows], float)
    A, B, C = reduce_forms(G[:, 0, 0], G[:, 0, 1], G[:, 1, 1])
    y = np.sqrt(A * C - B * B) / A
    x = np.abs(B) / A
    num = np.array([r['num'] for r in rows])
    size = np.array([r['size'] for r in rows])
    tors = np.array([int(np.prod(r['tors'])) if r['tors'] else 1 for r in rows])
    keys = np.array([f"{r['N']}{r['cls']}" for r in rows])
    opt = {k: i for i, k in enumerate(keys) if num[i] == 1}
    fresh = num >= 2

    print("1. fresh curves above 5: the neighbour that multiplies the partner's elongation by n")
    tail = np.nonzero(fresh & (y > BAD))[0]
    exact, other = {}, {}
    for i in tail:
        j = opt[keys[i]]
        n = relation_index(tau_of(A[j], B[j], C[j]), x[i], y[i])
        mult = n >= 1 and abs(y[i] - n * y[j]) <= 1e-6 * y[i]
        (exact if mult else other).setdefault(n, []).append(f"{rows[i]['N']}{rows[i]['cls']}{rows[i]['num']}")
    for n in sorted(set(exact) | set(other)):
        print(f"   n = {n:>2}: elongation exactly n x partner's: {len(exact.get(n, [])):>3}; otherwise: "
              f"{len(other.get(n, [])):>2} {other.get(n, [])}")
    print(f"   total {len(tail)}: exactly n x partner's {sum(map(len, exact.values()))}")

    print("\n2. optimal curves with a loop (class size >= 2) above 5, thinnest first")
    ol = np.nonzero((num == 1) & (size >= 2))[0]
    for i in ol[np.argsort(-y[ol])][:12]:
        r = rows[i]
        mark = '  <- above 5' if y[i] > BAD else ''
        print(f"   {r['N']}{r['cls']}{r['num']}: elongation {y[i]:.3f}, torsion {r['tors']}, class size {r['size']}{mark}")
    nl = np.nonzero((num == 1) & (size == 1))[0]
    print(f"   largest elongation, optimal with a loop: {y[ol].max():.3f}; with no loop: {y[nl].max():.3f}; "
          f"optimal curves above 8: {int(np.sum(y[num == 1] > 8))}, of them with a loop: {int(np.sum(y[ol] > 8))}")

    print("\n3. the graded statistic split by torsion (bootstrap over isogeny classes, as in L2)")
    rng = np.random.default_rng(SEED)
    loopless = (num == 1) & (size == 1)
    br = boot_q(*clusters(keys[loopless], y[loopless]), rng)
    qr = np.mean(y[loopless] > BAD) / np.mean(y[loopless] > FAIL)
    for name, m in (("fresh, no rational torsion", fresh & (tors == 1)), ("fresh, rational torsion", fresh & (tors > 1)),
                    ("optimal, any loop", (num == 1) & (size >= 2))):
        q = np.mean(y[m] > BAD) / np.mean(y[m] > FAIL)
        bt = boot_q(*clusters(keys[m], y[m]), rng)
        se = np.std(br - bt, ddof=1)
        print(f"   {name:28s} n={m.sum():>6}  above 2 {np.mean(y[m] > FAIL):.4f}  above 5 {int(np.sum(y[m] > BAD)):>3}  "
              f"q = {q:.4f} (s.e. {np.std(bt, ddof=1):.4f});  no loop q = {qr:.4f};  difference {(qr - q) / se:+.1f} s.e.")

    print("\n4. the 42 curves whose BSD quotient is 1/4 of their partner's: analytic Sha of both")
    pari = get_pari()
    reg = lambda r: r['G'][0][0] * r['G'][1][1] - r['G'][0][1] ** 2
    flagged = [i for i in np.nonzero(fresh)[0]
               if abs(rows[i]['bsd'] * reg(rows[i]) / (rows[opt[keys[i]]]['bsd'] * reg(rows[opt[keys[i]]])) - 1) > 1e-6]
    pairs = {}
    for i in flagged:
        res = []
        for r in (rows[opt[keys[i]]], rows[i]):
            E = pari.ellinit(r['ai'])
            ar = pari.ellanalyticrank(E)
            res.append((int(ar[0]), float(ar[1]) / math.factorial(int(ar[0])) / (r['bsd'] * reg(r))))
        pairs[f"{rows[i]['N']}{rows[i]['cls']}{rows[i]['num']}"] = res
        print(f"   {rows[i]['N']}{rows[i]['cls']}1 -> {rows[i]['N']}{rows[i]['cls']}{rows[i]['num']}: "
              f"analytic rank {res[0][0]}, {res[1][0]}; analytic Sha {res[0][1]:.6f}, {res[1][1]:.6f}")
    ok = all(a[0] == 2 and b[0] == 2 and abs(a[1] - 1) < 1e-4 and abs(b[1] - 4) < 1e-4 for a, b in pairs.values())
    print(f"   all {len(pairs)}: rank 2 on both, analytic Sha 1 on the optimal curve and 4 on the fresh one: {ok}")


if __name__ == '__main__':
    main(sys.argv[1])
