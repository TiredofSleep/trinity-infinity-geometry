"""round3.py -- round 3 of PREREG.md, committed with its predictions before the run.
The three questions round 2 left open:

  A. Is 0.732522 the largest total negativity at seven levels?
  B. Is the Legendre state the best odd state?
  C. Which side wins at eleven levels?

Both tools rest on one identity: sum_u |W_u| is the largest value of sum_u s_u W_u over sign choices s_u = +-1.
  - The sign ascent. Give each phase-space point the sign of the state's Wigner value there, and replace the state
    by the top eigenvector of sum_u s_u A_u. No step lowers sum |W|, so every start climbs to a local maximum.
  - The exhaustive count. If a symmetry g fixes a state, its signs are constant on g's orbits in phase space. So
    the best state fixed by g is the best top eigenvector, inside g's eigenspace, over sign choices constant on
    those orbits. For the half turn at seven levels that is 2^24 sign choices on each side, and all are tried.

numpy (and sympy for the exact polynomials).  One process at below-normal priority, at most four threads.
ASCII output; also written to round3.log.
Run:  python round3.py      (about seven minutes; seeded, so a rerun repeats it)
After the first run, the unscored section gained the exact polynomials and the recorded states, and the wording of
T8's output line was corrected. The scored code did not change, and a second run repeated every scored line.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "4")                                     # gentle: at most four threads
import ctypes
import math
import time
from collections import Counter

import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261108
LOG = None


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


# ------------------------------------------------------------------ the setting, for an odd prime d
def basics(d):
    w = np.exp(2j * np.pi / d)
    k = np.arange(d)
    X = np.roll(np.eye(d), 1, axis=0)                                  # X|k> = |k+1>
    Z = np.diag(w ** k)                                                # Z|k> = w^k |k>
    F = w ** (np.outer(k, k) % d) / np.sqrt(d)
    P = np.eye(d)[(-k) % d]                                            # P|k> = |-k>, the half turn
    T = np.diag(w ** ((pow(2, -1, d) * k * k) % d))                    # the quadratic phase (a shear)
    return w, X, Z, F, P, T


def phase_points(d):
    """A[q*d + p] = Z^p X^q P X^-q Z^-p, which sends |m> to w^(2p(q - m)) |2q - m>.  A[0] is the half turn."""
    w = np.exp(2j * np.pi / d)
    A = np.zeros((d * d, d, d), complex)
    m = np.arange(d)
    for q in range(d):
        for p in range(d):
            A[q * d + p, (2 * q - m) % d, m] = w ** ((2 * p * (q - m)) % d)
    return A


def sides(d):
    """orthonormal bases of the even and the odd states under the half turn"""
    E = np.zeros((d, (d + 1) // 2))
    O = np.zeros((d, (d - 1) // 2))
    E[0, 0] = 1
    for j in range(1, (d + 1) // 2):
        E[j, j] = E[d - j, j] = 1 / np.sqrt(2)
        O[j, j - 1], O[d - j, j - 1] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return E.astype(complex), O.astype(complex)


def legendre(d):
    chi = np.array([0] + [1 if pow(k, (d - 1) // 2, d) == 1 else -1 for k in range(1, d)], complex)
    return chi / np.linalg.norm(chi)


def compress(A, Q):
    return np.einsum("ia,nij,jb->nab", Q.conj(), A, Q)


def wigner(Phi, Ak, d):
    """Phi: (B, k) unit vectors in a k-dimensional subspace; Ak: the phase-point operators there.  W: (B, d*d)."""
    k = Ak.shape[1]
    R = (Phi.conj()[:, :, None] * Phi[:, None, :]).reshape(len(Phi), k * k)
    return (R @ Ak.reshape(len(Ak), k * k).T).real / d


def negativity(W):
    return (np.abs(W).sum(axis=-1) - 1) / 2


# ------------------------------------------------------------------ tool 1: the sign ascent
def ascend(Phi, Ak, d, max_steps=1000):
    """climb from each row of Phi; returns the end states, their total negativities and the number still moving"""
    Phi = Phi / np.linalg.norm(Phi, axis=1, keepdims=True)
    B, k = Phi.shape
    Af = Ak.reshape(len(Ak), k * k)
    signs = np.zeros((B, len(Ak)))
    live = np.arange(B)
    for _ in range(max_steps):
        W = wigner(Phi[live], Ak, d)
        s = np.where(W >= 0, 1.0, -1.0)
        moving = ~(s == signs[live]).all(axis=1)                       # the signs changed, so not yet at the top
        live, s = live[moving], s[moving]
        if len(live) == 0:
            break
        _, V = np.linalg.eigh((s @ Af).reshape(len(live), k, k) / d)
        Phi[live] = V[:, :, -1]
        signs[live] = s
    return Phi, negativity(wigner(Phi, Ak, d)), len(live)


def search(Ak, d, starts, rng, batch=20000, tops=60):
    """the sign ascent from uniformly random states.  Returns every end value, up to three end states for each of
    the highest `tops` distinct values (rounded to 1e-9), and how many starts were still moving at the step cap."""
    k = Ak.shape[1]
    values, reps, stuck = [], {}, 0
    for b in range(0, starts, batch):
        n = min(batch, starts - b)
        Phi0 = rng.normal(size=(n, k)) + 1j * rng.normal(size=(n, k))
        Phi, N, left = ascend(Phi0, Ak, d)
        values.append(N)
        stuck += left
        keys, first = np.unique(np.round(N, 9), return_index=True)
        for key, i in zip(keys[-tops:], first[-tops:]):
            if len(reps.setdefault(float(key), [])) < 3:
                reps[float(key)].append(Phi[i])
        for key in sorted(reps)[:-tops]:
            del reps[key]
    return np.concatenate(values), reps, stuck


# ------------------------------------------------------------------ tool 2: the exhaustive count
def exact_best(Ak, d, orbits, fixed=None, chunk=1 << 18, keep=600):
    """the top eigenvalues of sum_u s_u Ak_u / d over all sign choices constant on each orbit (some signs fixed).
    Returns the best `keep` values per chunk, merged and sorted, with their codes, and a way to rebuild a state."""
    fixed = fixed or {}
    k = Ak.shape[1]
    Bo = np.array([Ak[o].sum(axis=0) for o in orbits]) / d
    free = [j for j in range(len(orbits)) if j not in fixed]
    base = np.zeros((k, k), complex)
    for j, sgn in fixed.items():
        base += sgn * Bo[j]
    Bf = Bo[free].reshape(len(free), k * k)
    Br, Bi = Bf.real.copy(), Bf.imag.copy()
    nf = len(free)
    shifts = np.arange(nf, dtype=np.int64)
    vals, codes = [], []
    for start in range(0, 1 << nf, chunk):
        c = np.arange(start, min(start + chunk, 1 << nf), dtype=np.int64)
        s = 1.0 - 2.0 * ((c[:, None] >> shifts) & 1)
        lam = np.linalg.eigvalsh((s @ Br + 1j * (s @ Bi)).reshape(-1, k, k) + base)[:, -1]
        idx = np.argpartition(lam, -keep)[-keep:] if len(lam) > keep else np.arange(len(lam))
        vals.append(lam[idx])
        codes.append(c[idx])
    vals, codes = np.concatenate(vals), np.concatenate(codes)
    order = np.argsort(-vals)

    def rebuild(code):
        s = 1.0 - 2.0 * ((int(code) >> np.arange(nf)) & 1)
        H = base + np.tensordot(s, Bo[free], axes=1)
        ev, V = np.linalg.eigh(H)
        return V[:, -1], ev[-1]

    return vals[order], codes[order], rebuild, nf


def half_turn_orbits(d):
    q, p = np.divmod(np.arange(d * d), d)
    minus = ((-q) % d) * d + (-p) % d
    return [np.array([0])] + [np.array([n, minus[n]]) for n in range(1, d * d) if n < minus[n]]


# ------------------------------------------------------------------ symmetry in phase space
def sl2(d):
    return [(a, b, c, e) for a in range(d) for b in range(d) for c in range(d) for e in range(d)
            if (a * e - b * c) % d == 1]


def linear_parts(d):
    """for each S in SL(2, d), the coordinates of S u for every point u"""
    q, p = np.divmod(np.arange(d * d), d)
    return [((a * q + b * p) % d, (c * q + e * p) % d) for a, b, c, e in sl2(d)]


def images(lin, d):
    """for one linear part: row t holds the index of S u + t for every point u, over all translations t"""
    t1, t2 = np.divmod(np.arange(d * d), d)
    return ((lin[0][None, :] + t1[:, None]) % d) * d + (lin[1][None, :] + t2[:, None]) % d


def symmetries(W, d, lins, tol=1e-7):
    """the affine symplectic maps g with W(g u) = W(u) for every u: the state's Clifford symmetries, up to phase"""
    out = []
    for lin in lins:
        idx = images(lin, d)
        ok = np.abs(W[idx] - W[None, :]).max(axis=1) < tol
        out += [idx[j] for j in np.where(ok)[0]]
    return out


def carries(W1, W2, d, lins, tol=1e-7):
    """is there an affine symplectic g with W2(g u) = W1(u)?  Then a Clifford operation carries one state to the
    other"""
    if np.abs(np.sort(W1) - np.sort(W2)).max() > tol:
        return False
    return any((np.abs(W2[images(lin, d)] - W1[None, :]).max(axis=1) < tol).any() for lin in lins)


def perm_order(perm):
    seen, L = np.zeros(len(perm), bool), 1
    for i in range(len(perm)):
        n, j = 0, i
        while not seen[j]:
            seen[j], j, n = True, perm[j], n + 1
        if n:
            L = L * n // math.gcd(L, n)
    return L


def cycles(perm):
    seen, out = np.zeros(len(perm), bool), []
    for i in range(len(perm)):
        if not seen[i]:
            cyc, j = [], i
            while not seen[j]:
                seen[j] = True
                cyc.append(j)
                j = perm[j]
            out.append(np.array(cyc))
    return out


def perm_of(U, A):
    """the phase-space map of a Clifford unitary: U A(u) U^dagger = A(g u)"""
    d = U.shape[0]
    B = np.einsum("ij,njk,lk->nil", U, A, U.conj())
    ov = np.einsum("nij,mij->nm", B, A.conj()).real
    perm = ov.argmax(axis=1)
    assert np.allclose(ov[np.arange(len(A)), perm], d, atol=1e-8), "not a Clifford operation"
    return perm


def eigenspaces(U, tol=1e-6):
    ev, V = np.linalg.eig(U)
    out, used = [], np.zeros(len(ev), bool)
    for i in range(len(ev)):
        if not used[i]:
            g = np.where(np.abs(ev - ev[i]) < tol)[0]
            used[g] = True
            Q, _ = np.linalg.qr(V[:, g])
            assert np.allclose(U @ Q, ev[i] * Q, atol=1e-8)
            out.append(Q)
    assert sum(Q.shape[1] for Q in out) == U.shape[0]
    return out


def describe(W, d, lins):
    """symmetry count, element orders, and where the state touches the ceiling +1/d or the floor -1/d"""
    sym = symmetries(W, d, lins)
    orders = Counter(perm_order(g) for g in sym)
    up = int((np.abs(W - 1 / d) < 1e-9).sum())
    down = int((np.abs(W + 1 / d) < 1e-9).sum())
    return len(sym), dict(sorted(orders.items())), up, down, int((W < -1e-12).sum()), W.min()


# ------------------------------------------------------------------ one exact polynomial
def minimal_polynomial(signs, d, side, target):
    """the exact minimal polynomials of x = d * sum|W| = d(1 + 2N) and of N, for a state on one side whose sign
    pattern is `signs`.  The pattern is symmetric, so d*H = sum_u s_u A_u (entries in Z[w]) splits into an even and an
    odd block; the block is taken on an integer basis, and the norm down to Q is the product over the conjugates
    w -> w^g, g = 1, ..., (d-1)/2."""
    import sympy as sp
    w, x, n = sp.symbols("w x n")
    cyc = sp.Poly(sum(w ** j for j in range(d)), w)
    H = [[0] * d for _ in range(d)]
    for q in range(d):
        for p in range(d):
            for m in range(d):
                H[(2 * q - m) % d][m] += int(signs[q * d + p]) * w ** ((2 * p * (q - m)) % d)
    half = (d - 1) // 2
    V = [[0] * (half + (side == "even")) for _ in range(d)]            # |0>, |j> + |-j>  or  |j> - |-j>
    if side == "even":
        V[0][0] = 1
    for j in range(1, half + 1):
        c = j - (side == "odd")
        V[j][c], V[d - j][c] = 1, (1 if side == "even" else -1)
    V = sp.Matrix(V)
    M = (V.T * V).inv() * V.T * sp.Matrix(H) * V
    M = M.applyfunc(lambda e: sp.rem(sp.Poly(sp.expand(e), w), cyc).as_expr() if e != 0 else 0)
    coeffs = [sp.rem(sp.Poly(sp.expand(c), w), cyc).as_expr() for c in sp.Poly(M.charpoly(x).as_expr(), x).all_coeffs()]
    norm = 1
    for g in range(1, half + 1):
        norm *= sum(sp.expand(c.subs(w, w ** g)) * x ** (len(coeffs) - 1 - i) for i, c in enumerate(coeffs))
    red = [sp.rem(sp.Poly(c, w), cyc).as_expr() for c in sp.Poly(sp.expand(norm), x).all_coeffs()]
    assert all(c.is_Rational for c in red), "the norm should have rational coefficients"
    poly = sp.Poly(sum(c * x ** (len(red) - 1 - i) for i, c in enumerate(red)), x)
    lam = d * (1 + 2 * target)
    err, f = min(((min(abs(complex(rt) - lam) for rt in sp.Poly(f, x).nroots(n=40)), f)
                  for f, _ in sp.factor_list(poly)[1]), key=lambda t: t[0])
    fx = sp.Poly(f, x).monic()
    g = sp.Poly(sp.primitive(fx.as_expr().subs(x, d * (1 + 2 * n)))[1], n)
    return fx, (-g if g.LC() < 0 else g), err


def centred(psi, A, d):
    """move the state's single ceiling or floor point, if it has one, to the centre; make its largest amplitude real"""
    W = wigner(psi[None, :], A, d)[0]
    ext = np.where(np.abs(np.abs(W) - 1 / d) < 1e-9)[0]
    if len(ext) == 1:
        w, X, Z, F, P, T = basics(d)
        q0, p0 = divmod(int(ext[0]), d)
        psi = (np.linalg.matrix_power(Z, p0) @ np.linalg.matrix_power(X, q0)).conj().T @ psi
    psi = psi / np.linalg.norm(psi)
    return psi * np.exp(-1j * np.angle(psi[int(np.argmax(np.abs(psi)))]))


def fixed_by_symmetry_alone(psi, A, d, lins):
    """is the state the only one its symmetries fix (in its own eigenvalue type)?  The operators that commute with
    its symmetries are spanned by the sums of A_u over the symmetry orbits; it is the only one exactly when it is an
    eigenvector of every such sum.  Returns that verdict and the largest residual."""
    W = wigner(psi[None, :], A, d)[0]
    sym = symmetries(W, d, lins)
    label, changed = np.arange(d * d), True
    while changed:                                                     # label each point by its orbit's least point
        changed = False
        for g in sym:
            new = np.minimum(label, label[g])
            if (new != label).any():
                label, changed = new, True
    worst = 0.0
    for o in np.unique(label):
        v = A[label == o].sum(axis=0) @ psi
        worst = max(worst, np.linalg.norm(v - np.vdot(psi, v) * psi))
    return worst < 1e-8, worst


def amplitudes(psi):
    return ", ".join(f"{z.real:+.10f}{z.imag:+.10f}i" for z in psi)


# ------------------------------------------------------------------ the round
def main():
    global LOG
    LOG = open(os.path.join(HERE, "round3.log"), "w", encoding="utf-8")
    rng = np.random.default_rng(SEED)
    t0 = time.time()
    SC = {}

    def clock():
        return f"[{time.time() - t0:.0f} s]"

    # ---------------------------------------------------------- three levels: T1
    d = 3
    A = phase_points(d)
    E, O = sides(d)
    orb = half_turn_orbits(d)
    ve, _, _, _ = exact_best(compress(A, E), d, orb, {0: +1})
    vo, _, _, _ = exact_best(compress(A, O), d, orb, {0: -1})
    ne, no = (ve[0] - 1) / 2, (vo[0] - 1) / 2
    say(f"three levels: the best even state {ne:.12f}, the best odd state {no:.12f} "
        f"(all {2 ** (len(orb) - 1)} sign choices on each side)")
    SC["T1"] = abs(ne - 1 / 3) < 1e-9 and abs(no - 1 / 3) < 1e-9
    say(f"T1 {'HELD' if SC['T1'] else 'DIED'}: both sides reach 1/3 = {1 / 3:.12f}")

    # ---------------------------------------------------------- five levels: T2
    d = 5
    A = phase_points(d)
    E, O = sides(d)
    orb = half_turn_orbits(d)
    lins5 = linear_parts(d)
    jp = (np.sqrt(5) - 2 + np.sqrt(15 + 6 * np.sqrt(5))) / 10           # Jain and Prakash's maximum, as negativity
    ve, ce, rb_e, _ = exact_best(compress(A, E), d, orb, {0: +1})
    vo, co, rb_o, _ = exact_best(compress(A, O), d, orb, {0: -1})
    ne, no = (ve[0] - 1) / 2, (vo[0] - 1) / 2
    N5, reps5, stuck5 = search(A, d, 200000, rng)
    b5 = N5.max()
    say(f"\nfive levels: Jain and Prakash's maximum (sqrt5 - 2 + sqrt(15 + 6 sqrt5))/10 = {jp:.12f}")
    say(f"  the best even state {ne:.12f}; the best odd state {no:.12f} (all {2 ** (len(orb) - 1)} sign choices each)")
    say(f"  200000 sign ascents: best {b5:.12f}; {int((N5 > b5 - 1e-9).sum())} reached it; {stuck5} still moving")
    SC["T2"] = abs(ne - jp) < 1e-9 and no < jp + 1e-9 and abs(b5 - jp) < 1e-6
    say(f"T2 {'HELD' if SC['T2'] else 'DIED'}: nothing beats {jp:.6f}, and the best even state reaches it")
    phi, _ = rb_e(ce[0])
    W = wigner((E @ phi)[None, :], A, d)[0]
    say("  the best even ququint state: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points "
        "%d, deepest %+.6f" % describe(W, d, lins5))
    phi, _ = rb_o(co[0])
    W = wigner((O @ phi)[None, :], A, d)[0]
    say("  the best odd ququint state: symmetries %d, orders %s, ceiling points %d, floor points %d, negative "
        "points %d, deepest %+.6f" % describe(W, d, lins5))
    L5 = legendre(5)
    W = wigner(L5[None, :], A, d)[0]
    say(f"  the Legendre state of 5 (even here) has {negativity(W):.6f}; " +
        "symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, deepest %+.6f"
        % describe(W, d, lins5))
    say(clock())

    # ---------------------------------------------------------- seven levels: T3 - T6
    d = 7
    A = phase_points(d)
    w, X, Z, F, P, T = basics(d)
    E, O = sides(d)
    orb = half_turn_orbits(d)
    lins7 = linear_parts(d)
    rec0 = np.array([0.01922811 - 0.08424383j, -0.22656903 + 0.28410857j, 0.06990646 - 0.03366517j, 0.59849409,
                     -0.53922453 - 0.25967686j, -0.04837677 - 0.06066255j, 0.08086155 + 0.35427759j])
    rec, Nrec, _ = ascend(rec0[None, :].copy(), A, d)                  # polish round 2's record to its exact top
    rec, Nrec = rec[0], Nrec[0]
    Wrec = wigner(rec[None, :], A, d)[0]
    L7 = legendre(d)
    WL = wigner(L7[None, :], A, d)[0]
    NL = negativity(WL)
    say(f"\nseven levels: the round-2 record, polished, {Nrec:.12f}; the Legendre state {NL:.12f} "
        f"= (4cos(2pi/7) - 4cos(6pi/7) - 1)/7 = {(4 * np.cos(2 * np.pi / 7) - 4 * np.cos(6 * np.pi / 7) - 1) / 7:.12f}")

    vo, co, rb_o, nf = exact_best(compress(A, O), d, orb, {0: -1})
    best_odd = (vo[0] - 1) / 2
    top_o = co[vo > vo[0] - 1e-9]
    in_orbit = [carries(WL, wigner((O @ rb_o(c)[0])[None, :], A, d)[0], d, lins7) for c in top_o]
    second_o = (vo[vo < vo[0] - 1e-9][0] - 1) / 2
    odd_top = rb_o(co[0])
    say(f"  odd side, all {2 ** nf} sign choices: best {best_odd:.12f}, reached by {len(top_o)} sign choices, "
        f"{sum(in_orbit)} of them the Legendre state up to symmetry; the next value {second_o:.12f}")
    SC["T3"] = abs(best_odd - NL) < 1e-9 and all(in_orbit)
    say(f"T3 {'HELD' if SC['T3'] else 'DIED'}: the best odd state is the Legendre state")
    say(clock())

    ve, ce, rb_e, nf = exact_best(compress(A, E), d, orb, {0: +1})
    best_even = (ve[0] - 1) / 2
    top_e = ce[ve > ve[0] - 1e-9]
    in_orbit = [carries(Wrec, wigner((E @ rb_e(c)[0])[None, :], A, d)[0], d, lins7) for c in top_e]
    second_e = (ve[ve < ve[0] - 1e-9][0] - 1) / 2
    even_top = rb_e(ce[0])
    say(f"  even side, all {2 ** nf} sign choices: best {best_even:.12f}, reached by {len(top_e)} sign choices, "
        f"{sum(in_orbit)} of them the record up to symmetry; the next value {second_e:.12f}")
    SC["T4"] = abs(best_even - Nrec) < 1e-9 and all(in_orbit)
    say(f"T4 {'HELD' if SC['T4'] else 'DIED'}: the best even state is the round-2 record")
    say(clock())

    # every other kind of symmetry: order 3 (one kind) and order 7 (translations, shears, and the shears that move
    # every point); with the half turn (order 2) these cover every state that some Clifford operation fixes
    M2 = np.eye(d)[[(pow(2, -1, d) * k) % d for k in range(d)]]       # M2|k> = |2k>
    assert np.allclose(M2 @ np.eye(d)[:, 1], np.eye(d)[:, 2])

    def best_fixed_by(U):
        orbits = cycles(perm_of(U, A))
        return max((exact_best(compress(A, Q), d, orbits)[0][0] - 1) / 2 for Q in eigenspaces(U)), len(orbits)

    sym = {}
    for name, U in (("the multiplier x2 (order 3)", M2), ("the shift (order 7)", X), ("the shear (order 7)", T)):
        assert perm_order(perm_of(U, A)) in (3, 7)
        sym[name], n_orb = best_fixed_by(U)
        say(f"  states fixed by {name}: {n_orb} orbits; the best {sym[name]:.12f}")
    seen, moved = set(), []                                            # a shear times a shift, fixing no point
    for j in range(1, d):
        for a1 in range(d):
            for a2 in range(d):
                U = np.linalg.matrix_power(Z, a2) @ np.linalg.matrix_power(X, a1) @ np.linalg.matrix_power(T, j)
                pm = perm_of(U, A)
                if perm_order(pm) == d and not (pm == np.arange(d * d)).any():
                    pw, elems = np.arange(d * d), []
                    for _ in range(d - 1):
                        pw = pm[pw]
                        elems.append(tuple(pw))
                    if frozenset(elems) not in seen:                   # one representative per group of order 7
                        seen.add(frozenset(elems))
                        moved.append(U)
    best_moved = max(best_fixed_by(U)[0] for U in moved)
    say(f"  states fixed by a shear with a shift that fixes no point ({len(moved)} such groups of order 7): "
        f"the best {best_moved:.12f}")
    overall = max(best_odd, best_even, *sym.values(), best_moved)
    SC["T5"] = overall < Nrec + 1e-9
    say(f"T5 {'HELD' if SC['T5'] else 'DIED'}: the best state with any symmetry has {overall:.12f}")
    say(clock())

    N7, reps7, stuck7 = search(A, d, 1000000, rng)
    b7 = N7.max()
    hits = int((N7 > Nrec - 1e-9).sum())
    SC["T6"] = b7 < Nrec + 1e-9 and hits >= 1
    say(f"  1000000 sign ascents in the whole space: best {b7:.12f}; {hits} reached the record; {stuck7} still moving")
    say(f"T6 {'HELD' if SC['T6'] else 'DIED'}: no start beats the record, and the record is reached")
    say(clock())

    # ---------------------------------------------------------- eleven levels: T7 - T10
    d = 11
    A = phase_points(d)
    E, O = sides(d)
    lins11 = linear_parts(d)
    L11 = legendre(d)
    WL11 = wigner(L11[None, :], A, d)[0]
    NL11 = negativity(WL11)
    say(f"\neleven levels: the Legendre state has {NL11:.12f}; " +
        "symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, deepest %+.6f"
        % describe(WL11, d, lins11))
    Ae, Ao = compress(A, E), compress(A, O)
    Ne, reps_e, stuck_e = search(Ae, d, 1000000, rng)
    No, reps_o, stuck_o = search(Ao, d, 1000000, rng)
    Nf, reps_f, stuck_f = search(A, d, 1000000, rng)
    be, bo, bf = Ne.max(), No.max(), Nf.max()
    for name, b, Ns, stuck in (("among even states:  ", be, Ne, stuck_e), ("among odd states:   ", bo, No, stuck_o),
                               ("in the whole space:", bf, Nf, stuck_f)):
        say(f"  1000000 sign ascents {name} best {b:.12f} (reached {int((Ns > b - 1e-9).sum())} times; "
            f"{stuck} still moving)")
    odd_side = max(bo, NL11)                                           # the Legendre state is an odd state too
    SC["T7"] = be > odd_side + 1e-6
    say(f"T7 {'HELD' if SC['T7'] else 'DIED'}: the even side beats the odd side, {be:.6f} against {odd_side:.6f}")
    Wbo = wigner((O @ reps_o[max(reps_o)][0])[None, :], A, d)[0]
    is_legendre = abs(bo - NL11) < 1e-6 and carries(WL11, Wbo, d, lins11)
    SC["T8"] = bo < NL11 + 1e-6
    say(f"T8 {'HELD' if SC['T8'] else 'DIED'}: no odd state found beats the Legendre state ({bo:.6f} against "
        f"{NL11:.6f}); the best odd state found is the Legendre state: {is_legendre}")
    SC["T9"] = bf > NL11 + 1e-6
    say(f"T9 {'HELD' if SC['T9'] else 'DIED'}: the best state found beats the Legendre state, {bf:.6f} against "
        f"{NL11:.6f}")
    Wbf = wigner(reps_f[max(reps_f)][0][None, :], A, d)[0]
    info = describe(Wbf, d, lins11)
    SC["T10"] = info[2] == 1 and info[3] == 0
    say(f"T10 {'HELD' if SC['T10'] else 'DIED'}: the best state found touches the ceiling +1/11 at {info[2]} point(s) "
        f"and the floor at {info[3]}")
    say("  it has: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, deepest %+.6f"
        % info)
    say(clock())

    say(f"\nROUND 3 SCORE: {sum(SC.values())} of {len(SC)} held: "
        + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in SC.items()))

    # ---------------------------------------------------------- beyond the registered round (not scored)
    say("\nBEYOND THE REGISTERED ROUND (not scored)")
    say("  Exact values. x = d(1 + 2N) is d times the sum of |W|; each polynomial is exact and irreducible over Q.")
    d = 5
    A = phase_points(d)
    E, O = sides(d)
    orb = half_turn_orbits(d)
    for name, Q, side, sgn in (("the best even state (Jain and Prakash's)", E, "even", +1),
                               ("the best odd state", O, "odd", -1)):
        v, c, rb, _ = exact_best(compress(A, Q), d, orb, {0: sgn})
        phi, lam = rb(c[0])
        W = wigner((Q @ phi)[None, :], A, d)[0]
        fx, g, err = minimal_polynomial(np.where(W >= 0, 1, -1), d, side, (lam - 1) / 2)
        say(f"  five levels, {name}: N = {(lam - 1) / 2:.15f}; x is a root of {fx.as_expr()}; fixed by its "
            f"symmetries alone: {fixed_by_symmetry_alone(Q @ phi, A, d, lins5)[0]}")
    N = negativity(wigner(legendre(5)[None, :], A, d)[0])
    say(f"  five levels, the Legendre state: N = {N:.15f}, which is 2/5: {abs(N - 0.4) < 1e-12}")
    d = 7
    A = phase_points(d)
    E, O = sides(d)
    for name, (phi, lam), Q, side in (("the record, the best even state", even_top, E, "even"),
                                      ("the Legendre state, the best odd state", odd_top, O, "odd")):
        psi = centred(Q @ phi, A, d)
        W = wigner(psi[None, :], A, d)[0]
        fx, g, err = minimal_polynomial(np.where(W >= 0, 1, -1), d, side, (lam - 1) / 2)
        alone, res = fixed_by_symmetry_alone(psi, A, d, lins7)
        say(f"  seven levels, {name}: N = {(lam - 1) / 2:.15f}")
        say(f"    x is a root of {fx.as_expr()} (degree {fx.degree()}; the root matches to {err:.1e})")
        say(f"    N is a root of {g.as_expr()}")
        say(f"    fixed by its symmetries alone: {alone} (largest residual {res:.1e})")
        say(f"    moved to its centre: {amplitudes(psi)}")
    vals = Counter(np.round(N7, 9))
    say("  the ten highest tops of the 1000000 climbs at seven levels, with how often each was reached: "
        + ", ".join(f"{v:.9f} x{c}" for v, c in sorted(vals.items(), reverse=True)[:10]))
    for v in sorted(reps7, reverse=True)[:7]:
        Ws = [wigner(s[None, :], A, d)[0] for s in reps7[v]]
        one = all(carries(Ws[0], W2, d, lins7) for W2 in Ws[1:])
        say(f"    top {v:.9f}: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, "
            "deepest %+.6f" % describe(Ws[0], d, lins7) + f"; {len(Ws)} samples, one state up to symmetry: {one}; "
            f"fixed by its symmetries alone: {fixed_by_symmetry_alone(reps7[v][0], A, d, lins7)[0]}")
        say(f"      {amplitudes(centred(reps7[v][0], A, d))}")
    d = 11
    A = phase_points(d)
    E, O = sides(d)
    stays = abs(ascend(L11[None, :].copy(), A, d)[1][0] - NL11) < 1e-12
    say(f"  eleven levels, the Legendre state: a local maximum (a climb from it stays put: {stays}); "
        f"{int((np.abs(No - NL11) < 1e-9).sum())} of the 1000000 odd climbs ended there")
    for name, reps, Ns, Q in (("even", reps_e, Ne, E), ("odd", reps_o, No, O), ("whole-space", reps_f, Nf, np.eye(d))):
        say(f"  eleven levels, the {name} climbs: the five highest tops, with how often each was reached: "
            + ", ".join(f"{v:.9f} x{c}" for v, c in sorted(Counter(np.round(Ns, 9)).items(), reverse=True)[:5]))
        for v in sorted(reps, reverse=True)[:3]:
            Ws = [wigner((Q @ s)[None, :], A, d)[0] for s in reps[v]]
            one = all(carries(Ws[0], W2, d, lins11) for W2 in Ws[1:])
            say(f"    top {v:.9f}: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, "
                "deepest %+.6f" % describe(Ws[0], d, lins11) + f"; {len(Ws)} samples, one state up to symmetry: {one}")
    for name, reps, Q, side in (("the best odd state found", reps_o, O, "odd"),
                                ("the best state found, which is even", reps_e, E, "even")):
        psi = centred(Q @ reps[max(reps)][0], A, d)
        W = wigner(psi[None, :], A, d)[0]
        N = negativity(W)
        fx, g, err = minimal_polynomial(np.where(W >= 0, 1, -1), d, side, N)
        alone, res = fixed_by_symmetry_alone(psi, A, d, lins11)
        say(f"  eleven levels, {name}: N = {N:.15f}")
        say(f"    x is a root of {fx.as_expr()} (degree {fx.degree()}; the root matches to {err:.1e})")
        say(f"    fixed by its symmetries alone: {alone} (largest residual {res:.1e})")
        say(f"    moved to its centre: {amplitudes(psi)}")
    say(clock())
    LOG.close()


if __name__ == "__main__":
    main()
