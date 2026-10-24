"""
antinomy.py — the F2 antinomy detector (Test B of PREREG.md).

Give it contexts, each with parity demands on shared variables ("these signs must multiply to -1").
It says whether all the demands can hold at once. If not, it returns a smallest set of contexts whose
demands already contradict each other: the antinomy, with its certificate.

    detect(contexts) where contexts = {name: [(set_of_variables, rhs_bit), ...]}
    -> ("consistent", solution) or ("clash", smallest_clashing_context_names)

Validated on three known cases before use on anything new.
"""
import itertools
import numpy as np

def _solve(eqs, nvar):
    rows = [(sum(1 << v for v in vs), r) for vs, r in eqs]
    piv = {}
    for m, r in rows:
        for b, (pm, pr) in piv.items():
            if m >> b & 1: m ^= pm; r ^= pr
        if m == 0:
            if r: return None
            continue
        b = m.bit_length() - 1
        for b2, (pm, pr) in list(piv.items()):
            if pm >> b & 1: piv[b2] = (pm ^ m, pr ^ r)
        piv[b] = (m, r)
    x = [0] * nvar
    for b, (m, r) in piv.items(): x[b] = r          # free variables set to 0
    return x

def detect(contexts, max_certificate=None):
    names = list(contexts)
    var = sorted({v for c in contexts.values() for vs, _ in c for v in vs}, key=str)
    ix = {v: i for i, v in enumerate(var)}
    enc = {n: [({ix[v] for v in vs}, r & 1) for vs, r in contexts[n]] for n in names}
    sol = _solve([e for n in names for e in enc[n]], len(var))
    if sol is not None:
        return "consistent", {v: sol[ix[v]] for v in var}
    for k in range(1, (max_certificate or len(names)) + 1):
        for S in itertools.combinations(names, k):
            if _solve([e for n in S for e in enc[n]], len(var)) is None:
                return "clash", list(S)
    return "clash", names

# ---------------------------------------------------------------- validation
if __name__ == "__main__":
    results = {}

    # B1: Mermin–Peres square. Cells c00..c22 hold +-1 values (bit 1 = -1). Rows multiply to +1,
    # columns to +1, +1, -1 (the operator identities). Each cell sits in one row and one column.
    ctx = {f"row{i}": [({f"c{i}{j}" for j in range(3)}, 0)] for i in range(3)}
    ctx.update({f"col{j}": [({f"c{i}{j}" for i in range(3)}, int(j == 2))] for j in range(3)})
    verdict, cert = detect(ctx)
    results["B1"] = verdict == "clash" and len(cert) == 6
    print("B1 Mermin–Peres square:", verdict, "| smallest clash:", cert)

    # Octonion machinery for B2 and B3: a context = one Fano plane; its demands = the 3 parity
    # conditions on its 7 line signs that make it a copy of the octonions.
    rng = np.random.default_rng(3)
    def algebra(nbits, sign):
        N = 2 ** nbits; T = np.zeros((N, N, N))
        for a in range(N):
            for b in range(N):
                c = a ^ b
                if a == 0 or b == 0: s = 1
                elif a == b: s = -1
                else:
                    line = tuple(sorted((a, b, c))); x, y, z = line
                    s = sign[line] if (a, b) in {(x, y), (y, z), (z, x)} else -sign[line]
                T[a, b, c] = s
        return T
    def alternative(T, idx):
        n = T.shape[0]; P = lambda x, y: np.einsum("abc,a,b->c", T, x, y)
        for _ in range(6):
            x = np.zeros(n); y = np.zeros(n); x[idx] = rng.normal(size=len(idx)); y[idx] = rng.normal(size=len(idx))
            if not np.allclose(P(P(x, x), y), P(x, P(x, y))): return False
        return True
    lines_of = lambda pts: [t for t in itertools.combinations(sorted(pts), 3) if t[0] ^ t[1] ^ t[2] == 0]
    def plane_demands(P, nbits, all_lines):
        lp = lines_of(P)
        good = []
        for bits in itertools.product((0, 1), repeat=7):
            sign = {l: 1 for l in all_lines}; sign.update({l: (-1) ** b for l, b in zip(lp, bits)})
            if alternative(algebra(nbits, sign), [0] + sorted(P)): good.append(np.array(bits))
        g0 = good[0]; Vs = np.array([(g - g0) % 2 for g in good])
        eqs = []
        for w in itertools.product((0, 1), repeat=7):
            w = np.array(w)
            if w.any() and not ((Vs @ w) % 2).any():
                eqs.append(({lp[k] for k in range(7) if w[k]}, int(w @ g0 % 2)))
        return eqs                                     # all 7 nonzero checks of the 3-dim check space

    # B2: one Fano plane
    L3 = lines_of(range(1, 8))
    verdict, sol = detect({"fano": plane_demands(set(range(1, 8)), 3, L3)})
    results["B2"] = verdict == "consistent"
    print("B2 octonion signs on the Fano plane:", verdict)

    # B3: the 15 Fano planes inside 4 bits
    L4 = lines_of(range(1, 16))
    planes = sorted({frozenset({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c})
                     for a, b, c in itertools.combinations(range(1, 16), 3)
                     if len({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c}) == 7}, key=sorted)
    ctx = {f"plane{''.join(f'{p:x}' for p in sorted(P))}": plane_demands(P, 4, L4) for P in planes}
    verdict, cert = detect(ctx, max_certificate=6)
    results["B3"] = verdict == "clash" and len(cert) == 5
    print("B3 15 octonion copies in 16 dimensions:", verdict, "| smallest clash:", len(cert), "copies", cert)

    print("\nSCORE:", {k: ("PASS" if v else "FAIL") for k, v in results.items()})
    assert all(results.values())
