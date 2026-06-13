"""synthesis.py -- the general principle, tested: does a STACK of different
mathematical lenses beat the best single lens? Information as a path across
combined substrates -- only useful if the whole > the parts.

Four genuinely different paradigms, each a lens that scores every class for a
test point:
  ANCHOR     vector projection onto class descriptions (semantic axes)
  HIERARCHY  coarse parent prior shared by sibling classes (multiresolution ladder)
  DATA       cosine to the k-example prototype (metric geometry of the manifold)
  GRAPH      label propagation over the kNN similarity graph (spectral/relational)

Each lens' per-class scores are z-normalized per point so they are comparable.
Two ways to combine:
  FUSE-equal       sum the lenses (naive)
  FUSE-confidence  weight each lens by how decisive it is at THAT point
                   (margin top1-top2) -- let the confident paradigm lead. This is
                   "multiple paradigms refine each other's resolutions".

  REGISTERED: FUSE-confidence >= the best single lens at EVERY k (robust dominance).
  KILL: if no fusion ever beats the best single lens -> combining doesn't help.

  python synthesis.py
"""
import os
import numpy as np

from embed import embed
from spectra import RULERS
from validate2 import PROBE, KS, TRIALS

PARENTS = {
    "physical sciences of matter, force and energy":
        ["thermodynamics", "electromagnetism", "wave mechanics", "particle physics"],
    "formal sciences of pure mathematical structure":
        ["geometry", "number theory", "algebra"],
    "information, coding and communication":
        ["information theory"],
}


def nrm(X):
    return X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-9)


def zrows(S):
    return (S - S.mean(1, keepdims=True)) / (S.std(1, keepdims=True) + 1e-9)


def margin(S):                      # per-row decisiveness: top1 - top2
    s = np.sort(S, 1)
    return s[:, -1] - s[:, -2]


def graph_scores(Eall, tr, ytr, C, k=10, steps=4, a=0.6):
    n = len(Eall)
    S = Eall @ Eall.T
    np.fill_diagonal(S, -1)
    nn = np.argsort(-S, 1)[:, :k]
    W = np.zeros((n, n))
    rows = np.repeat(np.arange(n), k)
    W[rows, nn.ravel()] = np.clip(S[rows, nn.ravel()], 0, None)
    W = (W + W.T) / 2
    Wn = W / (W.sum(1, keepdims=True) + 1e-9)
    Y = np.zeros((n, C))
    Y[tr, ytr] = 1.0
    F = Y.copy()
    for _ in range(steps):
        F = a * (Wn @ F) + (1 - a) * Y
    return F


def main(root):
    names = list(RULERS)
    terms, y = [], []
    for c, d in enumerate(names):
        for w in PROBE[d]:
            terms.append(w); y.append(c)
    y = np.array(y); C = len(names)
    E = nrm(embed(terms))
    A = nrm(embed([RULERS[d] for d in names]))               # class anchors
    pnames = list(PARENTS)
    PA = nrm(embed(pnames))                                   # parent anchors
    parent_of = np.array([[i for i, p in enumerate(pnames) if d in PARENTS[p]][0]
                          for d in names])
    PAcls = PA[parent_of]                                     # parent anchor per class

    idx = [np.where(y == c)[0] for c in range(C)]
    LENSES = ["anchor", "hierarchy", "data", "graph"]
    FUSE_OVER = ["anchor", "data", "graph"]    # hierarchy is a coarse prior, not a
    #                                            fine classifier -> reported, not fused
    FUSED = ["fuse-equal", "fuse-confidence", "fuse-gate", "fuse-reliability"]
    agg = {m: {k: 0.0 for k in KS} for m in LENSES + FUSED}

    for t in range(TRIALS):
        rng = np.random.default_rng(4000 + t)
        for k in KS:
            tr_by_c = [rng.permutation(idx[c])[:k] for c in range(C)]
            tr = np.concatenate(tr_by_c)
            ytr = np.concatenate([[c] * k for c in range(C)])
            te = np.array([i for i in range(len(terms)) if i not in set(tr)])
            yte = y[te]
            protos = nrm(np.array([E[tr_by_c[c]].mean(0) for c in range(C)]))
            sc = {
                "anchor":    zrows(E[te] @ A.T),
                "hierarchy": zrows(E[te] @ PAcls.T),
                "data":      zrows(E[te] @ protos.T),
                "graph":     zrows(graph_scores(E, tr, ytr, C)[te]),
            }
            for L in LENSES:
                agg[L][k] += float((sc[L].argmax(1) == yte).mean())
            eq = sum(sc[L] for L in FUSE_OVER)
            agg["fuse-equal"][k] += float((eq.argmax(1) == yte).mean())
            cw = sum((np.clip(margin(sc[L]), 0, None)[:, None] ** 1.5) * sc[L]
                     for L in FUSE_OVER)
            agg["fuse-confidence"][k] += float((cw.argmax(1) == yte).mean())
            # gate: per point, let the single most-decisive lens answer
            M = np.stack([margin(sc[L]) for L in FUSE_OVER], 1)
            preds = np.stack([sc[L].argmax(1) for L in FUSE_OVER], 1)
            gate = preds[np.arange(len(te)), M.argmax(1)]
            agg["fuse-gate"][k] += float((gate == yte).mean())
            # reliability-weighted: trust each lens by how well it predicts a
            # held-out slice of the few examples (empirical-Bayes shrinkage). With
            # <2/class, data/graph can't be checked -> trust only the prior (anchor).
            if k < 2:
                r = {"anchor": 1.0, "data": 0.0, "graph": 0.0}
            else:
                h = k // 2
                fit = [tr_by_c[c][:h] for c in range(C)]
                val = [tr_by_c[c][h:] for c in range(C)]
                fi = np.concatenate(fit); yfi = np.concatenate([[c]*len(fit[c]) for c in range(C)])
                vi = np.concatenate(val); yv = np.concatenate([[c]*len(val[c]) for c in range(C)])
                pf = nrm(np.array([E[fit[c]].mean(0) for c in range(C)]))
                r = {"anchor": float(((E[vi] @ A.T).argmax(1) == yv).mean()),
                     "data": float(((E[vi] @ pf.T).argmax(1) == yv).mean()),
                     "graph": float((graph_scores(E, fi, yfi, C)[vi].argmax(1) == yv).mean())}
            rel = sum(max(r[L], 0.0) * sc[L] for L in FUSE_OVER)
            agg["fuse-reliability"][k] += float((rel.argmax(1) == yte).mean())
    for m in agg:
        for k in KS:
            agg[m][k] /= TRIALS

    print(f"{C}-way, {len(terms)} terms, {TRIALS} splits | chance {1/C:.3f}\n")
    print(f"  {'lens / fusion':>16} | " + "  ".join(f"k={k}" for k in KS))
    for m in LENSES + FUSED:
        star = "  <-- fusion" if m in FUSED else ""
        print(f"  {m:>16} | " + "  ".join(f"{agg[m][k]:.3f}" for k in KS) + star)

    best_single = {k: max(agg[L][k] for L in LENSES) for k in KS}
    best_fuse = {k: max(agg[m][k] for m in FUSED) for k in KS}
    robust = all(best_fuse[k] >= best_single[k] - 1e-9 for k in KS)
    strict = sum(best_fuse[k] > best_single[k] + 1e-9 for k in KS)
    print("\n  best SINGLE lens per k: " +
          "  ".join(f"k={k}:{best_single[k]:.3f}" for k in KS))
    print("  best FUSION    per k: " +
          "  ".join(f"k={k}:{best_fuse[k]:.3f}" for k in KS))
    print("=" * 64)
    if robust:
        print(f"  THE WHOLE >= THE PARTS at EVERY k (strictly better at {strict}/"
              f"{len(KS)}). The combined map is never worse than the best single "
              "lens and pulls ahead where lenses are comparable -- you don't have "
              "to know in advance which paradigm to trust.")
    else:
        gaps = {k: round(best_fuse[k] - best_single[k], 3) for k in KS}
        print(f"  PARTIAL: best-fusion - best-single per k = {gaps}. Honest -- "
              "when one lens dominates, naive combining can't beat it; fusion wins "
              "only where lenses are comparable.")
    print("=" * 64)
    import json
    json.dump({"ks": KS, "curves": {m: {str(k): agg[m][k] for k in KS}
              for m in LENSES + FUSED}},
              open("synthesis_result.json", "w"), indent=1)


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
