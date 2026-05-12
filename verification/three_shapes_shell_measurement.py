"""
Proper intrinsic arc length: integrate ONLY over the bump, where rho_norm > threshold.
Subtract the flat-line contribution to isolate the shape's actual arc.

Three corrected shape measures:
1. EDGE SIZE (1/I_r) — outer boundary
2. BUMP ARC — arc length of (u, rho_norm) restricted to rho_norm > 0.01,
              MINUS the straight u-distance traversed (so flat regions don't contribute)
3. SIGMA-RATE ANALOG — tunneling fraction beyond classical turning point
"""

import numpy as np
from scipy.special import genlaguerre, factorial
from scipy.integrate import quad
from scipy.optimize import brentq

def R_nl(r, n, l):
    if r == 0:
        return 0.0 if l > 0 else 2.0
    rho_arg = 2.0 * r / n
    norm = np.sqrt((2.0/n)**3 * factorial(n - l - 1) / (2.0 * n * factorial(n + l)))
    laguerre = genlaguerre(n - l - 1, 2*l + 1)(rho_arg)
    return norm * np.exp(-rho_arg/2) * rho_arg**l * laguerre

def density(r, n, l):
    return r**2 * R_nl(r, n, l)**2

def density_prime(r, n, l, eps=1e-6):
    return (density(r + eps, n, l) - density(r - eps, n, l)) / (2*eps)

def expected_r(n, l):
    R_max = 5.0 * n**2
    val, _ = quad(lambda r: r * density(r, n, l), 0, R_max, limit=300)
    return val

def max_density(n, l):
    R_max = 5.0 * n**2
    rs = np.linspace(0.01, R_max, 10000)
    return max(density(r, n, l) for r in rs)

def bump_arc(n, l, threshold=0.01):
    """
    Arc length of (u, rho_norm) curve, where u = r/<r>, rho_norm = rho/rho_max,
    restricted to where rho_norm >= threshold.
    
    Then SUBTRACT the (u_right - u_left) flat baseline so we isolate
    the bump's intrinsic arc length above its endpoints.
    
    A pure delta gives result -> 2 (up by 1, down by 1).
    A wide bump gives result > 2.
    """
    avg_r = expected_r(n, l)
    rho_max = max_density(n, l)
    
    def rho_norm(u):
        return density(u * avg_r, n, l) / rho_max
    
    # Find u_left and u_right where rho_norm crosses threshold
    R_max_u = 5.0 * n**2 / avg_r
    us = np.linspace(0.001, R_max_u, 20000)
    rho_vals = np.array([rho_norm(u) for u in us])
    above = rho_vals > threshold
    if not above.any():
        return None
    u_left = us[above].min()
    u_right = us[above].max()
    
    def integrand(u):
        r = u * avg_r
        deriv_u = avg_r * density_prime(r, n, l) / rho_max
        return np.sqrt(1.0 + deriv_u**2)
    
    arc_inside, _ = quad(integrand, u_left, u_right, limit=300)
    flat_baseline = u_right - u_left
    return arc_inside - flat_baseline

def edge_size(n, l):
    def integrand(r):
        rho = density(r, n, l)
        if rho <= 1e-30:
            return 0.0
        return density_prime(r, n, l)**2 / rho
    R_max = 5.0 * n**2
    I_r, _ = quad(integrand, 1e-4, R_max, limit=200)
    return 1.0 / I_r if I_r > 0 else float('inf')

def tunneling_fraction(n, l):
    if l*(l+1) > n**2:
        r_plus = n**2
    else:
        r_plus = n**2 + n * np.sqrt(n**2 - l*(l+1))
    R_max = 10.0 * n**2
    P_outside, _ = quad(lambda r: density(r, n, l), r_plus, R_max, limit=200)
    return P_outside

# ===========================================================================
# Compute three shapes for shells n=1..7
# ===========================================================================

print("="*84)
print("THREE SHAPES — corrected (bump arc only, no flat-region pollution)")
print("="*84)
print(f"{'shell':>5} {'<r>':>8} {'edge=1/I':>10} {'bump_arc':>10} {'tunnel':>10}")
print("-"*84)

results = []
letters = 'spdfghiklmn'
for n in range(1, 8):
    for l in range(0, n):
        try:
            es = edge_size(n, l)
            ba = bump_arc(n, l)
            tf = tunneling_fraction(n, l)
            ar = expected_r(n, l)
            label = f"{n}{letters[l]}"
            results.append({'n':n, 'l':l, 'avg_r':ar, 'edge':es, 'arc':ba, 'tunnel':tf, 'label':label})
            ba_s = f"{ba:.4f}" if ba is not None else "  --  "
            print(f"{label:>5} {ar:>8.2f} {es:>10.4f} {ba_s:>10} {tf:>10.5f}")
        except Exception as e:
            print(f"  Error n={n} l={l}: {e}")

# === Nodeless shells ===
print("\n" + "="*84)
print("NODELESS (max-l, no internal nodes) — most basic gate shape")
print("="*84)
nodeless = [r for r in results if r['l'] == r['n']-1]
print(f"{'shell':>5} {'edge_size':>11} {'bump_arc':>10} {'tunnel':>10}")
for r in nodeless:
    print(f"{r['label']:>5} {r['edge']:>11.4f} {r['arc']:>10.4f} {r['tunnel']:>10.5f}")

# === Wiggle factor revisited ===
print("\n" + "="*84)
print("WIGGLE: bump_arc(n,l) - bump_arc(n, l_max=n-1) — extra arc per node")
print("="*84)
for n in range(1, 8):
    n_data = [r for r in results if r['n'] == n]
    if not n_data: continue
    nodeless_arc = [r for r in n_data if r['l'] == n-1][0]['arc']
    print(f"\nShell n={n}, nodeless bump_arc = {nodeless_arc:.4f}")
    for r in n_data:
        n_nodes = n - r['l'] - 1
        excess = r['arc'] - nodeless_arc
        per_node = excess / n_nodes if n_nodes > 0 else 0
        print(f"  l={r['l']} ({n_nodes} nodes): arc={r['arc']:.4f}, excess/node = {per_node:.4f}")

# === Sigma-rate analog: tunneling vs n ===
print("\n" + "="*84)
print("SIGMA-RATE: tunneling decay with shell index (s-orbitals)")
print("="*84)
ns = [r for r in results if r['l'] == 0]
print(f"\n{'n':>3} {'tunnel':>9} {'tunnel*n':>10} {'tunnel*n^(1/2)':>16} {'2/n':>8}")
for r in ns:
    n = r['n']
    print(f"{n:>3} {r['tunnel']:>9.5f} {r['tunnel']*n:>10.5f} {r['tunnel']*np.sqrt(n):>16.5f} {2/n:>8.4f}")

# Try fitting tunnel = C / n^alpha
xs = np.log([r['n'] for r in ns])
ys = np.log([r['tunnel'] for r in ns])
slope, intercept = np.polyfit(xs, ys, 1)
print(f"\nFit log(tunnel) = {slope:.4f} log(n) + {intercept:.4f}")
print(f"=> tunnel ~ {np.exp(intercept):.4f} * n^({slope:.4f})")
print(f"   For comparison: 2/n means slope = -1")
print(f"   Observed slope ~ {slope:.3f}, NOT -1")

