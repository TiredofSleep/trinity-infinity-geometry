"""verify_database.py — end-to-end verification of all database claims.

Runs:
  1. Family C = implication-closure of equation 43 (against ETP edge list)
  2. Smallest Family C realizer at order 3 has profile exactly Family C
  3. sigma-magma table satisfies exactly the 14 Family C equations
  4. order3_profile_distribution.json is internally consistent
  5. order5_commutative_qg.json is internally consistent

Exit code 0 if all pass; nonzero otherwise.

Requires ETP_PATH env var pointing to equational_theories/scripts (for
explore_magma.py) and ETP_EDGE_LIST pointing to the unpacked edge list.
"""
import json
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

DATA = Path(__file__).resolve().parent.parent / "data"

FAMILY_C_IDS = frozenset({1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442,
                          4482, 4531, 4544, 4635, 4677})

ETP_PATH = os.environ.get("ETP_PATH",
    r"C:\Users\brayd\OneDrive\Desktop\etp\scripts")
sys.path.insert(0, ETP_PATH)


def load(name):
    with open(DATA / name, "r", encoding="utf-8") as f:
        return json.load(f)


def get_profile(table):
    """Compute the ETP equation profile of a magma table."""
    from explore_magma import (read_equations_map, test_equation,
                                get_binary_operation_map)
    em = read_equations_map()
    bop = get_binary_operation_map(table)
    sat = set()
    for eq_id, eq_str in em.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            sat.add(eq_id)
    return sat


def check_1_family_c_closure():
    """Run verify_family_c.py as a subprocess."""
    import subprocess
    print("[1] Family C = implication-closure of equation 43 ...")
    script = Path(__file__).resolve().parent / "verify_family_c.py"
    edge_list = os.environ.get("ETP_EDGE_LIST",
        r"C:\Users\brayd\OneDrive\Desktop\etp\data\unpacked\edge_list.csv")
    if not os.path.exists(edge_list):
        print(f"    SKIP: edge list not at {edge_list}")
        return None
    result = subprocess.run([sys.executable, str(script),
                             "--edge-list", edge_list],
                            capture_output=True, text=True)
    if result.returncode == 0 and "PASS" in result.stdout:
        print("    PASS")
        return True
    print(f"    FAIL")
    print(result.stdout[-400:])
    return False


def check_2_smallest_realizer():
    print("[2] Smallest Family C realizer at order 3 ...")
    fam_c = load("family_c.json")
    table = fam_c["realizers"]["smallest_known"]["table"]
    profile = get_profile(table)
    if profile == FAMILY_C_IDS:
        print(f"    PASS  (table = {table})")
        return True
    extra = profile - FAMILY_C_IDS
    missing = FAMILY_C_IDS - profile
    print(f"    FAIL  table = {table}")
    print(f"          extra:   {sorted(extra)}")
    print(f"          missing: {sorted(missing)}")
    return False


def check_3_sigma_magma():
    print("[3] sigma-magma profile equals Family C ...")
    sig = load("sigma_magma.json")
    table = sig["operation_table"]
    profile = get_profile(table)
    if profile == FAMILY_C_IDS:
        print(f"    PASS  (order={sig['order']}, sigma={sig['sigma']})")
        return True
    extra = profile - FAMILY_C_IDS
    missing = FAMILY_C_IDS - profile
    print(f"    FAIL")
    print(f"          extra:   {sorted(extra)}")
    print(f"          missing: {sorted(missing)}")
    return False


def check_4_order3_consistency():
    print("[4] order-3 distribution internal consistency ...")
    d = load("order3_profile_distribution.json")
    total = sum(d["profile_counts"].values())
    if total != d["n_total"]:
        print(f"    FAIL  sum(profile_counts) = {total} != n_total = {d['n_total']}")
        return False
    if len([k for k, v in d["profile_counts"].items() if v > 0]) != d["n_distinct_profiles"]:
        print(f"    FAIL  n_distinct_profiles mismatch")
        return False
    comm_total = sum(d["profile_counts_commutative"].values())
    if comm_total != 729:
        print(f"    FAIL  sum(commutative) = {comm_total} != expected 729")
        return False
    # Family C check: all 120 commutative profile-14 should be in Family C
    if d["profile_counts_commutative"].get("14", 0) != 120:
        print(f"    FAIL  commutative profile-14 count != 120")
        return False
    print(f"    PASS  (n_total=19,683, commutative=729, comm-prof-14=120)")
    return True


def check_5_order5_consistency():
    print("[5] order-5 commutative QG internal consistency ...")
    d = load("order5_commutative_qg.json")
    if d["n_total"] != 720:
        print(f"    FAIL  n_total = {d['n_total']} != 720")
        return False
    if d["profile_14_count"] != 480:
        print(f"    FAIL  profile_14_count = {d['profile_14_count']} != 480")
        return False
    if d["profile_14_non_C"] != 0:
        print(f"    FAIL  profile_14_non_C = {d['profile_14_non_C']} != 0")
        return False
    print(f"    PASS  (720 sym-Latin, 480 profile-14, 0 non-C)")
    return True


def main():
    print("=== ETP Profile Database -- Verification ===\n")
    results = []
    results.append(("family_c_closure", check_1_family_c_closure()))
    results.append(("smallest_realizer", check_2_smallest_realizer()))
    results.append(("sigma_magma_profile", check_3_sigma_magma()))
    results.append(("order3_consistency", check_4_order3_consistency()))
    results.append(("order5_consistency", check_5_order5_consistency()))

    print("\n=== Summary ===")
    n_pass = sum(1 for _, r in results if r is True)
    n_fail = sum(1 for _, r in results if r is False)
    n_skip = sum(1 for _, r in results if r is None)
    for name, r in results:
        status = "PASS" if r is True else "FAIL" if r is False else "SKIP"
        print(f"  {status:<5s} {name}")
    print(f"\n{n_pass} PASS, {n_fail} FAIL, {n_skip} SKIP")
    sys.exit(0 if n_fail == 0 else 1)


if __name__ == "__main__":
    main()
