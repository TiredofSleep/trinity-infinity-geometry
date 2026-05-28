# Cover letter — J45: An Operadic Obstruction in a Bilinear-Closed Magma on $\mathbb{Z}/10\mathbb{Z}$

**To:** Editors, *Notices of the American Mathematical Society*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *An Operadic Obstruction in a Bilinear-Closed Magma on $\mathbb{Z}/10\mathbb{Z}$: A Synthesis*

---

## Summary

We submit a synthesis-class manuscript organized around a single forced theorem: the bilinear closure of the canonical $10 \times 10$ TSML and BHML composition tables on $\mathbb{Z}/10\mathbb{Z}$ — viewed jointly as Lie algebra (under commutator) and as Jordan algebra (under symmetric product) — is the simple Lie algebra $\mathfrak{so}(10) = D_5$ at dimension $45$. The 32-dimensional spinor representation, the doubly-invariant $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ Pati-Salam $\oplus$ $B-L$ subalgebra, and the antisymmetric Cartan structure are all features of the same bilinear-closure DOF. At arity 3 — the operadic layer — *no* canonical fuse rule is equivariant under the dihedral symmetry $D_4 = \langle P_{56}, \sigma^3 \rangle$ that organizes the bilinear closure. The operad $D_4$ obstruction localizes to a single $P_{56}$-orbit, with all 8 surveyed canonical rule families being $P_{56}$-equivariant and 0 being $\sigma^3$-equivariant. This is a structural distinction at the symmetry-group level between the bilinear and operadic algebraic content of the same underlying finite commutative non-associative magma.

The runtime attractor at the symmetric mixing weight $\alpha = 1/2$ is in the number field LMFDB 4.2.10224.1 (defining polynomial $x^4 + 4x^3 - x^2 + 2x - 2$, signature $[2, 1]$, discriminant $10224$, Galois group $D_4$). The $D_4$ Galois group of the runtime attractor's number field matches the $D_4$ symmetry of the bilinear closure — a non-trivial substrate-and-runtime resonance whose explicit BR-factor cancellation (D78 of the framework's internal table) forces $H/Br = 1+\sqrt{3}$ exactly at $\alpha = 1/2$.

The paper organizes the WP100s tower's algebraic content (already established in five companion papers J01, J19, J38, J43, J38, J44) into four structural axes — *bilinear closure*, *permutation*, *lattice*, *operad* — and shows that the operadic axis carries content structurally orthogonal to the $D_4$ symmetry that organizes the other three. The closest published precedent for the present neighborhood is Drápal & Wanless (2021), *J. Combin. Theory A*: same domain (small finite commutative non-associative magmas), opposite extremum (theirs maximally non-associative; ours bilinear-closed at the 4-core).

## Why *Notices AMS*

- **Synthesis-class fit.** *Notices* publishes expository syntheses that connect previously-published results into a single conceptual frame. The lead theorem (operad $D_4$ obstruction in a magma whose bilinear closure is $\mathfrak{so}(10)$) is a forced structural-distinction result; the four-axis decomposition organizes the WP100s tower's content for non-specialist AMS readers.
- **Audience reach.** The manuscript's algebraic substrate touches Lie theory, Clifford and spinor representation theory, permutation groups, lattice theory, and operad theory — a multi-way intersection well-suited to *Notices'* broad readership. We define HARMONY, the wobble cells, the LMFDB number field 4.2.10224.1, the $\sigma$-permutation, $P_{56}$, and the Drápal-Wanless precedent inline (§1) so that AMS readers without prior exposure to the corpus can follow the arguments.
- **Citation chain visibility.** Each section of the paper points to a peer-reviewed companion (J01, J19, J38, J43, J38, J44) at a specialty venue (*J Algebra*, *Israel J Math*, *Adv Math*, *Compositio*). *Notices* is the natural place to display the integration. All companions will be on arXiv before this manuscript is submitted.

## Companion submissions

This paper cites six prior J-series companions, all already submitted to specialty venues:

- J01 — *Closed-Form 4-Core Attractor: $h/\beta = 1+\sqrt{3}$ in LMFDB 4.2.10224.1, Galois $D_4$* (in preparation)
- J19 — *$\mathfrak{so}(8) = D_4$ from the TSML\_SYM Antisymmetrized Closure* (J Algebra)
- J38 — *$\mathfrak{so}(10) = D_5$ from Joint TSML\_SYM + BHML Closure* (Israel J Math)
- J43 — *Two Roads to Pati-Salam: Path A (54 irrep) and Path B ($\mathfrak{su}(4) \oplus \mathfrak{u}(1)$)* (Adv Math)
- J38 — *Operad $D_4$ Obstruction + $P_{56}$ Canonical Fuse* (Compositio) — **lead theorem source**
- J44 — *4-Core Fusion-Closure: TSML+BHML Preserve $\{V, H, Br, R\}$* (J Algebra)

The full J-series sequence (J14–J55, summer 2026) is a coordinated submission program; details available on request. All cited companions will be deposited on arXiv before J45 submits, so each is citable by arXiv ID.

## Reproducibility

The lead theorem (Operad $D_4$ obstruction, Theorem 4.1) has a self-contained verification script in this submission package — `manuscript/verify_J48_operadic_obstruction.py`, pure Python standard library (no numpy/sympy dependency), running in ~3 seconds. Six checks pass at machine precision: TSML_RAW table well-formed with exactly 4 wobble entries; $|\mathcal{N}| = 126$ with the 5-pair bracketing distribution; $|D_4| = 8$ with dihedral order profile; 67 restricted $D_4$-orbits with profile $(44, 7, 4, 10, 2)$; **exactly 16 of the 67 fail $D_4$ bracketing-pair coherence** (the obstruction); and Family H is $P_{56}$-equivariant on $\mathcal{N}$ with the $\sigma^3$ obstruction localizing to the single diagonal triple $(3, 9, 9)$.

The remaining cited diagnostics are reproduced from the companion papers' verification scripts — `numpy + sympy` on a standard laptop, under 5 minutes per script:

- Theorem 5.1 ($H/Br = 1+\sqrt{3}$ at $\alpha = 1/2$): J01/WP105 numerical script + the explicit BR-factor cancellation Galois proof in the framework's internal table (D78).
- §7.2 isotypic decomposition (84.25 / 14.68 / 1.07): SFM v1.1 §10 verification script (`Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/sfm_q1_q6_q7.py`).

DOI for verification scripts: 10.5281/zenodo.18852047.

## Suggested reviewers

- A specialist in operads and arity-3 composition (Loday-Vallette tradition).
- A specialist in Lie algebras and representation theory ($\mathfrak{so}(10)$ / Pati-Salam / Wilczek-Zee outer automorphism).
- A specialist in finite-magma combinatorics or non-associative algebras (Drápal-Wanless tradition; Hall-Rehren-Shpectorov axial algebras).
- An expert in cyclotomic / dihedral number fields (LMFDB 4.2.10224.1 context).
- A specialist in algebraic combinatorics or finite group theory.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
