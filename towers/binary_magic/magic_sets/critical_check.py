"""
critical_check.py — the referee's correction, reproduced.

Stronger notion ("critical"): allow ANY subset of the observables that pairwise commutes and multiplies to
+-I as a context. A set is critical if no parity clash survives the deletion of any single observable.

For a graph star, a candidate context = a subset T of the M_S plus single-qubit observables. Their XOR must be
zero, so the singles are forced by sum(T); enumerate all 2^|F| subsets T.
Prediction (referee): odd cycles are critical; any non-cycle graph is not (its cycle space has dimension >= 2,
so it contains a proper even subgraph with an odd number of edges, giving a smaller star inside).
"""
import itertools
from ms_core import parse, symp, product_sign
from graph_star import graph_star

def all_contexts(labels):
    ops = [parse(l) for l in labels]; n = len(labels[0])
    idx = {o: i for i, o in enumerate(ops)}
    M = [i for i, l in enumerate(labels) if "I" not in l]                  # the M_S (full weight)
    single = {}
    for i, l in enumerate(labels):
        if l.count("I") == n - 1:
            q = next(k for k, ch in enumerate(l) if ch != "I"); single[(q, l[q])] = i
    out = set()
    for r in range(1, len(M) + 1):
        for T in itertools.combinations(M, r):
            if any(symp(ops[a], ops[b]) for a, b in itertools.combinations(T, 2)): continue
            x = z = 0
            for a in T: x ^= ops[a][0]; z ^= ops[a][1]
            ctx = list(T); ok = True
            for q in range(n):
                letter = "IXZY"[((x >> q) & 1) | (((z >> q) & 1) << 1)]
                if letter == "I": continue
                if (q, letter) not in single: ok = False; break
                ctx.append(single[(q, letter)])
            if not ok or len(ctx) < 3: continue
            if any(symp(ops[a], ops[b]) for a, b in itertools.combinations(ctx, 2)): continue
            out.add(tuple(sorted(ctx)))
    return ops, sorted(out)

def clash_exists(nv, ctxs, signs, banned=None):
    """F2 test: is there a set of contexts (avoiding `banned`) with all degrees even and an odd number negative?"""
    use = [k for k, c in enumerate(ctxs) if banned is None or banned not in c]
    rows = []
    for v in range(nv):                                      # row v: incidence of observable v
        r = 0
        for j, k in enumerate(use):
            if v in ctxs[k]: r |= 1 << j
        rows.append(r)
    s = 0
    for j, k in enumerate(use):
        if signs[k] == -1: s |= 1 << j
    def rank(rs):
        piv = {}
        for r in rs:
            for b, p in piv.items():
                if r >> b & 1: r ^= p
            if r: piv[r.bit_length() - 1] = r
            for b in list(piv):
                pass
        return len(piv)
    def reduce(r, basis):
        for b in sorted(basis, reverse=True):
            if r >> b & 1: r ^= basis[b]
        return r
    basis = {}
    for r in rows:
        r = reduce(r, basis)
        if r:
            hb = r.bit_length() - 1
            for b in list(basis):
                if basis[b] >> hb & 1: basis[b] ^= r
            basis[hb] = r
    return reduce(s, basis) != 0                             # s outside the row space <=> a clash exists

def critical(labels, given_ctxs):
    ops, ctxs = all_contexts(labels)
    given = {tuple(sorted(c)) for c in given_ctxs}
    signs = [product_sign([ops[v] for v in c]) for c in ctxs]
    assert given <= set(ctxs)
    assert clash_exists(len(ops), ctxs, signs)
    removable = [labels[v] for v in range(len(ops)) if clash_exists(len(ops), ctxs, signs, banned=v)]
    return len(ctxs), len(given), removable

if __name__ == "__main__":
    res = {}
    for n in (3, 5, 7, 9, 11, 13):
        labels, given = graph_star(n, [(q, (q + 1) % n) for q in range(n)])
        total, ng, removable = critical(labels, given)
        print(f"C{n}: {total} possible contexts (given {ng}); observables whose deletion leaves a clash: {len(removable)}"
              f" -> {'CRITICAL' if not removable else 'not critical'}")
        res[f"C{n}"] = not removable
    for name, n, E in (("triangle+C4", 6, [(0, 1), (1, 2), (0, 2), (0, 3), (3, 4), (4, 5), (5, 0)]),
                       ("bowtie (two triangles)", 5, [(0, 1), (1, 2), (0, 2), (0, 3), (3, 4), (0, 4)][:6]),
                       ("triangle+C6", 8, [(0, 1), (1, 2), (0, 2), (0, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0)])):
        if len(E) % 2 == 0: continue
        labels, given = graph_star(n, E)
        total, ng, removable = critical(labels, given)
        print(f"{name}: {total} possible contexts (given {ng}); deletable observables: {len(removable)}"
              f" -> {'CRITICAL' if not removable else 'not critical'}")
        res[name] = not removable
    assert all(res[f"C{n}"] for n in (3, 5, 7, 9, 11, 13)) and not res["triangle+C4"] and not res["triangle+C6"]
    print("\nodd cycles critical through n = 13; non-cycle graphs not critical (referee's correction reproduced)")
