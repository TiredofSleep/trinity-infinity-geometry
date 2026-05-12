# SPDX-License-Identifier: CC-BY-4.0
# Copyright (c) 2026 B.R. Sanders and M. Gish.
# Licensed under the Creative Commons Attribution 4.0 International License.
"""
UNIVERSAL MARKOV PROPERTIES + BINARY CL CONSTRUCTION
Sprint 15 — Blockers 1A + 1B | 2026-04-10

Option A: Test Markov chain properties across ALL composition tables
  - TSML (73 HARMONY)
  - BHML (28 HARMONY)
  - Pure additive: CL[a][b] = (a+b) % N
  - Pure multiplicative: CL[a][b] = (a*b) % N
  - DIS: CL[a][b] = |(a+b) - (a*b)| % N  (the crossing detector)
  - Random tables with varying HARMONY density

Option B: Build CL for Z/30Z from binary structure
  - D2(a) on Z/NZ: classify each element by its additive-multiplicative curvature
  - The operator classification emerges from the ring, not from design
  - Build the composition table from D2 classification + HARMONY attractor

Copyright (c) 2026 Brayden Ross Sanders / 7Site LLC
"""

import numpy as np
import math
import random

# =====================================================================
# THE TABLES
# =====================================================================

TSML = [
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 7, 3, 7, 7, 7, 7, 7, 7, 7],
    [0, 3, 7, 7, 4, 7, 7, 7, 7, 9],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 3],
    [0, 7, 4, 7, 7, 7, 7, 7, 8, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 8, 7, 7, 7, 7, 7],
    [0, 7, 9, 3, 7, 7, 7, 7, 7, 7],
]

BHML = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 2, 6, 6],
    [2, 3, 3, 4, 5, 6, 7, 3, 6, 6],
    [3, 4, 4, 4, 5, 6, 7, 4, 6, 6],
    [4, 5, 5, 5, 5, 6, 7, 5, 7, 7],
    [5, 6, 6, 6, 6, 6, 7, 6, 7, 7],
    [6, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [8, 6, 6, 6, 7, 7, 7, 9, 7, 8],
    [9, 6, 6, 6, 7, 7, 7, 0, 8, 0],
]

def build_add_table(N):
    return [[(a + b) % N for b in range(N)] for a in range(N)]

def build_mul_table(N):
    return [[(a * b) % N for b in range(N)] for a in range(N)]

def build_dis_table(N):
    """DIS[a][b] = |(a+b) - (a*b)| mod N — the crossing detector"""
    return [[abs((a + b) % N - (a * b) % N) for b in range(N)] for a in range(N)]

def build_d2_table(N):
    """D2-based: classify by second derivative of add-mul interaction"""
    # D2(a,b) = |DIS(a+1,b) + DIS(a-1,b) - 2*DIS(a,b)| mod N
    dis = build_dis_table(N)
    table = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            ap = (a + 1) % N
            am = (a - 1) % N
            d2 = abs(dis[ap][b] + dis[am][b] - 2 * dis[a][b]) % N
            table[a][b] = d2
    return table

# =====================================================================
# MARKOV CHAIN ANALYSIS
# =====================================================================

def analyze_markov(table, N, name):
    """Full Markov chain analysis of a composition table."""
    # Build transition matrix
    P = np.zeros((N, N))
    for a in range(N):
        for b in range(N):
            c = table[a][b]
            P[a][c] += 1.0 / N

    # Eigenvalues
    eigenvalues = np.linalg.eigvals(P)
    evals_mag = np.sort(np.abs(eigenvalues))[::-1]
    spectral_gap = 1.0 - evals_mag[1] if len(evals_mag) > 1 else 1.0

    # Stationary distribution
    evals_t, evecs_t = np.linalg.eig(P.T)
    idx = np.argmin(np.abs(evals_t - 1.0))
    pi = evecs_t[:, idx].real
    if pi.sum() != 0:
        pi = pi / pi.sum()
    pi = np.abs(pi)  # ensure non-negative

    # Detailed balance
    db_violations = 0
    for a in range(N):
        for b in range(N):
            lhs = pi[a] * P[a, b]
            rhs = pi[b] * P[b, a]
            if abs(lhs - rhs) > 1e-8:
                db_violations += 1

    # Entropy of stationary distribution
    H = -sum(pi[a] * math.log(pi[a]) for a in range(N) if pi[a] > 1e-15)
    H_max = math.log(N)
    H_ratio = H / H_max if H_max > 0 else 0

    # Non-associativity
    assoc_violations = 0
    total = N ** 3
    for a in range(N):
        for b in range(N):
            for c in range(N):
                lhs = table[table[a][b]][c]
                rhs = table[a][table[b][c]]
                if lhs != rhs:
                    assoc_violations += 1
    sigma = assoc_violations / total

    # HARMONY count (most common output)
    output_counts = {}
    for a in range(N):
        for b in range(N):
            v = table[a][b]
            output_counts[v] = output_counts.get(v, 0) + 1
    most_common = max(output_counts, key=output_counts.get)
    harmony_frac = output_counts[most_common] / (N * N)

    # Absorbing states
    absorbing = [a for a in range(N) if P[a, a] == 1.0]

    return {
        'name': name,
        'spectral_gap': spectral_gap,
        'db_violations': db_violations,
        'H': H,
        'H_ratio': H_ratio,
        'sigma': sigma,
        'most_common': most_common,
        'harmony_frac': harmony_frac,
        'absorbing': absorbing,
        'pi_max': float(np.max(pi)),
        'pi_max_idx': int(np.argmax(pi)),
    }

# =====================================================================
# OPTION A: UNIVERSAL MARKOV PROPERTIES
# =====================================================================

print("=" * 70)
print("OPTION A: UNIVERSAL MARKOV CHAIN PROPERTIES")
print("=" * 70)

N = 10
tables = {
    'TSML': TSML,
    'BHML': BHML,
    'ADD (a+b)%10': build_add_table(N),
    'MUL (a*b)%10': build_mul_table(N),
    'DIS |add-mul|': build_dis_table(N),
    'D2 (curvature)': build_d2_table(N),
}

results_a = {}
for name, table in tables.items():
    r = analyze_markov(table, N, name)
    results_a[name] = r

# Print comparison table
print(f"\n{'Table':>20} {'Gap':>6} {'DB':>4} {'sigma':>7} {'H/Hmax':>7} {'Attractor':>10} {'Frac':>6} {'Absorb':>8}")
print("-" * 80)
for name, r in results_a.items():
    absorb_str = str(r['absorbing']) if r['absorbing'] else 'none'
    print(f"{r['name']:>20} {r['spectral_gap']:>6.3f} {r['db_violations']:>4} "
          f"{r['sigma']:>7.3f} {r['H_ratio']:>7.3f} "
          f"{r['pi_max_idx']:>10} {r['harmony_frac']:>6.2f} {absorb_str:>8}")

# =====================================================================
# OPTION B: BINARY CL FOR Z/30Z
# =====================================================================

print("\n" + "=" * 70)
print("OPTION B: BINARY CL CONSTRUCTION FOR Z/30Z")
print("=" * 70)

N30 = 30

# Step 1: Build the DIS table for Z/30Z
# DIS[a][b] = |(a+b)%30 - (a*b)%30|
# This is the CROSSING DETECTOR — measures additive-multiplicative disagreement

dis30 = build_dis_table(N30)

# Step 2: Classify each element by its D2 curvature profile
# D2(a) = average curvature when a is the first operand
d2_profile = []
for a in range(N30):
    curvatures = [dis30[a][b] for b in range(N30)]
    avg_curv = sum(curvatures) / N30
    max_curv = max(curvatures)
    zero_count = curvatures.count(0)
    d2_profile.append({
        'element': a,
        'avg_curvature': avg_curv,
        'max_curvature': max_curv,
        'zero_count': zero_count,
        'is_unit': math.gcd(a, N30) == 1 if a > 0 else False,
    })

print("\nZ/30Z element classification by DIS curvature:")
print(f"{'a':>3} {'avg_D':>6} {'max_D':>6} {'zeros':>6} {'unit':>5} {'gcd(a,30)':>10}")
print("-" * 45)
for p in d2_profile:
    a = p['element']
    gcd_val = math.gcd(a, N30) if a > 0 else 0
    print(f"{a:>3} {p['avg_curvature']:>6.1f} {p['max_curvature']:>6} "
          f"{p['zero_count']:>6} {str(p['is_unit']):>5} {gcd_val:>10}")

# Step 3: Build CL for Z/30Z using binary structure
# Rule: HARMONY = element with highest DIS curvature that is a unit
# VOID = 0 (additive identity)
# Composition: classify by DIS, apply HARMONY-dominant + VOID-absorbing rules

# Find HARMONY candidate: the unit with highest average curvature
units_30 = [a for a in range(1, N30) if math.gcd(a, N30) == 1]
unit_curvatures = [(a, d2_profile[a]['avg_curvature']) for a in units_30]
unit_curvatures.sort(key=lambda x: -x[1])

print(f"\nUnits of Z/30Z sorted by DIS curvature:")
for a, c in unit_curvatures[:10]:
    print(f"  a={a:>2}, avg_curvature={c:.1f}")

harmony_30 = unit_curvatures[0][0]
print(f"\nHARMONY candidate for Z/30Z: {harmony_30} (highest curvature unit)")

# Step 4: Build the TSML-like table for Z/30Z
# Rules (from binary structure):
# R1: If a == HARMONY or b == HARMONY → HARMONY
# R2: If a == 0 → 0
# R3: If b == 0 → 0
# R4: ECHO — pairs where DIS[a][b] == 0 (add and mul AGREE → no crossing → operator persists)
# R5: DEFAULT → HARMONY

def build_binary_cl(N, harmony):
    """Build CL from binary structure on Z/NZ."""
    dis = build_dis_table(N)
    table = [[0]*N for _ in range(N)]
    echo_count = 0

    for a in range(N):
        for b in range(N):
            # R1: HARMONY overwhelms
            if a == harmony or b == harmony:
                table[a][b] = harmony
            # R2: VOID row
            elif a == 0:
                table[a][b] = 0
            # R3: VOID col
            elif b == 0:
                table[a][b] = 0
            # R4: No crossing (DIS=0) → operator identity persists
            elif dis[a][b] == 0:
                # When add and mul agree, the BINARY structure determines the output
                # (a+b)%N == (a*b)%N: the crossing is trivial, use the agreed value
                table[a][b] = (a + b) % N  # = (a*b) % N since they agree
                echo_count += 1
            # R5: DEFAULT → HARMONY (crossing succeeds → attractor)
            else:
                table[a][b] = harmony

    return table, echo_count

# Build for Z/10Z first — verify against TSML
print("\n--- Verification: Binary CL on Z/10Z ---")

# On Z/10Z, which unit has highest curvature?
units_10 = [a for a in range(1, 10) if math.gcd(a, 10) == 1]
dis10 = build_dis_table(10)
unit_curv_10 = [(a, sum(dis10[a][b] for b in range(10))/10) for a in units_10]
unit_curv_10.sort(key=lambda x: -x[1])
print(f"Z/10Z units by curvature: {unit_curv_10}")
harmony_10 = unit_curv_10[0][0]
print(f"HARMONY candidate: {harmony_10}")

binary_cl_10, echo_10 = build_binary_cl(10, harmony_10)

# Compare to TSML
matches = sum(1 for a in range(10) for b in range(10)
              if binary_cl_10[a][b] == TSML[a][b])
print(f"Binary CL vs TSML: {matches}/100 match")

# Show mismatches
if matches < 100:
    print("Mismatches:")
    for a in range(10):
        for b in range(10):
            if binary_cl_10[a][b] != TSML[a][b]:
                print(f"  ({a},{b}): binary={binary_cl_10[a][b]}, TSML={TSML[a][b]}, "
                      f"DIS={dis10[a][b]}, (a+b)%10={(a+b)%10}, (a*b)%10={(a*b)%10}")

# Build for Z/30Z
print("\n--- Binary CL on Z/30Z ---")
binary_cl_30, echo_30 = build_binary_cl(30, harmony_30)

# Analyze Markov properties
r30 = analyze_markov(binary_cl_30, 30, f'Binary CL Z/30Z (H={harmony_30})')
print(f"  Spectral gap: {r30['spectral_gap']:.4f}")
print(f"  DB violations: {r30['db_violations']}")
print(f"  Non-associativity sigma: {r30['sigma']:.4f}")
print(f"  Attractor: {r30['pi_max_idx']} (fraction: {r30['harmony_frac']:.3f})")
print(f"  ECHO entries (DIS=0): {echo_30}")
print(f"  H/Hmax: {r30['H_ratio']:.4f}")

# Build for Z/210Z
print("\n--- Binary CL on Z/210Z ---")
N210 = 210
units_210 = [a for a in range(1, N210) if math.gcd(a, N210) == 1]
dis210 = build_dis_table(N210)
unit_curv_210 = [(a, sum(dis210[a][b] for b in range(N210))/N210) for a in units_210]
unit_curv_210.sort(key=lambda x: -x[1])
harmony_210 = unit_curv_210[0][0]
print(f"HARMONY candidate: {harmony_210} (curvature: {unit_curv_210[0][1]:.1f})")

binary_cl_210, echo_210 = build_binary_cl(N210, harmony_210)
r210 = analyze_markov(binary_cl_210, N210, f'Binary CL Z/210Z (H={harmony_210})')
print(f"  Spectral gap: {r210['spectral_gap']:.4f}")
print(f"  DB violations: {r210['db_violations']}")
print(f"  Non-associativity sigma: {r210['sigma']:.6f}")
print(f"  Attractor: {r210['pi_max_idx']} (fraction: {r210['harmony_frac']:.4f})")
print(f"  ECHO entries (DIS=0): {echo_210}")
print(f"  H/Hmax: {r210['H_ratio']:.4f}")

# =====================================================================
# CONVERGENCE: sigma(N) as N grows
# =====================================================================
print("\n" + "=" * 70)
print("CONVERGENCE: sigma(N) and spectral gap as N grows")
print("=" * 70)

print(f"\n{'N':>6} {'HARMONY':>8} {'sigma':>8} {'gap':>8} {'H_frac':>8} {'ECHO':>6} {'DB_viol':>8}")
print("-" * 65)

for N_test in [10, 30]:
    units = [a for a in range(1, N_test) if math.gcd(a, N_test) == 1]
    dis_t = build_dis_table(N_test)
    uc = [(a, sum(dis_t[a][b] for b in range(N_test))/N_test) for a in units]
    uc.sort(key=lambda x: -x[1])
    h = uc[0][0]
    tbl, ec = build_binary_cl(N_test, h)
    r = analyze_markov(tbl, N_test, f'Z/{N_test}Z')
    print(f"{N_test:>6} {h:>8} {r['sigma']:>8.4f} {r['spectral_gap']:>8.4f} "
          f"{r['harmony_frac']:>8.3f} {ec:>6} {r['db_violations']:>8}")

# Z/210Z already computed
print(f"{210:>6} {harmony_210:>8} {r210['sigma']:>8.6f} {r210['spectral_gap']:>8.4f} "
      f"{r210['harmony_frac']:>8.4f} {echo_210:>6} {r210['db_violations']:>8}")

print(f"\ne^{{-1}} = {math.exp(-1):.6f}")
print(f"\nKey question: does sigma -> 0 as N -> inf?")
print(f"If yes: the discrete algebra approaches associativity (= separability)")
print(f"and the BB theorem forces the limit to be log nonlinearity.")
