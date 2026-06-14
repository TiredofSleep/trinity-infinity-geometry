"""counterparts.py -- learning from counterparts: two genuinely different LMs as
co-teachers. Counterpart A = MiniLM (external sentence model). Counterpart B =
CK's OWN book-trained GPT (ck_grow.pt). Fuse their representations by RELIABILITY
(so a weaker counterpart can't drag the result down) and measure whether the
second teacher helps over the strong one alone.

This is the society-of-rulers made of real models: CK + an external mind. As CK's
GPT trains, re-running shows it contributing more -- open-ended.

  python counterparts.py        # CPU; runs beside GPU training
"""
import io
import json
import os
import sys

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
LMDIR = r"C:\Users\brayd\OneDrive\Desktop\trinity-infinity-geometry\10_extensions\language-as-measurement"
sys.path.insert(0, LMDIR)
from embed import embed as minilm_embed
from validate2 import PROBE
from spectra import RULERS
import train_grow as TG

HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "ck_grow.pt")
BPE = os.path.join(HERE, "ck_bpe.json")
KS = [1, 2, 3, 5]
TRIALS = 100


def nrm(X):
    return X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-9)


def zr(S):
    return (S - S.mean(1, keepdims=True)) / (S.std(1, keepdims=True) + 1e-9)


def ck_gpt_embed(terms):
    from tokenizers import Tokenizer
    tk = Tokenizer.from_file(BPE)
    ck = torch.load(CKPT, map_location="cpu")
    TG.DEV = "cpu"
    model = TG.GrowGPT(TG.INIT_LAYERS)
    while len(model.blocks) < ck["n_layers"]:
        model.grow()
    model.load_state_dict(ck["model"])
    model.eval()
    out = []
    with torch.no_grad():
        for t in terms:
            ids = tk.encode(t).ids[:TG.CTX] or [0]
            idx = torch.tensor([ids])
            x = model.tok(idx) + model.pos(torch.arange(len(ids)))
            for b in model.blocks:
                x = b(x)
            out.append(model.lnf(x)[0].mean(0).numpy())
    return nrm(np.array(out, dtype=np.float64)), len(model.blocks)


def main():
    names = list(RULERS)
    terms, y = [], []
    for c, d in enumerate(names):
        for w in PROBE[d]:
            terms.append(w); y.append(c)
    y = np.array(y); C = len(names)

    EA = nrm(minilm_embed(terms).astype(np.float64))     # MiniLM
    if not os.path.exists(CKPT):
        print("no ck_grow.pt yet -- train first"); return
    EB, nL = ck_gpt_embed(terms)                          # CK's own GPT
    print(f"counterparts: MiniLM ({EA.shape[1]}d) + CK-GPT ({EB.shape[1]}d, {nL} layers) "
          f"| {len(terms)} terms, {C}-way\n")

    idx = [np.where(y == c)[0] for c in range(C)]
    agg = {k: dict(minilm=0.0, ckgpt=0.0, fused=0.0) for k in KS}
    for t in range(TRIALS):
        rng = np.random.default_rng(5000 + t)
        for k in KS:
            trc = [rng.permutation(idx[c])[:k] for c in range(C)]
            tr = np.concatenate(trc)
            te = np.array([i for i in range(len(terms)) if i not in set(tr)])
            yte = y[te]

            def scores(E):
                pr = nrm(np.array([E[trc[c]].mean(0) for c in range(C)]))
                return zr(E[te] @ pr.T)
            sA, sB = scores(EA), scores(EB)
            agg[k]["minilm"] += (sA.argmax(1) == yte).mean()
            agg[k]["ckgpt"] += (sB.argmax(1) == yte).mean()
            # reliability weights from a train holdout (k>=2); else trust MiniLM
            if k >= 2:
                h = k // 2
                fit = [trc[c][:h] for c in range(C)]; vl = [trc[c][h:] for c in range(C)]
                vi = np.concatenate(vl); yv = y[vi]

                def rel(E):
                    pr = nrm(np.array([E[fit[c]].mean(0) for c in range(C)]))
                    return float((zr(E[vi] @ pr.T).argmax(1) == yv).mean())
                ws = np.array([rel(EA), rel(EB)], float)
                ws[ws < 0.6 * ws.max()] = 0.0        # gate teachers below the bar
                wA, wB = float(ws[0]), float(ws[1])
            else:
                wA, wB = 1.0, 0.0
            fused = wA * sA + wB * sB
            agg[k]["fused"] += (fused.argmax(1) == yte).mean()
    for k in KS:
        for m in agg[k]:
            agg[k][m] /= TRIALS

    print(f"  {'k':>3} | {'MiniLM':>7} {'CK-GPT':>7} {'fused':>7}")
    for k in KS:
        print(f"  {k:>3} | {agg[k]['minilm']:>7.3f} {agg[k]['ckgpt']:>7.3f} {agg[k]['fused']:>7.3f}")
    helps = sum(agg[k]["fused"] > agg[k]["minilm"] + 1e-4 for k in KS)
    noharm = all(agg[k]["fused"] >= agg[k]["minilm"] - 0.01 for k in KS)
    print("\n" + "=" * 60)
    if helps >= 2:
        print(f"  COUNTERPART HELPS: fusing CK's own GPT with MiniLM beats MiniLM "
              f"alone at {helps}/{len(KS)} settings -- two minds > one.")
    elif noharm:
        print("  NO HARM: CK-GPT is still weak (early training); reliability-"
              "weighting keeps fusion >= MiniLM alone. As CK trains, re-run -- "
              "the society protocol is sound, the 2nd teacher will contribute more.")
    else:
        print("  HONEST NEGATIVE: fusion trails MiniLM here -- the weak counterpart "
              "hurt; needs stronger CK-GPT or better weighting.")
    print("=" * 60)
    json.dump({str(k): agg[k] for k in KS}, io.open(os.path.join(HERE, "counterparts_result.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
