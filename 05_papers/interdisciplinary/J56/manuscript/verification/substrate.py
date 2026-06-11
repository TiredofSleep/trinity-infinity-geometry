"""substrate.py -- the theorem-bearing reservoir.

State: a probability vector p over the 10 substrate nodes (Z/10Z
operators). Dynamics: the J01 bilinear iteration at the PROVEN mixing
point alpha = 1/2, driven by input injected as a second distribution:

    M(p, q)_k = (1/2) * T(p, q)_k + (1/2) * B(p, q)_k
    p_{t+1}   = normalize( (1 - leak) * M(p_t, q_t) + leak * p_t )

where T, B are the canonical TSML / BHML composition tables read as
bilinear maps (T(p,q)_k = sum_{i,j : TSML[i][j]=k} p_i q_j).

Canon anchors: alpha = 1/2 is the unique rational mixing point with an
algebraic attractor (J01 Theorem F.2); the autonomous iteration
contracts to the 4-core attractor with H/Br = 1 + sqrt(3) (J01/J15) --
the substrate analog of the echo-state property, which we additionally
verify empirically here (state convergence from distinct initial
conditions under identical input).

Features (NG-RC style): [1, p_t, p_{t-1}, uptri(p_t p_t^T),
uptri(p_{t-1} p_{t-1}^T)]  -> 131 dims; readout = ridge regression
(one linear solve). Trainable parameters live ONLY in the readout.

CC-BY-4.0. Sanders + Claude. 2026-06-10.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ck_tables  # noqa: E402  (canonical TSML/BHML)

N = 10
IU = np.triu_indices(N)          # 55 upper-tri indices


def _bilinear_tensor(table):
    M = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N):
            M[table[i][j], i, j] += 1.0
    return M


T_TEN = _bilinear_tensor(ck_tables.TSML)
B_TEN = _bilinear_tensor(ck_tables.BHML)
MIX_TEN = 0.5 * T_TEN + 0.5 * B_TEN          # alpha = 1/2 (Theorem F.2 point)

# the sigma permutation (canon: cycle (1 7 6 5 4 2), fixed {0,3,8,9})
SIGMA = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]


def mix_tensor(alpha):
    return alpha * T_TEN + (1.0 - alpha) * B_TEN


def encode_input(u):
    """Scalar in [0,1] -> distribution on the 10 nodes (triangular bump)."""
    x = 9.0 * np.clip(u, 0.0, 1.0)
    lo = int(np.floor(x))
    hi = min(lo + 1, 9)
    f = x - lo
    q = np.zeros(N)
    q[lo] += 1.0 - f
    q[hi] += f
    return q


N_ULAGS = 10        # raw-input lag block, identical for ALL models (fair)
N_PLAGS = 8         # substrate state-lag taps (memory lives in the taps,
                    # NG-RC style; the nonlinearity source stays the
                    # theorem-bearing bilinear map)


class SubstrateReservoir:
    """Fixed substrate dynamics; only the ridge readout is trained.

    Feature layout: [1 | u-lags (10) | p_t..p_{t-7} (80) | uptri(p_t) (55)]
    -> 146 dims. The matched random ESN gets the same constant + u-lag
    blocks and a 135-unit state, also 146 dims.
    """

    def __init__(self, leak=0.8, eps=1e-6):
        self.leak = leak
        self.eps = eps

    def run(self, u_seq):
        """Drive with scalar sequence u in [0,1]; return feature matrix."""
        p = np.full(N, 1.0 / N)
        hist = [p.copy() for _ in range(N_PLAGS)]
        ulag = np.zeros(N_ULAGS)
        n_feat = 1 + N_ULAGS + N_PLAGS * N + len(IU[0])
        feats = np.empty((len(u_seq), n_feat))
        for t, u in enumerate(u_seq):
            ulag = np.roll(ulag, 1)
            ulag[0] = u
            q = encode_input(u)
            m = np.einsum("kij,i,j->k", MIX_TEN, p, q)
            s = m.sum()
            m = m / s if s > 0 else np.full(N, 1.0 / N)
            p_new = (1.0 - self.leak) * m + self.leak * p
            p_new = np.maximum(p_new, self.eps)
            p_new /= p_new.sum()
            hist.pop()
            hist.insert(0, p_new)
            p = p_new
            op = np.outer(p, p)[IU]
            feats[t] = np.concatenate(([1.0], ulag,
                                       np.concatenate(hist), op))
        return feats

    def fading_memory_check(self, u_seq, n_check=200):
        """Echo-state-style check: two far-apart initial states converge
        under identical input. Returns final L1 distance."""
        rng = np.random.default_rng(0)
        p1 = np.full(N, 1.0 / N)
        p2 = rng.dirichlet(np.ones(N))
        for u in u_seq[:n_check]:
            q = encode_input(u)
            for tag in (1, 2):
                p = p1 if tag == 1 else p2
                m = np.einsum("kij,i,j->k", MIX_TEN, p, q)
                m /= m.sum()
                p_new = (1.0 - self.leak) * m + self.leak * p
                p_new = np.maximum(p_new, 1e-6)
                p_new /= p_new.sum()
                if tag == 1:
                    p1 = p_new
                else:
                    p2 = p_new
        return float(np.abs(p1 - p2).sum())


class LiftedSubstrate:
    """P2 fix: the LENS ENSEMBLE lift.

    The v0 single-core substrate lost 2/3 tasks to a width-matched ESN:
    a 10-dim simplex state is information-bottlenecked against a
    135-unit tanh reservoir. The ESN's advantage was DIVERSITY (random
    weights). The substrate's principled diversity axis is the J01
    alpha-FAMILY: every alpha in [0,1] gives a distinct bilinear
    dynamical lens on the same tables (alpha = 1/2 is the proven
    attractor point; the ensemble spans the family), crossed with leak
    timescales and sigma^k input-routing shifts (the canon permutation
    re-addressing the input bump -- 'same streets, different names').

    K units x 10 nodes; features = [1 | u-lags(10) | states(10K) |
    states^2 elementwise(10K)] -> 1 + 10 + 20K dims. Readout: ridge.
    """

    def __init__(self, K=12, leak=None, eps=1e-6):
        alphas = [0.0, 0.25, 0.5, 0.75, 1.0, 0.5,
                  0.125, 0.375, 0.625, 0.875, 0.5, 0.25]
        leaks = [0.6, 0.9, 0.75, 0.6, 0.9, 0.95,
                 0.7, 0.85, 0.6, 0.9, 0.5, 0.8]
        shifts = [0, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 5]
        if leak is not None:                 # global leak rescale (tuning)
            leaks = [min(0.98, l * leak / 0.75) for l in leaks]
        self.units = []
        for k in range(K):
            ten = mix_tensor(alphas[k % len(alphas)])
            # sigma^shift re-addresses input nodes ('renaming the streets')
            perm = np.arange(N)
            for _ in range(shifts[k % len(shifts)]):
                perm = np.array([SIGMA[i] for i in perm])
            self.units.append((ten, leaks[k % len(leaks)], perm))
        self.eps = eps
        self.K = K

    def run(self, u_seq):
        K = self.K
        ps = [np.full(N, 1.0 / N) for _ in range(K)]
        ulag = np.zeros(N_ULAGS)
        n_feat = 1 + N_ULAGS + 2 * K * N
        feats = np.empty((len(u_seq), n_feat))
        for t, u in enumerate(u_seq):
            ulag = np.roll(ulag, 1)
            ulag[0] = u
            q0 = encode_input(u)
            states = []
            for k, (ten, leak, perm) in enumerate(self.units):
                q = q0[perm]
                p = ps[k]
                m = np.einsum("kij,i,j->k", ten, p, q)
                s = m.sum()
                m = m / s if s > 0 else np.full(N, 1.0 / N)
                p_new = (1.0 - leak) * m + leak * p
                p_new = np.maximum(p_new, self.eps)
                p_new /= p_new.sum()
                ps[k] = p_new
                states.append(p_new)
            st = np.concatenate(states)
            feats[t] = np.concatenate(([1.0], ulag, st, st * st))
        return feats


def ridge_fit(X, y, lams=(1e-8, 1e-6, 1e-4, 1e-2, 1e-1), val_frac=0.2):
    """Ridge with lambda chosen on a tail validation split. One solve per
    lambda; returns (w, best_lambda)."""
    n = len(y)
    n_val = max(1, int(n * val_frac))
    Xtr, ytr = X[:-n_val], y[:-n_val]
    Xv, yv = X[-n_val:], y[-n_val:]
    A = Xtr.T @ Xtr
    b = Xtr.T @ ytr
    best = (None, None, np.inf)
    for lam in lams:
        w = np.linalg.solve(A + lam * np.eye(A.shape[0]), b)
        err = float(np.mean((Xv @ w - yv) ** 2))
        if err < best[2]:
            best = (w, lam, err)
    # refit on all data at the chosen lambda
    A = X.T @ X
    b = X.T @ y
    w = np.linalg.solve(A + best[1] * np.eye(A.shape[0]), b)
    return w, best[1]


def nrmse(yhat, y):
    return float(np.sqrt(np.mean((yhat - y) ** 2) / (np.var(y) + 1e-30)))
