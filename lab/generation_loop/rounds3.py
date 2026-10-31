#!/usr/bin/env python3
"""
rounds3.py -- generation_loop/PREREG.md Rounds G3-G5. Run from generation_loop/:  python3 rounds3.py
Prints ASCII only. Needs numpy and mpmath (search.py supplies delta_e and the G2 grammar).
G3: weighted mixtures of cube-axis states (pairs; 'a cone and two half cones' = weights 1, 1/2, 1/2; equal triples)
G4: the G2 grammar against the unrolled-cone targets (delta / sqrt2 and delta * sqrt2)
G5: the neutrino angle under P2's solution, against Brannen's delta_e + pi/12
"""
import itertools, math
from fractions import Fraction
import numpy as np
from search import delta_from_e_mu

SQ2 = math.sqrt(2)
DELTA_E, SIG_E = delta_from_e_mu()


def canon_delta(vals):
    """Angle in [0, pi/3] of three sqrt-masses on the Koide cone (labels: light n=1, middle n=2, heavy n=0)."""
    v = np.asarray(vals, float)
    A = v.mean()
    c = (v / A - 1) / SQ2
    return math.acos(max(-1.0, min(1.0, c.max())))


# ------------------------------------------------------------------ G3
def axes():
    out = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    out += [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
    out += [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)]
    return out


def proj(v):
    n2 = sum(x * x for x in v)
    return [[Fraction(v[i] * v[j], n2) for j in range(3)] for i in range(3)]


def mix(ps, ws):
    tot = sum(ws)
    return [[sum(w * p[i][j] for p, w in zip(ps, ws)) / tot for j in range(3)] for i in range(3)]


def purity(r):
    return sum(r[i][j] * r[j][i] for i in range(3) for j in range(3))


def kind(v):
    nz = sum(1 for x in v if x)
    return {1: "edge", 2: "face", 3: "body"}[nz]


def g3():
    ax = axes(); P = [proj(v) for v in ax]
    res = {}
    # pairs, equal weights
    pair_hits, pair_bad = [], 0
    for a, b in itertools.combinations(range(13), 2):
        r = mix([P[a], P[b]], [Fraction(1), Fraction(1)])
        if purity(r) == Fraction(2, 3):
            cos2 = Fraction(sum(x * y for x, y in zip(ax[a], ax[b])) ** 2,
                            sum(x * x for x in ax[a]) * sum(y * y for y in ax[b]))
            ev = np.linalg.eigvalsh(np.array(r, float))
            d = canon_delta(ev)
            pair_hits.append((kind(ax[a]), kind(ax[b]), d))
            if cos2 != Fraction(1, 3) or abs(d - math.pi / 12) > 1e-12:
                pair_bad += 1
    kinds = sorted({tuple(sorted(h[:2])) for h in pair_hits})
    print(f"G3  pairs at purity 2/3: {len(pair_hits)} (axis kinds {kinds}); all at the magic angle and at 15 deg: {pair_bad == 0}")
    res["G3a"] = len(pair_hits) > 0 and pair_bad == 0
    # 'a cone and two half cones': weight 1 on a, 1/2 on b and c; and equal triples
    for label, wfun, combos in (
            ("cone + two half cones (1, 1/2, 1/2)", lambda: [Fraction(1), Fraction(1, 2), Fraction(1, 2)],
             [(a, b, c) for a in range(13) for b, c in itertools.combinations([x for x in range(13) if x != a], 2)]),
            ("equal triples", lambda: [Fraction(1)] * 3, list(itertools.combinations(range(13), 3)))):
        hits = []
        for t in combos:
            r = mix([P[i] for i in t], wfun())
            if purity(r) == Fraction(2, 3):
                ev = np.linalg.eigvalsh(np.array(r, float))
                hits.append((t, ev, canon_delta(ev)))
        nonzero = [h for h in hits if h[1].min() > 1e-12]
        ds = sorted({round(math.degrees(h[2]), 6) for h in hits})
        print(f"    {label}: {len(combos)} mixtures, {len(hits)} at purity 2/3, {len(nonzero)} with three nonzero masses;"
              f" angles (deg): {ds[:10]}{' ...' if len(ds) > 10 else ''}")
        if label.startswith("cone"):
            res["G3b"] = len(nonzero) > 0
            for t, ev, d in nonzero[:3]:
                kinds3 = [kind(ax[i]) for i in t]
                print(f"      e.g. weight 1 on {kinds3[0]}, 1/2 on {kinds3[1]} and {kinds3[2]}: delta = {math.degrees(d):.4f} deg,"
                      f" sqrt-mass ratios {np.round(np.sort(ev) / np.sort(ev)[0], 4)}")
        res.setdefault("_all", []).extend(hits)
    best = min(abs(h[2] - DELTA_E) for h in res["_all"]) if res["_all"] else float("inf")
    print(f"    closest purity-2/3 mixture to delta_e = {math.degrees(DELTA_E):.4f} deg: {math.degrees(best):.4f} deg away")
    res["G3c"] = best > 1e-6
    del res["_all"]
    return res


# ------------------------------------------------------------------ G4
def g4():
    from fractions import Fraction as F
    twopi = 2 * math.pi
    base = sorted({(s * DELTA_E + k * twopi / 3) % twopi for s in (1, -1) for k in range(3)})
    tol = 3 * SIG_E
    targets = [(t / SQ2, tol / SQ2) for t in base] + [(t * SQ2, tol * SQ2) for t in base]
    targets = [(t, e) for t, e in targets if 0 < t < twopi]
    hits = []; n_rat = 0
    for q in range(1, 1001):
        n_rat += int(twopi * q)
        for t, e in targets:
            p = round(t * q)
            if p > 0 and abs(p / q - t) < e:
                hits.append((f"{p}/{q}", t))
    atoms = {"pi": math.pi, "atan(1/sqrt2)": math.atan(1 / SQ2), "atan(sqrt2)": math.atan(SQ2),
             "acos(1/3)": math.acos(1 / 3), "atan(1/2)": math.atan(0.5), "atan(1/3)": math.atan(1 / 3)}
    rats = sorted({F(p, r) for p in range(-12, 13) for r in range(1, 37) if p != 0})
    rv = np.array([float(x) for x in rats]); n_comb = 0
    for xn, x in atoms.items():
        for yn in [None] + [n for n in atoms if n != xn]:
            bases = [(None, 0.0)] if yn is None else [(r, float(r) * atoms[yn]) for r in rats]
            for r2, b in bases:
                vals = rv * x + b
                n_comb += int(np.count_nonzero((vals > 0) & (vals < twopi)))
                for t, e in targets:
                    for j in np.nonzero(np.abs(vals - t) < e)[0]:
                        hits.append((f"{rats[j]}*{xn}" + ("" if yn is None else f" + {r2}*{yn}"), t))
    n = n_rat + n_comb
    expected = n * sum(2 * e for _, e in targets) / twopi
    print(f"G4  unrolled-cone targets: {len(targets)}; candidates {n}; expected chance hits {expected:.3f}")
    for h in hits:
        print(f"    HIT: {h[0]} near target {h[1]:.12f}")
    if not hits:
        print("    no candidate within tolerance")
    return {"G4a": not hits}


# ------------------------------------------------------------------ G5
def g5(nsamp=20000, seed=5):
    rng = np.random.default_rng(seed)
    d21 = rng.normal(7.42e-5, 0.21e-5, nsamp); d31 = rng.normal(2.511e-3, 0.027e-3, nsamp)

    def solve(a, b):
        lo, hi = 1e-12, 0.01
        g = lambda m1: (m1 + math.sqrt(m1 * m1 + a) + math.sqrt(m1 * m1 + b)) / \
            (-math.sqrt(m1) + math.sqrt(math.sqrt(m1 * m1 + a)) + math.sqrt(math.sqrt(m1 * m1 + b))) ** 2 - 2 / 3
        for _ in range(80):
            mid = (lo + hi) / 2
            if g(mid) < 0: lo = mid
            else: hi = mid
        m1 = (lo + hi) / 2
        return [-math.sqrt(m1), math.sqrt(math.sqrt(m1 * m1 + a)), math.sqrt(math.sqrt(m1 * m1 + b))]

    central = canon_delta(solve(7.42e-5, 2.511e-3))
    ds = np.array([canon_delta(solve(a, b)) for a, b in zip(d21, d31)])
    diff = central - DELTA_E; sd = ds.std()
    z = (diff - math.pi / 12) / sd
    print(f"G5  delta_nu = {math.degrees(central):.4f} deg (+- {math.degrees(sd):.4f}); delta_e = {math.degrees(DELTA_E):.4f} deg")
    print(f"    delta_nu - delta_e = {math.degrees(diff):.4f} deg vs pi/12 = 15 deg: {z:+.2f} sigma")
    return {"G5a": abs(z) <= 3}


if __name__ == "__main__":
    res = g3(); res.update(g4()); res.update(g5())
    print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
