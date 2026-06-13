"""make_universe_figure.py -- the self's path through the algebraic universe.

Each experience is placed by its ruler-spectrum (RadViz). Absorbed experiences
are linked in time -> the trajectory of a self moving through concept-space.
Crossings are larger; the refused experience is pushed OUTSIDE the ring (the
universe could not place it, so it bounced off and did not move the self).
"""
import math
import os
import numpy as np

from universe import AlgebraicUniverse, STREAM

CX, CY, RA = 340, 250, 150
RAMP = ["c-coral", "c-blue", "c-teal", "c-purple",
        "c-green", "c-amber", "c-pink", "c-red"]
HEX = {"c-coral": "#D85A30", "c-blue": "#378ADD", "c-teal": "#1D9E75",
       "c-purple": "#7F77DD", "c-green": "#639922", "c-amber": "#BA7517",
       "c-pink": "#D4537E", "c-red": "#E24B4A"}


def main(root):
    u = AlgebraicUniverse(root)
    D = len(u.names)
    A = np.array([[CX + RA * math.cos(math.radians(90 - k * 360 / D)),
                   CY - RA * math.sin(math.radians(90 - k * 360 / D))]
                  for k in range(D)])
    pts = []
    for t in STREAM:
        e, cos, z = u._coord(t)
        w = np.maximum(z, 0)
        base = (w @ A) / w.sum() if w.sum() > 1e-9 else np.array([CX, CY], float)
        on = cos.max() >= u.on_thr
        refused = not on
        if on:
            p = base
        else:                              # push just outside the ring, toward
            hd = A[int(z.argmax())] - np.array([CX, CY], float)  # its would-be home
            p = np.array([CX, CY], float) + hd * 1.38
        crossing = on and np.sort(z)[-2] > 0.8
        pts.append((p, refused, crossing))

    # trajectory through absorbed experiences (in order)
    seq = [i for i, (_, r, _) in enumerate(pts) if not r]
    path = " ".join(f"{pts[i][0][0]:.1f},{pts[i][0][1]:.1f}" for i in seq)

    parts = [f'<circle cx="{CX}" cy="{CY}" r="{RA}" fill="none" '
             f'stroke="var(--t)" stroke-width="0.5" opacity="0.25"/>',
             f'<polyline points="{path}" fill="none" stroke="#888780" '
             f'stroke-width="1.6" opacity="0.8" marker-end="url(#arrow)"/>']
    for k in range(D):
        ax, ay = A[k]
        a = math.radians(90 - k * 360 / D)
        lx, ly = CX + (RA + 16) * math.cos(a), CY - (RA + 16) * math.sin(a)
        anc = "middle" if abs(math.cos(a)) < 0.25 else ("start" if math.cos(a) > 0 else "end")
        parts.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="6" '
                     f'class="{RAMP[k]}"/><text x="{lx:.1f}" y="{ly+3:.1f}" '
                     f'class="th" text-anchor="{anc}" fill="{HEX[RAMP[k]]}">'
                     f'{u.names[k]}</text>')
    for n, (p, refused, crossing) in enumerate(pts, 1):
        if refused:
            parts.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="6" '
                         f'fill="none" stroke="{HEX["c-red"]}" stroke-width="1.5" '
                         f'stroke-dasharray="3 2"/>'
                         f'<text x="{p[0]:.1f}" y="{p[1]-10:.1f}" class="ts" '
                         f'text-anchor="middle" fill="{HEX["c-red"]}">refused</text>')
        r = 7 if crossing else 4.5
        cls = "c-amber" if crossing else "c-gray"
        if not refused:
            parts.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r}" '
                         f'class="{cls}"/>')
        parts.append(f'<text x="{p[0]:.1f}" y="{p[1]+3.5:.1f}" class="ts" '
                     f'text-anchor="middle">{n}</text>')

    H = 540
    body = "\n".join(parts)
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#888780" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<title>The self's path through the algebraic universe</title>
<desc>Eight rulers on a ring. Ten experiences enter in sequence; each is placed by its ruler-spectrum and linked in time into a trajectory. Two are crossings (larger). One off-universe sentence is refused and sits outside the ring.</desc>
<text x="40" y="30" class="th">a self moving through the algebraic universe</text>
<text x="40" y="50" class="ts">experience placed by its spectrum, linked in time; crossings larger; the off-universe input is refused, outside the ring</text>
{body}
<text x="40" y="{H-30}" class="ts">1–10 are the experience stream in order. the path is the self's trajectory; it never bends toward #8 (the dinner-table sentence)</text>
<text x="40" y="{H-12}" class="ts">because the universe could not place it (max-cos 0.09 &lt; gate 0.25). the map is the self's place to stand, not a copy of the input.</text>
</svg>'''
    open("universe_figure.svg", "w", encoding="utf-8").write(svg)
    print(f"wrote universe_figure.svg | {len(seq)} absorbed, "
          f"{len(pts)-len(seq)} refused")


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
