# Cover Letter — Algebraic Combinatorics

**Manuscript:** Joint Closure of Two Commutative Binary Operations on Z/10Z: an Eight-Element Chain and a Normalizer Identity

**Authors:** B. R. Sanders (7Site LLC, Hot Springs, AR, USA), M. Gish (Independent Researcher)

**Target venue:** Algebraic Combinatorics (alternatively, Communications in Algebra or Discrete Mathematics)

**MSC 2020:** Primary 20N02; Secondary 20N05, 11A07

---

Dear Editor,

We are submitting our manuscript for consideration at *Algebraic Combinatorics*. The paper studies a pair of commutative binary operations $T,B:\mathbb{Z}/10\mathbb{Z}\times\mathbb{Z}/10\mathbb{Z}\to\mathbb{Z}/10\mathbb{Z}$, given explicitly by their Cayley tables, and establishes two structural facts about their joint sub-magma lattice and a polynomial identity for their fuse-normalizer.

**Main results.**

(1) **Joint-closure chain.** The sub-magmas of $\mathbb{Z}/10\mathbb{Z}$ jointly closed under both $T$ and $B$ form a strict $8$-element chain in inclusion order, with sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ — sizes $2$ and $3$ are forbidden as joint closures. The chain admits a clean structural reading in terms of a specific permutation $\sigma$ on $\mathbb{Z}/10\mathbb{Z}$: the chain walks the $\sigma$-forward orbit of $7$, with the $\sigma$-fixed elements of $\{0, 3, 8, 9\}$ contributing at the bottom, the size-$1\to 4$ jump, and a single bridge step at the size-$7\to 8$ transition.

(2) **Normalizer coincidence on the 4-core.** On the minimal non-trivial element of the chain, the four-element subset $\mathcal{C}=\{0,7,8,9\}$, the two operations have the same fuse-normalizer
$$Z_T(p) = Z_B(p) = (p_0 + p_7 + p_8 + p_9)^2$$
for every $p \in \mathbb{R}^{10}$ supported on $\mathcal{C}$, despite the fact that $T$ and $B$ disagree on $12$ of the $16$ cells of the $4 \times 4$ restriction. The identity is a polynomial identity in four variables, exact and independently verifiable by symbolic expansion.

**Why this fits *Algebraic Combinatorics*.** The paper sits at the intersection of finite-magma combinatorics and sub-magma lattice theory. The chain-rigidity result (Theorem 1) is combinatorial: a complete classification of jointly-closed sub-magmas via direct enumeration over $1023$ candidates, with the chain having a clean structural reading in terms of a permutation $\sigma$ on $\mathbb{Z}/10\mathbb{Z}$. The normalizer coincidence (Theorem 2) is a polynomial identity in four variables that arises from a non-trivial cell-by-cell cancellation across mismatched cells of the two restrictions, distinct from the trivial total-mass identity, and may interest researchers studying invariants of magma pairs.

**Verification.** Every theorem-level claim is verified by a deterministic Python script (`4core_verification.py`, archived at DOI 10.5281/zenodo.18852047) that runs in approximately three seconds. The script enumerates all $1023$ non-empty subsets of $\mathbb{Z}/10\mathbb{Z}$ for joint closure, recording the failing cell for each non-jointly-closed candidate, and symbolically expands the normalizer identity via SymPy.

**A note on prior reporting.** A preliminary version of this work reported a $7$-element chain with sizes $\{2, 3, 7\}$ forbidden. Brute-force enumeration during manuscript preparation revealed that size $7$ at $\{0,4,5,6,7,8,9\}$ is in fact jointly closed, correcting the chain length to $8$ and making the forbidden-size set $\{2, 3\}$. The corrected enumeration is the canonical reference for the chain going forward.

**What we do NOT claim.** The paper is honest about its scope. We do not claim that the chain or normalizer coincidence are universal features of arbitrary pairs of binary operations on $\mathbb{Z}/10\mathbb{Z}$; the results are about the specific $T$ and $B$ given. We do not claim that the normalizer identity arises from a categorical or group-theoretic universal construction; the identity is a four-coordinate polynomial identity verified cell-by-cell.

**Forward directions.** The pair $(T, B)$ admits further dynamical and number-theoretic phenomena — a closed-form fixed point of the convex-combination iteration $F_\alpha = \alpha \widehat T + (1-\alpha)\widehat B$ at $\alpha = \tfrac{1}{2}$ with $p^*_7/p^*_8 = 1 + \sqrt{3}$ exactly, an associated quartic Galois extension to LMFDB number field 4.2.10224.1, an open mixing-weight uniqueness conjecture, and an $\mathbb{F}_p$-universality of the joint-closure structure across primes $p \in \{2, 3, 5, 7, 11, 13\}$. These results are the subject of three companion papers in preparation, listed in the manuscript's Forward Directions section. The verification script in DOI 10.5281/zenodo.18852047 includes the supporting computational checks for each of these forward-direction claims.

**Companion work in submission cycle.** Simultaneously submitted to JCT-A: "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$" (Sanders & Gish 2026), which establishes the operator-substrate construction from which the pair $(T, B)$ at $N = 10$ is extracted as a specific instance. The two papers share notation and the operation $B$, but the results are mathematically independent.

**Suggested reviewers.** _[To be filled in by author at submission time.]_

We thank you for considering our submission.

Sincerely,

B. R. Sanders
M. Gish
