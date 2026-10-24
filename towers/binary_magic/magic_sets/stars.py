"""
stars.py — Round 8a of PREREG.md: magic sets built from binary codes (the pentagram's construction).
F = family of even-weight subsets S of n qubits; M_S = Y on S, X elsewhere.
Contexts: GHZ {M_S : S in F}; local {Y_i (i in S), X_j (j not in S), M_S} for each S.
"""
import itertools, sys
from collections import Counter
from ms_core import parse, label, check_magic, min_magic_rank, rank_rows, gram_of, verify_with_matrices

def star(n, F):
    ops, idx = [], {}
    def op(lbl):
        if lbl not in idx: idx[lbl] = len(ops); ops.append(lbl)
        return idx[lbl]
    ghz, local = [], []
    for S in F:
        m = op("".join("Y" if q in S else "X" for q in range(n)))
        ghz.append(m)
        local.append(tuple(op("".join(("Y" if q in S else "X") if r == q else "I" for r in range(n))) for q in range(n)) + (m,))
    return ops, [tuple(ghz)] + local

def analyse(n, F, limit_dim=24):
    labels, ctxs = star(n, F)
    ops = [parse(l) for l in labels]
    ok, neg, deg = check_magic(ops, ctxs)
    if not ok: return None
    r, d = min_magic_rank(len(ops), ctxs, limit_dim=limit_dim)
    return dict(F=F, observables=len(ops), contexts=len(ctxs), min_rank=r, gram_dim=d,
                own=rank_rows(gram_of(ops)), labels=labels, ctxs=ctxs)

res = {}
pent = analyse(3, [frozenset(), frozenset({0, 1}), frozenset({0, 2}), frozenset({1, 2})])
res["M1"] = pent is not None and pent["min_rank"] == 6 and pent["observables"] == 10
assert verify_with_matrices(pent["labels"], pent["ctxs"]).count(-1) == 1
print(f"M1  pentagram from its code: {pent['observables']} observables, min rank {pent['min_rank']} -> "
      f"{pent['min_rank'] // 2} qubits")

def families(n, max_size):
    ev = [frozenset(S) for k in range(0, n + 1, 2) for S in itertools.combinations(range(n), k)]
    for size in range(2, max_size + 1, 2):
        for F in itertools.combinations(ev, size):
            if all(sum(q in S for S in F) % 2 == 0 for q in range(n)): yield list(F)

best = {}
for n, max_size in ((3, 8), (4, 8), (5, 8), (6, 6)):
    tally = Counter(); seen = 0
    for F in families(n, max_size):
        a = analyse(n, F)
        seen += 1
        if a is None: tally["not magic"] += 1; continue
        q = a["min_rank"] // 2 if isinstance(a["min_rank"], int) else a["min_rank"]
        tally[("magic", q)] += 1
        if isinstance(q, int) and (n not in best or q > best[n][0] or (q == best[n][0] and a["observables"] < best[n][1]["observables"])):
            best[n] = (q, a)
    q, a = best.get(n, (None, None))
    print(f"n={n}: {seen} code families (|F| <= {max_size}); outcomes {dict(tally)};"
          f" most genuine qubits {q}" + (f" (smallest: {a['observables']} observables)" if a else ""))
res["M2"] = best.get(4, (0,))[0] < 4
res["M3"] = all(best.get(n, (0,))[0] <= 3 for n in (4, 5, 6))
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
