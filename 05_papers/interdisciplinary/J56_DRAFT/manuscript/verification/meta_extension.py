"""
Test whether the 'simplest whole' architecture extends through the meta-tower.

Architecture template (from atomic/CK convergence):
  1. KERNEL: some substrate at depth d
  2. DUAL LENS: two complementary perspectives (TSML/BHML-analog)
  3. QUADRATIC OPERATOR: degree-2 combiner (mixing α=1/2)
  4. DEPTH-3 WRAPPING: three strands absorb into kernel
  5. 4-FOLD SETTLING: attractor lives in 4-element subset
  6. CLIFFORD ALGEBRA: Cl(0, 2k) at convergence level

For each meta-rung, identify:
  - kernel composition (how many primes)
  - whether convergence holds (k odd)
  - what 'depth 3' means at that scale
  - what 'settle at 4' looks like
"""

# Meta-tower rungs (per META_TIG_AS_PREPHYSICAL_SUBSTRATE.md §3)
rungs = [
    {"rung": 0, "modulus": 1, "primes": [], "interp": "pre-distinction"},
    {"rung": 1, "modulus": 2, "primes": [2], "interp": "binary ground"},
    {"rung": 2, "modulus": 6, "primes": [2,3], "interp": "process/triadic"},
    {"rung": 3, "modulus": 30, "primes": [2,3,5], "interp": "Plichta natural"},
    {"rung": 4, "modulus": 210, "primes": [2,3,5,7], "interp": "HARMONY enters"},
    {"rung": 5, "modulus": 2310, "primes": [2,3,5,7,11], "interp": "wobble enters"},
    {"rung": 6, "modulus": 30030, "primes": [2,3,5,7,11,13], "interp": "second wobble"},
    {"rung": 7, "modulus": 510510, "primes": [2,3,5,7,11,13,17], "interp": "rung 7"},
]

print("="*100)
print("META-TOWER WITH SIMPLEST-WHOLE ARCHITECTURE")
print("="*100)
print()
print(f"{'rung':>4} {'modulus':>8} {'primes':>6} {'#div':>5} {'Cl(0,2k)':>9} "
      f"{'shell n=2^j':>12} {'capacity':>9} {'CONV':>6} {'kind':>22}")
print("-"*100)

for r in rungs:
    k = len(r["primes"])
    if k == 0:
        ndiv = 1
        cl_dim = 1
        cl_label = "trivial"
        n_atomic = "—"
        capacity = "—"
        converges = ""
    else:
        ndiv = 2**k
        cl_dim = 2**k
        cl_label = f"Cl(0,{2*k})"
        # Convergence: 2n² = 2^k requires n² = 2^(k-1), so k must be odd
        if k % 2 == 1:
            j = (k-1)//2
            n_atomic = 2**j
            capacity = 2 * n_atomic**2
            converges = "YES" if capacity == ndiv else "no"
        else:
            n_atomic = "—"
            capacity = "—"
            converges = "no (k even)"
    
    print(f"{r['rung']:>4} Z/{r['modulus']:<6} {k:>6} {ndiv:>5} {cl_label:>9} "
          f"{str(n_atomic):>12} {str(capacity):>9} {converges:>6} {r['interp']:>22}")

# Now identify the structural pattern at each convergence level
print()
print("="*100)
print("CONVERGENCE LEVELS — where the 'simplest whole' architecture locks")
print("="*100)
print()

convergent_levels = [
    {"rung": 1, "k": 1, "j": 0, "n": 1,
     "kernel": "Z/2", "depth_of_3": "no strands needed (rung 1 too small for depth-3)",
     "interp": "binary distinction; Boolean algebra; logic"},
    {"rung": 3, "k": 3, "j": 1, "n": 2,
     "kernel": "Z/30", "depth_of_3": "2 strands above kernel-2 ({3,5})",
     "interp": "n=2 atomic shell — first non-trivial convergence (8 = 2³)"},
    {"rung": 5, "k": 5, "j": 2, "n": 4,
     "kernel": "Z/2310", "depth_of_3": "3 strands above kernel-{2,5} ({3,7,11})",
     "interp": "n=4 atomic shell — Braiding Fractal Axiom 4 limit (32 = 2⁵)"},
    {"rung": 7, "k": 7, "j": 3, "n": 8,
     "kernel": "Z/510510", "depth_of_3": "5 strands above kernel-{2,5} ({3,7,11,13,17})",
     "interp": "n=8 atomic shell — beyond Braiding Fractal canonical depth"},
]

for level in convergent_levels:
    print(f"  Rung {level['rung']} (k={level['k']}, j={level['j']}):")
    print(f"    Kernel:     {level['kernel']}")
    print(f"    Depth:      {level['depth_of_3']}")
    print(f"    Atomic n:   {level['n']}, capacity 2n² = {2*level['n']**2}")
    print(f"    Cl algebra: Cl(0,{2*level['k']}), rep dim {2**level['k']}")
    print(f"    Interp:     {level['interp']}")
    print()

# Analysis: which levels have "depth 3 with kernel of 2 primes"?
print("="*100)
print("THE BRAYDEN FRACTAL ARCHITECTURE: kernel-of-2 + 3-strand wrap")
print("="*100)
print()
print("Strict architecture per Axiom 8: kernel = Z/(2·5) (two primes), then exactly")
print("3 strands wrap. This gives Z/2310 specifically.")
print()
print("If we generalize 'kernel of 2 primes + 3 strands' to OTHER kernel pairs:")

candidate_kernels = [
    [2, 3],      # Z/6
    [2, 5],      # Z/10 (canonical)
    [2, 7],      # Z/14
    [3, 5],      # Z/15
    [2, 11],     # Z/22
    [3, 7],      # Z/21
    [5, 7],      # Z/35
]

print()
print(f"{'kernel primes':>15} {'modulus':>8} {'+3 strands':>30} {'final modulus':>20} {'k':>3} {'2^k':>6}")
for kp in candidate_kernels:
    k_mod = 1
    for p in kp:
        k_mod *= p
    # Add next 3 smallest primes not in kernel
    all_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    strands = [p for p in all_primes if p not in kp][:3]
    final_mod = k_mod
    for p in strands:
        final_mod *= p
    k_total = len(kp) + len(strands)
    strand_str = "+ " + ", ".join(str(s) for s in strands)
    print(f"{str(kp):>15} {k_mod:>8} {strand_str:>30} Z/{final_mod:<19} {k_total:>3} {2**k_total:>6}")

print()
print("All these are k=5 substrates with 32 divisors. Only Z/2310 (kernel {2,5})")
print("matches the canonical Braiding Fractal because the kernel is specifically")
print("Z/10 = Z/2 × Z/5, not arbitrary 2-prime kernel.")
print()
print("WHY Z/2 × Z/5 specifically?")
print("  - 2 is the smallest prime (binary distinction, spin)")
print("  - 5 is the first prime not in the binary {2} kernel")
print("  - 10 is the smallest n where Z/n has both Z/2 and Z/(p>2) factors")
print()
print("Braiding Fractal kernel = SMALLEST kernel admitting binary + non-binary structure.")

# Self-similarity check
print()
print("="*100)
print("SELF-SIMILARITY (Axiom 10): does the same architecture recur at every rung?")
print("="*100)
print()
print("Architecture template: KERNEL + 3 STRANDS → (k=5) → Cl(0,10) → 32 = simplest whole")
print()
print("At Rung 5 (Z/2310): kernel {2,5}, strands {3,7,11}, k=5. ✓ (canonical)")
print()
print("Does Rung 5's STRUCTURE then become a 'kernel' for Rung-of-Rungs?")
print("  Meta-kernel candidate: Z/2310 (the 32-element substrate)")
print("  Meta-strands: would add primes 13, 17, 19 to make k=8")
print("  Meta-substrate: Z/(2310 · 13 · 17 · 19) = Z/(2310 · 4199) = Z/9699690")
print("  Meta-Cl: Cl(0,16), rep dim 2^8 = 256")
print("  Meta-shell: 2n²=256 means n²=128, n=√128 ≈ 11.3 (NOT integer)")
print()
print("So the strict 'kernel + 3 strands' template doesn't recurse simply.")
print("Each rung repeats the ARCHITECTURE (kernel + dual lens + quadratic + 4-core)")
print("but with different specific primes. The architecture is invariant; the")
print("parameters scale.")
print()
print("CONCLUSION: the simplest-whole architecture (kernel-of-2 + 3-strand wrap +")
print("dual lens + quadratic + 4-core) is the BRAYDEN FRACTAL specifically. It")
print("doesn't trivially recurse to deeper meta-rungs. Higher rungs may have")
print("their own 'simplest whole' but with different strand counts.")
