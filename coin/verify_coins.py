#!/usr/bin/env python3
"""verify_coins.py -- checks every [FORCED] line of THE_COIN.md.

    python verify_coins.py      (a few seconds)

A coin is a flip -- a move that, done twice, changes nothing -- with two sides (what it swaps)
and an edge (what it leaves in place). This script checks:

  1  the flips are flips, and the odd rule: whatever a flip negates vanishes on its edge
  2  the author's three coins on the sphere of numbers: -z, 1/z, -1/z are the half-turns about
     the three axes of the octahedron 0, oo, +-1, +-i; they commute; only the centre is kept by
     all three; z -> 1/conj(z) keeps the unit circle; z -> i/z swaps real and imaginary
  3  missing edges: x -> 2/x keeps no fraction (x -> n/x keeps one exactly when n is a square);
     x -> -1/x keeps no real number; the Dedekind cut at sqrt(2) has no edge among the fractions
  4  the keystone for sqrt(2): point toward it, measure off it, never stand on it
  5  one cube, two lenses: its two tetrahedra face-on and corner-on; the octahedron they share;
     the magic angle between the lenses; Cl(3)'s even and odd halves are the two tetrahedra
  6  the edge inhabited or empty: the solid symmetry groups have only even orbits besides the
     centre, so 5, 7, 9 stand on their centres; the plane's most symmetric n points are the n-gon
  7  the whole coin (heads, tails, edge): 27 = 8 + 12 + 6 + 1, 9 = 4 + 4 + 1
  8  every tower's coin: duality; conjugation; the mirror and the double cover; the dual
     lattice; the node; growing, shrinking and the circle
"""
import itertools
from fractions import Fraction
from math import comb, isqrt

import numpy as np
from numpy.polynomial import legendre

rng = np.random.default_rng(2)
PHI = (1 + 5 ** 0.5) / 2


def ok(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    assert cond, f"claim failed: {name}"


def keyset(A, nd=9):
    return {tuple(np.round(np.asarray(a, float), nd) + 0.0) for a in A}


# ======================================================== 1. what a coin is
print("1 -- a coin: a flip, its two sides, its edge")
z = rng.normal(size=300) + 1j * rng.normal(size=300)
x3 = rng.normal(size=(300, 3))
mirror = np.diag([1.0, 1.0, -1.0])
flips = [(lambda v: -v, z), (np.conj, z), (lambda v: 1 / np.conj(v), z),
         (lambda v: -v, x3), (lambda v: v @ mirror, x3)]
ok("negation, conjugation, inversion in the circle, the central flip and a mirror are flips: "
   "done twice, each changes nothing", all(np.allclose(f(f(s)), s) for f, s in flips))
edge_part = lambda f, x: (x + f(x)) / 2
side_part = lambda f, x: (x - f(x)) / 2
ok("every linear flip splits each thing in two: the average with its flip lies on the edge, half the "
   "difference is what the flip negates (checked for conjugation and the mirror)",
   all(np.allclose(f(edge_part(f, s)), edge_part(f, s)) and np.allclose(f(side_part(f, s)), -side_part(f, s))
       and np.allclose(edge_part(f, s) + side_part(f, s), s) for f, s in [(np.conj, z), (lambda v: v @ mirror, x3)]))
ok("... for conjugation the two parts are the real part and the imaginary part: z = Re z + i Im z",
   np.allclose(edge_part(np.conj, z), z.real) and np.allclose(side_part(np.conj, z), 1j * z.imag))
th = rng.uniform(-3, 3, 200)
ok("... for the turn, reversing its direction (theta -> -theta) splits e^(i theta) into cos theta, "
   "real, on the edge, and i sin theta, imaginary: Euler's formula is the turn's coin",
   np.allclose((np.exp(1j * th) + np.exp(-1j * th)) / 2, np.cos(th))
   and np.allclose((np.exp(1j * th) - np.exp(-1j * th)) / 2, 1j * np.sin(th)))
ok("... and for growth the same split of e^x is cosh x + sinh x",
   np.allclose((np.exp(th) + np.exp(-th)) / 2, np.cosh(th)) and np.allclose((np.exp(th) - np.exp(-th)) / 2, np.sinh(th)))
Am = rng.normal(size=(3, 3))
Sym, Skw = (Am + Am.T) / 2, (Am - Am.T) / 2


def expm(A, terms=60):
    out, term = np.eye(len(A)), np.eye(len(A))
    for k in range(1, terms):
        term = term @ A / k
        out = out + term
    return out


ok("... for matrices, the transpose splits A into a symmetric part (the edge: real eigenvalues; its "
   "exponential stretches) and a skew part (imaginary eigenvalues; its exponential turns)",
   np.allclose(Sym + Skw, Am) and np.allclose(np.linalg.eigvals(Sym).imag, 0)
   and np.allclose(np.linalg.eigvals(Skw).real, 0)
   and np.all(np.linalg.eigvalsh(expm(Sym)) > 0)
   and np.allclose(expm(Skw).T @ expm(Skw), np.eye(3)) and np.isclose(np.linalg.det(expm(Skw)), 1))
ok("the odd rule: whatever a flip negates vanishes on its edge -- Im(z) on the real line (above)",
   np.allclose(np.conj(z).imag, -z.imag) and np.allclose(edge_part(np.conj, z).imag, 0))
circle = np.exp(1j * rng.uniform(0, 2 * np.pi, 50))
ok("... log|z| is negated by inversion z -> 1/conj(z), and vanishes on its edge, the unit circle",
   np.allclose(np.log(abs(1 / np.conj(z))), -np.log(abs(z))) and np.allclose(1 / np.conj(circle), circle)
   and np.allclose(np.log(abs(circle)), 0))
ok("... the orbital p_z = z is negated by the mirror, and vanishes on its edge, the plane z = 0",
   np.allclose((x3 @ mirror)[:, 2], -x3[:, 2]))
ok("... the central flip keeps exactly one point, the centre (x = -x only at 0)",
   np.linalg.matrix_rank(-np.eye(3) - np.eye(3)) == 3)

# ======================================================== 2. the three coins on one sphere
print("\n2 -- the author's three coins are three flips of one sphere")


def S(w):
    """stereographic projection: a complex number, or None for infinity, to the unit sphere"""
    if w is None:
        return np.array([0.0, 0.0, 1.0])
    r2 = abs(w) ** 2
    return np.array([2 * w.real, 2 * w.imag, r2 - 1]) / (r2 + 1)


six = {"0": 0j, "oo": None, "1": 1 + 0j, "-1": -1 + 0j, "i": 1j, "-i": -1j}
P = {k: S(v) for k, v in six.items()}
ok("0, oo, 1, -1, i, -i land on the six corners of a regular octahedron (+-x, +-y, +-z)",
   keyset(P.values()) == keyset(np.vstack([np.eye(3), -np.eye(3)])))
H = {"-z": np.diag([-1.0, -1, 1]), "1/z": np.diag([1.0, -1, -1]), "-1/z": np.diag([-1.0, 1, -1])}
F = {"-z": lambda w: -w, "1/z": lambda w: 1 / w, "-1/z": lambda w: -1 / w}
ok("each flip is a half-turn of the sphere about an axis of that octahedron (300 random z)",
   all(np.allclose(S(F[k](w)), H[k] @ S(w)) for k in H for w in z))


def kept(R):
    return keyset([p for p in P.values() if np.allclose(R @ p, p)])


ok("their edges: -z keeps 0 and oo; 1/z keeps 1 and -1; -1/z keeps i and -i",
   kept(H["-z"]) == keyset([P["0"], P["oo"]]) and kept(H["1/z"]) == keyset([P["1"], P["-1"]])
   and kept(H["-1/z"]) == keyset([P["i"], P["-i"]]))


def swapped(R):
    names = list(P)
    return {frozenset((a, b)) for a in names for b in names if a != b and np.allclose(R @ P[a], P[b])}


ok("what they swap: -z trades 1/-1 and i/-i; 1/z trades 0/oo and i/-i; -1/z trades 0/oo and 1/-1",
   swapped(H["-z"]) == {frozenset(("1", "-1")), frozenset(("i", "-i"))}
   and swapped(H["1/z"]) == {frozenset(("0", "oo")), frozenset(("i", "-i"))}
   and swapped(H["-1/z"]) == {frozenset(("0", "oo")), frozenset(("1", "-1"))})
ok("the three commute, and any two make the third (the Klein four-group)",
   all(np.allclose(H[a] @ H[b], H[b] @ H[a]) for a in H for b in H)
   and np.allclose(H["-z"] @ H["1/z"], H["-1/z"]) and np.allclose(H["1/z"] @ H["-1/z"], H["-z"]))
ok("on the real line -1/x keeps nothing: x = -1/x means x^2 = -1, whose roots are +-i",
   np.allclose(sorted(np.roots([1, 0, 1]), key=lambda c: c.imag), [-1j, 1j]))
stack = np.vstack([R - np.eye(3) for R in H.values()])
ok("no number is kept by all three; the one point all three half-turns keep is the sphere's centre",
   np.linalg.matrix_rank(stack) == 3 and not any(all(np.allclose(R @ p, p) for R in H.values())
                                                 for p in P.values()))
ok("reflect instead of turn: z -> 1/conj(z) is the mirror in the equator -- it still trades 0 and oo, "
   "and keeps the whole unit circle",
   all(np.allclose(S(1 / np.conj(w)), mirror @ S(w)) for w in z) and all(np.isclose(S(c)[2], 0) for c in circle))
ip = np.exp(1j * np.pi / 4)
reals = rng.normal(size=40)
ok("z -> i/z trades the real axis for the imaginary axis (1 <-> i); its edge is +-e^(i pi/4) = +-sqrt(i)",
   np.allclose((1j / reals).real, 0) and np.allclose((1j / (1j * reals)).imag, 0)
   and np.isclose(1j / ip, ip) and np.isclose(ip ** 2, 1j) and np.allclose(1j / (1j / z), z))
ok("... on the sphere that edge is the midpoint of the octahedron's edge from 1 to i",
   np.allclose(S(ip), (P["1"] + P["i"]) / np.linalg.norm(P["1"] + P["i"])))

# ======================================================== 3. missing edges
print("\n3 -- missing edges: where the paradoxes are")
fracs = {Fraction(p, q) for q in range(1, 60) for p in range(1, 120)}
ok("x -> 2/x is a flip on the fractions; it swaps those whose square is below 2 with those above",
   all(2 / (2 / x) == x for x in fracs) and all((x * x < 2) == ((2 / x) ** 2 > 2) for x in fracs if x * x != 2))


def odd_prime(n):
    """a prime to an odd power in n -- the certificate that no fraction squares to n"""
    m, p = n, 2
    while p * p <= m:
        e = 0
        while m % p == 0:
            m, e = m // p, e + 1
        if e % 2:
            return p
        p += 1
    return m if m > 1 else None


ok("... and it keeps no fraction: p^2 = 2q^2 is impossible (2 appears to an odd power on one side)",
   odd_prime(2) == 2 and all(isqrt(2 * q * q) ** 2 != 2 * q * q for q in range(1, 20001)))
ok("x -> n/x keeps a fraction exactly when n is a square (n <= 200; every non-square has a prime "
   "to an odd power, the certificate)", all((isqrt(n) ** 2 == n) == (odd_prime(n) is None) for n in range(1, 201)))
ok("x -> -1/x is a flip on the real line; it swaps the positive and negative numbers and keeps none",
   np.allclose(-1 / (-1 / reals), reals) and np.all(np.sign(-1 / reals) == -np.sign(reals)))
step = lambda q: (2 * q + 2) / (q + 2)
ok("the cut at sqrt(2) has no edge among the fractions: below it there is always a larger fraction, "
   "above it a smaller one (Dedekind)",
   all((step(x) > x and step(x) ** 2 < 2) if x * x < 2 else (step(x) < x and step(x) ** 2 > 2) for x in fracs))

# ======================================================== 4. the keystone for sqrt(2)
print("\n4 -- the keystone for sqrt(2): point toward it, measure off it, never stand on it")
x, heron = Fraction(1), []
for _ in range(4):
    x = (x + 2 / x) / 2
    heron.append(x)
ok("point toward it: average the two sides, x -> (x + 2/x)/2: 3/2, 17/12, 577/408, 665857/470832",
   heron == [Fraction(3, 2), Fraction(17, 12), Fraction(577, 408), Fraction(665857, 470832)])
ok("... each average and its flip lie on the two sides, and the gap between them closes in",
   all(h * h > 2 > (2 / h) ** 2 for h in heron) and 0 < heron[-1] - 2 / heron[-1] < Fraction(1, 10 ** 11))
r2 = 2 ** 0.5
closest = [(round(q * r2), q) for q in range(1, 10001)]
ok("never stand on it: p^2 - 2q^2 is never 0 (so, being a whole number, it is at least 1 in size)",
   all(p * p - 2 * q * q != 0 for p, q in closest))
worst = min(q * q * abs(p / q - r2) for p, q in closest)
ok(f"measure off it: every fraction p/q stays more than 1/(3q^2) away (q <= 10000; closest {worst:.4f}/q^2)",
   worst > 1 / 3)

# ======================================================== 5. one cube, two lenses
print("\n5 -- one cube, two lenses")
C = np.array(list(itertools.product((1, -1), repeat=3)), float)
Tp, Tm = C[np.prod(C, axis=1) > 0], C[np.prod(C, axis=1) < 0]
dist = lambda A: np.linalg.norm(A[:, None] - A[None], axis=-1)[np.triu_indices(len(A), 1)]
ok("the cube's 8 corners are two regular tetrahedra, 4 + 4 (Kepler's stella octangula)",
   len(Tp) == len(Tm) == 4 and np.allclose(dist(Tp), 8 ** 0.5) and np.allclose(dist(Tm), 8 ** 0.5))
ok("the central flip x -> -x swaps the two tetrahedra (and keeps only the centre, section 1)",
   keyset(-Tp) == keyset(Tm))


def inside(T, p):
    lam = np.linalg.solve(np.vstack([T.T, np.ones(4)]), np.append(p, 1.0))
    return bool(np.all(lam >= -1e-12))


pts = rng.uniform(-1.2, 1.2, size=(4000, 3))
ok("what the two tetrahedra share, as solids, is the octahedron |x| + |y| + |z| <= 1 (4000 points)",
   all((inside(Tp, p) and inside(Tm, p)) == (np.abs(p).sum() <= 1) for p in pts))
face = lambda A: keyset(A[:, :2])
Bd = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[2 ** 0.5], [6 ** 0.5]])
corner = lambda A: keyset(A @ Bd.T)
ok("face-on, both tetrahedra cast the same square: the two sides cannot be told apart",
   face(Tp) == face(Tm) == keyset([(1, 1), (1, -1), (-1, 1), (-1, -1)]))
cp, cm = corner(Tp), corner(Tm)
tri = lambda K: {k for k in K if not np.allclose(k, 0)}
angles = lambda K: sorted(np.degrees(np.arctan2(k[1], k[0])) % 360 for k in K)
ok("corner-on they separate: two triangles turned 60 degrees against each other, filling a regular "
   "hexagon (the six-pointed star), with both apexes on the centre",
   (0.0, 0.0) in cp and (0.0, 0.0) in cm and len(tri(cp)) == len(tri(cm)) == 3
   and np.allclose(np.diff(angles(tri(cp))), 120) and np.allclose(np.diff(angles(tri(cm))), 120)
   and np.allclose(np.diff(angles(tri(cp) | tri(cm))), 60) and len({round(np.hypot(*k), 9) for k in tri(cp) | tri(cm)}) == 1)
ok("neither shadow alone tells the 8 corners apart (face-on 8 -> 4, corner-on 8 -> 7); the two together do",
   len(face(C)) == 4 and len(corner(C)) == 7
   and len({(tuple(np.round(c[:2], 9)), tuple(np.round(Bd @ c, 9))) for c in C}) == 8)
c2 = (np.array([0.0, 0, 1]) @ (np.ones(3) / 3 ** 0.5)) ** 2
ok("the angle between the two lenses is the magic angle: cos^2 = 1/3, where P2 = (3x^2 - 1)/2 is 0",
   np.isclose(c2, 1 / 3) and np.isclose((3 * c2 - 1) / 2, 0))


def blade_mul(a, b):
    """product of two basis blades of Cl(3) (bitmasks: bit i = e_(i+1)): (sign, blade)"""
    s, x = 0, a >> 1
    while x:
        s += bin(x & b).count("1")
        x >>= 1
    return (-1) ** s, a ^ b


coord = lambda b: tuple(1 - 2 * ((b >> i) & 1) for i in range(3))
even = [b for b in range(8) if bin(b).count("1") % 2 == 0]
odd = [b for b in range(8) if bin(b).count("1") % 2 == 1]
ok("in the cube's algebra Cl(3), the even pieces (1, e12, e13, e23) sit on one tetrahedron and the "
   "odd pieces (e1, e2, e3, e123) on the other",
   keyset([coord(b) for b in even]) == keyset(Tp) and keyset([coord(b) for b in odd]) == keyset(Tm))
biv = [3, 5, 6]
ok("the grade flip keeps the even half and negates the odd half; the even half is closed, and it is the "
   "quaternions: e12, e13, e23 each square to -1 and anticommute",
   all(blade_mul(a, b)[1] in even for a in even for b in even)
   and all(blade_mul(b, b) == (-1, 0) for b in biv)
   and all(blade_mul(a, b)[0] == -blade_mul(b, a)[0] for a in biv for b in biv if a != b))

# ======================================================== 6. the edge inhabited or empty
print("\n6 -- the centre: the edge every symmetry keeps -- inhabited, or empty")


def rot(axis, ang):
    a = np.asarray(axis, float) / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def closure(gens):
    key = lambda M: tuple(np.round(M, 6).ravel() + 0.0)
    G, todo = {key(np.eye(3)): np.eye(3)}, [np.eye(3)]
    while todo:
        new = []
        for A in todo:
            for g in gens:
                M = g @ A
                if key(M) not in G:
                    G[key(M)] = M
                    new.append(M)
        todo = new
    return list(G.values())


def orbit_sizes(G):
    """every orbit size: the centre, a generic point on each axis and each mirror, a generic point"""
    cands = [np.zeros(3), rng.normal(size=3)]
    for g in G:
        _, s, vt = np.linalg.svd(g - np.eye(3))
        Fix = vt[s < 1e-9].T
        if Fix.shape[1] in (1, 2):
            cands.append(Fix @ rng.normal(size=Fix.shape[1]))
    return sorted({len(keyset([g @ p for g in G], 6)) for p in cands})


Tr = closure([rot((1, 1, 1), 2 * np.pi / 3), rot((0, 0, 1), np.pi)])
Or = closure([rot((0, 0, 1), np.pi / 2), rot((1, 1, 1), 2 * np.pi / 3)])
Ir = closure([rot((0, 1, PHI), 2 * np.pi / 5), rot((1, 1, 1), 2 * np.pi / 3)])
Td = closure(Tr + [np.array([[0.0, 1, 0], [1, 0, 0], [0, 0, 1]])])
Th = closure(Tr + [-np.eye(3)])
Oh = closure(Or + [-np.eye(3)])
Ih = closure(Ir + [-np.eye(3)])
groups = dict(T=Tr, O=Or, I=Ir, Td=Td, Th=Th, Oh=Oh, Ih=Ih)
menus = {n: orbit_sizes(G) for n, G in groups.items()}
for n, m in menus.items():
    print(f"         {n:2s} ({len(groups[n]):3d} symmetries): orbits {m}")
ok("the solid symmetry groups: Td orbits 1, 4, 6, 12, 24; Oh 1, 6, 8, 12, 24, 48; Ih 1, 12, 20, 30, 60, 120",
   menus["Td"] == [1, 4, 6, 12, 24] and menus["Oh"] == [1, 6, 8, 12, 24, 48]
   and menus["Ih"] == [1, 12, 20, 30, 60, 120])
ok("every orbit except the centre is even, in all seven solid groups -- so an odd number of points with "
   "solid symmetry must stand on the centre: 5, 7 and 9 are forced to, not chosen",
   all(all(k % 2 == 0 for k in m if k != 1) for m in menus.values()))


def plane_best(n):
    """most symmetric n points in the plane: D_k has orbits 1 (the centre), k, 2k; maximize 2k"""
    ways = [(2 * k, k, c, a, b) for k in range(1, n + 1) for c in (0, 1)
            for a in range(n // k + 1) for b in range(n // (2 * k) + 1)
            if a + b >= 1 and c + a * k + 2 * b * k == n]
    top = max(w[0] for w in ways)
    return [w for w in ways if w[0] == top]


ok("in the plane the most symmetric n points are the regular n-gon, uniquely, and its centre is empty (n = 2..12)",
   all(plane_best(n) == [(2 * n, n, 0, 1, 0)] for n in range(2, 13)))


def walk(n, k):
    """walk the n corners of the flat face, k at a time: the loops it makes"""
    seen, loops = set(), []
    for s in range(n):
        if s in seen:
            continue
        loop, i = [], s
        while i not in loop:
            loop.append(i)
            i = (i + k) % n
        seen |= set(loop)
        loops.append(loop)
    return loops


from math import gcd

ok("the flat face, walked: stepping k at a time around n corners makes one loop exactly when k shares "
   "no factor with n -- otherwise gcd(n, k) separate loops (n = 3..16, every k)",
   all((len(walk(n, k)) == 1) == (gcd(n, k) == 1) and len(walk(n, k)) == gcd(n, k)
       for n in range(3, 17) for k in range(1, n)))
phi = lambda n: sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)
ok("... the single-loop steps number Euler's phi(n), and for a prime n every step is one loop -- the "
   "pentagon and the pentagram at 5, the heptagon and two heptagrams at 7",
   all(sum(1 for k in range(1, n) if len(walk(n, k)) == 1) == phi(n) for n in range(3, 17))
   and all(all(len(walk(p, k)) == 1 for k in range(1, p)) for p in (3, 5, 7, 11, 13))
   and [k for k in range(1, 4) if len(walk(7, k)) == 1] == [1, 2, 3])


def winding(n, k):
    """times the loop k, 2k, 3k, ... (mod n) goes round the centre: total turning / 2 pi"""
    turn = sum(np.angle(np.exp(2j * np.pi * k / n)) for _ in range(n))
    return round(turn / (2 * np.pi))


ok("... every single loop winds round the centre min(k, n - k) times and never touches it: the chord "
   "from one corner to the next passes the centre at distance cos(pi k / n) > 0",
   all(abs(winding(n, k)) == min(k, n - k) and np.cos(np.pi * min(k, n - k) / n) > 0
       for n in range(3, 17) for k in range(1, n) if gcd(n, k) == 1))
corner_hex = sorted((np.degrees(np.arctan2(k[1], k[0])) % 360, k) for k in tri(cp) | tri(cm))
ok("... and at 6, step 2 splits the hexagon into two triangles -- exactly the cube's corner-on shadow, "
   "whose alternate corners are its two tetrahedra",
   sorted(map(sorted, walk(6, 2))) == [[0, 2, 4], [1, 3, 5]]
   and all(({corner_hex[j][1] for j in loop} == tri(cp)) or ({corner_hex[j][1] for j in loop} == tri(cm))
           for loop in walk(6, 2)))

# ======================================================== 7. the whole coin
print("\n7 -- the whole coin: heads, tails, and the edge")
G3 = [tuple(v) for v in itertools.product((-1, 0, 1), repeat=3)]
by_edge = [sum(1 for v in G3 if v.count(0) == k) for k in range(4)]
ok("three coins that land heads (+1), tails (-1) or on the edge (0): 27 = 8 + 12 + 6 + 1, "
   "which is (2 + 1)^3 spelled out", by_edge == [8, 12, 6, 1] == [comb(3, k) * 2 ** (3 - k) for k in range(4)])
corners = [v for v in G3 if 0 not in v]
edges3 = [(a, b) for a, b in itertools.combinations(corners, 2) if sum(p != q for p, q in zip(a, b)) == 1]
mids = {tuple((p + q) // 2 for p, q in zip(a, b)) for a, b in edges3}
ok("... they are the cube's 8 corners, the midpoints of its 12 edges, the centres of its 6 faces, and "
   "its centre -- the Rubik's cube's corner pieces, edge pieces, centres and core",
   len(edges3) == 12 and mids == {v for v in G3 if v.count(0) == 1}
   and keyset([v for v in G3 if v.count(0) == 2]) == keyset(np.vstack([np.eye(3), -np.eye(3)])))
signed = [np.diag(s) @ np.eye(3)[list(p)] for p in itertools.permutations(range(3))
          for s in itertools.product((1, -1), repeat=3)]
ok("... and each of the four kinds is one orbit of the cube's 48 symmetries",
   all(keyset([M @ np.array(next(v for v in G3 if v.count(0) == k)) for M in signed])
       == keyset([v for v in G3 if v.count(0) == k]) for k in range(4)))


def siamese(n):
    """the book's walking rule (Ch. 13): start top-middle, step up-right, drop down when blocked"""
    M = np.zeros((n, n), int)
    i, j = 0, n // 2
    for s in range(1, n * n + 1):
        M[i, j] = s
        a, b = (i - 1) % n, (j + 1) % n
        i, j = (a, b) if M[a, b] == 0 else ((i + 1) % n, j)
    return M


ok("the magic square's coin: in every walked odd square (n = 3, 5, 7, 9) the half-turn swaps each number s "
   "with n^2 + 1 - s, and keeps the centre, (n^2 + 1)/2 -- in the Lo Shu, s with 10 - s round the 5",
   all((siamese(n) + np.rot90(siamese(n), 2) == n * n + 1).all() and siamese(n)[n // 2, n // 2] == (n * n + 1) // 2
       and len({*siamese(n).sum(0), *siamese(n).sum(1), np.trace(siamese(n)), np.trace(np.fliplr(siamese(n)))}) == 1
       for n in (3, 5, 7, 9)) and siamese(3)[1, 1] == 5)
G2 = list(itertools.product((-1, 0, 1), repeat=2))
ok("two such coins: 9 = 4 + 4 + 1 -- the 3 x 3 grid: four corners, four edge-midpoints, the centre",
   [sum(1 for v in G2 if v.count(0) == k) for k in range(3)] == [4, 4, 1])
ok("in any dimension: every coin on a side is the cube (2^n); exactly one on a side is the "
   "cross-polytope (2n); every coin on its edge is the centre (n = 1..6)",
   all(sum(1 for v in itertools.product((-1, 0, 1), repeat=n) if v.count(0) == 0) == 2 ** n
       and sum(1 for v in itertools.product((-1, 0, 1), repeat=n) if v.count(0) == n - 1) == 2 * n
       for n in range(1, 7)))

# ======================================================== 8. every tower's coin
print("\n8 -- every tower is a coin")
# tower 1: duality
ys = rng.normal(size=(200, 6))
ok("shapes: duality turns the cube into the cross-polytope and back -- the cube's widest reach in "
   "direction y is sum|y_i|, the cross-polytope's is max|y_i| (n = 2..6)",
   all(np.allclose(max(y[:n] @ c for c in itertools.product((1, -1), repeat=n)), np.abs(y[:n]).sum())
       and np.isclose(max(np.abs(y[:n])), max(np.max(np.vstack([np.eye(n), -np.eye(n)]) @ y[:n]), 0))
       for n in range(2, 7) for y in ys[:30]))
def facets(V, normals):
    """the faces of the convex hull of V cut out by the given directions, kept if (n-1)-dimensional"""
    out = set()
    for u in normals:
        h = V @ u
        Fv = V[np.isclose(h, h.max())]
        if np.linalg.matrix_rank(Fv[1:] - Fv[0]) == V.shape[1] - 1:
            out.add(frozenset(map(tuple, np.round(Fv, 9))))
    return out


def corners_are_faces(n):
    cubeV = np.array(list(itertools.product((1, -1), repeat=n)), float)
    crossV = np.vstack([np.eye(n), -np.eye(n)])
    f_cube, f_cross = facets(cubeV, crossV), facets(crossV, cubeV)
    return (len(f_cube) == 2 * n and all(len(f) == 2 ** (n - 1) for f in f_cube)
            and len(f_cross) == 2 ** n and all(len(f) == n for f in f_cross))


ok("... so corners and faces trade places: each corner of the cross-polytope cuts out a face of the "
   "cube (2n faces of 2^(n-1) corners), each corner of the cube a face of the cross-polytope (2^n "
   "faces, each a simplex of n corners) (n = 2..6)", all(corners_are_faces(n) for n in range(2, 7)))


def regular_simplex(n):
    E = np.eye(n + 1) - 1 / (n + 1)
    basis = np.linalg.svd(E)[2][:n]
    V = E @ basis.T
    return V / np.linalg.norm(V, axis=1, keepdims=True)


def simplex_self_dual(n):
    V = regular_simplex(n)
    W = -n * V                                      # the proposed dual: the simplex, turned over
    on = np.isclose(W @ V.T, 1)                     # w_j on the face opposite v_j: w_j . v_i = 1, i != j
    return np.allclose(V @ V.T - np.eye(n + 1) * (1 + 1 / n), -1 / n) and all(
        on[j].sum() == n and (W[j] @ V[j]) < 1 for j in range(n + 1))


ok("... and the simplex is its own dual (turned over), in every dimension: it sits on the edge (n = 2..7)",
   all(simplex_self_dual(n) for n in range(2, 8)))
ico = np.array([p for c in range(3) for p in (np.roll([0, s1, s2 * PHI], c)
                                             for s1 in (1, -1) for s2 in (1, -1))], float)
dic = np.linalg.norm(ico[:, None] - ico[None], axis=-1)
e_ico = np.isclose(dic, dic[dic > 0].min())
tris = [t for t in itertools.combinations(range(12), 3) if all(e_ico[a, b] for a, b in itertools.combinations(t, 2))]
dod = np.array([ico[list(t)].mean(axis=0) for t in tris])
ddd = np.linalg.norm(dod[:, None] - dod[None], axis=-1)
e_dod = np.isclose(ddd, ddd[ddd > 0].min())
def pentagon_round(v):
    """the centres of the 5 triangles around corner v: a flat regular pentagon (a face of the dual)"""
    Q = np.array([ico[list(t)].mean(axis=0) for t in tris if v in t])
    c = Q.mean(axis=0)
    plane = np.linalg.matrix_rank(Q[1:] - Q[0], tol=1e-9) == 2
    rad = np.linalg.norm(Q - c, axis=1)
    dq = np.linalg.norm(Q[:, None] - Q[None], axis=-1)
    side = dq[dq > 1e-9].min()
    return len(Q) == 5 and plane and np.allclose(rad, rad[0]) and all((np.isclose(dq[k], side)).sum() == 2 for k in range(5))


ok("... in three dimensions the icosahedron (12 corners, 20 faces) and the dodecahedron (20 corners, "
   "12 faces) trade too: the icosahedron's 20 face-centres are a dodecahedron's corners, 3 to a corner, "
   "and around each of the icosahedron's 12 corners they make one regular pentagonal face",
   len(tris) == 20 and len(dod) == 20 and e_dod.sum() // 2 == 30 and np.all(e_dod.sum(axis=1) == 3)
   and all(pentagon_round(v) for v in range(12)))


# tower 2: conjugation
def cd_conj(x):
    return np.concatenate([x[:1], -x[1:]])


def cd_mul(a, b):
    if len(a) == 1:
        return a * b
    h = len(a) // 2
    return np.concatenate([cd_mul(a[:h], b[:h]) - cd_mul(cd_conj(b[h:]), a[h:]),
                           cd_mul(b[h:], a[:h]) + cd_mul(a[h:], cd_conj(b[:h]))])


def conj_coin(n, trials=30):
    for _ in range(trials):
        x, y = rng.normal(size=(2, n))
        xx = cd_mul(x, cd_conj(x))
        if not (np.allclose(cd_conj(cd_conj(x)), x) and np.allclose(xx[1:], 0) and np.isclose(xx[0], x @ x)
                and np.allclose((x + cd_conj(x))[1:], 0)
                and np.allclose(cd_conj(cd_mul(x, y)), cd_mul(cd_conj(y), cd_conj(x)))):
            return False
    fixed = np.linalg.svd(np.diag(np.r_[1.0, -np.ones(n - 1)]) - np.eye(n))[1]
    return int(np.sum(fixed < 1e-9)) == 1          # the conjugation keeps a 1-dimensional edge: the reals


ok("numbers: conjugation is a flip on C, H, O and the 16-dimensional sedenions; it keeps exactly the "
   "real numbers; and a number plus, or times, its mirror lands on that edge: x xbar = |x|^2",
   all(conj_coin(n) for n in (2, 4, 8, 16)))
# tower 4: symmetry
tet = Tp
cub, octa = C, np.vstack([np.eye(3), -np.eye(3)])
dode = np.vstack([C, np.array([p for c in range(3) for p in (np.roll([0, s1 / PHI, s2 * PHI], c)
                                                              for s1 in (1, -1) for s2 in (1, -1))])])
swapxy = np.array([[0.0, 1, 0], [1, 0, 0], [0, 0, 1]])
solids = {"tetrahedron": (tet, swapxy), "cube": (cub, -np.eye(3)), "octahedron": (octa, -np.eye(3)),
          "icosahedron": (ico, -np.eye(3)), "dodecahedron": (dode, -np.eye(3))}
ok("symmetry: all five Platonic solids are their own mirror images (a reflection carries each onto "
   "itself) -- they sit on the edge of the mirror coin",
   all(np.isclose(np.linalg.det(M), -1) and keyset(V @ M.T) == keyset(V) for V, M in solids.values()))
sc = np.array([[0, 0, 0], [1, 0, 0], [0, 2, 0], [0, 0, 3]], float)
lengths = sorted(np.round(dist(sc), 9))
ok("... while a lopsided tetrahedron is not: its six edges differ, so a turning would have to keep "
   "every corner in place, yet its mirror image reverses its handedness",
   len(set(lengths)) == 6 and np.linalg.det(sc[1:] - sc[0]) * np.linalg.det((sc @ np.diag([-1.0, 1, 1]))[1:]) < 0)


def R(q):
    turn = lambda v: cd_mul(cd_mul(q, np.r_[0.0, v]), cd_conj(q))[1:]
    return np.column_stack([turn(v) for v in np.eye(3)])


qs = rng.normal(size=(20, 4))
qs /= np.linalg.norm(qs, axis=1, keepdims=True)
full = lambda t: np.r_[np.cos(t / 2), np.sin(t / 2) * np.array([0.0, 0, 1])]
ok("... and turning is a coin with no edge: q and -q give the same rotation, no unit quaternion is its "
   "own negative, and one full turn brings q to -q -- it takes two to come home",
   all(np.allclose(R(q), R(-q)) for q in qs) and np.allclose(full(2 * np.pi), [-1, 0, 0, 0])
   and np.allclose(R(full(2 * np.pi)), np.eye(3)) and np.allclose(full(4 * np.pi), [1, 0, 0, 0]))
# tower 5: the dual lattice
B_fcc = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], float)
B_bcc = np.array([[1, 0, 0], [0, 1, 0], [0.5, 0.5, 0.5]])
U = B_bcc @ np.linalg.inv(np.linalg.inv(B_fcc).T)
ok("lattices: the dual of the face-centred cubic lattice (the densest packing) is the body-centred "
   "cubic lattice (iron's)", np.allclose(U, np.round(U)) and np.isclose(abs(np.linalg.det(U)), 1))
Gh = np.array([[1, 0.5], [0.5, 1]])
flip2 = np.diag([1.0, -1])
A8 = 2 * np.eye(8)
for i, j in [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)]:
    A8[i - 1, j - 1] = A8[j - 1, i - 1] = -1
ok("... and some lattices are their own duals, on the edge: the cubic grid, the hexagonal plane "
   "(turned and scaled), and E8 (determinant 1)",
   np.allclose(np.linalg.inv(np.eye(3)).T, np.eye(3))
   and np.allclose(flip2 @ np.linalg.inv(Gh) @ flip2, Gh * 4 / 3)
   and np.isclose(np.linalg.det(A8), 1) and np.all(np.linalg.eigvalsh(A8) > 0)
   and np.allclose(np.linalg.inv(A8), np.round(np.linalg.inv(A8))))
# tower 6: the node
t = np.linspace(0, np.pi, 2001)
P2 = (3 * np.cos(t) ** 2 - 1) / 2
magic = np.arccos(1 / 3 ** 0.5)
ok("harmonics: P2 is positive near the poles, negative round the middle, and zero exactly on the cones "
   "at the magic angle -- its edge",
   np.all(P2[t < magic - 1e-3] > 0) and np.all(P2[(t > magic + 1e-3) & (t < np.pi - magic - 1e-3)] < 0)
   and np.isclose((3 * np.cos(magic) ** 2 - 1) / 2, 0))
ok("... and turning x to -x flips the odd harmonics and keeps the even: P_l(-x) = (-1)^l P_l(x), l = 0..8",
   all(np.allclose(legendre.legval(-t, np.eye(9)[l]), (-1) ** l * legendre.legval(t, np.eye(9)[l]))
       for l in range(9)))
# tower 8: growing, shrinking, turning
ok("growth: z -> -conj(z) swaps growing (Re z > 0) for shrinking (Re z < 0) and keeps pure turning "
   "(Re z = 0); e carries it onto the circle's coin: e^(-conj z) = 1/conj(e^z)",
   np.allclose(-np.conj(-np.conj(z)), z) and np.allclose(np.exp(-np.conj(z)), 1 / np.conj(np.exp(z)))
   and np.all((abs(np.exp(z)) > 1) == (z.real > 0)) and np.allclose(abs(np.exp(1j * reals)), 1))
ok("... e carries the additive coin (x -> -x, edge 0) to the multiplicative one (x -> 1/x, edge 1), "
   "and a half-turn of pure turning to the flip itself: e^(i pi) = -1",
   np.allclose(np.exp(-reals), 1 / np.exp(reals)) and np.isclose(np.exp(0), 1) and np.isclose(np.exp(1j * np.pi), -1))

print("\n" + "=" * 78)
print("ALL COIN CHECKS PASS -- two sides and an edge, every checkable line checked.")
print("=" * 78)
