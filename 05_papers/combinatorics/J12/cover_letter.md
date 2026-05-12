# Cover letter — J12: Non-CRT Sufficient Pairs and the Minimum Viable Jump Number on Squarefree Z/nZ

**To:** Editors, *European Journal of Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Non-CRT Sufficient Pairs and the Minimum Viable Jump Number on Squarefree Z/nZ*

---

## Summary

For squarefree $n = p_1 \cdots p_k$ ($k \geq 2$), we study the partition lattice of $\Z/n\Z$ from the CRT coordinate decomposition. Main results:

1. **Orbit-pair classification (Theorem 3.1).** $\{\pi_{\mathrm{DYN}}(g), \pi_{\mathrm{DYN}}(h)\}$ is sufficient iff $\langle g \rangle \cap \langle h \rangle = \{1\}$, equivalently $\gcd(\mathrm{ord}_{p_i}(g), \mathrm{ord}_{p_i}(h)) = 1$ at every prime $p_i \mid n$.

2. **Three-mechanism support classification (Theorem 4.1).** Sufficient orbit-pairs partition uniquely into three types: focused at distinct primes (M1), same-prime coprime orders (M2), or mixed (M3). Mechanism (M2) at a prime $p_i$ exists iff $p_i - 1$ has ≥ 2 distinct prime factors. Smallest five: 7, 11, 13, 19, 23.

3. **Three explicit non-CRT pairs on Z/30Z (Theorem 5.1).** $\{\pi_{\mathrm{DYN}}(7), \pi_{\mathrm{DYN}}(11)\}$ (orbit + orbit, mechanism M3), $\{\pi_2, \pi_{15}\}$ (residue + residue), $\{\pi_{\mathrm{SPEC}}, \pi_{15}\}$ (reflection + composite residue) — all sufficient with one orthogonal jump.

4. **Universal $\mathrm{MVJN} = 1$ (Theorem 7.2).** $\mathrm{MVJN}(\Z/n) = 1$ for every squarefree $n$ with $k \geq 2$ primes (this was a conjecture in earlier drafts; now promoted to a theorem via the construction $\{\pi_{p_1}, \pi_{n/p_1}\}$).

We work the $n = 10$ case in detail and provide an explicit parametrization of mechanism (M3) at $n = 42$.

## Why European Journal of Combinatorics

The paper is genuinely combinatorial: partition lattice structure, set-theoretic intersections, orbit structure, and minimum-element problems within the lattice. The orbit-pair classification (Theorem 3.1) is in the intellectual neighborhood of orthogonal cyclic Latin square existence theory (Bose–Shrikhande–Parker line). The three-mechanism support classification (Theorem 4.1) gives a clean number-theoretic-flavored combinatorial constraint ($p_i - 1$ has ≥ 2 distinct prime factors).

## Standalone scope

This paper is now standalone. All theorems proved by direct CRT-coordinate arguments; no dependencies on companion submissions for load-bearing content.

## Closest published precedent

Drápal & Wanless (2021), *J. Combin. Theory Ser. A* **184**, 105510, on small finite combinatorial structures with explicit CRT-coordinate criteria — same intellectual neighborhood, different specific topic.

## Reproducibility

The pair-injectivity computations are hand-checkable. The orbit classifications for n = 30 (Theorem 5.1) can be verified in under five minutes by direct enumeration of orbits in (Z/30Z)*. The DYN-pair examples at n = 42 (Theorem 4.1 mechanism (M3)) can be verified by computing orders mod 3 and mod 7. We have independently verified all numerical claims via numpy enumeration.

## Suggested reviewers

- A specialist in partition lattices and combinatorial designs.
- A specialist in finite group actions on residue classes.
- A specialist in the combinatorial structure of cyclic group orbit decompositions.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
