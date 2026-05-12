# Cover letter — J14: F_p Structural Invariance of a Commutative Non-Associative 4-Algebra Arising from the 4-Core of Z/10Z

**To:** Editors, *Algebra Universalis*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *F$_p$ Structural Invariance of a Commutative Non-Associative 4-Algebra Arising from the 4-Core of $\mathbb{Z}/10\mathbb{Z}$*

---

## Summary

We exhibit a 4-dimensional commutative non-associative algebra $V$ defined by an explicit $4 \times 4$ multiplication table over $\mathbb{F}_p$ whose **lens-invariant structural skeleton** transfers across the verified primes $p \in \{2, 3, 5, 7, 11, 13\}$:
- exactly $3$ non-zero idempotents (plus the zero idempotent);
- a $1$-dimensional left annihilator;
- $(1, 3)$ Minkowski signature on the operator $L_{e_2}$;
- $(2, 2)$ chirality signature on $L_{e_0}$;
- empty intersection of the $1$-eigenspace of $L_{e_2}$ with the $0$-eigenspace of $L_{e_0}$;
- commuting $L_{e_2}$ and $L_{e_0}$;
- $1$-dimensional associator image;
- power-associativity.

Distinct from this lens-invariant skeleton, two features **vary** with $p$ and are explicitly identified as non-invariants: $|\mathrm{Aut}(V_p)|$, which equals $40$ over $\mathbb{F}_5$ specifically (with structure $F_{20} \times \mathbb{Z}/2$) but takes values $\{6, 24, 40, 336, 1320, 2184\}$ at $p \in \{2, 3, 5, 7, 11, 13\}$ respectively; and the explicit form of orthogonal idempotent pairs $(p_+, p_-)$, which depends on the availability of primitive 4th roots of unity in $\mathbb{F}_p$. We conjecture the structural skeleton transfers to all primes $p \neq 2$.

The paper carries the four-tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) in §1.1 and an explicit lens-and-substrate paragraph in §1.2, both following the Drápal--Wanless (2021, *JCTA* 184, 105510) line of work on small finite commutative non-associative structures with structural invariants.

## Why *Algebra Universalis*

* The result is a structural theorem about a finite commutative non-associative algebra with a one-dimensional associator image, an explicit invariant skeleton, and a precisely-bounded characteristic-dependence — squarely within *Algebra Universalis*'s core.
* The proof is direct computation in a brute-force-tractable regime ($O(p^4)$ idempotent enumeration); all 14 algebraic checks for the $\mathbb{F}_5$ case run in under 2 seconds on a laptop. A 5-line `numpy/sympy` verification snippet is embedded in §2.3 of the manuscript so any referee can reproduce the core checks instantly.
* The clear separation of invariants (lens-invariant skeleton items 1--8) from non-invariants ($|\mathrm{Aut}(V_p)|$ varies with $p$; explicit form of $(p_+, p_-)$ depends on primitive 4th roots) prevents the kind of misreading where "F$_p$-invariance" is confused with "every quantity is the same across primes."
* The Drápal--Wanless 2021 *JCTA* neighborhood is the correct structural location for this work; the paper cites this published precedent explicitly.

## Defensive-exposition note

The manuscript includes (a) the multiplication table printed inline as Equation~\eqref{eq:Ttable}, (b) a worked associator example in §2.1, (c) a 5-line verification snippet in §2.3, and (d) a tabulated list of $|\mathrm{Aut}(V_p)|$ values for the verified primes in §4.1. These additions are designed so that any future referee with `numpy/sympy` open will reproduce the paper's claims without needing to consult the upstream `tig_dirac.py` library.

## Companion submissions

The TIG/CK research program is shipping a coordinated J-series. The papers most relevant as already-submitted companions to this manuscript are:

- J02 (Sanders & Gish), *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor*, submitted to *Algebraic Combinatorics*, 2026 (the combinatorial origin of the algebra).
- J05 (Sanders & Mayes), *Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas*, submitted to *J. Combin. Theory A*, 2026.
- J06 (Sanders & Gish), *Flatness Theorem: The Forced 2×2 Torus on Z/10Z*, submitted to *J. Pure Appl. Algebra*, 2026.

The closest published precedent is Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510.

## Reproducibility

Verification scripts: `verify_discrete_dirac_4core.py` (14 algebraic checks over $\mathbb{F}_5$) plus a parametric variant covering $p \in \{2, 3, 7, 11, 13\}$. Reference Python library: `tig_dirac.py` (functions `mul`, `all_automorphisms`, `T_F5`). All scripts run with `numpy` (and optionally `sympy` for symbolic eigenspace computation) as the only external dependencies in $<2$ seconds on a standard laptop. Deposited at https://github.com/TiredofSleep/ck/tree/tig-synthesis/Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04.

## Suggested reviewers

- A specialist on finite commutative non-associative algebras / quasigroup combinatorics (Drápal--Wanless neighborhood).
- A specialist on idempotent decomposition over finite fields with characteristic-dependent automorphism structure.
- A specialist on small finite-algebra structural invariants (Latin-square or magma-counting tradition).
(Three to five candidates to be selected by Brayden during pre-submission referee-rigor pass.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
