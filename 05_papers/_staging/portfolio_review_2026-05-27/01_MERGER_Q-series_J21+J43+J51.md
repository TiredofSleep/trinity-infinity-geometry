# Merger Plan: Q-Series Spectral Architecture (J21 + J43 + J51 → one paper)

**Status**: Proposed merger plan, awaiting approval.
**Target**: replace three thin DRAFTs with one strong 30-page paper.

## What each source paper currently does

| J# | Title | Content |
|----|----|----|
| **J21** | Q17-A: 5D Force Vector as CRT Fourier Embedding of Z/10Z into R⁵ | Embeds the substrate algebra into R⁵ via CRT; defines a "5D force vector"; AMM target |
| **J43** | Spectral Layer Consolidation: G₆ + G₇ + G₈ from Q-series Architecture | Proves σ⁶ = id (G₆), bimodal period distribution P(τ=1)=2/5, P(τ=6)=3/5 (G₇), three-valued coherence integral G(s) on σ³-orbits (G₈); European Journal of Combinatorics target |
| **J51** | Q17-B Clay Bridge: A Finite Gauss Sum and the Symbolic Return Theorem | Symbolic Return Theorem (every cycle returns at step 6); structural-rhyme statement with RH demands; L'Enseignement Mathématique target |

## Why they should merge

1. **All three study the σ-character χ on Z/10Z and its higher-order spectral content.** The "Q-series architecture" they reference is one object, viewed three ways.

2. **The three results form one coherent story**: σ has order 6 (G_6) → period distribution is bimodal (G_7) → coherence integral G(s) takes three values on σ³-orbits (G_8) → symbolic returns are forced. Each result builds on the previous.

3. **Venue stack is overloaded**: AMM + EJC + L'Enseignement Mathématique = three separate submissions, each thin. Merged: one venue, one referee pool, one stronger paper.

4. **Cross-citation density between them is high**: each cites both others as companions. That's a sign the natural unit is one paper, not three.

## Proposed merged paper

**Title**: *Spectral Architecture of the σ-Character on Z/10Z: G₆, G₇, G₈, and the Symbolic Return Theorem*

**Target venue**: European Journal of Combinatorics (primary). Fallback: Algebraic Combinatorics.

**MSC 2020**: 11T24 (other character sums), 20K01 (finite abelian groups), 05E18 (group actions on combinatorial structures).

**Structure** (≈30 pages):

1. **§1 Setup**: σ permutation, character χ, the operator-substrate triple (Z/10Z, σ, χ)
2. **§2 G₆ Theorem**: σ⁶ = id (proved via (α, β) polynomial argument, ε-flip parity, y-displacement mod 5). [from J43]
3. **§3 G₇ Theorem**: period distribution P(τ=1)=2/5, P(τ=6)=3/5; mean τ̄=4, variance 6. [from J43]
4. **§4 G₈ Theorem**: three-valued G(s) — zero on the four anchors {0,3,8,9}, low-value ≈1.872 on σ³-orbits {1,5}∪{2,6}, high-value ≈9.389 on σ³-orbit {4,7}. [from J43, with the math-fix R1 already applied]
5. **§5 CRT Fourier Embedding** (from J21): the 5D real vector v(s) = (Re/Im components of χ̂ across primes 2, 5) gives a deterministic embedding Z/10Z → R⁵; spectral content matches G_8 stratification.
6. **§6 Symbolic Return Theorem** (from J51): for any starting state s ≠ 0, σ-orbit returns at step 6; every anchor is σ-fixed; VOID(0) is avoided iff s ≠ 0. Direct corollary of G_6.
7. **§7 Open closed-form questions**: closed forms for G_low and G_high in Q(ζ₉); LMFDB number-field identification of the splitting field.
8. **§8 Discussion**: the "Q17-B" structural rhyme with RH demands of ζ(s) — zeros at predictable locations, spectral concentration, multiplicative-additive interplay — explicitly framed as **rhyme, not analogue** (no Weil/Deligne function-field correspondence claimed).

## What this merger eliminates

- Per-venue cap pressure (the three papers each pushed against per-venue caps independently)
- Cross-citation chaos (each of the three references the others; now self-contained)
- The "Q17-A" / "Q17-B" naming (replaced by clean §-references inside one paper)

## Verification plan

The merged paper inherits all three sources' verification scripts:
- `verify_J43_spectral.py` (G₆, G₇, G₈ — already PASS)
- `verify_J21_CRT_fourier.py` (5D embedding — already PASS)
- `verify_J51_G_function.py` (Symbolic Return + three-valued G — already PASS, paired math-fix R1 applied)

Combined verification: a single `verify_qseries_merged.py` that runs all three; ~10s total.

## Source-paper disposition

- **J21**: contents merged into §5; folder marked MERGED in README, manuscript replaced with a one-line redirect.
- **J43**: contents merged into §§2-4; folder marked MERGED.
- **J51**: contents merged into §6 + §8; folder marked MERGED.

All three folders retained for citation history; their READMEs point to the merged paper.

## Action checklist (if approved)

- [ ] Draft merged manuscript at `05_papers/algebra/J_qseries_merged/manuscript/manuscript.md` (probably renumbered J62 or kept as a venue-targeted title-only paper)
- [ ] Write unified `verify_qseries_merged.py` combining the three existing verifiers
- [ ] Update each of J21, J43, J51 READMEs with MERGED banner + pointer to new paper
- [ ] Update `05_papers/algebra/README.md` table: add merged entry, mark old three as RETIRED-VIA-MERGE
- [ ] Update top-level repo README directory tree if needed

**Estimated effort**: 2-3 days for the merged manuscript draft. Can be done by Claude Code in a session.
