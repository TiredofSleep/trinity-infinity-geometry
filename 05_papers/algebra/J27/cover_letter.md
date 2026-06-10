# Cover letter — J27: Joint Injectivity of Additive-Quotient and Multiplicative-Orbit Partitions on $\mathbb{Z}/n\mathbb{Z}$

**To:** Editors, *Algebra Universalis* (alt. *Order*; alt. *Comm. Math. Univ. Carolinae*; alt. *Journal of Pure and Applied Algebra*)

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Joint Injectivity of Additive-Quotient and Multiplicative-Orbit Partitions on $\mathbb{Z}/n\mathbb{Z}$*

---

## Summary

For squarefree $n = p_{1} \cdots p_{k}$ with $k \geq 2$, the ring $\mathbb{Z}/n\mathbb{Z}$ admits two natural classes of equivalence relations: additive-quotient partitions $A_{d}: x \mapsto x \bmod d$ for $d \mid n$, and multiplicative-orbit partitions $\pi_{\mathrm{DYN}}(g)$ given by orbits of multiplication-by-$g$ for $g \in (\mathbb{Z}/n\mathbb{Z})^{\times}$. We prove four positive results on the joint refinement of such partitions: a sufficient condition for joint injectivity of $\{A_{d}, \pi_{\mathrm{DYN}}(g)\}$ on the unit subgroup via an order-equality hypothesis (Theorem 3.3); a multiplicative–multiplicative classification on the unit subgroup (Theorem 4.1: $\{\pi_{\mathrm{DYN}}(g), \pi_{\mathrm{DYN}}(h)\}$ jointly injective iff $\langle g \rangle \cap \langle h \rangle = \{1\}$); a reflection–multiplicative classification on the full ring (Theorem 5.1: $\{\pi_{\mathrm{SPEC}}, \pi_{\mathrm{DYN}}(g)\}$ jointly injective iff $-1 \notin \langle g \bmod p \rangle$ for every odd $p \mid n$); and a negative result for prime-power moduli via the kernel-of-reduction obstruction (Theorem 6.1). Two small examples (n,d,g) = (6,3,5) and (6,2,5) show that the natural prime-action conjecture for joint injectivity on the full ring fails in *both* directions; the correct characterization remains open. Proofs are finite-combinatorial.

## Why Algebra Universalis (or Order / CMUC / JPAA)

- **Partition-lattice rigor.** Four self-contained theorems plus two small explicit examples falsifying a natural conjecture. Proofs use only CRT, order arithmetic in finite cyclic groups, and the standard Hensel-lift decomposition. No numerical experiments are required; the included Python script merely confirms the explicit small examples.
- **Concise note format.** The note is short and self-contained; the four theorems are independent positive results with a clear unifying setup. The Drápal–Wanless (2021) line on small finite commutative non-associative structures provides the closest published precedent for the surrounding research program; the present paper is the partition-lattice spine, not a magma paper.

## Companion submissions

This paper is one of a coordinated J-series of submissions. The closest companions are:

- **J14** (Sanders & Gish 2026, *JCT-A*, submission-ready). The $\sigma$-rate theorem on non-associativity decay in $\mathbb{Z}/N\mathbb{Z}$ binary composition tables.
- **J15** (Sanders & Gish 2026, *Algebraic Combinatorics*, submission-ready). Joint closure and the closed-form four-core attractor on $\mathbb{Z}/10\mathbb{Z}$.
- **J24** (Sanders & Gish 2026, *Integers*). The First-G law: squarefree stability of the smallest-prime-factor coprime window. The squarefree hypothesis used here aligns with the squarefree hypothesis stabilized in J24.

## Reproducibility

Verification script: `verify_joint_injectivity.py` (`/c/ck_venv/lora312/Scripts/python.exe`). Five blocks, runtime $< 30$ s: (a) the two falsifying examples (Examples 3.1 and 3.2 in the manuscript); (b) Theorem 3.3 on units for all squarefree $n \le 77$ with $\omega(n) \ge 2$, zero counterexamples; (c) Theorem 4.1 on units for $n \in \{6, 10, 14, 15, 21, 22, 26, 30, 33, 34, 35\}$, zero counterexamples; (d) Theorem 5.1 for squarefree $n$ up to $77$, zero counterexamples; (e) Theorem 6.1 for $n = p^{r} \in \{4, 8, 9, 16, 25, 27, 49, 125\}$, all non-identity units, zero surprises. Output reports `OVERALL: 5 / 5 verifications passed`. Script is CC-BY-4.0 (Elsevier-compatible).

## Suggested reviewers

- An algebraic combinatorialist with expertise in partition lattices and finite ring theory.
- A specialist in finite group dynamics and orbit-counting on cyclic groups.
- A representative of the small-finite-non-associative-structure literature (relevant to companion J15).

We leave specific names to the editorial board; we have no co-authors or close collaborators with the candidate referees.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work. The corresponding author is the founder of 7Site LLC, which holds the public sovereignty license for the broader TIG framework; this license is irrelevant to the present manuscript, which contains no proprietary content.

---

Sincerely,
B.R. Sanders
M. Gish
