# J04 — Algebraic Rigidity of the σ-Magma on ℤ/10ℤ: Simplicity, Trivial Automorphism Group, and Unique Sub-Magma

**Target venue:** *Semigroup Forum* (Springer)
**Alternative venues:** *Communications in Algebra* (Taylor & Francis), *Algebra Universalis* (Springer), *Algebraic Combinatorics* (Centre Mersenne)
**Status:** DRAFT — three independent rigidity theorems PROVED by exhaustive computation; awaiting Brayden green-light
**Author lane:** Sanders + Gish
**Tier:** 1 (ship-ready (Semigroup Forum; 4/4 PASS in ~3s; PROMOTED 2026-05-27))
**Source:** scrutiny + extension pass on `overnight_handoff_2026-05-27` (2026-05-26).

---

## §1 — Summary

The σ-magma at order 10 is defined by the operation
$$
x \diamond y = \sigma\bigl((x + y) \bmod 10\bigr),
$$
where σ is the permutation $[0, 7, 1, 3, 2, 4, 5, 6, 8, 9]$ with cycle structure $(0)(1\,7\,6\,5\,4\,2)(3)(8)(9)$ — 4 fixed points plus one 6-cycle. This object is the subject of a separate equational-extremality claim (14 ETP equations out of 4694, per Tao's Equational Theory Project) that lies outside this paper's scope.

The present paper establishes three independent **rigidity theorems** about the σ-magma, each proven by exhaustive computation:

**Theorem A (trivial automorphism group).** The only permutation $\pi$ of $\{0, 1, \ldots, 9\}$ satisfying $\pi(x \diamond y) = \pi(x) \diamond \pi(y)$ for all $(x, y)$ is the identity. Equivalently, $|\mathrm{Aut}(\text{σ-magma})| = 1$.

**Theorem B (congruence-simplicity).** The σ-magma has exactly two congruences: the identity (every element is its own equivalence class) and the universal (all elements in one class). No non-trivial homomorphic image exists.

**Theorem C (unique non-trivial sub-magma).** The σ-magma has exactly five sub-magmas: three singleton idempotent sub-magmas $\{0\}, \{1\}, \{2\}$, the full magma, and one non-trivial proper sub-magma $\{1, 6\}$, which is isomorphic to $\mathbb{Z}/2$ with multiplication table $1 \diamond 1 = 1$, $1 \diamond 6 = 6 \diamond 1 = 6$, $6 \diamond 6 = 1$.

**Theorem D (2-generation).** Every pair $\{a, b\} \subset \{0, \ldots, 9\}$ except $\{1, 6\}$ generates the full σ-magma under iterated $\diamond$, with generation depth at most 4. The pair $\{1, 6\}$ is the unique non-generating pair (consistent with Theorem C: $\{1, 6\}$ is the unique non-trivial sub-magma).

These four theorems collectively show that the σ-magma is **algebraically rigid in every standard universal-algebra sense**: no automorphisms (rigid), no homomorphic images (simple), no non-trivial proper sub-structures except a single $\mathbb{Z}/2$ (almost-substructure-free), and minimally generated (2-generated).

## §2 — Why this matters

Commutative quasigroups of order 10 are not classified in the literature; there are $\sim 10^9$ Latin squares of order 10 (Sloane A040082), of which an unknown but very large number are commutative. Among these, magmas with all of:

- Trivial automorphism group (Theorem A),
- Congruence-simplicity (Theorem B),
- A unique non-trivial sub-magma (Theorem C),

are *empirically rare*. We make no quantitative rarity claim in this paper — we simply observe that the σ-magma is a clean example of "maximally indecomposable" commutative quasigroup of order 10. The σ-magma arises in the Trinity Infinity Geometry (TIG) framework as the natural symmetric closure of a specific 10-element substrate; the framework provides the substrate, but the four rigidity theorems are framework-independent and stand on their own as universal-algebra results.

## §3 — Files in this folder

- `manuscript/manuscript.md` — full ~10-page note with proofs
- `manuscript/verification/verify_J59.py` — self-contained verification, 4/4 PASS
- `cover_letter.md` — venue-targeted cover letter

## §4 — Verification

```bash
python manuscript/verification/verify_J59.py
```

Expected: 4 OK lines + "Overall: PASS (4/4)." Runtime ~3 seconds.

The verification covers:
- Theorem A: exhaustive search over $10! = 3{,}628{,}800$ permutations.
- Theorem B: exhaustive search over Bell(10) $= 115{,}975$ partitions.
- Theorem C: exhaustive search over $2^{10} = 1024$ subsets.
- Theorem D: pair-by-pair generation for all $\binom{10}{2} = 45$ pairs.

## §5 — Tier discipline

- **PROVED.** Theorems A, B, C, D, each by exhaustive computational search bounded by a small finite cardinality.
- **STRUCTURAL.** The observation that all four rigidity properties hold simultaneously, while no general theorem connects them in the literature; we surface this as a structural fact about this specific object.
- **OPEN.** Whether the σ-magma is the unique commutative quasigroup of order 10 satisfying all four properties (congruence-simple + |Aut|=1 + unique non-trivial sub-magma + 2-generated). A full enumeration of commutative quasigroups of order 10 is computationally feasible but not done here.

## §6 — Relationship to other J-papers and OPEN_FRONTIERS

- **J01** (Four-Core Fusion-Closure) establishes that the 4-core $\mathcal{C} = \{0, 7, 8, 9\}$ is jointly closed under TSML, BHML, and CL_STD. NEGATIVE finding in this paper (§3): $\mathcal{C}$ is NOT closed under the σ-magma, so J01's 4-core does not transfer to the σ-magma's algebraic structure.
- **OPEN_FRONTIERS §64** introduces the σ-magma and its equational-extremality. This paper provides framework-independent rigidity theorems consistent with the extremality (rigidity + simplicity + unique-sub-magma is a strong necessary condition for "minimum equation count" in the ETP catalog).
- **J29** is the companion mod-3 paper on the Lo Shu D₄ orbit; the two papers are independent but share an "extremality through exhaustive verification" methodology.

## §7 — Citation footprint

Sanders, B.R., Gish, M. (2026). "Algebraic rigidity of the σ-magma on $\mathbb{Z}/10\mathbb{Z}$: simplicity, trivial automorphism group, and unique sub-magma." Submitted to *Semigroup Forum*.
