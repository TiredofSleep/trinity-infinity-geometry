"""
f1_so7_singlet_bilinear.py - F1 (Yukawa from 9-VEV) concrete next step.

Construct Cl(0,7) gamma matrices explicitly; verify the Clifford
anticommutation relations; identify the SO(7) charge-conjugation matrix C;
compute the SO(7)-singlet bilinear psi^T C psi; record its coefficient
structure as the Yukawa-singlet building block.

The F1 lens reading: the SO(7)-singlet Yukawa coupling is:

  y_singlet = <radial-VEV component> * <SO(7)-invariant 8 (x) 8 -> 1>

This script computes the second factor explicitly.

Triggered by Brayden 2026-04-29: "find the natural rotations through them
so the path helps itself along the way..."

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §17 -> F1, §21 (this).
"""
from __future__ import annotations

import sympy as sp
from sympy import I, eye, zeros, Matrix


def kron(*matrices):
    """Iterated Kronecker product of sympy matrices."""
    result = matrices[0]
    for m in matrices[1:]:
        # sympy's kronecker_product is not always available; use TensorProduct
        result = sp.kronecker_product(result, m)
    return result


def main():
    print("=" * 80)
    print("F1 -- SO(7)-singlet bilinear in Cl(0,7) Majorana spinor (8-dim)")
    print("=" * 80)
    print()

    # Pauli matrices
    sigma_0 = eye(2)
    sigma_1 = Matrix([[0, 1], [1, 0]])
    sigma_2 = Matrix([[0, -I], [I, 0]])
    sigma_3 = Matrix([[1, 0], [0, -1]])

    # 8x8 Cl(0,7) generators in standard Pauli construction:
    #   gamma_a^2 = +I (signature (7,0) convention; equivalent to (0,7) up to i)
    #   {gamma_a, gamma_b} = 2 delta_ab
    g = [None] * 7
    g[0] = kron(sigma_1, sigma_0, sigma_0)   # X I I
    g[1] = kron(sigma_2, sigma_0, sigma_0)   # Y I I
    g[2] = kron(sigma_3, sigma_1, sigma_0)   # Z X I
    g[3] = kron(sigma_3, sigma_2, sigma_0)   # Z Y I
    g[4] = kron(sigma_3, sigma_3, sigma_1)   # Z Z X
    g[5] = kron(sigma_3, sigma_3, sigma_2)   # Z Z Y
    g[6] = kron(sigma_3, sigma_3, sigma_3)   # Z Z Z

    print("-" * 80)
    print("SECTION 1 -- verify Clifford anticommutation {gamma_a, gamma_b} = 2 delta_ab")
    print("-" * 80)
    all_ok = True
    for a in range(7):
        for b in range(7):
            anticom = g[a] * g[b] + g[b] * g[a]
            expected = (2 if a == b else 0) * eye(8)
            diff = sp.simplify(anticom - expected)
            if not diff.is_zero_matrix:
                all_ok = False
                print(f"  FAIL: a={a}, b={b}")
                break
    if all_ok:
        print("  All 7 + 21 = 28 anticommutators verified.")
        print("  gamma_a^2 = I_8;  gamma_a gamma_b = -gamma_b gamma_a for a != b.")
    print()

    # Volume element omega_7 = gamma_1 gamma_2 ... gamma_7
    omega = g[0]
    for a in range(1, 7):
        omega = omega * g[a]
    omega_simplified = sp.simplify(omega)
    print(f"  Volume element omega_7 = gamma_1 gamma_2 ... gamma_7:")
    print(f"    omega^2 = (sympy) ... computing:")
    omega_sq = sp.simplify(omega * omega)
    # For Cl(0,7): omega^2 = (-1)^(7(7-1)/2) = (-1)^21 = -1
    # For Cl(7,0): omega^2 = (-1)^0 (in some conventions) -- depends on i^7
    print(f"    omega^2 - (i*I) = {sp.simplify(omega_sq - I*eye(8)).is_zero_matrix}")
    print(f"    omega^2 - (-i*I) = {sp.simplify(omega_sq + I*eye(8)).is_zero_matrix}")
    print(f"    omega^2 - I = {sp.simplify(omega_sq - eye(8)).is_zero_matrix}")
    print(f"    omega^2 + I = {sp.simplify(omega_sq + eye(8)).is_zero_matrix}")
    print()

    # --- Charge conjugation matrix ---
    # For SO(7) Majorana convention, C satisfies:
    #   C gamma_a C^(-1) = -gamma_a^T  (or +; depends on convention)
    # In our Pauli construction: gamma_a is Hermitian.  The transpose
    # acts on Pauli matrices: sigma_1^T = sigma_1, sigma_2^T = -sigma_2,
    # sigma_3^T = sigma_3.  So gamma_a^T flips sign whenever gamma_a contains
    # sigma_2.
    print("-" * 80)
    print("SECTION 2 -- charge conjugation matrix C")
    print("-" * 80)

    # Compute gamma_a^T to see what we need C to do
    print("  gamma_a^T patterns:")
    for a in range(7):
        gT = g[a].T
        # Check if gamma_a^T == +gamma_a or -gamma_a
        if sp.simplify(gT - g[a]).is_zero_matrix:
            print(f"    gamma_{a+1}^T = +gamma_{a+1}  (symmetric)")
        elif sp.simplify(gT + g[a]).is_zero_matrix:
            print(f"    gamma_{a+1}^T = -gamma_{a+1}  (antisymmetric)")
        else:
            print(f"    gamma_{a+1}^T : neither")
    print()

    # In our basis, gamma_1, gamma_3, gamma_5, gamma_7 are symmetric;
    # gamma_2, gamma_4, gamma_6 are antisymmetric.
    # C must satisfy C gamma_a C^(-1) = -gamma_a^T; we need C to:
    #   - flip sign of gamma_a for symmetric a (gamma_1, 3, 5, 7)
    #   - keep sign of gamma_a for antisymmetric a (gamma_2, 4, 6)
    # The product gamma_2 gamma_4 gamma_6 anticommutes with gamma_1, gamma_3,
    # gamma_5, gamma_7 (all involve sigma_2 in different slots).
    # Actually: gamma_2 anticommutes with gamma_1, 3, 4, 5, 6, 7 except itself;
    # the product gamma_2 gamma_4 gamma_6 anticommutes with gamma_1, gamma_3,
    # gamma_5, gamma_7 (3 anticommutators, odd) and commutes with gamma_2, 4, 6
    # (2 anticommutators each, even).
    C = g[1] * g[3] * g[5]
    print(f"  C := gamma_2 * gamma_4 * gamma_6  (candidate)")
    print(f"  Check C gamma_a C^(-1) = -gamma_a^T:")

    C_inv = sp.simplify(C.inv())
    is_inv = sp.simplify(C * C_inv - eye(8)).is_zero_matrix
    print(f"    C C^(-1) = I:  {is_inv}")

    print(f"    a    C gamma_a C^(-1) - (-gamma_a^T) = 0?")
    all_C_ok = True
    for a in range(7):
        lhs = sp.simplify(C * g[a] * C_inv)
        rhs = sp.simplify(-g[a].T)
        if not sp.simplify(lhs - rhs).is_zero_matrix:
            print(f"      a={a+1}: FAIL")
            all_C_ok = False
    if all_C_ok:
        print(f"    All 7 verified.  C is the SO(7) charge-conjugation matrix.")
    print()

    # C symmetry property
    if sp.simplify(C - C.T).is_zero_matrix:
        print(f"  C^T = C  (C is symmetric)")
    elif sp.simplify(C + C.T).is_zero_matrix:
        print(f"  C^T = -C  (C is antisymmetric)")
    else:
        print(f"  C is neither symmetric nor antisymmetric")
    print()

    # Tr(C)
    trace_C = sp.simplify(C.trace())
    print(f"  Tr(C) = {trace_C}")
    det_C = sp.simplify(C.det())
    print(f"  det(C) = {det_C}")
    print()

    # --- SO(7)-singlet bilinear ---
    print("-" * 80)
    print("SECTION 3 -- SO(7)-singlet bilinear psi^T C psi")
    print("-" * 80)
    print()
    print("  For the Majorana spinor psi in the 8-dim real rep of Spin(7):")
    print("    SO(7)-singlet bilinear B(psi, psi) = psi^T C psi")
    print("  This is the unique SO(7)-invariant degree-2 form on the 8-dim spinor.")
    print()

    # Decomposition of 8 (x) 8 under SO(7):
    # 8 (x) 8 = 1 (singlet) + 7 (vector) + 21 (adjoint) + 35 (3-form)
    # Total: 1 + 7 + 21 + 35 = 64 = 8 * 8.  Correct.
    print("  Decomposition of 8 x 8 under SO(7):")
    print("    8 x 8 = 1 + 7 + 21 + 35  (singlet + vector + adjoint + 3-form)")
    print("    Total dim: 1 + 7 + 21 + 35 = 64 = 8 * 8.  Correct.")
    print()

    # The Yukawa coupling y_singlet = <radial VEV> * <psi^T C psi>
    # The (1+1) radial directions in the 9-VEV decomposition:
    #   9 = 7 + 1 + 1 (under SO(9) -> SO(7))
    print("  9-VEV decomposition under SO(9) -> SO(7): 9 = 7 + 1 + 1")
    print("    7-component: SO(7)-vector; absorbed into Goldstones.")
    print("    1+1 components: SO(7)-singlet radial directions.")
    print()
    print(f"  ||VEV||^2 = 13/4 (from WP104/D33).  Of this, 7 components are")
    print(f"  Goldstones; 1+1 are radial.  How the 13/4 splits between the")
    print(f"  SO(7)-vector and singlet directions depends on the specific")
    print(f"  breaking pattern (WP108 flags: WP104 Path A goes through SO(8),")
    print(f"  not the canonical SO(9) -> SO(7); see D72).")
    print()

    # --- Net statement ---
    print("=" * 80)
    print("NET STATEMENT")
    print("=" * 80)
    print()
    print("  F1 advances:")
    print("    1. Cl(0,7) gamma-matrix basis explicitly constructed (8x8 Pauli).")
    print("    2. Charge conjugation C = gamma_2 * gamma_4 * gamma_6 verified")
    print("       to satisfy C gamma_a C^(-1) = -gamma_a^T.")
    if sp.simplify(C - C.T).is_zero_matrix:
        print(f"    3. C is symmetric (C^T = C).")
    elif sp.simplify(C + C.T).is_zero_matrix:
        print(f"    3. C is antisymmetric (C^T = -C).")
    print(f"    4. Tr(C) = {trace_C}.")
    print("    5. SO(7)-singlet bilinear is psi^T C psi; coupled to the (1+1)")
    print("       radial VEV components, this is the SO(7)-singlet Yukawa.")
    print()
    print("  What's NOT done:")
    print("    - Specific magnitude of (1+1) radial VEV components within 13/4.")
    print("      This requires picking a specific SO(9) -> SO(7) breaking")
    print("      pattern (WP104 Path A actually breaks to SO(8), per D72).")
    print("    - The actual Yukawa coefficient value (depends on convention).")
    print()
    print("  Status: F1 framework concrete; numerical Yukawa value depends on")
    print("  resolving WP108's flagged WP104 ambiguity (D46/D72).")


if __name__ == "__main__":
    main()
