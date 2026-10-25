#!/usr/bin/env python3
"""verify_two_faces_of_s4.py -- checks every [FORCED] claim in THE_TWO_FACES_OF_S4.md.

    python verify_two_faces_of_s4.py   # prints PASS/FAIL per check; exit code 1 on any failure

All 48 symmetries of the cube [-1,1]^3 are the signed 3x3 permutation matrices (O_h).
  T_d = the 24 that keep the tetrahedron  {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}
  O   = the 24 rotations (det = +1)
  T   = T_d and O together: the 12 rotations of the tetrahedron

S1  |O_h| = 48, |T_d| = |O| = 24, T_d meets O in T, |T| = 12;
    T_d = 12 rotations + 6 mirrors + 6 rotary reflections (90 degrees)
S2  T_d permutes the tetrahedron's 4 corners, O permutes the cube's 4 long diagonals;
    both maps are isomorphisms onto S4 (24 distinct permutations, products respected)
S3  the twist g -> det(g) g carries T_d onto O, respects products, keeps the S4 labels
    (corner i <-> the diagonal through it), sends mirrors to half-turns about edge axes and
    rotary reflections to quarter-turns, and fixes T pointwise
S4  traces by cycle type (e, (ij), (ijk), (ij)(kl), (ijkl)):
    tetrahedron face (3, 1, 0, -1, -1) = chi[3,1](s) = fix(s) - 1
    cube face        (3,-1, 0, -1,  1) = chi[2,1,1](s) = sgn(s) (fix(s) - 1);
    det = sgn on the tetrahedron face, det = +1 on the cube face
S5  the coin: the faces agree exactly on the 12 even permutations (A4) and are opposite on the
    12 odd ones; restricted to S3 (the permutations fixing one point) the tetrahedron face is
    A1 + E and the cube face is A2 + E
S6  all five irreducible characters of S4 (built here, not typed in) are orthonormal; the
    twist chi -> sgn * chi swaps [4]<->[1,1,1,1] and [3,1]<->[2,1,1] and fixes only [2,2]
S7  chemistry labels: (x, y, z) has the T2 characters of the T_d table (3, 0, -1, -1, 1 on
    E, 8C3, 3C2, 6S4, 6sigma_d) and the T1 characters of the O table (3, 0, -1, 1, -1 on
    E, 8C3, 6C2', 6C4, 3C2) -- one representation, two names

Standard library + numpy. Runtime: about a second.
"""
import itertools
import sys

import numpy as np

FAILS = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   (" + detail + ")") if detail else ""))
    if not ok:
        FAILS.append(name)


# ---- the 48 symmetries of the cube ---------------------------------------------------------
OH = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for r in range(3):
            M[r, perm[r]] = signs[r]
        OH.append(M)
key = lambda M: tuple(M.ravel())
det = lambda M: int(round(np.linalg.det(M)))

CORNERS = [np.array(v) for v in [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]]
cidx = {tuple(v): i for i, v in enumerate(CORNERS)}


def corner_perm(g):
    """permutation of the tetrahedron's corners, or None if g does not keep the tetrahedron"""
    out = []
    for v in CORNERS:
        w = tuple(g @ v)
        if w not in cidx:
            return None
        out.append(cidx[w])
    return tuple(out)


def diagonal_perm(g):
    """permutation of the 4 long diagonals; diagonal i is the line through corner i"""
    out = []
    for v in CORNERS:
        w = g @ v
        i = cidx.get(tuple(w), cidx.get(tuple(-w)))
        out.append(i)
    return tuple(out)


TD = [g for g in OH if corner_perm(g) is not None]
O = [g for g in OH if det(g) == 1]
T = [g for g in TD if det(g) == 1]
order = lambda g: next(n for n in range(1, 9) if np.array_equal(np.linalg.matrix_power(g, n), np.eye(3, dtype=int)))
mirrors = [g for g in TD if det(g) == -1 and order(g) == 2]
rotrefl = [g for g in TD if det(g) == -1 and order(g) == 4]

# S1 ------------------------------------------------------------------------------------------
ok = len(OH) == 48 and len({key(g) for g in OH}) == 48 and len(TD) == 24 and len(O) == 24
ok &= {key(g) for g in TD} & {key(g) for g in O} == {key(g) for g in T} and len(T) == 12
ok &= len(mirrors) == 6 and len(rotrefl) == 6 and all(int(np.trace(g)) == 1 for g in mirrors)
check("S1 |O_h|=48, |T_d|=|O|=24, T_d and O share T, |T|=12; T_d = 12 rotations + 6 mirrors + 6 rotary reflections", ok)


# S2 ------------------------------------------------------------------------------------------
def compose(p, q):            # (p after q)
    return tuple(p[q[i]] for i in range(4))


ok = len({corner_perm(g) for g in TD}) == 24 and len({diagonal_perm(g) for g in O}) == 24
ok &= all(corner_perm(g @ h) == compose(corner_perm(g), corner_perm(h)) for g in TD for h in TD)
ok &= all(diagonal_perm(g @ h) == compose(diagonal_perm(g), diagonal_perm(h)) for g in O for h in O)
check("S2 T_d -> S4 (corners) and O -> S4 (long diagonals) are isomorphisms", ok)

# S3 ------------------------------------------------------------------------------------------
twist = lambda g: det(g) * g
ok = key(-np.eye(3, dtype=int)) not in {key(g) for g in TD}      # the inversion swaps the two tetrahedra
ok &= len({key(twist(g)) for g in TD}) == 24 and {key(twist(g)) for g in TD} == {key(g) for g in O}
ok &= all(np.array_equal(twist(g @ h), twist(g) @ twist(h)) for g in TD for h in TD)
ok &= all(diagonal_perm(twist(g)) == corner_perm(g) for g in TD)
ok &= all(np.array_equal(twist(g), g) for g in T)
half_turns = [twist(g) for g in mirrors]
quarter_turns = [twist(g) for g in rotrefl]
ok &= all(order(h) == 2 and int(np.trace(h)) == -1 for h in half_turns)
# a half-turn's axis = its +1 eigenvector; edge axes look like (1, +-1, 0) (two nonzero entries)
axes = [np.round(np.linalg.eig(h.astype(float))[1][:, np.argmin(abs(np.linalg.eig(h.astype(float))[0] - 1))].real, 6) for h in half_turns]
ok &= all(sum(abs(a) > 1e-9) == 2 for a in axes)
ok &= all(order(q) == 4 and int(np.trace(q)) == 1 for q in quarter_turns)
check("S3 the twist g -> det(g) g: T_d onto O, a homomorphism, S4 labels kept, mirrors -> edge half-turns, "
      "rotary reflections -> quarter-turns, T fixed", ok)


# S4 ------------------------------------------------------------------------------------------
def cycle_type(p):
    seen, lens = set(), []
    for i in range(4):
        if i not in seen:
            n, j = 0, i
            while j not in seen:
                seen.add(j)
                j = p[j]
                n += 1
            lens.append(n)
    return tuple(sorted(lens, reverse=True))


def sgn(p):
    return (-1) ** sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])


fix = lambda p: sum(1 for i in range(4) if p[i] == i)
CLASSES = [(1, 1, 1, 1), (2, 1, 1), (3, 1), (2, 2), (4,)]
tet_face = {corner_perm(g): g for g in TD}          # sigma -> matrix (tetrahedron face)
cube_face = {diagonal_perm(g): g for g in O}        # sigma -> matrix (cube face)
S4 = list(itertools.permutations(range(4)))


def by_class(face):
    out = {}
    for s in S4:
        out.setdefault(cycle_type(s), set()).add(int(np.trace(face[s])))
    return tuple(sorted(out[c])[0] if len(out[c]) == 1 else None for c in CLASSES)


tet_chars, cube_chars = by_class(tet_face), by_class(cube_face)
ok = tet_chars == (3, 1, 0, -1, -1) and cube_chars == (3, -1, 0, -1, 1)
ok &= all(int(np.trace(tet_face[s])) == fix(s) - 1 for s in S4)
ok &= all(int(np.trace(cube_face[s])) == sgn(s) * (fix(s) - 1) for s in S4)
ok &= all(det(tet_face[s]) == sgn(s) for s in S4) and all(det(cube_face[s]) == 1 for s in S4)
check("S4 tetrahedron face = [3,1] (3,1,0,-1,-1), det = sgn; cube face = [2,1,1] (3,-1,0,-1,1), det = +1", ok,
      "tetrahedron %s, cube %s" % (tet_chars, cube_chars))

# S5 ------------------------------------------------------------------------------------------
even = [s for s in S4 if sgn(s) == 1]
odd = [s for s in S4 if sgn(s) == -1]
ok = len(even) == 12 and all(np.array_equal(tet_face[s], cube_face[s]) for s in even)
ok &= all(np.array_equal(tet_face[s], -cube_face[s]) for s in odd)
S3 = [s for s in S4 if s[3] == 3]                    # permutations fixing the 4th point
S3_IRR = {"A1": lambda s: 1, "A2": lambda s: sgn(s), "E": lambda s: fix(s[:3] + (3,)) - 2}


def decompose(face):
    out = {}
    for name, chi in S3_IRR.items():
        m = sum(int(np.trace(face[s])) * chi(s) for s in S3) / 6
        if round(m):
            out[name] = int(round(m))
    return out


d_tet, d_cube = decompose(tet_face), decompose(cube_face)
ok &= d_tet == {"A1": 1, "E": 1} and d_cube == {"A2": 1, "E": 1}
check("S5 the faces agree on A4, are opposite on odd permutations; on S3: tetrahedron A1+E, cube A2+E", ok,
      "tetrahedron %s, cube %s" % (d_tet, d_cube))

# S6 ------------------------------------------------------------------------------------------
# the 2-dimensional irrep [2,2]: S4 acts on the cube's 3 coordinate axes (through O), then the
# standard 2-dim irrep of S3 (character = fixed axes - 1)
axis_perm = lambda g: tuple(int(np.nonzero(g[:, j])[0][0]) for j in range(3))
chi = {
    "[4]": lambda s: 1,
    "[1,1,1,1]": lambda s: sgn(s),
    "[3,1]": lambda s: fix(s) - 1,
    "[2,1,1]": lambda s: sgn(s) * (fix(s) - 1),
    "[2,2]": lambda s: sum(1 for j, a in enumerate(axis_perm(cube_face[s])) if a == j) - 1,
}
names = list(chi)
gram = np.array([[sum(chi[a](s) * chi[b](s) for s in S4) / 24 for b in names] for a in names])
ok = np.allclose(gram, np.eye(5)) and sum(chi[n](tuple(range(4))) ** 2 for n in names) == 24
twisted = {}
for a in names:
    tw = [sgn(s) * chi[a](s) for s in S4]
    twisted[a] = next(b for b in names if [chi[b](s) for s in S4] == tw)
ok &= twisted == {"[4]": "[1,1,1,1]", "[1,1,1,1]": "[4]", "[3,1]": "[2,1,1]", "[2,1,1]": "[3,1]", "[2,2]": "[2,2]"}
check("S6 five orthonormal irreducible characters; the sign twist swaps [4]<->[1^4], [3,1]<->[2,1,1], fixes [2,2]", ok)


# S7 ------------------------------------------------------------------------------------------
def td_class(g):
    d, tr, o = det(g), int(np.trace(g)), order(g)
    if d == 1:
        return {(1, 3): "E", (3, 0): "8C3", (2, -1): "3C2"}[(o, tr)]
    return {(4, -1): "6S4", (2, 1): "6sd"}[(o, tr)]


def o_class(g):
    tr, o = int(np.trace(g)), order(g)
    if o == 2:   # face axis half-turn is diagonal (C4 squared), edge axis half-turn is not
        return "3C2" if np.count_nonzero(g) == 3 and np.array_equal(g, np.diag(np.diag(g))) else "6C2'"
    return {(1, 3): "E", (3, 0): "8C3", (4, 1): "6C4"}[(o, tr)]


TD_T2 = {"E": 3, "8C3": 0, "3C2": -1, "6S4": -1, "6sd": 1}            # T_d table, row T2: (x, y, z)
O_T1 = {"E": 3, "8C3": 0, "6C2'": -1, "6C4": 1, "3C2": -1}             # O table, row T1: (x, y, z)
sizes_td = {c: sum(1 for g in TD if td_class(g) == c) for c in TD_T2}
sizes_o = {c: sum(1 for g in O if o_class(g) == c) for c in O_T1}
ok = sizes_td == {"E": 1, "8C3": 8, "3C2": 3, "6S4": 6, "6sd": 6}
ok &= sizes_o == {"E": 1, "8C3": 8, "6C2'": 6, "6C4": 6, "3C2": 3}
ok &= all(int(np.trace(g)) == TD_T2[td_class(g)] for g in TD)
ok &= all(int(np.trace(g)) == O_T1[o_class(g)] for g in O)
check("S7 (x,y,z) is T2 in the T_d table and T1 in the O table (class sizes 1,8,3,6,6 and 1,8,6,6,3)", ok)

print()
if FAILS:
    print("FAILED: %d check(s): %s" % (len(FAILS), ", ".join(FAILS)))
    sys.exit(1)
print("All checks passed.")
