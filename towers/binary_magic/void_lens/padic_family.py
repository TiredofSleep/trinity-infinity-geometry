#!/usr/bin/env python3
"""
padic_family.py -- Round 8b (void_lens/PREREG.md): squares built from two linear Latin squares with
arbitrary digit relabelings,  M = n*pi1(a1 i + b1 j) + pi2(a2 i + b2 j) + 1.
Run from binary_magic/:  python3 void_lens/padic_family.py
Prints ASCII only. Exact integer determinants.
"""
import itertools, math, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from void_lens_core import det_bareiss

def member(n, p1, p2, a1, b1, a2, b2):
    return [[n * p1[(a1 * i + b1 * j) % n] + p2[(a2 * i + b2 * j) % n] + 1 for j in range(n)] for i in range(n)]

def magic_pandiag(M):
    n = len(M); s = n * (n * n + 1) // 2
    if sorted(v for r in M for v in r) != list(range(1, n * n + 1)): return False
    if any(sum(r) != s for r in M) or any(sum(c) != s for c in zip(*M)): return False
    return all(sum(M[i][(i + d) % n] for i in range(n)) == s and sum(M[i][(d - i) % n] for i in range(n)) == s
               for d in range(n))

res = {}
n = 5; U = [1, 2, 3, 4]; perms = list(itertools.permutations(range(n)))
fam = set()
slopes = [(a, b) for a in U for b in U]
for (a1, b1), (a2, b2) in itertools.product(slopes, repeat=2):
    # quick screen with identity digits: pandiagonality depends only on the slopes (each broken diagonal must
    # be a transversal of both Latin squares), so test it once per slope pair
    if not magic_pandiag(member(n, list(range(n)), list(range(n)), a1, b1, a2, b2)): continue
    for p1 in perms:
        for p2 in perms:
            fam.add(tuple(v for r in member(n, p1, p2, a1, b1, a2, b2) for v in r))
zeros_fam = sum(1 for key in fam if det_bareiss([list(key[5 * i:5 * i + 5]) for i in range(5)]) == 0)
print(f"p = 5 extended family: {len(fam)} distinct pandiagonal magic squares (prediction 28,800); singular: {zeros_fam}")
res["P1"] = len(fam) == 28800

rng = random.Random(81)
def random_zeros(n, trials):
    U = [u for u in range(1, n) if math.gcd(u, n) == 1]; z = 0; ex = None
    for _ in range(trials):
        p1 = list(range(n)); p2 = list(range(n)); rng.shuffle(p1); rng.shuffle(p2)
        M = member(n, p1, p2, rng.choice(U), rng.choice(U), rng.choice(U), rng.choice(U))
        if det_bareiss(M) == 0:
            z += 1; ex = ex or (p1, p2)
    return z, ex
pz = {}
for n in (5, 7, 11, 13):
    pz[n] = random_zeros(n, 20000 if n < 11 else 5000)[0]
print("primes, random members, zero determinants:", pz)
res["P2"] = zeros_fam == 0 and all(v == 0 for v in pz.values())
cz = {}
for n in (9, 15, 25):
    z, ex = random_zeros(n, 20000 if n == 9 else 3000)
    cz[n] = z
    if ex: print(f"  n = {n}: first singular member uses digit maps {ex[0]} / {ex[1]}")
print("composite n, random members, zero determinants:", cz)
res["P3"] = any(v > 0 for v in cz.values())
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
