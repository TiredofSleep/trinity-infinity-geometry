"""
mirror_brake.py — "at 16 a double mirror puts the brakes on the break".
A product where lengths multiply on R^n needs n-1 imaginary units: maps J with J^2 = -1 that pairwise
anticommute (left multiplication by each imaginary unit). Count how many exist on R^8 and R^16, and
what shows up when you go looking for one more.
"""
import itertools
import numpy as np

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mult(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mult(a, c) - mult(conj(d), b), mult(d, a) + mult(b, conj(c))])
def e(k, n=8):
    v = np.zeros(n); v[k] = 1; return v
def check(Js):
    n = Js[0].shape[0]; I = np.eye(n)
    sq = all(np.allclose(J @ J, -I) for J in Js)
    anti = all(np.allclose(A @ B + B @ A, 0) for A, B in itertools.combinations(Js, 2))
    return sq and anti
def anticommutant(Js):
    """All X with X J + J X = 0 for every J (solve the linear system)."""
    n = Js[0].shape[0]; I = np.eye(n)
    M = np.vstack([np.kron(I, J) + np.kron(J.T, I) for J in Js])   # vec(XJ + JX) = (J^T x I + I x J) vec X
    _, s, Vt = np.linalg.svd(M)
    null = Vt[np.sum(s > 1e-9):]
    return [v.reshape(n, n, order="F") for v in null]

# R^8: the 7 octonion imaginary units
L = [np.column_stack([mult(e(i), e(j)) for j in range(8)]) for i in range(1, 8)]
print("R^8 : 7 imaginary units (octonions), squares -1 and anticommuting:", check(L))
print("      looking for an 8th: solutions to 'anticommute with all 7' =", len(anticommutant(L)))

# R^16 = R^8 x R^2: lift the 7, add one more
sz = np.diag([1., -1.]); eps = np.array([[0., 1.], [-1., 0.]])
J16 = [np.kron(Li, sz) for Li in L] + [np.kron(np.eye(8), eps)]
print("\nR^16: 8 imaginary units built, squares -1 and anticommuting:", check(J16))
X = anticommutant(J16)
print("      looking for a 9th: solutions to 'anticommute with all 8' =", len(X))
W = X[0] / np.sqrt(np.trace(X[0].T @ X[0]) / 16)
omega = np.linalg.multi_dot(J16)
print("      that one solution is the product of all 8 (the stacked mirror):",
      np.allclose(W, omega) or np.allclose(W, -omega))
print("      it squares to", "+1 (a mirror, not a turn)" if np.allclose(W @ W, np.eye(16)) else "?",
      "-> it can never be an imaginary unit")
vals = np.round(np.linalg.eigvalsh((W + W.T) / 2)).astype(int)
print(f"      it splits R^16 into +1 and -1 halves of size {np.sum(vals == 1)} and {np.sum(vals == -1)}")

def rho(n):                                        # Radon-Hurwitz number: n = 2^(4a+b) * odd
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    a, b = divmod(k, 4); return 2 ** b + 8 * a
print("\nRadon-Hurwitz: imaginary units available on R^n vs needed for lengths to multiply")
for n in (2, 4, 8, 16, 32, 64, 128):
    print(f"   n = {n:3d}: available {rho(n) - 1:2d}, needed {n - 1:3d}  ->", "room" if rho(n) - 1 >= n - 1 else "broken")

# Two 8-rooms side by side instead of stacked: the Freudenthal-Tits square (Vinberg's formula)
dims = {"R": 1, "C": 2, "H": 4, "O": 8}; der = {"R": 0, "C": 0, "H": 3, "O": 14}
def vinberg(A, B):
    a, b = dims[A], dims[B]
    return der[A] + der[B] + 2 * (a + b - 2) + 3 * a * b
print("\nPairing instead of stacking: dimension of the symmetry built from A (x) B (Freudenthal-Tits square)")
print("       " + "".join(f"{k:>6s}" for k in dims))
for A in dims:
    print(f"   {A:3s} " + "".join(f"{vinberg(A, B):6d}" for B in dims))

# Cross-check the octonion row against root systems built directly
r8 = [v for i, j in itertools.combinations(range(8), 2) for si in (1, -1) for sj in (1, -1)
      for v in [np.eye(8)[i] * si + np.eye(8)[j] * sj]]
r8 += [np.array(s) for s in itertools.product((.5, -.5), repeat=8) if sum(x < 0 for x in s) % 2 == 0]
r8 = np.array(r8)
a1 = r8[0]; a2 = next(r for r in r8 if np.isclose(r @ a1, -1))            # two roots at 120 degrees
e7 = r8[np.isclose(r8 @ a1, 0)]; e6 = e7[np.isclose(e7 @ a2, 0)]
f4 = 24 + 8 + 16
print(f"   check: F4 {f4}+4 = {f4 + 4},  E6 {len(e6)}+6 = {len(e6) + 6},  E7 {len(e7)}+7 = {len(e7) + 7},"
      f"  E8 {len(r8)}+8 = {len(r8) + 8}")
