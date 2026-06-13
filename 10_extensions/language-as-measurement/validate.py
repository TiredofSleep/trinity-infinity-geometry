"""validate.py -- put Ruler Spectra on trial. Registered prediction + null + kill.

The honest question: is measuring concepts across designer-chosen rulers REAL
structure, or could random rulers do just as well? We test zero-shot, with a
null that controls for how the probe terms were chosen.

  PROBE: 80 canonical single-domain terms with OBJECTIVE labels (a capacitor is
         electromagnetism by any account, a quark is particle physics) + 12
         held-out bridge terms expected to be crossings.
  TEST 1 (classification): rulers built only from one-line domain descriptions
         classify each probe term by argmax z-response. Accuracy, 8-way.
  NULL : the SAME machinery with random rulers (random word anchors). If random
         rulers classify the probe as well as real ones, the method is vacuous,
         regardless of how I picked terms (the null cancels term-selection bias).
  TEST 2 (crossings): do the 12 bridge terms score higher on their 2nd ruler
         than single-domain terms? AUROC of the crossing-score.

  REGISTERED PREDICTIONS (before running):
    P1  real accuracy >= 0.55           (8-way; chance = 0.125)
    P2  real accuracy > 99th pct of random-ruler accuracy
    P3  bridge-vs-pure crossing AUROC >= 0.70
  KILL CRITERIA (honest negative if any):
    K1  real accuracy <= 0.25           (<= 2x chance -> no real classifier)
    K2  real not separable from random rulers (P2 fails)
    K3  AUROC <= 0.55                   (crossing detector is noise)

  python validate.py
"""
import os
import numpy as np

from embed import embed
from spectra import harvest, RULERS, ruler_dirs

# objective, single-domain canonical terms (membership not in dispute)
PROBE = {
 "thermodynamics":   ["enthalpy", "adiabatic", "isothermal", "calorimetry",
                      "refrigerant", "combustion", "boiling", "condensation",
                      "latent", "thermostat"],
 "electromagnetism": ["capacitor", "inductor", "voltage", "magnet", "solenoid",
                      "resistor", "dielectric", "electrode", "transformer",
                      "antenna"],
 "wave mechanics":   ["oscillation", "resonance", "wavelength", "harmonic",
                      "vibration", "pendulum", "diffraction", "reverberation",
                      "ultrasound", "waveform"],
 "particle physics": ["quark", "lepton", "boson", "fermion", "neutrino",
                      "hadron", "gluon", "muon", "baryon", "antimatter"],
 "information theory":["codeword", "compression", "redundancy", "checksum",
                      "encoding", "decoding", "datastream", "bitrate", "parity",
                      "codebook"],
 "geometry":         ["polygon", "triangle", "polyhedron", "tangent", "vertex",
                      "circle", "ellipse", "perpendicular", "congruent",
                      "hypotenuse"],
 "number theory":    ["divisor", "modulo", "factorial", "coprime", "fibonacci",
                      "totient", "residue", "congruence", "mersenne", "squarefree"],
 "algebra":          ["monoid", "homomorphism", "isomorphism", "determinant",
                      "eigenvector", "commutator", "automorphism", "subgroup",
                      "semigroup", "nilpotent"],
}
BRIDGES = ["entropy", "field", "symmetry", "wave", "operator", "spectrum",
           "energy", "frequency", "group", "charge", "network", "signal"]


def rand_dirs(Epool, rng, k=12):
    names = list(RULERS)
    U = []
    for _ in names:
        a = Epool[rng.integers(len(Epool))]            # random word anchor
        seed = Epool[np.argsort(Epool @ a)[-k:]]
        u = a + seed.mean(0)
        U.append(u / (np.linalg.norm(u) + 1e-12))
    return np.array(U)


def zclass(Et, U, Epool):
    """z-score probe responses against the pool distribution, then argmax."""
    Rp = Epool @ U.T
    mu, sd = Rp.mean(0), Rp.std(0) + 1e-12
    Z = ((Et @ U.T) - mu) / sd
    return Z


def auroc(pos, neg):
    s = np.concatenate([pos, neg]); y = np.concatenate([np.ones(len(pos)), np.zeros(len(neg))])
    o = np.argsort(s); r = np.empty(len(s)); r[o] = np.arange(1, len(s) + 1)
    return float((r[y == 1].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def main(root):
    names = list(RULERS)
    terms, labels = [], []
    for d, dom in enumerate(names):
        for w in PROBE[dom]:
            terms.append(w); labels.append(d)
    labels = np.array(labels)

    pool, files = harvest(root)
    Epool = embed(pool)
    Et = embed(terms)
    Eb = embed(BRIDGES)
    _, U = ruler_dirs(pool, Epool)            # real rulers

    print(f"pool {len(pool)} words / {files} files | probe {len(terms)} single-"
          f"domain terms (8 x 10) + {len(BRIDGES)} bridge terms\n")
    print("REGISTERED: P1 acc>=0.55  P2 acc>99th-pct random  P3 AUROC>=0.70 | "
          "KILL: acc<=0.25, acc~random, AUROC<=0.55\n")

    # TEST 1 -- real accuracy
    Zr = zclass(Et, U, Epool)
    pred = Zr.argmax(1)
    acc = float((pred == labels).mean())

    # NULL -- random-ruler accuracy
    rng = np.random.default_rng(0)
    accs = []
    for _ in range(200):
        Ur = rand_dirs(Epool, rng)
        accs.append(float((zclass(Et, Ur, Epool).argmax(1) == labels).mean()))
    accs = np.array(accs)
    p99 = np.quantile(accs, 0.99)
    pval = float((accs >= acc).mean())

    print("TEST 1 — zero-shot 8-way classification (chance 0.125):")
    print(f"  real rulers      accuracy = {acc:.3f}")
    print(f"  random rulers    mean {accs.mean():.3f}  max {accs.max():.3f}  "
          f"99th pct {p99:.3f}")
    print(f"  real > random    p = {pval:.4f}  ({'PASS' if pval < 0.01 else 'FAIL'})")

    # per-domain accuracy + where it errs
    print("  per-domain recall:")
    for d, dom in enumerate(names):
        m = labels == d
        print(f"    {dom:>18}: {(pred[m]==d).mean():.2f}  "
              f"(misses -> {', '.join(sorted({names[pred[i]] for i in np.where(m)[0] if pred[i]!=d})) or 'none'})")

    # TEST 2 -- bridges score higher on their 2nd ruler than pure terms
    def second(Z):
        s = np.sort(Z, 1); return s[:, -2]
    cs_pure = second(Zr)
    cs_bridge = second(zclass(Eb, U, Epool))
    roc = auroc(cs_bridge, cs_pure)
    print(f"\nTEST 2 — crossing-score (2nd-ruler z) separates bridges from pure:")
    print(f"  pure   mean {cs_pure.mean():.2f} | bridges mean {cs_bridge.mean():.2f}"
          f" | AUROC = {roc:.3f}  ({'PASS' if roc >= 0.70 else 'FAIL'})")
    topb = sorted(zip(cs_bridge, BRIDGES), reverse=True)[:6]
    print(f"  most crossing-like bridges: "
          f"{', '.join(f'{w}({s:.1f})' for s, w in topb)}")

    # VERDICT
    P1, P2, P3 = acc >= 0.55, pval < 0.01, roc >= 0.70
    kill = acc <= 0.25 or not P2 or roc <= 0.55
    print("\n" + "=" * 64)
    print(f"VERDICT: P1 {'ok' if P1 else 'X'} | P2 {'ok' if P2 else 'X'} | "
          f"P3 {'ok' if P3 else 'X'}")
    if kill:
        print("  KILL CRITERION MET — honest negative. Ruler Spectra does not "
              "carry real, non-random classifying structure here.")
    elif P1 and P2 and P3:
        print("  ALL PASS — the rulers carry real structure (far beyond random),"
              " classify zero-shot, and flag bridges as crossings. Worth pursuing.")
    else:
        print("  PARTIAL — real structure beats random, but not every bar cleared"
              " (see X above). Real signal, scoped honestly.")
    print("=" * 64)


if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    main(root)
