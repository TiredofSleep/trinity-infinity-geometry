"""
Verify the closed-form result: for max-l hydrogenic orbital,
edge_size = n^2 * (2l+1) / 4 where l = n-1.
Therefore D2/D1 = (2l+1) / (8*pi) is l-only-dependent (n cancels).
"""

import numpy as np
from sympy import symbols, integrate, exp, sqrt, Rational, factorial, simplify, oo

# Symbolic verification for max-l = n-1
# R_{n, n-1}(r) = norm * exp(-r/n) * (2r/n)^(n-1)
# norm^2 = (2/n)^3 * 0! / (2n * (2n-1)!) = (2/n)^3 / (2n * (2n-1)!)

# Density: rho = r^2 * R^2

# I_r = integral (rho')^2 / rho dr
# This is computationally intense symbolically. Instead verify numerically
# at high precision and check formula.

import mpmath as mp
mp.mp.dps = 30

def R_max_l_symbolic(r, n):
    """R_{n,l=n-1}(r) for max-l hydrogenic, exact form."""
    # norm = sqrt((2/n)^3 * 1 / (2n * (2n-1)!))
    norm_sq = mp.mpf(2)**3 / mp.mpf(n)**3 / (2 * mp.mpf(n) * mp.factorial(2*n - 1))
    norm = mp.sqrt(norm_sq)
    return norm * mp.exp(-r/n) * (2*r/n)**(n-1)

def density_max_l(r, n):
    return r**2 * R_max_l_symbolic(r, n)**2

def fisher_info_max_l(n):
    """Compute I_r for nodeless l=n-1 orbital at high precision."""
    def integrand(r):
        rho = density_max_l(r, n)
        if rho < mp.mpf(10)**(-50):
            return mp.mpf(0)
        eps = mp.mpf(10)**(-15)
        rho_p = (density_max_l(r+eps, n) - density_max_l(r-eps, n)) / (2*eps)
        return rho_p**2 / rho
    return mp.quad(integrand, [mp.mpf(10)**(-10), 5*n**2])

# Verify formula for n=1 to 7
print("Verifying formula: edge_size(nodeless n,l=n-1) = n^2 (2l+1) / 4")
print(f"{'n':>3} {'edge (computed)':>20} {'edge (formula)':>20} {'ratio':>15}")
for n in range(1, 8):
    l = n - 1
    edge_num = 1 / fisher_info_max_l(n)
    edge_formula = mp.mpf(n)**2 * (2*l + 1) / 4
    print(f"{n:>3} {float(edge_num):>20.6f} {float(edge_formula):>20.6f} "
          f"{float(edge_num/edge_formula):>15.10f}")

# Compute D2/D1 * 8*pi exactly
print(f"\nD2/D1 * 8*pi for nodeless orbitals:")
print(f"  Theoretical: (2l+1)")
for n in range(1, 8):
    l = n - 1
    edge = float(mp.mpf(n)**2 * (2*l + 1) / 4)
    perim = 2 * mp.pi * n**2
    ratio = edge / perim * 8 * mp.pi
    print(f"  n={n}, l={l} ({'spdfghi'[l]}): D2/D1 * 8pi = {float(ratio):.6f}, "
          f"matches 2l+1 = {2*l+1}: {abs(float(ratio) - (2*l+1)) < 1e-10}")

# Now make the substrate connection explicit
print("\n" + "="*72)
print("SUBSTRATE-PRIME APPEARANCE in D2/D1 ratio")
print("="*72)
substrate_primes = [3, 7, 11]
print(f"Substrate-click primes: {substrate_primes}")
print(f"Orbital multiplicities (2l+1): for l=0..6 = {[2*l+1 for l in range(7)]}")
print(f"Substrate matches l: ", end="")
for l in range(7):
    if (2*l+1) in substrate_primes:
        print(f"l={l} (orbital {'spdfghi'[l]}, mult {2*l+1})", end="; ")
print()
print()
print("So for nodeless orbitals at l = 1, 3, 5 (p, f, h):")
for l in [1, 3, 5]:
    n = l + 1
    mult = 2*l + 1
    d2d1 = mult / (8 * float(mp.pi))
    print(f"  {n}{'spdfghi'[l]}: D2/D1 = {mult}/(8*pi) = {d2d1:.6f} ← substrate prime {mult}")
print("And for skipped l = 2, 6 (d, i):")
for l in [2, 6]:
    n = l + 1
    mult = 2*l + 1
    d2d1 = mult / (8 * float(mp.pi))
    print(f"  {n}{'spdfghi'[l]}: D2/D1 = {mult}/(8*pi) = {d2d1:.6f} ← non-substrate {mult}")
