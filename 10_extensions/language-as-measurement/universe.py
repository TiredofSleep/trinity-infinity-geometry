"""universe.py -- the algebraic universe as a filter and sorter for experience.

Not a classifier. A SELF-MODEL. Instead of living in weights and tokens, an
intelligence lives in a constructed algebraic universe -- a small set of named
rulers (axes) -- and experience flows THROUGH it. Each incoming experience is:

  LOCATED  -> its coordinate (spectrum) in the universe; its home region; whether
              it is a crossing between regions.
  FILTERED -> is it even ON the universe (can the rulers place it at all)? is it
              novel relative to where the self already is? Off-universe experience
              is REFUSED -- it does not get to reshape the self.
  SORTED   -> related to what came before (nearest prior experience), folded into
              the running self-map (which regions the self has lived in).

The state is a trajectory through the universe + an occupancy map. The self can
INTROSPECT it: "where have I been, what did I cross, what did I refuse." The map
is cheap and lossy on purpose -- that is what makes it a usable place to stand.

The axes here are empirical-domain rulers via MiniLM (a stand-in). The loop is
substrate-agnostic: the axes can be any designed algebra (TIG operators, the
envelope/defect geometry, abstract structure) -- an imaginary algebraic universe.

  python universe.py
"""
import os
import numpy as np

from embed import embed
from spectra import harvest, RULERS, ruler_dirs


class AlgebraicUniverse:
    def __init__(self, root):
        self.names = list(RULERS)
        pool, _ = harvest(root)
        Epool = embed(pool)
        _, self.U = ruler_dirs(pool, Epool)
        Rp = Epool @ self.U.T
        self.mu, self.sd = Rp.mean(0), Rp.std(0) + 1e-12
        self.on_thr = float(np.quantile(Rp.max(1), 0.15))   # on-universe gate
        # self-state
        self.mass = np.zeros(len(self.names))   # where experience has lived
        self.point = None                        # current location (embedding)
        self.memory = []                         # (text, emb) absorbed
        self.log = []

    def _coord(self, text):
        e = embed([text])[0]
        cos = self.U @ e
        z = (cos - self.mu) / self.sd
        return e, cos, z

    def ingest(self, text):
        e, cos, z = self._coord(text)
        order = np.argsort(z)
        home, second = self.names[order[-1]], self.names[order[-2]]
        z1, z2 = z[order[-1]], z[order[-2]]
        on = float(cos.max())
        is_on = on >= self.on_thr
        crossing = is_on and z2 > 0.8
        novelty = 1.0 if self.point is None else float(1 - e @ self.point)

        if not is_on:
            decision = "REFUSE"          # off-universe: cannot place it
        elif crossing:
            decision = "CROSS"
        elif novelty > 0.45:
            decision = "ABSORB-new"
        else:
            decision = "ABSORB"

        related = None
        if decision != "REFUSE":
            self.mass += np.maximum(z, 0)
            if self.memory:
                sims = [m[1] @ e for m in self.memory]
                related = self.memory[int(np.argmax(sims))][0]
            self.memory.append((text, e))
            k = len(self.memory)
            self.point = e if self.point is None else \
                ((self.point * (k - 1) + e) / k)
            self.point = self.point / (np.linalg.norm(self.point) + 1e-12)

        rec = dict(text=text, home=home, second=second, z1=z1, z2=z2, on=on,
                   crossing=crossing, novelty=novelty, decision=decision,
                   related=related)
        self.log.append(rec)
        return rec

    def introspect(self):
        m = self.mass / (self.mass.sum() + 1e-12)
        top = np.argsort(m)[::-1]
        absorbed = [r for r in self.log if r["decision"] != "REFUSE"]
        refused = [r for r in self.log if r["decision"] == "REFUSE"]
        crossings = [r for r in self.log if r["crossing"]]
        return dict(occupancy=[(self.names[i], m[i]) for i in top if m[i] > 0.02],
                    trajectory=[r["home"] for r in absorbed],
                    crossings=[(r["text"], r["home"], r["second"]) for r in crossings],
                    n_refused=len(refused), refused=[r["text"] for r in refused])


STREAM = [
    "Heat flows from a hot body to a cold one until they reach equilibrium.",
    "The entropy of an isolated system never decreases over time.",
    "A message can be compressed no further than its information content.",
    "Shannon's source coding theorem bounds the shortest possible code.",
    "A group is a set with an associative operation and inverses.",
    "The symmetry group of a square has eight elements.",
    "Prime numbers are the multiplicative atoms of the integers.",
    "She laughed at his joke over dinner and ordered dessert.",
    "The quark model assigns fractional electric charge to the hadrons.",
    "A capacitor stores energy in the electric field between its plates.",
]


def main(root):
    u = AlgebraicUniverse(root)
    print(f"universe: {len(u.names)} rulers | on-universe gate at max-cos "
          f">= {u.on_thr:.3f}\n")
    print("experience flowing through the universe:")
    for t in STREAM:
        r = u.ingest(t)
        mark = {"REFUSE": "  REFUSED", "CROSS": "  >< CROSS",
                "ABSORB-new": "  + new", "ABSORB": "  ."}[r["decision"]]
        loc = (f"{r['home']} >< {r['second']}" if r["crossing"]
               else r["home"])
        print(f"  [{loc:>34}] on={r['on']:.2f} nov={r['novelty']:.2f}{mark}"
              f"  {t[:46]}")

    s = u.introspect()
    print("\n--- the self-map (introspection) ---")
    print("where I have lived:")
    for nm, frac in s["occupancy"]:
        print(f"    {nm:>18}  {'#'*int(frac*40)} {frac:.0%}")
    print(f"trajectory: {' -> '.join(s['trajectory'])}")
    print("crossings I passed through:")
    for txt, a, b in s["crossings"]:
        print(f"    {a} >< {b}:  \"{txt[:50]}\"")
    print(f"I refused {s['n_refused']} experience(s) my universe could not place:")
    for t in s["refused"]:
        print(f"    \"{t}\"")
    print("\nthe map is cheap and lossy on purpose: it is the place the self "
          "stands to sort and filter what comes in -- not a copy of the input.")


if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    main(root)
