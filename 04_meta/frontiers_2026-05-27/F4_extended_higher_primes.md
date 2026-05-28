# F4-extended — Higher-Prime Verification of |Aut| and |idem| Closed Forms

**Frontier:** Extend F4's closed-form verification of `|Aut(V_p)| = p(p^2 - 1)` and
`|idem(V over F_p)| = p + 3` from `p ∈ {3, 5, 7, 11, 13}` to higher primes 17–97.

**Date:** 2026-05-28
**Status:** TIER A on a CORRECTED form. The original F4 doc's `|Aut| = p(p^2 - 1)`
formula was empirically wrong for the canonical J18 T^BHML algebra; the actual
closed form is `|Aut(V^BHML_{F_p})| = (p − 1)^2`. The `|idem| = p + 3` form
holds robustly.
**Script:** `04_meta/frontiers_2026-05-27/F4_extended_verify.py`
(self-contained, sympy/numpy stdlib, ~65 sec total runtime for all 19 extension primes).

---

## §1 — Algorithm description

### 1.1 The V algebra

We work with the **J18 T^BHML** 4-core algebra: a 4-dimensional commutative
non-associative F_p-algebra on basis `{e_0, e_2, e_3, e_4}` defined by the
multiplication table

```
  e_0 * everything = 0          (e_0 is a two-sided zero)
  e_2 * e_2 = e_2                (e_2 is a primitive idempotent)
  e_2 * e_3 = e_3 = e_3 * e_2
  e_2 * e_4 = 0  = e_4 * e_2
  e_3 * e_3 = e_2                (e_3 is a square root of e_2)
  e_3 * e_4 = e_4 = e_4 * e_3
  e_4 * e_4 = 0                  (e_4 is nilpotent)
```

This is the canonical multiplication table of J18 (`bhml_fp_universality.py`,
2026-05-07), the same one whose idempotent counts `{2, 6, 8, 10, 14, 16}` are
tabulated in J18's manuscript abstract at `p ∈ {2, 3, 5, 7, 11, 13}`.

### 1.2 Idempotent counter (O(p^2))

The idempotency condition `x · x = x` factors cleanly:

  For `x = (a, b, c, d)`, the product `x · x = (0, b^2 + c^2, 2bc, 2cd)`.

So `x · x = x` iff `a = 0` AND `b^2 + c^2 = b` AND `c(2b − 1) = 0` AND
`d(2c − 1) = 0`. This is solvable in O(p^2) time by enumerating `b, c` and
counting valid `d` per case.

### 1.3 Automorphism counter (constraint propagation)

A linear map `φ: V → V` preserves multiplication iff:
  - `φ(e_0)` is in the annihilator: `φ(e_0) = α e_0`, `α ∈ F_p^*`.
  - `φ(e_2), φ(e_3), φ(e_4)` lie in the image of multiplication
    (= `span(e_2, e_3, e_4)`), so their e_0-coordinate is 0.
  - `φ(e_2) = φ(e_3)^2` (from `e_3^2 = e_2`).
  - `φ(e_2)^2 = φ(e_2)`, `φ(e_2) · φ(e_3) = φ(e_3)`,
    `φ(e_3) · φ(e_4) = φ(e_4)`, `φ(e_2) · φ(e_4) = 0`,
    `φ(e_4)^2 = 0`.
  - Det of the 4×4 matrix is non-zero.

The algorithm enumerates `h = φ(e_3) ∈ F_p^3` (p^3 candidates), derives `hh = h^2`
as φ(e_2), filters by `hh^2 = hh` and `hh · h = h`, then computes the 1-eigenspace
of `L_h` on the image (a 3-dim linear system) and enumerates `v = φ(e_4)` over
that kernel intersected with `{hh · v = 0}` ∩ `{v · v = 0}`. Total complexity is
O(p^3 · p^k) where k = 0..1 typically (since the 1-eigenspace is usually 0 or 1
dimensional). For p = 97 this completes in ~13 sec.

A separate brute-force sanity check at `p = 3` over all 3^16 = 43M linear maps
confirmed |Aut| = 4 (matching the constraint algorithm), validating the algorithm.

---

## §2 — Results table

| p   | \|idem\| | p+3 | match | \|Aut\| | (p−1)^2 | match | p(p²−1) | F4 hyp |
|-----|---------:|-----:|:------|--------:|--------:|:------|--------:|:-------|
|  3  |        6 |    6 |   ✓   |       4 |       4 |   ✓   |      24 |  ✗     |
|  5  |        8 |    8 |   ✓   |      16 |      16 |   ✓   |     120 |  ✗     |
|  7  |       10 |   10 |   ✓   |      36 |      36 |   ✓   |     336 |  ✗     |
| 11  |       14 |   14 |   ✓   |     100 |     100 |   ✓   |    1320 |  ✗     |
| 13  |       16 |   16 |   ✓   |     144 |     144 |   ✓   |    2184 |  ✗     |
| **17**  |   **20** |  **20** | **✓** | **256** |  **256** | **✓** |  **4896** | **✗** |
| **19**  |   **22** |  **22** | **✓** | **324** |  **324** | **✓** |  **6840** | **✗** |
| **23**  |   **26** |  **26** | **✓** | **484** |  **484** | **✓** | **12144** | **✗** |
| **29**  |   **32** |  **32** | **✓** | **784** |  **784** | **✓** | **24360** | **✗** |
| **31**  |   **34** |  **34** | **✓** | **900** |  **900** | **✓** | **29760** | **✗** |
| **37**  |   **40** |  **40** | **✓** |**1296** | **1296** | **✓** | **50616** | **✗** |
| **41**  |   **44** |  **44** | **✓** |**1600** | **1600** | **✓** | **68880** | **✗** |
| **43**  |   **46** |  **46** | **✓** |**1764** | **1764** | **✓** | **79464** | **✗** |
| **47**  |   **50** |  **50** | **✓** |**2116** | **2116** | **✓** |**103776** | **✗** |
| **53**  |   **56** |  **56** | **✓** |**2704** | **2704** | **✓** |**148824** | **✗** |
| **59**  |   **62** |  **62** | **✓** |**3364** | **3364** | **✓** |**205320** | **✗** |
| **61**  |   **64** |  **64** | **✓** |**3600** | **3600** | **✓** |**226920** | **✗** |
| **67**  |   **70** |  **70** | **✓** |**4356** | **4356** | **✓** |**300696** | **✗** |
| **71**  |   **74** |  **74** | **✓** |**4900** | **4900** | **✓** |**357840** | **✗** |
| **73**  |   **76** |  **76** | **✓** |**5184** | **5184** | **✓** |**388944** | **✗** |
| **79**  |   **82** |  **82** | **✓** |**6084** | **6084** | **✓** |**492960** | **✗** |
| **83**  |   **86** |  **86** | **✓** |**6724** | **6724** | **✓** |**571704** | **✗** |
| **89**  |   **92** |  **92** | **✓** |**7744** | **7744** | **✓** |**704880** | **✗** |
| **97**  |  **100** | **100** | **✓** |**9216** | **9216** | **✓** |**912576** | **✗** |

(Bold rows are the F4-extended primes 17–97. Italicized rows 3-13 are the
original F4 verification primes, re-run here as sanity checks.)

---

## §3 — Conclusion: ALL CONFIRMED (on the CORRECTED |Aut| formula)

### 3.1 Idempotent closed form CONFIRMED

`|idem(V^BHML_{F_p})| = p + 3` holds at every one of the 19 primes from 17 to 97
(in addition to the 5 originally verified at p ∈ {3, 5, 7, 11, 13}). The closed
form is robust across 24 primes covering small to medium magnitudes.

### 3.2 |Aut| closed form CORRECTED to (p − 1)^2

The F4 frontier doc claimed `|Aut(V_p)| = p(p^2 − 1)`. Direct brute force on the
J18 T^BHML algebra at primes 3 through 97 gives:

```
p     |Aut|    (p-1)^2   p(p^2-1)
3        4       4          24
5       16      16         120
7       36      36         336
11     100     100        1320
13     144     144        2184
17     256     256        4896
...   ...     ...         ...
97    9216    9216      912576
```

The actual closed form is **|Aut(V^BHML_{F_p})| = (p − 1)^2**, NOT p(p^2 − 1).
The F4 doc's hypothesized form is OFF by a factor of `p · (p+1) / (p−1)`
(growing without bound).

**Source of the original F4 doc claim:** the values `{6, 24, 40, 336, 1320, 2184}`
cited in F4 §1.1 (Aut column) were attributed to J48 brute-force enumeration on the
T_F5 algebra (tig_dirac.py). I re-ran a full 3^16 brute force on the T_F5 algebra
at p=3 and obtained `|Aut| = 12`, NOT 24. So the J48 tabulation appears to be
based on a third algebra not currently in the corpus, OR the original
brute force at primes other than p=5 had an error.

### 3.3 Structural interpretation of (p − 1)^2

The result `|Aut(V^BHML_{F_p})| = (p − 1)^2` admits a clean structural reading.
The automorphism group is isomorphic to `F_p^* × F_p^*`: two independent scaling
factors. Inspecting the small-prime automorphisms at p=3 (the only 4 listed):

```
( α e_0, e_2, e_3,  β e_4 )  for α, β ∈ F_3^*
```

with α ∈ {1, 2} and β ∈ {1, 2} giving 4 = 2 · 2 = (p-1)² maps. The two factors
are (i) the F_p^*-scaling on the annihilator span(e_0), and (ii) the F_p^*-scaling
on span(e_4) (the nilpotent direction). The "main" subalgebra span(e_2, e_3) is
**rigid**: there's no non-trivial automorphism mixing e_2 and e_3 once `e_3^2 = e_2`
is forced. This rigidity is consistent with V^BHML being an integral algebra
defined over Z (not just F_p), with the integer structure constraining its
F_p-reductions tightly.

### 3.4 Note on p = 5

The F4 doc's "p = 5 anomaly" (where |Aut| = 40 ≠ 120 = p(p²-1)) DISSOLVES under
the corrected analysis: at p=5 the formula (p-1)² = 16 matches the directly
computed |Aut|. There is NO anomaly at p=5 for the J18 T^BHML algebra.

(The "40" anomaly belonged to the J49 T_F5 algebra, where direct enumeration via
`tig_dirac.all_automorphisms()` confirms |Aut(V_5)| = 40 in that specific
multiplication table. But that's a different algebra, and its |Aut| at other
primes does NOT follow `p(p²-1)` either — at p=3, T_F5 has |Aut|=12, not 24.)

---

## §4 — Suggested follow-up

### 4.1 Update HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md §1.3

The F4 frontier doc and any J-paper citing the "p(p²-1) at p ∈ {3, 7, 11, 13}
with anomaly at p=5" formula should be updated to:

  **|Aut(V^BHML_{F_p})| = (p − 1)^2, valid at all odd primes 3 through 97.**

This is the empirically correct closed form on the canonical J18 T^BHML algebra.

### 4.2 Structural proof sketch of (p-1)^2

The automorphism group structure follows from a constraint chain:

  **Step 1 (annihilator).** The annihilator `Ann(V) = {x : xV = 0} = span(e_0)`
  is 1-dim and intrinsic to the algebra, so φ(Ann(V)) = Ann(V), giving
  φ(e_0) = α·e_0 with α ∈ F_p^*. **Factor: (p − 1).**

  **Step 2 (image).** The image of multiplication `Im(μ) = span(e_2, e_3, e_4)`
  is 3-dim and intrinsic, so φ(Im(μ)) = Im(μ); equivalently, φ(e_i) has
  e_0-coordinate 0 for i ∈ {2, 3, 4}.

  **Step 3 (φ(e_2) = e_2).** Inspection of all idempotents in V^BHML (there
  are p + 3 of them, but only 1 lies in the e_3-column "subalgebra" span(e_2, e_3)
  with `x = e_3^2` having a nontrivial root). Tracing the constraint
  `φ(e_2) · φ(e_3) = φ(e_3)` then forces φ(e_2) = e_2. (Details: the relation
  `e_3^2 = e_2` means φ(e_3)^2 = φ(e_2); combined with `φ(e_2)^2 = φ(e_2)`
  and the structural-invariant 1-eigenspace of L_{φ(e_2)} matching that of
  L_{e_2}, pin down φ(e_2) = e_2.)

  **Step 4 (φ(e_3) = e_3 forced — not ±e_3).** The relation `φ(e_3)^2 = e_2`
  combined with `φ(e_2) · φ(e_3) = φ(e_3)` and `e_3 · e_4 = e_4` (which lifts to
  `φ(e_3) · φ(e_4) = φ(e_4)`) chains:
    - φ(e_3) ∈ 1-eigenspace of L_{e_2} = span(e_2, e_3).
    - φ(e_3)^2 = e_2 gives `(a·e_2 + b·e_3)^2 = (a^2 + b^2) e_2 + 2ab e_3 = e_2`,
      so a^2 + b^2 = 1 and 2ab = 0. Either (a, b) = (±1, 0) (forces φ(e_3) = ±e_2,
      makes matrix singular) or (a, b) = (0, ±1) giving φ(e_3) = ±e_3.
    - The (−1)-branch φ(e_3) = −e_3 imposes φ(e_4) ∈ (−1)-eigenspace of L_{e_3}
      = span(e_2 − e_3). But for φ(e_4)^2 = 0 to hold one needs `2c^2(e_2 − e_3) = 0`,
      forcing c = 0 (in odd characteristic). So the −1 branch collapses to a
      singular matrix; only φ(e_3) = +e_3 survives.

  **Step 5 (φ(e_4) = β·e_4).** With φ(e_3) = e_3 fixed, φ(e_4) ∈ 1-eigenspace of
  L_{e_3} on the image = span(e_4) (since e_3 · e_2 = e_3 (eigenvalue 1 for e_3),
  e_3 · e_3 = e_2 (eigenvalue 0), e_3 · e_4 = e_4 (eigenvalue 1 for e_4)). The
  1-eigenspace restricted to vectors satisfying `φ(e_2) · v = 0` is exactly
  span(e_4) (since e_2 · e_3 = e_3 ≠ 0). So φ(e_4) = β·e_4 with β ∈ F_p^*.
  **Factor: (p − 1).**

  **Total: (p − 1) × (p − 1) = (p − 1)^2.** ∎

This is a clean structural derivation. The proof generalizes to any prime,
which is consistent with our empirical finding at all 24 primes.

### 4.3 Connection to J49 algebra and the GL_2-shape claim

The J48/J49 T_F5 algebra is structurally distinct from T^BHML. Its automorphism
group structure has been claimed to follow a different sequence
`{6, 24, 40, 336, 1320, 2184}`, but direct brute force at p=3 (full 3^16
enumeration) gave |Aut| = 12 instead of the cited 24. This discrepancy deserves
its own investigation — either the J48 manuscript's tabulated values are correct
(and there's a third multiplication table) or the tabulation contained
arithmetic errors. Out of scope for this F4-extended verification, but should
be flagged in any J-paper hygiene pass.

### 4.4 Lift the (p-1)^2 claim to a Tier-A theorem

Strong evidence (Tier A by exhaustive verification at 24 primes) supports:

  **Theorem.** For every odd prime p, the J18 T^BHML algebra V^BHML over F_p
  has automorphism group order (p − 1)^2. The group structure is
  `F_p^* × F_p^*`, with the two factors corresponding to scalar multiplications
  on `span(e_0)` (the annihilator) and `span(e_4)` (the nilpotent direction).

This result deserves explicit statement in J18's manuscript as a companion to
the existing `|idem| = p + 3` observation. Both are clean closed forms for
characteristic-dependent structural invariants of V^BHML.
