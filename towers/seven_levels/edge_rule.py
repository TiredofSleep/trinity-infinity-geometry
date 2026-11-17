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

  python edge_rule.py          # the forced checks F1 to F5                      -> runs/edge_rule_verify.log
  python edge_rule.py test     # round 21: the cubics at their edge primes 5 and 7 -> edge_rule_test.log
  python edge_rule.py test22   # round 22: the cubic in eleven variables          -> edge_rule_test22.log
                               #   (four worker processes at below-normal priority)
  python edge_rule.py test23   # round 23: the cubic in thirteen variables        -> edge_rule_test23.log
  python edge_rule.py test24   # round 24: thirteen blind, and fifteen            -> edge_rule_test24.log
  python edge_rule.py verify25 # the forced checks F6 to F8 for round 25          -> runs/edge_rule_verify25.log
  python edge_rule.py test25   # round 25: seventeen, twenty-one and the prime 3  -> edge_rule_test25.log
  python edge_rule.py verify26 # the forced checks F9 to F12 for round 26         -> runs/edge_rule_verify26.log
  python edge_rule.py test26   # round 26: twenty-seven, and the square classes   -> edge_rule_test26.log
  python edge_rule.py verify27 # the forced checks F13 to F18 for round 27        -> runs/edge_rule_verify27.log
  python edge_rule.py test27   # round 27: eighty-one, and twenty-five's own determinant -> edge_rule_test27.log
  python edge_rule.py test28   # round 28: Theorem 8's determinants past 27, blind -> edge_rule_test28.log

numpy + sympy + coin_at_five.py (and ../../base/verify_one_rule.py for F6).  ASCII output.
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
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)   # run logs go to runs/ (ignored); the committed copy is the reference
    LOG = open(os.path.join(HERE, "runs", "edge_rule_verify.log"), "w", encoding="utf-8")
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


# ------------------------------------------------------------------ round 24: thirteen's symmetric square, blind; fifteen
# read after round 23: u(p) + (-15015|p) p^2 = s_p b_p^2, where s_p holds the prime l exactly when (D_l|p) = -1
SYM2_CHARS = {-1: -15015, 2: -715, 3: 5005, 5: -3003, 11: -35, 13: -1155}


def sym2_class(p):
    s = 1
    for l, D in SYM2_CHARS.items():
        if kron(D, p) == -1:
            s *= l
    return s


def sym2_ok(p, u):
    """does u = s_p b^2 - (-15015|p) p^2 for an integer b?"""
    if u.denominator != 1:
        return False
    v = int(u) + kron(-15015, p) * p * p
    s = sym2_class(p)
    return v % s == 0 and v // s >= 0 and sympy.integer_nthroot(v // s, 2)[1]


def _x15(p):
    low_priority()
    return p, t_values(p, (3, 5, 7, 9, 11, 13, 15))


def test24():
    """round 24 (PREREG.md): R1 (thirteen's symmetric square, blind) and F1 to F4 (the cubic in fifteen variables)"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test24.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    P13, P15, E = primes(409, 601), primes(17, 401), [5, 7, 11, 13]
    say("Round 24: thirteen's symmetric square at new primes, and the cubic in fifteen variables (PREREG.md)")
    say(f"X13 at {P13[0]}..{P13[-1]} ({len(P13)}); X15 at {P15[0]}..{P15[-1]} ({len(P15)}) and the edge primes {E}")
    with Pool(4) as pool:
        r13 = dict(pool.map(_x13, P13))
        r15 = dict(pool.map(_x15, P15 + E))
    bad = []
    for p in P13:
        u = airy(p, r13[p])[13] / p ** 5
        ok = u.denominator == 1 and abs(u) <= 3 * p * p and sym2_ok(p, u)
        say(f"X13 {p} u={u} s_p={sym2_class(p)} {ok}")
        if not ok:
            bad.append(p)
    say(f"R1 u(p) + (-15015|p)p^2 = s_p b^2 at every prime 409..601: {'HELD' if not bad else 'FAILED at ' + str(bad)}")
    say("X15 p t15 w   [w = T15/p^7]")
    w, T15, inst = {}, {}, True
    for p in E + P15:
        t = r15[p]
        T = airy(p, t)
        a, g = T[7] / p ** 3, T[11] / p ** 5
        if p not in E:
            inst &= (T[1] == p and T[3] == 0 and T[5] == leg(5, p) * p ** 3 and a.denominator == 1
                     and abs(int(a)) == cf.cm35(p) and T[9] == leg(105, p) * p ** 5 and g.denominator == 1
                     and (g == 0) == (leg(-1155, p) == -1) and sym2_ok(p, T[13] / p ** 5))
        T15[p] = T[15]
        w[p] = T[15] / p ** 7
        say(f"X15 {p} {t[15]} {w[p]}")
    say(f"instrument: T1..T13 as found in rounds 19 to 23 at every prime 17..401: {inst}")
    bad1 = [p for p in P15 if w[p].denominator != 1 or abs(w[p]) > 2 * p]
    say(f"F1 T15 = p^7 w(p), w an integer with |w| <= 2p, at every prime 17..401: {'HELD' if not bad1 else 'FAILED at ' + str(bad1)}")
    f2 = f3 = False
    if not bad1:
        zeros = [p for p in P15 if w[p] == 0]
        S = sorted({squarefree_part(4 * p * p - int(w[p]) ** 2) for p in P15 if w[p] != 0})
        say(f"  w(p) = 0 at {len(zeros)} primes; squarefree parts of 4p^2 - w^2 at the others: {S}")
        if len(S) == 1:
            s = S[0]
            d = fundamental_disc(s)
            pattern = all((w[p] == 0) == (kron(d, p) == -1) for p in P15 if d % p)
            D = {p: 4 * p * p - int(w[p]) ** 2 for p in P15 if w[p] != 0}
            squares = all(D[p] % s == 0 and sympy.integer_nthroot(D[p] // s, 2)[1] for p in D)
            f2 = pattern and squares
            say(f"  one field: Q(sqrt -{s}), discriminant {d} = {sympy.factorint(abs(d))}; w = 0 exactly at its inert "
                f"primes: {pattern}; 4p^2 - w^2 = {s} v^2 at the others: {squares}")
            f3 = f2 and d == -3003
    say(f"F2 w has complex multiplication by one imaginary quadratic field: {'HELD' if f2 else 'FAILED'}")
    say(f"F3 the field is Q(sqrt -3003): 7, 11, 13 by the nodes, 3 at its square, 5 kept out: {'HELD' if f3 else 'FAILED'}")
    ok4 = T15[5] == 0 and all(abs(T15[q]) == q ** 8 for q in (7, 11, 13))
    for q in E:
        say(f"  edge q={q}: {len(cf.singular_sign_points(15, q))} nodes, T15 = {T15[q]} = q^8 * {T15[q] / q ** 8}")
    say(f"F4 T15(5) = 0 and |T15(q)| = q^8 at q = 7, 11, 13: {'HELD' if ok4 else 'FAILED'}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


# ------------------------------------------------------------------ round 25: seventeen, twenty-one, and the prime 3
#   "1 and 3, seventeen first"  -- the author, 15 November 2026
#   (1: register seventeen.  3: the reading at 13 -- its piece is both faces at once, as 13 is the icosahedron with its
#   centre.)
def signed(l):
    """the signed prime l* = (-1)^((l - 1)/2) l: Q(sqrt l*) is the quadratic field ramified at l alone"""
    return l if l % 4 == 1 else -l


def val(n, l):
    v = 0
    while n % l == 0:
        n //= l
        v += 1
    return v


def thin_nodes(k, l):
    """the ramified dimensions of V_k at l by the node reading, refined by the critical values (F7).  A node at a sign
    vector with sum j is thin (the total space is regular there, and inertia turns its vanishing cycle over) exactly when
    the critical value has odd valuation: v_l(j) for l >= 5, and v_3(j) - 1 in the good model at 3.  Up to k = 23 this
    is ramified_dim(k, l) for l >= 5; for 3 it counts the odd multiples of 9 (3 at its square)."""
    shift = 1 if l == 3 else 0
    return sum(1 for j in range(1, k + 1, 2) if j % l == 0 and (val(j, l) - shift) % 2 == 1)


def det_from_nodes(k):
    """the parity rule: V_k's determinant character is ramified exactly where V_k has an odd number of ramified
    dimensions (each thin node turns one vanishing cycle over, so inertia acts with determinant (-1)^r).  The character
    is (D|p), with D the product of the signed primes there."""
    D = 1
    for l in primes(3, k):
        if thin_nodes(k, l) % 2:
            D *= signed(l)
    return D


# the determinants' characters already read: V1 = p; V5 = (5|p)p^3 and V9 = (105|p)p^5 are lines; the forms at 7, 11
# and 15 have the characters of their CM fields (LMFDB 35.3.c at 7; at 11 and 15 because 4p^2 - a_p^2 = s v^2 > 0 at the
# split primes forces det = +p^2 there, and an odd character equal to 1 at every split prime is the field's); 13's
# symmetric square has (-15015|p) (round 24, R1)
MEASURED_DET = {1: 1, 5: 5, 7: -35, 9: 105, 11: -1155, 13: -15015, 15: -3003}


def nodes_count(n, l):
    """the nodes of X_n mod l: projective sign vectors whose sum j is a multiple of l (l >= 5), or of 9 in the good
    model at 3 (F7)"""
    step = 9 if l == 3 else l
    return sum(math.comb(n, (n + j) // 2) for j in range(1, n + 1, 2) if j % step == 0)


def e3_of(x, m=3):
    e1 = e2 = e3 = 0
    for xi in x:
        e3 = (e3 + e2 * xi) % m
        e2 = (e2 + e1 * xi) % m
        e1 = (e1 + xi) % m
    return e1, e2, e3


def count_e3(n):
    """N'_n = #{x in F_3^n : e1(x) = e3(x) = 0}, the cone over the good model at 3, by the numbers a, b of coordinates
    equal to 1 and to -1: then e1 = a - b, and e3 is the t^3 coefficient of (1 + t)^a (1 - t)^b"""
    N = 0
    for a in range(n + 1):
        for b in range(n + 1 - a):
            if (a - b) % 3:
                continue
            e3 = sum(math.comb(a, i) * math.comb(b, 3 - i) * (-1) ** (3 - i) for i in range(4))
            if e3 % 3 == 0:
                N += math.factorial(n) // (math.factorial(a) * math.factorial(b) * math.factorial(n - a - b))
    return N


def e3_brute(n):
    return sum(1 for x in itertools.product(range(3), repeat=n) if e3_of(x)[0] == 0 and e3_of(x)[2] == 0)


def normalize3(x):
    lead = next(v for v in x if v % 3)
    inv = 1 if lead % 3 == 1 else 2
    return tuple((inv * v) % 3 for v in x)


def singular_e3(n):
    """the singular points of {e1 = e3 = 0} in P^(n-1) over F_3, by brute force: grad e3 = (e2 + x_i^2)_i on e1 = 0,
    singular when it is a multiple of grad e1 = (1, ..., 1)"""
    pts = set()
    for x in itertools.product(range(3), repeat=n):
        if not any(x):
            continue
        e1, e2, e3 = e3_of(x)
        if e1 or e3:
            continue
        if len({(e2 + v * v) % 3 for v in x}) == 1:
            pts.add(normalize3(x))
    return pts


def rank_mod3(M):
    M = [[v % 3 for v in row] for row in M]
    r, cols = 0, len(M[0]) if M else 0
    for c in range(cols):
        piv = next((i for i in range(r, len(M)) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1 if M[r][c] == 1 else 2
        M[r] = [(inv * v) % 3 for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % 3 for a, b in zip(M[i], M[r])]
        r += 1
    return r


def hessian_rank_e3(n, j):
    """the Hessian of e3 on the hyperplane e1 = 0 at the node eps = (+1 x (n+j)/2, -1 x (n-j)/2), in the chart x_1 = 1:
    d^2 e3/dx_i dx_j = e1 - x_i - x_j = -(eps_i + eps_j) mod 3 (i != j), 0 on the diagonal, on sum y = 0"""
    eps = [1] * ((n + j) // 2) + [-1] * ((n - j) // 2)
    e = eps[1:]
    m = len(e)
    H = [[0 if a == b else -(e[a] + e[b]) for b in range(m)] for a in range(m)]
    B = [[(1 if r == c else 0) - (1 if r == m - 1 else 0) for c in range(m - 1)] for r in range(m)]  # e_c - e_last
    Q = [[sum(B[r][a] * H[r][s] * B[s][b] for r in range(m) for s in range(m)) for b in range(m - 1)] for a in range(m - 1)]
    return rank_mod3(Q), m - 1


def critical_value(j, model):
    """the critical value at the node of sum j (chart x_1 = 1): j(j - 2)/(j - 1)^2 for sum x^3, and a third of it for e3"""
    cv = Fraction(j * (j - 2), (j - 1) ** 2)
    return cv / 3 if model == "e3" else cv


def critical_value_direct(n, j, model):
    """e3 or p3 at the exact critical point (1, c eps') of the chart, c = -1/(j - 1), over Q"""
    eps = [1] * ((n + j) // 2) + [-1] * ((n - j) // 2)
    c = Fraction(-1, j - 1)
    x = [Fraction(1)] + [c * e for e in eps[1:]]
    if model == "p3":
        return sum(v ** 3 for v in x)
    e1 = e2 = e3 = Fraction(0)
    for v in x:
        e3 += e2 * v
        e2 += e1 * v
        e1 += v
    return e3


def fval(q, l):
    return val(q.numerator, l) - val(q.denominator, l)


def base_rule(ns, kmax=22):
    """the base's rule (../../base/verify_one_rule.py): the most symmetric arrangement of n points in 3-space, not all
    on a line, by searching every union of orbits of every point group -- the polyhedral groups and the axial families
    up to a kmax-fold axis (a ring off the axis has at least k points, so kmax >= n is enough).  Returns, for each n, the
    largest order, the winning groups with their orbit sizes, and whether every winner keeps an axis (an axial family:
    C, S or D), for the rule itself and for its variant that fills three dimensions."""
    sys.path.insert(0, os.path.join(HERE, "..", "..", "base"))
    import verify_one_rule as vor
    groups = vor.point_groups(kmax=kmax)
    orders = {g: len(G) for g, G in groups.items()}
    types = {g: vor.orbit_types(G) for g, G in groups.items()}
    out = {}
    for n in ns:
        res = {}
        for variant in ("rule", "solid"):
            top, win = 0, []
            for g, ty in types.items():
                if orders[g] < top:
                    continue
                for P, desc in vor.unions(ty, n):
                    if len(P) != n:
                        continue
                    r = vor.affine_rank(P)
                    if (variant == "rule" and r < 2) or (variant == "solid" and r < 3):
                        continue
                    if orders[g] > top:
                        top, win = orders[g], []
                    centre, chosen = desc
                    win.append((g, ("centre + " if centre else "") + "+".join(str(len(ty[i])) for i, m in chosen
                                                                                for _ in range(m)), P))
            full = {vor.sym_order(P) for _, _, P in win[:3]}
            res[variant] = (top, sorted({(g, d) for g, d, _ in win}), full, all(g[0] in "CSD" for g, _, _ in win))
        out[n] = res
    return out


def verify25():
    """the forced checks F6 to F8 behind round 25's registration; none of them counts X17 or X21, or the good model at 3"""
    global LOG
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)   # run logs go to runs/ (ignored); the committed copy is the reference
    LOG = open(os.path.join(HERE, "runs", "edge_rule_verify25.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("edge_rule.py verify25 -- the forced checks for round 25 (seventeen, twenty-one, the prime 3)")

    # F6: the base's rule at 13, 17 and 21, and whether its winner keeps an axis
    B = base_rule((13, 17, 21))
    ok = True
    for n, res in B.items():
        for variant, (top, win, full, axial) in res.items():
            say(f"  n = {n} ({variant}): largest order {top}, winners {win}, full symmetry {sorted(full)}, "
                f"{'keeps an axis' if axial else 'no axis kept by all its symmetries'}")
    ok &= B[13]["rule"][0] == 120 and not B[13]["rule"][3] and {g for g, _ in B[13]["rule"][1]} == {"Ih"}
    ok &= B[17]["rule"][0] == 68 and B[17]["rule"][3] and B[17]["rule"][2] == {68}
    ok &= B[21]["rule"][0] == 120 and not B[21]["rule"][3] and {g for g, _ in B[21]["rule"][1]} == {"Ih"}
    ok &= B[17]["solid"][3] and not B[13]["solid"][3] and not B[21]["solid"][3]
    check("F6. the base's rule: 13 -> the icosahedron with its centre (Ih, 120, no axis), 17 -> the regular 17-gon "
          "(68, one axis), 21 -> the dodecahedron with its centre (Ih, 120, no axis); in space (the variant filling three "
          "dimensions) 13 and 21 are the same, and 17's winner still keeps an axis", ok)

    # F7: the good model at 3
    ok, rows = True, []
    for n in (5, 7, 9, 11):
        S = singular_e3(n)
        want = set()  # every sign vector (entries 1 and -1 = 2) whose sum is a multiple of 9, up to sign
        for j in range(1, n + 1, 2):
            if j % 9 == 0:
                for plus in itertools.combinations(range(n), (n + j) // 2):
                    want.add(normalize3(tuple(1 if i in plus else 2 for i in range(n))))
        ok &= S == want
        rows.append(f"n={n}:{len(S)}")
    check("F7a. over Z_3, sum x^3 = 3 e3 on sum x = 0, so X_n = {e1 = e3 = 0}. Mod 3 its singular points are exactly the "
          "sign vectors whose sum is a multiple of 9 (none for n <= 7; n = 9: the centre alone) -- by brute force over "
          "F_3^n, n = 5, 7, 9, 11", ok, " ".join(rows))
    ok, rows = True, []
    for n in range(9, 28, 2):
        for j in (9, 27):
            if j <= n:
                r, d = hessian_rank_e3(n, j)
                ok &= r == d
                rows.append(f"n={n},j={j}:{r}/{d}")
    check("F7b. each of those nodes is ordinary: the Hessian on the tangent hyperplane has full rank mod 3 "
          "(n = 9..27, sums 9 and 27)", ok, " ".join(rows[:6]) + " ...")
    ok, rows = True, []
    for n, j in ((9, 9), (11, 9), (17, 9), (21, 9), (27, 27)):
        d = critical_value_direct(n, j, "e3")
        ok &= d == critical_value(j, "e3")
        rows.append(f"n={n},j={j}:{d}")
    for n, j in ((5, 5), (15, 15), (17, 5), (25, 25), (21, 7)):
        d = critical_value_direct(n, j, "p3")
        ok &= d == critical_value(j, "p3")
    v9, v27 = fval(critical_value(9, "e3"), 3), fval(critical_value(27, "e3"), 3)
    v5, v15, v25, v49 = (fval(critical_value(j, "p3"), l) for j, l in ((5, 5), (15, 5), (25, 5), (49, 7)))
    ok &= (v9, v27, v5, v15, v25, v49) == (1, 2, 1, 1, 2, 2)
    check("F7c. the critical values: j(j - 2)/(j - 1)^2 for sum x^3, a third of it for e3 (checked at the exact critical "
          "points). Their valuations: at 3, v_3(j) - 1 -- 1 at sum 9 (thin: the total space is regular), 2 at 27 "
          "(thick); at l >= 5, v_l(j) -- 1 at 5 and 15, 2 at 25 and 49", ok,
          f"{'; '.join(rows)}; v3: 9->{v9}, 27->{v27}; v5: 5->{v5}, 15->{v15}, 25->{v25}; v7: 49->{v49}")

    # F8: the bookkeeping for 17 and 21, and the parity rule on the characters already read
    ok, rows = True, []
    v = {k: len(classical_hodge(k)) for k in range(1, 22, 2)}
    for n in (17, 21):
        ok &= sum(ballot(n, k) * v[k] for k in range(1, n + 1, 2)) == betti_prim(n)
        rows.append(f"V{n}: dim {v[n]}, types {classical_hodge(n)}, b_prim {betti_prim(n)}")
        for l in [3] + primes(5, n):
            nodes = nodes_count(n, l)
            lower = sum(ballot(n, k) * thin_nodes(k, l) for k in range(1, n, 2))
            ok &= nodes - lower == thin_nodes(n, l)
            rows.append(f"n={n},l={l}: {nodes} nodes, lower {lower}, V{n} {nodes - lower}")
    check("F8a. X17 and X21: the lower pieces fill all but three dimensions (V17 and V21 have three each, of types "
          "(7,11), (9,9), (11,7) and (9,13), (11,11), (13,9)), and all but r nodes at each prime: at 17, r = 1 at 3, 7, "
          "11, 13, 17 and r = 2 at 5; at 21, r = 1 at 3, 11, 13, 17, 19 and r = 2 at 5 and 7", ok)
    for row in rows:
        say("  " + row)
    ok = all(det_from_nodes(k) == D for k, D in MEASURED_DET.items())
    check("F8b. the parity rule reproduces every determinant already read: " +
          ", ".join(f"k={k}: {det_from_nodes(k)}" for k in MEASURED_DET), ok)
    D17, D21 = det_from_nodes(17), det_from_nodes(21)
    check(f"F8c. its predictions: V17's determinant (D|p) with D = {D17} = {sympy.factorint(abs(D17))} (sign -); "
          f"V21's with D = {D21} = {sympy.factorint(abs(D21))} (sign -)", (D17, D21) == (-51051, -138567))
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()


def cone_counts_checked(p, ns):
    """cf.cone_counts with an overflow guard: each partial count is checked to stay inside int64 (no negative entry,
    and the counts sum to p^k exactly)"""
    x = np.arange(p, dtype=np.int64)
    x3 = x ** 3 % p
    c = {1: np.zeros((p, p), dtype=np.int64)}
    c[1][x, x3] = 1
    top = max((n + 1) // 2 for n in ns)
    for k in range(2, top + 1):
        acc = np.zeros((p, p), dtype=np.int64)
        for s in range(p):
            acc += np.roll(c[k - 1], (s, int(x3[s])), axis=(0, 1))
        if acc.min() < 0 or int(acc.astype(object).sum()) != p ** k:
            raise OverflowError(f"cone counts overflow at p = {p}, k = {k}")
        c[k] = acc
    neg = (-x) % p
    out = {}
    for n in ns:
        j = n // 2
        out[n] = int((c[j].astype(object) * c[n - j][np.ix_(neg, neg)].astype(object)).sum())
    return out


def t_values_checked(p, ns):
    N = cone_counts_checked(p, tuple(n for n in ns if n >= 3))
    N[1] = 1
    return {n: (Fraction(N[n]) - Fraction(p) ** (n - 2)) / (p - 1) for n in sorted(set(ns) | {1})}


def _x17(p):
    low_priority()
    return p, t_values_checked(p, tuple(range(3, 18, 2)))


def _x21(p):
    low_priority()
    return p, t_values_checked(p, tuple(range(3, 22, 2)))


def lower_pieces_ok(p, T):
    """T1 to T15 as found in rounds 19 to 24, at a good prime p >= 17"""
    a, g, w = T[7] / p ** 3, T[11] / p ** 5, T[15] / p ** 7
    ok = (T[1] == p and T[3] == 0 and T[5] == leg(5, p) * p ** 3 and a.denominator == 1 and abs(int(a)) == cf.cm35(p)
          and T[9] == leg(105, p) * p ** 5 and g.denominator == 1 and (g == 0) == (leg(-1155, p) == -1)
          and sym2_ok(p, T[13] / p ** 5) and w.denominator == 1 and (w == 0) == (leg(-3003, p) == -1))
    for f, s in ((g, 1155), (w, 3003)):
        if ok and f != 0:
            D_ = 4 * p * p - int(f) ** 2
            ok = D_ % s == 0 and sympy.integer_nthroot(D_ // s, 2)[1]
    if ok and p in LMFDB_35_3_c_b:
        ok = a == LMFDB_35_3_c_b[p]
    return ok


def det_sign_test(P, u, D):
    """an orthogonal three-dimensional piece has the eigenvalue det(p) p^2 (normalized), and the other two add up to at
    most 2p^2 in size; so wherever |u| > p^2 the sign of u is the determinant's character"""
    tested = [p for p in P if abs(u[p]) > p * p]
    bad = [p for p in tested if (1 if u[p] > 0 else -1) != kron(D, p)]
    return tested, bad


def fused_signature(P, u, D, modulus):
    """a twisted symmetric square: u + det(p) p^2 = chi(p) a_p^2 = +-s b^2, with s a squarefree divisor of the modulus"""
    return [p for p in P if (int(u[p]) + kron(D, p) * p * p) and modulus % squarefree_part(abs(int(u[p]) + kron(D, p) * p * p))]


def test25():
    """round 25 (PREREG.md): Z1 to Z5 (seventeen and the prime 3) and D1 to D3 (twenty-one)"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test25.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    P17, E17, P21 = primes(19, 401), [5, 7, 11, 13, 17], primes(23, 113)
    say("Round 25: seventeen, twenty-one, and the prime 3 (PREREG.md)")
    say(f"X17 at {P17[0]}..{P17[-1]} ({len(P17)}) and the edge primes {E17}; X21 at {P21[0]}..{P21[-1]} ({len(P21)})")
    with Pool(4) as pool:
        r17 = dict(pool.map(_x17, P17 + E17))
        r21 = dict(pool.map(_x21, P21))

    # ---- seventeen
    D17 = det_from_nodes(17)
    u, T17, inst = {}, {}, True
    say(f"X17 p t17 u ({D17}|p)   [u = T17/p^7]")
    for p in E17 + P17:
        T = airy(p, r17[p])
        if p not in E17:
            inst &= lower_pieces_ok(p, T)
        T17[p] = T[17]
        u[p] = T[17] / p ** 7
        say(f"X17 {p} {r17[p][17]} {u[p]} {kron(D17, p)}")
    say(f"instrument: T1..T15 as found in rounds 19 to 24 at every prime 19..401: {inst}")
    bad1 = [p for p in P17 if u[p].denominator != 1 or abs(u[p]) > 3 * p * p]
    z1 = not bad1
    say(f"Z1 T17 = p^7 u(p), u an integer with |u| <= 3p^2, at every prime 19..401: "
        f"{'HELD' if z1 else 'FAILED at ' + str(bad1)}")
    tested, bad2 = det_sign_test(P17, u, D17)
    alt = det_sign_test(P17, u, 17017)[1]
    z2 = z1 and not bad2 and len(tested) >= 10
    say(f"  |u| > p^2 at {len(tested)} primes; sign(u) = ({D17}|p) fails at {bad2}; with 3 left out, (17017|p) fails at "
        f"{len(alt)} of them")
    say(f"Z2 the determinant's character is ({D17}|p): 3 once (at 9), 5 twice (5 and 15), 7, 11, 13 and 17 once: "
        f"{'HELD' if z2 else 'FAILED'}")
    divides = [p for p in P17 if z1 and int(u[p]) % p == 0]
    say(f"  p divides u at {len(divides)} of the {len(P17)} primes: {divides}")
    z3, Dchi, dK, s, lines = split_tate_cm(P17, {p: int(u[p]) for p in P17}) if z1 else (False, None, None, None, [])
    for line in lines:
        say(line)
    say(f"Z3 (the reading at 13, made exact) V17 keeps a line -- a twisted Tate class beside a weight-5 form with complex "
        f"multiplication -- as the regular 17-gon keeps its axis: {'HELD' if z3 else 'FAILED'}")
    if z3:
        say(f"  G1 chi = (17|p) and K = Q(sqrt -3003): {'HELD' if (Dchi == 17 and dK == -3003) else 'FAILED'}")
    badf = fused_signature(P17, u, D17, 510510) if z1 else P17
    z3b = z1 and not z3 and len(divides) <= 3 and not badf
    say(f"  u + ({D17}|p)p^2 = +-s b^2 with s dividing 510510 = 2.3.5.7.11.13.17: fails at {badf}")
    say(f"Z3' (the same shape as 13) V17 keeps no line, and it is a twisted symmetric square: "
        f"{'HELD' if z3b else 'FAILED'}")
    ok4 = T17[5] in (5 ** 9, -5 ** 9)
    for q in (7, 11, 13, 17):
        v4 = T17[q] / q ** 7
        ok4 &= v4.denominator == 1 and abs(v4) <= 2 * q * q
    for q in E17:
        say(f"  edge q={q}: {nodes_count(17, q)} nodes, T17 = {T17[q]} = q^7 * {T17[q] / q ** 7}")
    say(f"Z4 T17(5) = +-5^9 (one line survives), and at 7, 11, 13 and 17 a plane survives: q^7 divides T17(q) and "
        f"|T17(q)| <= 2q^9: {'HELD' if ok4 else 'FAILED'}")

    # ---- the prime 3, in the good model
    brute = {n: (count_e3(n), e3_brute(n)) for n in (3, 5, 7, 9)}
    brute_ok = all(a == b for a, b in brute.values())
    say(f"instrument at 3: the count of e1 = e3 = 0 equals brute force over F_3^n for n = 3, 5, 7, 9: {brute_ok}")
    N3 = {n: count_e3(n) for n in range(3, 22, 2)}
    N3[1] = 1
    t3 = {n: (Fraction(N3[n]) - Fraction(3) ** (n - 2)) / 2 for n in range(1, 22, 2)}
    T3 = airy(3, t3)
    for k in range(1, 22, 2):
        say(f"  at 3: N'_{k} = {N3[k]}, T{k} = {T3[k]}, {len(classical_hodge(k))} dims, "
            f"{thin_nodes(k, 3)} ramified by 3 at its square")
    a3 = LMFDB_35_3_c_b[3]
    z5a = brute_ok and T3[1] == 3 and T3[3] == 0 and T3[5] == -27 and T3[7] == 27 * a3
    z5b = brute_ok and T3[9] == 0
    q13, q17 = T3[13] / 3 ** 5, T3[17] / 3 ** 7
    z5c = (brute_ok and abs(T3[11]) == 3 ** 6 and abs(T3[15]) == 3 ** 8 and q13.denominator == 1 and abs(q13) <= 18
           and q17.denominator == 1 and abs(q17) <= 18)
    say(f"Z5a below 9, 3 does not enter: T1 = 3, T3 = 0, T5 = (5|3)3^3 = -27, T7 = 3^3 a_3(35.3.c.b) = {27 * a3}: "
        f"{'HELD' if z5a else 'FAILED'}")
    say(f"Z5b 3 enters at 9: V9's line is ramified, T9 = 0: {'HELD' if z5b else 'FAILED'}")
    say(f"Z5c from 9 on, one dimension at a time: |T11| = 3^6 and |T15| = 3^8 (a line survives in each CM plane), and a "
        f"plane survives in V13 and V17 (3^5 | T13, |T13| <= 2.3^7; 3^7 | T17, |T17| <= 2.3^9): "
        f"{'HELD' if z5c else 'FAILED'}")

    # ---- twenty-one
    D21 = det_from_nodes(21)
    u21, inst21 = {}, True
    say(f"X21 p u21 ({D21}|p) T19/p^7   [u21 = T21/p^9]")
    for p in P21:
        T = airy(p, r21[p])
        inst21 &= lower_pieces_ok(p, T)
        u21[p] = T[21] / p ** 9
        say(f"X21 {p} {u21[p]} {kron(D21, p)} {T[19] / p ** 7}")
    say(f"instrument: T1..T15 as found in rounds 19 to 24 at every prime 23..113: {inst21}")
    bad = [p for p in P21 if u21[p].denominator != 1 or abs(u21[p]) > 3 * p * p]
    d1 = not bad
    say(f"D1 T21 = p^9 u21(p), u21 an integer with |u21| <= 3p^2, at every prime 23..113: "
        f"{'HELD' if d1 else 'FAILED at ' + str(bad)}")
    tested, bad2 = det_sign_test(P21, u21, D21)
    d2 = d1 and not bad2 and len(tested) >= 5
    say(f"  |u21| > p^2 at {len(tested)} primes; sign(u21) = ({D21}|p) fails at {bad2}")
    say(f"D2 the determinant's character is ({D21}|p): 3 once (at 9, not at 21), 5 and 7 twice, 11, 13, 17, 19 once: "
        f"{'HELD' if d2 else 'FAILED'}")
    div21 = [p for p in P21 if d1 and int(u21[p]) % p == 0]
    sp21 = split_tate_cm(P21, {p: int(u21[p]) for p in P21})[0] if d1 else True
    d3 = d1 and not sp21 and len(div21) <= 2
    say(f"  p divides u21 at {len(div21)} of the {len(P21)} primes: {div21}")
    say(f"D3 (the reading) V21 keeps no line, as the dodecahedron with its centre keeps no axis: "
        f"{'HELD' if d3 else 'FAILED'}")
    badf21 = fused_signature(P21, u21, D21, 9699690) if d1 else P21
    say(f"  u21 + ({D21}|p)p^2 = +-s b^2 with s dividing 9699690 = 2.3.5.7.11.13.17.19: fails at {badf21} (read)")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


# ------------------------------------------------------------------ round 26: twenty-seven first, and the classes blind
#   "2 and 3, 27 first"  -- the author, 15 November 2026
#   (2: test the sharpened rule at 25 and 27, three coins of 3, with 27 first.  3: seventeen's six characters, blind.)
#
# A faster exact counter.  N_n(F_q) = q^-2 sum over (s, t) in F_q^2 of S(s, t)^n, where S(s, t) = sum_x psi(s x + t x^3)
# and psi(z) = w^Tr(z).  For s != 0, S(s, t) = S(1, t/s^3), so only s = 0 and s = 1 are needed.  The sums are algebraic
# integers in Q(zeta_p).  They are computed mod primes l = 1 (mod p), where w is a primitive p-th root of unity, and N_n
# is joined back by the Chinese remainder theorem.  q = p, or q = p^2 for the squares of Frobenius.
from sympy.ntheory.modular import crt  # noqa: E402


def moduli_for(p, bits):
    """primes l = 1 (mod p) just above 2^30, enough that their product has more than `bits` bits"""
    out, prod = [], 1
    m = (1 << 30) // p + 1
    while prod.bit_length() <= bits:
        l = 1 + p * m
        if l >= 1 << 31:
            raise ValueError(f"not enough moduli below 2^31 for p = {p}")
        if sympy.isprime(l):
            out.append(l)
            prod *= l
        m += 1
    return out


def root_of_unity(p, l):
    for g in range(2, 1000):
        w = pow(g, (l - 1) // p, l)
        if w != 1:
            return w
    raise ValueError("no p-th root of unity found")


def field_data(p, r):
    """F_q, q = p^r (r = 1 or 2). For r = 2, x = a + b alpha with alpha^2 = nu (a non-square), indexed a + p b.
    Returns Tr(x) and the linear forms that give Tr(t x^3) on the coordinates of t."""
    if r == 1:
        x = np.arange(p, dtype=np.int64)
        return x, [x ** 3 % p]
    nu = nonsquare(p)
    idx = np.arange(p * p, dtype=np.int64)
    a, b = idx % p, idx // p
    ca = (a ** 3 + 3 * a * b * b * nu) % p
    cb = (3 * a * a * b + nu * b ** 3) % p
    return (2 * a) % p, [(2 * ca) % p, (2 * nu * cb) % p]


def exp_sums(p, r, mods):
    """S(0, t) and S(1, t) for every t in F_q, as residues mod each l in mods"""
    trx, L = field_data(p, r)
    q = p ** r
    pw = []
    for l in mods:
        w = root_of_unity(p, l)
        pw.append(np.array([pow(w, k, l) for k in range(p)], dtype=np.int64))
    S0 = [np.zeros(q, dtype=np.int64) for _ in mods]
    S1 = [np.zeros(q, dtype=np.int64) for _ in mods]
    ta = np.arange(p, dtype=np.int64)
    for tb in range(p if r == 2 else 1):
        base = ta[:, None] * L[0][None, :]
        if r == 2:
            base = base + tb * L[1][None, :]
        M0 = base % p
        M1 = (base + trx[None, :]) % p
        rows = slice(tb * p, (tb + 1) * p)
        for i, l in enumerate(mods):
            S0[i][rows] = pw[i][M0].sum(axis=1) % l
            S1[i][rows] = pw[i][M1].sum(axis=1) % l
    return S0, S1


def counts_crt(p, r, ns):
    """N_n(F_q) mod M for each odd n in ns, with M large enough to recover N_n - q^(n-2) exactly"""
    q = p ** r
    nmax = max(ns)
    bound = 4 * (q - 1) * betti_prim(nmax) * q ** ((nmax - 3) // 2)
    mods = moduli_for(p, bound.bit_length() + 1)
    S0, S1 = exp_sums(p, r, mods)
    res = {n: [] for n in ns}
    for i, l in enumerate(mods):
        c0, c1 = S0[i] % l, S1[i] % l
        s0, s1 = c0 * c0 % l, c1 * c1 % l
        inv = pow(q * q % l, l - 2, l)
        for n in range(1, nmax + 1, 2):
            if n in res:
                res[n].append((int(c0.sum()) + (q - 1) * int(c1.sum())) % l * inv % l)
            c0, c1 = c0 * s0 % l, c1 * s1 % l
    M = math.prod(mods)
    return {n: int(crt(mods, res[n])[0]) for n in ns}, M, bound


def t_values_crt(p, r, ns):
    """t_n = #X_n(F_q) - (1 + q + ... + q^(n-3)) exactly, q = p^r, for odd n (t_1 = 1/q, as in t_values)"""
    q = p ** r
    ns3 = tuple(n for n in ns if n >= 3)
    N, M, bound = counts_crt(p, r, ns3)
    t = {1: Fraction(1, q)}
    for n in ns3:
        v = (N[n] - q ** (n - 2)) % M
        if v > M // 2:
            v -= M
        if abs(v) > bound or v % (q - 1):
            raise ArithmeticError(f"the counter's self-check failed at p = {p}, r = {r}, n = {n}")
        t[n] = Fraction(v // (q - 1))
    return t


def cone_counts_fq(p, ns):
    """N_n(F_(p^2)) by convolving the measure of (x, x^3) on F_(p^2)^2, for small p: the brute-force check"""
    nu = nonsquare(p)
    pts = []
    for b in range(p):
        for a in range(p):
            pts.append((a, b, (a ** 3 + 3 * a * b * b * nu) % p, (3 * a * a * b + nu * b ** 3) % p))
    c = np.zeros((p, p, p, p), dtype=np.int64)
    c[0, 0, 0, 0] = 1
    out = {}
    for n in range(1, max(ns) + 1):
        acc = np.zeros_like(c)
        for sh in pts:
            acc += np.roll(c, sh, axis=(0, 1, 2, 3))
        c = acc
        if n in ns:
            out[n] = int(c[0, 0, 0, 0])
    return out


def hodge_sign(k):
    """complex conjugation swaps H^(a,b) and H^(b,a): det F_inf = (-1)^(pairs), times its sign on a middle class (a,a)"""
    types = classical_hodge(k)
    return (-1) ** sum(1 for a, b in types if a < b), any(a == b for a, b in types)


def nodes_by_kind(n, l):
    """the nodes of X_n at l, split into thin (odd valuation of the critical value: they ramify) and thick"""
    shift = 1 if l == 3 else 0
    step = 9 if l == 3 else l
    thin = thick = 0
    for j in range(1, n + 1, 2):
        if j % step == 0:
            c = math.comb(n, (n + j) // 2)
            if (val(j, l) - shift) % 2:
                thin += c
            else:
                thick += c
    return thin, thick


def naive_nodes(k, l):
    """the rule before the critical values: every node ramifies (odd multiples of l, or of 9 at 3)"""
    step = 9 if l == 3 else l
    return sum(1 for j in range(1, k + 1, 2) if j % step == 0)


def det_with(k, rule3, rule5):
    """the parity rule's determinant at k, with 3 and 5 counted by the thin rule or the naive one"""
    D = 1
    for l in primes(3, k):
        if l == 3:
            r = thin_nodes(k, 3) if rule3 == "thin" else naive_nodes(k, 3)
        elif l == 5:
            r = thin_nodes(k, 5) if rule5 == "thin" else naive_nodes(k, 5)
        else:
            r = thin_nodes(k, l)
        if r % 2:
            D *= signed(l)
    return D


def verify26():
    """the forced checks F9 to F12 behind round 26, and the new counter's validation. Nothing here counts X23, X25 or
    X27, or any cubic in 13 or more variables over a field of p^2 elements."""
    global LOG
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)   # run logs go to runs/ (ignored); the committed copy is the reference
    LOG = open(os.path.join(HERE, "runs", "edge_rule_verify26.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("edge_rule.py verify26 -- the forced checks for round 26 (twenty-seven, the 4-dimensional pieces)")

    # F9: the infinite place
    ok, rows = True, []
    for k, D in MEASURED_DET.items():
        sgn, mid = hodge_sign(k)
        ok &= (1 if D > 0 else -1) == sgn
        rows.append(f"k={k}:{'+' if sgn > 0 else '-'}{'m' if mid else ''}")
    check("F9a. complex conjugation: det F_inf = (-1)^(Hodge pairs) times +1 on the middle class matches the sign of every "
          "determinant already read (k = 1 to 15; m marks a middle class)", ok, " ".join(rows))
    cand = {(a, b): det_with(27, a, b) for a in ("thin", "naive") for b in ("thin", "naive")}
    sg27 = hodge_sign(27)
    allowed = {key: D for key, D in cand.items() if (1 if D > 0 else -1) == sg27[0]}
    ok = (sg27 == (1, False) and set(allowed) == {("thin", "thin"), ("thin", "naive")}
          and cand[("thin", "thin")] == 3187041)
    check(f"F9b. V27 has four Hodge types in two pairs and no middle class, so its determinant is even. The four "
          f"readings (3 at 27, 5 at 25: thin or naive) give {cand}. Only those with 3 thin are even: letting 3 enter at "
          f"its cube would make V27's determinant odd", ok)
    ok = all(hodge_sign(k)[0] == (1 if det_with(k, 'thin', 'thin') > 0 else -1) for k in (17, 19, 21, 23, 25, 27))
    check("F9c. the thin rule's determinants at 17 to 27 have the sign the Hodge types require (middle class +1)", ok,
          " ".join(f"k={k}:{det_with(k, 'thin', 'thin')}" for k in (19, 23, 25, 27)))

    # F10: reading a determinant from the traces of Frobenius and of its square
    rng = np.random.default_rng(26)
    ok = True
    for d in (3, 4, 5):
        for _ in range(200):
            Q, R = np.linalg.qr(rng.normal(size=(d, d)))
            Q = Q @ np.diag(np.sign(np.diag(R)))
            ev = np.linalg.eigvals(Q)
            e1, e2 = ev.sum().real, sum(ev[i] * ev[j] for i in range(d) for j in range(i + 1, d)).real
            e3 = sum(ev[i] * ev[j] * ev[k] for i in range(d) for j in range(i + 1, d) for k in range(j + 1, d)).real
            det = round(np.linalg.det(Q))
            if d == 3:
                ok &= abs(e2 - det * e1) < 1e-9
            elif d == 4 and det == -1:
                ok &= abs(e2) < 1e-9
            elif d == 5:
                ok &= abs(e3 - det * e2) < 1e-9
    check("F10. for an orthogonal piece with eigenvalues normalized to modulus 1: in dimension 3, e2 = det * e1; in "
          "dimension 4, det = -1 forces e2 = 0; in dimension 5, e3 = det * e2 (200 random cases each). With "
          "e2 = (T(p)^2 - T(p^2))/2, the counts over F_p and F_(p^2) read the determinant prime by prime", ok)

    # F11: the counter
    ok, rows = True, []
    for p in (23, 29, 31, 101, 113):
        ns = tuple(range(3, 22, 2))
        a, b = t_values_crt(p, 1, ns), t_values(p, ns)
        ok &= all(a[n] == b[n] for n in ns)
        rows.append(f"{p}:{all(a[n] == b[n] for n in ns)}")
    check("F11a. the new counter equals the convolution count of rounds 19 to 25 for every odd n up to 21 at p = 23, 29, "
          "31, 101 and 113", ok, " ".join(rows))
    ok, rows = True, []
    for p in (5, 7):
        ns = (3, 5, 7)
        brute = cone_counts_fq(p, ns)
        q = p * p
        tb = {n: Fraction(brute[n] - q ** (n - 2), q - 1) for n in ns}
        tc = t_values_crt(p, 2, ns)
        ok &= all(tb[n] == tc[n] for n in ns)
        rows.append(f"F_{q}:{all(tb[n] == tc[n] for n in ns)}")
    check("F11b. over F_(p^2) the counter equals a direct convolution on F_(p^2)^2 (p = 5, 7; n = 3, 5, 7)", ok,
          " ".join(rows))
    ok, rows = True, []
    for p in (29, 31):
        ns = tuple(range(3, 12, 2))
        T = airy(p, t_values_crt(p, 1, ns))
        q = p * p
        T2 = airy(q, t_values_crt(p, 2, ns))
        good = (T2[1] == q and T2[3] == 0 and T2[5] == T[5] ** 2 and T2[9] == T[9] ** 2
                and T2[7] == T[7] ** 2 - 2 * leg(-35, p) * p ** 8 and T2[11] == T[11] ** 2 - 2 * leg(-1155, p) * p ** 12)
        ok &= good
        rows.append(f"{p}:{good}")
    check("F11c. over F_(p^2) the known pieces are the squares of Frobenius: T1 = p^2, T3 = 0, T5 = T5(p)^2, "
          "T7 = T7(p)^2 - 2(-35|p)p^8, T9 = T9(p)^2, T11 = T11(p)^2 - 2(-1155|p)p^12 (p = 29, 31; n <= 11 only)", ok,
          " ".join(rows))

    # F12: the bookkeeping for 19 to 27
    ok, rows = True, []
    v = {k: len(classical_hodge(k)) for k in range(1, 28, 2)}
    for n in (19, 23, 25, 27):
        ok &= sum(ballot(n, k) * v[k] for k in range(1, n + 1, 2)) == betti_prim(n)
        rows.append(f"V{n}: dim {v[n]}, types {classical_hodge(n)}")
        for l in [3] + primes(5, n):
            thin, thick = nodes_by_kind(n, l)
            lower = sum(ballot(n, k) * thin_nodes(k, l) for k in range(1, n, 2))
            ok &= thin - lower == thin_nodes(n, l)
            if thick:
                rows.append(f"  n={n}, l={l}: {thin} thin nodes ({thin - lower} in V{n}) and {thick} thick")
    check("F12a. X19, X23, X25 and X27: the lower pieces fill all but 4, 4, 5 and 4 dimensions, and all but the thin "
          "nodes' share of each new piece. The thick nodes: at 25 the centre, mod 5 (sum 25); at 27 the centre mod 3 "
          "(sum 27) and the 27 sign vectors of sum 25, mod 5", ok)
    for row in rows:
        say("  " + row)
    D = {k: det_with(k, "thin", "thin") for k in (19, 23, 25, 27)}
    check(f"F12b. the thin rule's determinants: V19 ({D[19]}|p), V23 ({D[23]}|p), V25 ({D[25]}|p), V27 ({D[27]}|p). "
          f"The naive rule changes V25 to ({det_with(25, 'thin', 'naive')}|p) (5 at 25) and V27 to "
          f"({det_with(27, 'thin', 'naive')}|p) or ({det_with(27, 'naive', 'thin')}|p)",
          D == {19: 969969, 23: 3187041, 25: 3187041, 27: 3187041})
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()


# read after round 25: which characters decide the square classes of seventeen's and twenty-one's roots
R2_CHARS = {-1: -51051, 2: -715, 5: -1547, 7: -12155, 13: -35, 17: -3003}
R3_CHARS = {-1: -138567, 2: -19019, 3: -143, 5: -1547, 17: -1155, 19: -3003}
ODD27 = tuple(range(3, 28, 2))


def class_from(chars, p):
    s = 1
    for l, D in chars.items():
        if kron(D, p) == -1:
            s *= l
    return s


def square_class_ok(u, D, chars, p):
    """u + (D|p) p^2 = s_p b^2, with b an integer and s_p the product of the primes whose character is -1 at p"""
    if u.denominator != 1:
        return False
    v = int(u) + kron(D, p) * p * p
    if v == 0:
        return True
    s = class_from(chars, p)
    return v % s == 0 and v // s > 0 and sympy.integer_nthroot(v // s, 2)[1]


def _r26_fp(p):
    low_priority()
    return p, t_values_crt(p, 1, ODD27)


def _r26_fq(p):
    low_priority()
    return p, t_values_crt(p, 2, ODD27)


def lower_square_ok(p, T, T2):
    """the known pieces over F_(p^2): squares of their Frobenius eigenvalues, from their F_p traces and determinants"""
    q = p * p
    return (T2[1] == q and T2[3] == 0 and T2[5] == T[5] ** 2 and T2[9] == T[9] ** 2
            and T2[7] == T[7] ** 2 - 2 * leg(-35, p) * p ** 8
            and T2[11] == T[11] ** 2 - 2 * leg(-1155, p) * p ** 12
            and T2[13] == T[13] ** 2 - 2 * kron(-15015, p) * p ** 7 * T[13]
            and T2[15] == T[15] ** 2 - 2 * leg(-3003, p) * p ** 16
            and T2[17] == T[17] ** 2 - 2 * kron(-51051, p) * p ** 9 * T[17])


def test26():
    """round 26 (PREREG.md): Y1 to Y5 (twenty-seven, with nineteen and twenty-three beside it), W1 (twenty-five), R2 and
    R3 (seventeen's and twenty-one's square classes, blind)"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test26.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    PF, PQ = primes(29, 1999), primes(29, 151)
    say("Round 26: twenty-seven first, with 19, 23 and 25 beside it, and the square classes of 17 and 21 (PREREG.md)")
    say(f"over F_p at {PF[0]}..{PF[-1]} ({len(PF)} primes); over F_(p^2) at {PQ[0]}..{PQ[-1]} ({len(PQ)} primes)")
    with Pool(4) as pool:
        rq = dict(pool.map(_r26_fq, sorted(PQ, reverse=True)))
        rf = dict(pool.map(_r26_fp, PF))
    T = {p: airy(p, rf[p]) for p in PF}
    T2 = {p: airy(p * p, rq[p]) for p in PQ}

    # ---- the instruments
    inst = all(lower_pieces_ok(p, T[p]) for p in PF)
    say(f"instrument over F_p: T1..T15 as found in rounds 19 to 24 at every prime 29..1999: {inst}")
    old17 = [p for p in PF if p < 409 and fused_signature([p], {p: T[p][17] / p ** 7}, -51051, 510510)]
    say(f"instrument: seventeen's symmetric square (round 25, Z3') at 29..401: fails at {old17}")
    inst2 = all(lower_square_ok(p, T[p], T2[p]) for p in PQ)
    say(f"instrument over F_(p^2): T1..T17 are the squares of their Frobenius eigenvalues at every prime 29..151 "
        f"(this rereads the determinants of 7, 11, 13, 15 and 17 prime by prime): {inst2}")

    # ---- twenty-seven, and the four-dimensional pieces beside it
    def e2(k, p):
        v = (T[p][k] ** 2 - T2[p][k]) / 2
        return v

    say("X27 p u27 (3187041|p)   [u27 = T27/p^11]")
    u27 = {p: T[p][27] / p ** 11 for p in PF}
    for p in PF:
        say(f"X27 {p} {u27[p]} {kron(3187041, p)}")
    bad1 = [p for p in PF if u27[p].denominator != 1 or abs(u27[p]) > 4 * p ** 3]
    y1 = not bad1
    say(f"Y1 T27 = p^11 u27(p), u27 an integer with |u27| <= 4p^3, at every prime 29..1999: "
        f"{'HELD' if y1 else 'FAILED at ' + str(bad1)}")
    cands = {"thin": 3187041, "5 at 25": 15935205, "3 at 27": -1062347, "both": -5311735}
    say("X27sq p e2   [e2 = (T27(p)^2 - T27(p^2))/2; det = -1 exactly when e2 = 0]")
    zero27 = {p: e2(27, p) == 0 for p in PQ}
    for p in PQ:
        say(f"X27sq {p} {e2(27, p)} " + " ".join(f"{name}:{kron(D, p)}" for name, D in cands.items()))
    fits = {name: sum(1 for p in PQ if zero27[p] == (kron(D, p) == -1)) for name, D in cands.items()}
    y2 = y1 and fits["thin"] == len(PQ)
    say(f"  primes (of {len(PQ)}) where the reading fits: {fits}")
    say(f"Y2 V27's determinant is (3187041|p): 3 does not enter at 27, its cube, and 5 does not enter at 25, its square: "
        f"{'HELD' if y2 else 'FAILED'}")
    big = [p for p in PF if abs(u27[p]) > 2 * p ** 3]
    bad2b = [p for p in big if kron(3187041, p) != 1]
    rival = {name: sum(1 for p in big if kron(D, p) != 1) for name, D in cands.items()}
    y2b = y1 and not bad2b and len(big) >= 10
    say(f"  |u27| > 2p^3 at {len(big)} primes, where the determinant must be +1; the readings fail there: {rival}")
    say(f"Y2' wherever |u27| > 2p^3, (3187041|p) = +1: {'HELD' if y2b else 'FAILED'}")
    res3 = {}
    for k, D, wexp in ((23, 3187041, 9), (19, 969969, 7)):
        uk = {p: T[p][k] / p ** wexp for p in PF}
        shape = all(uk[p].denominator == 1 and abs(uk[p]) <= 4 * p ** 3 for p in PF)
        det_ok = all((e2(k, p) == 0) == (kron(D, p) == -1) for p in PQ)
        res3[k] = (shape, det_ok)
        say(f"  V{k}: T{k} = p^{wexp} u, u an integer with |u| <= 4p^3 at every prime: {shape}; e2 = 0 exactly where "
            f"({D}|p) = -1, at every prime 29..151: {det_ok}")
    y3 = all(a and b for a, b in res3.values())
    say(f"Y3 the controls: V23's determinant is (3187041|p), the same as the thin rule gives V27, and V19's is "
        f"(969969|p): {'HELD' if y3 else 'FAILED'}")
    bad4 = [p for p in PQ if T2[p][21] != T[p][21] ** 2 - 2 * kron(-138567, p) * p ** 11 * T[p][21]]
    y4 = not bad4
    say(f"Y4 V21's determinant is (-138567|p), prime by prime over F_(p^2) at 29..151: "
        f"{'HELD' if y4 else 'FAILED at ' + str(bad4)}")
    div27 = [p for p in PF if y1 and int(u27[p]) % p == 0]
    y5 = y1 and len(div27) <= 3
    say(f"  p divides u27 at {len(div27)} of the {len(PF)} primes: {div27}")
    say(f"Y5 V27 does not split into two CM planes: {'HELD' if y5 else 'FAILED'}")

    # ---- twenty-five
    u25 = {p: T[p][25] / p ** 9 for p in PF}
    shape25 = all(u25[p].denominator == 1 and abs(u25[p]) <= 5 * p ** 4 for p in PF)
    big25 = [p for p in PF if abs(u25[p]) > 3 * p ** 4]
    signs = {name: [p for p in big25 if (1 if u25[p] > 0 else -1) != kron(D, p)]
             for name, D in (("thin", 3187041), ("5 at 25", 15935205))}
    w1 = shape25 and not signs["thin"] and len(big25) >= 5
    say(f"  V25: T25 = p^9 u25, u25 an integer with |u25| <= 5p^4 at every prime: {shape25}; |u25| > 3p^4 at "
        f"{len(big25)} primes; wrong signs: thin {len(signs['thin'])}, 5 at 25 {len(signs['5 at 25'])}")
    say(f"W1 V25's middle eigenvalue has the sign (3187041|p): 5 does not enter at 25: {'HELD' if w1 else 'FAILED'}")
    for p in PQ:
        P = Fraction(p) ** 13
        a1, b2 = T[p][25] / P, e2(25, p) / P ** 2
        ok_d = []
        for d in (1, -1):
            A = a1 - d
            B = b2 - d * A - 2
            disc = A * A - 4 * B
            if disc >= 0:
                r = math.sqrt(float(disc))
                if abs((float(A) + r) / 2) <= 2 + 1e-9 and abs((float(A) - r) / 2) <= 2 + 1e-9:
                    ok_d.append(d)
        say(f"X25sq {p} determinants allowed by T25(p), T25(p^2) and the circle: {ok_d}; thin {kron(3187041, p)}, "
            f"5 at 25 {kron(15935205, p)} (read)")

    # ---- seventeen's and twenty-one's square classes, blind
    P2 = [p for p in PF if p >= 409]
    bad = [p for p in P2 if not square_class_ok(T[p][17] / p ** 7, -51051, R2_CHARS, p)]
    say(f"R2 seventeen's square classes, by the six characters read after round 25, at every prime 409..1999 "
        f"({len(P2)}): {'HELD' if not bad else 'FAILED at ' + str(bad[:12])}")
    P3 = [p for p in PF if p >= 127]
    bad = [p for p in P3 if not square_class_ok(T[p][21] / p ** 9, -138567, R3_CHARS, p)]
    say(f"R3 twenty-one's square classes, by its six characters, at every prime 127..1999 ({len(P3)}): "
        f"{'HELD' if not bad else 'FAILED at ' + str(bad[:12])}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


# ------------------------------------------------------------------ round 27: eighty-one, and twenty-five's determinant
#   "1 and 3, 81 first"  -- the author, 15 November 2026
#   (1: the cubic in 81 variables, four coins of 3, where the rule lets 3 in again.  3: twenty-five's own determinant,
#   read from the field of p^3 elements.)
ODD81 = tuple(range(3, 82, 2))


def cubic_hodge(n):
    """the primitive Hodge numbers h^(a, n-3-a) of a smooth cubic of dimension n - 3 (n odd, n - 1 variables). By
    Griffiths they count the monomials of degree 3(n - 2 - a) - (n - 1) in the Jacobian ring; for the Fermat cubic that
    ring has the monomials with exponents 0 and 1, so h = C(n - 1, 2n - 5 - 3a). Hodge numbers do not change in a smooth
    family, so this holds for X_n."""
    return {a: math.comb(n - 1, 2 * n - 5 - 3 * a) for a in range(n - 2) if 0 <= 2 * n - 5 - 3 * a <= n - 1}


def hodge_by_peeling(kmax):
    """every piece's Hodge types from the cubics alone. X_n holds V_n once and each lower V_k m(n, k) times; in T_k's
    normalization (weight k + 1) the type (a, b) of V_k sits in X_n at (a - 2 + (n - k)/2, ...). So V_n is what is left
    of X_n's numbers after the lower pieces: nothing here uses Sabbah and Yu's theorem."""
    V = {1: {1: 1}}
    for n in range(3, kmax + 1, 2):
        h = cubic_hodge(n)
        for k in range(1, n, 2):
            for a, c in V[k].items():
                s = a - 2 + (n - k) // 2
                h[s] = h.get(s, 0) - ballot(n, k) * c
        V[n] = {a + 2: c for a, c in h.items() if c}
    return V


def hodge_sign_fast(k):
    """hodge_sign without listing the types: V_k has one type for each i <= (k + 1)/2 with i = k (mod 3), and a middle
    class exactly when k = 1 (mod 4)"""
    m, r0 = (k + 1) // 2, (k % 3) or 3
    d = (m - r0) // 3 + 1 if m >= r0 else 0
    mid = k % 4 == 1
    return (-1) ** ((d - mid) // 2), mid


def airy_double_factorial(k):
    """A_k: the product of the odd numbers up to k, each multiple of 3 divided by 3 once (the cube's 3)"""
    A = 1
    for j in range(1, k + 1, 2):
        A *= j // 3 if j % 3 == 0 else j
    return A


def star_kernel(m):
    """the product of the signed primes l* over the primes with odd exponent in m. For odd m > 0 and a prime p not
    dividing m, (star_kernel(m)|p) is the Jacobi symbol (p/m), by quadratic reciprocity"""
    D = 1
    for l, e in sympy.factorint(m).items():
        if e % 2:
            D *= signed(l)
    return D


def sign_run(kmax):
    """the sign of the thin rule's determinant at every odd k <= kmax, kept up from A_k one factor at a time, beside the
    Hodge sign"""
    spf = list(range(kmax + 1))
    for i in range(2, int(kmax ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, kmax + 1, i):
                if spf[j] == j:
                    spf[j] = i
    odd, neg, rows = set(), 0, []
    for k in range(1, kmax + 1, 2):
        m = k // 3 if k % 3 == 0 else k
        while m > 1:
            l = spf[m]
            m //= l
            if l in odd:
                odd.remove(l)
                neg -= l % 4 == 3
            else:
                odd.add(l)
                neg += l % 4 == 3
        rows.append((k, (-1) ** neg, hodge_sign_fast(k)[0]))
    return rows


# the counter over F_(p^r) for r <= 3: S(1, t) for every t at once, as a Fourier transform over (Z/p)^r
def field_poly(p, r):
    """a monic irreducible f = x^r + c_(r-1) x^(r-1) + ... + c_0 over F_p, r <= 3 (no root in F_p suffices)"""
    if r == 1:
        return [0]
    for a1 in range(p):
        for a0 in range(1, p):
            c = [a0, a1] + [0] * (r - 2)
            if all((pow(x, r, p) + sum(ci * pow(x, i, p) for i, ci in enumerate(c))) % p for x in range(p)):
                return c
    raise ValueError(f"no irreducible polynomial of degree {r} found mod {p}")


def fq_mul(X, Y, c, p):
    """products in F_p[b]/(f) of coordinate arrays of shape (r, q), in the basis 1, b, ..., b^(r-1)"""
    r = len(c)
    prod = [np.zeros(X.shape[1], dtype=np.int64) for _ in range(2 * r - 1)]
    for i in range(r):
        for j in range(r):
            prod[i + j] = (prod[i + j] + X[i] * Y[j]) % p
    for d in range(2 * r - 2, r - 1, -1):
        top = prod[d]
        for i, ci in enumerate(c):
            prod[d - r + i] = (prod[d - r + i] - ci * top) % p
    return np.array(prod[:r])


def power_sums(c, p, m):
    """Tr(b^j) for j < m: traces of the powers of f's companion matrix"""
    r = len(c)
    C = sympy.zeros(r, r)
    for i in range(1, r):
        C[i, i - 1] = 1
    for i in range(r):
        C[i, r - 1] = -c[i]
    out, M = [], sympy.eye(r)
    for _ in range(m):
        out.append(int(M.trace()) % p)
        M = (M * C).applyfunc(lambda v: v % p)
    return out


def field_dual(p, r):
    """for every x in F_q (indexed sum x_i p^i): Tr(x), and the index of the dual coordinates c' of x^3, with
    Tr(t x^3) = sum_i t_i c'_i (c' = the trace form's matrix s_(i+j) applied to the coordinates of x^3)"""
    c = field_poly(p, r)
    q = p ** r
    idx = np.arange(q, dtype=np.int64)
    X = np.array([(idx // p ** i) % p for i in range(r)])
    X3 = fq_mul(fq_mul(X, X, c, p), X, c, p)
    s = power_sums(c, p, 2 * r - 1)
    tr = sum(s[i] * X[i] for i in range(r)) % p
    cidx = sum((sum(s[i + j] * X3[j] for j in range(r)) % p) * p ** i for i in range(r))
    return tr, cidx


def moduli_small(p, bits):
    """primes l = 1 (mod p) between 2^20 and 2^21, enough for `bits`: small enough that a sum of p products of residues
    stays below 2^53, so the Fourier transform runs exactly in floating point"""
    out, prod = [], 1
    m = (1 << 20) // p + 1
    while prod.bit_length() <= bits:
        l = 1 + p * m
        if l >= 1 << 21:
            raise ValueError(f"not enough moduli below 2^21 for p = {p}")
        if sympy.isprime(l):
            out.append(l)
            prod *= l
        m += 1
    return out


def dft_mod(H, p, r, W, l):
    """sum over c' of H(c') w^(t . c') for every t in (Z/p)^r, mod l, one axis at a time"""
    A = H.reshape((p,) * r)
    for ax in range(r):
        A = np.moveaxis(A, ax, 0)
        sh = A.shape
        A = np.fmod(W @ A.reshape(p, -1), l).reshape(sh)
        A = np.moveaxis(A, 0, ax)
    return A.reshape(-1)


def counts_dft(p, r, ns):
    """N_n(F_q) mod M, as counts_crt, with S(0, t) and S(1, t) from the Fourier transforms of the measures of x^3 and
    of x^3 weighted by e(Tr x / p)"""
    q = p ** r
    nmax = max(ns)
    bound = 4 * (q - 1) * betti_prim(nmax) * q ** ((nmax - 3) // 2)
    mods = moduli_small(p, bound.bit_length() + 1)
    tr, cidx = field_dual(p, r)
    H0 = np.bincount(cidx, minlength=q).astype(np.float64)
    res = {n: [] for n in ns}
    for l in mods:
        w = root_of_unity(p, l)
        pw = np.array([pow(w, k, l) for k in range(p)], dtype=np.int64)
        W = np.array([[pw[(t * x) % p] for x in range(p)] for t in range(p)], dtype=np.float64)
        H1 = np.fmod(np.bincount(cidx, weights=pw[tr].astype(np.float64), minlength=q), l)
        c0 = dft_mod(np.fmod(H0, l), p, r, W, l).astype(np.int64)
        c1 = dft_mod(H1, p, r, W, l).astype(np.int64)
        s0, s1 = c0 * c0 % l, c1 * c1 % l
        inv = pow(q * q % l, l - 2, l)
        for n in range(1, nmax + 1, 2):
            if n in res:
                res[n].append((int(c0.sum()) + (q - 1) * int(c1.sum())) % l * inv % l)
            c0, c1 = c0 * s0 % l, c1 * s1 % l
    M = math.prod(mods)
    return {n: int(crt(mods, res[n])[0]) for n in ns}, M, bound


def t_values_dft(p, r, ns):
    """t_n over F_(p^r) exactly, by counts_dft, with the same self-check as t_values_crt"""
    q = p ** r
    ns3 = tuple(n for n in ns if n >= 3)
    N, M, bound = counts_dft(p, r, ns3)
    t = {1: Fraction(1, q)}
    for n in ns3:
        v = (N[n] - q ** (n - 2)) % M
        if v > M // 2:
            v -= M
        if abs(v) > bound or v % (q - 1):
            raise ArithmeticError(f"the counter's self-check failed at p = {p}, r = {r}, n = {n}")
        t[n] = Fraction(v // (q - 1))
    return t


def cone_counts_f3(p, ns):
    """N_n(F_(p^3)) by convolving the measure of (x, x^3) on F_(p^3)^2, for p = 5 and 7: the brute-force check"""
    c = field_poly(p, 3)
    q = p ** 3
    idx = np.arange(q, dtype=np.int64)
    X = np.array([(idx // p ** i) % p for i in range(3)])
    X3 = fq_mul(fq_mul(X, X, c, p), X, c, p)
    pts = [tuple(int(v) for v in X[:, i]) + tuple(int(v) for v in X3[:, i]) for i in range(q)]
    cnt = np.zeros((p,) * 6, dtype=np.int64)
    cnt[(0,) * 6] = 1
    out = {}
    for n in range(1, max(ns) + 1):
        acc = np.zeros_like(cnt)
        for sh in pts:
            acc += np.roll(cnt, sh, axis=tuple(range(6)))
        cnt = acc
        if n in ns:
            out[n] = int(cnt[(0,) * 6])
    return out


def field_axioms_ok(p, r=3):
    """x^q = x for every x, and x^(q-1) = 1 for every x != 0, in F_p[b]/(f)"""
    c = field_poly(p, r)
    q = p ** r
    idx = np.arange(q, dtype=np.int64)
    X = np.array([(idx // p ** i) % p for i in range(r)])

    def power(B, e):
        R = np.zeros_like(B)
        R[0] = 1
        while e:
            if e & 1:
                R = fq_mul(R, B, c, p)
            B = fq_mul(B, B, c, p)
            e >>= 1
        return R
    one = np.zeros((r, q - 1), dtype=np.int64)
    one[0] = 1
    return bool(np.all(power(X, q) == X)) and bool(np.all(power(X[:, 1:], q - 1) == one))


def lower_cube_ok(p, T, T3):
    """the known pieces over F_(p^3): the cubes of their Frobenius eigenvalues, from the F_p traces and determinants
    (lines at 1, 5, 9; planes at 7, 11, 15; three-dimensional pieces at 13, 17, 21, where T(p^3) = T^3 - 3dPT^2 + 3dP^3)"""
    ok = T3[1] == p ** 3 and T3[3] == 0 and T3[5] == T[5] ** 3 and T3[9] == T[9] ** 3
    for k, D, e in ((7, -35, 8), (11, -1155, 12), (15, -3003, 16)):
        ok = ok and T3[k] == T[k] ** 3 - 3 * kron(D, p) * p ** e * T[k]
    for k, D in ((13, -15015), (17, -51051), (21, -138567)):
        d, P = kron(D, p), Fraction(p) ** ((k + 1) // 2)
        ok = ok and T3[k] == T[k] ** 3 - 3 * d * P * T[k] ** 2 + 3 * d * P ** 3
    return ok


def verify27():
    """the forced checks F13 to F18 behind round 27. Nothing here counts a cubic in more than 27 variables, or any cubic
    in 17 or more variables over the field of p^3 elements."""
    global LOG
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)   # run logs go to runs/ (ignored); the committed copy is the reference
    LOG = open(os.path.join(HERE, "runs", "edge_rule_verify27.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("edge_rule.py verify27 -- the forced checks for round 27 (eighty-one, and twenty-five's own determinant)")

    # F13: the Hodge types, from the cubics alone
    V = hodge_by_peeling(201)
    bad = [k for k in range(1, 202, 2) if V[k] != {a: 1 for a, _ in classical_hodge(k)}]
    check("F13a. the primitive Hodge numbers of smooth cubics, C(n - 1, 2n - 5 - 3a) (Griffiths, from the Fermat cubic), "
          "peeled by the ballot triangle, give every V_k up to k = 201 exactly Sabbah and Yu's classical types, each once",
          not bad, f"V79: {sorted(V[79])}; V81: {sorted(V[81])}; mismatches {bad}")
    ok = all(sum(ballot(n, k) * len(classical_hodge(k)) for k in range(1, n + 1, 2)) == betti_prim(n)
             for n in range(3, 82, 2))
    check("F13b. the pieces fill every smooth cubic up to 81 variables: sum of m(n, k) dim V_k = (2^(n-1) + 2)/3", ok)

    # F14: the infinite place at 79 and 81
    s79, s81 = hodge_sign(79), hodge_sign(81)
    new = [l for l in [3] + primes(5, 81) if thin_nodes(81, l) != thin_nodes(79, l)]
    D79, D81 = det_from_nodes(79), det_from_nodes(81)
    check(f"F14a. the only node new at 81 is the centre, of sum 81, which pinches only mod 3 (good model: critical value "
          f"of valuation {fval(critical_value(81, 'e3'), 3)} at 3, thin); every other node keeps its local equation, so the "
          f"thin counts of V79 and V81 differ only at {new}",
          new == [3] and fval(critical_value(81, "e3"), 3) == 3 and fval(critical_value_direct(81, 81, "e3"), 3) == 3)
    check(f"F14b. the infinite place: V79 has {len(classical_hodge(79))} types in 7 pairs (determinant odd), V81 has "
          f"{len(classical_hodge(81))}: 6 pairs and the middle class (41, 41) (determinant even, middle class +1 as at "
          f"every k read). So D81/D79 must be negative, and it can only be -3: 3 enters at 81. The thin rule gives "
          f"D79 < 0 < D81 with D81/D79 = -3 up to squares",
          s79 == (-1, False) and s81 == (1, True) and D79 < 0 < D81 and star_kernel(abs(D79 * D81)) == -3)
    say(f"  D79 = {D79}")
    say(f"  D81 = {D81}")

    # F15: every k
    rows = sign_run(20001)
    bad = [k for k, a, b in rows if a != b]
    flips = {k for (k, a, _), (_, a0, _) in zip(rows[1:], rows[:-1]) if a != a0}
    check("F15a. at every odd k up to 20001 the thin rule's determinant has the sign the Hodge types require (middle "
          "class +1), and both change sign exactly at k = 7, 9, 11 (mod 12)",
          not bad and flips == {k for k, _, _ in rows[1:] if k % 12 in (7, 9, 11)}, f"disagreements {bad[:5]}")
    ok = all(hodge_sign_fast(k) == hodge_sign(k) for k in range(1, 2002, 2))
    check("F15b. the fast Hodge sign agrees with the listed types for every odd k up to 2001", ok)
    table, ok = [], True
    for l in [3, 7, 11, 19, 23, 31, 43, 47]:
        a, enters = 1, []
        while l ** a <= 20001:
            k = l ** a
            flip = k % 12 in (7, 9, 11)
            thin = (val(k, l) - (1 if l == 3 else 0)) % 2 == 1
            ok &= flip == thin
            if flip:
                enters.append(a)
            a += 1
        table.append(f"{l}: enters at a = {enters} of 1..{a - 1}")
    check("F15c. at a power l^a of a prime l = 3 (mod 4) only l can change, and l* < 0, so the infinite place alone decides "
          "whether l enters, and it agrees with the thin rule: 3 at its even powers, every other such prime at its odd "
          "powers. At primes = 1 (mod 4), such as 5 and 13, l* > 0 and the infinite place is blind", ok, "; ".join(table))

    # F16: one symbol
    ok = all(det_from_nodes(k) == star_kernel(airy_double_factorial(k)) for k in range(1, 302, 2))
    known = {**MEASURED_DET, 17: -51051, 19: 969969, 21: -138567, 23: 3187041, 25: 3187041, 27: 3187041}
    ok2 = all(star_kernel(airy_double_factorial(k)) == D for k, D in known.items())
    ok3 = all(star_kernel(abs(star_kernel(airy_double_factorial(k)) * star_kernel(math.prod(range(1, k + 1, 2)))))
              in (1, -3) for k in range(1, 302, 2))
    check("F16. the thin rule is one symbol: V_k's determinant is the Jacobi symbol (p/A_k), with A_k the product of the "
          "odd numbers up to k, each multiple of 3 divided by 3 once (every odd k up to 301; the values read at 1 to 27). "
          "Yun's theorem for Kloosterman moments has (p/d!!); the two differ only by the cube's 3",
          ok and ok2 and ok3)

    # F17: the counter over F_(p^3)
    rows, ok = [], True
    for p, r in ((29, 1), (31, 1), (101, 1), (29, 2), (31, 2), (101, 2)):
        a, b = t_values_dft(p, r, ODD27), t_values_crt(p, r, ODD27)
        good = all(a[n] == b[n] for n in ODD27)
        ok &= good
        rows.append(f"F_{p}^{r}:{good}")
    check("F17a. the Fourier counter equals round 26's counter over F_p and F_(p^2) for every odd n up to 27 (p = 29, 31, "
          "101)", ok, " ".join(rows))
    rows, ok = [], True
    for p, ns in ((5, (3, 5, 7)), (7, (3, 5))):
        brute = cone_counts_f3(p, ns)
        q = p ** 3
        tb = {n: Fraction(brute[n] - q ** (n - 2), q - 1) for n in ns}
        tc = t_values_dft(p, 3, ns)
        good = field_axioms_ok(p) and all(tb[n] == tc[n] for n in ns)
        ok &= good
        rows.append(f"F_{q}:{good}")
    check("F17b. F_p[b]/(f) is a field of p^3 elements (x^q = x, x^(q-1) = 1), and over it the counter equals a direct "
          "convolution on F_(p^3)^2 (p = 5: n = 3, 5, 7; p = 7: n = 3, 5)", ok and field_axioms_ok(29), " ".join(rows))
    rows, ok = [], True
    for p in (29, 31):
        ns = tuple(range(3, 16, 2))
        T = airy(p, t_values_crt(p, 1, ns))
        T3 = airy(p ** 3, t_values_dft(p, 3, ns))
        good = (T3[1] == p ** 3 and T3[3] == 0 and T3[5] == T[5] ** 3 and T3[9] == T[9] ** 3
                and T3[7] == T[7] ** 3 - 3 * leg(-35, p) * p ** 8 * T[7]
                and T3[11] == T[11] ** 3 - 3 * leg(-1155, p) * p ** 12 * T[11]
                and T3[15] == T[15] ** 3 - 3 * leg(-3003, p) * p ** 16 * T[15]
                and T3[13] == T[13] ** 3 - 3 * kron(-15015, p) * p ** 7 * T[13] ** 2 + 3 * kron(-15015, p) * p ** 21)
        ok &= good
        rows.append(f"{p}:{good}")
    check("F17c. over F_(p^3) the known pieces are the cubes of their eigenvalues: T1 = p^3, T3 = 0, T5 and T9 cubed, "
          "T = a^3 - 3 det P^2 a on the planes 7, 11, 15, and T = a^3 - 3 det P a^2 + 3 det P^3 on V13 (p = 29, 31; n <= 15 "
          "only)", ok, " ".join(rows))

    # F18: reading a determinant from the first three traces
    rng = np.random.default_rng(27)
    ok = True
    for d in (3, 4, 5):
        for _ in range(300):
            Q, R = np.linalg.qr(rng.normal(size=(d, d)))
            Q = Q @ np.diag(np.sign(np.diag(R)))
            if rng.random() < 0.5:
                Q = Q @ np.diag([-1.0] + [1.0] * (d - 1))
            ev = np.linalg.eigvals(Q)
            e1 = ev.sum().real
            e2 = sum(ev[i] * ev[j] for i in range(d) for j in range(i + 1, d)).real
            e3 = sum(ev[i] * ev[j] * ev[k] for i in range(d) for j in range(i + 1, d) for k in range(j + 1, d)).real
            det = round(np.linalg.det(Q).real)
            ok &= abs(e3 - det * {3: 1, 4: e1, 5: e2}[d]) < 1e-9
    check("F18. for an orthogonal piece with eigenvalues of modulus 1: e3 = det in dimension 3, e3 = det * e1 in "
          "dimension 4, e3 = det * e2 in dimension 5 (300 random cases each, both determinants). With p3 = e1^3 - 3 e1 e2 "
          "+ 3 e3 and the counts over F_p, F_(p^2), F_(p^3), each prime reads the determinant directly", ok)
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()


def _r27_fp81(p):
    low_priority()
    return p, t_values_crt(p, 1, ODD81)


def _r27_pq(p):
    low_priority()
    return p, (t_values_crt(p, 1, ODD27), t_values_crt(p, 2, ODD27), t_values_dft(p, 3, ODD27))


def e123(T1, T2, T3):
    """the first three elementary symmetric functions of the eigenvalues, from the traces of Frobenius, its square and
    its cube"""
    e1 = T1
    e2 = (T1 * T1 - T2) / 2
    e3 = (T3 - T1 ** 3 + 3 * T1 * e2) / 3
    return e1, e2, e3


def test27():
    """round 27 (PREREG.md): Q1 to Q3 (eighty-one), Z1 and Z2 (twenty-five's own determinant, and the second reading of
    the four-dimensional pieces)"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test27.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    PF, PQ = primes(83, 1999), primes(29, 151)
    say("Round 27: eighty-one first, then twenty-five's own determinant (PREREG.md)")
    say(f"X_n for odd n <= 81 over F_p at {PF[0]}..{PF[-1]} ({len(PF)} primes); X_n for odd n <= 27 over F_p, F_(p^2) "
        f"and F_(p^3) at {PQ[0]}..{PQ[-1]} ({len(PQ)} primes)")
    with Pool(4) as pool:
        r81 = dict(pool.map(_r27_fp81, PF))
        rq = dict(pool.map(_r27_pq, sorted(PQ, reverse=True)))
    say(f"counted in {(time.time() - t0) / 60:.1f} minutes")
    T = {p: airy(p, r81[p]) for p in PF}

    # ---- eighty-one
    inst = all(lower_pieces_ok(p, T[p]) for p in PF)
    r2 = all(square_class_ok(T[p][17] / p ** 7, -51051, R2_CHARS, p) for p in PF if p >= 409)
    r3 = all(square_class_ok(T[p][21] / p ** 9, -138567, R3_CHARS, p) for p in PF if p >= 127)
    say(f"instrument over F_p at 83..1999: T1..T15 as found in rounds 19 to 24: {inst}; seventeen's and twenty-one's "
        f"square classes (rounds 25, 26): {r2 and r3}")
    shape_bad, ordinary = {}, {}
    for k in range(17, 82, 2):
        types = classical_hodge(k)
        h, d, top = min(a for a, _ in types), len(types), (k + 1) // 2
        bad, divs = [], []
        for p in PF:
            u = T[p][k] / p ** h
            if u.denominator != 1 or abs(u) > d * p ** (top - h):
                bad.append(p)
            elif int(u) % p == 0:
                divs.append(p)
        shape_bad[k], ordinary[k] = bad, divs
    for k in range(17, 82, 2):
        types = classical_hodge(k)
        say(f"V{k}: dim {len(types)}, lowest type {min(a for a, _ in types)}; shape fails at {shape_bad[k]}; p divides u "
            f"at {ordinary[k]}")
    q1 = all(not shape_bad[k] for k in range(29, 82, 2)) and all(not shape_bad[k] for k in range(17, 28, 2))
    say(f"Q1 every piece from 29 to 81 has the forced shape T_k = p^h u, u an integer, |u| <= d p^((k+1)/2 - h), at "
        f"every prime 83..1999 (17 to 27 beside them): {'HELD' if q1 else 'FAILED'}")
    worst = max(len(ordinary[k]) for k in range(29, 82, 2))
    q2 = q1 and worst <= 5
    say(f"Q2 ordinary: p divides u at no more than 5 primes for each k from 29 to 81 (most: {worst}): "
        f"{'HELD' if q2 else 'FAILED'}")
    mom = {}
    for k in range(17, 82, 2):
        x = [float(T[p][k] / Fraction(p) ** ((k + 1) // 2)) for p in PF]
        mom[k] = (sum(v for v in x) / len(x), sum(v * v for v in x) / len(x), sum(v ** 4 for v in x) / len(x))
    for k in range(17, 82, 2):
        say(f"moments V{k}: mean x {mom[k][0]:+.3f}, mean x^2 {mom[k][1]:.3f}, mean x^4 {mom[k][2]:.3f}")
    q3 = all(0.75 <= mom[k][1] <= 1.25 and 1.8 <= mom[k][2] <= 4.5 for k in (79, 81))
    say(f"Q3 V79 and V81 have big orthogonal Galois images: mean x^2 within 0.75..1.25 and mean x^4 within 1.8..4.5 "
        f"(x = T/p^((k+1)/2)): V79 {mom[79][1]:.3f}, {mom[79][2]:.3f}; V81 {mom[81][1]:.3f}, {mom[81][2]:.3f}: "
        f"{'HELD' if q3 else 'FAILED'}")

    # ---- twenty-five, and the four-dimensional pieces beside it
    Tq = {}
    for p in PQ:
        t1, t2, t3 = rq[p]
        Tq[p] = (airy(p, t1), airy(p * p, t2), airy(p ** 3, t3))
    inst2 = all(lower_square_ok(p, Tq[p][0], Tq[p][1]) for p in PQ)
    inst3 = all(lower_cube_ok(p, Tq[p][0], Tq[p][2]) for p in PQ)
    say(f"instrument over F_(p^2) at 29..151: the known pieces are the squares of their eigenvalues: {inst2}")
    say(f"instrument over F_(p^3) at 29..151: the known pieces are the cubes of their eigenvalues (1, 5, 9; 7, 11, 15; "
        f"13, 17, 21): {inst3}")
    cands = {"thin": 3187041, "5 at 25": 15935205}
    say("X25cube p e2!=0 eps   thin 5at25 (5|p)   [eps = e3/(p^13 e2)]")
    eps25, und = {}, []
    for p in PQ:
        e1, e2, e3 = e123(Tq[p][0][25], Tq[p][1][25], Tq[p][2][25])
        if e2 == 0:
            und.append(p)
            say(f"X25cube {p} undecided (e2 = 0)")
            continue
        eps25[p] = e3 / (Fraction(p) ** 13 * e2)
        say(f"X25cube {p} {eps25[p]}  {kron(3187041, p)} {kron(15935205, p)} {leg(5, p)}")
    shape25 = all(v in (1, -1) for v in eps25.values())
    fits = {name: sum(1 for p, v in eps25.items() if v == kron(D, p)) for name, D in cands.items()}
    split = [p for p in eps25 if leg(5, p) == -1]
    z1 = shape25 and fits["thin"] == len(eps25) and len(eps25) >= 20 and len(split) >= 8
    say(f"  decided at {len(eps25)} of {len(PQ)} primes ({len(split)} with (5|p) = -1, where the readings differ); "
        f"e3/(p^13 e2) is exactly +-1 at every one: {shape25}; fits: {fits}")
    say(f"Z1 V25's determinant is (3187041|p): 5 does not enter at 25, its square: {'HELD' if z1 else 'FAILED'}")
    z2, rows = True, []
    for k, D in ((27, 3187041), (23, 3187041), (19, 969969)):
        good, n_dec = True, 0
        for p in PQ:
            e1, e2, e3 = e123(Tq[p][0][k], Tq[p][1][k], Tq[p][2][k])
            if e1 == 0:
                continue
            n_dec += 1
            eps = e3 / (Fraction(p) ** (k + 1) * e1)
            good &= eps == kron(D, p)
        z2 &= good and n_dec >= 20
        rows.append(f"V{k}: e3 = ({D}|p) p^{k + 1} e1 at all {n_dec} primes with e1 != 0: {good}")
    for row in rows:
        say("  " + row)
    say(f"Z2 the second reading of the four-dimensional pieces, from the cube of Frobenius: {'HELD' if z2 else 'FAILED'}")

    # ---- read after (not scores)
    say("read: V25's characteristic polynomial at each decided prime, and whether it splits over Q")
    xx = sympy.symbols("x")
    for p in sorted(eps25):
        e1, e2, e3 = e123(Tq[p][0][25], Tq[p][1][25], Tq[p][2][25])
        P = p ** 13
        d = int(eps25[p])
        a = e1 - d * P
        b = e2 - d * P * a
        quartic = 1 - a * xx + b * xx ** 2 - a * P ** 2 * xx ** 3 + P ** 4 * xx ** 4
        fac = sympy.factor_list(sympy.Poly(quartic, xx))
        say(f"X25poly {p} a/p^9 = {a / p ** 9} b/p^18 = {b / p ** 18} quartic factors: {len(fac[1])}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


# ------------------------------------------------------------------ round 28: Theorem 8's first new determinants, blind
#   "2 and 3, the proof first"  -- the author, 16 November 2026
#   (DETERMINANTS.md proves det V_k = (p/A_k); this reads the five determinants past 27 that the fields of p, p^2 and
#   p^3 elements can see: V29 and V33 in five dimensions, V31, V35 and V39 in six.)
ODD39 = tuple(range(3, 40, 2))
R28_FIVE = {29: 92424189, 33: 260468169}
R28_SIX = {31: -2865149859, 35: -9116385915, 39: -25946636835}


def _r28(p):
    low_priority()
    return p, (t_values_crt(p, 1, ODD39), t_values_crt(p, 2, ODD39), t_values_dft(p, 3, ODD39))


def test28():
    """round 28 (PREREG.md): B1 to B5, the determinants of V29, V31, V33, V35 and V39 that Theorem 8 gives, read blind"""
    global LOG
    LOG = open(os.path.join(HERE, "edge_rule_test28.log"), "w", encoding="utf-8")
    t0 = time.time()
    from multiprocessing import Pool
    PQ = primes(41, 151)
    say("Round 28: Theorem 8's determinants past 27, read blind (PREREG.md)")
    say(f"X_n for odd n <= 39 over F_p, F_(p^2) and F_(p^3) at {PQ[0]}..{PQ[-1]} ({len(PQ)} primes)")
    with Pool(4) as pool:
        rq = dict(pool.map(_r28, sorted(PQ, reverse=True)))
    say(f"counted in {(time.time() - t0) / 60:.1f} minutes")
    Tq = {p: (airy(p, rq[p][0]), airy(p * p, rq[p][1]), airy(p ** 3, rq[p][2])) for p in PQ}

    # ---- the instruments
    inst = all(lower_square_ok(p, Tq[p][0], Tq[p][1]) and lower_cube_ok(p, Tq[p][0], Tq[p][2]) for p in PQ)
    old = True
    for k, D in ((19, 969969), (23, 3187041), (27, 3187041)):
        for p in PQ:
            e1, e2, e3 = e123(Tq[p][0][k], Tq[p][1][k], Tq[p][2][k])
            old &= e3 == kron(D, p) * Fraction(p) ** (k + 1) * e1
    for p in PQ:
        e1, e2, e3 = e123(Tq[p][0][25], Tq[p][1][25], Tq[p][2][25])
        old &= e2 != 0 and e3 == kron(3187041, p) * Fraction(p) ** 13 * e2
    say(f"instrument: the known pieces are the squares and cubes of their eigenvalues at every prime: {inst}; the "
        f"determinants of V19, V23, V25 and V27 as read in rounds 26 and 27: {old}")
    shape = {}
    for k in range(29, 40, 2):
        types = classical_hodge(k)
        h, d = min(a for a, _ in types), len(types)
        shape[k] = [p for p in PQ if (Tq[p][0][k] / p ** h).denominator != 1
                    or abs(Tq[p][0][k] / p ** h) > d * p ** ((k + 1) // 2 - h)]
    say(f"shape: every piece from V29 to V39 has its forced shape at every prime: {not any(shape.values())} {shape}")

    # ---- the five determinants
    import math as _m
    rival = {k: star_kernel(_m.prod(range(1, k + 1, 2))) for k in list(R28_FIVE) + list(R28_SIX)}
    scores = {}
    for k, D in R28_FIVE.items():
        decided, good, rfit, exact = 0, 0, 0, True
        say(f"X{k}cube p eps (D|p) rival   [eps = e3/(p^{(k + 1) // 2} e2)]")
        for p in PQ:
            e1, e2, e3 = e123(Tq[p][0][k], Tq[p][1][k], Tq[p][2][k])
            if e2 == 0:
                say(f"X{k}cube {p} undecided (e2 = 0)")
                continue
            eps = e3 / (Fraction(p) ** ((k + 1) // 2) * e2)
            decided += 1
            exact &= eps in (1, -1)
            good += eps == kron(D, p)
            rfit += eps == kron(rival[k], p)
            say(f"X{k}cube {p} {eps} {kron(D, p)} {kron(rival[k], p)}")
        scores[k] = exact and good == decided and decided >= 18
        say(f"  V{k}: decided at {decided} of {len(PQ)}; e3/(P e2) exactly +-1: {exact}; fits ({D}|p) at {good}, "
            f"the rival (p/{k}!!) at {rfit}")
    for k, D in R28_SIX.items():
        zero_where_minus, rfit, n_minus = True, 0, 0
        say(f"X{k}cube p e3==0 (D|p) rival   [six dimensions: det -1 exactly when e3 = 0]")
        for p in PQ:
            e1, e2, e3 = e123(Tq[p][0][k], Tq[p][1][k], Tq[p][2][k])
            z = e3 == 0
            n_minus += kron(D, p) == -1
            zero_where_minus &= z == (kron(D, p) == -1)
            rfit += z == (kron(rival[k], p) == -1)
            say(f"X{k}cube {p} {z} {kron(D, p)} {kron(rival[k], p)}")
        scores[k] = zero_where_minus and n_minus >= 6
        say(f"  V{k}: e3 = 0 exactly where ({D}|p) = -1: {zero_where_minus} ({n_minus} such primes); the rival "
            f"(p/{k}!!) fits {rfit} of {len(PQ)}")
    names = {29: "B1", 33: "B2", 31: "B3", 35: "B4", 39: "B5"}
    for k in (29, 33, 31, 35, 39):
        D = R28_FIVE.get(k, R28_SIX.get(k))
        say(f"{names[k]} V{k}'s determinant is ({D}|p), as Theorem 8 gives: {'HELD' if scores[k] else 'FAILED'}")
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
    elif mode == "test24":
        test24()
    elif mode == "verify25":
        verify25()
    elif mode == "test25":
        test25()
    elif mode == "verify26":
        verify26()
    elif mode == "test26":
        test26()
    elif mode == "verify27":
        verify27()
    elif mode == "test27":
        test27()
    elif mode == "test28":
        test28()
