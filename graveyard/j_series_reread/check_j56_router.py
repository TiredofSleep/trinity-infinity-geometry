"""Audit check for J56 P1 (the Gap Router) -- what produces the 125x?

Uses the paper's own suite (gap_router.py, imported from the archived J56
folder) and adds controls written fresh here:
  * a deterministic test-set seed (the original seeds test sets with id(self),
    a memory address, so its P1 numbers change from run to run);
  * per-type error breakdown;
  * 'uniform + library' : no taxonomy at all, just the router's feature library;
  * 'uniform + library + recency window' : still no classification;
  * the router with the hidden Type-II features removed from its library.

Run:  python -I check_j56_router.py <archive>/05_papers/interdisciplinary/J56/manuscript/verification
      (<archive> is a checkout of the tag archive-2026-09-24; see README.md)
"""
import os
import sys

import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) < 2:
    sys.exit("usage: python -I check_j56_router.py <path to the archived J56/manuscript/verification>")
src = sys.argv[1]
sys.path.insert(0, os.path.abspath(src))
import gap_router as gr  # noqa: E402

FAIL = []


def check(label, ok):
    print(("  [ok]   " if ok else "  [FAIL] ") + label)
    if not ok:
        FAIL.append(label)


# 1. reproducibility: the test set is seeded from id(self)
import inspect  # noqa: E402
src_ts = inspect.getsource(gr.Channel.test_set)
check("Channel.test_set seeds its RNG with id(self) (a memory address): P1 is not 'fully seeded'",
      "id(self)" in src_ts)

# deterministic replacement: seed from channel type and a per-suite index
_counter = {"k": 0}


def build_suite_det(n_per_type=6, seed0=100):
    chans = []
    for t in (1, 2, 3, 4):
        for k in range(n_per_type):
            ch = gr.Channel(t, seed0 + 10 * t + k)
            ch._tseed = 10_000 + 37 * t + k
            chans.append(ch)
    return chans


def test_set_det(self, n=600):
    r = np.random.default_rng(self._tseed)
    u = r.random(n)
    if self.ctype == 4:
        w = self.w2
        y = w[0] + w[1] * u + w[2] * u ** 2
    else:
        y = self.f(u)
    return u, y


gr.Channel.test_set = test_set_det


def per_type(losses, chans):
    out = {}
    for t in (1, 2, 3, 4):
        v = [l for l, c in zip(losses, chans) if c.ctype == t]
        out[t] = float(np.mean(v))
    return out


def run_uniform_variant(chans, extra=None, window=None, budget_per=200, probe_n=60):
    losses = []
    for ch in chans:
        u, y = ch.sample(probe_n + budget_per)
        w, ex = gr.fit_ridge(u, y, extra=extra, window=window)
        losses.append(gr.test_mse(ch, w, ex))
    return losses


def run_router_losses(chans, oracle=False):
    """Same allocator as gr.run_router, but returns per-channel losses."""
    budget_per, probe_n = 200, 60
    probes = []
    for ch in chans:
        u, y = ch.sample(probe_n)
        t_inf, d = (ch.ctype, None) if oracle else gr.diagnose(u, y)
        probes.append((ch, u, y, t_inf, d))
    n_live = sum(1 for p in probes if p[3] != 3)
    per_live = budget_per * len(chans) // max(n_live, 1)
    losses, correct = [], 0
    for ch, u0, y0, t_inf, d in probes:
        if t_inf == 3:
            w, ex = gr.fit_ridge(u0, y0)
            t_final = 3
        else:
            u1, y1 = ch.sample(per_live)
            u = np.concatenate([u0, u1])
            y = np.concatenate([y0, y1])
            t_final, d = (ch.ctype, d) if oracle else gr.diagnose(u, y)
            if t_final == 2:
                bp = ch.hidden if oracle else d["best_probe"]
                w, ex = gr.fit_ridge(u, y, extra=[bp])
            elif t_final == 4:
                w, ex = gr.fit_ridge(u, y, window=len(u) // 3)
            else:
                w, ex = gr.fit_ridge(u, y)
        correct += int(t_final == ch.ctype)
        losses.append(gr.test_mse(ch, w, ex))
    return losses, correct


ALL = list(gr.LIBRARY)
res = {}
s = build_suite_det()
res["uniform (paper)"] = run_uniform_variant(s)
s = build_suite_det()
res["router (paper)"], acc_r = run_router_losses(s)
s = build_suite_det()
res["oracle (paper)"], _ = run_router_losses(s, oracle=True)
s = build_suite_det()
res["uniform + library, no taxonomy"] = run_uniform_variant(s, extra=ALL)
s = build_suite_det()
res["uniform + library + last-third window, no taxonomy"] = run_uniform_variant(s, extra=ALL, window=87)

print("=" * 78)
print(f"{'allocator (deterministic test sets)':52s} {'mean MSE':>9s}   I      II     III    IV")
for k, v in res.items():
    pt = per_type(v, build_suite_det())
    print(f"{k:52s} {np.mean(v):9.5f}  " + "  ".join(f"{pt[t]:.4f}" for t in (1, 2, 3, 4)))
print("=" * 78)
check(f"router type accuracy on the paper's suite: {acc_r}/24", acc_r == 24)
U = per_type(res["uniform (paper)"], build_suite_det())
Rr = per_type(res["router (paper)"], build_suite_det())
UL = per_type(res["uniform + library, no taxonomy"], build_suite_det())
ULW = per_type(res["uniform + library + last-third window, no taxonomy"], build_suite_det())
share4 = U[4] / (U[1] + U[2] + U[3] + U[4])
check(f"uniform's mean error is {100 * share4:.0f}% Type IV (drift channels whose post-switch map is "
      f"built as roughly minus the pre-switch map)", share4 > 0.75)
check(f"the feature library alone, with no classification, fixes Type II: {U[2]:.4f} -> {UL[2]:.4f}",
      UL[2] < 0.01 * U[2])
check(f"a fixed recency window alone, with no classification, cuts Type IV {U[4]:.3f} -> {ULW[4]:.3f}",
      ULW[4] < 0.25 * U[4])
check(f"freezing Type III after a 60-sample probe makes those channels WORSE than uniform: "
      f"{Rr[3]:.4f} vs {U[3]:.4f}", Rr[3] > U[3])

# 5. remove the hidden Type-II features from the router's library (build the suite first:
#    the channels capture their hidden functions at construction)
s = build_suite_det()
saved = dict(gr.LIBRARY)
for kname in ("sin7pi", "absu"):
    gr.LIBRARY.pop(kname)
loss_nolib, acc_nolib = run_router_losses(s)
gr.LIBRARY.clear()
gr.LIBRARY.update(saved)
ptn = per_type(loss_nolib, build_suite_det())
print(f"router with sin7pi/absu removed from its library: mean MSE {np.mean(loss_nolib):.4f}, "
      f"type accuracy {acc_nolib}/24, per-type " + "  ".join(f"{ptn[t]:.4f}" for t in (1, 2, 3, 4)))
check(f"without the hidden features in its library the router's Type-II error returns to the uniform level "
      f"({ptn[2]:.4f} vs uniform {U[2]:.4f})", ptn[2] > 0.5 * U[2])

print(f"failures: {len(FAIL)}")
sys.exit(1 if FAIL else 0)
