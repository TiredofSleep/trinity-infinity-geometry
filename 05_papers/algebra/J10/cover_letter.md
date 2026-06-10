# Cover letter — J10: Operadic $D_4$ Orbits on the Non-Associative Locus of a Finite Commutative Magma on $\mathbb{Z}/10\mathbb{Z}$

**To:** Editors, *Journal of Algebra*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Operadic $D_4$ Orbits on the Non-Associative Locus of a Finite Commutative Magma on $\mathbb{Z}/10\mathbb{Z}$: A Structural Obstruction Theorem at Arity 3*

---

## Summary

We compute the dihedral $D_4$ orbit decomposition of the non-associative locus $\mathcal{N}\subset(\mathbb{Z}/10\mathbb{Z})^3$ of a fixed canonical commutative magma table $T$ ("TSML") on $\mathbb{Z}/10\mathbb{Z}$ — a finite-magma triad in the same intellectual neighborhood as the maximally non-associative commutative quasigroups of Drápal & Wanless, *J. Combin. Theory A* **184** (2021), 105510.

**Main results.**
- **Theorem A.** $\mathcal{N}$ has exactly $|\mathcal{N}|=126$ ordered triples, and the diagonal action of $D_4=\langle P_{56},\sigma^3\rangle\subset S_{10}$ (order $\mathbf{8}$) partitions $\mathcal{N}$ into $\mathbf{67}$ restricted orbits with size distribution $(44,7,4,10,2)$ at sizes $(1,2,3,4,8)$. Size-weighted sum: $44\cdot 1+7\cdot 2+4\cdot 3+10\cdot 4+2\cdot 8=126$.
- **Theorem B (obstruction).** Exactly $\mathbf{16}$ of the $67$ orbits fail the bracketing-pair coherence condition. Consequently, no function $\Phi:\mathcal{N}\to\mathbb{Z}/10\mathbb{Z}$ with $\Phi(t)\in\{a,b,c,L(t),R(t)\}$ is simultaneously $D_4$-equivariant.
- **Theorem C (sharpening).** Dropping the $\sigma^3$ generator, the partition under $\langle P_{56}\rangle$ has $\mathbf{98}$ orbits ($70$ singletons + $28$ doubletons), and every orbit is coherent. The structural obstruction is therefore *localized at $\sigma^3$*, not at $P_{56}$.
- **Theorem D (4-core arity-3 closure).** The 4-core $\mathcal{C}=\{0,7,8,9\}$ is closed under both arity-3 bracketings $L,R$ on all $4^3=64$ triples of $\mathcal{C}^3$; exactly $8$ of these $64$ are non-associative.

The verification is brute-force over $1000$ triples and the $8$ elements of $D_4$, runs in under $1$ second in pure-standard-library Python, and is bundled with the submission as `verify_J32_d4_orbits.py`.

## Why *Journal of Algebra*

- The paper is a clean structural theorem on the orbit decomposition of a finite-group action on a subset of a finite product set, with explicit obstruction and sharpening results. It sits squarely in the journal's profile.
- The result is *complementary, not overlapping*, with three companion papers in the same submission cycle (full transparency below). The arity-3 / operadic content is not addressed in any of the three.
- The setup neighbors Drápal & Wanless 2021 (small finite commutative non-associative structures on $\mathbb{Z}/n\mathbb{Z}$); the present paper sits at a different extremum (specifically structured at arity 2, with the non-associative *locus* — not the table itself — as the main object of study).

## Per-venue cap transparency

This is the **4th** *Journal of Algebra* submission from this corpus in the 2026 cycle, following:

- **J01** — *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$.* Submitted 2026-05-12. Six-fact fusion-closure / attractor / Galois-$D_4$ bundle; the corpus centerpiece.
- **J11** — *Wedderburn $D_4$-Isotypic Decomposition of the Lens-Pair Commutator $[\mathrm{TSML},\mathrm{BHML}]$ on $\mathbb{Z}/10\mathbb{Z}$.* Submitted 2026-05-12. Exact-rational $D_4$-isotypic projection of $[T,B]\in M_{10}(\mathbb{Z})$, identifying $\mathfrak{su}(4)\oplus\mathfrak{u}(1)\subset\mathfrak{so}(10)$.
- **J12** — *Galois $D_4$ over LMFDB 4.2.10224.1.* Submitted to *Communications in Algebra* 2026-05-12 (not *J. Algebra*; included here for full visibility of the $D_4$ companion bundle).

The present paper differentiates clearly:

- vs **J01** (binary joint closure + binary attractor + Galois $D_4$ bundle on the quartic): J01 is binary; J10 is arity-3 / operadic, and addresses a different structural object (the non-associative locus rather than the joint-closure lattice).
- vs **J11** (Wedderburn $D_4$-isotypic of the $10\times 10$ commutator $[T,B]$): J11 is a matrix-decomposition computation; J10 is a set-partition computation on a subset of $(\mathbb{Z}/10\mathbb{Z})^3$. No content overlap.
- vs **J12** (standalone Galois proof for the quartic): J12 is number-theoretic / Galois-theoretic; J10 is purely combinatorial-on-a-finite-group-action. No content overlap.

We recognize that *Journal of Algebra*'s editorial discretion includes per-author / per-corpus cap considerations, and we have prepared explicit fallback targets in case the present paper would exceed the editor's preferred density of contributions from a single corpus in a single cycle:

**Fallback venues (in priority order, all with equal mathematical fit):**
1. ***Communications in Algebra*** (Taylor & Francis) — same intellectual profile; the obstruction theorem and the orbit-distribution result are a natural fit. Companion paper J12 is already in the *Comm. Alg.* pipeline; J10 would join as a content-distinct submission.
2. ***Algebraic Combinatorics*** (CIRM, Diamond-OA) — the orbit decomposition and bracketing-pair combinatorics are a clean fit; the size distribution $(44,7,4,10,2)$ and the obstruction-orbit characterization are combinatorial-on-a-group-action content. Companion paper J15 (J01's four-core combinatorial framing) is already in the *Algebraic Combinatorics* pipeline.
3. ***Algebras and Representation Theory*** (Springer) — appropriate if the editor prefers a venue closer to the representation-theoretic interpretation in §6 (the operad layer carries content orthogonal to the doubly-invariant $\mathfrak{su}(4)\oplus\mathfrak{u}(1)$ structure of J11).

We are entirely open to the editor's preference and would migrate the submission promptly if asked.

## Companion submissions

The TIG/CK research program is shipping a coordinated $55$-paper sequence (J14–J55) over Summer 2026. The papers most relevant as already-submitted companions:

- **J01** (Sanders & Gish 2026, *J. Algebra*) — establishes the binary joint-closure / attractor / Galois-$D_4$ centerpiece. Cited in §1, §5, §6.
- **J12** (Sanders & Gish 2026, *Comm. Alg.*) — unfolds the standalone Galois proof on the quartic. Cited in §6.
- **J11** (Sanders & Gish 2026, *J. Algebra*) — Wedderburn $D_4$-isotypic of $[T,B]$; identifies $\mathfrak{su}(4)\oplus\mathfrak{u}(1)\subset\mathfrak{so}(10)$. Cited in §6.
- **J45** (Sanders & Gish 2026, *Comm. Alg.*) — operadic $\langle P_{56}\rangle$-equivariant fuse-rule survey (the constructive companion to Theorem C). Cited in §1, §7.

## Lens- and substrate-scope discipline

Per the corpus boilerplate `Atlas/META_PLAN_2026-05-06/J_PAPER_BOILERPLATE.md` §5.5, the paper is explicit about lens scope:

- $T$ is TSML_RAW, the canonical bit-pattern table on $\mathbb{Z}/10\mathbb{Z}$ (Appendix A of the manuscript). The orbit count $67$ and obstruction count $16$ are computed on TSML_RAW.
- The upper-triangle symmetrization TSML_SYM has $128$ non-associative triples instead of $126$; we do not record orbit counts for this variant.
- The $4$-core arity-$3$ closure (Theorem D) is lens-invariant because $\mathcal{C}=\{0,7,8,9\}$ is lens-invariant (asymmetric cells of TSML_RAW vs TSML_SYM all lie outside $\mathcal{C}$).

The PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN tier discipline is followed in the manuscript's §0.

## Reproducibility

The standalone verification script `manuscript/verification/verify_J32_d4_orbits.py` performs all six load-bearing claims at machine precision:

1. $|\mathcal{N}|=126$ (with optional JSON cross-check).
2. $|D_4|=8$ with the correct order spectrum $\{1:1,\,2:5,\,4:2\}$.
3. $67$ restricted orbits with size distribution $(44,7,4,10,2)$ summing to $126$.
4. Exactly $16$ bracketing-pair incoherent orbits among the $67$.
5. $98$ $\langle P_{56}\rangle$-orbits ($70$ singletons + $28$ doubletons), all coherent.
6. $4$-core arity-$3$ closure: $64$ in-core / $0$ out-of-core / $8$ non-associative.

The script depends only on the Python standard library (no `numpy`, no `sympy`). Total wall-clock under $1$ second. Deterministic. License header on the script is CC-BY-4.0 for journal compatibility.

## Suggested reviewers

- An expert in finite-magma / sub-quasigroup combinatorics (Drápal-Wanless line).
- An expert in algebraic operads at arity $3$ (Loday-Vallette tradition).
- An expert in finite permutation groups acting on combinatorial structures (Cameron-Cherlin tradition).

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
