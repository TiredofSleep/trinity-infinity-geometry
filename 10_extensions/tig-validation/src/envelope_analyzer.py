"""
envelope_analyzer.py — generic tool for the three-question discipline.

============================================================================
WHAT THIS TOOL DOES
============================================================================

Given (x, y) data, this module:

  1. Fits a line  y ~ a + b*x  (or log-log version: log y ~ a + b*log x)
  2. Computes residuals  r(x) = y - (a + b*x)
  3. Tests candidate envelope shapes against |r(x)|:
       - constant:     |r| ~ k
       - logarithmic:  |r| ~ k * log(x)
       - square-root:  |r| ~ k * sqrt(x)
       - linear:       |r| ~ k * x
       - power-law:    |r| ~ k * x^alpha  (alpha estimated)
  4. Reports the best-fit envelope and the three-question diagnostic.

============================================================================
WHY THIS EXISTS
============================================================================

The framework's discipline says: when you see a line in data, characterize
the envelope of the residual, do not celebrate the line.

This tool makes that discipline automatable. Hand it any (x, y) dataset and
it returns:
  - the best line fit
  - the best envelope shape (with goodness of fit)
  - explicit caveats about what the answer does and does not establish

============================================================================
WHAT IT DOES NOT DO
============================================================================

It does NOT determine the underlying mechanism. It tells you, e.g., that
the residual envelope is approximately sqrt(x); the question of WHY is
domain-specific (CLT, RH, fluctuation-dissipation, multifractal turbulence,
or something else). The tool helps you ask the right next question.

It also does not adjudicate between candidate envelope shapes that are all
within statistical-noise distance of one another. With finite, noisy data,
parabolic and slightly-super-parabolic envelopes can be hard to distinguish.
The tool reports relative goodness-of-fit; users should not over-interpret
small differences.
"""

import math
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np


# ----------------------------------------------------------------------------
# Linear fit on (possibly log-transformed) data
# ----------------------------------------------------------------------------

@dataclass
class LineFit:
    intercept: float       # 'a' in y = a + b*x
    slope: float           # 'b'
    coords: str            # "linear" or "log-log"
    r_squared: float       # coefficient of determination

    def predict(self, x: np.ndarray) -> np.ndarray:
        if self.coords == "linear":
            return self.intercept + self.slope * x
        else:  # log-log
            return np.exp(self.intercept) * (x ** self.slope)


def fit_line(x: np.ndarray, y: np.ndarray, coords: str = "linear") -> LineFit:
    """Fit y ~ a + b*x (linear) or log y ~ a + b*log x (log-log).
    Both axes must be positive for log-log."""
    if coords == "log-log":
        mask = (x > 0) & (y > 0)
        if not mask.all():
            raise ValueError("log-log fit requires strictly positive x and y")
        X = np.log(x)
        Y = np.log(y)
    elif coords == "linear":
        X, Y = x, y
    else:
        raise ValueError(f"coords must be 'linear' or 'log-log', got {coords!r}")

    b, a = np.polyfit(X, Y, deg=1)
    Y_pred = a + b * X
    ss_res = float(np.sum((Y - Y_pred) ** 2))
    ss_tot = float(np.sum((Y - Y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return LineFit(intercept=float(a), slope=float(b), coords=coords, r_squared=r2)


# ----------------------------------------------------------------------------
# Envelope hypotheses
# ----------------------------------------------------------------------------
#
# Each hypothesis is a function f(x) such that  |r(x)| ~ k * f(x).
# To fit k, we bin x, compute the local max |r| in each bin, and fit
# (log f(x_bin), log max|r(x_bin)|) by linear regression. The slope of
# that regression should be 1 if the hypothesis fits; the goodness-of-fit
# is the R^2 of the regression.

@dataclass
class EnvelopeFit:
    name: str
    k: float
    quality: float    # R^2 of log-log envelope fit; 1.0 = perfect, 0.0 = useless
    slope: float      # log-log slope of envelope fit; should be 1.0 if hypothesis fits

    @property
    def slope_deviation(self) -> float:
        """How far the empirical slope is from the expected slope of 1."""
        return abs(self.slope - 1.0)


def _bin_envelope_stat(x: np.ndarray, r: np.ndarray,
                       n_bins: int = 20,
                       percentile: float = 90.0) -> Tuple[np.ndarray, np.ndarray]:
    """Bin x into n_bins quantile-based bins, return (bin_centers,
    percentile_of_|r|_in_bin).

    Uses a percentile (default 90th) of |r| per bin rather than the max,
    because bin-max is dominated by individual extreme values and has
    high variance for single-realization stochastic processes. The 90th
    percentile captures the envelope robustly while staying defined for
    heavy-tailed processes (where variance may be infinite).
    """
    mask = x > 0
    x_pos = x[mask]
    r_pos = r[mask]
    if len(x_pos) < n_bins:
        n_bins = max(2, len(x_pos) // 2)
    quantiles = np.linspace(0, 1, n_bins + 1)
    edges = np.quantile(x_pos, quantiles)
    edges = np.unique(edges)
    n_bins_eff = len(edges) - 1
    centers = []
    stats = []
    for i in range(n_bins_eff):
        lo, hi = edges[i], edges[i + 1]
        if i < n_bins_eff - 1:
            in_bin = (x_pos >= lo) & (x_pos < hi)
        else:
            in_bin = (x_pos >= lo) & (x_pos <= hi)
        if in_bin.sum() == 0:
            continue
        centers.append(float(np.median(x_pos[in_bin])))
        stats.append(float(np.percentile(np.abs(r_pos[in_bin]), percentile)))
    return np.array(centers), np.array(stats)


# Backward-compatibility alias (the function used to be called _bin_max_residual
# and was used by internal callers below).
def _bin_max_residual(x: np.ndarray, r: np.ndarray,
                      n_bins: int = 20) -> Tuple[np.ndarray, np.ndarray]:
    """Deprecated alias. Use _bin_envelope_stat directly."""
    return _bin_envelope_stat(x, r, n_bins=n_bins, percentile=90.0)


def _fit_envelope(name: str,
                  f: Callable[[np.ndarray], np.ndarray],
                  bin_centers: np.ndarray,
                  bin_maxes: np.ndarray) -> EnvelopeFit:
    """Fit |r| ~ k * f(x). Use log-log linear regression of |r| against f(x).
    Returns the constant k, the goodness of fit (R^2), and the slope (which
    should be 1.0 if the hypothesis fits).

    Special case: when f(x) is constant (the 'constant' hypothesis itself),
    log f has zero variance and free regression is ill-posed. In that case,
    we report k as the geometric mean of |r|, slope as 0, and quality as 0
    (the constant hypothesis explains none of the variance in |r| by
    construction; it's the baseline against which other shapes are compared)."""
    fx = f(bin_centers)
    mask = (fx > 0) & (bin_maxes > 0)
    if mask.sum() < 3:
        return EnvelopeFit(name=name, k=float("nan"), quality=float("nan"),
                          slope=float("nan"))
    log_fx = np.log(fx[mask])
    log_r = np.log(bin_maxes[mask])

    # Constant hypothesis: log f has no variance, free regression degenerate.
    if float(np.var(log_fx)) < 1e-12:
        k = float(math.exp(np.mean(log_r)))
        return EnvelopeFit(name=name, k=k, quality=0.0, slope=0.0)

    slope, intercept = np.polyfit(log_fx, log_r, deg=1)
    k = math.exp(intercept)
    log_r_pred = intercept + slope * log_fx
    ss_res = float(np.sum((log_r - log_r_pred) ** 2))
    ss_tot = float(np.sum((log_r - log_r.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return EnvelopeFit(name=name, k=float(k), quality=float(r2),
                      slope=float(slope))


# The canonical envelope hypotheses
ENVELOPE_HYPOTHESES: Dict[str, Callable[[np.ndarray], np.ndarray]] = {
    "constant":         lambda x: np.ones_like(x, dtype=float),
    "logarithmic":      lambda x: np.log(np.maximum(x, math.e)),  # avoid log(1)=0
    "square-root":      lambda x: np.sqrt(np.maximum(x, 0.0)),
    "linear":           lambda x: x.astype(float),
}


# ----------------------------------------------------------------------------
# Power-law envelope: |r| ~ k * x^alpha with alpha estimated freely
# ----------------------------------------------------------------------------

@dataclass
class PowerLawFit:
    k: float
    alpha: float
    quality: float  # R^2 of log-log fit

    @property
    def name(self) -> str:
        return f"power-law (alpha = {self.alpha:.3f})"


def fit_power_law_envelope(x: np.ndarray, r: np.ndarray,
                           n_bins: int = 20) -> PowerLawFit:
    """Fit |r| ~ k * x^alpha by log-log regression of bin-max |r| vs x."""
    centers, maxes = _bin_max_residual(x, r, n_bins=n_bins)
    mask = (centers > 0) & (maxes > 0)
    X = np.log(centers[mask])
    Y = np.log(maxes[mask])
    alpha, log_k = np.polyfit(X, Y, deg=1)
    Y_pred = log_k + alpha * X
    ss_res = float(np.sum((Y - Y_pred) ** 2))
    ss_tot = float(np.sum((Y - Y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return PowerLawFit(k=float(math.exp(log_k)), alpha=float(alpha),
                      quality=float(r2))


# ----------------------------------------------------------------------------
# Full analysis
# ----------------------------------------------------------------------------

@dataclass
class EnvelopeAnalysis:
    line_fit: LineFit
    envelope_fits: List[EnvelopeFit]
    power_law: PowerLawFit
    best_envelope: str  # the name of the best-fitting hypothesis from ENVELOPE_HYPOTHESES
    n_data: int


def analyze(x: np.ndarray, y: np.ndarray,
            coords: str = "linear",
            n_bins: int = 20,
            skip_line_fit: bool = False) -> EnvelopeAnalysis:
    """Run the full three-question analysis on (x, y) data.

    Returns an EnvelopeAnalysis with:
      - line_fit:       the best line in the chosen coordinates
      - envelope_fits:  fits of the 4 canonical envelope hypotheses
      - power_law:      free power-law fit (estimates alpha)
      - best_envelope:  which canonical hypothesis fits best (by slope_deviation)

    If skip_line_fit=True, treats y as already a residual (e.g., random walk
    values around mean 0, or psi(x) - x for the prime staircase). Useful when
    the trend has been removed by domain knowledge rather than by fitting.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if skip_line_fit:
        # treat y as residual directly; record a 'null' line fit for the report
        lf = LineFit(intercept=0.0, slope=0.0, coords="(skipped)", r_squared=float("nan"))
        r = y
    else:
        lf = fit_line(x, y, coords=coords)
        r = y - lf.predict(x)
    centers, maxes = _bin_max_residual(x, r, n_bins=n_bins)

    fits = [
        _fit_envelope(name, f, centers, maxes)
        for name, f in ENVELOPE_HYPOTHESES.items()
    ]

    # Best envelope: smallest deviation of regression slope from 1.0
    # (the "well-behaved" hypothesis is the one whose chosen functional form
    #  already absorbs the right x-dependence, so the residual regression
    #  slope comes out near 1).
    valid_fits = [f for f in fits if not math.isnan(f.slope)]
    best = min(valid_fits, key=lambda f: f.slope_deviation) if valid_fits else None
    best_name = best.name if best else "no fit"

    pl = fit_power_law_envelope(x, r, n_bins=n_bins)
    return EnvelopeAnalysis(
        line_fit=lf, envelope_fits=fits, power_law=pl,
        best_envelope=best_name, n_data=len(x),
    )


def report(a: EnvelopeAnalysis, header: str = "Envelope analysis") -> str:
    """Format an EnvelopeAnalysis as a readable diagnostic."""
    lines = []
    lines.append("=" * 72)
    lines.append(header)
    lines.append("=" * 72)
    lines.append("")
    lines.append(f"Data:               {a.n_data} points")
    lines.append(f"Line fit ({a.line_fit.coords}):")
    lines.append(f"   intercept  =  {a.line_fit.intercept:+.6f}")
    lines.append(f"   slope      =  {a.line_fit.slope:+.6f}")
    lines.append(f"   R^2        =  {a.line_fit.r_squared:.6f}")
    lines.append("")
    lines.append("Envelope hypothesis fits (binned log-log regression of |r| vs envelope shape):")
    lines.append(f"   {'hypothesis':<14}  {'k':>10}  {'slope':>8}  {'|slope-1|':>10}  {'R^2':>8}")
    for f in a.envelope_fits:
        lines.append(f"   {f.name:<14}  {f.k:>10.4f}  {f.slope:>8.4f}  "
                     f"{f.slope_deviation:>10.4f}  {f.quality:>8.4f}")
    lines.append("")
    lines.append(f"Free power-law fit: |r(x)| ~ {a.power_law.k:.4f} * x^{a.power_law.alpha:.4f}")
    lines.append(f"   R^2        =  {a.power_law.quality:.6f}")
    lines.append("")
    lines.append(f"Best canonical envelope: {a.best_envelope}")
    lines.append("   (smallest deviation between regression slope and 1.0)")
    lines.append("")
    lines.append("Diagnostic (three-question discipline):")
    lines.append("   1. WHERE DOES THE LINE BREAK?")
    lines.append("      Inspect the residual plot for systematic deviations.")
    lines.append(f"      Line fit R^2 = {a.line_fit.r_squared:.4f}; high R^2 alone is")
    lines.append("      not sufficient -- structured residuals can hide in a high-R^2 fit.")
    lines.append("   2. WHAT IS THE RESIDUAL ENVELOPE?")
    lines.append(f"      Best fit among canonical hypotheses: {a.best_envelope}")
    lines.append(f"      Free power-law estimate: alpha = {a.power_law.alpha:.3f}")
    lines.append("      Interpret alpha: 0.5 = sqrt envelope (CLT/RH-like), 1.0 = linear")
    lines.append("      envelope (no fluctuation cancellation), in between =")
    lines.append("      anomalous diffusion / heavy-tailed steps.")
    lines.append("   3. WHAT MECHANISM IS ON THE TABLE?")
    lines.append("      This tool does NOT answer this question. Domain knowledge")
    lines.append("      required. Mechanism must predict envelope shape; check.")
    lines.append("")
    lines.append("=" * 72)
    return "\n".join(lines)
