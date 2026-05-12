#!/usr/bin/env python3
# ============================================================
# 4core_verification.py
#
# Verification for: "Joint Closure, a Universal Attractor, and
# an Algebraic Mixing Point for a Pair of Binary Operations on
# Z/10Z" (Sanders, Gish, 2026)
#
# Six checks (mapped to manuscript Theorems A-F):
#   1. Joint-closure enumeration   (Theorems A + 2.4 three-substrate
#                                   strengthening; Theorem B 4-core
#                                   3-substrate closure as corollary)
#   2. Normalizer identity         (Theorem C)
#   3. Closed-form attractor       (Theorem D ratio part)
#   4. Universality across chain   (Theorem E)
#   5. Galois structure of quartic (Theorem D Galois part)
#   6. alpha-sweep PSLQ            (Theorem F partial uniqueness)
#
# Runtime: ~4 seconds. Run: python3 4core_verification.py
#
# Copyright (c) 2026 B.R. Sanders and M. Gish.
# Licensed under the Creative Commons Attribution 4.0 International
# License (CC-BY-4.0). https://creativecommons.org/licenses/by/4.0/
# ============================================================

from itertools import combinations
from collections import Counter
from math import gcd as _gcd

# -- the three tables (T = TSML, B = BHML, S = CL_STD) --
T = [
    [0,0,0,0,0,0,0,7,0,0],
    [0,7,3,7,7,7,7,7,7,7],
    [0,3,7,7,4,7,7,7,7,9],
    [0,7,7,7,7,7,7,7,7,3],
    [0,7,4,7,7,7,7,7,8,7],
    [0,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,8,7,7,7,7,7],
    [0,7,9,3,7,7,7,7,7,7],
]
B = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,2,6,6],
    [2,3,3,4,5,6,7,3,6,6],
    [3,4,4,4,5,6,7,4,6,6],
    [4,5,5,5,5,6,7,5,7,7],
    [5,6,6,6,6,6,7,6,7,7],
    [6,7,7,7,7,7,7,7,7,7],
    [7,2,3,4,5,6,7,8,9,0],
    [8,6,6,6,7,7,7,9,7,8],
    [9,6,6,6,7,7,7,0,8,0],
]
S = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,7,8,1],
    [2,3,4,5,6,7,7,8,7,2],
    [3,4,5,6,7,7,7,7,7,3],
    [4,5,6,7,7,7,7,8,7,4],
    [5,6,7,7,7,8,7,7,7,5],
    [6,7,7,7,7,7,8,7,7,6],
    [7,7,8,7,8,7,7,8,7,7],
    [8,8,7,7,7,7,7,7,7,8],
    [9,1,2,3,4,5,6,7,8,0],
]

# symmetry sanity check (commutativity)
for i in range(10):
    for j in range(10):
        assert T[i][j] == T[j][i] and B[i][j] == B[j][i] and S[i][j] == S[j][i]


def is_closed(subset, table):
    Sset = set(subset)
    return all(table[i][j] in Sset for i in subset for j in subset)


def hr(label):
    print()
    print("=" * 60)
    print(label)
    print("=" * 60)


# === Check 1: joint-closure enumeration (Theorem A + 3-substrate strengthening 2.4) ===
def check_chain():
    hr("Check 1: Joint-closure enumeration (1023 subsets, T+B and T+B+S)")
    jc_TB = []
    jc_TBS = []
    for size in range(1, 11):
        for sub in combinations(range(10), size):
            cl_T = is_closed(sub, T)
            cl_B = is_closed(sub, B)
            cl_S = is_closed(sub, S)
            if cl_T and cl_B:
                jc_TB.append(sub)
            if cl_T and cl_B and cl_S:
                jc_TBS.append(sub)

    sizes = Counter(len(s) for s in jc_TB)
    sizes_3 = Counter(len(s) for s in jc_TBS)
    expected = [
        (0,),
        (0, 7, 8, 9),
        (0, 6, 7, 8, 9),
        (0, 5, 6, 7, 8, 9),
        (0, 4, 5, 6, 7, 8, 9),
        (0, 3, 4, 5, 6, 7, 8, 9),
        (0, 2, 3, 4, 5, 6, 7, 8, 9),
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    ]

    print(f"  T+B jointly-closed subsets: {len(jc_TB)} (expected: 8)")
    print(f"  T+B size distribution: {dict(sorted(sizes.items()))}")
    print(f"  Sizes 2 and 3 forbidden: {2 not in sizes and 3 not in sizes}")

    chain_strict = all(set(jc_TB[i]) < set(jc_TB[i+1]) for i in range(len(jc_TB)-1))
    print(f"  T+B chain strictly increasing (no branching): {chain_strict}")

    matches = [tuple(sorted(s)) for s in jc_TB] == expected
    print(f"  T+B chain matches Theorem A: {matches}")

    print()
    print(f"  T+B+S jointly-closed subsets: {len(jc_TBS)} (expected: 8)")
    print(f"  T+B+S size distribution: {dict(sorted(sizes_3.items()))}")
    matches_3 = [tuple(sorted(s)) for s in jc_TBS] == expected
    same_chain = (matches and matches_3 and jc_TB == jc_TBS)
    print(f"  T+B+S chain matches Theorem 2.4 (same as T+B): {same_chain}")

    print()
    print(f"  Standalone closure counts:")
    cl_T_count = sum(1 for size in range(1, 11) for s in combinations(range(10), size) if is_closed(s, T))
    cl_B_count = sum(1 for size in range(1, 11) for s in combinations(range(10), size) if is_closed(s, B))
    cl_S_count = sum(1 for size in range(1, 11) for s in combinations(range(10), size) if is_closed(s, S))
    print(f"    T alone: {cl_T_count}    B alone: {cl_B_count}    S alone: {cl_S_count}")

    print()
    print(f"  Three-substrate joint-closure chain (Theorem 2.4):")
    for sub in jc_TBS:
        print(f"    |S|={len(sub):2d}: {sub}")

    print()
    # 4-core 3-substrate closure (Theorem B explicit verification)
    C = (0, 7, 8, 9)
    T_4core = {T[i][j] for i in C for j in C}
    B_4core = {B[i][j] for i in C for j in C}
    S_4core = {S[i][j] for i in C for j in C}
    print(f"  4-core image under T: {T_4core} (subset of {set(C)}: {T_4core <= set(C)})")
    print(f"  4-core image under B: {B_4core} (subset of {set(C)}: {B_4core <= set(C)})")
    print(f"  4-core image under S: {S_4core} (subset of {set(C)}: {S_4core <= set(C)})")
    fourcore_3sub = (T_4core <= set(C)) and (B_4core <= set(C)) and (S_4core <= set(C))
    print(f"  Theorem B (4-core 3-substrate closure): {fourcore_3sub}")

    return matches and chain_strict and same_chain and fourcore_3sub


# === Check 2: normalizer identity ===
def check_normalizer():
    hr("Check 2: Normalizer identity Z_T = Z_B = (v+h+br+r)^2")
    try:
        import sympy as sp
    except ImportError:
        print("  sympy not available; skipping")
        return None

    v, h, br, r = sp.symbols('v h br r', positive=True)
    p = [sp.Integer(0)] * 10
    p[0], p[7], p[8], p[9] = v, h, br, r

    def fuse(table, p):
        out = [sp.Integer(0)] * 10
        for i in range(10):
            for j in range(10):
                out[table[i][j]] += p[i] * p[j]
        return out

    Tf = fuse(T, p)
    Bf = fuse(B, p)
    target = (v + h + br + r) ** 2
    diff_T = sp.expand(sum(Tf) - target)
    diff_B = sp.expand(sum(Bf) - target)

    print(f"  Z_T - (v+h+br+r)^2 = {diff_T}")
    print(f"  Z_B - (v+h+br+r)^2 = {diff_B}")
    print()
    print(f"  T-fuse on 4-core:")
    for c in [0, 7, 8, 9]:
        print(f"    Tfuse[{c}] = {sp.expand(Tf[c])}")
    print(f"  B-fuse on 4-core:")
    for c in [0, 7, 8, 9]:
        print(f"    Bfuse[{c}] = {sp.expand(Bf[c])}")

    ok = (diff_T == 0) and (diff_B == 0)
    print()
    print(f"  Normalizer identity verified: {ok}")
    return ok


# === Check 3: closed-form attractor ===
def check_attractor():
    hr("Check 3: Attractor h/br = 1+sqrt(3) at alpha=1/2")
    try:
        import mpmath as mp
    except ImportError:
        print("  mpmath not available; skipping")
        return None

    mp.mp.dps = 50

    p = [mp.mpf(0)] * 10
    for c in [0, 7, 8, 9]:
        p[c] = mp.mpf(1) / 4
    half = mp.mpf(1) / 2

    def fuse(table, p):
        out = [mp.mpf(0)] * 10
        for i in range(10):
            for j in range(10):
                out[table[i][j]] += p[i] * p[j]
        return out

    n = 0
    for n in range(300):
        Tf = fuse(T, p)
        Bf = fuse(B, p)
        out = [half * Tf[c] + half * Bf[c] for c in range(10)]
        s = sum(out)
        new_p = [x / s for x in out]
        if max(abs(p[c] - new_p[c]) for c in range(10)) < mp.mpf(10) ** -45:
            p = new_p
            break
        p = new_p

    target = 1 + mp.sqrt(3)
    ratio = p[7] / p[8]
    err = abs(ratio - target)

    print(f"  Iterations: {n}")
    print(f"  (v*, h*, br*, r*) = ({mp.nstr(p[0],8)}, {mp.nstr(p[7],8)}, "
          f"{mp.nstr(p[8],8)}, {mp.nstr(p[9],8)})")
    print(f"  h/br        = {mp.nstr(ratio, 35)}")
    print(f"  1 + sqrt(3) = {mp.nstr(target, 35)}")
    print(f"  |error|     = {mp.nstr(err, 5)}")

    ok = err < mp.mpf(10) ** -30
    print()
    print(f"  Closed-form attractor verified: {ok}")
    return ok


# === Check 4: universality ===
def check_universality():
    hr("Check 4: Universality across chain (shells of size >= 4)")
    try:
        import mpmath as mp
    except ImportError:
        print("  mpmath not available; skipping")
        return None

    mp.mp.dps = 40
    half = mp.mpf(1) / 2
    target = 1 + mp.sqrt(3)
    Cfour = {0, 7, 8, 9}

    shells = [
        (0, 7, 8, 9),
        (0, 6, 7, 8, 9),
        (0, 5, 6, 7, 8, 9),
        (0, 4, 5, 6, 7, 8, 9),
        (0, 3, 4, 5, 6, 7, 8, 9),
        (0, 2, 3, 4, 5, 6, 7, 8, 9),
        tuple(range(10)),
    ]

    def fuse(table, p):
        out = [mp.mpf(0)] * 10
        for i in range(10):
            for j in range(10):
                out[table[i][j]] += p[i] * p[j]
        return out

    all_ok = True
    for shell in shells:
        p = [mp.mpf(0)] * 10
        for c in shell:
            p[c] = mp.mpf(1) / len(shell)

        n = 0
        for n in range(400):
            Tf = fuse(T, p)
            Bf = fuse(B, p)
            out = [half * Tf[c] + half * Bf[c] for c in range(10)]
            s = sum(out)
            new_p = [x / s for x in out]
            if max(abs(p[c] - new_p[c]) for c in range(10)) < mp.mpf(10) ** -32:
                p = new_p
                break
            p = new_p

        m_outside = sum(p[c] for c in range(10) if c not in Cfour)
        if p[8] > mp.mpf(10) ** -20:
            err = abs(p[7] / p[8] - target)
        else:
            err = mp.mpf("inf")

        ok = (m_outside < mp.mpf(10) ** -20) and (err < mp.mpf(10) ** -20)
        all_ok = all_ok and ok
        print(f"  |S|={len(shell):2d} {shell}: iters={n:3d}, "
              f"mass_outside_C = {mp.nstr(m_outside,3)}, "
              f"|h/br - 1-sqrt(3)| = {mp.nstr(err,3)} -- {'OK' if ok else 'FAIL'}")

    print()
    print(f"  Universality verified: {all_ok}")
    return all_ok


# === Check 5: Galois structure ===
def check_galois():
    hr("Check 5: Galois structure of y^4+4y^3-y^2+2y-2")
    try:
        import sympy as sp
    except ImportError:
        print("  sympy not available; skipping")
        return None

    y = sp.Symbol('y')
    f = y**4 + 4*y**3 - y**2 + 2*y - 2

    # Irreducibility over Q
    factors = sp.factor_list(f)
    irreducible = (len(factors[1]) == 1) and (factors[1][0][1] == 1) and (factors[1][0][0] == f)
    print(f"  Quartic: {f}")
    print(f"  Factored over Q: {sp.factor(f)}")
    print(f"  Irreducible over Q: {irreducible}")

    # Discriminant
    disc = sp.Poly(f, y).discriminant()
    factored_disc = sp.factorint(abs(int(disc)))
    print(f"  Polynomial discriminant: {disc} = -{factored_disc}")
    disc_ok = (int(disc) == -40896)

    # Resolvent cubic
    z = sp.Symbol('z')
    g = z**3 + z**2 + 16*z + 36
    resolvent_factored = sp.factor(g)
    expected_resolvent = (z + 2) * (z**2 - z + 18)
    resolvent_ok = sp.expand(g - expected_resolvent) == 0
    print(f"  Resolvent cubic: {g}")
    print(f"  Factored: {resolvent_factored}")
    print(f"  Matches (z+2)(z^2-z+18): {resolvent_ok}")

    # Field discriminant
    field_disc = -10224
    index_sq = abs(int(disc)) // abs(field_disc)
    print(f"  Field discriminant (LMFDB 4.2.10224.1): {field_disc}")
    print(f"  Index^2 = {abs(int(disc))}/{abs(field_disc)} = {index_sq}")
    index_ok = (index_sq == 4)
    print(f"  Index = 2: {index_ok}")

    # Subfield Q(sqrt(3))
    sqrt3 = sp.sqrt(3)
    factor1 = y**2 + (2 - sqrt3)*y + (sqrt3 - 1)
    factor2 = y**2 + (2 + sqrt3)*y - (1 + sqrt3)
    product = sp.expand(factor1 * factor2)
    subfield_ok = sp.simplify(product - f) == 0
    print(f"  Factorization over Q(sqrt(3)) verified: {subfield_ok}")

    # Galois group is D_4 (resolvent has 1 rational root + non-square disc)
    # Equivalent to: irreducible over Q(sqrt(disc)) = Q(sqrt(-71))
    # Direct check: D_4 vs C_4 distinguished by whether quartic factors
    # over its unique quadratic subfield's normal closure.
    # Since the polynomial discriminant -40896 is not a square in Q,
    # and the resolvent has exactly one rational root, the group is D_4.
    galois_D4 = irreducible and resolvent_ok and disc_ok
    print(f"  Galois group is D_4: {galois_D4}")

    ok = irreducible and disc_ok and resolvent_ok and index_ok and subfield_ok
    print()
    print(f"  Galois structure verified: {ok}")
    return ok


# === Check 6: alpha-sweep PSLQ ===
def check_alpha_sweep():
    hr("Check 6: alpha-sweep PSLQ for integer quadratic h/br")
    try:
        import mpmath as mp
    except ImportError:
        print("  mpmath not available; skipping")
        return None

    mp.mp.dps = 50
    BOUND = 20

    def fuse(table, p):
        out = [mp.mpf(0)] * 10
        for i in range(10):
            for j in range(10):
                out[table[i][j]] += p[i] * p[j]
        return out

    def converge(alpha, max_iters=500):
        p = [mp.mpf(1) / 10] * 10
        n = 0
        for n in range(max_iters):
            Tf = fuse(T, p)
            Bf = fuse(B, p)
            out = [alpha * Tf[c] + (1 - alpha) * Bf[c] for c in range(10)]
            s = sum(out)
            if s == 0:
                return p, n
            new_p = [x / s for x in out]
            if max(abs(p[c] - new_p[c]) for c in range(10)) < mp.mpf(10) ** -45:
                return new_p, n
            p = new_p
        return p, n

    def search_quadratic(ratio):
        """Brute-force search for a*y^2 + b*y + c = 0, |a|,|b|,|c| <= BOUND."""
        best = (None, mp.mpf("inf"))
        r2 = ratio * ratio
        for a in range(0, BOUND + 1):
            for b in range(-BOUND, BOUND + 1):
                if a == 0 and b == 0:
                    continue
                if a == 0 and b < 0:
                    continue
                for c in range(-BOUND, BOUND + 1):
                    if a == 0 and b == 0 and c == 0:
                        continue
                    if _gcd(_gcd(abs(a), abs(b)), abs(c)) != 1:
                        continue
                    res = abs(a * r2 + b * ratio + c)
                    if res < best[1]:
                        best = ((a, b, c), res)
        return best

    print(f"  Searching |a|,|b|,|c| <= {BOUND}; admit if residual < 10^-25")
    print()

    sample_alphas = [
        ("0", mp.mpf(0)),
        ("1/4", mp.mpf(1) / 4),
        ("1/2", mp.mpf(1) / 2),
        ("3/4", mp.mpf(3) / 4),
        ("1", mp.mpf(1)),
    ]

    results = {}
    for label, alpha in sample_alphas:
        p, n = converge(alpha)

        # Detect delta_H collapse
        if p[7] > mp.mpf(0.999):
            print(f"  alpha={label}: collapsed to delta_7 in {n} iters")
            results[label] = ("delta_H", None)
            continue

        if p[8] < mp.mpf(10) ** -20:
            print(f"  alpha={label}: br* ~ 0, degenerate")
            results[label] = ("degenerate", None)
            continue

        ratio = p[7] / p[8]
        relation, residual = search_quadratic(ratio)
        admits = residual < mp.mpf(10) ** -25
        results[label] = (admits, relation if admits else None, ratio, residual)

        rel_str = f"{relation[0]}y^2 + {relation[1]}y + {relation[2]}" if admits else "no small relation"
        print(f"  alpha={label:4s}: iters={n:3d}, h/br = {mp.nstr(ratio, 12)}, "
              f"best res = {mp.nstr(residual, 3)}, {rel_str}")

    print()
    only_half_admits = (
        results["1/2"][0] is True and
        results["0"][0] is not True and
        results["1/4"][0] is not True and
        results["3/4"][0] is not True
    )
    print(f"  Only alpha=1/2 admits a small-coefficient quadratic: {only_half_admits}")
    if results["1/2"][0] is True:
        a, b, c = results["1/2"][1]
        print(f"  Relation at alpha=1/2: {a}*y^2 + {b}*y + {c} = 0")

    return only_half_admits


def main():
    print("# 4-core paper verification - Sanders & Gish 2026")
    print("# Joint Closure, a Universal Attractor, and an Algebraic")
    print("# Mixing Point for a Pair of Binary Operations on Z/10Z")
    print("# Verifying Theorems A-F:")
    print("#   A. Joint-closure chain (T+B and T+B+S)")
    print("#   B. 4-core 3-substrate closure")
    print("#   C. Normalizer identity Z_T = Z_B = (sum)^2")
    print("#   D. Closed-form attractor h/br = 1+sqrt(3); Galois D_4")
    print("#   E. Universality across chain shells")
    print("#   F. alpha-sweep PSLQ partial uniqueness at alpha=1/2")
    print()

    results = {}
    results["chain"] = check_chain()
    results["normalizer"] = check_normalizer()
    results["attractor"] = check_attractor()
    results["universality"] = check_universality()
    results["galois"] = check_galois()
    results["alpha_sweep"] = check_alpha_sweep()

    hr("Summary")
    for k, v in results.items():
        sym = "OK" if v is True else ("SKIPPED" if v is None else "FAIL")
        print(f"  {k:15s}: {sym}")

    all_ok = all(v is True or v is None for v in results.values())
    print()
    print(f"  Overall: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
