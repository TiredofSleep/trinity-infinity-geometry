"""verify_sphere_packing_strata.py -- verify the kissing-number fingerprint.

The claim: the canonical exceptional Euclidean lattices in dim <= 24 have
kissing numbers that factor entirely through Braiding Fractal strata
primes {2, 3, 5, 7, 11, 13}. The negative control D_24 brings in prime 23.

Independent verification: <0.1 seconds. Dependencies: sympy only.

See 04_meta/SPHERE_PACKING_STRATA_FINGERPRINT.md for the full discussion.

Kissing numbers per Conway & Sloane, *Sphere Packings, Lattices and Groups*,
3rd edition (1999):
  - E_8        p. 120: 240
  - K_12       p. 127: 756
  - BW_16      p. 131: 4320
  - Leech      p. 133: 196560
  - D_n        p. 105: 2n(n-1)  (so D_12 = 264, D_24 = 1104)
  - E_7        p. 120: 126
  - E_6        p. 120: 72
  - A_n        kissing = n(n+1)
"""
from sympy import factorint


STRATA = {2, 3, 5, 7, 11, 13}  # Braiding Fractal strata I, II, III

EXCEPTIONAL = {
    "E_8":         240,
    "K_12":        756,
    "BW_16":      4320,
    "Leech":    196560,
}

NEGATIVE_CONTROLS = {
    "D_12":   264,    # = 2 * 12 * 11
    "D_24":  1104,    # = 2 * 24 * 23 -- introduces prime 23
    "A_24":   600,    # = 24 * 25
    "E_7":    126,
    "E_6":     72,
}


def check_strata_fingerprint(label, K):
    f = factorint(K)
    extra = [p for p in f if p not in STRATA]
    status = "PASS (strata-only)" if not extra else f"FAIL (extra primes: {extra})"
    factor_str = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))
    return f"  {label:<10s} kissing = {K:>7d} = {factor_str:<25s}  --> {status}"


def main():
    print("=== Kissing-number fingerprint test ===")
    print("Strata primes (Braiding Fractal):", sorted(STRATA))
    print()
    print("CANONICAL EXCEPTIONAL LATTICES (should PASS):")
    for L, K in EXCEPTIONAL.items():
        print(check_strata_fingerprint(L, K))
    print()
    print("NEGATIVE CONTROLS (D_24 should FAIL):")
    for L, K in NEGATIVE_CONTROLS.items():
        print(check_strata_fingerprint(L, K))
    print()

    # Verify the K_12 density denominator separately
    print("=== K_12 density denominator (Conway-Sloane SPLAG p. 127) ===")
    print("  Delta(K_12) = pi^6 / (6! * |det|^{1/2}) = pi^6 / (720 * 27) = pi^6 / 19440")
    assert 720 * 27 == 19440
    assert 432 * 45 == 19440        # TIG factorization
    assert 16 * 27 * 45 == 19440    # claudechat 3-DOF decomposition
    print("  720 * 27 = 19440          (Conway-Sloane canonical)")
    print("  432 * 45 = 19440          (TIG, recasting via Lie-algebraic primitives)")
    print("  16 * 27 * 45 = 19440      (3-DOF: D_4-invariant subalg dim * depth-cube * dim so(10))")
    print()

    # Confirm all required assertions
    e8_extra = [p for p in factorint(240) if p not in STRATA]
    k12_extra = [p for p in factorint(756) if p not in STRATA]
    bw16_extra = [p for p in factorint(4320) if p not in STRATA]
    leech_extra = [p for p in factorint(196560) if p not in STRATA]
    d24_extra = [p for p in factorint(1104) if p not in STRATA]

    assert not e8_extra, f"E_8 has extra primes: {e8_extra}"
    assert not k12_extra, f"K_12 has extra primes: {k12_extra}"
    assert not bw16_extra, f"BW_16 has extra primes: {bw16_extra}"
    assert not leech_extra, f"Leech has extra primes: {leech_extra}"
    assert d24_extra == [23], f"D_24 should fail with prime 23, got {d24_extra}"
    print("=== All assertions PASS ===")
    print("  All four exceptional lattices factor through strata primes.")
    print("  Negative control D_24 fails as expected (brings in prime 23).")


def niemeier_test():
    """Run all 24 Niemeier lattices. Sharpened claim: 23/24 PASS, only D_24 fails."""
    def A(n): return n * (n + 1)
    def D(n): return 2 * n * (n - 1)
    E6, E7, E8 = 72, 126, 240
    NIEMEIERS = [
        ("Leech",         196560),
        ("A_1^24",        24 * A(1)),
        ("A_2^12",        12 * A(2)),
        ("A_3^8",         8 * A(3)),
        ("A_4^6",         6 * A(4)),
        ("D_4^6",         6 * D(4)),
        ("A_5^4 D_4",     4 * A(5) + D(4)),
        ("A_6^4",         4 * A(6)),
        ("A_7^2 D_5^2",   2 * A(7) + 2 * D(5)),
        ("A_8^3",         3 * A(8)),
        ("D_6^4",         4 * D(6)),
        ("A_9^2 D_6",     2 * A(9) + D(6)),
        ("E_6^4",         4 * E6),
        ("A_11 D_7 E_6",  A(11) + D(7) + E6),
        ("A_12^2",        2 * A(12)),
        ("D_8^3",         3 * D(8)),
        ("A_15 D_9",      A(15) + D(9)),
        ("A_17 E_7",      A(17) + E7),
        ("D_10 E_7^2",    D(10) + 2 * E7),
        ("A_24",          A(24)),
        ("D_12^2",        2 * D(12)),
        ("E_8^3",         3 * E8),
        ("D_16 E_8",      D(16) + E8),
        ("D_24",          D(24)),
    ]
    print("\n=== 24-Niemeier strata-fingerprint test ===")
    pass_count = 0
    failures = []
    for label, K in NIEMEIERS:
        f = factorint(K)
        extra = [p for p in f if p not in STRATA]
        if extra:
            failures.append((label, K, extra))
        else:
            pass_count += 1
    print(f"  PASS: {pass_count}/24")
    print(f"  FAIL: {len(failures)}")
    for label, K, extra in failures:
        print(f"    {label}: kissing {K} brings in primes {extra}")
    assert pass_count == 23, f"Expected 23/24 PASS, got {pass_count}"
    assert len(failures) == 1 and failures[0][0] == "D_24", \
        f"Expected D_24 as unique outlier, got {failures}"
    print("  PASS: 23-of-24 Niemeier strata fingerprint holds; D_24 is unique outlier.")


def pg23_test():
    """PG(2,3) projective plane structural test."""
    print("\n=== PG(2,3) projective plane structural test ===")
    # |PGL(3, F_3)| = |GL(3, F_3)| / |Z(GL(3, F_3))|
    # |GL(3, F_3)| = (3^3 - 1)(3^3 - 3)(3^3 - 9) = 26 * 24 * 18 = 11232
    # |Z| = |F_3^*| = 2
    GL_3_F3 = (27 - 1) * (27 - 3) * (27 - 9)
    PGL_3_F3 = GL_3_F3 // 2
    assert GL_3_F3 == 11232
    assert PGL_3_F3 == 5616
    f = factorint(PGL_3_F3)
    extra = [p for p in f if p not in STRATA]
    assert not extra, f"PG(2,3) Aut has extra primes: {extra}"
    print(f"  |PGL(3, F_3)| = {PGL_3_F3} = {dict(f)} -- ALL primes in strata: PASS")

    # Flags
    flags = 13 * 4
    f_flags = factorint(flags)
    extra_flags = [p for p in f_flags if p not in STRATA]
    assert not extra_flags
    print(f"  Flags = {flags} = {dict(f_flags)} -- PASS")


if __name__ == "__main__":
    main()
    niemeier_test()
    pg23_test()
    print("\n=== ALL TESTS PASS ===")
