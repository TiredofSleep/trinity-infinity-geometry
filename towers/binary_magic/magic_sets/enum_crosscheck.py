"""enum_crosscheck.py — the fast enumerator must produce exactly the hypergraphs the slow, obviously
complete one does (same class, same minimality filter, same canonical form)."""
import itertools
import lower_bound as slow
import lower_bound2 as fast

def slow_set(C, smax, Vmax):
    out = set()
    for mult in slow.enumerate_hypergraphs(C, 3, smax, Vmax):
        V, ctxs = slow.build(mult, C)
        if len(set(map(frozenset, ctxs))) < C or not fast.is_minimal(V, ctxs): continue
        out.add(fast.canon(C, ctxs, V))
    return out
def fast_set(C, smax, Vmax):
    out = set()
    for V in range(3, Vmax + 1):
        for highs, mg in fast.hypergraphs(C, V, smax):
            Vv, ctxs = fast.build(C, highs, mg)
            if len(set(map(frozenset, ctxs))) < C or not fast.is_minimal(Vv, ctxs): continue
            out.add(fast.canon(C, ctxs, Vv))
    return out
ok = True
for C, smax, Vmax in ((3, 4, 8), (4, 4, 9), (5, 4, 10), (4, 5, 10), (5, 5, 9)):
    a, b = slow_set(C, smax, Vmax), fast_set(C, smax, Vmax)
    print(f"C={C}, sizes<={smax}, V<={Vmax}: slow {len(a)}, fast {len(b)}, identical: {a == b}", flush=True)
    ok &= a == b
assert ok
print("fast enumerator matches the brute-force one on every tested class")
