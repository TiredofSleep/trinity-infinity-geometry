"""
proof_tsml_3layer_tower.py
Verifies the Sprint 17 (2026-04-17) Theorem A: TSML on Z/10Z is a 3-layer
canonical tower with empty residue-of-residue.

Theorem A. Let R = Z/10Z, h = 7, and sigma(u) = v_2(3u + 1).
Let S = {(1,2),(2,1),(2,4),(4,2),(2,9),(9,2),(4,8),(8,4)} (the seam residue),
    S_ADD = {(1,2),(2,1)}, S_MAX = S \\ S_ADD.
Define
    T(x,y) = max(x,y)        if (x,y) in S_MAX
           = (x+y) mod 10    if (x,y) in S_ADD
           = C0(x,y)         otherwise
where C0 is the canonical construction:
    (a) DEFAULT: C0(x,y) = h
    (b) V0: if x=0 or y=0, C0(x,y) = 0; EXCEPT (0,h),(h,0) -> h
    (c) Shell-stability: if x,y in U(R)\\{1} and sigma(x) != sigma(y),
        C0(x,y) = whichever of x,y has the lower shell
    (rules apply in priority order; each later rule overrides earlier)
Then T(x,y) = published_TSML(x,y) for every (x,y) in R^2.

This script verifies: (1) the 100/100 match, (2) the 92/6/2 decomposition,
(3) Lemma 5 (residue-of-residue empty), (4) Lemma 6 (each layer necessary).

Source for published TSML: papers/ck_tables.py.
Paper: Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/THEOREM_SPINE.md
"""

import sys
from ck_tables import TSML

R = 10
h = 7

# ----- Sprint 17 specification -----
S_ADD = {(1, 2), (2, 1)}
S_MAX = {(2, 4), (4, 2), (2, 9), (9, 2), (4, 8), (8, 4)}
S = S_ADD | S_MAX

UNITS = {1, 3, 7, 9}  # U(Z/10Z) = (Z/10Z)*


def v2(n):
    """2-adic valuation of n (n > 0)."""
    assert n > 0
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def shell(u):
    """Shell partition sigma(u) = v_2(3u + 1), u in UNITS."""
    return v2(3 * u + 1)


def C0(x, y):
    """Canonical construction: DEFAULT then V0 (with exceptions) then shell-stability."""
    val = h  # (a) DEFAULT
    if x == 0 or y == 0:
        # (b) V0 with exception (0,h) or (h,0)
        if (x, y) == (0, h) or (x, y) == (h, 0):
            val = h
        else:
            val = 0
    if x in UNITS and y in UNITS and x != 1 and y != 1:
        # (c) Shell-stability (only fires when both are units != 1)
        sx, sy = shell(x), shell(y)
        if sx != sy:
            val = x if sx < sy else y
    return val


def T_tower(x, y):
    """The 3-layer tower operator."""
    if (x, y) in S_MAX:
        return max(x, y)
    if (x, y) in S_ADD:
        return (x + y) % R
    return C0(x, y)


def banner(msg):
    print()
    print("=" * 72)
    print(msg)
    print("=" * 72)


# =====================================================================
# STEP 0: report shell partition for transparency
# =====================================================================
banner("STEP 0: Shell partition sigma(u) = v_2(3u + 1) on UNITS = {1,3,7,9}")
for u in sorted(UNITS):
    print(f"  u = {u}: 3u+1 = {3*u+1}, sigma(u) = v_2({3*u+1}) = {v2(3*u+1)}")
print("  Note: shell-stability skips u = 1 (per spec).")

# =====================================================================
# STEP 1: verify Theorem A (100/100)
# =====================================================================
banner("STEP 1: Theorem A -- T_tower(x,y) == published_TSML(x,y) for all (x,y)")
mismatches = []
for x in range(R):
    for y in range(R):
        if T_tower(x, y) != TSML[x][y]:
            mismatches.append((x, y, T_tower(x, y), TSML[x][y]))
matches = R * R - len(mismatches)
print(f"  Matches: {matches}/100")
if mismatches:
    print("  MISMATCHES:")
    for x, y, got, want in mismatches:
        print(f"    T_tower({x},{y}) = {got}, TSML[{x}][{y}] = {want}")
    print("  THEOREM A FAILED.")
    sys.exit(1)
print("  THEOREM A: 100/100 verified.  PASS")

# =====================================================================
# STEP 2: verify the 92/6/2 decomposition (THEOREM_SPINE counts)
# =====================================================================
banner("STEP 2: Decomposition -- 92 (C0) + 6 (C1=MAX) + 2 (C2=ADD) = 100")
n_default, n_v0_zero, n_v0_excep, n_shell, n_C1, n_C2 = 0, 0, 0, 0, 0, 0
for x in range(R):
    for y in range(R):
        if (x, y) in S_MAX:
            n_C1 += 1
        elif (x, y) in S_ADD:
            n_C2 += 1
        else:
            # classify within C0 by which rule produced the *visible* value
            v_default = h
            v_after_v0 = v_default
            if x == 0 or y == 0:
                v_after_v0 = h if (x, y) in {(0, h), (h, 0)} else 0
            v_after_shell = v_after_v0
            if x in UNITS and y in UNITS and x != 1 and y != 1:
                sx, sy = shell(x), shell(y)
                if sx != sy:
                    v_after_shell = x if sx < sy else y
            # bucket: V0-zero / V0-exception / shell-stability / default
            if v_after_shell != v_after_v0:
                n_shell += 1
            elif v_after_v0 == 0 and v_default != 0:
                n_v0_zero += 1
            elif v_after_v0 == h and (x == 0 or y == 0):
                n_v0_excep += 1
            else:
                n_default += 1

n_C0 = n_default + n_v0_zero + n_v0_excep + n_shell
print(f"  C0 (canonical construction) breakdown:")
print(f"    DEFAULT (returns h={h})           : {n_default}")
print(f"    V0 zeros (x=0 or y=0, no excep.)  : {n_v0_zero}")
print(f"    V0 exceptions ((0,h) and (h,0))   : {n_v0_excep}")
print(f"    Shell-stability (visible override): {n_shell}")
print(f"    -- C0 total                       : {n_C0}")
print(f"  C1 (MAX rule on S_MAX)              : {n_C1}")
print(f"  C2 (ADD mod 10 on S_ADD)            : {n_C2}")
print(f"  GRAND TOTAL                         : {n_C0 + n_C1 + n_C2}")

assert n_C0 == 92, f"C0 count: expected 92, got {n_C0}"
assert n_C1 == 6, f"C1 count: expected 6, got {n_C1}"
assert n_C2 == 2, f"C2 count: expected 2, got {n_C2}"
assert n_default == 71, f"DEFAULT count: expected 71, got {n_default}"
assert n_v0_zero == 17, f"V0-zero count: expected 17, got {n_v0_zero}"
assert n_v0_excep == 2, f"V0-exception count: expected 2, got {n_v0_excep}"
assert n_shell == 2, f"Shell-stability count: expected 2, got {n_shell}"
print("  Decomposition 92/6/2 (with C0 = 71+17+2+2) verified.  PASS")

# =====================================================================
# STEP 3: Lemma 5 -- residue-of-residue is empty (tower terminates)
# =====================================================================
banner("STEP 3: Lemma 5 -- residue-of-residue is empty")
residue_of_residue = [
    (x, y) for x in range(R) for y in range(R)
    if T_tower(x, y) != TSML[x][y]
]
print(f"  |{{ (x,y) : T_tower(x,y) != TSML(x,y) }}| = {len(residue_of_residue)}")
assert len(residue_of_residue) == 0
print("  Tower terminates; no further layer needed.  PASS")

# =====================================================================
# STEP 4: Lemma 6 -- each layer is necessary
# =====================================================================
banner("STEP 4: Lemma 6 -- each of {C0, C1, C2} is necessary")


def T_without_C1(x, y):
    if (x, y) in S_ADD:
        return (x + y) % R
    return C0(x, y)


def T_without_C2(x, y):
    if (x, y) in S_MAX:
        return max(x, y)
    return C0(x, y)


def T_without_C0(x, y):
    if (x, y) in S_MAX:
        return max(x, y)
    if (x, y) in S_ADD:
        return (x + y) % R
    return None  # 92 entries unspecified


miss_no_C1 = [(x, y) for x in range(R) for y in range(R)
              if T_without_C1(x, y) != TSML[x][y]]
miss_no_C2 = [(x, y) for x in range(R) for y in range(R)
              if T_without_C2(x, y) != TSML[x][y]]
miss_no_C0 = [(x, y) for x in range(R) for y in range(R)
              if T_without_C0(x, y) is None or T_without_C0(x, y) != TSML[x][y]]

print(f"  Without C1 (MAX): {len(miss_no_C1)} mismatches.")
print(f"    Sample: {miss_no_C1[:6]}")
assert len(miss_no_C1) == 6  # exactly the S_MAX entries
print(f"  Without C2 (ADD): {len(miss_no_C2)} mismatches.")
print(f"    Sample: {miss_no_C2[:2]}")
assert len(miss_no_C2) == 2  # exactly the S_ADD entries
print(f"  Without C0:       {len(miss_no_C0)} mismatches/unspecified.")
assert len(miss_no_C0) == 92
print("  Each layer is necessary.  PASS")

# =====================================================================
# STEP 5: Disjointness (Lemma 1, 2)
# =====================================================================
banner("STEP 5: Lemmas 1-2 -- domain disjointness")
print(f"  S_MAX cap S_ADD = {S_MAX & S_ADD}")
assert S_MAX & S_ADD == set()
assert S_MAX | S_ADD == S
all_pairs = {(x, y) for x in range(R) for y in range(R)}
domain_C0 = all_pairs - S
print(f"  |R^2 \\ S| = {len(domain_C0)}, |S_MAX| = {len(S_MAX)}, |S_ADD| = {len(S_ADD)}")
assert len(domain_C0) == 92 and len(S_MAX) == 6 and len(S_ADD) == 2
print("  Three domains partition R^2 = Z/10Z x Z/10Z.  PASS")

banner("ALL CHECKS PASSED -- Sprint 17 Theorem A verified")
print("  TSML on Z/10Z = 3-layer canonical tower (92/6/2).")
print("  Residue-of-residue is empty; each layer is necessary.")
print("  Reference: Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/")
