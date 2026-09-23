#!/usr/bin/env python3
"""verify_one_third_fold.py -- reproduces every [FORCED] claim in THE_ONE_THIRD_AND_THE_FOLD.md.

    python verify_one_third_fold.py
"""
import numpy as np
import itertools

# --- 1. the fold: the buildable cube has THREE distances (not equidistant) ---
V = np.array(list(itertools.product([0, 1], [0, 1], [0, 1])), float)
dists = sorted({round(float(np.linalg.norm(V[i] - V[j])), 9)
                for i, j in itertools.combinations(range(8), 2)})
assert len(dists) == 3
assert abs(dists[0] - 1) < 1e-9 and abs(dists[1] - np.sqrt(2)) < 1e-9 and abs(dists[2] - np.sqrt(3)) < 1e-9
print(f"1. FOLD: cube distances = {[round(d,4) for d in dists]} = 1, sqrt2, sqrt3 (three, not one)  OK")
print("   (8 truly-equidistant points = the 7-simplex, needs 7 dimensions -- unbuildable in 3D)")

# --- 2. one number, three faces: lift, fold, gap ---
lift = np.arccos(-1/3)                       # vertex angle
fold = (1/np.sqrt(3))**2                     # body-diagonal cos^2
dih = np.arccos(1/3)                         # dihedral angle
assert abs(np.degrees(lift) - 109.4712) < 1e-3
assert abs(fold - 1/3) < 1e-12
assert abs(np.degrees(dih) - 70.5288) < 1e-3
gap = 360 - 5 * np.degrees(dih)
assert 5.0 < 360/np.degrees(dih) < 5.2 and 7.0 < gap < 7.7
print(f"2. ONE 1/3, THREE FACES: lift cos=-1/3 ({np.degrees(lift):.2f} deg); fold cos^2={fold:.4f}; "
      f"dihedral {np.degrees(dih):.2f} deg -> 360/dih={360/np.degrees(dih):.3f} (gap {gap:.2f} deg, no tiling)  OK")

# --- 3. the 1/3 fractures up the tower R -> C -> H ---
theta = np.arccos(-1/3)
re, im = np.cos(theta), np.sin(theta)        # e^{i theta}
assert abs(re - (-1/3)) < 1e-12 and abs(im - np.sqrt(8)/3) < 1e-12
assert abs(re**2 + im**2 - 1) < 1e-12        # conserved on the unit circle
half = np.cos(theta/2)**2                    # quaternion half-angle
assert abs(half - 1/3) < 1e-12
print(f"3. FRACTURE: R: cos=-1/3 ; C: (re,im)=(-1/3, sqrt8/3), re^2+im^2=1 ; "
      f"H: cos^2(theta/2)={half:.4f}=1/3  -> the 1/3 is conserved, redistributed  OK")

print("\nAll FORCED claims verified. 'fold'/'crease'/'conserved invariant' are [READING];")
print("no welding framework-8 to the 7-simplex or Bott-8 ([FENCE]).")
