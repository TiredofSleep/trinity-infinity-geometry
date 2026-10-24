"""
mirror_room.py — how 2D turns and 2D forces use mirrors.
1. Two mirrors make a turn of twice their angle; the mirror pair covers each turn twice (+R and -R).
2. In 3D every plane has exactly one perpendicular line, so plane-things travel as arrows,
   and they give themselves away by flipping the wrong way in a mirror.
3. In 4D the mirror of a plane is a plane (the Hodge star). In ordinary 4D space it splits the
   6 planes into two independent sets of 3. In spacetime it squares to -1 and acts like i.
"""
import itertools
import numpy as np

# 1. two mirrors -> one turn, with a sign left over
X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]])
print("1. Two mirrors, angle phi apart (as 2x2 operators):")
for deg in (0, 90, 180, 360):
    p = np.radians(deg)
    R = (np.cos(p) * X + np.sin(p) * Y) @ X
    turn = (2 * deg) % 720
    print(f"   phi = {deg:3d} deg -> turns the plane by {2*deg:3d} deg; mirror pair = "
          f"{'+1' if np.allclose(R, np.eye(2)) else '-1' if np.allclose(R, -np.eye(2)) else 'a rotor'}")
print("   So a full 360-degree turn comes out as -1, and 720 degrees is needed to get +1: the mirror"
      " description has twice the room of the turn it builds.")

# 2. axial vectors: angular momentum L = r x p under the mirror x -> -x
M = np.diag([-1, 1, 1])
r, p = np.array([0, 1.0, 0]), np.array([0, 0, 1.0])
L = np.cross(r, p); L_mirror = np.cross(M @ r, M @ p)
print(f"\n2. L = r x p = {L}; after the mirror x -> -x, L becomes {L_mirror}. A true arrow along x would"
      f" have become {M @ L}. L is a plane (the y-z plane) travelling as its perpendicular line.")
assert np.allclose(L_mirror, L) and not np.allclose(M @ L, L)

# 3. the Hodge star on planes in 4D
def star_matrix(signature):
    idx = list(itertools.combinations(range(4), 2))
    S = np.zeros((6, 6))
    eta = np.diag(signature)
    for a, (i, j) in enumerate(idx):
        k, l = [m for m in range(4) if m not in (i, j)]
        perm = [i, j, k, l]
        sign = np.linalg.det(np.eye(4)[perm])
        S[idx.index((k, l)), a] = sign * eta[i, i] * eta[j, j]   # raise the indices with the metric
    return S, idx
for name, sig in (("4D space (+,+,+,+)", (1, 1, 1, 1)), ("spacetime (-,+,+,+)", (-1, 1, 1, 1))):
    S, idx = star_matrix(sig)
    sq = S @ S
    print(f"\n3. {name}: star applied twice = {'+1' if np.allclose(sq, np.eye(6)) else '-1' if np.allclose(sq, -np.eye(6)) else sq}")
    if np.allclose(sq, np.eye(6)):
        w, v = np.linalg.eigh(S)
        print(f"   eigenvalues {np.round(w).astype(int)}: the 6 planes split into 3 self-dual + 3 anti-self-dual")
        # check the two sets of turns commute with each other
        def gen(c):
            G = np.zeros((4, 4))
            for coef, (i, j) in zip(c, idx):
                G[i, j] -= coef; G[j, i] += coef
            return G
        plus = [gen(v[:, k]) for k in range(6) if w[k] > 0]
        minus = [gen(v[:, k]) for k in range(6) if w[k] < 0]
        ok = all(np.allclose(a @ b, b @ a) for a in plus for b in minus)
        print(f"   every self-dual turn commutes with every anti-self-dual turn: {ok}"
              "  -> two independent rooms of rotation (3 + 3)")
    else:
        print("   the star acts like i: electric and magnetic parts fuse into one complex field E + iB,"
              " and the vacuum Maxwell equations are unchanged by the mirror E -> B, B -> -E")
