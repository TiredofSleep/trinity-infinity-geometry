"""
tlc_hidden.py: the chat's "next test" on TLC's MS5-26 (Trandafir-Lisonek-Cabello, PRL 129, 200401,
arXiv:2202.13141v2, Appendix D.3).

Lemma 5 (LOWER_BOUND.md): b = C - 2 w_min (TLC Theorem 2), and in a context-minimal clash w_min = 1. So
w_min > 1 means the incidence matrix has a dependency T other than "all contexts", and T or its complement
is a smaller parity clash among the set's own contexts. TLC report b/Q = 24/30 for MS5-26, so w_min = 3.
Here: verify the printed assignment, compute w_min from scratch, list every hidden sub-clash, and ask how
many qubits each one needs (minimum magic Gram rank, TLC Cor. 10): first Lemma 1 (rank <= V_T - r_T), then the
vectorized search in gram_np.py (checked against ms_core.py), which stops at the first rank <= 8 and is exhaustive
up to Gram dimension 24. Prints ASCII only.
Usage: python tlc_hidden.py [processes]
"""
import itertools, sys
from collections import Counter
from multiprocessing import Pool
from ms_core import parse, check_magic, verify_with_matrices, min_magic_rank, rank_rows
from gram_np import min_rank_np

OBS = """IIIIZ IIIIX IIIZI IIIXI IIZII IIXXI IZIXI ZIIXX IIZIX XXZZI IYXII ZYXII ZIIII ZZZII XXIZX ZXYZI
XXIII YZIII ZYIII IZZII ZXYZZ YZXXZ ZYZZI IYXZZ ZYIIX ZYXIZ""".split()
CTX = [[1, 3, 11, 24], [1, 6, 18, 22], [1, 12, 26], [1, 16, 21], [2, 3, 15, 17], [2, 4, 8, 13], [2, 5, 9],
       [2, 19, 25], [3, 5, 10, 17], [3, 5, 19, 23], [3, 9, 23, 25], [3, 11, 14, 16], [3, 12, 16, 20],
       [3, 13, 24, 26], [3, 15, 18, 25], [3, 20, 21, 26], [4, 5, 7, 20], [4, 6, 12, 19], [4, 17, 22, 26],
       [6, 7, 16, 23], [6, 8, 11, 25], [7, 8, 9, 14], [7, 10, 21, 22], [8, 15, 22, 24], [9, 10, 15],
       [10, 18, 23], [11, 12, 13], [13, 14, 20], [14, 21, 24], [17, 18, 19]]


def dependencies(vecs):
    """basis of {T : the contexts in T sum to zero}, contexts given as observable bit masks"""
    piv, comb, basis = {}, {}, []
    for i, v in enumerate(vecs):
        c = 1 << i
        for b in sorted(piv, reverse=True):
            if v >> b & 1:
                v ^= piv[b]; c ^= comb[b]
        if v:
            b = v.bit_length() - 1
            piv[b] = v; comb[b] = c
        else:
            basis.append(c)
    return basis


def span(basis):
    out = {0}
    for b in basis:
        out |= {x ^ b for x in out}
    return out


def test_sub(args):
    """how many qubits a sub-collection of contexts needs: the walk stops as soon as it finds a magic Gram
    matrix of rank <= 8 (so 'fewer than 5' is certain); otherwise it is exhaustive"""
    mask, ctxs = args
    m = [i for i in range(len(ctxs)) if mask >> i & 1]
    used = sorted({v for i in m for v in ctxs[i]})
    relabel = {v: k for k, v in enumerate(used)}
    sub = [[relabel[v] for v in ctxs[i]] for i in m]
    r = rank_rows([sum(1 << relabel[v] for v in ctxs[i]) for i in m])
    own = r == len(m) - 1
    if len(used) - r < 10:                  # Lemma 1: Gram rank <= V - r < 10, so fewer than 5 qubits, no search
        return mask, len(m), len(used), own, "lemma1", len(used) - r
    q, dim, how = min_rank_np(len(used), sub, stop_at=8, exhaust_dim=24)
    return mask, len(m), len(used), own, (q, how), dim


def be_gentle():
    """below-normal priority on Windows; pool workers started afterwards inherit it"""
    if sys.platform == "win32":
        import ctypes
        k = ctypes.windll.kernel32
        k.SetPriorityClass(k.GetCurrentProcess(), 0x00004000)


if __name__ == "__main__":
    be_gentle()
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    ctxs = [[v - 1 for v in c] for c in CTX]
    V, C = len(OBS), len(ctxs)
    ops = [parse(s) for s in OBS]
    clash, neg, deg = check_magic(ops, ctxs)
    signs = verify_with_matrices(OBS, ctxs)
    assert [i for i, s in enumerate(signs) if s == -1] == neg
    d = Counter(deg); sz = Counter(map(len, ctxs))
    print(f"MS5-26 as printed: V = {V}, C = {C}; observable degrees {dict(sorted(d.items()))};"
          f" context sizes {dict(sorted(sz.items()))}")
    print(f"  explicit 32x32 matrices: every context commutes and multiplies to +-I; negative contexts"
          f" {[i + 1 for i in neg]} ({len(neg)}, odd = {len(neg) % 2 == 1}); parity clash = {clash}")
    vec = [sum(1 << v for v in c) for c in ctxs]
    r = rank_rows(vec)
    K = dependencies(vec)
    s = sum(1 << i for i in neg)
    print(f"  incidence rank r = {r} (context-minimal would need C - 1 = {C - 1}); dependencies: dim {len(K)};"
          f" Lemma 1: V >= 2n + r gives {V} >= {10 + r}")
    # w_min = min weight of y with y.t = s.t for every dependency t (y ranges over s + the column space)
    w = next(k for k in range(1, C + 1) for y in itertools.combinations(range(C), k)
             if all(bin(sum(1 << i for i in y) & t).count("1") % 2 == bin(s & t).count("1") % 2 for t in K))
    print(f"  w_min = {w} -> noncontextual bound b = C - 2 w_min = {C - 2 * w} (TLC Table II: 24/30)")
    q, dim = min_magic_rank(V, ctxs, limit_dim=22)
    print(f"  whole set: Gram space dimension {dim}, minimum magic rank {q} -> {q // 2} qubits")

    print("\nHidden sub-clashes: proper sub-collections T of the contexts with every observable of even")
    print("T-degree and an odd number of negative contexts")
    full = (1 << C) - 1
    subs = [T for T in span(K) if T not in (0, full)
            and sum(1 for i in range(C) if T >> i & 1 and i in neg) % 2 == 1]
    print(f"  {len(subs)} of them; testing each on {P} processes", flush=True)
    res = []
    with Pool(P) as pool:
        for k, r in enumerate(pool.imap_unordered(test_sub, [(T, ctxs) for T in subs], chunksize=4), 1):
            res.append(r)
            if k % 512 == 0:
                print(f"    {k} tested; so far {sum(1 for x in res if x[4] != 'lemma1' and x[4][1] == 'exhaustive' and x[4][0] >= 10)}"
                      f" need 5 qubits", flush=True)
    tally = Counter()
    genuine, unresolved = [], []
    for mask, nc, nv, own, q, dim in res:
        kind = ("fewer than 5 (Lemma 1)" if q == "lemma1" else
                "fewer than 5 (found)" if q[0] is not None and q[0] <= 8 else
                "needs 5" if q[1] == "exhaustive" and q[0] >= 10 else "unresolved")
        tally[(kind, own)] += 1
        if kind == "needs 5":
            genuine.append((nv, nc, own, mask))
        if kind == "unresolved":
            unresolved.append((nv, nc, dim, mask))
    for (kind, own), m in sorted(tally.items()):
        print(f"  {m:5d}  {kind:24s} context-minimal = {own}")
    print(f"  proper sub-clashes that still need all 5 qubits: {len(genuine)}")
    for nv, nc, own, mask in sorted(genuine)[:12]:
        print(f"    {nv} observables, {nc} contexts, context-minimal = {own}:"
              f" contexts {[i + 1 for i in range(C) if mask >> i & 1]}")
    if unresolved:
        print(f"  unresolved (Gram space dimension > 24): {len(unresolved)}; smallest"
              f" {[(nv, nc, dim) for nv, nc, dim, _ in sorted(unresolved)[:5]]}")
    if genuine:
        best = min(genuine)
        print(f"  smallest 5-qubit core inside MS5-26: {best[0]} observables, {best[1]} contexts")
