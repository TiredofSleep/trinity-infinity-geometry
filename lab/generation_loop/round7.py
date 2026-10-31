#!/usr/bin/env python3
"""
round7.py -- generation_loop/PREREG.md Round G7: do the colored families carry the color angle 2/9 exactly?
Run from generation_loop/:  python3 round7.py     Prints ASCII only. Needs numpy.
"""
import cmath, math
import numpy as np

def fit(light, middle, heavy):
    r = {0: math.sqrt(heavy), 1: math.sqrt(light), 2: math.sqrt(middle)}
    A = sum(r.values()) / 3
    c1 = sum(r[n] * cmath.exp(-2j * math.pi * n / 3) for n in range(3)) / 3
    return A, 2 * abs(c1) / A, cmath.phase(c1)

def mc(spec, nsamp=200000, seed=7):
    rng = np.random.default_rng(seed)
    draws = [rng.normal(v, s, nsamp) for v, s in spec]
    out = np.array([fit(*(d[i] for d in draws))[2] for i in range(nsamp)])
    return out

TARGET = 2 / 9
lep = fit(0.51099895, 105.6583755, 1776.93)
print(f"check: charged leptons -> amplitude b = {lep[1]:.6f} (sqrt2 = {math.sqrt(2):.6f}), delta = {lep[2]:.6f} (2/9 = {TARGET:.6f})")

scored = {"up-type (u, c, t)": [(2.14, 0.08), (1278.0, 13.0), (162500.0, 1800.0)],
          "down-type (d, s, b)": [(4.70, 0.05), (93.46, 0.58), (4200.0, 14.0)]}
res = {}
for (lab, spec), key in zip(scored.items(), ("G7a", "G7b")):
    A, b, d = fit(*(v for v, _ in spec))
    ds = mc(spec, nsamp=20000)
    sig = ds.std()
    z = (d - TARGET) / sig
    # mass-order labels (heavy n=0, light n=1, middle n=2) confine delta to (0, pi/3), so that is the chance range
    chance = min(1.0, 4 * sig / (math.pi / 3))
    print(f"{lab}: amplitude b = {b:.4f} (b^2 = {b*b:.4f}), delta = {d:.5f} +- {sig:.5f} rad = {math.degrees(d):.3f} deg;"
          f" vs 2/9: {z:+.1f} sigma (chance of landing within 2 sigma at random: {chance:.2%})")
    res[key] = abs(z) <= 2

print("not scored (other conventions, approximate inputs):")
for lab, (up, dn) in {"all six at one common scale (1-loop)": ((1.38, 638.0, 172100.0), (2.82, 57.0, 2860.0)),
                      "pole masses for c, b, t": ((2.14, 1670.0, 172520.0), (4.70, 93.46, 4780.0))}.items():
    for fam, m in (("up", up), ("down", dn)):
        A, b, d = fit(*m)
        print(f"   {lab:38s} {fam:5s}: b = {b:.4f}, delta = {d:.5f} rad ({math.degrees(d):.3f} deg)")

print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
