"""sts_15_classification.py -- test whether the profile-382-vs-342 split
in our Steiner quasigroup analysis tracks the geometric-vs-combinatorial
origin of STS.

At order 15: 80 non-isomorphic Steiner triple systems exist (per Colbourn
& Rosa). The two famous ones:
  - PG(3,2) STS(15): the projective geometry STS, "Kirkman's schoolgirl"-related
  - cyclic STS(15) from base blocks via Bose construction

Test:
  - Build PG(3,2) STS(15) -- 35 lines of PG(3,2)
  - Build cyclic STS(15)
  - Compute squag profiles
  - Compare against profile 382 (small geometric) and profile 342 (combinatorial)

Hypothesis: PG(3,2)-derived squag should have profile 382 (or different but
still distinct from cyclic); cyclic should have profile 342.
"""
import sys, os, json
from itertools import product

if hasattr(sys.stdout, "reconfigure"):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

ETP_PATH = os.environ.get("ETP_PATH",
    r"C:\Users\brayd\OneDrive\Desktop\etp\scripts")
sys.path.insert(0, ETP_PATH)
from explore_magma import (read_equations_map, test_equation,
                            get_binary_operation_map)


FAMILY_C = frozenset({1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442,
                       4482, 4531, 4544, 4635, 4677})
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


def sts_from_blocks(n, blocks):
    """Build squag from STS blocks. Returns table or None if invalid."""
    blocks = [frozenset(b) for b in blocks]
    pair_count = {}
    for b in blocks:
        if len(b) != 3:
            print(f"    BAD: block {b} has size {len(b)}")
            return None
        for x in b:
            for y in b:
                if x < y:
                    pair_count[(x, y)] = pair_count.get((x, y), 0) + 1
    bad = {k: v for k, v in pair_count.items() if v != 1}
    expected_pairs = n * (n - 1) // 2
    if len(pair_count) != expected_pairs or bad:
        print(f"    BAD STS: {len(pair_count)} pairs covered ({expected_pairs} expected); "
              f"{len(bad)} pairs with wrong count")
        return None
    t = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y:
                t[x][y] = x; continue
            for b in blocks:
                if x in b and y in b:
                    t[x][y] = next(iter(b - {x, y}))
                    break
    return t


def pg32_sts15():
    """PG(3, 2) projective space over F_2 has 15 points, 35 lines.
    Each line has 3 points. This forms STS(15).
    Points: nonzero vectors in F_2^4 / scalar (but F_2 scalar = 1, so just
    nonzero vectors in F_2^4). 15 = 2^4 - 1 points.
    Lines: each line is determined by 2 points x, y; third point = x + y in F_2^4.
    """
    points = list(product([0, 1], repeat=4))
    points = [p for p in points if any(p)]  # remove zero vector
    assert len(points) == 15
    idx = {p: i for i, p in enumerate(points)}
    blocks = set()
    for i in range(15):
        for j in range(i+1, 15):
            x = points[i]; y = points[j]
            z = tuple((a + b) % 2 for a, b in zip(x, y))
            block = frozenset({idx[x], idx[y], idx[z]})
            blocks.add(block)
    assert len(blocks) == 35
    return sts_from_blocks(15, list(blocks))


def cyclic_sts15():
    """Cyclic STS(15) -- use Heffter/Bose construction.
    For v = 15, base blocks (mod 15): we need 7 base blocks for STS(15)
    via cyclic. Standard cyclic STS(15) base blocks:
    {0,1,4}, {0,2,9}, {0,5,11} -- partial. Actually STS(15) has 35 blocks
    and cyclic STS(15) has 15*7/3 = 35 blocks via 7 orbits.

    Let's use a known cyclic STS(15) construction: triplet starters
    {0,1,5}, {0,2,11}, {0,3,7} -- but these need to be checked.

    Simpler: use Heffter's first difference set. Or just hardcode one
    from a reliable source.

    The cyclic STS(15) is NOT pure-cyclic (depending on construction);
    many constructions are "almost cyclic". Let's use the Netto STS(15):
    base blocks {0,1,4}, {0,2,8}, {0,5,11} mod 15.
    """
    base_blocks = [(0, 1, 4), (0, 2, 8), (0, 5, 11)]
    blocks_set = set()
    for bb in base_blocks:
        for shift in range(15):
            block = frozenset((x + shift) % 15 for x in bb)
            blocks_set.add(block)
    print(f"    candidate Netto STS(15): {len(blocks_set)} blocks")
    return sts_from_blocks(15, list(blocks_set))


def hadamard_3_sts():
    """Try a Hadamard-design-based STS(15) construction.
    H_3 = Hadamard matrix of order 4 (Sylvester construction).
    The associated STS(7) is the Fano plane; for STS(15) we use H_4 (order 8)
    or the Paley construction.

    Alternative: use the Galois field GF(16) cyclic difference set.
    GF(16) = F_2[x]/(x^4 + x + 1). Singer difference set:
    {1, 2, 4, 8} multiplied by powers of primitive elem gives STS(15) lines.

    For simplicity, return None -- PG(3,2) and Netto cover the main cases.
    """
    return None


def main():
    print("="*70)
    print("  STS(15) profile classification: geometric vs combinatorial")
    print("="*70)
    print()

    results = []

    # ---- PG(3,2) STS(15) ----
    print("[1] PG(3, 2) projective STS(15) (35 lines from F_2^4 \\ {0}):")
    t = pg32_sts15()
    if t:
        p = profile_of(t)
        extra = sorted(p - FAMILY_C)
        print(f"    profile size: {len(p)}")
        print(f"    contains Family C: {FAMILY_C.issubset(p)}")
        if len(p) == 382:
            print(f"    --> MATCHES profile 382 (small geometric STS pattern)")
        elif len(p) == 342:
            print(f"    --> matches profile 342 (broad squag variety)")
        else:
            print(f"    --> NEW profile (not 382, not 342)")
        results.append(("PG(3,2) STS(15)", len(p), sorted(p)))
    print()

    # ---- Netto / cyclic STS(15) ----
    print("[2] Netto cyclic STS(15) with base blocks {0,1,4}, {0,2,8}, {0,5,11}:")
    t = cyclic_sts15()
    if t:
        p = profile_of(t)
        extra = sorted(p - FAMILY_C)
        print(f"    profile size: {len(p)}")
        print(f"    contains Family C: {FAMILY_C.issubset(p)}")
        if len(p) == 382:
            print(f"    --> matches profile 382 (small geometric STS pattern)")
        elif len(p) == 342:
            print(f"    --> matches profile 342 (broad squag variety)")
        else:
            print(f"    --> NEW profile (not 382, not 342)")
        results.append(("Netto cyclic STS(15)", len(p), sorted(p)))
    print()

    # ---- Compare ----
    if len(results) >= 2:
        print("[3] Profile comparison:")
        p1 = set(results[0][2])
        p2 = set(results[1][2])
        print(f"    {results[0][0]}: profile size {len(p1)}")
        print(f"    {results[1][0]}: profile size {len(p2)}")
        print(f"    Symmetric difference: {len(p1 ^ p2)} equations")
        print(f"    In PG(3,2) but not Netto: {sorted(p1 - p2)[:10]}{'...' if len(p1-p2)>10 else ''}")
        print(f"    In Netto but not PG(3,2): {sorted(p2 - p1)[:10]}{'...' if len(p2-p1)>10 else ''}")

    # Save
    out_path = os.path.join(os.path.dirname(__file__), "..",
                             "overnight_outputs", "sts_15_classification.json")
    out = {
        "results": [
            {"name": name, "profile_size": size,
             "extras_vs_family_c": sorted(set(eqs) - FAMILY_C)[:50]}
            for name, size, eqs in results
        ],
    }
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
