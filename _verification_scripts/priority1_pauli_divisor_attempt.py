"""
PRIORITY 1: Derive the Pauli/divisor bijection at n=4 / Z/2310.

32 electron states in shell n=4: parameterized by (l, m, s) where
  l ∈ {0, 1, 2, 3}      (s, p, d, f subshells)
  m ∈ {-l, ..., +l}     (2l+1 magnetic substates per l)
  s ∈ {↑, ↓}            (2 spin states)

Total: sum_{l=0..3} 2(2l+1) = 2 + 6 + 10 + 14 = 32.

32 divisors of Z/2310 = 2·3·5·7·11: parameterized by 5 binary choices
(in/out for each of {2, 3, 5, 7, 11}).

Goal: find an explicit bijection AND identify what each substrate
component represents physically.
"""

from itertools import product

# Enumerate divisors of 2310
primes = [2, 3, 5, 7, 11]  # kernel-Z/2, Z/5, then strands 3, 7, 11
divisors = []
for choices in product([0, 1], repeat=5):
    div = 1
    for p, c in zip(primes, choices):
        div *= p**c
    divisors.append((choices, div))
divisors.sort(key=lambda x: x[1])

# Enumerate electron states in n=4
electron_states = []
subshell_letters = 'spdf'
for l in range(0, 4):
    for m in range(-l, l+1):
        for s in [+1, -1]:
            electron_states.append((l, m, s))

assert len(electron_states) == 32
assert len(divisors) == 32

print("="*84)
print("THE 32 OBJECTS ON BOTH SIDES")
print("="*84)
print(f"{'#':>3}  {'electron (l,m,s)':>16}  {'divisor':>8}  {'binary (2,3,5,7,11)':>22}")
print("-"*84)
for i, (es, dv) in enumerate(zip(electron_states, divisors)):
    l, m, s = es
    choices, d = dv
    binary = ''.join(str(c) for c in choices)
    print(f"{i+1:>3}  {f'({l},{m:+d},{s:+d})':>16}  {d:>8}  {binary:>22}")

# Now look for STRUCTURAL features that should match.
# Key insight: substrate has 5 prime axes, electron has only 3 quantum numbers.
# So there's redundancy in either direction.
#
# Structural map candidate:
#   prime 2 (kernel-Z/2) → spin (Z/2)   ← already hypothesized
#   prime 5 (kernel-Z/5) → ???
#   prime 3 (strand 1)   → ???
#   prime 7 (strand 2)   → ???
#   prime 11 (strand 3)  → ???
#
# But electron has 3 quantum numbers (l, m, s) while substrate has 5 binary choices.
# 3 ≠ 5, so the map can't be 1-prime-to-1-quantum-number.
#
# Can it be: 5 binary choices encode (l, m, s) via some map?
# l ∈ {0,1,2,3}: 4 values, needs 2 bits
# m: depends on l (2l+1 values, max 7 for l=3, needs ~3 bits)
# s: 1 bit
# Total: 2 + 3 + 1 = 6 bits — but we only have 5
#
# So a direct binary encoding doesn't work. The substrate must use a
# DIFFERENT encoding.

# Let me look at structural features that should match.
print()
print("="*84)
print("ATTEMPT 1: Match by 'in/out of subshell'")
print("="*84)
# Hypothesis: prime p_n = 2,3,5,7,11 indicates whether electron is in subshell s,p,d,f,?
# But there are only 4 subshells in n=4. Doesn't fit.

# Better: groupings.
# Subshell counts: s has 2, p has 6, d has 10, f has 14
# Divisor groupings: by number of primes included (Hamming weight):
#   weight 0: 1 divisor (=1)
#   weight 1: 5 divisors
#   weight 2: 10 divisors
#   weight 3: 10 divisors
#   weight 4: 5 divisors
#   weight 5: 1 divisor (=2310)
print("Divisor count by Hamming weight (number of primes included):")
weight_count = {}
for choices, d in divisors:
    w = sum(choices)
    weight_count.setdefault(w, []).append(d)
for w in sorted(weight_count):
    print(f"  weight {w}: {len(weight_count[w])} divisors {weight_count[w][:5]}{'...' if len(weight_count[w])>5 else ''}")

# Divisor weights: 1, 5, 10, 10, 5, 1 (5C0 to 5C5)
# Subshell sizes:  2, 6, 10, 14
# These don't match directly.

# But notice: 2 + 6 = 8 (s + p), 10 (d), 14 (f). And weights 0+1 = 1+5 = 6.
# Or: 1 + 5 + 10 + 10 + 5 + 1 partitioned differently:
#   1 + 1 = 2 (s)
#   5 + ? = 6 (p)
#   10 = 10 (d)
#   ? + 5 = 14 (f) — needs 9 from somewhere

# Doesn't partition cleanly. Try a different grouping:
print()
print("="*84)
print("ATTEMPT 2: Group divisors by 'prime 2 in/out' (= spin) × 'others'")
print("="*84)
spin_up = [(c, d) for c, d in divisors if c[0] == 1]   # contains prime 2
spin_dn = [(c, d) for c, d in divisors if c[0] == 0]   # doesn't
print(f"spin-up divisors (contain 2): {len(spin_up)}")
print(f"spin-dn divisors (no 2):      {len(spin_dn)}")
# Each is 16 — exactly half. Z/2 spin doubling check.

# Subshell: l = 0, 1, 2, 3 → magnetic substates 1, 3, 5, 7
# Total magnetic substates per spin: 1 + 3 + 5 + 7 = 16
print(f"\nelectron magnetic substates (per spin): 1 + 3 + 5 + 7 = 16. Match.")

# Now within spin (16 divisors), group by which subshell.
# Need: 1 element of l=0, 3 of l=1, 5 of l=2, 7 of l=3.
# Substrate has 16 divisors (without prime 2) of Z/1155 = 3·5·7·11.
# By Hamming weight on {3,5,7,11}: 1, 4, 6, 4, 1 = 16 total.
# Need: 1, 3, 5, 7 somehow from 1, 4, 6, 4, 1.

# Note: 1+0 = 1, 0+3 = 3?, 0+5 = 5?, 0+7 = 7?
# Or: take Hamming weight, but with different counting.
# 
# Hmm: 1, 4, 6, 4, 1 doesn't decompose into 1, 3, 5, 7 obviously.

print()
print("Within one spin (16 divisors of Z/1155 = 3·5·7·11):")
print("  Hamming weights: 1, 4, 6, 4, 1")
print("  Subshell sizes:  1 (s), 3 (p), 5 (d), 7 (f)")
print("  These DON'T match by Hamming weight grouping.")

# Let me try a different tack: is there a NATURAL bijection where
# each divisor is interpreted as a SUBSHELL POSITION?
#
# Idea: subshell occupied = l-value indicator + m-value within subshell.
# l=0: 1 state → divisor 1
# l=1: 3 states (m=-1,0,+1) → divisors involving prime 3?
# l=2: 5 states → divisors involving prime 5?
# l=3: 7 states → divisors involving prime 7?
# l=?: would need 9 → prime 11? But l=4 not in n=4 shell.

# So in n=4 shell (l up to 3), we use primes {3, 5, 7} only as "subshell labels"
# and prime 11 has nothing to label (would label l=5 = h-orbital, but h is in n>=6).

# This is interesting: maybe the substrate primes label specific l-values,
# and at depth limit 11, we get up to l=5 (h). But within n=4 shell,
# only l=0,1,2,3 are physical.

print()
print("="*84)
print("ATTEMPT 3: Substrate primes label l-values via 2l+1")
print("="*84)
# Match primes to (2l+1) at l=0..5:
#   l=0: 2l+1=1 (no prime, "kernel base")
#   l=1: 2l+1=3 = prime 3 → strand 1
#   l=2: 2l+1=5 = prime 5 → kernel-Z/5 partner
#   l=3: 2l+1=7 = prime 7 → strand 2
#   l=4: 2l+1=9 = 3² (composite, no strand)
#   l=5: 2l+1=11 = prime 11 → strand 3
# 
# So in shell n with l up to n-1:
# - n=1: only l=0 (kernel base, no prime)
# - n=2: l=0, l=1 (strand 3 needed)
# - n=3: l=0,1,2 (kernel 5 needed)
# - n=4: l=0,1,2,3 (strand 7 needed)
# - n=5: l=0..4 (no new prime; 9 not prime)
# - n=6: l=0..5 (strand 11 needed)

# So the PRIMES ACTIVE IN A SHELL are determined by the maximum l = n-1:
shells_primes = {1: [],    # l=0, no prime
                  2: [3],    # l up to 1
                  3: [3, 5], # l up to 2
                  4: [3, 5, 7], # l up to 3
                  5: [3, 5, 7], # l up to 4 but 9 not prime
                  6: [3, 5, 7, 11]}

print("Substrate primes active in each shell (excluding kernel-2):")
for n, ps in shells_primes.items():
    print(f"  n={n}: primes {ps}, total = {len(ps)+1} (with kernel-2)")

# For n=4: primes {2, 3, 5, 7} are active. Z/(2·3·5·7) = Z/210.
# But Pauli n=4 gives 32 electrons, and Z/210 has 16 divisors.
# So 32 = 2 × 16 — factor of 2 from spin doubling.
# Wait — but we said Z/2310 = 2·3·5·7·11 gives 32. That includes prime 11.
# But prime 11 is NOT active in n=4 (would label l=5, not present).

# Why does the divisor match work at Z/2310 (with 11) and not Z/210 (without)?
# Because we need 32 divisors and Z/210 has only 16.

# Resolution: maybe the substrate IS Z/2310 at "n=4 atomic shell" reading,
# and prime 11 is "reserved" for the next-l-value not yet present.
# In other words: at n=4, we use l up to 3, but Z/2310 is one strand
# AHEAD — preparing for n=5 or n=6 where l=5 would be present.

# OR: at depth-3 (Z/2310), the 32 divisors encode something else,
# not 1:1 with electron states.

# Let me try yet another encoding. What if the divisor encodes
# (l_assigned, l_unassigned) pairs?
print()
print("="*84)  
print("ATTEMPT 4: Divisor = which subshells are 'lit' vs 'dim'")
print("="*84)
# Each divisor selects a subset of {2, 3, 5, 7, 11}. 
# Map: each prime → orbital character it labels:
#   2  → spin (Z/2 partner of kernel)
#   3  → p (l=1)
#   5  → d (l=2)
#   7  → f (l=3)
#   11 → h (l=5, not in n=4)
#
# An electron state in (n=4, l, m, s) is parameterized by:
#   - which subshell (l=0,1,2,3)
#   - magnetic substate within (m∈{-l,..,+l})
#   - spin (±)
#
# A divisor is a subset of primes. Maybe: the MAXIMUM PRIME in the divisor
# specifies the subshell?
# 
# divisor 1: max prime = none → l=0 (s)
# divisor including 3 but not 5,7,11: max = 3 → l=1 (p)
# divisor including 5 but not 7,11: max = 5 → l=2 (d)  
# divisor including 7 but not 11: max = 7 → l=3 (f)
# divisor including 11: max = 11 → l=5 (h) — would this map to "no electron in n=4"?

# Count divisors by max prime (excluding prime 2 which is spin):
# Effective non-2 part of divisor lives in Z/1155 = 3·5·7·11.
# Multiply by 2 or not for spin → factor of 2.

count_by_max = {0: 0, 3: 0, 5: 0, 7: 0, 11: 0}
for choices, d in divisors:
    no_2_part = d if choices[0] == 0 else d // 2
    if no_2_part == 1:
        count_by_max[0] += 1
    else:
        # find max prime in {3, 5, 7, 11}
        max_p = 0
        for p in [3, 5, 7, 11]:
            if no_2_part % p == 0:
                max_p = p
        count_by_max[max_p] += 1

print("Divisors of Z/2310 grouped by 'max prime in non-2 part' (× spin doubling):")
for max_p, c in count_by_max.items():
    print(f"  max prime {max_p}: {c} divisors")

# Sum = 32. Matches.
# But the distribution: 0 → 2 (1 + spin-double), 3 → ?, 5 → ?, 7 → ?, 11 → ?
# Want: 2 (s), 6 (p), 10 (d), 14 (f), and... 0 for l=5.

# Let me compute properly — count of divisors having max-prime = X:
# Fix prime X as max. Remaining primes {3,5,7,11} ∖ {X} for which X is max.
# For X=3: only X=3. Other primes with X as max = {2}. So divisors with 3 as max
#   = divisors {2^a · 3} where a ∈ {0, 1}. 2 divisors.
# For X=5: {2,3} can be in/out. 4 divisors with 5 as max.
# For X=7: {2,3,5} can be in/out. 8 divisors.
# For X=11: {2,3,5,7} can be in/out. 16 divisors.
# For X=0 (no non-2 primes): just 1 and 2. 2 divisors.

# Total: 2 + 2 + 4 + 8 + 16 = 32. ✓

# Wanted: 2 (s, l=0), 6 (p, l=1), 10 (d, l=2), 14 (f, l=3).
# Got: 2, 2, 4, 8, 16.
# Doesn't match. (s OK, but p needs 6 from 2 — off by 4.)

# Try DIFFERENT assignment of primes to l-values:
# Maybe primes label DIFFERENTLY. Let's enumerate possibilities.

# We need: p (3 substates × 2 spin = 6 electrons)
#         d (5 × 2 = 10)
#         f (7 × 2 = 14)
# Substrate strands matching multiplicities: 3, 5, 7. So:
#   prime 3 → p
#   prime 5 → d
#   prime 7 → f

# But divisor count by max-prime is 2, 2, 4, 8, 16 — not 2, 6, 10, 14.

# Alternative: each subshell uses MULTIPLE primes.
# p has 3 substates: maybe represented by 3 specific divisors, not by "max prime = 3".
# Try: p-states = divisors having product / 2 ∈ {3, 6, ?}. Need 3 divisors.

# Or: divisors that EQUAL a specific value:
#   l=0 (m=0, ±): {1, 2} → 2 divisors. Match.
#   l=1 (m=-1,0,+1, ±): need 6 divisors.

# I don't see an obvious clean bijection. Let me try a structurally
# different idea: maybe the divisor count doesn't bijection onto
# electron states, but onto SOMETHING ELSE that happens to also be 32.

print()
print("="*84)
print("CONCLUSION")
print("="*84)
print("""
Direct bijection between Z/2310 divisors and n=4 electron states is not
clean by:
  - Hamming weight grouping
  - max-prime grouping  
  - prime-as-l-label grouping

The integer match 32=32 holds, but the GROUPING STRUCTURE differs:
  Substrate divisors group as 1, 5, 10, 10, 5, 1 (binomial)
  Electron states group as 2, 6, 10, 14 (Pauli per subshell)
  
The 10 in both is interesting (both give 10). But 1 vs 2, 5 vs 6, 10 vs 14
don't match.

So the integer coincidence 2n²=2^k at n=4, depth 3 is REAL but the
structural bijection doesn't fall out trivially. Either:
  (a) the bijection requires a different combinatorial structure not 
      directly using divisors
  (b) the integer coincidence is a Pascal-triangle-type number-theoretic
      accident, not a structural identity
  (c) the bijection exists but uses additional substrate structure 
      (e.g., σ-orbits) that we haven't tapped

This is an HONEST NEGATIVE for Priority 1 as stated. The map exists at the
integer level (32=32) but not at the combinatorial-decomposition level.
""")

