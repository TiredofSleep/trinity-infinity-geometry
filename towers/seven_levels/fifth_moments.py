"""fifth_moments.py -- the exact fifth moments (TORUS_MOMENTS.md section 8, Theorems 6 and 7) and round 17's test.

    "1, apply the hexagon method to the fifth moments"  -- the author, 14 November 2026

With I_n = sum over circles of Tr S_C^n and J_n = sum over circles of Tr(P S_C^n) (round 16):

  J5 = p (p + 1) [f15(p) - p a_E(p) + (4(-3|p) - 3) p - 1],     E: y^2 = x(x - 4)(4x^2 - 52x + 9)
  I5 = p (p + 1) [p^3 + 4p^2 - (1 + (5|p)) p - 4 + a10(p)] - p^5 - 1

f15 is the weight-3 newform of level 15 (Kloosterman's fifth moment), a10 the weight-4 newform of level 10, and E's
traces are those of the weight-2 newform of level 150 with a(7), a(11), a(13) = -2, 2, -6.  Behind I5:

  I5 = (p + 1)(p N_V - N_W),  N_W = (p^5 + 1)/(p + 1),  N_V = p^3 + 10p^2 - (20 + (5|p)) p - 4 - (-1|p) S_oct,
  S_oct = sum over the points [d] of P^3 = {d1 + ... + d5 = 0} of eta(e3(d) e5(d)),

a character sum on the double octic w^2 = e3 e5: the double cover of 3-space branched along Clebsch's diagonal cubic
surface (e1 = e3 = 0) and its five Sylvester planes (d_i = 0).  Measured: (-1|p) S_oct = 6p^2 - 19p - a10(p).

  python fifth_moments.py collect   # S_oct at every prime 7..401 -> fifth_moments_collect.log (seconds to a minute)
  python fifth_moments.py test      # round 17, registered in PREREG.md first -> fifth_moments_test.log
                                    #   (four worker processes at below-normal priority; about ten minutes)

numpy + sympy + modular_symbols.py + exact_moments.py (+ oscillator_states.py for the test).  ASCII output.
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


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def eta(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def primes(lo, hi):
    return [q for q in range(lo, hi + 1) if sympy.isprime(q)]


def S_oct(p):
    """sum over [d] in P^3 = {e1 = 0} of eta(e3 e5); points with a zero coordinate have e5 = 0, so only the chart
    [1 : a : b : c] (d5 = -(1 + a + b + c)) contributes.  On e1 = 0, e3 = (d1^3 + ... + d5^3)/3."""
    L = np.array([eta(v, p) for v in range(p)], dtype=np.int64)
    b, c = np.meshgrid(np.arange(p, dtype=np.int64), np.arange(p, dtype=np.int64), indexing="ij")
    b3, c3 = b * b % p * b % p, c * c % p * c % p
    tot = 0
    for a in range(p):
        d5 = (-(1 + a + b + c)) % p
        p3 = (1 + a ** 3 + b3 + c3 + d5 * d5 % p * d5) % p
        e5 = a * b % p * c % p * d5 % p
        tot += int(L[p3 * e5 % p].sum())
    return eta(3, p) * tot


def E_count(p):
    """points of E: y^2 = x(x - 4)(4x^2 - 52x + 9), with its two points at infinity (leading coefficient 4)"""
    x = np.arange(p, dtype=np.int64)
    sq = np.zeros(p, bool)
    sq[(x * x) % p] = True
    v = (x * (x - 4) % p * ((4 * x * x - 52 * x + 9) % p)) % p
    return p + 2 + int(np.where(v == 0, 0, np.where(sq[v], 1, -1)).sum())


def f15_coeffs(N):
    import exact_moments as emo
    A, B = emo.eta_coeffs([(3, 3), (5, 3)], N), emo.eta_coeffs([(1, 3), (15, 3)], N)
    return [a + b for a, b in zip(A, B)]


def named_forms(ps):
    """a10: the weight-4 rational eigensystem of level 10 that is not the level-5 oldform (a(7) = -4);
    e150: the weight-2 rational eigensystem of level 150 with a(7), a(11), a(13) = -2, 2, -6"""
    import modular_symbols as ms
    s10 = [s for s in ms.rational_eigensystems(10, ps, k=4) if s["ap"][7] == -4]
    s150 = [s for s in ms.rational_eigensystems(150, ps, k=2)
            if (s["ap"][7], s["ap"][11], s["ap"][13]) == (-2, 2, -6)]
    assert len(s10) == 1 and len(s150) == 1, (len(s10), len(s150))
    return s10[0]["ap"], s150[0]["ap"]


def I5_formula(p, a10):
    return p * (p + 1) * (p ** 3 + 4 * p * p - (1 + eta(5, p)) * p - 4 + a10) - p ** 5 - 1


def J5_formula(p, aE, f15):
    return p * (p + 1) * (f15 - p * aE + (4 * eta(-3, p) - 3) * p - 1)


def NV_from_octic(p, s):
    return p ** 3 + 10 * p * p - (20 + eta(5, p)) * p - 4 - eta(-1, p) * s


def collect():
    global LOG
    LOG = open(os.path.join(HERE, "fifth_moments_collect.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("the double octic's character sum S_oct = sum over [d] in P^3 (e1 = 0) of eta(e3 e5), at every prime 7..401")
    say("OCTIC p S_oct")
    for p in primes(7, 401):
        say(f"OCTIC {p} {S_oct(p)}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


def _counts(p):
    low_priority()
    import exact_moments as emo
    c, worst = emo.counts(p)
    return p, c, worst


def test():
    """round 17 (PREREG.md): F0..F6"""
    global LOG
    LOG = open(os.path.join(HERE, "fifth_moments_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    import exact_moments as emo
    import modular_symbols as ms
    from multiprocessing import Pool
    P_op = primes(409, 509)
    P_all = primes(409, 601)
    say("Round 17: the fifth moments, tested where they were not found (PREREG.md)")
    say(f"operator primes {P_op[0]}..{P_op[-1]} ({len(P_op)}), octic and curve primes {P_all[0]}..{P_all[-1]} ({len(P_all)})")
    # F0: the instrument
    known = {5: [(1, 4), (5, 4)], 6: [(1, 2), (2, 2), (3, 2), (6, 2)], 8: [(2, 4), (4, 4)], 9: [(3, 8)]}
    f0 = True
    for N, spec in known.items():
        cf = emo.eta_coeffs(spec, 601)
        sy = ms.rational_eigensystems(N, primes(7, 601))
        ok = len(sy) == 1 and all(sy[0]["ap"][p] == cf[p] for p in sy[0]["ap"])
        f0 &= ok
        say(f"F0 level {N}: the engine's one rational weight-4 system equals the eta product at every prime 7..601: {ok}")
    say(f"F0 {'HELD' if f0 else 'FAILED'}")
    a10, e150 = named_forms(primes(7, 601))
    f15 = f15_coeffs(601)
    # F3: the double octic
    bad3 = []
    for p in P_all:
        s = S_oct(p)
        ok = eta(-1, p) * s == 6 * p * p - 19 * p - a10[p]
        if not ok:
            bad3.append(p)
        say(f"F3 p={p}: S_oct = {s}, a10 = {a10[p]}, (-1|p) S_oct = 6p^2 - 19p - a10(p): {ok}")
    say(f"F3 {'HELD' if not bad3 else 'FAILED at ' + str(bad3)}")
    # F4: the curve
    bad4 = [p for p in P_all if p + 1 - E_count(p) != e150[p]]
    say(f"F4 E's traces equal the level-150 newform's at every prime {P_all[0]}..{P_all[-1]}: {not bad4} {bad4 if bad4 else ''}")
    say(f"F4 {'HELD' if not bad4 else 'FAILED'}")
    # F1, F2, F5, F6: the operators
    with Pool(4) as pool:
        res = pool.map(_counts, P_op)
    bad1, bad2, bad5, worst_all = [], [], [], 0.0
    keys = [f"{a}{n}" for n in range(2, 7) for a in "IJ"]
    say("EXACT p " + " ".join(keys) + " worst")
    for p, c, worst in sorted(res):
        say(f"EXACT {p} " + " ".join(str(c[k]) for k in keys) + f" {worst:.2e}")
    b6all = emo.eta_coeffs([(1, 2), (2, 2), (3, 2), (6, 2)], P_op[-1])
    for p, c, worst in sorted(res):
        worst_all = max(worst_all, worst)
        m = p + 1
        chi = eta(-3, p)
        ok1 = c["I5"] == I5_formula(p, a10[p])
        ok2 = c["J5"] == J5_formula(p, p + 1 - E_count(p), f15[p])
        proved = (c["I2"] == p * (p * p - 1) and c["J2"] == p * p - 1 and c["I3"] == (p + 1) * (p - 1) * (2 * p + 1)
                  and c["I4"] == 2 * p * p * (p - 1) * (p + 1) and c["J3"] == (-2 * p * (p + 1) if chi == -1 else 0)
                  and c["I6"] == emo.I6_formula(p, b6all) and c["J4"] == emo.J4_formula(p))
        if not ok1:
            bad1.append(p)
        if not ok2:
            bad2.append(p)
        if not proved:
            bad5.append(p)
        say(f"OPS p={p}: I5 = {c['I5']} formula {ok1};  J5 = {c['J5']} formula {ok2};  I2..I4, J2, J3, I6, J4 {proved};  worst {worst:.2e}")
    say(f"F1 {'HELD' if not bad1 else 'FAILED at ' + str(bad1)}")
    say(f"F2 {'HELD' if not bad2 else 'FAILED at ' + str(bad2)}")
    say(f"F5 {'HELD' if not bad5 else 'FAILED at ' + str(bad5)}")
    say(f"F6 worst distance of a raw operator value to its integer: {worst_all:.2e} -> {'HELD' if worst_all < 0.1 else 'INCONCLUSIVE'}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"
    if mode == "collect":
        collect()
    elif mode == "test":
        test()
