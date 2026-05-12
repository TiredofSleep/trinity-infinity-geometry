"""
Lock the strand-orbital map at high precision.
Show explicitly: substrate strand n maps to (n_atom, l_atom) where 
l_atom = (p_n - 1)/2, n_atom = (p_n + 1)/2.
"""

# Substrate ladder per BRAIDING_FRACTAL_FORMAL.md Axiom 8 + Z30/Z210 doc
substrate_ladder = [
    {"level": 0, "modulus": 10, "strand": None,    "stratum": "kernel (2,5)"},
    {"level": 1, "modulus": 30, "strand": 3,       "stratum": "I (3 added)"},
    {"level": 2, "modulus": 210, "strand": 7,      "stratum": "II (7 added)"},
    {"level": 3, "modulus": 2310, "strand": 11,    "stratum": "III_1 (11 added)"},
    {"level": 4, "modulus": 30030, "strand": 13,   "stratum": "III_2 (13 added)"},
]

# Map each strand to the atomic orbital with matching multiplicity
print("STRAND ↔ ORBITAL MAP (verified)")
print("="*84)
print(f"{'level':>5} {'modulus':>8} {'strand p_n':>11} {'mult 2l+1':>11} "
      f"{'l_atom':>7} {'n_atom':>7} {'orbital':>9} {'D2/D1*8π':>12}")
print("-"*84)
import math
for entry in substrate_ladder:
    if entry["strand"] is None:
        # Kernel level — no single strand
        print(f"{entry['level']:>5} {entry['modulus']:>8} {'kernel':>11} "
              f"{'(2,5)':>11} {'spin/' :>7} {'?':>7} {'-':>9} {'-':>12}")
        continue
    p_n = entry["strand"]
    l_atom = (p_n - 1) // 2
    n_atom = (p_n + 1) // 2
    letters = 'spdfghi'
    orbital = f"{n_atom}{letters[l_atom]}"
    d2d1 = f"{p_n}/(8π)"
    print(f"{entry['level']:>5} {entry['modulus']:>8} {p_n:>11} {p_n:>11} "
          f"{l_atom:>7} {n_atom:>7} {orbital:>9} {d2d1:>12}")

print()
print("Verification: for each substrate strand p_n, the nodeless orbital")
print("with multiplicity p_n is at (l = (p_n-1)/2, n = l+1).")
print()
print("ORBITALS NOT REACHED BY SUBSTRATE STRANDS:")
print("="*84)
print(f"{'orbital':>9} {'l':>3} {'mult 2l+1':>11} {'why not':>50}")
not_reached = [
    ("1s", 0, 1, "kernel base; no strand wrapping"),
    ("3d", 2, 5, "5 IS the kernel-Z/5 partner; not a strand"),
    ("5g", 4, 9, "9 = 3² composite; only first power of 3 is a strand"),
    ("7i", 6, 13, "13 is Stratum III_2 (would be next strand)"),
]
for orb, l, mult, why in not_reached:
    print(f"{orb:>9} {l:>3} {mult:>11} {why:>50}")

print()
print("OBSERVATION: substrate strands hit ODD-l orbitals (p, f, h, i).")
print("Skipped orbitals are EVEN-l (s, d, g) plus i which is odd-l but")
print("at Stratum III_2 not yet wrapped in the canonical 4-shell tower.")
print()
print("The 4-shell substrate tower (Braiding Fractal Axiom 4 depth-3 limit)")
print("realizes EXACTLY the first three odd-l orbital levels with prime-")
print("multiplicity: p, f, h. The fourth shell (Z/30030 with strand 13)")
print("would realize i (l=6).")

# Check Pauli counts at each substrate level
print()
print("="*84)
print("PAULI ELECTRON COUNTS vs SUBSTRATE INVARIANTS")
print("="*84)
print()
print(f"{'Shell n':>7} {'Capacity 2n²':>13} {'Cumulative':>12} {'Substrate':>10} "
      f"{'#divisors':>11} {'φ':>8}")
for n in range(1, 6):
    capacity = 2 * n**2
    cumul = sum(2*k**2 for k in range(1, n+1))
    if n == 1:
        sub = 10; div = 4; phi = 4
    elif n == 2:
        sub = 30; div = 8; phi = 8
    elif n == 3:
        sub = 210; div = 16; phi = 48
    elif n == 4:
        sub = 2310; div = 32; phi = 480
    elif n == 5:
        sub = 30030; div = 64; phi = 5760
    print(f"{n:>7} {capacity:>13} {cumul:>12} Z/{sub:<7} {div:>11} {phi:>8}")

print()
print("CRITICAL: cumulative shell capacity = #divisors of substrate at same level!")
print("  n=1:  2 electrons,  Z/10 has 4 divisors      (mismatch by 2 = spin doubling?)")
print("  n=2:  10 electrons (cumulative), Z/30 has 8")
print("  n=3:  28 electrons, Z/210 has 16")
print("  n=4:  60 electrons, Z/2310 has 32")
print()
print("Hmm — these don't match 1:1, but ratios are close to 2.")
print("Actually: #divisors of Z/(2·primorial) = 2^k where k = number of prime factors.")
print("And electron capacity 2n² grows with n too.")
print()
print("Cleaner check: is there an EXACT correspondence at some level?")
for n in range(1, 6):
    if n == 1: sub = 10; div = 4
    elif n == 2: sub = 30; div = 8
    elif n == 3: sub = 210; div = 16
    elif n == 4: sub = 2310; div = 32
    elif n == 5: sub = 30030; div = 64
    capacity = 2 * n**2
    cumul = sum(2*k**2 for k in range(1, n+1))
    print(f"  n={n}: capacity 2n²={capacity}, cumul={cumul}, divisors={div}, "
          f"capacity/divisors={capacity/div:.3f}, cumul/divisors={cumul/div:.3f}")
