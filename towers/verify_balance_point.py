#!/usr/bin/env python3
"""verify_balance_point.py -- checks every [FORCED] claim in THE_BALANCE_POINT.md.

    python verify_balance_point.py      # prints PASS/FAIL per check; exit code 1 on any failure

Setting: the f corners of a regular polygon are the f-th roots of unity, zeta^j with
zeta = exp(2 pi i / f). Walk k steps (stepping s corners at a time); the balance point of the
k corners visited is c = (1/k) * sum_{j=1..k} zeta^(j s).

B1  |c_k| = |sin(pi k/f)| / (k sin(pi/f))                         (s = 1; float, f <= 64)
B2  c_k = 0 exactly when f | k            (exact, in Z[z] modulo the cyclotomic polynomial)
B3  first lap: 1 = |c_1| > |c_2| > ... > |c_(f-1)| = 1/(f-1), and c_f = 0;
    and for every k, |c_k| <= 1/(k sin(pi/f))
B4  |c_k|^2 = sinc^2(k/f) / sinc^2(1/f)            (sinc(t) = sin(pi t)/(pi t))
B5  circle limit: |c_k|^2 -> sinc^2(t) as f -> oo with k/f = t; the gap is
    sinc^2(t)(1/sinc^2(1/f) - 1), about (pi^2/3) sinc^2(t)/f^2
B6  Fejer: k |c_k|^2 = F_k(2 pi/f), F_k(x) = sum_{|m|<k} (1-|m|/k) e^{imx}
    = sin^2(kx/2) / (k sin^2(x/2))      (exact polynomial identity in cos x, k <= 12)
B7  star walks (step s): |c| = |sin(pi k s/f)| / (k |sin(pi s/f)|), and c = 0 exactly when
    the walk has closed, i.e. f/gcd(f,s) divides k            (exact zero test, f <= 30)
B8  the Chapter 12 reading: k shares a factor with N exactly when one of N's prime polygons
    closes after k steps; the first such k is N's smallest prime, for every N >= 2
B9  (what the archive got wrong) sinc^2 is convex at t = 1/2, not concave: its second
    derivative there is about +1.73, and it changes sign at t = 0.4148 (J24, Remark 7.4)
B10 (what the archive got wrong) on Z/N, a window of k sites and a momentum state overlap with
    probability (k/N)|c_k|^2 -> (k/N) sinc^2(t), not sinc^2(t)/N (J26's continuum limit)

Standard library + numpy + sympy. Runtime: about ten seconds.
"""
import cmath
import math
import sys
from math import gcd

import numpy as np
import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   (" + detail + ")") if detail else ""))
    if not ok:
        FAILS.append(name)


def balance(k, f, s=1):
    """centre of mass of the corners zeta^s, zeta^2s, ..., zeta^ks (complex, float)"""
    return sum(cmath.exp(2j * math.pi * (j * s % f) / f) for j in range(1, k + 1)) / k


def closed(k, f, s=1):
    return abs(math.sin(math.pi * k * s / f)) / (k * abs(math.sin(math.pi * s / f)))


def sinc(t):
    return 1.0 if t == 0 else math.sin(math.pi * t) / (math.pi * t)


# ---- exact arithmetic in Z[z]/Phi_f(z) -------------------------------------------------
def int_poly_rem(num, den):
    """remainder of integer polynomial num by monic integer polynomial den (lists, high->low)"""
    num = list(num)
    while len(num) >= len(den):
        lead = num[0]
        if lead:
            for i in range(len(den)):
                num[i] -= lead * den[i]
        num.pop(0)
    return num


PHI = {}


def cyclo(f):
    if f not in PHI:
        PHI[f] = [int(c) for c in sp.Poly(sp.cyclotomic_poly(f, sp.Symbol('z')), sp.Symbol('z')).all_coeffs()]
    return PHI[f]


def walk_sum_is_zero_exact(k, f, s=1):
    """is sum_{j=1..k} zeta_f^(j s) = 0 ?  Reduce exponents mod f (zeta^f = 1), then mod Phi_f."""
    coeff = [0] * f                      # coefficient of z^r, r = 0..f-1
    for j in range(1, k + 1):
        coeff[(j * s) % f] += 1
    high_to_low = coeff[::-1]            # z^(f-1) ... z^0
    rem = int_poly_rem(high_to_low, cyclo(f))
    return all(c == 0 for c in rem)


# B1 -------------------------------------------------------------------------------------
dev = max(abs(abs(balance(k, f)) - closed(k, f)) for f in range(2, 65) for k in range(1, 3 * f + 1))
check("B1 |c_k| = |sin(pi k/f)| / (k sin(pi/f)), f=2..64, k=1..3f", dev < 1e-12, "max deviation %.1e" % dev)

# B2 -------------------------------------------------------------------------------------
ok = all(walk_sum_is_zero_exact(k, f) == (k % f == 0) for f in range(2, 41) for k in range(1, 2 * f + 2))
check("B2 the balance point is the centre exactly when f | k (exact, f=2..40, k=1..2f+1)", ok)

# B3 -------------------------------------------------------------------------------------
ok = True
for f in range(2, 401):
    vals = [closed(k, f) for k in range(1, f)]
    ok &= abs(vals[0] - 1.0) < 1e-13 and abs(vals[-1] - 1.0 / (f - 1)) < 1e-13
    ok &= all(vals[i] > vals[i + 1] * (1 + 1e-12) for i in range(len(vals) - 1))
    ok &= walk_sum_is_zero_exact(f, f) if f <= 60 else True
    ok &= all(closed(k, f) <= 1 / (k * math.sin(math.pi / f)) + 1e-15 for k in range(1, 4 * f))
check("B3 first lap: |c_1| = 1 > ... > |c_(f-1)| = 1/(f-1), c_f = 0; always |c_k| <= 1/(k sin(pi/f))  (f=2..400)", ok)

# B4 -------------------------------------------------------------------------------------
dev = max(abs(closed(k, f) ** 2 - sinc(k / f) ** 2 / sinc(1 / f) ** 2) for f in range(2, 300) for k in range(1, 2 * f))
check("B4 |c_k|^2 = sinc^2(k/f) / sinc^2(1/f)", dev < 1e-13, "max deviation %.1e" % dev)

# B5 -------------------------------------------------------------------------------------
ok = True
rows = []
for (p, q) in [(1, 2), (1, 4), (1, 3), (3, 2), (5, 2)]:
    t = p / q
    for f in [q * 10, q * 100, q * 1000, q * 10000]:
        k = p * f // q
        err = abs(closed(k, f) ** 2 - sinc(t) ** 2)
        bound = (1 / sinc(1 / f) ** 2 - 1) * sinc(t) ** 2 + 1e-15     # exact size of the gap, by B4
        ok &= err <= bound * (1 + 1e-9)
        ok &= err * f * f <= (math.pi ** 2 / 3) * sinc(t) ** 2 * 1.01 + 1e-9
        if f == q * 10000:
            rows.append("t=%s err=%.1e" % (sp.Rational(p, q), err))
check("B5 circle limit |c_k|^2 -> sinc^2(t); error = sinc^2(t)(1/sinc^2(1/f) - 1), within 1% of "
      "(pi^2/3) sinc^2(t)/f^2 for f >= 20", ok, "; ".join(rows))

# B6 -------------------------------------------------------------------------------------
x, c = sp.symbols('x c')
ok = True
for k in range(1, 13):
    lhs = (1 - c) * (k + 2 * sum((k - m) * sp.chebyshevt(m, c) for m in range(1, k)))
    rhs = 1 - sp.chebyshevt(k, c)
    ok &= sp.expand(lhs - rhs) == 0
check("B6a exact: (1 - cos x)(k + 2 sum_{m<k} (k-m) cos mx) = 1 - cos kx, k=1..12", ok)
dev = 0.0
for f in range(2, 41):
    xx = 2 * math.pi / f
    for k in range(1, 41):
        fejer = sum((1 - abs(m) / k) * cmath.exp(1j * m * xx) for m in range(-k + 1, k)).real
        dev = max(dev, abs(k * closed(k, f) ** 2 - fejer))
check("B6b k |c_k|^2 = Fejer kernel F_k(2 pi/f), f=2..40, k=1..40", dev < 1e-11, "max deviation %.1e" % dev)

# B7 -------------------------------------------------------------------------------------
dev = 0.0
ok_zero = True
for f in range(2, 31):
    for s in range(1, f):
        L = f // gcd(f, s)                      # the walk closes after L steps
        for k in range(1, 2 * f + 1):
            if (k * s) % f:
                dev = max(dev, abs(abs(balance(k, f, s)) - closed(k, f, s)))
            ok_zero &= walk_sum_is_zero_exact(k, f, s) == (k % L == 0)
check("B7a star walk: |c| = |sin(pi k s/f)| / (k |sin(pi s/f)|), f=2..30", dev < 1e-12, "max deviation %.1e" % dev)
check("B7b star walk: c = 0 exactly when f/gcd(f,s) divides k (exact, f=2..30)", ok_zero)

# B8 (the Chapter 12 reading) ---------------------------------------------------------------
# k shares a factor with N  <=>  for some prime p | N the p-gon walk of k steps has its balance
# point on the centre; the first such k is N's smallest prime, for EVERY N >= 2.
PR = [p for p in range(2, 38) if all(p % q for q in range(2, p))]
ZERO = {p: [walk_sum_is_zero_exact(r if r else p, p) for r in range(p)] for p in PR}   # exact, by residue
ok_pic, ok_first = True, True
for N in range(2, 5001):
    m, ps, q = N, [], 2
    while q * q <= m:
        if m % q == 0:
            ps.append(q)
            while m % q == 0:
                m //= q
        q += 1
    if m > 1:
        ps.append(m)
    first = next(k for k in range(1, N + 1) if gcd(k, N) > 1)
    ok_first &= first == ps[0]
    if max(ps) <= 37:
        for k in range(1, 2 * N + 1):
            ok_pic &= (gcd(k, N) > 1) == any(ZERO[p][k % p] for p in ps)
check("B8a k shares a factor with N iff one of N's prime polygons closes after k steps (exact, 37-smooth N<=5000)", ok_pic)
check("B8b the first k sharing a factor with N is N's smallest prime, every N=2..5000 (square-free or not)", ok_first)

# B9 (J24, Remark 7.4) ------------------------------------------------------------------------
t = sp.Symbol('t', positive=True)
g2 = sp.diff((sp.sin(sp.pi * t) / (sp.pi * t)) ** 2, t, 2)
at_half = float(g2.subs(t, sp.Rational(1, 2)))
root = float(sp.nsolve(g2, t, 0.41))
ok = at_half > 1.7 and abs(root - 0.4148) < 1e-4
ok &= float(g2.subs(t, sp.Rational(2, 5))) < 0 < float(g2.subs(t, sp.Rational(9, 20)))
check("B9 sinc^2 is convex at 1/2, not concave: (sinc^2)''(1/2) = %.4f, inflection at t = %.10f" % (at_half, root), ok)

# B10 (J26's continuum limit) --------------------------------------------------------------------
# |p> = momentum state exp(2 pi i x/f)/sqrt(N) on Z/N (f | N);  |w_k> = uniform window on k sites
N_, f_, k_ = 10000, 1000, 500
amp = sum(cmath.exp(2j * math.pi * x / f_) for x in range(k_)) / math.sqrt(N_ * k_)
overlap = abs(amp) ** 2
tt = k_ / f_
ok = abs(overlap - (k_ / N_) * closed(k_, f_) ** 2) < 1e-12
ok &= abs(overlap / ((k_ / N_) * sinc(tt) ** 2) - 1) < 1e-5
ok &= abs(overlap / (sinc(tt) ** 2 / N_) / k_ - 1) < 1e-5            # J26's sinc^2(t)/N misses the factor k
check("B10 Z/N window-momentum overlap = (k/N)|c_k|^2 -> (k/N) sinc^2(t) = %.5f; J26's sinc^2(t)/N = %.2e is off by k = %d"
      % (overlap, sinc(tt) ** 2 / N_, k_), ok)

print()
if FAILS:
    print("FAILED: %d check(s): %s" % (len(FAILS), ", ".join(FAILS)))
    sys.exit(1)
print("All checks passed.")
