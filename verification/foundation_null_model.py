#!/usr/bin/env python3
"""foundation_null_model.py -- does the foundation's structure beat random tables?

Every PROVED claim about TSML/BHML is a true statement about two specific 10x10
tables. Truth is not the question; SIGNIFICANCE is. This script asks, for each
headline structural claim: among random tables of the same kind, how often does
the property also hold? A property that nearly all random tables share is forced
by the construction (or by N = 10), not by TIG. One that random tables almost
never share is genuinely specific. See 04_meta/FOUNDATION_NULL_MODEL_AUDIT.md.

    python verification/foundation_null_model.py      (~30-60 s)

Three gates for a structural claim: TRUE (verified) -> SPECIFIC (random tables of the
same kind do not share it) -> NOT A READOUT (it survives a null that keeps the tables'
own construction rules). Sections (1)-(2) are gate 2; section (3) is gate 3.
The attractor row is in verification/attractor_null_census.py.

Null models (all seeded, reproducible):
  uniform   -- entries uniform on {0..9}
  matched   -- TSML-like (symmetric, ~73% HARMONY=7, 7 absorbing, 0-row/col -> 0)
               x BHML-like (symmetric, 0 a two-sided identity)
"""
import itertools
import numpy as np

N = 10
TSML = [[0,0,0,0,0,0,0,7,0,0],[0,7,3,7,7,7,7,7,7,7],[0,3,7,7,4,7,7,7,7,9],
        [0,7,7,7,7,7,7,7,7,3],[0,7,4,7,7,7,7,7,8,7],[0,7,7,7,7,7,7,7,7,7],
        [0,7,7,7,7,7,7,7,7,7],[7,7,7,7,7,7,7,7,7,7],[0,7,7,7,8,7,7,7,7,7],
        [0,7,9,3,7,7,7,7,7,7]]
BHML = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,2,6,6],[2,3,3,4,5,6,7,3,6,6],
        [3,4,4,4,5,6,7,4,6,6],[4,5,5,5,5,6,7,5,7,7],[5,6,6,6,6,6,7,6,7,7],
        [6,7,7,7,7,7,7,7,7,7],[7,2,3,4,5,6,7,8,9,0],[8,6,6,6,7,7,7,9,7,8],
        [9,6,6,6,7,7,7,0,8,0]]
FLOW = [1, 2, 3, 4, 6, 8]


# ---------- Lie closure of antisymmetrized left-multiplication operators (the J09 construction) ----------
def antisym(T, i):
    M = np.zeros((N, N))
    for j in range(N):
        M[T[i][j], j] = 1
    return M - M.T            # always an element of so(10), by construction


def closure_dim(gens, tol=1e-8, max_rounds=25):
    Q, elems = [], []

    def add(m):
        v = m.flatten().astype(float)
        for q in Q:
            v = v - np.dot(q, v) * q
        n = np.linalg.norm(v)
        if n > tol:
            Q.append(v / n)
            elems.append(m / np.linalg.norm(m))
            return True
        return False

    for g in gens:
        if np.linalg.norm(g) > tol:
            add(g)
    for _ in range(max_rounds):
        changed = False
        cur = list(elems)
        for a in range(len(cur)):
            for b in range(a + 1, len(cur)):
                if add(cur[a] @ cur[b] - cur[b] @ cur[a]):
                    changed = True
        if not changed or len(Q) >= 45:
            break
    return len(Q)


# ---------- joint sub-magma size spectrum (the J01 chain / 4-core) ----------
SUBSETS = [s for k in range(1, N + 1) for s in itertools.combinations(range(N), k)]


def spectrum(A, B):
    A, B = np.array(A), np.array(B)
    sizes = set()
    for s in SUBSETS:
        S = set(s)
        if all(A[a, b] in S and B[a, b] in S for a in s for b in s):
            sizes.add(len(s))
    return frozenset(sizes)


# ---------- null models ----------
rng = np.random.default_rng(20260923)


def sym(T):
    return np.triu(T) + np.triu(T, 1).T


def uniform():
    return rng.integers(0, N, (N, N)).tolist()


def tsml_like():
    T = rng.integers(0, N, (N, N))
    T = sym(np.where(rng.random((N, N)) < 0.73, 7, T))
    T[7, :] = 7; T[:, 7] = 7; T[0, :] = 0; T[:, 0] = 0; T[0, 7] = T[7, 0] = 7
    return T.tolist()


def bhml_like():
    T = sym(rng.integers(0, N, (N, N)))
    T[0, :] = np.arange(N); T[:, 0] = np.arange(N)
    return T.tolist()


def frac(xs):
    return sum(xs) / len(xs)


if __name__ == "__main__":
    print("=" * 74)
    print("FOUNDATION NULL-MODEL AUDIT -- does TIG's structure beat random tables?")
    print("=" * 74)

    # canonical values (must reproduce the J09 / J01 numbers)
    d_flow = closure_dim([antisym(TSML, r) for r in FLOW])
    d_joint = closure_dim([antisym(TSML, r) for r in FLOW] + [antisym(BHML, i) for i in range(N)])
    d_bhml = closure_dim([antisym(BHML, i) for i in range(N)])
    d_tsml = closure_dim([antisym(TSML, i) for i in range(N)])
    canon = spectrum(TSML, BHML)
    assert (d_flow, d_joint) == (28, 45) and canon == frozenset({1, 4, 5, 6, 7, 8, 9, 10})
    print(f"CANON  TSML-flow -> {d_flow} (so(8)) | TSML+BHML -> {d_joint} (so(10)) | "
          f"BHML alone -> {d_bhml} | TSML alone -> {d_tsml}")
    print(f"CANON  joint sub-magma sizes {sorted(canon)} (forbidden {{2,3}})\n")

    # (1) so(10): does a random table pair also generate so(10)?
    T = 150
    p_joint_uni = frac([closure_dim([antisym(uniform(), r) for r in FLOW] +
                                   [antisym(uniform(), i) for i in range(N)]) == 45 for _ in range(T)])
    p_joint_mat = frac([closure_dim([antisym(tsml_like(), r) for r in FLOW] +
                                   [antisym(bhml_like(), i) for i in range(N)]) == 45 for _ in range(T)])
    p_single = frac([closure_dim([antisym(uniform(), i) for i in range(N)]) == 45 for _ in range(T)])
    flow_dims = [closure_dim([antisym(tsml_like(), r) for r in FLOW]) for _ in range(T)]
    p_flow28 = frac([d == 28 for d in flow_dims])
    print("(1) so(10) closure")
    print(f"    P(joint -> so(10)) uniform pair       = {p_joint_uni:.3f}")
    print(f"    P(joint -> so(10)) matched pair       = {p_joint_mat:.3f}")
    print(f"    P(one random table -> so(10))         = {p_single:.3f}")
    print(f"    P(TSML-like flow -> exactly so(8)=28) = {p_flow28:.3f}")
    print("    VERDICT: so(10) is GENERIC (forced by N=10 + antisymmetrization);")
    print("             TSML-flow -> so(8) is the rare, table-specific part.\n")

    # (2) sub-magma chain / 4-core
    S = 300
    specs_mat = [spectrum(tsml_like(), bhml_like()) for _ in range(S)]
    specs_bhml = [spectrum(tsml_like(), BHML) for _ in range(S)]
    print("(2) joint sub-magma chain / 4-core")
    print(f"    matched pair:            P(exact canon chain) = {frac([s == canon for s in specs_mat]):.4f}"
          f"   P(has a 4-core) = {frac([4 in s for s in specs_mat]):.3f}"
          f"   P(2,3 forbidden) = {frac([2 not in s and 3 not in s for s in specs_mat]):.3f}")
    print(f"    real BHML x TSML-like:   P(exact canon chain) = {frac([s == canon for s in specs_bhml]):.4f}"
          f"   P(has a 4-core) = {frac([4 in s for s in specs_bhml]):.3f}")
    print("    VERDICT: the chain / 4-core is SPECIFIC (beats the matched null),")
    print("             and the specificity is carried by BHML; 'forbidden {2,3}' alone is weak.\n")

    # (3) second pass -- open the specific results: are they READOUTS of the construction rules?
    Ta, Ba = np.array(TSML), np.array(BHML)
    rank = {x: (10 if x == 0 else x) for x in range(N)}           # the ladder order 1<2<...<9<0
    climb_B = [(a, b, int(Ba[a][b])) for a in range(N) for b in range(a, N)
               if rank[Ba[a][b]] < min(rank[a], rank[b])]
    climb_T = [(a, b, int(Ta[a][b])) for a in range(N) for b in range(a, N)
               if Ta[a][b] not in (0, 7) and rank[Ta[a][b]] < min(rank[a], rank[b])]
    closed = [s for s in SUBSETS if all(Ta[a, b] in s and Ba[a, b] in s for a in s for b in s)]
    uppers = sorted([(0,)] + [tuple(sorted({0} | set(range(k, 10)))) for k in range(1, 8)])
    assert climb_B == [(8, 8, 7)] and climb_T == [] and sorted(closed) == uppers
    print("(3) readout test -- the mechanism behind what beat the null")
    print("    BHML climbs (a*b >= min(a,b) in the order 1<...<9<0) except the one cell 8*8=7;")
    print("    every TSML product is 0, 7, or climbs. So the jointly closed sets are EXACTLY {0} and")
    print("    the 7 upper sets {0}u{k..9}, k<=7 (all 8 enumerated). Sizes 3 and 2 are forbidden by")
    print(f"    two diagonal cells: {{8,9,0}} by 8*8=7, {{9,0}} by TSML 9*9={Ta[9][9]}.")
    rng89 = np.random.default_rng(89)
    cells89 = [(8, j) for j in range(1, 7)] + [(9, j) for j in range(1, 7)] + [(8, 8), (8, 9), (9, 9)]

    def rule89(climbing):
        M = Ba.copy()
        for (a, b) in cells89:
            ok = [v for v in range(N) if not climbing or rank[v] >= min(rank[a], rank[b])]
            v = rng89.choice(ok); M[a][b] = v; M[b][a] = v
        return M
    R89 = 1000
    p89 = frac([spectrum(TSML, rule89(False)) == canon for _ in range(R89)])
    ups = [frozenset(u) for u in uppers if len(u) >= 4]
    p89c = frac([all(all(Ta[a, b] in u and M[a, b] in u for a in u for b in u) for u in ups)
                 for M in (rule89(True) for _ in range(R89))])
    print(f"    keep BHML Rules 0/1/7, randomize Rule 89 (rows 8,9):   P(exact chain) = {p89:.4f}")
    print(f"    ...randomize Rule 89 but keep it CLIMBING: P(all upper sets closed) = {p89c:.3f}")
    G = np.vstack([antisym(TSML, r) for r in FLOW])
    kern = N - np.linalg.matrix_rank(G)
    e0, d56 = np.eye(N)[0], np.eye(N)[5] - np.eye(N)[6]
    assert kern == 2 and np.allclose(G @ e0, 0) and np.allclose(G @ d56, 0)
    assert (Ta[5] == Ta[6]).all() and closure_dim([antisym(TSML, r) for r in range(N) if r not in (0, 7)]) == 28
    print("    TSML-flow common kernel = span{e0, e5-e6}: 5 and 6 are TWINS (identical rows/cols, the")
    print("    only elements no exceptional pair touches, never produced) -> so(8) on the complement.")
    print("    VERDICT: specific against random tables, but READOUTS of the construction rules --")
    print("             the chain = 'products climb'; TSML's so(8) = 'S6 avoids 5 and 6'.\n")

    # (4) the associative spectrum (canon 6.1: Catalan / free commutative operad)
    def trees(lv):
        if len(lv) == 1:
            yield lv[0]; return
        for k in range(1, len(lv)):
            for L in trees(lv[:k]):
                for Rt in trees(lv[k:]):
                    yield (L, Rt)

    def spec4(Tb):
        Tb = np.asarray(Tb)
        X = [a.ravel() for a in np.meshgrid(*[np.arange(N)] * 4, indexing="ij")]
        ev = lambda t: X[t] if isinstance(t, int) else Tb[ev(t[0]), ev(t[1])]
        s = len({ev(t).tobytes() for t in trees((0, 1, 2, 3))})
        ac = len({ev(t).tobytes() for p in itertools.permutations(range(4)) for t in trees(p)})
        return s, ac
    assert spec4(TSML) == spec4(BHML) == (5, 15)
    p_spec = frac([spec4(sym(rng.integers(0, N, (N, N)))) == (5, 15) for _ in range(100)])
    print("(4) associative spectrum at n=4 (Catalan s4=5, ac-free 15)")
    print(f"    canon: TSML and BHML both maximal | random commutative tables maximal: P = {p_spec:.3f}")
    print("    VERDICT: GENERIC -- almost every commutative table generates the free operad.")
    print("=" * 74)
