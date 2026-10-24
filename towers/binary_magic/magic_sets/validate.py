"""validate.py — W1–W3 of PREREG.md: the toolkit on known magic sets."""
from ms_core import *

res = {}
def run(name, labels, ctxs, n, want_qubits, want_bound):
    ops = [parse(l) for l in labels]
    ok, neg, deg = check_magic(ops, ctxs)
    msign = verify_with_matrices(labels, ctxs)
    assert [i for i, s in enumerate(msign) if s == -1] == neg, "bit arithmetic and matrices disagree on signs"
    b = noncontextual_bound(len(ops), ctxs, neg)
    r, d = min_magic_rank(len(ops), ctxs)
    own = rank_rows(gram_of(ops))
    print(f"{name}: parity clash {ok}, negatives {neg}, bound {b}/{len(ctxs)}, Gram space dim {d},"
          f" min magic rank {r} -> {r // 2 if isinstance(r, int) else r} qubits (own operators: rank {own})")
    return ok and r == 2 * want_qubits and b == want_bound

square = ["XI", "IX", "XX", "IZ", "ZI", "ZZ", "XZ", "ZX", "YY"]
sq_ctx = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
res["W1"] = run("Mermin square", square, sq_ctx, 2, 2, 4)

penta = ["XII", "IXI", "IIX", "YII", "IYI", "IIY", "XXX", "YYX", "YXY", "XYY"]
pe_ctx = [(0, 1, 2, 6), (3, 4, 2, 7), (3, 1, 5, 8), (0, 4, 5, 9), (6, 7, 8, 9)]
res["W2"] = run("Mermin pentagram", penta, pe_ctx, 3, 3, 3)

padded = ["XIZ", "IXZ", "XXI", "IZI", "ZII", "ZZI", "XZZ", "ZXZ", "YYI"]   # a third qubit, cancelling on every line
res["W3"] = run("Mermin square, padded with a third qubit", padded, sq_ctx, 3, 2, 4)
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
assert all(res.values())
