#!/usr/bin/env python3
"""make_figures.py -- draws the front-page figures as plain SVG (no dependencies).

    python make_figures.py      ->  the_base.svg, the_coin.svg  (in this folder)

Each figure sits on a light card, so it reads the same in light and dark themes."""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INK, SOFT, ACC, CARD, EDGE = "#1f2328", "#8c959f", "#c0392b", "#ffffff", "#d0d7de"
AXES = ("#c0392b", "#2471a3", "#1e8449")
FONT = "font-family='-apple-system, Segoe UI, Helvetica, Arial, sans-serif'"


def project(p, yaw=0.62, pitch=0.38):
    """a fixed three-quarter view: returns (x, y, depth), y pointing down the page"""
    x, y, z = p
    x, y = x * math.cos(yaw) - y * math.sin(yaw), x * math.sin(yaw) + y * math.cos(yaw)
    y, z = y * math.cos(pitch) - z * math.sin(pitch), y * math.sin(pitch) + z * math.cos(pitch)
    return x, -z, y


def card(w, h):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>\n"
            f"<rect x='0.5' y='0.5' width='{w - 1}' height='{h - 1}' rx='10' fill='{CARD}' stroke='{EDGE}'/>\n")


# ---------------------------------------------------------------- the base: 0-9 as shapes

s3 = math.sqrt(3)
TET = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
OCT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
CUBE = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]


def edges_by_length(V):
    d = lambda a, b: sum((u - v) ** 2 for u, v in zip(a, b))
    m = min(d(a, b) for i, a in enumerate(V) for b in V[i + 1:])
    return [(i, j) for i in range(len(V)) for j in range(i + 1, len(V)) if abs(d(V[i], V[j]) - m) < 1e-9]


SHAPES = [
    ("0", "the void", [], [], False, True),
    ("1", "point", [(0, 0, 0)], [], False, False),
    ("2", "segment", [(-1.3, 0, 0), (1.3, 0, 0)], None, False, False),
    ("3", "triangle", [(math.cos(a), 0, math.sin(a)) for a in (math.pi / 2, math.pi / 2 + 2 * math.pi / 3,
                                                                  math.pi / 2 + 4 * math.pi / 3)], None, False, False),
    ("4", "tetrahedron", TET, None, False, False),
    ("5", "tetrahedron + centre", TET, None, True, False),
    ("6", "octahedron", OCT, None, False, False),
    ("7", "octahedron + centre", OCT, None, True, False),
    ("8", "cube", CUBE, None, False, False),
    ("9", "cube + centre", CUBE, None, True, False),
]


def draw_shape(cx, cy, scale, V, E, centre, void, flat=False):
    out = []
    if void:
        out.append(f"<circle cx='{cx}' cy='{cy}' r='{scale * 1.05:.1f}' fill='none' stroke='{SOFT}' "
                   f"stroke-width='1.4' stroke-dasharray='4 4'/>")
        return out
    view = (lambda p: (p[0], -p[2], p[1])) if flat else project
    P = [view(v) for v in V]
    if E is None:
        E = edges_by_length(V) if len(V) > 1 else []
    depth = sorted(E, key=lambda e: -(P[e[0]][2] + P[e[1]][2]))
    far = max((p[2] for p in P), default=0)
    for i, j in depth:
        back = (P[i][2] + P[j][2]) / 2 > 0.35
        out.append(f"<line x1='{cx + scale * P[i][0]:.1f}' y1='{cy + scale * P[i][1]:.1f}' "
                   f"x2='{cx + scale * P[j][0]:.1f}' y2='{cy + scale * P[j][1]:.1f}' stroke='{INK}' "
                   f"stroke-width='1.6' stroke-opacity='{0.35 if back else 0.9}' stroke-linecap='round'/>")
    if centre:
        for p in P:
            out.append(f"<line x1='{cx}' y1='{cy}' x2='{cx + scale * p[0]:.1f}' y2='{cy + scale * p[1]:.1f}' "
                       f"stroke='{ACC}' stroke-width='1' stroke-opacity='0.45' stroke-dasharray='2 3'/>")
    for p in sorted(P, key=lambda p: -p[2]):
        op = 0.55 if p[2] > 0.35 else 1
        out.append(f"<circle cx='{cx + scale * p[0]:.1f}' cy='{cy + scale * p[1]:.1f}' r='4.2' fill='{INK}' "
                   f"fill-opacity='{op}'/>")
    if centre:
        out.append(f"<circle cx='{cx}' cy='{cy}' r='5' fill='{ACC}'/>")
    return out


def the_base():
    cols, cw, rh, top = 5, 164, 150, 58
    w, h = cols * cw + 20, top + 2 * rh + 34
    svg = [card(w, h),
           f"<text x='{w / 2}' y='32' text-anchor='middle' {FONT} font-size='17' font-weight='600' fill='{INK}'>"
           f"The base: each integer from 0 to 9 as the shape it is forced to take</text>"]
    for k, (num, name, V, E, centre, void) in enumerate(SHAPES):
        r, c = divmod(k, cols)
        cx, cy = 10 + c * cw + cw / 2, top + r * rh + 58
        flat = num == "3"
        svg += draw_shape(cx, cy, 34 if num not in ("6", "7") else 40, V, E, centre, void, flat)
        svg.append(f"<text x='{cx}' y='{cy + 72}' text-anchor='middle' {FONT} font-size='14' fill='{INK}'>"
                   f"<tspan font-weight='700'>{num}</tspan>  {name}</text>")
    svg.append(f"<text x='{w / 2}' y='{h - 14}' text-anchor='middle' {FONT} font-size='12' fill='{SOFT}'>"
               f"one rule, the most symmetric arrangement · at 5, 7 and 9 the odd point must stand on the centre "
               f"(red)</text>")
    svg.append("</svg>\n")
    open(os.path.join(HERE, "the_base.svg"), "w", encoding="utf-8").write("\n".join(svg))
    print("  wrote the_base.svg")


# ---------------------------------------------------------------- the coin: three half-turns of one sphere


def the_coin():
    w, h = 840, 430
    cx, cy, R = 250, 222, 150
    svg = [card(w, h),
           f"<text x='{w / 2}' y='34' text-anchor='middle' {FONT} font-size='17' font-weight='600' fill='{INK}'>"
           f"The coin: two sides and an edge — three times, on one sphere of numbers</text>"]
    tilt = 0.32
    # the sphere and its equator (the unit circle)
    svg.append(f"<circle cx='{cx}' cy='{cy}' r='{R}' fill='#f6f8fa' stroke='{SOFT}' stroke-width='1.4'/>")
    ry = R * math.sin(tilt)
    svg.append(f"<path d='M {cx - R} {cy} A {R} {ry:.1f} 0 0 0 {cx + R} {cy}' fill='none' stroke='{SOFT}' "
               f"stroke-width='1.2'/>")
    svg.append(f"<path d='M {cx - R} {cy} A {R} {ry:.1f} 0 0 1 {cx + R} {cy}' fill='none' stroke='{SOFT}' "
               f"stroke-width='1.2' stroke-dasharray='4 4'/>")

    yaw = math.radians(34)

    def pt(x, y, z):   # z up, y toward the viewer; turned by `yaw` so no two axes line up on the page
        x, y = x * math.cos(yaw) - y * math.sin(yaw), x * math.sin(yaw) + y * math.cos(yaw)
        return cx + R * x, cy - R * (z * math.cos(tilt) - y * math.sin(tilt)), y

    # 1, i, −1, −i run counterclockwise seen from ∞ (y points toward the viewer, so i sits at y = −1)
    corners = {"∞": (0, 0, 1), "0": (0, 0, -1), "1": (1, 0, 0), "−1": (-1, 0, 0), "i": (0, -1, 0), "−i": (0, 1, 0)}
    P = {k: pt(*v) for k, v in corners.items()}
    # the octahedron's edges, faint
    names = list(corners)
    for a in range(6):
        for b in range(a + 1, 6):
            va, vb = corners[names[a]], corners[names[b]]
            if sum(x * y for x, y in zip(va, vb)) == 0:
                back = P[names[a]][2] + P[names[b]][2] < 0
                svg.append(f"<line x1='{P[names[a]][0]:.1f}' y1='{P[names[a]][1]:.1f}' x2='{P[names[b]][0]:.1f}' "
                           f"y2='{P[names[b]][1]:.1f}' stroke='{INK}' stroke-opacity='{0.15 if back else 0.3}' "
                           f"stroke-width='1.2'/>")
    # the three axes = the three flips
    for (a, b), col in zip((("∞", "0"), ("−1", "1"), ("−i", "i")), AXES):
        svg.append(f"<line x1='{P[a][0]:.1f}' y1='{P[a][1]:.1f}' x2='{P[b][0]:.1f}' y2='{P[b][1]:.1f}' "
                   f"stroke='{col}' stroke-width='2.6' stroke-linecap='round'/>")
        for k in (a, b):
            svg.append(f"<circle cx='{P[k][0]:.1f}' cy='{P[k][1]:.1f}' r='6.5' fill='{col}' stroke='white' "
                       f"stroke-width='1.5'/>")
    for k in corners:
        ux, uy = P[k][0] - cx, P[k][1] - cy
        n = math.hypot(ux, uy) or 1
        dx, dy = 20 * ux / n, 20 * uy / n + 6
        svg.append(f"<text x='{P[k][0] + dx:.1f}' y='{P[k][1] + dy:.1f}' text-anchor='middle' {FONT} "
                   f"font-size='17' font-style='{'italic' if 'i' in k else 'normal'}' font-weight='600' "
                   f"fill='{INK}'>{k}</text>")
    svg.append(f"<circle cx='{cx}' cy='{cy}' r='5' fill='white' stroke='{INK}' stroke-width='1.4'/>")
    # legend
    lx, ly = 470, 96
    rows = [("z → −z", "positive and negative", "keeps 0 and ∞", "swaps 1 with −1, i with −i"),
            ("z → 1/z", "finite and infinite", "keeps 1 and −1", "swaps 0 with ∞, i with −i"),
            ("z → −1/z", "real and imaginary", "keeps i and −i", "swaps 0 with ∞, 1 with −1")]
    for k, ((f, coin, keep, swap), col) in enumerate(zip(rows, AXES)):
        y = ly + k * 84
        svg.append(f"<rect x='{lx}' y='{y - 15}' width='14' height='14' rx='3' fill='{col}'/>")
        svg.append(f"<text x='{lx + 24}' y='{y - 2}' {FONT} font-size='15' font-weight='600' fill='{INK}'>"
                   f"{f}   <tspan font-weight='400' fill='{SOFT}'>· {coin}</tspan></text>")
        svg.append(f"<text x='{lx + 24}' y='{y + 20}' {FONT} font-size='14' fill='{INK}'>edge: {keep}</text>")
        svg.append(f"<text x='{lx + 24}' y='{y + 40}' {FONT} font-size='14' fill='{INK}'>sides: {swap}</text>")
    svg.append(f"<text x='{lx}' y='{ly + 3 * 84 + 4}' {FONT} font-size='13' fill='{SOFT}'>"
               f"The centre (open dot) is kept by all three flips —</text>")
    svg.append(f"<text x='{lx}' y='{ly + 3 * 84 + 22}' {FONT} font-size='13' fill='{SOFT}'>"
               f"a void that no number occupies.</text>")
    svg.append("</svg>\n")
    open(os.path.join(HERE, "the_coin.svg"), "w", encoding="utf-8").write("\n".join(svg))
    print("  wrote the_coin.svg")


if __name__ == "__main__":
    the_base()
    the_coin()
