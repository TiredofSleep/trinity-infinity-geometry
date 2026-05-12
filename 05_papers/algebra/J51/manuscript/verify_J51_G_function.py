"""J51 verification: Symbolic Return Theorem (sigma^6 = id) + three-valued G(s).

Tests the manuscript's central claims with the corrected partition:
- G(s) = 0 on the four anchors {0, 3, 8, 9}
- G(s) ~ 1.872 (G_low) on the sigma^3-orbits {1,5} U {2,6}
- G(s) ~ 9.389 (G_high) on the sigma^3-orbit {4,7}

Replaces the unrelated `proof_clay_rotation.py` (kept as supplementary context).
"""
import cmath
import math


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
    # Theorem 2.1 — Symbolic Return: sigma^6 = id on Z/10Z.
    # ------------------------------------------------------------------
    for s in range(10):
        assert apply_sigma(s, 6) == s, f"sigma^6({s}) != {s}"
    print("Theorem 2.1 (Symbolic Return): sigma^6 = id confirmed on Z/10Z.")

    # ------------------------------------------------------------------
    # Theorem 4.2 — Three-valued G(s) with the corrected partition.
    # HIGH at {4, 7}; LOW at {1, 2, 5, 6}; ZERO at {0, 3, 8, 9}.
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
    print(f"Theorem 4.2: three-valued image confirmed.")
    print(f"  ZERO on {zero_states}.")
    print(f"  LOW  on {low_states}, G_low  = {G_low:.6f}.")
    print(f"  HIGH on {high_states},   G_high = {G_high:.6f}.")
    print(f"  Ratio G_high / G_low = {G_high/G_low:.4f}")

    # ------------------------------------------------------------------
    # Sigma^3 pairing: G(s) = G(sigma^3(s)) on the 6-cycle.
    # The three 2-cycles of sigma^3 on {1,2,4,5,6,7} are {1,5}, {2,6}, {4,7}.
    # ------------------------------------------------------------------
    sigma3_pairs = [(1, 5), (2, 6), (4, 7)]
    for a, b in sigma3_pairs:
        assert apply_sigma(a, 3) == b, f"sigma^3({a}) = {apply_sigma(a,3)}, expected {b}"
        assert abs(G_vals[a] - G_vals[b]) < 1e-10, f"|G({a})| != |G({b})|"
        # Complex amplitudes differ by sign: G_cplx(b) = -G_cplx(a)
        assert abs(G_complex(a) + G_complex(b)) < 1e-10, \
            f"G_cplx({a}) + G_cplx({b}) = {G_complex(a) + G_complex(b)} != 0"
    print(f"Sigma^3 pairing {sigma3_pairs}: |G(a)| = |G(b)| within each pair (algebraically verified).")

    # ------------------------------------------------------------------
    # nu_+(s_0) discriminator: count of +1's in chi of first 3 orbit positions.
    # nu_+ = 1 on the LOW sigma^3-orbits; nu_+ in {0, 2} on the HIGH sigma^3-orbit.
    # ------------------------------------------------------------------
    print()
    print("Discriminator: chi-content of first 3 orbit positions.")
    print("  s | first 3 of orbit | chi-values         | nu_+")
    print("  --+------------------+-------------------+-----")
    nu_plus = {}
    for s0 in [1, 2, 4, 5, 6, 7]:
        first3_orbit = []
        cur = s0
        for _ in range(3):
            first3_orbit.append(cur)
            cur = sigma[cur]
        first3_chi = [chi[x] for x in first3_orbit]
        nu_plus[s0] = sum(1 for c in first3_chi if c == 1)
        marker = " <- HIGH" if s0 in {4, 7} else ""
        print(f"  {s0} | {tuple(first3_orbit)}        | {first3_chi}  | {nu_plus[s0]}{marker}")
    # Check claim: high-locus iff nu_+ in {0, 2}
    for s0 in [1, 2, 5, 6]:
        assert nu_plus[s0] == 1, f"Expected nu_+({s0}) = 1, got {nu_plus[s0]}"
    assert nu_plus[4] == 2, f"Expected nu_+(4) = 2, got {nu_plus[4]}"
    assert nu_plus[7] == 0, f"Expected nu_+(7) = 0, got {nu_plus[7]}"
    print()
    print("Discriminator confirmed: HIGH locus = {s0 : nu_+(s0) in {0, 2}}.")

    print("\nAll J51 verifications PASSED.")


if __name__ == "__main__":
    main()
