"""verify_lens_primes.py -- the checks behind THE_LENS.md section 8, "The lens on the primes".

Each row of that table restates a classical result next to one of the author's sentences of 20 November 2026. The
numbers were first computed in the lens handoff of that day. This script recomputes every one of them with its own
code (it does not run or import the handoff's scripts) and compares.

  python -I verify_lens_primes.py            (numpy, mpmath, and PARI through cypari or cypari2; a few minutes)

Nothing here is new mathematics, and nothing here bears on the Riemann hypothesis: every statement checked is a
theorem, a definition, or a finite computation.
"""
import cmath
import math
import sys
import time
from fractions import Fraction

import numpy as np
import mpmath as mp

RESULTS = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def low_priority():
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        k32.GetCurrentProcess.restype = ctypes.c_void_p
        k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint]
        k32.SetPriorityClass(k32.GetCurrentProcess(), 0x4000)
    except Exception:
        pass


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]


def von_mangoldt(n, P):
    lam = np.zeros(n + 1)
    for p in P:
        q, lp = int(p), math.log(int(p))
        while q <= n:
            lam[q] = lp
            q *= int(p)
    return lam


# ---------------------------------------------------------------------------------------------------------------
# row 1: "primes are the inside edges of coins" -- the divisor flip, Wilson, Zagier
# ---------------------------------------------------------------------------------------------------------------
def row_flips():
    M = 10 ** 5
    d = np.zeros(M + 1, dtype=np.int32)
    for k in range(1, M + 1):
        d[k::k] += 1
    P = set(primes_upto(M).tolist())
    three = {n for n in range(2, M + 1) if d[n] == 3}
    check("flip d -> n/d", three == {p * p for p in P if p * p <= M},
          f"the {len(three)} numbers up to {M} with exactly three divisors (one pair of sides and the edge sqrt n) "
          f"are the prime squares")
    ok = True
    for n in range(2, 3001):
        f = 1
        for k in range(2, n):
            f = f * k % n
        ok &= ((f == n - 1) == (n in P))
    check("Wilson", ok, "(n - 1)! = -1 (mod n) exactly when n is prime, n = 2..3000")
    bad = []
    for n in range(5, 2001, 4):
        S = [(x, y, (n - x * x) // (4 * y)) for x in range(1, math.isqrt(n) + 1) for y in range(1, n)
             if n - x * x > 0 and (n - x * x) % (4 * y) == 0]

        def zag(t):
            x, y, z = t
            if x < y - z:
                return (x + 2 * z, z, y - x - z)
            if x < 2 * y:
                return (2 * y - x, y, x - y + z)
            return (x - 2 * y, x - y + z, y)
        if not all(zag(zag(t)) == t for t in S):
            bad.append((n, 'not an involution'))
        fixed = sum(zag(t) == t for t in S)
        if fixed != d[n] // 2:
            bad.append((n, fixed))
        r = math.isqrt(n)
        if (fixed == 1) != (n in P or (r * r == n and r in P)):
            bad.append((n, 'one fixed point'))
    check("Zagier", not bad, "for every n = 1 (mod 4) up to 2000 his map is an involution of {x^2 + 4yz = n} with "
          "floor(tau(n)/2) fixed points; exactly one when n is a prime or a prime square")


# ---------------------------------------------------------------------------------------------------------------
# row 2: Liouville's walk; Polya's conjecture holds to 10^7 (it fails at 906 150 257)
# ---------------------------------------------------------------------------------------------------------------
def row_liouville():
    N = 10 ** 7
    P = primes_upto(N)
    om = np.zeros(N + 1, dtype=np.int8)
    for p in P:
        q = int(p)
        while q <= N:
            om[q::q] += 1
            q *= int(p)
    lam = np.where(om % 2 == 0, 1, -1).astype(np.int64)
    lam[0] = 0
    M = 200000
    s = np.zeros(M + 1, dtype=np.int64)
    for k in range(1, M + 1):
        s[k::k] += lam[k]
    sq = np.zeros(M + 1, dtype=np.int64)
    sq[[k * k for k in range(1, math.isqrt(M) + 1)]] = 1
    check("Liouville's divisor sum", np.array_equal(s[1:], sq[1:]),
          f"sum of lambda(d) over d | n is 1 on squares and 0 elsewhere, n <= {M}")
    L = np.cumsum(lam)
    x = np.arange(N + 1, dtype=float)
    ratio = L[100:] / np.sqrt(x[100:])
    check("Polya's walk to 10^7", L[2:].max() <= 0 and -1.34 < ratio.min() < -1.32,
          f"L(x) = sum of lambda(n), n <= x, is never positive for 2 <= x <= 10^7 (largest {int(L[2:].max())}); "
          f"L(x)/sqrt(x) for 100 <= x <= 10^7 lies in [{ratio.min():.3f}, {ratio.max():.3f}]")


# ---------------------------------------------------------------------------------------------------------------
# rows 3-4: the Davenport-Heilbronn function: balance (a functional equation) without an Euler product
# ---------------------------------------------------------------------------------------------------------------
mp.mp.dps = 30
CHI = [0, 1, 1j, -1j, -1]                     # the character mod 5 with chi(2) = i
CHIB = [0, 1, -1j, 1j, -1]
KAPPA = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
A_, B_ = (1 - 1j * KAPPA) / 2, (1 + 1j * KAPPA) / 2


def dh(s):
    return A_ * mp.dirichlet(s, CHI) + B_ * mp.dirichlet(s, CHIB)


def row_davenport_heilbronn():
    G = lambda s: (mp.mpf(5) / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * dh(s)   # chi is odd
    s0 = mp.mpc('0.31', '7.3')
    fe = abs(G(s0) - G(1 - s0)) / abs(G(s0))
    check("Davenport-Heilbronn balance", fe < 1e-20,
          f"Lambda(s) = (5/pi)^((s+1)/2) Gamma((s+1)/2) f(s) satisfies Lambda(s) = Lambda(1 - s): relative error {float(fe):.1e}")
    z = mp.findroot(dh, mp.mpc('0.8085', '85.6993'))
    spira = mp.mpc('0.808517182456637', '85.699348485377592')
    # its coefficients are real, so with the balance its zeros come in fours: z, conj(z), 1 - z, 1 - conj(z)
    z2 = mp.findroot(dh, 1 - mp.conj(z) + mp.mpc('0.001', '0.001'))
    check("its zero off the line", abs(z - spira) < 1e-14 and abs(dh(z)) < 1e-20 and abs(z2 - (1 - mp.conj(z))) < 1e-20,
          f"f has a zero at {mp.nstr(z.real, 16)} + {mp.nstr(z.imag, 17)} i (Spira 1994), |f| = {mp.nstr(abs(dh(z)), 3)}; "
          f"its mirror 1 - conj(z) = {mp.nstr(z2.real, 16)} + {mp.nstr(z2.imag, 17)} i is a zero too")
    a = lambda n: A_ * CHI[n % 5] + B_ * CHIB[n % 5]
    check("no Euler product", abs(a(6) - 1) < 1e-25 and abs(a(2) * a(3) + KAPPA ** 2) < 1e-25,
          f"its coefficients have a(6) = {mp.nstr(mp.re(a(6)), 6)} but a(2) a(3) = -kappa^2 = "
          f"{mp.nstr(mp.re(a(2) * a(3)), 6)}, so it is not multiplicative")


# ---------------------------------------------------------------------------------------------------------------
# row 5: Lehmer's pair
# ---------------------------------------------------------------------------------------------------------------
def row_lehmer():
    mp.mp.dps = 20
    Z = mp.siegelz
    a, b = mp.findroot(Z, 7005.06), mp.findroot(Z, 7005.10)
    m = mp.findroot(lambda t: mp.diff(Z, t), (a + b) / 2)
    ts = np.arange(6990, 7020, 0.01)
    v = np.array([abs(float(Z(t))) for t in ts])
    peaks = [v[i] for i in range(1, len(v) - 1) if v[i] > v[i - 1] and v[i] > v[i + 1]]
    check("Lehmer's pair", abs(float(b - a) - 0.0377) < 0.0005 and abs(abs(float(Z(m))) - 0.00397) < 0.00002,
          f"zeros of Z(t) at {mp.nstr(a, 12)} and {mp.nstr(b, 12)}, {float(b - a):.4f} apart; |Z| between them peaks at "
          f"{abs(float(Z(m))):.5f}, against a median peak of {np.median(peaks):.2f} over 6990-7020 ({len(peaks)} peaks)")
    mp.mp.dps = 30


# ---------------------------------------------------------------------------------------------------------------
# row 6: last digits of consecutive primes (Lemke Oliver and Soundararajan)
# ---------------------------------------------------------------------------------------------------------------
def row_last_digits():
    P = primes_upto(10 ** 8)
    P = P[P > 10]
    out = {}
    for m in (10, 12, 30):
        r = P % m
        cls = np.unique(r)
        ix = np.searchsorted(cls, r)
        k = len(cls)
        half = len(ix) // 2
        T = np.zeros((k, k))
        np.add.at(T, (ix[:half - 1], ix[1:half]), 1)
        pred = T.argmax(1)
        acc = np.mean(pred[ix[half:-1]] == ix[half + 1:])
        out[m] = (k, acc * k, np.mean(np.diag(T / T.sum(1, keepdims=True))), np.mean(ix[:-1] == ix[1:]))
    k, gain10, diag10, rep10 = out[10]
    check("last digits", abs(diag10 - 0.169) < 0.001 and abs(gain10 - 1.25) < 0.01 and abs(out[12][1] - 1.26) < 0.01
          and abs(out[30][1] - 1.87) < 0.01,
          f"primes 11..10^8: a last digit repeats in {rep10:.4f} of consecutive pairs ({diag10:.4f} averaged over the "
          f"four digits, first half), against 0.25; predicting the next residue from the last beats chance by "
          f"x{gain10:.3f} mod 10, x{out[12][1]:.3f} mod 12, x{out[30][1]:.3f} mod 30")


# ---------------------------------------------------------------------------------------------------------------
# row 7: the primes' spectrum (the explicit formula)
# ---------------------------------------------------------------------------------------------------------------
def row_spectrum():
    X = 10 ** 6
    P = primes_upto(X)
    lam = von_mangoldt(X, P)
    n = np.arange(1, X + 1, dtype=float)
    ln = np.log(n)
    w = (lam[1:] - 1.0) * (1 - ln / math.log(X)) / np.sqrt(n)
    T = np.arange(5, 60, 0.01)
    F = np.array([-(w * np.cos(t * ln)).sum() for t in T])
    pk = sorted(((F[i], T[i]) for i in range(1, len(T) - 1) if F[i] > F[i - 1] and F[i] > F[i + 1]), reverse=True)
    top = sorted(t for _, t in pk[:13])
    zeros = [float(mp.zetazero(j).imag) for j in range(1, 14)]
    miss = max(abs(a - b) for a, b in zip(top, zeros))
    check("the primes' spectrum", miss < 0.008,
          f"the 13 strongest lines of sum (Lambda(n) - 1) n^(-1/2) (1 - ln n/ln X) cos(t ln n), n <= 10^6, "
          f"sit at the first 13 zeros of zeta, within {miss:.3f}")
    # the failure worth keeping: a sharp cutoff, and the main term left in
    w2 = lam[1:] / np.sqrt(n)
    F2 = np.array([-(w2 * np.cos(t * ln)).sum() for t in T])
    pk2 = sorted(((F2[i], T[i]) for i in range(1, len(T) - 1) if F2[i] > F2[i - 1] and F2[i] > F2[i + 1]),
                 reverse=True)
    top2 = sorted(t for _, t in pk2[:13])
    hit2 = sum(min(abs(t - z) for t in top2) < 0.05 for z in zeros)
    gaps = np.diff(sorted(t for _, t in pk2))
    check("the same spectrum done wrong", hit2 <= 6,
          f"with a sharp cutoff and the main term left in, only {hit2} of the first 13 zeros lie within 0.05 of one "
          f"of the 13 strongest lines; the peaks ring at median spacing {np.median(gaps):.3f}, against "
          f"2 pi/ln X = {2 * math.pi / math.log(X):.3f}")


# ---------------------------------------------------------------------------------------------------------------
# row 8: brightness -- |zeta(s)| <= zeta(sigma), Mertens' 3-4-1, Li's criterion
# ---------------------------------------------------------------------------------------------------------------
def row_brightness():
    mp.mp.dps = 15
    sig = mp.mpf('1.05')
    ts = np.arange(0.5, 100, 0.1)

    def profile(L):
        L0 = abs(L(sig))
        return np.array([float(L0 ** 3 * abs(L(mp.mpc(sig, t))) ** 4 * abs(L(mp.mpc(sig, 2 * t)))) for t in ts])
    hz, hf = profile(mp.zeta), profile(dh)
    brighter = max(abs(mp.zeta(mp.mpc(sig, t))) for t in ts[::5]) > mp.zeta(sig)
    check("Mertens' 3-4-1", hz.min() >= 1 and not brighter and abs(hz.min() - 257.5) < 0.5
          and hf.min() < 0.01 and abs(ts[hf.argmin()] - 85.7) < 0.15,
          f"at sigma = 1.05, zeta(s)^3 |zeta(s+it)|^4 |zeta(s+2it)| >= {hz.min():.1f} for 0.5 <= t < 100, and no "
          f"|zeta(1.05 + it)| exceeds zeta(1.05); for the Davenport-Heilbronn blend the same product falls to "
          f"{hf.min():.4f} at t = {ts[hf.argmin()]:.1f}, below 1 at {np.mean(hf < 1):.2f} of the heights")
    mp.mp.dps = 40
    xi = lambda s: s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    M, r = 64, mp.mpf(1) / 4                  # Taylor coefficients of log xi(1/(1 - z)) by a 64-point contour
    vals = [mp.log(xi(1 / (1 - r * mp.expjpi(2 * mp.mpf(k) / M)))) for k in range(M)]
    lam = [n * mp.re(sum(vals[k] * mp.expjpi(-2 * mp.mpf(k) * n / M) for k in range(M)) / M / r ** n)
           for n in range(1, 13)]
    l1 = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    check("Li's numbers", all(v > 0 for v in lam) and abs(lam[0] - l1) < 1e-20,
          f"lambda_1..lambda_12 = {', '.join(mp.nstr(v, 6) for v in lam)}, all positive; "
          f"lambda_1 = 1 + gamma/2 - ln(4 pi)/2 = {mp.nstr(l1, 9)}")
    mp.mp.dps = 30


# ---------------------------------------------------------------------------------------------------------------
# row 9: Moebius balance
# ---------------------------------------------------------------------------------------------------------------
def row_moebius():
    N = 10 ** 7
    mu = np.ones(N + 1, dtype=np.int8)
    for p in primes_upto(N):
        p = int(p)
        mu[p::p] *= -1
        if p * p <= N:
            mu[p * p::p * p] = 0
    mu[0] = 0
    M = 100000
    s = np.zeros(M + 1, dtype=np.int64)
    for k in range(1, M + 1):
        s[k::k] += mu[k]
    c = np.cumsum(mu[1:] / np.arange(1, N + 1))
    lo = [c[10 ** k - 1] * 10 ** (k / 2) for k in range(1, 8)]
    check("Moebius balance", s[1] == 1 and not s[2:].any() and min(lo) > -0.22 and max(lo) < 0.33,
          f"sum of mu(d) over d | n is 0 for 1 < n <= {M}; sqrt(x) * sum of mu(n)/n, n <= x, at x = 10..10^7: "
          + ', '.join(f"{v:+.3f}" for v in lo))


# ---------------------------------------------------------------------------------------------------------------
# row 10: the circle method -- the primes' brightness at a/q is mu(q)/phi(q)
# ---------------------------------------------------------------------------------------------------------------
def row_crossings():
    N = 10 ** 6
    lam = von_mangoldt(N, primes_upto(N))
    n = np.arange(N + 1)
    S = lambda a: (lam * np.exp(2j * np.pi * a * n)).sum() / N

    def mobius(q):
        m, k, p = 1, q, 2
        while p * p <= k:
            if k % p == 0:
                k //= p
                if k % p == 0:
                    return 0
                m = -m
            p += 1
        return -m if k > 1 else m
    phi = lambda q: sum(1 for a in range(1, q + 1) if math.gcd(a, q) == 1)
    worst = max(abs(S(1 / q) - mobius(q) / phi(q)) for q in range(1, 17))
    rng = np.random.default_rng(1)
    rand = np.median([abs(S(a)) for a in rng.random(200)])
    check("the circle method", worst < 0.002 and rand < 0.01,
          f"(1/N) sum of Lambda(n) e(n/q), N = 10^6, is within {worst:.4f} of mu(q)/phi(q) for q = 1..16; at 200 "
          f"random points its median size is {rand:.4f}")


# ---------------------------------------------------------------------------------------------------------------
# row 11: wheel 9, the prime-square wheels, and the free turns (Banach-Tarski)
# ---------------------------------------------------------------------------------------------------------------
def row_wheels():
    P = primes_upto(10 ** 7)
    P = P[P > 7]
    cnt = np.bincount(P % 9, minlength=9)
    tri = {t: sum(cnt[a] for a in t) / len(P) for t in ((0, 3, 6), (1, 4, 7), (2, 5, 8))}
    bal = max(abs(sum(cnt[a] * cmath.exp(2j * math.pi * a / 9) for a in t)) / max(sum(cnt[a] for a in t), 1)
              for t in ((1, 4, 7), (2, 5, 8)))
    cyc, x = [], 1
    for _ in range(6):
        cyc.append(x)
        x = 2 * x % 9
    w = {q: abs(np.exp(2j * np.pi * (P % q) / q).mean()) for q in (9, 25, 49)}
    check("wheel 9", tri[(0, 3, 6)] == 0 and abs(tri[(1, 4, 7)] - 0.5) < 0.001 and bal < 0.0005
          and cyc == [1, 2, 4, 8, 7, 5] and max(w.values()) < 0.001,
          f"primes 11..10^7 mod 9: the triangle 0,3,6 empty, 1,4,7 holds {tri[(1, 4, 7)]:.4f} and 2,5,8 "
          f"{tri[(2, 5, 8)]:.4f}, each balanced within {bal:.5f} of the centre; doubling runs {cyc}; balance point of "
          f"all primes on wheels 9, 25, 49: {w[9]:.5f}, {w[25]:.5f}, {w[49]:.5f}")
    c, s = Fraction(3, 5), Fraction(4, 5)
    gens = {'a': ((c, -s, 0), (s, c, 0), (0, 0, 1)), 'A': ((c, s, 0), (-s, c, 0), (0, 0, 1)),
            'b': ((1, 0, 0), (0, c, -s), (0, s, c)), 'B': ((1, 0, 0), (0, c, s), (0, -s, c))}
    inv = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    mul = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    seen, layer, total = {I}, {'': I}, 0
    for _ in range(8):
        new = {}
        for word, Mx in layer.items():
            for g in 'aAbB':
                if word and inv[word[-1]] == g:
                    continue
                new[word + g] = mul(Mx, gens[g])
        total += len(new)
        seen.update(new.values())
        layer = new
    check("free turns", total == 13120 and len(seen) == total + 1,
          f"turns by arccos(3/5) about two perpendicular axes: the {total} reduced words of length 1-8 give "
          f"{len(seen) - 1} distinct rotations, none the identity (exact arithmetic)")


# ---------------------------------------------------------------------------------------------------------------
# rows 12-13: ranks and the height pairing (PARI)
# ---------------------------------------------------------------------------------------------------------------
def row_curves():
    try:
        from cypari import pari
    except ImportError:
        import cypari2
        pari = cypari2.Pari()
    pari.allocatemem(4 * 10 ** 8)
    table = {"11a1": [0, -1, 1, -10, -20], "37a1": [0, 0, 1, -1, 0], "389a1": [0, 1, 1, -2, 0], "5077a1": [0, 0, 1, -7, 6]}
    got = {}
    for name, ai in table.items():
        E = pari.ellinit(ai)
        got[name] = (int(pari.ellrank(E)[0]), int(pari.ellanalyticrank(E)[0]), int(pari.elltors(E)[0]))
    check("rank = order of vanishing", [got[k][:2] for k in table] == [(0, 0), (1, 1), (2, 2), (3, 3)] and got["11a1"][2] == 5,
          "11a1, 37a1, 389a1, 5077a1: rank and analytic rank " + ', '.join(f"{got[k][0]}/{got[k][1]}" for k in table)
          + f"; 11a1 has torsion of order {got['11a1'][2]} and L(1) is not 0")
    E = pari.ellinit(table["389a1"])
    P1, P2 = [-1, 1], [0, 0]
    h = lambda X: float(pari.ellheight(E, X))
    hs = h(pari.elladd(E, P1, P2))
    link = (hs - h(P1) - h(P2)) / 2
    reg = h(P1) * h(P2) - link ** 2
    ang = math.degrees(math.acos(link / math.sqrt(h(P1) * h(P2))))
    detH = float(pari.matdet(pari.ellheightmatrix(E, [P1, P2])))
    check("the pairing as a law of cosines", abs(reg - detH) < 1e-12 and abs(reg - 0.15246018) < 1e-8,
          f"389a1, P = (-1, 1), Q = (0, 0): h(P) = {h(P1):.6f}, h(Q) = {h(P2):.6f}, h(P + Q) = {hs:.6f}; "
          f"<P, Q> = {link:.6f}, angle {ang:.2f} degrees, regulator {reg:.8f}")


# ---------------------------------------------------------------------------------------------------------------
# row 14: Cramer -- in log time the normalised error has mean square sum 1/|rho|^2 = 2 + gamma - ln 4 pi
# ---------------------------------------------------------------------------------------------------------------
def row_cramer():
    X = 2 * 10 ** 7
    psi = np.cumsum(von_mangoldt(X, primes_upto(X)))
    t = np.linspace(math.log(1000), math.log(X), 400000)
    x = np.exp(t)
    e = (psi[np.floor(x).astype(np.int64)] - x) / np.sqrt(x)
    rms = []
    for a, b in ((3, 4), (4, 5), (5, 6), (6, 7.3)):
        m = (t >= a * math.log(10)) & (t < b * math.log(10))
        rms.append(math.sqrt(np.mean(e[m] ** 2)))
    pred = math.sqrt(2 + 0.5772156649015329 - math.log(4 * math.pi))
    check("Cramer's mean square", all(abs(r - pred) < 0.01 for r in rms),
          f"(psi(x) - x)/sqrt(x), sampled evenly in ln x: rms {', '.join(f'{r:.3f}' for r in rms)} over 10^3-10^4, "
          f"10^4-10^5, 10^5-10^6, 10^6-2*10^7; sqrt(2 + gamma - ln 4 pi) = {pred:.4f}")


if __name__ == '__main__':
    low_priority()
    t0 = time.time()
    for f in (row_flips, row_liouville, row_davenport_heilbronn, row_lehmer, row_last_digits, row_spectrum,
              row_brightness, row_moebius, row_crossings, row_wheels, row_curves, row_cramer):
        f()
    npass = sum(ok for _, ok in RESULTS)
    print(f"\n{npass} of {len(RESULTS)} checks pass ({time.time() - t0:.0f} s)")
    sys.exit(0 if npass == len(RESULTS) else 1)
