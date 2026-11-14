"""planes.py -- round 14 of PREREG.md: the triangle's unfolding, the Fano and affine-plane cubics, and the Smith
chart laid over the phase plane; committed with its predictions before the run.

    "if the triangle unfolds to 8 pointed curves under p=5, that makes sense to be a coin. does a triangle unfold to
    other amounts of points at p=n?... do the fano, consider the double smith"  -- the author, 14 November 2026
    "the smith chart from electrical engineering... laid over other planes"  -- the author, 14 November 2026

Three parts, all through round 13's identity (a cubic-phase state's Wigner values are the Walsh spectrum of its cubic
part, cubic_magic.py):
  1. the triangle: the norm form's curve is three conjugate lines with no point over F_p.  At 5 smooth curves with 8
     points tied its negativity.  At 7, 11 and 13, random ternary cubic forms are sampled; for every form that reaches
     the norm form's value the script logs its curve's point count and whether it has a rational singular point;
  2. the planes: the Fano cubic on 7 wheels, the sum of x_i x_j x_k over the 7 lines {i, i+1, i+3} mod 7, at p = 3, 5
     and 7, and the affine-plane cubic on 9 wheels (the 12 lines of AG(2, 3)) at p = 3 and 5, against samples of dense
     random cubics and of sparse random cubics with as many triples;
  3. the Smith chart: the map z -> (z - 1)/(z + 1), as the matrix [[1, -1], [1, 1]] over F_p.  Checked exactly: its
     square is the impedance-admittance flip z -> -1/z and its fourth power the identity; scaled into SL(2, p) when 2 is
     a square; inside the non-split torus (the turning wheel) exactly when p = 7 mod 8, where it has order 8; and at 7
     it generates the whole wheel.
numpy only.  One process, below-normal priority.  ASCII output.
Run:  python planes.py run       (about a quarter of an hour; writes planes_run.log)
      python planes.py combine   (writes planes_combined.log)
"""
import ctypes
import itertools
import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import time

import numpy as np

import cubic_magic as cm

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261115
TRIANGLE = {7: 2_000_000, 11: 1_000_000, 13: 600_000}
FANO = [(i, (i + 1) % 7, (i + 3) % 7) for i in range(7)]
AG23 = []
for a, b in itertools.product(range(3), repeat=2):
    for d in ((1, 0), (0, 1), (1, 1), (1, 2)):
        line = tuple(sorted(((a + k * d[0]) % 3) * 3 + (b + k * d[1]) % 3 for k in range(3)))
        if line not in AG23:
            AG23.append(line)
SAMPLES = {(7, 3): (2000, 2000), (7, 5): (200, 200), (7, 7): (20, 20), (9, 3): (500, 500), (9, 5): (8, 8)}
LOG = None
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def kappa_from_values(C, p, n):
    """S/sqrt q for the cubic-phase state whose cubic part takes the values C on F_p^n (kron order)"""
    q = p ** n
    ph = np.exp(-2j * np.pi * (2 * C % p) / p).reshape((p,) * n)
    S = np.fft.ifftn(ph) * q
    return float(np.abs(S).sum() / q / np.sqrt(q)), S


def triple_values(triples, coeffs, X, p):
    C = np.zeros(len(X), dtype=np.int64)
    for (i, j, k), c in zip(triples, coeffs):
        C = (C + c * X[:, i] * X[:, j] * X[:, k]) % p
    return C


def dense_values(rng, X, p, n):
    top = min(3, p - 1)
    C = np.zeros(len(X), dtype=np.int64)
    for e in itertools.product(range(top + 1), repeat=n):
        if sum(e) == 3:
            c = int(rng.integers(0, p))
            if c:
                term = np.ones(len(X), dtype=np.int64)
                for v, ev in enumerate(e):
                    for _ in range(ev):
                        term = (term * X[:, v]) % p
                C = (C + c * term) % p
    return C


def triangle_part():
    rng = np.random.default_rng([SEED, 1])
    for p, count in TRIANGLE.items():
        mons, Mv = cm.monomial_values(p, 3)
        Nn = cm.negativities(cm.norm_coeffs(p)[None, :], Mv, p, 3)[0][0]
        pts, sing, hits, hist = {}, {}, 0, {}
        batch = 4096 if p <= 7 else 2048
        for _ in range(count // batch):
            c = rng.integers(0, p, (batch, len(mons)))
            N, _ = cm.negativities(c, Mv, p, 3)
            Cv = (c @ Mv) % p
            k = ((Cv == 0).sum(axis=1) - 1) // (p - 1)
            for v in np.round(N, 6):
                hist[v] = hist.get(v, 0) + 1
            for i in np.where(np.abs(N - Nn) < 1e-9)[0]:
                hits += 1
                pts[int(k[i])] = pts.get(int(k[i]), 0) + 1
                if k[i] > 0:
                    sing[int(k[i])] = sing.get(int(k[i]), 0) + int(rational_singular(c[i], mons, p) > 0)
        above = sum(v for key, v in hist.items() if key > round(Nn, 6))
        say(f"TRIANGLE {p} {count} {Nn:.12f} {hits} {above} " + ";".join(f"{k}:{v}:{sing.get(k, 0)}" for k, v in sorted(pts.items())))


def rational_singular(c, mons, p):
    X = cm.points(p, 3)
    C = np.zeros(len(X), dtype=np.int64)
    grads = [np.zeros(len(X), dtype=np.int64) for _ in range(3)]
    for cc, e in zip(c, mons):
        if not cc:
            continue
        C = (C + cc * np.prod(X ** np.array(e), axis=1)) % p
        for v in range(3):
            if e[v]:
                e2 = list(e)
                e2[v] -= 1
                grads[v] = (grads[v] + cc * e[v] * np.prod(X ** np.array(e2), axis=1)) % p
    mask = (C == 0) & (grads[0] == 0) & (grads[1] == 0) & (grads[2] == 0)
    return int((mask.sum() - 1) // (p - 1))


def planes_part():
    rng = np.random.default_rng([SEED, 2])
    for (n, p), (dense, sparse) in SAMPLES.items():
        X = cm.points(p, n)
        lines = FANO if n == 7 else AG23
        k_plane, S = kappa_from_values(triple_values(lines, [1] * len(lines), X, p), p, n)
        nvals = len(np.unique(np.round(S.real / p ** n, 7)))
        allt = list(itertools.combinations(range(n), 3))
        k_sparse = []
        for _ in range(sparse):
            pick = rng.choice(len(allt), len(lines), replace=False)
            k_sparse.append(kappa_from_values(triple_values([allt[i] for i in pick], [1] * len(lines), X, p), p, n)[0])
        k_dense = [kappa_from_values(dense_values(rng, X, p, n), p, n)[0] for _ in range(dense)]
        say(f"PLANE {n} {p} {'fano' if n == 7 else 'ag23'} {k_plane:.9f} {nvals} {max(k_dense):.9f} {np.mean(k_dense):.6f} "
            f"{max(k_sparse):.9f} {np.mean(k_sparse):.6f} [{time.time() - T0:.0f} s]")


def smith_part():
    ok = True
    G = np.array([[1, -1], [1, 1]])
    ok &= np.array_equal(G @ G, np.array([[0, -2], [2, 0]]))                # twice z -> -1/z
    ok &= np.array_equal(np.linalg.matrix_power(G, 4), -4 * np.eye(2, dtype=int))   # a scalar: the identity map
    rows = []
    for p in [x for x in range(5, 200) if all(x % d for d in range(2, int(x ** 0.5) + 1))]:
        r2 = next((r for r in range(1, p) if r * r % p == 2), None)
        if r2 is None:
            rows.append((p, None))
            continue
        S = (np.array([[1, -1], [1, 1]], dtype=np.int64) * pow(r2, -1, p)) % p   # det 1
        M, order = S.copy(), 1
        while not np.array_equal(M, np.eye(2, dtype=np.int64)):
            M, order = (M @ S) % p, order + 1
        disc = (int(np.trace(S)) ** 2 - 4) % p                             # the characteristic polynomial's discriminant
        nonsplit = pow(disc, (p - 1) // 2, p) == p - 1
        rows.append((p, (order, nonsplit)))
    in_ns = [p for p, r in rows if r and r[1]]
    ok &= all(p % 8 == 7 for p in in_ns) and all(r[0] == 8 for p, r in rows if r)
    ok &= all((r is not None) == (p % 8 in (1, 7)) for p, r in rows)
    ok &= [p for p in in_ns if p + 1 == 8] == [7]
    say(f"SMITH {ok} " + ",".join(str(p) for p in in_ns))


def run():
    global LOG
    LOG = open(os.path.join(HERE, "planes_run.log"), "w", encoding="utf-8")
    say("round 14: the triangle, the planes and the Smith chart")
    say("TRIANGLE p sampled norm_value hits above point_count:forms:with_rational_singular_point")
    say("PLANE wheels p plane kappa distinct_values dense_max dense_mean sparse_max sparse_mean")
    smith_part()
    planes_part()
    triangle_part()
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


def combine():
    global LOG
    tri, pl, smith = {}, {}, None
    for line in open(os.path.join(HERE, "planes_run.log"), encoding="utf-8"):
        f = line.split()
        if line.startswith("TRIANGLE ") and f[1].isdigit():
            parts = {}
            for item in (f[6].split(";") if len(f) > 6 else []):
                k, v, s = map(int, item.split(":"))
                parts[k] = (v, s)
            tri[int(f[1])] = dict(N=float(f[3]), hits=int(f[4]), above=int(f[5]), parts=parts)
        elif line.startswith("PLANE ") and f[1].isdigit():
            pl[int(f[1]), int(f[2])] = dict(k=float(f[4]), nvals=int(f[5]), dmax=float(f[6]), smax=float(f[8]))
        elif line.startswith("SMITH "):
            smith = f[1] == "True"
    LOG = open(os.path.join(HERE, "planes_combined.log"), "w", encoding="utf-8")
    for p, t in sorted(tri.items()):
        say(f"  three wheels of {p}: norm value {t['N']:.9f}; {t['hits']} sampled forms reach it, {t['above']} exceed it; "
            f"their curves' point counts: " + ", ".join(f"{k} points ({v} forms, {s} with a rational singular point)"
                                                       for k, (v, s) in sorted(t["parts"].items())))
    for (n, p), r in sorted(pl.items()):
        say(f"  {n} wheels of {p}: the {'Fano' if n == 7 else 'affine-plane'} cubic's S/sqrt q {r['k']:.6f} ({r['nvals']} "
            f"values); dense random best {r['dmax']:.6f}; sparse random best {r['smax']:.6f}")
    ties = {p: [k for k in t["parts"] if k > 0] for p, t in tri.items()}
    T1 = bool(ties.get(11)) and not ties.get(7) and not ties.get(13)
    T2 = all(k == p + 3 and tri[p]["parts"][k][1] == 0 for p, ks in ties.items() for k in ks) and any(ties.values())
    F1 = all(pl[7, p]["k"] > max(pl[7, p]["dmax"], pl[7, p]["smax"]) for p in (3, 5, 7))
    F2 = all(pl[7, p]["k"] > 8 / (3 * np.pi) for p in (5, 7))
    F3 = all(pl[9, p]["k"] > pl[9, p]["dmax"] for p in (3, 5))
    for name, ok, what in (
            ("S0", smith, "the Smith chart's facts, exactly (forced)"),
            ("T1", T1, "the triangle unfolds at 11 (2 more than a multiple of 3) and not at 7 or 13"),
            ("T2", T2, "every non-norm form that ties the norm value is a curve with p + 3 points and no rational singular point"),
            ("F1", F1, "on 7 wheels at 3, 5 and 7 the Fano cubic beats every sampled dense and sparse cubic"),
            ("F2", F2, "the Fano cubic's S/sqrt q exceeds Sato-Tate's 8/(3 pi) at 5 and 7"),
            ("F3", F3, "on 9 wheels at 3 and 5 the affine-plane cubic beats every sampled dense cubic")):
        say(f"{name} {'HELD' if ok else 'DIED'}: {what}")
    LOG.close()


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "run"
    {"run": run, "combine": combine}[part]()
