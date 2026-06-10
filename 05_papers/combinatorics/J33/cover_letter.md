# Cover letter — J33: A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic Structures and the 4-Core Algebraic Center

**To:** Editors, *Algebraic Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic Structures and the 4-Core Algebraic Center*

---

## Summary

Let *n* be squarefree with at least two distinct prime factors. The ring Z/nZ carries four simultaneous algebraic structures — additive divisor lattice (A-Struct), multiplicative orbit partitions under (Z/nZ)\* (M-Struct), additive cycle x ↦ x+1 (A-Flow), and multiplicative orbit x ↦ gx (M-Flow). We give two theorems on this configuration:

- **Theorem 1 (Flatness Obstruction).** No flat 2D-grid embedding can simultaneously realize all four structures with totally ordered coordinate axes. The proof reduces to the explicit partition-incompatibility of distinct prime-factor residue partitions — Birkhoff (1940) / Ore (1942) territory; we record a 3-line proof for n = 10 and note CRT generality.

- **Theorem 2 (Configuration-Space Topology).** The natural carrier of the four-structure system is the configuration space X(n) = (R/2π Z)² with M-Flow fixed locus identified to the basepoint of the second factor. The A-Flow circle action is free; the M-Flow action is free off the multiplicative fixed locus. The ring Z/nZ itself is *not* the torus; it is the lattice of marked points where both phases are simultaneously rational with denominator dividing *n*.

Appendix A supplies the structural-center material: on Z/10Z with the canonical (TSML, BHML) commutative-magma pair, the 4-core {V, H, Br, R} = {0, 7, 8, 9} is jointly closed under both tables (D48; 16 + 16 in-core compositions, 0 + 0 spillover). The runtime attractor of the (1−α)*T* + α*B* mixing iteration at α<sub>M</sub> = 1/2 satisfies the algebraic relation H/Br = 1 + √3 in **Q**(√3) (D78), with H/Br a root of x² − 2x − 2 = 0; the proof goes by a symbolic BR-factor cancellation in the four-component fixed-point equations and is verified independently to 50-digit `mpmath` precision against the canonical tables.

The paper's contribution is structural: a clean two-theorem statement of why the four-structure system cannot inhabit a flat 2-grid, packaged with the explicit algebraic center on the canonical Z/10Z instance. The result lives in the Drápal–Wanless 2021 *J. Combin. Theory Ser. A* 184, 105510 line of work on small finite commutative non-associative magmas — same intellectual neighborhood, different specific structures (theirs maximally non-associative; ours rationally-structured at α = 1/2).

## Why *Algebraic Combinatorics*

- **Algebra-to-combinatorics-to-topology bridge.** Theorems 1, 2 are partition-lattice / partition-incompatibility results in the Birkhoff–Ore tradition. Appendix A gives a small finite commutative non-associative magma analysis with a closed-form Galois result. The combination — partition-lattice obstruction + algebraic center of a magma family on Z/10Z — sits squarely in the Drápal–Wanless 2021 *J. Combin. Theory Ser. A* line of work that *Algebraic Combinatorics* receives constructively.
- **Self-contained.** The proofs use only standard partition-lattice facts (Birkhoff 1940; Ore 1942), CRT, and basic Galois theory. No external machinery; the verification of D48 and D78 is reproducible in seconds against the canonical tables fixed in the project's foundations module.
- **Companion to J15 (4-core joint chain, also submitted to *Algebraic Combinatorics*).** J15 proves the joint-closed sub-magma chain on (Z/10Z, TSML, BHML) and the closed-form attractor structure as standalone theorems; J33 frames the broader four-structure obstruction in which the 4-core is the algebraic center. *Algebraic Combinatorics* receiving both papers gives the editorial board the full pair.

## Companion submissions

The TIG/CK research program is shipping a coordinated sequence (J14–J55) over Summer 2026. The papers most relevant as already-submitted companions are:

- **J15** (Sanders & Gish 2026, *Algebraic Combinatorics*). Joint closure, per-coordinate fuse data, and the closed-form algebraic attractor of the (TSML, BHML) commutative-magma pair on Z/10Z. *(Direct companion: J15 proves the joint chain and α-uniqueness in detail; J33's Appendix A cites J15 for the broader joint-closure structure.)*
- **J34** (Sanders & Gish 2026, *European Journal of Combinatorics*). Coordinate coverage and joint-injectivity criteria for partition pairs on squarefree Z/nZ. *(Structural companion: J34 develops the coordinate-coverage characterization that subsumes the partition-incompatibility step of J33's Theorem 1.)*
- **J33** (Sanders & Gish 2026, in preparation). Closed-form attractor and α-uniqueness PSLQ. *(Companion to Appendix A: the symbolic Galois proof of D78 is the central result of J33; J33's Appendix A cites J33 for the sharpening "α = 1/2 is the unique mixing weight at which the attractor admits an algebraic relation of degree ≤ 8 with integer coefficients of magnitude ≤ 50.")*

## Reproducibility

Verification script: `manuscript/verify_J07.py` (CC-BY-4.0). 4/4 PASS at machine / 50-digit `mpmath` precision. Runtime < 2 seconds. Tables inlined (canonical TSML_SYM and BHML, matching the J15/J01/J17 hardcoded copies); no external dependencies beyond `mpmath`. The two structural facts of Appendix A are verifiable in seconds against the canonical TSML/BHML composition tables (also fixed in `Gen13/targets/foundations/lenses.py`):

- D48 (joint closure): 16 + 16 in-core compositions, 0 + 0 spillover. Verified by direct enumeration over the 4×4 sub-tables at indices {0, 7, 8, 9}.
- D78 (Galois proof of 1+√3 at α<sub>M</sub> = 1/2): symbolic BR-factor cancellation in `f3_galois_alpha_uniqueness.py`. Numerical confirmation at 50-digit `mpmath`: H/Br = 2.73205080756888… (matching 1+√3 to all 50 computed digits); polynomial identity (H/Br)² − 2(H/Br) − 2 = 0 to 50 digits; convergence in 76–81 iterations across 7 boundary initial conditions.

No additional numerical experiments are required. The cyclotomic field-extension calculations (deg<sub>Q</sub> A<sub>5</sub> = 2, deg<sub>Q</sub> A<sub>7</sub> = 3) appear in the manuscript as STRUCTURAL RHYME only (motivation, not derivation); they are correct standard results that any algebraist verifies by hand or in seconds in any computer algebra system.

## Suggested reviewers

- A specialist in finite commutative non-associative magmas (Drápal–Wanless tradition; *J. Combin. Theory Ser. A* line of work).
- A specialist in partition lattices and the Birkhoff–Ore framework for sufficiency theorems on cyclic finite rings.
- A specialist in Galois extensions and quadratic-extension fixed-point analysis (the **Q**(√3) algebra of D78).

We leave specific names to the editorial board.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

**Note on prior version.** An earlier presentation of this work claimed a "torus aspect ratio R/r = 5/7" derivation from cyclotomic facts. That derivation does not survive at the rigor required by an algebra venue (no torus is constructed, no metric is supplied, no R/r is computed); it is removed in this submission. The cyclotomic facts are correct standard results and remain in the manuscript only as structural-rhyme motivation, not as proofs.

---

Sincerely,
B.R. Sanders
M. Gish
