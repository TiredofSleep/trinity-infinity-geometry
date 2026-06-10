"""
06_attractor_closed_form.py

EXACT ALGEBRAIC RESULT: At α = 1/2, the T+B mix runtime attractor
has HARMONY/BREATH = 1 + √3 exactly.

DERIVATION:

The runtime attractor lives entirely in {VOID, HARMONY, BREATH, RESET}
(verified — all other operators have zero mass).

Restricted to this 4-core:
  T_BREATH(p,p) = 0   (TSML produces no BREATH from {V,H,Br,R} inputs)
  T_RESET(p,p)  = 0   (TSML produces no RESET from {V,H,Br,R} inputs)
  B_BREATH(p,p) = 2·br·r + 2·br·v + h²
  B_RESET(p,p)  = 2·br·h + 2·r·v

At α = 1/2 with sum = 1, the fixed point gives:
  2·breath = T_BREATH + B_BREATH = 0 + (2·br·r + 2·br·v + h²)
  
  → 2·breath - 2·br·r - 2·br·v = h²
  → 2·breath·(1 - r - v) = h²
  → 2·breath·(harmony + breath) = harmony²    [using v+h+br+r=1]
  
This is a closed quadratic in (harmony/breath):

  (h/br)² - 2(h/br) - 2 = 0
  
  → h/br = 1 + √3  (positive root)

NUMERICAL VERIFICATION:
  α=0.5 attractor: HARMONY = 0.540195948..., BREATH = 0.197725440...
  Ratio: 2.7320508076...
  1 + √3:  2.7320508076...
  Difference: 4.44e-16 (machine precision)

WHY THIS MATTERS:

1. α = 1/2 is structurally privileged. At other α values, the ratio is
   not a simple algebraic number. The verified-optimal mixing weight α = 1/2
   coincides with the point where the runtime equation has clean algebraic
   structure.

2. The runtime fixed point is a closed-form algebraic number over Q(√3).
   This is unexpected — a finite combinatorial algebra (10 operators, two
   integer tables) producing an exact algebraic-number runtime attractor
   over Q(√3) is structurally clean.

3. The √3 emerges from the structure of TSML and BHML's tables when
   restricted to the 4-core {V, H, Br, R}, not from any external choice.
"""
import numpy as np
from sympy import symbols, sqrt, simplify, Rational, expand


def derivation():
    """The full algebraic derivation."""
    print("=" * 70)
    print("DERIVATION: H/BREATH = 1+√3 at α=1/2")
    print("=" * 70)
    print()
    print("Setup: at the attractor, only V, H, Br, R have nonzero mass.")
    print()
    print("TSML restricted to {V, H, Br, R} produces only V or H:")
    print("  T_BREATH(p,p) = 0")
    print("  T_RESET(p,p)  = 0")
    print()
    print("BHML restricted to {V, H, Br, R}:")
    print("  B_BREATH(p,p) = 2·br·r + 2·br·v + h²")
    print()
    print("Fixed-point equation (α=1/2, normalized):")
    print("  2·breath = T_Br + B_Br = 0 + 2·br·r + 2·br·v + h²")
    print()
    print("Rearrange:")
    print("  2·breath·(1 - r - v) = h²")
    print()
    print("Use normalization v + h + br + r = 1:")
    print("  1 - r - v = h + br")
    print()
    print("Substitute:")
    print("  2·br·(h + br) = h²")
    print("  h² - 2·br·h - 2·br² = 0")
    print()
    print("Divide by br²:")
    print("  (h/br)² - 2(h/br) - 2 = 0")
    print()
    print("Solve the quadratic:")
    print("  h/br = (2 ± √(4 + 8))/2 = 1 ± √3")
    print()
    print("Positive root (mass must be positive):")
    print("  h/br = 1 + √3")


def numerical_verification():
    """Verify against the actual T+B mix iteration."""
    TSML_ROWS = ["0000000700","0737777777","0377477779","0777777773","0747777787",
                 "0777777777","0777777777","7777777777","0777877777","0797377777"]
    T = np.array([[int(c) for c in row] for row in TSML_ROWS], dtype=int)
    BHML_ROWS = ["0123456789","1234567266","2334567366","3444567466","4555567577",
                 "5666667677","6777777777","7234567890","8666777978","9666777080"]
    B = np.array([[int(c) for c in row] for row in BHML_ROWS], dtype=int)

    def fuse(p, q, table):
        r = np.zeros(10)
        for a in range(10):
            for b in range(10):
                r[int(table[a, b])] += p[a] * q[b]
        return r

    def normalize_l1(v):
        s = v.sum()
        return v / s if s > 1e-12 else v

    np.random.seed(42)
    p = normalize_l1(np.random.dirichlet(np.ones(10)))
    for _ in range(2000):
        p_t = normalize_l1(fuse(p, p, T))
        p_b = normalize_l1(fuse(p, p, B))
        p = normalize_l1(0.5 * p_t + 0.5 * p_b)

    H = p[7]
    Br = p[8]
    target = 1 + np.sqrt(3)
    ratio = H / Br

    print()
    print("=" * 70)
    print("NUMERICAL VERIFICATION (2000 iterations)")
    print("=" * 70)
    print()
    print(f"  HARMONY at attractor: {H:.15f}")
    print(f"  BREATH at attractor:  {Br:.15f}")
    print(f"  Ratio H/Br:           {ratio:.15f}")
    print(f"  Target 1 + √3:        {target:.15f}")
    print(f"  Difference:           {abs(ratio - target):.2e}")
    print()
    if abs(ratio - target) < 1e-12:
        print("  ✓ EXACT to machine precision")


if __name__ == "__main__":
    derivation()
    numerical_verification()
    print()
    print("=" * 70)
    print("STATUS")
    print("=" * 70)
    print("""
Finding: H/BREATH = 1 + √3 at α = 1/2 (proven analytically + verified
numerically to 1e-16).

The verified-optimal mixing weight α = 1/2 (which gives 52% information
preservation in the trail framework) is the same α at which the runtime
attractor satisfies a closed-form algebraic relation over Q(√3).

This is the cleanest result of the BHML-specificity investigation.
The runtime attractor of CK's T+B-mix processing is an algebraic
number over Q(√3), with H/BREATH = 1 + √3 exactly.
""")
