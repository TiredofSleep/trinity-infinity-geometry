"""make_curve_figure.py -- the learning curves, straight from validate3_result.json.
Data-only few-shot vs algebra+data vs description-only. The gap at low k is the win.
"""
import json
import os

J = json.load(open(os.path.join(os.path.dirname(__file__), "validate3_result.json")))
KS = [1, 2, 3, 5, 8]
X0, X1, YT, YB = 110, 600, 80, 360            # plot box (YT=acc1.0, YB=acc0.0)


def X(i): return X0 + i / (len(KS) - 1) * (X1 - X0)
def Y(a): return YB - a * (YB - YT)


def line(alpha, color, dash=""):
    pts = " ".join(f"{X(i):.1f},{Y(J[alpha][str(k)]):.1f}" for i, k in enumerate(KS))
    d = f' stroke-dasharray="{dash}"' if dash else ""
    dots = "".join(f'<circle cx="{X(i):.1f}" cy="{Y(J[alpha][str(k)]):.1f}" '
                   f'r="3.5" fill="{color}"/>' for i, k in enumerate(KS))
    return (f'<polyline points="{pts}" fill="none" stroke="{color}" '
            f'stroke-width="2"{d}/>{dots}')


def main():
    base, ours, desc = "0.0", "0.5", "1.0"
    grid = []
    for a in (0.0, 0.125, 0.25, 0.5, 0.75, 1.0):
        yy = Y(a)
        grid.append(f'<line x1="{X0}" y1="{yy:.1f}" x2="{X1}" y2="{yy:.1f}" '
                    f'stroke="var(--t)" stroke-width="0.5" opacity="0.18"/>'
                    f'<text x="{X0-8}" y="{yy+4:.1f}" class="ts" '
                    f'text-anchor="end">{a:.2f}</text>')
    grid.append(f'<line x1="{X0}" y1="{Y(0.125):.1f}" x2="{X1}" y2="{Y(0.125):.1f}" '
                f'stroke="{ "#888780" }" stroke-width="1" stroke-dasharray="2 3"/>')
    xt = "".join(f'<text x="{X(i):.1f}" y="{YB+18:.1f}" class="ts" '
                 f'text-anchor="middle">{k}</text>' for i, k in enumerate(KS))
    # the win callout at k=1
    y_b, y_o = Y(J[base]["1"]), Y(J[ours]["1"])
    gain = J[ours]["1"] - J[base]["1"]
    callout = (f'<line x1="{X(0):.1f}" y1="{y_b:.1f}" x2="{X(0):.1f}" '
               f'y2="{y_o:.1f}" stroke="{ "#1D9E75" }" stroke-width="1" '
               f'stroke-dasharray="2 2"/>'
               f'<text x="{X(0)+8:.1f}" y="{(y_b+y_o)/2+4:.1f}" class="ts" '
               f'fill="#1D9E75">+{gain:.2f}</text>')
    H = 458
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Few-shot learning curves: the algebra as a prior beats data-only</title>
<desc>Accuracy versus number of training examples per domain. Data-only prototypes start at 0.57 at one example; algebra-plus-data start at 0.82; a description-only anchor with zero examples sits near 0.86 across the board. The gap is largest when examples are scarce and narrows as they accumulate.</desc>
<text x="40" y="30" class="th">the algebra is the head start — few-shot learning curves</text>
<text x="40" y="50" class="ts">8-way domain task, cosine nearest-prototype in raw 384-d, 80 splits. y = accuracy, x = labeled examples per domain</text>
{''.join(grid)}
{xt}
<text x="{(X0+X1)/2:.0f}" y="{YB+34:.0f}" class="ts" text-anchor="middle">examples per domain (k)</text>
{line(desc, "#888780", dash="5 4")}
{line(base, "#D85A30")}
{line(ours, "#1D9E75")}
{callout}
<circle cx="120" cy="{H-44}" r="4" fill="#D85A30"/><text x="130" y="{H-40}" class="ts">data-only (baseline)</text>
<circle cx="300" cy="{H-44}" r="4" fill="#1D9E75"/><text x="310" y="{H-40}" class="ts">algebra + data (ours)</text>
<circle cx="470" cy="{H-44}" r="4" fill="#888780"/><text x="480" y="{H-40}" class="ts">description only (0 examples)</text>
<text x="40" y="{H-16}" class="ts">the description-only anchor (zero labels) beats data-only prototypes at every k — the algebra is worth the examples it replaces.</text>
</svg>'''
    open(os.path.join(os.path.dirname(__file__), "curve_figure.svg"),
         "w", encoding="utf-8").write(svg)
    print("wrote curve_figure.svg")


if __name__ == "__main__":
    main()
