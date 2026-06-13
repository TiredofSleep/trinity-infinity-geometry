"""make_rulers_figure.py -- generate the two-rulers figure straight from the
real computation in rulers.py, so the picture cannot drift from the numbers.

Writes rulers_figure.svg (targeted at the Imagine widget host: color classes
c-teal/c-amber/c-gray and text classes t/ts/th are provided by that host).
"""
import math

from rulers import circle_by_squares, chebyshev_residual


def circle_panel(cx=185, cy=165, R=90, n=6):
    out = []
    cell = 2 * R / n
    ins = bnd = 0
    for i in range(n):
        for j in range(n):
            x0 = -1 + i * (2 / n); x1 = x0 + 2 / n
            y0 = -1 + j * (2 / n); y1 = y0 + 2 / n
            c = [x0 * x0 + y0 * y0 <= 1, x1 * x1 + y0 * y0 <= 1,
                 x0 * x0 + y1 * y1 <= 1, x1 * x1 + y1 * y1 <= 1]
            px = cx + x0 * R; py = cy - y1 * R
            if all(c):
                ins += 1
                out.append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{cell:.1f}" '
                           f'height="{cell:.1f}" rx="0" class="c-teal"/>')
            elif any(c):
                bnd += 1
                out.append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{cell:.1f}" '
                           f'height="{cell:.1f}" rx="0" class="c-amber"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" '
               f'stroke="var(--t)" stroke-width="1.5"/>')
    return "\n".join(out), ins, bnd


def line_panel(x0=375, x1=632, ymid=165, half=82, lo=100, hi=2000):
    out = chebyshev_residual(N=hi)
    xs, res = out["xs"], out["res"]
    pts = [(x, d) for x, d in zip(xs, res) if x >= lo]
    pts = pts[::max(1, len(pts) // 150)]   # subsample for a clean, light curve
    K = 1.0                              # envelope +/- K*sqrt(x); residual <= 0.78
    ymax = K * math.sqrt(hi) * 1.08

    def X(x): return x0 + (x - lo) / (hi - lo) * (x1 - x0)
    def Y(d): return ymid - (d / ymax) * half

    res_poly = " ".join(f"{X(x):.1f},{Y(d):.1f}" for x, d in pts)
    up = " ".join(f"{X(x):.1f},{Y(K*math.sqrt(x)):.1f}"
                  for x in range(lo, hi + 1, 25))
    dn = " ".join(f"{X(x):.1f},{Y(-K*math.sqrt(x)):.1f}"
                  for x in range(lo, hi + 1, 25))
    svg = [
        f'<line x1="{x0}" y1="{ymid}" x2="{x1}" y2="{ymid}" '
        f'stroke="var(--t)" stroke-width="1" stroke-dasharray="4 3"/>',
        f'<polyline points="{up}" fill="none" stroke="#BA7517" '
        f'stroke-width="1.5"/>',
        f'<polyline points="{dn}" fill="none" stroke="#BA7517" '
        f'stroke-width="1.5"/>',
        f'<polyline points="{res_poly}" fill="none" stroke="#1D9E75" '
        f'stroke-width="1.5"/>',
    ]
    return "\n".join(svg), out["alpha"], out["c_env"]


def main():
    ta, rows = circle_by_squares()
    last = rows[-1]
    cp, ins, bnd = circle_panel()
    lp, alpha, c_env = line_panel()
    H = 372
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Two rulers for measuring information</title>
<desc>Left: a circle tiled by squares; interior squares resolve the area to pi while the boundary squares measure a taxicab length of 8r, not the Euclidean 2 pi r. Right: the Chebyshev residual psi(x) minus x staying inside a parabolic square-root envelope.</desc>
<text x="40" y="34" class="th">two rulers: read the defect, not the summary</text>
<text x="40" y="54" class="ts">there is no single correct ruler — each reads a different, valid layer of the same object</text>

<text x="60" y="86" class="th">a circle measured by squares</text>
{cp}
<rect x="95" y="270" width="14" height="14" rx="0" class="c-teal"/>
<text x="115" y="281" class="ts">inside ({ins})</text>
<rect x="185" y="270" width="14" height="14" rx="0" class="c-amber"/>
<text x="205" y="281" class="ts">boundary defect ({bnd})</text>
<text x="60" y="306" class="ts">interior resolves area → {last['area_lo']:.2f} (→ π)</text>
<text x="60" y="324" class="ts">but the rim → taxicab 8r = 8.0,</text>
<text x="60" y="342" class="ts">never the Euclidean 2πr = 6.28</text>

<text x="375" y="86" class="th">a line measured by a parabola</text>
{lp}
<text x="396" y="120" class="ts">+√x</text>
<text x="396" y="220" class="ts">−√x</text>
<line x1="375" y1="270" x2="389" y2="270" stroke="var(--t)" stroke-width="1" stroke-dasharray="4 3"/>
<text x="395" y="275" class="ts">the line y = x (residual 0)</text>
<polyline points="375,288 389,288" fill="none" stroke="#1D9E75" stroke-width="1.5"/>
<text x="395" y="293" class="ts">residual ψ(x) − x</text>
<text x="375" y="324" class="ts">residual ≤ 0.78√x — just inside ±√x</text>
<text x="375" y="342" class="ts">growth exponent ≈ {alpha:.2f} (RH predicts 0.5)</text>
</svg>'''
    with open("rulers_figure.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote rulers_figure.svg  | circle inside={ins} boundary={bnd} "
          f"area_lo={last['area_lo']:.3f} taxicab={last['taxicab_len']:.3f}")
    print(f"line: alpha={alpha:.3f} c_env={c_env:.3f}")


if __name__ == "__main__":
    main()
