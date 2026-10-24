"""split_test.py — Round 9 of PREREG.md: chain-split graph-star contexts, then recheck magic and genuineness."""
from ms_core import parse, label, product_sign, check_magic, min_magic_rank, noncontextual_bound
from graph_star import graph_star

def chain_split(ops, ctxs, which):
    """ops: list of (x,z); ctxs: list of index tuples; which: indices of contexts to split into size-3 chains"""
    ops = list(ops); vid = {o: i for i, o in enumerate(ops)}
    out = []
    for ci, c in enumerate(ctxs):
        if ci not in which or len(c) <= 3: out.append(tuple(c)); continue
        cur = c[0]
        for k in range(1, len(c) - 1):
            if k == len(c) - 2:                                      # last piece closes on the final operator
                out.append((cur, c[k], c[k + 1])); break
            vx = ops[cur][0] ^ ops[c[k]][0]; vz = ops[cur][1] ^ ops[c[k]][1]
            if (vx, vz) not in vid: vid[(vx, vz)] = len(ops); ops.append((vx, vz))
            nxt = vid[(vx, vz)]
            out.append((cur, c[k], nxt)); cur = nxt
    return ops, out

res = {}
labels, ctxs = graph_star(5, [(q, (q + 1) % 5) for q in range(5)])
base = [parse(l) for l in labels]
for name, which in (("Q1 locals split", set(range(1, len(ctxs)))), ("Q2 GHZ split", {0})):
    ops, cs = chain_split(base, ctxs, which)
    ok, neg, deg = check_magic(ops, cs)
    r, d = min_magic_rank(len(ops), cs, limit_dim=24)
    b = noncontextual_bound(len(ops), cs, neg) if ok and len(ops) <= 24 else None
    q = r // 2 if isinstance(r, int) else r
    print(f"{name}: {len(ops)} observables, {len(cs)} contexts (max size {max(map(len, cs))}), parity clash {ok},"
          f" Gram dim {d}, min magic rank {r} -> {q} qubits" + (f", eps {1 - b / len(cs):.3f}" if b is not None else ""))
    res[name.split()[0]] = ok and isinstance(q, int) and q < 5
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
