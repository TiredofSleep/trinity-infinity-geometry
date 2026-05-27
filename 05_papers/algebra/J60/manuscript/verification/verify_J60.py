"""verify_J60.py -- machine-precision verification of J60's four theorems
via ETP scripts.

CC-BY-4.0. (c) 2026 Brayden Ross Sanders / 7Site LLC. M. Gish co-author.

Requires: clone of github.com/teorth/equational_theories accessible at
the ETP_PATH defined below. Reads its 4694-equation catalog and uses
its test_equation function.

Verifies:
  Theorem 1: Z/n has profile 32 for n in {5, 6, 7, 8, 9, 10}, with
             identical equation IDs across orders.
  Theorem 2: -(x+y) mod n has profile 294 for n = 4 and 10.
  Theorem 3: 8 commutative magmas' profile intersection = 14 specific IDs.
  Theorem 4: (5x + 3y + 6) mod 7 has profile 14 with different IDs from
             the sigma-magma's (verifies Family R distinct from Family C).

Runtime ~30 seconds.
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
