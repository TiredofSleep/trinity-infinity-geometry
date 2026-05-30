"""
verify_J53.py
=============

Self-contained verification of the two closed-form theorems of J53:

  Theorem 1: |idem(V^BHML over F_p)| = p + 3 for odd p
                                     = 2 at p = 2 (degenerate)

  Theorem 2: |Aut(V^BHML over F_p)| = (p - 1)^2 at every prime p >= 2
             with structure F_p^* x F_p^*

Verification is performed at primes p in {3, 5, 7, 11, 13}.
For higher-prime confirmation (p <= 97), see the companion script
  04_meta/frontiers_2026-05-27/F4_extended_verify.py

License: CC-BY-4.0
Authors: B.R. Sanders, M. Gish (2026)

Dependencies: Python standard library only (itertools).
Wall-clock runtime: ~2 seconds for the 5 verification primes.

V^BHML multiplication table (basis e_0, e_2, e_3, e_4 indexed 0..3):
  e_0 * everything = 0          (e_0 is the two-sided annihilator)
  e_2 * e_2 = e_2               (e_2 is a primitive idempotent)
  e_2 * e_3 = e_3 = e_3 * e_2
  e_2 * e_4 = 0   = e_4 * e_2
  e_3 * e_3 = e_2               (e_3 is a square root of e_2)
  e_3 * e_4 = e_4 = e_4 * e_3
  e_4 * e_4 = 0                 (e_4 is nilpotent)

Note: This script's algorithms are equivalent (and aliased) to the F4-extended
verification logic of `04_meta/frontiers_2026-05-27/F4_extended_verify.py`,
restricted to primes 3..13 for portability + speed.
"""

from __future__ import annotations
import sys
import time
from itertools import product

# ---------------------------------------------------------------------------
# Structure constants T_BHML[i][j][k] giving e_i * e_j = sum_k T[i][j][k] * e_k
# Basis indexed 0..3 = (e_0, e_2, e_3, e_4).
# ---------------------------------------------------------------------------
T_BHML = [
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # e_0 row
    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]],  # e_2 row
    [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],  # e_3 row
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]],  # e_4 row
]


def mul_p(x, y, p):
    """Compute x * y in V^BHML over F_p, where x, y are 4-vectors in F_p."""
    out = [0, 0, 0, 0]
    for i in range(4):
        xi = x[i]
        if xi == 0:
            continue
        for j in range(4):
            yj = y[j]
            if yj == 0:
                continue
            cij = T_BHML[i][j]
            coef = (xi * yj) % p
            if coef == 0:
                continue
            for k in range(4):
                ck = cij[k]
                if ck != 0:
                    out[k] = (out[k] + coef * ck) % p
    return out


# ---------------------------------------------------------------------------
# THEOREM 1: idempotent count via the O(p^2) symbolic counter.
#
# From the derivation in J53 §3.2: for x = (a, b, c, d), x*x = x reduces to
#   (I.0)  a = 0
#   (I.2)  b^2 + c^2 = b mod p
#   (I.3)  c(2b - 1) = 0 mod p
#   (I.4)  d(2c - 1) = 0 mod p
# Counting solutions: |idem| = p + 3 for odd p, = 2 at p = 2.
# ---------------------------------------------------------------------------
def count_idempotents_via_reduction(p):
    """Count |idem(V^BHML / F_p)| via the (b, c) -> d case split."""
    count = 0
    for b in range(p):
        for c in range(p):
            if (b * b + c * c - b) % p != 0:    # eq (I.2)
                continue
            if (2 * b * c - c) % p != 0:         # eq (I.3)
                continue
            if (2 * c - 1) % p == 0:             # eq (I.4): d free
                count += p
            else:                                # eq (I.4): d = 0
                count += 1
    return count


def count_idempotents_brute(p):
    """Brute-force enumeration of all p^4 elements of V^BHML / F_p,
    checking x*x = x. Cross-check for the symbolic counter."""
    count = 0
    for x in product(range(p), repeat=4):
        x = list(x)
        if mul_p(x, x, p) == x:
            count += 1
    return count


# ---------------------------------------------------------------------------
# THEOREM 2: automorphism count via constraint propagation.
#
# Following J53 §4.2 (and the F4-extended algorithm):
#   - phi(e_0) = alpha * e_0, alpha in F_p^*           [(p-1) free choices]
#   - phi(e_3) = h ranges over the 3-dim image
#   - phi(e_2) = h*h is derived; filter by phi(e_2)^2 = phi(e_2) and
#       phi(e_2) * h = h
#   - phi(e_4) = v in 1-eigenspace of L_h, intersected with {phi(e_2)*v = 0}
#       and {v*v = 0}
#   - Check the 3x3 sub-matrix on Im(mu) = span(e_2, e_3, e_4) is invertible
#   - Multiply by (p - 1) for alpha
#
# Expected: |Aut| = (p - 1)^2.
# ---------------------------------------------------------------------------
def count_automorphisms_constraint(p):
    """Count |Aut(V^BHML / F_p)| via constraint propagation."""
    count = 0
    for h2 in range(p):
        for h3 in range(p):
            for h4 in range(p):
                h = [0, h2, h3, h4]
                hh = mul_p(h, h, p)
                if hh == [0, 0, 0, 0]:
                    continue
                if mul_p(hh, hh, p) != hh:
                    continue
                if mul_p(hh, h, p) != h:
                    continue
                # Build L_h restricted to image (basis e_2, e_3, e_4)
                Lh_cols = [
                    mul_p(h, [0, 1, 0, 0], p),
                    mul_p(h, [0, 0, 1, 0], p),
                    mul_p(h, [0, 0, 0, 1], p),
                ]
                Lh_img = [
                    [Lh_cols[0][1], Lh_cols[1][1], Lh_cols[2][1]],
                    [Lh_cols[0][2], Lh_cols[1][2], Lh_cols[2][2]],
                    [Lh_cols[0][3], Lh_cols[1][3], Lh_cols[2][3]],
                ]
                # (L_h - I) v = 0 system
                M = [
                    [(Lh_img[0][0] - 1) % p, Lh_img[0][1] % p, Lh_img[0][2] % p],
                    [Lh_img[1][0] % p, (Lh_img[1][1] - 1) % p, Lh_img[1][2] % p],
                    [Lh_img[2][0] % p, Lh_img[2][1] % p, (Lh_img[2][2] - 1) % p],
                ]
                kernel = nullspace_3x3_mod_p(M, p)
                if not kernel:
                    continue
                k_dim = len(kernel)
                for coeffs in product(range(p), repeat=k_dim):
                    v_img = [0, 0, 0]
                    for ci, bi in zip(coeffs, kernel):
                        for j in range(3):
                            v_img[j] = (v_img[j] + ci * bi[j]) % p
                    v = [0, v_img[0], v_img[1], v_img[2]]
                    if v == [0, 0, 0, 0]:
                        continue
                    if mul_p(hh, v, p) != [0, 0, 0, 0]:
                        continue
                    if mul_p(v, v, p) != [0, 0, 0, 0]:
                        continue
                    sub = [
                        [hh[1] % p, h[1] % p, v[1] % p],
                        [hh[2] % p, h[2] % p, v[2] % p],
                        [hh[3] % p, h[3] % p, v[3] % p],
                    ]
                    if det_3x3_mod_p(sub, p) == 0:
                        continue
                    count += (p - 1)  # alpha factor
    return count


def nullspace_3x3_mod_p(M, p):
    """Return a basis for the nullspace of a 3x3 matrix M mod p."""
    A = [row[:] for row in M]
    pivot_cols = []
    r = 0
    for c in range(3):
        pivot = -1
        for k in range(r, 3):
            if A[k][c] % p != 0:
                pivot = k
                break
        if pivot < 0:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c] % p, p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for k in range(3):
            if k != r and A[k][c] % p != 0:
                factor = A[k][c] % p
                A[k] = [(A[k][j] - factor * A[r][j]) % p for j in range(3)]
        pivot_cols.append(c)
        r += 1
    free_cols = [c for c in range(3) if c not in pivot_cols]
    basis = []
    for free in free_cols:
        v = [0, 0, 0]
        v[free] = 1
        for pc_idx, pc in enumerate(pivot_cols):
            v[pc] = (-A[pc_idx][free]) % p
        basis.append(v)
    return basis


def det_3x3_mod_p(M, p):
    """3x3 determinant mod p."""
    a, b, c = M[0][0] % p, M[0][1] % p, M[0][2] % p
    d, e, f = M[1][0] % p, M[1][1] % p, M[1][2] % p
    g, h, i = M[2][0] % p, M[2][1] % p, M[2][2] % p
    return (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)) % p


# ---------------------------------------------------------------------------
# Main verification
# ---------------------------------------------------------------------------
PRIMES = [3, 5, 7, 11, 13]


def expected_idem(p):
    """Theorem 1 closed form."""
    return p + 3


def expected_aut(p):
    """Theorem 2 closed form."""
    return (p - 1) ** 2


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("=" * 72)
    print("J53 verification: two closed-form theorems for V^BHML over F_p")
    print("=" * 72)
    print()
    print("Theorem 1: |idem(V^BHML / F_p)| = p + 3 for odd p")
    print("Theorem 2: |Aut(V^BHML / F_p)| = (p - 1)^2 at every prime p >= 2")
    print()
    print(f"Verifying at primes {PRIMES} ...")
    print()

    fmt = "{:>4} {:>9} {:>7} {:>7} {:>9} {:>10} {:>7} {:>10}"
    print(fmt.format("p", "|idem|", "p+3", "match1", "|Aut|", "(p-1)^2", "match2", "time(s)"))
    print("-" * 72)

    all_idem_ok = True
    all_aut_ok = True

    for p in PRIMES:
        t0 = time.time()
        n_idem = count_idempotents_via_reduction(p)
        n_aut = count_automorphisms_constraint(p)
        # Cross-check idempotent count against brute force at small primes
        if p <= 7:
            n_idem_brute = count_idempotents_brute(p)
            assert n_idem == n_idem_brute, (
                f"Internal consistency failure at p={p}: "
                f"symbolic counter says {n_idem}, brute force says {n_idem_brute}"
            )
        dt = time.time() - t0

        idem_ok = (n_idem == expected_idem(p))
        aut_ok = (n_aut == expected_aut(p))
        all_idem_ok = all_idem_ok and idem_ok
        all_aut_ok = all_aut_ok and aut_ok

        print(fmt.format(
            p, n_idem, expected_idem(p), "OK" if idem_ok else "FAIL",
            n_aut, expected_aut(p), "OK" if aut_ok else "FAIL",
            f"{dt:.2f}"
        ))

    print("-" * 72)
    print()
    print("CHECK 1 (Theorem 1: |idem| = p + 3 at p in {3, 5, 7, 11, 13}): "
          + ("PASS" if all_idem_ok else "FAIL"))
    print("CHECK 2 (Theorem 2: |Aut| = (p-1)^2 at p in {3, 5, 7, 11, 13}): "
          + ("PASS" if all_aut_ok else "FAIL"))
    print()

    overall_pass = all_idem_ok and all_aut_ok
    n_pass = int(all_idem_ok) + int(all_aut_ok)
    print(f"Overall: {'PASS' if overall_pass else 'FAIL'} ({n_pass}/2)")

    if overall_pass:
        print()
        print("Both closed-form theorems verified at all 5 primes.")
        print("For higher-prime extension (24 primes total, p <= 97), see:")
        print("  04_meta/frontiers_2026-05-27/F4_extended_verify.py")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
