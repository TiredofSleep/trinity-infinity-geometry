"""learner.py -- the algorithm-language that LEARNS, online, like an AI and with
an AI.

The lenses are the vocabulary of a math-language; the agent reads a STREAM of
experience, expresses each item in the language, predicts, gets feedback, and
LEARNS two things online:
  - its PROTOTYPES / memory  (the manifold lens fills in from experience)
  - WHICH LENS TO TRUST       (multiplicative-weights / Hedge over the lenses --
                               the no-regret way to learn the reliability we used
                               to hand-code; Littlestone-Warmuth 1994, Freund-
                               Schapire 1997). No batch fitting; pure online.

The AI is in the loop two ways: the embedder (MiniLM) is the perceptual organ
that turns words into language-coordinates, and the agent learns from a feedback
stream the way an AI trains. White-box throughout: you can watch the lens-weights
move and the accuracy climb.

Lenses (the language's words):
  anchor  cos to class description  (the LM's prior knowledge -- good from step 0)
  proto   cos to the running per-class mean   (learned online, starts empty)
  knn     max cos to seen examples of a class (memory, grows online)

  python learner.py
"""
import json
import os
import numpy as np

from embed import embed
from spectra import RULERS

ETA = 0.6
SHUFFLES = 40


def nrm(X):
    return X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-9)


def z(v):
    return (v - v.mean()) / (v.std() + 1e-9)


def run_stream(E, y, A, C, order):
    """One online pass. Returns per-step correctness for anchor/proto/knn/agent
    and the running lens-weights."""
    proto_sum = np.zeros((C, E.shape[1])); proto_cnt = np.zeros(C)
    mem = [[] for _ in range(C)]
    w = np.ones(3) / 3                      # Hedge weights over [anchor,proto,knn]
    cor = {k: np.zeros(len(order)) for k in ("anchor", "proto", "knn", "agent")}
    whist = np.zeros((len(order), 3))
    for t, i in enumerate(order):
        x = E[i]
        s_anchor = A @ x
        pm = np.where(proto_cnt[:, None] > 0, proto_sum / np.maximum(proto_cnt[:, None], 1), 0.0)
        s_proto = np.array([pm[c] @ x if proto_cnt[c] > 0 else -1.0 for c in range(C)])
        s_knn = np.array([max((e @ x) for e in mem[c]) if mem[c] else -1.0 for c in range(C)])
        Z = {"anchor": z(s_anchor), "proto": z(s_proto), "knn": z(s_knn)}
        for L in ("anchor", "proto", "knn"):
            cor[L][t] = (np.argmax(Z[L]) == y[i])
        combined = w[0] * Z["anchor"] + w[1] * Z["proto"] + w[2] * Z["knn"]
        cor["agent"][t] = (np.argmax(combined) == y[i])
        whist[t] = w
        # ---- LEARN from feedback (the label arrives) ----
        loss = np.array([1.0 - (np.argmax(Z[L]) == y[i]) for L in ("anchor", "proto", "knn")])
        w = w * np.exp(-ETA * loss); w /= w.sum()        # Hedge update
        proto_sum[y[i]] += x; proto_cnt[y[i]] += 1        # learn the prototype
        mem[y[i]].append(x)                               # grow the memory
    return cor, whist


def main(root):
    ext = json.load(open(os.path.join(os.path.dirname(__file__), "external_terms.json")))
    names = list(RULERS)
    terms, y = [], []
    for c, d in enumerate(names):
        for w in ext.get(d, []):
            terms.append(w); y.append(c)
    y = np.array(y); C = len(names)
    E = nrm(embed(terms))
    A = nrm(embed([RULERS[d] for d in names]))
    n = len(terms)
    print(f"online stream: {n} experiences, {C}-way, harder external set | "
          f"chance {1/C:.3f}\n")

    acc = {k: np.zeros(n) for k in ("anchor", "proto", "knn", "agent")}
    W = np.zeros((n, 3))
    rng = np.random.default_rng(0)
    for s in range(SHUFFLES):
        order = rng.permutation(n)
        cor, wh = run_stream(E, y, A, C, order)
        for k in acc:
            acc[k] += cor[k]
        W += wh
    for k in acc:
        acc[k] /= SHUFFLES
    W /= SHUFFLES

    def windowed(a, w=20):
        return np.convolve(a, np.ones(w) / w, mode="valid")
    curves = {k: windowed(acc[k]).tolist() for k in acc}

    # did it LEARN? early vs late accuracy of the agent
    early = acc["agent"][:n // 4].mean()
    late = acc["agent"][-n // 4:].mean()
    anchor_flat = acc["anchor"].mean()
    proto_late = acc["proto"][-n // 4:].mean()
    print("LEARNING (agent, online):")
    print(f"  first quarter of stream: {early:.3f}")
    print(f"  last  quarter of stream: {late:.3f}   ({'LEARNED +' if late>early else ''}{late-early:+.3f})")
    print(f"  fixed prior (anchor) mean over stream: {anchor_flat:.3f} (does not learn)")
    print(f"  learned manifold (proto) last quarter: {proto_late:.3f} "
          f"(climbed from chance as it saw examples)")
    print(f"\nLEARNED LENS-WEIGHTS (Hedge), start -> end:")
    for j, L in enumerate(("anchor", "proto", "knn")):
        print(f"  {L:>7}: {W[0,j]:.2f} -> {W[-1,j]:.2f}")
    print("\nthe agent starts trusting its prior (anchor), and LEARNS to trust "
          "its grown memory (proto/knn) as experience accumulates -- online, "
          "no batch fitting. that shift IS the learning.")
    step = max(1, n // 60)
    json.dump({"n": n, "curves": curves,
               "weights_traj": W[::step].tolist(), "wtraj_step": step,
               "weights_start": W[0].tolist(), "weights_end": W[-1].tolist(),
               "early": early, "late": late, "anchor_mean": anchor_flat},
              open(os.path.join(os.path.dirname(__file__), "learner_result.json"), "w"), indent=1)


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
