"""Shared helpers for four_in_five.py and eccentric.py (exact arithmetic)."""
import itertools, math
from fractions import Fraction
import sympy as sp

def det_bareiss(A):
    A = [list(r) for r in A]; n = len(A); sign = 1; prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((r for r in range(k + 1, n) if A[r][k]), None)
            if p is None: return 0
            A[k], A[p] = A[p], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

def primitive(v):
    den = 1
    for x in v: den = den * x.denominator // math.gcd(den, x.denominator)
    w = [int(x * den) for x in v]; g = 0
    for x in w: g = math.gcd(g, x)
    return [x // g for x in w]

def kernels(M):  # needs sympy
    A = sp.Matrix(M)
    r = [primitive([Fraction(int(x.p), int(x.q)) for x in k]) for k in A.nullspace()]
    l = [primitive([Fraction(int(x.p), int(x.q)) for x in k]) for k in A.T.nullspace()]
    return r, l

def merge_or_drop(v, signed=False):
    if any(x == 0 for x in v): return "drop"
    vals = [abs(x) for x in v] if signed else v
    return "merge" if len(set(vals)) < len(vals) else None

def canon(M):
    n = len(M); G = [list(r) for r in M]; out = []
    for _ in range(4):
        G = [list(r) for r in zip(*G[::-1])]
        out += [tuple(v for r in G for v in r), tuple(v for r in G for v in r[::-1])]
    return min(out)

def local_certs(M):
    n = len(M); out = []
    for lines in ([list(c) for c in zip(*M)], [list(r) for r in M]):
        for k in range(2, n - 1):
            for S in itertools.combinations(range(n), k):
                v = [sum(lines[j][i] for j in S) for i in range(n)]
                if len(set(v)) == 1: out.append(S)
    return out

def global_index(M, c):
    n = len(M); pos = {M[i][j]: (i, j) for i in range(n) for j in range(n)}
    mp = {(i, j): pos.get(c - M[i][j]) for i in range(n) for j in range(n)}
    if any(v is None for v in mp.values()): return None
    P = [mp[(i, 0)][0] for i in range(n)]; Q = [mp[(0, j)][1] for j in range(n)]
    if not all(mp[(i, j)] == (P[i], Q[j]) for i in range(n) for j in range(n)): return None
    return abs((sum(i == x for i, x in enumerate(P)) + sum(j == x for j, x in enumerate(Q))) / 2 - 1)

