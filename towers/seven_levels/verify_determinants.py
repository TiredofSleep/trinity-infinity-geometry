"""verify_determinants.py -- checks DETERMINANTS.md, Theorem 8: the determinant of every Airy piece V_k is the Jacobi
symbol (p/A_k), where A_k is the product of the odd numbers up to k, each multiple of 3 divided by 3 once.

    "2 and 3, the proof first"  -- the author, 16 November 2026

The proof has seven steps; each is checked here where a computer can check it.
  D1. V_k is the antisymmetric part of the cubic X_k's primitive cohomology: the Jacobian ring
      R = Q[x_1..x_n]/(e1, x_i^2 - x_j^2) has R^{S_n} = Q[t]/(t^((n+1)/2)) and no antisymmetric part (n = 3 to 9).
  D2. Griffiths' residues turn the symmetric part of R into the antisymmetric part of H^(n-3), and its classical
      degrees give exactly Sabbah and Yu's classical types (n up to 401).
  D3. The singular points: mod l >= 5, the sign vectors whose sum is a multiple of l; mod 3 in the good model
      e1 = e3 = 0, those whose sum is a multiple of 9; mod 2, none (brute force).
  D4. Every one is an ordinary double point: the Hessian is nondegenerate on the tangent space (n up to 61).
  D5. The critical value at the node of sum j is j(j - 2)/(j - 1)^2 (a third of it for e3), so its valuation is
      v_l(j) for l >= 5 and v_3(j) - 1 at 3 (n up to 41).
  D6. A transposition fixing a node acts on its tangent space with determinant -1, so the stabilizer acts on the
      vanishing cycle by the sign character, and each orbit of nodes gives the antisymmetric part one vanishing cycle.
  D7. Picard-Lefschetz's input: an affine quadric Q(y) = c in an odd number of variables has
      q^(N-1) + eta((-1)^((N-1)/2) c det Q) q^((N-1)/2) points, so Galois acts on its vanishing class by the quadratic
      character of c, and inertia sees only v(c) mod 2.
  D8. Assembly: the ramified set gives D_k = prod of l*, which is 1 mod 4 (unramified at 2) and is (p/A_k).
  D9. The identification with what was measured: at k = 5 and 7, the trace of Frobenius on the antisymmetric part,
      computed from twisted point counts (Frobenius composed with every permutation), equals T_k(p)/p^2, and the
      symmetric part's trace is 0.
  D10. Corollary: complex conjugation fixes the middle class of every V_k, k = 1 (mod 4), twisted to weight 0.

numpy + sympy + edge_rule.py.  ASCII output; writes verify_determinants.log and exits with 1 if a check fails.
Run:  python verify_determinants.py      (a few minutes)
"""
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
from sympy.combinatorics import Permutation
from sympy.utilities.iterables import partitions

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edge_rule as er  # noqa: E402  (sets below-normal priority on import, through coin_at_five)

LOG = open(os.path.join(HERE, "verify_determinants.log"), "w", encoding="utf-8")
FAILS = []


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def check(name, ok, detail=""):
    say(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


def rank_mod(M, l):
    """rank of an integer matrix mod a prime l, by Gaussian elimination"""
    A = [[v % l for v in row] for row in M]
    r, rows = 0, len(A)
    cols = len(A[0]) if rows else 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], l - 2, l)
        A[r] = [(inv * v) % l for v in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(a - f * b) % l for a, b in zip(A[i], A[r])]
        r += 1
    return r


# ------------------------------------------------------------------ D1: the Jacobian ring
def jacobian_ring_dims(n, emax):
    """R' = Q[t] (x) squarefree monomials x_S, with x_i^2 = t; R = R'/(e1 R'). Returns, for each degree e, dim R_e,
    dim of its symmetric part, and whether every antisymmetrization of a basis monomial of R'_e vanishes."""
    basis = {e: [(a, S) for a in range(e // 2 + 1) for S in itertools.combinations(range(n), e - 2 * a)]
             for e in range(emax + 1)}
    index = {e: {b: i for i, b in enumerate(basis[e])} for e in basis}

    def times_e1(a, S):
        out = {}
        Sset = set(S)
        for i in range(n):
            if i in Sset:
                key = (a + 1, tuple(sorted(Sset - {i})))
            else:
                key = (a, tuple(sorted(Sset | {i})))
            out[key] = out.get(key, 0) + 1
        return out

    res = {}
    for e in range(emax + 1):
        rows = []
        if e >= 1:
            for (a, S) in basis[e - 1]:
                row = [0] * len(basis[e])
                for key, c in times_e1(a, S).items():
                    row[index[e][key]] += c
                rows.append(row)
        rk = rank_mod(rows, 1000003) if rows else 0
        dim = len(basis[e]) - rk
        # symmetric part: spanned by t^a e_s; its image under e1 comes from t^a e_s in degree e - 1
        sym_basis = [(a, e - 2 * a) for a in range(e // 2 + 1) if e - 2 * a <= n]
        img = []
        if e >= 1:
            for a in range((e - 1) // 2 + 1):
                s = e - 1 - 2 * a
                if s > n:
                    continue
                row = {}
                for S in itertools.combinations(range(n), s):
                    for key, c in times_e1(a, S).items():
                        row[key] = row.get(key, 0) + c
                # express in the symmetric basis: coefficient of t^a' e_s' is the coefficient of any one monomial
                img.append([row.get((aa, tuple(range(ss))), 0) for aa, ss in sym_basis])
        sym_dim = len(sym_basis) - (rank_mod(img, 1000003) if img else 0)
        # antisymmetrization of x_S vanishes when a transposition fixes S (two indices both in S or both outside)
        anti = all((len(S) >= 2 or n - len(S) >= 2) for (_, S) in basis[e]) if n >= 3 else False
        res[e] = (dim, sym_dim, anti)
    return res


def antisym_zero_bruteforce(n, e):
    """antisymmetrize every basis monomial t^a x_S of R'_e over S_n explicitly and check that it is 0"""
    for a in range(e // 2 + 1):
        s = e - 2 * a
        if s > n:
            continue
        for S in itertools.combinations(range(n), s):
            acc = {}
            for perm in itertools.permutations(range(n)):
                sign = Permutation(list(perm)).signature()
                key = tuple(sorted(perm[i] for i in S))
                acc[key] = acc.get(key, 0) + sign
            if any(acc.values()):
                return False
    return True


# ------------------------------------------------------------------ D3: singular points by brute force
def singular_naive(n, l):
    """the singular F_l-points of X_n = {sum x = sum x^3 = 0} in P^(n-1): on X, with (3x_i^2) a multiple of (1..1)"""
    pts = set()
    for x in itertools.product(range(l), repeat=n - 1):
        v = list(x) + [(-sum(x)) % l]
        if not any(v):
            continue
        if sum(t ** 3 for t in v) % l:
            continue
        g = {(3 * t * t) % l for t in v}
        if len(g) == 1:
            lead = next(t for t in v if t)
            inv = pow(lead, l - 2, l)
            pts.add(tuple((inv * t) % l for t in v))
    return pts


def sign_vectors(n, step, l):
    """projective sign vectors whose sum is a multiple of step, normalized mod l"""
    out = set()
    for bits in itertools.product((1, -1), repeat=n):
        if sum(bits) % step == 0:
            lead = bits[0]
            out.add(tuple((lead * b) % l for b in bits))
    return out


def gf4_singular_free(n):
    """X_n has no singular point over F_4 (F_4 = {0, 1, w, w^2}, w^2 = w + 1), checked by brute force"""
    add = lambda a, b: a ^ b  # noqa: E731  elements as 2-bit vectors in the basis 1, w
    def mul(a, b):
        # (a0 + a1 w)(b0 + b1 w) with w^2 = w + 1
        a0, a1, b0, b1 = a & 1, a >> 1, b & 1, b >> 1
        c0 = (a0 & b0) ^ (a1 & b1)
        c1 = (a0 & b1) ^ (a1 & b0) ^ (a1 & b1)
        return c0 | (c1 << 1)
    for x in itertools.product(range(4), repeat=n):
        if not any(x):
            continue
        s = 0
        for t in x:
            s = add(s, t)
        if s:
            continue
        c = 0
        for t in x:
            c = add(c, mul(mul(t, t), t))
        if c:
            continue
        if len({mul(t, t) for t in x}) == 1:  # 3 x_i^2 = x_i^2 in characteristic 2
            return False
    return True


# ------------------------------------------------------------------ D4: ordinary double points
def odp_rank_naive(n, j, l):
    """rank mod l of the Hessian form sum eps_i y_i^2 on W = {sum y = 0}, in the basis e_i - e_n: it is n - 2 exactly
    when the only degenerate direction is eps itself (an ordinary double point)"""
    eps = [1] * ((n + j) // 2) + [-1] * ((n - j) // 2)
    G = [[(eps[i] if i == k else 0) + eps[n - 1] for k in range(n - 1)] for i in range(n - 1)]
    return rank_mod(G, l)


def odp_rank_e3(n, j):
    """the same for e3 mod 3: its Hessian at the node is H_ik = -(eps_i + eps_k) off the diagonal (e1 = j = 0 mod 3) and 0
    on it; in the basis e_i - e_n of W the form is G_ik = H_ik - H_in - H_kn (i != k), G_ii = -2 H_in"""
    eps = [1] * ((n + j) // 2) + [-1] * ((n - j) // 2)
    H = lambda a, b: 0 if a == b else -(eps[a] + eps[b])  # noqa: E731
    G = [[(H(i, k) - H(i, n - 1) - H(k, n - 1)) if i != k else -2 * H(i, n - 1) for k in range(n - 1)]
         for i in range(n - 1)]
    return rank_mod(G, 3)


# ------------------------------------------------------------------ D6: the stabilizer on the tangent space
def det_on_W(perm):
    """the determinant of a permutation of coordinates acting on W = {sum y = 0}, in the basis e_i - e_n"""
    n = len(perm)
    cols = []
    for i in range(n - 1):
        img = [0] * n
        img[perm[i]] += 1
        img[perm[n - 1]] -= 1
        # write img (which lies in W) in the basis e_k - e_n: coefficient of e_k for k < n
        cols.append(img[: n - 1])
    return int(sympy.Matrix(cols).T.det())


# ------------------------------------------------------------------ D7: affine quadrics
def quadric_dist(p, coeffs):
    """the number of y in F_p^N with sum a_i y_i^2 = c, for every c, by brute force (p prime)"""
    sq = [0] * p
    for y in range(p):
        sq[(y * y) % p] += 1
    # convolution of the value distributions of a_i y_i^2
    dist = [1] + [0] * (p - 1)
    for a in coeffs:
        nd = [0] * p
        for v in range(p):
            if dist[v]:
                for s in range(p):
                    if sq[s]:
                        nd[(v + a * s) % p] += dist[v] * sq[s]
        dist = nd
    return dist


# ------------------------------------------------------------------ D9: twisted point counts over F_(p^c)
def trace_histogram(p, c, chunk=1 << 19):
    """H[a, b] = #{y in F_(p^c) : Tr y = a, Tr y^3 = b}, by enumerating the field in chunks"""
    if c == 1:
        H = np.zeros((p, p), dtype=np.int64)
        for y in range(p):
            H[y % p, pow(y, 3, p)] += 1
        return H
    X = sympy.symbols("X")
    f = None
    for coeffs in itertools.product(range(p), repeat=c):
        cand = sympy.Poly([1] + list(coeffs), X, modulus=p)
        if coeffs[-1] and cand.is_irreducible:
            f = [int(v) % p for v in reversed(cand.all_coeffs())]  # f[0] + ... + f[c] X^c, f[c] = 1
            break
    low = f[:c]  # X^c = -sum low_i X^i
    # power sums Tr(X^i), i < 2c - 1, from the companion matrix
    C = sympy.zeros(c, c)
    for i in range(1, c):
        C[i, i - 1] = 1
    for i in range(c):
        C[i, c - 1] = -low[i]
    s, M = [], sympy.eye(c)
    for _ in range(c):
        s.append(int(M.trace()) % p)
        M = (M * C).applyfunc(lambda v: v % p)
    s = np.array(s, dtype=np.int64)

    def mul(A, B):
        prod = [np.zeros(A.shape[1], dtype=np.int64) for _ in range(2 * c - 1)]
        for i in range(c):
            for k in range(c):
                prod[i + k] = (prod[i + k] + A[i] * B[k]) % p
        for d in range(2 * c - 2, c - 1, -1):
            top = prod[d]
            for i in range(c):
                if low[i]:
                    prod[d - c + i] = (prod[d - c + i] - low[i] * top) % p
        return np.array(prod[:c])

    q = p ** c
    H = np.zeros(p * p, dtype=np.int64)
    for start in range(0, q, chunk):
        idx = np.arange(start, min(q, start + chunk), dtype=np.int64)
        Y = np.array([(idx // p ** i) % p for i in range(c)])
        Y3 = mul(mul(Y, Y), Y)
        tr = (s[:, None] * Y).sum(axis=0) % p
        tr3 = (s[:, None] * Y3).sum(axis=0) % p
        H += np.bincount(tr * p + tr3, minlength=p * p)
    return H.reshape(p, p)


def conv2(A, B, p):
    """cyclic convolution on (Z/p)^2"""
    out = np.zeros((p, p), dtype=object)
    for a in range(p):
        for b in range(p):
            if A[a, b]:
                out += int(A[a, b]) * np.roll(np.roll(B.astype(object), a, axis=0), b, axis=1)
    return out


def isotypic_traces(k, p):
    """the traces of Frobenius on the antisymmetric and on the symmetric parts of H^(k-3)_prim(X_k), from the
    Lefschetz numbers of Frobenius composed with each permutation, grouped by cycle type"""
    H = {c: trace_histogram(p, c) for c in range(1, k + 1)}
    m = k - 3
    anti = sym = Fraction(0)
    for lam in partitions(k):
        parts = [c for c, mult in lam.items() for _ in range(mult)]
        size = math.factorial(k)
        for c, mult in lam.items():
            size //= c ** mult * math.factorial(mult)
        sign = (-1) ** (k - len(parts))
        acc = None
        for c in parts:
            acc = H[c].astype(object) if acc is None else conv2(acc, H[c], p)
        N = int(acc[0, 0])
        fix = Fraction(N - 1, p - 1)
        tr = fix - sum(Fraction(p) ** i for i in range(m + 1))
        anti += size * sign * tr
        sym += size * tr
    return anti / math.factorial(k), sym / math.factorial(k)


def main():
    t0 = time.time()
    say("verify_determinants.py -- DETERMINANTS.md, Theorem 8: det V_k = (p/A_k)")

    # D1
    rows, ok = [], True
    for n in (3, 5, 7, 9):
        res = jacobian_ring_dims(n, n + 1)
        dims_ok = all(res[e][0] == (math.comb(n - 1, e) if e <= n - 1 else 0) for e in res)
        sym_ok = all(res[e][1] == (1 if e % 2 == 0 and e <= n - 1 else 0) for e in res)
        anti_ok = all(res[e][2] for e in res)
        ok &= dims_ok and sym_ok and anti_ok
        rows.append(f"n={n}: dims {[res[e][0] for e in sorted(res)]}, symmetric {[res[e][1] for e in sorted(res)]}")
    brute = all(antisym_zero_bruteforce(n, e) for n in (3, 5) for e in range(n + 1))
    check("D1. the Jacobian ring R = Q[x]/(e1, x_i^2 - x_j^2) of the cubic on the hyperplane has dim R_e = C(n-1, e) "
          "(a smooth cubic), its symmetric part is one line in each even degree up to n - 1 (Q[t]/(t^((n+1)/2))), and it "
          "has no antisymmetric part (n = 3, 5, 7, 9; antisymmetrizations also done by brute force at n = 3, 5)",
          ok and brute, "; ".join(rows))

    # D2
    ok = True
    for n in range(1, 402, 2):
        js = [j for j in range(0, (n - 1) // 2 + 1) if (2 * j - (4 - n)) % 3 == 0]
        types = sorted(((n + 2 * (j + 1)) // 3, n + 1 - (n + 2 * (j + 1)) // 3) for j in js)
        ok &= types == sorted(er.classical_hodge(n))
    check("D2. Griffiths' residues (the volume form of the hyperplane changes sign under odd permutations) send R's "
          "symmetric part to the antisymmetric part of H^(n-3); its degrees 2j with 2j = 4 - n (mod 3) give exactly "
          "Sabbah and Yu's classical types, (n + 2j + 2)/3, for every odd n up to 401", ok)

    # D3
    rows, ok = [], True
    for n, l in ((5, 5), (7, 5), (9, 5), (7, 7), (5, 7)):
        got, want = singular_naive(n, l), sign_vectors(n, l, l)
        ok &= got == want
        rows.append(f"X{n} mod {l}: {len(got)}")
    for n in range(3, 14, 2):
        got = er.singular_e3(n)
        want = sign_vectors(n, 9, 3)
        ok &= got == want
        rows.append(f"good model n={n} mod 3: {len(got)}")
    ok2 = all(gf4_singular_free(n) for n in (3, 5, 7))
    check("D3. the singular points, by brute force: mod l >= 5 exactly the sign vectors whose sum is a multiple of l; "
          "mod 3, in the good model e1 = e3 = 0, exactly those whose sum is a multiple of 9; mod 2, none (over F_4, "
          "n = 3, 5, 7)", ok and ok2, "; ".join(rows))

    # D4
    bad = []
    for n in range(5, 62, 2):
        for l in er.primes(5, n):
            for j in range(l, n + 1, 2 * l):
                if odp_rank_naive(n, j, l) != n - 2:
                    bad.append((n, j, l))
        for j in range(9, n + 1, 18):
            if odp_rank_e3(n, j) != n - 2 or (n <= 21 and er.hessian_rank_e3(n, j)[0] != n - 2):
                bad.append((n, j, 3))
    check("D4. every node is an ordinary double point: the Hessian has rank n - 2 on the tangent space (mod l >= 5 for "
          "the cubic, mod 3 for e3), for every node of every X_n with n up to 61 (and e3's Hessian as round 25 "
          "computed it, n up to 21)", not bad, f"failures {bad[:5]}")

    # D5
    bad = []
    for n in range(3, 42, 2):
        for j in range(1, n + 1, 2):
            if j == 1:
                continue
            for model in ("p3", "e3"):
                if er.critical_value_direct(n, j, model) != er.critical_value(j, model):
                    bad.append((n, j, model))
    vals_ok = all(er.fval(er.critical_value(j, "p3"), l) == er.val(j, l)
                  for l in er.primes(5, 199) for j in range(l, 400, 2 * l))
    vals_ok &= all(er.fval(er.critical_value(j, "e3"), 3) == er.val(j, 3) - 1 for j in range(9, 400, 18))
    check("D5. the critical value at the node of sum j is j(j - 2)/(j - 1)^2 for the cubic and a third of it for e3 "
          "(exact, n up to 41); its valuation is v_l(j) at l >= 5 and v_3(j) - 1 at 3 (j up to 400)",
          not bad and vals_ok, f"failures {bad[:3]}")

    # D6
    ok = True
    for n in range(3, 12, 2):
        for a in range(n + 1):
            b = n - a
            for blk in ((0, 1), (a, a + 1)):
                i, k = blk
                if k >= (a if blk == (0, 1) else n) or i == k:
                    continue
                perm = list(range(n))
                perm[i], perm[k] = perm[k], perm[i]
                ok &= det_on_W(perm) == -1
    check("D6. a transposition that fixes a node (two plus signs or two minus signs swapped) acts on the hyperplane "
          "W, and so on the tangent space W/<eps>, with determinant -1 (n up to 11). So the stabilizer S_a x S_b acts on "
          "the vanishing cycle by the sign character, and by Frobenius reciprocity each orbit of nodes gives the "
          "antisymmetric part exactly one vanishing cycle", ok)

    # D7
    ok = True
    for p in (5, 7, 11):
        for N in (3, 5):
            forms = list(itertools.product(range(1, p), repeat=N))[:: 7 if N == 5 else 1]
            for coeffs in forms:
                dist = quadric_dist(p, coeffs)
                detq = math.prod(coeffs)
                for c in range(1, p):
                    want = p ** (N - 1) + er.leg(((-1) ** ((N - 1) // 2)) * c * detq, p) * p ** ((N - 1) // 2)
                    ok &= dist[c] == want
    check("D7. an affine quadric Q(y) = c in N = 3 or 5 variables has q^(N-1) + eta((-1)^((N-1)/2) c det Q) q^((N-1)/2) "
          "points (p = 5, 7, 11, every c, a sample of diagonal forms): Galois acts on its vanishing class by the "
          "quadratic character of c, so inertia at l sees only v_l(c) mod 2", ok)

    # D8
    ok = all(er.det_from_nodes(k) == er.star_kernel(er.airy_double_factorial(k)) for k in range(1, 302, 2))
    ok &= all(er.star_kernel(er.airy_double_factorial(k)) % 4 == 1 for k in range(1, 2002, 2))
    known = {**er.MEASURED_DET, 17: -51051, 19: 969969, 21: -138567, 23: 3187041, 25: 3187041, 27: 3187041}
    ok &= all(er.star_kernel(er.airy_double_factorial(k)) == D for k, D in known.items())
    check("D8. assembly: D_k = the product of the signed primes with an odd number of thin node orbits is (p/A_k) for "
          "every odd k up to 301, is 1 mod 4 for every odd k up to 2001 (so unramified at 2, which fixes its sign), "
          "and equals every determinant measured, k = 1 to 27", ok)

    # D9
    rows, ok = [], True
    for k, ps in ((5, (7, 11, 13)), (7, (11,))):
        for p in ps:
            anti, sym = isotypic_traces(k, p)
            T = er.airy(p, er.t_values(p, tuple(range(3, k + 1, 2))))
            good = anti == T[k] / p ** 2 and sym == 0
            ok &= good
            rows.append(f"k={k} p={p}: antisymmetric {anti}, T_k/p^2 {T[k] / p ** 2}, symmetric {sym}")
    check("D9. the measured pieces are the antisymmetric parts: from the twisted counts #{x : Frob(x) = sigma(x)} for "
          "every cycle type, the trace of Frobenius on the antisymmetric part of H^(k-3)_prim(X_k) equals T_k(p)/p^2, "
          "and the symmetric part's is 0 (k = 5 at p = 7, 11, 13; k = 7 at p = 11)", ok, "; ".join(rows))

    # D10
    rows = er.sign_run(20001)
    ok = all(a == b for _, a, b in rows)
    mids = sum(1 for k, _, _ in rows if k % 4 == 1)
    check(f"D10. corollary: with D_k proved, complex conjugation acts on V_k twisted to weight 0 with determinant "
          f"sign(D_k), which is (-1)^(Hodge pairs) at every odd k up to 20001. So it fixes the middle class at each of "
          f"the {mids} values k = 1 (mod 4)", ok)

    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
    LOG.close()
    sys.exit(0 if not FAILS else 1)


if __name__ == "__main__":
    main()
