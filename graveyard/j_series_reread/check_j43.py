"""Independent probe of J43's claims (fresh code; does not import the paper's script).

Checks:
 A. the 3-dim rep of S4 on the sum-zero subspace of R^4: character, label ([3,1] vs [2,1,1])
 B. the paper's printed U_4 matrix = image of the 4-cycle (1234) in the b-basis?
 C. the paper's V: does it send r(12) to the NV mirror and r(123) to diag(1,w,w^2)?
 D. is the S3 -> NV intertwiner unique "up to phase within each irrep" and is the S4 extension unique?
 E. does the PRINTED pulse table (G02, G01, G12 angles + Z phases) multiply to U_{4,SU3}?
 F. the paper's "24-element closure" check: what does it actually test?
"""
import itertools
import numpy as np

np.set_printoptions(precision=4, suppress=True)
rt = np.sqrt


def perm_mat(p):
    """matrix of the permutation i -> p[i] acting on R^4: e_i -> e_{p[i]}"""
    M = np.zeros((4, 4))
    for i in range(4):
        M[p[i], i] = 1.0
    return M


B = np.array([[1, -1, 0, 0], [1, 1, -2, 0], [1, 1, 1, -3]], dtype=float)
B = B / np.linalg.norm(B, axis=1, keepdims=True)


def rep(p):
    return B @ perm_mat(p) @ B.T


def sign(p):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    return s


def cycle_type(p):
    seen, lens = set(), []
    for i in range(4):
        if i in seen:
            continue
        L, j = 0, i
        while j not in seen:
            seen.add(j)
            j = p[j]
            L += 1
        lens.append(L)
    return tuple(sorted(lens, reverse=True))


perms = list(itertools.permutations(range(4)))
classes = {}
for p in perms:
    classes.setdefault(cycle_type(p), []).append(p)
order = [(1, 1, 1, 1), (2, 1, 1), (3, 1), (2, 2), (4,)]
names = ["e", "(ij)", "(ijk)", "(ij)(kl)", "(ijkl)"]
print("A. character of the sum-zero (tetrahedron) representation of S4")
chi = {}
for ct, nm in zip(order, names):
    vals = {round(np.trace(rep(p)), 9) for p in classes[ct]}
    dets = {round(np.linalg.det(rep(p)), 9) for p in classes[ct]}
    chi[nm] = vals
    print(f"   {nm:10s} size {len(classes[ct]):2d}  trace {vals}  det {dets}")
# Young-diagram characters for comparison (standard tables, Fulton-Harris 2.3):
#   [3,1]   : (3, 1, 0, -1, -1)   the standard rep V
#   [2,1,1] : (3,-1, 0, -1,  1)   V (x) sgn
print("   => (3,1,0,-1,-1) is the partition [3,1] (standard rep V), NOT [2,1,1] (= V (x) sgn)")

print("\nB. the paper's printed U_4 vs the image of (1234)")
U4_paper = np.array([[-0.5, -1 / (2 * rt(3)), -rt(2 / 3)],
                     [rt(3) / 2, -1 / 6, -rt(2) / 3],
                     [0.0, 2 * rt(2) / 3, -1 / 3]])
c4 = (1, 2, 3, 0)  # 0->1->2->3->0, i.e. the 4-cycle (1234) on labels 1..4
print("   max|U4_paper - rep((1234))| =", np.abs(U4_paper - rep(c4)).max())
print("   eig:", np.round(np.linalg.eigvals(U4_paper), 12), " det:", round(np.linalg.det(U4_paper), 12))

print("\nC. the paper's change of basis V")
V = np.array([[0, 0, 1], [1 / rt(2), 1j / rt(2), 0], [-1 / rt(2), 1j / rt(2), 0]])
r12 = rep((1, 0, 2, 3))
r123 = rep((1, 2, 0, 3))
w = np.exp(2j * np.pi / 3)
sig_v = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
print("   unitary:", np.allclose(V @ V.conj().T, np.eye(3)))
print("   max|V r12 V^-1 - sigma_v| =", np.abs(V @ r12 @ V.conj().T - sig_v).max())
C3 = V @ r123 @ V.conj().T
print("   V r123 V^-1 =\n", np.round(C3, 6))
print("   diagonal?", np.allclose(C3, np.diag(np.diag(C3))), " diag =", np.round(np.diag(C3), 6))
# what the script checked instead: eigenvalues of a conjugate -- true for ANY unitary
W = np.linalg.qr(np.random.default_rng(1).normal(size=(3, 3)) + 1j * np.random.default_rng(2).normal(size=(3, 3)))[0]
print("   (the paper's script only compares eigenvalues of V r123 V^-1 with {1,w,w^2};"
      " a random unitary W passes that too:",
      np.allclose(sorted(np.angle(np.linalg.eigvals(W @ r123 @ W.conj().T))), sorted(np.angle([1, w, w.conjugate()]))), ")")

print("\nD. uniqueness of the S3 intertwiner / S4 extension")
for alpha in [0.0, 0.7, 2.0]:
    D = np.diag([np.exp(1j * alpha), 1, 1])  # phase on the A1 line (|0>) relative to the E block
    V2 = D @ V
    ok_s3 = np.allclose(V2 @ r12 @ V2.conj().T, sig_v) and np.allclose(V2 @ r123 @ V2.conj().T, C3)
    U4nv = V @ U4_paper @ V.conj().T
    U4nv2 = V2 @ U4_paper @ V2.conj().T
    print(f"   alpha={alpha}: same S3 images {ok_s3}; U4_NV changes by {np.abs(U4nv2 - U4nv).max():.3f}")
print("   => the S3 data fix V only up to a relative phase between |0> and the E block;"
      " the 4-cycle's NV matrix is NOT unique (a one-parameter family).")

print("\nE. does the PRINTED pulse table compile U_{4,SU3}?")


def G(i, j, th, ph):
    M = np.eye(3, dtype=complex)
    M[i, i] = M[j, j] = np.cos(th)
    M[i, j] = 1j * np.sin(th) * np.exp(1j * ph)
    M[j, i] = 1j * np.sin(th) * np.exp(-1j * ph)
    return M


U4nv = V @ U4_paper @ V.conj().T
target = np.exp(1j * np.pi / 3) * U4nv
print("   det(target) =", np.round(np.linalg.det(target), 12))
table = [(0, 2, 1.1071, -4.1888), (0, 1, 0.7297, 0.0), (1, 2, 0.4636, -1.5708)]
best = None
for ordering in itertools.permutations(range(3)):
    for daggers in itertools.product([False, True], repeat=3):
        M = np.eye(3, dtype=complex)
        for idx, dag in zip(ordering, daggers):
            g = G(*table[idx])
            M = M @ (g.conj().T if dag else g)
        # distance up to a global phase
        ph = np.vdot(M.flatten(), target.flatten())
        ph = ph / abs(ph) if abs(ph) > 1e-12 else 1
        dist = np.linalg.norm(M * ph - target)
        if best is None or dist < best[0]:
            best = (dist, ordering, daggers)
print("   best residual over all 6 orders x 8 dagger choices (global phase free): %.3f" % best[0])
print("   (a correct compilation would give ~1e-4 at the printed 4-digit precision)")
# the paper's own derivation: G-pulses alone, without the R_k diagonal phases
M_plain = G(*table[0]) @ G(*table[1]) @ G(*table[2])
print("   plain product G02 G01 G12 vs target, Frobenius residual: %.3f" % np.linalg.norm(M_plain - target))

print("\nF. what the '24-element closure residual 1.84e-16' measures")
S4 = [rep(p) for p in perms]
res = max(np.linalg.norm(V.conj().T @ (V @ M @ V.conj().T) @ V - M) for M in S4)
print("   max |V^-1 (V M V^-1) V - M| = %.2e  (a round trip, true for ANY invertible V)" % res)
W = np.linalg.qr(np.random.default_rng(5).normal(size=(3, 3)))[0]
res2 = max(np.linalg.norm(np.linalg.inv(W) @ (W @ M @ np.linalg.inv(W)) @ W - M) for M in S4)
print("   same test with a random orthogonal W instead of V: %.2e" % res2)
