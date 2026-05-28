"""verify_J60.py -- machine-precision verification of J60's six checks
via ETP scripts.

CC-BY-4.0. (c) 2026 Brayden Ross Sanders / 7Site LLC. M. Gish co-author.

Requires: clone of github.com/teorth/equational_theories accessible at
the ETP_PATH defined below. Reads its 4694-equation catalog and uses
its test_equation function.

Verifies:
  C1 (Theorem 1): Z/n has profile 32 for n in {5, 6, 7, 8, 9, 10}, with
             identical equation IDs across orders.
  C2 (Theorem 2): -(x+y) mod n has profile 294 for n = 4 and 10.
  C3 (Theorem 3): 8 commutative magmas' profile intersection = 14 specific IDs.
  C4 (Theorem 4): (5x + 3y + 6) mod 7 has profile 14 with different IDs from
             the sigma-magma's (verifies Family R distinct from Family C).
  C5 (Section 4.7, order 3): exhaustive enumeration of all 729 = 3^6
             commutative order-3 magmas (symmetric 3x3 tables). Asserts:
             120 have profile 14; all 120 share the IDENTICAL Family C
             equation set; 0 have profile < 14.
  C6 (Section 4.7, order 5): exhaustive enumeration of all 720 symmetric
             5x5 Latin squares (commutative quasigroups of order 5).
             Asserts: 480 have profile 14; all 480 share the IDENTICAL
             Family C equation set; profile distribution matches
             {14:480, 15:120, 32:30, 89:24, 90:30, 176:6, 294:30}.

Runtime ~5-6 minutes total (C5 ~2.5 min, C6 ~2.5 min, others <1 min).
"""
import sys, os, time
from itertools import product

ETP_PATH = "C:\\Users\\brayd\\OneDrive\\Desktop\\etp"  # adjust as needed
sys.path.insert(0, os.path.join(ETP_PATH, "scripts"))
from explore_magma import (read_equations_map, test_equation,
                           get_binary_operation_map)


def profile_set(table):
    """Return the set of equation IDs satisfied by the magma table."""
    bop = get_binary_operation_map(table)
    sat = set()
    for eq_id, eq_str in EQ_MAP.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            sat.add(eq_id)
    return sat


def linear(a, b, c, n):
    return [[(a*x + b*y + c) % n for y in range(n)] for x in range(n)]


def main():
    t0 = time.time()
    print("J60 verification (ETP-based)")
    print()
    global EQ_MAP
    EQ_MAP = read_equations_map()
    print(f"Loaded {len(EQ_MAP)} equations in {time.time()-t0:.2f}s")
    print()

    checks = []

    # Theorem 1: Z/n profile = 32 for n in {5..10}, IDs identical
    print("Theorem 1: Z/n profile = 32 for n in {5..10}, IDs identical")
    profiles_zn = {}
    for n in range(5, 11):
        table = linear(1, 1, 0, n)
        profiles_zn[n] = profile_set(table)
        print(f"  Z/{n}: {len(profiles_zn[n])} equations")
    same_size = all(len(s) == 32 for s in profiles_zn.values())
    same_ids = (len(set(map(tuple, (sorted(s) for s in profiles_zn.values())))) == 1)
    t1_ok = same_size and same_ids
    print(f"  All profile size = 32: {same_size}")
    print(f"  All IDs identical across orders: {same_ids}")
    checks.append(("Theorem 1 (Z/n profile = 32, n in 5..10, IDs universal)", t1_ok))
    print()

    # Theorem 2: -(x+y) mod n = 294 for n = 4, 10
    print("Theorem 2: -(x+y) mod n profile = 294 for n = 4, 10")
    t2_ok = True
    for n in [4, 10]:
        table = linear(n-1, n-1, 0, n)
        p = profile_set(table)
        print(f"  -(x+y) mod {n}: {len(p)} equations")
        if len(p) != 294:
            t2_ok = False
    checks.append(("Theorem 2 (-(x+y) mod n = 294 for n = 4, 10)", t2_ok))
    print()

    # Theorem 3: 8 commutative magmas have intersection = 14 specific IDs
    print("Theorem 3: 8 commutative magmas, intersection = 14 IDs")
    SIGMA_10 = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
    sigma_magma = [[SIGMA_10[(x + y) % 10] for y in range(10)] for x in range(10)]
    BHML = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,2,6,6],[2,3,3,4,5,6,7,3,6,6],
            [3,4,4,4,5,6,7,4,6,6],[4,5,5,5,5,6,7,5,7,7],[5,6,6,6,6,6,7,6,7,7],
            [6,7,7,7,7,7,7,7,7,7],[7,2,3,4,5,6,7,8,9,0],[8,6,6,6,7,7,7,9,7,8],
            [9,6,6,6,7,7,7,0,8,0]]
    CL_STD = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,7,8,1],[2,3,4,5,6,7,7,8,7,2],
              [3,4,5,6,7,7,7,7,7,3],[4,5,6,7,7,7,7,8,7,4],[5,6,7,7,7,8,7,7,7,5],
              [6,7,7,7,7,7,8,7,7,6],[7,7,8,7,8,7,7,8,7,7],[8,8,7,7,7,7,7,7,7,8],
              [9,1,2,3,4,5,6,7,8,0]]
    sigma_10_min = [[((0 if k == 0 else (k + 1 if k < 9 else 1))*0 + 0)
                    for k in range(10)] for _ in range(10)]  # placeholder
    # rebuild sigma_10_min correctly
    sm = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    sigma_10_min = [[sm[(x+y) % 10] for y in range(10)] for x in range(10)]
    z3 = linear(1, 1, 0, 3)
    z5 = linear(1, 1, 0, 5)
    T4 = [[1, 0, 2], [0, 2, 1], [2, 1, 0]]
    TSML = [[0,0,0,0,0,0,0,7,0,0],[0,7,3,7,7,7,7,7,7,7],[0,3,7,7,4,7,7,7,7,9],
            [0,7,7,7,7,7,7,7,7,3],[0,7,4,7,7,7,7,7,8,7],[0,7,7,7,7,7,7,7,7,7],
            [0,7,7,7,7,7,7,7,7,7],[7,7,7,7,7,7,7,7,7,7],[0,7,7,7,8,7,7,7,7,7],
            [0,7,9,3,7,7,7,7,7,7]]

    profiles = [profile_set(m) for m in [sigma_magma, BHML, CL_STD,
                                          sigma_10_min, z3, z5, T4, TSML]]
    labels = ["sigma-magma", "BHML", "CL_STD", "sigma_10^min",
              "Z/3", "Z/5", "T_4", "TSML"]
    for lbl, p in zip(labels, profiles):
        print(f"  {lbl}: {len(p)} equations")
    intersection = profiles[0]
    for p in profiles[1:]:
        intersection = intersection & p
    expected_14 = {1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442,
                   4482, 4531, 4544, 4635, 4677}
    t3_ok = (intersection == expected_14)
    print(f"  Intersection size: {len(intersection)}")
    print(f"  Equals expected 14 IDs: {t3_ok}")
    checks.append(("Theorem 3 (intersection of 8 comm magmas = 14 IDs)", t3_ok))
    print()

    # Theorem 4: (5x+3y+6) mod 7 has profile 14, different IDs from sigma-magma
    print("Theorem 4: (5x+3y+6) mod 7 profile 14, different IDs from sigma-magma")
    family_R_magma = linear(5, 3, 6, 7)
    family_R_profile = profile_set(family_R_magma)
    sigma_profile = profiles[0]  # sigma-magma's profile
    t4_ok = (len(family_R_profile) == 14
              and family_R_profile != sigma_profile
              and family_R_profile & sigma_profile == {1})  # share only reflexivity
    print(f"  (5x+3y+6) mod 7 profile: {len(family_R_profile)}")
    print(f"  Different from sigma-magma: {family_R_profile != sigma_profile}")
    print(f"  Intersection with sigma-magma: {family_R_profile & sigma_profile}")
    checks.append(("Theorem 4 (profile 14 has multiple families)", t4_ok))
    print()

    # Family C's canonical 14-equation set (used by C5 + C6)
    FAMILY_C = {1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442,
                4482, 4531, 4544, 4635, 4677}

    # C5 (Section 4.7, order 3): exhaustive enumeration of all 729 = 3^6
    # commutative order-3 magmas (symmetric 3x3 tables). Manuscript claims:
    #   - 120 have profile 14, ALL sharing Family C
    #   - 0 have profile < 14
    #   - 609 have profile > 14
    print("C5 (Section 4.7, order 3): all 729 commutative magmas")
    print("  Enumerating 3^6 = 729 symmetric 3x3 tables...")
    n3 = 3
    ut_cells = [(i, j) for i in range(n3) for j in range(i, n3)]
    assert len(ut_cells) == 6 and n3**len(ut_cells) == 729

    profile_dist_n3 = {}
    profile14_sets_n3 = []
    total_n3 = 0
    t_start_c5 = time.time()
    for vals in product(range(n3), repeat=len(ut_cells)):
        table = [[0]*n3 for _ in range(n3)]
        for (i, j), v in zip(ut_cells, vals):
            table[i][j] = v
            table[j][i] = v
        prof = profile_set(table)
        sz = len(prof)
        profile_dist_n3[sz] = profile_dist_n3.get(sz, 0) + 1
        if sz == 14:
            profile14_sets_n3.append(frozenset(prof))
        total_n3 += 1
        if total_n3 % 100 == 0:
            print(f"    {total_n3}/729 ({time.time()-t_start_c5:.1f}s)")
    print(f"  Total enumerated: {total_n3} (expected 729)")
    print(f"  Distinct profile sizes observed: {len(profile_dist_n3)}")
    smallest_n3 = min(profile_dist_n3)
    n_at_14_n3 = profile_dist_n3.get(14, 0)
    n_below_14_n3 = sum(c for s, c in profile_dist_n3.items() if s < 14)
    n_above_14_n3 = sum(c for s, c in profile_dist_n3.items() if s > 14)
    print(f"  Smallest profile size: {smallest_n3} (manuscript: 14)")
    print(f"  Count at profile 14: {n_at_14_n3} (manuscript: 120)")
    print(f"  Count below profile 14: {n_below_14_n3} (manuscript: 0)")
    print(f"  Count above profile 14: {n_above_14_n3} (manuscript: 609)")
    distinct_14_n3 = set(profile14_sets_n3)
    print(f"  Distinct equation sets among profile-14 magmas: "
          f"{len(distinct_14_n3)} (manuscript: 1, = Family C)")
    if len(distinct_14_n3) == 1:
        the_set = next(iter(distinct_14_n3))
        is_family_c = (set(the_set) == FAMILY_C)
        print(f"  Profile-14 equation set == Family C: {is_family_c}")
    else:
        is_family_c = False
    c5_ok = (total_n3 == 729
             and smallest_n3 == 14
             and n_at_14_n3 == 120
             and n_below_14_n3 == 0
             and n_above_14_n3 == 609
             and len(distinct_14_n3) == 1
             and is_family_c)
    checks.append(("C5 (order-3 enumeration: 729 magmas, 120 hit Family C)",
                   c5_ok))
    print()

    # C6 (Section 4.7, order 5): exhaustive enumeration of all 720 symmetric
    # 5x5 Latin squares (commutative quasigroups of order 5). Manuscript
    # claims distribution: 14:480, 15:120, 32:30, 89:24, 90:30, 176:6, 294:30.
    # All 480 at profile 14 share Family C's equation set.
    print("C6 (Section 4.7, order 5): all 720 symmetric Latin squares")
    print("  Enumerating symmetric 5x5 Latin squares via backtracking...")
    n5 = 5

    def enumerate_sym_latin_squares(n):
        """Yield each symmetric n x n Latin square as a list-of-lists.
        A symmetric Latin square has L[i][j]=L[j][i], every row a
        permutation of {0,...,n-1}, every column likewise. We backtrack
        over the upper-triangular cells in row-major order, mirroring
        each off-diagonal placement to the lower triangle."""
        L = [[-1]*n for _ in range(n)]
        # precompute per-row and per-column used-value bitmasks for speed
        row_used = [0]*n
        col_used = [0]*n

        def back(idx):
            # idx counts cells in row-major upper-triangular order:
            # (0,0),(0,1),...,(0,n-1),(1,1),(1,2),...,(n-1,n-1)
            if idx == n*(n+1)//2:
                yield [row[:] for row in L]
                return
            # decode idx -> (i,j) with i<=j
            r = idx
            i = 0
            while r >= n - i:
                r -= n - i
                i += 1
            j = i + r
            for v in range(n):
                bit = 1 << v
                if row_used[i] & bit: continue
                if col_used[j] & bit: continue
                if i != j:
                    if row_used[j] & bit: continue
                    if col_used[i] & bit: continue
                # place
                L[i][j] = v
                row_used[i] |= bit
                col_used[j] |= bit
                if i != j:
                    L[j][i] = v
                    row_used[j] |= bit
                    col_used[i] |= bit
                yield from back(idx + 1)
                # unplace
                L[i][j] = -1
                row_used[i] &= ~bit
                col_used[j] &= ~bit
                if i != j:
                    L[j][i] = -1
                    row_used[j] &= ~bit
                    col_used[i] &= ~bit

        yield from back(0)

    profile_dist_n5 = {}
    profile14_sets_n5 = []
    total_n5 = 0
    t_start_c6 = time.time()
    for table in enumerate_sym_latin_squares(n5):
        prof = profile_set(table)
        sz = len(prof)
        profile_dist_n5[sz] = profile_dist_n5.get(sz, 0) + 1
        if sz == 14:
            profile14_sets_n5.append(frozenset(prof))
        total_n5 += 1
        if total_n5 % 60 == 0:
            print(f"    {total_n5}/720 ({time.time()-t_start_c6:.1f}s)")
    print(f"  Total enumerated: {total_n5} (expected 720)")
    print(f"  Profile distribution:")
    for sz in sorted(profile_dist_n5):
        print(f"    profile {sz}: {profile_dist_n5[sz]} magmas")
    expected_dist_n5 = {14: 480, 15: 120, 32: 30, 89: 24,
                        90: 30, 176: 6, 294: 30}
    distinct_14_n5 = set(profile14_sets_n5)
    print(f"  Distinct equation sets among profile-14 magmas: "
          f"{len(distinct_14_n5)} (manuscript: 1, = Family C)")
    if len(distinct_14_n5) == 1:
        the_set5 = next(iter(distinct_14_n5))
        is_family_c5 = (set(the_set5) == FAMILY_C)
        print(f"  Profile-14 equation set == Family C: {is_family_c5}")
    else:
        is_family_c5 = False
    c6_ok = (total_n5 == 720
             and profile_dist_n5 == expected_dist_n5
             and len(distinct_14_n5) == 1
             and is_family_c5)
    checks.append(("C6 (order-5 enumeration: 720 LS, 480 hit Family C)",
                   c6_ok))
    print()

    # Summary
    n_pass = sum(1 for _, ok in checks if ok)
    print("=" * 60)
    print(" SUMMARY")
    print("=" * 60)
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}: {name}")
    print()
    print(f"  Overall: {'PASS' if n_pass == len(checks) else 'FAIL'} "
          f"({n_pass}/{len(checks)})")
    print(f"  Total runtime: {time.time() - t0:.1f}s")

    return n_pass == len(checks)


if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
