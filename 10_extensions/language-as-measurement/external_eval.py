"""external_eval.py -- replicate the few-shot win on EXTERNAL, non-author-chosen
terms: Wikipedia category membership (curated by Wikipedia editors, labelled by
category), fetched live from the MediaWiki API. Removes the "you picked the
words" objection -- the terms and labels are not ours.

Same method as validate3 (text-anchored prototypes vs data-only). If the algebra
prior still beats the data-only baseline at low k on terms we never chose, the
result holds externally.

  python external_eval.py
"""
import json
import os
import re
import urllib.parse
import urllib.request
import numpy as np

from embed import embed
from spectra import harvest, RULERS, ruler_dirs

UA = {"User-Agent": "RulerSpectraResearch/1.0 (research; github TiredofSleep/trinity-infinity-geometry)"}
CATS = {                                   # ruler -> Wikipedia category
    "thermodynamics": "Thermodynamics",
    "electromagnetism": "Electromagnetism",
    "wave mechanics": "Waves",
    "particle physics": "Particle physics",
    "information theory": "Information theory",
    "geometry": "Elementary geometry",
    "number theory": "Number theory",
    "algebra": "Abstract algebra",
}
DROP = re.compile(r"\b(List|Glossary|Timeline|Index|Journal|Prize|Award|Conference|"
                  r"Seminar|History|Introduction|Proofs?|Outline|Comparison|Society|"
                  r"Foundation|Project|Theorem of|Notation)\b", re.I)


def fetch(cat, cap=500):
    out, cont = [], None
    while len(out) < cap:
        u = ("https://en.wikipedia.org/w/api.php?action=query&list=categorymembers"
             f"&cmtitle=Category:{urllib.parse.quote(cat)}&cmtype=page&cmlimit=500&format=json")
        if cont:
            u += "&cmcontinue=" + urllib.parse.quote(cont)
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
        out += [m["title"] for m in d["query"]["categorymembers"]]
        cont = d.get("continue", {}).get("cmcontinue")
        if not cont:
            break
    return out


def clean(title):
    t = re.sub(r"\s*\(.*?\)", "", title).strip()      # strip parenthetical
    if DROP.search(t) or not t:
        return None
    toks = t.split()
    if len(toks) > 4:
        return None
    if len(toks) <= 3 and all(w[:1].isupper() for w in toks):  # proper noun / person
        return None
    return t


def nrm(X):
    return X / (np.linalg.norm(X, axis=-1, keepdims=True) + 1e-9)


def main(root):
    names = list(RULERS)
    raw = {}
    for d in names:
        raw[d] = [c for c in (clean(t) for t in fetch(CATS[d])) if c]
        print(f"  {d:>18}: {len(raw[d])} usable terms from Category:{CATS[d]}")
    # dedupe across rulers: keep only unambiguous (single-category) terms
    seen = {}
    for d in names:
        for t in set(raw[d]):
            seen.setdefault(t.lower(), []).append(d)
    keep = {d: [t for t in sorted(set(raw[d])) if len(seen[t.lower()]) == 1] for d in names}
    n = min(len(keep[d]) for d in names)
    N = min(n, 30)
    rng = np.random.default_rng(0)
    terms, y = [], []
    for c, d in enumerate(names):
        pick = list(rng.permutation(keep[d])[:N])
        terms += pick; y += [c] * len(pick)
    y = np.array(y); C = len(names)
    print(f"\nbalanced external set: {N}/domain x {C} = {len(terms)} terms "
          f"(unambiguous, Wikipedia-labelled)\n")
    json.dump({names[c]: [terms[i] for i in range(len(terms)) if y[i] == c]
               for c in range(C)}, open("external_terms.json", "w"), indent=1)

    # ---- same pipeline as validate2/3
    pool, _ = harvest(root)
    Epool = embed(pool)
    E = nrm(embed(terms))
    A = nrm(embed([RULERS[d] for d in names]))            # description anchors
    _, U = ruler_dirs(pool, Epool)
    Rp = Epool @ U.T; mu, sd = Rp.mean(0), Rp.std(0) + 1e-9
    zs = float(((((E @ U.T) - mu) / sd).argmax(1) == y).mean())   # zero-shot ruler

    KS = [1, 2, 3, 5]
    idx = [np.where(y == c)[0] for c in range(C)]
    agg = {a: {k: 0.0 for k in KS} for a in (0.0, 0.5, 1.0)}
    TR = 100
    for t in range(TR):
        r = np.random.default_rng(3000 + t)
        for k in KS:
            tr, te = [], []
            for c in range(C):
                p = r.permutation(idx[c]); tr.append(p[:k]); te += list(p[k:])
            te = np.array(te); yte = y[te]
            means = nrm(np.array([E[tr[c]].mean(0) for c in range(C)]))
            for a in (0.0, 0.5, 1.0):
                proto = nrm(a * A + (1 - a) * means)
                agg[a][k] += float(((E[te] @ proto.T).argmax(1) == yte).mean())
    for a in agg:
        for k in KS:
            agg[a][k] /= TR

    print(f"EXTERNAL test | chance {1/C:.3f} | zero-shot ruler = {zs:.3f}")
    print(f"  {'method':>26} | " + "  ".join(f"k={k}" for k in KS))
    lbl = {0.0: "data-only (baseline)", 0.5: "algebra+data (ours)",
           1.0: "description-only (0 ex)"}
    for a in (0.0, 0.5, 1.0):
        print(f"  {lbl[a]:>26} | " + "  ".join(f"{agg[a][k]:.3f}" for k in KS))

    lo = [k for k in KS if k <= 3]
    win = all(agg[0.5][k] > agg[0.0][k] for k in lo)
    gain = np.mean([agg[0.5][k] - agg[0.0][k] for k in lo])
    print("\n" + "=" * 64)
    if win:
        print(f"  REPLICATES ON EXTERNAL TERMS: algebra+data beats data-only at "
              f"every k<=3, mean +{gain:.3f}.")
        print(f"    k=1: {agg[0.0][1]:.3f} -> {agg[0.5][1]:.3f} "
              f"(+{agg[0.5][1]-agg[0.0][1]:.3f}); description-only (0 labels) = "
              f"{agg[1.0][1]:.3f}. The win is not an artifact of our word list.")
    else:
        print(f"  DOES NOT replicate cleanly (mean {gain:+.3f} at k<=3) -- honest.")
    print("=" * 64)
    json.dump({"zero_shot": zs, "ks": KS, "N_per_domain": N,
               "curves": {str(a): {str(k): agg[a][k] for k in KS} for a in agg}},
              open("external_result.json", "w"), indent=1)


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
