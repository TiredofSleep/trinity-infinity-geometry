#!/usr/bin/env python3
"""
Verifies the corrected tutorial Part 5 attractor code.
Runs the same fuse-then-mix iteration as J35 verification.
Should produce H/Br = 1+sqrt(3) at machine precision.

Run: python verification/_verify_tutorial_attractor.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ck_tables import TSML, BHML
import mpmath as mp

mp.mp.dps = 50    # 50 decimal digits

def fuse(table, p):
    out = [mp.mpf(0)] * 10
    for i in range(10):
        for j in range(10):
            out[table[i][j]] += p[i] * p[j]
    return out

def joint_tick(p, alpha=mp.mpf(1)/2):
    Tf = fuse(TSML, p)
    Bf = fuse(BHML, p)
    out = [alpha * Tf[k] + (1 - alpha) * Bf[k] for k in range(10)]
    s = sum(out)
    return [x / s for x in out]

# Start from uniform on 4-core
p = [mp.mpf(0)] * 10
for c in [0, 7, 8, 9]:
    p[c] = mp.mpf(1) / 4

prev = list(p)
for step in range(300):
    p = joint_tick(p)
    delta = max(abs(p[k] - prev[k]) for k in range(10))
    if delta < mp.mpf(10) ** -45:
        print(f"Converged at step {step+1}, max delta = {mp.nstr(delta, 5)}")
        break
    prev = list(p)

V, H, Br, R = p[0], p[7], p[8], p[9]
print()
print(f"V (VOID)    = {mp.nstr(V, 12)}")
print(f"H (HARMONY) = {mp.nstr(H, 12)}")
print(f"Br (BREATH) = {mp.nstr(Br, 12)}")
print(f"R (RESET)   = {mp.nstr(R, 12)}")
print(f"4-core total = {mp.nstr(V + H + Br + R, 12)}")
print()

ratio = H / Br
target = 1 + mp.sqrt(3)
err = abs(ratio - target)
print(f"H / Br      = {mp.nstr(ratio, 35)}")
print(f"1 + sqrt(3) = {mp.nstr(target, 35)}")
print(f"|error|     = {mp.nstr(err, 5)}")
print()
ok = err < mp.mpf(10) ** -30
print(f"Tutorial corrected attractor: {'PASS' if ok else 'FAIL'}")
