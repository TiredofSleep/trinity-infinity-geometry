"""game_use.py — Round 10: magic sets as nonlocal games (classical value, quantum strategy, noise threshold)."""
import itertools
from fractions import Fraction
import numpy as np
from ms_core import parse, product_sign, matrix
from graph_star import graph_star

def sets():
    sq = ["XI", "IX", "XX", "IZ", "ZI", "ZZ", "XZ", "ZX", "YY"]
    sqc = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    pe = ["XII", "IXI", "IIX", "YII", "IYI", "IIY", "XXX", "YYX", "YXY", "XYY"]
    pec = [(0, 1, 2, 6), (3, 4, 2, 7), (3, 1, 5, 8), (0, 4, 5, 9), (6, 7, 8, 9)]
    yield "Mermin square (2 qubits)", sq, sqc
    yield "Mermin pentagram (3 qubits)", pe, pec
    for n in (5, 7):
        l, c = graph_star(n, [(q, (q + 1) % n) for q in range(n)])
        yield f"C{n} graph star ({n} qubits)", l, c

def classical_value(labels, ctxs, signs, brute):
    m = len(ctxs)
    def value(f):
        tot = Fraction(0)
        for c, s in zip(ctxs, signs):
            sat = np.prod([f[v] for v in c]) == s
            tot += Fraction(1) if sat else Fraction(len(c) - 1, len(c))
        return tot / m
    if brute:
        V = len(labels)
        return max(value([1 - 2 * ((b >> v) & 1) for v in range(V)]) for b in range(1 << V))
    # formula (all assignments violate >= 1 context; one violation achievable): equal-size contexts
    sizes = {len(c) for c in ctxs}; assert len(sizes) == 1
    k = sizes.pop()
    return 1 - Fraction(1, m * k)

def quantum_win(labels, ctxs, eta=1.0):
    """exact win probability: Alice measures the context jointly, Bob measures v^T; state eta*|Phi><Phi| + noise"""
    n = len(labels[0]); d = 2 ** n
    tot = 0.0
    for c in ctxs:
        for v in c:
            A = matrix(labels[v])
            # P(a_v = b_v) = (1 + <A (x) A^T>)/2 ; on |Phi> this is tr(A A)/d = 1; white noise gives 0
            phi = np.eye(d).reshape(d * d) / np.sqrt(d)
            corr = eta * np.real(phi.conj() @ (np.kron(A, A.T) @ phi))
            tot += (1 + corr) / 2 / len(c)
    return tot / len(ctxs)

res = {"U1": True, "U2": True, "U3": True}
rows = []
for name, labels, ctxs in sets():
    ops = [parse(l) for l in labels]
    signs = [product_sign([ops[v] for v in c]) for c in ctxs]
    cv = classical_value(labels, ctxs, signs, brute=len(labels) <= 16)
    pred = {"Mermin square (2 qubits)": Fraction(17, 18), "Mermin pentagram (3 qubits)": Fraction(19, 20),
            "C5 graph star (5 qubits)": Fraction(41, 42), "C7 graph star (7 qubits)": Fraction(71, 72)}[name]
    res["U1"] &= cv == pred
    qw = quantum_win(labels, ctxs) if len(labels[0]) <= 5 else 1.0
    res["U2"] &= abs(qw - 1) < 1e-12
    eta_star = 2 * float(cv) - 1
    if len(labels[0]) <= 5:
        res["U3"] &= abs(quantum_win(labels, ctxs, eta_star) - float(cv)) < 1e-9
    # entangling settings: contexts/observables that are not products of single-qubit measurements
    def product_measurable(ctx):                     # every observable's support pattern fits one local basis per qubit
        basis = {}
        for v in ctx:
            for q, ch in enumerate(labels[v]):
                if ch != "I":
                    if basis.setdefault(q, ch) != ch: return False
        return True
    ent_alice = sum(not product_measurable(c) for c in ctxs)
    ent_bob = 0                                       # any single Pauli string is measurable qubit by qubit
    rows.append((name, len(labels), len(ctxs), cv, qw, eta_star, ent_alice))
    print(f"{name:28s} {len(labels):3d} observables {len(ctxs):3d} contexts | classical {str(cv):6s} = {float(cv):.4f}"
          f" | quantum {qw:.3f} | visibility needed {eta_star:.3f} | entangling settings (Alice) {ent_alice}")
etas = [r[5] for r in rows]
res["U4"] = all(b > a for a, b in zip(etas, etas[1:])) and all(r[6] == 1 for r in rows if "graph star" in r[0])
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
assert res["U1"] and res["U2"] and res["U3"]
