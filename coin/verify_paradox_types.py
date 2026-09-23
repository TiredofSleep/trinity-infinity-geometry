#!/usr/bin/env python3
"""verify_paradox_types.py -- checks every [FORCED] line of PARADOX_TYPES.md.

    python verify_paradox_types.py      (a few seconds)

The author's four paradox types (Sanders & Mayes, April 2026), read through the coin:

  0  Theorem 0 (the Unified Orthogonality Principle): a family of views tells every pair apart
     exactly when no pair is merged by all of them -- on random maps, the cube's two shadows, and Z/30
  1  Type I, Zeno: the count view and the measure view
  2  Type II, the missing invariant: the free group's four pieces rebuild it twice over, and no
     way of measuring "how much" survives the turns
  3  Type III, a flip with no edge: the Liar (two values vs Kleene's three), the diagonal of
     Cantor / Lawvere, Russell's collection -- finite and exhaustive instances

The theorems themselves (Hausdorff, Banach-Tarski, Goedel, Tarski, Lawvere, Kripke) are cited, not
reproved; these are their finite instances.
"""
import itertools
import random
from fractions import Fraction

import numpy as np

rnd = random.Random(58)


def ok(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    assert cond, f"claim failed: {name}"


def merged(view, objects):
    """the ambiguity set of a view: the pairs of objects it cannot tell apart"""
    return {frozenset((x, y)) for x, y in itertools.combinations(objects, 2) if view(x) == view(y)}


def faithful(views, objects):
    return len({tuple(v(x) for v in views) for x in objects}) == len(objects)


# ============================================================ 0. Theorem 0
print("0 -- Theorem 0: views tell every pair apart exactly when no pair is merged by all of them")
agree = 0
for _ in range(3000):
    n, k = rnd.randint(2, 9), rnd.randint(1, 4)
    X = list(range(n))
    views = [dict((x, rnd.randrange(rnd.randint(1, 4))) for x in X) for _ in range(k)]
    fs = [v.__getitem__ for v in views]
    residual = set.intersection(*[merged(f, X) for f in fs])
    agree += faithful(fs, X) == (not residual)
ok(f"on 3000 random families of views: faithful exactly when the residual is empty ({agree}/3000)", agree == 3000)
X4 = range(4)
maps = list(itertools.product(range(2), repeat=4))
ok("exhaustively, every pair of yes/no views on 4 objects (256 pairs) obeys it",
   all(faithful([f.__getitem__, g.__getitem__], X4) == (not merged(f.__getitem__, X4) & merged(g.__getitem__, X4))
       for f in maps for g in maps))
C = [tuple(v) for v in itertools.product((1, -1), repeat=3)]
face = lambda v: (v[0], v[1])
Bd = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[2 ** 0.5], [6 ** 0.5]])
corner = lambda v: tuple(np.round(Bd @ np.array(v, float), 9) + 0.0)
Uf, Uc = merged(face, C), merged(corner, C)
ok(f"the cube's two shadows: face-on merges {len(Uf)} pairs of corners, corner-on merges {len(Uc)}, and no pair "
   "is merged by both -- so together they see all 8 corners", len(Uf) == 4 and len(Uc) == 1 and not Uf & Uc
   and faithful([face, corner], C))
Z30 = range(30)
mod = lambda m: (lambda x: x % m)
ok("on Z/30 (the principle's first home): mod 6 and mod 10 together tell all 30 apart (their lcm is 30); "
   "mod 2 and mod 6 do not, and adding more views of that same kind never helps",
   faithful([mod(6), mod(10)], Z30) and not faithful([mod(2), mod(6)], Z30)
   and not faithful([mod(2), mod(6), mod(3), mod(2)], Z30) and faithful([mod(2), mod(3), mod(5)], Z30))

# ============================================================ 1. Type I -- Zeno
print("\n1 -- Type I, insufficient coverage: Zeno")
steps = [Fraction(1, 2 ** k) for k in range(1, 41)]
partial = [sum(steps[:n]) for n in range(1, 41)]
ok("the count view sees infinitely many steps; the measure view sees them add to 1 - 1/2^n, below 1 and "
   "closing on it: the two views together say the runner arrives",
   all(p == 1 - Fraction(1, 2 ** (i + 1)) for i, p in enumerate(partial)) and all(p < 1 for p in partial)
   and 1 - partial[-1] < Fraction(1, 10 ** 12))

# ============================================================ 2. Type II -- the free group
print("\n2 -- Type II, the missing invariant: the free group on two turns")
INV = {"a": "A", "A": "a", "b": "B", "B": "b"}


def reduced_words(L):
    out = [""]
    frontier = [""]
    for _ in range(L):
        frontier = [w + c for w in frontier for c in "aAbB" if not (w and INV[w[-1]] == c)]
        out += frontier
    return out


def times(c, w):
    """left-multiply the reduced word w by the letter c"""
    return w[1:] if w and w[0] == INV[c] else c + w


W = reduced_words(9)
S = {c: {w for w in W if w.startswith(c)} for c in "aAbB"}
ok(f"its {len(W)} reduced words up to length 9 split into the identity and four pieces S(a), S(a^-1), S(b), "
   "S(b^-1) (the words starting with each letter)",
   sum(len(S[c]) for c in "aAbB") + 1 == len(W) and all(not S[x] & S[y] for x, y in itertools.combinations("aAbB", 2)))
ok("... and two pieces rebuild the whole group: every word is in S(a) or in a*S(a^-1), never both -- and the "
   "same with b: four pieces, two whole copies (Hausdorff)",
   all((w in S["a"]) != (times("A", w).startswith("A")) for w in W)
   and all((w in S["b"]) != (times("B", w).startswith("B")) for w in W))
m = 8
ok("... so no way of measuring 'how much' can survive the turns: among the words of length 8, S(a^-1) holds "
   "one quarter, yet its turn a*S(a^-1) holds three quarters",
   sum(1 for w in W if len(w) == m and w.startswith("A")) * 4 == sum(1 for w in W if len(w) == m)
   and sum(1 for w in W if len(w) == m and not w.startswith("a")) * 4 == 3 * sum(1 for w in W if len(w) == m))

# ============================================================ 3. Type III -- a flip with no edge
print("\n3 -- Type III, a flip with no edge, and self-reference that demands one")
NOT2 = {"T": "F", "F": "T"}
NOT3 = {"T": "F", "F": "T", "U": "U"}
ok("the Liar asks for a value equal to its own negation: two values have none; Kleene's three values have "
   "exactly one -- the edge, 'neither' (Kripke's ungrounded Liar)",
   [v for v in NOT2 if NOT2[v] == v] == [] and [v for v in NOT3 if NOT3[v] == v] == ["U"])


def diagonal_escapes(Y, flip, n):
    """does the flipped diagonal escape every family phi: A -> Y^A, for |A| = n?"""
    funcs = list(itertools.product(Y, repeat=n))
    for phi in itertools.product(funcs, repeat=n):
        d = tuple(flip[phi[a][a]] for a in range(n))
        if d in phi:
            return False
    return True


ok("Cantor / Lawvere, exhaustively for |A| = 1, 2, 3: with the yes/no flip (no edge), the flipped diagonal of "
   "every family is missing from it -- no family reaches every function",
   all(diagonal_escapes((0, 1), {0: 1, 1: 0}, n) for n in (1, 2, 3)))
ok("... give the flip an edge (a third value it keeps) and the argument fails: some family contains its own "
   "flipped diagonal", not diagonal_escapes((0, "U", 1), {0: 1, 1: 0, "U": "U"}, 2))


def russell_never_a_member(n):
    X = range(n)
    for bits in itertools.product((0, 1), repeat=n * n):
        E = {(x, y) for i, (x, y) in enumerate(itertools.product(X, X)) if bits[i]}   # (x, y): x is a member of y
        R = frozenset(x for x in X if (x, x) not in E)
        if any(R == frozenset(x for x in X if (x, y) in E) for y in X):
            return False
    return True


ok("Russell, exhaustively for every membership relation on 1, 2 and 3 objects: the collection of things "
   "that are not members of themselves is never one of the things", all(russell_never_a_member(n) for n in (1, 2, 3)))

print("\n" + "=" * 78)
print("ALL PARADOX-TYPE CHECKS PASS -- classified, not resolved.")
print("=" * 78)
