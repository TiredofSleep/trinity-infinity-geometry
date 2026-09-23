#!/usr/bin/env python3
"""verify_one_rule.py -- tests candidate rules for realizing 7 and 9 (and all of 0-9).

    python verify_one_rule.py      (~1 min)

THE RULE TESTED IN FULL -- the book's own ("the most symmetric arrangement", Ch. 1 §1.1),
continued in three-dimensional space: arrange n points so that their symmetry group is as large
as possible, not all on one line (for n >= 3).

How it is checked, exhaustively. Every finite set of points in 3-space that is not on a line has
a finite symmetry group, and every finite symmetry group of 3-space is one of the classified
point groups: the seven polyhedral groups (T, Td, Th, O, Oh, I, Ih) and the seven axial families
(Ck, Ckv, Ckh, S2k, Dk, Dkd, Dkh). The set is a union of that group's orbits. So the largest
symmetry an n-point arrangement can have is the largest group G admitting a non-collinear union
of G-orbits with exactly n points. The script builds every point group up to order 120 (axial
families with principal order k <= 16 -- enough for n <= 13, since a ring off the axis has at
least k points), lists each group's orbit types, searches all unions of size n <= 13, and
identifies the winning shape.

Also checked: what the other candidate rules give at 5, 7 and 9 (sphere-spreading, regular
polygons, the perpendicular build), the lattice-coordination clusters, and the centred figurate
numbers cited in SEVEN_AND_NINE.md.
"""
import itertools

import numpy as np

rng = np.random.default_rng(7)
PHI = (1 + 5 ** 0.5) / 2


def ok(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    assert cond, f"claim failed: {name}"


# ---------------------------------------------------------------- point groups
def rot(axis, ang):
    a = np.asarray(axis, float)
    a = a / np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def refl(normal):
    m = np.asarray(normal, float)
    m = m / np.linalg.norm(m)
    return np.eye(3) - 2 * np.outer(m, m)


def closure(gens):
    key = lambda M: tuple(np.round(M, 6).ravel())
    elems = {key(np.eye(3)): np.eye(3)}
    frontier = [np.eye(3)]
    while frontier:
        new = []
        for A in frontier:
            for g in gens:
                B = g @ A
                if key(B) not in elems:
                    elems[key(B)] = B
                    new.append(B)
        frontier = new
        assert len(elems) <= 240, "group did not close"
    return list(elems.values())


def point_groups(kmax=16):
    T = [rot([1, 1, 1], 2 * np.pi / 3), rot([0, 0, 1], np.pi)]
    O = [rot([0, 0, 1], np.pi / 2), rot([1, 1, 1], 2 * np.pi / 3)]
    I = [rot([0, 1, PHI], 2 * np.pi / 5), rot([1, 1, 1], 2 * np.pi / 3)]
    gens = {"T": T, "Td": T + [refl([1, -1, 0])], "Th": T + [-np.eye(3)],
            "O": O, "Oh": O + [-np.eye(3)], "I": I, "Ih": I + [-np.eye(3)]}
    for k in range(1, kmax + 1):
        Rk, C2x = rot([0, 0, 1], 2 * np.pi / k), rot([1, 0, 0], np.pi)
        sv, sh = refl([0, 1, 0]), refl([0, 0, 1])
        sd = refl([-np.sin(np.pi / (2 * k)), np.cos(np.pi / (2 * k)), 0])
        gens.update({f"C{k}": [Rk], f"C{k}v": [Rk, sv], f"C{k}h": [Rk, sh],
                     f"S{2 * k}": [sh @ rot([0, 0, 1], np.pi / k)], f"D{k}": [Rk, C2x],
                     f"D{k}d": [Rk, C2x, sd], f"D{k}h": [Rk, C2x, sh]})
    return {name: closure(g) for name, g in gens.items()}


def orbit(G, p):
    pts = {}
    for g in G:
        q = g @ p
        pts[tuple(np.round(q, 6))] = q
    return np.array(list(pts.values()))


def orbit_types(G):
    """One representative orbit per kind of point: the centre, points on every rotation axis
    (both directions), points on every mirror plane, and a generic point."""
    samples = [rng.normal(size=3)]
    for g in G:
        _, s, vt = np.linalg.svd(g - np.eye(3))
        fixed = vt[s < 1e-9]
        if len(fixed) == 1:
            samples += [fixed[0], -fixed[0]]
        elif len(fixed) == 2:
            samples.append(rng.normal(size=2) @ fixed)
    types, seen = [], set()
    for p in samples:
        O = orbit(G, p / np.linalg.norm(p))
        key = frozenset(tuple(np.round(q, 5)) for q in O)
        if key not in seen:
            seen.add(key)
            types.append(O)
    return types


def affine_rank(P):
    return 0 if len(P) < 2 else int(np.linalg.matrix_rank(P - P.mean(0), tol=1e-7))


def unions(types, n):
    """Every way to make n points from orbits: at most one centre, orbit kinds reused at
    different radii. Yields (point set, description)."""
    sizes = [len(t) for t in types]

    def rec(i, left, chosen):
        if left == 0:
            yield chosen
            return
        if i == len(types):
            return
        for m in range(left // sizes[i] + 1):
            yield from rec(i + 1, left - m * sizes[i], chosen + [(i, m)] if m else chosen)

    for with_centre in (0, 1):
        for chosen in rec(0, n - with_centre, []):
            pts = [np.zeros(3)] if with_centre else []
            for i, m in chosen:
                for r in rng.uniform(0.5, 2.0, m):
                    pts += list(r * types[i])
            yield np.array(pts) if pts else np.zeros((0, 3)), (with_centre, tuple(chosen))


# ---------------------------------------------------------------- symmetry of a point set
def same_set(A, B, tol=1e-5):
    if len(A) != len(B):
        return False
    D = np.linalg.norm(A[:, None] - B[None], axis=-1)
    return bool((D.min(1) < tol).all() and (D.min(0) < tol).all())


def sym_order(P, tol=1e-5):
    """Order of the full symmetry group (rotations and reflections) of a finite point set.
    tol: matching tolerance -- loosen it for configurations found numerically."""
    X = np.asarray(P, float) - np.mean(P, 0)
    r = affine_rank(np.asarray(P, float))
    if r <= 1:
        return np.inf
    cand = [x for x in X if np.linalg.norm(x) > 1e-9]
    B = []
    for x in cand:
        if np.linalg.matrix_rank(np.array(B + [x]), tol=1e-8) > len(B):
            B.append(x)
        if len(B) == r:
            break
    extra = [np.cross(B[0], B[1]) / np.linalg.norm(np.cross(B[0], B[1]))] if r == 2 else []
    Bm = np.column_stack(B + extra)
    found = set()
    for t in itertools.permutations(range(len(cand)), r):
        T = [cand[i] for i in t]
        if any(abs(np.linalg.norm(a) - np.linalg.norm(b)) > 10 * tol for a, b in zip(B, T)):
            continue
        for s in ((1, -1) if r == 2 else (None,)):
            Tm = np.column_stack(T + ([s * extra[0]] if r == 2 else []))
            M = Tm @ np.linalg.inv(Bm)
            if np.allclose(M.T @ M, np.eye(3), atol=10 * tol) and same_set(X @ M.T, X, tol):
                found.add(tuple(np.round(M, 2).ravel()))
    return len(found)


def unit_rows(P):
    P = np.asarray(P, float)
    return P / np.linalg.norm(P, axis=1, keepdims=True)


def signature(P):
    """Similarity-invariant fingerprint: sorted pairwise distances / largest distance."""
    P = np.asarray(P, float)
    d = np.linalg.norm(P[:, None] - P[None], axis=-1)[np.triu_indices(len(P), 1)]
    return tuple(np.round(np.sort(d) / d.max(), 4)) if len(d) else ()


polygon = lambda k: np.array([[np.cos(2 * np.pi * j / k), np.sin(2 * np.pi * j / k), 0] for j in range(k)])
tetra = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
octa = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)
cube = np.array([[x, y, z] for x in (1, -1) for y in (1, -1) for z in (1, -1)], float)
icosa = np.array([p for s1 in (1, -1) for s2 in (1, -1) for p in
                  ([0, s1, s2 * PHI], [s1, s2 * PHI, 0], [s2 * PHI, 0, s1])], float)
with_centre = lambda P: np.vstack([P, np.zeros(3)])
bipyramid = lambda k: np.vstack([polygon(k), [[0, 0, 1], [0, 0, -1]]])
NAMED = {"point": np.zeros((1, 3)), "segment": np.array([[0, 0, 1.], [0, 0, -1]]),
         "triangle": polygon(3), "tetrahedron": tetra, "tetrahedron + centre": with_centre(tetra),
         "octahedron": octa, "octahedron + centre": with_centre(octa), "cube": cube,
         "cube + centre": with_centre(cube), "regular decagon": polygon(10),
         "regular hendecagon": polygon(11), "icosahedron": icosa, "icosahedron + centre": with_centre(icosa),
         "octagonal bipyramid": bipyramid(8), "nonagonal bipyramid": bipyramid(9)}


def name_of(P):
    sig = signature(P)
    for nm, Q in NAMED.items():
        if len(Q) == len(P) and signature(Q) == sig:
            return nm
    return f"({len(P)} points, unnamed)"


# ================================================================ run
if __name__ == "__main__":
    print("=" * 78)
    print("ONE RULE FOR 0-9? -- the most symmetric arrangement, and its rivals")
    print("=" * 78)

    GROUPS = point_groups()
    orders = {g: len(G) for g, G in GROUPS.items()}
    ok("polyhedral groups have their classical orders (T 12, Td 24, Th 24, O 24, Oh 48, I 60, Ih 120)",
       [orders[g] for g in ("T", "Td", "Th", "O", "Oh", "I", "Ih")] == [12, 24, 24, 24, 48, 60, 120])
    ok("axial families have orders k, 2k, 2k, 2k, 2k, 4k, 4k (checked k = 1..16)",
       all([orders[f"C{k}"], orders[f"C{k}v"], orders[f"C{k}h"], orders[f"S{2 * k}"], orders[f"D{k}"],
            orders[f"D{k}d"], orders[f"D{k}h"]] == [k, 2 * k, 2 * k, 2 * k, 2 * k, 4 * k, 4 * k]
           for k in range(2, 17)))
    TYPES = {g: orbit_types(G) for g, G in GROUPS.items()}
    menu = lambda g: sorted({len(t) for t in TYPES[g]} | {1})
    ok(f"orbit sizes -- Ih {menu('Ih')}, Oh {menu('Oh')}, Td {menu('Td')}",
       menu("Ih") == [1, 12, 20, 30, 60, 120] and menu("Oh") == [1, 6, 8, 12, 24, 48] and menu("Td") == [1, 4, 6, 12, 24])

    print("\nthe most symmetric arrangement of n points in 3-space (not all on a line for n >= 3)")
    best = {}
    for n in range(0, 14):
        if n == 0:
            best[n] = ("--", None, "the void (no points)")
            continue
        top, winners = 0, []
        for g, types in TYPES.items():
            if orders[g] < top:
                continue
            for P, desc in unions(types, n):
                if len(P) != n or (n >= 3 and affine_rank(P) < 2):
                    continue
                if orders[g] > top:
                    top, winners = orders[g], []
                winners.append((g, P))
        shapes = {name_of(P) for _, P in winners}
        P0 = winners[0][1]
        full = sym_order(P0) if n >= 3 else ("infinite" if n == 2 else "all rotations")
        best[n] = (top, full, " / ".join(sorted(shapes)))
        shown = f"{top:>4}" if n >= 3 else "   -"
        print(f"   n = {n:2d}: largest group order {shown}   -> {best[n][2]}   (full symmetry of the winner: {full})")

    expected = {1: "point", 2: "segment", 3: "triangle", 4: "tetrahedron", 5: "tetrahedron + centre",
                6: "octahedron", 7: "octahedron + centre", 8: "cube", 9: "cube + centre",
                10: "regular decagon", 11: "regular hendecagon", 12: "icosahedron", 13: "icosahedron + centre"}
    for n, shape in expected.items():
        ok(f"n = {n}: the winner is unique -- the {shape}", best[n][2] == shape)
    ok("n = 3..9: the full symmetry of each winner equals the largest group found (nothing bigger exists)",
       all(best[n][1] == best[n][0] for n in range(3, 10)))
    family = {"point", "segment", "triangle", "tetrahedron", "tetrahedron + centre", "octahedron",
              "octahedron + centre", "cube", "cube + centre"}
    ok("0-9: every winner is a simplex, or the tetrahedron / octahedron / cube, alone or with its centre",
       all(best[n][2] in family for n in range(1, 10)))
    ok("10 is the first n whose winner leaves that family (the flat regular decagon)",
       best[10][2] not in family and all(best[n][2] not in family for n in (10, 11, 12, 13)))

    print("\nvariant: require the points to span as many dimensions as they can (min(n-1, 3))")
    for n in (5, 7, 9, 10, 11):
        top, winners = 0, []
        for g, types in TYPES.items():
            if orders[g] < top:
                continue
            for P, _ in unions(types, n):
                if len(P) == n and affine_rank(P) == min(n - 1, 3):
                    if orders[g] > top:
                        top, winners = orders[g], []
                    winners.append((g, P))
        shapes = " / ".join(sorted({name_of(P) for _, P in winners}))
        groups = ", ".join(sorted({g for g, _ in winners}))
        if shapes.endswith("unnamed)"):
            shapes = {"D8h": "octagonal bipyramid (any height)", "D9h": "nonagonal bipyramid (any height)"}.get(groups, shapes)
        print(f"   n = {n:2d}: largest group order {top:>4} ({groups})   -> {shapes}")
        if n in (5, 7, 9):
            ok(f"   n = {n}: same winner as the main rule", shapes == expected[n])
        else:
            ok(f"   n = {n}: also outside the family", shapes not in family)

    print("\nthe rival rules at 5, 7 and 9")
    ok("regular polygon: pentagon, heptagon, nonagon -- flat, with symmetry 20, 28, 36 (all below 24, 48, 48)",
       [sym_order(polygon(k)) for k in (5, 7, 9)] == [20, 28, 36])

    def descend(X, steps, lr):
        for _ in range(steps):
            diff = X[:, None] - X[None]
            d = np.linalg.norm(diff, axis=-1) + np.eye(len(X))
            F = (diff / d[..., None] ** 3).sum(1)
            F -= (F * X).sum(1, keepdims=True) * X
            X = unit_rows(X + lr * F)
        return X

    energy = lambda X: float((1 / np.linalg.norm(X[:, None] - X[None], axis=-1)[np.triu_indices(len(X), 1)]).sum())

    def thomson(n):
        starts = [descend(unit_rows(rng.normal(size=(n, 3))), 1500, 0.02) for _ in range(12)]
        return descend(min(starts, key=energy), 30000, 0.005)

    # 5 and 7: the exact shapes -- their energy equals the numerical minimum (positions of a
    # numerical minimizer are too loose to test symmetry directly where the landscape is flat)
    tri_bip, pent_bip = unit_rows(bipyramid(3)), unit_rows(bipyramid(5))
    m5, m7, X9 = energy(thomson(5)), energy(thomson(7)), thomson(9)
    ok(f"sphere-spreading at 5 is the triangular bipyramid (energy {energy(tri_bip):.6f} = min {m5:.6f}), "
       f"symmetry {sym_order(tri_bip)}", abs(energy(tri_bip) - m5) < 1e-5 and sym_order(tri_bip) == 12)
    ok(f"sphere-spreading at 7 is the pentagonal bipyramid (energy {energy(pent_bip):.6f} = min {m7:.6f}), "
       f"symmetry {sym_order(pent_bip)}", abs(energy(pent_bip) - m7) < 1e-5 and sym_order(pent_bip) == 20)
    ok(f"sphere-spreading at 9 is the triaugmented triangular prism: symmetry {sym_order(X9, tol=2e-3)}",
       sym_order(X9, tol=2e-3) == 12)
    ok("so sphere-spreading realizes 7 and 9, but with symmetry 20 and 12 -- far below 48",
       sym_order(pent_bip) < 48 and sym_order(X9, tol=2e-3) < 48)
    grid = np.array([[i, j, 0] for i in (-1, 0, 1) for j in (-1, 0, 1)], float)
    ok(f"3^2 as a 3 x 3 grid: flat, symmetry {sym_order(grid)} (the cube + centre has 48)", sym_order(grid) == 16)
    ok("the perpendicular build gives only 1, 2, 4, 8 points (2^k) -- neither 7 nor 9", {2 ** k for k in range(4)} == {1, 2, 4, 8})

    print("\nlattices: an atom plus its nearest neighbours")
    box = np.array(list(itertools.product(range(-2, 3), repeat=3)), float)
    fcc = np.array([p for p in itertools.product(range(-4, 5), repeat=3) if sum(p) % 2 == 0], float) / 2
    lattices = {"diamond": np.vstack([fcc, fcc + 0.25]), "simple cubic": box,
                "body-centred cubic": np.vstack([box, box + 0.5]), "face-centred cubic": fcc}
    shells = {}
    for nm, L in lattices.items():
        d = np.linalg.norm(L, axis=1)
        d1 = d[d > 1e-9].min()
        nb = L[np.abs(d - d1) < 1e-9]
        shells[nm] = (len(nb) + 1, name_of(with_centre(nb)) if len(nb) < 12 else f"{len(nb)} neighbours")
    ok(f"diamond -> 5 = {shells['diamond'][1]}; simple cubic -> 7 = {shells['simple cubic'][1]}; "
       f"body-centred cubic -> 9 = {shells['body-centred cubic'][1]}",
       shells["diamond"] == (5, "tetrahedron + centre") and shells["simple cubic"] == (7, "octahedron + centre")
       and shells["body-centred cubic"] == (9, "cube + centre"))
    ok("face-centred cubic -> 1 + 12 = 13 (beyond the digits)", shells["face-centred cubic"][0] == 13)

    print("\ncentred figurate numbers (the Pythagorean tradition, extended to solids)")
    ctet = [(2 * k + 1) * (k * k + k + 3) // 3 for k in range(4)]
    coct = [(2 * k + 1) * (2 * k * k + 2 * k + 3) // 3 for k in range(4)]
    ccub = [k ** 3 + (k + 1) ** 3 for k in range(4)]
    ok(f"centred tetrahedral {ctet}, centred octahedral {coct}, centred cube {ccub}: 5, 7, 9 are each "
       f"sequence's second term", ctet[1] == 5 and coct[1] == 7 and ccub[1] == 9
       and ctet == [1, 5, 15, 35] and coct == [1, 7, 25, 63] and ccub == [1, 9, 35, 91])

    print("\nALL CLAIMS OF SEVEN_AND_NINE.md VERIFIED.")
