"""lens.py -- a domain used as a RULER, decomposing a subject meta -> letter.

Each lens is a hypothesis about how a domain splits the subject:
    meta  ->  2-3 categories  ->  operations  ->  (... -> the letter)
The STRUCTURE is authored (the hypothesis). The GEOMETRY on it -- where each node
sits, how far the categories spread, how sharply each branch turns -- is MEASURED
by embedding the node labels. Same subject ("meaning"), three different rulers;
each reads a different valid layer.

  python lens.py
"""
import numpy as np

from embed import embed, turning_angles

# subject under study: "meaning" (a unit of language). Each lens reads it.
LENSES = {
    "thermodynamics": {
        "meta": "meaning as an energy system",
        "tree": {"energy": ["heat", "work"],
                 "entropy": ["disorder", "dispersal"],
                 "flow": ["transfer", "gradient"]},
    },
    "electrical engineering": {
        "meta": "meaning as a signal",
        "tree": {"power": ["amplitude", "gain"],
                 "noise": ["entropy", "interference"],
                 "channel": ["bandwidth", "transfer"]},
    },
    "wave mechanics": {
        "meta": "meaning as a wave",
        "tree": {"amplitude": ["intensity", "swell"],
                 "frequency": ["pitch", "rhythm"],
                 "phase": ["alignment", "interference"]},
    },
    "particle physics": {
        "meta": "meaning as a particle system",
        "tree": {"charge": ["polarity", "attraction"],
                 "spin": ["rotation", "orientation"],
                 "interaction": ["exchange", "coupling"]},
    },
}


def nodes_of(lens):
    """Flat list of (level, label) for a lens, root first."""
    L = LENSES[lens]
    out = [("meta", L["meta"])]
    for cat, ops in L["tree"].items():
        out.append(("category", cat))
        out += [("operation", op) for op in ops]
    return out


def measure(lens):
    L = LENSES[lens]
    cats = list(L["tree"])
    Emeta = embed([L["meta"]])[0]
    Ecats = embed(cats)
    # category spread: how far the categories sit from the meta, and from each other
    cat_from_meta = [float(np.linalg.norm(Ecats[i] - Emeta)) for i in range(len(cats))]
    pair = [float(np.linalg.norm(Ecats[i] - Ecats[j]))
            for i in range(len(cats)) for j in range(i + 1, len(cats))]
    print(f"=== {lens}: {L['meta']} ===")
    print(f"  categories: {', '.join(cats)}")
    print(f"  spread from meta:   mean {np.mean(cat_from_meta):.3f} "
          f"(min {min(cat_from_meta):.3f}, max {max(cat_from_meta):.3f})")
    print(f"  spread among cats:  mean {np.mean(pair):.3f}")
    # per-branch curvature: meta -> category -> each operation
    for cat, ops in L["tree"].items():
        for op in ops:
            P = embed([L["meta"], cat, op])
            _, ang = turning_angles(P)
            print(f"    branch  meta -> {cat} -> {op:<12}  turn {ang[0]:5.1f}°")
    print()


if __name__ == "__main__":
    for lens in LENSES:
        measure(lens)
    print("structure is authored (a hypothesis); the spreads and turns above are "
          "measured. Cross-lens crossings -> crossings.py")
