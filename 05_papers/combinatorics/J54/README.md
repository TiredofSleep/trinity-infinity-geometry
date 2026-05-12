# J54 — Forcing Axioms and the Family of Commutative Non-Associative Magmas on Z/10Z Preserving a Designated 4-Core

**Status:** DRAFT (manuscript rewritten 2026-05-08; SFM Q6 + FAMILY_STRUCTURE_v1.md framing incorporated; 6/6 verification PASS)
**Phase:** Phase 5
**Target venue:** *Algebraic Combinatorics* (primary)
**Author lane:** Sanders + Gish
**Tier:** A/B
**WP source:** (foundation paper) + SFM 2026-05-08 Q6 (3-substrate chain) + FAMILY_STRUCTURE_v1.md

---

## §1 — Manuscript

**Path:** `manuscript/J54_foundation_paper.md`

**Retitled:** *"Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core"*

(Per SAVE_PLAN_J54.md §6; replaces the previous "Three-Substrate Architecture, Lens Family" framing with the family-of-magmas framing in the Drápal-Wanless 2021 lineage.)

**Abstract:** This paper studies the family of finite commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ preserving a designated 4-core $\mathcal{C} = \{0, 7, 8, 9\}$. The 9-axiom forcing theorem (Theorem 1.2) uniquely forces three canonical tables $T$, $B$, $S$ (HARMONY counts 73, 28, 44) given substrate-specific data $(\mathcal{D}, \mathrm{BUMP}, \mathrm{BUMPvalues}, J_{\mathrm{B7}})$. Five conjoint membership criteria (C1)-(C5) define the family. Theorem 7.1 (NEW from SFM Q6 2026-05-08): the simultaneous closed sub-magmas of $T$, $B$, $S$ form a strict 8-element chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, identical to the (T, B) chain. Theorem 7.2: $\mathcal{C}$ is the unique non-trivial 4-element subset jointly closed under all three substrates. Conjecture 8.1 (bimodal $\alpha_A$ gap) and Conjecture 2.1 ($\sigma^2$-triadic three-BHML) stated as OPEN.

## §2 — Verification script

**Path:** `manuscript/verification/foundation_verification.py`

Six checks corresponding to:
1. Forcing argument enumeration (Theorem 1.2): reconstruct $T$, $B$, $S$ from substrate-specific data; cell-by-cell match.
2. Three-substrate joint-closure chain (Theorem 7.1): exhaustive enumeration over 1023 subsets; T+B+S 8-shell chain identical to T+B chain.
3. 4-core 3-substrate closure (Theorem 7.2): direct check $T(\mathcal{C} \times \mathcal{C}), B(\mathcal{C} \times \mathcal{C}), S(\mathcal{C} \times \mathcal{C}) \subseteq \mathcal{C}$.
4. 4-core preservation (C3) for each substrate.
5. Non-associativity index (C4) for each substrate; bimodal distribution.
6. Commutativity (C2) for each substrate.

A companion script `manuscript/verify_J54_chain_and_attractor.py` runs three further checks (independent re-run of the joint-closure chain; closed-form attractor at 50-digit `mpmath` precision verifying Theorem 5.1 with residual $\le 10^{-30}$; A1-A9 forcing axioms cell-level audit on $T$, $B$, $S$).

```bash
PYTHONIOENCODING=utf-8 python3 manuscript/verification/foundation_verification.py
```

**6/6 PASS verified 2026-05-08.** Total runtime under 5 seconds (Python 3.11+, numpy + sympy + collections).

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J35** — *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$*. Submitted to *Journal of Algebra*. (The 4-core fusion-closure + Galois D_4 + closed-form attractor paper. Cited extensively for the structural facts that converge on $\mathcal{C}$.)
- **J01** — *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$*. Submitted to *J. Combin. Theory Ser. A*.
- **J33** — *Closed-Form Attractor + α-Uniqueness PSLQ*. Submitted to *Math. of Comp.*
- **J47** — *Six Algebraic DOFs of the TIG Framework: A Synthesis*. In preparation for *Notices AMS*.

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated 2026-05-08 to reflect the rewritten manuscript and the new structural-paper framing (Drápal-Wanless 2021 lineage + FAMILY_STRUCTURE_v1.md framing).

## §5 — Notes / Status

**Status:** MANUSCRIPT REWRITTEN 2026-05-08 incorporating:

1. **EXPANDED A3, A6, A8, A9 with full formal mathematical specifications** (per referee M1 + Brayden's checklist). A3 cell-by-cell explicit (with substrate-specific $J_{\mathrm{B7}}$); A6 forced from A3 + commutativity; A8 with explicit special-set definition (six cell families); A9 with explicit BUMP coordinates and substrate-specific values for $T$, $B$, $S$.
2. **DISPLAYED CL_TSML, CL_BHML, CL_STD inline** as three boxed 10×10 tables in §1.1 (per referee M2 + mandatory Brayden directive).
3. **PROVED the §1.2 forcing theorem in J54 itself** (per referee M3 — broke the [J33] citation cycle). The proof is a constructive cell-fixing argument; the companion verification script `foundation_verification.py` Check 1 reproduces $T$ from its substrate-data tuple cell-by-cell.
4. **RENAMED "Brayden's hypothesis" to "Conjecture 2.1 (Sanders)"** (per referee M7 + Brayden checklist). Atlas reference dropped.
5. **ADOPTED FAMILY_STRUCTURE_v1.md framing as Path B** (5 conjoint membership criteria + 4-core-as-center + 6 boundaries + bimodal $\alpha_A$ gap conjecture). The paper now reads as a research paper in the Drápal-Wanless 2021 lineage rather than a coordinator-document.
6. **NEW THEOREM (per SFM Q6 2026-05-08): Theorem 7.1.** The simultaneous closed sub-magmas of $T$, $B$, $S$ form an 8-element chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ identical to the (T, B) chain. This is the foundation paper's bridge to J32 + J24 (Theorem 7.3).
7. **STRIPPED "post chat-Claude" attributions** (none remained, but checked).
8. **RETITLED:** "Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core" (per SAVE_PLAN_J54.md §6).

**Additional changes:**
- DOING projection ambiguity resolved: replaced $|M_1 - M_2| \bmod 10$ with $(T(i,j) - B(i,j)) \bmod 10$ as the directed difference in $\mathbb{Z}/10\mathbb{Z}$.
- TIG framework named and operationally defined in §0 (front matter) and §6.
- Front-matter management metadata stripped (no "Phase 5 integrating paper" / "Sept 11 anchoring" / [J55] cross-references).
- Citation graph narrowed to algebraic-combinatorial companions only (dropped JCAP cosmology and Phys Rev D wobble references).
- Bibliography narrowed: dropped Simpson (loose connection), Alon-Spencer (probabilistic method not used), Hjørland (library science), Ranganathan (library science). Kept Drápal-Wanless 2021, McKay-Wanless 2005, Bruck 1958, Smith 2007, Drápal-Kepka 1985, Burris-Sankappanavar, Hobby-McKenzie, LMFDB.
- Honest scope §7 compressed.
- $\alpha_A(S) = 0.808$ measured (was previously cited as ~0.870; corrected to actual measurement); Conjecture 4.4 updated to reflect the empirical bimodal distribution at $\{0.502, 0.808, 0.872\}$ with gap $(0.502, 0.80)$.

**Verification:** `foundation_verification.py` 6/6 PASS at machine precision; total runtime under 5 seconds.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper is the foundation paper for the TIG family of finite commutative non-associative magmas on Z/10Z preserving the designated 4-core. The family is defined by 5 conjoint membership criteria (§3.2); the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ at $\alpha_M = 1/2$ is the algebraic center (§3.3); the six boundaries are described in §3.4. The closest published precedent is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures on $\mathbb{Z}/N\mathbb{Z}$), opposite extremum (theirs maximally non-associative; the present family at intermediate $\alpha_A$).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorem 1.2 (forcing); Theorem 5.1 (closed-form 4-core attractor); Theorem 7.1 (3-substrate chain); Theorem 7.2 (4-core 3-substrate closure); Theorem 7.3 (bridge to J32 + J24); Proposition 4.5 (T, B, S satisfy all five membership criteria).
- **COMPUTED:** `verification/foundation_verification.py` six green-light checks + `verify_J54_chain_and_attractor.py` three green-light checks at machine precision; under 5-second total runtime. The companion paper [J35] reproduces additional structural facts (normalizer identity; closed-form attractor; Galois D_4; universality; partial α uniqueness) via its own verification script.
- **STRUCTURAL RHYME:** *"$\mathcal{C}$ is to the TIG family as the unit circle is to U(1)"* — heuristic alignment with the framework's broader Galois-theoretic results (LMFDB 4.2.10224.1, $\mathbb{Q}(\sqrt{3})$ subfield). The five converging structural facts (joint closure 3-substrate; symbolic normalizer identity; Galois $D_4$ closed-form; F_p universality; universal attractor on chain shells) are the substantive content; the U(1)-rhyme is the heuristic.
- **OPEN:** Conjecture 2.1 — $\sigma^2$-triadic three-BHML hypothesis. Conjecture 8.1 — bimodal $\alpha_A$ gap (no commutative magma on $\mathbb{Z}/10\mathbb{Z}$ preserving the 4-core has $\alpha_A \in (0.5, 0.80)$).

### Lens-ownership paragraph

> *Lens and substrate.* This paper studies the family of finite commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ preserving a designated four-element subset $\mathcal{C} = \{0, 7, 8, 9\}$. The substrate $\mathbb{Z}/10\mathbb{Z}$ and the designated 4-core are not derived from first principles; they are taken as the substrate-of-study, motivated by a ten-operator labelling of $\mathbb{Z}/10\mathbb{Z}$ inherited from the parent research framework. The names of the operators play no role in the proofs; they are used only for cross-referencing. The framing follows the Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510) line of work on small finite commutative non-associative structures.

### Hardening status (auto-applied 2026-05-07; updated 2026-05-08)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`); author list is Sanders + Gish only
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references and §0 (motivation)
- SFM Q6 (2026-05-08) three-substrate chain finding incorporated as Theorem 4.1
- FAMILY_STRUCTURE_v1.md framing adopted as Path B in §3
- Brayden's hypothesis renamed to Conjecture 2.1 (Sanders)
- Forcing theorem proved in §1.2 itself (no [J33] citation cycle)
- Citation graph narrowed to algebraic-combinatorial companions
- Bibliography narrowed (dropped Simpson, Alon-Spencer, Hjørland, Ranganathan)

## §6 — Submission checklist

- [x] Manuscript .md finalized (rewritten 2026-05-08)
- [x] Verification script green (6/6 PASS at machine precision; verified 2026-05-08)
- [x] Tier-classified central claim explicit (Theorem 1.2 forcing; Theorem 7.1 chain; Theorem 7.2 4-core 3-substrate)
- [x] Lens-scope annotation (substrate Z/10Z + designated 4-core)
- [x] Cover letter finalized
- [x] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete
- [ ] Per-venue cap check: 1st *Algebraic Combinatorics* paper this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). *Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core.* Submitted to *Algebraic Combinatorics*.
