"""sigma_k12_embedding.py -- test if the sigma-magma has any natural
embedding into the K_12 (Coxeter-Todd) lattice's automorphism group.

The full Aut(K_12) has order 78,382,080 = 2^9 * 3^6 * 5 * 7 * 11 * 13.
The number "19,440 = 432*45 = 2^4 * 3^5 * 5" referenced in the U-task brief
matches the order of |W(F_4) x Z_5| or a similar small subgroup; we test
several candidate subgroup orders dividing |Aut(K_12)|.

Candidate embeddings:
  (1) sigma-magma's underlying Z_10 -> Aut(K_12) (necessary condition: 10 | |G|).
  (2) sigma as a permutation in S_10 -> permutation rep of Aut(K_12).
  (3) sigma-magma quasigroup -> sub-quasigroup of some abelian subgroup.

We DON'T attempt to enumerate Aut(K_12) directly (impractical); instead
we check structural compatibility conditions.
"""
import sys
import os
from math import gcd

if hasattr(sys.stdout, "reconfigure"):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

SIGMA = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
N = 10

# |Aut(K_12)| factorization
AUT_K12 = 78_382_080
AUT_K12_FACTORS = [(2, 9), (3, 6), (5, 1), (7, 1), (11, 1), (13, 1)]


def magma_diamond(x, y):
    return SIGMA[(x + y) % N]


def perm_order(p):
    """Order of permutation p in S_n."""
    visited = [False] * len(p)
    cycles = []
    for i in range(len(p)):
        if visited[i]:
            continue
        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            cycle_len += 1
            j = p[j]
        cycles.append(cycle_len)
    from functools import reduce
    return reduce(lambda a, b: a*b//gcd(a, b), cycles, 1), cycles


def is_associative(t):
    n = len(t)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if t[t[a][b]][c] != t[a][t[b][c]]:
                    return False, (a, b, c)
    return True, None


def is_commutative(t):
    n = len(t)
    return all(t[i][j] == t[j][i] for i in range(n) for j in range(n))


def is_quasigroup(t):
    n = len(t)
    for i in range(n):
        if set(t[i]) != set(range(n)):
            return False
        if {t[k][i] for k in range(n)} != set(range(n)):
            return False
    return True


def main():
    print("="*70)
    print("  sigma-magma K_12 lattice embedding test")
    print("="*70)

    # ---------- Test 1: sigma as permutation -----------
    print("\n[1] sigma as a permutation of {0,...,9}:")
    print(f"    sigma = {SIGMA}")
    order, cycles = perm_order(SIGMA)
    print(f"    cycle structure: {cycles}  (sorted: {sorted(cycles, reverse=True)})")
    print(f"    order of sigma: {order}")
    # K_12 has elements of order dividing |Aut(K_12)|.
    # Element of order 6 is plausible (6 | |Aut(K_12)|).
    if AUT_K12 % order == 0:
        print(f"    PASS: {order} divides |Aut(K_12)| = {AUT_K12}")
    else:
        print(f"    FAIL: {order} does NOT divide |Aut(K_12)|")

    # ---------- Test 2: sigma-magma table structure ----------
    print("\n[2] sigma-magma operation table structure:")
    t = [[magma_diamond(i, j) for j in range(N)] for i in range(N)]
    print(f"    commutative: {is_commutative(t)}")
    is_assoc, witness = is_associative(t)
    print(f"    associative: {is_assoc}")
    if not is_assoc:
        a, b, c = witness
        print(f"      witness: ({a}*{b})*{c} = {t[t[a][b]][c]} != {a}*({b}*{c}) = {t[a][t[b][c]]}")
    print(f"    quasigroup (Latin square): {is_quasigroup(t)}")

    print()
    print(f"    --> sigma-magma is a commutative non-associative quasigroup of order 10.")
    print(f"    --> sigma-magma is NOT a group, so it cannot be an embedded subgroup of")
    print(f"        any group, including Aut(K_12).")

    # ---------- Test 3: underlying additive structure ----------
    print("\n[3] Underlying additive structure Z_10:")
    print(f"    Z_10 has order 10 = 2 * 5.")
    print(f"    |Aut(K_12)| = {AUT_K12} = 2^9 * 3^6 * 5 * 7 * 11 * 13.")
    print(f"    Z_10 = Z_2 x Z_5 (since gcd(2, 5) = 1).")
    print(f"    Z_2 embeds in Aut(K_12) trivially (order 2 elements exist).")
    print(f"    Z_5 embeds in Aut(K_12) trivially (order 5 elements exist).")
    print(f"    So Z_10 abstractly embeds, but the embedding is not unique or natural.")

    # ---------- Test 4: divisibility check for sigma-magma's 'algebraic image' ----------
    print("\n[4] Compatibility with Aut(K_12) algebraic structure:")
    # sigma-magma has 100 distinct (x,y,x*y) triples.
    # For an embedding ι: sigma-magma -> G, we need ι(x*y) = ι(x) op_G ι(y) for some op_G.
    # If op_G is a group operation (associative), then x*y must be associative -- false.
    # So no straightforward embedding exists.
    print(f"    Since sigma-magma is non-associative, any embedding ι into a GROUP")
    print(f"    fails: the image would have to be associative, contradicting our")
    print(f"    counterexample at ({witness[0]}*{witness[1]})*{witness[2]} != {witness[0]}*({witness[1]}*{witness[2]}).")

    # ---------- Test 5: could sigma-magma act as a permutation rep? ----------
    print("\n[5] sigma-magma as a permutation representation:")
    print(f"    Each row L_a (= x -> a*x) is a permutation of {{0..9}}.")
    perms = []
    for a in range(N):
        row = t[a]
        order_a, cycles_a = perm_order(row)
        perms.append((a, order_a, sorted(cycles_a, reverse=True)))
        print(f"    row {a}: order {order_a}, cycles {sorted(cycles_a, reverse=True)}")

    # Does the set of left-translation permutations form a subgroup?
    # For a GROUP, the LR rep is a subgroup of S_n; for a magma, generally not.
    # Check if {L_a : a in Z_10} is closed under composition.
    print("\n    Check if {L_a : a in Z_10} closed under composition:")
    L = [t[a] for a in range(N)]
    Lset = {tuple(l) for l in L}
    closed = True
    for a in range(N):
        for b in range(N):
            # composition: L_a o L_b means apply L_b first, then L_a
            comp = tuple(L[a][L[b][x]] for x in range(N))
            if comp not in Lset:
                closed = False
                break
        if not closed:
            break
    print(f"    closed under composition: {closed}")
    if not closed:
        print(f"    --> {{L_a}} is NOT a subgroup of S_10.")
        print(f"    --> Cannot embed sigma-magma via left-regular representation.")

    # ---------- Summary ----------
    print("\n" + "="*70)
    print("  SUMMARY")
    print("="*70)
    print()
    print("  Q: Does the sigma-magma have a natural embedding into Aut(K_12)?")
    print()
    print("  A: NO, with three independent obstructions:")
    print()
    print("  1. The sigma-magma is NON-ASSOCIATIVE. No embedding into any GROUP")
    print("     (including Aut(K_12)) can preserve its diamond operation, since")
    print("     groups are associative.")
    print()
    print("  2. The sigma-magma's automorphism group is TRIVIAL (|Aut| = 1, J60).")
    print("     So sigma-magma has no non-trivial group action on it; it sits")
    print("     ALGEBRAICALLY ISOLATED.")
    print()
    print("  3. The left-regular representation {L_a : a in Z_10} is NOT closed")
    print("     under composition (since sigma-magma is non-associative). So even")
    print("     the natural quasigroup permutation embedding fails.")
    print()
    print("  CONCLUSION: sigma-magma's underlying additive set Z_10 trivially")
    print("  embeds as a cyclic subgroup of order 10 in Aut(K_12), but this")
    print("  embedding does NOT preserve the diamond operation.")
    print()
    print("  No 'natural' (operation-preserving) embedding exists.")


if __name__ == "__main__":
    main()
