"""round4.py -- round 4 of PREREG.md, committed with its predictions before the run.

  seven:    toward a proof that no seven-level state beats the record: the best real state (every sign choice
            symmetric under the mirror), a bound on the number of negative points, and ten million climbs.
  eleven:   the true maximum at eleven: more climbs, kicks from the best tops, and exact counts for every
            symmetry of order 4, 5, 6 or 11.
  thirteen: which side wins at thirteen, and on which side a binary tetrahedral group's states can sit.

It uses round3.py's tools (the sign ascent and the exhaustive count).  numpy only.  One process per part, at
below-normal priority and two threads, so the three parts can run at once.  ASCII output; each part writes
round4_<part>.log.
Run:  python round4.py seven      (17 minutes when the three ran at once)
      python round4.py eleven     (43 minutes)
      python round4.py thirteen   (19 minutes)
Set ROUND4_SMOKE=1 for a quick test of the code at a tiny size; its scores mean nothing.
"""
import os
import sys

PART = sys.argv[1] if len(sys.argv) > 1 else "seven"
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import math
import time
from collections import Counter

import numpy as np

import round3 as r3

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261109
SMOKE = os.environ.get("ROUND4_SMOKE") == "1"


def n(x):
    """the number of climbs, kicks or outer steps: as registered, or tiny in the smoke test"""
    return max(x // 5000, 2) if SMOKE else x
LOG = None
T0 = time.time()
SC = {}
mp = np.linalg.matrix_power


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def clock():
    return f"[{time.time() - T0:.0f} s]"


def score(name, held, text):
    SC[name] = bool(held)
    say(f"{name} {'HELD' if held else 'DIED'}: {text}")


# ------------------------------------------------------------------ fast top eigenvalues
def top_eig(H):
    """the largest eigenvalue of each Hermitian matrix in a batch: closed forms for sizes 1, 2 and 3"""
    k = H.shape[-1]
    if k == 1:
        return H[:, 0, 0].real.copy()
    if k == 2:
        a, b, c = H[:, 0, 0].real, H[:, 1, 1].real, H[:, 0, 1]
        return (a + b) / 2 + np.sqrt(((a - b) / 2) ** 2 + np.abs(c) ** 2)
    if k == 3:
        a11, a22, a33 = H[:, 0, 0].real, H[:, 1, 1].real, H[:, 2, 2].real
        a12, a13, a23 = H[:, 0, 1], H[:, 0, 2], H[:, 1, 2]
        q = (a11 + a22 + a33) / 3
        b11, b22, b33 = a11 - q, a22 - q, a33 - q
        n12, n13, n23 = np.abs(a12) ** 2, np.abs(a13) ** 2, np.abs(a23) ** 2
        p = np.sqrt((b11 ** 2 + b22 ** 2 + b33 ** 2 + 2 * (n12 + n13 + n23)) / 6)
        det = b11 * b22 * b33 + 2 * np.real(a12 * a23 * np.conj(a13)) - b11 * n23 - b22 * n13 - b33 * n12
        with np.errstate(invalid="ignore", divide="ignore"):
            r = np.where(p > 1e-14, det / (2 * np.maximum(p, 1e-300) ** 3), 0.0)
        return q + 2 * p * np.cos(np.arccos(np.clip(r, -1.0, 1.0)) / 3)
    return np.linalg.eigvalsh(H)[:, -1]


def exact_best_big(Ak, d, orbits, fixed=None, inner_bits=10 if SMOKE else 20, keep=50):
    """r3.exact_best for large counts: the low `inner_bits` signs are tabulated once, the rest loop outside.
    Returns the best `keep` (value, code) pairs, rechecked with LAPACK, and a function that rebuilds a state."""
    fixed = fixed or {}
    k = Ak.shape[1]
    Bo = np.array([Ak[o].sum(axis=0) for o in orbits]) / d
    free = [j for j in range(len(orbits)) if j not in fixed]
    base = np.zeros((k, k), complex)
    for j, sgn in fixed.items():
        base += sgn * Bo[j]
    nf = len(free)
    ib = min(inner_bits, nf)
    Bf = Bo[free]
    codes_in = np.arange(1 << ib, dtype=np.int64)
    s_in = 1.0 - 2.0 * ((codes_in[:, None] >> np.arange(ib)) & 1)
    H_in = np.tensordot(s_in, Bf[:ib], axes=1)                         # (2^ib, k, k)
    best = []
    for outer in range(min(1 << (nf - ib), 2) if SMOKE else 1 << (nf - ib)):
        s_out = 1.0 - 2.0 * ((outer >> np.arange(nf - ib)) & 1)
        H_out = base + (np.tensordot(s_out, Bf[ib:], axes=1) if nf > ib else 0)
        lam = top_eig(H_in + H_out)
        idx = np.argpartition(lam, -keep)[-keep:] if len(lam) > keep else np.arange(len(lam))
        best += [(float(lam[i]), int(codes_in[i]) | (outer << ib)) for i in idx]
        best = sorted(best, reverse=True)[:keep * 4]

    def rebuild(code):
        s = 1.0 - 2.0 * ((int(code) >> np.arange(nf)) & 1)
        ev, V = np.linalg.eigh(base + np.tensordot(s, Bf, axes=1))
        return V[:, -1], ev[-1]

    best = sorted(((rebuild(c)[1], c) for _, c in best), reverse=True)    # recheck with LAPACK
    return best, rebuild, nf


# ------------------------------------------------------------------ symmetry with mirrors
def mirror_parts(d):
    """for each linear map with determinant -1, the coordinates of S u: the anti-unitary symmetries' maps"""
    q, p = np.divmod(np.arange(d * d), d)
    return [((a * q + b * p) % d, (c * q + e * p) % d) for a in range(d) for b in range(d) for c in range(d)
            for e in range(d) if (a * e - b * c) % d == d - 1]


def carries_ext(W1, W2, d, lins, mirs, tol=1e-7):
    """the same state up to a Clifford operation or a mirror image (an anti-unitary Clifford operation)"""
    return r3.carries(W1, W2, d, lins, tol) or r3.carries(W1, W2, d, mirs, tol)


def counts_ext(W, d, lins, mirs):
    return len(r3.symmetries(W, d, lins)), len(r3.symmetries(W, d, mirs))


# ------------------------------------------------------------------ the Clifford operations that fix the centre
def centre_group(d):
    """SL(2, d) as unitaries up to phase, generated by the Fourier transform, the shear and a primitive multiplier"""
    w, X, Z, F, P, T = r3.basics(d)
    g = next(a for a in range(2, d) if len({pow(a, e, d) for e in range(1, d)}) == d - 1)
    M = np.eye(d)[[(pow(g, -1, d) * k) % d for k in range(d)]]

    def canon(U):
        i = int(np.argmax(np.abs(U.ravel()) > 1e-6))
        return U / (U.ravel()[i] / abs(U.ravel()[i]))

    def key(U):
        return tuple(np.round(np.concatenate([U.real.ravel(), U.imag.ravel()]), 6))

    start = np.eye(d, dtype=complex)
    group, frontier = {key(start): start}, [start]
    while frontier:
        new = []
        for U in frontier:
            for G in (F, T, M):
                V = canon(G @ U)
                if key(V) not in group:
                    group[key(V)] = V
                    new.append(V)
        frontier = new
    return list(group.values())


def tetrahedral_states(d, A):
    """the states fixed (up to phase) by a binary tetrahedral subgroup of SL(2, d): common eigenvectors of two
    generators, an element of order 4 and one of order 3 that together make 24 elements with SL(2, 3)'s orders"""
    G = centre_group(d)
    perms = [r3.perm_of(U, A) for U in G]
    orders = [r3.perm_order(pm) for pm in perms]
    four = [i for i, o in enumerate(orders) if o == 4]
    three = [i for i, o in enumerate(orders) if o == 3]
    profile = {1: 1, 2: 1, 3: 8, 4: 6, 6: 8}
    for a in four[:1]:
        for b in three:
            elems, frontier = {tuple(range(d * d))}, [np.arange(d * d)]
            gens = (perms[a], perms[b])
            while frontier and len(elems) <= 24:
                new = []
                for x in frontier:
                    for gp in gens:
                        y = gp[x]
                        if tuple(y) not in elems:
                            elems.add(tuple(y))
                            new.append(y)
                frontier = new
            if len(elems) == 24 and dict(sorted(Counter(r3.perm_order(np.array(e)) for e in elems).items())) == profile:
                states = []
                for Ea in r3.eigenspaces(G[a]):
                    for Eb in r3.eigenspaces(G[b]):
                        u, s, _ = np.linalg.svd(Ea.conj().T @ Eb)
                        for j in np.where(s > 1 - 1e-8)[0]:
                            states.append(Ea @ u[:, j])
                return states, len(G)
    return None, len(G)


# ------------------------------------------------------------------ part A: seven levels
def part_seven(rng):
    d = 7
    A = r3.phase_points(d)
    lins, mirs = r3.linear_parts(d), mirror_parts(d)
    rec0 = np.array([0.01922811 - 0.08424383j, -0.22656903 + 0.28410857j, 0.06990646 - 0.03366517j, 0.59849409,
                     -0.53922453 - 0.25967686j, -0.04837677 - 0.06066255j, 0.08086155 + 0.35427759j])
    rec = r3.ascend(rec0[None, :].copy(), A, d)[0][0]
    Wrec = r3.wigner(rec[None, :], A, d)[0]
    Nrec = r3.negativity(Wrec)
    lam_rec = 1 + 2 * Nrec
    say(f"seven levels: the record {Nrec:.12f}")

    # every anti-unitary involution is conjugate to the mirror (q, p) -> (q, -p), i.e. to complex conjugation
    q, p = np.divmod(np.arange(d * d), d)
    K = q * d + (-p) % d
    affine = [r3.images(lin, d) for lin in lins]                      # rows: S u + t for every translation t
    conj_K = set()
    for blk in affine:
        for g in blk:
            ginv = np.empty_like(g)
            ginv[g] = np.arange(d * d)
            conj_K.add(tuple(g[K[ginv]]))
    invol = set()
    for blk in [r3.images(m, d) for m in mirs]:
        for g in blk:
            if (g[g] == np.arange(d * d)).all():
                invol.add(tuple(g))
    say(f"  anti-unitary involutions: {len(invol)}; conjugates of the mirror: {len(conj_K)}; the same set: "
        f"{invol == conj_K}")

    # U1: every sign choice symmetric under the mirror (2^28); then H is real
    orbits = [np.array([n]) for n in range(d * d) if K[n] == n] + \
             [np.array([n, K[n]]) for n in range(d * d) if n < K[n]]
    C = np.array([A[o].sum(axis=0).real for o in orbits]) / d       # real symmetric 7 x 7
    assert np.allclose(np.array([A[o].sum(axis=0).imag for o in orbits]), 0)
    m = len(orbits)
    Cf = C.reshape(m, d * d)
    sizes = np.array([len(o) for o in orbits])
    ib = 12 if SMOKE else 20
    codes_in = np.arange(1 << ib, dtype=np.int64)
    bits_in = (codes_in[:, None] >> np.arange(ib)) & 1
    H_in = (1.0 - 2.0 * bits_in) @ Cf[:ib]
    k_in = bits_in @ sizes[:ib]                                        # negative points among the inner orbits
    best, skipped = [], 0
    for outer in range(min(1 << (m - ib), 2) if SMOKE else 1 << (m - ib)):
        bits_out = (outer >> np.arange(m - ib)) & 1
        k = k_in + bits_out @ sizes[ib:]
        keep = np.where((k >= 8) & (k <= 24))[0]                       # outside 8..24 the record is out of reach (U2)
        skipped += (1 << ib) - len(keep)
        if len(keep) == 0:
            continue
        lam = np.linalg.eigvalsh((H_in[keep] + (1.0 - 2.0 * bits_out) @ Cf[ib:]).reshape(-1, d, d))[:, -1]
        kk = min(60, len(lam))
        idx = np.argpartition(lam, -kk)[-kk:]
        best += [(float(lam[i]), int(codes_in[keep[i]]) | (outer << ib)) for i in idx]
        best = sorted(best, reverse=True)[:400]
    top = [c for v, c in best if v > best[0][0] - 1e-9]
    nxt = next(v for v, c in best if v < best[0][0] - 1e-9)
    assert SMOKE or (nxt - 1) / 2 > 5 / 7 + 1e-6                       # so the skipped choices cannot hide a rival
    say(f"  {skipped} of the {2 ** m} choices have fewer than 8 or more than 24 negative points and were skipped")

    def rebuild(code):
        s = 1.0 - 2.0 * ((int(code) >> np.arange(m)) & 1)
        ev, V = np.linalg.eigh(np.tensordot(s, C, axes=1))
        return V[:, -1]

    in_orbit = [carries_ext(Wrec, r3.wigner(rebuild(c)[None, :].astype(complex), A, d)[0], d, lins, mirs)
                for c in top]
    say(f"  all {2 ** m} sign choices symmetric under the mirror: best {(best[0][0] - 1) / 2:.12f}, reached by "
        f"{len(top)} choices, {sum(in_orbit)} of them the record up to symmetry; the next value {(nxt - 1) / 2:.12f}")
    score("U1", abs(best[0][0] - lam_rec) < 1e-9 and all(in_orbit),
          "the best real state is the record, so no state with any symmetry, unitary or anti-unitary, beats it")
    say(clock())

    # U2: the eigenvalue-spread bound on the number of negative points
    def bound(k):
        return (math.sqrt(6 * k * (1 - k / 49)) - k / 7) / 7
    allowed = [k for k in range(1, 49) if bound(k) > Nrec]
    rnd = np.random.default_rng(1)
    worst = 0.0
    for k in range(1, 49):                                             # the bound holds on random sets of each size
        for _ in range(200):
            S = rnd.choice(d * d, size=k, replace=False)
            worst = max(worst, -np.linalg.eigvalsh(A[S].sum(axis=0))[0] / 7 - bound(k))
    score("U2", allowed == list(range(8, 25)) and worst < 1e-12,
          f"a state beating the record has between {allowed[0]} and {allowed[-1]} negative points "
          f"(the bound never fails on 9600 random sets: largest excess {worst:.1e})")

    # U3: ten million climbs
    N7, reps7, stuck = r3.search(A, d, n(10_000_000), rng)
    b7 = N7.max()
    hits = int((N7 > Nrec - 1e-9).sum())
    cnt = Counter(np.round(N7, 9))
    n1 = sum(1 for c in cnt.values() if c == 1)
    say(f"  10000000 climbs: best {b7:.12f}; {hits} reached the record; {len(cnt)} different tops; {n1} reached "
        f"only once, so the unreached tops' basins hold about {n1 / len(N7):.1e} of the starts (Good and Turing); "
        f"{stuck} still moving")
    score("U3", b7 < Nrec + 1e-9 and hits >= 1, "no climb beats the record")
    say("  the twelve highest tops, with how often each was reached, and their symmetries "
        "(unitary, anti-unitary):")
    for v in sorted(reps7, reverse=True)[:12]:
        W = r3.wigner(reps7[v][0][None, :], A, d)[0]
        u, a = counts_ext(W, d, lins, mirs)
        say(f"    {v:.9f} x{cnt[round(v, 9)]}: {u} unitary, {a} anti-unitary; negative points "
            f"{int((W < -1e-12).sum())}")
    say(clock())


# ------------------------------------------------------------------ part B: eleven levels
def part_eleven(rng):
    d = 11
    A = r3.phase_points(d)
    w, X, Z, F, P, T = r3.basics(d)
    E, O = r3.sides(d)
    lins, mirs = r3.linear_parts(d), mirror_parts(d)
    REC = 1.032585792266799
    TET = 1.029706813152930
    Ae, Ao = r3.compress(A, E), r3.compress(A, O)

    Ne, reps_e, st_e = r3.search(Ae, d, n(10_000_000), rng)
    say(f"eleven levels: 10000000 climbs among even states: best {Ne.max():.12f} "
        f"(reached {int((Ne > Ne.max() - 1e-9).sum())} times; {st_e} still moving) {clock()}")
    Nf, reps_f, st_f = r3.search(A, d, n(4_000_000), rng)
    say(f"  4000000 climbs in the whole space: best {Nf.max():.12f} (reached {int((Nf > Nf.max() - 1e-9).sum())} "
        f"times; {st_f} still moving) {clock()}")
    kicked = []
    for v in sorted(reps_f, reverse=True)[:20]:
        psi = reps_f[v][0]
        eps = rng.choice([0.03, 0.1, 0.3, 1.0], size=(n(2000), 1))
        g = rng.normal(size=(n(2000), d)) + 1j * rng.normal(size=(n(2000), d))
        g /= np.linalg.norm(g, axis=1, keepdims=True)
        kicked.append(r3.ascend(psi[None, :] + eps * g, A, d)[1].max())
    say(f"  2000 kicks from each of the 20 highest tops: best {max(kicked):.12f}")
    top_all = max(Ne.max(), Nf.max(), max(kicked))
    score("U4", top_all < REC + 1e-9, f"nothing beats {REC:.6f}: the best found is {top_all:.12f}")
    say(clock())

    # U5: exact counts for the symmetries of order 4, 5, 6 and 11
    def best_fixed(U, name):
        pm = r3.perm_of(U, A)
        orbits = r3.cycles(pm)
        origin = next(i for i, o in enumerate(orbits) if 0 in o)
        top_here = -1.0
        for Q in r3.eigenspaces(U):
            par = np.real(np.trace(Q.conj().T @ P @ Q)) / Q.shape[1]
            fixed = {origin: (1 if par > 0 else -1)} if len(orbits[origin]) == 1 and abs(abs(par) - 1) < 1e-9 else {}
            best, rb, nf = exact_best_big(r3.compress(A, Q), d, orbits, fixed)
            top_here = max(top_here, (best[0][0] - 1) / 2)
        say(f"  states fixed by {name} (order {r3.perm_order(pm)}, {len(orbits)} orbits): the best {top_here:.12f} "
            f"{clock()}")
        return top_here

    M3 = np.eye(d)[[(pow(3, -1, d) * k) % d for k in range(d)]]
    six = next(F @ mp(T, j) for j in range(1, d) if r3.perm_order(r3.perm_of(F @ mp(T, j), A)) == 6)
    found = {"F": best_fixed(F, "the Fourier transform, a quarter turn"),
             "M3": best_fixed(M3, "the multiplier x3"),
             "six": best_fixed(six, "a sixth of a turn"),
             "X": best_fixed(X, "the shift"),
             "T": best_fixed(T, "the shear")}
    seen, moved = set(), []
    for j in range(1, d):
        for a1 in range(d):
            for a2 in range(d):
                U = mp(Z, a2) @ mp(X, a1) @ mp(T, j)
                pm = r3.perm_of(U, A)
                if r3.perm_order(pm) == d and not (pm == np.arange(d * d)).any():
                    pw, elems = np.arange(d * d), []
                    for _ in range(d - 1):
                        pw = pm[pw]
                        elems.append(tuple(pw))
                    if frozenset(elems) not in seen:
                        seen.add(frozenset(elems))
                        moved.append(U)
    found["moved"] = max(max((r3.exact_best(r3.compress(A, Q), d, r3.cycles(r3.perm_of(U, A)))[0][0] - 1) / 2
                             for Q in r3.eigenspaces(U)) for U in moved)
    say(f"  states fixed by a shear with a shift that fixes no point ({len(moved)} groups of order 11): the best "
        f"{found['moved']:.12f}")
    score("U5", max(found.values()) < REC - 1e-9,
          f"no state with a symmetry of order 4, 5, 6 or 11 beats {REC:.6f}: the best has {max(found.values()):.12f}")
    say(clock())

    No, reps_o, st_o = r3.search(Ao, d, n(10_000_000), rng)
    say(f"  10000000 climbs among odd states: best {No.max():.12f} (reached {int((No > No.max() - 1e-9).sum())} "
        f"times; {st_o} still moving)")
    Wo = r3.wigner((O @ reps_o[max(reps_o)][0])[None, :], A, d)[0]
    D = r3.describe(Wo, d, lins)
    score("U6", abs(No.max() - TET) < 1e-9 and D[0] == 24, "the tetrahedral state is still the best odd state found")
    say(clock())

    # U7: tops whose samples a Clifford operation does not carry to each other are mirror images
    split, mended = 0, 0
    for reps, Q in ((reps_e, E), (reps_o, O), (reps_f, np.eye(d))):
        for v in sorted(reps, reverse=True)[:20]:
            Ws = [r3.wigner((Q @ s)[None, :], A, d)[0] for s in reps[v]]
            for W2 in Ws[1:]:
                if not r3.carries(Ws[0], W2, d, lins):
                    split += 1
                    mended += carries_ext(Ws[0], W2, d, lins, mirs)
    score("U7", mended == split, f"of {split} sample pairs no Clifford operation joins, {mended} are mirror images")
    for name, reps, Ns, Q in (("even", reps_e, Ne, E), ("odd", reps_o, No, O), ("whole-space", reps_f, Nf, np.eye(d))):
        say(f"  the {name} climbs' five highest tops: "
            + ", ".join(f"{v:.9f} x{c}" for v, c in sorted(Counter(np.round(Ns, 9)).items(), reverse=True)[:5]))
    say(clock())


# ------------------------------------------------------------------ part C: thirteen levels
def part_thirteen(rng):
    d = 13
    A = r3.phase_points(d)
    w, X, Z, F, P, T = r3.basics(d)
    E, O = r3.sides(d)
    lins, mirs = r3.linear_parts(d), mirror_parts(d)
    L = r3.legendre(d)
    WL = r3.wigner(L[None, :], A, d)[0]
    NL = r3.negativity(WL)
    say(f"thirteen levels: the Legendre state has {NL:.12f}; " +
        "symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, deepest %+.6f"
        % r3.describe(WL, d, lins))
    Ne, reps_e, st_e = r3.search(r3.compress(A, E), d, n(3_000_000), rng)
    No, reps_o, st_o = r3.search(r3.compress(A, O), d, n(3_000_000), rng)
    say(f"  3000000 climbs among even states: best {Ne.max():.12f} (reached {int((Ne > Ne.max() - 1e-9).sum())} "
        f"times); among odd states: best {No.max():.12f} (reached {int((No > No.max() - 1e-9).sum())} times) {clock()}")
    Nf, reps_f, st_f = r3.search(A, d, n(2_000_000), rng)
    say(f"  2000000 climbs in the whole space: best {Nf.max():.12f} (reached {int((Nf > Nf.max() - 1e-9).sum())} "
        f"times) {clock()}")
    even_side = max(Ne.max(), NL)
    score("U8", even_side > No.max() + 1e-6, f"the even side wins at 13: {even_side:.6f} against {No.max():.6f}")
    score("U9", 0 < even_side - No.max() < 0.01, f"by less than 0.01: {even_side - No.max():.6f}")
    Wf = r3.wigner(reps_f[max(reps_f)][0][None, :], A, d)[0]
    Df = r3.describe(Wf, d, lins)
    score("U10", Df[2] == 1 and Df[3] == 0, f"the best state found touches +1/13 at {Df[2]} point(s) and -1/13 at "
          f"{Df[3]}")
    say("    it has: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, deepest %+.6f"
        % Df)
    score("U11", np.allclose(P @ L, L) and Ne.max() > NL + 1e-6,
          f"the Legendre state of 13 is even, and the best even state found beats it: {Ne.max():.6f} against {NL:.6f}")
    sides_ok, lines = True, []
    for p_ in (3, 7, 11, 13):
        Ap = r3.phase_points(p_)
        wp, Xp, Zp, Fp, Pp, Tp = r3.basics(p_)
        states, order = tetrahedral_states(p_, Ap)
        leg = 1 if pow(p_ - 1, (p_ - 1) // 2, p_) == 1 else -1        # the Legendre symbol of -1
        pars = [] if states is None else [round(float(np.real(np.vdot(s, Pp @ s))), 6) for s in states]
        vals = [] if states is None else [float(r3.negativity(r3.wigner(s[None, :], Ap, p_)[0])) for s in states]
        sides_ok &= all(abs(x - leg) < 1e-6 for x in pars)
        found_txt = "was not found" if states is None else f"fixes {len(states)} state(s)"
        lines.append(f"    p = {p_}: SL(2, p) has {order} elements; a binary tetrahedral subgroup {found_txt}"
                     + (f", parities {pars}, total negativities {[round(x, 6) for x in vals]}" if states else "")
                     + f"; the Legendre state's side is {'even' if leg == 1 else 'odd'}")
    score("U12", sides_ok, "every state a binary tetrahedral group fixes lies on the Legendre state's side")
    for ln in lines:
        say(ln)
    alone = r3.fixed_by_symmetry_alone(reps_f[max(reps_f)][0], A, d, lins)
    score("U13", not alone[0], f"the winner at 13 is not fixed by its symmetries alone (residual {alone[1]:.1e})")
    for name, reps, Ns, Q in (("even", reps_e, Ne, E), ("odd", reps_o, No, O), ("whole-space", reps_f, Nf, np.eye(d))):
        say(f"  the {name} climbs' five highest tops: "
            + ", ".join(f"{v:.9f} x{c}" for v, c in sorted(Counter(np.round(Ns, 9)).items(), reverse=True)[:5]))
        for v in sorted(reps, reverse=True)[:2]:
            Ws = [r3.wigner((Q @ s)[None, :], A, d)[0] for s in reps[v]]
            say(f"    top {v:.9f}: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, "
                "deepest %+.6f" % r3.describe(Ws[0], d, lins) + f"; {len(Ws)} samples, one state up to symmetry or "
                f"mirror: {all(carries_ext(Ws[0], W2, d, lins, mirs) for W2 in Ws[1:])}; fixed by its symmetries "
                f"alone: {r3.fixed_by_symmetry_alone(Q @ reps[v][0], A, d, lins)[0]}")
    say(clock())


def main():
    global LOG
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
    except Exception:
        pass
    LOG = open(os.path.join(HERE, f"round4_{PART}.log"), "w", encoding="utf-8")
    rng = np.random.default_rng([SEED, ["seven", "eleven", "thirteen"].index(PART)])
    {"seven": part_seven, "eleven": part_eleven, "thirteen": part_thirteen}[PART](rng)
    say(f"\nROUND 4 ({PART}): {sum(SC.values())} of {len(SC)} held: "
        + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in SC.items()))
    LOG.close()


if __name__ == "__main__":
    main()
