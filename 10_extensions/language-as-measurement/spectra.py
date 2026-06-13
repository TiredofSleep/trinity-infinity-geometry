"""spectra.py -- Ruler Spectra: meaning as a spectrum across rulers.

  Idea (Claude, Opus 4.8, with Brayden, 2026-06-13):
  A concept's meaning is not a point. It is the SPECTRUM of how it answers to a
  chosen set of rulers. The designer chooses the rulers -- the axes of the
  language. The designer does NOT sort concepts into domains and does NOT decide
  the crossings. You hand the system a pool of words from real text, never sorted
  against these rulers, and the geometry decides:
    - a concept's HOME is the ruler it answers to most  -> distinguishings emerge
    - a CROSSING is a concept that answers to two rulers -> crossings emerge
  We design the apparatus; the model fills it in. Today the embedder (MiniLM) is
  the stand-in ruler-maker; tomorrow each ruler is its own unfrozen LM and this
  same protocol stitches them. No ruler is privileged; the value is the layered,
  comparable spectrum.

  python spectra.py                # harvest pool from the repo's own prose
  python spectra.py <dir> <top_n>
"""
import os
import re
import sys
from collections import Counter

import numpy as np

from embed import embed

# The rulers = the axes of the language (designer-chosen). Anchors DESCRIBE each
# domain without naming the bridge-words we hope to discover -- so crossings are
# the model's call, not ours.
RULERS = {
    "thermodynamics":     "the physics of heat, energy and entropy",
    "electromagnetism":   "electricity, magnetism, charge and current",
    "wave mechanics":     "waves, vibration, frequency and oscillation",
    "particle physics":   "elementary particles and their interactions",
    "information theory": "information, coding and communication",
    "geometry":           "shapes, space, distance and curvature",
    "number theory":      "integers, primes and divisibility",
    "algebra":            "groups, rings and abstract structure",
}

STOP = set("""the a an and or of to in is are was were be been being it its this that these those
for on at by with from as into than then so but not no yes if else we you they he she them his her
their our your can will would could should may might must have has had do does did done make made
which who whom whose what when where why how all any some each every both few more most other such
only own same very just also too then once here there about above below up down out off over under
again further while because until against between through during before after one two three four
five six seven eight nine ten first second third new old see use used using let lets get got like
many much such per via etc eg ie vs within without across among along around upon since thus hence
given case form note set let figure table section paper result results value values number numbers
physics physical mathematics mathematical math theory theoretical theories dynamics dynamic
structure structures structural structurally abstract framework frameworks approach approaches
analysis concept concepts notion notions general generic study studies understanding work works
idea ideas thing things way ways part parts kind sort level levels term terms point points fact
facts area areas topic context sense view based model models modeling system systems systemic
science scientific nature natural property properties object objects method methods process
processes principle principles example examples problem problems question questions different
follows following defined define definition standard simple complex various related specific
""".split())


def harvest(root, top_n=320):
    """Harvest an unsorted concept pool from real prose in the repo."""
    cnt = Counter()
    files = 0
    for dp, _, fns in os.walk(root):
        if ".git" in dp:
            continue
        for fn in fns:
            if not fn.endswith((".md", ".tex", ".txt")):
                continue
            try:
                txt = open(os.path.join(dp, fn), encoding="utf-8",
                           errors="ignore").read()
            except OSError:
                continue
            files += 1
            for w in re.findall(r"[a-z]{4,}", txt.lower()):
                if w not in STOP:
                    cnt[w] += 1
            if files > 600:
                break
    pool = [w for w, _ in cnt.most_common(top_n)]
    return pool, files


def ruler_dirs(pool, Epool, seed_k=12):
    """Each ruler direction = anchor + its nearest pool words (a region the ruler
    discovers from the pool, not a list we authored)."""
    names = list(RULERS)
    Eanc = embed([RULERS[n] for n in names])
    U = []
    for d in range(len(names)):
        sims = Epool @ Eanc[d]
        seed = Epool[np.argsort(sims)[-seed_k:]]
        u = (Eanc[d] + seed.mean(0))
        U.append(u / (np.linalg.norm(u) + 1e-12))
    return names, np.array(U)


def spectra(Epool, U):
    """Per-ruler response, z-scored across the pool so rulers are comparable."""
    R = Epool @ U.T                       # (n_pool, n_rulers) cosine response
    Z = (R - R.mean(0)) / (R.std(0) + 1e-12)
    return Z


def main(root, top_n):
    pool, files = harvest(root, top_n)
    print(f"harvested {len(pool)} concepts from {files} files of real prose "
          f"(unsorted against the rulers)\n")
    Epool = embed(pool)
    names, U = ruler_dirs(pool, Epool)
    Z = spectra(Epool, U)

    # a concept "belongs" to a ruler if its z-response clears T. The SHAPE of
    # the spectrum decides everything: 1 ruler = pure (a distinguishing), exactly
    # 2 = a crossing, >=3 = a generic hub. We pick T; the data picks the rest.
    T = 1.0
    order = np.argsort(Z, axis=1)
    z1 = Z[np.arange(len(pool)), order[:, -1]]
    z2 = Z[np.arange(len(pool)), order[:, -2]]
    belong = [np.where(Z[i] > T)[0] for i in range(len(pool))]
    home = Z.argmax(1)

    print("EMERGENT DISTINGUISHINGS — top concepts each ruler claims as its own "
          "(belongs to it alone; we never sorted these):")
    for d, nm in enumerate(names):
        pure = [i for i in range(len(pool))
                if home[i] == d and len(belong[i]) <= 1]
        pure.sort(key=lambda i: -Z[i, d])
        print(f"  {nm:>18}: {', '.join(pool[i] for i in pure[:6]) or '—'}")

    print("\nEMERGENT CROSSINGS — concepts that answer to EXACTLY two rulers "
          "(peaked spectrum; the model's call, not ours):")
    cr = [i for i in range(len(pool)) if len(belong[i]) == 2]
    cr.sort(key=lambda i: -z2[i])
    for i in cr[:16]:
        d1, d2 = names[order[i, -1]], names[order[i, -2]]
        print(f"  {pool[i]:>15}  {d1} ∩ {d2}   (z {z1[i]:.2f} / {z2[i]:.2f})")

    hubs = [pool[i] for i in sorted(range(len(pool)),
            key=lambda i: -len(belong[i])) if len(belong[i]) >= 4][:8]
    print(f"\ngeneric hubs (answer to many rulers — excluded from crossings): "
          f"{', '.join(hubs) or '—'}")

    # emergent domain adjacency from the exactly-2 crossings = the system map
    D = len(names)
    B = np.zeros((D, D))
    for i in cr:
        a, b = order[i, -1], order[i, -2]
        B[a, b] += 1; B[b, a] += 1
    print("\nEMERGENT DOMAIN BRIDGES (count of concepts bridging each pair):")
    pairs = [(B[a, b], names[a], names[b])
             for a in range(D) for b in range(a + 1, D) if B[a, b] > 0]
    for n, a, b in sorted(pairs, reverse=True)[:10]:
        print(f"  {int(n):>2}  {a}  <->  {b}")

    np.savez("spectra_cache.npz", pool=np.array(pool, object),
             names=np.array(names, object), Z=Z)
    print("\nsaved spectra_cache.npz (used by make_atlas_map.py). The rulers are "
          "ours; every concept's home, crossing, and bridge is the data's.")


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", ".."))
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 320
    main(root, top_n)
