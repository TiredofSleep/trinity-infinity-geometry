"""gap_router.py -- P1: the Gap Router experiment.

THE CLAIM (pre-registered in CK_INTELLIGENCE_SYNTHESIS_2026-06-10.md):
residual failure TYPES are identifiable from residual statistics alone
(UOP four-type taxonomy), and routing a fixed compute budget by inferred
type beats uniform allocation at matched total budget.

THE SUITE (24 channels, 6 per type; each channel is a supervised stream
y = f(u) + noise that the learner samples under budget):

  Type I   injectivity failure : y learnable in the BASE feature family
           (polynomials deg<=2); residual falls as samples grow.
           Correct route: buy more samples.
  Type II  missing invariant   : y needs a feature OUTSIDE the base
           family (sin(7 pi u), |u-1/2|, parity band). More samples
           plateau. Correct route: spend ONE growth action (probe the
           candidate library, adopt the best feature), then samples.
  Type III admissibility failure: y independent of u (pure noise).
           Correct route: freeze the channel; spend nothing further.
  Type IV  time-consistency    : the map switches mid-stream (drift).
           Correct route: refit on the recent window only.

THE DIAGNOSTICS (the UOP decision procedure, made numerical -- each uses
ONLY the channel's own residual statistics, never the ground-truth type):

  D-slope : learning-curve improvement between half-budget and full-
            budget fits (relative). Improving -> Type I evidence.
  D-probe : max |corr(residual, g(u))| over a candidate feature library.
            Significant structure -> Type II evidence.
  D-info  : compare residual variance to a u-shuffled refit (permutation
            test). No information -> Type III evidence.
  D-drift : fit on first half, test on both halves; divergence ratio.
            Second-half blowup -> Type IV evidence.

ALLOCATORS at matched total budget:
  UNIFORM : round-robin samples, pooled fit, no growth, never stops.
  ROUTER  : classify each channel from diagnostics, then route.
  ORACLE  : routes by ground-truth type (upper bound).

CC-BY-4.0. Sanders + Claude. 2026-06-10.
"""
import numpy as np

RNG = np.random.default_rng(42)

BASE_FEATS = [lambda u: np.ones_like(u), lambda u: u, lambda u: u ** 2]
LIBRARY = {
    "sin7pi": lambda u: np.sin(7 * np.pi * u),
    "absu":   lambda u: np.abs(u - 0.5),
    "sin3pi": lambda u: np.sin(3 * np.pi * u),
    "cos5pi": lambda u: np.cos(5 * np.pi * u),
}


def design(u, extra=None):
    cols = [f(u) for f in BASE_FEATS]
    if extra:
        cols += [LIBRARY[name](u) for name in extra]
    return np.stack(cols, 1)


class Channel:
    def __init__(self, ctype, seed):
        self.ctype = ctype
        self.rng = np.random.default_rng(seed)
        self.noise = 0.05
        r = self.rng
        if ctype == 1:      # learnable in base family
            self.f = lambda u, w=r.uniform(-1, 1, 3): w[0] + w[1]*u + w[2]*u**2
        elif ctype == 2:    # needs library feature
            self.hidden = r.choice(["sin7pi", "absu"])
            g = LIBRARY[self.hidden]
            w = r.uniform(0.8, 1.2)
            self.f = lambda u, g=g, w=w: 0.3 * u + w * g(u)
        elif ctype == 3:    # pure noise
            self.f = lambda u: np.zeros_like(u)
            self.noise = 0.5
        else:               # drift: coefficients switch at the midpoint
            w1 = r.uniform(-1, 1, 3)
            w2 = -w1 + r.uniform(-0.3, 0.3, 3)
            self.w1, self.w2 = w1, w2
        self.t = 0          # stream clock (drives Type-IV switching)

    def sample(self, n, horizon=400):
        """Draw n stream samples; Type IV switches at horizon/2."""
        r = self.rng
        u = r.random(n)
        if self.ctype == 4:
            ts = self.t + np.arange(n)
            w = np.where((ts < horizon // 2)[:, None], self.w1, self.w2)
            y = (w[:, 0] + w[:, 1] * u + w[:, 2] * u ** 2
                 + self.noise * r.standard_normal(n))
            self.t += n
        else:
            y = self.f(u) + self.noise * r.standard_normal(n)
        return u, y

    def test_set(self, n=600):
        r = np.random.default_rng(10_000 + id(self) % 1000)
        u = r.random(n)
        if self.ctype == 4:                       # post-switch regime
            w = self.w2
            y = w[0] + w[1] * u + w[2] * u ** 2
        else:
            y = self.f(u)
        return u, y                                # noiseless target


def fit_ridge(u, y, extra=None, lam=1e-6, window=None):
    if window:
        u, y = u[-window:], y[-window:]
    X = design(u, extra)
    w = np.linalg.solve(X.T @ X + lam * np.eye(X.shape[1]), X.T @ y)
    return w, (extra or [])


def test_mse(ch, w, extra):
    u, y = ch.test_set()
    return float(np.mean((design(u, extra) @ w - y) ** 2))


# ------------------------- diagnostics --------------------------------
def diagnose(u, y):
    """Return (inferred_type, diagnostics dict) from residual stats only."""
    n = len(u)
    half = n // 2

    def res(uu, yy, extra=None):
        w, _ = fit_ridge(uu, yy, extra)
        return yy - design(uu, extra) @ w

    r_half = res(u[:half], y[:half])
    r_full = res(u, y)
    v_half, v_full = np.var(r_half), np.var(r_full)
    slope = (v_half - v_full) / (v_half + 1e-12)          # D-slope

    probes = {k: abs(np.corrcoef(r_full, LIBRARY[k](u))[0, 1])
              for k in LIBRARY}
    best_probe, probe_val = max(probes.items(), key=lambda kv: kv[1])

    # D-info: shuffled-input refit
    rng = np.random.default_rng(7)
    r_shuf = res(rng.permutation(u), y)
    info = 1.0 - v_full / (np.var(r_shuf) + 1e-12)        # ~0 => no info

    # D-drift: first-half model on second half
    w1, _ = fit_ridge(u[:half], y[:half])
    e1 = np.mean((design(u[:half]) @ w1 - y[:half]) ** 2)
    e2 = np.mean((design(u[half:]) @ w1 - y[half:]) ** 2)
    drift = e2 / (e1 + 1e-12)

    d = dict(slope=slope, probe=probe_val, best_probe=best_probe,
             info=info, drift=drift)

    if drift > 2.5:
        return 4, d
    if info < 0.15 and probe_val < 0.25:
        return 3, d
    if probe_val > 0.30:
        return 2, d
    return 1, d


# ------------------------- allocators ---------------------------------
def run_uniform(channels, budget_per=200, probe_n=60):
    total = 0
    losses = []
    for ch in channels:
        u, y = ch.sample(probe_n + budget_per)
        total += probe_n + budget_per
        w, extra = fit_ridge(u, y)
        losses.append(test_mse(ch, w, extra))
    return float(np.mean(losses)), total


def run_router(channels, budget_per=200, probe_n=60, oracle=False):
    total = 0
    losses = []
    correct = 0
    freed = 0
    # phase 1: probe every channel
    probes = []
    for ch in channels:
        u, y = ch.sample(probe_n)
        total += probe_n
        t_inf, d = (ch.ctype, None) if oracle else diagnose(u, y)
        correct += int(t_inf == ch.ctype)
        probes.append((ch, u, y, t_inf, d))
    # Type-III channels are frozen: their unspent budget is REAL savings;
    # redistribute it to the live channels.
    n_live = sum(1 for _, _, _, t, _ in probes if t != 3)
    pool = budget_per * len(channels)
    per_live = pool // max(n_live, 1)
    n_correct_final = 0
    for ch, u0, y0, t_inf, d in probes:
        if t_inf == 3:
            w, extra = fit_ridge(u0, y0)      # freeze with probe fit
            freed += 1
            t_final = 3
        else:
            u1, y1 = ch.sample(per_live)
            total += per_live
            u = np.concatenate([u0, u1])
            y = np.concatenate([y0, y1])
            # RE-DIAGNOSE at fit time on the full purchased stream:
            # drift (Type IV) is undetectable from a pre-switch probe;
            # classification legitimately uses all residual statistics
            # available when the fit is made.
            t_final, d = (ch.ctype, d) if oracle else diagnose(u, y)
            if t_final == 2:
                bp = (ch.hidden if oracle else d["best_probe"])
                w, extra = fit_ridge(u, y, extra=[bp])
            elif t_final == 4:
                w, extra = fit_ridge(u, y, window=len(u) // 3)
            else:
                w, extra = fit_ridge(u, y)
        n_correct_final += int(t_final == ch.ctype)
        losses.append(test_mse(ch, w, extra))
    return (float(np.mean(losses)), total,
            n_correct_final / len(channels), freed)


def build_suite(n_per_type=6, seed0=100):
    chans = []
    for t in (1, 2, 3, 4):
        for k in range(n_per_type):
            chans.append(Channel(t, seed0 + 10 * t + k))
    return chans


def run_experiment():
    suite = build_suite()
    res_u = run_uniform(build_suite())
    res_r = run_router(build_suite())
    res_o = run_router(build_suite(), oracle=True)
    return {
        "uniform": {"mean_test_mse": res_u[0], "samples": res_u[1]},
        "router": {"mean_test_mse": res_r[0], "samples": res_r[1],
                   "type_accuracy": res_r[2], "frozen_channels": res_r[3]},
        "oracle": {"mean_test_mse": res_o[0], "samples": res_o[1]},
        "n_channels": len(suite),
    }
