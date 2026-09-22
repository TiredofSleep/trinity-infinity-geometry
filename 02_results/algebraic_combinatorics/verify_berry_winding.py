#!/usr/bin/env python3
"""
verify_berry_winding.py — numerical verification for BERRY_WINDING_WRITEUP.md

Recomputes, from first principles, the "winding-number" (Two-Cross) result of
TIG and prints exactly the facts quoted in the write-up. Pure integer arithmetic
for the algebra; the winding numbers are literal principal-branch argument sums
around each cyclic orbit embedded in S^1 by discrete logarithm.

There is NO Berry (geometric) phase to verify — this script confirms the
finite-group winding number and its counter-rotation, which is the real result.

Run:
    PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe verify_berry_winding.py
Exits 0 iff every claim holds.
"""
from cmath import exp, pi, phase


def mul(a, b):                       # multiplication in Z/10Z
    return (a * b) % 10


def orbit(gen, ident):               # multiplicative orbit of gen from ident
    seq, x = [ident], mul(ident, gen)
    while x != ident:
        seq.append(x)
        x = mul(x, gen)
    return seq


ok = True

def check(label, cond):
    global ok
    ok = ok and bool(cond)
    return cond


# ---- (i)/(ii) the two cyclic cross-cycles ----------------------------------
corners, edges = {1, 3, 7, 9}, {2, 4, 6, 8}
corner_cycle, edge_cycle = orbit(3, 1), orbit(2, 6)

corner_C4 = ({mul(a, b) for a in corners for b in corners} == corners
             and corner_cycle == [1, 3, 9, 7] and set(corner_cycle) == corners)
edge_C4 = ({mul(a, b) for a in edges for b in edges} == edges
           and all(mul(6, k) == k for k in edges)
           and edge_cycle == [6, 2, 4, 8] and set(edge_cycle) == edges)

print("corner cycle from gen 3: ", " -> ".join(map(str, corner_cycle)),
      "-> 1     is 1->3->9->7 :", corner_cycle == [1, 3, 9, 7],
      "  cyclic C4:", check("corner_C4", corner_C4))
print("edge   cycle from gen 2: ", " -> ".join(map(str, edge_cycle)),
      "-> 6     is 6->2->4->8 :", edge_cycle == [6, 2, 4, 8],
      "  cyclic C4:", check("edge_C4", edge_C4))

# ---- (iii) phi(x)=6x : corners -> edges isomorphism ------------------------
phi = {x: mul(6, x) for x in corners}
phi_iso = (set(phi.values()) == edges
           and all(mul(6, mul(a, b)) == mul(mul(6, a), mul(6, b))
                   for a in corners for b in corners))
print("phi(x)=6x :", phi, "  image == edges:", set(phi.values()) == edges,
      "  homomorphism:", check("phi_iso", phi_iso))

# ---- (iv) CRT idempotents --------------------------------------------------
crt = (mul(5, 5) == 5 and mul(6, 6) == 6 and mul(5, 6) == 0 and (5 + 6) % 10 == 1)
print("CRT: 5*5=%d  6*6=%d  5*6=%d  5+6=%d     5=(%d,%d) 6=(%d,%d)"
      % (mul(5, 5), mul(6, 6), mul(5, 6), (5 + 6) % 10,
         5 % 2, 5 % 5, 6 % 2, 6 % 5))
check("crt", crt)

# ---- counter-rotation: generators inverse mod 5 (torus-free) ---------------
inv_mod5 = (3 * 2) % 5 == 1
print("counter-rotation: 3*2 = %d mod 5  ->  3 = 2^-1 mod 5 :"
      % ((3 * 2) % 5), check("inv_mod5", inv_mod5))

# ---- discrete-log phase winding on S^1 -------------------------------------
def winding(cycle, base_pow):
    """(1/2pi) * sum of principal-branch arg steps of e^{2pi i dlog/4}."""
    dlog = {v % 5: e for e, v in enumerate(base_pow)}      # value mod5 -> exponent
    ang = [exp(2j * pi * dlog[x % 5] / 4) for x in cycle]
    ang.append(ang[0])
    return sum(phase(b / a) for a, b in zip(ang, ang[1:])) / (2 * pi)

# base-2 primitive root of (Z/5Z)^x : 2^0,2^1,2^2,2^3 = 1,2,4,3
w_c = round(winding([1, 3, 9, 7], [1, 2, 4, 3]))
w_e = round(winding([6, 2, 4, 8], [1, 2, 4, 3]))
print("discrete-log winding (base-2 embedding of Z/5Z^x):")
print("   corner-cycle winding number: %+.1f" % w_c)
print("   edge-cycle   winding number: %+.1f" % w_e)
print("   opposite (product = -1):", check("opposite", w_c * w_e == -1))

# base-3 primitive root : 3^0,3^1,3^2,3^3 = 1,3,4,2  -> signs flip, product same
w_c3 = round(winding([1, 3, 9, 7], [1, 3, 4, 2]))
w_e3 = round(winding([6, 2, 4, 8], [1, 3, 4, 2]))
print("   [base-3 embedding] corner: %+.1f  edge: %+.1f  -> signs flip, "
      "oppositeness invariant: %s" % (w_c3, w_e3,
      check("invariant", w_c3 * w_e3 == -1 and (w_c3, w_e3) == (-w_c, -w_e))))

print("\nSTATUS:", "PASS — winding number verified (no Berry phase exists to verify)"
      if ok else "FAIL")
import sys
sys.exit(0 if ok else 1)
