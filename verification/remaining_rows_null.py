#!/usr/bin/env python3
"""remaining_rows_null.py -- the remaining rows of the foundation null-model audit.

Three gates per claim: TRUE (verified) -> SPECIFIC (random structures of the same kind do not
share it) -> NOT A READOUT (it does not follow in a few lines from the construction itself).

  (5) J04       sigma-magma rigidity: Aut = 1, congruence-simple, exactly 5 sub-magmas, 2-generated
  (6) J18 / F4  |Aut(V^BHML / F_p)| = (p-1)^2 and |idem| = p+3, "uniform across 24 primes"
  (7) J11       BHML's P56-anti part "lies in the 54 along a 9-vector with ||v||^2 = 13/4"
  (8) J19       the prime 11 divides exactly c2 and c8 of charpoly(TSML_RAW)
  (9) J22       the 70/71/72/73 HARMONY ladder and its "triple coincidence" at 71

    python verification/remaining_rows_null.py      (a few minutes)

See 04_meta/FOUNDATION_NULL_MODEL_AUDIT.md.
"""
import itertools
from collections import Counter

import numpy as np
from sympy import Matrix, factorint

from foundation_null_model import BHML, N, TSML, bhml_like, sym, tsml_like

rng = np.random.default_rng(20260924)
T_SYM, B = np.array(TSML), np.array(BHML)


def frac(xs):
    xs = list(xs)
    return sum(xs) / len(xs)


# =====================================================================================
# (5) J04 -- the sigma-magma x <> y = sigma((x + y) mod 10), an isotope of Z/10
# =====================================================================================
SIGMA = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
MEMB = np.array([[(s >> x) & 1 for x in range(N)] for s in range(1, 1 << N)], dtype=bool)


def isotope(pi):
    return np.array([[pi[(x + y) % N] for y in range(N)] for x in range(N)])


def generated(M, S):
    S = set(S)
    while True:
        new = {int(M[a][b]) for a in S for b in S} - S
        if not new:
            return S
        S |= new


def n_submagmas(M):
    A = MEMB[:, :, None] & MEMB[:, None, :]
    return int((~(A & ~MEMB[:, M])).all(axis=(1, 2)).sum())


def n_automorphisms(M):
    gens = next(S for k in (1, 2, 3, 4) for S in itertools.combinations(range(N), k)
                if len(generated(M, S)) == N)
    count = 0
    for imgs in itertools.product(range(N), repeat=len(gens)):
        f, ok = dict(zip(gens, imgs)), True
        grew = True
        while grew and ok:
            grew = False
            for a, b in itertools.product(list(f), repeat=2):
                c, fc = int(M[a][b]), int(M[f[a]][f[b]])
                if c in f:
                    if f[c] != fc:
                        ok = False
                        break
                else:
                    f[c] = fc
                    grew = True
        if ok and len(f) == N and len(set(f.values())) == N and \
                all(f[int(M[a][b])] == int(M[f[a]][f[b]]) for a in range(N) for b in range(N)):
            count += 1
    return count


def congruence_simple(M):
    for x, y in itertools.combinations(range(N), 2):
        parent = list(range(N))

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        queue = [(x, y)]
        while queue:
            u, v = queue.pop()
            ru, rv = find(u), find(v)
            if ru == rv:
                continue
            parent[ru] = rv
            for z in range(N):
                queue.append((int(M[u][z]), int(M[v][z])))
                queue.append((int(M[z][u]), int(M[z][v])))
        if len({find(u) for u in range(N)}) > 1:
            return False
    return True


def non_generating_pairs(M):
    return sum(len(generated(M, p)) < N for p in itertools.combinations(range(N), 2))


def j04_profile(M):
    return (n_automorphisms(M) == 1, congruence_simple(M), n_submagmas(M) == 5, non_generating_pairs(M) == 1)


def random_6cycle():
    pts = rng.choice(N, 6, replace=False)
    pi = list(range(N))
    for a, b in zip(pts, np.roll(pts, -1)):
        pi[a] = int(b)
    return pi


# =====================================================================================
# (6) J18 / F4 -- the 4-dim algebra V^BHML (basis e0, e2, e3, e4) over F_p
# =====================================================================================
V_BHML = [[-1, -1, -1, -1], [-1, 1, 2, -1], [-1, 2, 1, 3], [-1, -1, 3, -1]]    # -1 = zero product


def _prod(C, X, Y, p):
    out = np.zeros((max(len(X), len(Y)), 4), dtype=np.int64)
    for i in range(4):
        for j in range(4):
            if C[i][j] >= 0:
                out[:, C[i][j]] += X[:, i] * Y[:, j]
    return out % p


def idem_count(C, p):
    X = np.array(list(itertools.product(range(p), repeat=4)))
    return int((_prod(C, X, X, p) == X).all(axis=1).sum())


def aut_count(C, p):
    V = np.array(list(itertools.product(range(p), repeat=4)))
    cons = [(i, j, C[i][j]) for i in range(4) for j in range(i, 4)]
    count = 0

    def rec(g):
        nonlocal count
        c = len(g)
        if c == 4:
            if round(np.linalg.det(np.array(g, dtype=float))) % p != 0:
                count += 1
            return
        mask = np.ones(len(V), dtype=bool)
        for (i, j, k) in cons:
            if max(i, j, k) != c:
                continue
            X = V if i == c else np.repeat(np.array(g[i])[None], len(V), 0)
            Y = V if j == c else np.repeat(np.array(g[j])[None], len(V), 0)
            tgt = np.zeros_like(V) if k < 0 else (V if k == c else np.repeat(np.array(g[k])[None], len(V), 0))
            mask &= (_prod(C, X, Y, p) == tgt).all(axis=1)
        for v in V[mask]:
            if v.any():
                rec(g + [v])
    rec([])
    return count


def random_monomial_algebra():
    C = [[-1] * 4 for _ in range(4)]
    for i in range(1, 4):
        for j in range(i, 4):
            C[i][j] = C[j][i] = int(rng.integers(-1, 4))
    return C


def fits_quadratic(ps, vals):
    """does an integer-coefficient polynomial of degree <= 2 through the first 3 points hit the rest?"""
    c = np.polyfit(ps[:3], vals[:3], 2)
    if not np.allclose(c, np.round(c), atol=1e-6):
        return False
    return all(abs(np.polyval(np.round(c), q) - v) < 1e-6 for q, v in zip(ps[3:], vals[3:]))


# =====================================================================================
# (8) J19 -- the characteristic polynomial and the prime 11
# =====================================================================================
TSML_RAW = T_SYM.copy()
TSML_RAW[9][3], TSML_RAW[9][4] = 7, 3        # the digit string "0797377777" (row 9, digits 3 and 4 swapped)


def charpoly_coeffs(M):
    return [int(c) for c in Matrix(M.tolist()).charpoly().all_coeffs()[1:]]


def primes_dividing_exactly_two(M, lo=11, hi=100):
    cs = [c for c in charpoly_coeffs(M) if c != 0]
    return [p for p in range(lo, hi) if factorint(p).get(p) == 1 and sum(c % p == 0 for c in cs) == 2]


# =====================================================================================
# (9) J22 -- the ladder rungs
# =====================================================================================
YM = [1, 2, 3, 4, 5, 6, 8, 9]


def rungs(Tb, Bb):
    Tb, Bb = np.asarray(Tb), np.asarray(Bb)
    return (int((Tb == 7).sum()), int((Tb[1:, 1:] == 7).sum()), int((Tb != Bb).sum()),
            int(round(np.linalg.det(Bb[np.ix_(YM, YM)].astype(float)))))


def rule89_random_bhml():
    M = B.copy()
    for (a, b) in [(8, j) for j in range(1, 7)] + [(9, j) for j in range(1, 7)] + [(8, 8), (8, 9), (9, 9)]:
        v = int(rng.integers(0, N))
        M[a][b] = M[b][a] = v
    return M


def s6s7_random_tsml():
    """keep TSML's principled axioms S1-S5; draw S6/S7 (five exceptional positions + values) at random"""
    M = T_SYM.copy()
    free = [(i, j) for i in [1, 2, 3, 4, 5, 6, 8, 9] for j in [1, 2, 3, 4, 5, 6, 8, 9] if i < j]
    for (i, j) in free:
        M[i][j] = M[j][i] = 7
    for idx in rng.choice(len(free), 5, replace=False):
        i, j = free[idx]
        M[i][j] = M[j][i] = int(rng.choice([1, 2, 3, 4, 5, 6, 8, 9]))
    return M


def window4(r):
    return max(r) - min(r) <= 3


if __name__ == "__main__":
    print("=" * 78)
    print("FOUNDATION NULL-MODEL AUDIT -- the remaining rows")
    print("=" * 78)

    # ---------------- (5) J04 ----------------
    Msig = isotope(SIGMA)
    canon5 = (n_automorphisms(Msig), congruence_simple(Msig), n_submagmas(Msig), non_generating_pairs(Msig))
    assert canon5 == (1, True, 5, 1)
    print("(5) J04 sigma-magma  x<>y = sigma(x+y mod 10)")
    print(f"    canon: |Aut| = {canon5[0]}, congruence-simple = {canon5[1]}, sub-magmas = {canon5[2]}, "
          f"non-generating pairs = {canon5[3]}")
    S5 = 1500
    uni = [j04_profile(isotope(list(rng.permutation(N)))) for _ in range(S5)]
    cyc = [j04_profile(isotope(random_6cycle())) for _ in range(S5)]
    for label, prof in [("uniform pi in S10       ", uni), ("pi of sigma's cycle type", cyc)]:
        print(f"    {label}: P(Aut=1) = {frac(p[0] for p in prof):.3f}   P(simple) = {frac(p[1] for p in prof):.3f}   "
              f"P(5 sub-magmas) = {frac(p[2] for p in prof):.3f}   P(1 non-gen pair) = {frac(p[3] for p in prof):.3f}   "
              f"P(all four) = {frac(all(p) for p in prof):.3f}")
    print("    VERDICT: Aut = 1 and simplicity are GENERIC (the typical isotope of Z/10 has both);")
    print("             the exact sub-magma count and generating profile are readouts of sigma.\n")

    # ---------------- (6) J18 / F4 ----------------
    print("(6) J18/F4  V^BHML over F_p (basis e0,e2,e3,e4; e2^2=e2, e2e3=e3, e3^2=e2, e3e4=e4, rest 0)")
    for p in (3, 5, 7):
        a, i = aut_count(V_BHML, p), idem_count(V_BHML, p)
        assert (a, i) == ((p - 1) ** 2, p + 3)
        print(f"    p={p}: |Aut| = {a} = (p-1)^2   |idem| = {i} = p+3")
    for p in (11, 13):
        assert idem_count(V_BHML, p) == p + 3
    print("    READOUT (a few lines, any odd p): Ann = <e0> and e4 enter the products only linearly ->")
    print("      two free scalings -> (p-1)^2. Idempotents: x0 = 0, 2*x2*x3 = x3, x2^2 + x3^2 = x2,")
    print("      (2*x3 - 1)*x4 = 0 -> {0, e2} + {x3 = -1/2} + a LINE {x3 = +1/2, x4 free} = p + 3.")
    ps = [3, 5, 7, 11, 13]
    algs = [random_monomial_algebra() for _ in range(300)]
    idem_poly = frac(fits_quadratic(ps, [idem_count(C, q) for q in ps]) for C in algs)
    print(f"    random monomial 4-dim algebras (e0 annihilating, products 0 or a basis vector):")
    print(f"      |idem| is an integer polynomial in p across p = 3,5,7,11,13 for {idem_poly:.3f} of them")
    print("    VERDICT: uniform closed forms are GENERIC for algebras with 0/1 structure constants;")
    print("             the particular exponents are READOUTS of the 4x4 table.\n")

    # ---------------- (7) J11 ----------------
    P = np.eye(N)
    P[[5, 6]] = P[[6, 5]]
    Banti = (B - P @ B @ P) / 2
    nz = int((np.abs(Banti) > 1e-12).sum())
    fro2 = float((Banti ** 2).sum())
    assert nz == 26 and abs(fro2 - 6.5) < 1e-12 and abs(np.trace(Banti)) < 1e-12
    diff = [j for j in range(N) if j not in (5, 6) and B[5][j] != B[6][j]]
    print("(7) J11  BHML's P56-anti part  (B - P56 B P56)/2")
    print(f"    canon: {nz} nonzero entries, all +-1/2 -> ||.||_F^2 = {fro2} = 13/2; J11's ||v||^2 = 13/4 is")
    print(f"    this with the half-trace norm. The 26 = rows/cols 5 and 6 of BHML differing at columns {diff}")
    print("    (x2 rows, x2 columns) + the 2 diagonal cells: 4*6 + 2 = 26.")
    traceless = frac(abs(np.trace((M - P @ M @ P) / 2)) < 1e-12 for M in (sym(rng.integers(0, N, (N, N))) for _ in range(500)))
    vals = Counter(float((((M - P @ M @ P) / 2) ** 2).sum() / 2) for M in (rule89_random_bhml() for _ in range(2000)))
    print(f"    'lies in the 54' (traceless): random symmetric tables P = {traceless:.3f} -- automatic")
    print(f"    Rule 89 random: P(||v||^2 = 13/4) = {vals.get(3.25, 0) / 2000:.3f}  (value set by Rule 89's cols 8,9)")
    print("    VERDICT: membership in the 54 is GENERIC; the value 13/4 is a READOUT (a cell count of rows 5,6).\n")

    # ---------------- (8) J19 ----------------
    J19_SYM = TSML_RAW.copy()
    J19_SYM[3][9] = J19_SYM[9][4] = 7                 # J19's "T_SYM": BOTH asymmetric cells set to 7
    cs_raw, cs_sym, cs_j19 = charpoly_coeffs(TSML_RAW), charpoly_coeffs(T_SYM), charpoly_coeffs(J19_SYM)
    div11 = lambda cs: [i + 1 for i, c in enumerate(cs) if c != 0 and c % 11 == 0]
    assert div11(cs_raw) == [2, 8] and cs_raw[1] == 33 and div11(cs_sym) == [7]
    assert cs_j19[1] == -23 and div11(cs_j19) == [] and (J19_SYM == J19_SYM.T).all()
    print("(8) J19  charpoly(TSML_RAW) and the prime 11")
    print(f"    TSML_RAW: 11 divides exactly c2 = {cs_raw[1]} and c8 = {cs_raw[7]} (J19's theorem -- true)")
    print(f"    the ORIGINAL table (ck.h, = canonical TSML): 11 divides only c7 = {cs_sym[6]}")
    print(f"    J19's comparison 'T_SYM' (c2 = {cs_j19[1]}, no 11) is neither symmetrization of RAW nor the original:")
    print("      it sets BOTH asymmetric cells to 7, deleting TSML's exceptional cell (3,9).")
    print("    PROVENANCE: TSML_RAW differs from the original only in row 9, digits 3 and 4 swapped")
    print("      ('0797377777'). The ck repository's first commit (2026-03-03, ck.h) has the symmetric row {0,7,9,3,7,...};")
    print("      the swapped digit string first appears 2026-04-25, when the table was retyped for the so(10)")
    print("      sprint. The 'wobble' is a transcription error.")
    typos = []
    for r in range(N):
        for c in range(N - 1):
            M = T_SYM.copy()
            if M[r][c] != M[r][c + 1]:
                M[r][c], M[r][c + 1] = M[r][c + 1], M[r][c]
                typos.append(M)
    tp = [bool(primes_dividing_exactly_two(M)) for M in typos]
    unif = [bool(primes_dividing_exactly_two(rng.integers(0, N, (N, N)))) for _ in range(300)]
    print(f"    every single adjacent-digit swap in TSML_SYM ({len(typos)} typos): P(some prime 11..97 divides")
    print(f"      exactly two charpoly coefficients) = {frac(tp):.3f};  uniform random 10x10 tables: {frac(unif):.3f}")
    print("    VERDICT: TRANSCRIPTION ARTIFACT -- the prime 11 is a property of a typo, and typos routinely")
    print("             produce such a prime.\n")

    # ---------------- (9) J22 ----------------
    canon9 = rungs(T_SYM, B)
    assert canon9 == (73, 71, 71, 70)
    print("(9) J22  the HARMONY ladder: HARM(T), HARM(T on 1..9), |T != B|, det(B on {1..6,8,9})")
    print(f"    canon: {canon9}.  HARM(T on 1..9) = HARM(T) - 2 is forced by S2 (VOID absorbs except (0,7)).")
    R = 3000
    for label, gen in [("matched pairs            ", lambda: (tsml_like(), bhml_like())),
                       ("real TSML x Rule-89-rand ", lambda: (T_SYM, rule89_random_bhml())),
                       ("S6/S7-rand TSML x BHML   ", lambda: (s6s7_random_tsml(), B))]:
        rs = [rungs(*gen()) for _ in range(R)]
        print(f"    {label}: P(|T!=B| in 70..73) = {frac(70 <= r[2] <= 73 for r in rs):.3f}   "
              f"P(|T!=B| = HARM-2) = {frac(r[2] == r[0] - 2 for r in rs):.3f}   "
              f"P(det in 70..73) = {frac(70 <= r[3] <= 73 for r in rs):.3f}   P(4 rungs in a 4-window) = "
              f"{frac(window4(r) for r in rs):.3f}")
    print("    VERDICT: NUMEROLOGY -- a juxtaposition of unlike numbers with no mechanism: 73 is S5's defined")
    print("             count; 71 = 73 - 2 is forced by S2; |T != B| = 71 recurs in ~13% of redraws of TSML's")
    print("             listed cells; det = 70 holds for none of the Rule-89 redraws -- one integer, read as")
    print("             C(8,4) (J18 itself calls it an integer coincidence).")
    print("=" * 78)
