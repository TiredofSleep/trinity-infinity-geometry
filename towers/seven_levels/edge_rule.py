"""edge_rule.py -- the coin on its edge (round 21), and the cubic in eleven variables (round 22).

    "1 and 2, the mirror rule first"  -- the author, 14 November 2026
    (1: yes, a coin on its edge shows the mirror, so register the mirror rule.  2: the cubic in eleven variables.)

The rule, made precise (round 21 of PREREG.md).  Every coin has a flip, two sides and an edge, and the edge is the
flip's fixed set (the author's classification).  At an edge prime the two sides merge into that fixed set.
  (a) A count without a phase sees the fixed set once: its symbol reads 0, the average of its two sides.
  (b) A count with a phase sees the phase vanish on the fixed set, which adds p for each merged point.  When the merged
      points are all the primitive q-th roots of unity and the edge prime is q itself, the edge is the exact mirror of
      the side that holds them, because there are q - 1 = p - 1 of them.  At a prime power the mirror fails.

The cubics X_n = {x_1 + ... + x_n = x_1^3 + ... + x_n^3 = 0} are counts without a phase.  Their primitive traces t_n
are the moments of the cubic exponential sums S(a) = sum_x e((x^3 + a x)/p), divided by p^2 (orthogonality), so they
split by the ballot numbers m(n, k) into the symmetric powers of the Airy sheaf:

    t_n = sum over odd k <= n of m(n, k) p^((n - k)/2 - 2) T_k(p),    m(n, k) = C(n, (n-k)/2) - C(n, (n-k)/2 - 1).

T_k(p) is the trace on the classical part of H^1(A^1, Sym^k Ai), whose Hodge numbers are Sabbah and Yu's
[NAMED: arXiv:2112.13405, Theorem 1.1].  Rounds 19 and 20 measured T_1 = p, T_3 = 0, T_5 = (5|p) p^3,
T_7 = p^3 c(p) with c the weight-3 CM form of Q(sqrt -35), and T_9 = (105|p) p^5.

  python edge_rule.py          # the forced checks F1 to F5                      -> edge_rule_verify.log
  python edge_rule.py test     # round 21: the cubics at their edge primes 5 and 7 -> edge_rule_test.log
  python edge_rule.py test22   # round 22: the cubic in eleven variables          -> edge_rule_test22.log
                               #   (four worker processes at below-normal priority)

numpy + sympy + coin_at_five.py.  ASCII output.
"""
import cmath
import itertools
import math
import os
import sys
import time
from fractions import Fraction

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
import sympy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import coin_at_five as cf  # noqa: E402  (sets below-normal priority on import)

primes, leg, low_priority = cf.primes, cf.leg, cf.low_priority
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


# ------------------------------------------------------------------ the ballot numbers and the Airy pieces
def ballot(n, k):
    """multiplicity of Sym^k in the n-th tensor power of the standard 2-dimensional representation of SL(2)"""
    if (n - k) % 2 or k > n or k < 0:
        return 0
    j = (n - k) // 2
    return math.comb(n, j) - (math.comb(n, j - 1) if j >= 1 else 0)


def t_values(p, ns):
    """t_n = (N_n - p^(n-2))/(p - 1) for odd n, exactly, where N_n counts F_p^n points with sum x = sum x^3 = 0.
    For n >= 3 this is #X_n(F_p) - (1 + p + ... + p^(n-3)); for n = 1 (N_1 = 1) it is 1/p."""
    N = cf.cone_counts(p, tuple(n for n in ns if n >= 3))
    N[1] = 1
    return {n: (Fraction(N[n]) - Fraction(p) ** (n - 2)) / (p - 1) for n in sorted(set(ns) | {1})}


def airy(p, t):
    """the traces T_k from the t_n, by inverting the ballot triangle: T_n = p^2 (t_n - sum_(k<n) m(n,k) p^((n-k)/2-2) T_k)"""
    T = {}
    for n in sorted(t):
        s = t[n] - sum(ballot(n, k) * Fraction(p) ** ((n - k) // 2 - 2) * T[k] for k in T)
        T[n] = s * p * p
    return T


def classical_hodge(k):
    """Sabbah-Yu, Theorem 1.1, k odd: h^(p,q) = 1 for p + q = k + 1, p = (k + 2i)/3, 1 <= i <= (k + 1)/2.
    The classical part is where p is an integer."""
    return [((k + 2 * i) // 3, k + 1 - (k + 2 * i) // 3) for i in range(1, (k + 1) // 2 + 1) if (k + 2 * i) % 3 == 0]


def betti_prim(n):
    """primitive middle Betti number of a smooth cubic of dimension n - 3 (n odd): (2^(n-1) + 2)/3"""
    return (2 ** (n - 1) + 2) // 3


def ramified_dim(k, p):
    """the node reading: the number of odd multiples of p that are at most k"""
    return sum(1 for s in range(p, k + 1, 2 * p))


# ------------------------------------------------------------------ the turning wheel's circles and the operators
def nonsquare(p):
    return next(e for e in range(2, p) if leg(e, p) == -1)


def circles(p):
    """the circles of a non-split torus: level sets r != 0 of the anisotropic form q^2 - eps k^2 (SO of it is the torus;
    every non-split torus gives the same moments, since they are integers and the tori are conjugate up to scaling)"""
    eps = nonsquare(p)
    C = {r: [] for r in range(1, p)}
    for q in range(p):
        for k in range(p):
            r = (q * q - eps * k * k) % p
            if r:
                C[r].append((q, k))
    return C, eps


def operators(p):
    """<a|A_(q,k)|b> = [a + b = 2q] w^(k(a - b)), w = e^(2 pi i/p); A_0 is the half turn P"""
    w = [cmath.exp(2j * math.pi * t / p) for t in range(p)]
    A = {}
    for q in range(p):
        for k in range(p):
            M = np.zeros((p, p), dtype=complex)
            for a in range(p):
                b = (2 * q - a) % p
                M[a, b] = w[(k * (a - b)) % p]
            A[(q, k)] = M
    return A


def J3_by_operators(p):
    C, _ = circles(p)
    A = operators(p)
    P = A[(0, 0)]
    tot = 0
    for r, pts in C.items():
        S = sum(A[v] for v in pts)
        tot += np.trace(P @ S @ S @ S)
    return tot


def J3_merge(p):
    """J3 = p sum_C sum over v1, v3 on C with v1 + v3 on C of w^(2<v1, v3>) (TORUS_MOMENTS.md section 6, Step 7),
    with the ratios mu = v3/v1 in F_p(sqrt eps) that occur, and whether every phase is 0"""
    C, eps = circles(p)
    w = [cmath.exp(2j * math.pi * t / p) for t in range(p)]
    tot, mus, phases = 0, set(), set()
    for r, pts in C.items():
        S = set(pts)
        rinv = pow(r, p - 2, p)
        for (q1, k1) in pts:
            for (q3, k3) in pts:
                s = ((q1 + q3) % p, (k1 + k3) % p)
                if s not in S:
                    continue
                ph = (2 * (q1 * k3 - k1 * q3)) % p
                tot += w[ph]
                phases.add(ph)
                a = (q3 * q1 - eps * k3 * k1) * rinv % p        # v3 * conj(v1) / N(v1)
                b = (k3 * q1 - q3 * k1) * rinv % p
                mus.add((a, b))
    return p * tot, mus, phases


# ------------------------------------------------------------------ verify: the forced checks
def verify():
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_verify.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("edge_rule.py -- the coin on its edge: the forced checks")

    # F1: the merge at J3's edge
    ok, detail = True, []
    for p in primes(3, 13):
        op = J3_by_operators(p)
        mg, mus, ph = J3_merge(p)
        side = -2 * p * (p + 1) if p % 3 == 2 else 0
        want = p * (p + 1) * (p - 1) if p == 3 else side
        ok &= abs(op - want) < 1e-6 and abs(mg - want) < 1e-6
        detail.append(f"{p}:{round(op.real)}")
    check("F1a. J3 from the operators equals the merge count: -2p(p + 1) when p = 2 mod 3, 0 when p = 1 mod 3, and "
          "p(p + 1)(p - 1) = 24 at p = 3", ok, " ".join(detail))
    ok = True
    for p in primes(5, 61):
        mg, mus, ph = J3_merge(p)
        cube = {(a, b) for (a, b) in mus if (a * a + nonsquare(p) * b * b + a + 1) % p == 0 and (2 * a * b + b) % p == 0}
        if p % 3 == 2:
            ok &= len(mus) == 2 and cube == mus and 0 not in ph and abs(mg + 2 * p * (p + 1)) < 1e-6
        else:
            ok &= len(mus) == 0 and abs(mg) < 1e-6
    mg3, mus3, ph3 = J3_merge(3)
    ok3 = mus3 == {(1, 0)} and ph3 == {0}
    check("F1b. the pairs: on the side p = 2 mod 3 the ratio v3/v1 is a primitive cube root of unity, two of them, with "
          "nonzero phase; at p = 1 mod 3 there are none (every prime 5..61); at the edge p = 3 the only ratio is 1, the "
          "two roots merged (x^2 + x + 1 = (x - 1)^2 mod 3), and every phase is 0", ok and ok3,
          f"p = 3: ratios {sorted(mus3)}, phases {sorted(ph3)}")

    # F2: the cyclotomic weights -- the mirror is exact at a prime edge and fails at a prime power
    x = sympy.symbols("x")
    rows, ok = [], True
    for q in (3, 5, 7, 11, 13, 4, 8, 9, 25, 27, 49):
        ell = sympy.factorint(q)
        ell, kk = next(iter(ell.items()))
        phi = sympy.totient(q)
        merged = sympy.Poly(sympy.cyclotomic_poly(q, x), x, modulus=ell) == sympy.Poly((x - 1) ** phi, x, modulus=ell)
        mirror = (ell - 1) == phi
        ok &= merged and (mirror == (kk == 1))
        rows.append(f"{q}: sides -{phi}, edge +{ell - 1}{' mirror' if mirror else ''}")
    check("F2. at the edge prime l the primitive q-th roots (q = l^k) merge into 1, Phi_q = (x - 1)^phi(q) mod l. Each "
          "root's phase sum is -1 on the side that holds them; the merged point's is l - 1. So the edge mirrors the side "
          "exactly when l - 1 = phi(q), that is when q = l is prime", ok, "; ".join(rows))

    # F3: the node identity
    ok, rows = True, []
    for n in range(5, 18, 2):
        for p in (5, 7, 11, 13):
            nodes = len(cf.singular_sign_points(n, p))
            pred = sum(ballot(n, k) * ramified_dim(k, p) for k in range(1, n + 1, 2))
            ok &= nodes == pred
            if n <= 11:
                rows.append(f"n={n},p={p}:{nodes}")
    check("F3. the node identity: #nodes(X_n mod p) = sum_k m(n, k) r_k(p), with r_k(p) the number of odd multiples of p "
          "up to k (every odd n from 5 to 17, p = 5, 7, 11, 13). So each node is one dimension ramified at p if V_k is "
          "ramified at p with dimension r_k(p): V_5 at 5; V_7 at 5, 7; V_9 at 5, 7; V_11 at 5, 7, 11", ok, " ".join(rows))

    # F4: Sabbah-Yu's classical Hodge numbers and the Betti numbers
    v = {k: len(classical_hodge(k)) for k in range(1, 14, 2)}
    ok = all(sum(ballot(n, k) * v[k] for k in range(1, n + 1, 2)) == betti_prim(n) for n in range(3, 14, 2))
    check("F4. the classical parts of Sabbah and Yu's Airy moments have dimensions v_k = 1, 0, 1, 2, 1, 2, 3 (k = 1..13) "
          "and Hodge types " + ", ".join(f"k={k}:{classical_hodge(k)}" for k in (1, 5, 7, 9, 11)) +
          "; with the ballot numbers they add up to the primitive Betti numbers 6, 22, 86, 342, 1366 of X_5..X_13", ok,
          f"v = {v}")

    # F5: the measured formulas in Airy form, at every prime 11..61
    ok, worst = True, ""
    for p in primes(11, 61):
        T = airy(p, t_values(p, (3, 5, 7, 9)))
        c = T[7] / p ** 3
        good = (T[1] == p and T[3] == 0 and T[5] == leg(5, p) * p ** 3 and c.denominator == 1
                and abs(int(c)) == cf.cm35(p) and T[9] == leg(105, p) * p ** 5)
        ok &= good
        if not good:
            worst += f" {p}"
    check("F5. rounds 19 and 20 in Airy form: T_1 = p, T_3 = 0, T_5 = (5|p)p^3, T_7 = p^3 c(p) with |c| the CM form of "
          "Q(sqrt -35), T_9 = (105|p)p^5, at every prime 11..61", ok, worst.strip())

    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()


# ------------------------------------------------------------------ round 21: the cubics at their edge primes
def lines_at_five():
    p = 5
    U, V = cf.lines_on_cubic(p)
    centre = np.array([1, 1, 1, 1])
    planes = through = 0
    for u, v in zip(U, V):
        l = (u, v)
        if cf.in_a_plane(l, p):
            planes += 1
        if cf.rank_mod_p(sympy.Matrix([list(u), list(v), list(centre)]), p) == 2:
            through += 1
    return len(U), planes, through


def J5_split(p):
    """J5 = p(pZ - N): N closed five-point configurations on one circle, Z of them with phase 0 (read, not scored)"""
    C, _ = circles(p)
    A = operators(p)
    P = A[(0, 0)]
    pts = C[1]
    N = Z = 0

    def walk(M, depth):  # depth-first over the 5-tuples, reusing partial products
        nonlocal N, Z
        if depth == 5:
            tr = np.trace(M)
            if abs(tr) > 0.5:
                N += 1
                ph = round(cmath.phase(tr) * p / (2 * math.pi)) % p
                Z += ph == 0
            return
        for v in pts:
            walk(M @ A[v], depth + 1)
    walk(P, 0)
    return N, Z, p * (p * Z - N)


def kloosterman_V5(p):
    w = [cmath.exp(2j * math.pi * t / p) for t in range(p)]
    K = [sum(w[(x + a * pow(x, p - 2, p)) % p] for x in range(1, p)).real for a in range(p)]
    return round(sum(k ** 5 for k in K[1:])), round(sum(k ** 5 for k in K))


def curve_Z(p):
    """the side formula for Z (TORUS_MOMENTS.md, Theorem 6, Step 4): (p + 1)(p + 2 + sum_nu eta(nu(nu - 4)(4nu^2 - 52nu + 9)))"""
    s = sum(leg(n * (n - 4) * (4 * n * n - 52 * n + 9), p) for n in range(p))
    return (p + 1) * (p + 2 + s)


def test():
    """round 21 (PREREG.md): K0 to K3, and the controls"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("Round 21: the coin on its edge -- the cubics at their edge primes 5 and 7 (PREREG.md)")
    # K0
    n, planes, through = lines_at_five()
    say(f"LINES p=5: {n} lines on Clebsch's cubic, {planes} in the Sylvester planes, {through} through the centre")
    k0 = n == 21 and planes == 15 and through == 6
    say(f"K0 21 lines over F_5: the 15 of the edge and 6 through the centre: {'HELD' if k0 else 'FAILED'}")
    # K1..K3
    T = {}
    for p in (5, 7):
        t = t_values(p, (3, 5, 7, 9))
        T[p] = airy(p, t)
        say(f"CUBIC p={p}: t3={t[3]} t5={t[5]} t7={t[7]} t9={t[9]}   T1={T[p][1]} T3={T[p][3]} T5={T[p][5]} "
            f"T7={T[p][7]} T9={T[p][9]}")
    ctrl = all(T[p][1] == p and T[p][3] == 0 for p in (5, 7)) and T[7][5] == -343
    say(f"control: T1 = p and T3 = 0 at 5 and 7, T5(7) = (5|7)7^3 = -343: {ctrl}")
    k1 = T[5][5] == 0
    say(f"K1 T5(5) = 0, so t5(5) = 25 (the symbol reads 0; the reflection would give 10): {'HELD' if k1 else 'FAILED'}  "
        f"(T5(5) = {T[5][5]})")
    k2 = abs(T[5][7]) == 5 ** 4 and abs(T[7][7]) == 7 ** 4
    say(f"K2 |T7(5)| = 5^4 and |T7(7)| = 7^4, so |c(5)| = 5 and |c(7)| = 7: {'HELD' if k2 else 'FAILED'}  "
        f"(c(5) = {T[5][7] / 125}, c(7) = {T[7][7] / 343})")
    k3 = T[5][9] == 0 and T[7][9] == 0
    say(f"K3 T9(5) = T9(7) = 0 (the symbol (105|p) reads 0): {'HELD' if k3 else 'FAILED'}  (T9(5) = {T[5][9]}, "
        f"T9(7) = {T[7][9]})")
    # read after the run, not scored: J5 split into Z and N
    say("READ (not scored): J5 = p(pZ - N) split at small primes")
    for p in (3, 5, 7, 11):
        N, Z, j5 = J5_split(p)
        V5a, V5b = kloosterman_V5(p)
        Nf = ((p + 1) ** 5 - (p + 1) * V5a) / p ** 2
        say(f"  p={p}: N = {N} (from Kloosterman's V5 = {V5a} over a != 0: {Nf:g}), Z = {Z} (the curve's side "
            f"formula: {curve_Z(p)}), J5 = {j5}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


# ------------------------------------------------------------------ round 22: the cubic in eleven variables
# LMFDB newform 35.3.c.b (weight 3, level 35, CM by Q(sqrt -35)): a_p at the primes to 97, read from its q-expansion
LMFDB_35_3_c_b = {2: 0, 3: 1, 5: -5, 7: 7, 11: -13, 13: -19, 17: 29, 19: 0, 23: 0, 29: 23, 31: 0, 37: 0, 41: 0, 43: 0,
                  47: -31, 53: 0, 59: 0, 61: 0, 67: 0, 71: 2, 73: -34, 79: -157, 83: 86, 89: 0, 97: 149}


def squarefree_part(n):
    s = 1
    for q, e in sympy.factorint(n).items():
        if e % 2:
            s *= q
    return s


def fundamental_disc(s):
    """the discriminant of Q(sqrt -s), s squarefree and positive"""
    return -s if (-s) % 4 == 1 else -4 * s


def _x11(p):
    low_priority()
    return p, t_values(p, (3, 5, 7, 9, 11))


def test22():
    """round 22 (PREREG.md): Q1 to Q4 -- the cubic eightfold X11 = {sum x = sum x^3 = 0} in eleven variables"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test22.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    P = primes(13, 401)
    E = [5, 7, 11]
    say("Round 22: the cubic in eleven variables (PREREG.md)")
    say(f"primes {P[0]}..{P[-1]} ({len(P)}), and the edge primes {E}")
    with Pool(4) as pool:
        res = dict(pool.map(_x11, P + E))
    say("X11 p t11 g (5|p) (105|p) a(p)   [t11 = p^4(132 + 110(5|p) + 10(105|p)) + 44p^3 a(p) + p^3 g(p)]")
    g, lower_ok, lmfdb_ok = {}, True, True
    for p in E + P:
        t = res[p]
        T = airy(p, t)
        a = T[7] / p ** 3
        if p not in E:
            lower_ok &= (T[1] == p and T[3] == 0 and T[5] == leg(5, p) * p ** 3 and a.denominator == 1
                         and abs(int(a)) == cf.cm35(p) and T[9] == leg(105, p) * p ** 5)
        if p in LMFDB_35_3_c_b:
            lmfdb_ok &= a == LMFDB_35_3_c_b[p]
        g[p] = T[11] / p ** 5
        say(f"X11 {p} {t[11]} {g[p]} {leg(5, p)} {leg(105, p)} {a}")
    say(f"instrument: T1 = p, T3 = 0, T5 = (5|p)p^3, |T7/p^3| = |c(p)|, T9 = (105|p)p^5 at every prime 13..401: {lower_ok}")
    say(f"read: X7's c(p) equals LMFDB 35.3.c.b's a_p at every prime to 97 here, the edges 5, 7, 11 included: {lmfdb_ok}")
    bad1 = [p for p in P if g[p].denominator != 1 or abs(g[p]) > 2 * p]
    say(f"Q1 p^5 divides T11 and |g(p)| <= 2p at every prime 13..401: {'HELD' if not bad1 else 'FAILED at ' + str(bad1)}")
    zeros = [p for p in P if g[p] == 0]
    svals = {p: squarefree_part(4 * p * p - int(g[p]) ** 2) for p in P if g[p] != 0 and not bad1}
    S = sorted(set(svals.values()))
    say(f"  g(p) = 0 at {len(zeros)} primes; squarefree parts of 4p^2 - g(p)^2 at the others: {S}")
    q2 = False
    if len(S) == 1 and not bad1:
        s = S[0]
        d = fundamental_disc(s)
        pattern = all((g[p] == 0) == (sympy.jacobi_symbol(d % p, p) == -1) for p in P if d % p)
        D = {p: 4 * p * p - int(g[p]) ** 2 for p in P if g[p] != 0}
        squares = all(D[p] % s == 0 and sympy.integer_nthroot(D[p] // s, 2)[1] for p in D)
        q2 = pattern and squares
        say(f"  one field: Q(sqrt -{s}), discriminant {d} = {sympy.factorint(abs(d))}; g = 0 exactly at its inert primes: "
            f"{pattern}; 4p^2 - g^2 = {s} v^2 at the others: {squares}")
    say(f"Q2 g has complex multiplication by one imaginary quadratic field: {'HELD' if q2 else 'FAILED'}")
    if q2:
        q3 = all(s % r == 0 for r in (5, 7, 11))
        say(f"Q3 5, 7 and 11 ramify in it (the nodes): {'HELD' if q3 else 'FAILED'}")
        say(f"Q3' it is Q(sqrt -1155) (the pattern 5, 7, 9 -> 3, 11): {'HELD' if s == 1155 else 'FAILED'}")
    else:
        say("Q3 and Q3': not scored, since Q2 failed")
    q4 = all(g[p].denominator == 1 and abs(g[p]) == p for p in E)
    for p in E:
        say(f"  edge p={p}: {len(cf.singular_sign_points(11, p))} nodes, g(p) = {g[p]}")
    say(f"Q4 |g(p)| = p at the edge primes 5, 7 and 11: {'HELD' if q4 else 'FAILED'}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


# ------------------------------------------------------------------ round 23: the cubic in thirteen variables
def _x13(p):
    low_priority()
    return p, t_values(p, (3, 5, 7, 9, 11, 13))


def fundamental_discs(limit):
    """every fundamental discriminant D with |D| <= limit, of either sign, and D = 1 (the trivial character)"""
    sf = bytearray([1]) * (limit + 1)
    for q in range(2, int(limit ** 0.5) + 1):
        sf[q * q::q * q] = bytearray(len(sf[q * q::q * q]))
    out = [1]
    for d in range(-limit, limit + 1):
        if d in (0, 1):
            continue
        if d % 4 == 1 and sf[abs(d)]:
            out.append(d)
        elif d % 4 == 0 and (d // 4) % 4 in (2, 3) and sf[abs(d // 4)]:
            out.append(d)
    return out


def kron(D, p):
    """the Kronecker symbol (D|p) for an odd prime p"""
    return leg(D, p) if D % p else 0


def split_tate_cm(P, U):
    """U[p] = chi(p) p^2 + h(p) with chi a quadratic character and h a weight-5 form with complex multiplication?
    At the primes inert in the CM field, h = 0 and p^2 divides U; at the split ones h is a unit mod p.  Returns
    (ok, D_chi, d_K, s, report lines)."""
    lines = []
    inert = [p for p in P if U[p] % p == 0]
    split = [p for p in P if U[p] % p]
    chi = {p: U[p] // (p * p) if U[p] % (p * p) == 0 else None for p in inert}
    lines.append(f"  p divides u at {len(inert)} primes; there u/p^2 = {sorted(set(chi.values()), key=str)}")
    if not all(v in (1, -1) for v in chi.values()):
        return False, None, None, None, lines
    # the CM field first: at each other prime one sign of chi(p) must leave 4p^4 - h^2 = s w^2, with one s for all
    opts = {}
    for p in split:
        opts[p] = {e: squarefree_part(4 * p ** 4 - (U[p] - e * p * p) ** 2)
                   for e in (1, -1) if abs(U[p] - e * p * p) < 2 * p * p}
    common = set.intersection(*(set(o.values()) for o in opts.values())) if opts else set()
    lines.append(f"  squarefree parts shared by every one of the {len(split)} other primes: {sorted(common)}")
    if len(common) != 1:
        return False, None, None, None, lines
    s = common.pop()
    for p in split:
        es = [e for e, v in opts[p].items() if v == s]
        chi[p] = es[0] if len(es) == 1 else None
    known = {p: v for p, v in chi.items() if v is not None}
    cands = [D for D in fundamental_discs(100000) if all(kron(D, p) == v for p, v in known.items())]
    lines.append(f"  quadratic characters matching chi at all {len(known)} primes where it is fixed, |D| <= 100000: "
                 f"{cands[:6]}")
    if len(cands) != 1:
        return False, None, None, s, lines
    Dchi = cands[0]
    h = {p: U[p] - kron(Dchi, p) * p * p for p in P}
    dK = fundamental_disc(s)
    pattern = all((p in inert) == (kron(dK, p) == -1) for p in P)
    squares = all((4 * p ** 4 - h[p] ** 2) % s == 0 and sympy.integer_nthroot((4 * p ** 4 - h[p] ** 2) // s, 2)[1]
                  for p in split)
    lines.append(f"  chi = ({Dchi}|p), {sympy.factorint(abs(Dchi)) if Dchi != 1 else 'trivial'}; K = Q(sqrt {dK}), "
                 f"{sympy.factorint(abs(dK))}; u = chi p^2 exactly at K's inert primes: {pattern}; "
                 f"4p^4 - h^2 = {s} w^2 at the others: {squares}")
    return pattern and squares, Dchi, dK, s, lines


def test23():
    """round 23 (PREREG.md): S1 to S7 -- the cubic in thirteen variables and its three-dimensional piece"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test23.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    P = primes(17, 401)
    E = [5, 7, 11, 13]
    say("Round 23: the cubic in thirteen variables (PREREG.md)")
    say(f"primes {P[0]}..{P[-1]} ({len(P)}), and the edge primes {E}")
    with Pool(4) as pool:
        res = dict(pool.map(_x13, P + E))
    say("X13 p t13 u (5|p) (105|p) a(p) g(p)   [u = T13/p^5]")
    u, T13, inst = {}, {}, True
    for p in E + P:
        t = res[p]
        T = airy(p, t)
        a, g = T[7] / p ** 3, T[11] / p ** 5
        if p not in E:
            inst &= (T[1] == p and T[3] == 0 and T[5] == leg(5, p) * p ** 3 and a.denominator == 1
                     and abs(int(a)) == cf.cm35(p) and T[9] == leg(105, p) * p ** 5 and g.denominator == 1
                     and (g == 0) == (leg(-1155, p) == -1))
            if g != 0:
                D_ = 4 * p * p - int(g) ** 2
                inst &= D_ % 1155 == 0 and sympy.integer_nthroot(D_ // 1155, 2)[1]
        if p in LMFDB_35_3_c_b:
            inst &= a == LMFDB_35_3_c_b[p]
        T13[p] = T[13]
        u[p] = T[13] / p ** 5
        say(f"X13 {p} {t[13]} {u[p]} {leg(5, p)} {leg(105, p)} {a} {g}")
    say(f"instrument: T1..T11 as found in rounds 19 to 22 at every prime 17..401: {inst}")
    bad1 = [p for p in P if u[p].denominator != 1 or abs(u[p]) > 3 * p * p]
    s1 = not bad1
    say(f"S1 T13 = p^5 u(p), u an integer with |u| <= 3p^2, at every prime 17..401: {'HELD' if s1 else 'FAILED at ' + str(bad1)}")
    s2 = s3 = s4 = s5 = s6 = s6b = s7 = False
    Dchi = dK = s = None
    if s1:
        s2, Dchi, dK, s, lines = split_tate_cm(P, {p: int(u[p]) for p in P})
        for line in lines:
            say(line)
    say(f"S2 the new piece splits into a twisted Tate class and a weight-5 form with complex multiplication: "
        f"{'HELD' if s2 else 'FAILED'}")
    if s2:
        def ram(D, q):
            return D % q == 0
        s3 = all(ram(Dchi, q) != ram(dK, q) for q in (5, 7, 11, 13))
        s4 = ram(Dchi, 3) != ram(dK, 3)
        s5 = Dchi > 0 and Dchi % 2 and dK % 2 and Dchi * dK == -15015
        s6 = Dchi == 5 and dK == -3003
        s6b = Dchi == 13 and dK == -1155
        say(f"S3 each of 5, 7, 11 and 13 ramifies in exactly one of chi and K (the nodes): {'HELD' if s3 else 'FAILED'}")
        say(f"S4 3 ramifies in exactly one of them (3 at its square): {'HELD' if s4 else 'FAILED'}")
        say(f"S5 chi is even and 2 ramifies in neither, so D_chi d_K = -15015: {'HELD' if s5 else 'FAILED'}")
        say(f"S6 chi = (5|p) and K = Q(sqrt -3003), the icosahedron's sqrt 5: {'HELD' if s6 else 'FAILED'}")
        say(f"S6' chi = (13|p) and K = Q(sqrt -1155), eleven's field kept: {'HELD' if s6b else 'FAILED'}")
        ok7 = True
        for q in E:
            v = T13[q]
            if ram(dK, q) and not ram(Dchi, q):
                good = v in (0, 2 * q ** 7, -2 * q ** 7)
            elif ram(Dchi, q) and not ram(dK, q):
                hq = v / q ** 5
                good = hq.denominator == 1 and abs(hq) <= 2 * q * q and (
                    (hq == 0) if kron(dK, q) == -1 else
                    ((4 * q ** 4 - int(hq) ** 2) % s == 0 and sympy.integer_nthroot((4 * q ** 4 - int(hq) ** 2) // s, 2)[1]))
            else:
                good = False
            ok7 &= good
            say(f"  edge q={q}: {len(cf.singular_sign_points(13, q))} nodes, T13 = {v} = q^5 * {v / q ** 5}; "
                f"ramified in {'K' if ram(dK, q) else ''}{'chi' if ram(Dchi, q) else ''}: {good}")
        s7 = ok7
        say(f"S7 at the edge primes 5, 7, 11 and 13, T13 is the trace on the unramified part: {'HELD' if s7 else 'FAILED'}")
    else:
        say("S3 to S7: not scored, since S2 failed")
        for q in E:
            say(f"  edge q={q}: T13 = {T13[q]} = q^5 * {T13[q] / q ** 5}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if mode == "verify":
        verify()
    elif mode == "test":
        test()
    elif mode == "test22":
        test22()
    elif mode == "test23":
        test23()
