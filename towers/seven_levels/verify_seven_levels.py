"""verify_seven_levels.py -- runs the eight predictions registered in PREREG.md (commit b42b65b) on a
seven-level quantum system, and reports each as HELD or DIED with its evidence.  Then it checks the README's
other lines: round 2's most negative state as recorded in most_negative.log, and round 3's results as recorded in
round3.log (it uses round3.py's tools), and rounds 4 to 9 likewise.  For round 8 it checks the family sizes
behind the confound and makes Y1's death at 13 exact.  For round 7 it checks the 7-wheel's calls at 31 and 37, the
number wheels that fit the sides that won, and the exceptional states at 31.  For round 9 it checks the arrays'
operators, the forced numbers for large arrays, and the norm state found on three wheels of 3 (README section 11).
For round 10 it checks larger_arrays.py's Wigner function against the operators, the norm-type states' flatness and
Kloosterman values on three wheels of 3, 5 and 7, the norm state on five wheels of 3, and the scores (section 12).
For round 11 it checks the torus states (the chirp, the orbit count, the purity identity, the averaged fourth-moment
identity) and the scores (section 13); for round 12, the counting steps of TORUS_MOMENTS.md's proof and the scores;
for round 13, the Walsh identity of cubic states, the exhaustive maxima at small sizes, and the scores (section 14).

numpy + scipy + round3.py + larger_arrays.py.  ASCII output.
Run:  python verify_seven_levels.py           (about two minutes)
      python verify_seven_levels.py --full    (also round 3's 2^24 sign choices on each side, round 4's 2^28 real
                                               sign choices, the tetrahedral states at 3, 7, 11 and 13, the norm
                                               state's exact count of symmetries, the fields' character states, and
                                               rounds 10 to 12's reruns; about 45 minutes)
"""
import ctypes
import itertools
import math
import sys
from collections import Counter

import numpy as np
from scipy.optimize import minimize

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

mp = np.linalg.matrix_power
RESULTS = {}


def report(name, held, detail):
    RESULTS[name] = held
    print(f"{name} {'HELD' if held else 'DIED'}: {detail}")


def setting(d):
    w = np.exp(2j * np.pi / d)
    X = np.roll(np.eye(d), 1, axis=0)                         # |k> -> |k+1>
    Z = np.diag(w ** np.arange(d))
    F = np.array([[w ** (j * k) for k in range(d)] for j in range(d)]) / np.sqrt(d)
    P = np.zeros((d, d))
    for k in range(d):
        P[(-k) % d, k] = 1
    return w, X, Z, F, P


def mult(a, d):
    M = np.zeros((d, d))
    for k in range(d):
        M[(a * k) % d, k] = 1
    return M


def weyl_member(U, d, X, Z):
    for a in range(d):
        for b in range(d):
            W = mp(X, a) @ mp(Z, b)
            c = np.trace(W.conj().T @ U) / d
            if abs(abs(c) - 1) < 1e-9 and np.allclose(U, c * W, atol=1e-9):
                return True
    return False


def clifford_permutations(d):
    w, X, Z, F, P = setting(d)
    found = []
    for perm in itertools.permutations(range(d)):
        Pm = np.zeros((d, d))
        for k in range(d):
            Pm[perm[k], k] = 1
        if weyl_member(Pm @ X @ Pm.T, d, X, Z) and weyl_member(Pm @ Z @ Pm.T, d, X, Z):
            found.append(perm)
    affine = {tuple((a * k + b) % d for k in range(d)) for a in range(1, d) for b in range(d)}
    return found, affine


def sl2(p):
    return [np.array([[a, b], [c, e]]) for a, b, c, e in itertools.product(range(p), repeat=4)
            if (a * e - b * c) % p == 1]


def psl_order(g, p):
    M, n = g.copy(), 1
    while not ((M % p == np.eye(2, dtype=int)).all() or (M % p == (p - 1) * np.eye(2, dtype=int)).all()):
        M, n = (M @ g) % p, n + 1
    return n


def wigner_ops(d, X, Z, P):
    return np.array([mp(Z, q2) @ mp(X, q1) @ P @ (mp(Z, q2) @ mp(X, q1)).conj().T
                     for q1 in range(d) for q2 in range(d)])


def wigner(psi, A, d):
    return np.real(np.einsum("i,nij,j->n", psi.conj(), A, psi)) / d


def key(M, digits=6):
    return tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), digits))


def closure(gens, limit=4000):
    elems = {key(g): g for g in gens}
    frontier = list(gens)
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = a @ g
                k = key(b)
                if k not in elems:
                    elems[k] = b
                    new.append(b)
                    if len(elems) > limit:
                        raise RuntimeError("group too large")
        frontier = new
    return list(elems.values())


def unit_det(M):
    n = M.shape[0]
    return M / np.linalg.det(M) ** (1 / n)


def derived(G):
    inv = {key(g): np.linalg.inv(g) for g in G}
    comms = {}
    for a in G:
        ia = inv[key(a)]
        for b in G[:60]:
            c = a @ b @ ia @ inv[key(b)]
            comms[key(c)] = c
    return closure(list(comms.values()))


def mat_order(M, limit=200):
    Q, n = M.copy(), 1
    while not np.allclose(Q, np.eye(M.shape[0]), atol=1e-8):
        Q, n = Q @ M, n + 1
        if n > limit:
            return None
    return n


d = 7
w, X, Z, F, P = setting(d)

# ------------------------------------------------------------------ Q1
found, affine = clifford_permutations(7)
report("Q1", len(found) == 42 and set(found) == affine,
       f"{len(found)} of the 5040 permutations are Clifford; all are maps k -> ak + b: {set(found) == affine}")

# ------------------------------------------------------------------ Q2
S7 = sl2(7)
psl = Counter(psl_order(g, 7) for g in S7)
psl = {k: v // 2 for k, v in sorted(psl.items())}
gl = []
for bits in itertools.product((0, 1), repeat=9):
    A = np.array(bits).reshape(3, 3)
    if round(np.linalg.det(A)) % 2:
        gl.append(A)


def gl2_order(A):
    M, n = A.copy(), 1
    while not (M % 2 == np.eye(3, dtype=int)).all():
        M, n = (M @ A) % 2, n + 1
    return n


fano = dict(sorted(Counter(gl2_order(A) for A in gl).items()))
report("Q2", len(S7) == 336 and psl == fano == {1: 1, 2: 21, 3: 56, 4: 42, 7: 48},
       f"|SL(2,7)| = {len(S7)}; orders mod +-1 {psl}; the Fano plane's 168 symmetries {fano}")

# ------------------------------------------------------------------ Q3
LINES = ["inf"] + list(range(7))                               # slope p/q of the line through (q, p)


def line_of(v):
    q, p_ = v[0] % 7, v[1] % 7
    return "inf" if q == 0 else (p_ * pow(int(q), 5, 7)) % 7    # q^-1 = q^5 mod 7


def act(g):
    rep = {"inf": np.array([0, 1])}
    rep.update({c: np.array([1, c]) for c in range(7)})
    return tuple(LINES.index(line_of(g @ rep[L])) for L in LINES)


bases = {"inf": np.eye(7, dtype=complex), 0: F.conj().T.copy()}
for c in range(1, 7):
    vals, vecs = np.linalg.eig(X @ mp(Z, c))
    bases[c] = vecs
check_bases = all(np.allclose(np.abs(bases[a].conj().T @ bases[b]) ** 2, 1 / 7)
                  for a, b in itertools.combinations(LINES, 2))


def where(U, L):
    """the basis that U carries the basis of line L onto"""
    for L2 in LINES:
        O = np.abs(bases[L2].conj().T @ U @ bases[L])
        if np.allclose(O.round(6), np.round(O) , atol=1e-6) and np.allclose((O > 0.5).sum(0), 1):
            return L2
    return None


mults = {a: [where(mult(a, 7), L) for L in LINES] for a in range(1, 7)}
fixed_two = all(m[0] == "inf" and m[1] == 0 for m in mults.values())
orbits = {frozenset(mults[a][LINES.index(c)] for a in range(1, 7)) for c in range(1, 7)}
fourier = [where(F, L) for L in LINES]
part_a = check_bases and fixed_two and orbits == {frozenset({1, 2, 4}), frozenset({3, 5, 6})}
part_b = (fourier[0] == 0 and fourier[1] == "inf" and {fourier[LINES.index(c)] for c in (1, 2, 4)} == {3, 5, 6})
perms = sorted({act(g) for g in S7})


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(b)))


def perm_order(a):
    e, n, x = tuple(range(len(a))), 1, a
    while x != e:
        x, n = compose(a, x), n + 1
    return n


def perm_closure(gens):
    G = set(gens)
    frontier = list(gens)
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = compose(a, g)
                if b not in G:
                    G.add(b)
                    new.append(b)
        frontier = new
    return G


o4 = [g for g in perms if perm_order(g) == 4]
o3 = [g for g in perms if perm_order(g) == 3]
S4s = set()
for a in o4:
    for b in o3:
        H = frozenset(perm_closure([a, b]))
        if len(H) == 24:
            S4s.add(H)


def fix_profile(group, n_points):
    out = Counter()
    for g in group:
        out[(perm_order(g), sum(1 for i in range(n_points) if g[i] == i))] += 1
    return dict(sorted(out.items()))


def orbit_count(group, n):
    seen, orbits_ = set(), 0
    for i in range(n):
        if i not in seen:
            orbits_ += 1
            seen |= {g[i] for g in group}
    return orbits_


corners = [np.array(c) for c in itertools.product((-1, 1), repeat=3)]
cube_rot = []
for pp in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        R = np.array([[s[i] if pp[i] == j else 0 for j in range(3)] for i in range(3)])
        if round(np.linalg.det(R)) == 1:
            cube_rot.append(tuple(int(np.argmin([np.abs(R @ c - c2).sum() for c2 in corners])) for c in corners))
cube_profile = fix_profile(cube_rot, 8)
part_c = (len(S4s) == 14 and all(fix_profile(H, 8) == cube_profile and orbit_count(H, 8) == 1 for H in S4s))
report("Q3", part_a and part_b and part_c,
       f"(a) {part_a}: multipliers fix the levels and the Fourier basis, orbits of the other six "
       f"{sorted(sorted(o, key=str) for o in orbits)}; (b) {part_b}: Fourier swaps them; (c) {part_c}: "
       f"{len(S4s)} subgroups shaped like S4, each moving the 8 bases as the cube's rotations move its corners "
       f"(order, fixed points): {cube_profile}")

# ------------------------------------------------------------------ Q4 and Q5
E = np.zeros((7, 3), complex)
for col, j in enumerate((1, 2, 4)):
    E[j, col], E[(-j) % 7, col] = 1 / np.sqrt(2), -1 / np.sqrt(2)
T = np.diag([w ** ((4 * k * k) % 7) for k in range(7)])          # the quadratic phase, 2^-1 = 4 mod 7
gens7 = [T, mult(2, 7), F]
stays = all(np.allclose(U @ E, E @ (E.conj().T @ U @ E)) for U in gens7)
R = [E.conj().T @ U @ E for U in gens7]
diag_ok = np.allclose(R[0], np.diag([w ** 4, w ** 2, w]))
cyc_ok = np.allclose(np.abs(R[1]), np.roll(np.eye(3), 1, axis=0))


def canon(M):
    flat = M.ravel()
    i = int(np.argmax(np.abs(flat) > 1e-6))
    return M / (flat[i] / abs(flat[i]))


proj = closure([canon(r) for r in R], limit=3000)
proj = {key(canon(g)): g for g in proj}


def quartic(v):
    x, y, z = v
    return x ** 3 * y + y ** 3 * z + z ** 3 * x


rng = np.random.default_rng(7)
V = rng.normal(size=(6, 3)) + 1j * rng.normal(size=(6, 3))
inv_ok = True
for r in R:
    ratios = [quartic(r @ v) / quartic(v) for v in V]
    inv_ok &= np.allclose(ratios, ratios[0]) and abs(abs(ratios[0]) - 1) < 1e-9
report("Q4", stays and diag_ok and cyc_ok and len(proj) == 168 and inv_ok,
       f"the odd subspace is kept: {stays}; quadratic phase diag(w^4, w^2, w): {diag_ok}; x2 cycles the "
       f"coordinates: {cyc_ok}; {len(proj)} elements up to scalars; Klein's quartic invariant: {inv_ok}")

G = closure([unit_det(r) for r in R], limit=3000)
K = derived(G) if len(G) != 168 else G
orders = {key(g): mat_order(g) for g in K}
by_key = {key(g): g for g in K}
o4m = [g for g in K if orders[key(g)] == 4]
o3m = [g for g in K if orders[key(g)] == 3]
subs = []
seen = set()
for a in o4m[:12]:
    for b in o3m:
        H = closure([a, b], limit=200)
        if len(H) == 24:
            fs = frozenset(key(h) for h in H)
            if fs not in seen:
                seen.add(fs)
                subs.append(H)
char_ok = True
for H in subs:
    for h in H:
        n_ = mat_order(h)
        tr = np.trace(h)
        expect = {1: 3, 2: -1, 3: 0, 4: 1}[n_]
        char_ok &= abs(tr - expect) < 1e-8
tr7 = {complex(round(np.trace(g).real, 6), round(np.trace(g).imag, 6)) for g in K if orders[key(g)] == 7}
gauss = {complex(-0.5, round(math.sqrt(7) / 2, 6)), complex(-0.5, -round(math.sqrt(7) / 2, 6))}
report("Q5", len(K) == 168 and len(subs) > 0 and char_ok and tr7 == gauss,
       f"the exact group in SU(3) has {len(K)} elements; {len(subs)} S4 subgroups found, each with the character "
       f"of the octahedron's rotations (3, -1, 0, 1 on orders 1, 2, 3, 4): {char_ok}; order-7 traces {sorted(tr7, key=lambda z: z.imag)}")

# ------------------------------------------------------------------ Q6
chi = np.array([0] + [1 if pow(k, 3, 7) == 1 else -1 for k in range(1, 7)], complex) / np.sqrt(6)
A7 = wigner_ops(7, X, Z, P)
eig_m = all(np.allclose(mult(a, 7) @ chi, (1 if pow(a, 3, 7) == 1 else -1) * chi) for a in range(1, 7))
eig_f = np.allclose(F @ chi, 1j * chi)
odd = np.allclose(P @ chi, -chi)
W_chi = wigner(chi, A7, 7)
centre = W_chi[0]
report("Q6", eig_m and eig_f and odd and abs(centre + 1 / 7) < 1e-12,
       f"multiplier eigenvector: {eig_m}; Fourier eigenvalue i: {eig_f}; odd under the half turn: {odd}; "
       f"Wigner value at the centre {centre:.6f} (sum {W_chi.sum():.6f})")

# ------------------------------------------------------------------ Q7
def negativity(psi):
    W = wigner(psi / np.linalg.norm(psi), A7, 7)
    return -W[W < 0].sum()


N_chi = negativity(chi)
N_pair = negativity((np.eye(7)[1] - np.eye(7)[6]) / np.sqrt(2))


def objective(x):
    return -negativity(x[:7] + 1j * x[7:])


best, best_psi = 0.0, None
starts = [np.concatenate([chi.real, chi.imag]) + 0.05 * rng.normal(size=14) for _ in range(5)]
starts += [rng.normal(size=14) for _ in range(120)]
for x0 in starts:
    r = minimize(objective, x0, method="Powell", options={"xtol": 1e-9, "ftol": 1e-12, "maxfev": 20000})
    if -r.fun > best:
        best, best_psi = -r.fun, (r.x[:7] + 1j * r.x[7:]) / np.linalg.norm(r.x[:7] + 1j * r.x[7:])
report("Q7", best <= N_chi + 1e-6,
       f"total negativity: Legendre state {N_chi:.6f}; (|1>-|6>)/sqrt2 {N_pair:.6f}; best found from "
       f"{len(starts)} starts {best:.6f}")
if best_psi is not None:
    best_psi = best_psi * np.exp(-1j * np.angle(best_psi[0]))           # make the |0> amplitude real
    shown = np.round(best_psi, 8)
    print(f"      the counterexample, amplitudes on |0>..|6> (8 decimals): "
          + ", ".join(f"{z.real:+.8f}{z.imag:+.8f}i" for z in shown))
    print(f"      recomputed from those 8 decimals: negativity {negativity(shown):.6f}; "
          f"|amplitudes| {np.round(np.abs(shown), 4).tolist()}; parity expectation "
          f"{np.real(shown.conj() @ P @ shown) / np.real(shown.conj() @ shown):+.4f} (not odd)")

# ------------------------------------------------------------------ Q8
found5, affine5 = clifford_permutations(5)
S5 = sl2(5)
psl5 = Counter(psl_order(g, 5) for g in S5)
psl5 = {k: v // 2 for k, v in sorted(psl5.items())}
w5, X5, Z5, F5, P5 = setting(5)
E5 = np.zeros((5, 2), complex)
for col, j in enumerate((1, 2)):
    E5[j, col], E5[(-j) % 5, col] = 1 / np.sqrt(2), -1 / np.sqrt(2)
T5 = np.diag([w5 ** ((3 * k * k) % 5) for k in range(5)])        # 2^-1 = 3 mod 5
gens5 = [T5, mult(2, 5), F5]
stays5 = all(np.allclose(U @ E5, E5 @ (E5.conj().T @ U @ E5)) for U in gens5)
G5 = closure([unit_det(E5.conj().T @ U @ E5) for U in gens5], limit=3000)
K5 = derived(G5)
prof5 = dict(sorted(Counter(mat_order(g) for g in K5).items()))
binary_icosahedral = {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}
report("Q8", len(found5) == 20 and set(found5) == affine5 and psl5 == {1: 1, 2: 15, 3: 20, 5: 24}
       and stays5 and len(K5) == 120 and prof5 == binary_icosahedral,
       f"{len(found5)} Clifford permutations (affine: {set(found5) == affine5}); orders mod +-1 {psl5}; "
       f"magic subspace kept: {stays5}; its group has {len(K5)} elements with orders {prof5}")

# ------------------------------------------------------------------ the page's other [FORCED] lines
from scipy.linalg import expm

FORCED_OK = True


def forced(label, ok):
    global FORCED_OK
    print(("PASS  " if ok else "FAIL  ") + label)
    FORCED_OK &= bool(ok)


print()
forced("the half turn is the Fourier transform done twice, and the multiplier by -1", np.allclose(F @ F, P)
       and np.allclose(mult(6, 7), P))
forced("the multiplier x3 fixes |0> and turns the other six in one cycle (1, 3, 2, 6, 4, 5)",
       [int(np.argmax(mult(3, 7)[:, k])) for k in range(7)] == [0, 3, 6, 2, 5, 1, 4])
m = np.arange(3, -4, -1)
Jp = np.zeros((7, 7), complex)
for i in range(1, 7):
    Jp[i - 1, i] = math.sqrt(12 - m[i] * (m[i] + 1))
Jx = (Jp + Jp.conj().T) / 2
ev = np.linalg.eigvals(expm(-1j * (2 * np.pi / 7) * np.diag(m)))
roots = w ** np.arange(7)
forced("spin 3: a seventh of a turn of space about the axis has exactly the seven 7th roots of unity as "
       "eigenvalues, so it is the clock",
       all(np.min(np.abs(roots - e)) < 1e-12 for e in ev) and all(np.min(np.abs(ev - r)) < 1e-12 for r in roots))
forced("spin 3: half a turn about a perpendicular axis sends each m to -m (up to sign): the flip",
       np.allclose(np.abs(expm(-1j * np.pi * Jx)), np.fliplr(np.eye(7)), atol=1e-10))
signed = [np.array([[s[i] if pp[i] == j else 0 for j in range(3)] for i in range(3)])
          for pp in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)]
forced("no symmetry of the octahedron has order 7 (its 48 have orders 1, 2, 3, 4, 6)",
       sorted({mat_order(g.astype(float)) for g in signed}) == [1, 2, 3, 4, 6])

# round 2: the most negative state found (most_negative.py), rebuilt from its 8 decimals in the log
rec = ("+0.01922811-0.08424383i, -0.22656903+0.28410857i, +0.06990646-0.03366517i, +0.59849409+0.00000000i, "
       "-0.53922453-0.25967686i, -0.04837677-0.06066255i, +0.08086155+0.35427759i")
top = np.array([complex(s.replace("i", "j")) for s in rec.split(", ")])
top /= np.linalg.norm(top)
Wt = wigner(top, A7, 7)
forced("round 2's maximizer: total negativity 0.732522, negative at 16 of the 49 points, none deeper than -0.068, "
       "and +1/7 at one point",
       abs(negativity(top) - 0.732522) < 1e-6 and int((Wt < -1e-9).sum()) == 16 and Wt.min() > -0.0681
       and abs(Wt.max() - 1 / 7) < 1e-8 and int((Wt > 1 / 7 - 1e-4).sum()) == 1)


def clifford_group(d):
    """the Clifford group of d levels (d an odd prime) up to phase: shift, clock, Fourier, the shear
    |k> -> w^(k^2/2)|k> and a primitive-root multiplier generate it"""
    w_, X_, Z_, F_, P_ = setting(d)
    T_ = np.diag([w_ ** ((pow(2, -1, d) * k * k) % d) for k in range(d)])
    g_ = next(a for a in range(2, d) if len({pow(a, e, d) for e in range(1, d)}) == d - 1)
    gens_ = [X_, Z_, F_, T_, mult(g_, d)]

    def canon_(U):
        flat = U.ravel()
        i = int(np.argmax(np.abs(flat) > 1e-6))
        return U / (flat[i] / abs(flat[i]))

    start = np.eye(d, dtype=complex)
    group = {key(start): start}
    frontier = [start]
    while frontier:
        new = []
        for U in frontier:
            for G_ in gens_:
                V_ = canon_(G_ @ U)
                k_ = key(V_)
                if k_ not in group:
                    group[k_] = V_
                    new.append(V_)
        frontier = new
    return np.array(list(group.values()))


CL = clifford_group(7)
images = np.einsum("nij,j->ni", CL, top)
stab = CL[np.abs(images.conj() @ top) > 1 - 1e-4]


def order_phase(U):
    Q_, n_ = U.copy(), 1
    while abs(abs(np.trace(Q_)) - U.shape[0]) > 1e-6:
        Q_, n_ = Q_ @ U, n_ + 1
    return n_


def symmetries(psi, C):
    return int((np.abs(np.einsum("nij,j->ni", C, psi).conj() @ psi) > 1 - 1e-6).sum())


faces = []
for U in [U for U in stab if order_phase(U) == 4]:                  # its two quarter turns, U and U^3
    views = [S_.conj().T @ top for S_ in CL if abs(abs(np.trace((S_ @ F @ S_.conj().T).conj().T @ U)) - 7) < 1e-6]
    lams = [v.conj() @ F @ v for v in views]                       # each view: a frame where U is F itself
    ok_ = all(np.linalg.norm(F @ v - l * v) < 1e-6 and abs(l - lams[0]) < 1e-6 for v, l in zip(views, lams))
    faces.append((lams[0], len(views), ok_, [abs(np.sum(v * v)) for v in views], views[0]))  # |sum v_k^2| = 1: real
faces.sort(key=lambda f_: f_[0].real)
two = (len(faces) == 2 and abs(faces[0][0] + 1) < 1e-6 and abs(faces[1][0] - 1) < 1e-6
       and all(f_[1] == 8 and f_[2] for f_ in faces))
v_m = faces[0][4] if two else top
W_m = wigner(v_m, A7, 7)
forced(f"the Clifford group has {len(CL)} operations up to phase; the maximizer's symmetries are 4, of orders "
       f"{sorted(order_phase(U) for U in stab)}; in each of the 8 frames where one of its quarter turns becomes the "
       "Fourier transform, it is a REAL Fourier eigenstate with eigenvalue -1, even, with +1/7 at the centre; in the 8 "
       "frames of the other quarter turn it is an eigenstate with eigenvalue +1, complex in every one "
       f"(|sum of squared amplitudes| {max(faces[-1][3]):.3f}; 1 means real)",
       len(CL) == 16464 and sorted(order_phase(U) for U in stab) == [1, 2, 4, 4] and two
       and min(faces[0][3]) > 1 - 1e-8 and max(faces[1][3]) < 0.99
       and np.allclose(P @ v_m, v_m, atol=1e-6) and abs(W_m[0] - 1 / 7) < 1e-8)
from scipy.optimize import minimize_scalar

evR, VR = np.linalg.eigh(F.real)            # on even states F is its real part, so its +1 and -1 spaces have real bases
best_real = {}
for target in (1, -1):
    B = VR[:, np.abs(evR - target) < 1e-6]

    def along(t, B=B):
        return negativity(math.cos(t) * B[:, 0] + math.sin(t) * B[:, 1])

    ts = np.linspace(0, math.pi, 3601)
    t0 = ts[int(np.argmax([along(t) for t in ts]))]
    r = minimize_scalar(lambda t: -along(t), bounds=(t0 - math.pi / 3600, t0 + math.pi / 3600), method="bounded",
                        options={"xatol": 1e-12})
    best_real[target] = max(along(t0), -r.fun)
forced(f"among REAL states, the -1 eigenspace still reaches {best_real[-1]:.6f}, the +1 eigenspace only "
       f"{best_real[1]:.6f}: the maximum's real face is the -1 one",
       abs(best_real[-1] - 0.732522) < 1e-6 and best_real[1] < 0.62)
forced("the centre's Wigner operator is the half turn itself, so parity decides the centre: the Legendre state (odd) "
       "sits on the floor there, -1/7, negative at 13 points (one at -1/7, twelve at "
       f"{np.sort(W_chi)[1]:.4f}); the maximizer seen even sits on the ceiling, +1/7, and spreads its negativity over "
       f"16 points, none below {W_m.min():.4f}",
       np.allclose(A7[0], P) and abs(W_chi[0] + 1 / 7) < 1e-12 and int((W_chi < -1e-12).sum()) == 13
       and np.allclose(np.sort(W_chi)[1:13], np.sort(W_chi)[1]) and int((W_m < -1e-9).sum()) == 16
       and W_m.min() > -0.0681)
n_chi = symmetries(chi, CL)
named = [mult(a, 7) for a in range(1, 7)] + [F @ mult(a, 7) for a in range(1, 7)]
named_fix = all(abs(abs(chi.conj() @ G_ @ chi) - 1) < 1e-9 for G_ in named)
forced(f"the Legendre state is fixed by {n_chi} Clifford operations, exactly the six multipliers and the Fourier "
       f"transform after each; the maximizer by {len(stab)}: the more symmetric state loses",
       n_chi == 12 and named_fix and len({key(canon(G_.astype(complex))) for G_ in named}) == 12 and len(stab) == 4)
C3 = clifford_group(3)
w3, X3, Z3, F3, P3 = setting(3)
A3 = wigner_ops(3, X3, Z3, P3)
strange = np.array([0, 1, -1], complex) / np.sqrt(2)
norrell = np.array([0, 1, 1], complex) / np.sqrt(2)                 # |N+> in Jain and Prakash (2020)
legendre3 = np.array([0] + [1 if pow(k, 1, 3) == 1 else -1 for k in range(1, 3)], complex) / np.sqrt(2)
Ws3, Wn3 = np.sort(wigner(strange, A3, 3)), np.sort(wigner(norrell, A3, 3))
forced(f"three levels, the same two sides: the strange state (|1> - |2>)/sqrt2 is the Legendre state of 3, odd, and "
       f"sits on the floor at the centre, -1/3, with +1/6 at the other eight points; the Norrell state (|1> + |2>)/sqrt2 "
       f"is even and sits on the ceiling, +1/3, with six +1/6 and two -1/6; both total 1/3; of the {len(C3)} Clifford "
       f"operations {symmetries(strange, C3)} fix the strange state and {symmetries(norrell, C3)} the Norrell state, so "
       "none carries one to the other",
       np.allclose(strange, legendre3) and np.allclose(Ws3, [-1 / 3] + [1 / 6] * 8)
       and np.allclose(Wn3, [-1 / 6] * 2 + [1 / 6] * 6 + [1 / 3]) and len(C3) == 216
       and abs(wigner(strange, A3, 3)[0] + 1 / 3) < 1e-12 and abs(wigner(norrell, A3, 3)[0] - 1 / 3) < 1e-12
       and symmetries(strange, C3) == 24 and symmetries(norrell, C3) == 6)
evF, VF = np.linalg.eig(F)
best_in = {}
for target in (1, -1, 1j, -1j):
    idx = [k for k in range(7) if abs(evF[k] - target) < 1e-6]
    Qe, _ = np.linalg.qr(VF[:, idx])
    if len(idx) == 1:
        best_in[target] = negativity(Qe[:, 0])
        continue
    th, ph = np.meshgrid(np.linspace(0, np.pi, 91), np.linspace(0, 2 * np.pi, 180, endpoint=False), indexing="ij")
    cands = [(negativity(Qe @ np.array([math.cos(a / 2), np.exp(1j * b) * math.sin(a / 2)])), a, b)
             for a, b in zip(th.ravel(), ph.ravel())]
    v0, a0, b0 = max(cands)
    r = minimize(lambda v: -negativity(Qe @ np.array([math.cos(v[0] / 2), np.exp(1j * v[1]) * math.sin(v[0] / 2)])),
                 [a0, b0], method="Powell", options={"xtol": 1e-12, "ftol": 1e-14})
    best_in[target] = max(v0, -r.fun)
forced("the most negative state in each eigenspace of the Fourier transform (a grid over each, then refined): "
       f"1: {best_in[1]:.6f}, -1: {best_in[-1]:.6f}, i: {best_in[1j]:.6f} (the Legendre state's value), "
       f"-i: {best_in[-1j]:.6f}",
       abs(best_in[1] - 0.732522) < 1e-6 and abs(best_in[-1] - 0.732522) < 1e-6
       and abs(best_in[1j] - N_chi) < 1e-6 and abs(best_in[-1j] - 0.601107) < 1e-6)

# ------------------------------------------------------------------ round 3 (round3.py; its output is round3.log)
from fractions import Fraction

import round3 as r3

FULL = "--full" in sys.argv


def amps(s):
    v = np.array([complex(t.replace("i", "j")) for t in s.split(", ")])
    return v / np.linalg.norm(v)


def climbed(s, d, A):
    """the recorded amplitudes (10 decimals), climbed back to their exact top by the sign ascent, in the recorded
    phase (an eigenvector comes back with an arbitrary phase)"""
    v = amps(s)
    c = r3.ascend(v[None, :].copy(), A, d)[0][0]
    z = np.vdot(c, v)
    return c * z / abs(z)


def strict_top(psi, A, d):
    """the state is the top eigenvector of its own sign operator, with a gap below: a strict local maximum"""
    W = r3.wigner(psi[None, :], A, d)[0]
    ev, V = np.linalg.eigh(np.tensordot(np.where(W >= 0, 1.0, -1.0), A, axes=1) / d)
    return (abs(ev[-1] - np.abs(W).sum()) < 1e-12 and abs(abs(np.vdot(V[:, -1], psi)) - 1) < 1e-10
            and ev[-1] - ev[-2] > 0.1)


def root_near(coeffs, x0, h=Fraction(1, 10 ** 9)):
    """an exact sign change of the integer polynomial across [x0 - h, x0 + h] proves a root there"""
    x0 = Fraction(x0).limit_denominator(10 ** 15)

    def val(x):
        v = Fraction(0)
        for c in coeffs:
            v = v * x + c
        return v
    return val(x0 - h) * val(x0 + h) < 0


print()
print("round 3:")
A5, (E5, O5), lins5 = r3.phase_points(5), r3.sides(5), r3.linear_parts(5)
orb5 = r3.half_turn_orbits(5)
ve5, ce5, rbe5, _ = r3.exact_best(r3.compress(A5, E5), 5, orb5, {0: 1})
vo5, co5, rbo5, _ = r3.exact_best(r3.compress(A5, O5), 5, orb5, {0: -1})
jp = (math.sqrt(5) - 2 + math.sqrt(15 + 6 * math.sqrt(5))) / 10
e5, o5 = E5 @ rbe5(ce5[0])[0], O5 @ rbo5(co5[0])[0]
De5 = r3.describe(r3.wigner(e5[None, :], A5, 5)[0], 5, lins5)
Do5 = r3.describe(r3.wigner(o5[None, :], A5, 5)[0], 5, lins5)
NL5 = r3.negativity(r3.wigner(r3.legendre(5)[None, :], A5, 5)[0])
forced(f"five levels, every sign choice on each side (2^12 each): the best even state is Jain and Prakash's, "
       f"{(ve5[0] - 1) / 2:.12f} = (sqrt5 - 2 + sqrt(15 + 6 sqrt5))/10, with {De5[0]} symmetries, one ceiling "
       f"point and deepest value {De5[5]:.6f}; 5(1 + 2N) is a root of x^4 - 12x^3 + 14x^2 + 12x + 1; the best odd "
       f"state has {(vo5[0] - 1) / 2:.6f}, also with {Do5[0]} symmetries; the Legendre state of 5, which is even, "
       "has exactly 2/5",
       abs((ve5[0] - 1) / 2 - jp) < 1e-12 and De5[0] == 6 and De5[2] == 1 and abs(De5[5] + 0.092780) < 1e-6
       and root_near([1, -12, 14, 12, 1], 5 * (1 + 2 * jp)) and abs((vo5[0] - 1) / 2 - 0.433070425601) < 1e-11
       and Do5[0] == 6 and Do5[3] == 1 and abs(NL5 - 0.4) < 1e-12)

A7r3, lins7 = r3.phase_points(7), r3.linear_parts(7)
E7, O7 = r3.sides(7)
REC7 = ("-0.0864103215+0.0000000000i, -0.3633885010+0.0000000000i, -0.0775903120-0.0000000000i, "
          "+0.5984940843-0.0000000000i, +0.5984940843-0.0000000000i, -0.0775903120+0.0000000000i, "
          "-0.3633885010-0.0000000000i")
rec7 = climbed(REC7, 7, A7r3)
Wr7 = r3.wigner(rec7[None, :], A7r3, 7)[0]
N_rec = r3.negativity(Wr7)
chi7 = r3.legendre(7)
REC7_X = [1, -36, 258, 3468, -39873, -108680, 1734236, 1510968, -26665265, -10245204, 127009090, 35031356,
           -154719151]
shifted = r3.centred(r3.ascend(top[None, :].copy(), A7r3, 7)[0][0], A7r3, 7)   # round 2's state, at its centre
forced(f"round 2's record, moved to its centre, is real and even, (a, b, c, e, e, c, b); it is a strict local "
       f"maximum, and x = 7(1 + 2N) = {7 * (1 + 2 * N_rec):.12f} is a root of the recorded degree-12 polynomial; "
       "the Legendre state's x is a root of x^3 - 15x^2 - 37x - 13",
       abs(abs(np.vdot(shifted, rec7)) - 1) < 1e-9 and np.abs(rec7.imag).max() < 1e-9
       and np.allclose(rec7, rec7[(-np.arange(7)) % 7]) and strict_top(rec7, A7r3, 7)
       and abs(N_rec - 0.732522000010631) < 1e-12 and root_near(REC7_X, 7 * (1 + 2 * N_rec))
       and strict_top(chi7, A7r3, 7) and root_near([1, -15, -37, -13], 7 * (1 + 2 * N_chi)))
alone_rec = r3.fixed_by_symmetry_alone(rec7, A7r3, 7, lins7)
alone_chi = r3.fixed_by_symmetry_alone(chi7, A7r3, 7, lins7)
forced(f"the Legendre state is the only state its 12 symmetries fix (residual {alone_chi[1]:.0e}); the record is not: "
       f"its 4 symmetries leave a two-dimensional family, and it is the best point of it (residual {alone_rec[1]:.1f})",
       alone_chi[0] and not alone_rec[0])

# every kind of symmetry other than the half turn, counted exhaustively (as round3.py does for T5)
w7_, X7_, Z7_, F7_, P7_, T7_ = r3.basics(7)
M2_ = np.eye(7)[[(pow(2, -1, 7) * k) % 7 for k in range(7)]]


def best_fixed(U):
    orbits = r3.cycles(r3.perm_of(U, A7r3))
    return max((r3.exact_best(r3.compress(A7r3, Q), 7, orbits)[0][0] - 1) / 2 for Q in r3.eigenspaces(U))


kinds = {"x2": best_fixed(M2_), "shift": best_fixed(X7_), "shear": best_fixed(T7_)}
seen_, moved_ = set(), []
for j in range(1, 7):
    for a1 in range(7):
        for a2 in range(7):
            U = mp(Z7_, a2) @ mp(X7_, a1) @ mp(T7_, j)
            pm = r3.perm_of(U, A7r3)
            if r3.perm_order(pm) == 7 and not (pm == np.arange(49)).any():
                pw, elems = np.arange(49), []
                for _ in range(6):
                    pw = pm[pw]
                    elems.append(tuple(pw))
                if frozenset(elems) not in seen_:
                    seen_.add(frozenset(elems))
                    moved_.append(U)
kinds["moved"] = max(best_fixed(U) for U in moved_)
forced(f"every other kind of symmetry, counted exhaustively: the best state fixed by x2 has {kinds['x2']:.6f} (the "
       f"Legendre state), by the shift {kinds['shift']:.6f}, by the shear {kinds['shear']:.6f}, and by the "
       f"{len(moved_)} groups of shears with a shift that fix no point {kinds['moved']:.6f}: none beats the record",
       abs(kinds["x2"] - N_chi) < 1e-12 and kinds["shift"] < 1e-12 and abs(kinds["shear"] - 0.320997086245) < 1e-11
       and len(moved_) == 42 and abs(kinds["moved"] - 0.725152059270) < 1e-11 and max(kinds.values()) < N_rec)

if FULL:
    orb7 = r3.half_turn_orbits(7)
    vo7, co7, rbo7, _ = r3.exact_best(r3.compress(A7r3, O7), 7, orb7, {0: -1})
    ve7, ce7, rbe7, _ = r3.exact_best(r3.compress(A7r3, E7), 7, orb7, {0: 1})
    top_o7, top_e7 = co7[vo7 > vo7[0] - 1e-9], ce7[ve7 > ve7[0] - 1e-9]
    W_chi7 = r3.wigner(chi7[None, :], A7r3, 7)[0]
    ok_o = all(r3.carries(W_chi7, r3.wigner((O7 @ rbo7(c)[0])[None, :], A7r3, 7)[0], 7, lins7) for c in top_o7)
    ok_e = all(r3.carries(Wr7, r3.wigner((E7 @ rbe7(c)[0])[None, :], A7r3, 7)[0], 7, lins7) for c in top_e7)
    forced(f"(--full) every one of the 2^24 odd sign choices: the best is the Legendre state, reached by {len(top_o7)} "
           f"choices, all its images; every one of the 2^24 even choices: the best is the record, reached by "
           f"{len(top_e7)}, all its images",
           abs((vo7[0] - 1) / 2 - N_chi) < 1e-12 and len(top_o7) == 28 and ok_o
           and abs((ve7[0] - 1) / 2 - N_rec) < 1e-12 and len(top_e7) == 84 and ok_e)

A11, lins11 = r3.phase_points(11), r3.linear_parts(11)
TET11 = ("+0.0000000000+0.0000000000i, -0.0662691948-0.0000000000i, +0.2299431906+0.0000000000i, "
          "+0.4981621116-0.0000000000i, -0.3097058288+0.0000000000i, +0.3140880978-0.0000000000i, "
          "-0.3140880978+0.0000000000i, +0.3097058288-0.0000000000i, -0.4981621116+0.0000000000i, "
          "-0.2299431906-0.0000000000i, +0.0662691948+0.0000000000i")
WIN11 = ("+0.4767846184+0.0000000000i, -0.3225795083-0.0992783298i, -0.2160886441-0.1863491300i, "
          "-0.0966836082-0.0356497256i, -0.0439107553-0.3891179782i, -0.0768803819-0.1453754310i, "
          "-0.0768803819-0.1453754310i, -0.0439107553-0.3891179782i, -0.0966836082-0.0356497256i, "
          "-0.2160886441-0.1863491300i, -0.3225795083-0.0992783298i")
tet = climbed(TET11, 11, A11)
win = climbed(WIN11, 11, A11)
Wt11, Ww11 = r3.wigner(tet[None, :], A11, 11)[0], r3.wigner(win[None, :], A11, 11)[0]
Nt, Nw = r3.negativity(Wt11), r3.negativity(Ww11)
Dt, Dw = r3.describe(Wt11, 11, lins11), r3.describe(Ww11, 11, lins11)
TET11_X = [1, -34, -615, 23880, 7074, -4124748, 20637882, 173161416, -1637462595, 3726459230, -1235597747]
WIN11_X = [1, -110, 4059, -22220, -2305347, 53173846, 116588263, -17214868088, 141074198749, 2091799880962,
           -36379724664129, -39652596935732, 3910966184300153, -14556796029974154, -208296087585036341,
           1525841726814407024, 4883102424135078803, -68624080291106399642, 5094817285875423073,
           1629009436243920609164, -2570676344121824786265, -21418168336766257247246, 50267931441656895942437,
           162072855148505968005768, -416000538733381509421745, -769288232150255907576058,
           1555464922065730094433861, 2391561387163614417129972, -1847323033936729869177757,
           -3543359770787538121857470, -1082294068352599534974487]
L11_ = r3.legendre(11)
NL11_ = r3.negativity(r3.wigner(L11_[None, :], A11, 11)[0])
forced(f"eleven levels, the best odd state found: {Nt:.12f}, {Dt[0]} symmetries with orders {Dt[1]} (the binary "
       f"tetrahedral group, the strange state's own), on the floor at its centre, real, the only state its symmetries "
       f"fix, a strict local maximum; 11(1 + 2N) is a root of the recorded degree-10 polynomial; the Legendre state "
       f"of 11 has only {NL11_:.6f}, though it is a local maximum too",
       abs(Nt - 1.029706813152930) < 1e-12 and Dt[0] == 24 and Dt[1] == {1: 1, 2: 1, 3: 8, 4: 6, 6: 8}
       and Dt[3] == 1 and np.abs(tet.imag).max() < 1e-9 and r3.fixed_by_symmetry_alone(tet, A11, 11, lins11)[0]
       and strict_top(tet, A11, 11) and root_near(TET11_X, 11 * (1 + 2 * Nt))
       and abs(NL11_ - 0.787711348725826) < 1e-12 and strict_top(L11_, A11, 11))
forced(f"eleven levels, the best state found: {Nw:.12f}, even, on the ceiling +1/11 at its centre only; its one "
       f"symmetry is the half turn there; negative at {Dw[4]} of the 121 points, none deeper than {Dw[5]:.6f}; a "
       "strict local maximum, not fixed by its symmetry alone; 11(1 + 2N) is a root of the recorded degree-30 "
       f"polynomial; it beats the odd side by {Nw - Nt:.6f}",
       abs(Nw - 1.032585792266799) < 1e-12 and Dw[0] == 2 and Dw[2] == 1 and Dw[3] == 0 and Dw[4] == 44
       and abs(Dw[5] + 0.039577) < 1e-6 and strict_top(win, A11, 11)
       and not r3.fixed_by_symmetry_alone(win, A11, 11, lins11)[0] and root_near(WIN11_X, 11 * (1 + 2 * Nw))
       and Nw - Nt > 0.0028)

# ------------------------------------------------------------------ round 4 (round4.py; its logs are round4_*.log)
import round4 as r4

print()
print("round 4:")


def samuelson(k):
    return (math.sqrt(6 * k * (1 - k / 49)) - k / 7) / 7


forced("a state that beats the record has between 8 and 24 negative points: outside that range the bound "
       "(sqrt(6k(1 - k/49)) - k/7)/7 falls below 0.732522 (at 7 and 25 it is exactly 5/7)",
       [k for k in range(1, 49) if samuelson(k) > N_rec] == list(range(8, 25))
       and abs(samuelson(7) - 5 / 7) < 1e-12 and abs(samuelson(25) - 5 / 7) < 1e-12)
mirs7 = r4.mirror_parts(7)
qq, pp = np.divmod(np.arange(49), 7)
Kmap = qq * 7 + (-pp) % 7
conj_K, invol = set(), set()
for lin in lins7:
    for g in r3.images(lin, 7):
        ginv = np.empty_like(g)
        ginv[g] = np.arange(49)
        conj_K.add(tuple(g[Kmap[ginv]]))
for m_ in mirs7:
    for g in r3.images(m_, 7):
        if (g[g] == np.arange(49)).all():
            invol.add(tuple(g))
u_rec, a_rec = r4.counts_ext(Wr7, 7, lins7, mirs7)
forced(f"all {len(invol)} anti-unitary involutions at seven levels are conjugate to the mirror (q, p) -> (q, -p); "
       f"the record has {u_rec} ordinary and {a_rec} mirror symmetries",
       len(invol) == 392 and invol == conj_K and u_rec == 4 and a_rec == 4)
A13, lins13 = r3.phase_points(13), r3.linear_parts(13)
L13 = r3.legendre(13)
D13 = r3.describe(r3.wigner(L13[None, :], A13, 13)[0], 13, lins13)
forced(f"the Legendre state of 13 is even, with {D13[0]} symmetries and total negativity "
       f"{r3.negativity(r3.wigner(L13[None, :], A13, 13)[0]):.12f}",
       np.allclose(r3.basics(13)[4] @ L13, L13) and D13[0] == 24 and D13[2] == 1
       and abs(r3.negativity(r3.wigner(L13[None, :], A13, 13)[0]) - 0.933850957749) < 1e-11)
forced("the half turn's operator has determinant 1 only as (-1 | p) times the parity: det P = (-1)^((p-1)/2) for "
       "p = 3, 5, 7, 11, 13",
       all(round(np.linalg.det(r3.basics(p_)[4])) == (-1) ** ((p_ - 1) // 2) for p_ in (3, 5, 7, 11, 13)))

if FULL:
    # U1: every sign choice symmetric under the mirror, with the 8..24 bound skipping the rest
    orbits = [np.array([n_]) for n_ in range(49) if Kmap[n_] == n_] + \
             [np.array([n_, Kmap[n_]]) for n_ in range(49) if n_ < Kmap[n_]]
    C_ = np.array([A7r3[o].sum(axis=0).real for o in orbits]) / 7
    m_o = len(orbits)
    Cf_ = C_.reshape(m_o, 49)
    sizes = np.array([len(o) for o in orbits])
    ib = 20
    codes_in = np.arange(1 << ib, dtype=np.int64)
    bits_in = (codes_in[:, None] >> np.arange(ib)) & 1
    H_in = (1.0 - 2.0 * bits_in) @ Cf_[:ib]
    k_in = bits_in @ sizes[:ib]
    top_val, n_top = -1.0, 0
    for outer in range(1 << (m_o - ib)):
        bits_out = (outer >> np.arange(m_o - ib)) & 1
        k = k_in + bits_out @ sizes[ib:]
        keep = np.where((k >= 8) & (k <= 24))[0]
        if len(keep):
            lam = np.linalg.eigvalsh((H_in[keep] + (1.0 - 2.0 * bits_out) @ Cf_[ib:]).reshape(-1, 7, 7))[:, -1]
            mx = lam.max()
            if mx > top_val + 1e-9:
                top_val, n_top = mx, int((lam > mx - 1e-9).sum())
            elif mx > top_val - 1e-9:
                n_top += int((lam > top_val - 1e-9).sum())
    forced(f"(--full) every one of the 2^28 mirror-symmetric sign choices: the best gives "
           f"{(top_val - 1) / 2:.12f}, the record, reached by {n_top} choices",
           abs((top_val - 1) / 2 - N_rec) < 1e-12 and n_top == 42)
    tets = []
    for p_ in (3, 7, 11, 13):
        Ap = r3.phase_points(p_)
        states, _ = r4.tetrahedral_states(p_, Ap)
        leg = 1 if pow(p_ - 1, (p_ - 1) // 2, p_) == 1 else -1
        pars = [float(np.real(np.vdot(s_, r3.basics(p_)[4] @ s_))) for s_ in (states or [])]
        vals = sorted(round(float(r3.negativity(r3.wigner(s_[None, :], Ap, p_)[0])), 6) for s_ in (states or []))
        tets.append((p_, leg, pars, vals))
    forced("(--full) the states a binary tetrahedral group fixes, with their parities: "
           + "; ".join(f"p = {p_}: {vals}" for p_, leg, pars, vals in tets)
           + ". Each lies on the Legendre state's side",
           all(abs(x - leg) < 1e-6 for p_, leg, pars, vals in tets for x in pars)
           and [vals for p_, leg, pars, vals in tets] == [[0.333333], [], [0.899019, 1.029707], [0.982303]])

# ------------------------------------------------------------------ round 5 (round5.py; its logs are round5_*.log)
import round5 as r5

print()
print("round 5:")
ex = {}
for p_ in (17, 19):
    Ap = r3.phase_points(p_)
    Pp = r3.basics(p_)[4]
    Lp = r3.legendre(p_)
    NLp = r3.negativity(r3.wigner(Lp[None, :], Ap, p_)[0])
    leg = 1 if pow(p_ - 1, (p_ - 1) // 2, p_) == 1 else -1
    Wl = r5.Weil(p_, Ap)
    pars, vals, names = [], [], []
    for name, a_, b_ in r5.exceptional(Wl, p_):
        names.append(name.split(" (")[0])
        for st in r5.fixed_states(r5.operator(Wl, a_), r5.operator(Wl, b_)):
            pars.append(float(np.real(np.vdot(st, Pp @ st))))
            vals.append(round(float(r3.negativity(r3.wigner(st[None, :], Ap, p_)[0])), 6))
    ex[p_] = (NLp, np.allclose(Pp @ Lp, leg * Lp), leg, pars, sorted(vals), names)
forced(f"the Legendre states: at 17 even, {ex[17][0]:.12f}; at 19 odd, {ex[19][0]:.12f}",
       ex[17][1] and ex[19][1] and ex[17][2] == 1 and ex[19][2] == -1
       and abs(ex[17][0] - 1.250924335054) < 1e-11 and abs(ex[19][0] - 1.356950270213) < 1e-11)
forced("the exceptional groups' states lie on the Legendre state's side: at 17 (" + ", ".join(ex[17][5]) + ") the "
       f"values {ex[17][4]}, all even; at 19 (" + ", ".join(ex[19][5]) + f") the values {ex[19][4]}, all odd",
       all(abs(x - 1) < 1e-6 for x in ex[17][3]) and all(abs(x + 1) < 1e-6 for x in ex[19][3])
       and ex[17][4] == [1.167172, 1.167172, 1.235683, 1.235683, 1.341419, 1.341419, 1.388656, 1.388656]
       and ex[19][4] == [1.223807, 1.278772, 1.495712])

# ------------------------------------------------------------------ round 6 (round6.py; its logs are round6_*.log)
print()
print("round 6:")
ex6 = {}
for p_ in (23, 29):
    Ap = r3.phase_points(p_)
    Pp = r3.basics(p_)[4]
    Lp = r3.legendre(p_)
    leg = 1 if pow(p_ - 1, (p_ - 1) // 2, p_) == 1 else -1
    Wl = r5.Weil(p_, Ap)
    pars, vals = [], []
    for name, a_, b_ in r5.exceptional(Wl, p_):
        for st in r5.fixed_states(r5.operator(Wl, a_), r5.operator(Wl, b_)):
            pars.append(float(np.real(np.vdot(st, Pp @ st))))
            vals.append(round(float(r3.negativity(r3.wigner(st[None, :], Ap, p_)[0])), 6))
    ex6[p_] = (r3.negativity(r3.wigner(Lp[None, :], Ap, p_)[0]), np.allclose(Pp @ Lp, leg * Lp), leg, pars,
               sorted(vals))
forced(f"the Legendre states: at 23 odd, {ex6[23][0]:.12f}; at 29 even, {ex6[29][0]:.12f}",
       ex6[23][1] and ex6[29][1] and ex6[23][2] == -1 and ex6[29][2] == 1
       and abs(ex6[23][0] - 1.341641910165) < 1e-11 and abs(ex6[29][0] - 1.878678879531) < 1e-11)
forced(f"the exceptional groups' states lie on the Legendre state's side: at 23 the values {ex6[23][4]}, all odd; "
       f"at 29 the values {ex6[29][4]}, all even",
       all(abs(x + 1) < 1e-6 for x in ex6[23][3]) and all(abs(x - 1) < 1e-6 for x in ex6[29][3])
       and ex6[23][4] == [1.490815, 1.490815, 1.490815, 1.490815] and ex6[29][4] == [1.656907, 1.79327, 1.79327])

# ------------------------------------------------------------------ round 8 (two_wheels.py; its logs are two_wheels_*.log)
print()
print("round 8:")


def wheels(p_):
    """each wheel's operators of order m > 2 at p, built as two_wheels.py builds them: the turning wheel's from an
    element of order p + 1, the multiplying wheel's from a primitive root"""
    Ap = r3.phase_points(p_)
    Wl = r5.Weil(p_, Ap)
    g = next(a for a in range(2, p_) if len({pow(a, e, p_) for e in range(1, p_)}) == p_ - 1)
    X = next(Y for Y in Wl.parent if r5.order(Y, p_) == p_ + 1)
    out = {}
    for m in (m for m in range(3, p_ + 2) if (p_ + 1) % m == 0):
        Y = (1, 0, 0, 1)
        for _ in range((p_ + 1) // m):
            Y = r5.mul(Y, X, p_)
        out["turning", m] = r5.operator(Wl, Y)
    for m in (m for m in range(3, p_) if (p_ - 1) % m == 0):
        a = pow(g, (p_ - 1) // m, p_)
        out["multiplying", m] = np.eye(p_)[[(pow(a, -1, p_) * k) % p_ for k in range(p_)]].astype(complex)
    return Ap, out


def lines_best(U, Ap, p_):
    """the best state among U's one-line eigenspaces, which is exact"""
    ones = [Q[:, 0] for Q in r3.eigenspaces(U) if Q.shape[1] == 1]
    return max(r3.negativity(r3.wigner(v[None, :], Ap, p_)[0]) for v in ones)


DIMS8 = {13: {("turning", 7): [2] * 6 + [1], ("turning", 14): [1] * 13, ("multiplying", 3): [5, 4, 4],
              ("multiplying", 4): [4, 3, 3, 3], ("multiplying", 6): [3, 2, 2, 2, 2, 2],
              ("multiplying", 12): [2] + [1] * 11},
         23: {("turning", 3): [8, 8, 7], ("turning", 4): [6, 6, 6, 5], ("turning", 6): [4] * 5 + [3],
              ("turning", 8): [3] * 7 + [2], ("turning", 12): [2] * 11 + [1], ("turning", 24): [1] * 23,
              ("multiplying", 11): [3] + [2] * 10, ("multiplying", 22): [2] + [1] * 21}}
w8 = {p_: wheels(p_) for p_ in (13, 23)}
dims8 = {p_: {key: sorted((Q.shape[1] for Q in r3.eigenspaces(U)), reverse=True) for key, U in w8[p_][1].items()}
         for p_ in (13, 23)}
forced("the confound of family size: at 13 the turning wheel's orders above 2 are only 7 and 14, against the "
       "multiplying wheel's 3, 4, 6 and 12; at 23 the turning wheel has 3, 4, 6, 8, 12 and 24 and the multiplying "
       "wheel only 11 and 22; every eigenspace dimension is as two_wheels_A.log records it", dims8 == DIMS8)
A13, U13 = w8[13]
A23, U23 = w8[23]
l13 = lines_best(U13["turning", 14], A13, 13)
l23t = lines_best(U23["turning", 24], A23, 23)
l23m = lines_best(U23["multiplying", 22], A23, 23)
forced(f"the one-line families are exact and agree with the log: at 13 the turning wheel's order 14, {l13:.9f}; at "
       f"23 the turning wheel's order 24, {l23t:.9f}, and the multiplying wheel's order 22, {l23m:.9f}",
       abs(l13 - 1.105228575) < 1e-9 and abs(l23t - 1.627721703) < 1e-9 and abs(l23m - 1.602496306) < 1e-9)
U7 = U13["turning", 7]
orb7 = r3.cycles(r3.perm_of(U7, A13))
t13 = max((r4.exact_best_big(r3.compress(A13, Q), 13, orb7)[0][0][0] - 1) / 2 if Q.shape[1] > 1
          else r3.negativity(r3.wigner(Q[:, 0][None, :], A13, 13)[0]) for Q in r3.eigenspaces(U7))
rng8 = np.random.default_rng(20261112)
m13 = max(r3.search(r3.compress(A13, Q), 13, 4000, rng8, batch=4000)[0].max()
          for Q in r3.eigenspaces(U13["multiplying", 4]))
forced(f"Y1's death at 13 is exact: counting every sign choice constant on the {len(orb7)} orbits of the turning "
       f"wheel's order 7 (2^25 in each eigenspace) puts its best state at {t13:.9f}, which order 14 shares; a search "
       f"finds a state that the multiplying wheel's order 4 fixes at {m13:.9f}",
       len(orb7) == 25 and abs(t13 - 1.105228575) < 1e-9 and m13 > 1.16736394)


# ------------------------------------------------------------------ round 7 (round7.py; its logs are round7_*.log)
print()
print("round 7:")


def period_of(b, p_):
    """the b-wheel's period modulo p: how many steps b, b^2, ... take to return to 1"""
    r, x = 1, b % p_
    while x != 1:
        x, r = x * b % p_, r + 1
    return r


WON = {5: "even", 7: "even", 11: "even", 13: "even", 17: "even", 19: "odd", 23: "even", 29: "odd", 31: "even"}


def wheel_fits(b, upto):
    return all(("even" if period_of(b, q) % 2 == 0 else "odd") == w for q, w in WON.items() if b % q and q <= upto)


fits29 = [b for b in range(2, 31) if wheel_fits(b, 29)]
fits31 = [b for b in range(2, 31) if wheel_fits(b, 31)]
forced(f"the 7-wheel has period {period_of(7, 31)} at 31 and {period_of(7, 37)} at 37, so the author's rule called "
       f"the odd side at both; with the sides that won from 5 to 29, the bases from 2 to 30 that fit every prime are "
       f"{fits29}, and with 31's even win, {fits31}",
       period_of(7, 31) == 15 and period_of(7, 37) == 9 and fits29 == [7] and fits31 == [])
A31 = r3.phase_points(31)
P31 = r3.basics(31)[4]
L31 = r3.legendre(31)
NL31 = r3.negativity(r3.wigner(L31[None, :], A31, 31)[0])
W31 = r5.Weil(31, A31)
pars31, vals31 = [], []
for name, a_, b_ in r5.exceptional(W31, 31):
    for st in r5.fixed_states(r5.operator(W31, a_), r5.operator(W31, b_)):
        pars31.append(float(np.real(np.vdot(st, P31 @ st))))
        vals31.append(round(float(r3.negativity(r3.wigner(st[None, :], A31, 31)[0])), 6))
forced(f"at 31 the Legendre state is odd, {NL31:.12f}, and the exceptional groups' states lie on its side: the values "
       f"{sorted(vals31)}, all odd",
       np.allclose(P31 @ L31, -L31) and abs(NL31 - 1.736567405507) < 1e-11
       and all(abs(x + 1) < 1e-6 for x in pars31) and sorted(vals31) == [1.779773] * 4 + [1.906903] * 4)

# ------------------------------------------------------------------ round 9 (many_wheels.py; its logs are many_wheels_*.log)
print()
print("round 9:")
from scipy.special import betainc

A3 = r3.phase_points(3)
A33 = np.einsum("aij,bkl->abikjl", A3, A3).reshape(81, 9, 9)          # two wheels of 3: products of operators
P3 = r3.basics(3)[4]
ev0 = np.linalg.eigvalsh(A33[0])
forced("two wheels of 3: each of the 81 points' operators is the product of the wheels' operators, they sum to 9 "
       "times the identity, and the origin's is the two half turns at once, with 5 eigenvalues +1 and 4 eigenvalues -1",
       np.allclose(A33.sum(axis=0), 9 * np.eye(9)) and np.allclose(A33[0], np.kron(P3, P3))
       and int((ev0 > 0).sum()) == 5 and int((ev0 < 0).sum()) == 4)
strange = np.array([0, 1, -1], complex) / np.sqrt(2)
N1 = r3.negativity(r3.wigner(strange[None, :], A3, 3)[0])
two = np.kron(strange, strange)
W2 = r3.wigner(two[None, :], A33, 9)[0]
N2 = r3.negativity(W2)


def sre2_state(psi, p_, n_):
    """M2 = -ln( sum over the D^2 Weyl operators of |<psi|W|psi>|^4 / D ), as many_wheels.py computes it"""
    T = psi.reshape((p_,) * n_)
    tot = 0.0
    for x in itertools.product(range(p_), repeat=n_):
        R = np.roll(T, shift=[-xi for xi in x], axis=tuple(range(n_)))
        tot += (np.abs(np.fft.fftn(np.conj(R) * T)) ** 4).sum()
    return float(-np.log(tot / p_ ** n_))


m2one, m2two = sre2_state(strange, 3, 1), sre2_state(two, 3, 2)
forced(f"a product's sum of sizes multiplies: the strange state has negativity {N1:.12f} = 1/3, and two of them side "
       f"by side {N2:.12f} = 8/9, the value Z1 found as the best at two wheels; their M2 are ln 2 and ln 4 "
       f"({m2one:.9f} and {m2two:.9f}), as the log records for the best states found there",
       abs(N1 - 1 / 3) < 1e-12 and abs(N2 - 8 / 9) < 1e-12 and abs(m2one - np.log(2)) < 1e-9
       and abs(m2two - np.log(4)) < 1e-9)


def mean_random(D):
    """the average sum of sizes over random states, as a fraction of sqrt D: each point's value is 2B - 1 with
    B ~ Beta((D + 1)/2, (D - 1)/2)"""
    if D > 10 ** 12:
        return float(np.sqrt(2 / np.pi))
    a, b = (D + 1) / 2, (D - 1) / 2
    m = a / (a + b)
    return float(np.sqrt(D) * 2 * ((m - 0.5) + 2 * (0.5 * betainc(a, b, 0.5) - m * betainc(a + 1, b, 0.5))))


rng9 = np.random.default_rng(20261110)
G = rng9.normal(size=(20000, 9)) + 1j * rng9.normal(size=(20000, 9))
G /= np.linalg.norm(G, axis=1, keepdims=True)
S = np.abs(r3.wigner(G, A33, 9)).sum(axis=1) / 3                         # sum of sizes over sqrt D
mc, se = S.mean(), S.std() / np.sqrt(len(S))
forced(f"the average random state's formula agrees with 20000 random states at two wheels of 3: {mean_random(9):.4f} "
       f"against {mc:.4f} +/- {se:.4f}", abs(mc - mean_random(9)) < 4 * se)
f9 = {3: (1 + 2 / 3) / np.sqrt(3), 5: (1 + 2 * 0.556677223351) / np.sqrt(5), 7: (1 + 2 * 0.732522000011) / np.sqrt(7)}
cross = {q: next(k for k in range(1, 200) if f9[q] ** k < mean_random(q ** k)) for q in (3, 5, 7)}
hundred = {q: f9[q] ** 100 for q in (3, 5, 7)}
forced(f"the 10 x 10 array: the best single-wheel state repeated reaches {f9[3]:.3f}, {f9[5]:.3f} and {f9[7]:.3f} of the "
       f"ceiling per wheel at 3, 5 and 7 levels; the average random state is ahead from {cross[3]}, {cross[5]} and "
       f"{cross[7]} wheels on; at 100 wheels the products reach {hundred[3]:.3g}, {hundred[5]:.3g} and "
       f"{hundred[7]:.3g}, the average random state {mean_random(3 ** 100):.3f}",
       cross == {3: 6, 5: 4, 7: 4} and abs(hundred[3] - 0.0213) < 5e-5 and abs(hundred[5] - 0.00354) < 5e-6
       and abs(hundred[7] - 0.000846) < 5e-7 and abs(mean_random(3 ** 100) - np.sqrt(2 / np.pi)) < 1e-12)


# the norm state of the 27-element field, read after round 9's run (README section 11)
def field_mul(x, y, p_, modulus):
    """multiply in F_p[t]/(modulus), modulus monic, coefficients lowest degree first; elements as tuples"""
    n_ = len(modulus) - 1
    prod = [0] * (2 * n_ - 1)
    for i in range(n_):
        for j in range(n_):
            prod[i + j] += x[i] * y[j]
    for k in range(2 * n_ - 2, n_ - 1, -1):                               # reduce t^k with t^n = -(lower terms)
        c, prod[k] = prod[k], 0
        for i in range(n_):
            prod[k - n_ + i] -= c * modulus[i]
    return tuple(v % p_ for v in prod[:n_])


def field_pow(x, e, p_, modulus):
    r = tuple([1] + [0] * (len(modulus) - 2))
    for _ in range(e):
        r = field_mul(r, x, p_, modulus)
    return r


def wigner_contract(psi, p_, n_):
    """<A_u> at every point of n wheels, one wheel at a time, in the order of many_wheels.array_points"""
    A1 = r3.phase_points(p_)
    R = np.outer(psi.conj(), psi).reshape((p_,) * (2 * n_))
    for k in range(n_):
        R = np.moveaxis(R, [0, n_ - k], [0, 1])
        R = np.moveaxis(np.tensordot(A1, R, axes=([1, 2], [0, 1])), 0, -1)
    return R.reshape(-1).real


def degree_le2(vals, p_, n_):
    """is the function F_p^n -> F_p with these values (in itertools.product order) a polynomial of degree <= 2?"""
    pts_ = list(itertools.product(range(p_), repeat=n_))
    mons = [lambda x: 1] + [lambda x, i=i: x[i] for i in range(n_)] + \
           [lambda x, i=i, k=k: x[i] * x[k] for i in range(n_) for k in range(i, n_)]
    M = [[m(x) % p_ for m in mons] + [v % p_] for x, v in zip(pts_, vals)]
    r, cols = 0, len(mons)
    for c in range(cols):
        piv = next((i for i in range(r, len(M)) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, p_)
        M[r] = [(v * inv) % p_ for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                fct = M[i][c]
                M[i] = [(a - fct * b) % p_ for a, b in zip(M[i], M[r])]
        r += 1
    return all(row[cols] == 0 for row in M[r:])


MOD27 = [2, 2, 0, 1]                                                     # t^3 - t - 1 over F_3
F27 = list(itertools.product(range(3), repeat=3))                       # c0 + c1 t + c2 t^2 is the basis state |c0 c1 c2>
NORM = {x: field_pow(x, 13, 3, MOD27) for x in F27}                      # N(x) = x x^3 x^9 = x^13
norm_in_f3 = all(v[1] == 0 and v[2] == 0 for v in NORM.values())
NORM = {x: v[0] for x, v in NORM.items()}
w3 = np.exp(2j * np.pi / 3)
psiN = np.array([w3 ** NORM[x] for x in F27]) / np.sqrt(27)
exN = wigner_contract(psiN, 3, 3)
levN = Counter(np.round(exN * 9).astype(int).tolist())
NN = (np.abs(exN).sum() / 27 - 1) / 2
P27 = np.kron(np.kron(P3, P3), P3)
forced(f"the norm state of the 27-element field, sum of w^N(x) |x> / sqrt 27 with N(x) = x^13: N lies in F_3; its "
       f"<A_u> take the values 2/9, -1/9 and -4/9 at {levN.get(2)}, {levN.get(-1)} and {levN.get(-4)} points, so its "
       f"negativity is {NN:.12f} = 17/9; |<A_u>| <= {np.abs(exN).max():.6f} = 4/9 everywhere, so it is no point's "
       f"eigenstate; the half turn sends it to its complex conjugate",
       norm_in_f3 and levN == {2: 351, -1: 351, -4: 27} and abs(NN - 17 / 9) < 1e-12
       and abs(np.abs(exN).max() - 4 / 9) < 1e-12 and abs(exN[0] + 4 / 9) < 1e-12 and np.allclose(P27 @ psiN, psiN.conj()))
eta27 = np.array([0 if NORM[x] == 0 else (1 if NORM[x] == 1 else -1) for x in F27], complex)
odd_part = (psiN - P27 @ psiN) / 2
forced("its odd part, of weight 13/18, is i sqrt(3)/2 times the field's Legendre state (the quadratic character "
       "x^13 as amplitudes); its even part, of weight 5/18, is |0> minus half of every other basis state, over sqrt 27",
       np.allclose(odd_part, 1j * np.sqrt(3) / 2 * eta27 / np.sqrt(27))
       and abs(np.vdot(odd_part, odd_part).real - 13 / 18) < 1e-12
       and np.allclose((psiN + P27 @ psiN) / 2, np.array([1.0] + [-0.5] * 26) / np.sqrt(27)))
# its characteristic function: zero on the 26 Z-type Weyl operators, 1/sqrt 27 in size on the other 702
X3, Z3 = np.roll(np.eye(3), 1, axis=0), np.diag(w3 ** np.arange(3))
chiN = {}
for a_ in F27:
    for b_ in F27:
        Wop = np.ones((1, 1), complex)
        for ai, bi in zip(a_, b_):
            Wop = np.kron(Wop, mp(Z3, bi) @ mp(X3, ai))
        chiN[a_, b_] = abs(np.vdot(psiN, Wop @ psiN))
zeroN = [k for k, v in chiN.items() if v < 1e-9]
forced(f"its Weyl expectations vanish on {len(zeroN)} operators, the Z-type ones (a Lagrangian with the identity), and "
       f"have size 1/sqrt 27 on the other {sum(1 for k, v in chiN.items() if abs(v - 27 ** -0.5) < 1e-9)}",
       sorted(zeroN) == sorted(((0, 0, 0), b_) for b_ in F27 if any(b_))
       and all(abs(v - 27 ** -0.5) < 1e-9 for k, v in chiN.items() if k[0] != (0, 0, 0)))
# its symmetries: 27 shifts, each with a quadratic phase, and 39 linear maps
idx27 = {x: i for i, x in enumerate(F27)}
squares = [m for m in F27 if any(m) and field_pow(m, 13, 3, MOD27) == (1, 0, 0)]
lin_maps = [lambda x, m=m, k=k: field_mul(m, field_pow(x, 3 ** k, 3, MOD27), 3, MOD27) for m in squares for k in range(3)]
add27 = lambda x, y: tuple((u + v) % 3 for u, v in zip(x, y))
lin_ok = all(all(L(add27(x, y)) == add27(L(x), L(y)) for x in F27[:9] for y in F27[:9]) and
             np.allclose(psiN[[idx27[L(x)] for x in F27]], psiN) for L in lin_maps)
shift_ok = all(degree_le2([(NORM[add27(x, a_)] - NORM[x]) % 3 for x in F27], 3, 3) for a_ in F27)
forced(f"its symmetries include {len(lin_maps)} linear maps, x -> m x^(3^k) for the {len(squares)} nonzero squares m "
       f"and k = 0, 1, 2, which fix it as permutations of the basis, and the 27 shifts x -> x + a, each made a "
       f"symmetry by the phase w^(N(x) - N(x + a)), a quadratic phase since N(x + a) - N(x) has degree 2: "
       f"{27 * len(lin_maps)} in all",
       len(squares) == 13 and len(lin_maps) == 39 and lin_ok and shift_ok)
m2N = sre2_state(psiN, 3, 3)
LOGGED_WHOLE33 = (1.888888888889, 2.621381818)                          # many_wheels_three.log: value and M2
forced(f"its M2 is ln(729/53) = {m2N:.9f}, the M2 that many_wheels_three.log records for the {LOGGED_WHOLE33[0]} "
       f"state the run found in the whole space of three wheels of 3",
       abs(m2N - np.log(729 / 53)) < 1e-9 and abs(LOGGED_WHOLE33[1] - m2N) < 1e-8
       and abs(LOGGED_WHOLE33[0] - 17 / 9) < 1e-11)
# the norm states of other arrays: stabilizer states at two wheels; 2000/729 at four wheels of 3
other = {}
for p_, mod_ in ((3, [1, 0, 1]), (5, [2, 0, 1]), (7, [1, 0, 1]), (3, [1, 0, 1, 1, 1])):    # irreducible moduli
    n_ = len(mod_) - 1
    els_ = list(itertools.product(range(p_), repeat=n_))
    e_ = (p_ ** n_ - 1) // (p_ - 1)
    wp = np.exp(2j * np.pi / p_)
    nv = [field_pow(x, e_, p_, mod_) for x in els_]
    assert all(all(c == 0 for c in v[1:]) for v in nv)
    ps = np.array([wp ** v[0] for v in nv]) / np.sqrt(p_ ** n_)
    ex_ = wigner_contract(ps, p_, n_)
    other[p_, n_] = (np.abs(ex_).sum() / p_ ** n_ - 1) / 2
forced(f"the norm states of the other arrays: at two wheels of 3, 5 and 7 the norm is quadratic and the state has "
       f"negativity {other[3, 2]:.1e}, {other[5, 2]:.1e} and {other[7, 2]:.1e}; at four wheels of 3 it has "
       f"{other[3, 4]:.12f} = 2000/729, below 98/27",
       max(other[3, 2], other[5, 2], other[7, 2]) < 1e-12 and abs(other[3, 4] - 2000 / 729) < 1e-12)
if FULL:
    # every affine map of the field's coordinates that keeps the norm state up to a quadratic phase
    count = 0
    for m in itertools.product(range(3), repeat=9):
        Mx = np.array(m).reshape(3, 3)
        if round(np.linalg.det(Mx)) % 3 == 0:
            continue
        for a_ in F27:
            img = [tuple((Mx @ np.array(x) + np.array(a_)) % 3) for x in F27]
            if degree_le2([(NORM[y] - NORM[x]) % 3 for x, y in zip(F27, img)], 3, 3):
                count += 1
    forced(f"(--full) every affine map x -> Mx + a that keeps the norm state up to a quadratic phase, among all "
           f"11232 x 27: {count}, so its Clifford symmetries are exactly 27 x 39", count == 1053)
if FULL:
    # the states of each field's multiplicative characters, sum over x != 0 of chi(x) |x>: all below the bests found
    BESTS9 = {(3, 2): 8 / 9, (3, 3): 17 / 9, (3, 4): 98 / 27, (5, 2): 1.766937254162, (7, 2): 2.719253432179}
    MODS9 = {(3, 2): [1, 0, 1], (3, 3): MOD27, (3, 4): [1, 0, 1, 1, 1], (5, 2): [2, 0, 1], (7, 2): [1, 0, 1]}
    char_top = {}
    for (p_, n_), mod_ in MODS9.items():
        q_ = p_ ** n_
        els_ = list(itertools.product(range(p_), repeat=n_))
        one_ = tuple([1] + [0] * (n_ - 1))

        def order_of(g):
            x, k = g, 1
            while x != one_:
                x, k = field_mul(x, g, p_, mod_), k + 1
            return k

        gen = next(g for g in els_ if any(g) and order_of(g) == q_ - 1)
        logs, x = {}, one_
        for k in range(q_ - 1):
            logs[x] = k
            x = field_mul(x, gen, p_, mod_)
        tops = []
        for k in range(1, q_ - 1):
            z = np.exp(2j * np.pi * k / (q_ - 1))
            ps = np.array([0 if not any(x) else z ** logs[x] for x in els_]) / np.sqrt(q_ - 1)
            ex_ = wigner_contract(ps, p_, n_)
            tops.append((np.abs(ex_).sum() / q_ - 1) / 2)
        char_top[p_, n_] = max(tops)
    forced("(--full) the states of the fields' multiplicative characters stay below every array's best: at most "
           + ", ".join(f"{char_top[k]:.6f} against {BESTS9[k]:.6f}" for k in MODS9),
           all(char_top[k] < BESTS9[k] - 1e-3 for k in MODS9))

# ------------------------------------------------------------------ round 10 (larger_arrays.py; its logs are larger_arrays_*.log)
print()
print("round 10:")
import larger_arrays as la

# the structured Wigner function equals the operators' one, point by point, on arrays round 9 wrote out
rng10 = np.random.default_rng([20261110, 10, 99])
err10 = 0.0
for p_, n_ in ((3, 2), (3, 3), (5, 2)):
    arr_ = la.Array(p_, n_)
    psi_ = rng10.normal(size=p_ ** n_) + 1j * rng10.normal(size=p_ ** n_)
    psi_ /= np.linalg.norm(psi_)
    dense_ = wigner_contract(psi_, p_, n_) / p_ ** n_                    # many_wheels' order: (q1 k1)(q2 k2)...
    fast_ = arr_.wigner(psi_[None, :])[0]                                # larger_arrays' order: (q1 q2 ..)(k1 k2 ..)
    dg_ = arr_.digits
    order_ = [int(sum(int(x) * (p_ * p_) ** (n_ - 1 - i) for i, x in enumerate(dg_[qi] * p_ + dg_[ki])))
              for qi in range(p_ ** n_) for ki in range(p_ ** n_)]
    err10 = max(err10, np.abs(dense_[order_] - fast_.ravel()).max())
forced(f"larger_arrays.py's Wigner function, one Fourier transform per point q, equals the operators' one at every point "
       f"of two and three wheels of 3 and two of 5 (largest difference {err10:.1e})", err10 < 1e-14)


def kloosterman(p_):
    a_ = np.arange(1, p_)
    inv_ = np.array([pow(int(x), -1, p_) for x in a_])
    return np.array([np.cos(2 * np.pi * ((a_ + m * inv_) % p_) / p_).sum() for m in range(1, p_)])


def norm_closed_form(p_):
    """the negativity of every norm-type state on three wheels of p: sum|W| = [(p + 1) + (p^2 + p + 1) sum_m |K(m)|]/p^2"""
    return (((p_ + 1) + (p_ * p_ + p_ + 1) * np.abs(kloosterman(p_)).sum()) / p_ ** 2 - 1) / 2


theorem_ok, closed_ok, rows10 = True, True, []
for p_ in (3, 5, 7):
    arr_ = la.Array(p_, 3)
    q_ = p_ ** 3
    K_ = kloosterman(p_)
    for c_ in range(1, p_):
        psi_ = la.norm_state(p_, 3, c_)
        C_ = la.weyl_sizes(arr_, psi_)                                   # rows a, columns b: |<psi| Z^b X^a |psi>|
        W_ = arr_.wigner(psi_[None, :])[0]
        theorem_ok &= bool(np.abs(C_[0, 1:]).max() < 1e-12 and np.allclose(C_[1:, :], q_ ** -0.5, atol=1e-12)
                           and q_ * np.abs(W_).max() < 1 - 1e-6
                           and np.allclose(psi_[arr_.neg], psi_.conj(), atol=1e-14))
        # the Wigner values: K(m)/p^5 at (p^2 + p + 1) q points for each m in F_p*, and -(p + 1)/p^5 at q points
        want = np.sort(np.concatenate([np.repeat(K_ / p_ ** 5, (p_ * p_ + p_ + 1) * q_),
                                       np.full(q_, -(p_ + 1) / p_ ** 5)]))
        closed_ok &= bool(np.allclose(np.sort(W_.ravel()), want, atol=1e-14))
        m2_ = float(-np.log((C_ ** 4).sum() / q_))
        theorem_ok &= abs(m2_ - np.log(q_ ** 2 / (2 * q_ - 1))) < 1e-9
    Nn_ = arr_.negativity(arr_.wigner(la.norm_state(p_, 3, 1)[None, :]))[0]
    closed_ok &= abs(Nn_ - norm_closed_form(p_)) < 1e-11
    rows10.append(f"{Nn_:.9f} at {p_} levels ({Nn_ / ((np.sqrt(q_) - 1) / 2):.4f} of the ceiling)")
forced("on three wheels of 3, 5 and 7, every norm-type state sum_x w^(c N(x)) |x> has Weyl expectations zero on the "
       "Z-type operators and of size 1/sqrt(p^3) on all others, is no point's eigenstate, is sent to its complex "
       "conjugate by the half turn, and has M2 = ln(q^2/(2q - 1))", theorem_ok)
big10 = {p_: norm_closed_form(p_) / ((p_ ** 1.5 - 1) / 2) for p_ in (997, 1999)}
forced("its Wigner values are Kloosterman sums: K(m)/p^5 at (p^2 + p + 1) p^3 points for each m in F_p*, and "
       "-(p + 1)/p^5 at p^3 points, for every c; so its negativity is " + "; ".join(rows10)
       + f"; and toward 8/(3 pi) = {8 / (3 * np.pi):.4f} of the ceiling at large p ({big10[997]:.4f} at 997, "
       f"{big10[1999]:.4f} at 1999)", closed_ok and abs(big10[1999] - 8 / (3 * np.pi)) < 0.01)
arr35 = la.Array(3, 5)
psi35 = la.norm_state(3, 5, 1)
N35 = arr35.negativity(arr35.wigner(psi35[None, :]))[0]
z35 = la.zero_set(arr35, psi35)
forced(f"on five wheels of 3 the norm state has negativity {N35:.12f} = 4232/729; its Weyl expectations vanish on "
       f"{z35[0]} operators, a Lagrangian with the identity, but it is not flat, so the theorem stops at three wheels",
       abs(N35 - 4232 / 729) < 1e-11 and z35 == (242, True, False))
# the scores, from the values larger_arrays_run.log records, and the bars from round 9's logged bests
LOG10 = {(5, 3): dict(even=4.293476409921, odd=4.291597773343, whole=4.162583641648, kicks=4.301387418094,
                      norm=4.252724292100, normfix=4.252724292100),
         (3, 5): dict(even=6.082020166220, odd=6.069251540379, whole=5.925176606383, kicks=6.052265927721,
                      norm=5.805212620027, normfix=6.052265927720),
         (7, 3): dict(even=7.238233221470, odd=7.241590191964, whole=7.097607760339, kicks=7.902228372125,
                      norm=7.902228372133, normfix=7.902228372133)}
R9B = {(3, 1): 1 / 3, (3, 4): 98 / 27, (5, 1): 0.556677223351, (5, 2): 1.766937254162, (7, 1): 0.732522000011,
       (7, 2): 2.719253432179}
S10 = lambda N: 1 + 2 * N
bar10 = {(5, 3): (S10(R9B[5, 1]) * S10(R9B[5, 2]) - 1) / 2, (3, 5): (S10(R9B[3, 4]) * S10(R9B[3, 1]) - 1) / 2,
         (7, 3): (S10(R9B[7, 1]) * S10(R9B[7, 2]) - 1) / 2}
best10 = {k: max(v.values()) for k, v in LOG10.items()}
ceil10 = {k: (np.sqrt(k[0] ** k[1]) - 1) / 2 for k in LOG10}
v10 = {"V0": True,
       "V1": all(best10[k] <= LOG10[k]["norm"] + 1e-9 for k in ((5, 3), (7, 3))),
       "V2": all(LOG10[k]["norm"] > max(LOG10[k]["even"], LOG10[k]["odd"]) + 1e-9 for k in ((5, 3), (7, 3))),
       "V3": best10[3, 5] > LOG10[3, 5]["norm"] + 1e-9,
       "V4": all(best10[k] > bar10[k] + 1e-9 for k in LOG10),
       "V5": all(LOG10[k]["odd"] > LOG10[k]["even"] + 1e-9 for k in LOG10),
       "V6": all(best10[k] >= 0.88 * ceil10[k] for k in LOG10)}
RECORDED10 = {"V0": True, "V1": False, "V2": False, "V3": True, "V4": False, "V5": False, "V6": False}
forced(f"the logged norm-type values are the closed form's ({norm_closed_form(5):.12f} and {norm_closed_form(7):.12f}); "
       f"the registered bars are products of round 9's logged bests ({bar10[5, 3]:.6f}, {bar10[3, 5]:.6f} = 517/81 and "
       f"{bar10[7, 3]:.6f}); and the logged values give the recorded scores: "
       + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in v10.items()),
       abs(LOG10[5, 3]["norm"] - norm_closed_form(5)) < 1e-11 and abs(LOG10[7, 3]["norm"] - norm_closed_form(7)) < 1e-11
       and abs(bar10[3, 5] - 517 / 81) < 1e-12 and abs(bar10[5, 3] - 4.290842) < 1e-6
       and abs(bar10[7, 3] - 7.435601) < 1e-6 and v10 == RECORDED10)
if FULL:
    # read after the run (flat_states.py): every flat state tried falls at or below the norm-type states
    import flat_states as fs
    flat10 = {}
    for p_ in (5, 7):
        cls_ = fs.scan(p_)
        flat10[p_] = (max(N for (N, fl) in cls_ if fl), max(N for (N, fl), c in cls_.items() if fl and "Alltop" in c),
                      sum(sum(c.values()) for (N, fl), c in cls_.items() if fl))
    gr_flat, gr_vals = fs.galois_ring_profile()
    forced(f"(--full) the flat states w^(Tr(a x^3) + b N(x)) on three wheels of 5 and 7: {flat10[5][2]} and "
           f"{flat10[7][2]} of them flat, the best {flat10[5][0]:.9f} and {flat10[7][0]:.9f}, the norm-type states' "
           f"values; the Alltop states (b = 0) reach {flat10[5][1]:.9f} and {flat10[7][1]:.9f}; the {sum(gr_vals.values())} "
           f"Galois-ring states on three wheels of 3 are all flat, at {max(gr_vals):.9f}, below 17/9",
           abs(flat10[5][0] - norm_closed_form(5)) < 1e-8 and abs(flat10[7][0] - norm_closed_form(7)) < 1e-8
           and abs(flat10[5][1] - 4.057182539) < 1e-8 and abs(flat10[7][1] - 7.458637718) < 1e-8
           and flat10[5][2] == 128 and flat10[7][2] == 804 and gr_flat == 702 and list(gr_vals) == [1.738432946])
    # read after the run (product_climbs.py): the seeded odd climbs on four wheels of 3, and the best state found on
    # three wheels of 5, rerun and checked
    import product_climbs as pc
    _, n4, psi4, used4 = pc.regain(("regain", 3, 4, "odd", 3.476833049264, 20_000))
    ex4 = wigner_contract(psi4, 3, 4)
    N4 = (np.abs(ex4).sum() / 81 - 1) / 2
    P81 = np.kron(np.kron(P3, P3), np.kron(P3, P3))
    forced(f"(--full) four wheels of 3: product_climbs.py's seeded odd climbs reach {N4:.12f} after {used4} climbs, by "
           f"the operators' contraction, at a state the half turn sends to minus itself; round 9 logged 3.476833 for the "
           f"odd side, and the even side's 98/27 stays ahead",
           abs(N4 - 3.533330767884) < 1e-9 and abs(n4 - N4) < 1e-9 and np.allclose(P81 @ psi4, -psi4) and N4 < 98 / 27)
    _, vals5, reps5, _, _ = la.kick_job(("kick", 5, 3, 2, 0.3, la.KICKS[5, 3], 100))
    top5 = max(reps5)
    psi5 = reps5[top5][0]
    W5 = la.Array(5, 3).wigner(psi5[None, :])[0]
    ov5 = abs(np.vdot(la.norm_state(5, 3, 2), psi5)) ** 2
    forced(f"(--full) three wheels of 5: round 10's kicks of the norm-type state c = 2 at size 0.3, rerun, climb to "
           f"{top5:.9f}, at a state that no point's operator has as an eigenstate (largest |<A_u>| "
           f"{125 * np.abs(W5).max():.6f}), so on neither face, and whose overlap with that norm-type state is {ov5:.6f}",
           abs(top5 - 4.301387418) < 1e-8 and 125 * np.abs(W5).max() < 0.3 and abs(ov5 - 0.956327) < 1e-5)

# ------------------------------------------------------------------ round 11 (oscillator_states.py; its logs are oscillator_states_*.log)
print()
print("round 11:")
import oscillator_states as osc

ok_torus, ok_sums, ok_levels, ok_id = True, True, True, True
for p_ in [q_ for q_ in osc.PRIMES if q_ <= 61]:
    Psi_, chk_ = osc.nonsplit_states(p_)
    Wn_ = osc.wigner(Psi_, p_)
    Ws_ = osc.wigner(osc.split_states(p_), p_)
    ok_torus &= bool(chk_["unitary"] and chk_["order"] == p_ + 1 and chk_["ortho"])
    if p_ in osc.ROUND8_TURNING:
        ok_torus &= abs(((np.abs(Wn_).sum(axis=(1, 2)) - 1) / 2).max() - osc.ROUND8_TURNING[p_]) < 2e-9
    for WW in (Wn_, Ws_):
        ok_sums &= bool(np.allclose(WW.sum(axis=(1, 2)), 1, atol=1e-12)
                        and np.allclose((WW ** 2).sum(axis=(1, 2)), 1 / p_, atol=1e-14))
        ok_levels &= max(1 + int((np.diff(np.sort(w.ravel() * p_ ** 1.5)) > 1e-7).sum()) for w in WW) <= p_ + 2
    off_ = Wn_.reshape(len(Wn_), -1)[:, 1:]
    ok_id &= abs(((off_ ** 4).mean(axis=1) / ((off_ ** 2).mean(axis=1)) ** 2).mean() - 2 * p_ / (p_ + 1)) < 1e-12
forced("the chirp's map generates the non-split torus (order p + 1) at every prime from 5 to 61, and its best "
       "eigenvector gives round 8's logged values from 5 to 29", ok_torus)
forced("every oscillator state from 5 to 61 has sum W = 1 and sum W^2 = 1/p, so S/sqrt p is mean |W| over rms W; and "
       "its Wigner function takes at most p + 2 values, constant on the torus's orbits", ok_sums and ok_levels)
forced("averaged over the non-split torus's eigenvectors, mu4/mu2^2 is 2p/(p + 1) at every prime from 5 to 61, to "
       "within 1e-12", ok_id)
LOG11 = dict(mean_s=0.846813, mean_r4=2.0032, wins=65, primes=77, best_from_37=0.8824)   # oscillator_states_combined.log
v11 = {"O1": abs(LOG11["mean_s"] - 8 / (3 * np.pi)) <= 0.01, "O2": abs(LOG11["mean_r4"] - 2) <= 0.1,
       "O3": LOG11["wins"] > 0.75 * LOG11["primes"], "O4": LOG11["best_from_37"] < 0.90}
forced(f"the logged values give the recorded scores: mean S/sqrt p {LOG11['mean_s']} against 8/(3 pi) = "
       f"{8 / (3 * np.pi):.6f}, mean mu4/mu2^2 {LOG11['mean_r4']}, {LOG11['wins']} wins of {LOG11['primes']}, best share "
       f"from 37 on {LOG11['best_from_37']}: " + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in v11.items()),
       all(v11.values()))
if FULL:
    # O1 and O2's statistics again, from the states themselves, at the primes from 211 to 401
    tot_, s_sum_, r_sum_ = 0, 0.0, 0.0
    for p_ in [q_ for q_ in osc.PRIMES if q_ >= 211]:
        for Psi_ in (osc.nonsplit_states(p_)[0], osc.split_states(p_)):
            N_, s_, r4_, _, _ = osc.stats(osc.wigner(Psi_, p_), p_)
            tot_, s_sum_, r_sum_ = tot_ + len(N_), s_sum_ + s_.sum(), r_sum_ + r4_.sum()
    forced(f"(--full) the primes from 211 to 401, recomputed: {tot_} states, mean S/sqrt p {s_sum_ / tot_:.6f}, mean "
           f"mu4/mu2^2 {r_sum_ / tot_:.4f}, as the log records",
           tot_ == 20056 and abs(s_sum_ / tot_ - LOG11["mean_s"]) < 1e-6 and abs(r_sum_ / tot_ - LOG11["mean_r4"]) < 1e-4)

# ------------------------------------------------------------------ round 12 (torus_moments.py; TORUS_MOMENTS.md's proof)
print()
print("round 12:")
import os
import verify_torus_moments as vtm
import torus_moments as tmo

ok_count, ok_phi = True, True
for p_ in [q_ for q_ in osc.PRIMES if q_ <= 61]:
    _, S12 = vtm.chirp(p_)
    orbs12 = vtm.orbits(S12, p_)
    m12 = p_ + 1
    ok_count &= len(orbs12) == p_ - 1 and all(len(o) == m12 for o in orbs12)
    phi12 = 0
    for orb in orbs12:
        P12 = np.array(orb)
        sums12 = ((P12[:, None, :] + P12[None, :, :]) % p_).reshape(-1, 2)
        cnt12 = np.bincount(sums12[:, 0] * p_ + sums12[:, 1], minlength=p_ * p_).astype(np.int64)
        ok_count &= int((cnt12 ** 2).sum()) == 3 * m12 * m12 - 3 * m12
        sy12 = (P12[:, None, 0] * P12[None, :, 1] - P12[:, None, 1] * P12[None, :, 0]) % p_
        phi12 += np.exp(2j * np.pi * 4 * sy12 / p_).sum()
    ok_phi &= abs(phi12 - (p_ - 1) * (p_ + 1)) < 1e-6
forced("TORUS_MOMENTS.md's counting steps at every prime from 5 to 61: the torus's orbits are p - 1 circles of p + 1 "
       "points, v1 + v3 = v2 + v4 has exactly 3m^2 - 3m solutions on each, and the circle sums Phi add up to "
       "(p - 1)(p + 1); with the trace steps this proves the average fourth-moment ratio 2p/(p + 1)", ok_count and ok_phi)
LOG12 = dict(m3=-0.0566, m6=5.0655, m8=14.3502, ns6=(5.0077, 5.0239), ns8=(14.0696, 14.2027), ks=0.0072)
v12 = {"M1": abs(LOG12["m3"]) <= 0.1, "M2": abs(LOG12["m6"] - 5) <= 0.3, "M3": abs(LOG12["m8"] - 14) <= 1.5,
       "M4": max(abs(x - 5) for x in LOG12["ns6"]) <= 0.3 and max(abs(x - 14) for x in LOG12["ns8"]) <= 1.5,
       "M5": LOG12["ks"] < 0.015}
forced("the logged values give round 12's recorded scores (torus_moments_combined.log): "
       + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in v12.items()), all(v12.values()))
if FULL:
    # M4's non-split basis averages again, from the states themselves, at the primes from 211 to 401
    logged12 = {}
    for line in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "torus_moments_run.log"), encoding="utf-8"):
        f12 = line.split()
        if line.startswith("MOM ") and f12[1].isdigit() and f12[2] == "nonsplit":
            logged12[int(f12[1])] = (float(f12[6]), float(f12[7]))
    ok12 = True
    for p_ in [q_ for q_ in osc.PRIMES if q_ >= 211]:
        V12 = osc.nonsplit_states(p_)[0]
        m6s, m8s = [], []
        for i in range(0, len(V12), 16):
            M12, _, _ = tmo.moments(osc.wigner(V12[i:i + 16], p_))
            m6s.append(M12[6]), m8s.append(M12[8])
        ok12 &= abs(np.concatenate(m6s).mean() - logged12[p_][0]) < 1e-6 and abs(np.concatenate(m8s).mean() - logged12[p_][1]) < 1e-5
    forced("(--full) the non-split basis averages of the sixth and eighth moments, recomputed at every prime from 211 to "
           "401, are the logged ones", ok12)

# ------------------------------------------------------------------ round 13 (cubic_magic.py; its logs are cubic_magic_*.log)
print()
print("round 13:")
import cubic_magic as cmg

rng13 = np.random.default_rng([20261114, 13])
worst13 = 0.0
for p_, n_ in ((5, 2), (7, 2), (3, 3), (5, 3)):
    mons13, Mv13 = cmg.monomial_values(p_, n_)
    X13 = cmg.points(p_, n_)
    for _ in range(4):
        c13 = rng13.integers(0, p_, len(mons13))
        lin13 = rng13.integers(0, p_, n_)
        q13 = rng13.integers(0, p_, (n_, n_))
        extra13 = (X13 @ lin13 + np.einsum("ai,ij,aj->a", X13, q13, X13)) % p_
        f13 = ((c13 @ Mv13) + extra13) % p_
        worst13 = max(worst13, abs(cmg.negativities(c13[None, :], Mv13, p_, n_)[0][0] - cmg.direct_negativity(f13, p_, n_)))
forced(f"every cubic-phase state's Wigner values are the Walsh spectrum of its cubic part: random cubic states with random "
       f"lower terms on two wheels of 5 and 7 and three of 3 and 5 agree with their own Wigner functions (largest "
       f"difference {worst13:.1e})", worst13 < 1e-10)
mons33, Mv33 = cmg.monomial_values(3, 3)
N33 = np.concatenate([cmg.negativities(c, Mv33, 3, 3)[0] for c in cmg.all_forms(3, len(mons33))])
xyz33 = np.zeros(len(mons33), dtype=np.int64)
xyz33[mons33.index((1, 1, 1))] = 1
mons52, Mv52 = cmg.monomial_values(5, 2)
N52 = np.concatenate([cmg.negativities(c, Mv52, 5, 2)[0] for c in cmg.all_forms(5, len(mons52))])
x3_5 = cmg.negativities(np.array([[1]]), cmg.monomial_values(5, 1)[1], 5, 1)[0][0]
forced(f"exhaustive: over all 2187 cubic forms on three wheels of 3 the best is {N33.max():.12f} = 17/9, the norm form's, and "
       f"xyz has {cmg.negativities(xyz33[None, :], Mv33, 3, 3)[0][0]:.12f} = 16/9; over all 625 on two wheels of 5 the best "
       f"is {N52.max():.12f} = (9 + 3 sqrt 5)/10, below round 9's 1.766937; the cube state w^(x^3) at 5 has {x3_5:.12f} = "
       f"1/sqrt 5; and no form reaches the ceiling", abs(N33.max() - 17 / 9) < 1e-12
       and abs(cmg.negativities(xyz33[None, :], Mv33, 3, 3)[0][0] - 16 / 9) < 1e-12
       and abs(N52.max() - (9 + 3 * np.sqrt(5)) / 10) < 1e-12 and abs(x3_5 - 1 / np.sqrt(5)) < 1e-12
       and N33.max() < (np.sqrt(27) - 1) / 2 and N52.max() < (np.sqrt(25) - 1) / 2)
LOG13 = {"K2": (1.570820393250, 1.766937254162, 2.567774657226, 2.719253432179), "K4": (4.252724292100, 4.252724292100),
         "K5": (7.902228372133, 7.902228372133)}
v13 = {"K2": LOG13["K2"][0] >= LOG13["K2"][1] - 1e-6 and LOG13["K2"][2] >= LOG13["K2"][3] - 1e-6,
       "K4": LOG13["K4"][0] > LOG13["K4"][1] + 1e-9, "K5": LOG13["K5"][0] <= LOG13["K5"][1] + 1e-9}
forced("the logged values give round 13's recorded scores: " + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in
       v13.items()) + " (K0, K1, K3 and K6 are checked above or exactly)",
       v13 == {"K2": False, "K4": False, "K5": True})
if FULL:
    # three wheels of 5, all 9 765 625 forms: the maximum is the norm form's
    mons53, Mv53 = cmg.monomial_values(5, 3)
    top53 = max(cmg.negativities(c, Mv53, 5, 3)[0].max() for c in cmg.all_forms(5, len(mons53)))
    forced(f"(--full) over all 9765625 cubic forms on three wheels of 5 the best is {top53:.12f}, the norm form's",
           abs(top53 - 4.252724292100) < 1e-9)

print()
print(f"SCORE: {sum(RESULTS.values())} of {len(RESULTS)} predictions held: "
      + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in RESULTS.items()))

# the outcome scored on 2026-11-07 (PREREG.md); a later run that disagrees exits with 1
RECORDED = {"Q1": True, "Q2": True, "Q3": True, "Q4": True, "Q5": True, "Q6": True, "Q7": False, "Q8": True}
same = RESULTS == RECORDED
print("matches the recorded score: " + ("yes" if same else "NO") + "; the page's other lines: "
      + ("all pass" if FORCED_OK else "A FAILURE"))
sys.exit(0 if same and FORCED_OK else 1)
