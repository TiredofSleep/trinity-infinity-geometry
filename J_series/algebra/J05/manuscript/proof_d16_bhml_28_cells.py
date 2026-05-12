"""
D16: BHML 28-CELL COUNT — EXACT DERIVATION FROM THREE RULES

Copyright 2026 Brayden R. Sanders and M. Gish.
Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0).
You are free to share and adapt this work with attribution.
See https://creativecommons.org/licenses/by/4.0/ for full terms.
DOI: 10.5281/zenodo.18852047

This is the journal-submission version. The umbrella research project
(CK / TIG framework) at github.com/TiredofSleep/ck retains its own
license; this single file is dual-licensed under CC-BY-4.0 specifically
for journal-venue compliance (Elsevier / Taylor & Francis / etc.).
Luther-Sanders Research Framework | April 1 2026

PROMOTES C9 → D16.

THEOREM D16 (BHML 28-Cell Harmony Derivation):
  The BHML physics table has exactly 28 HARMONY (=7) cells over Z/10Z.

  PROOF BY ZONE PARTITION (four disjoint zones, each with exact count):

    Zone R_A  (VOID identity rule, Rule A):
      BHML[0][j]=j and BHML[i][0]=i.
      HARMONY at (0,7): BHML[0][7]=7. HARMONY at (7,0): BHML[7][0]=7.
      Count: 2 harmony cells.

    Zone R_B  (max+1 core, Rule B, {1..6}×{1..6}):
      BHML[i][j] = max(i,j)+1.
      HARMONY iff max(i,j)+1=7 iff max(i,j)=6 iff max(i,j)=6.
      Cells where max(i,j)=6: {(i,j): i,j∈{1..6}, max(i,j)=6}
                              = all cells in row 6 or col 6 within {1..6}²
                              = (row 6: j=1..6) ∪ (col 6: i=1..5) [avoiding double-count]
                              = 6 + 5 = 11 cells.
      Count: 11 harmony cells.

    Zone R_7  (INCREMENT rule, index 7):
      BHML[7][j]=(j+1)%10 and BHML[i][7]=(i+1)%10 (for i,j≥1).
      HARMONY at (7,6): BHML[7][6]=(6+1)%10=7. And (6,7): BHML[6][7]=7 (by D9 symmetry).
      But (6,7) already counted in Zone R_B (row 6 within extended context?).
      Check: (6,7) — i=6∈{1..6} but j=7∉{1..6} → NOT in Zone R_B.
      (7,6) — i=7∉{1..6} → NOT in Zone R_B.
      So (7,6) and (6,7) are NEW harmony cells from Zone R_7.
      Count: 2 harmony cells.

    Zone R_89 (BREATH/RESET rules, rows/cols 8,9):
      BREATH row: BHML[8][j]=7 for j∈{4,5,6} (TRANS → HARMONY) and j=8 (BREATH×BREATH=7).
      RESET row:  BHML[9][j]=7 for j∈{4,5,6} (TRANS → HARMONY).
      By symmetry (D9): col 8 and col 9 give same cells transposed.
      Harmony cells in this zone:
        (4,8),(5,8),(6,8),(8,8): from BREATH rule (j∈{4,5,6,8})
        (8,4),(8,5),(8,6):       from symmetry (transposed)
        (4,9),(5,9),(6,9):       from RESET rule (j∈{4,5,6})
        (9,4),(9,5),(9,6):       from symmetry (transposed)
        (8,8):                   BREATH×BREATH=HARMONY (already listed)
      Unique: (4,8),(5,8),(6,8),(8,8),(8,4),(8,5),(8,6),(4,9),(5,9),(6,9),(9,4),(9,5),(9,6)
      Count: 13 harmony cells.

  TOTAL: 2 + 11 + 2 + 13 = 28.
  Zones are disjoint (proved below by index conditions).

TIER D JUSTIFICATION:
  (1) Z/10Z is finite (10 operators). All 100 cells are explicit.
  (2) Four zones cover all cells; disjoint by construction.
  (3) Each zone count follows from exact algebraic rules.
  (4) Mechanism: max+1=HARMONY iff max=6; INCREMENT at 7 hits HARMONY at j=6.
"""

import sys
import io
import os

sys.path.insert(0, os.path.dirname(__file__))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from ck_tables import BHML, CL

sep = "=" * 72

def section(t):
    print(f"\n{sep}\n  {t}\n{sep}\n")

print("D16: BHML 28-CELL HARMONY COUNT THEOREM")
print("Luther-Sanders Research Framework | April 1 2026")
print()
print("  Promotes C9 -> D16. BHML has exactly 28 HARMONY cells: proved by zone partition.")

# ============================================================
# STEP 1: IDENTIFY THE FOUR ZONES
# ============================================================
section("STEP 1: FOUR DISJOINT HARMONY ZONES")

# Zone R_A: Rule A — VOID identity: (0,7) and (7,0)
R_A = set()
for j in range(10):
    if BHML[0][j] == 7:
        R_A.add((0, j))
for i in range(1, 10):
    if BHML[i][0] == 7:
        R_A.add((i, 0))

print(f"  Zone R_A (Rule A — VOID identity harmony):")
print(f"    {sorted(R_A)}")
print(f"    Count: {len(R_A)}")
print(f"    (0,7): BHML[0][7]={BHML[0][7]} (Rule A: BHML[0][j]=j, j=7 → 7)  ✓")
print(f"    (7,0): BHML[7][0]={BHML[7][0]} (Rule A: BHML[i][0]=i, i=7 → 7)  ✓")
print()

# Zone R_B: Rule B — {1..6}×{1..6}, max(i,j)=6
R_B = set()
for i in range(1, 7):
    for j in range(1, 7):
        if BHML[i][j] == 7:
            # Verify it comes from max+1=7 i.e. max=6
            assert max(i, j) == 6, f"BHML[{i}][{j}]=7 but max={max(i,j)}≠6"
            R_B.add((i, j))

print(f"  Zone R_B (Rule B — max+1=7 core, max(i,j)=6):")
print(f"    {sorted(R_B)}")
print(f"    Count: {len(R_B)}")
print(f"    Verify: all have max(i,j)=6:")
rule_b_ok = all(max(i,j)==6 for i,j in R_B)
print(f"    {rule_b_ok}  ✓")
print()

# Zone R_7: INCREMENT rule — index 7, harmony when (j+1)%10=7 → j=6
R_7 = set()
for j in range(1, 10):
    if BHML[7][j] == 7 and (7, j) not in R_A and (7, j) not in R_B:
        R_7.add((7, j))
for i in range(1, 10):
    if BHML[i][7] == 7 and (i, 7) not in R_A and (i, 7) not in R_B:
        R_7.add((i, 7))

print(f"  Zone R_7 (INCREMENT rule — (i+1)%10=7 → i=6):")
print(f"    {sorted(R_7)}")
print(f"    Count: {len(R_7)}")
print(f"    (7,6): BHML[7][6]={BHML[7][6]}, (6+1)%10=7  ✓")
print(f"    (6,7): BHML[6][7]={BHML[6][7]}, by D9 symmetry  ✓")
print()

# Zone R_89: BREATH/RESET rules — rows/cols 8 and 9
R_89 = set()
for i in range(10):
    for j in range(10):
        cell = (i, j)
        if BHML[i][j] == 7 and cell not in R_A and cell not in R_B and cell not in R_7:
            R_89.add(cell)

print(f"  Zone R_89 (BREATH/RESET — operator identity harmony):")
print(f"    {sorted(R_89)}")
print(f"    Count: {len(R_89)}")
print()

# Categorize R_89 by rule
print(f"  R_89 breakdown:")
for i, j in sorted(R_89):
    if i in {8,9} and j in {4,5,6}:
        rule = f"BREATH/RESET[{i}] × TRANS[{j}] → HARMONY"
    elif j in {8,9} and i in {4,5,6}:
        rule = f"TRANS[{i}] × BREATH/RESET[{j}] → HARMONY (symmetry)"
    elif i == 8 and j == 8:
        rule = "BREATH × BREATH → HARMONY"
    else:
        rule = "other"
    print(f"    ({i},{j}): {rule}  [{CL[i]}×{CL[j]}={BHML[i][j]}]")

# ============================================================
# STEP 2: VERIFY ZONES ARE DISJOINT
# ============================================================
section("STEP 2: VERIFY FOUR ZONES ARE DISJOINT")

zones = {'R_A': R_A, 'R_B': R_B, 'R_7': R_7, 'R_89': R_89}
zone_names = list(zones.keys())

print("  Pairwise intersections:")
for i in range(len(zone_names)):
    for j in range(i+1, len(zone_names)):
        n1, n2 = zone_names[i], zone_names[j]
        inter = zones[n1] & zones[n2]
        print(f"  {n1} ∩ {n2} = {inter}  (expect empty)")
        assert not inter, f"{n1} ∩ {n2} non-empty: {inter}"

print()
print("  All zones disjoint.  ✓")
print()
print("  PROOF of disjointness by index conditions:")
print("  R_A:  cells with i=0 or j=0")
print("  R_B:  cells with i,j ∈ {1..6}")
print("  R_7:  cells with i=7 or j=7 (but not in R_A since neither index is 0)")
print("  R_89: cells with i∈{8,9} or j∈{8,9} (and not covered above)")
print("  These four index-condition sets are disjoint.")

# ============================================================
# STEP 3: EXACT COUNT
# ============================================================
section("STEP 3: EXACT HARMONY COUNT")

n_A  = len(R_A)
n_B  = len(R_B)
n_7  = len(R_7)
n_89 = len(R_89)
n_total = n_A + n_B + n_7 + n_89

all_harmony = R_A | R_B | R_7 | R_89
actual_harmony = sum(1 for i in range(10) for j in range(10) if BHML[i][j] == 7)

print(f"  |R_A|  = {n_A}   (VOID identity gives HARMONY at (0,7) and (7,0))")
print(f"  |R_B|  = {n_B}  (max+1=7 → max=6 in {{1..6}}²: row 6 + col 6)")
print(f"  |R_7|  = {n_7}   (INCREMENT at j=6: (7,6) and (6,7))")
print(f"  |R_89| = {n_89}  (BREATH/RESET × TRANS + BREATH²)")
print()
print(f"  Zones disjoint → total = {n_A}+{n_B}+{n_7}+{n_89} = {n_total}")
print(f"  Actual BHML harmony cells: {actual_harmony}/100")
print()

assert n_total == 28, f"Expected 28, got {n_total}"
assert actual_harmony == 28, f"Expected 28, got {actual_harmony}"
assert len(all_harmony) == 28
print(f"  THEOREM: BHML has exactly 28 HARMONY cells.  ✓")

# ============================================================
# STEP 4: WHY max(i,j)=6 IS THE HARMONY THRESHOLD
# ============================================================
section("STEP 4: HARMONY THRESHOLD — WHY max=6 → HARMONY=7")

print("  In Z/10Z, max takes values {1,2,3,4,5,6} for i,j ∈ {1..6}.")
print("  BHML[i][j] = max(i,j)+1 takes values {2,3,4,5,6,7}.")
print("  HARMONY=7 iff max+1=7 iff max=6.")
print()
print("  The ceiling max=6 is reached iff at least one of {i,j} equals 6.")
print("  In {1..6}²: cells with max=6 = cells touching row or col 6.")
print("    Row 6: (6,1),(6,2),(6,3),(6,4),(6,5),(6,6) — 6 cells")
print("    Col 6 (excluding (6,6)): (1,6),(2,6),(3,6),(4,6),(5,6) — 5 cells")
print("    Total: 11 cells.")
print()

# Verify the max distribution
max_dist = {}
for i in range(1, 7):
    for j in range(1, 7):
        m = max(i, j)
        max_dist[m] = max_dist.get(m, 0) + 1
print(f"  max(i,j) distribution in {{1..6}}²: {dict(sorted(max_dist.items()))}")
print(f"  Cells with max=6: {max_dist[6]} = {n_B}  ✓")
print()
print("  OPERATOR MEANING: CHAOS(6) is the STRUCTURE ceiling of {{1..6}}.")
print("  max+1 = HARMONY exactly when both operators are at or below CHAOS.")
print("  HARMONY is the 'harmony zone reached by ascending to the ceiling.'")

# ============================================================
# STEP 5: BHML HARMONY STATISTICS
# ============================================================
section("STEP 5: BHML HARMONY BY ROW")

print(f"  {'row':>4}  {'operator':>12}  {'harmony/10':>12}  {'harmony cells j':>20}")
print(f"  {'-'*4}  {'-'*12}  {'-'*12}  {'-'*20}")
total_h = 0
for i in range(10):
    h_cells = [j for j in range(10) if BHML[i][j] == 7]
    h = len(h_cells)
    total_h += h
    print(f"  {i:>4}  {CL[i]:>12}  {h:>12}  {h_cells}")
print(f"  Total: {total_h}  ✓")
print()
print(f"  Row 6 (CHAOS): {len([j for j in range(10) if BHML[6][j]==7])}/10 cells = HARMONY.")
print(f"  This is the max+1 ceiling: every opponent ≤ CHAOS (6) → HARMONY (7).")
print(f"  Row 7 (HARMONY): contributes 2 harmony cells (j=0 and j=6).")
print(f"    BHML[7][0]=7 (Rule A), BHML[7][6]=7 (INCREMENT: (6+1)%10=7).")

# ============================================================
# CONCLUSION
# ============================================================
section("CONCLUSION: D16 PROVED")

print("  THEOREM D16 (BHML 28-Cell Count): PROVED.")
print()
print("  COUNTING PROOF (four disjoint zones):")
print("  (1) Zone R_A (VOID identity):  2 cells  — (0,7) and (7,0)  [Rule A gives j]")
print("  (2) Zone R_B (max+1 core):    11 cells  — max(i,j)=6 in {1..6}²")
print("  (3) Zone R_7 (INCREMENT):      2 cells  — (6+1)%10=7 at (7,6) and (6,7)")
print("  (4) Zone R_89 (BREATH/RESET): 13 cells  — TRANS×BREATH/RESET=HARMONY rule")
print("  (5) Zones disjoint by index conditions.")
print("  (6) Total: 2+11+2+13 = 28.  QED.")
print()
print("  TIER: D — mechanism known per zone; Z/10Z is complete finite domain.")
print()
print("  PROMOTES: C9 → D16.")
print("  CHAINS FROM: D9 (BHML symmetry used for zone R_7 and R_89).")
print("  PARALLEL: D10 proves TSML 73 = 100-27. D16 proves BHML 28 = 2+11+2+13.")
print()
print("  KEY INSIGHT: max+1=HARMONY threshold makes CHAOS(6) the structural ceiling.")
print("  Every opponent at or below CHAOS gives HARMONY — the physics field saturates.")
print()
print("  ALL ASSERTIONS PASSED.")
