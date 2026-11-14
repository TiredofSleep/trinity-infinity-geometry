"""verify_sixth_moment.py -- checks each step of TORUS_MOMENTS.md section 8's proof of Theorem 4, the exact sixth moment:

    I6 = sum over circles of Tr S_C^6 = p (p Z6 - N6),
    N6 = ((p + 1)^6 + (p + 1) V6) / p^2,  V6 = sum_a K(a)^6 = 5p^4 - 10p^3 - (b(p) + 9) p^2 - 5p - 1,
    Z6 = (p + 1)(6p^2 + (4 - chi) p + 1),  chi = (-3|p).

  1. the trace phase of six phase-point operators on a closed hexagon is 2A(v1, v2, v3) + 2A(v4, v5, v6), with
     A(x, y, z) = <y - x, z - x>, and it agrees with the fan of free_moments.py                          (operators, p <= 13)
  2. in the field model (circle N(v) = r, <a, b> = Im(conj(a) b)): reversing a triangle keeps its alternating sum and
     negates its area; a triangle with x - y + z = w, s = y + w != 0, has area (N(w) - r) Im(x/s), and when s = 0 its
     area is 2<w, x>; the number of triangles over each (w, y) is 1 - eta(1 - 4r/N(s))          (every triangle, p <= 23)
  3. the three parts: w = 0 gives (1 - chi) m^2; w on the circle gives m (4p^2 + 6p - 2 + (-1|p)); every other w gives
     m (2p^2 - 3p + 3 - (-1|p) - (1 - chi)); so Z6 = m (6p^2 + (4 - chi) p + 1)                         (p <= 23, two circles)
  4. the Legendre-symbol lemmas behind part 3, at r = 1: Q = 2m - 3; sum_a B(a)^2 = 2p + 1 + (-1|p); L = 2p - 1;
     H = -(p - 1)/2 + [chi = -1]; K0 = (p - 2 + (-1|p))/2 - [chi = -1]                                 (every prime to 199)
  5. a circle's Fourier transform is a Kloosterman sum: sum over N(v) = r of psi(Tr(alpha v)) = -K(r N(alpha)) for every
     alpha != 0; hence N6 = ((p + 1)^6 + (p + 1) V6)/p^2, also counted directly as sum_w n_w^2        (p <= 23 and p <= 31)
  6. V6 = 5p^4 - 10p^3 - (b(p) + 9) p^2 - 5p - 1 with b(p) from (eta(t) eta(2t) eta(3t) eta(6t))^2 [Hulek, Spandaw, van
     Geemen and van Straten]                                                                              (every prime to 199)
  7. so, with the operators' exact counts of round 16 (exact_moments_collect.log and exact_moments_test.log), the
     phase-0 count read from the states is the proved Z6 at every prime from 7 to 401

numpy + oscillator_states.py + verify_torus_moments.py + exact_moments.py.  One process, below-normal priority.  ASCII output;
writes verify_sixth_moment.log and exits with 1 if a check fails.
Run:  python verify_sixth_moment.py     (about a minute)
"""
import ctypes
import os
import sys
from collections import Counter

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

import exact_moments as emo
import verify_torus_moments as vtm

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = None
OK = True


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def check(label, ok):
    global OK
    OK &= bool(ok)
    say(("PASS  " if ok else "FAIL  ") + label)


def eta(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def primes(lo, hi):
    return [q for q in range(max(lo, 5), hi + 1) if all(q % d for d in range(2, int(q ** 0.5) + 1))]


class Field:
    """F_p(sqrt eps) as pairs (x, y) = x + y sqrt eps"""
    def __init__(self, p):
        self.p = p
        self.eps = next(e for e in range(2, p) if eta(e, p) == -1)

    def add(self, u, v):
        return ((u[0] + v[0]) % self.p, (u[1] + v[1]) % self.p)

    def sub(self, u, v):
        return ((u[0] - v[0]) % self.p, (u[1] - v[1]) % self.p)

    def mul(self, u, v):
        p, e = self.p, self.eps
        return ((u[0] * v[0] + e * u[1] * v[1]) % p, (u[0] * v[1] + u[1] * v[0]) % p)

    def norm(self, u):
        return (u[0] * u[0] - self.eps * u[1] * u[1]) % self.p

    def sym(self, u, v):                                                  # Im(conj(u) v)
        return (u[0] * v[1] - u[1] * v[0]) % self.p

    def tr(self, u):
        return (2 * u[0]) % self.p


def triangles(Fd, C):
    """n_w(a) for every w: the triangles (x, y, z) on C with x - y + z = w and area a"""
    tri = Counter()
    for x in C:
        for y in C:
            for z in C:
                w = Fd.add(Fd.sub(x, y), z)
                tri[(w, Fd.sym(Fd.sub(y, x), Fd.sub(z, x)))] += 1
    nw = {}
    for (w, a), c in tri.items():
        nw.setdefault(w, Counter())[a] = c
    return nw


def main():
    global LOG
    LOG = open(os.path.join(HERE, "verify_sixth_moment.log"), "w", encoding="utf-8")
    say("TORUS_MOMENTS.md section 8, Theorem 4: the sixth moment, step by step")
    rng = np.random.default_rng(20261114)
    # 1. the trace phase of six operators splits into two triangles
    ok1 = True
    import free_moments as fmo
    for p in (5, 7, 11, 13):
        Aall = {(q, k): vtm.A(q, k, p) for q in range(p) for k in range(p)}
        for _ in range(40):
            U = rng.integers(0, p, (6, 2))
            U[5] = (U[0] - U[1] + U[2] - U[3] + U[4]) % p
            M = np.eye(p, dtype=complex)
            for u in U:
                M = M @ Aall[(int(u[0]), int(u[1]))]
            area = lambda a, b, c: (int(b[0] - a[0]) * int(c[1] - a[1]) - int(b[1] - a[1]) * int(c[0] - a[0])) % p
            Phi = (2 * area(U[0], U[1], U[2]) + 2 * area(U[3], U[4], U[5])) % p
            ok1 &= abs(np.trace(M) - p * np.exp(2j * np.pi * Phi / p)) < 1e-8
            ok1 &= int(fmo.phase(U[None], p)[0][0]) == Phi
    check("step 1: on a closed hexagon the six operators' trace phase is 2A(v1, v2, v3) + 2A(v4, v5, v6), the fan's "
          "value, at p = 5, 7, 11, 13", ok1)
    # 2 and 3: the field model
    ok2, ok3, ok5n = True, True, True
    for p in primes(5, 23):
        Fd = Field(p)
        chi, e1 = eta(-3, p), eta(-1, p)
        for r in (1, next(c for c in range(2, p) if eta(c, p) == -1)):
            C = [(x, y) for x in range(p) for y in range(p) if Fd.norm((x, y)) == r]
            m = len(C)
            nw = triangles(Fd, C)
            ok2 &= all(nw[w][a] == nw[w][(-a) % p] for w in nw for a in nw[w])
            for x in C:
                for y in C:
                    for z in C:
                        w = Fd.add(Fd.sub(x, y), z)
                        s = Fd.add(y, w)
                        A = Fd.sym(Fd.sub(y, x), Fd.sub(z, x))
                        if s == (0, 0):
                            ok2 &= A == (2 * Fd.sym(w, x)) % p
                        else:
                            ok2 &= A == ((Fd.norm(w) - r) * Fd.sym(s, x) * pow(Fd.norm(s), -1, p)) % p
            for w in [(0, 0)] + C[:3] + [(1, 1), (2, 1)]:
                for y in C:
                    s = Fd.add(y, w)
                    if s != (0, 0):
                        cnt = sum(1 for x in C if Fd.sub(s, x) in set(C))
                        ok2 &= cnt == 1 - eta((1 - 4 * r * pow(Fd.norm(s), -1, p)) % p, p)
            part0 = sum(c * c for c in nw.get((0, 0), Counter()).values())
            partC = sum(sum(c * c for c in nw[w].values()) for w in nw if Fd.norm(w) == r)
            partG = sum(sum(c * c for c in nw[w].values()) for w in nw if w != (0, 0) and Fd.norm(w) != r)
            ok3 &= part0 == (1 - chi) * m * m and partC == m * (4 * p * p + 6 * p - 2 + e1)
            ok3 &= partG == m * (2 * p * p - 3 * p + 3 - e1 - (1 - chi))
            ok3 &= part0 + partC + partG == m * (6 * p * p + (4 - chi) * p + 1)
            # N6 directly, as the sum over w of n_w^2, against the Kloosterman form
            N6 = sum(sum(nw[w].values()) ** 2 for w in nw)
            a = np.arange(1, p)
            inv = np.array([pow(int(v), -1, p) for v in a])
            V6 = int(round(sum(np.cos(2 * np.pi * ((a + c * inv) % p) / p).sum() ** 6 for c in range(1, p))))
            ok5n &= N6 * p * p == m ** 6 + m * V6
    check("step 2: in the field model, reversing a triangle negates its area; the area is (N(w) - r) Im(x/s) when "
          "s = y + w != 0 and 2<w, x> when s = 0; and each (w, y) carries 1 - eta(1 - 4r/N(s)) triangles, at every prime "
          "from 5 to 23 on two circles", ok2)
    check("step 3: the three parts are (1 - chi) m^2, m(4p^2 + 6p - 2 + (-1|p)) and m(2p^2 - 3p + 3 - (-1|p) - (1 - chi)), "
          "and Z6 = m(6p^2 + (4 - chi)p + 1), at every prime from 5 to 23 on two circles", ok3)
    # 4. the Legendre-symbol lemmas, r = 1
    ok4 = True
    for p in primes(5, 199):
        chi, e1 = eta(-3, p), eta(-1, p)
        m = p + 1
        eps = next(e for e in range(2, p) if eta(e, p) == -1)
        T = [(x, y) for x in range(p) for y in range(p) if (x * x - eps * y * y) % p == 1]
        Q = sum(1 - eta((((2 * x) % p) ** 2 - 4) % p, p) for (x, y) in T if (x, y) != (p - 1, 0))
        ok4 &= Q == 2 * m - 3
        B = Counter((2 * y) % p for (x, y) in T)                          # 2<w, x>/r = 2 Im(mu)
        ok4 &= sum(B[a] ** 2 for a in range(p)) == 2 * p + 1 + e1
        S = [s for s in range(1, p) if s != 4 % p and eta(s * (s - 4), p) == -1]
        D = lambda nu, s: ((s - 1 - nu) ** 2 - 4 * nu) % p
        nus = [nu for nu in range(2, p)]
        L = sum((1 - eta(D(nu, 4), p)) ** 2 for nu in nus)
        H = sum(eta(D(nu, s), p) for nu in nus for s in S)
        K0 = sum(1 for nu in nus for s in S if D(nu, s) == 0)
        ok4 &= L == 2 * p - 1 and H == -(p - 1) // 2 + (1 if chi == -1 else 0)
        ok4 &= K0 == (p - 2 + e1) // 2 - (1 if chi == -1 else 0)
    check("step 4: Q = 2m - 3, sum B^2 = 2p + 1 + (-1|p), L = 2p - 1, H = -(p - 1)/2 + [chi = -1] and "
          "K0 = (p - 2 + (-1|p))/2 - [chi = -1], at every prime from 5 to 199", ok4)
    # 5. the circle's Fourier transform
    ok5 = True
    for p in primes(5, 31):
        Fd = Field(p)
        a = np.arange(1, p)
        inv = np.array([pow(int(v), -1, p) for v in a])
        K = {c: np.cos(2 * np.pi * ((a + c * inv) % p) / p).sum() for c in range(1, p)}
        for r in (1, next(c for c in range(2, p) if eta(c, p) == -1)):
            C = [(x, y) for x in range(p) for y in range(p) if Fd.norm((x, y)) == r]
            for al in [(x, y) for x in range(p) for y in range(p)][1::max(1, p // 3)]:
                val = sum(np.exp(2j * np.pi * Fd.tr(Fd.mul(al, v)) / p) for v in C)
                ok5 &= abs(val + K[(r * Fd.norm(al)) % p]) < 1e-8
    check("step 5: a circle's Fourier transform is a Kloosterman sum, sum over N(v) = r of psi(Tr(alpha v)) = "
          "-K(r N(alpha)), at every prime from 5 to 31; and N6 = ((p + 1)^6 + (p + 1) V6)/p^2, counted directly as "
          "sum_w n_w^2, at every prime from 5 to 23", ok5 and ok5n)
    # 6. the classical sixth moment
    b6 = emo.eta_coeffs([(1, 2), (2, 2), (3, 2), (6, 2)], 401)
    ok6 = True
    for p in primes(7, 199):
        a = np.arange(1, p)
        inv = np.array([pow(int(v), -1, p) for v in a])
        V6 = int(round(sum(np.cos(2 * np.pi * ((a + c * inv) % p) / p).sum() ** 6 for c in range(1, p))))
        ok6 &= V6 == 5 * p ** 4 - 10 * p ** 3 - (b6[p] + 9) * p * p - 5 * p - 1
    check("step 6: V6 = 5p^4 - 10p^3 - (b(p) + 9)p^2 - 5p - 1, b(p) from (eta(t) eta(2t) eta(3t) eta(6t))^2, at every "
          "prime from 7 to 199 (Hulek, Spandaw, van Geemen and van Straten)", ok6)
    # 7. the operators' phase-0 count is the proved Z6
    ok7, n7 = True, 0
    for name in ("exact_moments_collect.log", "exact_moments_test.log"):
        keys = None
        for line in open(os.path.join(HERE, name), encoding="utf-8"):
            f = line.split()
            if f and f[0] == "EXACT" and f[1] == "p":
                keys = f[2:-2]
            elif f and f[0] == "EXACT" and f[1].isdigit():
                p = int(f[1])
                if p < 7:
                    continue
                c = dict(zip(keys or "I2 J2 I3 J3 I4 J4 I5 J5 I6 J6".split(), map(int, f[2:12])))
                m = p + 1
                V6 = 5 * p ** 4 - 10 * p ** 3 - (b6[p] + 9) * p * p - 5 * p - 1
                N6 = (m ** 6 + m * V6) // (p * p)
                Z6 = (c["I6"] // p + N6) // p
                ok7 &= Z6 == m * (6 * p * p + (4 - eta(-3, p)) * p + 1) and c["I6"] == p * (p * Z6 - N6)
                n7 += 1
    check(f"step 7: the phase-0 hexagons counted from the states' exact sixth moment are the proved Z6 at all {n7} "
          f"primes from 7 to 401", ok7 and n7 >= 70)
    say()
    say("ALL PASS" if OK else "A CHECK FAILED")
    LOG.close()
    sys.exit(0 if OK else 1)


if __name__ == "__main__":
    main()
