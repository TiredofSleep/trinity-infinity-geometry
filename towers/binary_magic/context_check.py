"""
context_check.py — can a magic square be a Mermin-Peres-type contextuality grid?

A line of operators is a valid measurement context only if they all commute.
Qubit reading: 4 bits -> a two-qubit Pauli; commute iff the symplectic product is 0.
Qutrit reading: 2 trits (a, b) -> clock^a shift^b on one qutrit; commute iff a*d - b*c = 0 mod 3.
"""
import json, itertools
from collections import Counter

def sym2(u, v, lab):          # lab: which bit is x1, z1, x2, z2
    b = lambda w, k: (w >> lab[k]) & 1
    return (b(u, 0) * b(v, 1) + b(u, 1) * b(v, 0) + b(u, 2) * b(v, 3) + b(u, 3) * b(v, 2)) % 2

# largest set of mutually commuting non-identity two-qubit Paulis
lab0 = (0, 1, 2, 3)
best = max(len(S) for r in range(1, 6) for S in itertools.combinations(range(1, 16), r)
           if all(sym2(a, b, lab0) == 0 for a, b in itertools.combinations(S, 2)))
print(f"two qubits: largest commuting set of non-identity Paulis = {best}")

squares = [s["square"] for s in json.load(open("squares_4x4.json"))]
LINES = [[(i, j) for j in range(4)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(4)]
most = Counter()
for M in squares:
    top = 0
    for lab in itertools.permutations(range(4)):
        ok = sum(all(sym2(M[a][b], M[c][d], lab) == 0 for (a, b), (c, d) in itertools.combinations(L, 2))
                 for L in LINES)
        top = max(top, ok)
    most[top] += 1
print(f"880 squares, best bit->Pauli labeling: number of rows+columns that are valid contexts: {dict(most)}")

# one qutrit: Lo Shu
best3 = max(len(S) for r in range(1, 5) for S in itertools.combinations(range(1, 9), r)
            if all(((a // 3) * (b % 3) - (a % 3) * (b // 3)) % 3 == 0 for a, b in itertools.combinations(S, 2)))
lo = [[3, 8, 1], [2, 4, 6], [7, 0, 5]]
L3 = [[(i, j) for j in range(3)] for i in range(3)] + [[(i, j) for i in range(3)] for j in range(3)]
ok3 = sum(all(((lo[a][b] // 3) * (lo[c][d] % 3) - (lo[a][b] % 3) * (lo[c][d] // 3)) % 3 == 0
              for (a, b), (c, d) in itertools.combinations(L, 2)) for L in L3)
print(f"one qutrit: largest commuting set of non-identity clock-shift operators = {best3}; "
      f"Lo Shu rows+columns that are valid contexts: {ok3} of 6")
