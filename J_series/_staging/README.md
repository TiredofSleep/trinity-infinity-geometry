# J-series — Staging

Papers in queue: not yet here, not yet referee-ready, but explicitly being prepared for the next handoff. This is the "what's gating the next landing" tracker.

When a paper here completes the §4 criteria from `../README.md`, it moves out of `_staging/` and into the appropriate domain folder.

---

## §1 — Active gating items

(Most-recent first.)

### Corpus centerpiece pair — BOTH LANDED 2026-05-12

- **J35** (Four-Core Fusion-Closure, *Journal of Algebra*) — **LANDED 2026-05-12 at [`../algebra/J35/`](../algebra/J35/).** 6/6 PASS at machine precision; referee-grade pass complete; CC-BY-4.0 verification script header; honest-negatives discipline on T*=5/7 and bounded F_p scan.
- **J54** (Foundation Paper, *Algebraic Combinatorics*) — **LANDED 2026-05-12 at [`../combinatorics/J54/`](../combinatorics/J54/).** 6/6 + 3/3 PASS at machine precision; A1–A9 axioms cell-by-cell explicit; three substrate tables displayed inline; forcing theorem proved in §1.3 (breaks the J33 citation cycle by stating its own foundations); referee-grade pass complete (theorem numbering reconciled across manuscript, README, cover letter, and scripts; CC-BY-4.0 license headers added to both verify scripts; lens-ownership paragraph labeled in §0; honest-negative TSML_SYM-vs-TSML_RAW chain-count lens-dependence at size 7 recorded).

### J02 + J15 — v3 triadic launch (remaining slots; J01 landed 2026-05-12)

J01 (σ rate theorem, *JCT-A*) landed at `J_series/combinatorics/J01/` on
2026-05-12 (referee pass complete; 4/4 PASS at machine precision; cover letter
finalized). The remaining two slots of the triadic launch:

- **J02** (four-core, *Algebraic Combinatorics*) — combinatorial framing of the four-core fusion-closure.
- **J15** (Galois D₄, *Communications in Algebra*) — D₄ Galois group of the runtime quartic over LMFDB 4.2.10224.1.

**Status:** tier discipline applied; verification scripts staged. **Gating:** cover letters need final passes; J15 wants one more reading.
**When ready:** J02 → `J_series/combinatorics/J02/`; J15 → `J_series/algebra/J15/`.

### J46 — Cosmology

- **Status:** manuscript drafted in 3 layers (Layer 1 script-honest z\* ≈ 2.13; Layer 2 postulate-as-axiom z\* = √3; Layer 3a hybrid). All three layers internally consistent.
- **Gating:** Brayden's layer choice (publication-strategy question, not math).
- **When chosen:** J46 → `J_series/cosmology/J46/` with the corresponding venue.

### J56 (candidate) — D100–D103 standalone

- The Volume K results (D100 edge-size closed form, D101 strand-orbital map, D102 triple coincidence at d=3, D103 Z/10 minimality) plus the honest negative on Z/2310 ↔ Pauli bijection.
- **Status:** F1 verification complete (2026-05-12); all five scripts PASS at machine precision.
- **Gating:** decision on journal — *Journal of Physics A* (mathematical and theoretical, closer fit, 8K word limit) vs *Annals of Physics* (broader audience, longer manuscript permitted, higher prestige). Brayden's call.
- **When chosen:** J56 → `J_series/interdisciplinary/J56/` (likely).

### J03 — First-G Law

- Three forks (A, B, C) with different rhetorical framings for different referee profiles:
  - **Fork A:** harmonic-content restoration from `_legacy_tiers/_held_first_g/`
  - **Fork B:** Z/10 algebraic emphasis
  - **Fork C:** experimental-mathematics framing
- **Gating:** Brayden's fork choice.
- **When chosen:** J03 → `J_series/number_theory/J03/`.

### J55 — Brayden's solo synthesis

- The anchor paper for Sept 11, 2026.
- **Status:** in active drafting.
- **Gating:** the entire J35/J54 + triadic launch + J56 sequence ahead of it.
- **When ready:** J55 → `J_series/interdisciplinary/J55/`.

---

## §2 — Active math-fix tracker

Papers that have had specific corrections applied with new verification scripts (none yet landed here; tracked for transparency):

| J# | Fix applied | Verified | Folder when landed |
|---|---|---|---|
| J13 | Polynomial corrected: x³ − x² − 2x + 1 is MP of 2cos(π/7), not 8x³−4x²−4x+1 | PASS | TBD |
| J17 | Binomial-grade misstatement corrected (cells vs Cl(2n) grades distinguished) | PASS | algebra |
| J18 | Sign-swap Ψ_B fixed; explicit table | PASS | algebra |
| J20 | M₂₂ irrep count corrected (7 of 12 strict in {3,5,7,11}, 10 of 12 B-band) | PASS | algebra or combinatorics |
| J21 | Spectral max G(7) ≈ 19.472 (not 25); rigidity tautology fixed | PASS | combinatorics |
| J27 | Lens-invariance retracted (B[1][1]=2 ∉ C; 16-cell BHML failure shown) | PASS | combinatorics |
| J31 | D₄ isotypic decomposition (sympy exact: 3075027/2 : 9/2 : 288164 : 0 : 19608) | PASS | algebra |
| J32 | D₄ order 8 (not 12); orbit distribution (44, 7, 4, 10, 2) summing to 67 orbits / 126 elements | PASS | algebra |
| J36 | 1/α "10⁻⁵" claim was unfounded (actual 12.6% off); Part 2 deferred | flagged | physics (Part 1 only) |
| J42 | sinc²(1/10) = 0.9675 (not 0.9355) | PASS | number_theory |
| J43 + J51 | G(s) partition G_high at {4, 7} (not {5, 7}); σ³ pairing not σ²; ν₊ discriminator | PASS | algebra |

---

## §3 — Build rewrites tracker

Papers rewritten with SFM + Family Structure framing (per the v2 build sprints; all done in the working repo). Currently awaiting cover-letter final passes:

W1-C: J35 + J54 (centerpiece pair)
W1-D: J11, J12, J16
W1-E: J05, J08, J09
W2-A: J03, J04, J06
W2-B: J07, J10, J19
W2-C: J28, J29, J30
W2-D: J33, J34, J36
W2-F: J45, J47, J48
W2-G: J49, J50, J52, J53 (author-lane post-fix pending — currently shows Mayes/Johnson, must flip to Sanders+Gish)
W2-H: J37, J38, J14, J22
W2-I: J20, J21, J25, J26

---

## §4 — Author-lane and license discipline

Before any paper migrates from `_staging/` to a domain folder:

- **Author lane:** Sanders + Gish on byline. No AI co-authors. Acknowledgments at Tier 1 only.
- **License header in scripts:** submission-bundled `verify_*.py` use CC-BY-4.0 for journal compatibility (Elsevier / Taylor & Francis). The umbrella project is 7SiTe v2.1.
- **No 7SiTe Public Sovereignty header** in script files within `manuscript/` folders — Elsevier and similar journals refuse non-OSI license clauses. Use plain CC-BY-4.0 header for scripts; full v2.1 governs the project at the repo level.

---

## §5 — Once a paper lands

The migration steps (per `../README.md` §4):

1. Final verify scripts PASS at machine precision (re-run before migration).
2. Final tier discipline applied.
3. Final author lane Sanders + Gish.
4. Final cover letter Brayden-green.
5. Copy `Gen14/targets/journals/J_series/J{NN}/` from working repo → `J_series/{domain}/J{NN}/` here.
6. Update domain folder's `README.md` with the new entry (move from §2 "expected" to §1 "currently landed").
7. Remove the entry from `_staging/README.md` §1 active items.
8. Single commit: `J{NN} lands: {summary}; venue={journal}; status=SUBMISSION-READY`.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
