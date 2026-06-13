"""crossings.py -- the payoff: detect COLLAPSES, CROSSINGS, and OVERLAPS between
two domain-rulers, by measured geometry rather than by assertion.

Take two lenses decomposing the same subject. Embed every node. Then:
  - LITERAL OVERLAP : same word in both lenses (cos ~ 1.0) -- a shared atom.
  - SEMANTIC CROSSING: different words, high cosine -- the domains meet here.
  - MUTUAL NEAREST  : each node is the other's closest -- the strongest crossing.

The interesting result is the semantic crossings: if the geometry puts
thermodynamic 'disorder' next to electrical 'noise' without us telling it to,
that crossing is a measurement, not a metaphor. Spurious matches are reported
too -- bare-word MiniLM is noisy and we don't hide it.

  python crossings.py
  python crossings.py thermodynamics "electrical engineering"
"""
import sys

import numpy as np

from embed import embed, cos
from lens import LENSES, nodes_of


def cross(lensA, lensB, sem_thr=0.30):
    a, b = nodes_of(lensA), nodes_of(lensB)
    EA, EB = embed([t for _, t in a]), embed([t for _, t in b])
    S = EA @ EB.T
    literal, semantic = [], []
    for i, (ka, la) in enumerate(a):
        for j, (kb, lb) in enumerate(b):
            s = float(S[i, j])
            if la.split()[0] == lb.split()[0]:
                literal.append((s, la, lb))
            elif s >= sem_thr:
                semantic.append((s, la, lb))
    # mutual nearest neighbours across lenses
    mutual = []
    for i, (ka, la) in enumerate(a):
        j = int(np.argmax(S[i]))
        if int(np.argmax(S[:, j])) == i:
            mutual.append((float(S[i, j]), la, b[j][1]))
    literal.sort(reverse=True); semantic.sort(reverse=True); mutual.sort(reverse=True)
    return literal, semantic, mutual


def main(lensA, lensB):
    print(f"crossings: [{lensA}]  x  [{lensB}]\n")
    literal, semantic, mutual = cross(lensA, lensB)

    print("LITERAL OVERLAPS (same atom in both rulers -- a shared sub-concept):")
    for s, la, lb in literal:
        print(f"  {la:>14}  =  {lb:<14}  cos {s:.3f}")
    print("\nSEMANTIC CROSSINGS (different words, geometry puts them together):")
    for s, la, lb in semantic[:8]:
        print(f"  {la:>14}  ~  {lb:<14}  cos {s:.3f}")
    print("\nMUTUAL NEAREST (strongest crossings -- each is the other's closest):")
    for s, la, lb in mutual:
        print(f"  {la:>14} <-> {lb:<14}  cos {s:.3f}")

    if semantic:
        s, la, lb = semantic[0]
        print(f"\ntop semantic crossing: '{la}' ~ '{lb}' (cos {s:.3f}) -- the two "
              f"domains genuinely meet here, measured not asserted.")
    print("\nhonest note: bare-word MiniLM is noisy; treat cos < ~0.35 as weak. "
          "Literal overlaps are lexical (we chose shared vocab); the semantic "
          "crossings are the real test.")
    return literal, semantic, mutual


if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        main("thermodynamics", "electrical engineering")
