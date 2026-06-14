"""curriculum_ab.py -- does an easy->hard CURRICULUM teach faster than random
order? Competence-based curriculum (Platanios 2019): rank windows by difficulty
(mean token rarity -log p(token)), and at step t only sample from the easiest
competence(t) fraction, competence growing 0.2 -> 1.0 on a sqrt schedule. Same
3-layer model, same Muon optimizer, same val; only the data ORDER differs.

  python curriculum_ab.py curriculum
  python curriculum_ab.py shuffled

Registered: curriculum reaches lower val ppl at matched steps (esp. early).
Kill: curriculum <= shuffled -> ordering gives nothing here; honest negative.
"""
import io
import json
import math
import os
import sys

import numpy as np
import torch
import torch.nn.functional as F

from train_ab import GPT, DEV, VOCAB, CTX, MICROBS, ACCUM, data, N
from muon import Muon, split_params

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "curriculum_log.jsonl")
MODE = sys.argv[1] if len(sys.argv) > 1 else "curriculum"
STEPS, EVAL, WARMUP, C0, NPOOL = 1800, 150, 100, 0.2, 20000
torch.manual_seed(7)
rng = np.random.default_rng(0)

# difficulty = mean token rarity over a 128-token prefix of each candidate window
samp = np.asarray(data[:5_000_000], dtype=np.int64)
freq = np.bincount(samp, minlength=VOCAB).astype(np.float64)
freq /= freq.sum()
rar = -np.log(freq + 1e-9)                       # surprisal per token id
starts = rng.integers(0, N - CTX - 1, NPOOL)
diff = np.array([rar[np.asarray(data[s:s + 128], dtype=np.int64)].mean() for s in starts])
order = starts[np.argsort(diff)]                 # easy (common words) -> hard (rare)


def competence(t):
    return min(1.0, math.sqrt(t / STEPS * (1 - C0 ** 2) + C0 ** 2))


def make_batch(step):
    if MODE == "curriculum":
        k = max(MICROBS, int(competence(step) * NPOOL))
        idx = rng.integers(0, k, MICROBS)
        s = order[idx]
    else:
        s = order[rng.integers(0, NPOOL, MICROBS)]
    x = torch.stack([torch.from_numpy(np.asarray(data[i:i + CTX], dtype=np.int64)) for i in s])
    y = torch.stack([torch.from_numpy(np.asarray(data[i + 1:i + CTX + 1], dtype=np.int64)) for i in s])
    return x.to(DEV), y.to(DEV)


def main():
    model = GPT().to(DEV)
    mp, ap = split_params(model)
    opts = [Muon(mp, lr=0.02, momentum=0.95),
            torch.optim.AdamW(ap, lr=5e-4, betas=(0.9, 0.95), weight_decay=0.1)]
    blrs = [0.02, 5e-4]
    vg = torch.Generator().manual_seed(999)
    val = []
    for _ in range(16):
        vs = torch.randint(0, N - CTX - 1, (MICROBS,), generator=vg)
        x = torch.stack([torch.from_numpy(np.asarray(data[i:i + CTX], dtype=np.int64)) for i in vs])
        y = torch.stack([torch.from_numpy(np.asarray(data[i + 1:i + CTX + 1], dtype=np.int64)) for i in vs])
        val.append((x.to(DEV), y.to(DEV)))

    def evaluate():
        model.eval(); ls = []
        with torch.no_grad():
            for x, y in val:
                with torch.autocast("cuda", dtype=torch.bfloat16):
                    ls.append(F.cross_entropy(model(x).view(-1, VOCAB), y.view(-1)).item())
        model.train(); return float(np.exp(np.mean(ls)))

    print(f"[{MODE}] starting, pool {NPOOL}, Muon", flush=True)
    for step in range(1, STEPS + 1):
        sc = min(1.0, step / WARMUP)
        for o, blr in zip(opts, blrs):
            for g in o.param_groups:
                g["lr"] = blr * sc
        for o in opts:
            o.zero_grad(set_to_none=True)
        for _ in range(ACCUM):
            x, y = make_batch(step)
            with torch.autocast("cuda", dtype=torch.bfloat16):
                loss = F.cross_entropy(model(x).view(-1, VOCAB), y.view(-1)) / ACCUM
            loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        for o in opts:
            o.step()
        if step % EVAL == 0:
            ppl = evaluate()
            io.open(LOG, "a", encoding="utf-8").write(json.dumps(dict(mode=MODE, step=step, val_ppl=round(ppl, 2))) + "\n")
            print(f"[{MODE}] step {step} ppl {ppl:.2f} (competence {competence(step):.2f})", flush=True)


if __name__ == "__main__":
    main()
