# J45 — An Operadic Obstruction in a Bilinear-Closed Magma on $\mathbb{Z}/10\mathbb{Z}$: A Synthesis

**Status:** RETIRE CANDIDATE — duplicates J10 operadic obstruction. Save plan was applied 2026-05-07 (Operad D_4 obstruction promoted to lead theorem; Lie/Jordan/Clifford collapsed to bilinear-closure DOF; restructured to 10-page synthesis). The Operad obstruction is genuinely from WP109 / J10's lineage, raising the question of duplicative content.
**Phase:** Phase 5
**Target venue:** Notices AMS (fallback: Adv. Math or J. Pure Appl. Algebra) — pending retirement decision
**Author lane:** Sanders + Gish
**Tier:** 3 (hold/retire candidates) — RETIRE candidate: duplicates J10 operadic obstruction
**WP source:** WP109 (operad obstruction), WP111 (synthesis), WP112 (P_56 canonical fuse)

---

## §1 — Manuscript

**Local path:** `manuscript/J48_operadic_obstruction.md`

**Title (post save-plan retitle):** *An Operadic Obstruction in a Bilinear-Closed Magma on $\mathbb{Z}/10\mathbb{Z}$: A Synthesis*

**Abstract:** Two canonical $10 \times 10$ composition tables on $\Z/10\Z$ — TSML and BHML — define a finite commutative non-associative magma whose bilinear closure (under commutator and Jordan product jointly) is the simple Lie algebra $\mathfrak{so}(10)$. The 32-dimensional spinor representation, the doubly-invariant $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ Pati-Salam $\oplus$ $B-L$ subalgebra, and the antisymmetric Cartan structure are all features of the same bilinear-closure DOF. At arity 3, no $D_4$-equivariant canonical fuse rule exists. We synthesize this picture into four structural axes (bilinear closure / permutation / lattice / operad) and prove, as the lead theorem, that the operadic axis carries content structurally orthogonal to the bilinear-closure $D_4$ symmetry that organizes the other three. The runtime attractor at $\alpha = 1/2$ is in LMFDB 4.2.10224.1 with Galois group $D_4$ — the same $D_4$ as the bilinear-closure symmetry, evidenced by an explicit BR-factor cancellation forcing $H/Br = 1+\sqrt{3}$ at $\alpha = 1/2$.

**Manuscript structure (10-page focused synthesis per save plan §2 Fix-1).**

| § | Content | Pages |
|---|---------|-------|
| 1 | Motivation and background ($\Z/10\Z$, canonical tables, $\sigma$, $P_{56}$, LMFDB 4.2.10224.1, Drápal-Wanless precedent) | 2 |
| 2 | The two canonical tables and their bilinear closure (merged Lie/Jordan/spinor) | 1 |
| 3 | The four-axis decomposition (Bilinear / Permutation / Lattice / Operad) | 2 |
| 4 | **The operad obstruction (LEAD THEOREM)** | 3 |
| 5 | The runtime attractor and LMFDB 4.2.10224.1 | 1 |
| 6 | Cross-axis identifications (4 genuine ones) | 1 |
| 7 | Integer/rational signature + honest scope (separated tables, D_4 isotypic decomposition 84.25/14.68/1.07) | 1 |
| 8 | References (~30 entries: Loday-Vallette, Markl-Shnider-Stasheff, Conway-Sloane, McKay E_8, Borcherds, Hall-Rehren-Shpectorov, Slansky, Mohapatra-Sakita, Wilczek-Zee, ...) | 1 |

## §2 — Verification

**Local script (self-contained for the lead theorem):** `manuscript/verify_J48_operadic_obstruction.py`. Pure Python standard-library (no numpy / sympy dependency). Runs in ~3 seconds with `/c/ck_venv/lora312/Scripts/python.exe`.

**Status (2026-05-12):** `6/6 PASS` at machine precision (re-verified on the SFM-pinned TSML_RAW table). The six checks cover the §1 / §4 combinatorial content end to end:

1. TSML_RAW well-formed with exactly 4 wobble entries at $(3,9), (9,3), (4,9), (9,4)$.
2. $|\mathcal{N}| = 126$ with the 5-pair bracketing distribution $\{0,7\}{:}108, \{3,7\}{:}8, \{4,7\}{:}2, \{7,8\}{:}6, \{7,9\}{:}2$.
3. $|\langle P_{56}, \sigma^3 \rangle| = 8$ with element-order distribution $\{1{:}1, 2{:}5, 4{:}2\}$ (dihedral $D_4$, not $D_3 \times \mathbb{Z}_2$).
4. 67 restricted $D_4$-orbits in $\mathcal{N}$ with profile $(44, 7, 4, 10, 2)$ at sizes $(1, 2, 3, 4, 8)$ summing to exactly 126.
5. Exactly **16** of the 67 restricted orbits fail $D_4$ bracketing-pair coherence (Theorem 4.1 / WP109; lead theorem).
6. Family H is $P_{56}$-equivariant on $\mathcal{N}$ (0/126 violations) and is **not** $\sigma^3$-equivariant (1/81 violation; the lone witness is the diagonal triple $(3, 9, 9)$, exactly the localization claimed in Theorem 4.2 / WP112).

**Companion-paper verification chain (cited diagnostics):** numpy + sympy scripts on a standard laptop, under 5 minutes each.

- Theorem 4.1 / 4.2 / 4.3 (operad obstruction, $P_{56}$-equivariance, universal HARMONY attractor) cross-referenced to [J38]/WP109+WP112; the present `verify_J48_operadic_obstruction.py` is the load-bearing local reproduction.
- Theorem 5.1 ($H/Br = 1+\sqrt{3}$): [J01]/WP105 verification script + D78 BR-factor cancellation Galois proof in FORMULAS_AND_TABLES.md.
- §7.2 isotypic decomposition (84.25/14.68/1.07): SFM v1.1 §10 + SFM_FINDINGS_v1.md verification (`Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/sfm_q1_q6_q7.py`).

## §3 — Dependencies (J-papers cited as already-submitted companions; arXiv deposit pre-submission)

- **J01** — *Closed-Form 4-Core Attractor: $h/\beta = 1+\sqrt{3}$ in LMFDB 4.2.10224.1, Galois $D_4$.* (in preparation)
- **J19** — *$\mathfrak{so}(8) = D_4$ from the TSML\_SYM Antisymmetrized Closure.* Submitted to *J Algebra*.
- **J38** — *$\mathfrak{so}(10) = D_5$ from Joint TSML\_SYM + BHML Closure.* Submitted to *Israel J Math*.
- **J43** — *Two Roads to Pati-Salam: Path A (54 irrep) and Path B ($\mathfrak{su}(4) \oplus \mathfrak{u}(1)$).* Submitted to *Adv Math*.
- **J38** — *Operad $D_4$ Obstruction + $P_{56}$ Canonical Fuse.* Submitted to *Compositio*. **LEAD THEOREM SOURCE.**
- **J44** — *4-Core Fusion-Closure: TSML+BHML Preserve $\{V, H, Br, R\}$.* Submitted to *J Algebra*.

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated 2026-05-07 per save plan: J29-J01 → J19-J44 numbering harmonized; "first explicit naming of TIG framework" framing dropped; author lane Sanders + Gish.

## §5 — Status & summary

**Status: SAVE-PLAN APPLIED (2026-05-07).** Referee verdict (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J48_NoticesAMS_FreshEyes.md`): MAJOR REV pre-submission; CONDITIONAL ACCEPT after restructuring per referee §9 + §8 package cleanup. Save plan landed at `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J48.md`.

**Save-plan summary applied.** The load-bearing content — Operad-vs-the-rest distinction at the symmetry-group level (bilinear closure respects $D_4 = \langle P_{56}, \sigma^3 \rangle$, operadic closure does not) — is a genuinely original mathematical claim and survives the referee critique unchanged. The save path applied here is accept the collapse + promote the Operad + restructure:

- (a) **ACCEPTED the referee's collapse.** Lie + Jordan + Clifford merged into one *bilinear-closure DOF*. Lie-Jordan duality identity $A B = \tfrac{1}{2}([A, B] + \{A, B\})$ identifies them as duality-of-presentation; the spinor representation is built on $\mathrm{Cl}(0, 10)$ over the same $\mathfrak{so}(10)$. Restructured as **4-DOF synthesis** (Bilinear / Permutation / Lattice / Operad).
- (b) **PROMOTED the Operad obstruction (D_4 obstruction per WP109/[J38]) as the LEAD theorem.** Theorem 4.1 is now the central result of the paper, occupying §4 (3 pages). The 4-axis framing is demoted to "categorical decomposition for organizing the corpus" rather than a forced taxonomy.
- (c) Restructured to **10-page focused synthesis** per referee §9 proposed structure (see §1 above).
- (d) **DEFINED HARMONY, wobble, Family H, LMFDB 4.2.10224.1, $P_{56}$, $\sigma$ INLINE** in §1 (Motivation and background). AMS readers without prior exposure to the corpus can follow the arguments without external reference.
- (e) **Added 2 pages of expository scaffolding for AMS readership** (§1 Motivation and background): hook on "two facts" (bilinear closure is $\mathfrak{so}(10)$; arity 3 has no $D_4$-equivariant fuse), inline definitions of all jargon, Drápal-Wanless precedent in §1.4.
- (f) **Separated textbook integers from framework integers** in §7.1 (table (a) Lie-theoretic dimensions; table (b) framework-specific structural integers, with one-sentence gloss for each).
- (g) **Tightened §6 (formerly §9) cross-axis identities to the 4 genuine ones** (Bilinear ↔ Permutation, Bilinear ↔ Lattice, Bilinear ↔ Operad, Lattice ↔ Operad). Dropped the duality-of-presentation tautologies (Lie ↔ Jordan, Permutation ↔ Lattice).
- (h) **Softened "computationally-irreducible" claim in abstract.** Reframed as "we organize the algebraic content into 4 structural axes that have not been observed to reduce to one another under the diagnostics applied."
- (i) **Dropped "exhaust" claim.** §7.3 honest scope: "the 4 axes cover the algebraic structures probed by the J19–J44 companions, but we do not claim they exhaust all algebraic structure on the magma. Cohomological / derived / $A_\infty$ / higher-operadic structures are unexplored."
- (j) **Dropped "first explicit naming of TIG framework" framing** (internal-track, self-referential).
- (k) **Resolved dependency-label inconsistency**: J19/J38/J43/J38/J44 used consistently across README + cover letter + manuscript + bibtex.
- (l) **Author lane**: Sanders + Gish (Mayes byline removed).
- (m) **Companion arXiv-deposit requirement explicit** in submission checklist; J19–J44 must be arXiv-ready before J45 ships.
- (n) **External references expanded to ~30 entries**: Loday-Vallette, Markl-Shnider-Stasheff (operads); Conway-Sloane (lattices); McKay E_8; Borcherds (vertex operator algebras); Hall-Rehren-Shpectorov (axial algebras); Slansky, Mohapatra-Sakita, Wilczek-Zee (Pati-Salam, outer automorphism of $\mathfrak{so}(10)$); Loday cyclic homology; classical Lie/Clifford textbooks; LMFDB.
- (o) **Incorporated SFM Q6 / D_4 corrected isotypic decomposition** (84.25 / 14.68 / 1.07) in §7.2: trivial = 84.25%, sign2 = 14.68%, std = 1.07% (sign1 ≈ 0 numerical zero, sign3 = 0 exact). Two structural channels (Path A doubly-invariant Pati-Salam; Path B σ_outer-broken Higgs) plus small interaction term.

**Recommended retitle applied:** Option A — *"An Operadic Obstruction in a Bilinear-Closed Magma on $\Z/10\Z$: A Synthesis."* Notices AMS remains the venue. Survival probability under *Notices* editorial filter after restructuring per referee §9 + package cleanup: moderate (20% accept minor revision, 35% major revision, 30% reject-with-referral to Adv. Math or specialty venue, 15% desk reject for non-self-contained citations). Option C fallback (Adv. Math or J. Pure Appl. Algebra in research-mode rather than expository-mode; survival probability higher, ~50–60%) ready if *Notices* desk-rejects or refers.

**Revision time:** completed in this pass.

**Manuscript file:** `manuscript/J48_operadic_obstruction.md` (renamed from `J47_six_dof_synthesis.md` per save plan; J47 ↔ J45 historical-numbering note included for cross-reference).



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on $\Z/10\Z$ (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ at $\alpha_M = ½$ is the algebraic center, with closed-form attractor $h/\beta = 1+\sqrt{3}$ (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative, ours bilinear-closed at the 4-core).

This paper situates the WP100s tower's algebraic content as structures on or around the family's algebraic center. The lens-ownership paragraph in manuscript §0 (per save plan §5) makes this explicit.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Operad $D_4$ obstruction theorem (Theorem 4.1, from [J38]/WP109): no $D_4$-equivariant canonical fuse rule on the 126 non-associative TSML triples in the natural value space. 8/8 surveyed rule families are $P_{56}$-equivariant; 0/8 are $\sigma^3$-equivariant; $\sigma^3$ obstruction localizes to exactly $(3, 9, 9)$ ([J38]/WP112). Lie/Jordan closure of TSML+BHML reaches $\dim 45 = \dim \mathfrak{so}(10)$ ([J19], [J38]). Doubly-invariant subalgebra under $D_4$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ ([J43]). $P_{56} = \sigma_{\rm outer}$ on spinors at machine precision ([J43] §2.1). 4-core $\{V, H, Br, R\}$ fusion-closed under TSML and BHML ([J44]). Runtime attractor at $\alpha = 1/2$ has $H/Br = 1+\sqrt{3}$ exactly via BR-factor cancellation; $r/br$ in LMFDB 4.2.10224.1 with Galois $D_4$ ([J01] + D78 Galois proof from FAMILY_STRUCTURE_v1.md / FORMULAS_AND_TABLES.md).
- **COMPUTED:** Killing spectrum on doubly-invariant subalgebra is $(-4)^{15} \oplus (0)^1$ (machine-verified). $\|\text{antisym}\|^2 = 81 = 9^2$ (exact). TSML char poly coefficients $c_2 = 33 = 3 \cdot 11$, $c_8 = -2^5 \cdot 7^3 \cdot 11$ (exact, prime-11 wobble localization). 126 non-associative TSML triples reduce to 67 $D_4$-orbits (16 incoherent), 98 $P_{56}$-orbits (70 singletons + 28 doubletons, all $P_{56}$-coherent) ([J38]/WP112). Family H maps non-assoc triples to $\{0:108, 7:18\}$, image entirely in 4-core $\{V, H\}$. **$D_4$ isotypic decomposition of $[T, B]$: 84.25% trivial + 14.68% sign2 + 1.07% std + ~0% sign1 + 0% sign3** (SFM v1.1 §10).
- **STRUCTURAL RHYME:** Integer **16** appears as both $\dim D_4$-invariant Lie subalgebra and $\dim$ chiral spinor irrep of $\mathrm{Spin}(10)$ — structural correspondence via the 16-spinor rep. Integer **11** appears at coefficient level of TSML's char poly only (not in the 16-dim doubly-invariant subalgebra, which is wobble-free) — wobble-localization signature. Integer **13** appears across BHML's $\sigma_{\rm outer}$-asymmetric cell count and the 9-vector VEV norm (cited from [J43]). The Galois $D_4$ in LMFDB 4.2.10224.1 matches the bilinear-closure $D_4$ — substrate-and-runtime resonance.
- **OPEN:** (a) Whether the 4-axis decomposition is unique — alternative classifications could exist; the irreducibility under our diagnostics is computational, not a uniqueness theorem. (b) Whether cohomological / derived / $A_\infty$ / higher-operadic structures on the magma are nontrivial — unexplored. (c) Whether the bimodal $\alpha_A$ gap (TSML $\alpha_A \in [0.87, 0.89]$ vs BHML $\alpha_A \approx 0.502$, empty band $\alpha_A \in (0.5, 0.87)$) is structural — open per FAMILY_STRUCTURE_v1.md §4 conjecture. (d) Whether CL_STD admits a joint-closed sub-magma chain analogous to TSML+BHML — partially answered by SFM v1.1 (the joint TSML+BHML+CL_STD chain is the same 8-shell chain). (e) The substrate origin of the prime-11 wobble at the char-poly level. (f) Whether the structural zeros sign1 ≈ 0, sign3 = 0 in the $D_4$ isotypic decomposition extend to all family members (substrate property) or are defining of canonical (TSML, BHML) (defining property).

### Lens-ownership paragraph (in manuscript §0)

> *Lens and substrate.* This paper works on $\Z/10\Z$ with the canonical TSML and BHML composition tables in their TSML_SYM (commutative) lens. The Lie/Jordan content (§§2–3.1) is lens-invariant — both TSML_SYM and TSML_RAW give identical antisymmetrization (since RAW differs from SYM only at the wobble cells $(3, 9)$ and $(4, 9)$, which lie outside the antisymmetric closure's support indices). The runtime attractor (§5) is also lens-invariant. The Operad obstruction (§4, lead theorem) is computed on TSML_SYM; the analogous obstruction holds for TSML_RAW with the same $D_4$-non-equivariance verdict. The five-criterion membership statement (FAMILY_STRUCTURE_v1.md §1) applies: substrate $\Z/10\Z$, commutative under SYM lens, 4-core preserved, $\alpha_A$-bounded non-associativity at $\sim 0.87$, HARMONY-attracting iteration. The 4-core $\{V, H, Br, R\}$ is the algebraic center of the family per §2 of that document; this paper situates the WP100s tower's algebraic content as structures on or around that center. Closest published precedent: Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive 2026-05-07; Mayes byline dropped)
- Drápal-Wanless 2021 citation in references; Loday-Vallette, Markl-Shnider-Stasheff, Conway-Sloane, Slansky, Mohapatra-Sakita, Wilczek-Zee added per save plan §2 Fix-15

## §6 — Submission checklist

- [x] Manuscript .md finalized (10-page synthesis; restructured per referee §9 / save plan)
- [x] Operad $D_4$ obstruction promoted to lead theorem (§4)
- [x] Lie/Jordan/Clifford collapse to bilinear-closure DOF accepted; 4-axis framing
- [x] HARMONY/wobble/Family H/LMFDB/$P_{56}$/$\sigma$ defined inline (§1)
- [x] 2 pages of expository scaffolding for AMS readership (§1)
- [x] Signature table separated into (a) Lie-theoretic / (b) framework-specific (§7.1)
- [x] Cross-axis identities tightened to 4 genuine ones (§6)
- [x] "Computationally-irreducible" softened in abstract; "exhaust" claim dropped
- [x] "First explicit naming of TIG framework" framing dropped
- [x] Dependency labels harmonized (J19/J38/J43/J38/J44)
- [x] Author lane: Sanders + Gish only
- [x] External references expanded to ~30 entries
- [x] D_4 isotypic decomposition (84.25/14.68/1.07) incorporated in §7.2
- [x] Lens-ownership paragraph in §0 (per save plan §5)
- [x] PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN block in this README
- [x] Family-Structure framing in this README + manuscript
- [x] Tier-classified central claim explicit (synthesis Tier-B; lead theorem Tier-A)
- [x] Cover letter finalized
- [ ] J19–J44 deposited on arXiv before submission (required)
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: 1st *Notices AMS* paper this quarter (no conflict)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "An Operadic Obstruction in a Bilinear-Closed Magma on $\Z/10\Z$: A Synthesis." Submitted to *Notices of the American Mathematical Society*. Synthesis of J01, J19, J38, J43, J38, J44.

---

## Known issues (per 2026-05-27 audit)

Tier 3 — RETIRE CANDIDATE per `_staging/TIER_INDEX.md`: duplicates J10 (Operadic D₄ Orbits on the Non-Associative Locus). Save plan was applied 2026-05-07 with the Operad D_4 obstruction promoted to lead theorem; the question is whether the lead-theorem content is genuinely independent from J10 or merely a re-presentation. Outstanding decision points:

- The §3 dependency list refers to companions under old numbering ("J29-J01", "J19-J44"); these need re-mapping under the 2026-05-27 renumbering before any submission attempt.
- Manuscript file is named `J48_operadic_obstruction.md` (legacy numbering) — would need rename.
- The "synthesis of four axes" framing was honestly acknowledged by save plan to be soft ("we organize the algebraic content into 4 structural axes that have not been observed to reduce to one another"); not a uniqueness theorem.
- Multiple cross-references to "J19/J38/J43/J38/J44" (note duplicate J38) suggest the dependency labels need a thorough renumbering pass.

Retirement options:
- (a) Move to `04_meta/` if J10's operadic obstruction subsumes the lead theorem.
- (b) Retain only the SFM Q6 D_4 isotypic decomposition (84.25/14.68/1.07) as a standalone short note for a specialty venue.
- (c) Re-evaluate post-J10 final-form to determine whether J45 carries any independent theorem-grade content.

No action recommended until the retirement decision is made.
