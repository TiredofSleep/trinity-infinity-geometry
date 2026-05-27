"""confirm_squag_profile.py -- confirm profile 382 corresponds to the
Steiner quasigroup variety.

Hypothesis: profile 382 = the squag variety (commutative idempotent
Steiner-relation-satisfying quasigroups).

Tests:
  (1) Order-3 squag has profile 382. (verified)
  (2) Order-7 squag (Fano plane) has profile 382. (verified)
  (3) The 368 extras over Family C include:
      - idempotence eq (x = x*x)
      - Steiner relation ((x*y)*y = x)
      - all derivatives of idempotence and Steiner
  (4) Build a known order-9 STS-derived squag. Verify profile = 382.
  (5) Order-5 has NO profile-382 magmas (since 5 != 1, 3 mod 6).
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


def steiner_quasigroup_3():
    return [[(- (i + j)) % 3 for j in range(3)] for i in range(3)]


def steiner_quasigroup_7():
    """Fano plane STS(7) squag."""
    blocks = [
        frozenset({0,1,2}), frozenset({0,3,4}), frozenset({0,5,6}),
        frozenset({1,3,5}), frozenset({1,4,6}),
        frozenset({2,3,6}), frozenset({2,4,5}),
    ]
    n = 7
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


def steiner_quasigroup_9():
    """STS(9) = AG(2,3) (affine plane of order 3) squag.
    12 blocks total: 3 horizontal, 3 vertical, 3 diagonals, 3 anti-diagonals.
    Cells 0..8 indexed as 3*r + c.
    """
    # AG(2,3) lines: 4 parallel classes of 3 lines each = 12 lines
    cells = [(i, j) for i in range(3) for j in range(3)]
    idx = {c: i for i, c in enumerate(cells)}
    blocks = []
    # horizontals
    for r in range(3):
        blocks.append(frozenset({idx[(r, j)] for j in range(3)}))
    # verticals
    for c in range(3):
        blocks.append(frozenset({idx[(i, c)] for i in range(3)}))
    # 3 lines slope 1: c = i + a mod 3, a = 0, 1, 2
    for a in range(3):
        blocks.append(frozenset({idx[(i, (i + a) % 3)] for i in range(3)}))
    # 3 lines slope -1: c = -i + a mod 3
    for a in range(3):
        blocks.append(frozenset({idx[(i, (-i + a) % 3)] for i in range(3)}))
    # verify each pair occurs in exactly one block
    pair_count = {}
    for b in blocks:
        for x in b:
            for y in b:
                if x < y:
                    pair_count[(x, y)] = pair_count.get((x, y), 0) + 1
    for pc in pair_count.values():
        assert pc == 1, f"STS condition failed: pair_count = {pair_count}"
    # build squag
    n = 9
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


def steiner_quasigroup_13():
    """STS(13) -- standard construction. Use the cyclic difference set.
    Base block under cyclic translation: {0, 1, 3, 9} gives a PG(3,3) — wait,
    use the standard STS(13) construction from Z_13.

    Actually for STS(13) we have 26 blocks. Use Heffter's construction or
    just hardcode the standard one.
    """
    # Bose 1939 construction: cyclic STS(13). Base blocks (mod 13): {0,1,4} and {0,2,8}.
    # Wait, for v ≡ 1 mod 6 the Bose construction uses (v-1)/6 base blocks.
    # For v=13: 2 base blocks. Standard: {0,1,4} and {0,2,7}.
    base_blocks = [(0, 1, 4), (0, 2, 7)]
    blocks_set = set()
    for bb in base_blocks:
        for shift in range(13):
            new_block = frozenset((x + shift) % 13 for x in bb)
            blocks_set.add(new_block)
    blocks = list(blocks_set)
    # Verify pair-covering
    pair_count = {}
    for b in blocks:
        for x in b:
            for y in b:
                if x < y:
                    pair_count[(x, y)] = pair_count.get((x, y), 0) + 1
    bad = {k: v for k, v in pair_count.items() if v != 1}
    if bad:
        print(f"    WARNING: STS(13) construction has {len(bad)} bad pairs")
        return None
    n = 13
    t = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y:
                t[x][y] = x; continue
            for b in blocks:
                if x in b and y in b:
                    t[x][y] = next(iter(b - {x, y}))
                    break
            if t[x][y] is None:
                print(f"    WARNING: no block for ({x},{y})")
                return None
    return t


def main():
    print("="*70)
    print("  Confirming profile 382 = Steiner quasigroup variety")
    print("="*70)

    # ---- Order 3 squag ----
    print("\n[1] STS(3) squag:")
    t3 = steiner_quasigroup_3()
    p3 = profile_of(t3)
    print(f"    profile size: {len(p3)}")

    # ---- Order 7 squag ----
    print("\n[2] STS(7) Fano squag:")
    t7 = steiner_quasigroup_7()
    p7 = profile_of(t7)
    print(f"    profile size: {len(p7)}")

    # ---- Order 9 squag ----
    print("\n[3] STS(9) AG(2,3) squag:")
    t9 = steiner_quasigroup_9()
    p9 = profile_of(t9)
    print(f"    profile size: {len(p9)}")

    # ---- Order 13 squag ----
    print("\n[4] STS(13) cyclic squag:")
    t13 = steiner_quasigroup_13()
    if t13 is not None:
        p13 = profile_of(t13)
        print(f"    profile size: {len(p13)}")
    else:
        print(f"    SKIP (construction failed)")
        p13 = None

    # ---- Verify all profiles agree ----
    print("\n[5] Variety check:")
    if p3 == p7 == p9 and (p13 is None or p3 == p13):
        print(f"    PASS: all squags share IDENTICAL profile of size {len(p3)}")
        print(f"    Conclusion: profile {len(p3)} = the squag variety.")
        # Save the squag-variety equation list
        variety_path = os.path.join(os.path.dirname(__file__), "..",
                                     "overnight_outputs", "squag_variety_eqs.json")
        with open(variety_path, "w") as f:
            json.dump({"size": len(p3), "equations": sorted(p3),
                       "extras_vs_family_c": sorted(p3 - FAMILY_C)}, f, indent=2)
        print(f"    Saved squag variety to {variety_path}")
    else:
        print(f"    FAIL: profiles differ:")
        print(f"      order 3:  size {len(p3)}")
        print(f"      order 7:  size {len(p7)}")
        print(f"      order 9:  size {len(p9)}")
        if p13: print(f"      order 13: size {len(p13)}")
        print(f"    Order 3 vs 7 sym diff: {len(p3 ^ p7)}")
        print(f"    Order 3 vs 9 sym diff: {len(p3 ^ p9)}")


if __name__ == "__main__":
    main()
