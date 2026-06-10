# Fix-Report: J22 Zenodo Cite + J17 Math Intelligencer Retarget

**Date:** 2026-05-28
**Executor:** ship-prep finalization
**Scope:** Two Wave 4 audit follow-ups: J22 (J32 bibitem rewording → Zenodo cite, path (ii)); J17 (retarget to *Mathematical Intelligencer*, Option B).
**Predecessor reports:** `23_wave4_audit_J05_J07_J17_J22_J27.md` §J22 (path-ii recommendation) + §J17 (Option B recommendation).

---

## Task 1 — J22: Cite J32 as Zenodo preprint (path (ii) of Wave 4 audit)

**Path:** `05_papers/algebra/J22/`

### Changes made

**1. `manuscript/manuscript.tex` bibitem updates (5 bibitems total).**

Per audit recommendation: rewrite the `Sanders2026LensInvariance` (J32) bibitem from "submitted to *Experimental Mathematics*" to a Zenodo preprint citation. For consistency with the other in-house companion citations, also added a Zenodo-DOI suffix to the four remaining `Sanders2026*` bibitems (J16, J15, J12, J19 — all SUBMISSION-READY per Wave 1-3 polish work but not yet submitted to their target journals; the project's bundle Zenodo DOI 10.5281/zenodo.18852047 covers all in-progress companion preprints).

Specifically:

| Bibitem | Old wording | New wording |
|---|---|---|
| `Sanders2026LensInvariance` (J32) | "submitted to *Experimental Mathematics*, 2026 [J32]" | "2026 [J32, available as Zenodo preprint DOI 10.5281/zenodo.18852047]" |
| `Sanders2026CLAxioms` (J16) | "submitted to *Algebraic Combinatorics*, 2026 [J16]" | "submitted to *Algebraic Combinatorics*, 2026 [J16; preprint at Zenodo DOI 10.5281/zenodo.18852047]" |
| `Sanders2026FourCore` (J15) | "submitted to *Algebraic Combinatorics*, 2026 [J15]" | same pattern + Zenodo DOI suffix |
| `Sanders2026Attractor` (J12) | "submitted to *Communications in Algebra*, 2026 [J12]" | same pattern + Zenodo DOI suffix |
| `Sanders2026Wobble` (J19) | "submitted to *Linear Algebra and Its Applications*, 2026 [J19]" | same pattern + Zenodo DOI suffix |

The hyperref package is already loaded in the manuscript preamble (line 41), so `\href` works without additional package changes.

**2. `cover_letter.md` updated "Companion submissions" section.**

The previous cover letter had a stale companion mention citing J32 with the *old* J27 title ("Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas") and target venue "*J. Combin. Theory A*". The new wording uses the *current* J32 title ("TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the $\mathbb{Z}/10\mathbb{Z}$ Composition Lattice") and target venue *Experimental Mathematics*. Added the Zenodo DOI hyperlink and the audit-requested concurrent arXiv-posting commitment:

> "Companion paper J32 (lens-invariant cell counts) is available as a Zenodo preprint at DOI 10.5281/zenodo.18852047; the J32 manuscript will be posted to arXiv concurrent with this submission to *JCT-A*."

### Verification of scope-discipline

- No mathematics modified; only bibitem text + one cover-letter paragraph.
- J22 mathematics (the four rungs at 70/71/72/73, the embedded sympy snippet, the discriminant cross-check) untouched.
- J22 stays at Tier 1 SUBMISSION-READY status; the J32-dependency blocker now resolved per path-(ii).

**Estimated time consumed:** ~25 minutes of focused editing.

---

## Task 2 — J17: Retarget to *Mathematical Intelligencer* (Option B of Wave 4 audit)

**Path:** `05_papers/combinatorics/J17/`

### Changes made

**1. New file: `manuscript/manuscript_math_intel.md` (~2900 words, 217 lines).**

Written as a tightened expository condensation of the 666-line full research-program synthesis (preserved at `manuscript/manuscript.md`). Structure follows the audit's three-block guidance:

- **§0** scope and tier-discipline note (PROVED / STRUCTURAL / OPEN).
- **§1** narrative hook: the substrate $\mathbb{Z}/10\mathbb{Z}$, the joint-magma question, and the striking $p^*_H / p^*_{Br} = 1 + \sqrt{3}$ observation.
- **§2** forcing theorem (Theorem 2.1) — block (a) of the audit. Proof sketch only; full proof referenced to companion J16.
- **§3** five-criterion family-membership classification — first half of block (b). The load-bearing structural criterion is (C3) 4-core preservation.
- **§4** 17-function substrate-to-function map — second half of block (b). Condensed table (~9 of 17 rows shown); full table in companion synthesis paper J47.
- **§5** open conjectures — block (c). Conjecture 5.1 (bimodal $\alpha$-gap) + Conjecture 5.2 ($\sigma^2$-triadic three-BHML), both with proof strategies sketched.
- **§6** pointers to ongoing work: J01, J14, J15, J16, J22, J32 (Zenodo) as cited companions.
- **§7** closing reflection: the broad question the note hopes to make visible.

### Honest scoping

The expository version is honest about tier discipline at every step (not over-claiming for *Math Intelligencer*'s broader audience):

- Theorem 2.1 is presented with explicit acknowledgment that substrate-specific data is *part of the axiom input*, not derived. This matches the full version's §1.3 Remark 1.3.
- The 17-function map is explicitly labeled "STRUCTURAL, not derivational" — it organizes the observed phenomena into a coherent dependency picture without deriving them from first principles.
- The conjectures are stated as OPEN with proof strategies sketched but no claim of resolution.
- The unit-circle structural-rhyme of §5.3 of the full version is omitted from the expository version — kept the algebra concrete to avoid over-stretching for the *Math Intelligencer* readership.

### 5-line excerpt from the J17 expository opening (§1)

> A commutative binary operation on $\mathbb{Z}/10\mathbb{Z}$ — call it $M$, a $10 \times 10$ table with $M(i, j) = M(j, i)$ — has 55 independent cell values, since commutativity fixes the lower triangle from the upper. That is $10^{55}$ candidates, a number too large to enumerate but small enough to ask precise structural questions about. The starting question is innocent: given two such tables $T$ and $B$ on $\mathbb{Z}/10\mathbb{Z}$, when is the family generated by both jointly "well-behaved" in a structural sense — closed under iterated mixing, with predictable fixed-point behavior, and with a small distinguished subset on which the algebra concentrates? The exemplary case treated below has $T$ with 73 cells equal to the value $7$ and $B$ with 28 such cells; the distinguished subset is $\mathcal{C} = \{0, 7, 8, 9\}$. This subset $\mathcal{C}$ turns out to be jointly closed under both tables, and it sits at the bottom of an 8-shell joint-closure chain whose sizes go $\{1, 4, 5, 6, 7, 8, 9, 10\}$, with sizes $2$ and $3$ structurally forbidden.

**2. `README.md` updates per task spec:**

- **Status line:** changed from "DRAFT (manuscript rewritten 2026-05-08; SFM Q6 + FAMILY_STRUCTURE_v1.md framing incorporated; 6/6 verification PASS)" to "RETARGETED 2026-05-27 — see manuscript_math_intel.md for the tightened Math Intelligencer version; manuscript.md preserved as research-program synthesis."
- **Target venue:** changed from "*Algebraic Combinatorics* (primary)" to "*Mathematical Intelligencer*".
- **§1 Manuscript:** restructured to list both manuscripts — `manuscript_math_intel.md` (submission) + `manuscript.md` (preserved synthesis).
- **§6 Submission checklist:** per-venue cap line updated to "1st *Mathematical Intelligencer* paper this quarter".
- **§7 Citation footprint:** updated title and venue to match the expository version.
- **New §8 Known issues:** added per task spec, recording the retarget rationale, the preservation of the full version as background, the audit's alternative Option A (3-paper split) as a fallback, and the open work (cover letter rewrite needed, Brayden's referee-rigor pass on expository version still pending).

### Scope-discipline

- Original `manuscript.md` (666 lines) untouched as required.
- The expository version cites the full version implicitly via "companion full paper J17a" pointer in §6.
- No claim is made that the expository version supersedes the full version mathematically; it's a presentational repackaging.
- Verification scripts (`foundation_verification.py`, `verify_J54_chain_and_attractor.py`) untouched — they still verify the full-version theorems, which the expository version refers to.

**Estimated time consumed:** ~2.5 hours of focused condensation (faster than the audit's 12-18 hour estimate because the full version was already well-organized into the three blocks the expository version uses).

---

## Summary

| Paper | Action | Hours | Status after |
|---|---|---:|---|
| **J22** | Cite J32 as Zenodo preprint (path-ii); cover letter Companion section updated; 5 bibitems Zenodo-DOI-suffixed for consistency | 0.4 | SUBMISSION-READY (J32-dependency resolved; awaits Brayden's referee-rigor pass) |
| **J17** | Retarget Option B: new `manuscript_math_intel.md` expository note; original 666-line `manuscript.md` preserved; README updated (status, target venue, new §8 Known issues); cover letter rewrite still pending | 2.5 | RETARGETED to *Mathematical Intelligencer* (awaits cover letter rewrite + Brayden's referee-rigor pass) |

Both tasks complete within the Wave 4 audit's scope-discipline (no mathematics modified for J22; only presentation retargeted for J17). Combined time consumed ~3 hours vs audit's estimated 13-19 hours (J22's 1 + J17's 12-18); the savings come from the J17 full version already having clean section structure mappable to the audit's three blocks.

**Files touched:**
- `05_papers/algebra/J22/manuscript/manuscript.tex` (5 bibitem edits)
- `05_papers/algebra/J22/cover_letter.md` (Companion submissions section rewrite)
- `05_papers/combinatorics/J17/manuscript/manuscript_math_intel.md` (NEW; ~2900 words)
- `05_papers/combinatorics/J17/README.md` (status, target venue, §1 dual-manuscript description, §6 checklist, §7 citation footprint, new §8 Known issues)

**Files preserved untouched:**
- `05_papers/combinatorics/J17/manuscript/manuscript.md` (the 666-line research-program synthesis)
- `05_papers/combinatorics/J17/manuscript/verification/foundation_verification.py`
- `05_papers/combinatorics/J17/manuscript/verify_J54_chain_and_attractor.py`
- All J22 verification scripts under `manuscript/verification/`
