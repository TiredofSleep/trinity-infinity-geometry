#!/usr/bin/env python3
"""attractor_null_census.py -- is the alpha = 1/2 attractor's closed form evidence, or a readout?

Canon (J16 06_attractor_closed_form.py): iterate p -> 1/2 fuse(p,p,TSML) + 1/2 fuse(p,p,BHML) on
the ten symbols; every start lands on the 4-core {V,H,Br,R} = {0,7,8,9}, with H/Br = 1 + sqrt(3)
exactly, in a quartic field with Galois group D4 (LMFDB 4.2.10224.1).

The derivation only uses the 4x4 top blocks of the two tables. TSML's block is fixed by its
principled axioms S2-S4 (0 near-absorbing, 7 absorbing, diagonal -> 7). BHML's block has six
free cells: 7*7, 7*8, 7*9 (Rule 7, the successor) and 8*8, 8*9, 9*9 (Rule 89, listed).
This script runs an EXHAUSTIVE census -- not a sample -- of every BHML top block with values in
the 4-core (so the core stays closed), and for each unique attractor identifies the exact field
(minimal polynomials by 120-digit PSLQ) and its Galois group:

  NULL A -- the three Rule-89 cells free (4^3 = 64 tables)
  NULL B -- all six top cells free        (4^6 = 4096 tables)

    python verification/attractor_null_census.py      (several minutes)

See 04_meta/FOUNDATION_NULL_MODEL_AUDIT.md.
"""
import itertools
import time
from collections import Counter

import mpmath as mp
import numpy as np
from sympy import Poly, discriminant, factor_list, symbols
from sympy.polys.numberfields.galoisgroups import galois_group

from foundation_null_model import BHML, TSML

X = symbols("x")
CORE = [0, 7, 8, 9]
IX = {c: k for k, c in enumerate(CORE)}
T4 = np.array([[IX[TSML[a][b]] for b in CORE] for a in CORE])
B4 = np.array([[IX[BHML[a][b]] for b in CORE] for a in CORE])
TOP = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]      # 7*7, 7*8, 7*9, 8*8, 8*9, 9*9
RULE89 = [(2, 2), (2, 3), (3, 3)]


def fuse10(p, tab):
    r = np.zeros(10)
    for a in range(10):
        for b in range(10):
            r[tab[a][b]] += p[a] * p[b]
    return r


def refine(p0, Tt, Bt, alpha, dps=120):
    """Newton-polish a numerical fixed point to `dps` digits."""
    mp.mp.dps = dps
    a = mp.mpf(alpha)

    def F(v, h, b):
        p = [v, h, b, 1 - v - h - b]
        out = [mp.mpf(0)] * 4
        for i in range(4):
            for j in range(4):
                out[Tt[i][j]] += a * p[i] * p[j]
                out[Bt[i][j]] += (1 - a) * p[i] * p[j]
        return [out[0] - v, out[1] - h, out[2] - b]
    s = mp.findroot(F, [mp.mpf(float(p0[0])), mp.mpf(float(p0[1])), mp.mpf(float(p0[2]))])
    return [s[0], s[1], s[2], 1 - s[0] - s[1] - s[2]]


def minpoly(z, maxdeg=8):
    """Minimal polynomial of z over Q (degree <= maxdeg), by PSLQ; None if not found."""
    if abs(z) < mp.mpf(10) ** (-mp.mp.dps + 10):
        return Poly(X, X)
    c = mp.findpoly(z, maxdeg, maxcoeff=10 ** 9, maxsteps=200000)
    if c is None:
        return None
    for f, _ in factor_list(Poly([int(t) for t in c], X).as_expr())[1]:
        fp = Poly(f, X)
        if abs(mp.polyval([mp.mpf(int(t)) for t in fp.all_coeffs()], z)) < mp.mpf(10) ** (-mp.mp.dps // 2):
            return fp
    return None


def gal_name(P):
    d = P.degree()
    if d <= 1:
        return "Q"
    if d == 2:
        return "C2"
    if d > 6:
        return f"deg{d} (group not computed)"
    G, _ = galois_group(P)
    o = G.order()
    names = {(3, 3): "C3", (3, 6): "S3", (4, 8): "D4", (4, 12): "A4", (4, 24): "S4"}
    if (d, o) == (4, 4):
        return "C4" if G.is_cyclic else "V4"
    return names.get((d, o), f"deg{d}/|G|={o}")


def identify(pt):
    """(field degree, Galois group, minimal polynomial) -- degree = max over the 4 coordinates."""
    polys = [minpoly(z) for z in pt]
    if any(P is None for P in polys):
        return (">8", None, None)
    Pk = max(polys, key=lambda P: P.degree())
    return (Pk.degree(), gal_name(Pk), Pk)


def census(cells, label):
    t0 = time.time()
    choices = list(itertools.product(range(4), repeat=len(cells)))
    K = len(choices)
    Bs = np.repeat(B4[None], K, axis=0)
    for k, ch in enumerate(choices):
        for (i, j), v in zip(cells, ch):
            Bs[k, i, j] = v
            Bs[k, j, i] = v
    OT, OB = np.eye(4)[T4], np.eye(4)[Bs]
    starts = [np.full(4, .25), np.array([.7, .1, .1, .1]), np.array([.1, .1, .1, .7]), np.array([.1, .1, .7, .1])]
    finals = []
    for s in starts:
        P = np.repeat(s[None], K, axis=0)
        diff = np.full(K, np.inf)
        active = np.arange(K)
        for it in range(20000):
            Pa = P[active]
            O = np.einsum("ki,kj->kij", Pa, Pa)
            Pn = 0.5 * np.einsum("kij,ijx->kx", O, OT) + 0.5 * np.einsum("kij,kijx->kx", O, OB[active])
            Pn /= Pn.sum(axis=1, keepdims=True)
            diff[active] = np.max(np.abs(Pn - Pa), axis=1)
            P[active] = Pn
            if it > 200:
                active = active[diff[active] >= 1e-14]
                if active.size == 0:
                    break
        finals.append((P.copy(), diff < 1e-10))
    res, gal, cache, canon_like = Counter(), Counter(), {}, 0
    for k in range(K):
        pts = [f[0][k] for f in finals]
        if not all(f[1][k] for f in finals):
            res["no fixed-point attractor (cycle / not converged)"] += 1
            continue
        if max(np.max(np.abs(pts[0] - q)) for q in pts[1:]) > 1e-7:
            res["several attractors (start-dependent)"] += 1
            continue
        key = tuple(np.round(pts[0], 9))
        if key not in cache:
            try:
                cache[key] = identify(refine(pts[0], T4, Bs[k], 0.5))
            except Exception:
                cache[key] = ("refine-failed", None, None)
        d, g, _ = cache[key]
        res[f"unique attractor, field degree {d}"] += 1
        if g:
            gal[g] += 1
        if d == 4 and g == "D4":
            canon_like += 1
    print(f"\n== {label}: {K} tables  ({time.time() - t0:.0f}s, {len(cache)} distinct attractors) ==")
    for kk, vv in sorted(res.items(), key=lambda t: -t[1]):
        print(f"   {vv:5d}  {kk}")
    print("   Galois groups (unique attractors):", dict(gal))
    print(f"   quartic + D4 like canon: {canon_like}/{K} = {canon_like / K:.3f}")
    return res, gal, canon_like


if __name__ == "__main__":
    print("=" * 74)
    print("ATTRACTOR NULL CENSUS -- is the alpha=1/2 closed form evidence, or a readout?")
    print("=" * 74)
    rng = np.random.default_rng(1)
    ends = []
    for _ in range(5):
        p = rng.dirichlet(np.ones(10))
        for _ in range(3000):
            p = 0.5 * fuse10(p, TSML) + 0.5 * fuse10(p, BHML)
            p = p / p.sum()
        ends.append(p)
    off = max(1 - sum(e[c] for c in CORE) for e in ends)
    spread = float(np.max(np.ptp(ends, axis=0)))
    assert off < 1e-12 and spread < 1e-9
    print(f"canon: 5 random starts on all ten symbols -> one attractor (spread {spread:.1e}), "
          f"mass off the 4-core {off:.1e}")
    canon_pt = refine(ends[0][CORE], T4, B4, 0.5)
    deg, gname, Pk = identify(canon_pt)
    disc = discriminant(Pk.as_expr(), X)
    assert (deg, gname) == (4, "D4") and abs(canon_pt[1] / canon_pt[2] - (1 + mp.sqrt(3))) < mp.mpf(10) ** -100
    print(f"canon alpha=1/2: H/Br = 1+sqrt(3) | field degree {deg}, Galois {gname} | minpoly {Pk.as_expr()} "
          f"| disc {disc} = -10224*16^2 (LMFDB 4.2.10224.1)")
    for al in ["1/3", "2/5", "3/5", "2/3"]:
        a = mp.mpf(int(al.split("/")[0])) / int(al.split("/")[1])
        p = np.full(4, 0.25)
        for _ in range(5000):
            o = np.zeros(4)
            for i in range(4):
                for j in range(4):
                    o[T4[i][j]] += float(a) * p[i] * p[j]
                    o[B4[i][j]] += (1 - float(a)) * p[i] * p[j]
            p = o / o.sum()
        d2, g2, _ = identify(refine(p, T4, B4, a))
        print(f"   canon at alpha={al}: field degree {d2}")
    census(RULE89, "NULL A: Rule 89 top cells (8*8, 8*9, 9*9) free")
    census(TOP, "NULL B: all six BHML top cells free")
    print("=" * 74)
