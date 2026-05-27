"""etp_engineering_toolkit_v2.py -- ETP-augmented engineering toolkit.

Built on Tao's Equational Theories Project (https://github.com/teorth/equational_theories).
Adds commands for fast tabulated-data lookups + family enumeration on top of
the original toolkit's per-magma probe via scripts/explore_magma.py.

USAGE
-----
  python etp_engineering_toolkit_v2.py <COMMAND> [args]

COMMANDS
--------
  profile_test TABLE
    Test a magma table through ETP; report profile size + equation IDs.
    TABLE is a JSON-like 2D list, e.g. "[[0,1,2],[1,2,0],[2,0,1]]"

  find_profile N [--order ORDER]
    Find all magmas in ETP tabulated data with profile size exactly N.
    Optional --order filters to a specific magma order.

  list_families N
    Find all magmas with profile N, group by distinct equation sets,
    report anchor equation for each family.

  family_anchors
    Survey all profile sizes that appear in ETP tabulated data,
    grouped by anchor equation (= lowest non-trivial equation ID).

  smallest_commutative
    Find the smallest-profile commutative magma in ETP tabulated data
    (= smallest commutative-forced minimum at small order).

  test_linear A B C N
    Build the linear magma (Ax + By + C) mod N and test through ETP.

  test_sigma_n_min N
    Build the sigma_n^min magma (1 fixed + (n-1)-cycle) at order N
    and test through ETP.

  show_equation EQ_ID [EQ_ID ...]
    Display textual form of one or more equation IDs.

  classify_table TABLE
    Comprehensive classification of a magma table: profile, commutativity,
    quasigroup property, identity element, idempotents, sub-magma count.

EXAMPLES
--------
  python etp_engineering_toolkit_v2.py profile_test "[[0,1,2],[1,2,0],[2,0,1]]"
  python etp_engineering_toolkit_v2.py find_profile 14
  python etp_engineering_toolkit_v2.py list_families 14
  python etp_engineering_toolkit_v2.py test_linear 5 3 6 7
  python etp_engineering_toolkit_v2.py show_equation 43 4658

"""
import sys
import os
import json
import re
import argparse
from collections import defaultdict

# Wire up ETP imports
ETP_BASE = "C:\\Users\\brayd\\OneDrive\\Desktop\\etp"
ETP_SCRIPTS = os.path.join(ETP_BASE, "scripts")
ETP_GENERATED = os.path.join(ETP_BASE, "equational_theories", "Generated",
                              "All4x4Tables", "data")
ETP_FINSEARCH = os.path.join(ETP_BASE, "equational_theories", "Generated",
                              "FinSearch", "data")
ETP_EQS = os.path.join(ETP_BASE, "equational_theories", "Equations")

sys.path.insert(0, ETP_SCRIPTS)
from explore_magma import (read_equations_map, test_equation,
                           get_binary_operation_map)

# Cache for parsed data
_TABULATED_MAGMAS = None
_EQUATIONS_MAP = None


def load_equations_map():
    global _EQUATIONS_MAP
    if _EQUATIONS_MAP is None:
        _EQUATIONS_MAP = read_equations_map()
    return _EQUATIONS_MAP


def load_tabulated_magmas():
    """Yield (table, profile_set, source_file) from all ETP tabulated data."""
    global _TABULATED_MAGMAS
    if _TABULATED_MAGMAS is not None:
        return _TABULATED_MAGMAS
    data_files = [
        os.path.join(ETP_GENERATED, f) for f in [
            "refutations2x2.txt", "refutations3x3.txt", "refutations4x4.txt",
            "extra.txt", "vampire-generated.txt", "z3-generated.txt",
            "cancellative-manual.txt", "manual-5x5.txt",
            "manual-11x11.txt", "manual-13x13.txt",
        ]
    ]
    data_files.append(os.path.join(ETP_FINSEARCH, "refutations.txt"))

    out = []
    for path in data_files:
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
                    except json.JSONDecodeError:
                        current = None
                        continue
                    if current:
                        try:
                            table = json.loads(current)
                            out.append((table, tuple(sorted(proves)),
                                       os.path.basename(path)))
                        except Exception:
                            pass
                    current = None
    _TABULATED_MAGMAS = out
    return out


# ============================================================================
# Commands

def cmd_profile_test(args):
    table = json.loads(args.table)
    em = load_equations_map()
    bop = get_binary_operation_map(table)
    sat = []
    for eq_id, eq_str in em.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            sat.append(eq_id)
    print(f"Profile: {len(sat)} / {len(em)}")
    print(f"Equation IDs: {sat}")


def cmd_find_profile(args):
    target_n = args.n
    order_filter = args.order
    magmas = load_tabulated_magmas()
    found = []
    for table, proves, src in magmas:
        if len(proves) != target_n:
            continue
        if order_filter and len(table) != order_filter:
            continue
        found.append((table, proves, src))
    print(f"Found {len(found)} magmas with profile {target_n}"
          + (f" at order {order_filter}" if order_filter else ""))
    for table, proves, src in found[:20]:
        print(f"  order {len(table)}, src={src}: {table}")
    if len(found) > 20:
        print(f"  ... and {len(found) - 20} more")


def cmd_list_families(args):
    target_n = args.n
    magmas = load_tabulated_magmas()
    families = defaultdict(list)
    for table, proves, src in magmas:
        if len(proves) == target_n:
            families[proves].append((table, src))

    em = load_equations_map()
    print(f"Profile-{target_n} families in ETP tabulated data: {len(families)}")
    print()
    fam_list = sorted(families.items(),
                       key=lambda kv: min((e for e in kv[0] if e > 1),
                                          default=float('inf')))
    for i, (eq_set, occurs) in enumerate(fam_list, 1):
        non_trivial = [e for e in eq_set if e > 1]
        anchor = min(non_trivial) if non_trivial else 1
        anchor_txt = em.get(anchor, "?").replace("◇", "*")
        print(f"FAMILY #{i}")
        print(f"  Anchor: equation {anchor} = '{anchor_txt}'")
        print(f"  Equation IDs ({len(eq_set)}): {list(eq_set)}")
        print(f"  Realized by {len(occurs)} magma(s):")
        for tbl, src in occurs[:3]:
            print(f"    order {len(tbl)}, src={src}: {tbl}")
        if len(occurs) > 3:
            print(f"    ... and {len(occurs) - 3} more")
        print()


def cmd_family_anchors(args):
    magmas = load_tabulated_magmas()
    em = load_equations_map()

    # Map anchor_id -> list of (profile_size, count)
    by_anchor = defaultdict(lambda: defaultdict(int))
    for table, proves, src in magmas:
        non_trivial = [e for e in proves if e > 1]
        anchor = min(non_trivial) if non_trivial else 1
        by_anchor[anchor][len(proves)] += 1

    print(f"Anchor equation survey across {len(magmas)} tabulated magmas")
    print()
    for anchor in sorted(by_anchor.keys()):
        anchor_txt = em.get(anchor, "?").replace("◇", "*")
        profiles = by_anchor[anchor]
        total_count = sum(profiles.values())
        profile_list = sorted(profiles.items())[:5]
        profile_str = ", ".join(f"profile {p}: {c}" for p, c in profile_list)
        if len(profiles) > 5:
            profile_str += f", ... ({len(profiles) - 5} more)"
        print(f"  Anchor {anchor} ({total_count} magmas): {anchor_txt}")
        print(f"    {profile_str}")


def cmd_smallest_commutative(args):
    magmas = load_tabulated_magmas()
    comm_magmas = [(t, p, s) for t, p, s in magmas
                   if all(t[i][j] == t[j][i]
                          for i in range(len(t))
                          for j in range(len(t)))]
    if not comm_magmas:
        print("No commutative magmas found in tabulated data.")
        return
    min_comm = min(comm_magmas, key=lambda x: len(x[1]))
    print(f"Smallest commutative profile in ETP tabulated data: "
          f"{len(min_comm[1])} (order {len(min_comm[0])})")
    print(f"  Table: {min_comm[0]}")
    print(f"  Equations: {list(min_comm[1])[:30]}"
          f"{'...' if len(min_comm[1]) > 30 else ''}")
    print(f"  Source: {min_comm[2]}")


def cmd_test_linear(args):
    a, b, c, n = args.a, args.b, args.c, args.n
    table = [[(a * x + b * y + c) % n for y in range(n)] for x in range(n)]
    em = load_equations_map()
    bop = get_binary_operation_map(table)
    sat = []
    for eq_id, eq_str in em.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            sat.append(eq_id)
    print(f"({a}x + {b}y + {c}) mod {n}: profile {len(sat)} / {len(em)}")
    comm = all(table[i][j] == table[j][i] for i in range(n) for j in range(n))
    print(f"  Commutative: {comm}")
    print(f"  Equation IDs: {sat}")


def cmd_test_sigma_n_min(args):
    n = args.n
    sigma = [0] + [(k + 1) if k < n - 1 else 1 for k in range(1, n)]
    table = [[sigma[(x + y) % n] for y in range(n)] for x in range(n)]
    em = load_equations_map()
    bop = get_binary_operation_map(table)
    sat = []
    for eq_id, eq_str in em.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            sat.append(eq_id)
    print(f"sigma_{n}^min = {sigma}")
    print(f"  Profile: {len(sat)} / {len(em)}")
    print(f"  Equation IDs: {sat}")


def cmd_show_equation(args):
    em = load_equations_map()
    for eq_id in args.ids:
        eq_str = em.get(eq_id, "?").replace("◇", "*")
        print(f"  {eq_id}: {eq_str}")


def cmd_classify_table(args):
    table = json.loads(args.table)
    n = len(table)
    em = load_equations_map()
    bop = get_binary_operation_map(table)
    sat = []
    for eq_id, eq_str in em.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            sat.append(eq_id)

    comm = all(table[i][j] == table[j][i] for i in range(n) for j in range(n))
    s = set(range(n))
    quasi = (all(set(table[i]) == s for i in range(n))
             and all(set(table[i][j] for i in range(n)) == s
                      for j in range(n)))
    idempotents = [i for i in range(n) if table[i][i] == i]
    identity = None
    for e in range(n):
        if all(table[e][i] == i and table[i][e] == i for i in range(n)):
            identity = e
            break
    print(f"Magma classification (order {n}):")
    print(f"  Table:      {table}")
    print(f"  Profile:    {len(sat)} / {len(em)} ETP equations")
    print(f"  Equations:  {sat[:20]}{'...' if len(sat) > 20 else ''}")
    print(f"  Commutative: {comm}")
    print(f"  Quasigroup:  {quasi}")
    print(f"  Identity:    {identity if identity is not None else 'none'}")
    print(f"  Idempotents: {idempotents}")


# ============================================================================
# Main / argparse

def main():
    parser = argparse.ArgumentParser(description="ETP engineering toolkit v2")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("profile_test")
    p.add_argument("table")
    p.set_defaults(func=cmd_profile_test)

    p = sub.add_parser("find_profile")
    p.add_argument("n", type=int)
    p.add_argument("--order", type=int, default=None)
    p.set_defaults(func=cmd_find_profile)

    p = sub.add_parser("list_families")
    p.add_argument("n", type=int)
    p.set_defaults(func=cmd_list_families)

    p = sub.add_parser("family_anchors")
    p.set_defaults(func=cmd_family_anchors)

    p = sub.add_parser("smallest_commutative")
    p.set_defaults(func=cmd_smallest_commutative)

    p = sub.add_parser("test_linear")
    p.add_argument("a", type=int)
    p.add_argument("b", type=int)
    p.add_argument("c", type=int)
    p.add_argument("n", type=int)
    p.set_defaults(func=cmd_test_linear)

    p = sub.add_parser("test_sigma_n_min")
    p.add_argument("n", type=int)
    p.set_defaults(func=cmd_test_sigma_n_min)

    p = sub.add_parser("show_equation")
    p.add_argument("ids", nargs="+", type=int)
    p.set_defaults(func=cmd_show_equation)

    p = sub.add_parser("classify_table")
    p.add_argument("table")
    p.set_defaults(func=cmd_classify_table)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
