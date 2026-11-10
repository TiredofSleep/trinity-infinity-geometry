"""edge_state.py -- read after round 9's run (not registered): the best state found on three wheels of 3 levels.

Round 9's whole-space search on three wheels of 3 found total negativity 17/9, above the best of both sides.  This
script searches the whole space again with a fresh seed, and for each best state found it checks:
  - that no phase-point operator has it as an eigenstate (it is neither even nor odd about any centre);
  - that its Weyl expectations vanish on a Lagrangian (26 operators and the identity);
  - that in that Lagrangian's eigenbasis all its amplitudes have the same size and cube-root-of-unity phases w^f(j);
  - that f(j) = e N(Mj + a) + (a polynomial of degree <= 2) for some invertible M, shift a and sign e, where N is the
    norm of the 27-element field F_3[t]/(t^3 - t - 1) in the basis 1, t, t^2.  So the state is the norm state
    sum_x w^N(x) |x> / sqrt 27 up to a Clifford operation (README section 11; the verifier checks the norm state).

numpy only.  Below-normal priority, three threads.  ASCII output; writes edge_state.log.
Run:  python edge_state.py      (about twenty minutes)
"""
import itertools
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "3")
import time

import numpy as np

import round3 as r3
import many_wheels as mw

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = [20261110, 3, 3, 7]
CLIMBS = 200_000
LOG = None
T0 = time.time()
W3 = np.exp(2j * np.pi / 3)
J = list(itertools.product(range(3), repeat=3))
ZERO = ((0, 0, 0), (0, 0, 0))


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def weyl(v):
    """Z^b X^a on three qutrits, for v = (a, b)"""
    X1, Z1 = np.roll(np.eye(3), 1, axis=0), np.diag(W3 ** np.arange(3))
    M = np.ones((1, 1), complex)
    for ai, bi in zip(*v):
        M = np.kron(M, np.linalg.matrix_power(Z1, bi) @ np.linalg.matrix_power(X1, ai))
    return M


def symp(v1, v2):
    (a, b), (c, d) = v1, v2
    return (sum(x * y for x, y in zip(a, d)) - sum(x * y for x, y in zip(b, c))) % 3


def add(s, v, k=1):
    return tuple((p + k * q) % 3 for p, q in zip(s[0], v[0])), tuple((p + k * q) % 3 for p, q in zip(s[1], v[1]))


def norm_table():
    """N(x) = x^13 in F_3[t]/(t^3 - t - 1), for x = c0 + c1 t + c2 t^2 indexed by (c0, c1, c2)"""
    def mul(x, y):
        prod = [0] * 5
        for i in range(3):
            for k in range(3):
                prod[i + k] += x[i] * y[k]
        for k in (4, 3):                                                # t^3 = t + 1
            c, prod[k] = prod[k], 0
            prod[k - 3] += c
            prod[k - 2] += c
        return tuple(v % 3 for v in prod[:3])
    out = {}
    for x in J:
        r = (1, 0, 0)
        for _ in range(13):
            r = mul(r, x)
        assert r[1] == 0 and r[2] == 0
        out[x] = r[0]
    return out


def in_degree2_span():
    """a test: is a function F_3^3 -> F_3 (values in the order of J) a polynomial of degree <= 2?"""
    mons = [lambda x: 1] + [lambda x, i=i: x[i] for i in range(3)] + \
           [lambda x, i=i, k=k: x[i] * x[k] for i in range(3) for k in range(i, 3)]
    rows = []                                                            # reduced basis of the span, as (pivot, row)
    for m in mons:
        v = [m(x) % 3 for x in J]
        for pc, b in rows:
            if v[pc]:
                v = [(a - v[pc] * c) % 3 for a, c in zip(v, b)]
        nz = next((i for i, a in enumerate(v) if a), None)
        if nz is not None:
            v = [(a * (1 if v[nz] == 1 else 2)) % 3 for a in v]
            rows = [(pc, [(a - b[nz] * c) % 3 for a, c in zip(b, v)]) for pc, b in rows]
            rows.append((nz, v))

    def test(vals):
        v = [int(a) % 3 for a in vals]
        for pc, b in rows:
            if v[pc]:
                v = [(a - v[pc] * c) % 3 for a, c in zip(v, b)]
        return not any(v)
    return test


def analyse(psi, A, ops, NT, quadratic):
    ex = np.real(np.einsum("i,uij,j->u", psi.conj(), A, psi))
    levels = sorted((int(k), int(c)) for k, c in zip(*np.unique(np.round(ex * 9).astype(int), return_counts=True)))
    chi = {v: np.vdot(psi, ops[v] @ psi) for v in ops}
    Lset = [v for v in ops if abs(chi[v]) < 1e-6] + [ZERO]
    lagrangian = len(Lset) == 27 and all(symp(x, y) == 0 for x in Lset for y in Lset)
    flat = all(abs(abs(chi[v]) - 27 ** -0.5) < 1e-6 for v in ops if v not in Lset)
    gens, span = [], {ZERO}
    for v in Lset:
        if v not in span and len(gens) < 3:
            gens.append(v)
            span |= {add(s, v, k) for s in span for k in (1, 2)}
    hs = []
    for j in range(3):
        hs.append(next(v for v in ops if v != ZERO and all(symp(gens[i], v) == (i == j) for i in range(3))
                       and all(symp(v, h) == 0 for h in hs)))
    ev, U = np.linalg.eig(ops[gens[0]] + np.sqrt(2) * ops[gens[1]] + np.pi * ops[gens[2]])
    b0 = U[:, 0] / np.linalg.norm(U[:, 0])
    basis = []
    for j in J:
        v = b0
        for k in range(3):
            v = np.linalg.matrix_power(ops[hs[k]], j[k]) @ v
        basis.append(v)
    c = np.array([np.vdot(b, psi) for b in basis])
    c = c / c[0]
    k = np.angle(c) / (2 * np.pi / 3)
    cube = np.allclose(np.abs(c), 1, atol=1e-6) and np.allclose(k, np.round(k), atol=1e-6)
    f = np.round(k).astype(int) % 3
    found = None
    for m in itertools.product(range(3), repeat=9):
        M = np.array(m).reshape(3, 3)
        if round(np.linalg.det(M)) % 3 == 0:
            continue
        for a in J:
            g = np.array([NT[tuple((M @ np.array(j) + np.array(a)) % 3)] for j in J])
            for e in (1, 2):
                if quadratic((f - e * g) % 3):
                    found = (M.tolist(), a, "+" if e == 1 else "-")
                    break
            if found:
                break
        if found:
            break
    return levels, float(np.abs(ex).max()), lagrangian, flat, cube, found


def main():
    global LOG
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
    except Exception:
        pass
    LOG = open(os.path.join(HERE, "edge_state.log"), "w", encoding="utf-8")
    A = mw.array_points(3, 3)
    ops = {v: weyl(v) for v in itertools.product(J, J) if v != ZERO}
    NT = norm_table()
    quadratic = in_degree2_span()
    assert quadratic([x[0] * x[1] % 3 for x in J]) and not quadratic([NT[x] for x in J])
    Ns, reps, stuck = r3.search(A, 27, CLIMBS, np.random.default_rng(SEED), batch=5000)
    top = max(reps)
    say(f"three wheels of 3, {CLIMBS} climbs in the whole space (seed {SEED}): best {Ns.max():.12f} (17/9 = "
        f"{17 / 9:.12f}), reached {int((Ns > Ns.max() - 1e-9).sum())} times; {stuck} still moving "
        f"[{time.time() - T0:.0f} s]")
    say("  the next tops: " + ", ".join(f"{v:.6f}" for v in sorted(reps, reverse=True)[1:6]))
    for i, phi in enumerate(reps[top]):
        levels, mx, lag, flat, cube, found = analyse(phi, A, ops, NT, quadratic)
        say(f"  best state {i + 1}: <A_u> x 9 takes the values (value, count) {levels}; largest |<A_u>| {mx:.9f}, so "
            f"it is {'no' if mx < 0.999 else 'some'} point's eigenstate")
        say(f"    its Weyl expectations vanish on a Lagrangian: {lag}; equal size 1/sqrt 27 elsewhere: {flat}; in that "
            f"Lagrangian's eigenbasis its amplitudes are equal in size with cube-root phases: {cube}")
        say(f"    equivalent to the norm state (f = e N(Mj + a) + degree <= 2): "
            + (f"yes, M = {found[0]}, a = {found[1]}, sign {found[2]}" if found else "NO"))
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


if __name__ == "__main__":
    main()
