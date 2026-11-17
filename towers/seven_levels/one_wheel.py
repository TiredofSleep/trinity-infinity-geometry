"""one_wheel.py -- round 29 of PREREG.md: one wheel, the qudit T state, and the ladder of diagonal magic states.

    "where can we try and extend this to be useful on the frontier of applications?"  -- the author, 17 November 2026
    "1 yes, then the qudit round"  -- the author, 17 November 2026

A phase state on one wheel of p levels (p an odd prime) is psi_f = sum_x w^f(x) |x> / sqrt p, w = exp(2 pi i / p), for a
function f: F_p -> F_p.  When f is a polynomial of degree d < p, psi_f is the magic state of a diagonal gate of the d-th
level of the Clifford hierarchy (Cui, Gottesman and Krishna); d = 3 is the qudit T gate (Howard and Vala), the standard
non-Clifford resource for fault tolerance with qudits (Campbell, Anwar and Browne).  The Wigner function is
    W(q, s) = p^-2 sum_y w^(f(q + y/2) - f(q - y/2) - s y),
and the measure is the sum of sizes S = sum |W| (round 8 on; the mana is ln S, and the ceiling is sqrt p).

  E1  f = c x^3 + ...:  W(q, s) = S_t(f'(q) - s) / p^2, t = c/4, S_t(a) = sum_x w^(t x^3 + a x)  (round 13, one wheel).
  E2  f = c x^4:  W(0, s) = [s = 0] / p and W(q, s) = S_(cq)(4 c q^3 - s) / p^2 for q != 0.
  E3  the ladder's constants kappa_m = E|tr U|, U Haar in USp(2m) (Weyl integral; Monte Carlo), and the exact mean of
      S for a Haar-random state, p E|2X - 1| with X ~ Beta((p+1)/2, (p-1)/2).
  E4  the moments: the class average of sum_a S_t(a)^n is p^2 t_n (Livne's cubics, edge_rule.t_values); for p = 2 mod 3
      every class; and the seventh moment carries a_p of 35.3.c.b.
  E5  p = 1 mod 3: sum_a S_t(a)^3 = 2p^2 + 2p Re(chi(3t) G(chi)^2), G the cubic Gauss sum; the fourth moment is
      2p^3 - p^2 for every class.

  python one_wheel.py calibrate   # E1-E5 at the primes up to 29, before the registration  -> one_wheel_calibrate.log
  python one_wheel.py test        # E4, E5 over the full ranges, and Q1-Q5 (round 29)     -> one_wheel_test.log

numpy + sympy (mpmath) + edge_rule.py.  Four worker processes at below-normal priority for the ladder.  ASCII output.
"""
import itertools
import math
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import mpmath
import numpy as np
import sympy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edge_rule as er  # noqa: E402  (sets below-normal priority on import, through coin_at_five)

SEED = 20261117
KAPPA = {1: 8 / (3 * math.pi), 2: 0.790497, 3: 0.798491}     # E|tr U| on USp(2m); E3 recomputes them
GAUSS = math.sqrt(2 / math.pi)
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


# ------------------------------------------------------------------ states and Wigner functions
def wigner_state(psi, p):
    """W(q, s) = (1/p) sum_y w^(-s y) psi(q + y/2) conj psi(q - y/2), for a normalized state psi on p levels"""
    h = pow(2, -1, p)
    q, y = np.arange(p)[:, None], np.arange(p)[None, :]
    G = psi[(q + y * h) % p] * np.conj(psi[(q - y * h) % p])
    return (np.fft.fft(G, axis=1) / p).real


def wigner_phase(f, p):
    """the Wigner function of psi_f = sum_x w^f(x) |x> / sqrt p, from the integer values f(x) mod p"""
    h = pow(2, -1, p)
    q, y = np.arange(p)[:, None], np.arange(p)[None, :]
    ph = (f[(q + y * h) % p] - f[(q - y * h) % p]) % p
    return (np.fft.fft(np.exp(2j * np.pi * ph / p), axis=1) / p ** 2).real


def poly_values(coeffs, p):
    """f(x) mod p for x in F_p, coeffs[k] the coefficient of x^k"""
    x = np.arange(p, dtype=np.int64)
    f = np.zeros(p, dtype=np.int64)
    for k, c in enumerate(coeffs):
        if c:
            f = (f + c * np.array([pow(int(v), k, p) for v in x], dtype=np.int64)) % p
    return f


def birch(t, p):
    """S_t(a) = sum_x w^(t x^3 + a x) for a in F_p (real)"""
    x = np.arange(p, dtype=np.int64)
    v = np.exp(2j * np.pi * ((t * (x ** 3 % p)) % p) / p)
    return (p * np.fft.ifft(v)).real


def classes(p):
    """one t in each cubic class of F_p*: just 1 when p = 2 mod 3"""
    if p % 3 == 2:
        return [1]
    g = sympy.primitive_root(p)
    return [1, g, g * g % p]


def T_size(t, p):
    return float(np.abs(birch(t, p)).sum() / p)


def haar_size(p):
    """E[sum |W|] for a Haar-random pure state: p E|2X - 1|, X ~ Beta((p+1)/2, (p-1)/2), since every phase-point
    operator has (p+1)/2 eigenvalues +1 and (p-1)/2 eigenvalues -1"""
    mpmath.mp.dps = 30
    a, b = mpmath.mpf(p + 1) / 2, mpmath.mpf(p - 1) / 2
    half = mpmath.mpf(1) / 2
    P = mpmath.betainc(a, b, 0, half, regularized=True)
    EX = a / (a + b) * mpmath.betainc(a + 1, b, 0, half, regularized=True)
    return float(p * ((a - b) / (a + b) + 2 * (P - 2 * EX)))


def cubic_char(p):
    """chi(v) = exp(2 pi i k/3) for v = g^k, as an array over F_p (chi(0) = 0), and the Gauss sum G(chi)"""
    g = sympy.primitive_root(p)
    chi = np.zeros(p, dtype=complex)
    v = 1
    for k in range(p - 1):
        chi[v] = np.exp(2j * np.pi * (k % 3) / 3)
        v = v * g % p
    G = complex((chi * np.exp(2j * np.pi * np.arange(p) / p)).sum())
    return chi, G


# ------------------------------------------------------------------ E3: the ladder's constants
def kappa_quadrature(m, N):
    """E|tr U| for U Haar in USp(2m): the Weyl density on x_i = cos(theta_i) is prop. to
    prod_(i<j) (x_i - x_j)^2 prod sqrt(1 - x_i^2); Gauss quadrature for the weight sqrt(1 - x^2); tr = 2 sum x_i"""
    k = np.arange(1, N + 1)
    x = np.cos(k * np.pi / (N + 1))
    w = np.pi / (N + 1) * np.sin(k * np.pi / (N + 1)) ** 2
    X = np.meshgrid(*([x] * m), indexing="ij")
    Wt = np.ones_like(X[0])
    for Wi in np.meshgrid(*([w] * m), indexing="ij"):
        Wt = Wt * Wi
    V = np.ones_like(X[0])
    for i, j in itertools.combinations(range(m), 2):
        V = V * (X[i] - X[j]) ** 2
    tr = 2 * sum(X)
    return float((Wt * V * np.abs(tr)).sum() / (Wt * V).sum())


def haar_usp(n, rng):
    """a Haar-random element of USp(2n): Gram-Schmidt on Gaussian vectors, closing each v under v -> J conj(v)"""
    J = np.block([[np.zeros((n, n)), -np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    V, Wc = [], []
    for _ in range(n):
        v = rng.standard_normal(2 * n) + 1j * rng.standard_normal(2 * n)
        for c in V + Wc:
            v = v - c * (c.conj() @ v)
        v = v / np.linalg.norm(v)
        V.append(v)
        Wc.append(J @ v.conj())
    return np.array(V + Wc).T


# ------------------------------------------------------------------ calibrate
def calibrate():
    global LOG
    LOG = open(os.path.join(HERE, "one_wheel_calibrate.log"), "w", encoding="utf-8")
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    say("one_wheel.py calibrate -- the forced identities of round 29, at the primes up to 29, before the registration")
    say()
    small = [int(p) for p in sympy.primerange(5, 30)]

    # E0: the Wigner function's normalization
    ok = True
    for p in small:
        psi = rng.standard_normal(p) + 1j * rng.standard_normal(p)
        psi /= np.linalg.norm(psi)
        W = wigner_state(psi, p)
        ok &= abs(W.sum() - 1) < 1e-12 and abs((W ** 2).sum() - 1 / p) < 1e-12
    check("E0 sum W = 1 and sum W^2 = 1/p for random states, p = 5..29", ok)

    # E1: cubic phase states (round 13, one wheel)
    ok = True
    for p in small:
        for _ in range(3):
            c, b, a1 = int(rng.integers(1, p)), int(rng.integers(0, p)), int(rng.integers(0, p))
            f = poly_values([0, a1, b, c], p)
            W = wigner_state(np.exp(2j * np.pi * f / p) / math.sqrt(p), p)
            t = c * pow(4, -1, p) % p
            S = birch(t, p)
            fp = (3 * c * np.arange(p) ** 2 + 2 * b * np.arange(p) + a1) % p
            pred = np.array([[S[(fp[q] - s) % p] for s in range(p)] for q in range(p)]) / p ** 2
            ok &= np.abs(W - pred).max() < 1e-12
    check("E1 cubic phase states: W(q, s) = S_t(f'(q) - s)/p^2 with t = c/4, against the state's own Wigner function, "
          "p = 5..29", ok)

    # E2: quartic phase states fall to cubic rows
    ok = True
    for p in small:
        c = int(rng.integers(1, p))
        f = poly_values([0, 0, 0, 0, c], p)
        W = wigner_phase(f, p)
        pred = np.zeros((p, p))
        pred[0, 0] = 1 / p
        for q in range(1, p):
            S = birch(c * q % p, p)
            pred[q] = [S[(4 * c * q ** 3 - s) % p] / p ** 2 for s in range(p)]
        Sform = 1 / p + sum(np.abs(birch(c * q % p, p)).sum() for q in range(1, p)) / p ** 2
        ok &= np.abs(W - pred).max() < 1e-12 and abs(np.abs(W).sum() - Sform) < 1e-10
    check("E2 quartic phase states: W(0, s) = [s = 0]/p and W(q, s) = S_cq(4cq^3 - s)/p^2, so "
          "S = 1/p + p^-2 sum_(q != 0) sum_a |S_cq(a)|, p = 5..29", ok)
    ok = all(np.abs(wigner_phase(poly_values([0, 0, 0, 0, 1], p), p)).sum() < T_size(1, p) for p in small if p % 3 == 2)
    check("    and the quartic state is below the T state at every p = 2 mod 3 up to 29 (forced: S_T > 1)", ok)

    # E3: the ladder's constants and the Haar mean
    say("E3 the ladder's constants, E|tr U| for U Haar in USp(2m), by the Weyl integral:")
    kq = {1: kappa_quadrature(1, 6400), 2: kappa_quadrature(2, 1200), 3: kappa_quadrature(3, 160)}
    for m in (1, 2, 3):
        say(f"     USp({2 * m}): {kq[m]:.6f}")
    say(f"     Gaussian limit sqrt(2/pi) = {GAUSS:.6f}")
    check("E3 the quadrature gives 8/(3 pi) for USp(2), and the constants used in the registration",
          abs(kq[1] - KAPPA[1]) < 1e-6 and abs(kq[2] - KAPPA[2]) < 5e-6 and abs(kq[3] - KAPPA[3]) < 5e-6)
    mc = {}
    for n, k in ((2, 100000), (3, 50000)):
        tr = np.array([np.trace(haar_usp(n, rng)).real for _ in range(k)])
        mc[n] = (np.abs(tr).mean(), np.abs(tr).std() / math.sqrt(k))
        say(f"     Monte Carlo, {k} Haar matrices in USp({2 * n}): {mc[n][0]:.4f} +- {mc[n][1]:.4f}")
    check("    the Monte Carlo agrees within 3 standard errors, and USp(4) lies below the Gaussian value",
          all(abs(mc[n][0] - KAPPA[n]) < 3 * mc[n][1] for n in (2, 3)) and KAPPA[2] < GAUSS)
    ok = True
    for p, k in ((7, 20000), (11, 20000)):
        vals = []
        for _ in range(k):
            psi = rng.standard_normal(p) + 1j * rng.standard_normal(p)
            psi /= np.linalg.norm(psi)
            vals.append(np.abs(wigner_state(psi, p)).sum())
        m, se = float(np.mean(vals)), float(np.std(vals) / math.sqrt(k))
        say(f"     p = {p}: {k} Haar-random states, mean S = {m:.5f} +- {se:.5f}; the formula gives {haar_size(p):.5f}")
        ok &= abs(m - haar_size(p)) < 4 * se
    check("    the exact Haar mean p E|2X - 1| agrees with random states at 7 and 11", ok)

    # E4: the moments are the counts
    ok = ok7 = True
    for p in small:
        tv = er.t_values(p, (3, 5, 7, 9))
        for n in (3, 5, 7, 9):
            mom = [float((birch(t, p) ** n).sum()) for t in classes(p)]
            target = float(p * p * tv[n])
            ok &= abs(np.mean(mom) - target) < 1e-6 * max(1.0, abs(target))
            if p % 3 == 2:
                ok &= all(abs(m - target) < 1e-6 * max(1.0, abs(target)) for m in mom)
        if p in er.LMFDB_35_3_c_b and p >= 11:
            target7 = p ** 4 * (14 + 6 * er.leg(5, p)) + p ** 3 * er.LMFDB_35_3_c_b[p]
            ok7 &= abs(np.mean([float((birch(t, p) ** 7).sum()) for t in classes(p)]) - target7) < 1e-6 * target7
    check("E4 the class average of sum_a S_t(a)^n is p^2 t_n (Livne's cubics) for n = 3, 5, 7, 9, and every class "
          "equals it when p = 2 mod 3, p = 5..29", ok)
    check("    the seventh moment is p^4 (14 + 6(5|p)) + p^3 a_p(35.3.c.b) on average over the classes, p = 11..29", ok7)

    # E5: the cubic Gauss sum decides the third moment
    ok3 = ok4 = True
    for p in small:
        if p % 3 != 1:
            continue
        chi, G = cubic_char(p)
        for t in range(1, p):
            S = birch(t, p)
            pred3 = 2 * p * p + 2 * p * (chi[3 * t % p] * G * G).real
            ok3 &= abs((S ** 3).sum() - pred3) < 1e-8 * p ** 3
            ok4 &= abs((S ** 4).sum() - (2 * p ** 3 - p * p)) < 1e-8 * p ** 4
    check("E5 p = 1 mod 3: sum_a S_t(a)^3 = 2p^2 + 2p Re(chi(3t) G(chi)^2) for every t, p = 7, 13, 19", ok3)
    check("    and sum_a S_t(a)^4 = 2p^3 - p^2 for every t", ok4)
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


# ------------------------------------------------------------------ test (round 29)
def _ladder(p):
    """S/sqrt p for x^5, x^6, x^7, x^8 and a seeded random polynomial of each degree"""
    er.low_priority()
    out = {}
    for d in (5, 6, 7, 8):
        mono = np.zeros(d + 1, dtype=np.int64)
        mono[d] = 1
        rng = np.random.default_rng([SEED, p, d])
        rand = rng.integers(0, p, size=d + 1)
        rand[:3] = 0                                   # degree <= 2 is Clifford
        rand[d] = int(rng.integers(1, p))
        for name, c in (("x^%d" % d, mono), ("random %d" % d, rand)):
            f = poly_values([int(v) for v in c], p)
            out[name] = float(np.abs(wigner_phase(f, p)).sum() / math.sqrt(p))
    return p, out


def phase_batch(F, p):
    """sum |W| for a batch of phase functions F (rows of values mod p)"""
    h = pow(2, -1, p)
    q, y = np.arange(p)[:, None], np.arange(p)[None, :]
    A, B = (q + y * h) % p, (q - y * h) % p
    ph = (F[:, A] - F[:, B]) % p
    W = np.fft.fft(np.exp(2j * np.pi * ph / p), axis=2) / p ** 2
    return np.abs(W.real).sum(axis=(1, 2))


def small_phases(p, sample=None, rng=None, batch=20000):
    """the best phase state at p: f = sum_(k=3)^(p-1) c_k x^k, all of them or a sample; also the best T class"""
    V = np.array([[pow(x, k, p) for x in range(p)] for k in range(3, p)], dtype=np.int64)
    best, arg = -1.0, None

    def every():
        it = itertools.product(range(p), repeat=p - 3)
        while True:
            C = np.array(list(itertools.islice(it, batch)), dtype=np.int64)
            if len(C) == 0:
                return
            yield C

    def drawn():
        for i in range(0, sample, batch):
            yield rng.integers(0, p, size=(min(batch, sample - i), p - 3))

    coeff_iter = every() if sample is None else drawn()
    count = 0
    for C in coeff_iter:
        if len(C) == 0:
            continue
        F = (C @ V) % p
        S = phase_batch(F, p)
        count += len(C)
        i = int(np.argmax(S))
        if S[i] > best:
            best, arg = float(S[i]), C[i].copy()
    deg = max((k + 3 for k in range(p - 3) if arg[k]), default=0)
    bestT = max(T_size(t, p) for t in classes(p))
    return best, arg, deg, bestT, count


def test():
    global LOG
    LOG = open(os.path.join(HERE, "one_wheel_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("Round 29: one wheel -- the qudit T state and the ladder of diagonal magic states (PREREG.md)")
    say()

    # F1: E4 and E5 over the full ranges (forced)
    ok = True
    for p in [int(p) for p in sympy.primerange(5, 102)]:
        tv = er.t_values(p, (3, 5, 7, 9))
        for n in (3, 5, 7, 9):
            mom = [float((birch(t, p) ** n).sum()) for t in classes(p)]
            target = float(p * p * tv[n])
            ok &= abs(np.mean(mom) - target) < 1e-6 * max(1.0, abs(target))
            if p % 3 == 2:
                ok &= all(abs(m - target) < 1e-6 * max(1.0, abs(target)) for m in mom)
    check("F1 E4 at every prime to 101: the moments are p^2 t_n (n = 3, 5, 7, 9), every class when p = 2 mod 3", ok)
    ok3 = ok4 = True
    kummer = {}
    for p in [int(p) for p in sympy.primerange(7, 1001) if p % 3 == 1]:
        chi, G = cubic_char(p)
        for t in classes(p):
            S = birch(t, p)
            ok3 &= abs((S ** 3).sum() - (2 * p * p + 2 * p * (chi[3 * t % p] * G * G).real)) < 1e-7 * p ** 3
            ok4 &= abs((S ** 4).sum() - (2 * p ** 3 - p * p)) < 1e-7 * p ** 4
        kummer[p] = (chi, G)
    check("F2 E5 at every prime = 1 mod 3 to 1000: the third moment is 2p^2 + 2p Re(chi(3t) G(chi)^2), the fourth "
          "2p^3 - p^2, in every class", ok3 and ok4)
    say()

    # the T state at every prime 31..5000
    P = [int(p) for p in sympy.primerange(31, 5001)]
    rows = {}
    for p in P:
        rows[p] = ([T_size(t, p) for t in classes(p)], haar_size(p))
    say(f"the T state at the {len(P)} primes 31..5000 ({(time.time() - t0) / 60:.1f} minutes so far)")
    say("  p  S/sqrt(p) for each class  |  Haar mean S/sqrt(p)    (every 20th prime shown)")
    for i, p in enumerate(P):
        if i % 20 == 0 or p in (31, 997, 4999):
            Ts, H = rows[p]
            say(f"  {p:5d}  " + " ".join(f"{s / math.sqrt(p):.5f}" for s in Ts) + f"  |  {H / math.sqrt(p):.5f}")
    win = [s / math.sqrt(p) for p in P if 1000 <= p <= 3000 for s in rows[p][0]]
    m1 = float(np.mean(win))
    check(f"Q1 over every class at every prime 1000..3000, the mean S/sqrt(p) is within 0.003 of 8/(3 pi) = "
          f"{KAPPA[1]:.5f}", abs(m1 - KAPPA[1]) < 0.003, f"mean {m1:.5f} over {len(win)} states")
    bad_a = [p for p in P if 500 <= p <= 5000 and min(rows[p][0]) <= rows[p][1]]
    bad_b = [p for p in P if 31 <= p < 500 and min(rows[p][0]) <= rows[p][1]]
    check("Q2a every class beats the exact Haar mean at every prime 500..5000", not bad_a,
          f"falls short at {bad_a[:10]}" if bad_a else "")
    check("Q2b (Claude's reading) the same at every prime 31..500", not bad_b,
          f"falls short at {bad_b[:10]}" if bad_b else "")
    dev = {p: max(abs(s / math.sqrt(p) - KAPPA[1]) for s in rows[p][0]) for p in P}
    hi = [p for p in P if p >= 1000]
    slope = np.polyfit(np.log(hi), np.log([max(dev[p], 1e-12) for p in hi]), 1)[0]
    say(f"  read: the largest deviation |S/sqrt(p) - 8/(3 pi)| by range: "
        + ", ".join(f"{lo}-{hi_}: {max(dev[p] for p in P if lo <= p < hi_):.4f}"
                    for lo, hi_ in ((31, 100), (100, 500), (500, 1000), (1000, 2000), (2000, 5001)))
        + f"; log-log slope over 1000..5000: {slope:.2f}")
    spread = [max(rows[p][0]) - min(rows[p][0]) for p in P if p % 3 == 1]
    say(f"  read: p = 1 mod 3, the spread of S between the three classes, relative to sqrt p: largest "
        f"{max(s / math.sqrt(p) for s, p in zip(spread, [p for p in P if p % 3 == 1])):.4f}")
    agree = tot = 0
    for p in [p for p in P if p % 3 == 1 and p <= 1000]:
        chi, G = kummer[p]
        third = [2 * p * p + 2 * p * (chi[3 * t % p] * G * G).real for t in classes(p)]
        agree += int(np.argmax(third) == int(np.argmax(rows[p][0])))
        tot += 1
    say(f"  read: the class with the largest third moment (the Gauss sum's choice) is the most negative class at "
        f"{agree} of {tot} primes = 1 mod 3 up to 1000")
    say()

    # the ladder (Q3, Q4)
    from multiprocessing import Pool
    PL = [int(p) for p in sympy.primerange(700, 1501)]
    with Pool(4) as pool:
        lad = dict(pool.map(_ladder, PL))
    Hm = float(np.mean([haar_size(p) / math.sqrt(p) for p in PL]))
    say(f"the ladder at the {len(PL)} primes 700..1500 ({(time.time() - t0) / 60:.1f} minutes so far); "
        f"mean Haar S/sqrt(p) = {Hm:.5f}")
    means = {name: float(np.mean([lad[p][name] for p in PL])) for name in lad[PL[0]]}
    for name, m in means.items():
        say(f"     {name:9s} mean S/sqrt(p) = {m:.5f}   (spread over the primes: "
            f"{min(lad[p][name] for p in PL):.5f} .. {max(lad[p][name] for p in PL):.5f})")
    five = ["x^5", "x^6", "random 5", "random 6"]
    seven = ["x^7", "x^8", "random 7", "random 8"]
    check(f"Q3 degrees 5 and 6: every family's mean is within 0.004 of kappa_2 = {KAPPA[2]:.5f} and below the "
          f"Haar mean", all(abs(means[n] - KAPPA[2]) < 0.004 and means[n] < Hm for n in five),
          ", ".join(f"{n} {means[n]:.5f}" for n in five))
    check(f"Q4 degrees 7 and 8: every family's mean is within 0.004 of kappa_3 = {KAPPA[3]:.5f}",
          all(abs(means[n] - KAPPA[3]) < 0.004 for n in seven), ", ".join(f"{n} {means[n]:.5f}" for n in seven))
    say()

    # Q5 and the small primes
    rng = np.random.default_rng([SEED, 5])
    for p, sample in ((5, None), (7, None), (11, 1_000_000), (13, 1_000_000)):
        best, arg, deg, bestT, count = small_phases(p, sample, rng)
        say(f"  p = {p}: {'all' if sample is None else 'a sample of'} {count} phase classes: best S = {best:.6f} "
            f"({best / math.sqrt(p):.4f} of the ceiling), degree {deg}, coefficients x^3..x^{p - 1} = "
            f"{[int(v) for v in arg]}; best T class S = {bestT:.6f} ({bestT / math.sqrt(p):.4f}); "
            f"Haar mean {haar_size(p):.6f}")
        if p == 7:
            check("Q5 at 7, over all 2401 phase classes, the most negative phase state is not a T state",
                  best > bestT + 1e-9 and deg > 3, f"best {best:.6f} at degree {deg} against T {bestT:.6f}")
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


if __name__ == "__main__":
    {"calibrate": calibrate, "test": test}[sys.argv[1] if len(sys.argv) > 1 else "calibrate"]()
