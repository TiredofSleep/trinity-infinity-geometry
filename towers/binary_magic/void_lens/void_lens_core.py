"""Exact integer linear algebra shared by the void_lens scripts."""
import math

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

def rank_exact(A):
    A = [list(r) for r in A]; m, n = len(A), len(A[0]); r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        for i in range(m):
            if i != r and A[i][c]:
                f, g = A[r][c], A[i][c]
                A[i] = [f * x - g * y for x, y in zip(A[i], A[r])]
                gg = 0
                for x in A[i]: gg = math.gcd(gg, x)
                if gg > 1: A[i] = [x // gg for x in A[i]]
        r += 1
        if r == m: break
    return r

