"""embed.py -- shared semantic-geometry helper for the language-as-measurement
kit. Words/topics become points in a real embedding space (local MiniLM, 384-d),
so curvature, drift, and cross-lens crossings are MEASURED, not asserted.

MiniLM is sentence-trained; single bare words are a noisier signal than phrases.
We embed bare terms (no phrasing bias) and report similarities honestly, spurious
ones included. Loads fully locally (no network).
"""
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

_M = "sentence-transformers/all-MiniLM-L6-v2"
_tok = _mdl = None


def _load():
    global _tok, _mdl
    if _mdl is None:
        _tok = AutoTokenizer.from_pretrained(_M, local_files_only=True)
        _mdl = AutoModel.from_pretrained(_M, local_files_only=True).eval()


def embed(texts):
    """Mean-pooled, L2-normalized MiniLM embeddings. Returns (n, 384) float64."""
    _load()
    b = _tok(list(texts), padding=True, truncation=True, max_length=64,
             return_tensors="pt")
    with torch.no_grad():
        o = _mdl(**b).last_hidden_state
    m = b["attention_mask"].unsqueeze(-1).float()
    v = (o * m).sum(1) / m.sum(1).clamp(min=1)
    v = torch.nn.functional.normalize(v, dim=1)
    return v.numpy().astype(np.float64)


def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


def pca2d(X):
    """Project rows of X to 2D via PCA (for figures only)."""
    Xc = X - X.mean(0)
    _, _, Vt = np.linalg.svd(Xc, full_matrices=False)
    return Xc @ Vt[:2].T


def turning_angles(P):
    """Discrete curvature along a path P (rows = points): the turning angle
    (degrees) between consecutive step vectors. Returns (step_lengths, angles)."""
    V = np.diff(P, axis=0)
    Ln = np.linalg.norm(V, axis=1)
    ang = []
    for i in range(len(V) - 1):
        c = (V[i] @ V[i + 1]) / (Ln[i] * Ln[i + 1] + 1e-12)
        ang.append(float(np.degrees(np.arccos(np.clip(c, -1, 1)))))
    return Ln, ang
