#!/usr/bin/env python3
# ============================================================
# verify_J07.py
#
# Verification for:
#   "A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic
#    Structures and the 4-Core Algebraic Center"
#   Sanders, B. R. & Gish, M. (2026). Submitted to
#   Algebraic Combinatorics.
#
# Four checks:
#   1. Partition incompatibility on Z/10Z (Theorem 1, 3-line proof)
#   2. 4-core sub-tables at indices {0,7,8,9} match manuscript display
#   3. D48 -- joint closure: 16+16 in-core, 0+0 spillover
#   4. D78 -- closed-form attractor H/Br = 1+sqrt(3) at alpha=1/2
#            at 50-digit mpmath precision, with polynomial identity
#            (H/Br)^2 - 2(H/Br) - 2 = 0
#
# Tables are inlined (canonical TSML_SYM and BHML from
# Gen13/targets/foundations/lenses.py).  No external imports
# beyond sympy and mpmath.
#
# License: CC-BY-4.0 (for journal compatibility)
# Run: python3 verify_J07.py
# ============================================================

from itertools import combinations


# -- canonical tables (TSML_SYM and BHML on Z/10Z) --
# These match J02/J35/J54's hardcoded tables exactly.
T = [
    [0,0,0,0,0,0,0,7,0,0],
    [0,7,3,7,7,7,7,7,7,7],
    [0,3,7,7,4,7,7,7,7,9],
    [0,7,7,7,7,7,7,7,7,3],
    [0,7,4,7,7,7,7,7,8,7],
    [0,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,8,7,7,7,7,7],
    [0,7,9,3,7,7,7,7,7,7],
]
B = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,2,6,6],
    [2,3,3,4,5,6,7,3,6,6],
    [3,4,4,4,5,6,7,4,6,6],
    [4,5,5,5,5,6,7,5,7,7],
    [5,6,6,6,6,6,7,6,7,7],
    [6,7,7,7,7,7,7,7,7,7],
    [7,2,3,4,5,6,7,8,9,0],
    [8,6,6,6,7,7,7,9,7,8],
    [9,6,6,6,7,7,7,0,8,0],
]

# symmetry sanity
for i in range(10):
    for j in range(10):
        assert T[i][j] == T[j][i], f"T not symmetric at ({i},{j})"
        assert B[i][j] == B[j][i], f"B not symmetric at ({i},{j})"


def hr(label):
    print()
    print("=" * 60)
    print(label)
    print("=" * 60)


# === Check 1: Partition incompatibility (Theorem 1, 3-line proof) ===
def check_partition_incompatibility():
    hr("Check 1: Partition incompatibility on Z/10Z (Theorem 1)")
    n = 10
    pi_2 = {}
    pi_5 = {}
    for x in range(n):
        pi_2.setdefault(x % 2, []).append(x)
        pi_5.setdefault(x % 5, []).append(x)
    blocks_2 = [tuple(sorted(b)) for b in pi_2.values()]
    blocks_5 = [tuple(sorted(b)) for b in pi_5.values()]
    blocks_2.sort()
    blocks_5.sort()

    print(f"  pi_2 ({len(blocks_2)} blocks of size {len(blocks_2[0])}): "
          f"{blocks_2}")
    print(f"  pi_5 ({len(blocks_5)} blocks of size {len(blocks_5[0])}): "
          f"{blocks_5}")

    # No block of pi_5 is contained in any block of pi_2:
    pi5_in_pi2 = any(
        set(b5) <= set(b2) for b5 in blocks_5 for b2 in blocks_2
    )
    # No block of pi_2 is contained in any block of pi_5:
    pi2_in_pi5 = any(
        set(b2) <= set(b5) for b2 in blocks_2 for b5 in blocks_5
    )

    print(f"  any pi_5-block <= a pi_2-block?  {pi5_in_pi2}")
    print(f"  any pi_2-block <= a pi_5-block?  {pi2_in_pi5}")
    incomparable = (not pi5_in_pi2) and (not pi2_in_pi5)
    print(f"  pi_2 and pi_5 INCOMPARABLE in partition lattice: {incomparable}")
    return incomparable


# === Check 2: 4-core sub-tables (manuscript display in A.1) ===
def check_subtables():
    hr("Check 2: 4-core sub-tables at indices {0, 7, 8, 9}")
    core = [0, 7, 8, 9]

    # manuscript A.1 display
    T_expected = [
        [0, 7, 0, 0],
        [7, 7, 7, 7],
        [0, 7, 7, 7],
        [0, 7, 7, 7],
    ]
    B_expected = [
        [0, 7, 8, 9],
        [7, 8, 9, 0],
        [8, 9, 7, 8],
        [9, 0, 8, 0],
    ]

    T_sub = [[T[a][b] for b in core] for a in core]
    B_sub = [[B[a][b] for b in core] for a in core]

    print("  TSML | 0  7  8  9")
    print("  -----+----------")
    for a, row in zip(core, T_sub):
        print(f"    {a}  | " + "  ".join(f"{v}" for v in row))
    print()
    print("  BHML | 0  7  8  9")
    print("  -----+----------")
    for a, row in zip(core, B_sub):
        print(f"    {a}  | " + "  ".join(f"{v}" for v in row))

    ok = (T_sub == T_expected) and (B_sub == B_expected)
    print()
    print(f"  Sub-tables match manuscript display: {ok}")
    return ok


# === Check 3: D48 joint closure on the 4-core ===
def check_d48_joint_closure():
    hr("Check 3: D48 -- joint closure 16+16 in-core, 0+0 spillover")
    core_set = {0, 7, 8, 9}
    core = [0, 7, 8, 9]

    T_in = sum(1 for a in core for b in core if T[a][b] in core_set)
    B_in = sum(1 for a in core for b in core if B[a][b] in core_set)
    T_out = 16 - T_in
    B_out = 16 - B_in

    print(f"  TSML in-core compositions:  {T_in}  (expected 16)")
    print(f"  BHML in-core compositions:  {B_in}  (expected 16)")
    print(f"  TSML spillover:             {T_out} (expected 0)")
    print(f"  BHML spillover:             {B_out} (expected 0)")

    ok = (T_in == 16) and (B_in == 16) and (T_out == 0) and (B_out == 0)
    print()
    print(f"  D48 joint closure verified: {ok}")
    return ok


# === Check 4: D78 closed-form attractor at alpha = 1/2 ===
def check_d78_attractor():
    hr("Check 4: D78 -- attractor H/Br = 1+sqrt(3) at alpha=1/2")
    try:
        import mpmath as mp
    except ImportError:
        print("  mpmath not available; skipping")
        return None

    mp.mp.dps = 50

    # Start at uniform-on-core distribution
    p = [mp.mpf(0)] * 10
    for c in [0, 7, 8, 9]:
        p[c] = mp.mpf(1) / 4
    half = mp.mpf(1) / 2

    def fuse(table, p):
        out = [mp.mpf(0)] * 10
        for i in range(10):
            for j in range(10):
                out[table[i][j]] += p[i] * p[j]
        return out

    iters = 0
    for iters in range(400):
        Tf = fuse(T, p)
        Bf = fuse(B, p)
        out_ = [half * Tf[c] + half * Bf[c] for c in range(10)]
        s = sum(out_)
        new_p = [x / s for x in out_]
        if max(abs(p[c] - new_p[c]) for c in range(10)) < mp.mpf(10) ** -45:
            p = new_p
            break
        p = new_p

    V, H, Br, R = p[0], p[7], p[8], p[9]
    target = 1 + mp.sqrt(3)
    ratio = H / Br
    err = abs(ratio - target)
    # polynomial identity check: r^2 - 2r - 2 = 0
    poly = ratio * ratio - 2 * ratio - 2
    poly_err = abs(poly)

    print(f"  Iterations to convergence:   {iters}")
    print(f"  (V*, H*, Br*, R*) =")
    print(f"     V*  = {mp.nstr(V,  20)}")
    print(f"     H*  = {mp.nstr(H,  20)}")
    print(f"     Br* = {mp.nstr(Br, 20)}")
    print(f"     R*  = {mp.nstr(R,  20)}")
    print(f"  Manuscript p*       (0.13815, 0.54020, 0.19773, 0.12393)")
    print(f"  H/Br        = {mp.nstr(ratio,  35)}")
    print(f"  1 + sqrt(3) = {mp.nstr(target, 35)}")
    print(f"  |H/Br - (1+sqrt(3))|       = {mp.nstr(err,      5)}")
    print(f"  |(H/Br)^2 - 2(H/Br) - 2|   = {mp.nstr(poly_err, 5)}")

    ok = (err < mp.mpf(10) ** -30) and (poly_err < mp.mpf(10) ** -30)
    # Also check the 4-core is mass-preserving
    mass_outside = sum(p[c] for c in range(10) if c not in (0, 7, 8, 9))
    print(f"  mass outside 4-core: {mp.nstr(mass_outside, 5)}")
    ok = ok and (mass_outside < mp.mpf(10) ** -30)
    print()
    print(f"  D78 closed-form attractor verified: {ok}")
    return ok


# === Drive ===
def main():
    results = [
        ("Check 1 (Theorem 1 partition incompatibility)",
         check_partition_incompatibility()),
        ("Check 2 (manuscript A.1 sub-tables)",
         check_subtables()),
        ("Check 3 (D48 joint closure)",
         check_d48_joint_closure()),
        ("Check 4 (D78 closed-form attractor)",
         check_d78_attractor()),
    ]

    hr("SUMMARY")
    n_pass = 0
    n_total = 0
    for label, status in results:
        marker = "PASS" if status else ("SKIP" if status is None else "FAIL")
        print(f"  {marker:4s}  {label}")
        if status is True:
            n_pass += 1
            n_total += 1
        elif status is False:
            n_total += 1
    print()
    print(f"  {n_pass}/{n_total} PASS")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
