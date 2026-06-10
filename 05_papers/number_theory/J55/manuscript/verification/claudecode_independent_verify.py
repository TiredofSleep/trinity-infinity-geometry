"""claudecode_independent_verify.py -- INDEPENDENT verification of the
2026-06-10 dim-6 kissing handoff claims (ClaudeCode pickup, action items
A1-A4).

Independence from the chat-session scripts:
  * q-expansions computed with EXACT INTEGER arithmetic (no mpmath series),
    via direct polynomial multiplication of (1-q^n)^6 factors.
  * Atkin-Lehner W_3 eigenvalue cross-checked TWO new ways:
      (i)  the newform relation a_p = -eps_p * p^(k/2-1) at p=3 (k=6):
           a_3 = +9  <=>  eps_3 = -1.
      (ii) direct numerical functional equation F(i/(3t)) = eps*(sqrt3*t)^6*F(it)
           tested at 6 values of t (mpmath, 30 dps).
  * Hecke structure verified via BOTH multiplicativity a_mn = a_m*a_n
    (gcd(m,n)=1) AND the prime-power recursion
           a_{p^2} = a_p^2 - p^5            (p coprime to level 3)
           a_{3^2} = a_3^2                  (ramified prime: a_{p^j}=a_p^j)
    which the chat-session script did NOT test.
  * psi_+ Laurent expansion to q^20 via exact integer series division
    (handoff's psi_plus_qexp.json only reached low order).

Checks:
  C1  eta^6*eta_3^6 q-expansion sanity: a_1=1, a_2=-6, a_3=9, a_4=4
  C2  Hecke multiplicativity for all coprime pairs (m,n), mn <= 100
  C3  prime-power recursion a_{p^2} = a_p^2 - p^5 for p in {2,5,7}
      and a_9 = a_3^2 (ramified)
  C4  Ramanujan-Petersson |a_p| <= 2 p^(5/2) for all p <= 97
  C5  A-L eigenvalue via newform relation: a_3 = +9 ==> eps_3 = -1
  C6  A-L eigenvalue via numerical functional equation (6 t-values)
  C7  E_6(q)^2 - 729*E_6(q^3)^2 constant term = -728 ==> residue of
      psi_+ at infinity = -728 = -(2^3 * 7 * 13)
  C8  psi_+ Laurent expansion to q^20 (exact), coefficient factorizations
      + strata/supersingular classification
  C9  psi_+ functional equation numerically: psi_+(i/(3t)) = +27 t^6 psi_+(it)
      (Fricke +1 at 6 t-values)

CC-BY-4.0. Sanders + Claude (ClaudeCode session 2026-06-10).
"""
import json
import os
from fractions import Fraction

import mpmath as mp

N_TRUNC = 130          # q-expansion truncation (need a_p through p=97)
PSI_ORDER = 80         # Laurent order computed for psi_+ (coefficients grow
                       # ~ e^(c sqrt(n)); 80 terms give clean numerics for C9)
PSI_REPORT = 20        # order reported/factored in stdout per action item A3

STRATA = {2, 3, 5, 7, 11, 13}
SUPERSINGULAR = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71}

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


# ----------------------------------------------------------------------
# Exact integer power series helpers (lists of ints, index = q-power)
# ----------------------------------------------------------------------

def series_mul(a, b, n):
    out = [0] * n
    for i, ai in enumerate(a):
        if ai == 0 or i >= n:
            continue
        for j, bj in enumerate(b):
            if i + j >= n:
                break
            if bj:
                out[i + j] += ai * bj
    return out


def eta_power6(n, step=1):
    """(prod_{m>=1} (1 - q^(step*m)))^6 truncated to q^n, exact ints."""
    # First the Euler product to the 1st power, then raise to 6th by
    # repeated multiplication (3 squarings would also work; keep simple).
    base = [0] * n
    base[0] = 1
    for m in range(1, n // step + 1):
        # multiply by (1 - q^(step*m))
        nxt = base[:]
        for i in range(n - step * m):
            if base[i]:
                nxt[i + step * m] -= base[i]
        base = nxt
    out = [0] * n
    out[0] = 1
    for _ in range(6):
        out = series_mul(out, base, n)
    return out


def sigma5(n):
    s = 0
    for d in range(1, n + 1):
        if n % d == 0:
            s += d ** 5
    return s


def E6_series(n, step=1):
    """E_6(step*tau) = 1 - 504 sum sigma_5(m) q^(step*m), exact ints."""
    out = [0] * n
    out[0] = 1
    for m in range(1, (n - 1) // step + 1):
        out[step * m] = -504 * sigma5(m)
    return out


def series_div(num, den, n, num_low=0, den_low=0):
    """Divide num/den as Laurent series. den[den_low] must be nonzero.
    Returns (coeffs, low) with coeffs[i] = coefficient of q^(low+i),
    exact Fractions (will be integers when division is exact)."""
    low = num_low - den_low
    d0 = den[den_low]
    out = []
    num_shift = num[num_low:]
    den_shift = den[den_low:]
    for i in range(n):
        acc = Fraction(num_shift[i]) if i < len(num_shift) else Fraction(0)
        for j in range(1, i + 1):
            if j < len(den_shift) and den_shift[j]:
                acc -= Fraction(den_shift[j]) * out[i - j]
        out.append(acc / d0)
    return out, low


def factorint(n):
    n = abs(n)
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def classify(n):
    if n == 0:
        return "zero"
    primes = set(factorint(n))
    if primes <= STRATA:
        return "strata-clean"
    if primes <= SUPERSINGULAR:
        return "supersingular"
    outside = sorted(primes - SUPERSINGULAR)
    return f"outside: {outside}"


# ----------------------------------------------------------------------
# Build the forms
# ----------------------------------------------------------------------

print("=" * 70)
print("INDEPENDENT VERIFICATION -- dim-6 kissing handoff (ClaudeCode)")
print("=" * 70)

# F = eta(tau)^6 eta(3tau)^6 = q * prod (1-q^n)^6 (1-q^3n)^6
prod1 = eta_power6(N_TRUNC, step=1)
prod3 = eta_power6(N_TRUNC, step=3)
prod = series_mul(prod1, prod3, N_TRUNC)
F = [0] * N_TRUNC
for i in range(N_TRUNC - 1):
    F[i + 1] = prod[i]          # multiply by q
a = {n: F[n] for n in range(1, N_TRUNC)}

checks = []

# C1 -- sanity
c1 = (a[1], a[2], a[3], a[4]) == (1, -6, 9, 4)
checks.append(("C1 q-expansion sanity a1,a2,a3,a4 = 1,-6,9,4", c1))
print(f"\nC1: a_1..a_4 = {a[1]}, {a[2]}, {a[3]}, {a[4]}  "
      f"{'OK' if c1 else 'FAIL'}")

# C2 -- multiplicativity
from math import gcd
c2 = True
pairs_checked = 0
for m in range(2, 101):
    for n in range(2, 101 // m + 1):
        if gcd(m, n) == 1 and m * n < N_TRUNC:
            if a[m * n] != a[m] * a[n]:
                c2 = False
                print(f"  C2 FAIL at (m,n)=({m},{n})")
            pairs_checked += 1
checks.append((f"C2 Hecke multiplicativity ({pairs_checked} coprime pairs)", c2))
print(f"C2: multiplicativity on {pairs_checked} coprime pairs  "
      f"{'OK' if c2 else 'FAIL'}")

# C3 -- prime-power recursion (NEW check, not in chat-session scripts)
c3 = True
for p in (2, 5, 7):
    lhs = a[p * p]
    rhs = a[p] ** 2 - p ** 5
    if lhs != rhs:
        c3 = False
    print(f"C3: a_{p}^2 - {p}^5 = {rhs}, a_{p*p} = {lhs}  "
          f"{'OK' if lhs == rhs else 'FAIL'}")
# ramified prime 3: a_9 = a_3^2
c3_ram = a[9] == a[3] ** 2
print(f"C3: ramified a_9 = {a[9]}, a_3^2 = {a[3]**2}  "
      f"{'OK' if c3_ram else 'FAIL'}")
c3 = c3 and c3_ram
checks.append(("C3 prime-power recursion a_p2 = a_p^2 - p^5 (+ ramified 3)", c3))

# C4 -- Ramanujan-Petersson
primes = [p for p in range(2, 98)
          if all(p % d for d in range(2, int(p ** 0.5) + 1))]
c4 = True
for p in primes:
    bound = 2 * p ** 2.5
    if abs(a[p]) > bound:
        c4 = False
        print(f"  C4 FAIL at p={p}: |a_p|={abs(a[p])} > {bound:.1f}")
checks.append((f"C4 Ramanujan-Petersson |a_p| <= 2p^2.5 for p <= 97", c4))
print(f"C4: Ramanujan-Petersson at {len(primes)} primes  "
      f"{'OK' if c4 else 'FAIL'}")

# C5 -- A-L eigenvalue via the newform relation (NEW check)
# For a newform of weight k, level N, p || N:  a_p = -eps_p p^(k/2 - 1).
# k=6, p=3: p^(k/2-1) = 9. a_3 = +9 ==> eps_3 = -1.
eps3 = -a[3] // 9
c5 = (a[3] == 9 and eps3 == -1)
checks.append(("C5 A-L via newform relation: a_3=+9 ==> eps_3=-1", c5))
print(f"C5: a_3 = {a[3]} ==> eps_3 = {eps3}  {'OK' if c5 else 'FAIL'}")

# C6 -- A-L eigenvalue via direct numerical functional equation.
# Convention note: (f|W_3)(tau) = 3^(-3) tau^(-6) f(-1/(3tau)) = eps*f(tau).
# At tau = it the factor (it)^(-6) = -t^(-6) flips sign, so
#   f(i/(3t)) = -eps * 27 t^6 f(it),
# i.e. the observable ratio f(i/(3t)) / [(sqrt3 t)^6 f(it)] equals -eps.
# For eps = -1 the expected ratio is +1.
mp.mp.dps = 30


def F_num(t):
    q = mp.exp(-2 * mp.pi * t)
    s = mp.mpf(0)
    for n in range(1, N_TRUNC):
        if a[n]:
            s += a[n] * q ** n
    return s


c6 = True
for t in (0.7, 0.9, 1.1, 1.3, 0.6, 1.0):
    lhs = F_num(1 / (3 * t))
    rhs = (mp.sqrt(3) * t) ** 6 * F_num(t)
    ratio = lhs / rhs            # = -eps; expect +1 for eps = -1
    ok = abs(ratio - 1) < mp.mpf("1e-15")
    if not ok:
        c6 = False
    print(f"C6: t={t}: ratio = {mp.nstr(ratio, 12)} (= -eps; +1 <=> eps=-1)  "
          f"{'OK' if ok else 'FAIL'}")
checks.append(("C6 A-L eps_3 = -1 via numerical functional equation", c6))

# C7 -- residue of psi_+ at infinity
E6_1 = E6_series(PSI_ORDER + 3, step=1)
E6_3 = E6_series(PSI_ORDER + 3, step=3)
num = [x - 729 * y for x, y in
       zip(series_mul(E6_1, E6_1, PSI_ORDER + 3),
           series_mul(E6_3, E6_3, PSI_ORDER + 3))]
c7 = num[0] == -728
res_fact = factorint(728)
checks.append(("C7 numerator constant term = -728 (residue of psi_+)", c7))
print(f"\nC7: [q^0](E6^2 - 729 E6(3.)^2) = {num[0]}  "
      f"(= -(2^3*7*13): {res_fact})  {'OK' if c7 else 'FAIL'}")

# C8 -- psi_+ Laurent expansion (exact division to PSI_ORDER)
den = F[:PSI_ORDER + 3]            # starts at q^1
psi, low = series_div(num, den, PSI_ORDER + 2, num_low=0, den_low=1)
# integrality check + factorization table
c8 = all(c.denominator == 1 for c in psi)
print(f"\nC8: psi_+ Laurent coefficients (q^{low} .. q^{low+len(psi)-1}), "
      f"all integers: {'OK' if c8 else 'FAIL'}")
print(f"     (first {PSI_REPORT+1} factored below; full table to "
      f"q^{low+len(psi)-1} in claudecode_independent.json)")
psi_table = {}
for i, c in enumerate(psi):
    k = low + i
    ci = int(c)
    psi_table[k] = ci
    if k <= PSI_REPORT:
        tag = classify(ci)
        print(f"     [q^{k:>2}] = {ci:>26}   {tag}")
checks.append(("C8 psi_+ Laurent exact + integral to q^%d" % (low + len(psi) - 1),
               c8))

# C9 -- psi_+ Fricke +1 functional equation numerically
def psi_num(t):
    q = mp.exp(-2 * mp.pi * t)
    s = mp.mpf(0)
    for i, c in enumerate(psi):
        k = low + i
        s += int(c) * q ** k
    return s


# Same convention: observable ratio = -eps. For psi_+ with eps = +1,
# expect ratio = -1. Test points kept near (but NOT at) the Fricke fixed
# point 1/sqrt(3) ~ 0.577 so BOTH arguments t and 1/(3t) stay in the
# fast-convergence zone of the 80-term Laurent series. (The fixed point
# itself is excluded: psi_+ vanishes there -- see C10 -- so the ratio
# test is 0/0-ill-conditioned at that point.)
c9 = True
for t in (0.62, 0.68, 0.75, 0.82, 0.90, 0.96):
    lhs = psi_num(1 / (3 * t))
    rhs = (mp.sqrt(3) * t) ** 6 * psi_num(t)
    ratio = lhs / rhs            # = -eps; expect -1 for eps = +1
    ok = abs(ratio + 1) < mp.mpf("1e-12")
    if not ok:
        c9 = False
    print(f"C9: t={t}: ratio = {mp.nstr(ratio, 15)} (= -eps; -1 <=> eps=+1)  "
          f"{'OK' if ok else 'FAIL'}")
checks.append(("C9 psi_+ Fricke eps = +1 functional equation (6 t-values)", c9))

# C10 -- FORCED ZERO of psi_+ at the Fricke fixed point tau = i/sqrt(3).
# For weight k = 6, the fixed-point slash factor is i^(-k) = -1, so a
# +1-eigenfunction must satisfy psi(i/sqrt3) = -psi(i/sqrt3) = 0.
# (eta^6 eta_3^6, with eps = -1, has NO forced zero there -- check both.)
t_star = 1 / mp.sqrt(3)
psi_at_fix = psi_num(t_star)
F_at_fix = F_num(t_star)
# scale-reference: psi at a nearby generic point
psi_ref = abs(psi_num(mp.mpf("0.75")))
c10 = abs(psi_at_fix) / psi_ref < mp.mpf("1e-12") and abs(F_at_fix) > 1e-6
print(f"\nC10: psi_+(i/sqrt3) = {mp.nstr(psi_at_fix, 6)}  "
      f"(|psi|/|psi(0.75i)| = {mp.nstr(abs(psi_at_fix)/psi_ref, 3)})")
print(f"C10: eta6eta3_6(i/sqrt3) = {mp.nstr(F_at_fix, 6)} (nonzero, eps=-1 "
      f"form has no forced zero)  {'OK' if c10 else 'FAIL'}")
checks.append(("C10 forced zero of psi_+ at Fricke fixed point i/sqrt(3)", c10))

# ----------------------------------------------------------------------
# Save artifacts
# ----------------------------------------------------------------------
out = {
    "form": "eta(tau)^6 * eta(3tau)^6, weight 6, level 3 (newform 3.6.a.a)",
    "a_n_first_40": {str(n): a[n] for n in range(1, 41)},
    "a_p_with_factorization": {
        str(p): {"a_p": a[p],
                 "factorization": factorint(a[p]) and
                 {str(k): v for k, v in factorint(a[p]).items()},
                 "class": classify(a[p])}
        for p in primes},
    "atkin_lehner_W3": -1,
    "psi_plus_laurent": {str(k): v for k, v in psi_table.items()},
    "psi_plus_residue_at_infinity": -728,
    "verified_by": "claudecode_independent_verify.py (exact integer arithmetic)",
}
os.makedirs(DATA, exist_ok=True)
with open(os.path.join(DATA, "claudecode_independent.json"), "w",
          encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)

print("\n" + "=" * 70)
n_pass = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  {'PASS' if ok else 'FAIL'}: {name}")
print(f"\n  Overall: {n_pass}/{len(checks)} "
      f"{'PASS' if n_pass == len(checks) else 'FAIL'}")
