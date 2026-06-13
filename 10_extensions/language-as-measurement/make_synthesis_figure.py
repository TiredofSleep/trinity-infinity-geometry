"""make_synthesis_figure.py -- the combined map rides the best-available paradigm
across data scales. Straight from synthesis_result.json.
"""
import json
import os

J = json.load(open(os.path.join(os.path.dirname(__file__), "synthesis_result.json")))
KS = J["ks"]
C = J["curves"]
X0, X1, YT, YB, AT, AB = 120, 600, 80, 350, 0.90, 0.50


def X(i): return X0 + i / (len(KS) - 1) * (X1 - X0)
def Y(a): return YB - (a - AB) / (AT - AB) * (YB - YT)


def line(key, color, w=2, dash=""):
    pts = " ".join(f"{X(i):.1f},{Y(C[key][str(k)]):.1f}" for i, k in enumerate(KS))
    d = f' stroke-dasharray="{dash}"' if dash else ""
    dots = "".join(f'<circle cx="{X(i):.1f}" cy="{Y(C[key][str(k)]):.1f}" r="3" '
                   f'fill="{color}"/>' for i, k in enumerate(KS))
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{w}"{d}/>{dots}'


def main():
    grid = []
    for a in (0.5, 0.6, 0.7, 0.8, 0.9):
        yy = Y(a)
        grid.append(f'<line x1="{X0}" y1="{yy:.1f}" x2="{X1}" y2="{yy:.1f}" '
                    f'stroke="var(--t)" stroke-width="0.5" opacity="0.18"/>'
                    f'<text x="{X0-8}" y="{yy+4:.1f}" class="ts" text-anchor="end">{a:.1f}</text>')
    xt = "".join(f'<text x="{X(i):.1f}" y="{YB+18:.1f}" class="ts" '
                 f'text-anchor="middle">{k}</text>' for i, k in enumerate(KS))
    H = 430
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>The combined map rides the best-available paradigm</title>
<desc>Accuracy versus examples per class for three single mathematical lenses (semantic anchor, data manifold, relational graph) and the reliability-weighted fusion of them. The anchor lens leads when data is scarce; the data and graph lenses catch up and overtake as examples grow; the fusion tracks whichever is best and pulls ahead once they are comparable.</desc>
<text x="40" y="30" class="th">information as a path across substrates — the whole rides the best part</text>
<text x="40" y="50" class="ts">8-way task, 80 splits. three different math paradigms as lenses + their reliability-weighted fusion. y = accuracy, x = examples/class</text>
{''.join(grid)}
{xt}
<text x="{(X0+X1)/2:.0f}" y="{YB+34:.0f}" class="ts" text-anchor="middle">examples per class (k)</text>
{line("anchor", "#D85A30")}
{line("data", "#378ADD")}
{line("graph", "#1D9E75")}
{line("fuse-reliability", "#444441", w=3.5)}
<circle cx="95" cy="392" r="4" fill="#D85A30"/><text x="105" y="396" class="ts">anchor (semantic axes)</text>
<circle cx="270" cy="392" r="4" fill="#378ADD"/><text x="280" y="396" class="ts">data (manifold)</text>
<circle cx="410" cy="392" r="4" fill="#1D9E75"/><text x="420" y="396" class="ts">graph (relational)</text>
<circle cx="555" cy="392" r="4" fill="#444441"/><text x="565" y="396" class="ts">fusion</text>
<text x="40" y="416" class="ts">anchor leads when data is scarce; data/graph overtake as it grows; the reliability-weighted fusion tracks the best and wins once they're comparable.</text>
</svg>'''
    open(os.path.join(os.path.dirname(__file__), "synthesis_figure.svg"),
         "w", encoding="utf-8").write(svg)
    print("wrote synthesis_figure.svg")


if __name__ == "__main__":
    main()
