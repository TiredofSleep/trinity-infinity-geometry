"""squag_variety_diff.py -- identify what distinguishes profile-382 squags
(STS(3), STS(7), STS(9)) from profile-342 squags (cyclic STS(13)).

The 40 equations in profile-382 but NOT in profile-342 are the equations
that hold in SMALL squags (orders 3, 7, 9) but FAIL in larger ones.
These should be "small-order coincidences" -- accidental algebraic identities
in the symmetric small STS that don't hold in general STS.
"""
import sys, os, json
if hasattr(sys.stdout, "reconfigure"):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

ETP_PATH = os.environ.get("ETP_PATH",
    r"C:\Users\brayd\OneDrive\Desktop\etp\scripts")
sys.path.insert(0, ETP_PATH)
from explore_magma import (read_equations_map, test_equation,
                            get_binary_operation_map)


EM = None
def get_em():
    global EM
    if EM is None: EM = read_equations_map()
    return EM


def profile_of(t):
    em = get_em()
    bop = get_binary_operation_map(t)
    sat = set()
    for eq_id, eq_str in em.items():
        if test_equation(eq_str, bop)[0]:
            sat.add(eq_id)
    return sat


def squag_3():
    return [[(- (i + j)) % 3 for j in range(3)] for i in range(3)]


def squag_7():
    blocks = [
        frozenset({0,1,2}), frozenset({0,3,4}), frozenset({0,5,6}),
        frozenset({1,3,5}), frozenset({1,4,6}),
        frozenset({2,3,6}), frozenset({2,4,5}),
    ]
    n = 7
    t = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y: t[x][y] = x; continue
            for b in blocks:
                if x in b and y in b:
                    t[x][y] = next(iter(b - {x, y}))
                    break
    return t


def squag_9():
    cells = [(i, j) for i in range(3) for j in range(3)]
    idx = {c: i for i, c in enumerate(cells)}
    blocks = []
    for r in range(3):
        blocks.append(frozenset({idx[(r, j)] for j in range(3)}))
    for c in range(3):
        blocks.append(frozenset({idx[(i, c)] for i in range(3)}))
    for a in range(3):
        blocks.append(frozenset({idx[(i, (i + a) % 3)] for i in range(3)}))
    for a in range(3):
        blocks.append(frozenset({idx[(i, (-i + a) % 3)] for i in range(3)}))
    n = 9
    t = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y: t[x][y] = x; continue
            for b in blocks:
                if x in b and y in b:
                    t[x][y] = next(iter(b - {x, y}))
                    break
    return t


def squag_13_cyclic():
    base_blocks = [(0, 1, 4), (0, 2, 7)]
    blocks_set = set()
    for bb in base_blocks:
        for shift in range(13):
            new_block = frozenset((x + shift) % 13 for x in bb)
            blocks_set.add(new_block)
    blocks = list(blocks_set)
    n = 13
    t = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y: t[x][y] = x; continue
            for b in blocks:
                if x in b and y in b:
                    t[x][y] = next(iter(b - {x, y}))
                    break
    return t


def main():
    em = get_em()

    print("Computing profiles...")
    p3  = profile_of(squag_3())
    p7  = profile_of(squag_7())
    p9  = profile_of(squag_9())
    p13 = profile_of(squag_13_cyclic())
    print(f"  STS(3):  size {len(p3)}")
    print(f"  STS(7):  size {len(p7)}")
    print(f"  STS(9):  size {len(p9)}")
    print(f"  STS(13): size {len(p13)}")
    print()

    # The 40 extras hold in 3,7,9 but not 13.
    common_small = p3 & p7 & p9
    only_in_small = common_small - p13
    print(f"Equations satisfied by STS(3), STS(7), STS(9) but NOT STS(13):")
    print(f"  count: {len(only_in_small)}")
    print(f"  IDs: {sorted(only_in_small)}")
    print()

    # Print the textual equations
    print("Texts:")
    for eid in sorted(only_in_small):
        print(f"  eq {eid}: {em[eid]}")

    # Save
    out = {
        "profile_3":  {"size": len(p3),  "eq_ids": sorted(p3)},
        "profile_7":  {"size": len(p7),  "eq_ids": sorted(p7)},
        "profile_9":  {"size": len(p9),  "eq_ids": sorted(p9)},
        "profile_13": {"size": len(p13), "eq_ids": sorted(p13)},
        "small_sts_extras": {
            "count": len(only_in_small),
            "eq_ids": sorted(only_in_small),
            "eq_texts": {str(eid): em[eid] for eid in sorted(only_in_small)},
        },
        "common_squag_variety_at_orders_3_7_9_13": {
            "size": len(p3 & p7 & p9 & p13),
            "eq_ids": sorted(p3 & p7 & p9 & p13),
        },
    }
    out_path = os.path.join(os.path.dirname(__file__), "..",
                             "overnight_outputs", "squag_variety_diff.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved diff to {out_path}")


if __name__ == "__main__":
    main()
