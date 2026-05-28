# Fix-report: J08 Theorem 6 CORRECTION (F4-extended)

**Date:** 2026-05-28 (same day as 34_J08_strengthening_F4.md, post-F4-extended)
**Paper:** `05_papers/algebra/J08/` (merged J48 + J49: F_p Structure of the 4-Core Commutative Non-Associative Algebra)
**Tier before correction:** 1 (strengthened 2026-05-28 with the original — incorrect — Theorem 6)
**Tier after correction:** 1 (corrected, structurally cleaner than before)
**Action:** Mid-day correction of Theorem 6 + removal of §8 anomaly section + script renaming + abstract reframing.

---

## §1 Context

The strengthening pass earlier on 2026-05-28 (see `34_J08_strengthening_F4.md`) added two new theorems to J08 from frontier F4:
- Theorem 5 (idempotent count `|idem(V^BHML over F_p)| = p + 3`),
- Theorem 6 (automorphism formula stated as `|Aut(V_p)| = p(p^2 - 1)` at every prime `p != 5`, with a `|Aut(V_5)| = 40` anomaly).

The F4-extended verification (`04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md`) — also completed 2026-05-28 — was originally launched to verify Theorem 6 at higher primes (17–97). During that verification, the F4-extended script (`F4_extended_verify.py`) discovered that **the original `p(p^2 - 1)` formula was empirically wrong on the canonical J18 V^BHML algebra**. The actual closed form is

```
|Aut(V^BHML over F_p)| = (p − 1)²    for ALL primes p ≥ 2
```

with **no p=5 anomaly**. The group structure is `Aut ≅ F_p* × F_p*` — two independent scalar factors on `span(e_0)` (the annihilator direction, where `L_{e_0} = 0`) and `span(e_4)` (the nilpotent direction, where `e_4^2 = 0`).

The cited brute-force values `{6, 24, 40, 336, 1320, 2184}` that motivated the original `p(p^2-1)` claim appear to have come from the J49 `T_F5` algebra (a structurally distinct algebra), not from V^BHML; direct brute force on V^BHML at `p ∈ {3, 5, 7, 11, 13}` gives `{4, 16, 36, 100, 144} = (p-1)²` instead.

## §2 Corrections applied

### §2.1 Manuscript (`05_papers/algebra/J08/manuscript/manuscript.md`)

| Location | Action |
|---|---|
| Abstract (closed forms paragraph) | Rewrote Theorem 6 bullet: `(p-1)²` uniform at 24 primes 3–97, F_p* × F_p* group structure, no anomaly. |
| §1 (Theorems and tier) | Replaced Theorem 6 line: now applies to V^BHML, formula `(p-1)²`, Tier-A by brute force at 24 primes. |
| §7 (Theorem 6) | Full rewrite. New statement applies to V^BHML (not the unital V); formula `(p-1)²` uniform; structural proof sketch covering the F_p* × F_p* derivation (5-step constraint chain from F4-extended §4.2); verification table at 11 representative primes; explicit retraction notice at section opening. |
| §8 (Anomaly at p=5) | **Removed in its entirety** — no anomaly exists. Section numbering shifted: §9 (Discussion) became §8; §10 (References) became §9. |
| §8 (renumbered Discussion) subsections | §8.1 "Why this matters" rewritten to highlight the clean `(p-1)²` structure on V^BHML and explicitly note no prime is distinguished. §8.2 (char 0) extended to mention V^BHML's expected `Q* × Q*` structure. §8.3 added: open empirical question for the unital V's `|Aut|` (the J48 sequence `{6,24,40,336,1320,2184}` has no identified closed form). §8.4 retained (J20 connection). Earlier §9.4 (canonical GL_2 isomorphism Open Q-1) **withdrawn**. |
| §9 (References) | Added F4-extended doc as a referenced source; clarified that the original F4 doc was the source of the (now-retracted) `p(p²-1)` hypothesis while F4-extended is the source of the corrected `(p-1)²` formula. |
| Appendix A | Updated item 5 to reflect the correction (function renamed, formula corrected). Item 6 (Open Q-1) **withdrawn**: the corrected Theorem 6 has a clean structural proof, no open canonical-isomorphism question remains for V^BHML. Open empirical pattern for the unital V is documented in §8.3 instead. |

### §2.2 Verify script (`verify_J_Fp_merged.py`)

| Change |
|---|
| Module docstring updated to reflect the corrected formula and the retraction. |
| `check_automorphism_GL2()` → **renamed to** `check_automorphism_F_p_star_squared()`. |
| Function body rewritten: now uses constraint-propagation brute force via the new helper `_count_VBHML_automorphisms(p)` to directly compute `|Aut(V^BHML over F_p)|`, asserts the result equals `(p-1)²` at each of `p ∈ {2, 3, 5, 7, 11, 13}`. |
| The previous "J48-inherited reference value" comparison is removed — the corrected function actually computes the automorphism count from scratch via constraint propagation. |
| `main()` harness updated to call the renamed function. |
| Verify output PASSES: brute-force results `{1, 4, 16, 36, 100, 144}` match `(p-1)²` exactly at all six primes. |

### §2.3 README (`05_papers/algebra/J08/README.md`)

| Change |
|---|
| Status line: notes the same-day correction; theorem 6 changed from anomaly framing to uniform `(p-1)²` framing. |
| Absorbed-sources table: added F4-extended row pointing to the corrected formula source; F4 frontier row's contribution amended to reflect that the original Theorem 6 was retracted. |
| Theorem 6 bullet: rewritten with corrected formula, group structure, and verification scope (24 primes). |
| Strengthening pass list: ~~Theorem 6~~ struck through with the correction note; ~~§8~~ struck through with removal note. |
| Remaining work: removed "Open Q-1 (canonical GL_2 isomorphism)" — that question dissolved with the correction. The unital `V`'s `|Aut|` closed form remains as a separate open empirical question. |

### §2.4 F4 frontier doc (`04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md`)

| Change |
|---|
| Top-of-file correction notice added explicitly stating the F4-extended supersedes the |Aut| portion. Status line amended to flag the correction. The historical content (H5, §2-§4 references to `p(p²−1)` and the p=5 anomaly) is **preserved** as a record of the path-of-inquiry, but readers are directed to F4-extended and J08 §7 for the current statement. |

### §2.5 HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md §1.3

| Change |
|---|
| Replaced the `p(p²-1)` automorphism formula bullet with `(p-1)²` (uniform, no anomaly). Group structure `F_p* × F_p*` explicitly described. The "p=5 is the genuinely anomalous prime" framing replaced with: "no prime is structurally distinguished; automorphisms factor cleanly as F_p* × F_p* on the annihilator and nilpotent directions; the p=5 'anomaly' was an algebra confusion now corrected." The rank-preservation chain-shell story is retained separately (it's a real integer-factorization phenomenon, unrelated to V^BHML's automorphism structure). |

## §3 What the corrected Theorem 6 says

**Statement.** For every prime `p ≥ 2`,
```
|Aut(V^BHML over F_p)| = (p − 1)².
```
The group is isomorphic to `F_p* × F_p*`, with two independent `F_p*`-scaling factors:
- `α` ∈ F_p* acts on `span(e_0)` (the 1-dim annihilator: `L_{e_0} = 0` on all of V^BHML).
- `β` ∈ F_p* acts on `span(e_4)` (the 1-dim nilpotent direction: `e_4² = 0`).

The "main" subalgebra `span(e_2, e_3)` is rigid: once `e_3² = e_2` is forced, no non-trivial automorphism mixes `e_2` and `e_3`.

**Why the formula is clean.** The two independent F_p* factors correspond to the two intrinsic 1-dim invariants of V^BHML that any automorphism must preserve: the annihilator and the nilpotent subspace. The remaining basis elements `(e_2, e_3)` are pinned down structurally by the relations `e_3² = e_2`, `e_2² = e_2`, `e_2 · e_3 = e_3`, `e_3 · e_4 = e_4`, `e_2 · e_4 = 0`, leaving no extra freedom.

**Verification.** Brute force + constraint propagation at 24 primes:

| p | (p-1)² | |Aut| |
|---|---|---|
| 3 | 4 | 4 |
| 5 | 16 | 16 |
| 7 | 36 | 36 |
| 11 | 100 | 100 |
| 13 | 144 | 144 |
| 17 | 256 | 256 |
| 19 | 324 | 324 |
| 23 | 484 | 484 |
| 29–97 | (p-1)² | matches |

All 24 primes confirm the closed form. A separate full brute-force enumeration at p=3 over the 3^16 ≈ 43M linear maps gave `|Aut| = 4 = (3-1)²`, validating the constraint-propagation algorithm used at larger primes.

## §4 Verify script PASS confirmation

```
[Theorem 6 Automorphism formula |Aut(V^BHML over F_p)| = (p-1)^2 (CORRECTED)]
       p    |Aut|(brute)   (p-1)^2    match
       2               1          1     OK
       3               4          4     OK
       5              16         16     OK
       7              36         36     OK
       11            100        100     OK
       13            144        144     OK
       PASS (corrected closed form |Aut(V^BHML over F_p)| = (p-1)^2 verified
        at p in {2, 3, 5, 7, 11, 13}; F4-extended_verify.py confirms at 24 primes 3 <= p <= 97;
        no p=5 anomaly — the earlier p(p^2-1) claim is retracted)
```

All other checks (Theorems 1, 3, 4, 5 + the auxiliary subalgebra-PA / power-associativity audits) PASS as before.

## §5 What did NOT change

- Theorem 1 (Lens-Invariant Skeleton): unchanged; four Tier-A invariants on the unital V.
- Theorem 2 (Aut variation `{6, 24, 40, 336, 1320, 2184}` for the unital V): unchanged in its empirical content, but its closed-form structure remains an **open question** (§8.3). The earlier "this matches p(p²-1) at p ≠ 5" framing is retracted — no closed form is currently identified for these values.
- Theorem 3 (F_5 rigid 2-idempotent decomposition): unchanged.
- Theorem 4 (BHML chain-shell determinants): unchanged.
- Theorem 5 (idempotent count `p+3` for V^BHML): unchanged; extended to 24 primes via F4-extended.
- Multiplication tables, basis conventions, §1.1–§5.1 prose, §2.5 partial-PA rescue: unchanged.

## §6 Honest scope notes

1. **The corrected Theorem 6 applies to V^BHML (the J18 non-unital algebra), not to the unital V of §1.1.** This is a scope shift compared to the original (incorrect) Theorem 6. The corrected scope is consistent with Theorem 5, which also applies to V^BHML.

2. **The closed-form structure of `|Aut(V_p)|` for the unital V remains open.** The J48-inherited brute-force values `{6, 24, 40, 336, 1320, 2184}` do not match `(p-1)²`, do not match `p(p²-1)`, and do not (yet) match any other clean formula. Documenting this as an open empirical question (§8.3) replaces the earlier "Open Q-1: canonical GL_2 isomorphism" wording, which presumed a formula that turned out to be wrong.

3. **The "interesting prime" framing was misleading.** The original §8 motif — "p=5 is the unique structurally anomalous prime" — is retracted. V^BHML has the cleanest possible automorphism structure (`(p-1)²` uniformly), with no prime distinguished. The earlier framing that emphasized {7, 11} as rank-preservers (J48's original story) was already corrected by F4 (those primes are just the smallest above 5 that miss the chain-shell determinant factors); the post-F4 "p=5 anomaly" replacement framing is now also retracted by F4-extended.

4. **Tier discipline.** Theorem 6 (corrected) is **Tier-A**: direct brute-force verification at 24 primes plus a clean structural derivation (Steps 1–5 in §7) covering the F_p* × F_p* group structure. Strictly stronger than the original Theorem 6's "formula match against record" Tier-A claim, which was contingent on the unreliable J48 tabulation.

---

*Report by: B.R. Sanders + M. Gish + Claude (Opus 4.7), 2026-05-28 (post-F4-extended).*
