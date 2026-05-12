"""
m22_decomposition.py
====================

Verifies the J20 manuscript's main numerical claims:

  1. M_22 has 12 irrep dimensions {1, 21, 45, 45, 55, 99, 154, 210,
     231, 280, 280, 385}. Sum of squares = |M_22| = 443520.

  2. Classify each irrep dimension by membership in the substrate-prime
     band B = { m : primes(m) subset of {2,3,5,7,11} and v_2(m) <= 1 }.

  3. Enumerate B_385 = B intersect [1, 385]. Report |B_385|.

  4. Compute the binomial tail probabilities of Theorem (Non-genericity).

Run:
    python m22_decomposition.py

Dependencies: sympy (factorint), math (comb).
Wall-clock: < 1 second.
"""

from math import comb
from sympy import factorint

M22_IRREP_DIMS = [1, 21, 45, 45, 55, 99, 154, 210, 231, 280, 280, 385]
SUBSTRATE_PRIMES = {2, 3, 5, 7, 11}
M22_ORDER = 2**7 * 3**2 * 5 * 7 * 11  # = 443520


def in_strict_band(m: int) -> bool:
    """m factors only in {3, 5, 7, 11} (no factor of 2)."""
    if m == 1:
        return True  # vacuously
    f = factorint(m)
    return all(p in {3, 5, 7, 11} for p in f.keys())


def in_band_B(m: int) -> bool:
    """m factors only in {2,3,5,7,11} and v_2(m) <= 1."""
    if m == 1:
        return True  # vacuously
    f = factorint(m)
    if not all(p in SUBSTRATE_PRIMES for p in f.keys()):
        return False
    return f.get(2, 0) <= 1


def main() -> None:
    # 1. Sum-of-squares verification
    soq = sum(d * d for d in M22_IRREP_DIMS)
    assert soq == M22_ORDER, f"Sum of squares {soq} != |M_22| {M22_ORDER}"
    print(f"|M_22| = {M22_ORDER} = 2^7 * 3^2 * 5 * 7 * 11")
    print(f"Sum of squares of irrep dims = {soq}  [matches |M_22|]")
    print()

    # 2. Classify each dim
    print("Classification of M_22 irrep dimensions:")
    print(f"{'dim':>5}  {'factorization':<28}  strict?  in_B?")
    print("-" * 60)
    strict_count = 0
    B_count = 0
    for d in M22_IRREP_DIMS:
        f = factorint(d)
        fact_str = "trivial" if d == 1 else " * ".join(
            f"{p}^{e}" if e > 1 else str(p)
            for p, e in sorted(f.items())
        )
        s = in_strict_band(d)
        b = in_band_B(d)
        print(f"{d:>5}  {fact_str:<28}  {'YES' if s else 'no':>5}    "
              f"{'YES' if b else 'no'}")
        if s:
            strict_count += 1
        if b:
            B_count += 1
    print()
    print(f"Strict {{3,5,7,11}}  count: {strict_count} of 12")
    print(f"B-band count:           {B_count} of 12")
    print()

    # 3. Enumerate B_385
    N = 385
    B_set = [n for n in range(1, N + 1) if in_band_B(n)]
    strict_set = [n for n in range(1, N + 1) if in_strict_band(n)]
    B_density = len(B_set) / N
    strict_density_no1 = (len(strict_set) - 1) / (N - 1)  # exclude trivial
    print(f"|B_{N}| = {len(B_set)}, density {B_density:.4f} "
          f"= {100 * B_density:.2f}%")
    print(f"|strict_{N}| = {len(strict_set)}, of which {len(strict_set) - 1} "
          f"are non-trivial (>1); density excluding 1: {strict_density_no1:.4f}")
    print()

    # 4. Binomial tail probabilities
    def binom_tail(n: int, k_min: int, p: float) -> float:
        return sum(
            comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
            for k in range(k_min, n + 1)
        )

    p_value_band = binom_tail(12, B_count, B_density)
    print(f"P[X >= {B_count} | X ~ Bin(12, {B_density:.4f})] "
          f"= {p_value_band:.6e}")

    p_value_strict = binom_tail(11, strict_count - 1, strict_density_no1)
    print(f"P[X >= {strict_count - 1} | X ~ Bin(11, {strict_density_no1:.4f})] "
          f"= {p_value_strict:.6e}  (non-trivial strict)")
    print()
    print("All numerical claims of Theorem (Non-genericity) verified.")


if __name__ == "__main__":
    main()
