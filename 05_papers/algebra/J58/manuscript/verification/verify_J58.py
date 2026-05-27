"""verify_J58.py -- machine-precision verification of all theorems of J58.

CC-BY-4.0. (c) 2026 Brayden Ross Sanders / 7Site LLC. M. Gish co-author.

Verifies (Theorems A-F from §2-§4):
  A. The Lo Shu D_4 orbit has 8 distinct elements.
  B. The mod-3 reductions of the 8 orbit elements yield exactly 4 distinct
     magma tables, each appearing twice in the orbit.
  C. The two non-commutative tables T_1 and T_3 are opposite magmas
     (T_3[x][y] = T_1[y][x] for all x, y).
  D. All four tables are quasigroups (every row and every column is a
     permutation of {0, 1, 2}).
  E. The matrix cumulant kappa(M) = Tr(M^2) - Tr(M)^2 takes exactly two
     values across the 8 orbit elements: -48 for the 4 elements whose
     mod-3 reduction is commutative, +48 for the 4 elements whose mod-3
     reduction is non-commutative.
  F. T_2 (one of the commutative tables) is exactly Z/3.

Plus (Theorem E.1 from §3.2 and §7 Durer extension):
  E1. The V_4' subgroup of D_4 preserves kappa for ANY 3x3 matrix
      (verified on 100 random matrices).
  G. The same pattern (4 distinct mod-3 tables, 2 comm + 2 non-comm,
     kappa witness with values +/- 128) holds for the Durer 4x4
     magic square.

Run:  python verify_J58.py
Runtime: under 2 seconds on a 2020-era laptop.
"""
from itertools import product
import numpy as np


# The Lo Shu magic square.
LO_SHU = np.array([
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8],
], dtype=int)


def d4_orbit(M):
    """Generate the 8 elements of the D_4 orbit of M (as a list of np arrays).

    D_4 = {e, r, r^2, r^3, f, rf, r^2 f, r^3 f}, where r = 90-deg rotation
    and f = horizontal flip. We use numpy's rot90 and fliplr.
    """
    orbit = []
    seen = set()
    for k in range(4):
        for flip in (False, True):
            B = np.rot90(M, k)
            if flip:
                B = np.fliplr(B)
            key = tuple(B.flatten().tolist())
            if key not in seen:
                seen.add(key)
                orbit.append(B.copy())
    return orbit


def magma_table_of(M):
    """Return the 3x3 mod-3 magma table of M as a tuple of tuples."""
    return tuple(tuple(int(M[x][y]) % 3 for y in range(3)) for x in range(3))


def is_commutative(table):
    n = len(table)
    return all(table[x][y] == table[y][x]
               for x in range(n) for y in range(n))


def is_quasigroup(table):
    n = len(table)
    s = set(range(n))
    rows_ok = all(set(table[x]) == s for x in range(n))
    cols_ok = all(set(table[x][y] for x in range(n)) == s
                  for y in range(n))
    return rows_ok and cols_ok


def cumulant(M):
    """Tr(M^2) - Tr(M)^2 for a real square matrix M."""
    A = np.array(M, dtype=float)
    A2 = A @ A
    return float(np.trace(A2) - np.trace(A) ** 2)


def opposite_magma(table):
    """Return T'[x][y] = T[y][x]."""
    n = len(table)
    return tuple(tuple(table[y][x] for y in range(n)) for x in range(n))


# ============================================================================

def main():
    print("=" * 64)
    print(" J58 verification -- Lo Shu D_4 orbit mod 3")
    print("=" * 64)
    print()

    orbit = d4_orbit(LO_SHU)
    checks = []

    # CHECK 1 (Theorem A: orbit has 8 distinct elements)
    n_orbit = len(orbit)
    checks.append(("Theorem A (orbit has 8 distinct elements)",
                   n_orbit == 8))

    # Compute the four-table refinement
    tables_seen = {}
    for i, M in enumerate(orbit):
        t = magma_table_of(M)
        if t not in tables_seen:
            tables_seen[t] = {
                "indices": [],
                "is_commutative": is_commutative(t),
                "is_quasigroup": is_quasigroup(t),
                "cumulants": [],
            }
        tables_seen[t]["indices"].append(i)
        tables_seen[t]["cumulants"].append(cumulant(M))

    # CHECK 2 (Theorem B: 4 distinct tables, each appearing twice)
    n_tables = len(tables_seen)
    multiplicities = sorted(len(info["indices"])
                            for info in tables_seen.values())
    checks.append((
        "Theorem B (4 distinct mod-3 tables, each x2)",
        n_tables == 4 and multiplicities == [2, 2, 2, 2]
    ))

    # Sort tables for stable labeling: T_2 = Z/3 first by convention,
    # then by (is_commutative_desc, table_lex_order)
    Z3_table = tuple(tuple((x + y) % 3 for y in range(3))
                     for x in range(3))

    # Find T_2 = Z/3
    z3_present = Z3_table in tables_seen
    # CHECK 6 (Theorem F: Z/3 is in the orbit)
    checks.append(("Theorem F (Z/3 cyclic group is one of the tables)",
                   z3_present))

    # CHECK 4 (Theorem D: all 4 tables are quasigroups)
    all_quasi = all(info["is_quasigroup"]
                    for info in tables_seen.values())
    checks.append(("Theorem D (all 4 tables are quasigroups)", all_quasi))

    # CHECK 5 (Theorem E: cumulant +/-48 separates commutativity)
    epsilon = 1e-9
    correlation_ok = True
    for info in tables_seen.values():
        for c in info["cumulants"]:
            if info["is_commutative"]:
                if abs(c - (-48.0)) > epsilon:
                    correlation_ok = False
            else:
                if abs(c - 48.0) > epsilon:
                    correlation_ok = False
    checks.append((
        "Theorem E (cumulant +/-48 separates commutativity)",
        correlation_ok
    ))

    # CHECK 3 (Theorem C: the two non-commutative tables are opposites)
    non_comm_tables = [t for t, info in tables_seen.items()
                       if not info["is_commutative"]]
    if len(non_comm_tables) == 2:
        T_a, T_b = non_comm_tables
        opposite_pair = (opposite_magma(T_a) == T_b)
    else:
        opposite_pair = False
    checks.append((
        "Theorem C (two non-comm tables are opposite magmas)",
        opposite_pair
    ))

    # CHECK 7 (Theorem E.1: V_4' preserves kappa for ANY 3x3 matrix)
    # V_4' = {e, R^2, transpose, anti-diag flip}. In numpy convention,
    # this is the set of (rot_k, flip) with (k + int(flip)) even.
    rng = np.random.default_rng(42)
    v4_invariance_ok = True
    failed_examples = []
    for trial in range(100):
        M = rng.integers(-10, 11, size=(3, 3))
        kappas_v4 = []
        kappas_other = []
        for k in range(4):
            for flip in (False, True):
                B = np.rot90(M, k)
                if flip:
                    B = np.fliplr(B)
                kv = cumulant(B)
                if (k + int(flip)) % 2 == 0:
                    kappas_v4.append(round(kv, 6))
                else:
                    kappas_other.append(round(kv, 6))
        if len(set(kappas_v4)) != 1:
            v4_invariance_ok = False
            failed_examples.append(M.tolist())
        if len(set(kappas_other)) != 1:
            v4_invariance_ok = False
            failed_examples.append(M.tolist())
    checks.append((
        "Theorem E.1 (V_4' preserves kappa for any 3x3 matrix; 100 trials)",
        v4_invariance_ok
    ))

    # CHECK 8 (Theorem G: Durer 4x4 mod-3 has the same kappa-witness pattern
    # as Lo Shu, with values +/- 128).
    DURER = np.array([
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ])

    def is_comm_n(t):
        n = len(t)
        return all(t[x][y] == t[y][x]
                   for x in range(n) for y in range(n))

    def mod_n_table(M_arr, n, dim):
        return tuple(tuple(int(M_arr[i][j]) % n for j in range(dim))
                     for i in range(dim))

    durer_orbit = []
    for k in range(4):
        for flip in (False, True):
            B = np.rot90(DURER, k)
            if flip:
                B = np.fliplr(B)
            durer_orbit.append(B.copy())

    durer_tables = {}
    for M_arr in durer_orbit:
        t = mod_n_table(M_arr, 3, 4)
        if t not in durer_tables:
            durer_tables[t] = {"kappas": [],
                               "is_comm": is_comm_n(t)}
        durer_tables[t]["kappas"].append(round(cumulant(M_arr), 6))

    # Test: 4 distinct tables, 2 comm + 2 noncomm, kappa = +/- 128 witnesses comm
    n_durer_tables = len(durer_tables)
    n_durer_comm = sum(1 for info in durer_tables.values()
                       if info["is_comm"])
    n_durer_noncomm = sum(1 for info in durer_tables.values()
                          if not info["is_comm"])
    durer_kappa_ok = True
    for info in durer_tables.values():
        cs = set(info["kappas"])
        if info["is_comm"]:
            if cs != {-128.0}:
                durer_kappa_ok = False
        else:
            if cs != {128.0}:
                durer_kappa_ok = False
    durer_ok = (n_durer_tables == 4 and n_durer_comm == 2
                and n_durer_noncomm == 2 and durer_kappa_ok)
    checks.append((
        "Theorem G (Durer 4x4 mod-3: same pattern, kappa = +/- 128)",
        durer_ok
    ))

    # CHECK 9 (Diagonal Lemma: no 3x3 commutative quasigroup table has
    # constant-multiset diagonal). Exhaustively enumerate all 3x3 magma
    # tables on {0,1,2} (3^9 = 19683 of them), filter to commutative
    # quasigroups, and confirm none has a repeated diagonal entry.
    n_comm_quasi = 0
    n_with_repeat_diag = 0
    bad_table = None
    for entries in product(range(3), repeat=9):
        t = ((entries[0], entries[1], entries[2]),
             (entries[3], entries[4], entries[5]),
             (entries[6], entries[7], entries[8]))
        # Commutativity check
        if t[0][1] != t[1][0] or t[0][2] != t[2][0] or t[1][2] != t[2][1]:
            continue
        # Quasigroup check
        s = {0, 1, 2}
        if not (set(t[0]) == s and set(t[1]) == s and set(t[2]) == s):
            continue
        if not (set(t[i][0] for i in range(3)) == s
                and set(t[i][1] for i in range(3)) == s
                and set(t[i][2] for i in range(3)) == s):
            continue
        n_comm_quasi += 1
        # Diagonal check
        diag = (t[0][0], t[1][1], t[2][2])
        if len(set(diag)) < 3:
            n_with_repeat_diag += 1
            if bad_table is None:
                bad_table = t
    lemma_ok = (n_with_repeat_diag == 0 and n_comm_quasi > 0)
    checks.append((
        "Diagonal Lemma (no 3x3 comm-quasigroup has repeated diagonal; "
        f"{n_comm_quasi} found, {n_with_repeat_diag} violations)",
        lemma_ok
    ))

    # CHECK 10 (Corollary: V_4'-coset elements of L all have constant
    # diagonal mod 3, so by Lemma forced non-commutative.)
    L_diag_mod3 = sorted([int(LO_SHU[i, i]) % 3 for i in range(3)])
    L_antidiag_mod3 = sorted([int(LO_SHU[i, 2 - i]) % 3 for i in range(3)])
    corollary_ok = (len(set(L_diag_mod3)) == 1
                    and len(set(L_antidiag_mod3)) == 3)
    checks.append((
        f"Corollary (Lo Shu diag mod 3 = {{{L_diag_mod3[0]},{L_diag_mod3[1]},{L_diag_mod3[2]}}}={'constant' if len(set(L_diag_mod3)) == 1 else 'NOT-constant'}; anti-diag mod 3 = {set(L_antidiag_mod3)})",
        corollary_ok
    ))

    # Print results
    n_pass = 0
    print("Detailed checks:")
    for i, (name, ok) in enumerate(checks, start=1):
        status = "PASS" if ok else "FAIL"
        if ok:
            n_pass += 1
        print(f"  CHECK {i} ({name}): {status}")

    print()
    print(f"  Overall: {'PASS' if n_pass == len(checks) else 'FAIL'} "
          f"({n_pass}/{len(checks)})")

    # Display the 4 tables for the manuscript appendix
    print()
    print("-" * 64)
    print(" Detailed orbit information")
    print("-" * 64)
    print()
    print(f"  Orbit size: {n_orbit}")
    print(f"  Distinct mod-3 tables: {n_tables}")
    print()
    for j, (t, info) in enumerate(tables_seen.items(), start=1):
        cums = set(round(c, 6) for c in info["cumulants"])
        is_z3 = (t == Z3_table)
        labels = []
        labels.append("COMMUTATIVE" if info["is_commutative"]
                      else "NON-COMMUTATIVE")
        labels.append("QUASIGROUP" if info["is_quasigroup"]
                      else "NOT-QUASIGROUP")
        if is_z3:
            labels.append("== Z/3")
        labels_s = ", ".join(labels)
        print(f"  Table T{j}  ({labels_s})")
        print(f"    orbit indices: {info['indices']}")
        print(f"    cumulants: {sorted(cums)}")
        for row in t:
            print("    " + "  ".join(f"{v}" for v in row))
        print()

    # The full kappa table across orbit elements
    print("  Per-orbit-element cumulants:")
    for i, M in enumerate(orbit):
        t = magma_table_of(M)
        com_tag = "C" if tables_seen[t]["is_commutative"] else "N"
        print(f"    orbit[{i}]: cumulant = {cumulant(M):+.0f} ({com_tag})")

    return n_pass == len(checks)


if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
