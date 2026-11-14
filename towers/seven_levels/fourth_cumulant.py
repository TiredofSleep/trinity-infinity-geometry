"""fourth_cumulant.py -- Theorem 5 of TORUS_MOMENTS.md section 8 in full: J4's elliptic-surface sum, and round 18.

    "1 and 2, J4's surface sum first"  -- the author, 14 November 2026

  J4 = (3p + 1)(p^2 - 1) - 4p(p + 1) b^2,   p = a^2 + b^2 with b even (b = 0 when p = 3 mod 4),

and with it the fourth free cumulant, rest on one count (section 8, "Every odd I_n and even J_n is one count"):

  T(p) = sum over k != 0 and A of eta(k A (k + 4 - 4A)((k + 4)A - 4k)) = (2 + (-1|p)) p - 4 b^2.

The proof (TORUS_MOMENTS.md section 8, Theorem 5), each step checked here:
  1. Legendre form.  For k != 0, -4 the sum over A is eta(-k) L(16k/(k + 4)^2), where L(l) = sum_X eta(X(X-1)(X-l))
     is the Legendre curve's sum; at k = -4 it is p - 1.
  2. Landen.  With k = 4t the parameter is 4t/(1 + t)^2, and L(4t/(1 + t)^2) = L(t^2) for t != 0, 1, -1: the two
     curves are 2-isogenous over F_p, so they have the same number of points.  L(1) = -1.
  3. So T = p - 1 - (-1|p) + sum over t != 0, +-1 of eta(-t) L(t^2).  The terms at t and -t cancel when p = 3 mod 4,
     so T = p.  When p = 1 mod 4, T = p + W with W = sum_t eta(t) L(t^2).
  4. Quartic Jacobi sums.  Put u = t^2: eta(t) = chi(u) for a character chi of order 4.  Then
     W = J(chi, eta)^2 + J(chi-bar, eta)^2 = 2(a^2 - b^2), where J(chi, eta) = a + bi has norm p.  And a is odd: the
     curve y^2 = t^3 - t has p + 1 + 2a points, a number divisible by 4 since its three points of order 2 are rational.
  5. The pairing.  N_V(4) = sum over k != 0 of (1 - eta(k)) F(k), with F(k) = p - 1 + 2 eta(k + 4) + G(k), G(k) the
     sum over A above without the factor eta(k), and sum_k G(k) = 2 + (-1|p) p.  So N_V(4) = (p - 1)^2 + 2 + (-1|p) p
     - T(p) = (p - 1)(p - 3) + 4b^2, and J4 = p^4 - 1 - p(p + 1) N_V(4) by section 8's reduction.

  python fourth_cumulant.py           # every step at every prime 3..401; N_V(4) by brute force at 3..31; the chain
                                      #   against the operators' J4 (logs to 509)  -> fourth_cumulant_verify.log
  python fourth_cumulant.py test      # round 18 (PREREG.md): 409..3001 and 409..1009 -> fourth_cumulant_test.log
                                      #   (four worker processes at below-normal priority; a few minutes)

numpy + sympy.  ASCII output.  Exits with 1 if a check fails.
"""
import ctypes
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
import sympy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def low_priority():
    try:
        ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
    except Exception:
        pass


low_priority()
LOG = None
FAILS = []


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def check(name, ok, detail=""):
    say(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


def primes(lo, hi):
    return [q for q in range(lo, hi + 1) if sympy.isprime(q)]


def eta_table(p):
    E = -np.ones(p, dtype=np.int64)
    E[0] = 0
    E[(np.arange(1, p, dtype=np.int64) ** 2) % p] = 1
    return E


def ab(p):
    """p = a^2 + b^2 with a odd and b even, both positive (p = 1 mod 4); (0, 0) when p = 3 mod 4"""
    if p % 4 == 3:
        return 0, 0
    for a in range(1, int(p ** 0.5) + 1, 2):
        b = int(round((p - a * a) ** 0.5))
        if b * b == p - a * a:
            return a, b


def T_formula(p):
    return (2 + (1 if p % 4 == 1 else -1)) * p - 4 * ab(p)[1] ** 2


def J4_theorem(p):
    return (3 * p + 1) * (p * p - 1) - 4 * p * (p + 1) * ab(p)[1] ** 2


def surface_rows(p, E, chunk=256):
    """G1(k) = sum_A eta(k A (k + 4 - 4A)((k + 4)A - 4k)) for k = 1..p-1, and G(k), the same without the factor k"""
    A = np.arange(p, dtype=np.int64)[None, :]
    G1, G = np.zeros(p, dtype=np.int64), np.zeros(p, dtype=np.int64)
    for k0 in range(1, p, chunk):
        k = np.arange(k0, min(p, k0 + chunk), dtype=np.int64)[:, None]
        v = A * ((k + 4 - 4 * A) % p) % p * (((k + 4) * A - 4 * k) % p) % p
        G[k0:k0 + len(k)] = E[v].sum(axis=1)
        G1[k0:k0 + len(k)] = E[(k * v) % p].sum(axis=1)
    return G1, G


def legendre_family(p, E, chunk=256):
    """L(l) = sum_X eta(X(X - 1)(X - l)) for every l in F_p"""
    X = np.arange(p, dtype=np.int64)[None, :]
    base = X * (X - 1) % p
    L = np.zeros(p, dtype=np.int64)
    for l0 in range(0, p, chunk):
        lam = np.arange(l0, min(p, l0 + chunk), dtype=np.int64)[:, None]
        L[l0:l0 + len(lam)] = E[base * ((X - lam) % p) % p].sum(axis=1)
    return L


def T_direct(p):
    E = eta_table(p)
    return int(surface_rows(p, E)[0][1:].sum())


def steps(p):
    """each step of the proof at the prime p: a dict of booleans"""
    E = eta_table(p)
    inv = lambda x: pow(int(x) % p, p - 2, p)
    G1, G = surface_rows(p, E)
    L = legendre_family(p, E)
    T = int(G1[1:].sum())
    out = {}
    # 1. Legendre form
    ok = True
    for k in range(1, p):
        if k == (-4) % p:
            ok &= int(G1[k]) == p - 1
        else:
            ok &= int(G1[k]) == int(E[(-k) % p]) * int(L[16 * k * inv((k + 4) ** 2) % p])
    out["legendre"] = ok
    # 2. Landen
    t = np.arange(2, p - 1, dtype=np.int64)
    lam = np.array([4 * int(s) * inv((1 + int(s)) ** 2) % p for s in t], dtype=np.int64)
    out["landen"] = bool(np.all(L[lam] == L[(t * t) % p])) and int(L[1]) == -1
    # 3, 4. the sum, and the quartic Jacobi sums
    s = np.arange(1, p, dtype=np.int64)
    W = int((E[s] * L[(s * s) % p]).sum())
    if p % 4 == 3:
        out["sum"] = T == p
        out["jacobi"] = True
    else:
        out["sum"] = T == p + W
        g = int(sympy.primitive_root(p))
        ind = np.zeros(p, dtype=np.int64)
        x = 1
        for j in range(p - 1):
            ind[x] = j
            x = x * g % p
        v = np.arange(2, p, dtype=np.int64)                    # v = 0 and v = 1 contribute 0
        q = ind[v] % 4                                        # chi(v) = i^q
        w = E[(1 - v) % p]
        a = int((w * (q == 0)).sum() - (w * (q == 2)).sum())   # J(chi, eta) = a + b i
        b = int((w * (q == 1)).sum() - (w * (q == 3)).sum())
        cm = int(E[(s ** 3 - s) % p].sum()) + int(E[0])        # sum over t of eta(t^3 - t)
        out["jacobi"] = (a * a + b * b == p and W == 2 * (a * a - b * b) and a % 2 != 0 and b % 2 == 0
                         and cm == 2 * a and (abs(a), abs(b)) == ab(p))
    out["T"] = T == T_formula(p)
    # 5. the pairing
    A = np.arange(1, p, dtype=np.int64)[None, :]
    Ainv = np.array([0] + [inv(a) for a in range(1, p)], dtype=np.int64)[1:][None, :]
    k = np.arange(1, p, dtype=np.int64)[:, None]
    F = ((1 - E[(k + 4 - 4 * A) % p]) * (1 - E[(k + 4 - 4 * k * Ainv) % p])).sum(axis=1)
    F0 = int(((1 - E[4 % p]) * (1 - E[(4 - 4 * np.arange(p)) % p])).sum() * 2 - (1 - E[4 % p]) ** 2)
    kk = np.arange(1, p, dtype=np.int64)
    okF = bool(np.all(F == p - 1 + 2 * E[(kk + 4) % p] + G[1:]))
    sumG = int(G[1:].sum()) == 2 + int(E[p - 1]) * p
    NV = int(((1 - E[kk]) * F).sum())
    out["pairing"] = okF and sumG and F0 == 0 and NV == (p - 1) ** 2 + 2 + int(E[p - 1]) * p - T
    out["NV"] = NV
    return out


def NV4_brute(p):
    """N_V(4) = #{d in F_p^4: d1 + d2 + d3 + d4 = 0, 1 + eps e2 + eps^2 e4 = 0}"""
    eps = next(e for e in range(2, p) if pow(e, (p - 1) // 2, p) == p - 1)
    g = np.indices((p, p, p)).reshape(3, -1).astype(np.int64)
    d = [g[0], g[1], g[2], (-(g[0] + g[1] + g[2])) % p]
    e = [np.ones_like(d[0])] + [np.zeros_like(d[0]) for _ in range(4)]
    for c in d:
        for j in range(4, 0, -1):
            e[j] = (e[j] + e[j - 1] * c) % p
    return int(((1 + eps * e[2] + eps * eps % p * e[4]) % p == 0).sum())


def operator_J4():
    """J4 from the operators' logs (exact_moments_collect.log, exact_moments_test.log, fifth_moments_test.log)"""
    out = {}
    for name in ("exact_moments_collect.log", "exact_moments_test.log", "fifth_moments_test.log"):
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            continue
        keys = "I2 J2 I3 J3 I4 J4 I5 J5 I6 J6".split()
        for line in open(path, encoding="utf-8"):
            f = line.split()
            if f and f[0] == "EXACT" and f[1] == "p":
                keys = [k for k in f[2:] if k not in ("even", "worst")]
            elif f and f[0] == "EXACT" and f[1].isdigit():
                out[int(f[1])] = int(dict(zip(keys, f[2:2 + len(keys)]))["J4"])
    return out


def verify():
    global LOG
    LOG = open(os.path.join(HERE, "fourth_cumulant_verify.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("fourth_cumulant.py -- Theorem 5 (TORUS_MOMENTS.md section 8): T(p), the pairing and J4, step by step")
    PS = primes(3, 401)
    res = {p: steps(p) for p in PS}
    for key, name in (("legendre", "1. Legendre form: the sum over A is eta(-k) L(16k/(k + 4)^2), and p - 1 at k = -4"),
                      ("landen", "2. Landen: L(4t/(1 + t)^2) = L(t^2) for t != 0, +-1 (2-isogenous curves); L(1) = -1"),
                      ("sum", "3. T = p when p = 3 mod 4 and T = p + W when p = 1 mod 4, W = sum_t eta(t) L(t^2)"),
                      ("jacobi", "4. W = J(chi, eta)^2 + J(chi-bar, eta)^2 = 2(a^2 - b^2), J = a + bi, a odd = half the "
                                 "sum of eta(t^3 - t)"),
                      ("T", "   so T(p) = (2 + (-1|p))p - 4b^2"),
                      ("pairing", "5. the pairing: F(0) = 0, F(k) = p - 1 + 2 eta(k + 4) + G(k), sum G = 2 + (-1|p)p, "
                                  "N_V(4) = (p - 1)^2 + 2 + (-1|p)p - T")):
        bad = [p for p in PS if not res[p][key]]
        check(f"{name}  (every prime 3..401)", not bad, f"fails at {bad}" if bad else "")
    small = primes(3, 31)
    ok = all(NV4_brute(p) == res[p]["NV"] == (p - 1) * (p - 3) + 4 * ab(p)[1] ** 2 for p in small)
    check("   N_V(4) by brute force = the pairing's count = (p - 1)(p - 3) + 4b^2  (every prime 3..31)", ok)
    ops = operator_J4()
    have = sorted(p for p in ops if p >= 5)
    ok = all(ops[p] == J4_theorem(p) == p ** 4 - 1 - p * (p + 1) * ((p - 1) * (p - 3) + 4 * ab(p)[1] ** 2) for p in have)
    check(f"6. the chain: J4 = p^4 - 1 - p(p + 1)N_V(4) = (3p + 1)(p^2 - 1) - 4p(p + 1)b^2 equals the operators' "
          f"integers at all {len(have)} primes {have[0]}..{have[-1]}", ok)
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()
    sys.exit(1 if FAILS else 0)


def _T(p):
    low_priority()
    return p, T_direct(p)


def _steps(p):
    low_priority()
    return p, steps(p)


def test():
    """round 18 (PREREG.md): G1..G3"""
    global LOG
    LOG = open(os.path.join(HERE, "fourth_cumulant_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    P1, P2 = primes(409, 3001), primes(409, 1009)
    say("Round 18: J4's surface sum, proved, tested where it was not measured (PREREG.md)")
    say(f"G1 primes {P1[0]}..{P1[-1]} ({len(P1)}); G2, G3 primes {P2[0]}..{P2[-1]} ({len(P2)})")
    with Pool(4) as pool:
        rT = dict(pool.map(_T, P1))
        rS = dict(pool.map(_steps, P2))
    say("T p T(p) formula")
    bad1 = []
    for p in P1:
        say(f"T {p} {rT[p]} {T_formula(p)}")
        if rT[p] != T_formula(p):
            bad1.append(p)
    say(f"G1 {'HELD' if not bad1 else 'FAILED at ' + str(bad1)}")
    bad2 = [p for p in P2 if not all(rS[p][k] for k in ("legendre", "landen", "sum", "jacobi", "T"))]
    for p in P2:
        say(f"STEPS {p} " + " ".join(f"{k}:{rS[p][k]}" for k in ("legendre", "landen", "sum", "jacobi", "T", "pairing")))
    say(f"G2 {'HELD' if not bad2 else 'FAILED at ' + str(bad2)}")
    bad3 = [p for p in P2 if not rS[p]["pairing"]]
    say(f"G3 {'HELD' if not bad3 else 'FAILED at ' + str(bad3)}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if mode == "verify":
        verify()
    elif mode == "test":
        test()
