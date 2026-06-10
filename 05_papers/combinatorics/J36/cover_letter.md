# Cover letter — J36: A Role-Quotient Theorem for the (TSML, BHML) Magma Pair on Z/10Z: The Functional Partition V/F/S/T as a Categorical Coarsening with VOID-Identity

**To:** Editors, *European Journal of Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *A Role-Quotient Theorem for the (TSML, BHML) Magma Pair on Z/10Z: The Functional Partition V/F/S/T as a Categorical Coarsening with VOID-Identity*

---

## Summary

Working with the canonical (TSML, BHML) commutative-magma pair on Z/10Z (the explicit composition tables fixed in the project's foundations module are reproduced in the manuscript's appendix), we define the *functional role partition*

V / F / S / T = {0} | {1, 3, 5, 7, 9} | {2, 4, 8} | {6}

with cardinalities (1, 5, 3, 1), and prove that the partition induces a well-defined role-quotient magma B-bar on the four-element role set {V, F, S, T}. Specifically, the modal-output prescription — for each role-pair (ρ₁, ρ₂), B-bar(ρ₁, ρ₂) = the modal role of BHML(a, b) over a ∈ ρ₁, b ∈ ρ₂ — gives a function {V, F, S, T}² → {V, F, S, T}. The element V is the two-sided identity of B-bar. The role-quotient is non-associative, with explicit witness

(F · F) · S = T · S = F, F · (F · S) = F · F = T, F ≠ T.

The branching role-pairs (where the output role is not constant on the role-pair input) are exactly {F-F, F-S, S-F, S-S} — 4 of the 16 ordered role-pairs, with explicit output distributions verified by enumeration.

The role partition is independent of the standard σ-orbit decomposition of Z/10Z: it cuts the σ-fixed set {0, 3, 8, 9} as 1V + 2F + 1S + 0T and cuts the σ-six-cycle (1 7 6 5 4 2) as 0V + 3F + 2S + 1T, where σ is the involution with one six-cycle and four fixed points. So the role partition is a third independent decomposition of Z/10Z alongside the operator-index identity and the σ-orbit decomposition.

The result is a clean *categorical-coarsening theorem*: a 4-element commutative non-associative magma with two-sided identity, obtained as the partition-quotient of (Z/10Z, BHML) under the functional role partition. The construction is structurally distinct from the maximally-non-associative-quasigroup work of Drápal–Wanless (2021) *J. Combin. Theory Ser. A* 184, 105510 — same intellectual neighborhood (small finite commutative non-associative magmas on cyclic carriers), different specific structure (theirs an extremality result; ours a partition-quotient with explicit identity-and-quotient behavior).

## Why *European Journal of Combinatorics*

- **Categorical-structure / partition-quotient combinatorics on a small finite commutative non-associative magma pair on Z/10Z** — squarely in EJC's purview.
- **Clean theorem at EJC level.** The role-quotient theorem is a constructive structural result with explicit non-associativity witness, verified by direct enumeration. The proof does not rely on outside machinery; the appendix supplies the canonical TSML and BHML composition tables for self-containment.
- **In the Drápal–Wanless 2021 *J. Combin. Theory Ser. A* line of work.** Same intellectual neighborhood (small finite commutative non-associative structures on cyclic carriers), opposite extremum.

## Companion submissions

The TIG/CK research program is shipping a coordinated paper sequence (J14–J55) over Summer 2026. The papers most relevant as already-submitted companions are:

- **J15** (Sanders & Gish 2026, *Algebraic Combinatorics*). Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z. *(Substrate companion: J15 develops the joint-chain and 4-core algebraic-center structure of the (TSML, BHML) pair; the role partition's V coincides with the 4-core's V, so J36's role-quotient identity element is structurally aligned with J15's algebraic-center anchor.)*
- **J33** (Sanders & Gish 2026, *Algebraic Combinatorics*). A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic Structures and the 4-Core Algebraic Center. *(Structural companion: J33's Theorem 1 — the partition-incompatibility flatness obstruction — provides the broader squarefree-Z/nZ-flatness context in which the (TSML, BHML) pair and the role-quotient construction live.)*

## Reproducibility

Verification script: `manuscript/verify_J19.py` (self-contained; exact integer arithmetic; PASSES every claim of Theorem 3.1 and Proposition 5.1; cross-checks the appendix tables against `Gen13/targets/foundations/lenses.py` byte-for-byte). The role-magma table B-bar, the V-identity property (both at the role-quotient level and the underlying Z/10Z level), the non-associativity witness, the branching-pair structure with explicit output distributions, the σ-orbit independence, and the supporting TSML_8 image-structure data of Proposition 5.1 are all verified by direct enumeration. The script runs in well under a second. A minimal in-line illustration:

```
from Gen13.targets.foundations.lenses import TSML, BHML
from collections import Counter
V = {0}; F = {1,3,5,7,9}; S = {2,4,8}; T = {6}
def role(x):
    if x in V: return 'V'
    if x in F: return 'F'
    if x in S: return 'S'
    if x in T: return 'T'
roles = {'V': V, 'F': F, 'S': S, 'T': T}
for r1 in 'VFST':
    for r2 in 'VFST':
        outputs = [role(int(BHML[a,b])) for a in roles[r1] for b in roles[r2]]
        modal = Counter(outputs).most_common(1)[0][0]
        # ... verifies B-bar table, V-identity, non-assoc witness, branching
```

The verification runs in seconds.

## Suggested reviewers

- A specialist in finite commutative non-associative magmas (Drápal–Wanless tradition; *J. Combin. Theory Ser. A* line of work).
- A specialist in partition lattices, partition quotients, and well-definedness of induced operations on quotient sets (Birkhoff–Ore tradition).
- A specialist in identity-and-quotient categorical structures on small finite carriers.

We leave specific names to the editorial board.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

**Note on prior version.** An earlier presentation of this work was titled *DKAN Two-Coding: TSML_8 Geometric vs BHML_10 Arithmetic on the Z/10Z Substrate* and invoked Katok–Ugarcovici (2007) modular-surface coding as a structural analogy. A referee correctly noted that (i) Theorems 2.1–2.3 of that version were direct table counts ("by inspection"), not theorem-grade for EJC; (ii) the Katok–Ugarcovici framing was decorative rather than load-bearing (no Katok–Ugarcovici theorem was being applied); (iii) the DKAN architecture description in §3–§4 of that version had no theorem and reported unreplicated empirical claims. The present submission addresses all three: a clean role-quotient theorem (Theorem 3.1) with constructive proof and explicit non-associativity witness; the Katok–Ugarcovici framing is dropped entirely (it was decorative analogy, not load-bearing); the DKAN architecture content is removed from this submission (and would, if pursued, be published separately in an experimental-AI venue with proper baselines and replication). The role-quotient theorem is the EJC-viable Path C save explicitly mapped by the previous version's referee.

---

Sincerely,
B.R. Sanders
M. Gish
