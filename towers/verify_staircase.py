#!/usr/bin/env python3
"""verify_staircase.py -- checks every [FORCED] claim in THE_STAIRCASE.md, and computes its [measured] numbers.

    python verify_staircase.py      # prints PASS/FAIL per check; exit code 1 on any failure

The page restores the author's interleave staircase (WP34, March 2026) and makes its words exact: the interleaving,
the line it cancels to, the compression and the taper, and their finite-field twin.

S1  the interleave staircase: for the 153 semiprimes b = pq <= 500, the non-units among 1..k number
    floor(k/p) + floor(k/q) - floor(k/pq) for every k < b; the first appears at k = p; and the pairs (b, k) with
    2 <= k <= b - 1 number 36 662, WP34's census
S2  the line: for every b <= 1000 the wobble |G_k| - (1 - phi(b)/b) k = sum over d | b of mu(d) {k/d} has period b
    and lies strictly between -2^(w - 1) and 2^(w - 1) - 1, w the number of b's prime factors; for b = pq, in (-2, 1)
S3  Mertens: e^g ln y prod_(p <= y) (1 - 1/p) lies within 1/(2 ln^2 y) of 1 (Rosser and Schoenfeld) at y = 10^3..10^7
S4  the sieve over-predicts: near x = 10^5, 10^6, 10^7 its density prod_(p <= sqrt x) (1 - 1/p), over the primes' true
    local density, is near 2e^-g = 1.1229 (Mertens with the prime number theorem)                    [measured]
S5  the compression: pi(x) = theta(x)/ln x + integral_2^x theta(t)/(t ln^2 t) dt exactly, at x = 10^3..10^7, and
    pi(x)/(li(x) - li(2)) tends to 1
S6  the straight line and its envelope: psi(x)/x tends to 1, and |psi(x) - x| < sqrt(x) ln^2 x/(8 pi) for every x
    from 74 to 10^7 (Schoenfeld's bound, which the Riemann hypothesis implies)                      [checked, not proved]
S7  the waves: the explicit formula with the first 10, 30 and 100 zeros of zeta (mpmath) at x = 2.5, 3.5, ..., 100.5:
    the error shrinks as zeros are added
S8  the function-field staircase is exactly straight: counting monic irreducible polynomials by brute force, for
    q = 2 (n <= 10), 3 (n <= 6), 5 (n <= 4) and 7 (n <= 3), sum over d | n of d N_q(d) = q^n, and N_q(n) is Gauss's
    (1/n) sum over d | n of mu(d) q^(n/d)
S9  a curve's waves, with the taper proved: for curves y^2 = x^3 + ax + b over F_p (p = 5, 7, 11, 13), counting points
    over F_(p^n) for n = 1, 2, 3 gives p^n + 1 - alpha^n - conj(alpha)^n, with alpha conj(alpha) = p and
    |alpha + conj(alpha)| <= 2 sqrt p (Hasse, Weil)
S10 Kloosterman sums: |K(a, p)| <= 2 sqrt p for every a and every prime 5 <= p <= 199 (Weil), and the exact moments
    sum_a K^2 = p^2 - p - 1 and sum_a K^4 = 2p^3 - 3p^2 - 3p - 1 (a from 1 to p - 1)
S11 directions: the curve y^2 = x^3 + x + 1 gives each prime p an angle, a_p = 2 sqrt(p) cos(theta_p); over the primes
    from 3 to 10^5 (not 31), the moments of a_p/sqrt p and the Kolmogorov distance to Sato-Tate      [measured]
Prime-forced dispersion (C. A. Luther's question in WP34), section 9:
S12 the CRT cross: for every semiprime b = pq <= 1000, exactly two non-units in each period are followed by a non-unit,
    at the cross's two corners (for b = 2q, one run of three); a prime square has none
S13 Luther's dispersion, WP34's interleave score, from the primes alone: a floor formula equal to the direct count at
    every k for the 153 semiprimes up to 500; over a period 1 - 2/(p + q - 2), (q - 2)/(q - 1) for b = 2q, 1 for p^2
S14 {k/d} and {k/d'} have covariance (g^2 - 1)/(12 d d') over a common period, g = gcd(d, d') (d, d' <= 30, exactly)
S15 the wobble's variance over a period, exactly for every b <= 400, and its limit (2^w - 1)/12 for w primes

numpy + mpmath (mpmath only for S7).  One process, below-normal priority.  ASCII output; writes verify_staircase.log.
Runtime: about a minute.
"""
import ctypes
import itertools
import math
import os
import sys
import time
from itertools import product
from math import gcd, log, sqrt

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
GAMMA = 0.57721566490153286
LOG = None
FAILS = []


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def check(tag, label, ok):
    if not ok:
        FAILS.append(tag)
    say(("PASS  " if ok else "FAIL  ") + tag + "  " + label)


def sieve(n):
    s = np.ones(n + 1, bool)
    s[:2] = False
    for i in range(2, math.isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def factor(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def mobius_divisors(n):
    """the squarefree divisors d of n with mu(d)"""
    ps = factor(n)
    out = []
    for mask in range(1 << len(ps)):
        d, sgn = 1, 1
        for i, p in enumerate(ps):
            if mask >> i & 1:
                d *= p
                sgn = -sgn
        out.append((d, sgn))
    return out


def s1_s2():
    semis = [b for b in range(4, 501) if len(factor(b)) <= 2 and
             (lambda f: (len(f) == 2 and f[0] * f[1] == b) or (len(f) == 1 and f[0] ** 2 == b))(factor(b))]
    ok, pairs = True, 0
    for b in semis:
        f = factor(b)
        p, q = f[0], (f[1] if len(f) == 2 else f[0])
        G = 0
        first = None
        for k in range(1, b):
            if gcd(k, b) > 1:
                G += 1
                if first is None:
                    first = k
            want = k // p + k // q - k // (p * q) if p != q else k // p
            ok &= G == want
        ok &= first == p
        pairs += b - 2
    check("S1", f"the interleave staircase: for the {len(semis)} semiprimes b <= 500 the non-units among 1..k number "
          f"floor(k/p) + floor(k/q) - floor(k/pq), the first is k = p, and the pairs (b, k) number {pairs} (WP34: 36 662)",
          ok and len(semis) == 153 and pairs == 36662)
    ok2, worst = True, {}
    for b in range(2, 1001):
        md = mobius_divisors(b)
        w = len(factor(b))
        dens = sum(sg / d for d, sg in md)                                  # phi(b)/b
        G = 0
        es = []
        for k in range(1, 2 * b + 1):
            G += gcd(k, b) > 1
            e = G - (1 - dens) * k
            es.append(e)
            ok2 &= -2 ** (w - 1) - 1e-9 < e < 2 ** (w - 1) - 1 + 1e-9
            ok2 &= abs(e - sum(sg * (k / d - k // d) for d, sg in md)) < 1e-9
        ok2 &= all(abs(es[i] - es[i + b]) < 1e-9 for i in range(b))
        if w == 2:
            worst[b] = (min(es), max(es))
    lo = min(v[0] for v in worst.values())
    hi = max(v[1] for v in worst.values())
    check("S2", f"the interleaving cancels to a straight line: for every b <= 1000 the wobble about the line of slope "
          f"1 - phi(b)/b is sum mu(d){{k/d}}, has period b and stays in (-2^(w-1), 2^(w-1) - 1); for two primes it "
          f"runs from {lo:.3f} to {hi:.3f}, inside (-2, 1)", ok2 and lo > -2 and hi < 1)


def main():
    global LOG
    t0 = time.time()
    LOG = open(os.path.join(HERE, "verify_staircase.log"), "w", encoding="utf-8")
    say("THE_STAIRCASE.md: the interleave staircase, its line, its compression and its taper")
    s1_s2()

    N = 10 ** 7
    s = sieve(N)
    P = np.nonzero(s)[0]
    # S3 Mertens, with Rosser and Schoenfeld's explicit bounds
    ok3, rows = True, []
    for y in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
        prod = math.exp(np.log1p(-1.0 / P[P <= y]).sum())
        r = math.exp(GAMMA) * log(y) * prod
        ok3 &= abs(r - 1) < 1 / (2 * log(y) ** 2)
        rows.append(f"{r:.6f}")
    check("S3", "Mertens: e^g ln y prod(1 - 1/p) at y = 10^3..10^7 is " + ", ".join(rows) +
          ", each within 1/(2 ln^2 y) of 1", ok3)
    # S4 the sieve's over-prediction
    rows, last = [], None
    for x in (10 ** 5, 10 ** 6, 10 ** 7):
        prod = math.exp(np.log1p(-1.0 / P[P <= math.isqrt(x)]).sum())
        H = x // 10
        local = s[x - H:x].sum() / H
        last = prod / local
        rows.append(f"{last:.4f}")
    check("S4", "the sieve's density over the primes' local density, near 10^5, 10^6 and 10^7: " + ", ".join(rows) +
          f" (2e^-g = {2 * math.exp(-GAMMA):.4f}) [measured]", abs(last - 2 * math.exp(-GAMMA)) < 0.01)
    # S5 the compression: summation by parts, exactly
    logs = np.log(P.astype(float))
    ok5, rows = True, []
    import mpmath
    for x in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
        Pi = P[P <= x]
        th = np.cumsum(logs[:len(Pi)])                                   # theta just after each prime
        ends = np.append(Pi[1:], x).astype(float)                        # theta is th[i] on [Pi[i], ends[i])
        integral = (th * (1 / np.log(Pi.astype(float)) - 1 / np.log(ends))).sum()
        val = th[-1] / log(x) + integral
        ok5 &= abs(val - len(Pi)) < 1e-6 * len(Pi)
        rows.append(f"{len(Pi) / float(mpmath.li(x) - mpmath.li(2)):.5f}")
    check("S5", "the compression: pi(x) = theta(x)/ln x + int theta(t)/(t ln^2 t) dt exactly at x = 10^3..10^7, and "
          "pi(x)/(li(x) - li(2)) = " + ", ".join(rows), ok5)
    # S6 the line and its envelope, at every integer up to 10^7
    Lam = np.zeros(N + 1)
    for p in P:
        pk = int(p)
        while pk <= N:
            Lam[pk] = log(p)
            if pk > N // p:
                break
            pk *= p
    psi = np.cumsum(Lam)
    n = np.arange(74, N + 1, dtype=float)
    dev = np.maximum(np.abs(psi[74:] - n), np.abs(psi[74:] - (n + 1)))  # sup over [n, n + 1)
    bound = np.sqrt(n) * np.log(n) ** 2 / (8 * math.pi)
    rows = [f"{psi[x] / x:.6f}" for x in (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7)]
    check("S6", "the straight line: psi(x)/x at 10^4..10^7 = " + ", ".join(rows) + f"; |psi(x) - x| stays below "
          f"sqrt(x) ln^2 x/(8 pi) from 74 to 10^7 (largest ratio {float((dev / bound).max()):.3f}) [checked, not proved]",
          bool((dev < bound).all()))
    # S7 the explicit formula
    mpmath.mp.dps = 20
    zeros = [complex(mpmath.zetazero(k)) for k in range(1, 101)]
    xs = np.arange(2.5, 101, 1.0)
    errs = {}
    for M in (10, 30, 100):
        e = []
        for x in xs:
            waves = sum(2 * (x ** r / r).real for r in zeros[:M])
            approx = x - waves - log(2 * math.pi) - 0.5 * log(1 - x ** -2)
            e.append(approx - psi[int(x)])
        errs[M] = float(np.sqrt(np.mean(np.square(e))))
    check("S7", "the waves: the explicit formula with the first 10, 30 and 100 zeros of zeta misses psi at x = 2.5 .. "
          f"100.5 by {errs[10]:.3f}, {errs[30]:.3f} and {errs[100]:.3f} (root mean square)",
          errs[10] > errs[30] > errs[100] and errs[100] < 0.5)
    # S8 the function-field staircase
    ok8, rows = True, []
    for q, nmax in ((2, 10), (3, 6), (5, 4), (7, 3)):
        Nq = {}
        for deg in range(1, nmax + 1):
            reducible = set()
            for d in range(1, deg // 2 + 1):
                for f in product(range(q), repeat=d):
                    for g in product(range(q), repeat=deg - d):
                        F, Gp = list(f) + [1], list(g) + [1]                # monic, low degree first
                        h = [0] * (deg + 1)
                        for i, a in enumerate(F):
                            for j, c in enumerate(Gp):
                                h[i + j] = (h[i + j] + a * c) % q
                        reducible.add(tuple(h))
            Nq[deg] = q ** deg - len(reducible)
            divs = [d for d in range(1, deg + 1) if deg % d == 0]
            ok8 &= sum(d * Nq[d] for d in divs) == q ** deg
            gauss = sum(sg * q ** (deg // d) for d, sg in mobius_divisors(deg)) // deg if deg > 1 else q
            ok8 &= Nq[deg] == gauss
        rows.append(f"q={q}: " + " ".join(str(Nq[d]) for d in range(1, nmax + 1)))
    check("S8", "the function-field staircase is exactly straight: sum over d | n of d N_q(d) = q^n, and N_q(n) is "
          "Gauss's formula (" + "; ".join(rows) + ")", ok8)
    # S9 Hasse-Weil
    ok9, tested = True, 0
    for p in (5, 7, 11, 13):
        eps = next(e for e in range(2, p) if pow(e, (p - 1) // 2, p) == p - 1)
        cubic = next((a, b) for a in range(p) for b in range(1, p) if all((x ** 3 + a * x + b) % p for x in range(p)))
        mods = {1: [1], 2: [(-eps) % p, 0, 1], 3: [cubic[1], cubic[0], 0, 1]}         # monic moduli, low degree first
        for (A, B) in ((1, 1), (2, 3), (p - 1, 1)):
            if (4 * A ** 3 + 27 * B * B) % p == 0:
                continue
            counts = {}
            for deg in (1, 2, 3):
                f = mods[deg]

                def mul(u, v, f=f, deg=deg):
                    h = [0] * (2 * deg - 1)
                    for i, a in enumerate(u):
                        if a:
                            for j, c in enumerate(v):
                                h[i + j] = (h[i + j] + a * c) % p
                    for i in range(len(h) - 1, deg - 1, -1):                 # reduce by the monic modulus
                        c = h[i]
                        if c:
                            for j in range(deg + 1):
                                h[i - deg + j] = (h[i - deg + j] - c * f[j]) % p
                    return h[:deg]

                def power(u, e):
                    r, b = [1] + [0] * (deg - 1), u
                    while e:
                        if e & 1:
                            r = mul(r, b)
                        b = mul(b, b)
                        e >>= 1
                    return r

                one, half = [1] + [0] * (deg - 1), (p ** deg - 1) // 2
                total = 1                                                   # the point at infinity
                for xv in product(range(p), repeat=deg):
                    xv = list(xv)
                    x3 = mul(mul(xv, xv), xv)
                    rhs = [(x3[i] + A * xv[i] + (B if i == 0 else 0)) % p for i in range(deg)]
                    if not any(rhs):
                        total += 1
                    elif power(rhs, half) == one:
                        total += 2
                counts[deg] = total
            a = p + 1 - counts[1]
            s_n = {1: a, 2: a * a - 2 * p}
            s_n[3] = a * s_n[2] - p * s_n[1]
            ok9 &= abs(a) <= 2 * sqrt(p) and all(counts[d] == p ** d + 1 - s_n[d] for d in (1, 2, 3))
            tested += 1
    check("S9", f"a curve's waves: on {tested} curves over F_5, F_7, F_11 and F_13 the points over F_(p^n), n = 1, 2, 3, "
          "number p^n + 1 - alpha^n - conj(alpha)^n with |alpha| = sqrt p (Hasse, Weil)", ok9 and tested >= 10)
    # S10 Kloosterman sums
    ok10 = True
    for p in [int(v) for v in P[(P >= 5) & (P <= 199)]]:
        a = np.arange(1, p)
        inv = np.array([pow(int(v), -1, p) for v in a])
        K = np.array([np.cos(2 * np.pi * ((a + m * inv) % p) / p).sum() for m in range(1, p)])
        ok10 &= bool((np.abs(K) <= 2 * sqrt(p) + 1e-9).all())
        ok10 &= abs((K ** 2).sum() - (p * p - p - 1)) < 1e-6 and abs((K ** 4).sum() - (2 * p ** 3 - 3 * p * p - 3 * p - 1)) < 1e-4
    check("S10", "Kloosterman sums: |K(a, p)| <= 2 sqrt p at every a for every prime from 5 to 199, and sum K^2 = "
          "p^2 - p - 1, sum K^4 = 2p^3 - 3p^2 - 3p - 1", ok10)
    # S11 directions: Sato-Tate for a curve without complex multiplication
    ap = []
    for p in [int(v) for v in P[(P >= 3) & (P < 10 ** 5)]]:
        if p == 31:
            continue
        x = np.arange(p, dtype=np.int64)
        sq = np.zeros(p, bool)
        sq[(x * x) % p] = True
        v = (x * x % p * x + x + 1) % p
        chi = np.where(v == 0, 0, np.where(sq[v], 1, -1))
        ap.append((p, -int(chi.sum())))
    t = np.array([a / sqrt(p) for p, a in ap])
    mom = [float((t ** k).mean()) for k in (2, 4, 6)]
    theta = np.sort(np.arccos(np.clip(t / 2, -1, 1)))
    F_st = (theta - np.sin(theta) * np.cos(theta)) / math.pi
    F_unif = theta / math.pi
    emp = np.arange(1, len(theta) + 1) / len(theta)
    ks_st = float(np.max(np.abs(emp - F_st)))
    ks_u = float(np.max(np.abs(emp - F_unif)))
    check("S11", f"directions: for y^2 = x^3 + x + 1 at the {len(t)} primes from 3 to 10^5 (not 31), a_p/sqrt p has "
          f"moments {mom[0]:.3f}, {mom[1]:.3f}, {mom[2]:.3f} (Sato-Tate 1, 2, 5); the angles lie at Kolmogorov distance "
          f"{ks_st:.4f} from Sato-Tate's law and {ks_u:.4f} from a uniform angle [measured]",
          abs(mom[0] - 1) < 0.05 and abs(mom[1] - 2) < 0.15 and ks_st < 0.02 < ks_u)
    s12_s15()
    say()
    say(f"{15 - len(FAILS)} of 15 pass" + (f"; failed: {', '.join(FAILS)}" if FAILS else "") +
        f"  ({time.time() - t0:.0f} s)")
    LOG.close()
    sys.exit(1 if FAILS else 0)


def semiprimes(limit):
    out = []
    for b in range(4, limit + 1):
        f = factor(b)
        if (len(f) == 2 and f[0] * f[1] == b) or (len(f) == 1 and f[0] ** 2 == b):
            out.append((b, f[0], f[1] if len(f) == 2 else f[0]))
    return out


def interleave_direct(b, k):
    s = [gcd(x, b) > 1 for x in range(1, k + 1)]
    T = sum(1 for i in range(k - 1) if s[i] != s[i + 1])
    G = sum(s)
    return T / (2 * min(k - G, G)) if min(k - G, G) > 0 else 0.0


def corners(p, q):
    """the two n mod pq with n and n + 1 both non-units: n = 0 mod p, -1 mod q, and n = 0 mod q, -1 mod p"""
    return (p * ((q - 1) * pow(p, -1, q) % q), q * ((p - 1) * pow(q, -1, p) % p))


def interleave_formula(p, q, k):
    """WP34's interleave score from the primes alone (b = pq with p < q, or b = p^2 with q = p)"""
    b = p * q
    if p == q:
        G, A = k // p, 0
    else:
        G = k // p + k // q - k // b
        A = sum((k - 1 - r) // b + 1 for r in corners(p, q) if k - 1 >= r)
    last = k % p == 0 or k % q == 0
    T = 2 * (G - A) - (1 if last else 0)
    return T / (2 * min(k - G, G)) if min(k - G, G) > 0 else 0.0


def wobble_variance(primes):
    """the variance of e(k) = sum over d | b of mu(d){k/d} over a period, b = product of the given primes, from the
    covariance (g^2 - 1)/(12 d d') of {k/d} and {k/d'}"""
    from fractions import Fraction
    subsets = [S for r in range(1, len(primes) + 1) for S in itertools.combinations(primes, r)]
    tot = Fraction(0)
    for S in subsets:
        for S2 in subsets:
            d, d2 = math.prod(S), math.prod(S2)
            g = math.prod(set(S) & set(S2)) if set(S) & set(S2) else 1
            tot += Fraction((-1) ** (len(S) + len(S2)) * (g * g - 1), 12 * d * d2)
    return tot


def s12_s15():
    from fractions import Fraction
    # S12: the corners of the CRT cross
    ok = True
    for b, p, q in semiprimes(1000):
        adj = [n for n in range(1, b - 1) if gcd(n, b) > 1 and gcd(n + 1, b) > 1]
        if p == q:
            ok &= adj == []
        else:
            ok &= sorted(adj) == sorted(corners(p, q))
            if p == 2:
                ok &= sorted(adj) == [q - 1, q]                         # one run of three: q - 1, q, q + 1
    check("S12", "the CRT cross: for every semiprime b = pq <= 1000 exactly two non-units are followed by a non-unit "
          "in each period, at the cross's two corners (for b = 2q one run of three: q - 1, q, q + 1); a prime square "
          "has none", ok)
    # S13: Luther's dispersion as a formula from the primes
    ok, full = True, True
    for b, p, q in semiprimes(500):
        for k in range(2, b):
            ok &= abs(interleave_formula(p, q, k) - interleave_direct(b, k)) < 1e-12
        want = 1.0 if p == q else ((q - 2) / (q - 1) if p == 2 else 1 - 2 / (p + q - 2))
        full &= abs(interleave_formula(p, q, b - 1) - want) < 1e-12
    wp34 = [round(interleave_direct(b, 9), 3) for b in (15, 21, 22, 26, 34, 38)]
    check("S13", "Luther's dispersion (WP34's interleave score) from the primes alone: the floor formula equals the "
          "direct count at every k for all 153 semiprimes up to 500; over a period it is 1 - 2/(p + q - 2), "
          f"(q - 2)/(q - 1) for b = 2q, and 1 for p^2; WP34's k = 9 values come back ({wp34})",
          ok and full and wp34 == [0.625, 0.625, 1.0, 1.0, 1.0, 1.0])
    # S14: the covariance of fractional parts
    ok = True
    for d in range(1, 31):
        for d2 in range(1, 31):
            L = d * d2 // gcd(d, d2)
            ks = range(L)
            ex = Fraction(sum(k % d for k in ks), d * L)
            ey = Fraction(sum(k % d2 for k in ks), d2 * L)
            exy = Fraction(sum((k % d) * (k % d2) for k in ks), d * d2 * L)
            g = gcd(d, d2)
            ok &= exy - ex * ey == Fraction(g * g - 1, 12 * d * d2)
    check("S14", "over a common period, {k/d} and {k/d'} have covariance (g^2 - 1)/(12 d d'), g = gcd(d, d'), exactly, "
          "for every d, d' <= 30 (the discrete form of Franel's integral)", ok)
    # S15: the wobble's spread, and its limit (2^w - 1)/12
    ok = True
    for b in range(2, 401):
        ps = factor(b)
        es = []
        for k in range(b):
            G = sum(1 for x in range(1, k + 1) if gcd(x, b) > 1)
            dens = Fraction(math.prod(p_ - 1 for p_ in ps) * b // math.prod(ps), b)     # phi(b)/b
            es.append(G - (1 - dens) * k)
        mean = sum(es, Fraction(0)) / b
        var = sum(((e - mean) ** 2 for e in es), Fraction(0)) / b
        ok &= var == wobble_variance(ps)
    big = [1000003, 1000033, 1000037, 1000039]
    lim = [float(wobble_variance(big[:w])) for w in (1, 2, 3, 4)]
    check("S15", "the wobble's variance over a period is (1/12) sum over nonempty prime sets S, S' of "
          "(-1)^(|S| + |S'|)(d_(S and S')^2 - 1)/(d_S d_S'), exactly, for every b <= 400; with primes near 10^6 it is "
          + ", ".join(f"{v:.6f}" for v in lim) + " for 1 to 4 primes, against (2^w - 1)/12 = 0.083333, 0.25, 0.583333, "
          "1.25", ok and all(abs(v - (2 ** w - 1) / 12) < 1e-4 for v, w in zip(lim, (1, 2, 3, 4))))


if __name__ == "__main__":
    main()
