#!/usr/bin/env python3
"""
search.py -- generation_loop/PREREG.md Rounds G1 and G2. Run from generation_loop/:  python3 search.py
Prints ASCII only. Needs numpy and mpmath.
G1: do sums of cube rotations give Koide spectra (the 45 deg cone), and the lepton hierarchy?
G2: is Brannen's angle delta a simple geometric angle at the 1e-9 level?
"""
import itertools, math
from fractions import Fraction
import numpy as np
import mpmath as mp

# ------------------------------------------------------------------ G1
def cube_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for r, (c, s) in enumerate(zip(perm, signs)):
                M[r, c] = s
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    return out

def g1():
    R = cube_rotations()
    assert len(R) == 24
    sym = [(g + g.T) for g in R]            # 2 * symmetric part (integer); scale drops out of Q and ratios
    target = (math.sqrt(105.6583755 / 0.51099895), math.sqrt(1776.93 / 0.51099895))
    n_mats = 0; exact = set(); best = None; near = 0
    for k in (1, 2, 3):
        for T in itertools.combinations(range(24), k):
            for eps in itertools.product((1, -1), repeat=k):
                S = sum(e * sym[i] for e, i in zip(eps, T))
                n_mats += 1
                tr = int(np.trace(S))
                if tr == 0:
                    continue
                Q = Fraction(int(np.sum(S * S)), tr * tr)          # tr(S^2)/(tr S)^2, exact
                if Q != Fraction(2, 3):
                    continue
                ev = np.sort(np.abs(np.linalg.eigvalsh(S.astype(float))))
                key = tuple(np.round(ev / ev[-1], 9))
                exact.add(key)
                if ev[0] > 1e-12:
                    r = (ev[1] / ev[0], ev[2] / ev[0])
                    err = max(abs(r[0] / target[0] - 1), abs(r[1] / target[1] - 1))
                    if best is None or err < best[0]:
                        best = (err, r, key)
                    near += err < 0.01
    print(f"G1  matrices scanned: {n_mats}; distinct exact-Koide spectra (up to scale): {len(exact)}")
    for key in sorted(exact)[:8]:
        print(f"    exact-Koide spectrum |eigenvalues| / largest: {key}")
    if best:
        print(f"    closest to the lepton ratios ({target[0]:.2f}, {target[1]:.2f}): "
              f"({best[1][0]:.3f}, {best[1][1]:.3f}), worst relative miss {best[0]:.1%}")
    res = {"G1a": len(exact) > 0, "G1b": near == 0}
    return res

# ------------------------------------------------------------------ G2
def delta_from_e_mu():
    mp.mp.dps = 40
    me, mmu, dmu = mp.mpf('0.51099895000'), mp.mpf('105.6583755'), mp.mpf('0.0000023')
    c = lambda d, n: 1 + mp.sqrt(2) * mp.cos(d + 2 * mp.pi * n / 3)
    f = lambda d, mm: c(d, 2) / c(d, 1) - mp.sqrt(mm / me)
    d0 = mp.findroot(lambda d: f(d, mmu), mp.mpf(2) / 9)
    d1 = mp.findroot(lambda d: f(d, mmu + dmu), mp.mpf(2) / 9)
    return float(d0), float(abs(d1 - d0))

def g2():
    d, sig = delta_from_e_mu()
    tol = 3 * sig
    twopi = 2 * math.pi
    targets = sorted({(s * d + k * twopi / 3) % twopi for s in (1, -1) for k in range(3)})
    print(f"G2  delta = {d:.10f} +- {sig:.1e} (from electron and muon, Koide exact); tolerance {tol:.1e}")
    hits = []
    # pure rationals p/q
    n_rat = 0
    for q in range(1, 1001):
        n_rat += int(twopi * q)
        for t in targets:
            p = round(t * q)
            if p > 0 and abs(p / q - t) < tol:
                hits.append((f"{p}/{q}", p / q, t))
    # rational combinations of geometric atoms
    atoms = {"pi": math.pi, "atan(1/sqrt2)": math.atan(1 / math.sqrt(2)), "atan(sqrt2)": math.atan(math.sqrt(2)),
             "acos(1/3)": math.acos(1 / 3), "atan(1/2)": math.atan(0.5), "atan(1/3)": math.atan(1 / 3)}
    rats = sorted({Fraction(p, r) for p in range(-12, 13) for r in range(1, 37) if p != 0})
    rv = np.array([float(x) for x in rats])
    n_comb = 0
    names = list(atoms)
    for xn in names:
        x = atoms[xn]
        for yn in [None] + [n for n in names if n != xn]:
            bases = [(None, 0.0)] if yn is None else [(r, float(r) * atoms[yn]) for r in rats]
            for r2, b in bases:
                vals = rv * x + b
                n_comb += int(np.count_nonzero((vals > 0) & (vals < twopi)))
                for t in targets:
                    diff = np.abs(vals - t)
                    for j in np.nonzero(diff < tol)[0]:
                        expr = f"{rats[j]}*{xn}" + ("" if yn is None else f" + {r2}*{yn}")
                        hits.append((expr, vals[j], t))
    n_total = n_rat + n_comb
    expected = n_total * len(targets) * 2 * tol / twopi
    print(f"    candidates: {n_rat} pure rationals + {n_comb} atom combinations = {n_total}; "
          f"expected chance hits {expected:.3f}")
    for expr, v, t in hits:
        print(f"    HIT: {expr} = {v:.12f} vs target {t:.12f} (miss {abs(v - t):.1e} = {abs(v - t) / sig:.1f} sigma)")
    if not hits:
        print("    no candidate within tolerance")
    miss29 = min(abs(2 / 9 - t) for t in targets)
    print(f"    2/9 misses the nearest target by {miss29:.2e} ({miss29 / sig:.0f} sigma)")
    return {"G2a": len(hits) == 0, "G2b": miss29 > 1e-7}

if __name__ == "__main__":
    res = g1()
    res.update(g2())
    print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
