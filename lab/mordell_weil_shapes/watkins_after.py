"""watkins_after.py -- read after round 10 (not registered; description and checks only).

  python -I watkins_after.py RESULTS.json [n_bsd]

1. Are the lattices right at large conductor? For n_bsd curves of stratum D (half at random, half the thinnest), the
   analytic order of Sha from the BSD formula, L''(1)/2! = Omega * Reg * prod(c_p) * Sha / |tors|^2, with Reg from the
   generators found here (PARI's ellanalyticrank and ellbsd). A basis gives a square; generators spanning a sublattice
   of index k would give Sha divided by k^2.
2. How could 35.4% arise? The shapes of the same Gram matrices with the off-diagonal entry doubled, [[A, 2B], [2B, C]]
   in the reduced basis (the pairing taken as h(P + Q) - h(P) - h(Q), without the 1/2), and halved, against Watkins's
   shares and his Table 1.
"""
import json
import math
import random
import sys

WATKINS = {1: 0.935, 2: 0.354, 4: 0.094, 8: 0.017, 16: 0.002}
WATKINS_X = [0.090, 0.096, 0.098, 0.099, 0.100, 0.100, 0.102, 0.105, 0.106, 0.105]


def reduce_form(A, B, C):
    for _ in range(400):
        if A > C:
            A, C = C, A
        k = round(B / A)
        if k == 0:
            break
        C, B = C - 2 * k * B + k * k * A, B - k * A
    if A > C:
        A, C = C, A
    return A, B, C


def xy(A, B, C):
    A, B, C = reduce_form(A, B, C)
    d = A * C - B * B
    if d <= 0:
        return None
    return abs(B) / A, math.sqrt(d) / A


def report(name, shapes):
    ok = [s for s in shapes if s is not None]
    line = f"  {name:44s} n={len(ok):>5} (degenerate {len(shapes) - len(ok)})  " + '  '.join(
        f"y>={Y}: {sum(1 for _, y in ok if y >= Y) / len(ok):.4f}" for Y in WATKINS)
    print(line)
    big = [x for x, y in ok if y >= 1]
    h = [0] * 10
    for x in big:
        h[min(int(x / 0.05), 9)] += 1
    print(f"  {'':44s} x by tenths (y >= 1): " + ' '.join(f"{c / len(big):.3f}" for c in h))


def main(path, n_bsd=30):
    res = [r for r in json.load(open(path)) if r.get('ok')]
    try:
        from cypari import pari
    except ImportError:
        import cypari2
        pari = cypari2.Pari()
    pari.allocatemem(2 * 10 ** 9)

    print("1. the BSD formula at large conductor (stratum D): analytic order of Sha from the generators found here")
    D = [r for r in res if r['stratum'] == 'D']
    random.seed(20261124)
    pick = random.sample(D, n_bsd // 2) + sorted(D, key=lambda r: -r['y'])[:n_bsd - n_bsd // 2]
    worst = 0.0
    for r in pick:
        E = pari.ellinit(r['ai'])
        Em = pari(f"ellminimalmodel(ellinit({r['ai']}))")
        reg = r['G'][0][0] * r['G'][1][1] - r['G'][0][1] ** 2
        ar = pari.ellanalyticrank(Em)
        sha = float(ar[1]) / math.factorial(int(ar[0])) / (float(pari.ellbsd(Em)) * reg)
        nearest = round(math.sqrt(sha)) ** 2 if sha > 0.5 else 0
        worst = max(worst, abs(sha - nearest))
        print(f"   N = {r['N']}: elongation {r['y']:.3f}, analytic rank {int(ar[0])}, analytic Sha {sha:.6f}")
    print(f"   largest distance from a perfect square: {worst:.2e}")

    print("\n2. the shares under three readings of the height pairing (stratum U, Watkins's population)")
    U = [r for r in res if r['stratum'] == 'U']
    true_s, dbl, half = [], [], []
    for r in U:
        A, B, C = reduce_form(r['G'][0][0], r['G'][0][1], r['G'][1][1])
        true_s.append(xy(A, B, C))
        dbl.append(xy(A, 2 * B, C))
        half.append(xy(A, B / 2, C))
    print(f"  {'Watkins (2006), section 6.4':44s}          " + '  '.join(f"y>={Y}: {v:.4f}" for Y, v in WATKINS.items()))
    print(f"  {'':44s} x by tenths (y >= 1): " + ' '.join(f"{v:.3f}" for v in WATKINS_X))
    report("the pairing <P,Q> = (h(P+Q) - h(P) - h(Q))/2", true_s)
    report("off-diagonal doubled, h(P+Q) - h(P) - h(Q)", dbl)
    report("off-diagonal halved", half)
    print(f"  {'the uniform law':44s}          " + '  '.join(f"y>={Y}: {min(1, 3 / math.pi / Y):.4f}" for Y in WATKINS))


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 30)
