"""verify_transpose_coin.py -- checks every [FORCED] line of THE_TRANSPOSE_COIN.md
("The transpose's coin: byes in a round robin, and the Lo Shu mod 3").

Standard library + numpy.  ASCII output.  Exit code 1 on any failure.
Run:  python verify_latin_diagonal.py      (about a second)
"""
import random
import sys
from itertools import combinations, product

import numpy as np

FAILED = []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILED.append(label)


# ------------------------------------------------------------------ helpers
def is_latin(T):
    n = len(T)
    full = set(range(n))
    return (all(set(row) == full for row in T)
            and all({T[i][j] for i in range(n)} == full for j in range(n)))


def is_symmetric(T):
    n = len(T)
    return all(T[i][j] == T[j][i] for i in range(n) for j in range(n))


def diagonal(T):
    return [T[i][i] for i in range(len(T))]


def symmetric_latin_squares(n):
    """Every symmetric Latin square of order n, by filling the upper triangle."""
    cells = [(i, j) for i in range(n) for j in range(i, n)]
    G = [[None] * n for _ in range(n)]
    used = [set() for _ in range(n)]          # symbols already in row i (= column i)
    out = []

    def fill(k):
        if k == len(cells):
            out.append([row[:] for row in G])
            return
        i, j = cells[k]
        for s in range(n):
            if s in used[i] or s in used[j]:
                continue
            G[i][j] = G[j][i] = s
            used[i].add(s)
            used[j].add(s)
            fill(k + 1)
            used[i].discard(s)
            used[j].discard(s)
            G[i][j] = G[j][i] = None

    fill(0)
    return out


# ------------------------------------------- 1. the coin: parity on the edge
def involutions(n):
    """All involutions of {0..n-1} (as tuples p with p[p[i]] = i)."""
    def rec(rest, p):
        if not rest:
            yield tuple(p)
            return
        a = rest[0]
        p[a] = a
        yield from rec(rest[1:], p)
        for b in rest[1:]:
            p[a], p[b] = b, a
            yield from rec([x for x in rest[1:] if x != b], p)
        p[a] = a
    yield from rec(list(range(n)), [None] * n)


ok = True
counts = []
for n in range(1, 9):
    invs = list(involutions(n))
    counts.append(len(invs))
    ok &= all(sum(1 for i in range(n) if p[i] == i) % 2 == n % 2 for p in invs)
check("every involution of an n-set (n = 1..8) fixes a number of points with the parity of n "
      f"(involution counts {counts})", ok and counts == [1, 2, 4, 10, 26, 76, 232, 764])

# ------------------------------- 2. odd order: the diagonal is a transversal
for n, expected in ((3, 6), (5, 720)):
    S = symmetric_latin_squares(n)
    ok = all(sorted(diagonal(G)) == list(range(n)) for G in S)
    check(f"order {n}: all {len(S)} symmetric Latin squares (expected {expected}) carry every symbol "
          "exactly once on the diagonal", ok and len(S) == expected)

def random_symmetric_latin(n, rng, cap=20000):
    """One symmetric Latin square found by depth-first search in a random symbol order
    (restarted whenever a search exceeds `cap` nodes)."""
    cells = [(i, j) for i in range(n) for j in range(i, n)]
    while True:
        G = [[None] * n for _ in range(n)]
        used = [set() for _ in range(n)]
        nodes = [0]

        def fill(k):
            nodes[0] += 1
            if nodes[0] > cap:
                return None                       # give up on this search
            if k == len(cells):
                return True
            i, j = cells[k]
            syms = list(range(n))
            rng.shuffle(syms)
            for s in syms:
                if s in used[i] or s in used[j]:
                    continue
                G[i][j] = G[j][i] = s
                used[i].add(s)
                used[j].add(s)
                r = fill(k + 1)
                if r:
                    return True
                used[i].discard(s)
                used[j].discard(s)
                G[i][j] = G[j][i] = None
                if r is None:
                    return None
            return False

        if fill(0):
            return G


rng = random.Random(2026)
ok = True
seen = set()
for n in (7, 9):
    for _ in range(100):
        G = random_symmetric_latin(n, rng)
        seen.add((n, tuple(map(tuple, G))))
        ok &= is_latin(G) and is_symmetric(G) and sorted(diagonal(G)) == list(range(n))
check(f"orders 7 and 9: 200 symmetric Latin squares from randomized search ({len(seen)} distinct), "
      "diagonal always a transversal", ok and len(seen) > 190)
ok = True
for n in (7, 9, 11):
    for _ in range(300):
        # relabel a(x + y) mod n: one permutation on rows and columns, another on symbols
        P = list(range(n)); rng.shuffle(P)
        Q = list(range(n)); rng.shuffle(Q)
        a = rng.randrange(1, n)
        while np.gcd(a, n) != 1:
            a = rng.randrange(1, n)
        G = [[Q[(a * P[i] + a * P[j]) % n] for j in range(n)] for i in range(n)]
        ok &= is_latin(G) and is_symmetric(G) and sorted(diagonal(G)) == list(range(n))
check("orders 7, 9, 11: 900 random relabelings of the cyclic squares a(x + y), same result", ok)
fano = [{(k + 0) % 7, (k + 1) % 7, (k + 3) % 7} for k in range(7)]
ST7 = [[i if i == j else [next(iter(l - {i, j})) for l in fano if {i, j} <= l][0] for j in range(7)]
       for i in range(7)]
check("the Steiner quasigroup of the Fano plane (x*y = third point on the line xy, x*x = x) is a "
      "symmetric Latin square of order 7 with diagonal 0..6",
      is_latin(ST7) and is_symmetric(ST7) and diagonal(ST7) == list(range(7)))

K4 = [[i ^ j for j in range(4)] for i in range(4)]
Z4 = [[(i + j) % 4 for j in range(4)] for i in range(4)]
check("even order breaks it: Klein four-group table, diagonal "
      f"{diagonal(K4)}; Z/4 table, diagonal {diagonal(Z4)}",
      is_symmetric(K4) and is_symmetric(Z4) and diagonal(K4) == [0, 0, 0, 0] and diagonal(Z4) == [0, 2, 0, 2])

G5 = [[(i + 2 * j) % 5 for j in range(5)] for i in range(5)]
check("the converse fails at order 5: x + 2y (mod 5) has a transversal diagonal "
      f"{diagonal(G5)} but is not symmetric", is_latin(G5) and not is_symmetric(G5)
      and sorted(diagonal(G5)) == list(range(5)))

lat3 = [np.array(t).reshape(3, 3).tolist() for t in product(range(3), repeat=9)]
lat3 = [T for T in lat3 if is_latin(T)]
ok = all(is_symmetric(T) == (sorted(diagonal(T)) == [0, 1, 2]) for T in lat3)
check(f"order 3 only: among all {len(lat3)} Latin squares, symmetric <=> transversal diagonal",
      ok and len(lat3) == 12)

# --------------------------------------------------- 3. the round robin
S5 = [G for G in symmetric_latin_squares(5) if diagonal(G) == [0, 1, 2, 3, 4]]
V = list(range(6))                       # teams 0..4 plus the extra team 5
edges = list(combinations(V, 2))
matchings = []
for m in combinations(edges, 3):
    if len({v for e in m for v in e}) == 6:
        matchings.append(frozenset(m))
factorizations = set()
for five in combinations(matchings, 5):
    if len(set().union(*five)) == 15:
        factorizations.add(frozenset(five))
ok = True
for G in S5:
    rounds = []
    for r in range(5):
        games = {(i, j) for i in range(5) for j in range(i + 1, 5) if G[i][j] == r}
        bye = [i for i in range(5) if G[i][i] == r]
        ok &= len(bye) == 1
        rounds.append(frozenset(games | {(bye[0], 5)}))
    ok &= frozenset(rounds) in factorizations
check(f"order 5 with diagonal 0..4: {len(S5)} squares = {len(factorizations)} one-factorizations of K6 "
      "(OEIS A000438 gives 6); each square is a 5-team round robin with exactly one bye per round",
      ok and len(S5) == len(factorizations) == 6)

# --------------------------------------------------- 4. the Lo Shu mod 3
L = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
orients = []
R = L.copy()
for _ in range(4):
    orients += [R.copy(), R.T.copy()]
    R = np.rot90(R)
check("the Lo Shu has 8 distinct orientations", len({tuple(M.ravel()) for M in orients}) == 8)
tables = {}
for M in orients:
    tables.setdefault(tuple((M % 3).ravel()), []).append(M)
check("mod 3 they give 4 distinct tables, each from exactly 2 orientations",
      len(tables) == 4 and all(len(v) == 2 for v in tables.values()))
x = np.arange(3)[:, None]
y = np.arange(3)[None, :]
forms = {"x + y": (x + y) % 3, "1 - x - y": (1 - x - y) % 3,
         "x - y + 2": (x - y + 2) % 3, "y - x + 2": (y - x + 2) % 3}
names = {}
for key in tables:
    T = np.array(key).reshape(3, 3)
    names[key] = [nm for nm, F in forms.items() if (F == T).all()]
check(f"the four tables are exactly {sorted(n[0] for n in names.values())} (mod 3)",
      sorted(len(n) for n in names.values()) == [1, 1, 1, 1])
check("the Lo Shu itself reduces to x - y + 2 (mod 3)", ((L % 3) == forms["x - y + 2"]).all())
check("all four are Latin squares", all(is_latin(np.array(k).reshape(3, 3).tolist()) for k in tables))
lo = (L - 1) % 3
hi = (L - 1) // 3
check("why Latin (de la Hire): L - 1 in base 3 is two orthogonal Latin squares, and L = 1 + low digit (mod 3)",
      is_latin(lo.tolist()) and is_latin(hi.tolist())
      and len(set(zip(lo.ravel().tolist(), hi.ravel().tolist()))) == 9 and ((L % 3) == (lo + 1) % 3).all())
rows = []
for M in orients:
    d = [int(v) for v in np.diag(M)]
    rows.append((tuple(d), tuple(v % 3 for v in d), is_symmetric((M % 3).tolist())))
const = [r for r in rows if len(set(r[1])) == 1]
trans = [r for r in rows if sorted(r[1]) == [0, 1, 2]]
check(f"4 orientations keep the diagonal {sorted(set(r[0] for r in const))[0]} (= 2,2,2 mod 3): "
      "none commutative, as the coin forces", len(const) == 4 and not any(r[2] for r in const))
check(f"the other 4 carry the anti-diagonal {sorted(set(r[0] for r in trans))[0]} (a transversal mod 3): "
      "all commutative", len(trans) == 4 and all(r[2] for r in trans))
nc = [np.array(k).reshape(3, 3) for k in tables if not is_symmetric(np.array(k).reshape(3, 3).tolist())]
check("the two non-commutative tables are each other's transposes", len(nc) == 2 and (nc[0] == nc[1].T).all())
Q = np.rot90(L) % 3
check("the quarter-turn's table is a 3-team round robin: each round one game and one bye",
      is_symmetric(Q.tolist()) and sorted(np.diag(Q).tolist()) == [0, 1, 2])

print("-" * 72)
if FAILED:
    print(f"{len(FAILED)} check(s) FAILED")
    sys.exit(1)
print("all checks passed")
