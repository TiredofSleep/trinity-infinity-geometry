"""make_system_map.py -- the whole-system crossing map (chord diagram).

All four domain-rulers (thermodynamics, electrical engineering, wave mechanics,
particle physics) decompose the subject 'meaning' into 9 concepts each = 36 nodes
around a circle, grouped into 4 colored arcs. Chords link concepts that CROSS
across domains. Drawn: the 4 shared atoms (cos 1.0) + semantic crossings cos>=0.50
(weaker 0.40-0.50 crossings exist -- omitted for legibility, noted honestly).
"""
import math

from crossings import system

CX, CY, R = 340, 250, 170
ORDER = ["thermodynamics", "electrical engineering",
         "wave mechanics", "particle physics"]
CENTER = {"thermodynamics": 135, "electrical engineering": 45,
          "wave mechanics": 315, "particle physics": 225}
COLOR = {"thermodynamics": "c-coral", "electrical engineering": "c-blue",
         "wave mechanics": "c-teal", "particle physics": "c-purple"}
SPAN = 64


def main():
    nodes, edges = system(sem_thr=0.50)
    # group nodes by domain, preserve tree order
    by_dom = {d: [n for n in nodes if n[0] == d] for d in ORDER}
    pos = {}
    for d in ORDER:
        ns = by_dom[d]; m = len(ns); c = CENTER[d]
        for i, n in enumerate(ns):
            ang = math.radians(c - SPAN / 2 + (i + 0.5) * SPAN / m)
            x = CX + R * math.cos(ang); y = CY - R * math.sin(ang)
            pos[(n[0], n[2])] = (x, y, ang, i)

    drawn = edges                      # already thresholded by system()
    active = set()
    for _, a, b, _ in drawn:
        active.add((a[0], a[2])); active.add((b[0], b[2]))

    parts = []
    # chords first (under the dots)
    for s, a, b, lit in drawn:
        xa, ya, _ = pos[(a[0], a[2])]; xb, yb, _ = pos[(b[0], b[2])]
        w = 0.6 + 2.6 * s; op = 0.30 + 0.6 * s
        parts.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" '
                     f'y2="{yb:.1f}" stroke="#888780" stroke-width="{w:.2f}" '
                     f'opacity="{op:.2f}"/>')
    # dots + labels
    for (dom, lab), (x, y, ang) in pos.items():
        act = (dom, lab) in active
        r = 5 if act else 3.2
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" '
                     f'class="{COLOR[dom]}"{"" if act else " opacity=\"0.5\""}/>')
        if act:
            lx = CX + (R + 11) * math.cos(ang); ly = CY - (R + 11) * math.sin(ang)
            anc = "end" if math.cos(ang) < -0.01 else ("middle" if abs(math.cos(ang)) < 0.2 else "start")
            parts.append(f'<text x="{lx:.1f}" y="{ly+4:.1f}" class="ts" '
                         f'text-anchor="{anc}">{lab}</text>')
    # domain headers
    for d in ORDER:
        a = math.radians(CENTER[d])
        hx = CX + (R + 44) * math.cos(a); hy = CY - (R + 44) * math.sin(a)
        parts.append(f'<circle cx="{hx-6:.1f}" cy="{hy-4:.1f}" r="5" '
                     f'class="{COLOR[d]}"/>')
        parts.append(f'<text x="{hx+4:.1f}" y="{hy:.1f}" class="th" '
                     f'text-anchor="middle">{d}</text>')

    H = 540
    body = "\n".join(parts)
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>The whole-system crossing map</title>
<desc>Four domain-rulers -- thermodynamics, electrical engineering, wave mechanics, particle physics -- each split the subject meaning into nine concepts arranged around a circle. Chords link concepts that the embedding geometry places together across domains, such as energy with power and transfer with exchange.</desc>
<text x="40" y="30" class="th">the whole system: where every ruler crosses every other</text>
<text x="40" y="50" class="ts">4 domains × 9 concepts; chords = cross-domain crossings (cos ≥ 0.50, plus shared atoms at 1.0)</text>
{body}
<text x="40" y="{H-28}" class="ts">strongest: energy≈power 0.68, transfer≈exchange 0.56, power≈charge 0.53; shared atoms entropy, transfer, amplitude, interference (1.0).</text>
<text x="40" y="{H-10}" class="ts">36 concepts total; faint dots didn't cross at this threshold. 26 weaker crossings (0.40–0.50) omitted for legibility.</text>
</svg>'''
    with open("system_map.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote system_map.svg | nodes {len(nodes)} drawn-edges {len(drawn)} "
          f"active-nodes {len(active)}")
    for s, a, b, lit in drawn:
        print(f"  {'LIT' if lit else 'sem'} {s:.2f}  {a[0][:5]}.{a[2]} <-> "
              f"{b[0][:5]}.{b[2]}")


if __name__ == "__main__":
    main()
