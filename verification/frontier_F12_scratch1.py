#!/usr/bin/env python3
"""F12 scratch: cycle-type sampling for Gal(h/Q(alpha_special))."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from sympy import Symbol, Poly, ZZ, sieve
from collections import Counter
import time

a = Symbol('a')
xi = Symbol('xi')

Q = (
    4*a**4*xi**6 - 8*a**4*xi**5 - 16*a**4*xi**4 + 16*a**4*xi**3
    + 16*a**4*xi**2 - 64*a**4*xi
    - 2*a**3*xi**7 + 28*a**3*xi**5 - 12*a**3*xi**4 - 16*a**3*xi**3
    + 32*a**3*xi**2 + 160*a**3*xi
    + 3*a**2*xi**7 - 13*a**2*xi**6 - 12*a**2*xi**5 + 64*a**2*xi**4
    - 84*a**2*xi**3 - 108*a**2*xi**2 - 144*a**2*xi + 16*a**2
    - a*xi**7 + 8*a*xi**6 - 8*a*xi**5 - 27*a*xi**4 + 100*a*xi**3
    + 52*a*xi**2 + 40*a*xi - 16*a
    - 20*xi**3 + 4
)
P_24_expr = (
    28311552*a**24 - 353894400*a**23 + 1993900032*a**22 - 6690619392*a**21
    + 15603892224*a**20 - 32432816128*a**19 + 81439860736*a**18 - 225728144384*a**17
    + 535543922176*a**16 - 1010691466496*a**15 + 1582899022720*a**14 - 2251232005184*a**13
    + 3118379604416*a**12 - 4131827146208*a**11 + 4855752468824*a**10 - 4749347962604*a**9
    + 3731481660606*a**8 - 2308838329013*a**7 + 1107558919312*a**6 - 404683623882*a**5
    + 110031153354*a**4 - 21534954597*a**3 + 2873272500*a**2 - 233550000*a + 8437500
)

P24_poly = Poly(P_24_expr, a, domain=ZZ)
disc_P24 = P24_poly.discriminant()
lc_P24 = int(P24_poly.LC())

cycle_types = Counter()
n_primes_target = 2000
n_processed = 0
n_with_special_fiber = 0
t0 = time.time()
for p in sieve.primerange(3, 500000):
    if n_with_special_fiber >= n_primes_target:
        break
    n_processed += 1
    if lc_P24 % p == 0:
        continue
    if disc_P24 % p == 0:
        continue
    # Factor P_24 mod p
    P24_modp = Poly(P_24_expr, a, modulus=p)
    facs = P24_modp.factor_list()[1]
    # Find linear factors: a + c0 -> alpha_root = -c0 mod p
    for f, m in facs:
        if f.degree() == 1 and m == 1:
            lc_f = int(f.all_coeffs()[0]) % p
            if lc_f == 0:
                continue
            c0 = int(f.all_coeffs()[1]) % p
            alpha_modp = (-c0 * pow(lc_f, -1, p)) % p
            # Substitute into Q
            Q_at = Q.subs(a, alpha_modp)
            Qp = Poly(Q_at, xi, modulus=p)
            if Qp.degree() != 7:
                continue
            # Check for double root
            dQp = Qp.diff(xi)
            g = Qp.gcd(dQp)
            if g.degree() != 1:
                continue
            # Has double root; this is the "special fiber" for this prime
            lc_g = int(g.all_coeffs()[0]) % p
            if lc_g == 0:
                continue
            c0g = int(g.all_coeffs()[1]) % p
            xi_dbl_modp = (-c0g * pow(lc_g, -1, p)) % p
            # Divide Qp by (xi - xi_dbl_modp)^2
            sq_factor = Poly((xi - xi_dbl_modp)**2, xi, modulus=p)
            try:
                h_polyp, rem = Qp.div(sq_factor)
            except Exception:
                continue
            if not rem.is_zero:
                continue
            if h_polyp.degree() != 5:
                continue
            # Factor h_polyp
            h_facs = h_polyp.factor_list()[1]
            # Check all multiplicities are 1 (separable, else skip)
            if any(mult != 1 for _, mult in h_facs):
                continue
            cycle = tuple(sorted([fac.degree() for fac, _ in h_facs]))
            if sum(cycle) != 5:
                continue
            cycle_types[cycle] += 1
            n_with_special_fiber += 1
            break

print(f"Processed {n_processed} primes; {n_with_special_fiber} useful 'special fibers' (with double-root)")
print(f"Time: {time.time()-t0:.2f}s")
print()
print(f"Observed cycle-type spectrum on the 5 xi-roots of h:")
total = sum(cycle_types.values())
print(f"  {'cycle type':18s}  observed   freq")
for ct in sorted(cycle_types.keys(), key=lambda x: (-sum(x), x)):
    print(f"  {str(ct):18s}  {cycle_types[ct]:>6d}   {cycle_types[ct]/total:.4f}")
print()

# Cycle-type parity
def cycle_parity(ct):
    return sum(c - 1 for c in ct) % 2

# Theory: S_5 cycle frequencies
S5_theory = {
    (1,1,1,1,1): 1/120,
    (1,1,1,2):  10/120,
    (1,2,2):    15/120,
    (1,1,3):    20/120,
    (2,3):      20/120,
    (1,4):      30/120,
    (5,):       24/120,
}
print("S_5 reference frequencies vs observed:")
for ct, freq in sorted(S5_theory.items(), key=lambda x: (-sum(x[0]), x[0])):
    obs = cycle_types.get(ct, 0)
    print(f"  {str(ct):18s}  obs={obs:>5d}  obs_freq={obs/total if total else 0:.4f}  S_5={freq:.4f}")
print()

# Transitive subgroup candidates
candidates = {
    'Z/5  (order 5)':  {(1,1,1,1,1), (5,)},
    'D_5  (order 10)': {(1,1,1,1,1), (5,), (1,2,2)},
    'F_20 (order 20)': {(1,1,1,1,1), (5,), (1,2,2), (1,4)},
    'A_5  (order 60)': {ct for ct in S5_theory if cycle_parity(ct) == 0},
    'S_5  (order 120)': set(S5_theory.keys()),
}
print("Compatibility check (Gal(h/Q(alpha_special)) is contained in...):")
obs_set = set(cycle_types.keys())
for name, allowed in candidates.items():
    extras = obs_set - allowed
    print(f"  {name}? {'YES' if not extras else 'NO (extras: ' + str(sorted(extras)[:3]) + ')'}")
print()

# Parity check
odd_observed = [ct for ct in cycle_types if cycle_parity(ct) == 1]
print(f"Odd parity cycle types observed: {len(odd_observed)} distinct, with {sum(cycle_types[ct] for ct in odd_observed)} total")
if odd_observed:
    print(f"  examples: {odd_observed[:5]}")
    print(f"  -> Gal(h/Q(alpha_special)) is NOT contained in A_5.")
else:
    print("  -> No odd cycle types observed: Gal(h/Q(alpha_special)) is POSSIBLY in A_5.")
print()

# Final verdict for Galois group of h
print("="*60)
print("VERDICT for Gal(h/Q(alpha_special)):")
if (5,) in obs_set:
    print("  Contains a 5-cycle (the prime 5 = degree).")
if odd_observed:
    print("  Has odd permutations.")
print()
# Decision tree
if (1,1,3) in obs_set:
    print("  Contains a 3-cycle.")
    if odd_observed:
        # Cannot be A_5 (parity) and contains 3-cycle and 5-cycle
        # Transitive + 5-cycle + 3-cycle + odd = S_5 (only S_5 has all these)
        print("  Transitive (5-cycle present) + has 3-cycle + has odd parity")
        print("  -> Gal(h/Q(alpha_special)) = S_5 (Tier-A)")
    else:
        print("  No odd permutation: probably A_5")
elif (1,1,1,2) in obs_set or (1,4) in obs_set:
    print("  Contains a transposition or 4-cycle (odd-parity).")
    print("  Cannot be Z/5 or D_5.")
    print("  Group could be F_20 (4-cycle), S_5, or A_5 (no, odd)")
    print("  -> Need further analysis")
else:
    print("  Limited observed types; need more samples or different analysis.")
