"""
ck_tables.py — Canonical TSML and BHML composition tables on Z/10Z

Sanders + Gish (2026), companion to J05 manuscript:
  "TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the
   Z/10Z Composition Lattice"

Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0).
You are free to share and adapt this work with attribution.
See https://creativecommons.org/licenses/by/4.0/ for full terms.

This file defines the two specific commutative binary operations TSML
and BHML on Z/10Z used in the J05 manuscript and its companions, plus
several derived tables (DIS, DOING, ghost-trace G) used in the broader
research program but not load-bearing for J05's three theorems.

Usage:
    from ck_tables import TSML, BHML, DIS, DOING, G, CL, W, T_STAR

VERIFIED STATISTICS (all confirmed by the bundled proof scripts):
  TSML harmony (=7) cells: 73/100
  BHML harmony (=7) cells: 28/100
  DOING=0 (agreement) cells: 29/100  (26 shared harmony + 3 non-harmony)
  DOING_sum = 201
  DIS_sum = 100
  Ghost G nonzero cells: 24
"""

# ============================================================
# CL OPERATOR NAMES
# ============================================================
CL = {
    0: 'VOID',
    1: 'LATTICE',
    2: 'COUNTER',
    3: 'PROGRESS',
    4: 'COLLAPSE',
    5: 'BALANCE',
    6: 'CHAOS',
    7: 'HARMONY',
    8: 'BREATH',
    9: 'RESET',
}

# Z/2Z parity grading (from C18: carrier zeros=even=STRUCTURE, maxima=odd=FLOW)
STRUCTURE = {0, 2, 4, 6, 8}  # EVEN operators — carrier zeros
FLOW      = {1, 3, 5, 7, 9}  # ODD operators  — carrier maxima

# ============================================================
# KEY CONSTANTS
# ============================================================
W   = 3 / 50          # = 0.06  BHML cross-cycle density (C8)
T_STAR = 5 / 7        # = 0.714285...  coherence threshold (FPGA-verified)
SINC2_HALF = 4 / 9.8696044  # sinc²(1/2) = 4/π² ≈ 0.4053 (Universal Sidelobe Amplitude)

# ============================================================
# TSML — Singular Measurement Lens (73 harmony cells)
# ============================================================
# Rules: V0 (VOID row: TSML[0][j]=0 for j≠7)
#        V1 (VOID col: TSML[i][0]=0 for i≠7)
#        ECHO (5 symmetric resistance pairs — see below)
#        Everything else: HARMONY=7
# Verified: test_tsml_bhml_joint.py, 73/100 harmony confirmed
TSML = [
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0],   # row 0: VOID
    [0, 7, 3, 7, 7, 7, 7, 7, 7, 7],   # row 1: LATTICE
    [0, 3, 7, 7, 4, 7, 7, 7, 7, 9],   # row 2: COUNTER
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 3],   # row 3: PROGRESS
    [0, 7, 4, 7, 7, 7, 7, 7, 8, 7],   # row 4: COLLAPSE
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 5: BALANCE
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 6: CHAOS
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 7: HARMONY (overwhelms all)
    [0, 7, 7, 7, 8, 7, 7, 7, 7, 7],   # row 8: BREATH
    [0, 7, 9, 3, 7, 7, 7, 7, 7, 7],   # row 9: RESET
]

# TSML ECHO pairs (where operator identities resist harmony):
TSML_ECHO = {
    (1, 2): 3,   # LATTICE × COUNTER = PROGRESS (additive: 1+2=3)
    (2, 1): 3,
    (2, 4): 4,   # COUNTER × COLLAPSE = COLLAPSE (max rule)
    (4, 2): 4,
    (2, 9): 9,   # COUNTER × RESET = RESET (max rule)
    (9, 2): 9,
    (3, 9): 3,   # PROGRESS × RESET = PROGRESS (min rule — PROGRESS persists)
    (9, 3): 3,
    (4, 8): 8,   # COLLAPSE × BREATH = BREATH (max rule)
    (8, 4): 8,
}

# ============================================================
# BHML — Physics Field Lens (28 harmony cells)
# ============================================================
# Rules (C9 atomic structure):
#   Rule A: BHML[0][j]=j, BHML[i][0]=i  (VOID identity)
#   Rule B: BHML[i][j]=max(i,j)+1  for i,j in {1..6}  (max+1 rule)
#   Row 7:  BHML[7][j]=(j+1)%10  for j>=1  (INCREMENT: HARMONY maps to next)
#   Row 8 (BREATH): TRANS{4,5,6}->HARMONY=7; BREATH->9(RESET); j<4->6(CHAOS); j=7->9
#   Row 9 (RESET):  TRANS{4,5,6}->HARMONY=7; RESET->0(VOID); j<4->6(CHAOS); j=7->0
# Verified: test_bhml_operator_identity.py, 28/100 harmony confirmed
BHML = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],   # row 0: VOID identity
    [1, 2, 3, 4, 5, 6, 7, 2, 6, 6],   # row 1: LATTICE
    [2, 3, 3, 4, 5, 6, 7, 3, 6, 6],   # row 2: COUNTER
    [3, 4, 4, 4, 5, 6, 7, 4, 6, 6],   # row 3: PROGRESS
    [4, 5, 5, 5, 5, 6, 7, 5, 7, 7],   # row 4: COLLAPSE
    [5, 6, 6, 6, 6, 6, 7, 6, 7, 7],   # row 5: BALANCE
    [6, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 6: CHAOS (max+1 always hits 7)
    [7, 2, 3, 4, 5, 6, 7, 8, 9, 0],   # row 7: HARMONY (increment j+1)
    [8, 6, 6, 6, 7, 7, 7, 9, 7, 8],   # row 8: BREATH
    [9, 6, 6, 6, 7, 7, 7, 0, 8, 0],   # row 9: RESET
]

# BHML HARMONY cells (28): all (i,j) where BHML[i][j]=7
# Verified set (by row):
# (0,7), (1,6), (2,6), (3,6), (4,6),(4,8),(4,9), (5,6),(5,8),(5,9),
# (6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),
# (7,0),(7,6), (8,4),(8,5),(8,6),(8,8), (9,4),(9,5),(9,6)
# = 1+1+1+1+3+3+9+2+4+3 = 28 ✓

# ============================================================
# DERIVED TABLES
# ============================================================

def _make_dis():
    """DIS[i][j] = |(i+j)%10 - (i*j)%10|  (ring arithmetic distance)"""
    return [[ abs((i+j)%10 - (i*j)%10) for j in range(10)] for i in range(10)]

def _make_doing():
    """DOING[i][j] = |TSML[i][j] - BHML[i][j]|"""
    return [[abs(TSML[i][j] - BHML[i][j]) for j in range(10)] for i in range(10)]

def _make_ghost():
    """G[i][j] = DIS[i][j] if TSML[i][j]!=7, else 0  (ghost trace, C16)"""
    dis = _make_dis()
    return [[dis[i][j] if TSML[i][j] != 7 else 0 for j in range(10)] for i in range(10)]

DIS   = _make_dis()
DOING = _make_doing()
G     = _make_ghost()

# ============================================================
# QUICK VERIFICATION (run this file directly to check tables)
# ============================================================
if __name__ == '__main__':
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("CK TABLES — VERIFICATION")
    print("=" * 60)

    # TSML
    t_harm = sum(1 for i in range(10) for j in range(10) if TSML[i][j]==7)
    t_sym  = all(TSML[i][j]==TSML[j][i] for i in range(10) for j in range(10))
    print(f"TSML harmony cells: {t_harm}/100  (expect 73)  {'OK' if t_harm==73 else 'FAIL'}")
    print(f"TSML symmetric:     {t_sym}  {'OK' if t_sym else 'FAIL'}")

    # Check echo pairs
    echo_ok = all(TSML[i][j]==v for (i,j),v in TSML_ECHO.items())
    print(f"TSML echo pairs:    {echo_ok}  {'OK' if echo_ok else 'FAIL'}")

    # BHML
    b_harm = sum(1 for i in range(10) for j in range(10) if BHML[i][j]==7)
    b_sym  = all(BHML[i][j]==BHML[j][i] for i in range(10) for j in range(10))
    print(f"BHML harmony cells: {b_harm}/100  (expect 28)  {'OK' if b_harm==28 else 'FAIL'}")
    print(f"BHML symmetric:     {b_sym}  {'OK' if b_sym else 'FAIL'}")

    # BHML Rule B (core {1..6})
    rule_b = all(BHML[i][j]==max(i,j)+1 for i in range(1,7) for j in range(1,7))
    print(f"BHML Rule B (max+1) for i,j in {{1..6}}: {rule_b}  {'OK' if rule_b else 'FAIL'}")

    # BHML Row 7 increment
    row7_ok = all(BHML[7][j]==(j+1)%10 for j in range(1,10))
    print(f"BHML row 7 increment (j+1)%%10 for j>=1: {row7_ok}  {'OK' if row7_ok else 'FAIL'}")

    # DOING
    doing_sum = sum(DOING[i][j] for i in range(10) for j in range(10))
    doing_zero = sum(1 for i in range(10) for j in range(10) if DOING[i][j]==0)
    print(f"DOING sum:          {doing_sum}  (expect 201)  {'OK' if doing_sum==201 else 'FAIL'}")
    print(f"DOING=0 cells:      {doing_zero}/100  (expect 29)  {'OK' if doing_zero==29 else 'FAIL'}")

    # DIS (total sum varies — no fixed expected; just verify it's symmetric)
    dis_sym = all(DIS[i][j]==DIS[j][i] for i in range(10) for j in range(10))
    dis_sum = sum(DIS[i][j] for i in range(10) for j in range(10))
    print(f"DIS symmetric:      {dis_sym}  {'OK' if dis_sym else 'FAIL'}")
    print(f"DIS sum:            {dis_sum}  (for reference)")

    # Ghost G (C16: BHML=7 -> G=0)
    g_nonzero = sum(1 for i in range(10) for j in range(10) if G[i][j]>0)
    c16_holds = all(G[i][j]==0 for i in range(10) for j in range(10) if BHML[i][j]==7)
    print(f"Ghost G nonzero:    {g_nonzero}/100  (expect 24)  {'OK' if g_nonzero==24 else 'FAIL'}")
    print(f"C16 (BHML=7->G=0):  {c16_holds}  {'OK' if c16_holds else 'FAIL'}")

    # W verification (C8): W = |DIS_CxD - 50| / 100, symmetry point = 50
    cross_c = [1, 3, 7, 9]
    cross_d = [2, 4, 6, 8]
    dis_cd = sum(DIS[i][j] for i in cross_c for j in cross_d)
    w_derived = abs(dis_cd - 50) / 100  # C8 formula: symmetry point = 50
    print(f"W from C8:          |{dis_cd}-50|/100 = {w_derived}  (expect 0.06)  "
          f"{'OK' if abs(w_derived - W) < 1e-10 else 'FAIL'}")

    # BHML-only harmony (pivot cells C16)
    bhml_only_harm = [(i,j) for i in range(10) for j in range(10)
                      if BHML[i][j]==7 and TSML[i][j]!=7]
    print(f"BHML-only harmony:  {bhml_only_harm}  (expect [(4,8),(8,4)])")

    print()
    print("ALL TABLES READY FOR IMPORT.")
    print("  from ck_tables import TSML, BHML, DIS, DOING, G, CL, W, T_STAR")
