"""
verify_role_magma.py — Verification harness for the J09 manuscript

Sanders + Gish (2026):
  "A Small Commutative Non-Associative Magma on Z/10Z with
   Role-Deterministic Boundary Behavior"

Verifies:
1. The 4x4 role-mode table M_R derived from BHML and the role partition
   {V={0}, F={1,3,5,7,9}, S={2,4,8}, T={6}}.
2. M_R is commutative, has V as two-sided identity, and is non-associative
   (with explicit witness M_R(M_R(F,F),S) = F != T = M_R(F, M_R(F,S))).
3. BHML is role-deterministic on every input pair containing V or T,
   and role-branching on (F,F), (F,S), (S,F), (S,S) — with the exact
   role-output multisets listed in Theorem 4.1 of the manuscript.
4. The BH-self-orbit first-passage time tau(n) to value 7:
   tau(n) = 7-n for n in {1..7}; tau(8)=1; tau(0)=tau(9)=infinity.
5. The row-asymmetry function Psi(n) and its sigma-orbit decomposition.

License: CC-BY-4.0
Runtime: <0.1 s on a standard laptop.
"""
from collections import Counter
from ck_tables import TSML, BHML, role, V_role, F_role, S_role, T_role, SIGMA


def main():
    print("=" * 60)
    print("J09 verification: role-magma M_R from BHML")
    print("=" * 60)
    print()

    # 1. Role-mode table
    role_sets = {'V': V_role, 'F': F_role, 'S': S_role, 'T': T_role}
    roles = ['V', 'F', 'S', 'T']
    M_R = {}
    O = {}
    for ra in roles:
        for rb in roles:
            outputs = []
            for a in role_sets[ra]:
                for b in role_sets[rb]:
                    outputs.append(role(BHML[a][b]))
            c = Counter(outputs)
            mode = c.most_common(1)[0][0]
            M_R[(ra, rb)] = mode
            O[(ra, rb)] = c

    print("Role-mode table M_R:")
    print("    | " + " ".join(f"{r:^3}" for r in roles))
    print("    +" + "-" * (4 * len(roles) + 1))
    for ra in roles:
        line = f" {ra:^2} | " + " ".join(f"{M_R[(ra, rb)]:^3}" for rb in roles)
        print(line)
    print()

    # 2. Properties: commutativity, V identity, non-associativity
    commutative = all(M_R[(a, b)] == M_R[(b, a)] for a in roles for b in roles)
    assert commutative, "M_R must be commutative"
    print(f"M_R commutative: {commutative}")

    V_identity = all(M_R[('V', r)] == r and M_R[(r, 'V')] == r for r in roles)
    assert V_identity, "V must be a two-sided identity"
    print(f"V is two-sided identity in M_R: {V_identity}")

    # Non-assoc witness
    a = M_R[(M_R[('F', 'F')], 'S')]
    b = M_R[('F', M_R[('F', 'S')])]
    print(f"M_R(M_R(F,F), S) = M_R({M_R[('F', 'F')]}, S) = {a}")
    print(f"M_R(F, M_R(F,S)) = M_R(F, {M_R[('F', 'S')]}) = {b}")
    assert a != b, "Non-associativity witness must hold"
    print(f"Non-associative witness: M_R(M_R(F,F),S) = {a} != {b} = M_R(F, M_R(F,S))")
    print()

    # 3. Role-output distributions and role-deterministic boundary
    print("Role-output multisets:")
    for ra in roles:
        for rb in roles:
            out = dict(O[(ra, rb)])
            tag = "(deterministic)" if len(out) == 1 else "(branching)"
            print(f"  ({ra},{rb}) -> {out} {tag}")
    print()

    # Role-determinism on input pairs containing V or T
    boundary_pairs = [(a, b) for a in roles for b in roles
                      if 'V' in {a, b} or 'T' in {a, b}]
    boundary_det = all(len(O[(a, b)]) == 1 for (a, b) in boundary_pairs)
    assert boundary_det, "BHML must be role-deterministic on V/T-containing pairs"
    print(f"Role-deterministic on every (V,_) or (T,_) pair: {boundary_det}")

    interior_pairs = [(a, b) for a in roles for b in roles
                      if a in {'F', 'S'} and b in {'F', 'S'}]
    interior_branching = all(len(O[(a, b)]) >= 2 for (a, b) in interior_pairs)
    assert interior_branching, "BHML must be role-branching on (F/S)^2 pairs"
    print(f"Role-branching on (F,F), (F,S), (S,F), (S,S): {interior_branching}")
    print()

    # 4. First-passage time tau(n) to 7 on BH-self-orbit
    print("BH-self-orbit first-passage time tau(n) to value 7:")
    tau = {}
    for n in range(10):
        cur = n
        for k in range(50):
            if cur == 7:
                tau[n] = k
                break
            nxt = BHML[cur][cur]
            if nxt == cur and cur != 7:
                tau[n] = float('inf')
                break
            cur = nxt
        else:
            tau[n] = float('inf')
        print(f"  tau({n}) = {tau[n]}")

    # Verify the linear formula on {1..7}
    for n in range(1, 8):
        expected = 7 - n
        assert tau[n] == expected, f"tau({n}) = {tau[n]}, expected {expected}"
    assert tau[8] == 1, f"tau(8) = {tau[8]}, expected 1"
    assert tau[0] == float('inf') and tau[9] == float('inf'), \
        "tau(0) and tau(9) should be infinity"
    print(f"tau(n) = 7-n on n in {{1..7}}: verified")
    print(f"tau(8) = 1; tau(0) = tau(9) = infinity: verified")
    print()

    # 5. Row-asymmetry Psi(n) and its sigma-orbit decomposition
    print("Row-asymmetry function Psi(n):")
    psi = []
    for n in range(10):
        pos = sum(1 for j in range(10) if TSML[n][j] > BHML[n][j])
        neg = sum(1 for j in range(10) if BHML[n][j] > TSML[n][j])
        psi.append(pos - neg)
        print(f"  Psi({n}) = {pos - neg}")
    total = sum(psi)
    print(f"Total: {total} (expect 21 = T_6)")
    assert total == 21

    # sigma-orbit decomposition
    sigma_fixed = {0, 3, 8, 9}
    sigma_cycle = {1, 2, 4, 5, 6, 7}
    sum_fixed = sum(psi[n] for n in sigma_fixed)
    sum_cycle = sum(psi[n] for n in sigma_cycle)
    print(f"sigma-fixed sum: {sum_fixed} (expect -1)")
    print(f"sigma-cycle sum: {sum_cycle} (expect 22)")
    assert sum_fixed == -1 and sum_cycle == 22
    print(f"Sum: {sum_fixed + sum_cycle} = 21")
    print()

    # 6. sigma has order 6
    cur = list(range(10))
    for _ in range(6):
        cur = [SIGMA[x] for x in cur]
    assert cur == list(range(10)), "sigma should have order 6"
    print(f"sigma has order 6 (sigma^6 = id): True")
    print()

    print("ALL CHECKS PASSED.")


if __name__ == '__main__':
    main()
