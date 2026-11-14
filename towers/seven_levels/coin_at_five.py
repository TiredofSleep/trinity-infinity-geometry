"""coin_at_five.py -- the coin at 5 in the fifth moments, its edge, and the coin at 7 (round 19).

    "1 and 2, J4's surface sum first"  -- the author, 14 November 2026
    (1: yes, register a test of the reading that the fifth moment's split by (5|p) is the coin at 5)

The author's classification (base/SEVEN_AND_NINE.md): 5 is a coin.  Its flat face is the pentagon, with its centre
empty; its solid face is the tetrahedron with its centre filled, 5 = 4 + centre; the edge between them is the centre.

The dictionary [FORCED; `python coin_at_five.py`].  In the fifth moment the five Cayley coordinates d1..d5 of the
points on the turning wheel sum to 0: 0 is their centre.  The double octic w^2 = e3 e5 behind I5 is branched along
  - e5 = d1 d2 d3 d4 d5 = 0, the five Sylvester planes: one point sits at the centre and the other four sum to 0
    round it.  That is the solid face, the tetrahedron with its centre filled;
  - e3 = 0, Clebsch's diagonal cubic: it holds the regular pentagon (1, z, z^2, z^3, z^4), z^5 = 1, with its centre
    empty.  That is the flat face;
  - the two meet in 15 lines, each the centre with two opposite pairs, (0, a, -a, b, -b).  That is the edge.
The cubic's other 12 lines form a double six.  The even permutations keep each six and the odd ones swap them, and over
Q the two sixes are conjugate by sqrt5 -> -sqrt5 [NAMED: Clebsch 1871; Hirzebruch 1976].  So there are 27 lines over
F_p when (5|p) = 1 and 15 when (5|p) = -1: that is the (5|p) in I5.  In characteristic 5, where (5|p) = 0, the cubic
gets one singular point, the centre [1:1:1:1:1].  In n variables the centre is singular exactly when p > 3 divides n.

  python coin_at_five.py          # the dictionary, checked                         -> coin_at_five_verify.log
  python coin_at_five.py test     # round 19 (PREREG.md)                            -> coin_at_five_test.log
                                  #   (four worker processes at below-normal priority; a few minutes)

numpy + sympy + exact_moments.py (+ oscillator_states.py for the test).  ASCII output.
"""
import ctypes
import itertools
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


def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


# ------------------------------------------------------------------ the lines of Clebsch's cubic over F_p
def all_lines(p):
    """every line of P^3 = {d1 + ... + d5 = 0} over F_p, as two spanning vectors in the coordinates d1..d4
    (row-reduced echelon form, one representative per line)"""
    U, V = [], []
    r = range(p)
    for a, b, c, d in itertools.product(r, r, r, r):
        U.append((1, 0, a, b)); V.append((0, 1, c, d))
    for a, b, c in itertools.product(r, r, r):
        U.append((1, a, 0, b)); V.append((0, 0, 1, c))
    for a, b in itertools.product(r, r):
        U.append((1, a, b, 0)); V.append((0, 0, 0, 1))
        U.append((0, 1, 0, a)); V.append((0, 0, 1, b))
    for a in r:
        U.append((0, 1, a, 0)); V.append((0, 0, 0, 1))
    U.append((0, 0, 1, 0)); V.append((0, 0, 0, 1))
    return np.array(U, dtype=np.int64), np.array(V, dtype=np.int64)


def cubic(P, p):
    """sum of the five cubes, d5 = -(d1 + d2 + d3 + d4); on {sum = 0} this is 3 e3"""
    d5 = (-P.sum(axis=-1)) % p
    return ((P ** 3).sum(axis=-1) + d5 ** 3) % p


def lines_on_cubic(p):
    U, V = all_lines(p)
    on = np.ones(len(U), dtype=bool)
    for Q in (U, V, (U + V) % p, (U - V) % p):        # a binary cubic vanishing at 4 points of the line vanishes on it
        on &= cubic(Q, p) == 0
    return U[on], V[on]


def full(v, p):
    return np.append(v, (-v.sum()) % p) % p


def meets(l1, l2, p):
    M = sympy.Matrix([list(l1[0]), list(l1[1]), list(l2[0]), list(l2[1])])
    return M.det() % p == 0


def in_a_plane(l, p):
    """the line lies in a Sylvester plane d_m = 0 when the m-th coordinate vanishes on both spanning vectors"""
    u, v = full(l[0], p), full(l[1], p)
    return any(u[m] == 0 and v[m] == 0 for m in range(5))


def permute(l, perm, p):
    """apply a permutation of the five coordinates to a line, returned as a pair of full 5-vectors"""
    u, v = full(l[0], p), full(l[1], p)
    return u[list(perm)], v[list(perm)]


def same_line(a, b, p):
    """two lines given by spanning 5-vectors are equal when their four vectors span a plane"""
    return rank_mod_p(sympy.Matrix([list(a[0]), list(a[1]), list(b[0]), list(b[1])]), p) == 2


def rank_mod_p(M, p):
    A = [[int(x) % p for x in row] for row in M.tolist()]
    rank, cols = 0, len(A[0])
    for c in range(cols):
        piv = next((r for r in range(rank, len(A)) if A[r][c]), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        iv = pow(A[rank][c], p - 2, p)
        A[rank] = [x * iv % p for x in A[rank]]
        for r in range(len(A)):
            if r != rank and A[r][c]:
                f = A[r][c]
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[rank])]
        rank += 1
    return rank


def double_six(lines, p):
    """the 12 lines: is their meeting graph two sixes, each of skew lines, every line meeting 5 of the other six?
    returns (ok, six A as indices)"""
    n = len(lines)
    G = [[i != j and meets(lines[i], lines[j], p) for j in range(n)] for i in range(n)]
    A = {0}
    B = {j for j in range(n) if G[0][j]}
    for i in range(1, n):
        if i not in B and not any(G[i][j] for j in A):
            A.add(i)
    B = set(range(n)) - A
    ok = len(A) == 6 and len(B) == 6
    ok &= all(not G[i][j] for i in A for j in A) and all(not G[i][j] for i in B for j in B)
    ok &= all(sum(G[i][j] for j in B) == 5 for i in A) and all(sum(G[i][j] for j in A) == 5 for i in B)
    return ok, A


def sign(perm):
    s, seen = 1, set()
    for i in range(len(perm)):
        if i in seen:
            continue
        j, c = i, 0
        while j not in seen:
            seen.add(j)
            j = perm[j]
            c += 1
        s *= (-1) ** (c - 1)
    return s


# ------------------------------------------------------------------ the cubics {sum x = sum x^3 = 0} in n variables
def cone_counts(p, ns=(5, 7, 9)):
    """N(n) = #{x in F_p^n: sum x = 0, sum x^3 = 0} for each n, exactly, by convolving the measure of (x, x^3) on F_p^2"""
    x = np.arange(p, dtype=np.int64)
    x3 = x ** 3 % p
    c = {1: np.zeros((p, p), dtype=np.int64)}
    c[1][x, x3] = 1
    top = max((n + 1) // 2 for n in ns)
    for k in range(2, top + 1):
        acc = np.zeros((p, p), dtype=np.int64)
        for s in range(p):
            acc += np.roll(c[k - 1], (s, int(x3[s])), axis=(0, 1))
        c[k] = acc
    neg = (-x) % p
    out = {}
    for n in ns:
        j = n // 2
        out[n] = int((c[j] * c[n - j][np.ix_(neg, neg)]).sum())
    return out


def projective(N, p):
    assert (N - 1) % (p - 1) == 0
    return (N - 1) // (p - 1)


def primitive_trace(n, Xp, p):
    """#X_n(F_p) minus the powers of the hyperplane class (X_n has dimension n - 3)"""
    return Xp - sum(p ** i for i in range(n - 2))


def singular_sign_points(n, p):
    """the singular points of {sum x = sum x^3 = 0} in P^(n-1) over F_p (p > 3): x_i^2 all equal, so x is a sign
    vector up to scale; it is singular exactly when its sum vanishes mod p.  Returned as sets of + positions."""
    out = []
    for k in range(n + 1):
        if (2 * k - n) % p == 0:
            out.extend(itertools.combinations(range(n), k))
    pts = set()
    for S in out:
        v = tuple(1 if i in S else -1 for i in range(n))
        w = tuple(-t for t in v)
        pts.add(min(v, w))
    return pts


def singular_brute(n, p):
    """the same by brute force over every point of P^(n-1) on the variety (small n, p)"""
    pts = []
    for v in itertools.product(range(p), repeat=n):
        if not any(v):
            continue
        first = next(t for t in v if t)
        if first != 1:
            continue
        if sum(v) % p or sum(t ** 3 for t in v) % p:
            continue
        sq = {t * t % p for t in v}
        if len(sq) == 1:
            pts.append(v)
    return pts


def verify():
    global LOG
    LOG = open(os.path.join(HERE, "coin_at_five_verify.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("coin_at_five.py -- the coin at 5 in the fifth moments: the dictionary, checked")
    # D1: the pentagon lies on the flat face, off the solid face
    ok = True
    for p in [q for q in primes(11, 101) if q % 5 == 1]:
        z = next(a for a in range(2, p) if pow(a, 5, p) == 1)
        pent = [pow(z, i, p) for i in range(5)]
        e = [1, 0, 0, 0, 0, 0]
        for t in pent:
            for j in range(5, 0, -1):
                e[j] = (e[j] + e[j - 1] * t) % p
        ok &= e[1] == e[2] == e[3] == e[4] == 0 and e[5] != 0
    check("D1. the regular pentagon (1, z, z^2, z^3, z^4) has e1 = e2 = e3 = e4 = 0 and e5 != 0: on the flat face "
          "(Clebsch's cubic, e3 = 0), off the solid face (e5 = 0)  (every p = 1 mod 5 to 101)", ok)
    # D2: each plane meets the cubic in three lines
    d1, d2, d3 = sympy.symbols("d1 d2 d3")
    d4 = -(d1 + d2 + d3)
    e3 = sum(a * b * c for a, b, c in itertools.combinations([d1, d2, d3, d4], 3))
    ok = sympy.expand(e3 + (d1 + d2) * (d1 + d3) * (d2 + d3)) == 0
    check("D2. on the plane d5 = 0 (with d1 + d2 + d3 + d4 = 0), e3 = -(d1 + d2)(d1 + d3)(d2 + d3): three lines, each "
          "the centre with two opposite pairs (0, a, -a, b, -b); five planes, 15 lines, the edge", ok)
    # D3: the 27 lines, the double six, and the flip
    ok_count, ok_edge, ok_six, ok_flip = True, True, True, True
    detail = []
    for p in primes(7, 31):
        U, V = lines_on_cubic(p)
        L = list(zip(U, V))
        planar = [l for l in L if in_a_plane(l, p)]
        golden = [l for l in L if not in_a_plane(l, p)]
        want = 27 if leg(5, p) == 1 else 15
        ok_count &= len(L) == want
        ok_edge &= len(planar) == 15
        detail.append(f"{p}:{len(L)}")
        if leg(5, p) == 1:
            ok6, A = double_six(golden, p)
            ok_six &= ok6
            sixA = [golden[i] for i in sorted(A)]
            fullgold = [(full(l[0], p), full(l[1], p)) for l in golden]
            for perm in itertools.permutations(range(5)):
                if perm == tuple(range(5)):
                    continue
                img = [permute(l, perm, p) for l in sixA]
                inA = all(any(same_line(im, (full(a[0], p), full(a[1], p)), p) for a in sixA) for im in img)
                inB = all(any(same_line(im, g, p) for g in fullgold) for im in img) and not any(
                    any(same_line(im, (full(a[0], p), full(a[1], p)), p) for a in sixA) for im in img)
                ok_flip &= (inA if sign(perm) == 1 else inB)
    check("D3a. lines on Clebsch's cubic over F_p: 27 when (5|p) = 1, 15 when (5|p) = -1  (every prime 7..31)",
          ok_count, " ".join(detail))
    check("D3b. exactly 15 of them lie in the Sylvester planes, at every p: the edge is rational", ok_edge)
    check("D3c. when (5|p) = 1 the other 12 form a double six: two sixes of skew lines, each line meeting 5 of the other", ok_six)
    check("D3d. the flip: every even permutation of the five points keeps each six, every odd one swaps them "
          "(all 119 non-identity permutations, at p = 11, 19, 29, 31)", ok_flip)
    # D4: the edge is the centre
    ok = True
    for p in (5, 7, 11, 13):
        br = singular_brute(5, p)
        ok &= (br == [(1, 1, 1, 1, 1)]) if p == 5 else (br == [])
    check("D4a. Clebsch's cubic is singular in characteristic 5 at the centre [1:1:1:1:1] alone, and smooth at 7, 11, 13 "
          "(brute force over every point)", ok)
    ok = True
    rows = []
    for n in (5, 7, 9):
        for p in (5, 7, 11, 13):
            pts = singular_sign_points(n, p)
            centre = tuple([-1] * n) in pts or tuple([1] * n) in pts
            ok &= centre == (n % p == 0)
            rows.append(f"n={n},p={p}:{len(pts)}{'*' if centre else ''}")
    ok &= singular_brute(7, 7) == [(1,) * 7]
    check("D4b. in n variables (p > 3) the singular points are the sign vectors whose sum vanishes mod p, and the centre "
          "[1:...:1] is singular exactly when p divides n: at 5 for n = 5, at 7 for n = 7, and never for n = 9, whose "
          "only prime is 3, where every one of these cubics degenerates (x^3 sums to (sum x)^3)  (* marks the centre)",
          ok, " ".join(rows))
    # the positive control for the test's counts
    ok = all(primitive_trace(5, projective(cone_counts(p, (5,))[5], p), p) == (5 + leg(5, p)) * p for p in primes(7, 61))
    check("D5. the exact count: #X5(F_p) = p^2 + (6 + (5|p))p + 1 for Clebsch's cubic, so its primitive trace is "
          "(5 + (5|p))p  (every prime 7..61)", ok)
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()
    sys.exit(1 if FAILS else 0)


# ------------------------------------------------------------------ round 19
PRED = dict(I5_5=3504, J5_5=-930, I5_3=368, J5_3=(-84, -192), J3_3=(-12, 0), J4_3=80)


def _cones(p):
    low_priority()
    return p, cone_counts(p, (5, 7, 9))


def test():
    """round 19 (PREREG.md): C0..C3"""
    global LOG
    LOG = open(os.path.join(HERE, "coin_at_five_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    import exact_moments as emo
    from multiprocessing import Pool
    say("Round 19: the coin at 5 -- its edge in the moments, and the coin at 7 (PREREG.md)")
    # C0, C1: the operators at the edge primes 3 and 5
    ops = {}
    for p in (3, 5):
        c, worst = emo.counts(p)
        ops[p] = c
        say(f"EDGE p={p}: " + " ".join(f"{k}={c[k]}" for k in "I2 J2 I3 J3 I4 J4 I5 J5 I6 J6".split()) + f"  worst {worst:.1e}")
    c0 = True
    for p in (3, 5):
        c = ops[p]
        c0 &= c["I2"] == p * (p * p - 1) and c["J2"] == p * p - 1 and c["I3"] == (p + 1) * (p - 1) * (2 * p + 1)
        c0 &= c["I4"] == 2 * p * p * (p - 1) * (p + 1)
    c0 &= ops[3]["J4"] == PRED["J4_3"] and ops[5]["J4"] == -96
    say(f"C0 the proved I2, J2, I3, I4 and Theorem 5's J4 (80 at 3, -96 at 5) at p = 3 and 5: {'HELD' if c0 else 'FAILED'}")
    r = {
        "I5 at 5 = 3504": ops[5]["I5"] == PRED["I5_5"],
        "J5 at 5 = -930": ops[5]["J5"] == PRED["J5_5"],
        "I5 at 3 = 368": ops[3]["I5"] == PRED["I5_3"],
    }
    for k, v in r.items():
        say(f"C1 {k}: {v}  (operators: {ops[5 if 'at 5' in k else 3][k[:2]]})")
    j53 = ops[3]["J5"]
    say(f"C1 J5 at 3: operators {j53}; with the equation's count (a_E(3) = -2): -84 {j53 == -84}; with the newform's "
        f"a(3) = 1: -192 {j53 == -192}")
    j33 = ops[3]["J3"]
    say(f"C1 J3 at 3: operators {j33}; the edge average -(1 - (-3|p))p(p + 1) = -12: {j33 == -12}; the p mod 3 form, 0: {j33 == 0}")
    c1 = all(r.values()) and j53 in PRED["J5_3"] and j33 in PRED["J3_3"]
    say(f"C1 {'HELD' if c1 else 'FAILED'}")
    # C2, C3: the cubics in 7 and 9 variables
    P = primes(11, 397)
    with Pool(4) as pool:
        cones = dict(pool.map(_cones, P))
    say("CONE p N5 N7 N9 t5 t7 t9")
    T = {}
    for p in P:
        N = cones[p]
        t = {n: primitive_trace(n, projective(N[n], p), p) for n in (5, 7, 9)}
        T[p] = t
        say(f"CONE {p} {N[5]} {N[7]} {N[9]} {t[5]} {t[7]} {t[9]}")
    ctrl = all(T[p][5] == (5 + leg(5, p)) * p for p in P)
    say(f"control: t5 = (5 + (5|p))p at every prime 11..397: {ctrl}")
    inert = [p for p in P if leg(-35, p) == -1]
    split = [p for p in P if leg(-35, p) == 1]
    bad_inert = [p for p in inert if T[p][7] % (p * p)]
    bad_split = [p for p in split if T[p][7] % (p * p) == 0]
    say(f"C2 t7 divisible by p^2 at every prime inert in Q(sqrt -35) ({len(inert)}): {not bad_inert} {bad_inert if bad_inert else ''}")
    say(f"C2 t7 not divisible by p^2 at every split prime ({len(split)}): {not bad_split} {bad_split if bad_split else ''}")
    c2 = not bad_inert and not bad_split and ctrl
    say(f"C2 {'HELD' if c2 else 'FAILED'}")
    # C3: a first look, not scored
    say("C3 (a first look, not scored)")
    for p in inert:
        say(f"  inert p={p}: t7/p^2 = {T[p][7] // (p * p)}   (5|p) = {leg(5, p)}, (-3|p) = {leg(-3, p)}, (-1|p) = {leg(-1, p)}, (2|p) = {leg(2, p)}")
    for p in split[:12]:
        say(f"  split p={p}: t7/p = {T[p][7] // p}, so t7/p mod p = {(T[p][7] // p) % p}")
    for p in P:
        q = T[p][9]
        say(f"  X9 p={p}: t9 = {q}, t9 mod p = {q % p}, mod p^2 = {q % (p * p)}, mod p^3 = {q % p ** 3}, p mod 9 = {p % 9}")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if mode == "verify":
        verify()
    elif mode == "test":
        test()
