"""J05 claims about linear magmas (a x + b y + c) mod n, recomputed with the independent engine."""
import os, sys, time, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E

t0 = time.time()

def lin(a, b, c, n):
    x = np.arange(n)
    return (a * x[:, None] + b * x[None, :] + c) % n

FAMC = {1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677}

print("Z/n (a=b=1, c=0):")
zp = {}
for n in range(1, 21):
    zp[n] = E.profile(lin(1, 1, 0, n)) if n <= 10 else E.profile_big(lin(1, 1, 0, n))
    print(f"  n={n}: {len(zp[n])}")
base = zp[5]
print("  identical ID sets for n=5..20:", all(zp[n] == base for n in range(5, 21)))
print("  C2 (Family C) inside Z/5 profile:", FAMC <= base, " extras:", len(base - FAMC))

print("negation magma -(x+y) mod n:")
npf = {}
for n in range(1, 21):
    npf[n] = E.profile(lin(n - 1, n - 1, 0, n)) if n <= 10 else E.profile_big(lin(n - 1, n - 1, 0, n))
    print(f"  n={n}: {len(npf[n])}")
print("  identical ID sets for n=4..20:", all(npf[n] == npf[4] for n in range(4, 21)))
print("  -(x+y) mod 2 equals Z/2:", npf[2] == zp[2])

print("J05 section 6 table entries:")
rows = [(1, 1, 0, 3, 60), (2, 2, 0, 3, 179), (0, 0, 0, 3, 1556), (1, 1, 0, 4, 116), (3, 3, 0, 4, 294),
        (1, 1, 0, 5, 32), (4, 4, 0, 5, None), (1, 1, 0, 7, 32), (6, 6, 0, 7, 294), (1, 4, 6, 7, 23),
        (5, 3, 6, 7, 14), (6, 3, 3, 7, 49), (2, 0, 3, 7, 347), (1, 1, 0, 10, 32), (9, 9, 0, 10, 294),
        (1, 3, 0, 10, 18), (3, 1, 0, 10, 18), (3, 7, 0, 10, 46), (9, 1, 0, 10, 163)]
for a, b, c, n, claim in rows:
    T = lin(a, b, c, n)
    p = E.profile(T) if n <= 10 else E.profile_big(T)
    quasi = math.gcd(a, n) == 1 and math.gcd(b, n) == 1
    print(f"  ({a},{b},{c}) mod {n}: profile {len(p)}  claimed {claim}  comm={a % n == b % n} quasigroup={quasi}"
          + ("" if claim is None or claim == len(p) else "   <-- MISMATCH"))

fr = E.profile(lin(5, 3, 6, 7))
print("  (5x+3y+6) mod 7 profile:", sorted(fr))
print("     contains 203:", 203 in fr, " contains 4658:", 4658 in fr, " shares with C2:", sorted(fr & FAMC))
for i in sorted(fr):
    print("       ", i, E.show(i))
p130 = E.profile(lin(1, 3, 0, 10))
print("  (x+3y) mod 10 profile:", sorted(p130), " superset of C2?", FAMC <= p130)

print("sigma_n^min: x*y = s(x+y mod n), s = cycle (1 2 ... n-1) fixing 0")
for n in range(5, 16):
    s = [0] + [(k + 1) if k < n - 1 else 1 for k in range(1, n)]
    x = np.arange(n)
    T = np.array(s)[(x[:, None] + x[None, :]) % n]
    p = E.profile_big(T) if n > 9 else E.profile(T)
    print(f"  n={n}: profile {len(p)}  == C2: {p == FAMC}")
print("time %.1fs" % (time.time() - t0))
