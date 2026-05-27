# Merger Plan: Fejér Spectral Squarefree Pair (J03 + J08 → one paper) — *evaluate before deciding*

**Status**: Proposed merger plan. Read J03 and J08 manuscripts before deciding whether to merge or to leave separate.

## What each source paper currently does

| J# | Title | Status | Content |
|----|----|----|----|
| **J03** | Discrete Fejér Quotient on Squarefree Moduli: Spectral Characterization | MERGED (absorbed J04 on 2026-05-13) | Spectral characterization of Fejér quotients restricted to squarefree moduli; Integers journal |
| **J08** | First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Z/nZ | REVISED (2026-05-08) | First-coprime-failure phenomenon framed via the discrete Fejér kernel |

## The question

Do J03 and J08 study the same object or related objects?

- **Same kernel**: both use the discrete Fejér kernel on Z/nZ for squarefree n.
- **Different phenomena**: J03 focuses on the Fejér *quotient* (a ratio of spectral functions); J08 focuses on the *first-coprime-failure*, a discrete event in a sequence.
- **Both have already absorbed companions**: J03 absorbed J04; J08 underwent a major referee fix.

## Decision criterion

**MERGE** if §3 of J03 and §2 of J08 cite the same theorems / use the same kernel construction in the same direction. Then the work is one piece of mathematics presented in two slices.

**KEEP SEPARATE** if they're orthogonal results that happen to share the Fejér kernel as a technical tool. In that case, two papers in *Integers* is fine.

## Recommended action

Before approving a merger, do the following inspection (estimated 30 min):

1. Read J03's §1-§3 and J08's §1-§3.
2. Compare theorem statements.
3. Look for direct cross-citation between them: does J03 cite J08, or vice versa, for a load-bearing claim?
4. If theorems are interleaved (J03's Thm 2 uses J08's Thm 1 as a step), they are one paper.
5. If theorems are independent (J03's Thm 2 doesn't use anything from J08), keep them separate.

## If merged

**Title**: *Spectral Characterization of the Discrete Fejér Kernel on Squarefree Moduli: Quotient Identities and First-Coprime-Failure*

**Target venue**: Integers (still primary). 25-30 pages.

**Structure**:
1. §1 Setup: Fejér kernel on Z/nZ, restriction to squarefree n.
2. §2 Quotient identities (from J03).
3. §3 First-coprime-failure (from J08).
4. §4 Joint structural picture: how the quotient identities and the first-coprime-failure both follow from the same multiplicative-structure-on-squarefree fact.
5. §5 Open: extension to non-squarefree n.

## If kept separate

Both J03 and J08 stand as currently revised. No action needed beyond ensuring each cites the other where load-bearing.

## What I do NOT know without reading the manuscripts

- Whether J03's Thm 2 actually uses J08's Thm 1.
- Whether the "Fejér quotient" of J03 is the same expression as the "Fejér kernel" of J08.
- Whether the audience for both is the same number-theory referee pool, or whether J03 leans toward harmonic analysis and J08 toward combinatorial number theory.

## Action checklist

- [ ] **First**: read J03 §1-3 and J08 §1-3 (or assign Claude Code to do the comparison)
- [ ] **Then**: decide merge vs separate based on theorem interleaving
- [ ] If merge: write the merged manuscript and update both READMEs
- [ ] If separate: confirm each has the correct citation to the other

**Estimated effort**: 30 min inspection + (2 days if merge approved).
