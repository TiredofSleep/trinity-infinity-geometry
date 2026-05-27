"""steiner_vs_family_c.py -- compare Family C (commutativity-min) against
classical block-design quasigroups (Steiner, Schroeder, distributive,
abelian-group induced).

Tests:
  (1) Steiner triple system at order 3 (the trivial one, Z_3 over {0,1,2})
       -- compute profile, compare to Family C
  (2) Steiner triple system at order 7 (Fano plane)
       -- build the squag, compute profile, compare to Family C
  (3) Profile-15 commutative quasigroup at order 5
       -- find one in our enumeration, identify the "+1" extra equation
  (4) Z_n with x*y = (ax + by) mod n (linear commutative quasigroups)
       -- compute profile for n=3,5,7
  (5) Profile-32, profile-89, profile-90, profile-176, profile-294 representatives
       -- pick one of each, identify the extras
"""
import sys
import json
import os

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

# Loaded once
EM = None
EM_FULL = None
def get_em():
    global EM, EM_FULL
    if EM is None:
        EM_FULL = read_equations_map()
        EM = EM_FULL
    return EM


def profile_of(table):
    """Return the ETP profile of a magma table."""
    em = get_em()
    bop = get_binary_operation_map(table)
    sat = set()
    for eq_id, eq_str in em.items():
        passed, _ = test_equation(eq_str, bop)
        if passed:
            sat.add(eq_id)
    return sat


def eq_text(eq_id):
    em = get_em()
    return em.get(eq_id, f"<unknown eq {eq_id}>")


# ---------- (1) Steiner quasigroup at order 3 ----------

def steiner_quasigroup_3():
    """x ⋄ y = (-(x+y)) mod 3 satisfies idempotence + Steiner triple property."""
    return [[(- (i + j)) % 3 for j in range(3)] for i in range(3)]


# ---------- (2) Steiner quasigroup at order 7 (from Fano plane) ----------

def steiner_quasigroup_7():
    """Order-7 squag from STS(7) = Fano plane.
    Blocks: {0,1,2}, {0,3,4}, {0,5,6}, {1,3,5}, {1,4,6}, {2,3,6}, {2,4,5}.
    Squag operation: x·y = z where {x,y,z} is a block (z != x, z != y).
    x·x = x (idempotent).
    """
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
                t[x][y] = x
                continue
            # find the block containing {x, y}
            for b in blocks:
                if x in b and y in b:
                    others = b - {x, y}
                    assert len(others) == 1
                    t[x][y] = next(iter(others))
                    break
    return t


# ---------- (3) Linear commutative quasigroup over Z_n ----------

def linear_comm_qg(n, a):
    """x*y = a(x+y) mod n. Commutative; quasigroup iff gcd(a, n) = 1."""
    return [[(a * (x + y)) % n for y in range(n)] for x in range(n)]


# ---------- (4) Find one symmetric Latin square of each profile size at order 5 ----------

def enumerate_5x5_sym_latin_squares():
    """Same as in enumerate_comm_qg_order5.py."""
    N = 5
    results = []
    grid = [[None]*N for _ in range(N)]
    def fill(pos):
        if pos == N * N:
            for i in range(N):
                if set(grid[i]) != set(range(N)):
                    return
            results.append([list(row) for row in grid])
            return
        i, j = pos // N, pos % N
        if grid[i][j] is not None:
            fill(pos + 1)
            return
        if j < i:
            grid[i][j] = grid[j][i]
            fill(pos + 1)
            grid[i][j] = None
            return
        used_row = {grid[i][k] for k in range(N) if grid[i][k] is not None}
        used_col = {grid[k][j] for k in range(N) if grid[k][j] is not None}
        forbidden = used_row | used_col
        for v in range(N):
            if v in forbidden:
                continue
            grid[i][j] = v
            if i != j:
                grid[j][i] = v
            fill(pos + 1)
            grid[i][j] = None
            if i != j:
                grid[j][i] = None
    fill(0)
    return results


def main():
    print("="*70)
    print("  Family C vs classical block-design / Steiner-type quasigroups")
    print("="*70)
    print()

    # ---- (1) Steiner quasigroup at order 3 ----
    print("[1] Steiner quasigroup at order 3 (Z_3 with x*y = -(x+y) mod 3):")
    t3 = steiner_quasigroup_3()
    print(f"    table: {t3}")
    p3 = profile_of(t3)
    extra = p3 - FAMILY_C
    print(f"    profile size: {len(p3)}")
    print(f"    contains Family C? {FAMILY_C.issubset(p3)}")
    print(f"    extra equations beyond Family C: {len(extra)}")
    print()

    # ---- (2) Steiner quasigroup at order 7 (Fano) ----
    print("[2] Steiner quasigroup at order 7 (Fano plane squag):")
    t7 = steiner_quasigroup_7()
    print(f"    table: {t7}")
    p7 = profile_of(t7)
    extra7 = p7 - FAMILY_C
    print(f"    profile size: {len(p7)}")
    print(f"    contains Family C? {FAMILY_C.issubset(p7)}")
    print(f"    extra equations beyond Family C: {len(extra7)}")
    print()

    # ---- (3) Linear commutative quasigroups ----
    print("[3] Linear commutative quasigroups x*y = (a(x+y)) mod n:")
    for n in [3, 5, 7]:
        for a in [1, 2, 3]:
            if a >= n:
                continue
            if __import__('math').gcd(a, n) != 1:
                continue
            t = linear_comm_qg(n, a)
            p = profile_of(t)
            extra = p - FAMILY_C
            print(f"    n={n}, a={a}: profile size {len(p)}, "
                  f"Family C subset? {FAMILY_C.issubset(p)}, "
                  f"extras: {len(extra)}")
    print()

    # ---- (4) Profile-15 commutative quasigroup at order 5: find one ----
    print("[4] Profile-15 symmetric Latin squares at order 5:")
    sls = enumerate_5x5_sym_latin_squares()
    print(f"    Enumerated {len(sls)} symmetric Latin squares of order 5.")
    p15_examples = []
    for t in sls:
        p = profile_of(t)
        if len(p) == 15:
            p15_examples.append((t, p))
            if len(p15_examples) >= 3:
                break
    if p15_examples:
        print(f"    Found {len(p15_examples)} profile-15 examples.")
        t, p = p15_examples[0]
        extra = sorted(p - FAMILY_C)
        print(f"    Example table: {t}")
        print(f"    Extra equation beyond Family C: {extra}")
        for eid in extra:
            print(f"      eq {eid}: {eq_text(eid)}")
    print()

    # ---- (5) Other profile sizes at order 5 ----
    print("[5] Higher-profile commutative QGs at order 5 — extras beyond Family C:")
    seen_profiles = {14, 15}
    for t in sls:
        p = profile_of(t)
        sz = len(p)
        if sz in seen_profiles:
            continue
        seen_profiles.add(sz)
        extra = sorted(p - FAMILY_C)
        print(f"    Profile {sz} (1 example): table={t}")
        print(f"      extras ({len(extra)} eqs): {extra[:15]}{'...' if len(extra)>15 else ''}")
        # Identify a few key extras
        if 1485 in extra:
            print(f"        - eq 1485 present ('distributivity-ish')")
        if 4 in extra:
            print(f"        - eq 4 present ('x*x = y*y')")
        if 8 in extra:
            print(f"        - eq 8 present ('x = x*x' — idempotent)")
    print()


if __name__ == "__main__":
    main()
