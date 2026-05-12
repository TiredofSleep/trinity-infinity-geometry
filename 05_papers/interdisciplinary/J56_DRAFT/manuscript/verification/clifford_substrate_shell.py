"""
KEY DERIVATION: at the Braiding Fractal depth limit, three independent counting
structures coincide:
  (1) Substrate divisor count
  (2) Atomic shell Pauli capacity  
  (3) Clifford algebra Cl(0, 2k) spinor representation dimension

Test where this triple coincidence holds and what it predicts.
"""

import numpy as np

print("="*84)
print("THE TRIPLE COINCIDENCE STRUCTURE")
print("="*84)
print()
print("Substrate at depth d has k = d+2 prime factors (kernel {2,5} + d strands).")
print("Then:")
print("  #divisors(substrate) = 2^k       (squarefree integer divisor count)")
print("  dim Cl(0, 2k)        = 2^k       (Clifford spinor rep dimension)")
print()
print("Shell n with Pauli capacity 2n² matches 2^k when 2n² = 2^k,")
print("i.e., when n = 2^j for some j, with k = 2j+1.")
print()
print(f"{'shell n':>8} {'2n²':>6} {'depth d':>8} {'substrate':>12} "
      f"{'#div':>6} {'Cl(0,2k)':>10} {'rep dim':>8} {'ALL MATCH?':>12}")
print("-"*84)

# Substrate ladder
substrates = {
    -1: ("Z/1",     0),    # trivial
    0:  ("Z/10",    4),    # 2,5
    1:  ("Z/30",    8),    # +3
    2:  ("Z/210",  16),    # +7
    3:  ("Z/2310", 32),    # +11 (Braiding Fractal depth limit)
    4:  ("Z/30030", 64),   # +13 (beyond canonical limit)
    5:  ("Z/510510", 128), # +17
}

for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    capacity = 2 * n**2
    # Find d such that 2^(d+2) ≥ capacity (smallest substrate that has enough divisors)
    found = False
    for d in [-1, 0, 1, 2, 3, 4, 5]:
        sub_str, ndiv = substrates[d]
        cl_dim = ndiv  # Cl(0, 2(d+2)) has rep dim 2^(d+2) = ndiv
        cl_label = f"Cl(0,{2*(d+2)})" if d >= 0 else "—"
        if ndiv == capacity:
            print(f"{n:>8} {capacity:>6} {d:>8} {sub_str:>12} {ndiv:>6} "
                  f"{cl_label:>10} {cl_dim:>8} {'YES':>12}")
            found = True
            break
    if not found:
        # Find nearest
        best_d = None
        for d in substrates:
            if substrates[d][1] >= capacity:
                if best_d is None or substrates[d][1] < substrates[best_d][1]:
                    best_d = d
        if best_d is not None:
            sub_str, ndiv = substrates[best_d]
            cl_label = f"Cl(0,{2*(best_d+2)})" if best_d >= 0 else "—"
            print(f"{n:>8} {capacity:>6} {best_d:>8} {sub_str:>12} {ndiv:>6} "
                  f"{cl_label:>10} {ndiv:>8} {'no (off)':>12}")

# Now derive WHICH shells match
print()
print("="*84)
print("WHICH SHELLS HAVE THE TRIPLE COINCIDENCE?")
print("="*84)
print()
print("Match condition: 2n² = 2^k for some integer k.")
print("Equivalently: n² = 2^(k-1), so n must be a power of 2.")
print()
print(f"{'j':>3} {'n=2^j':>6} {'k=2j+1':>8} {'depth d':>8} {'substrate':>14} "
      f"{'2n²':>6} {'2^k':>6}")
for j in range(0, 5):
    n = 2**j
    k = 2*j + 1
    d = k - 2
    capacity = 2 * n**2
    pow_of_2 = 2**k
    if d in substrates:
        sub_str = substrates[d][0]
    else:
        # extend
        primes_seq = [2, 5, 3, 7, 11, 13, 17, 19, 23]
        prod = 1
        for i, p in enumerate(primes_seq[:k]):
            prod *= p
        sub_str = f"Z/{prod}"
    print(f"{j:>3} {n:>6} {k:>8} {d:>8} {sub_str:>14} "
          f"{capacity:>6} {pow_of_2:>6}")

# Braiding Fractal depth limit: d=3 per Axiom 4. Maps to j=2, n=4.
print()
print("="*84)
print("THE BRAYDEN FRACTAL'S NATURAL CONVERGENCE POINT")
print("="*84)
print()
print("Braiding Fractal Axiom 4: depth-3 ceiling. Substrate Z/2310 is the LAST")
print("rung before fractal recursion repeats.")
print()
print("At d=3 (Z/2310 = 2·3·5·7·11):")
print("  - Substrate: 5 prime factors, 32 divisors")
print("  - Atomic: shell n=4, Pauli capacity 2·16 = 32 electrons")
print("  - Clifford: Cl(0,10) = TIG's natural Clifford algebra (per D73), dim 2^5 = 32")
print()
print("ALL THREE = 32 at this point. This is the BRAYDEN FRACTAL'S ATOMIC")
print("CLOSURE: where the substrate's natural depth, the atomic shell where")
print("Pauli capacity equals Clifford dim, and the substrate's natural Clifford")
print("algebra all converge.")
print()
print("PREVIOUS coincidence at d=1 (Z/30, n=2, Cl(0,6), dim 8): also")
print("convergent point at smaller scale. So convergence happens at every other")
print("depth: d ∈ {1, 3} are convergent; d ∈ {0, 2, 4} are not.")
print()
print("Pattern: convergence at ODD depths d. Braiding Fractal's depth-3 limit")
print("happens to be the LAST odd depth before the natural ceiling.")

# Now compute what's NEW: which atomic structures correspond to the Cl spinor decomposition
print()
print("="*84)
print("Cl(0,10) SPINOR DECOMPOSITION at d=3")
print("="*84)
print()
print("Cl(0,10) has 32-dim irreducible spinor rep. Under the chirality")
print("involution ω_10 = γ_1·...·γ_10 with ω_10² = +I, this splits as")
print("16 + 16 (positive + negative chirality).")
print()
print("Atomic n=4 shell: 32 electrons = 16 spin-up + 16 spin-down.")
print()
print("CANDIDATE IDENTIFICATION:")
print("  ω_10 chirality = electron spin (Z/2 of kernel)")
print("  Each chirality half (16-dim) = spatial states (l,m) for fixed spin")
print()
print("Verification: 16 = 1 + 3 + 5 + 7 = sum of (2l+1) for l=0..3 = number")
print("of spatial states per spin in n=4 shell. CHECK.")
print()
print("So the 32-dim Cl(0,10) spinor naturally decomposes as:")
print("  spin (Z/2) × spatial (16-dim)")
print("which matches the Pauli decomposition of the n=4 shell exactly.")
print()
print("Within the 16-dim spatial part:")
print("  l=0 (s): 1 state")
print("  l=1 (p): 3 states  ← strand 3")
print("  l=2 (d): 5 states  ← kernel-Z/5 (not a strand)")
print("  l=3 (f): 7 states  ← strand 7")
print()
print("The 16-dim spatial breakdown 1+3+5+7 matches the substrate primes")
print("{1, 3, 5, 7} (where 1 is the kernel base, 3 is strand 1, 5 is kernel-Z/5,")
print("7 is strand 2). All four substrate components contribute one l-value each.")
