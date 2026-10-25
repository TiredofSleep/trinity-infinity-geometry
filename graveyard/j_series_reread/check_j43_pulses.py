"""J43 follow-ups: (a) are the printed theta's right and only the phases wrong?
(b) can G_12 be built from Delta m = 1 pulses alone? (c) restriction of [3,1] and [2,1,1] to S3."""
import itertools
import numpy as np
from scipy.optimize import least_squares

rt = np.sqrt
B = np.array([[1, -1, 0, 0], [1, 1, -2, 0], [1, 1, 1, -3]], float)
B /= np.linalg.norm(B, axis=1, keepdims=True)
def pm(p):
    M = np.zeros((4, 4)); [M.__setitem__((p[i], i), 1.0) for i in range(4)]; return M
rep = lambda p: B @ pm(p) @ B.T
V = np.array([[0, 0, 1], [1/rt(2), 1j/rt(2), 0], [-1/rt(2), 1j/rt(2), 0]])
U4 = rep((1, 2, 3, 0))
target = np.exp(1j*np.pi/3) * (V @ U4 @ V.conj().T)

def G(i, j, th, ph):
    M = np.eye(3, dtype=complex)
    M[i, i] = M[j, j] = np.cos(th); M[i, j] = 1j*np.sin(th)*np.exp(1j*ph); M[j, i] = 1j*np.sin(th)*np.exp(-1j*ph)
    return M

# (a) keep the printed thetas, free the three phases + a diagonal phase layer + global phase
th = [1.1071, 0.7297, 0.4636]
pairs = [(0, 2), (0, 1), (1, 2)]
def model(x, order):
    M = np.eye(3, dtype=complex)
    for idx in order:
        M = M @ G(*pairs[idx], th[idx], x[idx])
    M = M @ np.diag(np.exp(1j*np.array([x[3], x[4], x[5]])))
    return M
def resid(x, order):
    d = (model(x, order) - target).ravel()
    return np.concatenate([d.real, d.imag])
best = (9, None)
rng = np.random.default_rng(0)
for order in itertools.permutations(range(3)):
    for _ in range(60):
        r = least_squares(resid, rng.uniform(-np.pi, np.pi, 6), args=(order,))
        val = np.linalg.norm(resid(r.x, order))
        if val < best[0]:
            best = (val, order, r.x)
print("(a) printed thetas, phases free (+diagonal layer): best residual %.2e for order %s" % (best[0], [ ['G02','G01','G12'][i] for i in best[1]]))
print("    fitted phases:", np.round(best[2][:3], 4), " printed phases: [-4.1888, 0.0, -1.5708]")
# full free fit (thetas free too) to show a valid 3-Givens + diagonal compilation exists
def resid2(x):
    M = G(0, 2, x[0], x[1]) @ G(0, 1, x[2], x[3]) @ G(1, 2, x[4], x[5]) @ np.diag(np.exp(1j*x[6:9]))
    d = (M - target).ravel(); return np.concatenate([d.real, d.imag])
b2 = min((least_squares(resid2, rng.uniform(-np.pi, np.pi, 9)) for _ in range(200)), key=lambda r: np.linalg.norm(r.fun))
print("    a valid G02*G01*G12*Diag compilation exists: residual %.1e, thetas %s, phases %s, diag %s" %
      (np.linalg.norm(b2.fun), np.round(b2.x[[0, 2, 4]] % np.pi, 4), np.round(b2.x[[1, 3, 5]], 4), np.round(b2.x[6:], 4)))

# (b) G_12 from Delta m = 1 pulses: P = pi-pulse on (0,1); P G_02 P^dagger acts on (1,2)
P = G(0, 1, np.pi/2, 0.0)
for theta, phi in [(0.4636, -1.5708), (1.0, 0.3)]:
    built = P @ G(0, 2, theta, phi) @ P.conj().T
    best = min(np.linalg.norm(built - G(1, 2, theta, ph2)) for ph2 in np.linspace(-np.pi, np.pi, 72001))
    print("(b) P G02(%.4f,%.4f) P^dag equals some G12(theta, phi'): residual %.1e; acts only on (|+1>,|-1>): %s"
          % (theta, phi, best, np.allclose(built[0], [1, 0, 0])))

# (c) restriction to S3 = Stab(4): characters on e, (12), (123)
for name, tw in [("[3,1]  (the matrices J43 uses)", lambda p, M: M), ("[2,1,1] (the label J43 prints)", lambda p, M: np.linalg.det(M)*M)]:
    chis = [round(np.trace(tw(p, rep(p))).real, 6) for p in [(0, 1, 2, 3), (1, 0, 2, 3), (1, 2, 0, 3)]]
    # S3 irreps: A1=(1,1,1), A2=(1,-1,1), E=(2,0,-1); multiplicities by inner product
    sizes = [1, 3, 2]
    mult = {n: sum(s*c*x for s, c, x in zip(sizes, chis, ch))/6 for n, ch in [("A1", (1, 1, 1)), ("A2", (1, -1, 1)), ("E", (2, 0, -1))]}
    print("(c) %s restricted to S3: character %s -> %s" % (name, chis, {k: int(round(v)) for k, v in mult.items() if round(v)}))
