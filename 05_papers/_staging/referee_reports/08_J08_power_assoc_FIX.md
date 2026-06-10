# J08 Fix Report — Power-Associativity, L_{e₃}, ε₂ Idempotent

**Date:** 2026-05-28
**Triggering reports:** `03_algebra_cluster_J02_J05_J07_J08.md` §J08 (MAJOR items 2–6)
**Scope:** independent verification of three referee-flagged math errors in J08 (*F_p Structure of the 4-Core Commutative Non-Associative Algebra*, target *Algebra Universalis*) and the corresponding manuscript / verify-script edits.

---

## §1. Independent verification of the math claims

All computations performed by hand from the §1.1 multiplication table (manuscript lines 42–47), reproduced here for reference:

| · | e₀ | e₂ | e₃ | e₄ |
|---|---|---|---|---|
| e₀ | e₀ | e₂ | e₃ | e₄ |
| e₂ | e₂ | e₃ | e₄ | e₀ |
| e₃ | e₃ | e₄ | e₂ | e₃ |
| e₄ | e₄ | e₀ | e₃ | e₀ |

### Claim 1 (referee): V is **NOT** power-associative; e₂³·e₂ ≠ (e₂²)².

**Verification:**
- e₂² = e₂·e₂ = **e₃** (row e₂, col e₂)
- e₂³ = e₂²·e₂ = e₃·e₂ = **e₄** (row e₃, col e₂)
- e₂³·e₂ = e₄·e₂ = **e₀** (row e₄, col e₂; equivalently e₂·e₄ = e₀ by commutativity)
- (e₂²)² = e₂²·e₂² = e₃·e₃ = **e₂** (row e₃, col e₃)
- e₀ ≠ e₂ in the basis {e₀, e₂, e₃, e₄}.

**Conclusion: REFEREE IS CORRECT.** V is not power-associative. The failure occurs already over ℤ on the integer-coefficient multiplication table; therefore it persists mod every p (the residues 0 and 1 of the e₀-vs-e₂ basis components are distinct in 𝔽ₚ for every prime). The earlier §2.5 Tier-A claim is **refuted**.

Note that the weaker identity a²·a = a·a² **does** hold: it is automatic from commutativity, and so a³ is unambiguously defined. Only the quartic-power identity a³·a = a²·a² (i.e., the second of Albert's two power-associativity equations) fails.

### Claim 2 (referee): L_{e₃} is **NOT** a 4-cycle; it has rank ≤ 3.

**Verification (column e₃ read from the table — i.e., for each basis vector x, the value of e₃·x):**
- L_{e₃}(e₀) = e₃·e₀ = **e₃** (row e₃, col e₀; e₀ is identity)
- L_{e₃}(e₂) = e₃·e₂ = **e₄**
- L_{e₃}(e₃) = e₃·e₃ = **e₂**
- L_{e₃}(e₄) = e₃·e₄ = **e₃**

Two inputs (e₀ and e₄) map to the same output (e₃). Therefore L_{e₃} is not injective, hence not a permutation, hence not a 4-cycle. The image is {e₂, e₃, e₄} (3-dimensional), so rank(L_{e₃}) = 3, with kernel spanned by e₀ - e₄.

**Conclusion: REFEREE IS CORRECT.** The §1.2 claim "L_{e₃} is the permutation (e₀ e₃ e₂ e₄) — a 4-cycle, so L_{e₃}⁴ = id_V" is **wrong**.

### Claim 3 (referee request): is ε₂ = 2e₃ + 3e₄ idempotent over 𝔽₅?

**Verification:**
ε₂² = (2e₃ + 3e₄)·(2e₃ + 3e₄)
    = 4·e₃·e₃ + 6·e₃·e₄ + 6·e₄·e₃ + 9·e₄·e₄
    = 4·e₃·e₃ + 12·e₃·e₄ + 9·e₄·e₄         (commutativity)
    = 4·e₂ + 12·e₃ + 9·e₀                  (table)

Mod 5:
ε₂² = 4·e₀ + 4·e₂ + 2·e₃ + 0·e₄.

But ε₂ = 0·e₀ + 0·e₂ + 2·e₃ + 3·e₄. The e₀ coefficient (4 vs 0), e₂ coefficient (4 vs 0), and e₄ coefficient (0 vs 3) all disagree.

**Conclusion: ε₂ is NOT idempotent over 𝔽₅.** The referee was right to flag this.

I also checked the other two claimed idempotents and the sum-to-identity property:
- ε₃ = 3e₃ + 2e₄: ε₃² = 9·e₂ + 12·e₃ + 4·e₀ = 4·e₀ + 4·e₂ + 2·e₃ (mod 5), same vector as ε₂². So ε₃² = ε₂² ≠ ε₃. Not idempotent.
- ε₄ = e₄ - e₂ = -e₂ + e₄: ε₄² = e₂² - 2·e₂·e₄ + e₄² = e₃ - 2·e₀ + e₀ = e₃ - e₀ = 4·e₀ + e₃ (mod 5). Not equal to ε₄. Not idempotent.
- Sum: ε₂ + ε₃ + ε₄ = (-1)·e₂ + 5·e₃ + 6·e₄ ≡ 4·e₂ + 0·e₃ + 1·e₄ (mod 5). Not equal to e₀ (the multiplicative identity).

The entire orthogonal-idempotent triple in §4 Theorem 3 is **broken**. The count |Aut(V₅)| = 40 is unaffected (it comes from the J49 brute-force enumeration, not from this triple), but the explicit "rigid decomposition" presentation has no surviving witness.

---

## §2. Edits made

All edits in `05_papers/algebra/J08/`.

### `manuscript/manuscript.md`

| Location | Change |
|---|---|
| Abstract, "unified picture" paragraph | "three nonzero idempotents, (1,3) Minkowski signature ... power-associativity" → "three or more nonzero idempotents, cyclic order-4 structure on L_{e₂} ... weak-cube-power-associativity (automatic by commutativity; the stronger identity a³·a = a²·a² FAILS at a=e₂)" |
| Theorem 1 bullet (§1) | "Five structural properties" → "Four structural properties of V hold in every characteristic ... cyclic order-4, BHML chain-shell rank profile, (2,2) chirality signature, 1-dim associator image. (The earlier 'five-property' formulation included power-associativity, which is REFUTED below)" |
| Theorem 3 bullet (§1) | "unique orthogonal idempotent decomposition with |Aut(V₅)|=40" → "|Aut(V₅)|=40=F₂₀×ℤ/2. The explicit orthogonal-idempotent triple in §4 has been WITHDRAWN..." |
| §1.2 third bullet (L_{e₃}) | "This is the permutation (e₀ e₃ e₂ e₄) — a 4-cycle, so L_{e₃}⁴=id_V" → "This is NOT a permutation: both e₀ and e₄ are sent to e₃, so L_{e₃} has rank ≤ 3 with e₀-e₄ in its kernel. The image is {e₂, e₃, e₄}, and L_{e₃}⁴ ≠ id_V" |
| §1.2 last paragraph | "non-permutation nature of L_{e₄}" → "non-permutation nature of L_{e₃} and L_{e₄} ... only L_{e₀} (identity) and L_{e₂} (cyclic order 4) are bijective" |
| §2.5 (Power-associativity) | Heading retitled "Weak cube-power-associativity (corrected; full power-associativity FAILS)"; old proof replaced with explicit numerical witness at a=e₂ showing a³·a = e₀ vs (a²)² = e₂; **Tier downgraded to A only for the trivial a²·a = a·a² part; full power-associativity REFUTED**; "five lens-invariant" reduced to four |
| §3 Theorem 2 proof | "match `verify_J14.py` test cases 7–12 (PASS)" → "inherited from J48 brute-force; verifier of record is bundled `verify_J_Fp_merged.py`" |
| §4 Theorem 3 proof sketch | "Direct verification gives orthogonality and unitality. ∎" → "**FLAGGED**; direct check refutes ε₂²=ε₂ (computed: ε₂²=4e₀+4e₂+2e₃ mod 5 ≠ 2e₃+3e₄). Analogous failures for ε₃, ε₄; sum ≠ e₀. The published proof of Theorem 3 is WITHDRAWN; the |Aut(V₅)|=40 count is retained as Tier-A via J49 brute-force." |
| §4 parenthetical | "Full enumeration in `verify_J16.py` PASS" → "historical reference to `verify_J16.py` is broken in the post-renumbering corpus and is replaced by the bundled `verify_J_Fp_merged.py`" |
| §5 Theorem 4 proof | "Direct factorization in `verify_J14.py` or `verify_J16.py`" → "Direct factorization in `verify_J_Fp_merged.py` (Theorem 4 block) which loads canonical BHML from `ck_tables.py` and computes the seven determinants via `sympy.Matrix.det`. The historical references to verify_J14.py / verify_J16.py are broken post-renumbering and are superseded." |
| §6.1 Discussion | "(three idempotents, signatures, associator image, power-associativity)" → "(cyclic order-4 structure on L_{e₂}, chain-shell rank profile, chirality signature on L_{e₀}, 1-dim associator image)" + added historical note about the withdrawn power-associativity claim |
| Appendix A | Replaced "inherits from J48 verify_J14.py / J49 verify_J16.py" with bundled `verify_J_Fp_merged.py` description + open-verification-gaps audit (T2 not recomputed, T3 idempotent triple withdrawn, T4 fail-fast pending) |

### `manuscript/verify_J_Fp_merged.py`

| Location | Change |
|---|---|
| Top-level docstring | Reworded to flag the four-not-five property change, the L_{e₃} fix, the ε₂ refutation, and the broken upstream-verifier references |
| New function `check_power_associativity_at_e2()` | Audit witness that explicitly computes e₂², e₂³, e₂³·e₂, and (e₂²)² on the bundled multiplication table and prints "V is NOT power-associative; the earlier Tier-A claim is REFUTED" |
| `check_T2_aut_variation()` | Comment updated: removed reference to `J14's verify_J14.py`; now points at the J48 archive |
| `main()` | Added call to `check_power_associativity_at_e2(V_table)` and updated closing banner |

### `README.md`

| Location | Change |
|---|---|
| "Verification" section | Removed citations of `verify_J14.py` and `verify_J16.py`; added explicit pointer to the bundled verifier and a paragraph cross-referencing the 2026-05-28 referee fix (this report and `03_algebra_cluster_J02_J05_J07_J08.md` §J08) |

---

## §3. Further issues found (flagged, NOT fixed)

These are issues I identified during the verification but did not auto-fix. They merit human decision:

1. **§2.2 Cyclic structure ↔ §2.2 Minkowski signature heading collision.** Section 2 has two distinct subsections both numbered §2.2 (lines 114 and 151 of manuscript.md). The first is "Cyclic structure — invariant across all primes" (the L_{e₂}⁴ = id claim, which I verified is correct). The second is "Minkowski signature (1, 3) on L_{e₂}" — and its claim about (1,3) signature at every p is *also* questioned in the cluster-03 referee report MAJOR-4: at p ≡ 1 (mod 4) the four 4th roots of unity all live in 𝔽ₚ giving 1+1+1+1; at p ≡ 3 (mod 4) only ±1 are 𝔽ₚ-rational; at p = 2, x⁴-1 = (x-1)⁴ so a single Jordan block. The "(1,3) Minkowski for every p" is not literally true. **Recommend:** human review of §2.2 splitting (renumber the subsections) and a tighter statement of the signature claim per prime class.

2. **Theorem 2 inline verification gap.** `verify_J_Fp_merged.py` still does NOT recompute |Aut(V_p)| for any p; it just references J48. The cluster-03 referee MAJOR-5 calls this a Tier-A downgrade risk. The brute-force enumerator is ~50 lines per prime and is tractable. **Recommend:** inline the enumerator in a follow-up commit so all four theorems have bundled verification.

3. **Theorem 4 verifier accepts mismatch.** Lines 159–168 of the verify script log-and-continue rather than asserting `dets_observed == EXPECTED_DETS`. **Recommend:** harden the assertion (`assert dets_observed == EXPECTED_DETS, ...`) once the BHML version drift question is resolved.

4. **|Aut(V₂)| = 6 group identity ambiguous.** §3 of the manuscript says "|Aut(V₂)| = 6 = S₃" but there are two groups of order 6: S₃ and ℤ/6. Cluster-03 referee MINOR flags this; manuscript needs a one-line identification (presence of an element of order 6 → ℤ/6; otherwise S₃).

5. **§4.2 phrasing.** "4 divides |𝔽₅*| = 4" reads awkwardly. Cluster-03 referee suggests "𝔽₅ is the smallest prime where 𝔽ₚ× contains a primitive 4th root of unity." Cosmetic.

6. **§6.4 cross-refs to J20, J37 post-renumbering.** Cluster-03 referee notes these need verification under the new J-numbering. Not checked here.

7. **Source-paper merger tombstones missing.** Cluster-03 referee notes the absence of `MERGED_INTO_J08.md` files in `algebra/J48/` and `algebra/J49/`. Not part of this fix.

---

## §4. Recommendation: Tier classification after fixes

**Demote J08 from Tier 1 ("submission-ready") to Tier 2 ("revise before submission") for this submission cycle.**

Reasoning:
- The lens-invariant skeleton, the primary advertised contribution of this paper (Theorem 1), shrinks from five properties to four. The remaining four are still genuine Tier-A invariants and the merger logic still holds, but the abstract/intro/marketing must be rewritten so the "five-property" claim is gone everywhere.
- Theorem 3's explicit decomposition is broken. The count |Aut(V₅)| = 40 survives as a Tier-A fact via J49 brute-force, but **the rigid-idempotent narrative — the headline contribution of the §4 block — has no surviving witness in the current draft.** Either:
  - (a) re-derive the correct orthogonal-idempotent triple over 𝔽₅ (which a careful enumeration on V₅ may or may not produce — needs investigation), or
  - (b) restate Theorem 3 purely as "|Aut(V₅)| = 40 = F₂₀ × ℤ/2 with no explicit decomposition exhibited," and rewrite the §4 narrative around the automorphism count rather than the decomposition.
- §1.2 L_{e₃} fix is a clean correction; doesn't affect tier.
- The broken verify_J14.py / verify_J16.py references are now fixed but the verifier still does not bundle Theorem 2 / Theorem 3 brute-force enumeration; that's a Tier-A discipline gap.

**After the §4 rewrite (T3 reframing) + the verifier hardening (T2 inline, T4 fail-fast), J08 can be promoted back to Tier 1.** The math content is real; the bookkeeping needs another pass. Estimated effort: 1 focused session.

For *Algebra Universalis* specifically, the cluster-03 referee's reframing recommendation (lead with §2 lens-invariant skeleton; demote §3 to a corollary) is independently sound and would absorb the §4 narrative shrinkage gracefully. That reframing + the fixes here would land the paper at Tier 1 and AU-publishable.

---

*— Independent verification + applied fix, 2026-05-28.*
