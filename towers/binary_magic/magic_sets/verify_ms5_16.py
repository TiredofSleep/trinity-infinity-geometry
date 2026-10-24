"""
verify_ms5_16.py — independent verification of the 16-observable 5-qubit magic set from stars.py.
Does not use gram_space(), min_magic_rank() or the Theorem 7 functional.

The set: F = {∅, 01, 02, 13, 24, 34} (all-X plus the edges of a 5-cycle). Observables: the 10 single-qubit
operators X_q, Y_q and the six M_S (Y on S, X elsewhere). Contexts: GHZ {M_S} and, for each S, its local
context {singles of M_S, M_S}.

Lower bound on qubits, from first principles: in any Pauli assignment each M_S is the product of the singles
in its local context, so the whole assignment is fixed by the 10 singles, and its Gram matrix G (10x10,
alternating over F2) has rank = 2 x (qubits used). Enumerate every G allowed by the commutation constraints,
build an explicit Pauli realisation of each with that Gram matrix, multiply out every context, and count
negative contexts. Genuine 5-qubit <=> no G of rank <= 8 gives an odd count.
"""
import itertools, json, os
import numpy as np
from ms_core import parse, label, product_sign, verify_with_matrices, symp

n = 5
F = [frozenset(), frozenset({0, 1}), frozenset({0, 2}), frozenset({1, 3}), frozenset({2, 4}), frozenset({3, 4})]
singles = [("X", q) for q in range(n)] + [("Y", q) for q in range(n)]
sid = {s: k for k, s in enumerate(singles)}
local = [[sid[("Y" if q in S else "X", q)] for q in range(n)] for S in F]       # singles of each local context

# 1. the actual operators: matrices, signs, minimality
lab = lambda s: "".join(s[0] if r == s[1] else "I" for r in range(n))
MS = ["".join("Y" if q in S else "X" for q in range(n)) for S in F]
labels = [lab(s) for s in singles] + MS
ctxs = [tuple(range(10, 16))] + [tuple(local[k]) + (10 + k,) for k in range(6)]
signs = verify_with_matrices(labels, ctxs)                                      # explicit 32x32 matrices
deg = [sum(v in c for c in ctxs) for v in range(16)]
print("explicit matrices: all contexts commute and multiply to +-I; signs", signs)
print("degrees all even:", all(d % 2 == 0 for d in deg), "| negative contexts:", signs.count(-1))
assert all(d % 2 == 0 for d in deg) and signs.count(-1) % 2 == 1
minimal = all(not (all(sum(v in ctxs[c] for c in T) % 2 == 0 for v in range(16))
                   and sum(signs[c] == -1 for c in T) % 2 == 1)
              for k in range(1, 7) for T in itertools.combinations(range(7), k))
print("no proper subset of contexts is a parity clash (brute force over all 126):", minimal)
assert minimal
assert len(set(labels)) == 16

# 2. every Gram matrix of the singles allowed by commutation
co = set()
for L in local:
    for a, b in itertools.combinations(sorted(L), 2): co.add((a, b))
free = [(a, b) for a in range(10) for b in range(a + 1, 10) if (a, b) not in co]
print(f"\nsingle pairs never in a common context (free Gram entries): {len(free)}")
def G_of(bits):
    G = np.zeros((10, 10), dtype=np.uint8)
    for k, (a, b) in enumerate(free):
        if bits >> k & 1: G[a, b] = G[b, a] = 1
    return G
def ghz_ok(G):                                     # every pair M_S, M_T must commute
    for s, t in itertools.combinations(range(6), 2):
        if int(sum(G[a, b] for a in local[s] for b in local[t])) % 2: return False
    return True
def f2rank(G):
    A = G.copy() % 2; r = 0
    rows, cols = A.shape
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i, c]), None)
        if p is None: continue
        A[[r, p]] = A[[p, r]]
        for i in range(rows):
            if i != r and A[i, c]: A[i] ^= A[r]
        r += 1
    return r
def realise(G):
    """explicit Pauli vectors (x, z) on k = rank/2 qubits whose symplectic Gram matrix is G"""
    B = lambda u, w: int(u @ G @ w) % 2
    basis = [np.eye(10, dtype=np.int64)[i] for i in range(10)]
    pairs = []
    pool = basis[:]
    while True:
        found = None
        for u in pool:
            for w in pool:
                if B(u, w): found = (u, w); break
            if found: break
        if not found: break
        e, f = found
        pairs.append((e, f))
        newpool = []
        for u in pool:                              # make u orthogonal to e and f
            u2 = (u + B(u, f) * e + B(u, e) * f) % 2
            if u2.any(): newpool.append(u2)
        pool = newpool
    k = len(pairs)
    ops = []
    for i in range(10):
        u = basis[i]
        x = sum(B(u, f) << a for a, (e, f) in enumerate(pairs))
        z = sum(B(e, u) << a for a, (e, f) in enumerate(pairs))
        ops.append((x, z))
    for i in range(10):
        for j in range(10):
            assert symp(ops[i], ops[j]) == G[i, j]
    return k, ops
def negatives(ops):
    allops = ops + [tuple(np.bitwise_xor.reduce([np.array(ops[a]) for a in L])) for L in local]
    allops = [(int(x), int(z)) for x, z in allops]
    return sum(product_sign([allops[v] for v in c]) == -1 for c in ctxs), allops

tally = {}
for bits in range(1 << len(free)):
    G = G_of(bits)
    if not ghz_ok(G): continue
    r = f2rank(G)
    k, ops = realise(G)
    assert 2 * k == r
    neg, allops = negatives(ops)
    tally.setdefault(r, [0, 0])[neg % 2] += 1
    if r <= 8 and neg % 2 == 1:
        raise SystemExit(f"realisable on {k} qubits: not genuine 5-qubit")
    if r <= 6 and k <= 3:                          # spot-check the sign count with explicit matrices
        lbls = [label(o, k) for o in allops]
        assert verify_with_matrices(lbls, ctxs).count(-1) == neg
print("allowed Gram matrices by rank -> [even negatives, odd negatives]:", dict(sorted(tally.items())))
assert all(v[1] == 0 for r, v in tally.items() if r <= 8)
print("\nVERIFIED: every assignment on 4 or fewer qubits has an even number of negative contexts,")
print("so this 16-observable magic set needs 5 qubits (genuine 5-qubit).")
json.dump(dict(F=[sorted(S) for S in F], labels=labels, contexts=[[labels[v] for v in c] for c in ctxs], signs=signs),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ms5_16.json"), "w"), indent=1)
