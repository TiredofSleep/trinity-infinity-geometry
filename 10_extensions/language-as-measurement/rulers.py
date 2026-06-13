"""rulers.py -- the two measurement primitives, computed honestly.

The thesis (Brayden, 2026-06-13): there is no single correct way to measure
information. Any *consistent* measurement system that adds a layer of unique,
valuable information about the thing studied is valid. We start from two dual
rulers that the envelope methodology gives us, and we read the DEFECT, not the
summary -- the defect is where the information lives.

  RULER A -- a CIRCLE measured by SQUARES (discrete quadrature / box-counting).
    Tile a curved region with a square grid. The fully-inside squares give a
    lower-bound area; the boundary squares are the DEFECT. The defect count does
    NOT vanish -- rescaled it converges to the PERIMETER. Curvature lives in the
    boundary, not the interior.

  RULER B -- a LINE measured by a PARABOLIC ENVELOPE (track-the-defect).
    A linear summary y = x is surrounded by an envelope y = x +/- k*sqrt(x).
    The residual (data - line) is the DEFECT; its size and growth EXPONENT are
    the information. Demonstrated on the Chebyshev staircase psi(x): the residual
    psi(x) - x stays inside a sqrt(x) envelope (the empirical content of RH).

These are duals: circle<->line, area<->length, 2D square-grid<->1D envelope.
Together they are a starter basis for "measuring information." No claim of proof
here -- Ruler B illustrates a conjecture (RH effective form) empirically.

  python rulers.py
"""
import math


# ----------------------------------------------------------------------------
# RULER A -- a circle measured by squares
# ----------------------------------------------------------------------------
def circle_by_squares(r=1.0, sides=(4, 8, 16, 32, 64, 128, 256)):
    """Tile [-r,r]^2 with `n x n` squares; classify each by its 4 corners.
    Returns (true_area, rows) where each row is a dict of the measurement."""
    true_area = math.pi * r * r
    rows = []
    for n in sides:
        h = (2 * r) / n
        inside = boundary = 0
        for i in range(n):
            x0 = -r + i * h
            for j in range(n):
                y0 = -r + j * h
                c = [(x0 * x0 + y0 * y0 <= r * r),
                     ((x0 + h) ** 2 + y0 * y0 <= r * r),
                     (x0 * x0 + (y0 + h) ** 2 <= r * r),
                     ((x0 + h) ** 2 + (y0 + h) ** 2 <= r * r)]
                if all(c):
                    inside += 1
                elif any(c):
                    boundary += 1
        lower = inside * h * h                 # fully-inside area (lower bound)
        upper = (inside + boundary) * h * h    # +boundary (upper bound)
        rows.append(dict(n=n, h=h, inside=inside, boundary=boundary,
                         area_lo=lower, area_hi=upper,
                         bracket=upper - lower,        # -> 0     (area RESOLVES)
                         taxicab_len=boundary * h))    # -> 8r    (NOT 2*pi*r !)
    return true_area, rows


# ----------------------------------------------------------------------------
# RULER B -- a line measured by a parabolic envelope (Chebyshev staircase)
# ----------------------------------------------------------------------------
def chebyshev_residual(N=100_000):
    """psi(x) = sum_{p^k <= x} log p. Returns the residual psi(x)-x sampled,
    the empirical envelope constant c = max |psi(x)-x| / sqrt(x), and the
    growth exponent of the running max (slope of log-max vs log-x ~ 0.5)."""
    sieve = bytearray([1]) * (N + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, N + 1, i)))
    dpsi = [0.0] * (N + 1)
    for p in range(2, N + 1):
        if sieve[p]:
            lp, pk = math.log(p), p
            while pk <= N:
                dpsi[pk] += lp
                pk *= p
    psi = 0.0
    xs, res = [], []
    c_env = 0.0
    run_max = 0.0
    growth = []                     # (log x, log running-max|residual|)
    step = max(1, N // 1200)        # sample ~1200 points for the figure
    for x in range(1, N + 1):
        psi += dpsi[x]
        d = psi - x
        ad = abs(d)
        if x >= 100:
            c_env = max(c_env, ad / math.sqrt(x))
            if ad > run_max:
                run_max = ad
                growth.append((math.log(x), math.log(run_max)))
        if x % step == 0:
            xs.append(x); res.append(d)
    # slope of log running-max vs log x (least squares) -> empirical exponent
    n = len(growth)
    sx = sum(a for a, _ in growth); sy = sum(b for _, b in growth)
    sxx = sum(a * a for a, _ in growth); sxy = sum(a * b for a, b in growth)
    alpha = (n * sxy - sx * sy) / (n * sxx - sx * sx) if n > 1 else float("nan")
    within = sum(1 for x, d in zip(xs, res)
                 if x >= 100 and abs(d) <= 3 * math.sqrt(x))
    total = sum(1 for x in xs if x >= 100)
    return dict(N=N, xs=xs, res=res, c_env=c_env, alpha=alpha,
                frac_within_3sqrt=within / total if total else float("nan"))


if __name__ == "__main__":
    print("=" * 68)
    print("RULER A -- a circle measured by squares  (r = 1, true area = pi)")
    print("=" * 68)
    ta, rows = circle_by_squares()
    print(f"{'n':>5} {'inside':>8} {'boundary':>9} {'area_lo':>9} "
          f"{'area_hi':>9} {'bracket':>9} {'taxicab':>10}")
    for r in rows:
        print(f"{r['n']:>5} {r['inside']:>8} {r['boundary']:>9} "
              f"{r['area_lo']:>9.4f} {r['area_hi']:>9.4f} {r['bracket']:>9.4f} "
              f"{r['taxicab_len']:>10.4f}")
    print(f"true area = {ta:.6f}   Euclidean perim = {2*math.pi:.6f}   "
          f"taxicab perim (8r) = {8.0:.6f}")
    print("READ: squares resolve the AREA exactly (bracket -> 0, area_lo -> pi).")
    print("      But the same squares measure the boundary as TAXICAB length")
    print("      (-> 8r = 8.0), never the Euclidean 2*pi*r -- and refining the")
    print("      grid does NOT fix it (the staircase paradox, 'why pi != 4').")
    print("      LESSON: the ruler decides which invariant you can read. Curvature")
    print("      is invisible to squares; to see it you must switch rulers.")

    print("\n" + "=" * 68)
    print("RULER B -- a line measured by a parabolic envelope (Chebyshev psi)")
    print("=" * 68)
    out = chebyshev_residual()
    print(f"  N = {out['N']}")
    print(f"  empirical envelope constant  c = max|psi(x)-x|/sqrt(x) = "
          f"{out['c_env']:.4f}   (x >= 100)")
    print(f"  fraction of samples inside  +/- 3*sqrt(x)            = "
          f"{out['frac_within_3sqrt']:.4f}")
    print(f"  growth exponent of running max |residual| (log-log slope) = "
          f"{out['alpha']:.4f}   (RH predicts ~0.5)")
    print("READ: the staircase's defect off the line stays in a sqrt(x) envelope.")
    print("      The EXPONENT is the information -- it names the mechanism class.")
