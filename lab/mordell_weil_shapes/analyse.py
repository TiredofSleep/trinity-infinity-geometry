"""analyse.py -- reproduce the lens handoff's Part F tables (20 November 2026) from run_all.py's all_rows.json.

  python -I analyse.py OUT_DIR/all_rows.json

Each line prints the recomputed value and, in brackets, the handoff's.
"""
import json, math, sys
import numpy as np
from scipy import stats
rows = json.load(open(sys.argv[1]))
r2 = [r for r in rows if r["r"] == 2]
N = np.array([r["N"] for r in r2], float)
G = np.array([r["G"] for r in r2], float)
A, B, C = G[:, 0, 0].copy(), G[:, 0, 1].copy(), G[:, 1, 1].copy()
for _ in range(200):                                       # Lagrange-Gauss reduction, vectorized
    sw = A > C; A[sw], C[sw] = C[sw], A[sw]
    k = np.round(B / A); C = C - 2 * k * B + k * k * A; B = B - k * A
sw = A > C; A[sw], C[sw] = C[sw], A[sw]
assert np.all(np.abs(B) <= A / 2 + 1e-12) and np.all(A <= C + 1e-12)
x, y = np.abs(B) / A, np.sqrt(A * C - B * B) / A
dens = math.pi / (4 * y)
tors = np.array([int(np.prod(r["tors"])) if r["tors"] else 1 for r in r2])
tstr = np.array([str(r["tors"]) for r in r2])
iso = np.array([r["iso"] for r in r2])
dsign = np.array([r["disc_sign"] for r in r2])
imtau = np.array([r["tau"][1] for r in r2])
print(f"rank-2 optimal curves: {len(r2)}; conductor {int(N.min())}..{int(N.max())}")
bands = [(1e3, 1e4), (1e4, 3e4), (3e4, 6e4), (6e4, 1e5), (1e5, 2e5), (2e5, 3e5), (3e5, 4e5), (4e5, 5e5)]
hand = [0.2430, 0.2324, 0.2175, 0.2124, 0.2040, 0.1980, 0.1922, 0.1870]
print("thin share (elongation > 2) by band, recomputed vs handoff:")
for (lo, hi), h in zip(bands, hand):
    m = (N >= lo) & (N < hi)
    print(f"  {int(lo):>7}-{int(hi) - 1:<7} n={m.sum():>6}  {np.mean(y[m] > 2):.4f}  (handoff {h:.4f})")
print("by torsion: n, thin share, mean density (handoff: 228531/0.2222/0.544, 46462/0.0982/0.603, 2779/0.0583/0.623, 800/0.0175/0.659, 312/0.0032/0.670)")
for t in ["[]", "[2]", "[3]", "[4]", "[2, 2]", "[5]", "[6]", "[7]", "[8]", "[2, 4]"]:
    m = tstr == t
    if m.sum():
        print(f"  {t:8} n={m.sum():>6}  thin {np.mean(y[m] > 2):.4f}  density {dens[m].mean():.4f}")
lf = (tors == 1) & (iso == 1); il = (tors == 1) & (iso >= 2)
d1, d2 = dens[lf], dens[il]
se = math.sqrt(d1.var(ddof=1) / len(d1) + d2.var(ddof=1) / len(d2))
print(f"hidden loops: no loop n={lf.sum()} {d1.mean():.4f}; isogeny only n={il.sum()} {d2.mean():.4f}; diff {d2.mean() - d1.mean():.4f}, {((d2.mean() - d1.mean()) / se):.1f} s.e. (handoff 223050/0.5434, 5481/0.5835, 18.7 s.e.)")
pos, neg = lf & (dsign > 0), lf & (dsign < 0)
se = math.sqrt(dens[pos].var(ddof=1) / pos.sum() + dens[neg].var(ddof=1) / neg.sum())
print(f"A1 real loop: disc>0 n={pos.sum()} {dens[pos].mean():.4f}; disc<0 n={neg.sum()} {dens[neg].mean():.4f}; {(dens[pos].mean() - dens[neg].mean()) / se:.1f} s.e. (handoff 75482/0.5474, 147568/0.5414, 7.8)")
for lab, m in (("disc>0", pos), ("disc<0", neg)):
    rho = stats.spearmanr(dens[m], imtau[m]).statistic
    print(f"B1 {lab}: Spearman(density, Im tau) = {rho:.3f} (handoff -0.128 / -0.032)")
egg = [r["egg"] for r in r2]
reach = np.array([(e is not None and any(e)) for e in egg])
m_reach, m_miss = pos & reach, pos & ~reach
se = math.sqrt(dens[m_reach].var(ddof=1) / m_reach.sum() + dens[m_miss].var(ddof=1) / m_miss.sum())
print(f"points on the loop: reach n={m_reach.sum()} {dens[m_reach].mean():.4f}; miss n={m_miss.sum()} {dens[m_miss].mean():.4f}; "
      f"{(dens[m_reach].mean() - dens[m_miss].mean()) / se:.1f} s.e.; share missing {m_miss.sum() / pos.sum():.4f} (handoff 73331/0.5481, 2145/0.5254, 6.1, 2.8%)")
print(f"largest elongation {y.max():.2f} at conductor {int(N[y.argmax()])} (handoff 13.17, 383786); counts above 3, 5, 8, 10, 15:",
      [int((y > t).sum()) for t in (3, 5, 8, 10, 15)], "(handoff 15885, 1705, 63, 8, 0)")
print(f"mean density, all rank 2: {dens.mean():.4f} (handoff 0.555); median elongation {np.median(y):.3f}")
# rank 3: lattice vs dual
from cypari import pari
r3 = [r for r in rows if r["r"] == 3]
grid = np.array([(i, j, k) for i in range(-4, 5) for j in range(-4, 5) for k in range(-4, 5) if (i, j, k) != (0, 0, 0)], float)
def minnorm(Gm):
    U = pari.qflllgram(pari.matrix(3, 3, [Gm[i][j] for i in range(3) for j in range(3)]))
    Um = np.array([[float(U[i][j]) for j in range(3)] for i in range(3)])
    Gr = Um.T @ np.array(Gm) @ Um
    return np.einsum("ni,ij,nj->n", grid, Gr, grid).min()
dl, dd = [], []
for r in r3:
    Gm = np.array(r["G"]); det = np.linalg.det(Gm)
    m1 = minnorm(Gm); m2 = minnorm(np.linalg.inv(Gm))
    dl.append(math.pi / 6 * m1 ** 1.5 / math.sqrt(det)); dd.append(math.pi / 6 * m2 ** 1.5 * math.sqrt(det))
dl, dd = np.array(dl), np.array(dd); diff = dl - dd
print(f"rank 3: n={len(r3)}; density lattice {dl.mean():.4f}, dual {dd.mean():.4f}; paired diff {diff.mean():.4f} "
      f"({diff.mean() / (diff.std(ddof=1) / math.sqrt(len(diff))):.1f} s.e.); lattice denser in {np.mean(diff > 0):.3f} "
      f"(handoff 0.3055, 0.3179, -0.0123, -15.6 s.e., 42.9%)")
