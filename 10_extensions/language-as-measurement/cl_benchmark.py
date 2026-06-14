"""cl_benchmark.py -- Split-CIFAR-100 class-incremental learning, standard protocol.
Tests whether our learner's core (nearest-class-mean prototypes on frozen features,
replay-free, training-free, interpretable) is COMPETITIVE with the standard CL
baselines (Fine-tune, EWC, Experience Replay) and how far it is from the Joint
upper bound.

Setting: 10 tasks x 10 classes, class-incremental (task-agnostic inference).
Backbone: ImageNet-pretrained ResNet-18, FROZEN (the "CL with pretrained models"
setting, e.g. RanPAC 2023). Metrics: final average accuracy, average incremental
accuracy, and forgetting (Chaudhry 2018).

  python cl_benchmark.py [seed]

Honest scope: a first, lightly-tuned pass (1 backbone, modest baseline tuning).
The field standard also wants 3+ seeds and tuned baselines -- run with several
seeds and report mean+/-std; this script supports a seed arg for that.
"""
import io
import json
import os
import sys

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "cifar_data")
FEATS = os.path.join(HERE, "cifar100_feats.npz")
DEV = "cuda" if torch.cuda.is_available() else "cpu"
T, PER = 10, 10                      # 10 tasks, 10 classes each
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 0


def extract_features():
    if os.path.exists(FEATS):
        d = np.load(FEATS)
        return d["Xtr"], d["ytr"], d["Xte"], d["yte"]
    import torchvision
    from torchvision.models import resnet18, ResNet18_Weights
    w = ResNet18_Weights.IMAGENET1K_V1
    net = resnet18(weights=w); net.fc = nn.Identity(); net.eval().to(DEV)
    tf = w.transforms()

    def feats(train):
        ds = torchvision.datasets.CIFAR100(DATA, train=train, download=True, transform=tf)
        dl = torch.utils.data.DataLoader(ds, batch_size=256, num_workers=0)
        X, Y = [], []
        with torch.no_grad():
            for xb, yb in dl:
                with torch.autocast("cuda", dtype=torch.bfloat16):
                    f = net(xb.to(DEV))
                X.append(f.float().cpu().numpy()); Y.append(yb.numpy())
        return np.concatenate(X), np.concatenate(Y)
    Xtr, ytr = feats(True); Xte, yte = feats(False)
    np.savez(FEATS, Xtr=Xtr, ytr=ytr, Xte=Xte, yte=yte)
    print(f"extracted features: train {Xtr.shape}, test {Xte.shape}", flush=True)
    return Xtr, ytr, Xte, yte


def nrm(X):
    return X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)


def acc_matrix_ncm(Xtr, ytr, Xte, yte, tasks, cls2task):
    Xtrn, Xten = nrm(Xtr), nrm(Xte)
    protos = {}
    R = np.zeros((T, T))
    for t in range(T):
        for c in tasks[t]:
            protos[c] = Xtrn[ytr == c].mean(0)
        seen = [c for tt in range(t + 1) for c in tasks[tt]]
        P = np.stack([protos[c] for c in seen]); Pn = nrm(P)
        for i in range(t + 1):
            m = np.isin(yte, tasks[i])
            pred = np.array(seen)[(Xten[m] @ Pn.T).argmax(1)]
            R[t, i] = (pred == yte[m]).mean()
    return R


def acc_matrix_linear(Xtr, ytr, Xte, yte, tasks, cls2task, method):
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-6
    Xtr2, Xte2 = (Xtr - mu) / sd, (Xte - mu) / sd
    Xtr2 = torch.tensor(Xtr2, dtype=torch.float32, device=DEV)
    Xte2 = torch.tensor(Xte2, dtype=torch.float32, device=DEV)
    ytr_t = torch.tensor(ytr, device=DEV); yte_t = torch.tensor(yte, device=DEV)
    clf = nn.Linear(Xtr.shape[1], 100).to(DEV)
    buf_x, buf_y, BUF = [], [], 2000
    fisher, star = None, None
    R = np.zeros((T, T))
    seen_mask = torch.zeros(100, dtype=torch.bool, device=DEV)
    rng = np.random.default_rng(SEED)
    for t in range(T):
        for c in tasks[t]:
            seen_mask[c] = True
        idx = np.where(np.isin(ytr, tasks[t]))[0]
        opt = torch.optim.Adam(clf.parameters(), lr=1e-3, weight_decay=1e-4)
        epochs = 10 if method == "joint" else 6
        src = np.where(np.isin(ytr, [c for tt in range(t + 1) for c in tasks[tt]]))[0] if method == "joint" else idx
        for _ in range(epochs):
            perm = rng.permutation(src)
            for b in range(0, len(perm), 256):
                bi = perm[b:b + 256]
                xb, yb = Xtr2[bi], ytr_t[bi]
                if method == "er" and buf_x:
                    k = min(128, len(buf_x))
                    sel = rng.choice(len(buf_x), k, replace=False)
                    xb = torch.cat([xb, torch.stack([buf_x[j] for j in sel])])
                    yb = torch.cat([yb, torch.tensor([buf_y[j] for j in sel], device=DEV)])
                opt.zero_grad()
                loss = F.cross_entropy(clf(xb), yb)
                if method == "ewc" and fisher is not None:
                    loss = loss + 50.0 * (fisher * (torch.cat([p.flatten() for p in clf.parameters()]) - star) ** 2).sum()
                loss.backward(); opt.step()
        if method == "er":
            for j in idx:                                  # reservoir
                if len(buf_x) < BUF:
                    buf_x.append(Xtr2[j].detach()); buf_y.append(int(ytr[j]))
                else:
                    r = rng.integers(0, len(buf_x))
                    if r < BUF:
                        buf_x[r] = Xtr2[j].detach(); buf_y[r] = int(ytr[j])
        if method == "ewc":
            clf.zero_grad()
            for j in idx[:2000]:
                F.cross_entropy(clf(Xtr2[j:j + 1]), ytr_t[j:j + 1]).backward()
            g = torch.cat([p.grad.flatten() for p in clf.parameters()]) / min(2000, len(idx))
            fisher = g ** 2 if fisher is None else fisher + g ** 2
            star = torch.cat([p.detach().flatten() for p in clf.parameters()])
        with torch.no_grad():
            logits = clf(Xte2); logits[:, ~seen_mask] = -1e9
            pred = logits.argmax(1)
            for i in range(t + 1):
                m = torch.tensor(np.isin(yte, tasks[i]), device=DEV)
                R[t, i] = (pred[m] == yte_t[m]).float().mean().item()
    return R


def metrics(R):
    final = float(np.mean([R[T - 1, i] for i in range(T)]))
    aia = float(np.mean([np.mean([R[t, i] for i in range(t + 1)]) for t in range(T)]))
    forget = float(np.mean([max(R[t, i] for t in range(i, T)) - R[T - 1, i] for i in range(T - 1)]))
    return final, aia, forget


def main():
    Xtr, ytr, Xte, yte = extract_features()
    rng = np.random.default_rng(SEED)
    order = rng.permutation(100)
    tasks = [list(order[i * PER:(i + 1) * PER]) for i in range(T)]
    cls2task = {c: t for t, cs in enumerate(tasks) for c in cs}
    print(f"Split-CIFAR-100 | {T} tasks x {PER} | frozen ResNet-18 | seed {SEED} | {DEV}\n")

    res = {}
    res["NCM (ours)"] = acc_matrix_ncm(Xtr, ytr, Xte, yte, tasks, cls2task)
    for m in ["finetune", "ewc", "er", "joint"]:
        res[m] = acc_matrix_linear(Xtr, ytr, Xte, yte, tasks, cls2task, m)

    print(f"{'method':>14} | {'final acc':>9} | {'avg-inc':>7} | {'forgetting':>10}")
    out = {}
    for k, R in res.items():
        fa, aia, fg = metrics(R)
        out[k] = dict(final=round(fa, 4), avg_inc=round(aia, 4), forget=round(fg, 4))
        print(f"{k:>14} | {fa:>9.3f} | {aia:>7.3f} | {fg:>10.3f}")
    json.dump({"seed": SEED, "results": out},
              io.open(os.path.join(HERE, f"cl_result_seed{SEED}.json"), "w"), indent=1)
    print("\nfinal acc = class-incremental accuracy on all 100 classes after task 10; "
          "forgetting lower=better. NCM (ours) is replay-free + training-free.")


if __name__ == "__main__":
    main()
