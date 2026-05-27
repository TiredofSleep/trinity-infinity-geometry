# Merger Plan: F_p Invariance + F_5 Rigidity of the 4-Algebra (J14 + J16 → one paper)

**Status**: Proposed merger plan, awaiting approval.
**Target**: replace two papers on the same algebra with one unified treatment.

## What each source paper currently does

| J# | Title | Content |
|----|----|----|
| **J14** | F_p Structural Invariance of a Commutative Non-Associative 4-Algebra | Studies the 4-algebra V (basis {e_0, e_2, e_3, e_4}, derived from 4-core {0,7,8,9}) at six primes p ∈ {2,3,5,7,11,13}; identifies the lens-invariant skeleton (3 nonzero idempotents, (1,3) Minkowski signature on L_{e_2}, (2,2) chirality on L_{e_0}, 1-dim associator image, power-associativity) vs the prime-dependent features (|Aut(V_p)| takes values 6, 24, 40, 336, 1320, 2184). Target: Algebra Universalis. |
| **J16** | A Commutative Non-Associative 4-Algebra over F_5 with Rigid Idempotent Decomposition | The same 4-algebra V, but at F_5 specifically: gives a rigid idempotent decomposition, characterizes |Aut(V_5)| = 40 = F_{20} × Z/2, identifies the F_5-specific structure. Target: Algebras and Representation Theory. |

## Why they should merge

1. **Same algebraic object** — V is the F_p extension of the BHML 4-core algebra. J14 says "here's what holds across all primes"; J16 says "here's what's specific to p=5". These are two views of one algebra; the natural treatment is to present both in one paper.

2. **Cross-citation is tight** — J14 cites J16's specific F_5 structure as an example of the "prime-dependent" features it identifies; J16 cites J14 for the broader F_p framework.

3. **Currently inconsistent**: J14's claims about V_5 must match J16's claims about V_5. Keeping these in sync across two separate manuscripts is error-prone; readers would have to chase between them.

4. **Venue alignment**: Algebra Universalis can take a single broader paper covering both. Algebras and Representation Theory is a fine fallback. Two-for-one venue load.

## Proposed merged paper

**Title**: *F_p Structure of the BHML 4-Core Algebra: Invariant Skeleton across Primes and Rigid F_5 Idempotent Decomposition*

**Target venue**: Algebra Universalis (primary). Fallback: Algebras and Representation Theory.

**MSC 2020**: 17A30 (non-associative algebras), 17A36 (automorphisms, derivations), 13A02 (graded rings), 13F20 (polynomial rings and ideals), 17B25 (exceptional Lie algebras and superalgebras).

**Structure** (≈25 pages):

1. **§1 Setup**: define V_p = the 4-algebra on basis {e_0, e_2, e_3, e_4} with the multiplication table induced by BHML's restriction to the 4-core; introduce the six primes p ∈ {2,3,5,7,11,13}.
2. **§2 The lens-invariant skeleton** (from J14): 5 properties that hold at every p — 3 nonzero idempotents, eigenspace signatures of L_{e_2} and L_{e_0}, 1-dim associator image, power-associativity. Each proved via an integer-level witness that's nonzero in every characteristic.
3. **§3 Prime-dependent variation** (from J14): the table |Aut(V_p)| ∈ {6, 24, 40, 336, 1320, 2184}; the explicit form of orthogonal idempotent pairs (depends on whether 4 | (p-1)).
4. **§4 The F_5 case** (from J16): rigid idempotent decomposition over F_5; |Aut(V_5)| = 40 = F_{20} × Z/2 in detail; the F_5-specific structure (why p=5 is the smallest "non-degenerate" prime where everything is sharp).
5. **§5 Mod-p rank profile of the BHML 10×10**: from J26 — chain-shell determinants and the rank-preservation profile (p ∈ {7, 11} preserve rank everywhere; p=13 fails only at BHML_6; etc.). Treat as application of §2-§4.
6. **§6 The Dirac substrate** (from J16): F_5 + Cl(0, 10) connection; substrate identification.
7. **§7 Open questions**: extension to larger primes; characteristic-0 behavior; connection to Drápal-Wanless 2021.

## What this merger eliminates

- **Sync risk**: claims about V_5 must match across two papers. Single paper, single source of truth.
- **Reader friction**: a referee currently has to read both to evaluate either.
- **Two venue caps**: AlgUni + AlgRepTheory becomes one of either.

## Source-paper disposition

- **J14**: contents merged into §§1-3 and parts of §5; folder marked MERGED.
- **J16**: contents merged into §§4 and 6; folder marked MERGED.

Both retained for citation history; their READMEs point to the merged paper.

## Verification

J14 has `verify_J14.py` (12/12 PASS); J16 has its own verification. Combined: `verify_J14_J16_merged.py` runs both suites in sequence (~10s).

## Risks of NOT merging

- A referee at AlgUni might ask "what about the F_5-specific structure?" — and the answer is "see the companion J16 at Algebras and Rep. Theory". That's a weak answer; better to have it in the same paper.
- The Algebra Universalis 2026-05-07 fresh-eyes referee already flagged a confusion between J14's signature claim and what V_5 actually does. Co-locating the proofs removes this risk.

## Action checklist (if approved)

- [ ] Draft merged manuscript at `05_papers/algebra/J14_J16_merged/manuscript/manuscript.md`
- [ ] Combine verification scripts
- [ ] Mark J14 and J16 READMEs as MERGED
- [ ] Update `05_papers/algebra/README.md` accordingly

**Estimated effort**: 2 days for merged manuscript.
