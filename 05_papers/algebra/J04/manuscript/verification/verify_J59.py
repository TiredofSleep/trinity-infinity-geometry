"""verify_J59.py -- machine-precision verification of the four
rigidity theorems for the sigma-magma at order 10.

CC-BY-4.0. (c) 2026 Brayden Ross Sanders / 7Site LLC. M. Gish co-author.

Verifies (Theorems A, B, C, D):
  A. The sigma-magma has trivial automorphism group: |Aut| = 1.
  B. The sigma-magma is congruence-simple: only 2 magma congruences
     (identity + universal).
  C. The sigma-magma has exactly 5 sub-magmas: {0}, {1}, {2}, {1, 6},
     and the full magma. The {1, 6} sub-magma is the unique non-trivial
     proper sub-magma; it is isomorphic to Z/2.
  D. The sigma-magma is 2-generated; {1, 6} is the unique 2-element
     non-generating subset.

Run:  python verify_J59.py
Runtime: ~3 seconds on a 2020-era laptop.
"""
from itertools import permutations, combinations
import time


SIGMA = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
N = 10


def diamond(x, y):
    return SIGMA[(x + y) % N]


def check_homomorphism(pi):
    """Is pi a magma homomorphism?"""
    for x in range(N):
        for y in range(N):
            if pi[diamond(x, y)] != diamond(pi[x], pi[y]):
                return False
    return True


def all_partitions(s):
    """Yield all set partitions of list s (as list of lists)."""
    if not s:
        yield []
        return
    first = s[0]
    rest = s[1:]
    for p in all_partitions(rest):
        # Add first to each existing block
        for i in range(len(p)):
            new_p = [list(b) for b in p]
            new_p[i].append(first)
            yield new_p
        # Or as singleton
        yield [[first]] + [list(b) for b in p]


def check_congruence(partition):
    """Is the partition a magma congruence (substitutivity)?"""
    c_idx = [0] * N
    for i, block in enumerate(partition):
        for x in block:
            c_idx[x] = i
    for a in range(N):
        for b in range(N):
            for a2 in range(N):
                if c_idx[a] != c_idx[a2]:
                    continue
                if c_idx[diamond(a, b)] != c_idx[diamond(a2, b)]:
                    return False
            for b2 in range(N):
                if c_idx[b] != c_idx[b2]:
                    continue
                if c_idx[diamond(a, b)] != c_idx[diamond(a, b2)]:
                    return False
    return True


def is_sub_magma(S):
    for x in S:
        for y in S:
            if diamond(x, y) not in S:
                return False
    return True


def find_all_sub_magmas():
    subs = []
    for size in range(1, N + 1):
        for subset in combinations(range(N), size):
            S = set(subset)
            if is_sub_magma(S):
                subs.append(tuple(sorted(S)))
    return subs


def gens_full(seeds):
    """Returns True iff iterating diamond from seeds eventually yields all of {0..N-1}."""
    S = set(seeds)
    while True:
        new_S = set(S)
        for x in S:
            for y in S:
                new_S.add(diamond(x, y))
        if new_S == S:
            return False  # stable proper subset
        S = new_S
        if S == set(range(N)):
            return True


def main():
    t0 = time.time()
    print("=" * 64)
    print(" J59 verification -- rigidity theorems for the sigma-magma")
    print("=" * 64)
    print(f"  sigma = {SIGMA}")
    print(f"  operation: x diamond y = sigma((x+y) mod 10)")
    print()

    checks = []

    # CHECK 1 (Theorem A: |Aut| = 1)
    t1 = time.time()
    print("CHECK 1: Theorem A -- |Aut(sigma-magma)| = 1", flush=True)
    aut_count = 0
    for pi in permutations(range(N)):
        if check_homomorphism(pi):
            aut_count += 1
    print(f"  Searched 10! = {sum(1 for _ in permutations(range(N)))} permutations "
          f"in {time.time() - t1:.1f}s", flush=True)
    print(f"  |Aut| = {aut_count}")
    checks.append(("Theorem A (|Aut| = 1)", aut_count == 1))
    print()

    # CHECK 2 (Theorem B: congruence-simple)
    t2 = time.time()
    print("CHECK 2: Theorem B -- exactly 2 magma congruences (identity + universal)",
          flush=True)
    n_congruences = 0
    for partition in all_partitions(list(range(N))):
        if check_congruence(partition):
            n_congruences += 1
    print(f"  Searched Bell(10) = 115,975 partitions in {time.time() - t2:.1f}s",
          flush=True)
    print(f"  Number of congruences = {n_congruences}")
    checks.append(("Theorem B (congruence-simple, 2 congruences)",
                   n_congruences == 2))
    print()

    # CHECK 3 (Theorem C: exactly 5 sub-magmas)
    t3 = time.time()
    print("CHECK 3: Theorem C -- exactly 5 sub-magmas with {1, 6} as unique non-trivial proper",
          flush=True)
    subs = find_all_sub_magmas()
    print(f"  Searched 2^10 = 1024 subsets in {time.time() - t3:.1f}s", flush=True)
    print(f"  Sub-magmas found: {len(subs)}")
    for s in subs:
        print(f"    {set(s)}")
    proper = [s for s in subs if 1 < len(s) < N]
    expected = {(1, 6)}
    checks.append(("Theorem C (5 sub-magmas, {1,6} unique non-trivial proper)",
                   len(subs) == 5 and set(proper) == expected))
    print()

    # CHECK 4 (Theorem D: 2-generated, {1, 6} unique non-gen pair)
    t4 = time.time()
    print("CHECK 4: Theorem D -- 2-generated; {1, 6} is the unique non-generating pair",
          flush=True)
    non_gen = []
    for a, b in combinations(range(N), 2):
        if not gens_full([a, b]):
            non_gen.append((a, b))
    print(f"  Tested all 45 pairs in {time.time() - t4:.1f}s", flush=True)
    print(f"  Non-generating pairs: {non_gen}")
    checks.append(("Theorem D (2-generated, {1,6} unique non-generator)",
                   non_gen == [(1, 6)]))
    print()

    # Final report
    n_pass = sum(1 for _, ok in checks if ok)
    print("=" * 64)
    print(" Summary")
    print("=" * 64)
    for name, ok in checks:
        status = "PASS" if ok else "FAIL"
        print(f"  {status}: {name}")
    print()
    print(f"  Overall: {'PASS' if n_pass == len(checks) else 'FAIL'} "
          f"({n_pass}/{len(checks)})")
    print(f"  Total runtime: {time.time() - t0:.1f}s")

    return n_pass == len(checks)


if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
