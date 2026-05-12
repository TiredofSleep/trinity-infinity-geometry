"""J42 verification: discrete sinc^2 identity at machine precision.

Checks Theorem 3.1 (closed form), Corollary 4.2 (first zero unrestricted to f >= 2),
and the special value sinc^2(1/10) = 25(sqrt(5)-1)^2/(4*pi^2) ~ 0.9675.
"""
import numpy as np
from sympy import sqrt, pi


def R_geom(k: int, f: int) -> float:
    """Direct geometric-sum evaluation of R(k, f)."""
    j = np.arange(1, k + 1)
    s = np.sum(np.exp(2j * np.pi * j / f))
    return abs(s) ** 2 / (k * k)


def R_closed(k: int, f: int) -> float:
    """Closed-form Fejer-kernel evaluation of R(k, f)."""
    return np.sin(np.pi * k / f) ** 2 / (k * k * np.sin(np.pi / f) ** 2)


def main() -> None:
    # ------------------------------------------------------------------
    # Theorem 3.1 — closed form matches geometric sum at machine precision.
    # Verification covers prime AND composite f.
    # ------------------------------------------------------------------
    max_dev = 0.0
    test_f = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19, 23]
    for f in test_f:
        for k in range(1, f + 2):
            if k == f:
                # closed-form is 0/0 numerically at k = f; geometric sum is 0
                dev = abs(R_geom(k, f))
            else:
                dev = abs(R_geom(k, f) - R_closed(k, f))
            max_dev = max(max_dev, dev)
    print(f"Theorem 3.1: max deviation across f in {test_f}, k in [1..f+1]: {max_dev:.2e}")
    assert max_dev < 1e-12, f"Closed form failed (max dev {max_dev:.2e})"

    # ------------------------------------------------------------------
    # Corollary 4.2 (UNRESTRICTED): first zero of R(., f) at k = f for all f >= 2.
    # The prime restriction in the original draft was unnecessary.
    # ------------------------------------------------------------------
    for f in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]:
        for k in range(1, f):
            assert R_closed(k, f) > 0, f"Unexpected zero at f={f}, k={k}"
        # at k = f, R = 0 (closed form is 0/0; geometric sum gives 0)
        assert abs(R_geom(f, f)) < 1e-12, f"Expected zero at k=f={f}"
    print("Corollary 4.2 (unrestricted, f >= 2): first zero at k = f confirmed for f in [2..15].")

    # ------------------------------------------------------------------
    # Special value sinc^2(1/10) = 25(sqrt(5)-1)^2 / (4*pi^2) ~ 0.9675
    # NOT 0.9355 (the value originally printed in the manuscript was wrong).
    # ------------------------------------------------------------------
    closed_sym = 25 * (sqrt(5) - 1) ** 2 / (4 * pi ** 2)
    val_sym = float(closed_sym)
    val_direct = np.sin(np.pi / 10) ** 2 / (np.pi / 10) ** 2
    print(f"sinc^2(1/10) closed form (sympy): {val_sym:.10f}")
    print(f"sinc^2(1/10) direct numeric     : {val_direct:.10f}")
    assert abs(val_sym - 0.9675312093) < 1e-9, "sinc^2(1/10) closed form value wrong"
    assert abs(val_direct - 0.9675312093) < 1e-9, "sinc^2(1/10) direct value wrong"
    print("Special value sinc^2(1/10) ~ 0.9675 (corrected from manuscript's 0.9355).")

    # ------------------------------------------------------------------
    # Proposition 5.1 — synchronization with First-G event.
    # For b > 1 with smallest prime factor p_1, first integer k with R(k, p_1) = 0
    # equals p_1, which equals the First-G event of b.
    # ------------------------------------------------------------------
    test_b = [(6, 2), (10, 2), (15, 3), (21, 3), (22, 2), (35, 5), (105, 3)]
    for b, p1_expected in test_b:
        # smallest prime factor of b
        p1 = 2
        while b % p1 != 0:
            p1 += 1
        assert p1 == p1_expected, f"spf({b}) computed {p1}, expected {p1_expected}"
        # first zero of R(., p_1)
        first_zero = next(k for k in range(1, p1 + 1) if abs(R_geom(k, p1)) < 1e-12)
        assert first_zero == p1, f"First zero of R(., {p1}) is {first_zero}, expected {p1}"
    print("Proposition 5.1: synchronization k*(b) = p_1 verified for b in {6, 10, 15, 21, 22, 35, 105}.")

    print("\nAll J42 verifications PASSED.")


if __name__ == "__main__":
    main()
