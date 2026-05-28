"""verify_qseries_merged.py -- consolidated verification for J_qseries_merged.

Combines verification of all five theorems of the merged Q-series paper:
  G_6  (Periodicity): sigma^6 = id on Z/10Z
  G_7  (Period Distribution): P(tau=1)=2/5, P(tau=6)=3/5
  G_8  (Three-Valued Coherence): G(s) takes 3 distinct values
  Q17-A (5D Fourier Embedding): Phi : Z/10Z -> R^5 injective
  Q17-B (Symbolic Return): corollary of G_6

Dependencies: NumPy only. Runtime: ~5 seconds.

Independent re-verification of J21, J43, J51 source results
combined into one runner.
"""
import sys
import numpy as np
from cmath import exp, pi


# ============================================================
# Setup: sigma permutation and chi character
# ============================================================
# sigma = (0)(3)(8)(9)(1 7 6 5 4 2)
SIGMA = {0: 0, 3: 3, 8: 8, 9: 9,
         1: 7, 7: 6, 6: 5, 5: 4, 4: 2, 2: 1}

# chi: Z/10Z -> {-1, 0, +1} (beta-exception character, canonical from J43)
CHI = {0: 0, 3: 0, 8: 0, 9: 0, 1: +1, 4: +1, 2: -1, 5: -1, 6: -1, 7: -1}


def sigma_iter(s, k):
    for _ in range(k):
        s = SIGMA[s]
    return s


# ============================================================
# G_6: sigma^6 = identity
# ============================================================

def check_G6():
    print("[G_6 Periodicity] sigma^6 = identity on Z/10Z")
    for s in range(10):
        assert sigma_iter(s, 6) == s, f"sigma^6({s}) != {s}"
    print("       PASS\n")


# ============================================================
# G_7: period distribution P(tau=1)=2/5, P(tau=6)=3/5
# ============================================================

def period(s):
    """Smallest k > 0 such that sigma^k(s) = s."""
    for k in range(1, 11):
        if sigma_iter(s, k) == s:
            return k
    return -1


def check_G7():
    print("[G_7 Period Distribution] bimodal {1, 6}")
    periods = [period(s) for s in range(10)]
    n_fixed = sum(1 for p in periods if p == 1)
    n_cycle6 = sum(1 for p in periods if p == 6)
    print(f"       fixed (tau=1): {n_fixed} ({n_fixed}/10 = {n_fixed/10})")
    print(f"       6-cycle (tau=6): {n_cycle6} ({n_cycle6}/10 = {n_cycle6/10})")
    assert n_fixed == 4 and n_cycle6 == 6, "period distribution mismatch"
    mean_tau = sum(periods) / 10
    var_tau = sum((p - mean_tau)**2 for p in periods) / 10
    print(f"       mean = {mean_tau} (expected 4)")
    print(f"       variance = {var_tau} (expected 6)")
    assert abs(mean_tau - 4.0) < 1e-9, "mean mismatch"
    assert abs(var_tau - 6.0) < 1e-9, "variance mismatch"
    print("       PASS\n")


# ============================================================
# G_8: three-valued G(s) coherence integral
# ============================================================

def G_complex(s):
    """G_cplx(s) = sum_{j=0..8} omega^j chi(sigma^j(s)) where omega = exp(2*pi*i/9)."""
    omega = exp(2j * pi / 9)
    total = 0 + 0j
    for j in range(9):
        total += (omega ** j) * CHI[sigma_iter(s, j)]
    return total


def G(s):
    return abs(G_complex(s)) ** 2


def check_G8():
    """Full check using canonical chi from J43."""
    print("[G_8 Three-Valued Coherence Integral]")
    values = {s: round(G(s), 6) for s in range(10)}
    print(f"       G values: {values}")
    # (1) Anchors give G = 0
    for s in [0, 3, 8, 9]:
        assert G(s) < 1e-9, f"G({s}) != 0"
    print("       (1) Anchors {0,3,8,9} give G = 0: PASS")
    # (2) sigma^3 pairing on 6-cycle
    assert SIGMA[SIGMA[SIGMA[1]]] == 5, "sigma^3(1) != 5"
    assert SIGMA[SIGMA[SIGMA[2]]] == 6, "sigma^3(2) != 6"
    assert SIGMA[SIGMA[SIGMA[4]]] == 7, "sigma^3(4) != 7"
    print("       (2) sigma^3 pairing {1,5}, {2,6}, {4,7}: PASS")
    # (3) Three-valued: LOW on {1,2,5,6}, HIGH on {4,7}
    g_low = G(1)
    g_high = G(4)
    assert abs(g_low - 1.871644) < 1e-4, f"G_low {g_low} != 1.871644"
    assert abs(g_high - 9.389185) < 1e-4, f"G_high {g_high} != 9.389185"
    print(f"       (3) G_low (orbits {{1,5}},{{2,6}}) = {g_low:.6f}")
    print(f"       (3) G_high (orbit {{4,7}}) = {g_high:.6f}")
    print(f"           ratio G_high / G_low = {g_high / g_low:.4f}")
    for orbit in [{1, 5}, {2, 6}, {4, 7}]:
        for s in orbit:
            ref = g_low if orbit != {4, 7} else g_high
            assert abs(G(s) - ref) < 1e-9, f"G({s}) != {ref}"
    print("       PASS\n")


# ============================================================
# Q17-A: 5D CRT Fourier Embedding
# ============================================================

def Phi(s):
    """5D embedding via CRT-aligned characters of Z/2 (-1) and Z/5 (5th roots)."""
    return (np.cos(2 * np.pi * s / 5),
            np.sin(2 * np.pi * s / 5),
            np.cos(4 * np.pi * s / 5),
            np.sin(4 * np.pi * s / 5),
            (-1) ** s)


def check_Q17A():
    print("[Q17-A 5D CRT Fourier Embedding]")
    images = [Phi(s) for s in range(10)]
    print(f"       Phi: Z/10Z -> R^5 (10 image vectors)")
    # Check injective
    for i in range(10):
        for j in range(i + 1, 10):
            di = np.linalg.norm(np.array(images[i]) - np.array(images[j]))
            assert di > 1e-9, f"Phi({i}) = Phi({j})"
    print("       Phi is injective: PASS")

    # Decagonal D_10 symmetry: the rotation s -> s+1 acts on R^5
    # by rotation in the (cos, sin) pairs and sign-flip in the 5th coord.
    # The composite has order 10.
    #
    # TODO: D_10 symmetry check not implemented; see Open Problem O_X.
    # The previous implementation was a no-op stub (`lambda v_s, v_s1: True`)
    # which returned True unconditionally regardless of input. Implementing a
    # real check requires specifying which D_10 generator action (rotation by
    # 2*pi/10 in the (cos, sin) pairs combined with sign-flip on the 5th
    # coord) is being tested against Phi(s+1) vs Phi(s). Left as a TODO
    # rather than carrying a stub that asserts PASS for any input.
    print("       D_10 symmetry: SKIP (not implemented; see Open Problem O_X)")
    print()


# ============================================================
# Q17-B: Symbolic Return -- corollary of G_6
# ============================================================

def check_Q17B():
    print("[Q17-B Symbolic Return Theorem]")
    print("       For every s in Z/10Z, sigma^6(s) = s.")
    for s in range(10):
        assert sigma_iter(s, 6) == s, f"sigma^6({s}) != {s}"
    print("       (Direct corollary of G_6. PASS.)")
    # Also check: VOID(0) is avoided by non-VOID trajectories.
    for s in range(1, 10):
        trajectory = {sigma_iter(s, k) for k in range(10)}
        assert 0 not in trajectory or s == 0, f"trajectory of {s} reaches VOID"
    print("       VOID avoidance for s != 0: PASS\n")


# ============================================================
# Master harness
# ============================================================

def main():
    if hasattr(sys.stdout, "reconfigure"):
        try: sys.stdout.reconfigure(encoding="utf-8")
        except: pass

    print("=== J_qseries_merged -- Consolidated Verification ===\n")
    check_G6()
    check_G7()
    check_G8()
    check_Q17A()
    check_Q17B()
    print("=" * 55)
    print("  ALL 5 THEOREMS PASS at machine precision.")
    print("=" * 55)


if __name__ == "__main__":
    main()
