"""watkins_compare.py -- Cremona's rank-2 lattices of prime conductor against Watkins (2006), section 6.4.

  python -I watkins_compare.py OUT_DIR/all_rows.json

Watkins placed the Mordell-Weil lattices of 2 143 079 rank-2 curves of prime conductor below 10^10 (the Stein-Watkins
database) in the fundamental domain of SL2(Z), with x in [0, 1/2] and y the elongation. He found 93.5% with y >= 1,
35.4% with y >= 2, 9.4% with y >= 4, 1.7% with y >= 8 and 0.2% with y >= 16, against (3/pi)/Y for the uniform
(Haar) law, and x skewed toward 1/2 (his Table 1). His footnote 9: his prime-conductor curves have |disc| = N with
few exceptions. This script makes the same counts for every optimal rank-2 curve of prime conductor below 500 000 in
Cremona's tables, and splits them by the exponent k in |disc| = N^k, by conductor and by the period lattice's shape.
Description only: none of this was registered.
"""
import json
import math
import sys

import numpy as np

WATKINS_Y = {1: 0.935, 2: 0.354, 4: 0.094, 8: 0.017, 16: 0.002}
WATKINS_X = [0.090, 0.096, 0.098, 0.099, 0.100, 0.100, 0.102, 0.105, 0.106, 0.105]


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17):          # deterministic for n < 3.4e14
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def reduce_forms(A, B, C):
    for _ in range(300):
        sw = A > C
        A[sw], C[sw] = C[sw], A[sw]
        k = np.round(B / A)
        if not k.any():
            break
        C, B = C - 2 * k * B + k * k * A, B - k * A
    sw = A > C
    A[sw], C[sw] = C[sw], A[sw]
    return A, B, C


def main(path):
    rows = [r for r in json.load(open(path)) if r['r'] == 2]
    N = np.array([r['N'] for r in rows])
    G = np.array([r['G'] for r in rows], float)
    A, B, C = reduce_forms(G[:, 0, 0].copy(), G[:, 0, 1].copy(), G[:, 1, 1].copy())
    x, y = np.abs(B) / A, np.sqrt(A * C - B * B) / A
    prime = np.array([is_prime(int(n)) for n in N])
    k = np.array([r['logdisc'] for r in rows]) / np.log(N)
    imtau = np.array([r['tau'][1] for r in rows])
    tors = np.array([int(np.prod(r['tors'])) if r['tors'] else 1 for r in rows])
    iso = np.array([r['iso'] for r in rows])

    def shares(m):
        return '  '.join(f"y>={Y}: {np.mean(y[m] >= Y):.4f}" for Y in WATKINS_Y)

    print(f"optimal rank-2 curves: {len(rows)}; of prime conductor: {prime.sum()}")
    print(f"  uniform law (3/pi)/Y      " + '  '.join(f"y>={Y}: {min(1, 3 / math.pi / Y):.4f}" for Y in WATKINS_Y))
    print(f"  Watkins, prime N < 1e10   " + '  '.join(f"y>={Y}: {v:.4f}" for Y, v in WATKINS_Y.items()))
    print(f"  Cremona, prime N < 5e5    {shares(prime)}")
    print(f"  Cremona, all N < 5e5      {shares(np.ones(len(rows), bool))}")

    kk = np.rint(k)
    print("\nprime conductor, by the exponent k in |disc| = N^k:")
    for kv in sorted(set(kk[prime].astype(int))):
        m = prime & (kk == kv)
        if m.sum() >= 20:
            print(f"  k = {kv}: n = {m.sum():>5}  {shares(m)}")
    print(f"  (k is an integer to within {np.abs(k[prime] - kk[prime]).max():.1e} on every prime-conductor curve)")

    print("\nprime conductor with |disc| = N, by conductor band:")
    for lo, hi in ((0, 5e4), (5e4, 1e5), (1e5, 2e5), (2e5, 3e5), (3e5, 4e5), (4e5, 5e5)):
        m = prime & (kk == 1) & (N >= lo) & (N < hi)
        print(f"  {int(lo):>6}-{int(hi) - 1:<6} n = {m.sum():>5}  {shares(m)}")

    print("\nprime conductor, by the shape of the curve's own period lattice (Im tau, fifths):")
    q = np.quantile(imtau[prime], [0, .2, .4, .6, .8, 1])
    for a, b in zip(q[:-1], q[1:]):
        m = prime & (imtau >= a) & (imtau <= b)
        print(f"  Im tau {a:6.3f}-{b:7.3f}: n = {m.sum():>5}  y>=2: {np.mean(y[m] >= 2):.4f}")

    print("\nhorizontal distribution for y >= 1 (Watkins's Table 1), prime conductor:")
    m = prime & (y >= 1)
    h = np.histogram(x[m], bins=np.linspace(0, 0.5, 11))[0] / m.sum()
    print("  x bin        " + ' '.join(f"{0.05 * i:.2f}" for i in range(10)))
    print("  Watkins      " + ' '.join(f"{v:.3f}" for v in WATKINS_X))
    print(f"  Cremona      " + ' '.join(f"{v:.3f}" for v in h) + f"   (n = {m.sum()}, s.e. per bin about "
          f"{math.sqrt(0.1 * 0.9 / m.sum()):.3f})")
    m = y >= 1
    h = np.histogram(x[m], bins=np.linspace(0, 0.5, 11))[0] / m.sum()
    print(f"  Cremona, all " + ' '.join(f"{v:.3f}" for v in h) + f"   (every conductor, n = {m.sum()})")
    print(f"  uniform      " + ' '.join(f"{0.1:.3f}" for _ in range(10)))
    print(f"\nprime conductor: torsion trivial in {np.mean(tors[prime] == 1):.4f}, class size 1 in "
          f"{np.mean(iso[prime] == 1):.4f}")


if __name__ == '__main__':
    main(sys.argv[1])
