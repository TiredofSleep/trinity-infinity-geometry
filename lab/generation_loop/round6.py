#!/usr/bin/env python3
"""
round6.py -- generation_loop/PREREG.md Round G6: where on the cube-flag Koide circle do the leptons sit?
Run from generation_loop/:  python3 round6.py     Prints ASCII only. Needs numpy and mpmath.
"""
import math
from fractions import Fraction
import numpy as np
import mpmath as mp
from search import delta_from_e_mu

mp.mp.dps = 40
E = mp.matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
F = mp.matrix([[mp.mpf(1) / 2, mp.mpf(1) / 2, 0], [mp.mpf(1) / 2, mp.mpf(1) / 2, 0], [0, 0, 0]])
B = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        B[i, j] = mp.mpf(1) / 3


def rho(phi):
    wf = mp.mpf(1) / 2 + mp.cos(phi) / 2
    wb = 1 + mp.sin(phi) / 2
    return (E + wf * F + wb * B) / (1 + wf + wb)


def delta_of(phi):
    ev, _ = mp.eigsy(rho(phi))
    v = [ev[i] for i in range(3)]
    A = sum(v) / 3
    cmax = max((x / A - 1) / mp.sqrt(2) for x in v)
    return mp.acos(cmax)


def purity(phi):
    r = rho(phi)
    return sum(r[i, j] * r[j, i] for i in range(3) for j in range(3))


def main():
    d_e, s_e = delta_from_e_mu()
    d_e = mp.mpf(d_e)
    # sanity: the whole circle is on the Koide cone
    worst = max(abs(purity(mp.mpf(k) * 2 * mp.pi / 64) - mp.mpf(2) / 3) for k in range(64))
    print(f"G6  purity on the flag circle: max |purity - 2/3| over 64 points = {mp.nstr(worst, 3)}")
    for deg in (0, -90, 90, 180):
        print(f"    phi = {deg:4d} deg -> delta = {float(mp.degrees(delta_of(mp.radians(deg)))):.4f} deg")
    sols = []
    grid = [mp.radians(x) for x in range(-180, 181, 2)]
    vals = [delta_of(p) - d_e for p in grid]
    for (p0, v0), (p1, v1) in zip(zip(grid, vals), zip(grid[1:], vals[1:])):
        if v0 == 0 or (v0 < 0) != (v1 < 0):
            s = mp.findroot(lambda p: delta_of(p) - d_e, (p0, p1), solver="bisect")
            h = mp.mpf("1e-12")
            slope = (delta_of(s + h) - delta_of(s - h)) / (2 * h)
            sols.append((s % (2 * mp.pi), abs(mp.mpf(s_e) / slope)))
    for s, sg in sols:
        print(f"    lepton point: phi_e = {mp.nstr(s, 15)} rad = {float(mp.degrees(s)):.6f} deg (+- {float(sg):.1e} rad);"
              f" weights (edge, face, body) = (1, {float(mp.mpf(1)/2 + mp.cos(s)/2):.6f}, {float(1 + mp.sin(s)/2):.6f})")
    in_range = any(math.radians(90) < float(s) < math.radians(180) for s, _ in sols)
    # grammar test (G2 grammar, unchanged)
    twopi = 2 * math.pi
    targets = [(float(s), 3 * float(sg)) for s, sg in sols]
    hits = []; n_rat = 0
    for q in range(1, 1001):
        n_rat += int(twopi * q)
        for t, e in targets:
            p = round(t * q)
            if p > 0 and abs(p / q - t) < e:
                hits.append(f"{p}/{q}")
    atoms = {"pi": math.pi, "atan(1/sqrt2)": math.atan(1 / math.sqrt(2)), "atan(sqrt2)": math.atan(math.sqrt(2)),
             "acos(1/3)": math.acos(1 / 3), "atan(1/2)": math.atan(0.5), "atan(1/3)": math.atan(1 / 3)}
    rats = sorted({Fraction(p, r) for p in range(-12, 13) for r in range(1, 37) if p != 0})
    rv = np.array([float(x) for x in rats]); n_comb = 0
    for xn, x in atoms.items():
        for yn in [None] + [n for n in atoms if n != xn]:
            bases = [(None, 0.0)] if yn is None else [(r, float(r) * atoms[yn]) for r in rats]
            for r2, b in bases:
                v = rv * x + b
                n_comb += int(np.count_nonzero((v > 0) & (v < twopi)))
                for t, e in targets:
                    for j in np.nonzero(np.abs(v - t) < e)[0]:
                        hits.append(f"{rats[j]}*{xn}" + ("" if yn is None else f" + {r2}*{yn}"))
    n = n_rat + n_comb
    expected = n * sum(2 * e for _, e in targets) / twopi
    print(f"    grammar: {n} candidates; expected chance hits {expected:.3f}; hits: {hits if hits else 'none'}")
    res = {"G6a": in_range, "G6b": not hits}
    print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})


if __name__ == "__main__":
    main()
