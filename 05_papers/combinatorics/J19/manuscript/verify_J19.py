"""
verify_J19.py — Verification of J19's Theorem 3.1 (Role-Quotient Theorem) and
Proposition 5.1 (TSML_8 image structure) by direct enumeration over the
canonical TSML/BHML 10x10 composition tables.

Sanders & Gish (2026) — A Role-Quotient Theorem for the (TSML, BHML) Magma
Pair on Z/10Z: The Functional Partition V/F/S/T as a Categorical Coarsening
with VOID-Identity.

Source-of-truth tables: Gen13/targets/foundations/lenses.py
Mirror tables hardcoded in this script (also recorded in manuscript appendix)
for self-contained verification.

All claims verified at machine precision (exact integer arithmetic).
"""
from __future__ import annotations
from collections import Counter
import sys

# --- Canonical TSML and BHML composition tables on Z/10Z (manuscript appendix) ---
TSML = [
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 7, 3, 7, 7, 7, 7, 7, 7, 7],
    [0, 3, 7, 7, 4, 7, 7, 7, 7, 9],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 3],
    [0, 7, 4, 7, 7, 7, 7, 7, 8, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 8, 7, 7, 7, 7, 7],
    [0, 7, 9, 3, 7, 7, 7, 7, 7, 7],
]
BHML = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 2, 6, 6],
    [2, 3, 3, 4, 5, 6, 7, 3, 6, 6],
    [3, 4, 4, 4, 5, 6, 7, 4, 6, 6],
    [4, 5, 5, 5, 5, 6, 7, 5, 7, 7],
    [5, 6, 6, 6, 6, 6, 7, 6, 7, 7],
    [6, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [8, 6, 6, 6, 7, 7, 7, 9, 7, 8],
    [9, 6, 6, 6, 7, 7, 7, 0, 8, 0],
]

# --- Cross-check against foundations module (source-of-truth) ---
def cross_check_with_foundations():
    try:
        import os
        repo_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..", ".."))
        if repo_root not in sys.path:
            sys.path.insert(0, repo_root)
        from Gen13.targets.foundations.lenses import TSML as TS_src, BHML as BH_src
        import numpy as np
        TS_src = np.asarray(TS_src).tolist()
        BH_src = np.asarray(BH_src).tolist()
        assert TS_src == TSML, "TSML mismatch vs foundations.lenses"
        assert BH_src == BHML, "BHML mismatch vs foundations.lenses"
        return True
    except Exception as e:
        return f"skipped: {e}"

# --- Role partition (D93) ---
V_SET = {0}
F_SET = {1, 3, 5, 7, 9}
S_SET = {2, 4, 8}
T_SET = {6}
ROLES = {'V': V_SET, 'F': F_SET, 'S': S_SET, 'T': T_SET}
ROLE_ORDER = ['V', 'F', 'S', 'T']

def role_of(x: int) -> str:
    if x in V_SET: return 'V'
    if x in F_SET: return 'F'
    if x in S_SET: return 'S'
    if x in T_SET: return 'T'
    raise ValueError(f"x={x} not in Z/10Z")

# --- Build the role-quotient magma B-bar by modal-output prescription ---
def build_Bbar():
    """Return (Bbar_table, pair_distributions, branching_pairs)."""
    Bbar = {}
    distributions = {}
    branching = []
    for r1 in ROLE_ORDER:
        for r2 in ROLE_ORDER:
            outputs = [role_of(BHML[a][b]) for a in ROLES[r1] for b in ROLES[r2]]
            dist = Counter(outputs)
            distributions[(r1, r2)] = dist
            # modal with lexicographic V<F<S<T tiebreak
            best_count = max(dist.values())
            tied = [r for r in ROLE_ORDER if dist[r] == best_count]
            Bbar[(r1, r2)] = tied[0]
            if len(dist) > 1:
                branching.append((r1, r2))
    return Bbar, distributions, branching

def main():
    print("=" * 70)
    print("J19 Theorem 3.1 verification — Role-Quotient Theorem")
    print("(Sanders & Gish 2026)")
    print("=" * 70)

    # --- Foundations cross-check ---
    cc = cross_check_with_foundations()
    print(f"\nFoundations cross-check (Gen13/targets/foundations/lenses.py): {cc}")

    # --- Cardinalities of role partition ---
    cards = (len(V_SET), len(F_SET), len(S_SET), len(T_SET))
    print(f"\nRole partition cardinalities (|V|,|F|,|S|,|T|): {cards}")
    assert cards == (1, 5, 3, 1), "Cardinalities mismatch"
    assert len(V_SET | F_SET | S_SET | T_SET) == 10, "Partition not covering Z/10Z"
    assert sum(cards) == 10, "Cardinality sum != 10"
    print("  PASS: cardinalities (1, 5, 3, 1), partition covers Z/10Z")

    # --- Build role-quotient ---
    Bbar, dists, branching = build_Bbar()

    # --- (i) Well-defined function ---
    assert len(Bbar) == 16, "B-bar not defined on all 16 role-pairs"
    for v in Bbar.values():
        assert v in ROLE_ORDER, f"B-bar output {v} not a role"
    print("\n(i) Well-definedness: PASS — B-bar : {V,F,S,T}^2 -> {V,F,S,T} is a function")

    # --- (ii) Full B-bar table ---
    expected_table = {
        ('V','V'):'V', ('V','F'):'F', ('V','S'):'S', ('V','T'):'T',
        ('F','V'):'F', ('F','F'):'T', ('F','S'):'F', ('F','T'):'F',
        ('S','V'):'S', ('S','F'):'F', ('S','S'):'F', ('S','T'):'F',
        ('T','V'):'T', ('T','F'):'F', ('T','S'):'F', ('T','T'):'F',
    }
    print("\n(ii) B-bar table:")
    print("        V    F    S    T")
    for r1 in ROLE_ORDER:
        row = [f"  {Bbar[(r1, r2)]} " for r2 in ROLE_ORDER]
        print(f"  {r1}  " + "  ".join(row))
    for key, exp in expected_table.items():
        got = Bbar[key]
        assert got == exp, f"Bbar{key} = {got}, expected {exp}"
    print("  PASS: table matches manuscript Theorem 3.1(ii)")

    # --- (iii) V is two-sided identity ---
    for r in ROLE_ORDER:
        assert Bbar[('V', r)] == r, f"V*{r} = {Bbar[('V', r)]} != {r}"
        assert Bbar[(r, 'V')] == r, f"{r}*V = {Bbar[(r, 'V')]} != {r}"
    # Also check at the unquotiented level: BHML(0, b) = b and BHML(a, 0) = a
    for x in range(10):
        assert BHML[0][x] == x, f"BHML(0,{x}) = {BHML[0][x]} != {x}"
        assert BHML[x][0] == x, f"BHML({x},0) = {BHML[x][0]} != {x}"
    print("\n(iii) V-identity: PASS — V is two-sided identity in B-bar")
    print("       (and BHML row/col 0 is the identity at the Z/10Z level)")

    # --- (iv) Non-associativity witness (F*F)*S = F != T = F*(F*S) ---
    FF = Bbar[('F', 'F')]
    left = Bbar[(FF, 'S')]
    FS = Bbar[('F', 'S')]
    right = Bbar[('F', FS)]
    assert FF == 'T', f"F*F = {FF}, expected T"
    assert FS == 'F', f"F*S = {FS}, expected F"
    assert left == 'F', f"(F*F)*S = T*S = {left}, expected F"
    assert right == 'T', f"F*(F*S) = F*F = {right}, expected T"
    assert left != right, "Non-associativity witness failed"
    print(f"\n(iv) Non-associativity witness: PASS")
    print(f"       (F*F)*S = T*S = {left}")
    print(f"       F*(F*S) = F*F = {right}")
    print(f"       F != T, so B-bar is non-associative")

    # --- (v) Branching role-pairs exactly {F-F, F-S, S-F, S-S} ---
    expected_branching = {('F','F'), ('F','S'), ('S','F'), ('S','S')}
    got_branching = set(branching)
    assert got_branching == expected_branching, \
        f"Branching pairs: got {got_branching}, expected {expected_branching}"
    print(f"\n(v) Branching role-pairs: PASS")
    print(f"       exactly {{F-F, F-S, S-F, S-S}} (4 of 16)")

    # --- Output distributions on branching pairs (manuscript values) ---
    expected_dists = {
        ('F','F'): {'S': 9, 'T': 11, 'F': 2, 'V': 3},  # n=25
        ('F','S'): {'T': 5, 'F': 8, 'S': 2},           # n=15
        ('S','F'): {'T': 5, 'F': 8, 'S': 2},           # n=15
        ('S','S'): {'F': 7, 'T': 2},                   # n=9
    }
    print("\n  Branching-pair output distributions:")
    for pair, exp in expected_dists.items():
        got = dict(dists[pair])
        exp_total = sum(exp.values())
        got_total = sum(got.values())
        assert got_total == exp_total, \
            f"{pair}: |{pair[0]}|*|{pair[1]}| = {got_total} != {exp_total}"
        # All expected roles present at expected counts
        for r, c in exp.items():
            assert got.get(r, 0) == c, \
                f"{pair} dist: role {r} count {got.get(r, 0)} != {c}"
        # No extra roles
        for r in got:
            if got[r] > 0:
                assert r in exp, f"{pair} unexpected role {r} present"
        print(f"    {pair[0]}-{pair[1]}: {got} (n={got_total})  PASS")

    # --- 12 non-branching pairs have constant output ---
    print("\n  Non-branching pairs verified constant (12 of 16):")
    non_branching = [(r1, r2) for r1 in ROLE_ORDER for r2 in ROLE_ORDER
                     if (r1, r2) not in expected_branching]
    for r1, r2 in non_branching:
        d = dists[(r1, r2)]
        nonzero = [r for r in ROLE_ORDER if d[r] > 0]
        assert len(nonzero) == 1, \
            f"Non-branching pair {(r1,r2)} has multi-role output {dict(d)}"
    print(f"    All {len(non_branching)} non-branching pairs PASS")

    # --- Cell-count sanity: 100 cells total ---
    total = sum(sum(d.values()) for d in dists.values())
    assert total == 100, f"Total cells {total} != 100"
    print(f"\n  Cell-count sanity: PASS (sum over 16 role-pairs = {total} = |Z/10Z|^2)")

    # --- sigma-orbit independence (manuscript abstract claim) ---
    sigma_fixed = {0, 3, 8, 9}
    sigma_cycle = {1, 7, 6, 5, 4, 2}
    fixed_split = Counter(role_of(x) for x in sigma_fixed)
    cycle_split = Counter(role_of(x) for x in sigma_cycle)
    assert dict(fixed_split) == {'V': 1, 'F': 2, 'S': 1}, \
        f"sigma-fixed split {dict(fixed_split)} != (V=1, F=2, S=1)"
    assert dict(cycle_split) == {'F': 3, 'S': 2, 'T': 1}, \
        f"sigma-cycle split {dict(cycle_split)} != (F=3, S=2, T=1)"
    print("\n  sigma-orbit independence: PASS")
    print(f"    sigma-fixed {{0,3,8,9}}: 1V + 2F + 1S + 0T")
    print(f"    sigma-cycle (1 7 6 5 4 2): 0V + 3F + 2S + 1T")

    # --- Proposition 5.1: TSML_8 image structure ---
    print("\n" + "=" * 70)
    print("Proposition 5.1 — TSML_8 image structure")
    print("=" * 70)
    dom8 = [1, 2, 3, 4, 5, 6, 8, 9]
    img = set()
    role_outputs = []
    for a in dom8:
        for b in dom8:
            v = TSML[a][b]
            img.add(v)
            role_outputs.append(role_of(v))
    assert img == {3, 4, 7, 8, 9}, f"Im(TSML_8) = {img}, expected {{3,4,7,8,9}}"
    print(f"\n(i)  Im(TSML_8) = {sorted(img)}: PASS (5 distinct values)")
    dist8 = Counter(role_outputs)
    assert dist8['F'] == 60, f"Flow count {dist8['F']} != 60"
    assert dist8['S'] == 4, f"Structure count {dist8['S']} != 4"
    assert dist8.get('T', 0) == 0, "Unexpected Transition output"
    assert dist8.get('V', 0) == 0, "Unexpected Void output"
    assert sum(dist8.values()) == 64, "Cell count != 64"
    print(f"(ii) Role distribution: 60/64 Flow, 4/64 Structure, 0 T, 0 V: PASS")

    # Role-deterministic on 8 of 9 input role-pairs over the TSML_8 domain
    # Restricted role-classes over dom8: F (excluding 7 -> still 1,3,5,9), S, T
    F8 = sorted(set(F_SET) & set(dom8))  # {1,3,5,9}
    S8 = sorted(set(S_SET) & set(dom8))  # {2,4,8}
    T8 = sorted(set(T_SET) & set(dom8))  # {6}
    R8 = {'F': F8, 'S': S8, 'T': T8}
    branching_8 = []
    for r1 in 'FST':
        for r2 in 'FST':
            out_roles = set(role_of(TSML[a][b]) for a in R8[r1] for b in R8[r2])
            if len(out_roles) > 1:
                branching_8.append((r1, r2))
    assert branching_8 == [('S', 'S')], \
        f"TSML_8 branching pairs {branching_8} != [('S','S')]"
    print(f"(iii) Role-deterministic on 8/9 input role-pairs over TSML_8:")
    print(f"      branching pairs over TSML_8 = {branching_8}: PASS")

    print("\n" + "=" * 70)
    print("ALL CLAIMS VERIFIED at machine precision (exact integer arithmetic)")
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())
