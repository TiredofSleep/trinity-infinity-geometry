"""exact_moments.py -- the exact sixth moment and the fourth free cumulant (TORUS_MOMENTS.md section 9): the exact integer
counts behind the moments, collected from the states, fitted on the primes up to 199, and tested on 211 to 401.

    "go after an exact formula for the 6th moment first.. The free fourth cumulant equals 3/p^2 to every digit the log
     keeps. Worth a short exact proof as a small theorem"  -- the author, 14 November 2026

For the non-split torus's eigenbasis psi_j (parity eps_j = p W_j(0)), the circle operators S_C = sum of A_v over a
circle C, and m = p + 1, the moments are integers in disguise (TORUS_MOMENTS.md section 7):
    I_n = sum over circles of Tr S_C^n        = p^n m^(n - 1) sum_j sum_(u != 0) W_j(u)^n
    J_n = sum over circles of Tr (P S_C^n)    = p^n m^(n - 1) sum_j eps_j sum_(u != 0) W_j(u)^n
This script computes them from the states (as floats, then rounded, reporting the distance to the nearest integer).

  python exact_moments.py collect   # p = 5 .. 199: writes exact_moments_collect.log (used to find the formulas)
  python exact_moments.py test      # p = 211 .. 401: writes exact_moments_test.log (registered in PREREG.md first)

numpy + oscillator_states.py.  One process, one thread, below-normal priority.  ASCII output.
"""
import ctypes
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

import oscillator_states as osc

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
NMAX = 6
LOG = None


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def primes(lo, hi):
    return [q for q in range(max(lo, 5), hi + 1) if all(q % d for d in range(2, int(q ** 0.5) + 1))]


def counts(p):
    """the integers I_n and J_n (n = 2..NMAX) and the worst distance of a raw value to its integer"""
    V = osc.nonsplit_states(p)[0]
    x = np.arange(p)
    eps = np.rint(np.real(np.sum(V.conj() * V[:, (-x) % p], axis=1)))   # p W_j(0) = +-1
    acc = np.zeros((len(V), NMAX + 1))
    two_k = (2 * x) % p
    for q in range(p):
        F = V.conj()[:, (q + x) % p] * V[:, (q - x) % p]
        Wq = np.real(np.fft.ifft(F, axis=1)[:, two_k])
        if q == 0:
            Wq = Wq[:, 1:]
        Wq = Wq * p ** 1.5                                               # values of size about 1
        Wn = np.ones_like(Wq)
        for n in range(1, NMAX + 1):
            Wn = Wn * Wq
            acc[:, n] += Wn.sum(axis=1)
    m = p + 1
    out, worst = {}, 0.0
    for n in range(2, NMAX + 1):
        scale = p ** n * m ** (n - 1) / p ** (1.5 * n)
        for name, w in (("I", np.ones(len(V))), ("J", eps)):
            raw = float((w * acc[:, n]).sum()) * scale
            val = int(round(raw))
            worst = max(worst, abs(raw - val))
            out[f"{name}{n}"] = val
    out["even"] = int((eps == 1).sum())
    return out, worst


def collect(ps, logname):
    global LOG
    LOG = open(os.path.join(HERE, logname), "w", encoding="utf-8")
    t0 = time.time()
    keys = [f"{a}{n}" for n in range(2, NMAX + 1) for a in "IJ"]
    say("EXACT p " + " ".join(keys) + " even worst")
    for p in ps:
        c, worst = counts(p)
        say(f"EXACT {p} " + " ".join(str(c[k]) for k in keys) + f" {c['even']} {worst:.2e}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


def eta_coeffs(spec, N):
    """q-expansion coefficients 0..N of the product of eta(d tau)^r (integer q-shift)"""
    shift = sum(d * r for d, r in spec)
    assert shift % 24 == 0
    poly = [0] * (N + 1)
    poly[0] = 1
    for d, r in spec:
        for n in range(1, N // d + 1):
            step = d * n
            for _ in range(r):
                for k in range(N, step - 1, -1):
                    poly[k] -= poly[k - step]
    s = shift // 24
    return [0] * s + poly[:N + 1 - s]


def b_even(p):
    """b with p = a^2 + b^2, b even, when p = 1 mod 4; 0 when p = 3 mod 4"""
    if p % 4 == 3:
        return 0
    for a in range(1, int(p ** 0.5) + 1, 2):
        b = int(round((p - a * a) ** 0.5))
        if b * b == p - a * a:
            return b


def legendre(a, p):
    return 0 if a % p == 0 else (1 if pow(a % p, (p - 1) // 2, p) == 1 else -1)


def I6_formula(p, b6):
    return p * (5 * p ** 4 - p ** 3 - 5 * p ** 2 - 1 + (p + 1) * (b6[p] - legendre(-3, p) * p * p))


def J4_formula(p):
    return (3 * p + 1) * (p * p - 1) - 4 * p * (p + 1) * b_even(p) ** 2


def kappa4_exact(p):
    """the basis average of the standardized fourth moment off the origin, minus 2, from J4 (exact rational)"""
    from fractions import Fraction as Fr
    P = Fr(p)
    m, N = P + 1, P * P - 1
    I3, I4 = (P + 1) * (P - 1) * (2 * P + 1), 2 * P * P * (P - 1) * (P + 1)
    J3 = -2 * P * m if p % 3 == 2 else Fr(0)
    A3, B3 = (1 + I3 / m ** 2) / P ** 3, (P + J3 / m ** 2) / P ** 3
    A4, B4 = (P + I4 / m ** 3) / P ** 4, (1 + Fr(J4_formula(p)) / m ** 3) / P ** 4
    tot = Fr(0)
    for e in (1, -1):
        n = (P + e) / 2
        S1, S2 = 1 - Fr(e) / P, 1 / P - 1 / P ** 2
        S3 = (A3 + e * B3) / (P + e) - Fr(e) / P ** 3
        S4 = (A4 + e * B4) / (P + e) - 1 / P ** 4
        mu, m2, m3, m4 = S1 / N, S2 / N, S3 / N, S4 / N
        c2 = m2 - mu ** 2
        c4 = m4 - 4 * mu * m3 + 6 * mu ** 2 * m2 - 3 * mu ** 4
        tot += (n / P) * c4 / c2 ** 2
    return tot - 2


def states_k4_m6(p):
    """from the states: the basis average of the standardized fourth moment off the origin minus 2, and
    (1/p) sum_j sum_u W_j(u)^6 over all points"""
    V = osc.nonsplit_states(p)[0]
    x = np.arange(p)
    W0 = np.real(np.sum(V.conj() * V[:, (-x) % p], axis=1)) / p
    N = p * p - 1
    mu = (1 - W0) / N
    sd = np.sqrt((1 / p - W0 ** 2) / N - mu ** 2)
    z4 = np.zeros(len(V))
    s6 = float((W0 ** 6).sum())
    two_k = (2 * x) % p
    for q in range(p):
        F = V.conj()[:, (q + x) % p] * V[:, (q - x) % p]
        Wq = np.real(np.fft.ifft(F, axis=1)[:, two_k])
        if q == 0:
            Wq = Wq[:, 1:]
        z4 += (((Wq - mu[:, None]) / sd[:, None]) ** 4).sum(axis=1)
        s6 += float((Wq ** 6).sum())
    return float((z4 / N).mean() - 2), s6 / p


def test():
    global LOG
    LOG = open(os.path.join(HERE, "exact_moments_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("exact_moments.py test: round 16 of PREREG.md, the formulas fitted on 7..199, tested on 211..401 and against")
    say("the states at 503, 701, 907 and 1009")
    b6 = eta_coeffs([(1, 2), (2, 2), (3, 2), (6, 2)], 1009)
    c16 = eta_coeffs([(4, 6)], 1009)
    ps = primes(211, 401)
    ok0 = all(c16[p] == (2 * ((p - b_even(p) ** 2) - b_even(p) ** 2) if p % 4 == 1 else 0) for p in primes(5, 1009))
    say(f"E0 {'HELD' if ok0 else 'DIED'}: the coefficients of eta(4 tau)^6 are 2(a^2 - b^2) for p = a^2 + b^2 = 1 mod 4 "
        f"and 0 for p = 3 mod 4, at every prime to 1009 (so the two forms of E2 agree)")
    keys = [f"{a}{n}" for n in range(2, NMAX + 1) for a in "IJ"]
    e1 = e2 = e3 = True
    worst = 0.0
    for p in ps:
        c, w = counts(p)
        worst = max(worst, w)
        say(f"EXACT {p} " + " ".join(str(c[k]) for k in keys) + f" {c['even']} {w:.2e}")
        e1 &= c["I6"] == I6_formula(p, b6)
        e2 &= c["J4"] == J4_formula(p)
        e3 &= (c["I2"] == p * (p - 1) * (p + 1) and c["I3"] == (p + 1) * (p - 1) * (2 * p + 1)
               and c["I4"] == 2 * p * p * (p - 1) * (p + 1) and c["J2"] == p * p - 1
               and c["J3"] == (-2 * p * (p + 1) if p % 3 == 2 else 0))
    say(f"(largest distance of a raw value to its integer: {worst:.2e})")
    say(f"E1 {'HELD' if e1 else 'DIED'}: I6 = p[5p^4 - p^3 - 5p^2 - 1 + (p + 1)(b(p) - (-3|p) p^2)] at every prime "
        f"from 211 to 401 ({len(ps)} primes)")
    say(f"E2 {'HELD' if e2 else 'DIED'}: J4 = (3p + 1)(p^2 - 1) - 4p(p + 1) b^2 at every prime from 211 to 401")
    say(f"E3 {'HELD' if e3 else 'DIED'}: the proved counts I2, I3, I4, J2, J3 at every prime from 211 to 401")
    e4 = e5 = True
    for p in (211, 503, 701, 907, 1009):
        k4s, m6s = states_k4_m6(p)
        k4f = float(kappa4_exact(p))
        m6f = (p + I6_formula(p, b6) / (p + 1) ** 5) / p ** 7
        e4 &= abs(k4s - k4f) < 1e-11
        if p >= 503:
            e5 &= abs(m6s / m6f - 1) < 1e-10
        say(f"STATES {p}: kappa4 from the states {k4s:.12e}, exact {k4f:.12e}; sixth moment {m6s:.12e}, "
            f"exact {m6f:.12e}")
    say(f"E4 {'HELD' if e4 else 'DIED'}: the exact kappa4 is the states' value within 1e-11 at 211, 503, 701, 907, 1009")
    say(f"E5 {'HELD' if e5 else 'DIED'}: the exact sixth moment is the states' within 1e-10 (relative) at 503 to 1009")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"
    if mode == "collect":
        collect(primes(5, 199), "exact_moments_collect.log")
    elif mode == "test":
        test()
