"""make_atlas_map.py -- the Crossing Atlas, rendered straight from spectra.py.

RadViz: the rulers are fixed anchors on a ring (the only thing we place). Every
concept sits at the weighted centre of the rulers it answers to -- so a pure
concept hugs its ruler, and a crossing falls BETWEEN the rulers it bridges. We
place the rulers; the data places every concept and every collision.
"""
import math

import numpy as np

c = np.load("spectra_cache.npz", allow_pickle=True)
pool = list(c["pool"]); names = list(c["names"]); Z = c["Z"]
D = len(names)
CX, CY, RA = 340, 250, 150
RAMP = ["c-coral", "c-blue", "c-teal", "c-purple",
        "c-green", "c-amber", "c-pink", "c-red"]
HEX = {"c-coral": "#D85A30", "c-blue": "#378ADD", "c-teal": "#1D9E75",
       "c-purple": "#7F77DD", "c-green": "#639922", "c-amber": "#BA7517",
       "c-pink": "#D4537E", "c-red": "#E24B4A"}


def anchor_xy(k):
    a = math.radians(90 - k * 360 / D)
    return CX + RA * math.cos(a), CY - RA * math.sin(a), a


def main():
    A = np.array([anchor_xy(k)[:2] for k in range(D)])
    home = Z.argmax(1)
    belong = [np.where(Z[i] > 1.0)[0] for i in range(len(pool))]
    P = np.zeros((len(pool), 2))
    for i in range(len(pool)):
        w = np.maximum(Z[i], 0.0)
        P[i] = (w @ A) / w.sum() if w.sum() > 1e-9 else [CX, CY]

    dots = []
    for i in range(len(pool)):
        cross = len(belong[i]) == 2
        r = 4.4 if cross else 2.3
        op = 0.95 if cross else 0.5
        dots.append(f'<circle cx="{P[i,0]:.1f}" cy="{P[i,1]:.1f}" r="{r}" '
                    f'class="{RAMP[home[i]]}" opacity="{op}"/>')

    # label the exactly-2 crossings (the emergent bridges), placed AT the data.
    # Greedy: in the model's own z-order, draw a label only if it fits; the rest
    # stay as dots. We don't move points and don't pick which crossings exist.
    z2 = np.sort(Z, 1)[:, -2]
    cr = sorted([i for i in range(len(pool)) if len(belong[i]) == 2],
                key=lambda i: -z2[i])
    labels, placed = [], []
    for i in cr:
        w = len(pool[i]) * 6.0
        anc = "start" if P[i, 0] >= CX else "end"
        x0 = P[i, 0] + 6 if anc == "start" else P[i, 0] - 6 - w
        y0 = P[i, 1]
        if any(abs(y0 - py) < 13 and not (x0 + w < px or px + pw < x0)
               for px, py, pw in placed):
            continue
        placed.append((x0, y0, w))
        dx = 6 if anc == "start" else -6
        labels.append(f'<text x="{P[i,0]+dx:.1f}" y="{P[i,1]+3:.1f}" '
                      f'class="ts" text-anchor="{anc}">{pool[i]}</text>')

    anchors = []
    for k in range(D):
        ax, ay, a = anchor_xy(k)
        lx = CX + (RA + 16) * math.cos(a); ly = CY - (RA + 16) * math.sin(a)
        anc = "middle" if abs(math.cos(a)) < 0.25 else ("start" if math.cos(a) > 0 else "end")
        anchors.append(
            f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="6" class="{RAMP[k]}"/>'
            f'<text x="{lx:.1f}" y="{ly+3:.1f}" class="th" '
            f'text-anchor="{anc}" fill="{HEX[RAMP[k]]}">{names[k]}</text>')

    H = 560
    body = "\n".join(dots + labels + anchors)
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>The Crossing Atlas — meaning as a spectrum across rulers</title>
<desc>Eight domain rulers fixed on a ring. 320 concepts harvested from real prose, each placed at the weighted centre of the rulers it answers to. Pure concepts sit near one ruler; crossings such as symmetry (particle physics and geometry) and information (information theory and thermodynamics) fall between their domains.</desc>
<text x="40" y="30" class="th">the crossing atlas — every concept placed by its own ruler-spectrum</text>
<text x="40" y="50" class="ts">we place only the 8 rulers; each of 320 concepts sits at the centre of the rulers it answers to. crossings fall between domains.</text>
{body}
<text x="40" y="{H-30}" class="ts">found, not drawn: symmetry = particle physics ∩ geometry; information = information theory ∩ thermodynamics; mass = thermo ∩ particle.</text>
<text x="40" y="{H-12}" class="ts">big dots = concepts answering to exactly two rulers (crossings); faint = pure/home; centre = generic hubs. honest: electromagnetism is weakly grounded in this math-heavy corpus.</text>
</svg>'''
    open("atlas_map.svg", "w", encoding="utf-8").write(svg)
    print(f"wrote atlas_map.svg | {len(pool)} concepts, {D} rulers, "
          f"{len(cr)} crossings labeled")


if __name__ == "__main__":
    main()
