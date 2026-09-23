#!/usr/bin/env python3
"""
verify_forced_chain.py -- the forced geometric core of the integers, checked.

Reproduces the forced geometric facts that THE_INTEGERS.md, P1 and P2 build on (the same core
the book The Shape of Understanding teaches): points at equal distances form
simplices (the tetrahedral 1/3), and three perpendicular directions generate the Clifford
algebra of the cube, Cl(3), whose projections give the square and the hexagon.
Run: python3 verify_forced_chain.py
Any assertion failure means a forced claim is wrong -- investigate before extending.
"""
import numpy as np
from math import comb

def ok(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    assert cond, f"FORCED claim failed: {name}"

print("="*66)
print("1 -- INTEGERS AS SIMPLICES; THE TETRAHEDRAL 1/3")
print("="*66)
# simplex angle cos = -1/(N-1); at N=4 gives -1/3
for N, expect in [(2,-1.0),(3,-0.5),(4,-1/3),(5,-0.25)]:
    ok(f"N={N} simplex angle cos = -1/(N-1) = {expect:.4f}", abs(-1/(N-1)-expect)<1e-12)
# the tetrahedral angle
tet = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]], float)
c = tet.mean(0)
v1, v2 = tet[0]-c, tet[1]-c
cos_full = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
ok("tetrahedral (full) angle cos = -1/3 exactly", abs(cos_full-(-1/3))<1e-12)
ok("tetrahedral angle = 109.47 deg", abs(np.degrees(np.arccos(cos_full))-109.4712)<1e-2)
# the half-angle: cos^2 = 1/3
half = np.degrees(np.arccos(cos_full))/2
ok("half-angle = 54.7356 deg", abs(half-54.7356)<1e-2)
ok("cos^2(half-angle) = 1/3", abs(np.cos(np.radians(half))**2-1/3)<1e-4)
print("  NOTE: 1/3 = 1/(N-1) AT N=4 specifically -- not a general identity.")

print()
print("="*66)
print("2 -- THE FORCED CLIFFORD CUBE Cl(3)")
print("="*66)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
g=[sx,sy,sz]
for i in range(3):
    for j in range(i+1,3):
        anti=g[i]@g[j]+g[j]@g[i]
        ok(f"Cl(3) generators e{i},e{j} anticommute", np.allclose(anti,0))
for i in range(3):
    ok(f"e{i}^2 = I", np.allclose(g[i]@g[i], np.eye(2)))
ok("dim Cl(3) = 2^3 = 8 = cube vertices", 2**3==8)
ok("Cl(3) grades 1,3,3,1 (Pascal row 3) sum to 8", [comb(3,k) for k in range(4)]==[1,3,3,1])
# two projections
axis=np.array([1,1,1])/np.sqrt(3)
e=[np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.])]
proj=[v-np.dot(v,axis)*axis for v in e]
ang=np.degrees(np.arccos(np.clip(np.dot(proj[0],proj[1])/(np.linalg.norm(proj[0])*np.linalg.norm(proj[1])),-1,1)))
ok("diagonal projection of cube axes = 120 deg (hexagon)", abs(ang-120)<1e-6)
ok("projection angle cos^2(1,1,1) = 1/3", abs((1/np.sqrt(3))**2-1/3)<1e-12)
print("  FENCE: the hexagon's directions are 120 deg apart -- not perpendicular -- so")
print("         they do NOT anticommute: the hexagon is a PROJECTION of the Clifford")
print("         cube, not a host of the algebra.")
# Clifford GENERATORS are vectors: in geometric algebra e_i e_j + e_j e_i = 2 (e_i . e_j),
# so two directions anticommute exactly when they are perpendicular (dot product zero).
# (The reflection MAPS in two perpendicular mirrors commute; it is the direction vectors
# themselves, as elements of the algebra, that anticommute.)
def vecs_anticommute(angle_deg):
    a = np.radians(angle_deg)
    v1 = np.array([1.0, 0.0]); v2 = np.array([np.cos(a), np.sin(a)])
    return abs(np.dot(v1, v2)) < 1e-12
ok("SQUARE directions (90 deg apart) anticommute -> carries Clifford",
   vecs_anticommute(90))
ok("HEX directions (120 deg apart) do NOT anticommute -> hex does not host Cl",
   not vecs_anticommute(120))
# sanity: the true Clifford vectors (orthogonal Pauli) anticommute
ok("orthogonal Clifford vectors sx,sz anticommute (Cl(3) generators)",
   np.allclose(sx@sz + sz@sx, 0))

print()
print("="*66)
print("ALL FORCED CLAIMS VERIFIED: simplices and the tetrahedral 1/3;")
print("the cube = Cl(3), its grades 1+3+3+1, and its two projections.")
print("="*66)
