"""unfrozen.py -- a continually-learning agent that does NOT get frozen.

One invocation = one study session. The agent LOADS its prior state from disk,
studies a fresh batch of experience (it never resets), GROWS its own vocabulary
when its current words don't fit, evaluates on a fixed held-out test set, SAVES
its state, and APPENDS the session to a log. Run it again tomorrow and it keeps
going from where it was -- the opposite of trained-then-frozen.

  state     : unfrozen_state.npz   (prototypes, their classes, Hedge weights,
                                     how much experience it has lived)
  log       : unfrozen_log.jsonl   (one line per session -> the merit record)
  AI in loop: MiniLM embeds the experience (perception); the agent learns online.

  vocabulary growth: each class is represented by sub-prototypes ("words"). When
  an experience is far from all of its class's words, the agent COINS A NEW WORD
  (adds a sub-prototype) instead of blurring an old one. Capacity grows to fit
  the manifold; the language expands from experience.

  python unfrozen.py        # run once per session; run repeatedly to accumulate

merit = held-out test accuracy rising across sessions as lived experience grows.
"""
import io
import json
import os
import numpy as np

from embed import embed
from spectra import RULERS

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "unfrozen_state.npz")
LOG = os.path.join(HERE, "unfrozen_log.jsonl")
CACHE = os.path.join(HERE, "unfrozen_cache.npz")
BATCH, ETA, GROW, MAXPC = 43, 0.6, 0.55, 6


def nrm(X):
    return X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-9)


def zr(S):
    return (S - S.mean(1, keepdims=True)) / (S.std(1, keepdims=True) + 1e-9)


def load_pool():
    names = list(RULERS)
    terms, y = [], []
    pr = json.load(io.open(os.path.join(HERE, "validate2_helper.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(HERE, "validate2_helper.json")) else None
    from validate2 import PROBE
    for c, d in enumerate(names):
        for w in PROBE[d]:
            terms.append(w); y.append(c)
    ext = json.load(io.open(os.path.join(HERE, "external_terms.json"), encoding="utf-8"))
    for c, d in enumerate(names):
        for w in ext.get(d, []):
            terms.append(w); y.append(c)
    return terms, np.array(y), names


def get_embeddings(terms):
    if os.path.exists(CACHE):
        d = np.load(CACHE, allow_pickle=True)
        if len(d["terms"]) == len(terms) and list(d["terms"]) == terms:
            return d["E"], d["A"]
    E = nrm(embed(terms))
    A = nrm(embed([RULERS[d] for d in RULERS]))
    np.savez(CACHE, terms=np.array(terms, object), E=E, A=A)
    return E, A


def proto_scores(X, protos, plabel, C):
    s = np.full((len(X), C), -1.0)
    if len(protos):
        sim = X @ protos.T
        for c in range(C):
            m = plabel == c
            if m.any():
                s[:, c] = sim[:, m].max(1)
    return s


def main():
    terms, y, names = load_pool()
    C = len(names)
    E, A = get_embeddings(terms)
    n = len(terms)
    rng = np.random.default_rng(7)
    perm = rng.permutation(n)
    ntest = int(n * 0.3)
    test, train = perm[:ntest], perm[ntest:]                 # fixed split

    if os.path.exists(STATE):
        s = np.load(STATE, allow_pickle=True)
        protos = s["protos"]; plabel = s["plabel"]; pcount = s["pcount"]
        w = s["w"]; consumed = int(s["consumed"]); sess = int(s["sess"])
    else:
        protos = np.zeros((0, E.shape[1])); plabel = np.zeros(0, int)
        pcount = np.zeros(0); w = np.ones(2) / 2; consumed = 0; sess = 0

    # this session's fresh batch (advance through the train pool, wrapping)
    batch = [train[(consumed + i) % len(train)] for i in range(BATCH)]
    grew = 0
    for i in batch:
        x, yy = E[i], y[i]
        a_pred = int((A @ x).argmax())
        psc = proto_scores(x[None], protos, plabel, C)[0]
        p_pred = int(psc.argmax()) if len(protos) else -1
        loss = np.array([1.0 - (a_pred == yy), 1.0 - (p_pred == yy)])
        w = w * np.exp(-ETA * loss); w = w / w.sum()         # learn what to trust
        # grow / update the vocabulary for class yy
        m = plabel == yy
        if not m.any():
            protos = np.vstack([protos, x]); plabel = np.append(plabel, yy)
            pcount = np.append(pcount, 1.0); grew += 1
        else:
            sims = protos[m] @ x
            if sims.max() < GROW and m.sum() < MAXPC:
                protos = np.vstack([protos, x]); plabel = np.append(plabel, yy)
                pcount = np.append(pcount, 1.0); grew += 1
            else:
                gi = np.where(m)[0][int(sims.argmax())]
                protos[gi] = nrm((protos[gi] * pcount[gi] + x)[None])[0]
                pcount[gi] += 1

    # evaluate on the fixed held-out test set
    za = zr(E[test] @ A.T)
    zp = zr(proto_scores(E[test], protos, plabel, C))
    comb = w[0] * za + w[1] * zp
    acc = float((comb.argmax(1) == y[test]).mean())
    acc_anchor = float((za.argmax(1) == y[test]).mean())

    consumed += BATCH; sess += 1
    np.savez(STATE, protos=protos, plabel=plabel, pcount=pcount, w=w,
             consumed=consumed, sess=sess)
    rec = dict(session=sess, lived_experiences=consumed, test_acc=round(acc, 4),
               test_acc_anchor_only=round(acc_anchor, 4), vocab=int(len(protos)),
               grew_this_session=grew, w_anchor=round(float(w[0]), 3),
               w_proto=round(float(w[1]), 3))
    with io.open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"session {sess}: lived {consumed} | test {acc:.3f} "
          f"(anchor-only {acc_anchor:.3f}) | vocab {len(protos)} (+{grew}) | "
          f"trust anchor {w[0]:.2f}/proto {w[1]:.2f}")


if __name__ == "__main__":
    main()
