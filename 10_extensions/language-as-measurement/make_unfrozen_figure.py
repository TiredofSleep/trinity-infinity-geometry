"""make_unfrozen_figure.py -- the merit of staying unfrozen, from unfrozen_log.jsonl.
Left: test accuracy climbs across persistent sessions while the frozen prior stays flat.
Right: the agent flips its own trust from prior to grown memory.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, "unfrozen_log.jsonl"))]
S = [r["session"] for r in rows]
acc = [r["test_acc"] for r in rows]
anc = [r["test_acc_anchor_only"] for r in rows]
wa = [r["w_anchor"] for r in rows]
wp = [r["w_proto"] for r in rows]
LX0, LX1, RX0, RX1, YT, YB = 80, 320, 405, 645, 95, 300


def lx(i): return LX0 + i / (len(S) - 1) * (LX1 - LX0)
def ly(a): return YB - (a - 0.55) / 0.25 * (YB - YT)         # acc 0.55..0.80
def rx(i): return RX0 + i / (len(S) - 1) * (RX1 - RX0)
def ry(v): return YB - v * (YB - YT)


def poly(fx, fy, vals, color, w=2):
    pts = " ".join(f"{fx(i):.1f},{fy(v):.1f}" for i, v in enumerate(vals))
    dots = "".join(f'<circle cx="{fx(i):.1f}" cy="{fy(v):.1f}" r="3" fill="{color}"/>'
                   for i, v in enumerate(vals))
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{w}"/>{dots}'


def main():
    g = []
    for a in (0.55, 0.65, 0.75):
        yy = ly(a)
        g.append(f'<line x1="{LX0}" y1="{yy:.1f}" x2="{LX1}" y2="{yy:.1f}" stroke="var(--t)" stroke-width="0.5" opacity="0.18"/>'
                 f'<text x="{LX0-6}" y="{yy+4:.1f}" class="ts" text-anchor="end">{a:.2f}</text>')
    for v in (0.0, 0.5, 1.0):
        yy = ry(v)
        g.append(f'<line x1="{RX0}" y1="{yy:.1f}" x2="{RX1}" y2="{yy:.1f}" stroke="var(--t)" stroke-width="0.5" opacity="0.18"/>'
                 f'<text x="{RX0-6}" y="{yy+4:.1f}" class="ts" text-anchor="end">{v:.1f}</text>')
    H = 392
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>The merit of staying unfrozen</title>
<desc>Left: across twelve persistent study sessions the agent's held-out test accuracy rises from 0.63 to 0.72 while the frozen prior stays flat at 0.63. Right: the agent's trust weights flip from the prior to the memory it grew from experience.</desc>
<text x="40" y="28" class="th">the merit of staying unfrozen — it keeps learning across sessions</text>
<text x="40" y="48" class="ts">12 persistent sessions (separate processes; state on disk). the frozen prior cannot improve; the unfrozen agent does</text>
<text x="{(LX0+LX1)//2}" y="76" class="ts" text-anchor="middle">held-out test accuracy</text>
<text x="{(RX0+RX1)//2}" y="76" class="ts" text-anchor="middle">what it trusts</text>
{''.join(g)}
{poly(lx, ly, anc, "#D85A30")}
{poly(lx, ly, acc, "#444441", w=3.5)}
{poly(rx, ry, wa, "#D85A30")}
{poly(rx, ry, wp, "#378ADD")}
<text x="{(LX0+LX1)//2}" y="{YB+18}" class="ts" text-anchor="middle">session →</text>
<text x="{(RX0+RX1)//2}" y="{YB+18}" class="ts" text-anchor="middle">session →</text>
<circle cx="80" cy="{H-44}" r="4" fill="#D85A30"/><text x="90" y="{H-40}" class="ts">frozen prior (anchor) — flat</text>
<circle cx="290" cy="{H-44}" r="4" fill="#444441"/><text x="300" y="{H-40}" class="ts">unfrozen agent — climbs</text>
<circle cx="490" cy="{H-44}" r="4" fill="#378ADD"/><text x="500" y="{H-40}" class="ts">trust in grown memory</text>
<text x="40" y="{H-18}" class="ts">0.63 → 0.72 from lived experience alone; the agent flipped its own trust (anchor→memory) once the memory became reliable.</text>
</svg>'''
    open(os.path.join(HERE, "unfrozen_figure.svg"), "w", encoding="utf-8").write(svg)
    print("wrote unfrozen_figure.svg")


if __name__ == "__main__":
    main()
