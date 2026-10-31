#!/usr/bin/env python3
"""
round8.py -- generation_loop/PREREG.md Round G8: Koide on the cross-family quark triplets (-s, c, b) and (c, b, t).
Run from generation_loop/:  python3 round8.py     Prints ASCII only. Needs numpy.
"""
import numpy as np

def Q(signs, m):
    r = np.array(signs) * np.sqrt(np.array(m, float))
    return (np.array(m, float)).sum() / r.sum() ** 2

def qmc(signs, spec, nsamp=200000, seed=8):
    rng = np.random.default_rng(seed)
    d = np.array([rng.normal(v, s, nsamp) for v, s in spec])
    r = np.array(signs)[:, None] * np.sqrt(d)
    return d.sum(0) / r.sum(0) ** 2

MS, MC, MB = (93.46, 0.58), (1278.0, 13.0), (4200.0, 14.0)
tests = {"G8a": ("(-s, c, b)", (-1, 1, 1), {"P6 own-mass (scored)": [MS, MC, MB],
                                            "one common scale (unscored)": [(57.0, 0.4), (638.0, 6.5), (2860.0, 10.0)]}),
         "G8b": ("(c, b, t)", (1, 1, 1), {"P6 own-mass (scored)": [MC, MB, (162500.0, 1800.0)],
                                          "authors' mixed, direct top (unscored)": [MC, MB, (172520.0, 330.0)],
                                          "one common scale (unscored)": [(638.0, 6.5), (2860.0, 10.0), (172100.0, 1800.0)]})}
res = {}
for key, (lab, signs, convs) in tests.items():
    for cname, spec in convs.items():
        q0 = Q(signs, [v for v, _ in spec])
        sig = qmc(signs, spec).std()
        z = (q0 - 2 / 3) / sig
        print(f"{key} {lab:11s} {cname:40s}: Q = {q0:.5f} +- {sig:.5f}  ({z:+.1f} sigma from 2/3)")
        if "scored" in cname and "unscored" not in cname:
            res[key] = abs(z) <= 2
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
