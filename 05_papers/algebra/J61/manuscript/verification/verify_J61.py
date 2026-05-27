"""verify_J61.py -- methodology paper verification.

CC-BY-4.0. (c) 2026 Brayden Ross Sanders / 7Site LLC. M. Gish co-author.

Requires the Equational Theories Project repo at ETP_PATH.

Verifies the 5 checks of section 10:
  1. Closure of equation 43 (commutativity) in ETP graph has size 14.
  2. sigma-magma's profile equals {1} ∪ closure(43).
  3. Intersection of 8 commutative magmas equals {1} ∪ closure(43).
  4. None of 24 ETP-tabulated profile-14 magmas matches any size-14 closure.
  5. Constant-diagonal random magmas at order 5 realize closure of eq 40
     (C1, "all squares equal").

Runtime ~15 seconds.
"""
import sys, os, json, time, random
ETP_PATH = "C:\\Users\\brayd\\OneDrive\\Desktop\\etp"
sys.path.insert(0, os.path.join(ETP_PATH, "scripts"))
from explore_magma import (read_equations_map, test_equation,
                           get_binary_operation_map)


def main():
    t0 = time.time()
    print("J61 verification")
    print()

    # Load equations + implications
    em = read_equations_map()
    with open(os.path.join(ETP_PATH, "equational_theories", "Generated",
                            "All4x4Tables", "data", "implications.json")) as f:
        imp_data = json.load(f)
    from collections import defaultdict
    implies = defaultdict(set)
    for imp in imp_data["implications"]:
        lhs = int(imp["lhs"].replace("Equation", ""))
        rhs = int(imp["rhs"].replace("Equation", ""))
        implies[lhs].add(rhs)

    def closure(start):
        visited = {start}
        frontier = {start}
        while frontier:
            nf = set()
            for eq in frontier:
                for ne in implies[eq]:
                    if ne not in visited:
                        visited.add(ne)
                        nf.add(ne)
            frontier = nf
        return visited

    def profile_set(table):
        bop = get_binary_operation_map(table)
        sat = set()
        for eq_id, eq_str in em.items():
            passed, _ = test_equation(eq_str, bop)
            if passed:
                sat.add(eq_id)
        return sat

    checks = []

    # Check 1: closure(43) has size 14
    cl43 = closure(43)
    family_C = cl43 | {1}
    c1_ok = (len(family_C) == 14)
    print(f"Check 1: |closure(43) U {{1}}| = {len(family_C)} (expected 14)")
    checks.append(("Closure of eq 43 has size 14", c1_ok))

    # Check 2: sigma-magma profile equals Family C
    SIGMA = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
    sigma_table = [[SIGMA[(x+y) % 10] for y in range(10)] for x in range(10)]
    sigma_profile = profile_set(sigma_table)
    c2_ok = (sigma_profile == family_C)
    print(f"Check 2: sigma-magma profile equals Family C? {c2_ok}")
    checks.append(("sigma-magma realizes Family C", c2_ok))

    # Check 3: intersection of 8 commutative magmas = Family C
    BHML = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,2,6,6],[2,3,3,4,5,6,7,3,6,6],
            [3,4,4,4,5,6,7,4,6,6],[4,5,5,5,5,6,7,5,7,7],[5,6,6,6,6,6,7,6,7,7],
            [6,7,7,7,7,7,7,7,7,7],[7,2,3,4,5,6,7,8,9,0],[8,6,6,6,7,7,7,9,7,8],
            [9,6,6,6,7,7,7,0,8,0]]
    CL_STD = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,7,8,1],[2,3,4,5,6,7,7,8,7,2],
              [3,4,5,6,7,7,7,7,7,3],[4,5,6,7,7,7,7,8,7,4],[5,6,7,7,7,8,7,7,7,5],
              [6,7,7,7,7,7,8,7,7,6],[7,7,8,7,8,7,7,8,7,7],[8,8,7,7,7,7,7,7,7,8],
              [9,1,2,3,4,5,6,7,8,0]]
    TSML = [[0,0,0,0,0,0,0,7,0,0],[0,7,3,7,7,7,7,7,7,7],[0,3,7,7,4,7,7,7,7,9],
            [0,7,7,7,7,7,7,7,7,3],[0,7,4,7,7,7,7,7,8,7],[0,7,7,7,7,7,7,7,7,7],
            [0,7,7,7,7,7,7,7,7,7],[7,7,7,7,7,7,7,7,7,7],[0,7,7,7,8,7,7,7,7,7],
            [0,7,9,3,7,7,7,7,7,7]]
    s10min = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    s10min_table = [[s10min[(x+y) % 10] for y in range(10)] for x in range(10)]
    Z3 = [[(x+y) % 3 for y in range(3)] for x in range(3)]
    Z5 = [[(x+y) % 5 for y in range(5)] for x in range(5)]
    T4 = [[1, 0, 2], [0, 2, 1], [2, 1, 0]]

    comm_magmas = [sigma_table, BHML, CL_STD, s10min_table, TSML, Z3, Z5, T4]
    profiles = [profile_set(m) for m in comm_magmas]
    intersection = profiles[0]
    for p in profiles[1:]:
        intersection = intersection & p
    c3_ok = (intersection == family_C)
    print(f"Check 3: Intersection of 8 commutative magmas equals Family C? {c3_ok}")
    print(f"  Sizes: sigma={len(profiles[0])}, BHML={len(profiles[1])}, "
          f"CL_STD={len(profiles[2])}, sigma_10^min={len(profiles[3])}, "
          f"TSML={len(profiles[4])}, Z/3={len(profiles[5])}, "
          f"Z/5={len(profiles[6])}, T_4={len(profiles[7])}")
    checks.append(("Intersection of 8 commutative magmas = Family C",
                  c3_ok))

    # Check 4: No ETP-tabulated profile-14 magma matches any size-14 closure
    # Load all tabulated magmas
    ETP_GEN = os.path.join(ETP_PATH, "equational_theories", "Generated",
                            "All4x4Tables", "data")
    p14_magmas = []
    for fname in ["refutations2x2.txt", "refutations3x3.txt", "refutations4x4.txt",
                  "extra.txt", "vampire-generated.txt", "z3-generated.txt",
                  "cancellative-manual.txt"]:
        path = os.path.join(ETP_GEN, fname)
        if not os.path.exists(path):
            continue
        current = None
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Table "):
                    current = line[6:].strip()
                elif line.startswith("Proves "):
                    try:
                        proves = json.loads(line[7:].strip())
                    except:
                        current = None
                        continue
                    if current and len(proves) == 14:
                        try:
                            tbl = json.loads(current)
                            p14_magmas.append((tbl, frozenset(proves)))
                        except:
                            pass
                    current = None

    # The 8 size-14 closures
    size_14_anchors = [40, 43, 1312, 2241, 4295, 4303, 4610, 4637]
    size_14_closures = [closure(a) | {1} for a in size_14_anchors]

    n_matching = 0
    for tbl, p in p14_magmas:
        if any(p == cl for cl in size_14_closures):
            n_matching += 1
    c4_ok = (n_matching == 0)
    print(f"Check 4: 0 of {len(p14_magmas)} tabulated profile-14 magmas "
          f"matches any size-14 closure? {c4_ok} (matched: {n_matching})")
    checks.append(("No tabulated profile-14 magma matches a size-14 closure",
                  c4_ok))

    # Check 5: Constant-diagonal random magmas realize C1 (closure of eq 40)
    C1 = closure(40) | {1}
    random.seed(42)
    n_C1_found = 0
    n_C1_trials = 30
    for _ in range(n_C1_trials):
        n = 5
        tbl = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    tbl[i][j] = 0
                else:
                    tbl[i][j] = random.randint(0, n-1)
        if profile_set(tbl) == C1:
            n_C1_found += 1
    c5_ok = (n_C1_found > 0)
    print(f"Check 5: Random constant-diagonal magmas realize C1? "
          f"{n_C1_found}/{n_C1_trials} hits -> {c5_ok}")
    checks.append(("Random const-diag magmas realize C1", c5_ok))

    # Summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    n_pass = 0
    for name, ok in checks:
        status = "PASS" if ok else "FAIL"
        if ok:
            n_pass += 1
        print(f"  {status}: {name}")
    print()
    print(f"  Overall: {'PASS' if n_pass == len(checks) else 'FAIL'} "
          f"({n_pass}/{len(checks)})")
    print(f"  Runtime: {time.time() - t0:.1f}s")

    return n_pass == len(checks)


if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
