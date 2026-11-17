"""verify_fifth_moment.py -- checks each step of TORUS_MOMENTS.md section 8's fifth moments (Theorems 6 and 7):

  J5 = p (p + 1) [f15(p) - p a_E(p) + (4 chi - 3) p - 1],  E: y^2 = x(x - 4)(4x^2 - 52x + 9),  chi = (-3|p)
  I5 = p (p + 1) [p^3 + 4p^2 - (1 + (5|p)) p - 4 + a10(p)] - p^5 - 1

  1. the instrument: modular_symbols.py reproduces the weight-4 eta products of levels 5, 6, 8, 9     (primes to 199)
  2. the phase in the field model: with u_i = (-1)^i v_i, a 5-tuple on the circle has phase 0 exactly when
     sum_{i<j} Im(conj(u_i) u_j) = 0; that count, Z5, is the operators' (I5 + m^5)/p                      (p = 7, 11, 13)
  3. Hermitian Gauss sums: Z_n = p^-(n+1) sum_r (-p)^r p^(2(n-r)) (p A_r - B_r)/(p - 1) over the rank strata of
     diag(lam) + hK; for h != 0 the rank is n or n - 1 (the rank lemma); hence I_n = (p + 1)(p N_V - N_W) for odd n
     and J_n = p^n - 1 - p (p + 1) N_V for even n                                         (n = 3, 4, 5; p = 7, 11, 13)
  4. N_W = #{Prod(1 + sqrt(eps) d_i) in F_p} = (p^5 + 1)/(p + 1), by the torus                        (p = 7 .. 17)
  5. the third moment again: N_V(3) = 3p - 2, so I3 = (p + 1)(p - 1)(2p + 1) (section 6)              (p = 7 .. 31)
  6. the fifth: N_V = p^3 + 10p^2 - (20 + (5|p)) p - 4 - (-1|p) S_oct, through the Clebsch cubic
     (p^2 + (6 + (5|p)) p + 1 points), its five Sylvester planes (5p^2 - 5p + 5) and their 15 common lines (15p - 20)
                                                                                     (N_V: p = 7 .. 19; counts: 7 .. 43)
  7. the double octic: (-1|p) S_oct = 6p^2 - 19p - a10(p), a10 the weight-4 newform of level 10
     (recomputed at 7 .. 101; fifth_moments_collect.log to 401)                         [measured; round 17 to 601]
  8. so I5's formula holds against the operators' integers at every prime from 7 to 401
  9. J5's phase-0 count: chords and triangles with the same alternating sum w; (p + 1) #E(F_p); the special
     classes (13|p) and (-15|p) cancel                                                    (field model, p = 7 .. 23)
 10. Kloosterman's fifth moment V5 = 1 + 4p + 5p^2 + 4 chi p^3 + p^2 f15(p) [Peters, Top and van der Vlugt]
     (primes to 199), so J5's formula holds against the operators at every prime to 401; E's traces are those of the
     weight-2 newform of level 150 with a(7), a(11), a(13) = -2, 2, -6                                (primes to 401)
 11. J4's count reduced: N_V(4) = (p - 1)(p - 3) + 4b^2 by brute force (p = 7 .. 29) and from round 16's J4 (to 401)
     and, pairing the points, N_V(4) = (p - 1)^2 + 2 + (-1|p)p - T(p) with T one elliptic surface's character sum,
     T(p) = (2 + (-1|p))p - 4b^2, now proved (fourth_cumulant.py)                    (p = 7 .. 29; T at every prime to 401)
 12. the free picture: sqrt(p) times the normalized fifth moment tends to 5 (free cumulants k1 = 1/sqrt p,
     k3 = -1/sqrt p, k5 = o(1/sqrt p))
 13. a piece the whole does not carry (kept as a dead end): split by w, the part of Z5 with w on the circle holds the
     surface sum S2 = 2p - 1 + c11(p) - p (r3(p) - 1), with c11 the weight-3 CM form of Q(sqrt -11) and r3 the roots
     of x^3 - x^2 + x + 1 (a weight-1 form, discriminant -44); Theorem 7 has neither, so they cancel   (primes 7..101)

numpy + sympy + modular_symbols.py + fifth_moments.py + exact_moments.py.  One process, below-normal priority.  ASCII
output; writes runs/verify_fifth_moment.log and exits with 1 if a check fails.
Run:  python verify_fifth_moment.py     (about two minutes)
"""
import itertools
import os
import sys
import time

import numpy as np
import sympy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fifth_moments as fm          # sets below-normal priority
import modular_symbols as ms
import exact_moments as emo

os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)   # run logs go to runs/ (ignored); the committed copy is the reference
LOG = open(os.path.join(HERE, "runs", "verify_fifth_moment.log"), "w", encoding="utf-8")
FAILS = []
eta = fm.eta


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def check(name, ok, detail=""):
    say(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


def op_counts():
    out = {}
    for name in ("exact_moments_collect.log", "exact_moments_test.log"):
        keys = "I2 J2 I3 J3 I4 J4 I5 J5 I6 J6".split()      # the test log reuses the collect log's columns
        for line in open(os.path.join(HERE, name), encoding="utf-8"):
            f = line.split()
            if f and f[0] == "EXACT" and f[1] == "p":
                keys = f[2:-2]
            elif f and f[0] == "EXACT" and f[1].isdigit():
                out[int(f[1])] = dict(zip(keys, map(int, f[2:2 + len(keys)])))
    return out


def nonsq(p):
    return next(e for e in range(2, p) if eta(e, p) == -1)


def circle(p, eps):
    return [(x, y) for x in range(p) for y in range(p) if (x * x - eps * y * y) % p == 1]


def esym(cols, p):
    e = [np.ones_like(cols[0])] + [np.zeros_like(cols[0]) for _ in cols]
    for c in cols:
        for k in range(len(cols), 0, -1):
            e[k] = (e[k] + e[k - 1] * c) % p
    return e


def rank_strata(n, p):
    """A_r, B_r: points (lam, h) of F_p^(n+1) where diag(lam) + hK has rank r (B), and also e1(lam) = 0 (A).
    h = 0: rank = number of nonzero lam_i.  h != 0: delta = 2 lam/h, rank of A_n + sqrt(eps) diag(delta) read from
    its principal minors: |S| even -> sum_j even eps^(j/2) e_j(d_S);  |S| odd -> sum_j odd eps^((j-1)/2) e_j(d_S)."""
    eps = nonsq(p)
    g = np.indices((p,) * n).reshape(n, -1).astype(np.int64)
    d = [g[i] for i in range(n)]
    rank = np.zeros(g.shape[1], dtype=np.int64)
    for size in range(1, n + 1):
        for S in itertools.combinations(range(n), size):
            es = esym([d[i] for i in S], p)
            js = range(0 if size % 2 == 0 else 1, size + 1, 2)
            val = np.zeros_like(d[0])
            for j in js:
                val = (val + pow(eps, j // 2, p) * es[j]) % p
            rank = np.where(val != 0, np.maximum(rank, size), rank)
    e1zero = (sum(d) % p) == 0
    nz = (np.array(d) != 0).sum(axis=0)
    B = np.bincount(nz, minlength=n + 1) + (p - 1) * np.bincount(rank, minlength=n + 1)
    A = np.bincount(nz[e1zero], minlength=n + 1) + (p - 1) * np.bincount(rank[e1zero], minlength=n + 1)
    hrank_min = int(rank.min())
    return A, B, hrank_min


def Z_from_strata(n, p):
    A, B, rmin = rank_strata(n, p)
    tot = sum((-p) ** r * p ** (2 * (n - r)) * (p * int(A[r]) - int(B[r])) for r in range(n + 1))
    assert tot % ((p - 1) * p ** (n + 1)) == 0
    return tot // ((p - 1) * p ** (n + 1)), rmin


def Z_direct(n, p, closed_origin=False):
    """phase-0 n-tuples on the unit circle in the field model: sum_{i<j} Im(conj(u_i) u_j) = 0"""
    eps = nonsq(p)
    C = circle(p, eps)
    m = len(C)
    X = np.array([c[0] for c in C]); Y = np.array([c[1] for c in C])
    S = (X[:, None] * Y[None, :] - Y[:, None] * X[None, :]) % p
    idx = np.indices((m,) * n).reshape(n, -1)
    F = np.zeros(idx.shape[1], dtype=np.int64)
    for i in range(n):
        for j in range(i + 1, n):
            F = (F + S[idx[i], idx[j]]) % p
    return int((F == 0).sum())


def N_V_direct(n, p):
    eps = nonsq(p)
    g = np.indices((p,) * (n - 1)).reshape(n - 1, -1).astype(np.int64)
    d = [g[i] for i in range(n - 1)]
    d.append((-sum(d)) % p)
    e = esym(d, p)
    js = range(1 if n % 2 else 0, n + 1, 2)
    val = np.zeros_like(d[0])
    for j in js:
        val = (val + pow(eps, j // 2, p) * e[j]) % p
    return int((val == 0).sum())


def b_even(p):
    if p % 4 == 3:
        return 0
    return emo.b_even(p)


def main():
    t0 = time.time()
    say("verify_fifth_moment.py -- TORUS_MOMENTS.md section 8, the fifth moments")
    data = op_counts()
    PS = [p for p in sorted(data) if p >= 7]
    # 1. the instrument
    known = {5: [(1, 4), (5, 4)], 6: [(1, 2), (2, 2), (3, 2), (6, 2)], 8: [(2, 4), (4, 4)], 9: [(3, 8)]}
    ok = True
    for N, spec in known.items():
        cf = emo.eta_coeffs(spec, 200)
        sy = ms.rational_eigensystems(N, fm.primes(7, 199))
        ok &= len(sy) == 1 and all(sy[0]["ap"][p] == cf[p] for p in sy[0]["ap"])
    check("1. the modular-symbols engine reproduces the weight-4 eta products of levels 5, 6, 8, 9 (primes 7..199)", ok)
    # 2. the phase in the field model
    ok = all(Z_direct(5, p) == (data[p]["I5"] + (p + 1) ** 5) // p for p in (7, 11, 13))
    check("2. Z5 counted in the field model equals the operators' (I5 + m^5)/p at p = 7, 11, 13", ok)
    # 3. Hermitian Gauss sums and the rank lemma
    ok, rk = True, True
    for n in (3, 4, 5):
        for p in (7, 11, 13):
            z, rmin = Z_from_strata(n, p)
            ok &= z == Z_direct(n, p)
            rk &= rmin >= n - 1
            m = p + 1
            NW = (p ** n + 1) // (p + 1) if n % 2 else (p ** n - 1) // (p + 1)
            NV = N_V_direct(n, p)
            if n % 2:
                ok &= p * z - m ** n == m * (p * NV - NW)
            else:
                ok &= p * z - m ** n == p ** n - 1 - p * m * NV
    check("3a. Z_n from the Hermitian rank strata equals the direct count (n = 3, 4, 5; p = 7, 11, 13)", ok)
    check("3b. the rank lemma: for h != 0 the rank of diag(lam) + hK is n or n - 1", rk)
    ok = all(data[p]["J4"] == p ** 4 - 1 - p * (p + 1) * N_V_direct(4, p) for p in (7, 11, 13))
    check("3c. J4 = p^4 - 1 - p(p + 1) N_V(4) against the operators at p = 7, 11, 13", ok)
    # 4. N_W
    ok = all(fm_NW(p) == (p ** 5 + 1) // (p + 1) for p in (7, 11, 13, 17))
    check("4. N_W = #{d in F_p^5: Prod(1 + sqrt(eps) d_i) in F_p} = (p^5 + 1)/(p + 1) at p = 7..17", ok)
    # 5. the third moment again
    ok = all(N_V_direct(3, p) == 3 * p - 2 and (p + 1) * (p * (3 * p - 2) - (p ** 3 + 1) // (p + 1)) == (p + 1) * (p - 1) * (2 * p + 1)
             for p in fm.primes(7, 31))
    check("5. N_V(3) = 3p - 2 and so I3 = (p + 1)(p - 1)(2p + 1), the theorem of section 6 (p = 7..31)", ok)
    # 6. the fifth: Clebsch, the planes, the lines, and N_V
    ok_c = True
    for p in fm.primes(7, 43):
        cl, pl, li = clebsch_counts(p)
        ok_c &= cl == p * p + (6 + eta(5, p)) * p + 1 and pl == 5 * p * p - 5 * p + 5 and li == 15 * p - 20
    check("6a. on e1 = 0: the Clebsch cubic e3 = 0 has p^2 + (6 + (5|p))p + 1 points, the planes 5p^2 - 5p + 5, "
          "their common lines 15p - 20 (p = 7..43)", ok_c)
    ok = all(N_V_direct(5, p) == fm.NV_from_octic(p, fm.S_oct(p)) for p in fm.primes(7, 19))
    check("6b. N_V = p^3 + 10p^2 - (20 + (5|p))p - 4 - (-1|p) S_oct (p = 7..19)", ok)
    # 7. the double octic
    a10, e150 = fm.named_forms(PS)
    logS = {}
    for line in open(os.path.join(HERE, "fifth_moments_collect.log"), encoding="utf-8"):
        f = line.split()
        if f and f[0] == "OCTIC" and f[1].isdigit():
            logS[int(f[1])] = int(f[2])
    ok_re = all(fm.S_oct(p) == logS[p] for p in fm.primes(7, 101))
    check("7a. S_oct recomputed at every prime 7..101 equals fifth_moments_collect.log", ok_re)
    ok = all(eta(-1, p) * logS[p] == 6 * p * p - 19 * p - a10[p] for p in PS)
    check(f"7b. (-1|p) S_oct = 6p^2 - 19p - a10(p) at all {len(PS)} primes 7..401 [measured]", ok,
          f"a10(7..23) = {[a10[p] for p in PS[:6]]}")
    # 8. I5
    ok = all(data[p]["I5"] == fm.I5_formula(p, a10[p]) for p in PS)
    check(f"8. I5 = p(p + 1)[p^3 + 4p^2 - (1 + (5|p))p - 4 + a10(p)] - p^5 - 1 at all {len(PS)} primes 7..401", ok)
    # 9. J5's phase-0 count
    ok9 = all(j5_parts(p) for p in fm.primes(7, 23))
    check("9. J5's phase-0 polygons: chords, triangles and the special classes as in the proof; Z = (p + 1) #E(F_p) (p = 7..23)", ok9)
    # 10. V5, J5 and E
    f15 = fm.f15_coeffs(401)
    ok = True
    for p in fm.primes(7, 199):
        K = kloosterman(p)
        V5 = int(round(float((K ** 5).sum())))
        ok &= V5 == 1 + 4 * p + 5 * p * p + 4 * eta(-3, p) * p ** 3 + p * p * f15[p]
    check("10a. Kloosterman's fifth moment V5 = 1 + 4p + 5p^2 + 4(-3|p)p^3 + p^2 f15(p) (primes 7..199) [NAMED: Peters, Top, van der Vlugt]", ok)
    ok = all(data[p]["J5"] == fm.J5_formula(p, p + 1 - fm.E_count(p), f15[p]) for p in PS)
    check(f"10b. J5 = p(p + 1)[f15(p) - p a_E(p) + (4(-3|p) - 3)p - 1] at all {len(PS)} primes 7..401", ok)
    ok = all(p + 1 - fm.E_count(p) == e150[p] for p in PS)
    check("10c. E's traces equal the level-150 newform's (a(7), a(11), a(13) = -2, 2, -6) at every prime 7..401 [measured]", ok)
    # 11. J4's count
    ok = all(N_V_direct(4, p) == (p - 1) * (p - 3) + 4 * b_even(p) ** 2 for p in fm.primes(7, 29))
    ok2 = all((p ** 4 - 1 - data[p]["J4"]) == p * (p + 1) * ((p - 1) * (p - 3) + 4 * b_even(p) ** 2) for p in PS)
    check("11. J4's count: N_V(4) = (p - 1)(p - 3) + 4b^2 by brute force (p = 7..29) and from round 16's J4 (to 401)", ok and ok2)
    ok = all(N_V_direct(4, p) == (p - 1) ** 2 + 2 + eta(-1, p) * p - T_surface(p) for p in fm.primes(7, 29))
    ok2 = all(T_surface(p) == (2 + eta(-1, p)) * p - 4 * b_even(p) ** 2 for p in PS)
    check("11b. pairing: N_V(4) = (p - 1)^2 + 2 + (-1|p)p - T(p), T the elliptic surface's sum (p = 7..29); and "
          "T(p) = (2 + (-1|p))p - 4b^2 at every prime 7..401 [proved: fourth_cumulant.py, Theorem 5]", ok and ok2)
    # 12. the free picture
    vals = []
    for p in (101, 199, 401):
        m = p + 1
        M5 = data[p]["I5"] / ((p - 1) * p * m ** 2.5)
        vals.append((p, round(float(np.sqrt(p) * M5), 4)))
    ok = all(abs(v - 5) < 12 / np.sqrt(p) for p, v in vals)
    check("12. sqrt(p) x the normalized fifth moment I5/((p - 1) p m^(5/2)) approaches 5, the free picture's value", ok, str(vals))
    # 13. a piece the whole does not carry
    ok = all(S2_circle(p) == 2 * p - 1 + c11(p) - p * (r3(p) - 1) for p in fm.primes(7, 101))
    check("13. the circle part's surface sum S2 = 2p - 1 + c11(p) - p(r3(p) - 1) (Q(sqrt -11)'s weight-3 CM form and a "
          "weight-1 form) at every prime 7..101; Theorem 7 carries neither, so they cancel [a dead end, kept]", ok)
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()
    sys.exit(1 if FAILS else 0)


def T_surface(p):
    """sum over k != 0 and A of eta(k A (k + 4 - 4A)((k + 4)A - 4k)): J4's open count after pairing"""
    L = np.array([eta(v, p) for v in range(p)], dtype=np.int64)
    k = np.arange(1, p, dtype=np.int64)[:, None]
    A = np.arange(p, dtype=np.int64)[None, :]
    val = (k * A % p * ((k + 4 - 4 * A) % p) % p * (((k + 4) * A - 4 * k) % p)) % p
    return int(L[val].sum())


def S2_circle(p):
    """sum over z = X + Y sqrt(eps) on the unit circle and a in F_p of eta((1 + eps a^2/4)((X - 1)^2 + eps a^2 + 2 eps a Y))"""
    eps = nonsq(p)
    L = np.array([eta(v, p) for v in range(p)], dtype=np.int64)
    C = np.array(circle(p, eps), dtype=np.int64)
    X, Y = C[:, 0][:, None], C[:, 1][:, None]
    a = np.arange(p, dtype=np.int64)[None, :]
    inv4 = pow(4, p - 2, p)
    B = (1 + eps * a * a % p * inv4) % p
    T = ((X - 1) ** 2 + eps * a * (a + 2 * Y)) % p
    return int(L[B * T % p].sum())


def c11(p):
    """the weight-3 newform with CM by Q(sqrt -11): pi^2 + conj(pi)^2 with 4p = A^2 + 11 B^2, 0 at inert p"""
    if p == 11:
        return -11
    if eta(-11, p) != 1:
        return 0
    for B in range(1, int((4 * p / 11) ** 0.5) + 1):
        A2 = 4 * p - 11 * B * B
        A = int(round(A2 ** 0.5))
        if A * A == A2:
            return (A * A - 11 * B * B) // 2


def r3(p):
    return sum(1 for x in range(p) if (x ** 3 - x * x + x + 1) % p == 0)


def fm_NW(p):
    return N_W_direct(p)


def N_W_direct(p):
    eps = nonsq(p)
    g = np.indices((p,) * 5).reshape(5, -1).astype(np.int64)
    e = esym([g[i] for i in range(5)], p)
    return int(((e[1] + eps * e[3] + eps * eps % p * e[5]) % p == 0).sum())


def clebsch_counts(p):
    """points of P^3 = {e1 = 0} on e3 = 0 (Clebsch), on e5 = 0 (the planes), on both (the lines)"""
    cl = pl = li = 0
    pts = []
    for a in range(p):                                   # [1 : a : b : c]
        for b in range(p):
            for c in range(p):
                pts.append((1, a, b, c))
    for b in range(p):
        for c in range(p):
            pts.append((0, 1, b, c))
    for c in range(p):
        pts.append((0, 0, 1, c))
    pts.append((0, 0, 0, 1))
    P_ = np.array(pts, dtype=np.int64)
    d5 = (-P_.sum(axis=1)) % p
    D = np.concatenate([P_, d5[:, None]], axis=1)
    e3 = (D ** 3).sum(axis=1) % p                        # 3 e3 on e1 = 0
    e5 = np.prod(D % p, axis=1) % p
    cl = int((e3 == 0).sum()); pl = int((e5 == 0).sum()); li = int(((e3 == 0) & (e5 == 0)).sum())
    return cl, pl, li


def kloosterman(p):
    a = np.arange(1, p)
    inv = np.array([pow(int(x), p - 2, p) for x in a])
    K = np.zeros(p - 1)
    for i, x in enumerate(a):
        K += np.cos(2 * np.pi * ((x * a + inv[i]) % p) / p)
    return K


def j5_parts(p):
    """J5's phase-0 count in the field model, part by part, against the proof (section 8, Theorem 6):
    chords v2 - v1 = w have areas +-Y with 4 eps Y^2 = nu^2 - 4 nu (nu = N(w)); triangles with alternating sum w and
    area +-Y number 1 - eta(4 nu^2 - 52 nu + 9) off the special classes; nu = 1 gives 2(1 + (13|p)) when chi = -1,
    nu = 4 gives 1 - (-15|p), 2 nu + 1 = 0 gives 0; and the total is (p + 1) #E(F_p)."""
    eps = nonsq(p)
    C = circle(p, eps)
    m = len(C)
    sym = lambda u, v: (u[0] * v[1] - u[1] * v[0]) % p
    sub = lambda u, v: ((u[0] - v[0]) % p, (u[1] - v[1]) % p)
    add = lambda u, v: ((u[0] + v[0]) % p, (u[1] + v[1]) % p)
    area = lambda x, y, z: sym(sub(y, x), sub(z, x))
    n = {}
    for x in C:
        for y in C:
            for z in C:
                w = add(sub(x, y), z)
                n.setdefault(w, {}).setdefault(area(x, y, z), 0)
                n[w][area(x, y, z)] += 1
    Z = 0
    ok = True
    chi = eta(-3, p)
    for v1 in C:
        for v2 in C:
            w = sub(v2, v1)
            a = sym(v1, v2)
            Z += n.get(w, {}).get((-a) % p, 0)
    # the per-class predictions, at one w of each norm
    byclass = {}
    for v1 in C:
        for v2 in C:
            w = sub(v2, v1)
            if w == (0, 0):
                continue
            nu = (w[0] * w[0] - eps * w[1] * w[1]) % p
            byclass.setdefault(nu, set()).add(w)
    for nu, ws in byclass.items():
        w = next(iter(ws))
        chords = [(v1, v2) for v1 in C for v2 in C if sub(v2, v1) == w]
        tot = sum(n.get(w, {}).get((-sym(v1, v2)) % p, 0) for v1, v2 in chords)
        if nu == 1:
            pred = 2 * (1 + eta(13, p)) if chi == -1 else 0
        elif nu == 4:
            pred = 1 - eta(-15, p)
        elif (2 * nu + 1) % p == 0:
            pred = 0
        else:
            pred = 2 * (1 - eta(4 * nu * nu - 52 * nu + 9, p))
        ok &= tot == pred and len(chords) == (1 if nu == 4 else 2)
    return ok and Z == m * fm.E_count(p)


if __name__ == "__main__":
    main()
