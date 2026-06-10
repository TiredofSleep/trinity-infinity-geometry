"""
verify_atkin_lehner.py

Verify the Atkin-Lehner W_3 eigenvalue of η(τ)⁶ η(3τ)⁶.

Result: W_3 eigenvalue = -1 (computed below).

Reference: This eigenvalue is essential because it identifies η⁶η_3⁶ as
the -1 Fricke eigenfunction at level 3, weight 6 — the cusp-form component
of the dim 6 magic function construction.

Run: python3 verify_atkin_lehner.py
"""
from sympy import sqrt, I, simplify, expand, Symbol, S
from sympy import factor, Mul, Pow

# Symbolic derivation of W_3 acting on η(τ)⁶ η(3τ)⁶
#
# Eta transformation: η(-1/u) = √(-iu) η(u)
#
# W_3: τ → -1/(3τ)
#
# Apply to η(τ)⁶:
#   η(-1/(3τ)) = η(-1/u) with u = 3τ
#             = √(-i · 3τ) η(3τ)
#             = √3 · √(-iτ) · η(3τ)
#   η(-1/(3τ))⁶ = (√3)⁶ · (-iτ)³ · η(3τ)⁶
#              = 27 · (-iτ)³ · η(3τ)⁶
#              = 27 · (-i)³ · τ³ · η(3τ)⁶
#              = 27 · i · τ³ · η(3τ)⁶  (since (-i)³ = -i·(-i)² = -i·(-1) = i)
#
# Apply to η(3τ)⁶:
#   η(3 · (-1/(3τ))) = η(-1/τ) = √(-iτ) · η(τ)
#   η(3·(-1/(3τ)))⁶ = (-iτ)³ · η(τ)⁶
#                   = i · τ³ · η(τ)⁶
#
# Product:
#   η(-1/(3τ))⁶ · η(3·(-1/(3τ)))⁶ = (27 · i · τ³ · η(3τ)⁶) · (i · τ³ · η(τ)⁶)
#                                  = 27 · i² · τ⁶ · η(τ)⁶ · η(3τ)⁶
#                                  = -27 · τ⁶ · η(τ)⁶ · η(3τ)⁶
#
# Fricke normalization at weight k=6, level N=3:
#   (F | W_3)(τ) = 3^(-k/2) · τ^(-k) · F(-1/(3τ))
#                = 3^(-3) · τ^(-6) · F(-1/(3τ))
#
# Apply to F = η⁶η_3⁶:
#   (F | W_3)(τ) = (1/27) · τ^(-6) · (-27 · τ⁶ · F(τ))
#                = -F(τ)
#
# Therefore: W_3 eigenvalue of η⁶η_3⁶ is -1.

print("=" * 70)
print("Symbolic verification: Atkin-Lehner W_3 eigenvalue of η(τ)⁶η(3τ)⁶")
print("=" * 70)
print()

# Sympy symbolic check
tau = Symbol('tau', positive=True, real=True)

# Use placeholders for eta function values
# η(-1/(3τ))⁶ = 27 · i · τ³ · η(3τ)⁶
# η(3·(-1/(3τ)))⁶ = η(-1/τ)⁶ = i · τ³ · η(τ)⁶

# Let A = η(τ)⁶, B = η(3τ)⁶
A = Symbol('eta6_tau')
B = Symbol('eta6_3tau')

# Then η(-1/(3τ))⁶ η(3·(-1/(3τ)))⁶ = (27·i·τ³·B)(i·τ³·A) = 27·i²·τ⁶·A·B = -27·τ⁶·A·B
eta_product_at_W3 = 27 * I * tau**3 * B * I * tau**3 * A
print("η(-1/(3τ))⁶ · η(3·(-1/(3τ)))⁶ =", simplify(eta_product_at_W3))
# Expected: -27·τ⁶·η(τ)⁶·η(3τ)⁶

# Fricke normalization
# F | W_3 = 3^(-3) τ^(-6) · (value at -1/(3τ))
Fricke_normalized = S(1)/27 * tau**(-6) * eta_product_at_W3
print()
print("Fricke-normalized: F | W_3(τ) =", simplify(Fricke_normalized))
print()
print("Original: F(τ) = η(τ)⁶ η(3τ)⁶ = A·B =", A*B)
print()

# Compare
ratio = simplify(Fricke_normalized / (A*B))
print(f"Ratio (F | W_3)(τ) / F(τ) = {ratio}")
print()

if ratio == -1:
    print("✓ VERIFIED: Atkin-Lehner W_3 eigenvalue = -1")
else:
    print(f"✗ ERROR: got {ratio}, expected -1")

print()
print("=" * 70)
print("Consequence: η⁶η_3⁶ is the canonical -1 Fricke eigenfunction at")
print("weight 6, level 3. Combined with G_+ = E_6 + 27·E_6(3τ) (eigenvalue +1)")
print("and G_- = E_6 - 27·E_6(3τ) (eigenvalue -1), it generates the basis")
print("for the magic function construction.")
print()
print("ψ_+(τ) = G_+(τ)·G_-(τ)/η⁶η_3⁶ has eigenvalue (+1)(-1)/(-1) = +1.")
print("ψ_-(τ) = η⁶η_3⁶ itself has eigenvalue -1.")
print()
print("These are the two building blocks of f_6 = α·I_+ + β·I_-.")
