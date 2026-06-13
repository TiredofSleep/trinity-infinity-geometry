"""validate3.py -- the algebra as a PRIOR beats data-only few-shot.

validate2 showed the ruler spectrum is a lossy standalone feature (loses to the
raw embedding). The honest lesson: the algebra's value is as a PRIOR, not a
replacement. So we test the synthesis -- text-anchored prototypes (prototypical
networks, Snell 2017, with a CLIP-style text prior, Radford 2021):

  prototype_d = normalize( alpha * anchor_d  +  (1-alpha) * mean(k examples_d) )

  alpha = 0   -> data-only prototypes               == the BASELINE
  alpha = 1   -> description anchor only            == zero-shot, no examples
  alpha = 0.5 -> the algebra blended with the data  == OURS (pre-registered)

All in the strong raw 384-d space, cosine nearest-prototype. Same task as
validate2 (8-way, 16 terms/domain), many splits.

  REGISTERED: at k<=3, alpha=0.5 (algebra+data) > alpha=0 (data-only baseline).
  KILL: if alpha=0.5 <= alpha=0 at every k -> the prior does not help, negative.

  python validate3.py
"""
import json
import os
import numpy as np

from embed import embed
from spectra import RULERS
from validate2 import PROBE, KS, TRIALS

ALPHAS = [0.0, 0.25, 0.5, 0.75, 1.0]


def nrm(X):
    return X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-9)


def main(root):
    names = list(RULERS)
    terms, y = [], []
    for c, dom in enumerate(names):
        for w in PROBE[dom]:
            terms.append(w); y.append(c)
    y = np.array(y); C = len(names)
    E = nrm(embed(terms))
    A = nrm(embed([RULERS[d] for d in names]))      # description anchors, raw space

    idx = [np.where(y == c)[0] for c in range(C)]
    agg = {a: {k: 0.0 for k in KS} for a in ALPHAS}
    for t in range(TRIALS):
        rng = np.random.default_rng(2000 + t)
        for k in KS:
            tr, te = [], []
            for c in range(C):
                p = rng.permutation(idx[c]); tr.append(p[:k]); te += list(p[k:])
            te = np.array(te); yte = y[te]
            means = np.array([E[tr[c]].mean(0) for c in range(C)])
            means = nrm(means)
            for a in ALPHAS:
                proto = nrm(a * A + (1 - a) * means)
                pred = (E[te] @ proto.T).argmax(1)
                agg[a][k] += float((pred == yte).mean())
    for a in ALPHAS:
        for k in KS:
            agg[a][k] /= TRIALS

    print(f"8-way, {len(terms)} terms, {TRIALS} splits | cosine nearest-prototype"
          f" in raw 384-d | chance 0.125\n")
    print(f"  {'alpha':>22} | " + "  ".join(f"k={k}" for k in KS))
    lbl = {0.0: "0.0  data-only (BASE)", 0.5: "0.5  algebra+data (OURS)",
           1.0: "1.0  anchor-only (0-shot)"}
    for a in ALPHAS:
        print(f"  {lbl.get(a, f'{a}'):>22} | " + "  ".join(f"{agg[a][k]:.3f}" for k in KS))

    lo = [k for k in KS if k <= 3]
    base, ours = agg[0.0], agg[0.5]
    win = all(ours[k] > base[k] for k in lo)
    gain = np.mean([ours[k] - base[k] for k in lo])
    kill = all(ours[k] <= base[k] for k in KS)
    print("\n" + "=" * 64)
    if kill:
        print("  KILL — the prior never helps. Honest negative.")
    elif win:
        print(f"  BEATS BASELINE: algebra+data (alpha=0.5) beats data-only "
              f"prototypes at every k<=3, mean +{gain:.3f} accuracy.")
        print(f"    k=1: {base[1]:.3f} -> {ours[1]:.3f}  (+{ours[1]-base[1]:.3f}) | "
              f"k=3: {base[3]:.3f} -> {ours[3]:.3f}  (+{ours[3]-base[3]:.3f})")
        print("  The algebraic prior (one-line domain descriptions) is the head "
              "start: it helps most when examples are scarce, exactly the "
              "founding hypothesis.")
    else:
        print(f"  PARTIAL — wins at some k<=3 (mean {gain:+.3f}).")
    print("=" * 64)
    json.dump({str(a): {str(k): agg[a][k] for k in KS} for a in ALPHAS},
              open("validate3_result.json", "w"), indent=1)


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
