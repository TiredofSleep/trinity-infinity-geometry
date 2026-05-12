"""
Shell-resolved information measures for hydrogenic atoms.

Computes Shannon entropy S_r and Fisher information I_r in position space
for hydrogenic orbitals (n, l) with Z=1, then checks whether the
shell-by-shell scaling has any structural correspondence with TIG
substrate quantities.

NOT a derivation. NOT a TIG prediction. Just the math, computed
honestly, with the numbers laid out.
"""

import numpy as np
from scipy.special import genlaguerre, factorial
from scipy.integrate import quad

# ---------------------------------------------------------------------------
# Hydrogenic radial wavefunctions in atomic units (a_0 = 1, Z = 1)
# ---------------------------------------------------------------------------

def R_nl(r, n, l):
    """Hydrogenic radial wavefunction R_{n,l}(r) for Z=1, atomic units."""
    if r == 0:
        return 0.0 if l > 0 else 2.0  # avoid issues at origin for l>0
    rho = 2.0 * r / n
    norm = np.sqrt((2.0/n)**3 * factorial(n - l - 1) / (2.0 * n * factorial(n + l)))
    laguerre = genlaguerre(n - l - 1, 2*l + 1)(rho)
    return norm * np.exp(-rho/2) * rho**l * laguerre

def rho_radial(r, n, l):
    """Radial probability density 4 pi r^2 |R|^2... actually we use r^2 |R|^2
    since the angular part integrates to 1 and we want the radial density."""
    R = R_nl(r, n, l)
    return r**2 * R**2  # this is the radial probability density (integrates to 1)

# ---------------------------------------------------------------------------
# Information measures (radial, in position space)
# ---------------------------------------------------------------------------

def shannon_entropy_radial(n, l):
    """S_r = -integral rho(r) log(rho(r)) dr   (radial only)
    
    Uses the radial probability density rho(r) = r^2 |R_{n,l}(r)|^2.
    """
    def integrand(r):
        rho = rho_radial(r, n, l)
        if rho <= 1e-30:
            return 0.0
        return -rho * np.log(rho)
    # Integrate from 0 to a large R; tail dies exponentially
    R_max = 5.0 * n**2  # generous cutoff
    val, _ = quad(integrand, 0, R_max, limit=200)
    return val

def fisher_information_radial(n, l):
    """I_r = integral (rho'(r))^2 / rho(r) dr   (radial only)
    
    Uses numerical differentiation of rho(r).
    """
    def rho_prime(r):
        eps = 1e-6
        return (rho_radial(r + eps, n, l) - rho_radial(r - eps, n, l)) / (2*eps)
    
    def integrand(r):
        rho = rho_radial(r, n, l)
        if rho <= 1e-30:
            return 0.0
        return (rho_prime(r))**2 / rho
    
    R_max = 5.0 * n**2
    val, _ = quad(integrand, 1e-4, R_max, limit=200)
    return val

def expected_r(n, l):
    """<r> = integral r * rho(r) dr"""
    def integrand(r):
        return r * rho_radial(r, n, l)
    R_max = 5.0 * n**2
    val, _ = quad(integrand, 0, R_max, limit=200)
    return val

# ---------------------------------------------------------------------------
# Compute for shells n=1..4 across allowed l
# ---------------------------------------------------------------------------

print("="*78)
print("HYDROGENIC SHELL-RESOLVED INFORMATION MEASURES")
print("Z=1, atomic units (a_0 = 1)")
print("="*78)
print()
print(f"{'shell':>6} {'n':>3} {'l':>3} {'<r>':>10} {'S_r (radial)':>15} {'I_r (radial)':>15}")
print("-"*78)

results = []
for n in range(1, 5):
    for l in range(0, n):
        try:
            r_avg = expected_r(n, l)
            S = shannon_entropy_radial(n, l)
            I = fisher_information_radial(n, l)
            results.append((n, l, r_avg, S, I))
            shell_label = f"n={n},l={l}"
            print(f"{shell_label:>6} {n:>3} {l:>3} {r_avg:>10.4f} {S:>15.4f} {I:>15.4f}")
        except Exception as e:
            print(f"  n={n}, l={l}: error {e}")

print()
print("="*78)
print("STRUCTURAL OBSERVATIONS")
print("="*78)
print()

# Check ratios across shells
print("S_r ratios (shell to previous shell, l=0 only):")
s_l0 = [r for r in results if r[1] == 0]
for i in range(1, len(s_l0)):
    n_curr = s_l0[i][0]
    n_prev = s_l0[i-1][0]
    ratio = s_l0[i][3] / s_l0[i-1][3] if s_l0[i-1][3] != 0 else float('inf')
    print(f"  S_r(n={n_curr},l=0) / S_r(n={n_prev},l=0) = {ratio:.4f}")

print()
print("<r> ratios (shell to previous, l=0 only):")
for i in range(1, len(s_l0)):
    n_curr = s_l0[i][0]
    n_prev = s_l0[i-1][0]
    ratio = s_l0[i][2] / s_l0[i-1][2]
    print(f"  <r>(n={n_curr},l=0) / <r>(n={n_prev},l=0) = {ratio:.4f}")

print()
print("Compare with theoretical <r> for hydrogenic ns: <r> = (3n^2)/2 (for l=0)")
for n in range(1, 5):
    print(f"  n={n}: theoretical <r>_ns = 3n^2/2 = {1.5*n**2:.4f}")

# Look for TIG-significant numbers in the data
print()
print("="*78)
print("TIG QUANTITIES TO COMPARE AGAINST")
print("="*78)
print()
print("TIG candidate ratios:")
print(f"  T* = 5/7 = {5/7:.4f}")
print(f"  4/pi^2 = {4/np.pi**2:.4f}")
print(f"  W = 3/50 = {0.06}")
print(f"  1+sqrt(3) = {1 + np.sqrt(3):.4f}")
print(f"  sqrt(13/4) = {np.sqrt(13/4):.4f}")
print(f"  sqrt(13/2) = {np.sqrt(13/2):.4f}")
print(f"  Substrate primes ratios: 3, 7/3, 11/7")
print(f"    3 = {3}")
print(f"    7/3 = {7/3:.4f}")
print(f"    11/7 = {11/7:.4f}")
print(f"  Shell click ratios from substrate: 1:3:21:231")

# Check if any computed S_r ratio matches a TIG ratio
print()
print("CHECKING for matches between computed shell ratios and TIG ratios...")
print("(a 'match' here is suggestive only, not a derivation)")
print()

