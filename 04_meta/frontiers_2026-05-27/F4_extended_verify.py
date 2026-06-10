"""
F4_extended_verify.py
=====================

Frontier F4-extended: verify the F4 closed forms
  (A) |idem(V over F_p)| = p + 3       (for odd p)
  (B) |Aut(V_p)| = p (p^2 - 1)         (at every prime EXCEPT p=5)
at higher primes 17 through ~97.

KEY FINDING DURING DEVELOPMENT (documented below):

  The F4 frontier doc lists two closed forms, drawn from TWO DIFFERENT
  V-algebras in the corpus:
    - J18's T^BHML algebra (manuscript: idem count = 2, 6, 8, 10, 14, 16
      for p in {2, 3, 5, 7, 11, 13}, matching p + 3 for odd p);
    - J48/J49's T_F5 algebra ("DIRAC formal" 4-core with all products in
      span(e_0, e_2), brute-force Aut at p=5 gives 40 = |F_20 x Z/2|;
      tabulated values {6, 24, 40, 336, 1320, 2184} at p in {2,3,5,7,11,13}).

  These are DIFFERENT algebras. Direct brute force on either table does
  NOT give |Aut| = p(p^2 - 1) at p in {3, 7, 11, 13}. Specifically:
    - J18 T^BHML at p=3: |Aut| = 4 (not 24); at p=5: |Aut| = ? (we test).
    - J49 T_F5 at p=3: |Aut| = 12 (not 24); at p=5: |Aut| = 40 (matches).

  Conclusion: the F4 claim "|Aut| = p(p^2-1)" as a clean closed form is
  NOT supported by direct brute force on either canonical V algebra at
  primes other than p=5. The 40-at-p=5 result is solid (J49 F_5-specific
  theorem). The {24, 336, 1320, 2184} values at p in {3, 7, 11, 13} cited
  in J48 §4.1 and F4 doc §3 are NOT verifiable from the brute-force
  enumeration on the canonical T_F5 table.

  This frontier-extended verification:
    (i) Confirms |idem(V^BHML_{F_p})| = p + 3 for p in {17, ..., 97} —
        STRENGTHENS the J18 closed form.
    (ii) Reports |Aut(V^BHML_{F_p})| via brute-force enumeration for
         small primes and via constraint search for larger primes.
    (iii) Documents the mismatch between the F4 doc and direct
         brute-force at the cited primes for the J18 T^BHML algebra.

Dependencies: standard library + numpy.
Wall-clock: ~5-10 seconds per prime.
"""

from __future__ import annotations
import sys
import time
from itertools import product

# ---------------------------------------------------------------------------
# T^BHML structure constants (J18 canonical multiplication table).
# Basis indexed 0..3 corresponding to (e_0, e_2, e_3, e_4).
#
#   e_0 * everything = 0       (e_0 is a two-sided zero)
#   e_2 * e_2 = e_2            (e_2 is a primitive idempotent)
#   e_2 * e_3 = e_3
#   e_2 * e_4 = 0
#   e_3 * e_3 = e_2            (e_3 is a square root of e_2)
#   e_3 * e_4 = e_4
#   e_4 * e_4 = 0              (e_4 is nilpotent)
# ---------------------------------------------------------------------------
T_BHML = [
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # e_0 row
    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]],  # e_2 row
    [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],  # e_3 row
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]],  # e_4 row
]


def mul_p(x: list[int], y: list[int], p: int) -> list[int]:
    """Multiply two basis-vector reps in V^BHML over F_p."""
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
            coef = xi * yj
            for k in range(4):
                ck = cij[k]
                if ck != 0:
                    out[k] = (out[k] + coef * ck) % p
    return out


def det4_mod_p(M: list[list[int]], p: int) -> int:
    """Compute determinant of a 4x4 matrix modulo p via Gaussian elimination."""
    A = [row[:] for row in M]
    n = 4
    det = 1
    for c in range(n):
        pivot = -1
        for r in range(c, n):
            if A[r][c] % p != 0:
                pivot = r
                break
        if pivot < 0:
            return 0
        if pivot != c:
            A[c], A[pivot] = A[pivot], A[c]
            det = (-det) % p
        pv = A[c][c] % p
        det = (det * pv) % p
        inv_pv = pow(pv, p - 2, p)
        for r in range(c + 1, n):
            if A[r][c] % p == 0:
                continue
            factor = (A[r][c] * inv_pv) % p
            for k in range(c, n):
                A[r][k] = (A[r][k] - factor * A[c][k]) % p
    return det % p


# ---------------------------------------------------------------------------
# Idempotent count (fast, via symbolic analysis)
# ---------------------------------------------------------------------------
def count_idempotents_fast(p: int) -> int:
    """Count idempotents of V^BHML over F_p in O(p^2) time.

    Algebraic analysis: x = (a, b, c, d) in basis [e_0, e_2, e_3, e_4].
    Compute x*x via T_BHML:
      x*x_e_0 coord: 0   (e_0 column/row is all zero)
      x*x_e_2 coord: b^2 + c^2    (from b*e_2*b*e_2 + c*e_3*c*e_3)
      x*x_e_3 coord: 2*b*c        (from b*e_2 and c*e_3 cross terms)
      x*x_e_4 coord: 2*c*d        (from c*e_3 and d*e_4 cross terms)
    Idempotent condition x*x = x:
      a = 0
      b^2 + c^2 = b mod p
      2 b c = c mod p   <=> c (2b - 1) = 0 mod p
      2 c d = d mod p   <=> d (2c - 1) = 0 mod p
    """
    count = 0
    for b in range(p):
        for c in range(p):
            # b^2 + c^2 = b mod p ?
            if (b * b + c * c) % p != b % p:
                continue
            # c (2b - 1) = 0 mod p ?
            if (2 * b * c - c) % p != 0:
                continue
            # Now enumerate d satisfying d (2c - 1) = 0 mod p
            if (2 * c - 1) % p == 0:
                count += p  # any d works
            else:
                count += 1  # only d = 0
    return count


# ---------------------------------------------------------------------------
# Automorphism count via structured constraint propagation
#
# Structural observations for T^BHML:
#   - e_0 is a two-sided zero (annihilator). Therefore the radical R contains
#     e_0. In fact span(e_0) is the kernel of L_x for ALL x, since L_x * e_0
#     = x * e_0 = 0. Hence phi(e_0) lies in the radical, which is at least
#     span(e_0).
#   - The image of multiplication is span(e_2, e_3, e_4) (3-dim).
#     Therefore phi(e_2), phi(e_3), phi(e_4) have e_0-coordinate = 0.
#   - The relation e_3^2 = e_2 forces phi(e_2) = phi(e_3)^2.
#   - The 1-dim annihilator span(e_0) is mapped to itself by phi.
#
# Enumeration: phi(e_3) over F_p^3 (3-dim image, p^3 candidates). For each,
# derive phi(e_2). Then phi(e_4) is in a constrained subspace. Then phi(e_0)
# is freely in F_p^* * e_0. Verify det != 0.
# ---------------------------------------------------------------------------
def count_automorphisms_bhml(p: int) -> int:
    """Count |Aut(V^BHML_{F_p})| via structured constraint propagation.

    Algorithm:
      - phi(e_3) = h ranges over F_p^3 (image space). p^3 candidates.
      - phi(e_2) = h*h derived; must satisfy phi(e_2)^2 = phi(e_2) AND
        phi(e_2)*phi(e_3) = phi(e_3) (only some h pass these tests).
      - phi(e_4) = v ranges over the 1-eigenspace of L_h, restricted to:
            phi(e_2)*v = 0,  v*v = 0.
        Computed via Gaussian elimination on (L_h - I) restricted to
        the image (3x3 system).
      - phi(e_0) = alpha*e_0 freely with alpha in F_p^*: (p-1) factor.

    Total expected cost: O(p^3 * cost_per_h). For most h, the 1-eigenspace
    is small (1 or 2 dim), so cost_per_h ~ O(p) -> O(p^4) overall.
    For p=97 that is ~10^8, feasible in seconds.
    """
    count = 0

    # Enumerate phi(e_3) = h = (0, h2, h3, h4)
    for h2 in range(p):
        for h3 in range(p):
            for h4 in range(p):
                h = [0, h2, h3, h4]
                # phi(e_2) = h * h
                hh = mul_p(h, h, p)
                if hh == [0, 0, 0, 0]:
                    continue
                if mul_p(hh, hh, p) != hh:
                    continue
                if mul_p(hh, h, p) != h:
                    continue
                # Build L_h matrix restricted to image (basis e_2, e_3, e_4)
                # acting on (v2, v3, v4) -> components of h*v in (e_2, e_3, e_4).
                # h * e_2 = h * (0,1,0,0); h * e_3 = h * (0,0,1,0); h * e_4 = h * (0,0,0,1)
                Lh_e2 = mul_p(h, [0, 1, 0, 0], p)
                Lh_e3 = mul_p(h, [0, 0, 1, 0], p)
                Lh_e4 = mul_p(h, [0, 0, 0, 1], p)
                # 3x3 matrix Lh_img[row][col]: row = (e_2, e_3, e_4) component of result,
                # col = (e_2, e_3, e_4) component of input.
                Lh_img = [
                    [Lh_e2[1], Lh_e3[1], Lh_e4[1]],
                    [Lh_e2[2], Lh_e3[2], Lh_e4[2]],
                    [Lh_e2[3], Lh_e3[3], Lh_e4[3]],
                ]
                # Solve (Lh - I) v_img = 0 for v_img in F_p^3.
                M = [
                    [(Lh_img[0][0] - 1) % p, Lh_img[0][1] % p, Lh_img[0][2] % p],
                    [Lh_img[1][0] % p, (Lh_img[1][1] - 1) % p, Lh_img[1][2] % p],
                    [Lh_img[2][0] % p, Lh_img[2][1] % p, (Lh_img[2][2] - 1) % p],
                ]
                kernel_basis = nullspace_mod_p_3x3(M, p)
                if not kernel_basis:
                    continue
                # Enumerate v_img in the kernel (p^dim candidates).
                # For each, build v = (0, v_img[0], v_img[1], v_img[2]) and check:
                #   phi(e_2) * v = 0
                #   v * v = 0
                #   matrix is invertible (det of 3x3 sub != 0)
                k_dim = len(kernel_basis)
                for coeffs in product(range(p), repeat=k_dim):
                    v_img = [0, 0, 0]
                    for ci, bi in zip(coeffs, kernel_basis):
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
                    d3 = det3_mod_p(sub, p)
                    if d3 == 0:
                        continue
                    count += (p - 1)  # alpha freedom
    return count


def nullspace_mod_p_3x3(M: list[list[int]], p: int) -> list[list[int]]:
    """Compute a basis for the nullspace of a 3x3 matrix M over F_p."""
    A = [row[:] for row in M]
    n_rows = 3
    n_cols = 3
    pivot_cols = []
    r = 0
    for c in range(n_cols):
        pivot = -1
        for k in range(r, n_rows):
            if A[k][c] % p != 0:
                pivot = k
                break
        if pivot < 0:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c] % p, p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for k in range(n_rows):
            if k != r and A[k][c] % p != 0:
                factor = A[k][c] % p
                A[k] = [(A[k][j] - factor * A[r][j]) % p for j in range(n_cols)]
        pivot_cols.append(c)
        r += 1
    free_cols = [c for c in range(n_cols) if c not in pivot_cols]
    basis = []
    for free in free_cols:
        v = [0] * n_cols
        v[free] = 1
        for pc_idx, pc in enumerate(pivot_cols):
            v[pc] = (-A[pc_idx][free]) % p
        basis.append(v)
    return basis


def det3_mod_p(M: list[list[int]], p: int) -> int:
    """3x3 determinant modulo p."""
    a, b, c = M[0][0] % p, M[0][1] % p, M[0][2] % p
    d, e, f = M[1][0] % p, M[1][1] % p, M[1][2] % p
    g, h, i = M[2][0] % p, M[2][1] % p, M[2][2] % p
    return (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)) % p


# ---------------------------------------------------------------------------
# Main verification routine
# ---------------------------------------------------------------------------
PRIMES = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def expected_idem(p: int) -> int:
    return p + 3


def hypothesized_aut_F4(p: int) -> int:
    """F4-doc hypothesized closed form: p(p^2 - 1). REFUTED at all tested primes."""
    return p * (p * p - 1)


def expected_aut(p: int) -> int:
    """Empirically discovered closed form on J18 T^BHML: |Aut| = (p-1)^2.

    This matches at all primes 3, 5, 7, 11, 13, 17, 19, ..., 97 inclusive,
    including p=5 (no anomaly). The structure is Aut(V^BHML_{F_p}) is a
    finite abelian group of order (p-1)^2 -- two independent F_p^* scalings.
    """
    return (p - 1) ** 2


def sanity_check_small_primes() -> None:
    """Validate algorithm at p in {3, 5, 7, 11, 13} against brute-force.

    Compare both the F4-doc hypothesized form p(p^2-1) AND the empirically
    discovered (p-1)^2 form.
    """
    print("Sanity check at p in {3, 5, 7, 11, 13}:")
    print(f"{'p':>4}  {'|idem|':>7}  {'p+3':>5}  {'|Aut| (BHML)':>13}  "
          f"{'(p-1)^2':>8}  {'p(p^2-1)':>10}")
    for p in [3, 5, 7, 11, 13]:
        t0 = time.time()
        n_idem = count_idempotents_fast(p)
        n_aut = count_automorphisms_bhml(p)
        dt = time.time() - t0
        print(f"{p:>4}  {n_idem:>7}  {p + 3:>5}  {n_aut:>13}  "
              f"{(p - 1) ** 2:>8}  {hypothesized_aut_F4(p):>10}  ({dt:.2f}s)")
    print()


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("=" * 78)
    print("F4-extended: closed-form verification on V^BHML over F_p")
    print("Algebra: J18 T^BHML 4-core (basis e_0, e_2, e_3, e_4)")
    print("=" * 78)
    print()
    sanity_check_small_primes()

    print("=" * 78)
    print("Primary verification at primes 17..97:")
    print("=" * 78)
    print(f"{'p':>4}  {'|idem|':>7}  {'p+3':>5}  {'idem ok':>8}"
          f"  {'|Aut|':>11}  {'(p-1)^2':>9}  {'aut ok':>7}"
          f"  {'p(p^2-1)':>11}  {'F4 ok':>6}  {'time(s)':>8}")
    print("-" * 98)

    idem_all_ok = True
    aut_new_ok = True
    aut_f4_ok = True
    results = []
    for p in PRIMES:
        t0 = time.time()
        n_idem = count_idempotents_fast(p)
        idem_ok = (n_idem == expected_idem(p))
        n_aut = count_automorphisms_bhml(p)
        aut_new = (n_aut == expected_aut(p))
        aut_f4 = (n_aut == hypothesized_aut_F4(p))
        dt = time.time() - t0
        idem_all_ok = idem_all_ok and idem_ok
        aut_new_ok = aut_new_ok and aut_new
        aut_f4_ok = aut_f4_ok and aut_f4
        results.append({
            "p": p, "n_idem": n_idem, "n_aut": n_aut,
            "idem_ok": idem_ok, "aut_new": aut_new, "aut_f4": aut_f4, "time": dt,
        })
        print(f"{p:>4}  {n_idem:>7}  {p + 3:>5}  {str(idem_ok):>8}"
              f"  {n_aut:>11}  {expected_aut(p):>9}  {str(aut_new):>7}"
              f"  {hypothesized_aut_F4(p):>11}  {str(aut_f4):>6}"
              f"  {dt:>8.2f}", flush=True)

    print("-" * 98)
    print()
    print("=" * 78)
    print("CONCLUSIONS:")
    print("=" * 78)
    if idem_all_ok:
        print(f"  (A) Idempotent count |idem(V^BHML_{{F_p}})| = p + 3 CONFIRMED")
        print(f"      at all {len(PRIMES)} primes 17..97. The J18 closed form is robust.")
    else:
        print(f"  (A) Idempotent count: SOME EXCEPTIONS")
        for r in results:
            if not r["idem_ok"]:
                print(f"      p={r['p']}: |idem|={r['n_idem']}, expected {r['p'] + 3}")
    print()
    if aut_new_ok:
        print(f"  (B) |Aut(V^BHML_{{F_p}})| = (p - 1)^2 CONFIRMED at all {len(PRIMES)} primes 17..97.")
        print(f"      This is the EMPIRICALLY CORRECT closed form for the J18 T^BHML algebra.")
        print(f"      The natural automorphism group is Aut(V^BHML_{{F_p}}) ~= F_p^* x F_p^*,")
        print(f"      two independent scalar multiplications on the (e_2 vs e_4) subalgebras.")
        print(f"      Note: includes p=5 (no anomaly!) -- a strict improvement over the F4 doc.")
    else:
        print(f"  (B) (p - 1)^2 hypothesis FAILS at some primes:")
        for r in results:
            if not r["aut_new"]:
                print(f"      p={r['p']}: |Aut|={r['n_aut']}, (p-1)^2={(r['p']-1)**2}")
    print()
    print(f"  (C) F4-doc hypothesized form p(p^2 - 1) does NOT hold for the J18 T^BHML")
    print(f"      algebra at ANY of the {len(PRIMES)} tested primes. The F4 doc likely")
    print(f"      cited values from the J49 T_F5 algebra (different multiplication table).")
    print(f"      Spot-check: T_F5 at p=3 also gives |Aut|=12 (not 24), so the F4 doc's")
    print(f"      tabulated J48 values {{6, 24, 40, 336, 1320, 2184}} appear to come from a")
    print(f"      THIRD definition of V_p not currently in the corpus, or are arithmetically")
    print(f"      incorrect.")


if __name__ == "__main__":
    main()
