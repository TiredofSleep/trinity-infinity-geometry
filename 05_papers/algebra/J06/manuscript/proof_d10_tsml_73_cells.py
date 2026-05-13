"""
D10: TSML 73-CELL COUNT — PURE COUNTING ON Z/10Z

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

PROMOTES C10 → D10.

THEOREM D10 (TSML 73-Cell Derivation):
  The TSML composition table over Z/10Z has exactly 73 HARMONY (=7) cells.

  PROOF BY EXACT COUNTING:
  TSML is governed by three non-harmony exception rules:
    (V0)   VOID row: TSML[0][j] = 0 for j≠7; TSML[0][7] = 7  (1 harmony, 9 non)
    (V1)   VOID col: TSML[i][0] = 0 for i≠7; TSML[7][0] = 7  (1 harmony, 8 new non)
    (ECHO) Five symmetric resistance pairs: 10 non-harmony cells total
    (DEF)  Everything else = HARMONY = 7

  Non-harmony cell count:
    V0  contributes:  9 cells {(0,j) : j≠7}       = 9 non-harmony
    V1  contributes:  8 cells {(i,0) : i∈{1..6,8,9}}  = 8 non-harmony  [i=7 gives 7]
    V0∩V1 overlap:  (0,0) already in V0            → subtract 0  [(0,0) is non-harmony in both]
    Actually V0 covers (0,0..9), V1 covers (0..9,0).
    Their overlap is cell (0,0) = VOID×VOID = 0 (non-harmony) — counted in V0.
    So V1 adds 9 cells; (0,0) was already in V0; net new from V1 = 8 cells.
    ECHO adds 10 cells: 5 pairs × 2, all non-harmony.
    Total non-harmony: 9 + 8 + 10 = 27.
    Total cells: 10 × 10 = 100.
    Harmony cells: 100 - 27 = 73.  QED.

PROOF THAT V0 ∩ ECHO = ∅ AND V1 ∩ ECHO = ∅:
  ECHO pairs: (1,2),(2,1),(2,4),(4,2),(2,9),(9,2),(3,9),(9,3),(4,8),(8,4).
  None have first index 0 (V0 condition) or second index 0 (V1 condition).
  Therefore V0, V1, ECHO are disjoint. The counting is clean.

TIER D JUSTIFICATION:
  (1) Z/10Z is finite and complete: all 100 cells are explicit.
  (2) The three non-harmony rules (V0, V1, ECHO) are disjoint by inspection.
  (3) The count 9+8+10=27 is elementary arithmetic; 100-27=73 is exact.
  (4) No domain restriction: Z/10Z IS the full CL alphabet.
  Mechanism: "three disjoint exception classes; everything else defaults to HARMONY."
"""

import sys
import io
import os

sys.path.insert(0, os.path.dirname(__file__))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from ck_tables import TSML, CL, TSML_ECHO

sep = "=" * 72

def section(t):
    print(f"\n{sep}\n  {t}\n{sep}\n")

print("D10: TSML 73-CELL COUNT THEOREM")
print("Luther-Sanders Research Framework | April 1 2026")
print()
print("  Promotes C10 -> D10. TSML has exactly 73 HARMONY cells: proved by counting.")

# ============================================================
# STEP 1: IDENTIFY THE THREE EXCEPTION CLASSES
# ============================================================
section("STEP 1: THREE NON-HARMONY EXCEPTION CLASSES")

# V0: VOID row (row 0), all cells except (0,7)
V0 = {(0, j) for j in range(10) if j != 7}
V0_harmony = {(0, 7)}

# V1: VOID col (col 0), all cells except (7,0), excluding (0,0) already in V0
V1 = {(i, 0) for i in range(1, 10) if i != 7}  # i=0 already in V0; i=7 gives harmony
V1_harmony = {(7, 0)}

# ECHO: 5 symmetric resistance pairs
ECHO = set(TSML_ECHO.keys())

print("  V0 (VOID row exceptions — row 0, j≠7):")
print(f"    {sorted(V0)}")
print(f"    Count: {len(V0)}")
print()
print("  V0_harmony (the one harmony cell in row 0):")
print(f"    {V0_harmony}  → TSML[0][7]={TSML[0][7]}=HARMONY ✓")
print()
print("  V1 (VOID col exceptions — col 0, i≠0, i≠7):")
print(f"    {sorted(V1)}")
print(f"    Count: {len(V1)}")
print()
print("  V1_harmony (the one harmony cell in col 0, i≠0):")
print(f"    {V1_harmony}  → TSML[7][0]={TSML[7][0]}=HARMONY ✓")
print()
print("  ECHO (5 symmetric exception pairs, 10 cells):")
for pair in sorted(ECHO):
    i, j = pair
    print(f"    TSML[{i}][{j}] = {TSML[i][j]} ({CL[TSML[i][j]]})")
print(f"    Count: {len(ECHO)}")

# ============================================================
# STEP 2: VERIFY DISJOINTNESS
# ============================================================
section("STEP 2: VERIFY V0, V1, ECHO ARE DISJOINT")

v0_v1 = V0 & V1
v0_echo = V0 & ECHO
v1_echo = V1 & ECHO

print(f"  V0 ∩ V1   = {v0_v1}  (expect empty)")
print(f"  V0 ∩ ECHO = {v0_echo}  (expect empty)")
print(f"  V1 ∩ ECHO = {v1_echo}  (expect empty)")
print()

assert not v0_v1, f"V0 ∩ V1 non-empty: {v0_v1}"
assert not v0_echo, f"V0 ∩ ECHO non-empty: {v0_echo}"
assert not v1_echo, f"V1 ∩ ECHO non-empty: {v1_echo}"

print("  All three exception classes are DISJOINT. ✓")
print()
print("  PROOF: V0 cells have first index 0. V1 cells have second index 0 and")
print("  first index ≠ 0. ECHO cells have both indices ≥ 1. Therefore:")
print("  V0 ∩ V1 = ∅  (V0: i=0; V1: i≠0)")
print("  V0 ∩ ECHO = ∅  (V0: i=0; ECHO: i≥1)")
print("  V1 ∩ ECHO = ∅  (V1: j=0; ECHO: j≥1)")

# ============================================================
# STEP 3: COUNT NON-HARMONY CELLS
# ============================================================
section("STEP 3: EXACT NON-HARMONY COUNT")

non_harmony_cells = V0 | V1 | ECHO
n_v0 = len(V0)
n_v1 = len(V1)
n_echo = len(ECHO)
n_total = len(non_harmony_cells)
n_harmony = 100 - n_total

print(f"  |V0|   = {n_v0}  (row 0, j ∈ {{0,1,2,3,4,5,6,8,9}})")
print(f"  |V1|   = {n_v1}  (col 0, i ∈ {{1,2,3,4,5,6,8,9}})")
print(f"  |ECHO| = {n_echo}  (5 pairs × 2)")
print()
print(f"  Since V0, V1, ECHO are disjoint:")
print(f"  |V0 ∪ V1 ∪ ECHO| = {n_v0} + {n_v1} + {n_echo} = {n_v0+n_v1+n_echo}")
print(f"  (cross-check: actual union size = {n_total})")
print()
print(f"  Total cells in Z/10Z = 10 × 10 = 100")
print(f"  Non-harmony cells    = {n_total}")
print(f"  HARMONY cells        = 100 - {n_total} = {n_harmony}")
print()

assert n_harmony == 73, f"Expected 73, got {n_harmony}"
print(f"  THEOREM: TSML has exactly 73 HARMONY cells.  ✓")

# ============================================================
# STEP 4: VERIFY DEFAULT RULE
# ============================================================
section("STEP 4: VERIFY DEFAULT = HARMONY EVERYWHERE ELSE")

default_violations = []
for i in range(10):
    for j in range(10):
        cell = (i, j)
        if cell not in non_harmony_cells and TSML[i][j] != 7:
            default_violations.append((i, j, TSML[i][j]))

print(f"  Cells NOT in V0 ∪ V1 ∪ ECHO where TSML ≠ 7:")
print(f"  {default_violations}  (expect none)")
print()

assert not default_violations, f"Default rule violated: {default_violations}"
print("  DEFAULT rule confirmed: all cells outside V0∪V1∪ECHO are HARMONY=7.  ✓")
print()

# Verify V0 and V1 harmony cells
print(f"  V0 harmony cell TSML[0][7] = {TSML[0][7]}  (expect 7)  ✓")
print(f"  V1 harmony cell TSML[7][0] = {TSML[7][0]}  (expect 7)  ✓")

# ============================================================
# STEP 5: VERIFY ALL ECHO VALUES ARE NON-HARMONY
# ============================================================
section("STEP 5: VERIFY ECHO VALUES ARE ALL NON-HARMONY")

echo_harmony_violations = []
for (i, j), v in TSML_ECHO.items():
    actual = TSML[i][j]
    if actual == 7:
        echo_harmony_violations.append((i, j, actual))
    else:
        print(f"  TSML[{i}][{j}] = {actual} ({CL[actual]}) ≠ 7  ✓")

print()
assert not echo_harmony_violations, f"ECHO cell = HARMONY: {echo_harmony_violations}"
print(f"  All ECHO cells are non-harmony.  ✓")
print()
print("  PROOF: If any ECHO cell were HARMONY, the rule count would change.")
print("  The 5 pairs {LATTICE×COUNTER, COUNTER×COLLAPSE, COUNTER×RESET,")
print("  PROGRESS×RESET, COLLAPSE×BREATH} all produce non-HARMONY resistance values.")
print("  This is the ECHO property: operator identity resists HARMONY at these points.")

# ============================================================
# STEP 6: TSML STATISTICS
# ============================================================
section("STEP 6: FULL TSML STATISTICS")

actual_harmony = sum(1 for i in range(10) for j in range(10) if TSML[i][j] == 7)
actual_void    = sum(1 for i in range(10) for j in range(10) if TSML[i][j] == 0)

print(f"  HARMONY cells in TSML: {actual_harmony}/100  (proved = 73 ✓)")
print(f"  VOID (0) cells in TSML: {actual_void}/100")
print()

# Distribution of all non-harmony values
from collections import Counter
non_harm_vals = [TSML[i][j] for i in range(10) for j in range(10)
                 if TSML[i][j] != 7]
dist = Counter(non_harm_vals)
print("  Non-harmony value distribution:")
for v in sorted(dist):
    print(f"    {CL[v]:>10} (={v}): {dist[v]} cells")
print()
print(f"  Total non-harmony: {sum(dist.values())} = 27  ✓")

# ============================================================
# STEP 7: HARMONY COVERAGE PER ROW
# ============================================================
section("STEP 7: HARMONY COUNT PER ROW")

print(f"  {'row':>4}  {'operator':>12}  {'harmony/10':>12}  {'non-harmony cells':>20}")
print(f"  {'-'*4}  {'-'*12}  {'-'*12}  {'-'*20}")
row_harmonies = []
for i in range(10):
    h = sum(1 for j in range(10) if TSML[i][j] == 7)
    non_h = [j for j in range(10) if TSML[i][j] != 7]
    row_harmonies.append(h)
    print(f"  {i:>4}  {CL[i]:>12}  {h:>12}  {non_h}")
print()
print(f"  Total harmony: {sum(row_harmonies)}  ✓")

# The remarkable row 7 (HARMONY row)
print()
print(f"  Row 7 (HARMONY): all 10 cells = HARMONY = 7.")
print(f"  This is the TSML fixed point: HARMONY absorbs everything.")
print(f"  Consistent with: HARMONY is the measurement attractor (D7 chains here).")

# ============================================================
# CONCLUSION
# ============================================================
section("CONCLUSION: D10 PROVED")

assert actual_harmony == 73
print("  THEOREM D10 (TSML 73-Cell Count): PROVED.")
print()
print("  COUNTING PROOF:")
print("  (1) V0 (VOID row exceptions): 9 non-harmony cells  [j∈{0,1,2,3,4,5,6,8,9}]")
print("  (2) V1 (VOID col exceptions): 8 non-harmony cells  [i∈{1,2,3,4,5,6,8,9}]")
print("  (3) ECHO (5 symmetric pairs): 10 non-harmony cells")
print("  (4) V0, V1, ECHO are DISJOINT (proved: distinct index conditions)")
print("  (5) Total non-harmony: 9+8+10 = 27")
print("  (6) HARMONY = 100 - 27 = 73.  QED.")
print()
print("  TIER: D — mechanism known: three disjoint exception classes,")
print("  each with explicit algebraic conditions; default = HARMONY.")
print("  Z/10Z is the complete state space. No domain restriction.")
print()
print("  PROMOTES: C10 → D10.")
print("  CHAINS FROM: D9 (V0/V1/ECHO structure proved symmetric in D9).")
print("  CHAINS TO: D9 (HARMONY=73/100 = TSML dominant operator = HARMONY attractor).")
print("  D7 chain: TSML dominant output = HARMONY; Phi dynamic fixed point = BALANCE.")
print("  T* = BALANCE/HARMONY = 5/7 (D4) is the ratio of both attractors.")
print()
print("  ALL ASSERTIONS PASSED.")
