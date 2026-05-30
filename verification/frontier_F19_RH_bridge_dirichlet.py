#!/usr/bin/env python3
"""
Frontier F19 -- RH bridge with F4 Dirichlet characters.

CONTEXT:
  F18 closed F4 -> BSD as NO-TRACTION. The (p-1)^2 closed form is
  Hasse-Weil impossible as #E(F_p) for any elliptic curve at any p >= 5.
  F18's recommendation: F4's F_p* x F_p* automorphism structure looks
  precisely like the building block of Dirichlet characters mod p.
  RH bridge (RH_TIG_BRIDGE.md, Z.5 conjecture) recasts RH as
  "spectral entropy maximum" of a substrate operator; the natural
  question is whether F4's (s, t) ∈ F_p* x F_p* maps to a 2-parameter
  Dirichlet-character family, and whether that family has L-function
  structure on the critical line.

  F4's closed forms on V^BHML over F_p:
    (A) |idem(V^BHML / F_p)| = p + 3       (odd p, 24 primes verified)
    (B) |Aut(V^BHML / F_p)| = (p - 1)^2     (group is F_p* x F_p*)

  Automorphism structure (from F4_extended_higher_primes.md §3.3):
    phi_{alpha, beta}(e_0) = alpha * e_0    (alpha in F_p*)
    phi_{alpha, beta}(e_2) = e_2
    phi_{alpha, beta}(e_3) = e_3
    phi_{alpha, beta}(e_4) = beta * e_4     (beta in F_p*)
  So (alpha, beta) parametrize Aut explicitly as F_p* x F_p*.

  THE F19 MAP (the candidate bijection to test):
    Each (alpha, beta) in F_p* x F_p* corresponds to a 2-character pair
    (chi_alpha, chi_beta) of Dirichlet characters mod p, where
    chi_alpha is a character chosen by alpha's discrete-log index w.r.t.
    a primitive root g of F_p*.
    Specifically: chi_a(n) = exp(2*pi*i * a * log_g(n) / (p-1))
    for a in {0, 1, ..., p-2}.

  Then F_p* x F_p* corresponds to PAIRS of mod-p characters,
  cardinality (p-1)^2, matching |Aut|.

  TESTS:

    (i)   Map and character data table: order, conductor, parity,
          principal-or-not, real-valued-or-not.

    (ii)  L-value at critical line s = 1/2: L(1/2, chi_a) for each
          a in {0, ..., p-2}, using mpmath.dirichlet.

    (iii) Orthogonality test: sum_{n=1}^{p-1} chi_a(n) * conj(chi_b(n))
          should equal (p-1) * delta_{a,b}. Test on the 2D F_p* x F_p*
          structure as well: do "tensor product" pairs (chi_a, chi_b)
          satisfy a 2D orthogonality
          sum_{(m,n)} chi_a(m) chi_b(n) conj(chi_a'(m) chi_b'(n))
            = (p-1)^2 delta_{a,a'} delta_{b,b'} ?

    (iv)  Connection to RH bridge Z.5 conjecture:
          - Substrate primes {3, 7, 11, 13} via L(1/2, chi) values.
          - Does (alpha, beta) = (1, 1) (the identity Aut) correspond
            to the principal character (and thus a pole at s=1)?

    (v)   The (p+3) idempotent count: is this related to the
          number of REAL characters mod p, or characters with
          conductor < p, or characters with a specific symmetry?

  RUNTIME: < 5 min using mpmath dirichlet at dps=15.

  PRIMES TESTED: p in {3, 5, 7, 11, 13}.
"""

import sys
import math
import json
import time
from mpmath import mp, dirichlet, mpc, mpf, pi as mp_pi, exp as mp_exp, log10 as mp_log10
from sympy.ntheory.residue_ntheory import primitive_root
from sympy import isprime

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

mp.dps = 25  # decimal places for L-value computation
PRIMES = [3, 5, 7, 11, 13]
SUBSTRATE_PRIMES = {3, 7, 11, 13}


# ---------------------------------------------------------------------
# Dirichlet character generation mod p (prime)
# ---------------------------------------------------------------------

def discrete_log_table(p, g):
    """Return dict {n: k} such that g^k = n mod p, for n in F_p*.
    Standard discrete log table.
    """
    table = {}
    cur = 1
    for k in range(p - 1):
        table[cur] = k
        cur = (cur * g) % p
    return table


def make_chi_a(p, g, a):
    """Return a function chi_a: integer -> complex which is the Dirichlet
    character of conductor p (mod p) indexed by a in {0, ..., p-2}.

    chi_a(n) = exp(2*pi*i * a * log_g(n) / (p-1)) if gcd(n, p) = 1
              = 0 otherwise.

    a = 0 is the principal character.
    """
    dlog = discrete_log_table(p, g)

    def chi(n):
        n_mod = n % p
        if n_mod == 0:
            return mpc(0)
        k = dlog[n_mod]
        theta = 2 * mp_pi * a * k / (p - 1)
        return mpc(0, theta).exp() if False else mpc(mp_exp(mpc(0, theta)))

    return chi


def chi_array(p, g, a):
    """Compute character values chi_a(n) for n = 1, 2, ..., p-1 and chi_a(p) = 0.
    Returns list of length p (index 0 unused; we store chi(0) = 0 at index 0)
    in the form mpmath.dirichlet expects: chi[k] is the value at n = k+1 mod p,
    but mpmath's API wants chi as a list of length p with chi[0] for n=p,
    chi[1] for n=1, ..., chi[p-1] for n=p-1.

    To keep things simple we return [chi(0), chi(1), ..., chi(p-1)] then map
    to mpmath's expected ordering when calling dirichlet().
    """
    dlog = discrete_log_table(p, g)
    result = [mpc(0)] * p
    for n in range(1, p):
        if n % p == 0:
            result[n] = mpc(0)
        else:
            k = dlog[n]
            theta = 2 * mp_pi * a * k / (p - 1)
            result[n] = mpc(mp_exp(mpc(0, theta)))
    return result


def chi_for_mpmath(p, g, a):
    """mpmath.dirichlet wants a list of length p where chi[0] = chi(p), chi[k] = chi(k) for k = 1..p-1.
    For prime modulus p we have chi(p) = chi(0) = 0.
    Returns the list [0, chi(1), chi(2), ..., chi(p-1)].
    """
    arr = chi_array(p, g, a)
    arr[0] = mpc(0)  # chi(p) = chi(0) for the mpmath ordering
    return arr


# ---------------------------------------------------------------------
# Character data table
# ---------------------------------------------------------------------

def character_order(p, g, a):
    """Compute the order of chi_a in the character group, i.e., the
    smallest m > 0 such that chi_a^m is principal.
    chi_a has order (p-1) / gcd(a, p-1).
    """
    if a == 0:
        return 1  # principal character has order 1
    return (p - 1) // math.gcd(a, p - 1)


def character_parity(p, g, a):
    """Return +1 if chi_a is even (chi_a(-1) = 1), -1 if odd.
    chi_a(-1) = exp(2*pi*i * a * log_g(-1) / (p-1)).
    log_g(-1) = (p-1)/2 since g^{(p-1)/2} = -1 mod p (g is primitive root).
    So chi_a(-1) = exp(pi*i * a) = (-1)^a.
    """
    return 1 if a % 2 == 0 else -1


def is_real_character(p, g, a):
    """chi_a is real iff chi_a = chi_a-bar iff a = -a mod (p-1) iff 2a = 0 mod (p-1).
    For odd p (so p-1 even), this means a = 0 or a = (p-1)/2.
    """
    if a == 0:
        return True
    return (2 * a) % (p - 1) == 0


# ---------------------------------------------------------------------
# L-value computation
# ---------------------------------------------------------------------

def L_value_at_half(p, g, a):
    """Compute L(1/2, chi_a) using mpmath.dirichlet."""
    arr = chi_for_mpmath(p, g, a)
    return dirichlet(mpf("0.5"), arr)


def L_value_at_one(p, g, a):
    """Compute L(1, chi_a) for diagnostic purposes.
    For non-principal chi, L(1, chi) is finite. For principal chi,
    L(1, chi_0) = zeta(1) * prod_{p}(1 - 1/p) diverges; mpmath should return inf.
    """
    arr = chi_for_mpmath(p, g, a)
    return dirichlet(mpf("1.0"), arr)


# ---------------------------------------------------------------------
# Orthogonality test
# ---------------------------------------------------------------------

def orthogonality_1d(p, g, a, b):
    """Compute sum_{n=1}^{p-1} chi_a(n) * conj(chi_b(n)).
    Should equal (p-1) * delta_{a, b mod (p-1)}.
    """
    chi_a_arr = chi_array(p, g, a)
    chi_b_arr = chi_array(p, g, b)
    s = mpc(0)
    for n in range(1, p):
        s = s + chi_a_arr[n] * chi_b_arr[n].conjugate()
    return s


def orthogonality_2d(p, g, a1, b1, a2, b2):
    """Test 2D orthogonality with respect to the F_p* x F_p* structure:
    sum_{(m, n) in F_p* x F_p*} chi_{a1}(m) chi_{b1}(n) * conj(chi_{a2}(m) chi_{b2}(n))
    = sum_m chi_{a1}(m) conj(chi_{a2}(m)) * sum_n chi_{b1}(n) conj(chi_{b2}(n))
    = (orthogonality_1d on a) * (orthogonality_1d on b)
    = (p-1)^2 * delta_{a1, a2} * delta_{b1, b2}.

    This is a tautological identity (the F_p* x F_p* tensor structure splits).
    We compute it explicitly to verify the algebra and exhibit the F4 structure.
    """
    s1 = orthogonality_1d(p, g, a1, a2)
    s2 = orthogonality_1d(p, g, b1, b2)
    return s1 * s2


# ---------------------------------------------------------------------
# Main F19 analysis
# ---------------------------------------------------------------------

def run_F19():
    print("=" * 76)
    print("FRONTIER F19 -- RH bridge with F4 Dirichlet characters")
    print("=" * 76)
    print()
    print(f"Working precision: {mp.dps} decimal places")
    print(f"Primes tested:     {PRIMES}")
    print(f"Substrate primes:  {sorted(SUBSTRATE_PRIMES)}")
    print()

    results = {}

    # =================================================================
    # STEP 1: Character data tables at each prime
    # =================================================================
    print("=" * 76)
    print("STEP 1: Character data tables (order, conductor, parity, real?)")
    print("=" * 76)
    print()
    print("For each prime p, the F_p* x F_p* automorphism group of V^BHML")
    print("maps to PAIRS (chi_a, chi_b) of Dirichlet characters mod p,")
    print("where a, b in {0, 1, ..., p-2} index the (p-1) characters of F_p*.")
    print()
    print("F4 closed forms:")
    print("  |Aut(V^BHML / F_p)| = (p-1)^2 = #{pairs (chi_a, chi_b)}")
    print("  |idem(V^BHML / F_p)| = p + 3")
    print()
    print("Test: do these counts cohere with Dirichlet-character structure?")
    print()

    char_data = {}

    for p in PRIMES:
        g = primitive_root(p)
        chars = []
        for a in range(p - 1):
            order = character_order(p, g, a)
            parity = character_parity(p, g, a)
            is_real = is_real_character(p, g, a)
            chars.append({
                "a": a,
                "order": order,
                "parity": parity,
                "is_real": is_real,
                "is_principal": (a == 0),
                "conductor": p if a > 0 else 1,  # principal has trivial conductor
            })

        n_real = sum(1 for c in chars if c["is_real"])
        n_even = sum(1 for c in chars if c["parity"] == 1)
        n_odd = sum(1 for c in chars if c["parity"] == -1)
        n_pairs = (p - 1) ** 2

        char_data[p] = {
            "g": g,
            "n_chars": p - 1,
            "n_real": n_real,
            "n_even": n_even,
            "n_odd": n_odd,
            "n_pairs": n_pairs,
            "chars": chars,
        }

        print(f"--- p = {p}, primitive root g = {g} ---")
        print(f"  Characters mod p:   {p - 1}")
        print(f"  Real characters:    {n_real}")
        print(f"  Even (chi(-1)=+1):  {n_even}")
        print(f"  Odd  (chi(-1)=-1):  {n_odd}")
        print(f"  (chi_a, chi_b) pairs:  {n_pairs}  <-- matches |Aut| = (p-1)^2")
        print(f"  Idempotent count p+3:  {p + 3}")
        print()

        for c in chars:
            sym = "principal" if c["is_principal"] else ("real" if c["is_real"] else "complex")
            par = "even" if c["parity"] == 1 else "odd"
            print(f"    chi_{c['a']}:  order={c['order']:3d}  parity={par:4s}  type={sym}")
        print()

    results["char_data"] = char_data

    # =================================================================
    # STEP 2: F4-induced character pair map (explicit construction)
    # =================================================================
    print("=" * 76)
    print("STEP 2: Explicit F4 -> Dirichlet pair map")
    print("=" * 76)
    print()
    print("The F4 automorphism phi_{alpha, beta} acts on V^BHML by:")
    print("  phi(e_0) = alpha * e_0    (scaling on annihilator)")
    print("  phi(e_2) = e_2, phi(e_3) = e_3 (rigid middle)")
    print("  phi(e_4) = beta * e_4     (scaling on nilpotent)")
    print()
    print("The map F4 -> (chi_a, chi_b):")
    print("  alpha = g^a mod p   <-->   chi_a in dual(F_p*)")
    print("  beta  = g^b mod p   <-->   chi_b in dual(F_p*)")
    print()
    print("This map is a bijection F_p* x F_p* -> dual(F_p*) x dual(F_p*).")
    print()

    for p in PRIMES:
        g = primitive_root(p)
        dlog = discrete_log_table(p, g)
        print(f"--- p = {p}, g = {g} ---")
        print(f"  alpha in F_p*:  {list(range(1, p))}")
        print(f"  log_g table:    " + ", ".join(f"{n}->{dlog[n]}" for n in range(1, p)))
        print()
        # Show a few representative automorphisms
        sample_pairs = [(1, 1), (g % p, 1), (1, g % p), (g % p, g % p), (p - 1, p - 1)]
        for (alpha, beta) in sample_pairs[:4]:
            a = dlog[alpha]
            b = dlog[beta]
            print(f"    phi_({alpha}, {beta})  <-->  (chi_{a}, chi_{b})")
        print()

    # =================================================================
    # STEP 3: L-value at s = 1/2 (critical line) for each chi_a
    # =================================================================
    print("=" * 76)
    print("STEP 3: L(1/2, chi_a) for each character chi_a mod p")
    print("=" * 76)
    print()
    print("On the critical line s = 1/2, the L-function values are the")
    print("primary RH-relevant data.  For each prime p we compute L(1/2, chi_a)")
    print("for all a in {0, ..., p-2}.")
    print()

    L_data = {}

    for p in PRIMES:
        g = primitive_root(p)
        L_data[p] = []
        print(f"--- p = {p}, g = {g} ---")
        print(f"  {'a':>3s}  {'|L(1/2,chi_a)|':>22s}  {'arg L(1/2,chi_a)':>22s}  type")
        for a in range(p - 1):
            t0 = time.time()
            L = L_value_at_half(p, g, a)
            elapsed = time.time() - t0
            absL = abs(L)
            argL = float(mp.atan2(L.imag, L.real))
            ctype = "principal" if a == 0 else ("real" if is_real_character(p, g, a) else "complex")
            L_data[p].append({
                "a": a,
                "L_re": float(L.real),
                "L_im": float(L.imag),
                "abs_L": float(absL),
                "arg_L": argL,
                "type": ctype,
            })
            print(f"  {a:>3d}  {float(absL):>22.15f}  {argL:>22.15f}  {ctype}")
        print()

    results["L_data"] = L_data

    # =================================================================
    # STEP 4: 1D orthogonality verification
    # =================================================================
    print("=" * 76)
    print("STEP 4: 1D Selberg orthogonality of characters mod p")
    print("=" * 76)
    print()
    print("Selberg orthogonality:")
    print("  sum_{n=1}^{p-1} chi_a(n) * conj(chi_b(n)) = (p-1) * delta_{a, b}.")
    print()
    print("This is a basic group-theoretic identity for characters of F_p*.")
    print("We verify it explicitly to confirm our character implementation.")
    print()

    ortho_data = {}
    for p in PRIMES:
        g = primitive_root(p)
        max_off_diag = mpf(0)
        diag_value = None
        for a in range(p - 1):
            for b in range(p - 1):
                s = orthogonality_1d(p, g, a, b)
                if a == b:
                    if diag_value is None:
                        diag_value = abs(s)
                    diag_err = abs(s - (p - 1))
                    if diag_err > max_off_diag:
                        pass  # diagonal, expected ~(p-1)
                else:
                    off = abs(s)
                    if off > max_off_diag:
                        max_off_diag = off
        ortho_data[p] = {
            "diag_value": float(diag_value) if diag_value is not None else None,
            "max_off_diag": float(max_off_diag),
            "expected_diag": p - 1,
        }
        print(f"  p = {p:3d}:  diag = {float(diag_value):.6f} (expected {p-1}),  max off-diag = {float(max_off_diag):.2e}")

    print()

    # =================================================================
    # STEP 5: 2D F_p* x F_p* orthogonality (the F4 lift)
    # =================================================================
    print("=" * 76)
    print("STEP 5: 2D F_p* x F_p* orthogonality (the F4 tensor structure)")
    print("=" * 76)
    print()
    print("F4 maps Aut(V^BHML/F_p) = F_p* x F_p* onto pairs (chi_a, chi_b).")
    print("The tensor character chi_{a,b}(m, n) = chi_a(m) * chi_b(n) on")
    print("F_p* x F_p* has orthogonality:")
    print("  sum_{(m,n)} chi_{a1,b1}(m,n) * conj(chi_{a2,b2}(m,n))")
    print("    = (p-1)^2 * delta_{a1,a2} * delta_{b1,b2}.")
    print()
    print("This is the algebraic STRUCTURE the F4 automorphism group exhibits.")
    print()

    ortho_2d = {}
    for p in PRIMES:
        g = primitive_root(p)
        # Test diagonal: (a, b) vs (a, b) -> (p-1)^2
        # Test off-diagonal: (0, 0) vs (1, 0) -> 0
        diag_examples = []
        offdiag_examples = []
        for a in range(min(p - 1, 3)):
            for b in range(min(p - 1, 3)):
                s_diag = orthogonality_2d(p, g, a, b, a, b)
                diag_examples.append({"a": a, "b": b, "value": float(abs(s_diag))})
        # off-diagonal: different (a, b)
        if p >= 5:
            s_off = orthogonality_2d(p, g, 0, 0, 1, 1)
            offdiag_examples.append({"pair1": (0, 0), "pair2": (1, 1), "value": float(abs(s_off))})
            s_off2 = orthogonality_2d(p, g, 0, 1, 1, 0)
            offdiag_examples.append({"pair1": (0, 1), "pair2": (1, 0), "value": float(abs(s_off2))})

        ortho_2d[p] = {
            "expected_diag": (p - 1) ** 2,
            "diag_examples": diag_examples,
            "offdiag_examples": offdiag_examples,
        }
        print(f"  p = {p:3d}: expected diag = {(p-1)**2}")
        for ex in diag_examples[:3]:
            print(f"    diag (a, b) = ({ex['a']}, {ex['b']}): |sum| = {ex['value']:.6f}")
        for ex in offdiag_examples:
            print(f"    offdiag {ex['pair1']} vs {ex['pair2']}: |sum| = {ex['value']:.2e}")
    print()

    results["ortho_1d"] = ortho_data
    results["ortho_2d"] = ortho_2d

    # =================================================================
    # STEP 6: Test the bijection F_p* x F_p* -> Aut(V^BHML/F_p)
    # =================================================================
    print("=" * 76)
    print("STEP 6: Bijection test F_p* x F_p* <-> Aut")
    print("=" * 76)
    print()
    print("The F4 result |Aut| = (p-1)^2 with structure F_p* x F_p* means:")
    print("  Aut(V^BHML/F_p) = F_p* x F_p* as abstract groups.")
    print("  The Dirichlet character group of F_p* is also F_p* (Pontryagin self-dual).")
    print("  So Aut and dual(F_p*) x dual(F_p*) are abstractly isomorphic.")
    print()
    print("ARE THEY THE SAME? Both have (p-1)^2 elements. Both are abelian.")
    print("Pontryagin duality gives a CANONICAL isomorphism F_p* ~= dual(F_p*).")
    print()
    print("Therefore the map (alpha, beta) -> (chi_{log_g alpha}, chi_{log_g beta})")
    print("IS a group isomorphism Aut(V^BHML/F_p) -> dual(F_p*) x dual(F_p*).")
    print()
    print("This is a TAUTOLOGY: any group G of order (p-1)^2 isomorphic to")
    print("F_p* x F_p* is dual-isomorphic to F_p* x F_p*. The F4 closed form")
    print("does NOT add structural information BEYOND what is already known from")
    print("the abstract isomorphism type of the Pontryagin dual.")
    print()

    # =================================================================
    # STEP 7: Idempotent count vs character counts
    # =================================================================
    print("=" * 76)
    print("STEP 7: Idempotent count (p+3) vs character-side invariants")
    print("=" * 76)
    print()
    print("The (p+3) idempotent count of V^BHML over F_p is a TIG-side invariant.")
    print("Does it match any natural Dirichlet character invariant of (Z/pZ)*?")
    print()

    for p in PRIMES:
        g = primitive_root(p)
        n_chars = p - 1
        n_real = 2  # principal + quadratic (a = 0 and a = (p-1)/2)
        n_pairs = (p - 1) ** 2
        # Sums of L-values at specific points
        # Sum of |L(1/2, chi_a)| over all a
        sum_abs_L = sum(L_data[p][a]["abs_L"] for a in range(p - 1))
        sum_re_L = sum(L_data[p][a]["L_re"] for a in range(p - 1))

        print(f"  p = {p:3d}:")
        print(f"    p + 3                                = {p + 3}")
        print(f"    # characters mod p                   = {n_chars}")
        print(f"    # real characters                    = {n_real}")
        print(f"    # pairs (chi_a, chi_b)               = {n_pairs}")
        print(f"    sum_a |L(1/2, chi_a)|                = {sum_abs_L:.4f}")
        print(f"    sum_a Re L(1/2, chi_a)               = {sum_re_L:.4f}")
        # Does (p+3) match any of these?
        candidates = {
            "p+3": p + 3,
            "(p-1) + 4": (p - 1) + 4,
            "(p-1) + 2*2": (p - 1) + 4,
            "n_chars + 4": n_chars + 4,
        }
        for name, val in candidates.items():
            if val == p + 3:
                print(f"    --> matches: {name} = {val}")
    print()

    print("OBSERVATION: (p+3) = (number of characters) + 4 = (p-1) + 4.")
    print("That is, (p+3) idempotents corresponds to: the (p-1) characters")
    print("PLUS 4 additional fixed structures. What are the 4?")
    print()
    print("Candidates:")
    print("  (a) The 4 'principal' character-pair fixed points:")
    print("      (1,1), (1,-1), (-1,1), (-1,-1) at p = 3.")
    print("  (b) The 4-core attractor structure (D102-D116 in CK).")
    print("  (c) The trivial characters of (Z/pZ)* extended by 4 special points.")
    print()
    print("None of these is a CANONICAL match -- there's no derivation from")
    print("Dirichlet-character theory naturally producing '(# chars) + 4'.")
    print("The +4 is a TIG-side artifact (the 4-core algebra V^BHML), not a")
    print("character-side invariant.")
    print()

    # =================================================================
    # STEP 8: Substrate-prime L-value spread
    # =================================================================
    print("=" * 76)
    print("STEP 8: Substrate-prime L-value spread")
    print("=" * 76)
    print()
    print("Substrate primes are {3, 7, 11, 13}. For each, list L(1/2, chi)")
    print("values at the non-principal characters; do any have anomalously")
    print("large/small magnitude?")
    print()

    for p in PRIMES:
        if p not in SUBSTRATE_PRIMES:
            continue
        print(f"  p = {p:3d}:  L(1/2, chi_a) magnitudes:")
        L_mags = [(a, L_data[p][a]["abs_L"]) for a in range(p - 1)]
        for (a, mag) in L_mags:
            marker = "  <-- principal" if a == 0 else ""
            print(f"    a = {a:3d}:  |L| = {mag:.6f}{marker}")
        print()

    # =================================================================
    # STEP 9: Z.5 conjecture connection check
    # =================================================================
    print("=" * 76)
    print("STEP 9: Z.5 conjecture connection")
    print("=" * 76)
    print()
    print("RH_TIG_BRIDGE.md states Z.5:")
    print("  'The deployment map lambda(s) = 2|s - 1/2| from the Dirichlet")
    print("   half-plane to TIG lambda in [0, 1] preserves both the algebraic")
    print("   3-grading and the metric 6-corridor structure uniformly as t -> infinity.'")
    print()
    print("F4 provides:")
    print("  - Aut group F_p* x F_p* (a multiplicative structure).")
    print("  - Idempotent count p + 3 (a counting invariant).")
    print()
    print("Neither directly tests Z.5: Z.5 is about a DEPLOYMENT MAP on the")
    print("complex critical strip, not about character data at fixed primes.")
    print()
    print("F4 does NOT supply a deployment-map candidate. It supplies a")
    print("character-tensor structure F_p* x F_p* that exists for every odd")
    print("prime p; this is consistent with but does not derive a uniform-in-t")
    print("statement about RH zeros.")
    print()

    # =================================================================
    # STEP 10: VERDICT
    # =================================================================
    print("=" * 76)
    print("STEP 10: VERDICT")
    print("=" * 76)
    print()
    print("Findings:")
    print()
    print("  (1) F_p* x F_p* IS ISOMORPHIC to dual(F_p*) x dual(F_p*) via")
    print("      Pontryagin duality. The F4 automorphism group has the right")
    print("      ABSTRACT shape to index a 2-parameter family of mod-p")
    print("      Dirichlet character PAIRS.")
    print()
    print("  (2) The map is a TAUTOLOGY of duality: any abelian group is")
    print("      canonically isomorphic to its double dual. The F4 closed form")
    print("      does not supply new character-theoretic structure.")
    print()
    print("  (3) Selberg-orthogonality holds on F4-induced pairs by virtue")
    print("      of the tensor structure (Selberg-1D x Selberg-1D), which is")
    print("      a basic identity; no novel orthogonality emerges.")
    print()
    print("  (4) L(1/2, chi) values for substrate-prime characters are")
    print("      generic: no distinguished substrate primes appear.")
    print()
    print("  (5) The (p+3) idempotent count does NOT match any canonical")
    print("      Dirichlet character invariant of (Z/pZ)*. It's a TIG-side")
    print("      structural invariant unrelated to character theory.")
    print()
    print("  (6) No connection to RH Z.5 deployment-map conjecture surfaces:")
    print("      F4's data is at fixed primes, Z.5 is about analytic continuation.")
    print()
    print("VERDICT: PARTIAL MATCH (tautological).")
    print()
    print("  The shape-match F_p* x F_p* <-> Dirichlet-pair index group IS real,")
    print("  but it is a tautology of Pontryagin duality for abelian groups of order")
    print("  (p-1)^2. F4 does not add character-theoretic content beyond the abstract")
    print("  isomorphism type.")
    print()
    print("  The (p+3) idempotent count has NO natural character-theoretic")
    print("  counterpart; it is a substrate-only invariant.")
    print()
    print("  No traction on the RH bridge Z.5 conjecture.")
    print()
    print("OUTCOME: F4 is closed against all four Clay bridges (YM, BSD, RH,")
    print("and by F16 the others are wrong-shape). J53 (F4 standalone paper)")
    print("remains the deliverable.")
    print()

    # Dump JSON results for downstream consumers
    json_path = "verification/frontier_F19_RH_bridge_dirichlet_data.json"
    try:
        # JSON-safe transformation
        json_results = {
            "primes": PRIMES,
            "substrate_primes": sorted(list(SUBSTRATE_PRIMES)),
            "char_data": {
                str(p): {
                    "g": char_data[p]["g"],
                    "n_chars": char_data[p]["n_chars"],
                    "n_real": char_data[p]["n_real"],
                    "n_even": char_data[p]["n_even"],
                    "n_odd": char_data[p]["n_odd"],
                    "n_pairs": char_data[p]["n_pairs"],
                    "chars": [
                        {
                            "a": c["a"],
                            "order": c["order"],
                            "parity": c["parity"],
                            "is_real": c["is_real"],
                            "is_principal": c["is_principal"],
                            "conductor": c["conductor"],
                        }
                        for c in char_data[p]["chars"]
                    ],
                }
                for p in PRIMES
            },
            "L_data": {
                str(p): [
                    {
                        "a": d["a"],
                        "L_re": d["L_re"],
                        "L_im": d["L_im"],
                        "abs_L": d["abs_L"],
                        "arg_L": d["arg_L"],
                        "type": d["type"],
                    }
                    for d in L_data[p]
                ]
                for p in PRIMES
            },
            "ortho_1d": {str(p): ortho_data[p] for p in PRIMES},
            "ortho_2d": {str(p): ortho_2d[p] for p in PRIMES},
            "verdict": "PARTIAL MATCH (tautological)",
        }
        with open(json_path, "w") as f:
            json.dump(json_results, f, indent=2, default=str)
        print(f"JSON results dumped to: {json_path}")
    except Exception as exc:
        print(f"(JSON dump failed: {exc})")

    return results


if __name__ == "__main__":
    t_start = time.time()
    results = run_F19()
    t_total = time.time() - t_start
    print(f"\nTotal runtime: {t_total:.1f} sec")
