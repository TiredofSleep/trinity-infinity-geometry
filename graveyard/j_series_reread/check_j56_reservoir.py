"""Audit control for J56 P2: does the 'theorem-bearing' reservoir need the
canonical (disowned) TSML/BHML tables?  Swap in random commutative tables and
re-run the paper's LIFTED substrate with the paper's own tuning grid.

Run:  python -I check_j56_reservoir.py <archive>/05_papers/interdisciplinary/J56/manuscript/verification [n_tables]
      (<archive> is a checkout of the tag archive-2026-09-24; see README.md)
"""
import os
import sys
import time

import numpy as np

src = sys.argv[1]
n_tab = int(sys.argv[2]) if len(sys.argv) > 2 else 6
sys.path.insert(0, os.path.abspath(src))
import substrate as S  # noqa: E402
from benchmarks import make_tasks  # noqa: E402

WASHOUT = 200
LIFT_GRID = [dict(leak=l) for l in (0.6, 0.75, 0.9)]


def eval_lifted(tasks):
    out = {}
    for name, (u_tr, y_tr, u_te, y_te) in tasks.items():
        n_val = len(u_tr) // 5
        best = (None, np.inf)
        for cfg in LIFT_GRID:
            m = S.LiftedSubstrate(**cfg)
            F = m.run(u_tr)[WASHOUT:]
            yy = y_tr[WASHOUT:]
            w, _ = S.ridge_fit(F[:-n_val], yy[:-n_val])
            err = S.nrmse(F[-n_val:] @ w, yy[-n_val:])
            if err < best[1]:
                best = (m, err)
        m = best[0]
        w, _ = S.ridge_fit(m.run(u_tr)[WASHOUT:], y_tr[WASHOUT:])
        out[name] = S.nrmse(m.run(u_te)[WASHOUT:] @ w, y_te[WASHOUT:])
    return out


def rand_comm_table(rng):
    A = rng.integers(0, 10, (10, 10))
    return np.triu(A) + np.triu(A, 1).T


t0 = time.time()
tasks = make_tasks()
canon = eval_lifted(tasks)
print("canonical TSML/BHML LIFTED:", {k: round(v, 4) for k, v in canon.items()})
rng = np.random.default_rng(2026)
wins = {k: 0 for k in canon}
rows = []
for i in range(n_tab):
    T = rand_comm_table(rng)
    B = rand_comm_table(rng)
    S.T_TEN = S._bilinear_tensor(T.tolist())
    S.B_TEN = S._bilinear_tensor(B.tolist())
    S.MIX_TEN = 0.5 * S.T_TEN + 0.5 * S.B_TEN
    r = eval_lifted(tasks)
    rows.append(r)
    for k in canon:
        wins[k] += r[k] <= canon[k]
    print(f"random pair {i}:", {k: round(v, 4) for k, v in r.items()})
print("random pairs at least as good as canonical, per task:", wins, f"(of {n_tab})")
mg = [r["MackeyGlass-84"] for r in rows]
print(f"MackeyGlass-84: canonical {canon['MackeyGlass-84']:.4f}; random median {np.median(mg):.4f}, "
      f"min {min(mg):.4f}, max {max(mg):.4f}; paper's ESN(251) baseline 0.2002")
print(f"elapsed {time.time() - t0:.1f} s")
