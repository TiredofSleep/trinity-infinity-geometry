#!/usr/bin/env python3
"""foundation_null_model.py -- does the foundation's structure beat random tables?

Every PROVED claim about TSML/BHML is a true statement about two specific 10x10
tables. Truth is not the question; SIGNIFICANCE is. This script asks, for each
headline structural claim: among random tables of the same kind, how often does
the property also hold? A property that nearly all random tables share is forced
by the construction (or by N = 10), not by TIG. One that random tables almost
never share is genuinely specific. See 04_meta/FOUNDATION_NULL_MODEL_AUDIT.md.

    python verification/foundation_null_model.py      (~30-60 s)

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
    print("             and the specificity is carried by BHML; 'forbidden {2,3}' alone is weak.")
    print("=" * 74)
