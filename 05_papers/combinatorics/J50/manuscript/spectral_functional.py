"""
spectral_functional.py
======================

Verifies the J21 manuscript's spectral functional values
(Table 1, Lemma 5.2 corrected statement).

The functional G(n) is defined for each n in Z/10Z by

    G(n) = | sum_{j=0}^{4} omega^j * chi_1(y(sigma^j(n))) |^2

with omega = e^(2 pi i / 5), chi_1(y) = e^(2 pi i y / 5),
y(m) = m mod 5, and sigma the order-6 permutation
sigma = (0)(3)(8)(9)(1 7 6 5 4 2) of Z/10Z.

Table 1 in the manuscript reports:
  n=0: 0.000        n=5: 9.472
  n=1: 10.528       n=6: 16.708
  n=2: 3.292        n=7: 19.472   (global max)
  n=3: 0.000        n=8: 0.000
  n=4: 5.000        n=9: 0.000

This script computes G(n) for each n and asserts agreement.

Run:
    python spectral_functional.py
"""

import numpy as np

# sigma : Z/10Z -> Z/10Z (cycle structure (0)(3)(8)(9)(1 7 6 5 4 2))
# 1 -> 7, 7 -> 6, 6 -> 5, 5 -> 4, 4 -> 2, 2 -> 1; 0, 3, 8, 9 fixed.
SIGMA = {0: 0, 3: 3, 8: 8, 9: 9,
         1: 7, 7: 6, 6: 5, 5: 4, 4: 2, 2: 1}


def y_coord(n: int) -> int:
    """y(n) = n mod 5."""
    return n % 5


def G_value(n: int) -> float:
    """Compute G(n) directly from the definition."""
    omega = np.exp(2j * np.pi / 5)
    nj = n
    s = 0 + 0j
    for j in range(5):
        chi1_yj = np.exp(2j * np.pi * y_coord(nj) / 5)
        s += (omega ** j) * chi1_yj
        nj = SIGMA[nj]
    return abs(s) ** 2


def main() -> None:
    expected = {
        0: 0.000,
        1: 10.528,
        2: 3.292,
        3: 0.000,
        4: 5.000,
        5: 9.472,
        6: 16.708,
        7: 19.472,
        8: 0.000,
        9: 0.000,
    }

    print("Spectral functional G(n) for n in Z/10Z:")
    print(f"{'n':>2}  {'epsilon':>7}  {'y':>3}  {'G(n)':>10}  {'expected':>10}")
    print("-" * 50)
    g_values = {}
    for n in range(10):
        g = G_value(n)
        g_values[n] = g
        eps = n % 2
        y = y_coord(n)
        print(f"{n:>2}  {eps:>7}  {y:>3}  {g:>10.4f}  {expected[n]:>10.3f}")

    # Assertions
    for n, exp in expected.items():
        assert abs(g_values[n] - exp) < 0.005, (
            f"G({n}) = {g_values[n]:.4f}, expected {exp}"
        )

    # Maximum is at n=7
    n_max = max(g_values, key=g_values.get)
    print()
    print(f"Global maximum: G({n_max}) = {g_values[n_max]:.4f}")
    assert n_max == 7, f"Expected max at n=7, got n={n_max}"

    # Zero set
    zeros = sorted(n for n in g_values if g_values[n] < 1e-10)
    print(f"Zero set (G(n) = 0): {zeros}")
    assert zeros == [0, 3, 8, 9], (
        f"Expected zeros at sigma-fixed indices {{0, 3, 8, 9}}, got {zeros}"
    )

    print()
    print("All values match Table 1; max at n=7; zeros at sigma-fixed "
          "{0, 3, 8, 9}.")
    print("Lemma 5.2 (corrected) verified.")


if __name__ == "__main__":
    main()
