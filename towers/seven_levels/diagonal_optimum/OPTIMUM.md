# The most Wigner-negative diagonal states at 3, 5 and 7

> *1 yes, then p = 5 alongside everything else* — the author, 21 November 2026

For a diagonal state ψ_φ = (1/√p) Σ_x e^{iφ(x)} |x⟩ on p levels, let S(φ) = Σ_{q,s} |W(q, s)| be the total absolute
value of its Wigner function. At the first three odd primes its maximum is now known exactly, with rigorous bounds.

| p | the maximum of S | attained at | proved by |
|---|---|---|---|
| 3 | 1.58625682771454… | the qutrit T state: 2 points of D, 18 states | `bb3.exe` (Li and Luo's theorem [LL], reproduced) |
| **5** | **1.97757582130854208841…** | **one orbit of 500 states, not a T state** | **`bb5.exe`: new** |
| 7 | 2.45030411854008217396… | the T states of the best class: 2 points of D, 98 states | [`../t7_rigorous/`](../t7_rigorous/RIGOROUS.md); again by `bb7.exe` |

**Theorem (p = 5).** Every diagonal state on five levels has

  S ≤ S*₅ = 1.97757582130854208841477817308660330000376679…,

with equality exactly on one orbit of 500 states under the diagonal Clifford group: the 25 Clifford phases times the
20 affine maps x ↦ αx + t, with complex conjugation acting inside the orbit.
- The rigorous enclosure is S*₅ ∈ [1.9775758213085037, 1.9775758213085828]. The 60 digits above come from Newton's
  method at 130 digits on the certified critical point.
- Feng and Luo report 500 diagonal gates at 5 that beat the T gate [FL26]. The optimal states form one orbit of
  exactly 500, matching their count. The theorem says that no other diagonal state does as well, and gives the
  common value S*₅.
- The T state at 5 has S = 1.8944, so the optimum beats it by 4.4%.

**The maximizer.** In D it has phases (in turns) 0, 0.011856558…, 0.023713116…, 0.363229316…, 0.660483800….
- φ(2) = 2φ(1) exactly (to 131 digits).
- Its only symmetry is the reflection x ↦ 2 − x combined with complex conjugation, with no Clifford phase. So
  φ(x) + φ(2 − x) = φ(2), and re-centred at x = 1 the state is odd: ψ(−y) = −ψ(y). The maximum lies in a
  two-parameter family of odd states, as round 33 found numerically.
- No integer polynomial of degree at most 24, with coefficients up to 10⁹, has S*₅ or the cosines of the phases as a
  root (PSLQ at 125 digits). If S*₅ has a closed form, it is of higher degree. An exact polynomial would come from
  eliminating the two-parameter critical-point equations; that is not attempted here.

## How it is proved ([`bb.c`](bb.c))

`bb.c` is the rigorous branch and bound of [`../t7_rigorous/t7_rigorous.c`](../t7_rigorous/t7_rigorous.c),
generalized to any small odd prime (fixed when compiled). Its arithmetic is the same: every rounding is enclosed,
cos and sin come from its own interval enclosures, and the constants come from
[`bb_constants.py`](bb_constants.py) in exact rational arithmetic.

What is new: the maximizers need not be known in closed form. [`prepare.py`](prepare.py) finds a candidate in
floating point and maps it through every symmetry into the box D = [−π/p, π/p]² × [0, 2π]^(p−3). For each candidate
c, the program then proves:
1. every E(q, s) keeps its sign on a box B_c of half-width ρ around it, so S is smooth there;
2. the interval Hessian of S over B_c is negative definite (an interval LDL^T of −H with every pivot positive), so S
   is strictly concave on B_c and has at most one critical point there;
3. the Krawczyk operator of ∇S maps a box X_c of half-width 10⁻⁹ into its own interior, so ∇S has exactly one zero
   φ_c* in X_c, and φ_c* is the maximum of S over B_c;
4. for c > 0, the symmetry that produced the candidate maps X_0 into B_c, so φ_c* is the image of φ_0* and has the
   same value;
5. the boxes B_c are pairwise disjoint, so the critical points are distinct.

The branch and bound then discards every box of D:
- by the bound, when its upper bound for S is below S_LO, a rigorous lower bound for S at a candidate;
- by monotonicity, when S is smooth on it and a partial derivative cannot vanish;
- or because it lies inside a certified box.

So every global maximizer in D is one of the φ_c*, they all share one value, and that value is enclosed between
S_LO and the upper bound of S on X_c. The reduction to D and the reason the three rules suffice are those of
[`../t7_rigorous/RIGOROUS.md`](../t7_rigorous/RIGOROUS.md) §2–3.

| p | candidates in D | certified half-width ρ | boxes | time (4 threads) | enclosure of the maximum | log |
|---|---|---|---|---|---|---|
| 3 | 2 | 0.02 | 348 | 0.0 s | [1.5862568277145306, 1.586256827714561] | [`bb3.log`](bb3.log) |
| 5 | 20 | 0.004 | 629 676 | 11.2 s | [1.9775758213085037, 1.9775758213085828] | [`bb5.log`](bb5.log) |
| 7 | 2 | 0.004 | 47 174 654 | 41.8 min | [2.4503041185400107, 2.4503041185401555] | [`bb7.log`](bb7.log) |

At p = 7 the second program agrees with the first, which used a cube lemma proved by hand
([`../t7_rigorous/constants.py`](../t7_rigorous/constants.py)). Here the cubes are certified by the program itself
(smallest pivot of −H on a cube 15.0). Both runs examined the same 47 174 654 boxes, split the same way: 23 423 054
by the bound, 163 901 by monotonicity and 884 inside the cubes.

**Provenance.** The three runs used one build (2026-11-21) of `bb.c`, SHA-256
003221679dfd822c60180660d91c5f1b847e9fc73ff0d89fd73ba1d272af4e79, with `bb_constants.h`, SHA-256
eac005c6f8bc3068403eb44bf0b6dcea70e051957837425f3cf7e337945c6cb6. Both hashes are of the files as stored in the
repository, with LF line endings.

## Checks that are not part of the proof ([`bb_selftest.py`](bb_selftest.py), [`bb_selftest.log`](bb_selftest.log))

At each of p = 3, 5, 7, the program's bounds were tested on 2000 boxes, from the first grid down to 10⁻⁷, many near
the maximizers.
- S at 64 sampled points of each box never exceeded the upper bound and never fell below the lower bound.
- Every box flagged monotone had sampled gradients of one fixed sign in some coordinate.
- At p = 7 the upper bounds agree with `t7_rigorous.exe` to 2·10⁻¹⁴, with the same flags on all 2000 boxes. The
  small difference is because the constants 2πk/7 are computed here in interval arithmetic rather than taken from
  exact rational enclosures.

## What is trusted

The same as for the p = 7 proof:
- IEEE 754 double arithmetic, rounded to nearest, as compiled by MSVC with `/fp:strict` on x64;
- Python's exact integers and fractions, for the constants.

`prepare.py` is not trusted: its candidates are only starting points, and everything the proof uses about them is
certified in `bb.c`. Nothing is formally verified in a proof assistant, and no human referee has checked it.

## Standing

- **p = 3** reproduces Li and Luo's theorem [LL] that the qutrit T gate is optimal.
- **p = 5** is new as far as we know. Feng and Luo found 500 gates beating the T gate [FL26]. Here the optimal
  states are proved to be exactly one orbit of 500, with their value, enclosed to 10⁻¹³.
- **p = 7** is the theorem of [`../t7_rigorous/`](../t7_rigorous/RIGOROUS.md).

At 11 the same method would need a 10-dimensional search, which is out of reach as it stands.

## Reproduce

```
python bb_constants.py          # the prime-independent constants, exact rational arithmetic -> bb_constants.h
build.bat                       # MSVC: bb3.exe, bb5.exe, bb7.exe (cl /O2 /fp:strict /openmp /DP=p)
python prepare.py 5             # candidates -> candidates_5.txt (likewise 3 and 7)
bb5.exe prove candidates_5.txt 4
python bb_selftest.py           # the checks above, a minute
```

## Sources

- [LL] F. Li and S. Luo, *Phys. Lett. A* (2023), doi 10.1016/j.physleta.2022.128620: the qutrit T gate is optimal
  for Wigner negativity among diagonal gates.
- [FL26] L. Feng and S. Luo, *Phys. Rev. A* **113**, 042434 (2026): diagonal gates in prime dimension; at 5, 500
  gates beat the T gate.
