"""flat_states.py -- read after round 10's run (not registered): the flat states on three wheels.

Round 10's theorem: on three wheels of any odd prime p, every norm-type state psi_c = sum_x w^(c N(x)) |x> / sqrt q
(q = p^3) has Weyl expectations zero on the Z-type operators and of size 1/sqrt q on all others.  This script
  1. checks the closed form found after the run: psi_c's Wigner function takes the value K(m)/p^5 at (p^2 + p + 1) q
     points for each m in F_p* (K the Kloosterman sum over F_p) and -(p + 1)/p^5 at q points, so
         sum |W| = [(p + 1) + (p^2 + p + 1) sum_m |K(m)|] / p^2,
     and it tabulates that negativity for primes up to 1999 (it tends to 8/(3 pi) of the ceiling);
  2. scans the other flat states it could find: at 5 and 7 levels the cubic phase states w^(Tr(a x^3) + b N(x))
     over the field (b = 0 gives the Alltop / Klappenecker-Roetteler states), and at 3 levels the Galois-ring states
     sum_(j in T) w9^tr(a j^3) |j mod 3> in GR(9, 3) = Z_9[t]/(t^3 + 2t + 2), as we reconstructed the p = 3
     construction of Damski, Bistron, Ponterio, Czartowski and Zyczkowski (2026);
  3. compares them with round 10's bests, read from larger_arrays_run.log.

numpy + scipy + larger_arrays.py.  One process, one thread, below-normal priority.  ASCII output; writes
flat_states.log.
Run:  python flat_states.py      (under a minute)
"""
import ctypes
import itertools
import os
from collections import Counter

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import time

import numpy as np

import larger_arrays as la

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = None
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def kloosterman(p):
    a = np.arange(1, p)
    inv = np.array([pow(int(x), -1, p) for x in a])
    return np.array([np.cos(2 * np.pi * ((a + m * inv) % p) / p).sum() for m in range(1, p)])


def closed_form(p):
    return (((p + 1) + (p * p + p + 1) * np.abs(kloosterman(p)).sum()) / p ** 2 - 1) / 2


def field(p, n=3):
    """multiplication and addition tables, the cube map, the trace and the norm of F_p[t]/(MODULI), on basis indices"""
    m = la.MODULI[p, n]
    q = p ** n
    C = np.array(list(itertools.product(range(p), repeat=n)))
    wt = p ** np.arange(n - 1, -1, -1)
    prod = np.zeros((q, q, 2 * n - 1), dtype=np.int64)
    for i in range(n):
        for k in range(n):
            prod[:, :, i + k] += C[:, None, i] * C[None, :, k]
    for deg in range(2 * n - 2, n - 1, -1):
        c = prod[:, :, deg].copy()
        prod[:, :, deg] = 0
        for i in range(n):
            prod[:, :, deg - n + i] -= c * m[i]
    mul = (prod[:, :, :n] % p) @ wt
    add = ((C[:, None, :] + C[None, :, :]) % p) @ wt
    one = int(wt[0])

    def power(e):
        r, b = np.full(q, one), np.arange(q)
        while e:
            if e & 1:
                r = mul[r, b]
            b, e = mul[b, b], e >> 1
        return r

    frob = power(p)
    tr_el = add[add[np.arange(q), frob], frob[frob]]
    assert (C[tr_el][:, 1:] == 0).all(), "the trace lies in F_p"
    return dict(q=q, mul=mul, cube=power(3), trace=C[tr_el][:, 0], norm=la.norm_values(p, n))


def profile(arr, psi):
    N = arr.negativity(arr.wigner(psi[None, :]))[0]
    C = la.weyl_sizes(arr, psi)
    nz = int((C < 1e-6).sum())
    flat = nz == arr.D - 1 and bool(np.allclose(C[C >= 1e-6][1:], arr.D ** -0.5, atol=1e-6))
    return N, flat


def galois_ring_states():
    """GR(9, 3) = Z_9[t]/(t^3 + 2t + 2); T = {x : x^27 = x}; sigma lifts x -> x^3; tr = 1 + sigma + sigma^2"""
    n, h = 3, [2, 2, 0, 1]

    def mul(x, y):
        prod = [0] * (2 * n - 1)
        for i in range(n):
            for k in range(n):
                prod[i + k] += x[i] * y[k]
        for deg in range(2 * n - 2, n - 1, -1):
            c, prod[deg] = prod[deg], 0
            for i in range(n):
                prod[deg - n + i] -= c * h[i]
        return tuple(v % 9 for v in prod[:n])

    def pw(x, e):
        r, b = (1, 0, 0), x
        while e:
            if e & 1:
                r = mul(r, b)
            b, e = mul(b, b), e >> 1
        return r

    ring = list(itertools.product(range(9), repeat=3))
    T = [x for x in ring if pw(x, 27) == x]
    teich = {tuple(v % 3 for v in x): x for x in T}
    assert len(T) == 27 and len(teich) == 27

    def sigma(y):
        y0 = teich[tuple(v % 3 for v in y)]
        y1 = teich[tuple(((a - b) // 3) % 3 for a, b in zip(y, y0))]
        return tuple((a + 3 * b) % 9 for a, b in zip(pw(y0, 3), pw(y1, 3)))

    def tr(y):
        s1 = sigma(y)
        t = tuple((a + b + c) % 9 for a, b, c in zip(y, s1, sigma(s1)))
        assert t[1] == 0 and t[2] == 0
        return t[0]

    w9 = np.exp(2j * np.pi / 9)
    wt = np.array([9, 3, 1])
    for a in ring:
        if not any(v % 3 for v in a):
            continue
        psi = np.zeros(27, complex)
        for j in T:
            psi[int(np.array([v % 3 for v in j]) @ wt)] = w9 ** tr(mul(a, pw(j, 3)))
        yield a, psi / np.sqrt(27)


def scan(p):
    """the states w^(Tr(a x^3) + b N(x)) / sqrt q on three wheels of p, sorted into classes of (negativity, flat)"""
    F = field(p)
    arr = la.Array(p, 3)
    w = np.exp(2j * np.pi / p)
    classes = {}
    for a in range(F["q"]):
        ta = F["trace"][F["mul"][a, F["cube"]]]
        for b in range(p):
            if a == 0 and b == 0:
                continue
            N, flat = profile(arr, w ** ((ta + b * F["norm"]) % p) / np.sqrt(F["q"]))
            kind = ("norm" if a == 0 else "Alltop" if b == 0 else "mixed")
            classes.setdefault((round(N, 9), flat), Counter()).update([kind])
    return classes


def galois_ring_profile():
    """how many of the 702 Galois-ring states are flat, and their negativities"""
    vals, nflat, arr = Counter(), 0, la.Array(3, 3)
    for a, psi in galois_ring_states():
        N, flat = profile(arr, psi)
        vals[round(N, 9)] += 1
        nflat += flat
    return nflat, vals


def run_bests():
    out = {}
    path = os.path.join(HERE, "larger_arrays_run.log")
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        f = line.split()
        if line.startswith("RESULT "):
            key = (int(f[1]), int(f[2]))
            out[key] = max(out.get(key, 0.0), float(f[4]))
        elif line.startswith("KICK "):
            key = (int(f[1]), int(f[2]))
            out[key] = max(out.get(key, 0.0), float(f[6]))
    return out


def main():
    global LOG
    LOG = open(os.path.join(HERE, "flat_states.log"), "w", encoding="utf-8")
    say("1. the norm-type state on three wheels of p, from Kloosterman sums: sum|W| = [(p + 1) + (p^2 + p + 1) "
        "sum_m |K(m)|]/p^2")
    for p in (3, 5, 7):
        arr = la.Array(p, 3)
        K = kloosterman(p)
        q = p ** 3
        want = np.sort(np.concatenate([np.repeat(K / p ** 5, (p * p + p + 1) * q), np.full(q, -(p + 1) / p ** 5)]))
        ok = all(np.allclose(np.sort(arr.wigner(la.norm_state(p, 3, c)[None, :])[0].ravel()), want, atol=1e-14)
                 for c in range(1, p))
        say(f"  {p} levels: the Kloosterman sums K(m), m = 1..{p - 1}: {', '.join(f'{k:.6f}' for k in K)}; every "
            f"norm-type state's Wigner values are K(m)/p^5 and -(p + 1)/p^5 as claimed: {ok}")
    primes = [x for x in range(3, 2000) if all(x % d for d in range(2, int(x ** 0.5) + 1))]
    rows = [(p, closed_form(p)) for p in primes]
    for p, N in rows:
        if p < 60 or p in (97, 199, 499, 997, 1999):
            say(f"  p = {p:4d}: negativity {N:.6f}, {N / ((p ** 1.5 - 1) / 2):.4f} of the ceiling")
    tail = [N / ((p ** 1.5 - 1) / 2) for p, N in rows if p > 1000]
    say(f"  the mean fraction over the primes from 1000 to 2000: {np.mean(tail):.4f}; 8/(3 pi) = {8 / (3 * np.pi):.4f}")
    say(f"  the primes up to 2000 where it reaches 90% of the ceiling: "
        f"{[p for p, N in rows if N >= 0.9 * (p ** 1.5 - 1) / 2]}")
    say()
    bests = run_bests()
    say("2. other flat states")
    for p in (5, 7):
        classes = scan(p)
        flat_vals = sorted((N for (N, flat) in classes if flat), reverse=True)
        say(f"  {p} levels: {sum(sum(c.values()) for c in classes.values())} states w^(Tr(a x^3) + b N(x)); "
            f"{sum(sum(c.values()) for (N, flat), c in classes.items() if flat)} of them flat")
        for (N, flat), c in sorted(classes.items(), reverse=True)[:8]:
            say(f"    negativity {N:.9f}, flat {flat}: " + ", ".join(f"{v} {k}" for k, v in sorted(c.items())))
        if (p, 3) in bests:
            say(f"    round 10's best found on three wheels of {p}: {bests[p, 3]:.9f}; the best flat state here "
                f"{flat_vals[0]:.9f}")
    nflat, vals = galois_ring_profile()
    say(f"  3 levels: the Galois-ring states (702 units a): flat {nflat} of 702; negativities "
        + ", ".join(f"{N:.9f} ({c})" for N, c in sorted(vals.items(), reverse=True))
        + f"; the norm state 17/9 = {17 / 9:.9f}")
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


if __name__ == "__main__":
    main()
