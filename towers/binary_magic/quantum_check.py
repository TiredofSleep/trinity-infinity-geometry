"""
quantum_check.py — the two contextuality objects, built and checked.

A. Two qubits: every 3x3 grid of two-qubit Pauli operators whose rows and columns are commuting
   triples (Mermin-Peres squares). For each: line signs, sign parity, classical vs quantum win rate
   of the magic-square game.
B. One qutrit: the KCBS pentagram. Five measurements in a 5-cycle (neighbors orthogonal).
   Classical bound 2, quantum value sqrt(5).
"""
import itertools
import numpy as np
from functools import reduce

# ---------- A. two qubits ----------
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Z = np.diag([1, -1])
def pauli(v):                     # v = (x1 z1 x2 z2) as 4 bits; Hermitian convention (Y = iXZ)
    x1, z1, x2, z2 = (v >> 3) & 1, (v >> 2) & 1, (v >> 1) & 1, v & 1
    P1 = (1j ** (x1 * z1)) * np.linalg.matrix_power(X, x1) @ np.linalg.matrix_power(Z, z1)
    P2 = (1j ** (x2 * z2)) * np.linalg.matrix_power(X, x2) @ np.linalg.matrix_power(Z, z2)
    return np.kron(P1, P2)
P = {v: pauli(v) for v in range(16)}
def commute(a, b):
    return np.allclose(P[a] @ P[b], P[b] @ P[a])
lines = [t for t in itertools.combinations(range(1, 16), 3)
         if t[0] ^ t[1] ^ t[2] == 0 and all(commute(a, b) for a, b in itertools.combinations(t, 2))]
print(f"A. commuting triples of two-qubit Paulis whose product is +-I: {len(lines)}")
def sign(line):
    M = reduce(lambda a, b: a @ b, (P[v] for v in line))
    s = M[0, 0].real
    assert np.allclose(M, s * np.eye(4)) and abs(abs(s) - 1) < 1e-9
    return int(round(s))
grids = set()
for rows in itertools.combinations(lines, 3):
    pts = set().union(*map(set, rows))
    if len(pts) != 9:
        continue
    cols = [L for L in lines if all(len(set(L) & set(R)) == 1 for R in rows)]
    for cs in itertools.combinations(cols, 3):
        if len(set().union(*map(set, cs))) == 9:
            grids.add(frozenset([frozenset(map(frozenset, rows)), frozenset(map(frozenset, cs))]))
print(f"   distinct 3x3 grids (rows/columns unordered, transposes identified): {len(grids)}")

def game_values(rows, cols):
    rs = [sign(r) for r in rows]; cs = [sign(c) for c in cols]
    cell = {(i, j): (set(rows[i]) & set(cols[j])).pop() for i in range(3) for j in range(3)}
    # classical: Alice picks +-1 for her row's cells with product = row sign, Bob likewise per column
    def assigns(line_cells, s):
        return [a for a in itertools.product((1, -1), repeat=3) if a[0] * a[1] * a[2] == s]
    best = 0
    A_opts = [assigns(None, s) for s in rs]; B_opts = [assigns(None, s) for s in cs]
    for A in itertools.product(*A_opts):
        for B in itertools.product(*B_opts):
            wins = sum(A[i][j] == B[j][i] for i in range(3) for j in range(3))
            best = max(best, wins)
    # quantum: two Bell pairs; Alice measures P on her qubits, Bob measures P^T on his
    bell = np.zeros(4); bell[0] = bell[3] = 1 / np.sqrt(2)
    phi = np.kron(bell, bell)                          # qubits A1 B1 A2 B2
    perm = [0, 2, 1, 3]                                # reorder to A1 A2 B1 B2
    phi = phi.reshape(2, 2, 2, 2).transpose(perm).reshape(16)
    q = min(np.real(phi.conj() @ np.kron(P[v], P[v].T) @ phi) for v in cell.values())
    return rs, cs, np.prod(rs) * np.prod(cs), best, q
parities = set()
for g in grids:
    rows, cols = [list(map(sorted, part)) for part in g]
    rows = [tuple(r) for r in rows]; cols = [tuple(c) for c in cols]
    rs, cs, parity, best, q = game_values(rows, cols)
    parities.add((parity, best, round(q, 9)))
print(f"   every grid: (sign parity, classical best wins out of 9, quantum agreement) = {parities}")

# ---------- B. one qutrit: KCBS pentagram ----------
c = np.cos(np.pi / 5)
cos_t = np.sqrt(c / (1 + c)); sin_t = np.sqrt(1 - cos_t ** 2)
V = [np.array([cos_t, sin_t * np.cos(4 * np.pi * k / 5), sin_t * np.sin(4 * np.pi * k / 5)]) for k in range(5)]
assert all(abs(V[k] @ V[(k + 1) % 5]) < 1e-12 for k in range(5))
S = sum(np.outer(v, v) for v in V)
qmax = np.linalg.eigvalsh(S).max()
classical = max(sum(a) for a in itertools.product((0, 1), repeat=5)
                if all(not (a[k] and a[(k + 1) % 5]) for k in range(5)))
print(f"\nB. KCBS pentagram: neighbors orthogonal: True; classical max = {classical}; "
      f"quantum max = {qmax:.6f} (sqrt 5 = {np.sqrt(5):.6f}); golden ratio check: 2*phi - 1 = {2*(1+np.sqrt(5))/2 - 1:.6f}")
assert classical == 2 and abs(qmax - np.sqrt(5)) < 1e-9
