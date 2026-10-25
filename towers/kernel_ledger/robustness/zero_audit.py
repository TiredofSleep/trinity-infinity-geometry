#!/usr/bin/env python3
"""
zero_audit.py -- a reusable audit of where a structure's zeros come from, and a robustness test of the design rule
(robustness/PREREG.md, R1-R6). Run from kernel_ledger/robustness/:  python3 zero_audit.py      ASCII only.

audit(G): for a bipartite graph (Hueckel model of a carbon network), returns
  n, sublattice sizes, matching number nu, zero modes (exact integer rank), paid = n - 2nu (Levels 0+2:
  imbalance |N_A - N_B| plus any extra missing pairing), bought = zero modes - paid.
"""
import math, os, random, sys
import numpy as np
import networkx as nx

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(2350)
res = {}

def rank_exact(A):
    A = [list(r) for r in A]; m, n = len(A), len(A[0]); r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        for i in range(m):
            if i != r and A[i][c]:
                f, g = A[r][c], A[i][c]; A[i] = [f * x - g * y for x, y in zip(A[i], A[r])]
                gg = 0
                for x in A[i]: gg = math.gcd(gg, x)
                if gg > 1: A[i] = [x // gg for x in A[i]]
        r += 1
        if r == m: break
    return r

def audit(G):
    nodes = list(G.nodes()); idx = {v: i for i, v in enumerate(nodes)}; n = len(nodes)
    A = [[0] * n for _ in range(n)]
    for u, v in G.edges(): A[idx[u]][idx[v]] = A[idx[v]][idx[u]] = 1
    col = nx.bipartite.color(G); na = sum(1 for v in nodes if col[v] == 0)
    nu = len(nx.max_weight_matching(G, maxcardinality=True))
    zero = n - rank_exact(A); paid = n - 2 * nu
    return {"n": n, "sublattices": (max(na, n - na), min(na, n - na)), "nu": nu, "zero_modes": zero,
            "paid_imbalance": abs(2 * na - n), "paid_pairing": paid - abs(2 * na - n), "bought": zero - paid}

# ---------------- molecules
def flake(hexes):
    verts, edges = {}, set()
    def vid(x, y): return verts.setdefault((round(x, 4) + 0.0, round(y, 4) + 0.0), len(verts))
    for q, r in hexes:
        cx, cy = math.sqrt(3) * (q + r / 2), 1.5 * r
        vs = [vid(cx + math.cos(math.radians(60 * k + 30)), cy + math.sin(math.radians(60 * k + 30))) for k in range(6)]
        for k in range(6): edges.add(tuple(sorted((vs[k], vs[(k + 1) % 6]))))
    G = nx.Graph(); G.add_edges_from(edges); return G

tri3 = flake([(q, r) for q in range(3) for r in range(3) if q + r <= 2])
phen = flake([(0, 0), (1, 0), (0, 1)])
col = nx.bipartite.color(phen); maj = 0 if list(col.values()).count(0) > list(col.values()).count(1) else 1
zvec = np.linalg.svd(nx.to_numpy_array(phen, nodelist=list(phen.nodes())))[2][-1]
deg2_min = next(v for v in phen.nodes() if phen.degree(v) == 2 and col[v] != maj)
dimer = nx.disjoint_union(phen, phen)
dimer.add_edge(list(phen.nodes()).index(deg2_min), len(phen) + list(phen.nodes()).index(deg2_min))
c4 = nx.cycle_graph(4); c12 = nx.cycle_graph(12)
mols = {"[3]triangulene C22": tri3, "phenalenyl dimer (goblet mechanism)": dimer, "cyclobutadiene C4": c4, "[12]annulene C12": c12}
print("ZERO AUDIT (Hueckel graphs; exact ranks)")
aud = {}
for name, G in mols.items():
    a = audit(G); aud[name] = a
    print(f"  {name:38s} n={a['n']:3d} sublattices {a['sublattices'][0]}/{a['sublattices'][1]}  zero modes {a['zero_modes']}"
          f"  paid: imbalance {a['paid_imbalance']} + pairing {a['paid_pairing']}  bought {a['bought']}")

def spectrum(G, delta, kind):
    H = nx.to_numpy_array(G, nodelist=list(G.nodes()))
    if kind == "bond":
        W = np.zeros_like(H)
        for i, j in zip(*np.nonzero(np.triu(H))):
            W[i, j] = W[j, i] = delta * rng.uniform(-1, 1)
        H = H + W
    elif kind == "site":
        H = H + np.diag(delta * rng.uniform(-1, 1, len(H)))
    return np.sort(np.abs(np.linalg.eigvalsh(H)))

deltas = np.logspace(-4, -1, 8)
def slope(G, kind, k=0, trials=50):
    meds = []
    for d in deltas:
        meds.append(np.median([spectrum(G, d, kind)[k] for _ in range(trials)]))
    s = np.polyfit(np.log10(deltas), np.log10(meds), 1)[0]
    return s, meds

# R1: paid-for modes survive bond disorder
r1 = True
for name in ("[3]triangulene C22", "phenalenyl dimer (goblet mechanism)"):
    for d in deltas:
        for _ in range(50):
            e = spectrum(mols[name], d, "bond")
            if not (e[1] < 1e-10 and e[2] > 1e-6): r1 = False
print(f"\nR1 bond disorder, paid-for modes survive in all {len(deltas) * 50} trials each: {r1}")
res["R1"] = r1
curves = {}
s_c4, curves["C4 bought, bond disorder"] = slope(c4, "bond")
s_c12, curves["C12 bought, bond disorder"] = slope(c12, "bond")
s_tri, curves["triangulene paid, on-site disorder"] = slope(tri3, "site")
_, curves["triangulene paid, bond disorder"] = slope(tri3, "bond")
print(f"R2 bought modes, bond disorder: slope C4 {s_c4:.2f}, C12 {s_c12:.2f}")
print(f"R3 paid modes, on-site disorder: slope triangulene {s_tri:.2f}")
res["R2"] = 0.8 <= s_c4 <= 1.2 and 0.8 <= s_c12 <= 1.2
res["R3"] = 0.8 <= s_tri <= 1.2

# ---------------- frames
def rigidity(P, bars):
    R = np.zeros((len(bars), 2 * len(P)))
    for b, (i, j) in enumerate(bars):
        d = P[i] - P[j]; R[b, 2 * i:2 * i + 2] = d; R[b, 2 * j:2 * j + 2] = -d
    return R
def svals(P, bars): return np.linalg.svd(rigidity(P, bars), compute_uv=False)
L = np.array([(-2.0, 0.0), (-3.0, 2.0), (-1.0, 3.0)]); P_sym = np.vstack([L, L * np.array([-1, 1])])
bars_sym = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (0, 3), (1, 4), (2, 5)]       # 9 bars, 6 joints: symmetry-paid
bars_under = bars_sym[:-1]                                                                  # 8 bars: count-paid mechanism
def perturb(P, d, symmetric):
    if symmetric:
        U = rng.normal(size=(3, 2)); U /= np.linalg.norm(U, axis=1, keepdims=True)
        return P + d * np.vstack([U, U * np.array([-1, 1])])
    U = rng.normal(size=P.shape); U /= np.linalg.norm(U, axis=1, keepdims=True)
    return P + d * U
def rank_tol(s, tol=1e-9): return int(np.sum(s > tol * s[0]))
r4 = True; stiff = []
for d in deltas:
    for _ in range(50):
        if rank_tol(svals(perturb(P_sym, d, False), bars_under)) >= 9: r4 = False      # count-paid survives
        if rank_tol(svals(perturb(P_sym, d, True), bars_sym)) != 8: r4 = False         # symmetry-paid survives symmetric
        s_gen = svals(perturb(P_sym, d, False), bars_sym)
        if rank_tol(s_gen) != 9: r4 = False                                            # ...and vanishes generically
    stiff.append(np.median([svals(perturb(P_sym, d, False), bars_sym)[-1] for _ in range(50)]))
s_frame = np.polyfit(np.log10(deltas), np.log10(stiff), 1)[0]
curves["frame symmetry-paid, generic perturbation (sigma_min)"] = stiff
print(f"R4 frames: count-paid survives all, symmetry-paid survives symmetric only: {r4}")
print(f"R5 symmetry-paid mechanism stiffens with slope {s_frame:.2f}")
res["R4"] = r4
res["R5"] = 0.8 <= s_frame <= 1.2

# R6: the audit's labels match the chemistry literature
res["R6"] = aud["cyclobutadiene C4"]["bought"] == 2 and aud["phenalenyl dimer (goblet mechanism)"]["paid_pairing"] == 2
print("R6 cyclobutadiene: bought", aud["cyclobutadiene C4"]["bought"], "; goblet-type dimer: paid by pairing",
      aud["phenalenyl dimer (goblet mechanism)"]["paid_pairing"])

import json
json.dump({"deltas": list(deltas), "curves": {k: [float(x) for x in v] for k, v in curves.items()}},
          open(os.path.join(HERE, "curves.json"), "w"), indent=1)
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
