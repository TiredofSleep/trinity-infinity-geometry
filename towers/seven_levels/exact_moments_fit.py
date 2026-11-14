"""exact_moments_fit.py -- how round 16's formulas were found (TORUS_MOMENTS.md section 9).  It reads the exact integers in
exact_moments_collect.log (primes 7 to 199) and looks for exact fits: a polynomial in p of degree at most 6, plus the
characters of p mod 3 and mod 4 times polynomials of degree at most 5, plus one modular form (times p^j for j = 0..3,
one power or two adjacent ones) from a library of fourteen eta products. A fit counts only if it is exact, in rational
arithmetic, at every prime, with at least four more primes than unknowns.

    python exact_moments_fit.py                       # the exact fits: Kloosterman's sixth moment, J4 and I6
    python exact_moments_fit.py I5 J5 J6 SumK^5       # the searches that found nothing (slow)

numpy + sympy.  ASCII output.
"""
import itertools, sys
import numpy as np
import sympy as sp
import os
HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "exact_moments_collect.log")
keys, data = None, {}
for line in open(LOGF, encoding="utf-8"):
    f = line.split()
    if f and f[0] == "EXACT" and f[1] == "p":
        keys = f[2:-2]
    elif f and f[0] == "EXACT":
        data[int(f[1])] = dict(zip(keys, map(int, f[2:2 + len(keys)])))
PS = [p for p in sorted(data) if p >= 7]
NQ = 205

def eta_product(spec):
    """q-expansion coefficients (index = exponent) of prod eta(d tau)^r, assuming the q-shift is an integer"""
    shift = sum(d * r for d, r in spec)
    assert shift % 24 == 0, spec
    s = shift // 24
    poly = np.zeros(NQ + 1, dtype=object); poly[0] = 1
    for d, r in spec:
        for n in range(1, NQ // d + 1):
            for _ in range(abs(r)):
                f = np.zeros(NQ + 1, dtype=object); f[0] = 1; f[d * n] = -1
                if r > 0:
                    poly = np.array([sum(poly[i] * f[k - i] for i in (0, k - d * n) if 0 <= i <= k and (k - i) in (0, d * n)) for k in range(NQ + 1)], dtype=object)
    out = np.zeros(NQ + 1, dtype=object)
    out[s:] = poly[:NQ + 1 - s]
    return out

def eta_fast(spec):
    shift = sum(d * r for d, r in spec); assert shift % 24 == 0
    s = shift // 24
    poly = [0] * (NQ + 1); poly[0] = 1
    for d, r in spec:
        for n in range(1, NQ // d + 1):
            step = d * n
            for _ in range(r):
                for k in range(NQ, step - 1, -1):
                    poly[k] -= poly[k - step]
    return [0] * s + poly[:NQ + 1 - s]

FORMS = {
    "w4 l6 (eta1 eta2 eta3 eta6)^2": eta_fast([(1, 2), (2, 2), (3, 2), (6, 2)]),
    "w4 l8 eta2^4 eta4^4": eta_fast([(2, 4), (4, 4)]),
    "w4 l9 eta3^8 (CM -3)": eta_fast([(3, 8)]),
    "w4 l5 eta1^4 eta5^4": eta_fast([(1, 4), (5, 4)]),
    "w3 l16 eta4^6 (CM i)": eta_fast([(4, 6)]),
    "w3 l12 eta2^3 eta6^3 (CM -3)": eta_fast([(2, 3), (6, 3)]),
    "w3 l8 eta1^2 eta2 eta4 eta8^2 (CM -2)": eta_fast([(1, 2), (2, 1), (4, 1), (8, 2)]),
    "w3 l7 eta1^3 eta7^3 (CM -7)": eta_fast([(1, 3), (7, 3)]),
    "w2 l11 (eta1 eta11)^2": eta_fast([(1, 2), (11, 2)]),
    "w2 l15 eta1 eta3 eta5 eta15": eta_fast([(1, 1), (3, 1), (5, 1), (15, 1)]),
    "w2 l32 (eta4 eta8)^2 (CM i)": eta_fast([(4, 2), (8, 2)]),
    "w2 l36 eta6^4 (CM -3)": eta_fast([(6, 4)]),
    "w6 l4? eta2^12": eta_fast([(2, 12)]),
    "w5 l4? eta1^4 eta2^2 eta4^4": eta_fast([(1, 4), (2, 2), (4, 4)]),
}

def kloost_moments(p, ks):
    a = np.arange(1, p)
    inv = np.array([pow(int(v), -1, p) for v in a])
    K = np.array([np.cos(2 * np.pi * ((a + m * inv) % p) / p).sum() for m in range(1, p)])
    return {k: int(round(float((K ** k).sum()))) for k in ks}

KM = {p: kloost_moments(p, (5, 6)) for p in PS}
TARGETS = {"SumK^5": {p: KM[p][5] for p in PS}, "SumK^6": {p: KM[p][6] for p in PS}}
for k in ("I5", "J5", "I6", "J6", "J4"):
    TARGETS[k] = {p: data[p][k] for p in PS}
chi4 = lambda p: 1 if p % 4 == 1 else -1
chi3 = lambda p: 1 if p % 3 == 1 else -1

def try_fit(target, deg, form_terms):
    cols = []
    names = []
    for k in range(deg + 1):
        cols.append([sp.Integer(p) ** k for p in PS]); names.append(f"p^{k}")
    for k in range(deg):
        cols.append([sp.Integer(chi4(p) * p ** k) for p in PS]); names.append(f"chi4 p^{k}")
        cols.append([sp.Integer(chi3(p) * p ** k) for p in PS]); names.append(f"chi3 p^{k}")
        cols.append([sp.Integer(chi3(p) * chi4(p) * p ** k) for p in PS]); names.append(f"chi12 p^{k}")
    for fname, j in form_terms:
        cols.append([sp.Integer(FORMS[fname][p] * p ** j) for p in PS]); names.append(f"p^{j} a[{fname}]")
    M = sp.Matrix(len(PS), len(cols), lambda i, c: cols[c][i])
    y = sp.Matrix([target[p] for p in PS])
    if M.shape[1] >= M.shape[0] - 4:
        return None
    try:
        sol, params = M.gauss_jordan_solve(y)
    except ValueError:
        return None
    sol = sol.subs({t: 0 for t in params})
    return [(n, c) for n, c in zip(names, sol) if c != 0]

which = sys.argv[1:] if len(sys.argv) > 1 else ["SumK^6", "J4", "I6"]
for tname in which:
    target = TARGETS[tname]
    deg = 4 if tname.startswith("Sum") else 6
    found = False
    res = try_fit(target, deg, [])
    if res is not None:
        print(f"{tname}: polynomial + characters alone fit:", res); found = True; continue
    for fname in FORMS:
        for js in ([0], [1], [2], [3], [0, 1], [1, 2], [2, 3]):
            res = try_fit(target, deg, [(fname, j) for j in js])
            if res is not None:
                print(f"{tname}: FIT with {fname}, powers {js}:")
                for n, c in res:
                    print(f"     {c} * {n}")
                found = True
                break
        if found:
            break
    if not found:
        print(f"{tname}: no fit with one form")
