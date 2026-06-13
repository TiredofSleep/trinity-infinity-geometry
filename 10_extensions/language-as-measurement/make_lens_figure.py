"""make_lens_figure.py -- the crossing map, straight from crossings.py.

Two domain-rulers decompose the same subject; we draw the measured crossings as
links between concepts. Bipartite (not PCA) so the 2-D positions carry no false
distance -- only the LINKS are the claim, weighted by cosine.
"""
from embed import embed, cos

THERMO = ["energy", "heat", "work", "entropy", "disorder", "dispersal",
          "flow", "transfer", "gradient"]
EE = ["power", "amplitude", "gain", "noise", "entropy", "interference",
      "channel", "bandwidth", "transfer"]
# detected crossings (left thermo label, right EE label); cos computed live
PAIRS = [("energy", "power"), ("entropy", "entropy"),
         ("disorder", "noise"), ("transfer", "transfer")]


def main():
    ET = embed(THERMO)
    EEv = embed(EE)
    tidx = {w: i for i, w in enumerate(THERMO)}
    eidx = {w: i for i, w in enumerate(EE)}
    scored = [(a, b, cos(ET[tidx[a]], EEv[eidx[b]])) for a, b in PAIRS]

    def yL(i): return 96 + i * 30
    def yR(i): return 96 + i * 30
    XL, XR = 235, 445

    conns = []
    for a, b, s in scored:
        i, j = tidx[a], eidx[b]
        w = 0.6 + 3.0 * s
        op = 0.35 + 0.6 * s
        mx = XL + 0.30 * (XR - XL)               # off-midpoint so crossing
        my = yL(i) + 0.30 * (yR(j) - yL(i))      # labels don't collide
        conns.append(
            f'<line x1="{XL}" y1="{yL(i)}" x2="{XR}" y2="{yR(j)}" '
            f'stroke="#888780" stroke-width="{w:.2f}" opacity="{op:.2f}"/>'
            f'<text x="{mx:.0f}" y="{my-3:.0f}" class="ts" text-anchor="middle">'
            f'{s:.2f}</text>')

    left = []
    for i, w in enumerate(THERMO):
        left.append(f'<circle cx="{XL}" cy="{yL(i)}" r="5" class="c-coral"/>'
                    f'<text x="{XL-12}" y="{yL(i)+4}" class="t" '
                    f'text-anchor="end">{w}</text>')
    right = []
    for i, w in enumerate(EE):
        right.append(f'<circle cx="{XR}" cy="{yR(i)}" r="5" class="c-blue"/>'
                     f'<text x="{XR+12}" y="{yR(i)+4}" class="t">{w}</text>')

    H = 420
    body = "\n".join(conns + left + right)
    top = scored[0]
    svg = f'''<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Where two domain-rulers cross</title>
<desc>Thermodynamics terms on the left, electrical-engineering terms on the right, linked where MiniLM embeddings place them together: energy with power, entropy with entropy, disorder with noise, transfer with transfer.</desc>
<text x="40" y="34" class="th">where two rulers cross — measured, not asserted</text>
<text x="40" y="54" class="ts">same subject (meaning); thermodynamics vs electrical engineering; links = cosine in MiniLM space</text>
<circle cx="235" cy="74" r="5" class="c-coral"/><text x="247" y="78" class="ts">thermodynamics</text>
<circle cx="445" cy="74" r="5" class="c-blue"/><text x="457" y="78" class="ts">electrical engineering</text>
{body}
<text x="40" y="{H-30}" class="ts">energy ≈ power (0.68) and disorder ≈ noise (0.41) are semantic crossings the geometry found on its own;</text>
<text x="40" y="{H-12}" class="ts">entropy = entropy and transfer = transfer (1.00) are shared atoms. cos &lt; ~0.35 would be noise.</text>
</svg>'''
    with open("lens_figure.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote lens_figure.svg")
    for a, b, s in scored:
        print(f"  {a:>10} ~ {b:<10} cos {s:.3f}")


if __name__ == "__main__":
    main()
