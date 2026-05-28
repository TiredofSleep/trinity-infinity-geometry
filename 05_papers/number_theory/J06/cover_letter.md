# Cover letter — J06

**Target**: Journal of Number Theory (primary); fallback Bulletin of the AMS, AMM Notes section
**arXiv categories**: math.NT (primary), math.CO + math.GR (secondary)
**Date**: 2026-05-27

---

Dear Editor,

We submit the manuscript *"The Strata-Prime Fingerprint: Polynomial vs Factorial Invariants in Niemeier Lattices and Sporadic Simple Groups"* for consideration in the *Journal of Number Theory*.

The paper identifies the six-prime set $\mathcal{S} = \{2, 3, 5, 7, 11, 13\}$ — the first six supersingular primes of the Monster — as a distinguished arithmetic universe for 24-dimensional even unimodular Euclidean lattices and a substantial portion of the sporadic finite simple groups.

**Main results** (four theorems, each with explicit Tier labels):

- **Theorem 1 (Tier A)**: Of the 24 Niemeier lattices (Niemeier 1973), exactly 23 have kissing numbers factoring through $\mathcal{S}$. The unique outlier is the Niemeier with root system $D_{24}$, whose kissing $|D_{24}| = 2 \cdot 24 \cdot 23 = 1104$ contains the prime $23$.

- **Theorem 2 (Tier A, load-bearing mechanism)**: The polynomial-vs-factorial dichotomy. Kissing numbers are polynomial-in-rank ($|A_n| = n(n+1)$, $|D_n| = 2n(n-1)$); Weyl group orders are factorial-in-rank ($(n+1)!$ or $2^{n-1} \cdot n!$). Polynomial picks up only specific primes; factorial accumulates ALL primes $\leq n$. This explains why the kissing test is 23/24-sharp while the Weyl test is 21/24-sharp.

- **Theorem 3 (Tier B)**: Partial extension to sporadic finite simple groups — 8 of 26 sporadics have orders factoring through $\mathcal{S}$. The boundary aligns with prime $23$ (the natural cutoff between Mathieu-sized and Conway/Leech-sized structures).

- **Theorem 4 (Tier A, Conway-Norton anchored)**: The prime $71$ appears in exactly one sporadic order — the Monster. Anchored by the Conway-Norton 1979 characterization of supersingular primes: $71$ is the largest prime $p$ for which the modular curve $X_0(p)$ has genus $0$, equivalently the unique upper bound of the genus-0 Hauptmodul spectrum.

Verification: 4 theorems + 2 companion observations (Eisenstein-prime classification of strata; $\mathrm{PG}(2, q)$ family strata-cleanness for $q \in \{2, 3, 4, 9\}$) all PASS at machine precision via `verify_J63.py` (~2 seconds, sympy + math).

**Closest published precedents**: Conway & Sloane, *Sphere Packings, Lattices and Groups* (3rd ed., 1999) for the Niemeier classification + lattice arithmetic; Conway-Curtis-Norton-Parker-Wilson, *Atlas of Finite Groups* (1985), for sporadic-group orders; Conway-Norton (1979, *Bull. London Math. Soc.* 11, 308) for the supersingular-prime characterization that anchors Theorem 4. Borcherds 1992 (the proof of the Conway-Norton conjecture) provides additional grounding.

**Tier discipline**: Two structural anchors are established (Theorem 2's polynomial-vs-factorial dichotomy + Theorem 4's Conway-Norton characterization). Three companion observations are explicitly Tier B/C. The intermediate-prime gap $\{17, 19, 23, 29, 31, 41, 47, 59\}$ is recorded as an open structural question (§7.2), not papered over.

**Originality**: original work, not under review elsewhere. No conflicts of interest.

**Suggested referees** (no co-authorship conflict): G. Nebe (RWTH Aachen) — lattices and codes expert; E. Bannai (formerly Kyushu) — algebraic combinatorics + designs; S. Lee (UC Berkeley) — modular forms + sphere packing.

We hope you find the work suitable.

Best regards,

Brayden R. Sanders (corresponding)
7Site LLC, Hot Springs, Arkansas, USA
brayden@7site.co

M. Gish
Independent Researcher, Hot Springs, Arkansas, USA
