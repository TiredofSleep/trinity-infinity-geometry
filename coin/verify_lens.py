"""verify_lens.py -- checks the [FORCED] lines of ../THE_LENS.md that no other script covers:
the glue, "a thing times its flip lands on the edge", on five coins.

numpy + scipy (Qhull for the polar).  ASCII output.  Exit code 1 on any failure.
Run:  python verify_lens.py      (a few seconds)
"""
import sys
from itertools import product

import numpy as np
from scipy.spatial import ConvexHull

FAILED = []
PASSED = []
rng = np.random.default_rng(20261107)


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    (PASSED if ok else FAILED).append(label)


# ------------------------------------------------------------------ 1. real and imaginary: z -> conj(z)
z = rng.normal(size=1000) + 1j * rng.normal(size=1000)
g = z * np.conj(z)
check("z conj(z) is real for 1000 random z: it lands on the edge of the real/imaginary coin",
      np.abs(g.imag).max() < 1e-12)
check("... and it is |z|^2, never negative", (g.real >= 0).all() and np.allclose(g.real, np.abs(z) ** 2))


# ------------------------------------------------------------------ 2. the two square roots of 2
def mul2(a, b):
    """(p + q r)(s + t r) with r^2 = 2, done exactly on integer pairs."""
    return (a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


N = 300
on_edge, never_zero = True, True
for p in range(-N, N + 1):
    for q in range(-N, N + 1):
        n = mul2((p, q), (p, -q))
        on_edge &= n[1] == 0 and n[0] == p * p - 2 * q * q
        if (p, q) != (0, 0):
            never_zero &= n[0] != 0
check(f"(p + q sqrt2)(p - q sqrt2) = p^2 - 2q^2, a whole number, for every |p|, |q| <= {N}", on_edge)
check("... and it is 0 only at p = q = 0, because no fraction squares to 2", never_zero)


# ------------------------------------------------------------------ 3. quaternions: q -> conj(q) reverses products
def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return np.array([a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
                     a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
                     a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
                     a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0])


def qconj(a):
    return np.array([a[0], -a[1], -a[2], -a[3]])


Q, R = rng.normal(size=(500, 4)), rng.normal(size=(500, 4))
check("quaternion conjugation reverses products: conj(ab) = conj(b) conj(a), on 500 random pairs",
      all(np.allclose(qconj(qmul(a, b)), qmul(qconj(b), qconj(a))) for a, b in zip(Q, R)))
check("q conj(q) is real and equals |q|^2, although quaternions do not commute",
      all(np.allclose(qmul(a, qconj(a)), [a @ a, 0, 0, 0]) for a in Q))

# ------------------------------------------------------------------ 4. transpose: A -> A^T reverses products
symmetric, not_negative = True, True
for _ in range(300):
    m, n = rng.integers(1, 7, size=2)
    A = rng.integers(-9, 10, size=(m, n))
    G = A @ A.T
    symmetric &= bool((G == G.T).all())
    not_negative &= np.linalg.eigvalsh(G.astype(float)).min() > -1e-9
check("A A^T is symmetric for 300 random integer matrices of every shape up to 6 x 6", symmetric)
check("... and none of its eigenvalues is negative", not_negative)


# ------------------------------------------------------------------ 5. polarity: K -> K°
def polar(V):
    """Vertices of the polar {y : v.y <= 1 for every v in V}; the origin must be inside conv(V)."""
    h = ConvexHull(np.asarray(V, float))
    if (h.equations[:, -1] >= -1e-12).any():
        raise ValueError("origin not strictly inside")
    out = {}
    for eq in h.equations:
        p = eq[:-1] / -eq[-1]
        out.setdefault(tuple(np.round(p, 7)), p)
    return np.array(list(out.values()))


def same_set(A, B, tol=1e-6):
    return len(A) == len(B) and all(np.min(np.linalg.norm(B - a, axis=1)) < tol for a in A)


bodies = {"cube": np.array(list(product([-1, 1], repeat=3)), float),
          "octahedron": np.vstack([np.eye(3), -np.eye(3)])}
for i in range(5):
    P = rng.normal(size=(40, 3))
    bodies[f"random body {i + 1}"] = P[ConvexHull(P).vertices]
for name, V in bodies.items():
    W = polar(V)
    back = polar(W)
    vk, vw = ConvexHull(V).volume, ConvexHull(W).volume
    check(f"{name}: the polar of its polar is itself, so |K||K^o| = {vk * vw:.6f} is one number for both sides",
          same_set(back, V) and abs(vk * vw - vw * ConvexHull(back).volume) < 1e-9 * vk * vw)

# ------------------------------------------------------------------ 6. the average: an affine flip keeps midpoints
check("(z + conj z)/2 is real: the average of a thing and its flip lies on the edge",
      np.abs(((z + np.conj(z)) / 2).imag).max() == 0)
square_ok = True
for _ in range(300):
    m = int(rng.integers(1, 7))
    A = rng.integers(-9, 10, size=(m, m))
    square_ok &= bool(((A + A.T) == (A + A.T).T).all())
check("(A + A^T)/2 is symmetric for 300 random square integer matrices", square_ok)


def flip(n):
    return 15 - n


check("on 0..15, n -> 15 - n done twice changes nothing, every average (n + (15 - n))/2 is 7.5, and the flip keeps 7.5",
      all(flip(flip(n)) == n and (n + flip(n)) / 2 == 7.5 for n in range(16)) and flip(7.5) == 7.5)

# ------------------------------------------------------------------ 7. the worked example: Duerer's square, numbered from 0
D = [[15, 2, 1, 12], [4, 9, 10, 7], [8, 5, 6, 11], [3, 14, 13, 0]]
cells = sum(D, [])
lines = D + [list(col) for col in zip(*D)] + [[D[i][i] for i in range(4)], [D[i][3 - i] for i in range(4)]]
check("Duerer's square numbered from 0 holds 0..15 once each; its 4 rows, 4 columns and 2 diagonals all add to 30",
      sorted(cells) == list(range(16)) and all(sum(line) == 30 for line in lines))
check("no cell holds the centre value 7.5, and eight cells lie on each side of it",
      7.5 not in cells and sum(n < 7.5 for n in cells) == 8)
check("each cell and its mirror through the middle add to 15: in this square the flip is also a place",
      all(D[i][j] + D[3 - i][3 - j] == 15 for i in range(4) for j in range(4)))


def det_int(M):
    """Exact determinant of an integer matrix (Bareiss elimination)."""
    M = [row[:] for row in M]
    n, sign, prev = len(M), 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for r in range(k + 1, n):
                if M[r][k] != 0:
                    M[k], M[r] = M[r], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[-1][-1]


check("... and the square is singular: its determinant is exactly 0", det_int(D) == 0)
check("(control: the same routine finds the Lo Shu square's determinant, 360, so it can see a nonzero one)",
      det_int([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) == 360)

print()
print(f"{len(PASSED)} of {len(PASSED) + len(FAILED)} checks pass")
sys.exit(1 if FAILED else 0)
