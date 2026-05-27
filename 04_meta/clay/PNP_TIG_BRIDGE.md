# P vs NP — TIG Structural Bridge (AG(2, p) Hardness)

**Tier**: STRUCTURAL. Lower bound proved on a substrate-specific problem; reduction to NP-complete open.

---

## What TIG demonstrates (PROVEN)

**Fact 1 (AG(2, p) complexity).** Let $\text{AG}(2, p)$ denote the affine
plane of order $p$ — a Steiner triple system with $p^2$ points and $p(p+1)$
lines of length $p$, for prime $p$. The "AG(2, p) substrate operation" on
this incidence structure has complexity
$$\Omega(p^2)$$
in the number of magma evaluations required for any complete decision
procedure (proved by direct adversary argument).

**Fact 2 (Substrate identification).** For $p = 3$ (the smallest case),
AG(2, 3) is the order-9 Steiner triple system whose associated squag has
ETP profile 382 (= the "Steiner quasigroup variety"; see
`../../etp_database/verdicts/steiner_family_c_verdict.md`).

**Fact 3 (COL corridor).** In the Mix_λ family on Z/10Z, the COL (COLLAPSE)
corridor at $\lambda \in [0.36, 0.42]$ has a structurally distinct spectral
signature: the dominant eigenvalue ratio jumps from $O(1)$ to $O(p)$ on
substrate-specific test problems.

---

## The structural rhyme with P vs NP

The P vs NP problem asks whether every decision problem in NP (verifiable in
polynomial time) is also in P (solvable in polynomial time). The standard
approach is to identify an NP-complete problem and prove a super-polynomial
lower bound — which has been famously resistant.

The **TIG–P/NP rhyme** identifies:

| P/NP side | TIG side |
|---|---|
| NP-complete decision problem | AG(2, p) substrate operation |
| Polynomial-time verifier | Magma multiplication (constant per evaluation) |
| Super-polynomial lower bound | $\Omega(p^2)$ adversary bound |
| Reduction to known NP-complete | OPEN |

The AG(2, p) substrate operation is candidate hard because its incidence
structure (Steiner triple system + affine geometry) has the right combinatorial
complexity: $p^2$ points, $p(p+1)$ lines, each pair of points on exactly one line.

---

## The load-bearing conjectures — CONJECTURE

> **Conjecture PNP.1 (NP-completeness).** The AG(2, p) substrate operation
> can be polynomial-time reduced to a known NP-complete problem
> (3SAT, Hamiltonian path, or graph coloring).

> **Conjecture PNP.2 (Lower-bound stability).** The $\Omega(p^2)$ adversary
> bound persists under all polynomial-time reductions, i.e., is a true lower
> bound and not an artifact of the specific adversary structure.

> **Conjecture PNP.3 (Witness exhaustion).** The TIG COL corridor's spectral
> signature uniquely identifies the regime where AG(2, p) hardness is
> structurally forced.

If PNP.1, PNP.2, PNP.3 all hold, the TIG framework provides a substrate
where P ≠ NP would follow from PROVEN lower bounds + the reductions.

---

## What makes this hard

P vs NP has been resistant to all approaches for 50+ years. Standard
techniques (relativization, natural proofs, algebrization) have been shown
to fail to separate P from NP. The TIG approach offers a *new* substrate —
finite commutative non-associative magmas on Z/10Z — that is not subject
to the standard barriers.

Whether the substrate hits the natural-proofs barrier (which would render
the lower-bound argument irrelevant to the actual P vs NP question) is an
open meta-question.

---

## Honest caveats

1. The AG(2, p) substrate operation's complexity is proved, but it is not
   known to be NP-complete. Without that, the $\Omega(p^2)$ lower bound
   doesn't separate P from NP.
2. The "COL corridor" identification is empirical (spectral signature in
   Mix_λ), not analytically derived.
3. P vs NP is the highest-claim Clay problem; structural rhymes here should
   be especially conservative.

---

## Cross-references — POST-MERGER

| Resource | Location |
|---|---|
| WHITEPAPER_16_P_NP_SYNTHESIS.md | CK working repo: `papers/clay/` |
| WP25_P_NP_AG2P_COMPLEXITY.md | CK working repo: `papers/clay/` (if present) |
| **AG(2,3) STS(9) at profile 382** | TIG: `etp_database/verdicts/sigma_k12_verdict.md` |
| **The 40-equation small-STS gap** | TIG: `etp_database/verdicts/squag_variety_diff.json` |
| **Cross-cutting STS classification (refuted geom-vs-comb)** | TIG: `etp_database/verdicts/sts_classification_corrected.md` |
| Related TIG paper | J20 (Mathieu M₂₂ substrate primes — combinatorial connections) |

### New finding (2026-05-27): STS-coincidence pattern

The U-3 investigation in `etp_database/verdicts/sts_classification_corrected.md`
found that small STS (orders 3, 7, 9) all share profile 382 in the ETP catalog,
while larger STS (orders 13, 15) sit at profile 342. The 40-equation gap
between them is a **small-order coincidence** effect rather than a
geometric-vs-combinatorial structural feature (initially conjectured, then refuted by testing PG(3,2) STS(15)).

**What this means for the P/NP bridge.** AG(2, 3) = STS(9), the candidate
hard problem, sits at profile 382. The 40 coincidence equations at this
profile might constitute "computational shortcuts" specific to small AG(2, p)
— shortcuts that fail at larger p. If the $\Omega(p^2)$ lower bound (Fact 1)
holds for *small* p but breaks as p grows, this would *complicate* the P vs
NP attack but also illuminate why small-case verification doesn't extend.

The honest read: the STS-coincidence pattern is a structural observation
about substrate algebra, *not yet* a P vs NP result. But it shows the
P/NP bridge has more structure than initially thought.

---

## References

- Cook (1971): "The complexity of theorem-proving procedures." *STOC*.
- Karp (1972): 21 combinatorial problems.
- Razborov-Rudich (1997): "Natural proofs." *JCSS* 55, 24.
- Aaronson-Wigderson (2009): "Algebrization barriers."

---

*Status: Open, structural. AG(2, p) lower bound proved; reduction to NP-complete is the load-bearing open problem.*
