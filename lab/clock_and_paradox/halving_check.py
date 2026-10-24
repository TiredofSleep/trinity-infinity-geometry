"""
halving_check.py — is the paradox residue the failure to divide by 2?

Odd p: 2 has an inverse mod p, so the phase of X^a Z^b can be split evenly ("halved"):
D(u) = w^{(a b)/2} X^a Z^b. Then any commuting triple with u + v + w = 0 multiplies to exactly 1.
p = 2: there is no 1/2 mod 2, and no sign choice makes every commuting triple multiply to +1.
"""
import itertools
import numpy as np
from functools import reduce

def ops(p, symmetric):
    w = np.exp(2j * np.pi / p)
    X = np.roll(np.eye(p), 1, axis=0); Z = np.diag([w ** k for k in range(p)])
    half = pow(2, -1, p) if p % 2 else None
    def one(a, b):
        M = np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b)
        if symmetric and half is not None:
            M = w ** ((half * a * b) % p) * M
        if p == 2 and a and b:
            M = 1j * M                                   # Hermitian Y; the best qubits can do
        return M
    V = [u for u in itertools.product(range(p), repeat=4) if any(u)]
    return V, {u: np.kron(one(u[0], u[1]), one(u[2], u[3])) for u in V}

def triples(p, V, D):
    out = []
    for u in V:
        for v in V:
            w_ = tuple((-x - y) % p for x, y in zip(u, v))
            if any(w_) and len({u, v, w_}) == 3 and np.allclose(D[u] @ D[v], D[v] @ D[u]):
                out.append((u, v, w_))
    return out

for p in (3, 5):
    V, D = ops(p, symmetric=True)
    T = triples(p, V, D)
    phases = {round(np.angle(reduce(np.matmul, (D[x] for x in t))[0, 0]) / (2 * np.pi) * p) % p for t in T}
    print(f"p = {p}: {len(T)} commuting triples; with halved phases every product is w^k for k in {phases}")
    V, D = ops(p, symmetric=False)
    T = triples(p, V, D)
    phases = {round(np.angle(reduce(np.matmul, (D[x] for x in t))[0, 0]) / (2 * np.pi) * p) % p for t in T}
    print(f"        without halving the same triples leave residues k in {sorted(phases)}")

V, D = ops(2, symmetric=True)
T = {frozenset(t) for t in triples(2, V, D)}
sign = {t: int(round(reduce(np.matmul, (D[x] for x in sorted(t)))[0, 0].real)) for t in T}
print(f"\np = 2: {len(T)} commuting triples; product signs: {sorted(set(sign.values()))}")
ok = 0
for s in itertools.product((1, -1), repeat=len(V)):
    val = dict(zip(V, s))
    if all(val[a] * val[b] * val[c] == sign[t] for t in T for a, b, c in [tuple(t)]):
        ok += 1
print(f"       sign assignments to the 15 operators that satisfy every triple: {ok} of {2 ** len(V)}")
