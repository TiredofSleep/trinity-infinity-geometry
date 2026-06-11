"""baselines.py -- the two fair comparators for P2.

1. RandomESN: classic echo-state network, reservoir size chosen so the
   trained readout has the SAME width as the substrate reservoir's
   feature vector (matched trainable parameters; the only honest axis).
2. NGRC: next-generation reservoir computing on raw input lags
   (deterministic polynomial features, no dynamics at all) -- the
   strongest minimal deterministic baseline from the literature.

CC-BY-4.0. Sanders + Claude. 2026-06-10.
"""
import numpy as np


N_ULAGS = 10        # identical raw-input lag block for all models


class RandomESN:
    def __init__(self, n_features, seed=0, rho=0.9, leak=0.55,
                 in_scale=1.0, density=0.1):
        # features = [1 | u-lags | state] -> state size matches
        self.Nr = n_features - 1 - N_ULAGS
        rng = np.random.default_rng(seed)
        W = rng.standard_normal((self.Nr, self.Nr))
        mask = rng.random((self.Nr, self.Nr)) < density
        W = W * mask
        eig = np.max(np.abs(np.linalg.eigvals(W)))
        self.W = W * (rho / (eig + 1e-12))
        self.win = rng.uniform(-in_scale, in_scale, self.Nr)
        self.b = rng.uniform(-0.2, 0.2, self.Nr)
        self.leak = leak

    def run(self, u_seq):
        x = np.zeros(self.Nr)
        ulag = np.zeros(N_ULAGS)
        feats = np.empty((len(u_seq), 1 + N_ULAGS + self.Nr))
        for t, u in enumerate(u_seq):
            ulag = np.roll(ulag, 1)
            ulag[0] = u
            pre = self.W @ x + self.win * u + self.b
            x = (1 - self.leak) * x + self.leak * np.tanh(pre)
            feats[t] = np.concatenate(([1.0], ulag, x))
        return feats


class NGRC:
    """Deterministic polynomial features on input lags (no reservoir)."""

    def __init__(self, n_lags=10):
        self.k = n_lags

    def run(self, u_seq):
        n = len(u_seq)
        lag = np.zeros((n, self.k))
        for j in range(self.k):
            lag[j:, j] = u_seq[: n - j]
        iu = np.triu_indices(self.k)
        feats = np.empty((n, 1 + self.k + len(iu[0])))
        for t in range(n):
            quad = np.outer(lag[t], lag[t])[iu]
            feats[t] = np.concatenate(([1.0], lag[t], quad))
        return feats
