#!/usr/bin/env python3
"""
round10.py -- generation_loop/PREREG.md Round G10: is the gap between exact Koide and exact 2/9 a 'natural' small number?
Run from generation_loop/:  python3 round10.py     Prints ASCII only. Needs numpy and mpmath.
"""
import math
from fractions import Fraction
import numpy as np
import mpmath as mp
from search import delta_from_e_mu

mp.mp.dps = 40
ME, MMU, DMU, MTAU = mp.mpf("0.51099895000"), mp.mpf("105.6583755"), mp.mpf("0.0000023"), 1776.93
ALPHA = 1 / 137.035999177


# ------------------------------------------------------------------ targets
def eta_of(mmu):
    c = lambda d, b, n: 1 + b * mp.cos(d + 2 * mp.pi * n / 3)
    d = mp.mpf(2) / 9
    b = mp.findroot(lambda b: c(d, b, 2) / c(d, b, 1) - mp.sqrt(mmu / ME), mp.sqrt(2))
    Q = (1 + b * b / 2) / 3
    return 1 - Q / (mp.mpf(2) / 3)


dK, sdK = delta_from_e_mu()
eps, s_eps = 1 - dK / (2 / 9), sdK / (2 / 9)
eta = float(eta_of(MMU)); s_eta = float(abs(eta_of(MMU + DMU) - eta_of(MMU)))
TARGETS = {"eps (angle form)": (eps, s_eps), "eta (cone form)": (eta, s_eta)}
for k, (t, s) in TARGETS.items():
    print(f"target {k}: {t:.6e} +- {s:.2e}  (relative {s/t:.2%}); 2-sigma window +-{2*s/t:.2%}")

# ------------------------------------------------------------------ grammar
me, mmu = float(ME), float(MMU)
rhos = {"me/mmu": me / mmu, "me/mtau": me / MTAU, "mmu/mtau": mmu / MTAU}
logs = {"ln(mmu/me)": math.log(mmu / me), "ln(mtau/me)": math.log(MTAU / me), "ln(mtau/mmu)": math.log(MTAU / mmu)}
xs = {"alpha": ALPHA, "alpha/pi": ALPHA / math.pi, "alpha/(4pi)": ALPHA / (4 * math.pi)}
S = {}
for xn, x in xs.items():
    for k in range(1, 5):
        S[f"({xn})^{k}"] = x ** k
for rn, r in rhos.items():
    for k in (0.5, 1, 1.5, 2, 2.5, 3, 4):
        S[f"({rn})^{k:g}"] = r ** k
for xn in ("alpha", "alpha/pi"):
    for rn, r in rhos.items():
        for k in (0.5, 1, 1.5, 2):
            S[f"{xn}*({rn})^{k:g}"] = xs[xn] * r ** k
for k in (2, 3):
    for ln_, L in logs.items():
        for j in (1, 2):
            S[f"(alpha/pi)^{k}*{ln_}^{j}"] = (ALPHA / math.pi) ** k * L ** j
assert len(S) == 69, len(S)

T2 = [Fraction(1), Fraction(1, 2), Fraction(2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 2), Fraction(3),
      Fraction(4, 3), Fraction(2, 9), Fraction(9, 2), Fraction(8), Fraction(1, 8), Fraction(1, 9), Fraction(9)]
T3 = sorted({Fraction(p, q) for p in range(1, 13) for q in range(1, 13)})
TIERS = {"G10a T1 (c = 1)": [Fraction(1)], "G10b T2 (color/cone c)": T2, "G10c T3 (all p/q <= 12)": T3}


def candidates(coefs):
    labels, vals = [], []
    for c in coefs:
        for n, v in S.items():
            labels.append((f"{c} * " if c != 1 else "") + n); vals.append(float(c) * v)
    return labels, np.array(vals)


def poisson_tail(k, lam):
    return 1.0 if k == 0 else 1 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k))


rng = np.random.default_rng(10)
NTRIAL = 20000
res = {}
for tier, coefs in TIERS.items():
    labels, vals = candidates(coefs)
    lv = np.sort(np.log(vals))
    hits, expected = [], 0.0
    for tn, (t, s) in TARGETS.items():
        idx = np.nonzero(np.abs(vals - t) <= 2 * s)[0]
        hits += [(tn, labels[i], vals[i], (vals[i] - t) / s) for i in idx]
        j = int(np.argmin(np.abs(np.log(vals / t))))
        print(f"{tier} | {tn}: nearest {labels[j]} = {vals[j]:.6e} ({(vals[j]-t)/s:+.1f} sigma, {vals[j]/t-1:+.3%})")
        w = math.log(1 + 2 * s / t)
        rt = np.log(t) + rng.uniform(-1, 1, NTRIAL) * math.log(10)
        expected += float(np.mean(np.searchsorted(lv, rt + w) - np.searchsorted(lv, rt - w)))
    p = poisson_tail(len(hits), expected)
    print(f"{tier}: {len(vals)} candidates per target; hits {len(hits)}; expected by chance {expected:.3f}; P(>= hits) = {p:.3g}")
    for h in hits:
        print(f"    HIT {h[0]}: {h[1]} = {h[2]:.6e} ({h[3]:+.2f} sigma)")
    res[tier.split()[0]] = len(hits) >= 1 and p < 0.01

print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
