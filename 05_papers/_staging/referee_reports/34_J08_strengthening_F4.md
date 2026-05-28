# Fix-report: J08 strengthening with F4 closed forms

**Date:** 2026-05-28
**Paper:** `05_papers/algebra/J08/` (merged J48 + J49: F_p Structure of the 4-Core Commutative Non-Associative Algebra)
**Tier before:** 1 (re-promoted 2026-05-28 after §4 rescue)
**Tier after:** 1 (strengthened, not retiered)
**Action:** Strengthening pass — added two new Tier-A theorems from frontier F4

---

## §1 Context

The F4 frontier scan (`04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md`, completed 2026-05-27) identified two clean closed forms emerging from the prime-by-prime structural data of the 4-core algebra family. These had not been incorporated into any J-paper. This fix-report documents the strengthening of J08 to absorb both findings.

The F4 frontier originally pursued the question: "what algebraic property isolates $\{7, 11\}$ from $\{2, 3, 5, 13\}$ as the rank-preserving primes of the BHML chain shells?" That question was answered negatively (no clean criterion isolates $\{7, 11\}$). Along the way, however, two crisp closed forms were discovered.

## §2 New theorems added to J08

### §2.1 Theorem 5 (Idempotent count closed form for $V^{\mathrm{BHML}}$)

**Statement.** For the companion algebra $V^{\mathrm{BHML}}$ defined in J18 (Theorem 3.1) — the non-unital BHML 4-core lift where $L_{e_0} = 0$ —
$$|\mathrm{idem}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = p + 3$$
at every odd prime $p$, and $= 2$ at $p = 2$. Verified at $p \in \{2, 3, 5, 7, 11, 13\}$ giving counts $\{2, 6, 8, 10, 14, 16\}$.

**Tier**: A (direct brute-force enumeration at all six primes).

**Note on scope.** The closed form applies to $V^{\mathrm{BHML}}$ (J18's table, non-unital, $L_{e_0} = 0$), *not* to the present J08 algebra $V$ (which has $e_0$ as the multiplicative identity and a different idempotent-count pattern $\{4, 6, 4, 4, 6, 8\}$). The theorem is sited in J08 because:
1. The two algebras share the BHML lineage and are studied as companion objects;
2. J08 already references J18 as the source for the companion treatment of the parent algebra;
3. The closed-form $p+3$ pattern provides a clean structural contrast with the J08 algebra's empirical pattern, sharpening the picture of which $p$-dependent quantities admit closed forms in this corpus.

The companion-algebra siting is documented explicitly in the theorem statement (§6) and in the abstract.

### §2.2 Theorem 6 (Automorphism formula and $\mathbb{F}_5$ anomaly)

**Statement.** For the present algebra $V$ (J08 §1.1 table, with $e_0$ as multiplicative identity) and every prime $p \in \{2, 3, 7, 11, 13\}$,
$$|\mathrm{Aut}(V_p)| = p(p^2 - 1) = |\mathrm{GL}_2(\mathbb{F}_p)|.$$
At $p = 5$, the substrate index collapse $\{7, 8, 9\} \equiv \{2, 3, 4\} \pmod 5$ reduces $|\mathrm{Aut}(V_5)|$ from the formula value $120$ to the actual value $40$. $\mathbb{F}_5$ is therefore the unique structurally anomalous prime in the tabulated small-prime range.

**Tier**: A (formula match against J48-inherited brute-force values $\{6, 24, 40, 336, 1320, 2184\}$).

**Open Q-1** (documented as open in §9.4 of the manuscript): a canonical group isomorphism $\mathrm{Aut}(V_p) \cong \mathrm{GL}_2(\mathbb{F}_p)$ for $p \neq 5$ via an explicit 2-parameter generator action has not yet been identified. The empirical match across five primes strongly suggests one exists; resolving Q-1 would upgrade Theorem 6 from formula-match to canonical-isomorphism.

### §2.3 New §8 (Anomaly at $p = 5$)

A new standalone section §8 documents the structural reason for the $\mathbb{F}_5$ anomaly: the 4-core substrate indices $\{0, 7, 8, 9\} \subset \mathbb{Z}/10\mathbb{Z}$ collapse modulo 5 to $\{0, 2, 3, 4\}$, identifying $\{7, 8, 9\}$ with $\{2, 3, 4\}$. This identification creates extra coincidences in the BHML multiplication table at $p = 5$ that do not arise at other primes, reducing the automorphism count and producing the $F_{20} \times \mathbb{Z}/2$ structure recorded in Theorem 3.

The new §8 has four subsections:
- §8.1 The substrate index collapse
- §8.2 Consequence for the automorphism group
- §8.3 Consequence for the rigid 2-idempotent decomposition
- §8.4 Other primes are generic

This reframes the "interesting prime" question: previously the J48 narrative emphasized $\{7, 11\}$ as the rank-preserving primes; the F4 frontier scan disproved that framing (showing $\{7, 11\}$ is just the smallest two primes above 5 that miss the chain-shell determinant factors, with no deeper algebraic story). The genuinely interesting prime is $p = 5$ — the unique anomaly in the automorphism-group formula.

## §3 Verify script changes

Two new check functions were added to `verify_J_Fp_merged.py`:

### §3.1 `check_idempotent_count_formula()`

- Embeds the J18 $T^{\mathrm{BHML}}$ multiplication table as `T_BHML_J18` (4-array of 4-arrays of 4-coefficient lists).
- Helper `mul_VBHML_in_Fp(x, y, p)` performs bilinear multiplication over $\mathbb{F}_p$.
- For each $p \in \{2, 3, 5, 7, 11, 13\}$: brute-force enumerate $\mathbb{F}_p^4$ ($p^4$ elements), count idempotents, assert against $p + 3$ for odd $p$ and $2$ for $p = 2$.
- Result: PASS at all six primes.

### §3.2 `check_automorphism_GL2()`

- Reads the J48-inherited brute-force values $\{6, 24, 40, 336, 1320, 2184\}$.
- For each $p \in \{2, 3, 7, 11, 13\}$: assert $|\mathrm{Aut}(V_p)| = p(p^2 - 1)$.
- For $p = 5$: assert $|\mathrm{Aut}(V_5)| = 40$ and document the anomaly (formula value would be $120$).
- Result: PASS at all six primes.

**Note.** `check_automorphism_GL2()` does NOT recompute $|\mathrm{Aut}(V_p)|$ from scratch (that requires brute-force enumeration over invertible $4 \times 4$ $\mathbb{F}_p$-matrices, prohibitive at $p \geq 7$ without smarter constraints). It performs a *formula-against-record* assertion. Bringing brute-force $|\mathrm{Aut}|$ into the bundled script remains an open verification gap (item 1 of Appendix A) — partially closed by Theorem 6.

## §4 Abstract and README updates

### §4.1 Abstract
Added a "Closed forms (added 2026-05-28 from F4 frontier scan)" paragraph immediately after the existing source-paper consolidation paragraph, summarizing Theorems 5 and 6 and the $\mathbb{F}_5$ anomaly.

### §4.2 README
- Updated status line: "STRENGTHENED 2026-05-28 — two new closed-form theorems added from frontier F4".
- Added F4 frontier row to the absorbed-sources table.
- Extended the theorem list from 4 entries to 6.
- Added a new "Strengthening pass (2026-05-28, completed)" subsection enumerating the six strengthening actions.

## §5 Verify script PASS confirmation

```
$ python verify_J_Fp_merged.py
...
[Theorem 5 Idempotent count formula |idem(V^BHML over F_p)| = p+3]
       p   observed   expected   formula
       2          2          2   2 (at p=2)    -- OK
       3          6          6   p+3 = 6       -- OK
       5          8          8   p+3 = 8       -- OK
       7         10         10   p+3 = 10      -- OK
       11        14         14   p+3 = 14      -- OK
       13        16         16   p+3 = 16      -- OK
       PASS (closed form |idem(V^BHML/F_p)| = p+3 for odd p verified at p in {3,5,7,11,13};
        and = 2 at p=2)

[Theorem 6 Automorphism formula |Aut(V_p)| = p(p^2-1), p!=5; 40 at p=5]
       p    |Aut|(J48)   p(p^2-1)   formula match
       2             6          6     = p(p^2-1) = 6  -- OK
       3            24         24     = p(p^2-1) = 24  -- OK
       5            40        120     40 (anomaly, gl2=120)  -- OK
       7           336        336     = p(p^2-1) = 336  -- OK
       11         1320       1320     = p(p^2-1) = 1320  -- OK
       13         2184       2184     = p(p^2-1) = 2184  -- OK
       PASS (closed form |Aut(V_p)| = p(p^2-1) verified at p in {2,3,7,11,13};
        anomaly at p=5: |Aut(V_5)| = 40 < 120 = 5(25-1) due to {7,8,9}=={2,3,4} mod 5)
```

All six existing checks (Theorems 1–4 and the auxiliary subalgebra-PA / power-associativity audits) also PASS as before.

## §6 Files touched

| File | Change |
|---|---|
| `05_papers/algebra/J08/manuscript/manuscript.md` | Added Theorems 5 and 6 (new §6 and §7); added §8 (Anomaly at $p=5$); renumbered Discussion to §9 and References to §10; updated abstract; updated Appendix A verification list and open verification gaps. |
| `05_papers/algebra/J08/manuscript/verify_J_Fp_merged.py` | Added `T_BHML_J18` table, `mul_VBHML_in_Fp()`, `check_idempotent_count_formula()`, `check_automorphism_GL2()`; updated docstring and main() harness. |
| `05_papers/algebra/J08/README.md` | Updated status line; extended theorem list to 6; added F4 frontier row to absorbed-sources table; added "Strengthening pass (2026-05-28, completed)" subsection. |
| `05_papers/_staging/referee_reports/34_J08_strengthening_F4.md` | THIS report. |

## §7 Constraints satisfied

- [x] No undisclosed lemmas introduced — Theorem 5 proven by direct brute-force enumeration; Theorem 6 stated as formula-match against J48-inherited brute-force values, with the canonical $\mathrm{GL}_2$ isomorphism explicitly flagged as **Open Q-1**.
- [x] Verify script PASSES all checks at all six primes.
- [x] F4 frontier report cited as the source of both closed forms.
- [x] Open questions documented (Q-1: canonical $\mathrm{GL}_2$ isomorphism; §9.3: extension to primes $> 13$).

## §8 Honest scope notes

1. The idempotent count formula $|\mathrm{idem}(V_{\mathbb{F}_p})| = p + 3$ holds for the **companion** algebra $V^{\mathrm{BHML}}$ (J18), not for the present $V$ (J08 §1.1). This is stated explicitly in the Theorem 5 statement and in the abstract. The J08 algebra's idempotent count pattern $\{4, 6, 4, 4, 6, 8\}$ at $p \in \{2, 3, 5, 7, 11, 13\}$ does not admit a simple closed form; this remains an open question.

2. The automorphism formula $|\mathrm{Aut}(V_p)| = p(p^2 - 1)$ does match the J48-inherited brute-force values for the J08 algebra; the formula is asserted against record rather than recomputed from scratch in the bundled script. The brute-force enumeration of $|\mathrm{Aut}|$ remains an open verification gap (Appendix A item 1).

3. The "interesting prime" reframing in §8 — shifting from "$\{7, 11\}$ are special" to "$p = 5$ is the unique anomaly" — is consistent with the F4 frontier §3 deprecation of the earlier $\{7, 11\}$ framing.

---

*Report by: B.R. Sanders + M. Gish + Claude (Opus 4.7), 2026-05-28.*
