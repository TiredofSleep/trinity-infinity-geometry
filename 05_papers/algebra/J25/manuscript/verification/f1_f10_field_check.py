"""
f1_f10_field_check.py - F1 (charge conjugation) and F10 (Prym psi-bar)
                       share the algebraic primitive M^2 = -I, with
                       eigenvalues +/-i.  Do they share a number field?

§28 noted both F1 and F10 have M^2 = -I with eigenvalues +/-i.  Both
require the algebraic extension Q(i) for the eigenspace decomposition.

Question: do their CHARACTERISTIC POLYNOMIALS factor through Q(i)
identically, or are they different complex structures?

For F1 (C in Cl(0,7)):  C is 8x8 with C^2 = -I_8, so char poly of C is
(x^2 + 1)^4 -- factors over Q(i) as ((x-i)(x+i))^4.

For F10 (psi-bar on Prym):  psi-bar is 4x4 with psi-bar^2 = -I_4, so
char poly is (x^2 + 1)^2 -- factors over Q(i) as ((x-i)(x+i))^2.

So both have the SAME characteristic polynomial structure: power of x^2+1.
Both eigenspace decompositions live in Q(i).

CONCLUSION: F1 and F10 share Q(i) (degree-2 extension over Q).  They're
both at *algebraic-depth 2* but with different *operator-depths* (since
their dimensions differ).  Same depth-2 field, same primitive, two
different geometric realizations.

Triggered by Brayden 2026-04-29: "keep going until you run out of rope".

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §28, §32, §33 (this).
"""
from __future__ import annotations

import sympy as sp
from sympy import Matrix, eye, I


def kron(*matrices):
    result = matrices[0]
    for m in matrices[1:]:
        result = sp.kronecker_product(result, m)
    return result


def main():
    print("=" * 80)
    print("F1 (Cl(0,7) C) and F10 (Prym psi-bar) share Q(i)")
    print("=" * 80)
    print()

    x = sp.Symbol('x', real=True)

    # F1 -- charge conjugation
    sigma_0 = eye(2)
    sigma_1 = Matrix([[0, 1], [1, 0]])
    sigma_2 = Matrix([[0, -I], [I, 0]])
    sigma_3 = Matrix([[1, 0], [0, -1]])
    g = [None] * 7
    g[0] = kron(sigma_1, sigma_0, sigma_0)
    g[1] = kron(sigma_2, sigma_0, sigma_0)
    g[2] = kron(sigma_3, sigma_1, sigma_0)
    g[3] = kron(sigma_3, sigma_2, sigma_0)
    g[4] = kron(sigma_3, sigma_3, sigma_1)
    g[5] = kron(sigma_3, sigma_3, sigma_2)
    g[6] = kron(sigma_3, sigma_3, sigma_3)
    C = g[1] * g[3] * g[5]

    print("-" * 80)
    print("F1 -- C = gamma_2 * gamma_4 * gamma_6 (8x8 in Cl(0,7))")
    print("-" * 80)
    char_C = sp.simplify(C.charpoly(x).as_expr())
    print(f"  Characteristic polynomial of C:")
    print(f"    char(C, x) = {char_C}")
    print(f"    factored: {sp.factor(char_C)}")
    expected = (x**2 + 1)**4
    print(f"    expected (x^2+1)^4 = {sp.expand(expected)}")
    print(f"    match: {sp.simplify(char_C - expected) == 0}")
    print()

    # F10 -- Prym psi-bar
    print("-" * 80)
    print("F10 -- psi-bar = block-diag(J, J) (4x4 on Prym), J = [[0,-1],[1,0]]")
    print("-" * 80)
    J = Matrix([[0, -1], [1, 0]])
    M = sp.diag(J, J)
    char_M = sp.simplify(M.charpoly(x).as_expr())
    print(f"  Characteristic polynomial of psi-bar:")
    print(f"    char(psi-bar, x) = {char_M}")
    print(f"    factored: {sp.factor(char_M)}")
    expected_M = (x**2 + 1)**2
    print(f"    expected (x^2+1)^2 = {sp.expand(expected_M)}")
    print(f"    match: {sp.simplify(char_M - expected_M) == 0}")
    print()

    # --- Field analysis ---
    print("-" * 80)
    print("Field decomposition analysis")
    print("-" * 80)
    print()
    print("  Both characteristic polynomials are powers of x^2 + 1.")
    print("  x^2 + 1 has discriminant -4 = -2^2, squarefree(-4) = -1.")
    print("  Field generated: Q(i) = Q(sqrt(-1)) -- degree 2 over Q.")
    print()
    print("  F1's eigenspace decomposition: 8-dim splits as 4+4 over Q(i)")
    print("  F10's eigenspace decomposition: 4-dim splits as 2+2 over Q(i)")
    print()
    print("  Both at algebraic-depth 2 (Q(i)).")
    print("  F1 operator-depth: 4 (since C^4 = I_8, and C is non-diagonal)")
    print("  F10 operator-depth: 4 (since psi-bar^4 = I_4 from psi^4 = id)")
    print()

    # --- Cross-frontier picture ---
    print("=" * 80)
    print("CROSS-FRONTIER: depth-2 algebraic depth Q(i) vs Q(sqrt 3)")
    print("=" * 80)
    print()
    print("  Q(i) = Q(sqrt(-1))  -- imaginary quadratic, disc -4")
    print("    F1, F10 live here.")
    print()
    print("  Q(sqrt 3) -- real quadratic, disc 12")
    print("    F3 H/Br = 1 + sqrt 3 lives here.")
    print()
    print("  Q(omega) = Q(sqrt -3) -- imaginary quadratic, disc -3")
    print("    sigma^2 (depth-3 primitive) lives here.")
    print()
    print("  At algebraic-depth 2, TIG visits THREE different quadratic fields:")
    print("    Q(i), Q(sqrt 3), Q(sqrt -3)")
    print("  These three are the imaginary/real/cyclotomic quadratic extensions")
    print("  with the smallest possible discriminants (|d| in {3, 4, 12}).")
    print()
    print("  These are also Q(zeta_n) for n=4 (giving Q(i)), n=6 or 3 (giving")
    print("  Q(omega) = Q(sqrt -3)), and the simplest non-cyclotomic extension")
    print("  Q(sqrt 3).")
    print()
    print("  At algebraic-depth 4 (LMFDB 4.2.10224.1):")
    print("    F8 trace polynomial AND WP105 R/Br quartic both live here.")
    print()
    print("  The depth-2 cluster (§28) splits into:")
    print("    Q(i)        -- F1, F10 (involution-with-i-eigenvalues type)")
    print("    Q(sqrt 3)   -- F3 (real quadratic extension type)")
    print("  These are different quadratic extensions, but BOTH are depth-2.")
    print()
    print("  And depth-3 (sigma^2, eigenvalues cube roots of unity) gives")
    print("  Q(omega) = Q(sqrt -3) -- a DIFFERENT imaginary quadratic.")
    print()
    print("  TIG-natural quadratic fields visited so far:")
    print("    Q(sqrt 3)    -- F3 H/Br quadratic                  (D78)")
    print("    Q(sqrt -3)   -- sigma^2 cube roots                 (D86)")
    print("    Q(sqrt -1)   -- F1 charge conj + F10 Prym psi-bar  (D77, D81)")
    print("  All three: discriminants {-3, 12, -4}, smallest possible imaginary")
    print("  + real quadratic primitives.  TIG is structurally connected to")
    print("  the THREE simplest quadratic fields.")


if __name__ == "__main__":
    main()
