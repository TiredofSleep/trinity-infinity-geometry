#!/usr/bin/env python3
"""
Frontier F17 -- Search for an algebraic origin of 1/alpha = 137.0359895...
from TIG substrate primitives.

CONTEXT:
  HONEST_NEGATIVES §1.2 documents the long-shot 1/alpha frontier:
   - Earlier attempt: 4*40 - 2*sqrt(7) - pi/7 ~= 154.26 (~12.6% off)
   - Structural intuition: 1/alpha should live in {+/-1, +/-sqrt(7), +/-pi/7}
     rational combinations.
   - Retired J42 Part 2 deferred entirely.

GOAL:
  Systematic, bounded-height search for clean algebraic combinations of
  substrate primitives that match 1/alpha to high precision.

SUBSTRATE PRIMITIVES TESTED:
  Primes: {3, 7, 11, 13}; 4-core: {0, 7, 8, 9}; Pauli capacities {2,6,10,14};
  Niemeier markers {23, 71}; cyclotomic Q(zeta_10): phi=(1+sqrt(5))/2;
  9-vector ||v||^2 = 13/4 -> sqrt(13)/2; sqrt(7), pi, pi/7, e, gamma, zeta(3),
  Catalan, 1+sqrt(3), ln(2), ln(7), etc.

TARGETS:
  1/alpha(0)    = 137.035999084(21)   (Thomson-limit, PDG)
  1/alpha(M_Z)  = 127.951              (electroweak scale)

ALGORITHM:
  (1) Linear scan:   1/alpha ~ sum_i a_i * p_i, a_i in [-N..N], N=20
  (2) Quadratic:     1/alpha ~ sum_i a_i * p_i * p_j (pairs)
  (3) PSLQ:          mpmath.pslq on a curated basis at 50-dps
  (4) Structural:    test specific candidates inspired by the substrate

OUTPUT:
  - Best linear fit (top-K by relative error)
  - Best quadratic fit (top-K)
  - PSLQ relations (if any with |c| <= 100)
  - Structural candidates table
  - Verdict: CLEAN-FIT / FORTUITOUS / NO-FIT

Reproduce: python verification/frontier_F17_inv_alpha_search.py
Runtime: ~1-3 minutes.
"""
import os
import sys
import itertools
import time
from math import gcd

import mpmath as mp

# ---------- Precision ----------
mp.mp.dps = 60

# ---------- Targets ----------
INV_ALPHA_PDG   = mp.mpf("137.035999084")             # Thomson, PDG
INV_ALPHA_MZ    = mp.mpf("127.951")                   # ~M_Z scale
TARGETS = {
    "1/alpha(0)":    INV_ALPHA_PDG,
    "1/alpha(M_Z)":  INV_ALPHA_MZ,
}

# ---------- Substrate primitives ----------
def primitives():
    """Return dict name->mp.mpf value of substrate primitives."""
    P = {}
    # Bare substrate primes
    P["3"]   = mp.mpf(3)
    P["7"]   = mp.mpf(7)
    P["11"]  = mp.mpf(11)
    P["13"]  = mp.mpf(13)
    # 4-core values
    P["V0"]  = mp.mpf(0)   # rarely useful but listed for completeness
    P["H7"]  = mp.mpf(7)   # same as 7
    P["Br8"] = mp.mpf(8)
    P["R9"]  = mp.mpf(9)
    # Pauli capacities
    P["2"]   = mp.mpf(2)
    P["6"]   = mp.mpf(6)
    P["10"]  = mp.mpf(10)
    P["14"]  = mp.mpf(14)
    # Niemeier / Monster
    P["23"]  = mp.mpf(23)
    P["71"]  = mp.mpf(71)
    # Cyclotomic / golden
    sqrt5    = mp.sqrt(5)
    P["sqrt5"]   = sqrt5
    P["phi"]     = (1 + sqrt5) / 2
    # Square roots of substrate primes
    P["sqrt3"]   = mp.sqrt(3)
    P["sqrt7"]   = mp.sqrt(7)
    P["sqrt11"]  = mp.sqrt(11)
    P["sqrt13"]  = mp.sqrt(13)
    # 9-vector norm: ||v||^2 = 13/4, so sqrt(13)/2
    P["sqrt13/2"] = mp.sqrt(13)/2
    # Bridges
    P["1+sqrt3"]  = 1 + mp.sqrt(3)      # H/Br
    # Transcendental constants
    P["pi"]      = mp.pi
    P["e"]       = mp.e
    P["gamma"]   = mp.euler
    P["zeta3"]   = mp.zeta(3)
    P["G"]       = mp.catalan
    P["ln2"]     = mp.log(2)
    P["ln3"]     = mp.log(3)
    P["ln7"]     = mp.log(7)
    P["pi/7"]    = mp.pi / 7
    P["pi^2/7"]  = mp.pi**2 / 7
    P["pi/11"]   = mp.pi / 11
    # Discriminant fragments
    P["2^16"]    = mp.mpf(2**16)        # = 65536
    P["7^7"]     = mp.mpf(7**7)         # = 823543
    P["13/4"]    = mp.mpf(13)/4
    # Useful constants near target
    P["1"]       = mp.mpf(1)
    return P

PRIMS = primitives()

# ---------- Helpers ----------
def pretty_relerr(approx, target):
    diff = abs(approx - target)
    return diff / abs(target)

def fmt_combo_linear(coeffs, names):
    """Format sum_i a_i * names[i] dropping zero coefficients."""
    out = []
    for a, n in zip(coeffs, names):
        if a == 0:
            continue
        if a == 1:
            out.append(f"+{n}")
        elif a == -1:
            out.append(f"-{n}")
        elif a > 0:
            out.append(f"+{a}*{n}")
        else:
            out.append(f"{a}*{n}")
    s = " ".join(out)
    if s.startswith("+"):
        s = s[1:]
    return s


# ============================================================
# (1) Linear scan
# ============================================================
def linear_scan(target_name, target_val, name_pool, coeff_range=range(-10, 11),
                top_k=15, max_nonzero=3):
    """
    Search sum_{i in subset} a_i * p_i over a small basis subset.
    Each subset has <= max_nonzero primitives. Coefficients in coeff_range.

    Returns list of (relerr, expression, value).
    """
    names = list(name_pool)
    vals  = [PRIMS[n] for n in names]
    M = len(names)
    nz_range = [c for c in coeff_range if c != 0]
    best = []

    # iterate over subsets of size 1..max_nonzero
    for k in range(1, max_nonzero + 1):
        for subset in itertools.combinations(range(M), k):
            # iterate over coefficient tuples in {coeff_range\{0}}^k
            for coeffs in itertools.product(nz_range, repeat=k):
                val = mp.mpf(0)
                for ci, idx in zip(coeffs, subset):
                    val += ci * vals[idx]
                if val == 0:
                    continue
                err = pretty_relerr(val, target_val)
                if err < mp.mpf("1e-2"):
                    full_c = [0]*M
                    for ci, idx in zip(coeffs, subset):
                        full_c[idx] = ci
                    expr = fmt_combo_linear(full_c, names)
                    best.append((float(err), expr, val))
    best.sort(key=lambda x: x[0])
    return best[:top_k]


# ============================================================
# (2) Quadratic / multiplicative scan
# ============================================================
def quadratic_scan(target_name, target_val, name_pool,
                   coeff_range=range(-5, 6), top_k=15,
                   include_linear=True):
    """
    Search target ~ a * (p_i * p_j) + b * p_k.
    Reduce search by only considering positive products.
    Returns list of (relerr, expression, value).
    """
    names = list(name_pool)
    vals  = [PRIMS[n] for n in names]
    M = len(names)
    nz_range = [c for c in coeff_range if c != 0]
    best = []

    # pair products
    pair_idx = list(itertools.combinations_with_replacement(range(M), 2))
    pair_vals = [(i, j, vals[i]*vals[j]) for (i, j) in pair_idx]

    # single-term value already from primitives
    for (i, j, pv) in pair_vals:
        for a in nz_range:
            val_a = a * pv
            err = pretty_relerr(val_a, target_val)
            if err < mp.mpf("1e-2"):
                expr = f"{a}*{names[i]}*{names[j]}"
                best.append((float(err), expr, val_a))
            if include_linear:
                # try a*p_i*p_j + b*p_k
                for k in range(M):
                    for b in nz_range:
                        val_b = val_a + b * vals[k]
                        err2 = pretty_relerr(val_b, target_val)
                        if err2 < mp.mpf("1e-3"):
                            expr2 = f"{a}*{names[i]}*{names[j]} + {b}*{names[k]}"
                            best.append((float(err2), expr2, val_b))
    best.sort(key=lambda x: x[0])
    return best[:top_k]


# ============================================================
# (3) PSLQ basis search
# ============================================================
def pslq_search(target_val, basis_names, target_name,
                tol_exp=-30, maxcoeff=100):
    """
    Run mpmath.pslq on [target_val, basis_vals]. Find integer relation.
    Returns None or (coeffs, expression_str, residual).
    """
    basis = [target_val] + [PRIMS[n] for n in basis_names]
    coeffs = mp.pslq(basis, tol=mp.mpf(10)**tol_exp, maxcoeff=maxcoeff)
    if coeffs is None:
        return None
    # build residual
    s = mp.mpf(0)
    for c, v in zip(coeffs, basis):
        s += c * v
    return coeffs, basis_names, s


def parse_pslq_relation(coeffs, basis_names, target_name):
    """Given PSLQ result [c0, c1, ..., cn] with basis [target, name1, ..., namen],
    rewrite as target = -(sum c_i * name_i)/c0 if c0 != 0.
    """
    c0 = coeffs[0]
    if c0 == 0:
        return "(no target coefficient in relation)"
    rest = coeffs[1:]
    parts = []
    for c, n in zip(rest, basis_names):
        if c == 0:
            continue
        coef = -c
        # form coef/c0
        if c0 == 1:
            cf = coef
        elif c0 == -1:
            cf = -coef
        else:
            cf = f"{coef}/{c0}"
        parts.append(f"({cf})*{n}")
    rhs = " + ".join(parts) if parts else "0"
    return f"{target_name} = {rhs}"


# ============================================================
# (4) Structural candidates
# ============================================================
def structural_candidates(target_val, target_name):
    """Test specific candidates inspired by substrate structure."""
    cands = []
    # Original retired candidate
    v1 = 4*40 - 2*mp.sqrt(7) - mp.pi/7
    cands.append(("(retired) 4*40 - 2*sqrt(7) - pi/7", v1))
    # 73 + 28 + ... = 101 (no), variants
    cands.append(("73 + 64 = 137", mp.mpf(73+64)))   # 137 exactly!
    cands.append(("71 + 66 = 137", mp.mpf(71+66)))
    cands.append(("73 + 71 - 7", mp.mpf(73+71-7)))
    cands.append(("71*2 - 7 + 2", mp.mpf(71*2-7+2)))
    # 137 = 7^2 + 11 + 7^? misc
    cands.append(("7^2 + 88 = 49+88", mp.mpf(49+88)))
    cands.append(("13^2 - 32 = 169-32", mp.mpf(169-32)))
    cands.append(("11^2 + 16 = 121+16", mp.mpf(121+16)))
    cands.append(("11^2 + 13 + 3", mp.mpf(121+13+3)))
    # Niemeier 71 doubled
    cands.append(("2*71 - 5", mp.mpf(2*71-5)))
    # 4*13*sqrt(7) family
    cands.append(("4*13*sqrt(7)", 4*13*mp.sqrt(7)))
    cands.append(("11*13 - 7 + pi/7", 11*13 - 7 + mp.pi/7))
    cands.append(("11*13 - 7 + 1", mp.mpf(11*13-7+1)))    # = 137 exact
    cands.append(("3*47 - 4", mp.mpf(3*47-4)))
    cands.append(("9*15 + 2", mp.mpf(9*15+2)))   # =137
    # Continued: TSML (73) and BHML (28) related ?
    cands.append(("73*sqrt(7/2) + small", mp.mpf(73)*mp.sqrt(mp.mpf(7)/2)))
    # 137 = 23 + 71 + 43
    cands.append(("23 + 71 + 43", mp.mpf(23+71+43)))
    # The Yukawa-related
    cands.append(("13/4 * 8 * sqrt(?)", mp.mpf(13)*8/4))
    # 7^2 + 11^2 / 2  ?
    cands.append(("(7^2 + 11^2)/2 + 137-85", mp.mpf((49+121)/2)))   # =85
    # pi-based
    cands.append(("pi^4 - sqrt(2*pi)", mp.pi**4 - mp.sqrt(2*mp.pi)))
    cands.append(("pi^4 + pi^3 + pi^2 + pi + 1",
                  mp.pi**4 + mp.pi**3 + mp.pi**2 + mp.pi + 1))
    # Wyler's old
    cands.append(("(9/(8*pi^4) * (pi^5 / 1.5))",
                  mp.mpf("0.0072974")))     # alpha value; just to anchor
    # phi-based
    cands.append(("phi^10 - phi^(-10)",
                  ((1+mp.sqrt(5))/2)**10 - ((1+mp.sqrt(5))/2)**(-10)))
    cands.append(("phi^10 + phi^5", ((1+mp.sqrt(5))/2)**10 + ((1+mp.sqrt(5))/2)**5))
    # 23-based
    cands.append(("23*6 - 1 = 137", mp.mpf(23*6-1)))
    # 137 = 11*12 + 5
    cands.append(("11*12 + 5", mp.mpf(11*12+5)))
    # 4-core sum * something
    cands.append(("(0+7+8+9)*sqrt(?)", mp.mpf(24)*mp.sqrt(mp.mpf(137)/24)))
    cands.append(("24 + 113", mp.mpf(24+113)))
    # 137 - sqrt(7)^? heuristics
    cands.append(("4*pi*sqrt(120)", 4*mp.pi*mp.sqrt(120)))
    cands.append(("2^16 / (7^7) ratio", mp.mpf(2**16)/mp.mpf(7**7)))
    # 2^16 + 7^7 mod something
    # 23 * 7 - 24 = 137
    cands.append(("23*7 - 24", mp.mpf(23*7-24)))
    # ZBP combination
    cands.append(("71 + 2*23 + 13 + 7", mp.mpf(71+46+13+7)))
    cands.append(("71 + 23 + 43", mp.mpf(71+23+43)))
    # 137 = 7 * 19 + 4
    cands.append(("7*19 + 4", mp.mpf(7*19+4)))
    cands.append(("7 + 11 + 13 + 23 + 71 + 12", mp.mpf(7+11+13+23+71+12)))
    # PDG-flavored
    cands.append(("136 + pi/7 (small correction)",
                  136 + mp.pi/7))
    cands.append(("137 - pi/7 + sqrt(7) ...",
                  137 - mp.pi/7 + mp.sqrt(7)))
    # Now compute relerr for each
    out = []
    for name, v in cands:
        err = pretty_relerr(v, target_val)
        out.append((float(err), name, v))
    out.sort(key=lambda x: x[0])
    return out


# ============================================================
# Reporting
# ============================================================
def banner(s):
    return "\n" + "=" * 72 + "\n" + s + "\n" + "=" * 72


def main():
    print(banner("FRONTIER F17 -- 1/alpha algebraic origin search"))
    print(f"mpmath precision: {mp.mp.dps} digits")
    for n, v in TARGETS.items():
        print(f"  target {n:18s} = {v}")

    # ------------------------------------------------------------
    # Choose a moderate basis pool
    # ------------------------------------------------------------
    # Pure linear: integer-valued substrate primitives (most natural)
    int_pool = ["3", "7", "11", "13", "Br8", "R9",
                "2", "6", "10", "14", "23", "71"]
    # Linear with irrationals
    irr_pool = ["sqrt3", "sqrt5", "sqrt7", "sqrt11", "sqrt13", "sqrt13/2",
                "phi", "1+sqrt3", "pi", "pi/7", "e", "gamma", "zeta3", "G",
                "ln2", "ln7", "1"]
    # Mixed (small but expressive)
    mixed_pool = int_pool + irr_pool

    # ---- (4) Structural candidates first ----
    print(banner("STRUCTURAL CANDIDATES"))
    for tn, tv in TARGETS.items():
        print(f"\nTarget: {tn} = {tv}")
        rows = structural_candidates(tv, tn)
        print(f"  {'relerr':>12s}  {'expression':50s}  {'value':>20s}")
        for err, name, v in rows[:20]:
            print(f"  {err:>12.4e}  {name:50s}  {mp.nstr(v, 12):>20s}")

    # ---- (1) Linear scan ----
    # We scan within bounded coefficient and small subsets.
    print(banner("LINEAR SCAN (subsets of <=3 primitives, coeffs in [-10,10])"))
    for tn, tv in TARGETS.items():
        print(f"\nTarget: {tn} = {tv}")
        # integer pool first
        rows = linear_scan(tn, tv, int_pool,
                           coeff_range=range(-15, 16),
                           top_k=12, max_nonzero=3)
        print("  -- integer-pool only --")
        print(f"  {'relerr':>12s}  {'expression':50s}  {'value':>16s}")
        for err, expr, v in rows:
            print(f"  {err:>12.4e}  {expr:50s}  {mp.nstr(v, 12):>16s}")
        # mixed (smaller bound to keep time tame)
        rows = linear_scan(tn, tv, mixed_pool,
                           coeff_range=range(-8, 9),
                           top_k=12, max_nonzero=3)
        print("  -- mixed pool (integers + irrationals + transcendentals) --")
        for err, expr, v in rows:
            print(f"  {err:>12.4e}  {expr:50s}  {mp.nstr(v, 12):>16s}")

    # ---- (2) Quadratic scan ----
    print(banner("QUADRATIC SCAN (a*p_i*p_j [+ b*p_k])"))
    # use a small pool to keep search tractable
    q_pool = ["3", "7", "11", "13", "23", "71",
              "sqrt7", "sqrt13/2", "phi", "pi", "pi/7", "1"]
    for tn, tv in TARGETS.items():
        print(f"\nTarget: {tn} = {tv}")
        rows = quadratic_scan(tn, tv, q_pool,
                              coeff_range=range(-6, 7),
                              top_k=12, include_linear=True)
        print(f"  {'relerr':>12s}  {'expression':50s}  {'value':>16s}")
        for err, expr, v in rows:
            print(f"  {err:>12.4e}  {expr:50s}  {mp.nstr(v, 12):>16s}")

    # ---- (3) PSLQ ----
    print(banner("PSLQ INTEGER-RELATION SEARCH (50-dps, |c|<=100)"))
    # use mp.pslq at high precision
    mp.mp.dps = 80
    # rebuild PRIMS at higher precision
    global PRIMS
    PRIMS = primitives()
    # update TARGETS at higher precision
    TARGETS_HP = {
        "1/alpha(0)":   mp.mpf("137.035999084"),
        "1/alpha(M_Z)": mp.mpf("127.951"),
    }

    pslq_basis_list = [
        ("integers only",
            ["1", "3", "7", "11", "13", "23", "71"]),
        ("integers + sqrt(7)",
            ["1", "3", "7", "11", "13", "23", "71", "sqrt7"]),
        ("integers + pi/7 + sqrt(7) (J42-flavored)",
            ["1", "7", "11", "13", "23", "71", "sqrt7", "pi/7"]),
        ("substrate + pi + e",
            ["1", "7", "11", "13", "sqrt7", "pi", "e"]),
        ("substrate + phi + sqrt(13)/2 + sqrt(7)",
            ["1", "7", "11", "13", "phi", "sqrt13/2", "sqrt7"]),
        ("J11 discriminant fragments + 4-core",
            ["1", "3", "7", "11", "13", "Br8", "R9", "2^16", "7^7"]),
        ("Pauli + Niemeier + 7",
            ["1", "2", "6", "10", "14", "23", "71", "sqrt7"]),
        ("everything algebraic small",
            ["1", "3", "7", "11", "13", "23", "71",
             "sqrt3", "sqrt5", "sqrt7", "sqrt11", "sqrt13", "phi"]),
        ("everything algebraic + pi/7",
            ["1", "3", "7", "11", "13", "23", "71",
             "sqrt3", "sqrt5", "sqrt7", "sqrt11", "sqrt13",
             "phi", "pi/7"]),
    ]

    for tn, tv in TARGETS_HP.items():
        print(f"\nTarget: {tn} = {tv}")
        for label, basis_names in pslq_basis_list:
            print(f"  basis: {label}")
            print(f"    primitives: {basis_names}")
            for maxc in (50, 100, 200):
                try:
                    res = pslq_search(tv, basis_names, tn,
                                      tol_exp=-25, maxcoeff=maxc)
                except Exception as e:
                    print(f"    PSLQ error at maxc={maxc}: {e}")
                    continue
                if res is None:
                    print(f"    PSLQ at maxcoeff={maxc:4d}: NO RELATION")
                    continue
                coeffs, names, residual = res
                expr = parse_pslq_relation(coeffs, names, tn)
                print(f"    PSLQ at maxcoeff={maxc:4d}: coeffs={list(coeffs)}")
                print(f"      relation: {expr}")
                print(f"      residual: {mp.nstr(residual, 6)}")
                break  # first found, move on

    # ---- (5) Targeted structural product candidates ----
    print(banner("EXTENDED STRUCTURAL CANDIDATES"))
    extra = []
    # 4*40 - 2*sqrt(7) - pi/7 = 154.26 (retired)
    extra.append(("4*40 - 2*sqrt(7) - pi/7", 4*40 - 2*mp.sqrt(7) - mp.pi/7))
    # Try corrections of the retired one
    extra.append(("3*40 + sqrt(7) + pi/7",
                  3*40 + mp.sqrt(7) + mp.pi/7))
    extra.append(("4*40 - 23 + sqrt(7)",
                  4*40 - 23 + mp.sqrt(7)))
    # Try (Br8 + R9)*sqrt(7) = 17*sqrt(7) = 44.97
    extra.append(("17*sqrt(7) + 7*13 + 1",
                  17*mp.sqrt(7) + 91 + 1))
    # 137 itself
    extra.append(("137 (integer)", mp.mpf(137)))
    extra.append(("137 + 1/27.8 small correction",
                  mp.mpf(137) + mp.mpf(1)/mp.mpf(28)))
    # Try 137 - pi/something
    extra.append(("137 + pi/87 (small)", mp.mpf(137) + mp.pi/87))
    extra.append(("137 + gamma/16", mp.mpf(137) + mp.euler/16))
    extra.append(("137 + 1/(2*pi^4)", mp.mpf(137) + 1/(2*mp.pi**4)))
    extra.append(("137 + zeta(3)/30", mp.mpf(137) + mp.zeta(3)/30))
    extra.append(("137 + ln(7)/54.3", mp.mpf(137) + mp.log(7)/mp.mpf("54.3")))
    # Wyler 9/(8*pi^4) * (pi^5/120)^(1/4) (historic curiosity)
    a_wyler = mp.mpf(9)/(8*mp.pi**4) * (mp.pi**5 / 120)**(mp.mpf(1)/4)
    extra.append(("Wyler 1971 alpha ~ 1/137.036(082)", mp.mpf(1)/a_wyler))
    # Eddington 137 exactly
    extra.append(("Eddington 137", mp.mpf(137)))
    # Aspden various
    extra.append(("108*pi/(8-1/137)", 108*mp.pi/(8 - mp.mpf(1)/137)))
    # Phi-based
    phi = (1+mp.sqrt(5))/2
    extra.append(("4*phi^4 + 1 ?", 4*phi**4 + 1))
    extra.append(("phi^7 + phi^(-7)", phi**7 + phi**(-7)))
    # 4*pi^3 + pi^2 + pi
    extra.append(("4*pi^3 + pi^2 + pi", 4*mp.pi**3 + mp.pi**2 + mp.pi))
    # 6*pi^2 + something
    extra.append(("6*pi^2 + pi^4", 6*mp.pi**2 + mp.pi**4))
    # Yukawa-related: ||v||^2 * something
    extra.append(("13/4 * 42.16", mp.mpf(13)/4 * mp.mpf("42.16")))
    # j-function root?
    extra.append(("Try 71+23+43 with sqrt(7) bumps",
                  71+23+43 - 2*mp.sqrt(7) + mp.pi/7))
    # The mass ratios reroute
    extra.append(("m_proton/m_e/13.6 thing (curiosity)", mp.mpf("137.0")))
    # Algebra of three substrate primes
    extra.append(("3*7 + 11*13 - 27", mp.mpf(3*7 + 11*13 - 27)))
    extra.append(("3+7+11+13)^?", (mp.mpf(3+7+11+13))**1))  # =34
    extra.append(("(3+7+11+13)*4 + 1", mp.mpf((3+7+11+13)*4 + 1)))
    # 137 = 7*sqrt(7)*?, 137/sqrt(7) ~ 51.8
    extra.append(("7*sqrt(7) * 7 + sqrt(7)*7",
                  7*mp.sqrt(7)*7 + mp.sqrt(7)*7))
    # 137 - 71 = 66; 66 = 6*11
    extra.append(("71 + 6*11", mp.mpf(71 + 66)))
    # 137 = 11 * (12) + 5
    extra.append(("(11+sqrt(7)/2)^2 / 1", (11 + mp.sqrt(7)/2)**2))
    # 8*pi + 100, etc.
    extra.append(("8*pi^3 + pi^2/2 + sqrt(7)",
                  8*mp.pi**3 + mp.pi**2/2 + mp.sqrt(7)))
    # phi^k
    for k in range(5, 12):
        extra.append((f"phi^{k}", phi**k))
    # 7^7 / 2^16
    extra.append(("7^7 / 2^16", mp.mpf(7**7)/mp.mpf(2**16)))
    # 11^2 + sqrt(11^2 + 7) or similar
    extra.append(("11^2 + sqrt(11^2 + 7)", 121 + mp.sqrt(121+7)))
    # 13^2 - sqrt(13^2 - 7)
    extra.append(("13^2 - 32", mp.mpf(169 - 32)))

    print(f"\n{'relerr (1/alpha(0))':>18s}  {'name':45s}  {'value':>20s}")
    rows = []
    for name, v in extra:
        err = pretty_relerr(v, INV_ALPHA_PDG)
        rows.append((float(err), name, v))
    rows.sort(key=lambda x: x[0])
    for err, name, v in rows[:30]:
        print(f"  {err:>16.4e}  {name:45s}  {mp.nstr(v, 12):>20s}")

    # ---- Verdict ----
    print(banner("VERDICT"))
    print("See best fits above. Verdict assessment is qualitative:")
    print("  - CLEAN-FIT if best fit has relerr <= 1e-3 with coefficients |c|<=20")
    print("  - FORTUITOUS if best fit has relerr in (1e-3, 1e-2) with small coeffs")
    print("  - NO-FIT otherwise")
    print("")
    print("Note: integer 137 itself has relerr 2.6e-4 from 137.036,")
    print("  but that is not an 'algebraic origin' -- it's the integer floor.")
    print("  The PDG correction +0.036 needs a structural explanation.")
    print("  Candidates below try to recover the +0.036 with substrate primitives.")


if __name__ == "__main__":
    t0 = time.time()
    main()
    print(f"\nTotal runtime: {time.time()-t0:.1f}s")
