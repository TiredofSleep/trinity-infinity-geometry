"""
Task 5 — alpha-sweep for privileged values.

The bhml addendum found that at alpha = 1/2, the T+B-mix runtime
attractor satisfies:
  HARMONY/BREATH = 1 + sqrt(3)        exact (degree 2)
  r/br satisfies x^4 + 4x^3 - x^2 + 2x - 2 = 0   exact (degree 4)

Question: are there OTHER alpha values where the attractor has clean
algebraic structure?

Sweep alpha in [0.05, 0.95], compute the runtime attractor numerically
to high precision, then for each:
  1. extract H, V, Br, R from the attractor
  2. compute the candidate ratio H/Br and check for low-degree algebraic
     numbers (LLL/PSLQ-style brute integer relation finding)
  3. flag any alpha where the relation is "clean" (small integer
     coefficients, or square root of a small rational)
"""
from __future__ import annotations

import numpy as np

# canonical TSML / BHML
TSML_ROWS = [
    "0000000700",  "0737777777",  "0377477779",  "0777777773",  "0747777787",
    "0777777777",  "0777777777",  "7777777777",  "0777877777",  "0797377777",
]
BHML_ROWS = [
    "0123456789",  "1234567266",  "2334567366",  "3444567466",  "4555567577",
    "5666667677",  "6777777777",  "7234567890",  "8666777978",  "9666777080",
]
T = np.array([[int(c) for c in row] for row in TSML_ROWS], dtype=int)
B = np.array([[int(c) for c in row] for row in BHML_ROWS], dtype=int)


def fuse(p, q, table):
    r = np.zeros(10)
    for a in range(10):
        for b in range(10):
            r[int(table[a, b])] += p[a] * q[b]
    return r


def normalize_l1(v, eps=1e-15):
    s = v.sum()
    return v / s if s > eps else v


def attractor(alpha, max_iter=2000, tol=1e-14):
    """Iterate the T+B mix from a fixed starting distribution (uniform over
    the 4-core {V=0, H=7, Br=8, R=9}) until convergence.
    """
    p = np.zeros(10)
    p[0] = 0.25
    p[7] = 0.25
    p[8] = 0.25
    p[9] = 0.25
    for k in range(max_iter):
        p_t = normalize_l1(fuse(p, p, T))
        p_b = normalize_l1(fuse(p, p, B))
        p_new = normalize_l1(alpha * p_t + (1 - alpha) * p_b)
        if np.max(np.abs(p_new - p)) < tol:
            return p_new, k
        p = p_new
    return p, max_iter


def find_quadratic_relation(x, max_coeff=10, tol=1e-9):
    """Brute search for integers a, b, c with a*x^2 + b*x + c = 0,
    |a|,|b|,|c| <= max_coeff. Return (a,b,c, residual) or None.
    """
    best = None
    for a in range(-max_coeff, max_coeff + 1):
        if a == 0:
            continue
        for b in range(-max_coeff, max_coeff + 1):
            for c in range(-max_coeff, max_coeff + 1):
                resid = a * x * x + b * x + c
                if abs(resid) < tol:
                    if best is None or abs(resid) < best[3]:
                        best = (a, b, c, abs(resid))
    return best


def find_quartic_relation(x, max_coeff=8, tol=1e-9):
    """Brute search for integers a4..a0 with min poly relation,
    |coeff| <= max_coeff. Returns (a4,a3,a2,a1,a0, residual) or None.
    Slow: O(max_coeff^5) so use small max_coeff.
    """
    best = None
    for a4 in range(1, max_coeff + 1):
        for a3 in range(-max_coeff, max_coeff + 1):
            for a2 in range(-max_coeff, max_coeff + 1):
                for a1 in range(-max_coeff, max_coeff + 1):
                    for a0 in range(-max_coeff, max_coeff + 1):
                        resid = a4 * x**4 + a3 * x**3 + a2 * x**2 + a1 * x + a0
                        if abs(resid) < tol:
                            if best is None or abs(resid) < best[5]:
                                best = (a4, a3, a2, a1, a0, abs(resid))
    return best


def main():
    alphas = np.linspace(0.05, 0.95, 19)
    print("=" * 90)
    print("TASK 5 -- alpha-sweep for privileged attractor values")
    print("=" * 90)
    print()
    print(f"{'alpha':<8} {'iters':<8} {'V':<10} {'H':<10} {'Br':<10} {'R':<10} {'H/Br':<12}  {'note'}")
    print("-" * 100)
    rows = []
    for alpha in alphas:
        attr, iters = attractor(alpha)
        V = float(attr[0])
        H = float(attr[7])
        Br = float(attr[8])
        R = float(attr[9])
        ratio = H / Br if Br > 1e-12 else float("inf")

        # check whether H/Br satisfies a small-integer quadratic
        relq = find_quadratic_relation(ratio, max_coeff=10, tol=1e-9) if Br > 1e-12 else None
        note = ""
        if relq is not None:
            a, b, c, resid = relq
            # display the relation
            note = f"H/Br: {a}*x^2 + {b}*x + {c} = 0 (resid {resid:.1e})"

        print(f"{alpha:<8.3f} {iters:<8} {V:<10.6f} {H:<10.6f} {Br:<10.6f} {R:<10.6f} {ratio:<12.6f}  {note}")
        rows.append((alpha, V, H, Br, R, ratio, note))

    print()
    print("=" * 90)
    print("CLEAN-ALGEBRAIC-RELATION HIGHLIGHTS")
    print("=" * 90)
    print()

    # Highlight any alpha at a rational with small denominator that gave a
    # clean quadratic relation; also find ALPHAS where the relation has
    # particularly small coefficients (proxy for clean algebraic structure).
    for alpha, V, H, Br, R, ratio, note in rows:
        if note:
            print(f"  alpha = {alpha:.3f}: {note}")
            # also test r/br against a quartic
            if Br > 1e-9:
                rbr = R / Br
                rel4 = find_quartic_relation(rbr, max_coeff=5, tol=1e-9)
                if rel4 is not None:
                    a4, a3, a2, a1, a0, resid = rel4
                    print(f"    r/br = {rbr:.10f} satisfies "
                          f"{a4}x^4 + {a3}x^3 + {a2}x^2 + {a1}x + {a0} = 0 (resid {resid:.1e})")


if __name__ == "__main__":
    main()
