"""verify_seven_levels.py -- runs the eight predictions registered in PREREG.md (commit b42b65b) on a
seven-level quantum system, and reports each as HELD or DIED with its evidence.  Then it checks the README's
other lines, among them round 2's most negative state as recorded in most_negative.log.

numpy + scipy.  ASCII output.  Run:  python verify_seven_levels.py      (about half a minute)
"""
import ctypes
import itertools
import math
import sys
from collections import Counter

import numpy as np
from scipy.optimize import minimize

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
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

print()
print(f"SCORE: {sum(RESULTS.values())} of {len(RESULTS)} predictions held: "
      + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in RESULTS.items()))

# the outcome scored on 2026-11-07 (PREREG.md); a later run that disagrees exits with 1
RECORDED = {"Q1": True, "Q2": True, "Q3": True, "Q4": True, "Q5": True, "Q6": True, "Q7": False, "Q8": True}
same = RESULTS == RECORDED
print("matches the recorded score: " + ("yes" if same else "NO") + "; the page's other lines: "
      + ("all pass" if FORCED_OK else "A FAILURE"))
sys.exit(0 if same and FORCED_OK else 1)
