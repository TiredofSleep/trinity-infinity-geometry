# Cover letter — J10: Coordinate Coverage and Joint-Injectivity Criteria for Partition Pairs on Squarefree Z/nZ

**To:** Editors, *European Journal of Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Coordinate Coverage and Joint-Injectivity Criteria for Partition Pairs on Squarefree Z/nZ*

---

## Summary

For squarefree *n* = *p*<sub>1</sub>···*p*<sub>k</sub> with k ≥ 2, we give a clean sufficient condition for a pair of partition-inducing maps *f*, *g* : Z/nZ → · to have injective joint map *J* = (*f*, *g*): if the resolving prime sets satisfy *D*<sub>f</sub> ∪ *D*<sub>g</sub> = {*p*<sub>1</sub>, …, *p*<sub>k</sub>}, then *J* is injective. The converse fails in general. This is the *coordinate-coverage characterization* (Theorem 4.1 in the manuscript). Several known and folklore sufficiency theorems on Z/nZ — multiplicative-orbit + multiplicative-orbit; additive-residue + multiplicative-orbit; the corrected multiplicative-orbit + additive-residue; additive-residue + additive-residue (CRT lcm-characterization) — are obtained as one-paragraph corollaries by computing the resolving-prime set *D*<sub>h</sub> for each algebraic class. The unifying observation is the per-class *D*<sub>h</sub> computation, not a partition-lattice tautology: the underlying joint-fiber characterization of partition meet is recorded as a Lemma citing Birkhoff (1940) and Ore (1942).

We also (i) record an explicit counterexample at *n* = 15 to a previously-asserted incorrect *M+A* condition (with *G* = ⟨2⟩ in (Z/15Z)\* and the *T*<sub>2</sub>-orbit of 5 equal to {5, 10}, both ≡ 0 mod 5, the previously-asserted condition is satisfied but {5, 10} is in the unresolved-pair sets of both partitions); (ii) prove the corrected Theorem C; (iii) prove the *refinement trap* (no partition family lying in a single refinement chain of the partition lattice can be sufficient unless one element is already the discrete partition); (iv) verify MVJN(Z/30Z) = 1 with two explicit witnesses ({π<sub>SPEC</sub>, π<sub>15</sub>} and {π<sub>DYN</sub>(7), π<sub>DYN</sub>(11)}) framed as an immediate application of the coordinate-coverage theorem; (v) state the conjecture MVJN(Z/nZ) = 1 for every squarefree *n* ≥ 6.

## Why *European Journal of Combinatorics*

- **Partition-lattice and CRT-coordinate combinatorics on a finite cyclic ring** — squarely in EJC's purview.
- **Per-class D_h computation as the substantive unifying observation.** The contribution is structural: a clean sufficient condition (coordinate coverage) plus the per-algebraic-class computation that recovers folklore CRT (Theorem D) and the previously-stated implicit-CRT M+M (Theorem A) as corollaries, alongside Theorem B with the exact "G trivial on n/d" formulation and the corrected Theorem C with the n=15 counterexample. This is a clean unification, not a re-discovery.
- **Self-contained.** The proofs use only standard CRT and partition-lattice facts (Birkhoff 1940; Ore 1942); the n=15 counterexample is verifiable by hand.

## Companion submissions

The TIG/CK research program is shipping a coordinated paper sequence (J01–J55) over Summer 2026. The papers most relevant as already-submitted companions are:

- **J11** (Sanders & Gish 2026, *J. Number Theory*). Corrected Theorem C: n=15 counterexample and the sharpened M+A condition. *(Direct companion: J11 develops the n=15 counterexample into a stand-alone short note, while the present J10 records it as Example 6.1 with full per-class D_h backing.)*
- **J07** (Sanders & Gish 2026, *Algebraic Combinatorics*). A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic Structures and the 4-Core Algebraic Center. *(Structural companion: J07's Theorem 1 — the partition-incompatibility flatness obstruction — uses the same partition-lattice meet machinery developed in this paper as one ingredient.)*
- **J03** (Sanders & Gish 2026, *Integers*). First-G Law: Squarefree Stability of the Smallest-Prime-Factor Coprime Window. *(Cited in §1.4 as one of the predecessor frameworks that motivated the coordinate-coverage approach.)*

## Reproducibility

Verification script: `manuscript/verify_J10.py`, PASSING at machine precision. The proofs are finite-combinatorial and hand-checkable; the script confirms the three computational families directly: (i) the n=15 counterexample (Example 6.1) — *G* = ⟨2⟩ = {1, 2, 4, 8} in (Z/15Z)\*, *T*<sub>2</sub>-orbit of 5 equals {5, 10}, both ≡ 0 mod 5; (ii) the two MVJN(Z/30Z) = 1 witnesses ({π<sub>6</sub>, π<sub>15</sub>} and {π<sub>DYN</sub>(7), π<sub>DYN</sub>(11)}) verified by orbit-by-orbit enumeration plus coordinate-coverage check; (iii) small-n sanity for Theorem D. Pure Python standard library; no third-party dependencies.

## Suggested reviewers

- A specialist in finite cyclic ring combinatorics and the partition lattice (Birkhoff–Ore tradition).
- A specialist in CRT-coordinate decomposition theorems for Z/nZ.
- A specialist in matroid theory and incomparability conditions for partition pairs (Tutte tradition; the "incomparable refinement" notion in Theorem 7.1 is matroid-flavored).

We leave specific names to the editorial board.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

**Note on prior version.** An earlier presentation of this work was titled *The Universal Orthogonality Principle: Joint-Map Injectivity as the Sufficiency Criterion for Two-Partition Families on Squarefree Z/nZ* and was submitted to a number-theory venue. A referee correctly noted that (i) the central "UOP" theorem is the partition-lattice meet definition unfolded (Birkhoff 1940; Ore 1942) and is not theorem-grade in its abstract form; (ii) "orthogonality" terminology overlaps with character-orthogonality in the number-theory literature; (iii) Theorems A and D are folklore implicit in CRT. The present submission addresses all three: UOP demoted to Lemma 2.1 with explicit Birkhoff/Ore citation; "orthogonality" terminology removed throughout; folklore status of A and D explicitly delineated in the prior-literature subsection (§1.4); the substantive contribution made explicit (the coordinate-coverage characterization plus per-class D_h computation, Theorem B with the exact "G trivial on n/d" formulation, the n=15 counterexample, the corrected Theorem C, the refinement trap, and the MVJN(Z/30Z) = 1 result with explicit witnesses).

---

Sincerely,
B.R. Sanders
M. Gish
