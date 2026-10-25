#!/usr/bin/env python3
"""fourier_fresh.py -- Round K3' fresh test (F1-F3). Prints ASCII only.
Singularity is decided EXACTLY: determinant mod two primes p = 1 mod n (a ring map Z[zeta_n] -> F_p), for
every certified minor and every minor whose singular-value ratio is below 1e-5. Everything else is
nonsingular (an exactly singular matrix has ratio ~1e-14). Two earlier runs used floating tests and misread
borderline singular minors: |det| < 1e-7 in run 1, numpy's default matrix_rank tolerance in run 2. Both are kept
as fourier_fresh_firstrun.log and fourier_fresh_secondrun.log."""
import itertools, random, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fourier_certs import certified
rng = random.Random(1212); res = {}

def primes_1_mod(n, count, start=10 ** 6):
    out, p = [], start
    while len(out) < count:
        p += 1
        if p % n == 1 and all(p % q for q in range(2, int(p ** 0.5) + 1)): out.append(p)
    return out
def root_of_unity(n, p):
    for g in range(2, p):
        z = pow(g, (p - 1) // n, p)
        if all(pow(z, n // q, p) != 1 for q in range(2, n + 1) if n % q == 0 and all(q % r for r in range(2, q))):
            return z
def det_mod(M, p):
    M = [r[:] for r in M]; k = len(M); d = 1
    for c in range(k):
        piv = next((r for r in range(c, k) if M[r][c] % p), None)
        if piv is None: return 0
        if piv != c: M[c], M[piv] = M[piv], M[c]; d = -d
        d = d * M[c][c] % p; inv = pow(M[c][c], p - 2, p)
        for r in range(c + 1, k):
            f = M[r][c] * inv % p
            if f: M[r] = [(x - f * y) % p for x, y in zip(M[r], M[c])]
    return d % p
def exact_singular(n, R, C, ctx):
    return all(det_mod([[pow(z, (t * f) % n, p) for f in C] for t in R], p) == 0 for p, z in ctx)

def check(n, pairs):
    ctx = [(p, root_of_unity(n, p)) for p in primes_1_mod(n, 2)]
    w = np.exp(2j * np.pi / n); F = w ** np.outer(range(n), range(n))
    s = cov = unsound = exact_checked = 0
    for R, C in pairs:
        c = certified(n, R, C)
        sv = np.linalg.svd(F[np.ix_(R, C)], compute_uv=False)
        if c or sv[-1] < 1e-5 * sv[0]:
            exact_checked += 1; sing = exact_singular(n, R, C, ctx)
        else:
            sing = False
        if c and not sing: unsound += 1
        if sing: s += 1; cov += c
    return s, cov, unsound, exact_checked, 0
def all_pairs(n):
    for k in range(1, n + 1):
        for R in itertools.combinations(range(n), k):
            for C in itertools.combinations(range(n), k): yield R, C
def rand_pairs(n, N):
    for _ in range(N):
        k = rng.randint(2, n - 2)
        yield tuple(sorted(rng.sample(range(n), k))), tuple(sorted(rng.sample(range(n), k)))
import json
part = sys.argv[1] if len(sys.argv) > 1 else "all"
jobs = {"a": [("n=12 exhaustive", lambda: check(12, all_pairs(12)))],
        "b": [("n=16 sampled", lambda: check(16, rand_pairs(16, 300000))),
              ("n=11 sampled", lambda: check(11, rand_pairs(11, 300000))),
              ("n=13 sampled", lambda: check(13, rand_pairs(13, 300000)))]}
if part in jobs:                                   # run one half, save its counts, stop (for 2-core parallel runs)
    json.dump({k: f() for k, f in jobs[part]}, open(f"fourier_part_{part}.json", "w")); sys.exit(0)
if part == "merge":
    out = {}
    for q in "ab": out.update({k: tuple(v) for k, v in json.load(open(f"fourier_part_{q}.json")).items()})
else:
    out = {k: f() for q in "ab" for k, f in jobs[q]}
for name, (s, cov, uns, dis, smp) in out.items():
    print(f"{name}: singular {s} (exact), certified {cov} ({100 * cov / max(s, 1):.1f}%), unsound {uns}; "
          f"{dis} minors decided exactly")
s12, s16 = out["n=12 exhaustive"], out["n=16 sampled"]
res["F1"] = s12[2] == 0 and s16[2] == 0
res["F2"] = s12[1] / s12[0] >= 0.85 and s16[1] / max(s16[0], 1) >= 0.85
res["F3"] = out["n=11 sampled"][0] == 0 and out["n=13 sampled"][0] == 0
print("SCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
