#!/usr/bin/env python3
"""
mermin_28.py -- reproduces the atlas claim "unique across all 28 ways of labeling two-qubit operators by
numbers" and "the only 3x3 magic square with sum 30 whose rows and columns all XOR to zero".

A labeling of 1..15 by two-qubit Paulis (XOR = product up to phase) is fixed, as far as commutation goes, by a
nondegenerate alternating form on F2^4. There are |GL(4,2)| / |Sp(4,2)| = 20160 / 720 = 28 of them.
Prints ASCII only.
"""
import itertools

def det_mod2(A):
    A = [row[:] for row in A]; n = len(A)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c]), None)
        if p is None: return 0
        A[c], A[p] = A[p], A[c]
        for r in range(n):
            if r != c and A[r][c]:
                A[r] = [(x + y) % 2 for x, y in zip(A[r], A[c])]
    return 1

forms = []
for bits in itertools.product([0, 1], repeat=6):
    A = [[0] * 4 for _ in range(4)]; k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            A[i][j] = A[j][i] = bits[k]; k += 1
    if det_mod2(A): forms.append(A)
assert len(forms) == 28

def om(A, x, y):
    return sum(((x >> i) & 1) * A[i][j] * ((y >> j) & 1) for i in range(4) for j in range(4)) % 2

sols = []
for a, b, c in itertools.permutations(range(16), 3):
    if a + b + c != 30 or a ^ b ^ c: continue
    for d, g in itertools.permutations([v for v in range(16) if v not in (a, b, c)], 2):
        if a + d + g != 30 or a ^ d ^ g: continue
        for e in range(16):
            f = 30 - d - e; h = 30 - b - e; i = 30 - g - h; M = (a, b, c, d, e, f, g, h, i)
            if len(set(M)) < 9 or min(M) < 0 or max(M) > 15: continue
            L = [M[0:3], M[3:6], M[6:9], M[0::3], M[1::3], M[2::3]]
            if any(sum(x) != 30 or x[0] ^ x[1] ^ x[2] for x in L) or a + e + i != 30 or c + e + g != 30: continue
            sols.append(M)

def canon(M):
    G = [list(M[0:3]), list(M[3:6]), list(M[6:9])]; out = []
    for _ in range(4):
        G = [list(r) for r in zip(*G[::-1])]
        out += [tuple(v for r in G for v in r), tuple(v for r in G for v in r[::-1])]
    return min(out)

classes = {canon(M) for M in sols}
per_form = []
for A in forms:
    per_form.append(sum(all(om(A, x, y) == 0 for l in (M[0:3], M[3:6], M[6:9], M[0::3], M[1::3], M[2::3])
                            for x, y in itertools.combinations(l, 2)) for M in sols))
print("nondegenerate alternating forms on F2^4:", len(forms))
print("3x3 magic squares (sum 30, distinct 0-15) with rows and columns XOR 0:", len(sols),
      "->", len(classes), "up to rotation/reflection:", sorted(classes))
print("forms under which those squares have commuting rows and columns:", sum(1 for n in per_form if n),
      "of 28 (that form takes all", max(per_form), "orientations)")
ok = len(classes) == 1 and sum(1 for n in per_form if n) == 1
print("PASS" if ok else "MISMATCH")
assert ok
