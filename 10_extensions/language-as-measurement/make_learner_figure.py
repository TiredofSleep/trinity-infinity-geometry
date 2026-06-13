"""make_learner_figure.py -- the online learner, drawn from learner_result.json.
Left: accuracy climbs as it learns. Right: it learns what to trust (weights shift
from the prior to the grown memory).
"""
import json
import os

J = json.load(open(os.path.join(os.path.dirname(__file__), "learner_result.json")))
C = J["curves"]
WT = J["weights_traj"]
nC = len(C["agent"])
nW = len(WT)
COL = {"anchor": "#D85A30", "proto": "#378ADD", "knn": "#1D9E75", "agent": "#444441"}

LX0, LX1 = 78, 320          # left panel (accuracy)
RX0, RX1 = 410, 650         # right panel (weights)
YT, YB = 90, 300


def axc(i): return LX0 + i / (nC - 1) * (LX1 - LX0)
def ayc(a): return YB - (a - 0.1) / 0.6 * (YB - YT)          # acc 0.1..0.7
def wxc(j): return RX0 + j / (nW - 1) * (RX1 - RX0)
def wyc(v): return YB - v * (YB - YT)                         # weight 0..1


def poly(xs, ys, color, w=2, dash=""):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{w}"{d}/>'


def acc_line(key, w=2):
    step = 5
    xs = [axc(i) for i in range(0, nC, step)]
    ys = [ayc(C[key][i]) for i in range(0, nC, step)]
    return poly(xs, ys, COL[key], w)


def w_line(j_lens, color):
    xs = [wxc(j) for j in range(nW)]
    ys = [wyc(WT[j][j_lens]) for j in range(nW)]
    return poly(xs, ys, color, 2)


def main():
    g = []
    for a in (0.1, 0.3, 0.5, 0.7):
        y = ayc(a)
        g.append(f'<line x1="{LX0}" y1="{y:.1f}" x2="{LX1}" y2="{y:.1f}" stroke="var(--t)" stroke-width="0.5" opacity="0.18"/>'
                 f'<text x="{LX0-6}" y="{y+4:.1f}" class="ts" text-anchor="end">{a:.1f}</text>')
    for v in (0.0, 0.5, 1.0):
        y = wyc(v)
        g.append(f'<line x1="{RX0}" y1="{y:.1f}" x2="{RX1}" y2="{y:.1f}" stroke="var(--t)" stroke-width="0.5" opacity="0.18"/>'
                 f'<text x="{RX0-6}" y="{y+4:.1f}" class="ts" text-anchor="end">{v:.1f}</text>')
    # chance line on accuracy panel
    g.append(f'<line x1="{LX0}" y1="{ayc(0.125):.1f}" x2="{LX1}" y2="{ayc(0.125):.1f}" stroke="#888780" stroke-width="1" stroke-dasharray="2 3"/>')
    H = 400
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>An algorithm-language that learns online, like an AI and with an AI</title>
<desc>Left panel: windowed accuracy over a stream of 240 experiences. The fixed semantic prior stays flat; the learned manifold lens climbs from chance; the agent climbs above the prior as it learns. Right panel: the agent's lens-weights over the same stream, shifting from the prior to the grown memory.</desc>
<text x="40" y="28" class="th">an algorithm-language that learns online — like an AI, with an AI</text>
<text x="40" y="48" class="ts">240-experience stream, averaged over 40 orders. the LM embeds; the agent predicts, gets feedback, and updates — no batch training</text>
<text x="{(LX0+LX1)//2}" y="74" class="ts" text-anchor="middle">it learns: accuracy climbs</text>
<text x="{(RX0+RX1)//2}" y="74" class="ts" text-anchor="middle">it learns what to trust</text>
{''.join(g)}
{acc_line("anchor")}
{acc_line("proto")}
{acc_line("agent", w=3.5)}
{w_line(0, COL["anchor"])}
{w_line(1, COL["proto"])}
{w_line(2, COL["knn"])}
<text x="{(LX0+LX1)//2}" y="{YB+18}" class="ts" text-anchor="middle">experiences seen →</text>
<text x="{(RX0+RX1)//2}" y="{YB+18}" class="ts" text-anchor="middle">experiences seen →</text>
<circle cx="78" cy="{H-46}" r="4" fill="#D85A30"/><text x="88" y="{H-42}" class="ts">anchor (prior)</text>
<circle cx="210" cy="{H-46}" r="4" fill="#378ADD"/><text x="220" y="{H-42}" class="ts">proto (learned memory)</text>
<circle cx="410" cy="{H-46}" r="4" fill="#1D9E75"/><text x="420" y="{H-42}" class="ts">knn</text>
<circle cx="470" cy="{H-46}" r="4" fill="#444441"/><text x="480" y="{H-42}" class="ts">agent (combined)</text>
<text x="40" y="{H-20}" class="ts">the agent starts on its prior, then learns to trust the memory it grew from experience (proto weight 0.33→0.91). that shift is the learning.</text>
</svg>'''
    open(os.path.join(os.path.dirname(__file__), "learner_figure.svg"), "w", encoding="utf-8").write(svg)
    print("wrote learner_figure.svg")


if __name__ == "__main__":
    main()
