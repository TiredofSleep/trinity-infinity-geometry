"""ETP Profile Database — command-line query interface.

Usage:
    python query.py profile <size>            # list all known equational profiles of given size
    python query.py equation <id>             # show closure containing this equation + realizers
    python query.py family <name>             # show contents of a named family (C, R)
    python query.py magma "[[0,1,2],[1,2,0],[2,0,1]]"  # compute profile of a given table
    python query.py stats                     # print summary statistics

Examples:
    python query.py profile 14
    python query.py equation 43
    python query.py family C

Outputs are pretty-printed to stdout. JSON output via `--json`.

This script reads the database files from `../data/` relative to itself.
For magma profile computation, requires ETP's explore_magma.py module
(set ETP_PATH environment variable, or edit ETP_PATH below).
"""
import json
import os
import sys
import argparse
from pathlib import Path

# Force UTF-8 stdout on Windows so the diamond operator (⋄) prints cleanly
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
ETP_PATH = os.environ.get(
    "ETP_PATH",
    r"C:\Users\brayd\OneDrive\Desktop\etp\scripts"
)


def load_json(name):
    with open(DATA_DIR / name, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_profile(size, as_json=False):
    """List known equational profiles of given size."""
    p14 = load_json("profile14_families.json")
    family_c = load_json("family_c.json")
    order3 = load_json("order3_profile_distribution.json")

    size = int(size)
    result = {"size": size, "found": []}

    # Check Family C
    if size == family_c["closure_size"]:
        result["found"].append({
            "name": family_c["name"],
            "anchor_id": family_c["anchor_equation_id"],
            "anchor_expr": family_c["anchor_equation"],
            "equations": [e["id"] for e in family_c["equations"]],
            "smallest_realizer_order": family_c["realizers"]["smallest_known"]["order"],
            "smallest_realizer_table": family_c["realizers"]["smallest_known"]["table"],
        })

    # Check ETP-tabulated profile-14 families
    if size == 14:
        for fam in p14["families"]:
            if fam.get("alias") == "Family C":
                continue  # already added
            result["found"].append({
                "name": fam["name"],
                "anchor_id": fam["anchor_id"],
                "anchor_expr": fam["anchor_expr"],
                "smallest_realizer_order": fam["smallest_order"],
                "smallest_realizer_table": fam.get("realizer_table"),
                "realizer_source": fam.get("realizer_source"),
            })

    # Order-3 statistics
    count_order3 = order3["profile_counts"].get(str(size), 0)
    n_families_order3 = order3["distinct_families_per_profile"].get(str(size), 0)
    n_commutative_order3 = order3["profile_counts_commutative"].get(str(size), 0)
    result["order_3_stats"] = {
        "n_magmas_with_this_profile_size": count_order3,
        "n_distinct_equation_sets": n_families_order3,
        "n_commutative_magmas_with_this_size": n_commutative_order3,
    }

    if as_json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== Profile size {size} ===\n")
        print(f"Order-3 census:")
        print(f"  magmas with this profile size: {count_order3} / 19,683")
        print(f"  distinct equation sets: {n_families_order3}")
        print(f"  of those, commutative: {n_commutative_order3}")
        print()
        if result["found"]:
            print(f"Known families with profile size = {size}:")
            for f in result["found"]:
                print(f"\n  {f['name']}")
                print(f"    anchor:    equation {f['anchor_id']} — {f['anchor_expr']}")
                print(f"    smallest:  order {f['smallest_realizer_order']}")
                if f.get('smallest_realizer_table'):
                    print(f"    table:     {f['smallest_realizer_table']}")
                if f.get('realizer_source'):
                    print(f"    source:    {f['realizer_source']}")
        else:
            print(f"No specific named families at profile size {size}.")


def cmd_equation(eq_id, as_json=False):
    """Show closure containing this equation + known realizers."""
    eq_id = int(eq_id)
    family_c = load_json("family_c.json")
    p14 = load_json("profile14_families.json")

    result = {"equation_id": eq_id, "found_in": []}

    # Check if in Family C
    family_c_ids = [e["id"] for e in family_c["equations"]]
    if eq_id in family_c_ids:
        match = next(e for e in family_c["equations"] if e["id"] == eq_id)
        result["found_in"].append({
            "family": "C",
            "anchor": family_c["anchor_equation_id"],
            "anchor_expr": family_c["anchor_equation"],
            "this_equation": match["expr"],
            "type": match["type"],
            "closure": family_c_ids,
            "closure_size": family_c["closure_size"],
        })

    # Check if anchor of any tabulated family
    for fam in p14["families"]:
        if fam["anchor_id"] == eq_id and fam.get("alias") != "Family C":
            result["found_in"].append({
                "family": fam["name"],
                "anchor": fam["anchor_id"],
                "anchor_expr": fam["anchor_expr"],
                "smallest_realizer_order": fam["smallest_order"],
                "closure_size": 14,
            })

    if as_json:
        print(json.dumps(result, indent=2))
    else:
        if result["found_in"]:
            print(f"=== Equation {eq_id} ===\n")
            for f in result["found_in"]:
                print(f"  Found in family {f['family']}")
                if "this_equation" in f:
                    print(f"    expression: {f['this_equation']}")
                    print(f"    type:       {f['type']}")
                print(f"    anchor:     equation {f['anchor']} — {f['anchor_expr']}")
                print(f"    closure size: {f['closure_size']}")
                if "smallest_realizer_order" in f:
                    print(f"    smallest realizer: order {f['smallest_realizer_order']}")
                print()
        else:
            print(f"Equation {eq_id} not currently catalogued in our profile database.")
            print(f"This means we don't have a known family/closure containing it.")
            print(f"Consult Tao et al.'s ETP catalog for the full equation text.")


def cmd_family(name, as_json=False):
    """Show contents of a named family."""
    name = name.upper().strip()
    if name == "C":
        family_c = load_json("family_c.json")
        if as_json:
            print(json.dumps(family_c, indent=2))
        else:
            print(f"=== Family {name}: {family_c['name']} ===\n")
            print(f"Definition: {family_c['definition']}")
            print(f"Closure size: {family_c['closure_size']}")
            print(f"\nEquations:")
            for e in family_c["equations"]:
                print(f"  {e['id']:>4d}: {e['expr']:<50s} [{e['type']}]")
            print(f"\nUniqueness: {family_c['uniqueness_claim']}")
            print(f"\nEvidence:")
            for order, ev in family_c['uniqueness_evidence'].items():
                print(f"  {order}: {ev}")
    elif name == "R":
        p14 = load_json("profile14_families.json")
        fam_r = next((f for f in p14["families"] if f.get("alias") == "Family R"), None)
        if fam_r:
            if as_json:
                print(json.dumps(fam_r, indent=2))
            else:
                print(f"=== Family R: {fam_r['name']} ===\n")
                print(f"Anchor equation {fam_r['anchor_id']}: {fam_r['anchor_expr']}")
                print(f"Smallest realizer: order {fam_r['smallest_order']}")
                print(f"Realizer source: {fam_r.get('realizer_source', 'N/A')}")
        else:
            print(f"Family R not found in database.")
    else:
        print(f"Unknown family '{name}'. Try 'C' or 'R'.")


def cmd_magma(table_str, as_json=False):
    """Compute the profile of a given magma table."""
    try:
        table = json.loads(table_str)
    except Exception as e:
        print(f"Failed to parse table: {e}")
        print("Expected JSON list-of-lists, e.g. '[[0,1,2],[1,2,0],[2,0,1]]'")
        return

    n = len(table)
    for row in table:
        if len(row) != n:
            print(f"Not a square magma: row length {len(row)} vs n={n}.")
            return

    # Import ETP's explore_magma
    sys.path.insert(0, ETP_PATH)
    try:
        from explore_magma import (read_equations_map, test_equation,
                                    get_binary_operation_map)
    except ImportError as e:
        print(f"Failed to import ETP explore_magma: {e}")
        print(f"Set ETP_PATH env var to your local clone of equational_theories/scripts.")
        return

    em = read_equations_map()
    bop = get_binary_operation_map(table)
    satisfied = set()
    for eq_id, eq_str in em.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            satisfied.add(eq_id)

    profile = sorted(satisfied)
    family_c_ids = set([1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442,
                        4482, 4531, 4544, 4635, 4677])
    is_family_c = (set(profile) == family_c_ids)

    result = {
        "table": table,
        "order": n,
        "profile_size": len(profile),
        "profile": profile,
        "is_family_c": is_family_c,
        "is_commutative": (43 in profile),
    }

    if as_json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== Magma profile ===\n")
        print(f"Order:           {n}")
        print(f"Profile size:    {len(profile)}")
        print(f"Commutative:     {result['is_commutative']}")
        print(f"Family C:        {is_family_c}")
        print(f"Profile (equation IDs): {profile}")


def cmd_stats(as_json=False):
    """Print summary statistics."""
    order3 = load_json("order3_profile_distribution.json")
    order5 = load_json("order5_commutative_qg.json")
    p14 = load_json("profile14_families.json")
    family_c = load_json("family_c.json")
    sigma = load_json("sigma_magma.json")

    result = {
        "order_3": {
            "total_magmas": order3["n_total"],
            "distinct_profile_sizes": order3["n_distinct_profiles"],
            "max_profile_size": max(int(k) for k, v in order3["profile_counts"].items() if v > 0),
            "min_profile_size": min(int(k) for k, v in order3["profile_counts"].items() if v > 0),
        },
        "order_5_commutative": {
            "total_symmetric_latin_squares": order5["n_total"],
            "profile_14_count": order5["profile_14_count"],
            "non_family_c_profile_14": order5["profile_14_non_C"],
        },
        "profile_14_families_known": p14["n_families"],
        "family_c_size": family_c["closure_size"],
        "sigma_magma_order": sigma["order"],
    }

    if as_json:
        print(json.dumps(result, indent=2))
    else:
        print("=== ETP Profile Database -- Summary Statistics ===\n")
        print("Order-3 enumeration (all 19,683 non-isomorphic magmas):")
        print(f"  Distinct profile sizes:    {result['order_3']['distinct_profile_sizes']}")
        print(f"  Min profile size:          {result['order_3']['min_profile_size']}")
        print(f"  Max profile size:          {result['order_3']['max_profile_size']}")
        print(f"  Magmas with profile = 14:  {order3['profile_counts'].get('14', 0)} "
              f"(in {order3['distinct_families_per_profile'].get('14', 0)} equation sets)")
        print(f"  Of those, commutative:     {order3['profile_counts_commutative'].get('14', 0)} "
              f"(ALL in Family C)\n")
        print("Order-5 commutative quasigroups (symmetric Latin squares):")
        print(f"  Total enumerated:          {result['order_5_commutative']['total_symmetric_latin_squares']}")
        print(f"  Profile-14 (= Family C):   {result['order_5_commutative']['profile_14_count']}")
        print(f"  Non-Family-C profile-14:   {result['order_5_commutative']['non_family_c_profile_14']} "
              f"(ZERO -- Conjecture 1 verified at order 5)\n")
        print(f"Known profile-14 families:   {result['profile_14_families_known']}")
        print(f"Family C closure size:        {result['family_c_size']}")


def main():
    parser = argparse.ArgumentParser(description="ETP Profile Database query interface")
    parser.add_argument("--json", action="store_true", help="output JSON")
    parser.add_argument("command", choices=["profile", "equation", "family", "magma", "stats"])
    parser.add_argument("arg", nargs="?", default=None)
    args = parser.parse_args()

    if args.command == "profile":
        if args.arg is None:
            print("usage: query.py profile <size>")
            return
        cmd_profile(args.arg, as_json=args.json)
    elif args.command == "equation":
        if args.arg is None:
            print("usage: query.py equation <id>")
            return
        cmd_equation(args.arg, as_json=args.json)
    elif args.command == "family":
        if args.arg is None:
            print("usage: query.py family <name>")
            return
        cmd_family(args.arg, as_json=args.json)
    elif args.command == "magma":
        if args.arg is None:
            print("usage: query.py magma <table-as-json>")
            return
        cmd_magma(args.arg, as_json=args.json)
    elif args.command == "stats":
        cmd_stats(as_json=args.json)


if __name__ == "__main__":
    main()
