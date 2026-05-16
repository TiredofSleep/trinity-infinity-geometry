"""
Generate the explicit verification needed to upgrade Paper 01's proof
from informal sketch to mechanical verification with cell values.
"""
from canonical_tables import BHML_10, OPS

print("="*70)
print("EXPLICIT VERIFICATION FOR PAPER 01 §4")
print("="*70)
print()

# §4.1: prove {1,4,9} -> Z/10 in 2 steps with explicit cells
print("§4.1: {1,4,9} closure under BHML_10")
print()
S = {1, 4, 9}
print(f"S_0 = {sorted(S)}")
print()
print("Compositions for S_1 (commutative, so unordered pairs):")
new_elements_step1 = set()
for a in [1, 4, 9]:
    for b in [1, 4, 9]:
        if a <= b:  # commutative, only show unordered
            v = BHML_10[a][b]
            new_elements_step1.add(v)
            print(f"  BHML[{a}][{b}] = {v}  ({OPS[a]} ∘_B {OPS[b]} = {OPS[v]})")
S_1 = S | new_elements_step1
print(f"S_1 = {sorted(S_1)}")
print()

# Step 2
print("Compositions for S_2 (using S_1):")
S_1_list = sorted(S_1)
new_elements_step2 = set()
critical_cells = {}
for a in S_1_list:
    for b in S_1_list:
        if a <= b:
            v = BHML_10[a][b]
            if v not in S_1:
                # This is a new element produced
                if v not in critical_cells:
                    critical_cells[v] = (a, b)
            new_elements_step2.add(v)

S_2 = S_1 | new_elements_step2
print(f"  Critical new-element-producing cells:")
for v in sorted(critical_cells):
    a, b = critical_cells[v]
    print(f"    BHML[{a}][{b}] = {v}  ({OPS[a]} ∘_B {OPS[b]} = {OPS[v]})")
print(f"S_2 = {sorted(S_2)}")
print(f"S_2 = Z/10 ? {S_2 == set(range(10))}")
print()

# §4.2: prove {0,8,9} stalls at {0,7,8,9}
print("§4.2: {0,8,9} closure under BHML_10")
print()
print("Step 1 compositions:")
S = {0, 8, 9}
for a in sorted(S):
    for b in sorted(S):
        if a <= b:
            v = BHML_10[a][b]
            print(f"  BHML[{a}][{b}] = {v}  ({OPS[a]} ∘_B {OPS[b]} = {OPS[v]})")
S_1 = S | {BHML_10[a][b] for a in S for b in S}
print(f"S_1 = {sorted(S_1)}")
print()

# Now verify {0,7,8,9} is closed
print("Step 2: verify {0,7,8,9} is closed under BHML_10:")
four_core = [0, 7, 8, 9]
new_outside = set()
for a in four_core:
    for b in four_core:
        if a <= b:
            v = BHML_10[a][b]
            inside = "INSIDE" if v in four_core else "OUTSIDE"
            print(f"  BHML[{a}][{b}] = {v}  ({OPS[v]})  [{inside}]")
            if v not in four_core:
                new_outside.add(v)
print()
if not new_outside:
    print("  → 4-core {0,7,8,9} is CLOSED under BHML_10. ✓")
else:
    print(f"  ⚠ FAIL: new elements outside 4-core: {new_outside}")
print()

# §4.3: verify clause (c) by exhaustion
print("§4.3: exhaustive verification — no seed without 1 of size ≤ 3 generates Z/10")
print()
from itertools import combinations
total_seeds = 0
generators_without_1 = []
for size in [1, 2, 3]:
    for seed in combinations([i for i in range(10) if i != 1], size):
        total_seeds += 1
        # Iterate closure
        S = set(seed)
        for _ in range(20):  # plenty
            S_new = S | {BHML_10[a][b] for a in S for b in S}
            if S_new == S:
                break
            S = S_new
        if S == set(range(10)):
            generators_without_1.append(seed)

print(f"Total seeds tested (size 1, 2, or 3, not containing 1): {total_seeds}")
print(f"Seeds that generate Z/10: {len(generators_without_1)}")
if generators_without_1:
    print(f"  Counterexamples: {generators_without_1}")
else:
    print("  → No seed without 1 generates Z/10. Clause (c) verified by exhaustion. ✓")
