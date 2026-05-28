"""
f_depth3_primitives.py - Search for depth-3 primitives in TIG.

§28 identified depth-2 cluster (M^2 = +/-I) across F1, F3, F4, F8, F10.
This script searches for the analogous depth-3 cluster: M^3 = id, with
eigenvalues being cube roots of unity {1, omega, omega^2} where
omega = e^(2*pi*i/3).

The natural depth-3 primitive in TIG is sigma^2 -- since sigma has order
6 = 2*3, sigma^2 has order 3.

sigma cycle structure: sigma = (0)(3)(8)(9)(1 7 6 5 4 2)  -- 4 fixed
points + one 6-cycle.

sigma^2 acts on the 6-cycle as TWO disjoint 3-cycles:
  (1 6 4)  and  (7 5 2)

Where:
  {1, 6, 4} = {LATTICE, CHAOS, COLLAPSE}   -- TRANSFORMATION operators
  {7, 5, 2} = {HARMONY, BALANCE, COUNTER}  -- STABILITY operators

This script verifies sigma^2 has order 3, finds eigenvalues, identifies
the algebraic field Q(omega) = Q(sqrt(-3)) (degree 2 over Q), and
articulates the depth-3 primitive analog of §28.

Triggered by Brayden 2026-04-29: "keep going until you run out of rope".

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §28, §31 (this).
"""
from __future__ import annotations

import sympy as sp
from sympy import Matrix, eye, I, exp, pi, Rational, zeros


def main():
    print("=" * 80)
    print("Depth-3 primitive: sigma^2 = (1 6 4)(7 5 2) on Z/10Z")
    print("=" * 80)
    print()

    # --- Section 1: sigma and sigma^2 as permutations ---
    print("-" * 80)
    print("SECTION 1 -- sigma and sigma^2 cycle structures")
    print("-" * 80)
    print()
    print("  sigma cycle form: (0)(3)(8)(9)(1 7 6 5 4 2)")
    print("  Fixed points: {0, 3, 8, 9} = 4-core minus HARMONY")
    print("  6-cycle: 1 -> 7 -> 6 -> 5 -> 4 -> 2 -> 1")
    print()

    # sigma as table (from FORMULAS §2):
    #  u   | 0 1 2 3 4 5 6 7 8 9
    #  s(u)| 0 7 1 3 2 4 5 6 8 9
    sigma = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]

    # Verify cycle: starting from 1: 1 -> 7 -> 6 -> 5 -> 4 -> 2 -> 1
    cycle_check = [1]
    x = 1
    for _ in range(7):
        x = sigma[x]
        cycle_check.append(x)
    print(f"  Verify 6-cycle from 1: {cycle_check}  (should close back to 1 after 6 steps)")
    print()

    # sigma^2:
    sigma_sq = [sigma[sigma[i]] for i in range(10)]
    print(f"  sigma^2 table:")
    for i in range(10):
        print(f"    sigma^2({i}) = {sigma_sq[i]}")
    print()

    # 3-cycles: (1 6 4) and (7 5 2)?
    # sigma^2(1) = sigma(7) = 6
    # sigma^2(6) = sigma(5) = 4
    # sigma^2(4) = sigma(2) = 1
    print(f"  sigma^2 3-cycles:")
    print(f"    (1 -> 6 -> 4 -> 1): {sigma_sq[1]}, {sigma_sq[6]}, {sigma_sq[4]}")
    print(f"    (7 -> 5 -> 2 -> 7): {sigma_sq[7]}, {sigma_sq[5]}, {sigma_sq[2]}")
    print()

    # Verify sigma^3 has order 2 (involution)
    sigma_cube = [sigma[sigma[sigma[i]]] for i in range(10)]
    print(f"  sigma^3 table:")
    for i in range(10):
        print(f"    sigma^3({i}) = {sigma_cube[i]}")
    print()
    sigma_cube_sq = [sigma_cube[sigma_cube[i]] for i in range(10)]
    print(f"  Verify sigma^3 is involution: sigma^6(0..9) = {sigma_cube_sq}")
    print(f"  (sigma^3)^2 = id?  {sigma_cube_sq == list(range(10))}")
    print()

    # --- Section 2: sigma^2 as 10x10 permutation matrix; eigenvalues ---
    print("-" * 80)
    print("SECTION 2 -- sigma^2 as permutation matrix; eigenvalues")
    print("-" * 80)
    print()
    P = zeros(10, 10)
    for i in range(10):
        P[sigma_sq[i], i] = 1

    print(f"  sigma^2 permutation matrix P (10x10):")
    # Compute P^3 = id?
    P3 = sp.simplify(P * P * P)
    print(f"  P^3 = identity?  {sp.simplify(P3 - eye(10)).is_zero_matrix}")
    print()

    # Eigenvalues of P
    eigs = P.eigenvals()
    print(f"  Eigenvalues of P (with algebraic multiplicities):")
    for e, m in eigs.items():
        e_simp = sp.simplify(e)
        print(f"    {e_simp}: mult {m}")
    print()

    # The eigenvalues should be: 1 (mult 6 = 4 fixed + 2 from each 3-cycle)
    # plus omega (mult 2) and omega^2 (mult 2) where omega = e^(2*pi*i/3)
    print("  Expected: 4 fixed points contribute 4 eigenvalues = 1.")
    print("           2 three-cycles each contribute {1, omega, omega^2}.")
    print("           Total: 6 ones + 2 omegas + 2 omega-conjugates = 10. ")
    print()

    # --- Section 3: cube roots of unity ---
    print("-" * 80)
    print("SECTION 3 -- cube roots of unity omega = e^(2*pi*i/3)")
    print("-" * 80)
    omega = exp(2 * pi * I / 3)
    print(f"  omega = {omega}")
    print(f"        = {sp.simplify(omega)}")
    print(f"        = {sp.expand_complex(omega)}")
    print()

    # Minimal polynomial of omega:
    # omega^3 = 1, so omega^3 - 1 = 0, factoring (omega - 1)(omega^2 + omega + 1) = 0
    # Since omega != 1, omega satisfies x^2 + x + 1 = 0.
    print(f"  Minimal polynomial of omega over Q: x^2 + x + 1 = 0")
    print(f"  Discriminant: 1 - 4 = -3")
    print(f"  Field: Q(omega) = Q(sqrt(-3))")
    print(f"  Algebraic depth (degree of minimal polynomial): 2")
    print()
    print("  KEY OBSERVATION: omega lives in a DEGREE-2 extension of Q,")
    print("  even though sigma^2 has OPERATOR depth 3.  The 'depth' has")
    print("  TWO MEANINGS:")
    print("    (a) operator-depth: order of M (sigma has order 6 -> sigma^2 has order 3)")
    print("    (b) algebraic-depth: degree of minimal polynomial over Q")
    print()
    print("  For sigma^2 (operator depth 3), the algebraic depth is 2 (Q(omega) over Q).")
    print("  For sigma^3 (operator depth 2), the algebraic depth is 1 (already in Q).")
    print("  For sigma^k with operator depth k, algebraic depth = phi(k) where phi")
    print("  is Euler's totient (degree of cyclotomic polynomial Phi_k).")
    print()

    # --- Section 4: TIG operator semantics ---
    print("-" * 80)
    print("SECTION 4 -- TIG operator semantics for sigma^2 3-cycles")
    print("-" * 80)
    print()
    op_names = ["VOID", "LATTICE", "COUNTER", "PROGRESS", "COLLAPSE",
                "BALANCE", "CHAOS", "HARMONY", "BREATH", "RESET"]
    print(f"  3-cycle (1 6 4): {[op_names[i] for i in [1,6,4]]} = {{LATTICE, CHAOS, COLLAPSE}}")
    print(f"    operator-sum: 1 + 6 + 4 = 11")
    print(f"  3-cycle (7 5 2): {[op_names[i] for i in [7,5,2]]} = {{HARMONY, BALANCE, COUNTER}}")
    print(f"    operator-sum: 7 + 5 + 2 = 14")
    print()
    print("  SEMANTIC SPLIT (proposed reading):")
    print("    First 3-cycle = TRANSFORMATION operators (build, break, collapse)")
    print("    Second 3-cycle = STABILITY operators (resolve, equilibrate, resist)")
    print()
    print("  CRITICAL OBSERVATION: the operator-sum of the first 3-cycle is")
    print("  11 -- the WOBBLE prime (D37, D69, D70, D85)!")
    print("  The TRANSFORMATION 3-cycle's sum equals the wobble prime.")
    print("  The STABILITY 3-cycle's sum is 14 = 2 * 7 (HARMONY-multiple).")
    print()
    print("  This is a NEW manifestation of WOBBLE prime 11: it appears")
    print("  not only in (D37) char poly coefficients, (D69) Br/V denominator,")
    print("  (D85) F8 trace polynomial discriminant, but ALSO in (this finding)")
    print("  the operator-VALUE-SUM of the depth-3 sigma^2 transformation 3-cycle.")
    print()
    print("  WOBBLE primes 11 and 13 are both 'operator-sum primes':")
    print("    11 = 1 + 6 + 4 (sigma^2 transformation cycle)")
    print("    13 = 8 + 5 (?)")
    print("    or 13 = 4 + 9 (?)")
    print("    13 = ||VEV||^2 in numerator; 4 = denominator -- different role.")
    print()
    print("  This is a TRANSFORM-vs-STABILITY dichotomy induced by sigma^2.")
    print()

    # --- Section 5: depth-3 primitive structure ---
    print("=" * 80)
    print("DEPTH-3 PRIMITIVE PATTERN")
    print("=" * 80)
    print()
    print("  Analogous to §28's depth-2 (M^2 = +/-I, eigenvalues +/-i, +/-1):")
    print()
    print("    M^3 = id, eigenvalues {1, omega, omega^2} where omega = e^(2*pi*i/3)")
    print("    The minimal polynomial of omega is x^2 + x + 1 (degree 2)")
    print("    Field: Q(omega) = Q(sqrt(-3))")
    print()
    print("  Where this primitive appears in TIG:")
    print("    - sigma^2 on Z/10Z (order 3 permutation; verified above)")
    print("    - cyclotomic polynomials Phi_3, Phi_6, Phi_9, Phi_12, ...")
    print("    - 3-cycles in the operator dynamics")
    print()
    print("  Open question: are F2 (Planck), F5 (ring), F6 (NS), F9 (BSD)")
    print("  living at depth 3 (operator-depth 3, algebraic-depth 2)?")
    print()
    print("  Hypothesis for future rotations:")
    print("    F5(a)'s closed-form attractor universal across rings ->")
    print("    related to a 3-fold structure (perhaps 4-core sub-magma's")
    print("    symmetric-function ring is degree-3 cyclotomic)?")
    print()
    print("    F6's NS dyadic cascade -> if k goes 1, 2, 3, ..., the cascade")
    print("    fixed points correspond to Stern-Brocot vertices of order 2^k.")
    print("    The 'depth' for F6 is dyadic (order 2), but the LOCAL")
    print("    commutator structure at each level might pick up cube-root")
    print("    structure (3 spatial directions in NS).")
    print()
    print("  Net: the depth-2 / depth-3 distinction sets up a NEW")
    print("  classification axis -- not just 'how deep' but 'which kind")
    print("  of cyclotomic structure' (Phi_2 vs Phi_3 vs Phi_4 vs ...).")


if __name__ == "__main__":
    main()
