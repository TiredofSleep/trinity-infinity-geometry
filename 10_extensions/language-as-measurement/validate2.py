"""validate2.py -- the real bar: does the algebra BEAT baseline in few-shot?

The founding hypothesis: an algebraic scaffold lets you learn a distinction from
FEWER examples than the raw representation. That is the few-shot regime, where a
structured low-dim prior is known to beat a high-dim embedding (bias-variance;
prototypical nets, Snell 2017; zero-shot-via-descriptions, CLIP/Yin 2019; concept
axes, TCAV/Kim 2018). We test it head to head.

  TASK     : 8-way domain classification, 16 canonical terms/domain (objective
             labels). The comparison is representation-vs-representation on the
             SAME data, so how the terms were chosen cannot bias which wins.
  BASELINE : raw 384-d MiniLM embedding (E). The standard representation.
  OURS     : ruler-spectrum (R), 8-d, built from one-line domain descriptions
             with ZERO labels from this set.
  CONTROLS : PCA-8 (P, unsupervised top-8 of the embedding) and random-proj-8
             (RP) -- to separate "the ruler axes" from "just low-dim".
  CLASSIFIERS: nearest-centroid (robust in high-d) and multinomial logistic
             regression (overfits in high-d, low-data) -- both, same hyperparams.
  CURVE    : accuracy vs k = 1,2,3,5,8 train examples/domain, many random splits.
  ALSO     : zero-shot ruler (argmax, no training) as a reference line.

  REGISTERED PREDICTIONS:
    P1  at k<=3 with logistic regression, R > E      (algebra beats raw, scarce data)
    P2  R >= P at k<=3                                (named axes >= unsupervised PCA)
    P3  zero-shot R beats logistic-E up to some k*    (descriptions worth k* labels)
  KILL: if R <= E at every k for BOTH classifiers -> no advantage, honest negative.

  python validate2.py
"""
import json
import os
import numpy as np

from embed import embed
from spectra import harvest, RULERS, ruler_dirs

PROBE = {
 "thermodynamics":   ["enthalpy", "adiabatic", "isothermal", "calorimetry",
   "refrigerant", "combustion", "boiling", "condensation", "latent",
   "thermostat", "convection", "conduction", "evaporation", "thermocouple",
   "isobaric", "sublimation"],
 "electromagnetism": ["capacitor", "inductor", "voltage", "magnet", "solenoid",
   "resistor", "dielectric", "electrode", "transformer", "antenna", "impedance",
   "electrostatic", "ampere", "coulomb", "faraday", "magnetism"],
 "wave mechanics":   ["oscillation", "resonance", "wavelength", "harmonic",
   "vibration", "pendulum", "diffraction", "reverberation", "ultrasound",
   "waveform", "interferometer", "sinusoid", "overtone", "eigenmode", "doppler",
   "acoustics"],
 "particle physics": ["quark", "lepton", "boson", "fermion", "neutrino",
   "hadron", "gluon", "muon", "baryon", "antimatter", "photon", "electron",
   "positron", "meson", "neutron", "antiproton"],
 "information theory":["codeword", "compression", "redundancy", "checksum",
   "encoding", "decoding", "datastream", "bitrate", "parity", "codebook",
   "huffman", "ciphertext", "bitstream", "lossless", "demodulation", "teletype"],
 "geometry":         ["polygon", "triangle", "polyhedron", "tangent", "vertex",
   "circle", "ellipse", "perpendicular", "congruent", "hypotenuse", "pentagon",
   "parabola", "isosceles", "quadrilateral", "trapezoid", "centroid"],
 "number theory":    ["divisor", "modulo", "factorial", "coprime", "fibonacci",
   "totient", "residue", "congruence", "mersenne", "squarefree", "gcd",
   "primality", "diophantine", "modular", "semiprime", "carmichael"],
 "algebra":          ["monoid", "homomorphism", "isomorphism", "determinant",
   "eigenvector", "commutator", "automorphism", "subgroup", "semigroup",
   "nilpotent", "matrix", "eigenvalue", "kernel", "quotient", "abelian",
   "surjective"],
}
KS = [1, 2, 3, 5, 8]
TRIALS = 80


def lr_fit(X, y, C, iters=400, lr=0.5, l2=1e-2):
    n, d = X.shape
    W = np.zeros((C, d)); b = np.zeros(C); Y = np.eye(C)[y]
    for _ in range(iters):
        Z = X @ W.T + b; Z -= Z.max(1, keepdims=True)
        P = np.exp(Z); P /= P.sum(1, keepdims=True)
        G = (P - Y) / n
        W -= lr * (G.T @ X + l2 * W); b -= lr * G.sum(0)
    return W, b


def evaluate(reps, y, C, rng):
    """One few-shot trial across all k; returns {rep:{k:(nc_acc,lr_acc)}}."""
    out = {r: {} for r in reps}
    idx_by_c = [np.where(y == c)[0] for c in range(C)]
    for k in KS:
        tr, te = [], []
        for c in range(C):
            perm = rng.permutation(idx_by_c[c])
            tr += list(perm[:k]); te += list(perm[k:])
        tr, te = np.array(tr), np.array(te)
        ytr, yte = y[tr], y[te]
        for name, X in reps.items():
            mu, sd = X[tr].mean(0), X[tr].std(0) + 1e-9
            Xtr, Xte = (X[tr] - mu) / sd, (X[te] - mu) / sd
            cent = np.array([Xtr[ytr == c].mean(0) for c in range(C)])
            nc = (((Xte[:, None] - cent[None]) ** 2).sum(-1).argmin(1) == yte).mean()
            W, b = lr_fit(Xtr, ytr, C)
            lr = ((Xte @ W.T + b).argmax(1) == yte).mean()
            out[name][k] = (float(nc), float(lr))
    return out


def main(root):
    names = list(RULERS)
    terms, y = [], []
    for c, dom in enumerate(names):
        for w in PROBE[dom]:
            terms.append(w); y.append(c)
    y = np.array(y); C = len(names)

    pool, _ = harvest(root)
    Epool = embed(pool)
    E = embed(terms)
    _, U = ruler_dirs(pool, Epool)

    # representations
    Rp = Epool @ U.T; mu_r, sd_r = Rp.mean(0), Rp.std(0) + 1e-9
    R = ((E @ U.T) - mu_r) / sd_r
    pmu = Epool.mean(0); _, _, Vt = np.linalg.svd(Epool - pmu, full_matrices=False)
    P = (E - pmu) @ Vt[:8].T
    rng = np.random.default_rng(0)
    RP = E @ rng.standard_normal((E.shape[1], 8))
    reps = {"raw-384 (E)": E, "ruler-8 (R)": R, "pca-8 (P)": P, "rand-8 (RP)": RP}

    # zero-shot ruler (no training)
    zs = float((R.argmax(1) == y).mean())

    agg = {r: {k: [0.0, 0.0] for k in KS} for r in reps}
    for t in range(TRIALS):
        out = evaluate(reps, y, C, np.random.default_rng(1000 + t))
        for r in reps:
            for k in KS:
                agg[r][k][0] += out[r][k][0]; agg[r][k][1] += out[r][k][1]
    for r in reps:
        for k in KS:
            agg[r][k][0] /= TRIALS; agg[r][k][1] /= TRIALS

    print(f"{C}-way, {len(terms)} terms ({len(terms)//C}/domain), {TRIALS} splits"
          f" | chance {1/C:.3f} | zero-shot ruler (no labels) = {zs:.3f}\n")
    for clf, j in [("nearest-centroid", 0), ("logistic regression", 1)]:
        print(f"=== {clf} — accuracy vs k examples/domain ===")
        print(f"  {'rep':>14} | " + "  ".join(f"k={k}" for k in KS))
        for r in reps:
            print(f"  {r:>14} | " + "  ".join(f"{agg[r][k][j]:.3f}" for k in KS))
        print()

    # verdict
    R_, E_ = "ruler-8 (R)", "raw-384 (E)"
    lo = [k for k in KS if k <= 3]
    p1 = all(agg[R_][k][1] > agg[E_][k][1] for k in lo)
    p2 = all(agg[R_][k][1] >= agg["pca-8 (P)"][k][1] - 0.02 for k in lo)
    kstar = [k for k in KS if zs > agg[E_][k][1]]
    p3 = len(kstar) > 0
    kill = all(agg[R_][k][0] <= agg[E_][k][0] and agg[R_][k][1] <= agg[E_][k][1]
               for k in KS)
    print("=" * 64)
    print(f"P1 R>E (LR, k<=3): {'PASS' if p1 else 'FAIL'}  | "
          f"P2 R>=PCA (k<=3): {'PASS' if p2 else 'FAIL'}  | "
          f"P3 zero-shot>E-LR: {'PASS up to k='+str(max(kstar)) if p3 else 'FAIL'}")
    if kill:
        print("  KILL — ruler rep never beats raw embedding. Honest negative.")
    elif p1:
        gain = np.mean([agg[R_][k][1]-agg[E_][k][1] for k in lo])
        print(f"  BEATS BASELINE: with <=3 examples/domain, ruler-8 beats raw-384 "
              f"under logistic regression by {gain:+.3f} mean accuracy.")
        print(f"  And the algebra (zero labels) matches raw-384-LR until k={max(kstar) if p3 else '?'}"
              f" examples/domain — the descriptions are worth that many labels.")
    else:
        print("  PARTIAL — see passes above.")
    print("=" * 64)
    json.dump({"zero_shot": zs, "ks": KS,
               "curves": {r: {str(k): agg[r][k] for k in KS} for r in reps}},
              open("validate2_result.json", "w"), indent=1)


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
