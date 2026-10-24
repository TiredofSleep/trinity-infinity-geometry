"""
mirror_tower.py — "stacked, nested, and mirrored in imaginary".
Cayley-Dickson builds each level as pairs of the level below, and the rule uses the conjugation mirror
(keep the real axis, flip every imaginary one). Checks:
  1. conjugation is a true mirror (determinant -1) at every level, because the imaginary count 2^n - 1 is odd;
  2. the new imaginary unit l mirrors whatever passes through it: l a = a* l;
  3. take the mirror out of the doubling rule and the room collapses (zero divisors, lengths stop multiplying);
  4. the mirror is necessary, not sufficient: at 16 it is still there and the room still breaks.
"""
import numpy as np
rng = np.random.default_rng(1)

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mult(x, y, mirror=True):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    C = conj if mirror else (lambda v: v)
    m = lambda p, q: mult(p, q, mirror)
    return np.concatenate([m(a, c) - m(C(d), b), m(d, a) + m(b, C(c))])
def keeps_length(n, mirror, trials=300):
    for _ in range(trials):
        x, y = rng.normal(size=n), rng.normal(size=n)
        if not np.isclose(np.linalg.norm(mult(x, y, mirror)), np.linalg.norm(x) * np.linalg.norm(y)): return False
    return True

print("1. conjugation as a matrix: determinant at each level")
for n in (2, 4, 8, 16):
    print(f"   dim {n:2d}: {n-1:2d} imaginary axes flipped, det = {int(round(np.linalg.det(np.diag([1] + [-1]*(n-1)))))}")

print("2. the new unit l = (0,1) at each level: l a == conj(a) l  for random a below it")
for n in (2, 4, 8, 16):
    l = np.zeros(n); l[n // 2] = 1
    ok = all(np.allclose(mult(l, A), mult(conj(A), l)) for A in
             (np.concatenate([rng.normal(size=n // 2), np.zeros(n // 2)]) for _ in range(100)))
    print(f"   dim {n:2d}: {ok}")

print("3. doubling with and without the mirror: do lengths multiply?")
for n in (2, 4, 8, 16):
    print(f"   dim {n:2d}: with mirror {keeps_length(n, True)!s:5s}  without mirror {keeps_length(n, False)}")
x = np.array([1., 0, 0, 1]); y = np.array([1., 0, 0, -1])      # (1, i) and (1, -i) as pairs of complex numbers
print("   (1,i)*(1,-i) without the mirror:", mult(x, y, False), "<- two nonzero numbers multiply to zero")
print("   (1,i)*(1,-i) with the mirror:   ", mult(x, y, True))
