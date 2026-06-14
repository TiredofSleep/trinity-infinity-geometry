"""muon.py -- the Muon optimizer (Keller Jordan, 2024): orthogonalize each
weight-matrix update via a few Newton-Schulz iterations, so steps move in the
spectral geometry of the matrix rather than coordinate-wise. <1% overhead, real
LM-training speedups at scale. Use Muon for the hidden 2-D weight matrices; keep
AdamW for embeddings, the head, norms, and biases.

This is the geometry-of-the-update lever from the Geometric Scribe plan, applied
to CK's trainer. We MEASURE whether it helps at our scale (train_ab.py), not
assume it.
"""
import torch


@torch.no_grad()
def _orthogonalize(G, steps=5):
    """Approximate the orthogonal factor of G via the quintic Newton-Schulz
    iteration (Jordan 2024 coefficients)."""
    a, b, c = 3.4445, -4.7750, 2.0315
    X = G.float()
    transposed = X.size(0) > X.size(1)
    if transposed:
        X = X.T
    X = X / (X.norm() + 1e-7)
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * (A @ A)
        X = a * X + B @ X
    if transposed:
        X = X.T
    return X


class Muon(torch.optim.Optimizer):
    def __init__(self, params, lr=0.02, momentum=0.95, nesterov=True, ns_steps=5):
        super().__init__(params, dict(lr=lr, momentum=momentum,
                                      nesterov=nesterov, ns_steps=ns_steps))

    @torch.no_grad()
    def step(self):
        for grp in self.param_groups:
            mom, nest, ns = grp["momentum"], grp["nesterov"], grp["ns_steps"]
            for p in grp["params"]:
                if p.grad is None:
                    continue
                st = self.state[p]
                if "m" not in st:
                    st["m"] = torch.zeros_like(p.grad)
                buf = st["m"]
                buf.mul_(mom).add_(p.grad)
                g = p.grad.add(buf, alpha=mom) if nest else buf
                O = _orthogonalize(g, ns)
                scale = max(1.0, p.size(0) / p.size(1)) ** 0.5
                p.add_(O.to(p.dtype), alpha=-grp["lr"] * scale)


def split_params(model):
    """Hidden 2-D weight matrices -> Muon; everything else -> AdamW."""
    muon, adam = [], []
    for name, p in model.named_parameters():
        if not p.requires_grad:
            continue
        hidden_2d = (p.ndim == 2 and not any(k in name.lower()
                     for k in ("emb", "lm_head", "head", "ln", "norm")))
        (muon if hidden_2d else adam).append(p)
    return muon, adam
