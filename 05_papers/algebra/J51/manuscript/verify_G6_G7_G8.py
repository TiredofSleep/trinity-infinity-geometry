"""J43 verification: G6 (sigma^6 = id), G7 (period bimodal 2/5, 3/5),
G8 (three-valued G(s) with corrected partition: HIGH on {4,7}, LOW on {1,2,5,6}).
"""
import cmath
import math


# Canonical sigma and chi (from manuscript section 1, 4.1)
sigma = {0: 0, 3: 3, 8: 8, 9: 9, 1: 7, 7: 6, 6: 5, 5: 4, 4: 2, 2: 1}
chi = {0: 0, 3: 0, 8: 0, 9: 0, 1: +1, 4: +1, 2: -1, 5: -1, 6: -1, 7: -1}
omega = cmath.exp(2j * math.pi / 9)


def apply_sigma(s: int, k: int) -> int:
    cur = s
    for _ in range(k):
        cur = sigma[cur]
    return cur


def G_complex(s: int) -> complex:
    cur = s
    total = 0
    for j in range(9):
        total += (omega ** j) * chi[cur]
        cur = sigma[cur]
    return total


def G(s: int) -> float:
    return abs(G_complex(s)) ** 2


def main() -> None:
    # ------------------------------------------------------------------
    # G6: sigma^6 = id on Z/10Z
    # ------------------------------------------------------------------
    for s in range(10):
        assert apply_sigma(s, 6) == s, f"sigma^6({s}) != {s}"
    print("G6: sigma^6 = id confirmed on all of Z/10Z.")

    # ------------------------------------------------------------------
    # G7: period bimodal {1: 2/5, 6: 3/5}; mean 4; var 6
    # ------------------------------------------------------------------
    periods = {}
    for s in range(10):
        for k in range(1, 7):
            if apply_sigma(s, k) == s:
                periods[s] = k
                break
    n1 = sum(1 for p in periods.values() if p == 1)
    n6 = sum(1 for p in periods.values() if p == 6)
    assert n1 == 4, f"P(tau=1) count {n1}, expected 4"
    assert n6 == 6, f"P(tau=6) count {n6}, expected 6"
    mean = sum(periods.values()) / 10
    var = sum((p - mean) ** 2 for p in periods.values()) / 10
    assert mean == 4.0, f"Mean {mean} != 4"
    assert var == 6.0, f"Var {var} != 6"
    print(f"G7: P(tau=1)=2/5, P(tau=6)=3/5; mean={mean}, var={var}.")

    # ------------------------------------------------------------------
    # G8: three-valued G(s) with CORRECTED partition.
    # ZERO on {0,3,8,9}; LOW on {1,2,5,6} ~ 1.872; HIGH on {4,7} ~ 9.389.
    # ------------------------------------------------------------------
    G_vals = {s: G(s) for s in range(10)}
    zero_states = sorted(s for s in range(10) if G_vals[s] < 1e-10)
    low_states = sorted(s for s in range(10) if 1.0 < G_vals[s] < 5.0)
    high_states = sorted(s for s in range(10) if G_vals[s] > 5.0)
    assert zero_states == [0, 3, 8, 9], f"ZERO  states: {zero_states}"
    assert low_states == [1, 2, 5, 6], f"LOW   states: {low_states}"
    assert high_states == [4, 7], f"HIGH  states: {high_states}"
    G_low = G_vals[1]
    G_high = G_vals[4]
    assert abs(G_low - 1.871644) < 1e-4, f"G_low {G_low}"
    assert abs(G_high - 9.389185) < 1e-4, f"G_high {G_high}"
    print(f"G8: ZERO on {zero_states}; LOW on {low_states} ~ {G_low:.6f}; HIGH on {high_states} ~ {G_high:.6f}.")
    print(f"    Ratio G_high/G_low = {G_high/G_low:.4f}")

    # ------------------------------------------------------------------
    # Sigma^3 pairing: G(s) = G(sigma^3(s)) on the 6-cycle.
    # The 2-cycles of sigma^3 on the 6-cycle are {1,5}, {2,6}, {4,7}.
    # ------------------------------------------------------------------
    sigma3_pairs = [(1, 5), (2, 6), (4, 7)]
    for a, b in sigma3_pairs:
        assert apply_sigma(a, 3) == b, f"sigma^3({a}) = {apply_sigma(a,3)}, expected {b}"
        assert abs(G_vals[a] - G_vals[b]) < 1e-10, f"G({a}) != G({b})"
        # Complex amplitudes differ by sign: G_cplx(b) = -G_cplx(a)
        assert abs(G_complex(a) + G_complex(b)) < 1e-10, \
            f"G_cplx({a}) + G_cplx({b}) = {G_complex(a) + G_complex(b)} != 0"
    print(f"Sigma^3 pairing {sigma3_pairs}: |G(a)| = |G(b)| within each pair (verified algebraically).")

    # ------------------------------------------------------------------
    # nu_+ discriminator (manuscript §4.3): the high-locus {4, 7} is exactly
    # the set of starting states whose first three sigma-orbit positions have
    # an extremal +1 count nu_+ = 0 or nu_+ = 2 (rather than the typical 1).
    # The 9-step sum visits the orbit's first three positions twice, weighting
    # them in the spectral-coherence integral G(s).
    # ------------------------------------------------------------------
    print()
    print("nu_+ discriminator (count of chi=+1 in first 3 orbit positions):")
    nu_plus = {}
    for s in [1, 2, 4, 5, 6, 7]:
        cur = s
        first_three = []
        for _ in range(3):
            first_three.append(cur)
            cur = sigma[cur]
        chi_first3 = [chi[x] for x in first_three]
        nu = sum(1 for v in chi_first3 if v == 1)
        nu_plus[s] = nu
        marker = " <-- high-locus (extremal nu)" if s in {4, 7} else ""
        print(f"  s={s}: first3={first_three}  chi={chi_first3}  nu_+={nu}{marker}")
    # Verify the claim: high-locus = extremal nu_+
    extremal = {s for s, nu in nu_plus.items() if nu in {0, 2}}
    assert extremal == {4, 7}, f"extremal nu_+ states {extremal}, expected {{4, 7}}"
    print("Verified: nu_+ = 0 or 2 occurs exactly on s in {4, 7}; nu_+ = 1 on s in {1, 2, 5, 6}.")

    print("\nAll J43 verifications PASSED.")


if __name__ == "__main__":
    main()
