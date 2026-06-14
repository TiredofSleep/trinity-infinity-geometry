"""study_loop.py -- the unfrozen agent, run long. It measures itself, keeps
iterating, persists across restarts, and posts its progress to GitHub.

Experience source: dozens of Wikipedia categories (human-curated truth -- the
"counterpart" teacher), fetched live. A large many-way task so there is genuinely
new experience to learn from for a long time. Perception: MiniLM on the GPU.

Each session: pull a fresh batch, predict in the algorithm-language, get feedback,
learn online (grow per-class vocabulary + Hedge over [prior, grown-memory]),
measure held-out accuracy, log, and every PUSH_EVERY sessions git-commit+push the
log and figure. State persists to disk, so killing and relaunching resumes.

  python study_loop.py            # runs MAXSESS sessions then exits (resumable)

Honest: meaningful learning is bounded by how much NEW experience exists; this
covers a large category space and is built to run indefinitely as data grows.
"""
import io
import json
import os
import re
import subprocess
import time
import urllib.parse
import urllib.request

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

HERE = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(HERE, "study_pool.json")
EMB = os.path.join(HERE, "study_embed.npz")
STATE = os.path.join(HERE, "study_state.npz")
LOG = os.path.join(HERE, "study_log.jsonl")
UA = {"User-Agent": "RulerSpectraResearch/1.0 (github TiredofSleep/trinity-infinity-geometry)"}
BATCH, ETA, GROW, MAXPC = 64, 0.6, 0.55, 10
MAXSESS, PUSH_EVERY = 300, 30
CATS = [
    "Thermodynamics", "Electromagnetism", "Particle physics", "Number theory",
    "Abstract algebra", "Elementary geometry", "Information theory", "Optics",
    "Quantum mechanics", "Organic chemistry", "Mammals", "Birds", "Trees",
    "Insects", "Musical instruments", "Dances", "Martial arts", "Greek mythology",
    "Economics", "Linguistics", "Chemical elements", "Constellations",
    "Programming languages", "Gemstones", "Sports",
]
DROP = re.compile(r"\b(List|Glossary|Timeline|Index|Journal|Prize|Award|History|"
                  r"Introduction|Proofs?|Outline|Comparison|Society|Foundation|"
                  r"Project|Conference)\b", re.I)

_dev = "cuda" if torch.cuda.is_available() else "cpu"
_tok = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2", local_files_only=True)
_mdl = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2", local_files_only=True).eval().to(_dev)


def embed(texts, bs=512):
    out = []
    for i in range(0, len(texts), bs):
        b = _tok(texts[i:i + bs], padding=True, truncation=True, max_length=32, return_tensors="pt").to(_dev)
        with torch.no_grad():
            o = _mdl(**b).last_hidden_state
        m = b["attention_mask"].unsqueeze(-1).float()
        v = (o * m).sum(1) / m.sum(1).clamp(min=1)
        v = torch.nn.functional.normalize(v, dim=1)
        out.append(v.cpu().numpy())
    return np.vstack(out).astype(np.float32)


def _members(cat, cap, types):
    out, cont = [], None
    while len(out) < cap:
        u = ("https://en.wikipedia.org/w/api.php?action=query&list=categorymembers"
             f"&cmtitle=Category:{urllib.parse.quote(cat)}&cmtype={types}"
             "&cmprop=title|type&cmlimit=500&format=json")
        if cont:
            u += "&cmcontinue=" + urllib.parse.quote(cont)
        d = None
        for attempt in range(3):                       # polite retry on throttle
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
                break
            except Exception:
                time.sleep(1.5 * (attempt + 1))
        if d is None:
            break
        out += [(m["title"], m.get("type", "page")) for m in d["query"]["categorymembers"]]
        cont = d.get("continue", {}).get("cmcontinue")
        time.sleep(0.4)                                # rate-limit: be a good citizen
        if not cont:
            break
    return out


def fetch(cat, cap=400):
    """Direct pages plus pages from a few subcategories -- so broad categories
    (Mammals, Musical instruments) that hold mostly subcats still yield terms."""
    ms = _members(cat, cap, "page|subcat")
    pages = [t for t, ty in ms if ty == "page"]
    subcats = [t.split(":", 1)[1] for t, ty in ms if ty == "subcat"]
    for sc in subcats[:5]:                             # cap fan-out to avoid throttle
        if len(pages) >= cap:
            break
        pages += [t for t, _ in _members(sc, 80, "page")]
    return pages[:cap]


def clean(t):
    t = re.sub(r"\s*\(.*?\)", "", t).strip()
    if not t or DROP.search(t):
        return None
    toks = t.split()
    if len(toks) > 4 or (len(toks) <= 3 and all(w[:1].isupper() for w in toks)):
        return None
    return t


def build_pool():
    if os.path.exists(POOL) and os.path.exists(EMB):
        d = json.load(io.open(POOL, encoding="utf-8"))
        e = np.load(EMB)
        return d["terms"], np.array(d["y"]), d["names"], e["E"], e["A"]
    raw = {}
    for c in CATS:
        raw[c] = [x for x in (clean(t) for t in fetch(c)) if x]
        print(f"  fetched {c}: {len(raw[c])}", flush=True)
    seen = {}
    for c in CATS:
        for t in set(raw[c]):
            seen.setdefault(t.lower(), []).append(c)
    terms, y = [], []
    for ci, c in enumerate(CATS):
        for t in sorted(set(raw[c])):
            if len(seen[t.lower()]) == 1:
                terms.append(t); y.append(ci)
    E = embed(terms)
    A = embed(CATS)
    json.dump({"terms": terms, "y": y, "names": CATS}, io.open(POOL, "w", encoding="utf-8"))
    np.savez(EMB, E=E, A=A)
    print(f"  pool: {len(terms)} terms, {len(CATS)} categories, dim {E.shape[1]}, device {_dev}", flush=True)
    return terms, np.array(y), CATS, E, A


def zr(S):
    return (S - S.mean(1, keepdims=True)) / (S.std(1, keepdims=True) + 1e-9)


def proto_scores(X, protos, plabel, C):
    s = np.full((len(X), C), -1.0, np.float32)
    if len(protos):
        sim = X @ protos.T
        for c in range(C):
            m = plabel == c
            if m.any():
                s[:, c] = sim[:, m].max(1)
    return s


def push(msg):
    try:
        subprocess.run(["git", "-C", os.path.join(HERE, "..", ".."), "add",
                        "10_extensions/language-as-measurement/study_log.jsonl",
                        "10_extensions/language-as-measurement/study_figure.svg"],
                       check=False, capture_output=True, timeout=60)
        subprocess.run(["git", "-C", os.path.join(HERE, "..", ".."), "commit", "-q", "-m", msg],
                       check=False, capture_output=True, timeout=60)
        r = subprocess.run(["git", "-C", os.path.join(HERE, "..", ".."), "push", "origin", "main"],
                           check=False, capture_output=True, timeout=120)
        print(f"  pushed: {'ok' if r.returncode == 0 else r.stderr.decode()[:80]}", flush=True)
    except Exception as e:
        print(f"  push failed: {e}", flush=True)


def figure(rows):
    xs = [r["session"] for r in rows]
    acc = [r["test_acc"] for r in rows]
    anc = [r["test_acc_anchor_only"] for r in rows]
    if len(xs) < 2:
        return
    x0, x1, yt, yb = 80, 640, 90, 320
    lo, hi = min(anc + acc) - 0.03, max(anc + acc) + 0.03
    def X(i): return x0 + i / (len(xs) - 1) * (x1 - x0)
    def Y(a): return yb - (a - lo) / (hi - lo + 1e-9) * (yb - yt)
    def pl(v, col, w=2):
        p = " ".join(f"{X(i):.1f},{Y(a):.1f}" for i, a in enumerate(v))
        return f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{w}"/>'
    svg = (f'<svg width="100%" viewBox="0 0 680 380" role="img" xmlns="http://www.w3.org/2000/svg">'
           f'<title>Unfrozen study loop</title><desc>Held-out accuracy across sessions.</desc>'
           f'<text x="40" y="30" class="th">unfrozen study loop — {len(CATS)}-way, '
           f'{rows[-1]["lived_experiences"]} experiences lived, session {xs[-1]}</text>'
           f'<text x="40" y="50" class="ts">held-out test accuracy across persistent self-measured sessions; frozen prior is flat</text>'
           f'{pl(anc, "#D85A30")}{pl(acc, "#444441", 3)}'
           f'<circle cx="80" cy="356" r="4" fill="#D85A30"/><text x="90" y="360" class="ts">frozen prior</text>'
           f'<circle cx="240" cy="356" r="4" fill="#444441"/><text x="250" y="360" class="ts">unfrozen agent (current {acc[-1]:.3f})</text>'
           f'</svg>')
    io.open(os.path.join(HERE, "study_figure.svg"), "w", encoding="utf-8").write(svg)


def main():
    print("building experience pool (Wikipedia categories)...", flush=True)
    terms, y, names, E, A = build_pool()
    C = len(names)
    rng = np.random.default_rng(7)
    perm = rng.permutation(len(terms))
    ntest = int(len(terms) * 0.2)
    test, train = perm[:ntest], perm[ntest:]

    if os.path.exists(STATE):
        s = np.load(STATE, allow_pickle=True)
        protos, plabel, pcount = s["protos"], s["plabel"], s["pcount"]
        w, consumed, sess = s["w"], int(s["consumed"]), int(s["sess"])
    else:
        protos = np.zeros((0, E.shape[1]), np.float32); plabel = np.zeros(0, int)
        pcount = np.zeros(0); w = np.ones(2) / 2; consumed = 0; sess = 0

    rows = [json.loads(l) for l in io.open(LOG, encoding="utf-8")] if os.path.exists(LOG) else []
    for _ in range(MAXSESS):
        batch = [train[(consumed + i) % len(train)] for i in range(BATCH)]
        grew = 0
        for i in batch:
            x, yy = E[i], y[i]
            a_pred = int((A @ x).argmax())
            psc = proto_scores(x[None], protos, plabel, C)[0]
            p_pred = int(psc.argmax()) if len(protos) else -1
            loss = np.array([1.0 - (a_pred == yy), 1.0 - (p_pred == yy)])
            w = w * np.exp(-ETA * loss); w = w / w.sum()
            m = plabel == yy
            if not m.any() or (protos[m] @ x).max() < GROW and m.sum() < MAXPC:
                protos = np.vstack([protos, x]); plabel = np.append(plabel, yy)
                pcount = np.append(pcount, 1.0); grew += 1
            else:
                gi = np.where(m)[0][int((protos[m] @ x).argmax())]
                protos[gi] = (protos[gi] * pcount[gi] + x)
                protos[gi] /= (np.linalg.norm(protos[gi]) + 1e-9); pcount[gi] += 1
        za, zp = zr(E[test] @ A.T), zr(proto_scores(E[test], protos, plabel, C))
        acc = float(((w[0] * za + w[1] * zp).argmax(1) == y[test]).mean())
        acc_a = float((za.argmax(1) == y[test]).mean())
        consumed += BATCH; sess += 1
        rec = dict(session=sess, lived_experiences=consumed, test_acc=round(acc, 4),
                   test_acc_anchor_only=round(acc_a, 4), vocab=int(len(protos)),
                   grew=grew, w_anchor=round(float(w[0]), 3), w_proto=round(float(w[1]), 3))
        rows.append(rec)
        io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec) + "\n")
        np.savez(STATE, protos=protos, plabel=plabel, pcount=pcount, w=w, consumed=consumed, sess=sess)
        print(f"s{sess}: lived {consumed} test {acc:.3f} (prior {acc_a:.3f}) "
              f"vocab {len(protos)} trust a{w[0]:.2f}/p{w[1]:.2f}", flush=True)
        if sess % PUSH_EVERY == 0:
            figure(rows)
            push(f"study loop: session {sess}, {consumed} lived, test {acc:.3f} (prior {acc_a:.3f}) [auto]")
    figure(rows)
    push(f"study loop: session {sess} final, test {rows[-1]['test_acc']:.3f} [auto]")
    print("done (resumable: relaunch to continue)", flush=True)


if __name__ == "__main__":
    main()
