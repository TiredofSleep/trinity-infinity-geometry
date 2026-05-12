#!/usr/bin/env python3
# ============================================================
# verify_J54_chain_and_attractor.py
#
# Verification script for J54 -- "Forcing Axioms and the Family
# of Commutative Non-Associative Magmas on Z/10Z Preserving a
# Designated 4-Core" (Sanders, Gish, 2026)
#
# Three checks (mapped to manuscript sections):
#   1. Q6: 3-table joint closure chain (Theorem 7.1)
#       (TSML, BHML, CL_STD all-three jointly closed sub-magmas
#        form the same 8-shell chain {1,4,5,6,7,8,9,10} as
#        TSML+BHML alone; independent re-run of foundation_verification.py
#        Check 2)
#   2. 4-core attractor h/br = 1+sqrt(3) at alpha_M = 1/2 (Theorem 5.1)
#       (iteration on TSML, BHML at alpha=1/2 with 50-digit mpmath;
#        residual <= 10^-30 in 99 iterations from uniform-on-4-core init)
#   3. A1-A9 forcing -- shared axioms
#       (cell-by-cell verification that CL_TSML, CL_BHML, CL_STD
#        all satisfy the substrate-defining axioms A1, A2 (puncture),
#        A4, commutativity; A9 BUMP-disagreement-count signatures)
#
# Runtime: ~5 seconds. Run: python3 verify_J54_chain_and_attractor.py
#
# License: CC-BY-4.0 (Creative Commons Attribution 4.0 International).
# Authors: B.R. Sanders, M. Gish (c) 2026.
# ============================================================

from __future__ import annotations

from itertools import combinations
from collections import Counter
from math import gcd as _gcd

# ============================================================
# The three canonical tables (verbatim from the J-series corpus)
#   T = CL_TSML   (73 HARMONY)
#   B = CL_BHML   (28 HARMONY)
#   S = CL_STD    (44 HARMONY)
# ============================================================
T = [
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 7, 3, 7, 7, 7, 7, 7, 7, 7],
    [0, 3, 7, 7, 4, 7, 7, 7, 7, 9],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 3],
    [0, 7, 4, 7, 7, 7, 7, 7, 8, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 8, 7, 7, 7, 7, 7],
    [0, 7, 9, 3, 7, 7, 7, 7, 7, 7],
]
B = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 2, 6, 6],
    [2, 3, 3, 4, 5, 6, 7, 3, 6, 6],
    [3, 4, 4, 4, 5, 6, 7, 4, 6, 6],
    [4, 5, 5, 5, 5, 6, 7, 5, 7, 7],
    [5, 6, 6, 6, 6, 6, 7, 6, 7, 7],
    [6, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [8, 6, 6, 6, 7, 7, 7, 9, 7, 8],
    [9, 6, 6, 6, 7, 7, 7, 0, 8, 0],
]
S = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 7, 8, 1],
    [2, 3, 4, 5, 6, 7, 7, 8, 7, 2],
    [3, 4, 5, 6, 7, 7, 7, 7, 7, 3],
    [4, 5, 6, 7, 7, 7, 7, 8, 7, 4],
    [5, 6, 7, 7, 7, 8, 7, 7, 7, 5],
    [6, 7, 7, 7, 7, 7, 8, 7, 7, 6],
    [7, 7, 8, 7, 8, 7, 7, 8, 7, 7],
    [8, 8, 7, 7, 7, 7, 7, 7, 7, 8],
    [9, 1, 2, 3, 4, 5, 6, 7, 8, 0],
]


# ============================================================
# Utility helpers
# ============================================================
def is_closed(subset, table):
    Sset = set(subset)
    return all(table[i][j] in Sset for i in subset for j in subset)


def hr(label):
    print()
    print("=" * 72)
    print(label)
    print("=" * 72)


# ============================================================
# CHECK 1: Q6 -- 3-table joint closure chain
# ============================================================
def check_3table_chain():
    hr("CHECK 1: Q6 -- 3-table joint closure chain (TSML + BHML + CL_STD)")

    jc_T = []
    jc_B = []
    jc_S = []
    jc_TB = []
    jc_TBS = []

    for size in range(1, 11):
        for sub in combinations(range(10), size):
            cl_T = is_closed(sub, T)
            cl_B = is_closed(sub, B)
            cl_S = is_closed(sub, S)
            if cl_T:
                jc_T.append(sub)
            if cl_B:
                jc_B.append(sub)
            if cl_S:
                jc_S.append(sub)
            if cl_T and cl_B:
                jc_TB.append(sub)
            if cl_T and cl_B and cl_S:
                jc_TBS.append(sub)

    expected = [
        (0,),
        (0, 7, 8, 9),
        (0, 6, 7, 8, 9),
        (0, 5, 6, 7, 8, 9),
        (0, 4, 5, 6, 7, 8, 9),
        (0, 3, 4, 5, 6, 7, 8, 9),
        (0, 2, 3, 4, 5, 6, 7, 8, 9),
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    ]

    print()
    print("  Standalone closure counts (per SFM_FINDINGS_v1.md):")
    print(f"    TSML   alone: {len(jc_T)}     (expected 449)")
    print(f"    BHML   alone: {len(jc_B)}     (expected 9)")
    print(f"    CL_STD alone: {len(jc_S)}     (expected 50)")

    print()
    print("  Joint closure counts:")
    print(f"    TSML and BHML        : {len(jc_TB)}      (expected 8)")
    print(f"    TSML, BHML, CL_STD   : {len(jc_TBS)}      (expected 8)")

    sizes_TB = sorted(len(s) for s in jc_TB)
    sizes_TBS = sorted(len(s) for s in jc_TBS)
    print()
    print(f"  Size distribution TSML+BHML  : {sizes_TB}")
    print(f"  Size distribution all-three  : {sizes_TBS}")
    print("  Expected (both rows)         : [1, 4, 5, 6, 7, 8, 9, 10]")

    # forbid sizes 2 and 3
    forbid_ok = (2 not in sizes_TBS) and (3 not in sizes_TBS)

    # match the canonical chain
    matches_TB = [tuple(sorted(s)) for s in jc_TB] == expected
    matches_TBS = [tuple(sorted(s)) for s in jc_TBS] == expected
    same_chain = (jc_TB == jc_TBS) and matches_TB and matches_TBS

    print()
    print(f"  TSML+BHML chain matches J02 Theorem 1     : {matches_TB}")
    print(f"  All-three chain matches TSML+BHML chain   : {same_chain}")
    print(f"  Sizes 2 and 3 both forbidden              : {forbid_ok}")

    print()
    print("  Three-table joint closure chain:")
    for sub in jc_TBS:
        print(f"    |S|={len(sub):2d} : {sub}")

    print()
    # 4-core 3-substrate closure (Theorem B)
    C = (0, 7, 8, 9)
    T_4core = {T[i][j] for i in C for j in C}
    B_4core = {B[i][j] for i in C for j in C}
    S_4core = {S[i][j] for i in C for j in C}
    print("  4-core 3-substrate closure (corollary of chain):")
    print(f"    image(4-core, T) subset of 4-core : {T_4core <= set(C)}    image = {sorted(T_4core)}")
    print(f"    image(4-core, B) subset of 4-core : {B_4core <= set(C)}    image = {sorted(B_4core)}")
    print(f"    image(4-core, S) subset of 4-core : {S_4core <= set(C)}    image = {sorted(S_4core)}")
    fourcore_3sub = (T_4core <= set(C)) and (B_4core <= set(C)) and (S_4core <= set(C))

    return matches_TB and same_chain and forbid_ok and fourcore_3sub


# ============================================================
# CHECK 2: 4-core attractor h/br = 1 + sqrt(3) at alpha_M = 1/2
# ============================================================
def check_attractor():
    hr("CHECK 2: 4-core attractor h/br = 1 + sqrt(3) at alpha_M = 1/2")

    try:
        import mpmath as mp
    except ImportError:
        print("  mpmath not available; skipping")
        return None

    mp.mp.dps = 50

    # initial uniform distribution on the 4-core {0, 7, 8, 9}
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

    n_iters = 0
    for n_iters in range(300):
        Tf = fuse(T, p)
        Bf = fuse(B, p)
        out = [half * Tf[c] + half * Bf[c] for c in range(10)]
        s = sum(out)
        new_p = [x / s for x in out]
        if max(abs(p[c] - new_p[c]) for c in range(10)) < mp.mpf(10) ** -45:
            p = new_p
            break
        p = new_p

    target = 1 + mp.sqrt(3)
    ratio = p[7] / p[8]
    err = abs(ratio - target)

    print()
    print(f"  Iterations to convergence : {n_iters}")
    print()
    print("  Equilibrium probabilities (V*, H*, Br*, R*):")
    print(f"    V*  = {mp.nstr(p[0], 20)}")
    print(f"    H*  = {mp.nstr(p[7], 20)}")
    print(f"    Br* = {mp.nstr(p[8], 20)}")
    print(f"    R*  = {mp.nstr(p[9], 20)}")

    # mass outside the 4-core should be zero
    mass_outside = sum(p[c] for c in range(10) if c not in {0, 7, 8, 9})
    print(f"    mass outside 4-core      = {mp.nstr(mass_outside, 5)}")

    print()
    print(f"  H*/Br*       = {mp.nstr(ratio, 35)}")
    print(f"  1 + sqrt(3)  = {mp.nstr(target, 35)}")
    print(f"  | residual | = {mp.nstr(err, 5)}")

    ok_ratio = err < mp.mpf(10) ** -30
    ok_mass = mass_outside < mp.mpf(10) ** -20

    print()
    print(f"  Closed-form attractor verified            : {ok_ratio}")
    print(f"  Mass-outside-4-core vanishes              : {ok_mass}")

    return ok_ratio and ok_mass


# ============================================================
# CHECK 3: A1-A9 forcing -- cell-by-cell verification
#
# We verify the substrate-level shared structure (A1, A2, A4, A7,
# A5, A6) on all three tables T, B, S, and then summarise their
# distinguishing A9-BUMP signatures (the entries that distinguish
# CL_TSML, CL_BHML, CL_STD pairwise).
# ============================================================
def check_A1_A9_forcing():
    hr("CHECK 3: A1-A9 forcing -- shared axioms hold on T, B, S")

    def axiom_A1(M):
        # 10x10 with entries in Z/10Z
        if len(M) != 10:
            return False
        for i in range(10):
            if len(M[i]) != 10:
                return False
            for j in range(10):
                v = M[i][j]
                if not (0 <= v <= 9):
                    return False
        return True

    def axiom_A2(M):
        # T[0, j] = 0 for all j != 7; T[0, 7] = 7 (VOID-HARMONY puncture).
        # CL_TSML satisfies A2 strictly. For CL_BHML and CL_STD the
        # row-0 axiom is weakened: only the (0, 7) puncture is preserved
        # (BHML / STD use row-0 = identity-row instead). We report both.
        strict = (M[0][7] == 7) and all(M[0][j] == 0 for j in range(10) if j != 7)
        puncture_preserved = (M[0][7] == 7)
        return strict, puncture_preserved

    def axiom_A4(M):
        # Pati-Salam puncture: (0, 7) and (7, 0) cells together break
        # the absorbing/idempotent symmetry. Required: M[0][7] = M[7][0] = 7.
        return (M[0][7] == 7) and (M[7][0] == 7)

    def axiom_A7(M):
        # Diagonal HARMONY: M[i][i] = 7 for i not in {0}.
        # CL_TSML satisfies A7 on i in {1..8}. CL_BHML and CL_STD have
        # weaker diagonals; we still record the count.
        return [M[i][i] for i in range(10)]

    def axiom_A5(M):
        # Column VOID: M[i, 0] = 0 for all i except i = 7 (T-strict).
        # Reported by counting how many column-0 entries match A5.
        return sum(1 for i in range(10) if M[i][0] == 0) + (1 if M[7][0] == 7 else 0)

    def axiom_A6(M):
        # Column HARMONY: M[i, 7] obeys the A3-symmetric pattern.
        # Reported by counting how many column-7 entries equal 7.
        return sum(1 for i in range(10) if M[i][7] == 7)

    def commutative(M):
        for i in range(10):
            for j in range(10):
                if M[i][j] != M[j][i]:
                    return False
        return True

    def harmony_count(M):
        return sum(1 for i in range(10) for j in range(10) if M[i][j] == 7)

    def row0_pattern(M):
        return tuple(M[0][j] for j in range(10))

    def row7_pattern(M):
        return tuple(M[7][j] for j in range(10))

    print()
    for name, M in [("CL_TSML", T), ("CL_BHML", B), ("CL_STD", S)]:
        a1 = axiom_A1(M)
        a2_strict, a2_punct = axiom_A2(M)
        a4 = axiom_A4(M)
        diag = axiom_A7(M)
        a7_strict = all(diag[i] == 7 for i in range(1, 10))
        a7_main = sum(1 for i in range(1, 10) if diag[i] == 7)
        a5 = axiom_A5(M)
        a6 = axiom_A6(M)
        comm = commutative(M)
        h = harmony_count(M)

        print(f"  {name:8s} :")
        print(f"    A1  10x10 over Z/10Z              : {a1}")
        print(f"    A2  row-0 (VOID absorbing-strict) : {a2_strict}")
        print(f"    A2' VOID-HARMONY (0,7) puncture   : {a2_punct}")
        print(f"    A4  Pati-Salam (0,7)+(7,0) = 7    : {a4}")
        print(f"    A5  col-0 weak match              : {a5}")
        print(f"    A6  col-7 HARMONY count           : {a6}")
        print(f"    A7  diag = HARMONY on {{1..9}}      : {a7_strict}  ({a7_main}/9)")
        print(f"    --  commutative                   : {comm}")
        print(f"    --  HARMONY count                 : {h}")
        print(f"    --  row 0                         : {row0_pattern(M)}")
        print(f"    --  row 7                         : {row7_pattern(M)}")
        print()

    # Shared substrate-level axioms: A1, A4, commutativity, the (0,7)
    # puncture (A2'). Report PASS if all three tables share them.
    shared = (
        all(axiom_A1(M) for M in (T, B, S))
        and all(axiom_A4(M) for M in (T, B, S))
        and all(commutative(M) for M in (T, B, S))
        and all(axiom_A2(M)[1] for M in (T, B, S))
    )
    print(f"  Shared substrate-level axioms (A1, A2', A4, commutativity)")
    print(f"  hold on all three tables                  : {shared}")

    # A9 BUMP signatures: which cells distinguish the three tables
    # pairwise. Report counts.
    def diff_cells(M1, M2):
        return [(i, j) for i in range(10) for j in range(10)
                if M1[i][j] != M2[i][j]]

    d_TB = diff_cells(T, B)
    d_TS = diff_cells(T, S)
    d_BS = diff_cells(B, S)
    print()
    print("  A9 BUMP signatures (cells where tables disagree):")
    print(f"    TSML vs BHML   : {len(d_TB):3d} cells")
    print(f"    TSML vs CL_STD : {len(d_TS):3d} cells")
    print(f"    BHML vs CL_STD : {len(d_BS):3d} cells")

    return shared


# ============================================================
# Driver
# ============================================================
def main():
    print()
    print("# J54 verification -- Sanders & Gish 2026")
    print("# Forcing Axioms and the Family of Commutative Non-Associative")
    print("# Magmas on Z/10Z Preserving a Designated 4-Core")
    print("#")
    print("# Verifying:")
    print("#   1. Q6 -- 3-table joint closure chain")
    print("#   2. 4-core attractor h/br = 1 + sqrt(3) at alpha_M = 1/2")
    print("#   3. A1-A9 forcing -- shared substrate-level axioms")
    print()

    results = {}
    results["q6_chain"] = check_3table_chain()
    results["attractor"] = check_attractor()
    results["a1_a9"] = check_A1_A9_forcing()

    hr("Summary")
    for k, v in results.items():
        sym = "OK" if v is True else ("SKIPPED" if v is None else "FAIL")
        print(f"  {k:15s}: {sym}")

    all_ok = all(v is True or v is None for v in results.values())
    print()
    print(f"  Overall: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
