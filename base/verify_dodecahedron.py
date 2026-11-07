"""verify_dodecahedron.py -- an exact proof of which energy contests the dodecahedron loses
(SYMMETRY_AND_ENERGY.md section 3; THE_LENS.md section 7).

Claim.  Let f(r^2) be completely monotone on (0, 4] (Cohn and Kumar's class).
  - If f is a polynomial of degree at most 5 in r^2, the dodecahedron minimizes the energy: it is a
    5-design, and such a potential cannot tell it from the best.
  - Every other such f makes the dodecahedron a saddle, so some 20 points have lower energy.
The same check, one step down, gives the cube: degree at most 3 it ties, anything more and its twist wins.

Proof, as computed here.  Write s for the cosine between two corners, so r^2 = 2 - 2s and 4 - r^2 = 2(1 + s).
By Bernstein's theorem f = sum c_n (4 - r^2)^n with every c_n >= 0.  For a move u of the corners along the
sphere, the second derivative of the energy at a balanced arrangement is
    sum over pairs [ g''(s) (u_i.x_j + x_i.u_j)^2 + g'(s) (2 u_i.u_j - s (|u_i|^2 + |u_j|^2)) ],   g(s) = f(2 - 2s).
For g = (1 + s)^n call it Lambda_n(u).  One exact move u (the dodecahedron's floppy family, built by projecting
with the symmetry group) gives Lambda_n = 0 for n <= 5 and Lambda_n < 0 for every n >= 6: exactly for n <= 60,
and by an explicit bound beyond.  So sum c_n 2^n Lambda_n < 0 unless every c_n with n >= 6 is zero.

Exact arithmetic in Q(sqrt5) throughout; numpy is used only to list the 120 symmetries.  ASCII output.
Run:  python verify_dodecahedron.py      (a few seconds)
"""
import math
import sys
from fractions import Fraction as Fr
from itertools import product

import numpy as np

FAILED = []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILED.append(label)


class Q5:
    """a + b sqrt5 with a, b rational"""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = lift(o)
        return Q5(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-lift(o))

    def __rsub__(self, o):
        return lift(o) - self

    def __mul__(self, o):
        o = lift(o)
        return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = lift(o)
        n = o.a * o.a - 5 * o.b * o.b
        c = self * Q5(o.a, -o.b)
        return Q5(c.a / n, c.b / n)

    def __pow__(self, k):
        out, p = Q5(1), self
        while k:
            if k & 1:
                out = out * p
            p, k = p * p, k >> 1
        return out

    def conj(self):
        return Q5(self.a, -self.b)

    def sign(self):
        a, b = self.a, self.b
        if b == 0 or a == 0 or (a > 0) == (b > 0):
            v = a if b == 0 else b if a == 0 else a
            return (v > 0) - (v < 0)
        d = a * a - 5 * b * b                    # a and b have opposite signs: compare |a| with |b| sqrt5
        return 0 if d == 0 else ((1 if a > 0 else -1) if d > 0 else (1 if b > 0 else -1))

    def __eq__(self, o):
        o = lift(o)
        return self.a == o.a and self.b == o.b

    def __abs__(self):
        return self if self.sign() >= 0 else -self

    def __float__(self):
        return float(self.a) + float(self.b) * math.sqrt(5)


def lift(x):
    return x if isinstance(x, Q5) else Q5(x)


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def comb(u, cu, v, cv):
    return tuple(cu * u[k] + cv * v[k] for k in range(3))


def symmetries(V):
    """every orthogonal map carrying the corner set to itself: (permutation, rotation part's trace, det)"""
    X = np.array([[float(c) for c in v] for v in V])
    n = len(X)
    base = next(t for t in product(range(n), repeat=3) if abs(np.linalg.det(X[list(t)])) > 1e-6)
    B = X[list(base)]
    G = B @ B.T
    out = {}
    for img in product(range(n), repeat=3):
        W = X[list(img)]
        if np.abs(W @ W.T - G).max() > 1e-9:
            continue
        M = W.T @ np.linalg.inv(B.T)
        Y = X @ M.T
        perm = [int(np.argmin(np.linalg.norm(X - y, axis=1))) for y in Y]
        if np.abs(X[perm] - Y).max() < 1e-9 and len(set(perm)) == n:
            d = round(np.linalg.det(M))
            out[tuple(perm)] = (d * np.trace(M), d)
    return list(out.items())


def second_derivative_data(V, u, s_classes):
    """for each class of pairs: A = sum (u_i.x_j + x_i.u_j)^2 and B = sum (2 u_i.u_j - s(|u_i|^2 + |u_j|^2)),
    per unit |u|^2.  Corners V are given with |v|^2 = 3 (so x = v / sqrt3)."""
    A = [Q5(0) for _ in s_classes]
    Bc = [Q5(0) for _ in s_classes]
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            s = dot(V[i], V[j]) / 3
            k = next(m for m, c in enumerate(s_classes) if c == s)
            first = dot(u[i], V[j]) + dot(V[i], u[j])
            A[k] = A[k] + first * first / 3
            Bc[k] = Bc[k] + 2 * dot(u[i], u[j]) - s * (dot(u[i], u[i]) + dot(u[j], u[j]))
    norm = sum((dot(w, w) for w in u), Q5(0))
    return [x / norm for x in A], [x / norm for x in Bc]


def lam(n, s_classes, A, B):
    """the second derivative along u for the potential g = (1 + s)^n"""
    tot = Q5(0)
    for s, a, b in zip(s_classes, A, B):
        base = 1 + s
        if n >= 2:
            tot = tot + n * (n - 1) * base ** (n - 2) * a
        if n >= 1:
            tot = tot + n * base ** (n - 1) * b
    return tot


def tail_bound(n, s_classes, A, B):
    """sum over the classes after the first (the nearest pairs) of the terms of Lambda_n / (n (1 + s_1)^(n-1)),
    taken in absolute value; with r = (1 + s_k)/(1 + s_1) < 4/5 each term falls as n grows (n >= 6)"""
    top = 1 + s_classes[0]
    tot, ok = Q5(0), True
    for s, a, b in zip(s_classes[1:], A[1:], B[1:]):
        r = (1 + s) / top
        ok &= (Fr(4, 5) - r).sign() > 0
        if r.sign() == 0:
            continue
        tot = tot + (n - 1) * abs(a) * r ** (n - 2) / top + abs(b) * r ** (n - 1)
    return tot, ok


# ------------------------------------------------------------------ the dodecahedron, exactly
PHI = Q5(Fr(1, 2), Fr(1, 2))
IPHI = PHI - 1                                                  # 1/phi
D = [tuple(Q5(c) for c in v) for v in product((-1, 1), repeat=3)]
for p in (-1, 1):
    for q in (-1, 1):
        D += [(Q5(0), p * IPHI, q * PHI), (p * IPHI, q * PHI, Q5(0)), (q * PHI, Q5(0), p * IPHI)]
S_D = [Q5(0, Fr(1, 3)), Q5(Fr(1, 3)), Q5(Fr(-1, 3)), Q5(0, Fr(-1, 3)), Q5(-1)]   # cosines between corners
check("20 corners, each at squared distance 3 from the centre; the cosines between corners are "
      "sqrt5/3, 1/3, -1/3, -sqrt5/3 and -1",
      len(D) == 20 and all(dot(v, v) == 3 for v in D)
      and all(any(dot(D[i], D[j]) / 3 == c for c in S_D) for i in range(20) for j in range(i + 1, 20)))

G = symmetries(D)
check(f"the dodecahedron has {len(G)} symmetries (rotations and reflections)", len(G) == 120)

# the floppy family: project one tangent move at corner 0 onto the type T2g (character = the Galois
# conjugate of the rotation part's trace, the same for a rotation and its mirror image)
TRACE = {3: Q5(3), 0: Q5(0), -1: Q5(-1)}
nbr = next(j for j in range(1, 20) if dot(D[0], D[j]) / 3 == S_D[0])
c0 = dot(D[nbr], D[0]) / 3
w = comb(D[nbr], Q5(1), D[0], -c0)                             # tangent at corner 0
u = [(Q5(0), Q5(0), Q5(0)) for _ in range(20)]
for perm, (tr, det) in G:
    t = next((v for k, v in TRACE.items() if abs(tr - k) < 1e-9), None)
    if t is None:
        t = PHI if abs(tr - float(PHI)) < 1e-9 else 1 - PHI
    chi = t.conj()
    image = comb(D[perm[nbr]], Q5(1), D[perm[0]], -c0)          # the symmetry applied to w, without its matrix
    j = perm[0]
    u[j] = comb(u[j], Q5(1), image, chi)
check("the projected move is not zero and is tangent to the sphere at every corner",
      any(dot(x, x).sign() > 0 for x in u) and all(dot(u[j], D[j]) == 0 for j in range(20)))
A, B = second_derivative_data(D, u, S_D)
check("it is a flex: it keeps every edge's length to first order (A = 0 for the nearest pairs)", A[0] == 0)
check("it is even: opposite corners move together, so antipodal pairs add nothing (A = B = 0 there)",
      A[4] == 0 and B[4] == 0)
check("the nearest pairs separate at second order along it (B < 0 for them)", B[0].sign() < 0)

N0 = 60
L = [lam(n, S_D, A, B) for n in range(N0 + 1)]
check("Lambda_n = 0 for n = 0..5: polynomials of degree at most 5 cannot see the move (a 5-design)",
      all(L[n] == 0 for n in range(6)))
check(f"Lambda_n < 0 for every n from 6 to {N0}, exactly", all(L[n].sign() < 0 for n in range(6, N0 + 1)))
T, small = tail_bound(N0 + 1, S_D, A, B)
check(f"and for every n > {N0}: the other classes' share stays below the nearest pairs' (an explicit bound)",
      small and (T + B[0]).sign() < 0)
print(f"      Lambda_6 = {float(L[6]):.10f}, so at the weak end a Gaussian gives about "
      f"{float(L[6]) * 64 / 720:.6f} a^6 along the move")


def gaussian(a, Ls):
    """the second derivative for e^(-a r^2) = e^(-4a) sum (2a)^n (1+s)^n / n!, from the exact Lambda_n"""
    tot, term = 0.0, 1.0
    for n, Ln in enumerate(Ls):
        if n:
            term *= 2 * a / n
        tot += term * float(Ln)
    return math.exp(-4 * a) * tot


check("cross-check against the run's double-precision second derivative: a = 1 gives -0.0511660, a = 4 "
      "gives -1.489893", abs(gaussian(1, L) + 0.0511660) < 1e-6 and abs(gaussian(4, L) + 1.489893) < 1e-5)

# ------------------------------------------------------------------ the cube, one step down
C = [tuple(Q5(c) for c in v) for v in product((-1, 1), repeat=3)]
S_C = [Q5(Fr(1, 3)), Q5(Fr(-1, 3)), Q5(-1)]
twist = [(-v[1], v[0], Q5(0)) if v[2].sign() > 0 else (Q5(0), Q5(0), Q5(0)) for v in C]
Ac, Bc = second_derivative_data(C, twist, S_C)
Lc = [lam(n, S_C, Ac, Bc) for n in range(N0 + 1)]
Tc, small_c = tail_bound(N0 + 1, S_C, Ac, Bc)
check("the cube's twist is a flex (A = 0 for the edges); Lambda_n = 0 for n = 0..3 (a 3-design) and < 0 for "
      f"every n from 4 to {N0}, with the same kind of bound beyond",
      Ac[0] == 0 and all(Lc[n] == 0 for n in range(4)) and all(Lc[n].sign() < 0 for n in range(4, N0 + 1))
      and small_c and (Tc + Bc[0]).sign() < 0)

print()
print(f"{'ALL CHECKS PASS' if not FAILED else str(len(FAILED)) + ' FAILED'}")
sys.exit(1 if FAILED else 0)
