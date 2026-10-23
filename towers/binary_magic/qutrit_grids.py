"""
qutrit_grids.py — the two-qutrit version of the Mermin-Peres search.

Operators: u = (a1, b1, a2, b2) in Z3^4  ->  X^a1 Z^b1 (x) X^a2 Z^b2   (Z X = w X Z, w = e^{2 pi i/3}).
They commute iff  a1 b1' - b1 a1' + a2 b2' - b2 a2' = 0 (mod 3).
A grid: 3x3 of distinct non-identity operators; every row and column is a commuting triple whose
product is a multiple of the identity (u + v + w = 0).
Contextuality test: a grid is paradoxical iff (product of row phases) != (product of column phases).
Also: is any grid a numerical magic square under some digit order of its labels?
"""
import itertools
from collections import Counter

V = [u for u in itertools.product(range(3), repeat=4) if any(u)]
idx = {u: i for i, u in enumerate(V)}
add = lambda u, v: tuple((x + y) % 3 for x, y in zip(u, v))
neg = lambda u: tuple((-x) % 3 for x in u)
def sym(u, v):
    return (u[0] * v[1] - u[1] * v[0] + u[2] * v[3] - u[3] * v[2]) % 3
def beta(p, q):              # phase exponent of (X^p Z^p')(X^q Z^q'): Z^b X^c = w^{bc} X^c Z^b
    return (p[1] * q[0] + p[3] * q[2]) % 3
def line_phase(u, v, w):
    return (beta(u, v) + beta(add(u, v), w)) % 3

comm = {u: [v for v in V if v != u and sym(u, v) == 0 and add(u, v) != (0, 0, 0, 0)] for u in V}
lines = {frozenset((u, v, neg(add(u, v)))) for u in V for v in comm[u]}
print(f"commuting triples with product ~ I: {len(lines)}")

grids = 0; ratio = Counter(); magic = Counter()
digit_orders = list(itertools.permutations(range(4)))
def label(u, order):
    return sum(u[order[k]] * 3 ** (3 - k) for k in range(4))
for x00 in V:
    for x01 in comm[x00]:
        x02 = neg(add(x00, x01))
        for x10 in comm[x00]:
            x20 = neg(add(x00, x10))
            if len({x00, x01, x02, x10, x20}) < 5:
                continue
            for x11 in comm[x10]:
                if sym(x11, x01) != 0:
                    continue
                x12 = neg(add(x10, x11)); x21 = neg(add(x01, x11))
                x22 = add(add(x00, x01), add(x10, x11))
                G = [[x00, x01, x02], [x10, x11, x12], [x20, x21, x22]]
                cells = [c for r in G for c in r]
                if (0, 0, 0, 0) in cells or len(set(cells)) < 9:
                    continue
                if not (sym(x20, x21) == sym(x20, x22) == sym(x21, x22) == 0 and
                        sym(x02, x12) == sym(x02, x22) == sym(x12, x22) == 0):
                    continue
                grids += 1
                rp = sum(line_phase(*G[i]) for i in range(3)) % 3
                cp = sum(line_phase(G[0][j], G[1][j], G[2][j]) for j in range(3)) % 3
                ratio[(rp - cp) % 3] += 1
                for o, order in enumerate(digit_orders):
                    L = [[label(c, order) for c in r] for r in G]
                    s = sum(L[0])
                    if all(sum(r) == s for r in L) and all(sum(c) == s for c in zip(*L)) and \
                       L[0][0] + L[1][1] + L[2][2] == s and L[0][2] + L[1][1] + L[2][0] == s:
                        magic[order] += 1
print(f"ordered grids: {grids:,}  -> distinct grids (rows/cols permuted, transposed): {grids // 72:,}")
print(f"row-phase product / column-phase product (exponent of w): {dict(ratio)}  "
      f"(any nonzero would be a paradox)")
tot = sum(magic.values())
print(f"grids that are also magic squares (sum on all 8 lines), over all 24 digit orders: {tot // 8} "
      f"distinct squares; by digit order: {dict((k, v // 8) for k, v in magic.items()) if magic else 0}")

# Why there are none. Corner cells x00, x01, x10, x11 fix the grid (every line sums to 0).
# Let a = [x01, x10] and b = [x00, x11]. The last row commutes iff a = b; the last column iff a = -b.
# Mod 2, a = -b is the same as a = b, so a = b = 1 works: that is the Mermin square.
# Mod 3, a = b and a = -b force a = b = 0. Then all four corners commute, so all nine cells lie in one
# isotropic plane, which has only 8 non-identity operators. Nine distinct cells cannot fit.
def check(p):
    Vp = [u for u in itertools.product(range(p), repeat=4) if any(u)]
    ad = lambda u, v: tuple((x + y) % p for x, y in zip(u, v))
    ng = lambda u: tuple((-x) % p for x in u)
    sy = lambda u, v: (u[0] * v[1] - u[1] * v[0] + u[2] * v[3] - u[3] * v[2]) % p
    seen = Counter()
    for x00 in Vp:
        for x01 in Vp:
            if sy(x00, x01): continue
            for x10 in Vp:
                if sy(x00, x10): continue
                for x11 in Vp:
                    if sy(x10, x11) or sy(x01, x11): continue
                    a, b = sy(x01, x10), sy(x00, x11)
                    x02, x12 = ng(ad(x00, x01)), ng(ad(x10, x11))
                    x20, x21 = ng(ad(x00, x10)), ng(ad(x01, x11))
                    x22 = ad(ad(x00, x01), ad(x10, x11))
                    row_ok = sy(x20, x21) == sy(x20, x22) == sy(x21, x22) == 0
                    col_ok = sy(x02, x12) == sy(x02, x22) == sy(x12, x22) == 0
                    assert row_ok == (a == b) and col_ok == (a == (-b) % p)
                    cells = {x00, x01, x02, x10, x11, x12, x20, x21, x22}
                    seen[(a == b, a == (-b) % p, a == 0, len(cells) == 9 and (0,) * 4 not in cells)] += 1
    return seen
s3 = check(3)
assert not any(k[0] and k[1] and k[3] for k in s3)            # never a full grid
assert all(k[2] for k in s3 if k[0] and k[1])                  # both conditions => a = b = 0
print("proof check (mod 3): last row <=> a = b, last column <=> a = -b; together they force a = b = 0,"
      " and then the nine cells never fit: True")
