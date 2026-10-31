#!/usr/bin/env python3
"""g10_calibration_check.py -- a second look at Round G10's chance calibration (generation_loop/round10.py).

Rebuilt from generation_loop/PREREG.md, without importing round10.py or search.py:
  * the targets eps (angle form) and eta (cone form) from m_e and m_mu;
  * the 69 small factors and the three coefficient tiers;
  * hits = candidates within 2 sigma of a target.
Then the expected number of chance hits per tier, three ways:
  A. the registered calibration: random targets log-uniform within +-1 decade, same relative window;
  B. the same within +-0.3 decade (and +-0.1), which weighs the grammar's density near the targets;
  C. random constants: alpha, m_e, m_mu and m_tau each scaled by an independent log-uniform factor in [1/2, 2],
     the whole grammar recomputed, and hits counted on the real targets. This keeps the grammar's own clustering
     (every p/q multiple of one factor moves with it) and breaks any real relation.
A tier would hold only with at least one hit and P(at least that many | Poisson) < 0.01, as registered.
ASCII output; needs numpy and mpmath.
"""
import math
from fractions import Fraction

import mpmath as mp
import numpy as np

mp.mp.dps = 40
ME, MMU, DMU, MTAU = mp.mpf("0.51099895000"), mp.mpf("105.6583755"), mp.mpf("0.0000023"), 1776.93
ALPHA = 1 / 137.035999177


def ratio(d, b):        # sqrt(m_mu/m_e) for labels: heaviest n = 0, electron n = 1, muon n = 2
    c = lambda n: 1 + b * mp.cos(d + 2 * mp.pi * n / 3)
    return c(2) / c(1)


def delta_koide(mmu):
    return mp.findroot(lambda d: ratio(d, mp.sqrt(2)) - mp.sqrt(mmu / ME), mp.mpf("0.2222"))


def eta_of(mmu):
    b = mp.findroot(lambda b: ratio(mp.mpf(2) / 9, b) - mp.sqrt(mmu / ME), mp.sqrt(2))
    return 1 - ((1 + b * b / 2) / 3) / (mp.mpf(2) / 3)


dK = delta_koide(MMU)
eps = float(1 - dK / (mp.mpf(2) / 9))
s_eps = float(abs(delta_koide(MMU + DMU) - dK) / (mp.mpf(2) / 9))
eta = float(eta_of(MMU))
s_eta = float(abs(eta_of(MMU + DMU) - eta_of(MMU)))
TARGETS = [(eps, s_eps), (eta, s_eta)]
print(f"targets: delta_Koide = {float(dK):.10f}; eps = {eps:.6e} +- {s_eps:.2e}; eta = {eta:.6e} +- {s_eta:.2e}")


def factors(alpha, me, mmu, mtau):
    xs = [alpha, alpha / math.pi, alpha / (4 * math.pi)]
    rhos = [me / mmu, me / mtau, mmu / mtau]
    logs = [math.log(mmu / me), math.log(mtau / me), math.log(mtau / mmu)]
    S = [x ** k for x in xs for k in range(1, 5)]
    S += [r ** k for r in rhos for k in (0.5, 1, 1.5, 2, 2.5, 3, 4)]
    S += [x * r ** k for x in xs[:2] for r in rhos for k in (0.5, 1, 1.5, 2)]
    S += [(alpha / math.pi) ** k * L ** j for k in (2, 3) for L in logs for j in (1, 2)]
    assert len(S) == 69
    return np.array(S)


T2 = [Fraction(x) for x in ("1", "1/2", "2", "1/3", "2/3", "3/2", "3", "4/3", "2/9", "9/2", "8", "1/8", "1/9", "9")]
T3 = sorted({Fraction(p, q) for p in range(1, 13) for q in range(1, 13)})
TIERS = {"T1": np.array([1.0]), "T2": np.array([float(c) for c in T2]), "T3": np.array([float(c) for c in T3])}
print("tier sizes:", {k: len(v) * 69 for k, v in TIERS.items()})


def hits(vals):
    return sum(int(np.count_nonzero(np.abs(vals - t) <= 2 * s)) for t, s in TARGETS)


def poisson_tail(k, lam):
    return 1.0 if k == 0 else 1 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k))


S0 = factors(ALPHA, float(ME), float(MMU), MTAU)
rng = np.random.default_rng(2026_10_31)
rows = []
for tier, coefs in TIERS.items():
    vals = np.outer(coefs, S0).ravel()
    lv = np.sort(np.log(vals))
    h = hits(vals)
    exp = {}
    for label, dec in (("A +-1 decade", 1.0), ("B +-0.3 decade", 0.3), ("B +-0.1 decade", 0.1)):
        e = 0.0
        for t, s in TARGETS:
            w = math.log(1 + 2 * s / t)
            rt = math.log(t) + rng.uniform(-1, 1, 40000) * dec * math.log(10)
            e += float(np.mean(np.searchsorted(lv, rt + w) - np.searchsorted(lv, rt - w)))
        exp[label] = e
    tot = 0
    NTR = 20000
    for _ in range(NTR):
        f = np.exp(rng.uniform(-math.log(2), math.log(2), 4))
        Sr = factors(ALPHA * f[0], float(ME) * f[1], float(MMU) * f[2], MTAU * f[3])
        tot += hits(np.outer(coefs, Sr).ravel())
    exp["C random constants"] = tot / NTR
    rows.append((tier, len(coefs) * 69, h, exp))

print()
for tier, n, h, exp in rows:
    print(f"{tier}: {n} candidates per target, {h} hits on the real targets")
    for label, e in exp.items():
        p = poisson_tail(h, e)
        verdict = "HOLDS" if (h >= 1 and p < 0.01) else "LOST"
        print(f"    {label:22s} expected {e:7.3f}   P(>= {h}) = {p:.3g}   verdict {verdict}")
