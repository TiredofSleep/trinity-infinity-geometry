"""
waegell_stars.py: the literature gate for the graph stars. Waegell's thesis (arXiv:1307.6264, Ch. 6.2,
Tables 26-27) gives two "Star" families of parity proofs for all N. Are they the C_n graph stars, and are
they genuine N-qubit in the Trandafir-Lisonek-Cabello sense?

Kernels, read off the tables (qubit q = position q in the string):
  odd N  (Table 26, Aravind; N = 5 is DiVincenzo-Peres):  Z^N and the N cyclic shifts of X Z X.
  even N (Table 27, Waegell-Aravind): Z^N, X X Z^(N-2), Z X X, X Z I X, X X on (3,4) ... (N-2,N-1), X on 2 and N-1.
Each kernel observable K also gets a local context: K plus its factors. The thesis's figures (Fig. 10,
N = 4; Fig. 17, N = 6) group the block Z^(N-2) on qubits 2..N-1 that Z^N and X X Z^(N-2) share into one
observable; "ungrouped" uses single-qubit factors everywhere. Fig. 16 (N = 5) has no grouping.
Prints ASCII only.
"""
import itertools, sys
from collections import Counter
from ms_core import parse, label, check_magic, verify_with_matrices, min_magic_rank, noncontextual_bound
from lower_bound2 import is_minimal


def odd_kernel(N):
    ks = ["Z" * N]
    for c in list(range(1, N)) + [0]:                     # the table's row order: centres 1..N-1, then 0
        s = ["I"] * N
        s[(c - 1) % N] = "X"; s[c] = "Z"; s[(c + 1) % N] = "X"
        ks.append("".join(s))
    return ks


def even_kernel(N):
    def op(d):
        s = ["I"] * N
        for q, ch in d.items():
            s[q] = ch
        return "".join(s)
    ks = ["Z" * N, "XX" + "Z" * (N - 2), op({0: "Z", 1: "X", 2: "X"}), op({0: "X", 1: "Z", 3: "X"})]
    ks += [op({q: "X", q + 1: "X"}) for q in range(3, N - 1)]
    ks.append(op({2: "X", N - 1: "X"}))
    return ks


def star(kernel, group_tail=False):
    """observables (labels) and contexts (index lists): the kernel, then one local context per kernel element"""
    N = len(kernel[0])
    obs, idx = [], {}
    def get(lbl):
        if lbl not in idx:
            idx[lbl] = len(obs); obs.append(lbl)
        return idx[lbl]
    K = [get(k) for k in kernel]
    tail = "II" + "Z" * (N - 2)
    ctxs = [K]
    for k in kernel:
        parts = []
        grouped = group_tail and k[2:] == "Z" * (N - 2)
        for q, ch in enumerate(k):
            if ch == "I" or (grouped and q >= 2):
                continue
            s = ["I"] * N; s[q] = ch
            parts.append(get("".join(s)))
        if grouped:
            parts.append(get(tail))
        ctxs.append([idx[k]] + parts)
    return obs, ctxs


def graph_star_cycle(n):
    """the C_n graph star (THEOREM.md): X_v, Y_v, M_0 = X^n, M_e = Y on e and X elsewhere"""
    obs, idx = [], {}
    def get(lbl):
        if lbl not in idx:
            idx[lbl] = len(obs); obs.append(lbl)
        return idx[lbl]
    def single(q, ch):
        s = ["I"] * n; s[q] = ch; return get("".join(s))
    E = [(i, (i + 1) % n) for i in range(n)]
    M0 = get("X" * n)
    Me = []
    for e in E:
        s = ["X"] * n
        for q in e:
            s[q] = "Y"
        Me.append(get("".join(s)))
    ctxs = [[M0] + Me, [M0] + [single(q, "X") for q in range(n)]]
    for e, m in zip(E, Me):
        ctxs.append([m] + [single(q, "Y" if q in e else "X") for q in range(n)])
    return obs, ctxs


def profile(obs, ctxs):
    deg = Counter(v for c in ctxs for v in c)
    d = Counter(deg[v] for v in range(len(obs)))
    s = Counter(len(c) for c in ctxs)
    return ("observables " + " ".join(f"{m}x deg {k}" for k, m in sorted(d.items())),
            "contexts " + " ".join(f"{m}x size {k}" for k, m in sorted(s.items())))


def report(name, obs, ctxs, n, matrices=True, limit_dim=22):
    ops = [parse(l) for l in obs]
    clash, neg, deg = check_magic(ops, ctxs)
    V, C = len(obs), len(ctxs)
    line = [f"{name}: V = {V}, C = {C}, parity clash = {clash}, negative contexts = {neg}"]
    if matrices and n <= 8:
        signs = verify_with_matrices(obs, ctxs)
        line.append(f"  explicit {2**n}x{2**n} matrices: commute, products +-I, signs {signs}")
    line.append("  " + "; ".join(profile(obs, ctxs)))
    mini = is_minimal(V, ctxs)
    line.append(f"  minimal (incidence rank C-1, Lemma 2): {mini};  Lemma 1-2 cap on qubits: {(V - C + 1) // 2}")
    q, d = min_magic_rank(V, ctxs, limit_dim=limit_dim)
    if q == "too big":
        line.append(f"  Gram space dimension {d} > {limit_dim}: not enumerated")
    elif q is None:
        line.append(f"  Gram space dimension {d}: no magic Gram matrix")
    else:
        line.append(f"  Gram space dimension {d}; minimum magic rank {q} -> needs {q // 2} qubits"
                    f" ({'GENUINE' if q >= 2 * n else 'fewer than ' + str(n)} at n = {n})")
    if V <= 22:
        b = noncontextual_bound(V, ctxs, neg)
        line.append(f"  noncontextual bound b = {b} of {C}  (C - 2 = {C - 2});  eps = 1 - b/C = {1 - b / C:.4f}")
    print("\n".join(line), flush=True)
    return q


if __name__ == "__main__":
    Ns = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6, 7]
    print("Kernels as read from Tables 26-27:")
    for N in Ns:
        print(f"  N = {N}:", " ".join(odd_kernel(N) if N % 2 else even_kernel(N)))
    print()
    for N in Ns:
        if N % 2:
            q = report(f"odd Star N={N} (Table 26)", *star(odd_kernel(N)), N)
            g = report(f"C_{N} graph star", *graph_star_cycle(N), N)
            assert g == 2 * N                                   # the graph star is genuine
            assert q == "too big" or (q == 2 * N) == (N == 3)   # the Star is genuine only at N = 3 (the pentagram)
        else:
            for grouped in (True, False):
                q = report(f"even Star N={N}, " + ("grouped tail (as in the thesis figures)" if grouped
                           else "all single-qubit factors"), *star(even_kernel(N), grouped), N)
                assert q == "too big" or q < 2 * N                # never genuine
        print()
    print("PASS: no Star with N >= 4 is genuine; every C_N graph star is")
