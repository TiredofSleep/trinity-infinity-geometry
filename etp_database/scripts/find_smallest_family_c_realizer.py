"""Find smallest-order Family C realizer (a commutative non-associative
magma with profile exactly the Family C 14 equations).

Searches order 3 only — the T-3 enumeration found 120 such magmas.
Returns the first one in lexicographic order and verifies its profile.
"""
import sys, json, os
ETP_PATH = os.environ.get(
    "ETP_PATH",
    r"C:\Users\brayd\OneDrive\Desktop\etp\scripts"
)
sys.path.insert(0, ETP_PATH)
from explore_magma import (read_equations_map, test_equation,
                           get_binary_operation_map)

FAMILY_C_IDS = frozenset({1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442,
                          4482, 4531, 4544, 4635, 4677})


def is_commutative(t, n):
    return all(t[i][j] == t[j][i] for i in range(n) for j in range(n))


def enumerate_commutative_3x3():
    """Brute-force all 3x3 commutative magmas (3^6 = 729)."""
    n = 3
    out = []
    for d in range(3**(n*(n+1)//2)):  # 6 cells to fill (upper triangle + diag)
        cells = []
        x = d
        for _ in range(n*(n+1)//2):
            cells.append(x % n)
            x //= n
        t = [[0]*n for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(i, n):
                t[i][j] = cells[idx]
                t[j][i] = cells[idx]
                idx += 1
        out.append(t)
    return out


def main():
    em = read_equations_map()
    print(f"Loaded {len(em)} ETP equations.")
    candidates = enumerate_commutative_3x3()
    print(f"Enumerated {len(candidates)} commutative 3x3 magmas.")

    family_c_realizers = []
    for t in candidates:
        bop = get_binary_operation_map(t)
        sat = set()
        for eq_id, eq_str in em.items():
            passed, _ = test_equation(eq_str, bop)
            if passed:
                sat.add(eq_id)
        if sat == FAMILY_C_IDS:
            family_c_realizers.append(t)
            if len(family_c_realizers) >= 5:
                break  # show first 5

    print(f"\nFound {len(family_c_realizers)} Family C realizers (showing first {min(5, len(family_c_realizers))}):")
    for i, t in enumerate(family_c_realizers):
        print(f"  #{i+1}: {t}")

    if family_c_realizers:
        smallest = family_c_realizers[0]
        print(f"\nSmallest (lex-first) Family C realizer at order 3:")
        print(f"  table: {smallest}")
        print(f"  commutative: {is_commutative(smallest, 3)}")
        # Save to a small file
        out = {
            "order": 3,
            "table": smallest,
            "profile_size": 14,
            "profile": sorted(FAMILY_C_IDS),
            "family": "C",
            "method": "Lexicographic-first commutative non-associative 3x3 magma satisfying exactly the Family C 14 equations.",
            "n_total_family_c_at_order_3": 120,
        }
        out_path = os.path.join(
            os.path.dirname(__file__), "..", "data",
            "smallest_family_c_realizer.json"
        )
        with open(out_path, "w") as f:
            json.dump(out, f, indent=2)
        print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
