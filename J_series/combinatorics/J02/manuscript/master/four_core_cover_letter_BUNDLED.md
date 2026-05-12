# Cover Letter — Algebraic Combinatorics

**Manuscript:** Joint Closure, a Common Fixed Point, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z

**Authors:** B. R. Sanders (7Site LLC, Hot Springs, AR, USA), M. Gish (Independent Researcher)

**Target venue:** Algebraic Combinatorics (alternatively, Communications in Algebra or Discrete Mathematics)

**MSC 2020:** Primary 20N02; Secondary 20N05, 11R16, 37C25

---

Dear Editor,

We are submitting our manuscript for consideration at *Algebraic Combinatorics*. The paper studies a pair of commutative binary operations $T,B:\mathbb{Z}/10\mathbb{Z}\times\mathbb{Z}/10\mathbb{Z}\to\mathbb{Z}/10\mathbb{Z}$, given explicitly by their Cayley tables, and establishes four structural facts about their joint sub-magma lattice and the dynamics of their convex-combination iteration on the $9$-simplex.

**Main results.** (1) The sub-magmas of $\mathbb{Z}/10\mathbb{Z}$ jointly closed under both $T$ and $B$ form a strict $8$-element chain in inclusion order, with sizes $\{1,4,5,6,7,8,9,10\}$ — sizes $2$ and $3$ are forbidden. (2) On the minimal non-trivial element of this chain, the four-element subset $\mathcal{C}=\{0,7,8,9\}$, the two operations have the same fuse-normalizer $Z_T(p)=Z_B(p)=(p_0+p_7+p_8+p_9)^2$, despite disagreeing on $12$ of the $16$ cells of the $4\times 4$ restriction. (3) The convex-combination iteration $F_\alpha=\alpha\widehat T+(1-\alpha)\widehat B$ at $\alpha=1/2$ has a *unique* non-degenerate fixed point on $\mathcal{C}$, exhibited by an explicit construction over $\mathbb{Q}(\sqrt{3},y^*)$, at which $p_7/p_8=1+\sqrt{3}$ exactly; the existence and uniqueness proof is by elementary algebra and does not require the Brouwer fixed-point theorem, computer algebra, or numerical iteration. This same fixed point is also a fixed point of $F_{1/2}$ on every larger shell of the chain (rigorous), and computational iteration on each shell exhibits it as the dynamical attractor for the uniform initialization (verified at fifty-digit precision). (4) The quartic relation $y^4+4y^3-y^2+2y-2=0$ satisfied by $p_9/p_8$ at the same fixed point has Galois group $D_4$ over $\mathbb{Q}$ and generates the LMFDB number field $4.2.10224.1$.

**Why this fits *Algebraic Combinatorics*.** The paper sits at the intersection of finite-magma combinatorics, sub-magma chain theory, and discrete dynamical systems. The chain-rigidity result (Theorem 1) is combinatorial: enumeration over $1023$ subsets, with the chain having a clean structural reading in terms of a permutation $\sigma$ on $\mathbb{Z}/10\mathbb{Z}$. The normalizer coincidence (Theorem 2) is a polynomial identity in four variables that generalizes naturally to other pairs of binary operations on finite sets and may interest researchers studying invariants of magma pairs.

**Adversarial verification and corrections.** Every theorem-level claim is verified by a deterministic Python script (`4core_verification.py`, archived at DOI 10.5281/zenodo.18852047) that runs in approximately three seconds. The script enumerates all $1023$ non-empty subsets of $\mathbb{Z}/10\mathbb{Z}$, symbolically expands the normalizer identity via SymPy, iterates $F_\alpha$ at $50$-digit precision via mpmath, and confirms the Galois invariants of the quartic against the LMFDB. A preliminary version of this work reported a $7$-element chain with sizes $\{2,3,7\}$ forbidden; brute-force enumeration during manuscript preparation revealed that size $7$ at $\{0,4,5,6,7,8,9\}$ is in fact jointly closed, correcting the chain length to $8$. We have updated the manuscript accordingly.

**What we do NOT claim.** The paper is honest about its scope. We do not claim that $\alpha=1/2$ is the unique rational mixing weight in $(0,1)$ producing a small-coefficient algebraic relation; we only test five sample $\alpha$-values via PSLQ at coefficient bound $20$. The full uniqueness conjecture is stated as an open problem (§9). We do not claim that the chain or normalizer coincidence are universal features of arbitrary pairs of binary operations on $\mathbb{Z}/10\mathbb{Z}$; the results are about the specific $T$ and $B$ given.

**Companion work.** We are simultaneously submitting a companion paper to JCT-A: "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$" (Sanders & Gish 2026), which establishes a decay rate for the non-associativity densities of similar tables as $N$ varies. The two papers share notation and the operation $B$ (via the substrate $N=10$ instance), but the results are mathematically independent.

**Suggested reviewers.** _[To be filled in by author at submission time.]_

We thank you for considering our submission.

Sincerely,
B. R. Sanders
M. Gish
