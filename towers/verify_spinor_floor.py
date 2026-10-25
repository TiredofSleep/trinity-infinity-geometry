#!/usr/bin/env python3
"""verify_spinor_floor.py -- checks every [FORCED] claim in THE_SPINOR_FLOOR.md.

    python verify_spinor_floor.py         # prints PASS/FAIL per check; exit code 1 on any failure

Jordan-Wigner: with the Pauli matrices X, Y, Z and n switches (sites), put
    g(2j-1) = Z x ... x Z x X x 1 x ... x 1,    g(2j) = Z x ... x Z x Y x 1 x ... x 1
(j-1 factors Z in front). These are 2n matrices of size 2^n x 2^n.

P1  g(a) g(b) + g(b) g(a) = 2 delta(a,b): 2n perpendicular directions, i.e. generators of Cl(2n)
P2  the 4^n ordered products g(S), S a subset of {1..2n}, are an orthogonal basis of ALL
    2^n x 2^n complex matrices (Hilbert-Schmidt Gram matrix = 2^n * identity), and C(2n,k) of
    them have grade |S| = k: over C, Cl(2n) is the full matrix algebra, 4^n = (2^n)^2
P3  a(j) = (g(2j-1) + i g(2j))/2 obey a(i)a(j)^+ + a(j)^+a(i) = delta, a(i)a(j) + a(j)a(i) = 0;
    the count N = sum a(j)^+ a(j) is diagonal on the n-bit strings with eigenvalue = number of
    1s, multiplicities C(n,k) (Pascal's row n); a(j) kills 00...0, and products of k raising
    operators on 00...0 fill the k-th layer
P4  chirality G = (-i)^n g(1) g(2) ... g(2n) = Z x Z x ... x Z = (-1)^(number of 1s);
    G^2 = 1, G anticommutes with every g(a) and commutes with every product of two:
    the spinor splits into two halves of 2^(n-1) states, each kept by the even part
P5  n = 3: the 8 spinor states are the cube's corners 000..111; the layers are 1, 3, 3, 1;
    the two halves are {0,3,5,6} and {1,2,4,7}, each a regular tetrahedron (all distances
    sqrt 2), swapped by the complement b -> 111 - b (the cube's central inversion), which
    anticommutes with G
P6  over R, the first floor: X and Z are real, square to 1 and anticommute, and 1, X, Z, XZ
    span all real 2x2 matrices: Cl(2,0) = R(2)   (higher floors: Bott, cited not checked)
P7  J20's "coarse cells", read correctly (n = 3): each column of the 2^n x 2^n matrices is kept by
    left multiplication (a copy of the spinor space); counted by 1s in the column index: C(n,k)

Checked for n = 1..5 (P1-P4). Standard library + numpy. Runtime: a few seconds.
"""
import itertools
import math
import sys
from functools import reduce

import numpy as np

FAILS = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   (" + detail + ")") if detail else ""))
    if not ok:
        FAILS.append(name)


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
kron = lambda mats: reduce(np.kron, mats)


def gammas(n):
    out = []
    for j in range(n):
        for P in (X, Y):
            out.append(kron([Z] * j + [P] + [I2] * (n - j - 1)))
    return out


def popcount(i):
    return bin(i).count("1")


NMAX = 5
for n in range(1, NMAX + 1):
    D = 2 ** n
    g = gammas(n)
    Id = np.eye(D, dtype=complex)

    # P1
    ok = all(np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * Id) for a in range(2 * n) for b in range(2 * n))
    check("P1 n=%d: %d generators anticommute and square to 1" % (n, 2 * n), ok)

    # P2
    prods, grades = [], []
    for mask in range(2 ** (2 * n)):
        M = Id.copy()
        for a in range(2 * n):
            if mask >> a & 1:
                M = M @ g[a]
        prods.append(M.ravel())
        grades.append(popcount(mask))
    A = np.array(prods)
    gram = A.conj() @ A.T
    ok = np.allclose(gram, D * np.eye(4 ** n))
    ok &= all(grades.count(k) == math.comb(2 * n, k) for k in range(2 * n + 1))
    check("P2 n=%d: the %d products are an orthogonal basis of all %dx%d matrices; grades = Pascal row %d"
          % (n, 4 ** n, D, D, 2 * n), ok)

    # P3
    a = [(g[2 * j] + 1j * g[2 * j + 1]) / 2 for j in range(n)]
    ad = [m.conj().T for m in a]
    ok = all(np.allclose(a[i] @ ad[j] + ad[j] @ a[i], (i == j) * Id) for i in range(n) for j in range(n))
    ok &= all(np.allclose(a[i] @ a[j] + a[j] @ a[i], 0 * Id) for i in range(n) for j in range(n))
    Nop = sum(ad[j] @ a[j] for j in range(n))
    ok &= np.allclose(Nop, np.diag([popcount(i) for i in range(D)]))
    ok &= all([popcount(i) for i in range(D)].count(k) == math.comb(n, k) for k in range(n + 1))
    vac = np.zeros(D, dtype=complex)
    vac[0] = 1
    ok &= all(np.allclose(m @ vac, 0) for m in a)
    for k in range(n + 1):
        layer = [reduce(lambda v, j: ad[j] @ v, S, vac) for S in itertools.combinations(range(n), k)]
        span_rank = np.linalg.matrix_rank(np.array(layer)) if layer else 0
        ok &= span_rank == math.comb(n, k)
        ok &= all(np.allclose(Nop @ v, k * v) for v in layer)
    check("P3 n=%d: a(j) obey the anticommutation rules; N counts 1s; layers C(%d,k) = %s"
          % (n, n, [math.comb(n, k) for k in range(n + 1)]), ok)

    # P4
    G = (-1j) ** n * reduce(lambda u, v: u @ v, g)
    ok = np.allclose(G, kron([Z] * n)) and np.allclose(G, np.diag([(-1) ** popcount(i) for i in range(D)]))
    ok &= np.allclose(G @ G, Id)
    ok &= all(np.allclose(G @ m, -m @ G) for m in g)
    ok &= all(np.allclose(G @ (g[p] @ g[q]), (g[p] @ g[q]) @ G) for p in range(2 * n) for q in range(2 * n))
    ok &= sum(1 for i in range(D) if popcount(i) % 2 == 0) == 2 ** (n - 1)
    check("P4 n=%d: chirality = Z x...x Z = (-1)^(#1s); halves of 2^(n-1) = %d states each, kept by the even part" % (n, 2 ** (n - 1)), ok)

# P5 ------------------------------------------------------------------------------------------
n = 3
even = [i for i in range(8) if popcount(i) % 2 == 0]
odd = [i for i in range(8) if popcount(i) % 2 == 1]
pt = lambda i: np.array([(i >> 2) & 1, (i >> 1) & 1, i & 1], dtype=float)
regular = lambda S: all(abs(np.linalg.norm(pt(p) - pt(q)) - math.sqrt(2)) < 1e-12 for p, q in itertools.combinations(S, 2))
layers = [sum(1 for i in range(8) if popcount(i) == k) for k in range(4)]
comp = kron([X] * 3)                                        # b -> 111 - b
ok = even == [0, 3, 5, 6] and odd == [1, 2, 4, 7] and regular(even) and regular(odd) and layers == [1, 3, 3, 1]
ok &= sorted(7 - i for i in even) == odd
ok &= np.allclose(comp @ kron([Z] * 3), -kron([Z] * 3) @ comp)
check("P5 n=3: corners 000..111, layers 1,3,3,1, halves {0,3,5,6} and {1,2,4,7} = the two regular tetrahedra, "
      "swapped by the central inversion", ok)

# P6 ------------------------------------------------------------------------------------------
Xr, Zr = X.real, Z.real
ok = np.allclose(Xr @ Xr, np.eye(2)) and np.allclose(Zr @ Zr, np.eye(2)) and np.allclose(Xr @ Zr, -Zr @ Xr)
ok &= np.linalg.matrix_rank(np.array([np.eye(2).ravel(), Xr.ravel(), Zr.ravel(), (Xr @ Zr).ravel()])) == 4
check("P6 over R: X, Z real anticommuting with square 1; 1, X, Z, XZ span all real 2x2 matrices: Cl(2,0) = R(2)", ok)

# P7 ------------------------------------------------------------------------------------------
# J20's coarse cells, read correctly: fix the column index b (n bits) of the 2^n x 2^n matrices.
# Each column space L_b is 2^n-dimensional and is kept by left multiplication by every element of
# the algebra (a copy of the spinor space); the columns, counted by the number of 1s in b, are C(n,k).
n = 3
D = 2 ** n
g = gammas(n)
rng = np.random.default_rng(3)
ok = True
for b in range(D):
    basis_b = [np.outer(np.eye(D)[a], np.eye(D)[b]) for a in range(D)]         # E_{a,b}, a = 0..D-1
    for _ in range(5):
        A = sum(rng.normal() * gm for gm in g) + rng.normal() * (g[0] @ g[3])  # a random element
        for E in basis_b:
            M = A @ E
            ok &= np.allclose(np.delete(M, b, axis=1), 0)                       # stays in column b
ok &= [sum(1 for b in range(D) if popcount(b) == k) for k in range(n + 1)] == [math.comb(n, k) for k in range(n + 1)]
check("P7 n=3: each column of the 8x8 matrices is a left ideal of dimension 8 (a copy of the spinors); "
      "columns by number of 1s: 1,3,3,1", ok)

print()
if FAILS:
    print("FAILED: %d check(s): %s" % (len(FAILS), ", ".join(FAILS)))
    sys.exit(1)
print("All checks passed.")
