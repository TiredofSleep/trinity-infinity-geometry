"""benchmarks.py -- three classic reservoir tasks with published
reference ranges, all CPU-seconds.

  NARMA-10        : nonlinear autoregressive system driven by U[0,0.5]
  Mackey-Glass    : tau=17 chaotic series, predict 84 steps ahead
  Lorenz x->z     : infer z(t) from x(t) (cross-prediction)

CC-BY-4.0. Sanders + Claude. 2026-06-10.
"""
import numpy as np


def narma10(n, seed=1):
    rng = np.random.default_rng(seed)
    u = rng.uniform(0, 0.5, n + 50)
    y = np.zeros(n + 50)
    for t in range(9, n + 49):
        y[t + 1] = (0.3 * y[t]
                    + 0.05 * y[t] * np.sum(y[t - 9:t + 1])
                    + 1.5 * u[t - 9] * u[t]
                    + 0.1)
    return u[50:], y[50:]            # input in [0,0.5] -> scale later


def mackey_glass(n, tau=17, seed=2, beta=0.2, gamma=0.1, nexp=10, dt=1.0):
    rng = np.random.default_rng(seed)
    hist = 1.2 + 0.2 * (rng.random(tau + 1) - 0.5)
    x = list(hist)
    for _ in range(n + 500):
        xt = x[-1]
        xtau = x[-tau - 1]
        dx = beta * xtau / (1 + xtau ** nexp) - gamma * xt
        x.append(xt + dt * dx)
    s = np.array(x[500:500 + n])
    s = (s - s.min()) / (s.max() - s.min())          # to [0,1]
    return s


def lorenz(n, dt=0.02, seed=3):
    rng = np.random.default_rng(seed)
    xyz = np.array([1.0, 1.0, 1.0]) + 0.01 * rng.random(3)
    out = np.empty((n + 200, 3))
    for t in range(n + 200):
        x, y, z = xyz
        d = np.array([10 * (y - x), x * (28 - z) - y, x * y - 8 / 3 * z])
        xyz = xyz + dt * d
        out[t] = xyz
    out = out[200:]
    out = (out - out.min(0)) / (out.max(0) - out.min(0))
    return out[:, 0], out[:, 2]                       # x -> z


def make_tasks():
    """Returns dict: name -> (u_train, y_train, u_test, y_test)."""
    tasks = {}

    u, y = narma10(6000)
    u2 = u / 0.5                                     # scale input to [0,1]
    tasks["NARMA-10"] = (u2[:4000], y[:4000], u2[4000:6000], y[4000:6000])

    s = mackey_glass(6000)
    horizon = 84
    u_mg = s[:-horizon]
    y_mg = s[horizon:]
    tasks["MackeyGlass-84"] = (u_mg[:4000], y_mg[:4000],
                               u_mg[4000:5800], y_mg[4000:5800])

    x, z = lorenz(6000)
    tasks["Lorenz-x2z"] = (x[:4000], z[:4000], x[4000:6000], z[4000:6000])
    return tasks
