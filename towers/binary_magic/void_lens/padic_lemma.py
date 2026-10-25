#!/usr/bin/env python3
"""padic_lemma.py -- Round 8e: the valuation lemma behind Round 8b. Prints ASCII only.
N(f^) = prod_{k=1}^{p-1} f^(k) is an integer, and its p-adic valuation equals the (1-w)-adic valuation
of f^. It is computed exactly as the resultant of the polynomial f(t) = sum_x f(x) t^x with the p-th
cyclotomic polynomial, so no floating point is used."""
import itertools, random
import sympy as sp

t = sp.symbols("t")
def vp(n, p):
    n = abs(int(n)); v = 0
    while n and n % p == 0: n //= p; v += 1
    return v if n else None
def val(pi, p):
    h = sp.Rational(p - 1, 2)
    f = sum((2 * (pi[x] - h)) * t ** x for x in range(p))          # doubled to stay integral; 2 is a unit at p
    N = sp.resultant(sp.Poly(f, t), sp.Poly(sp.cyclotomic_poly(p, t), t))
    return vp(N, p)
ok = True; seen = {}
rng = random.Random(84)
for p in (5, 7, 11, 13):
    pool = itertools.permutations(range(p)) if p <= 7 else (rng.sample(range(p), p) for _ in range(20000))
    vs = set()
    for pi in pool:
        v = val(pi, p); vs.add(v)
        if v is None or v < 1 or v > p - 2: ok = False
    seen[p] = sorted(vs)
print("valuations seen:", seen)
print("SCORE:", {"P4": "HELD" if ok else "LOST"})
