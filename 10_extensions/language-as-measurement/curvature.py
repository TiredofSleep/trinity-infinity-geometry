"""curvature.py -- the first real "English -> shapes": a chain of words/topics
becomes a path in semantic space, and we MEASURE its shape.

Two shape signals along the chain w_0, w_1, ..., w_n (embedded by MiniLM):
  - SPEED      step length |w_{i+1} - w_i| -- how far meaning moves per step.
  - CURVATURE  turning angle between consecutive steps -- how sharply the
               conceptual path bends. A big turn = a domain boundary.

This is the discrete Frenet reading of the meaning-curve. Ruler B (the parabolic
envelope) then applies to the cumulative drift: a smooth topic walk is a near-line,
and the deviations are the information.

  python curvature.py
  python curvature.py heat flow entropy information message language
"""
import sys

import numpy as np

from embed import embed, turning_angles, pca2d

DEFAULT = ["heat", "flow", "entropy", "information", "message", "language"]


def analyze(chain):
    P = embed(chain)
    Ln, ang = turning_angles(P)
    return P, Ln, ang


def main(chain):
    print(f"chain ({len(chain)} nodes): {' -> '.join(chain)}\n")
    P, Ln, ang = analyze(chain)

    print("SPEED  (semantic distance per step, MiniLM):")
    for i, d in enumerate(Ln):
        bar = "#" * int(round(d * 40))
        print(f"  {chain[i]:>12} -> {chain[i+1]:<12} {d:.3f}  {bar}")

    print("\nCURVATURE  (turning angle at each interior node; bigger = sharper "
          "conceptual turn):")
    for i, a in enumerate(ang):
        bar = "#" * int(round(a / 3))
        print(f"  at {chain[i+1]:>12}  {a:6.1f}°  {bar}")

    if ang:
        k = int(np.argmax(ang)) + 1
        print(f"\nsharpest turn: '{chain[k]}' ({ang[k-1]:.1f}°) -- the chain "
              f"changes direction most here (a likely domain edge between "
              f"'{chain[k-1]}' and '{chain[k+1]}').")

    # cumulative drift vs a straight walk (Ruler B applied to meaning)
    drift = np.concatenate([[0.0], np.cumsum(Ln)])
    chord = np.linalg.norm(P - P[0], axis=1)          # straight-line distance
    slack = drift - chord                              # path length beyond chord
    print(f"\nDRIFT: total path length {drift[-1]:.3f} vs straight chord "
          f"{chord[-1]:.3f} (end-to-start). Path/chord = {drift[-1]/max(chord[-1],1e-9):.2f}"
          f" -- >1 means the walk curves rather than going straight.")
    return P, Ln, ang


if __name__ == "__main__":
    chain = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT
    main(chain)
