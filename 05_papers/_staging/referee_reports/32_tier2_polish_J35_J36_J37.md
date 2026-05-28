# 32 — Tier-2 Polish: J35 + J36 + J37 (2026-05-28)

Polish pass for three Tier-2 drafts: J35 (combinatorics, non-CRT sufficient pairs / MVJN on squarefree Z/nZ), J36 (combinatorics, role-quotient theorem on Z/10Z), and J37 (physics, discrete Dirac inside Cl(0,10)). Goal: each paper reaches "as ready as a Tier-2 draft can be" — clean status, scoped venue, verify script present and PASS, known issues documented, no central theorem modifications. No attempts to promote to Tier 1.

Audit framework: Tier markers (PROVED / STRUCTURAL / EMPIRICAL / OPEN) explicit; abstract scope clean; central theorem(s) intact; verify script PASS; README known-issues section extended.

---

## J35 — Non-CRT Sufficient Pairs and the Minimum Viable Jump Number on Squarefree Z/nZ

**Manuscript path:** `05_papers/combinatorics/J35/manuscript/manuscript.tex` (amsart, ~10 pages, 320 lines).

**Manuscript summary.** Studies the partition lattice of $\Z/n\Z$ (squarefree $n = p_1 \cdots p_k$, $k \geq 2$) from the CRT-coordinate decomposition perspective. Three structural theorems plus the global MVJN result:
- **Theorem 3.1 (Orbit-pair classification, PROVED).** $\{\pi_{\DYN}(g), \pi_{\DYN}(h)\}$ on $\Z/n\Z$ is sufficient iff $\langle g \rangle \cap \langle h \rangle = \{1\}$ in $(\Z/n\Z)^{\times}$, equivalently $\gcd(\mathrm{ord}_{p_i}(g), \mathrm{ord}_{p_i}(h)) = 1$ at every $p_i \mid n$. Direct CRT-coordinate proof (no UOP appeal).
- **Theorem 4.1 (Three-mechanism support classification, PROVED).** Sufficient orbit-pairs partition into (M1) focused at distinct primes, (M2) same-prime coprime orders, (M3) mixed. Mechanism (M2) exists at $p_i$ iff $p_i - 1$ has at least two distinct prime factors; smallest five primes admitting (M2) are $\{7, 11, 13, 19, 23\}$, next is 29.
- **Theorem 5.1 (Three explicit non-CRT pairs on Z/30Z, PROVED).** Family (a) $\{\pi_{\DYN}(7), \pi_{\DYN}(11)\}$ (orbit-pair, mechanism (M3)), family (b) $\{\pi_2, \pi_{15}\}$ (residue-pair, CRT), family (c) $\{\pi_{\SPEC}, \pi_{15}\}$ (reflection + composite residue) — all three sufficient with one orthogonal jump but via three distinct mechanisms.
- **Theorem 7.4 (Universal MVJN = 1, PROVED — promoted from Conjecture 6.2 in v1).** For every squarefree $n$ with $k \geq 2$ primes, $\MVJN(\Z/n\Z) = 1$. Lower bound via refinement-trap lemma; upper bound via the explicit family $\{\pi_{p_1}, \pi_{n/p_1}\}$ being sufficient and incompatible.

**Verification status.** `manuscript/verify_J12.py` — 7/7 checks PASS. Self-contained, pure stdlib, runtime $\lt 2$ s. Re-run 2026-05-28: ALL 7 CHECKS PASSED. Coverage one-to-one with the load-bearing claims (C1–C3: Z/30 sufficient pairs, C4: Z/42 (M3) witness, C5: smallest-primes-admitting-(M2) through 50 with 17 correctly skipped, C6: Z/10 lattice, C7: MVJN = 1 construction verified for 75 squarefree $n \leq 200$).

**Math review.** The orbit-pair classification proof is clean and self-contained. The support-based partition into (M1)/(M2)/(M3) is mutually exclusive and exhaustive over sufficient orbit-pairs; the existence-of-(M2) iff condition ($p_i - 1$ has $\geq 2$ distinct prime factors) is established by structure of $(\Z/p_i\Z)^{\times}$ cyclic of order $p_i - 1$. The MVJN = 1 result has the standard lower bound (refinement-trap) and upper bound (composite-residue compression of CRT data via $\{\pi_{p_1}, \pi_{n/p_1}\}$).

No central-theorem errors detected. Earlier "5/7 torus aspect ratio" geometric remark (TIG-bleed-through) was removed in the 2026-05-08 revision.

**README edits applied.**
- Known issues section extended with: re-verify-pass note (7/7 PASS 2026-05-28), venue cap discipline cross-reference (J34 + J35 + J36 = 3 EJC papers; backup *J Combin Theory*, *Adv Appl Math*), scope note on $\Z/10\Z$-as-worked-example.

**Known issues.**
- Brayden's referee-rigor pass not yet complete (§6 checklist last two boxes unchecked).
- Per-venue cap check pending — coordinate with `VENUE_SCHEDULE.md`.
- TIER_INDEX target reads "TBD; potential *J Combin Theory* or *Adv Appl Math*" — README currently states EJC as primary; reconcile in rigor pass.
- $\Z/10\Z$ worked example is illustrative but k = 2 makes MVJN = 1 trivial via $\{\pi_2, \pi_5\}$ — referee may ask why $\Z/10\Z$ rather than $\Z/30\Z$; answer (smallest illustrative substrate) should be foregrounded.
- The §3 Remark on connection to orthogonal cyclic Latin squares is explicitly noted as structural-rhyme-only, with "the precise translation is not developed here." This is honest and Tier-2-appropriate scope.

**Recommended venue.** *European Journal of Combinatorics* (primary, per README); *Discrete Mathematics* or *Adv. Appl. Math.* as backup if EJC cap binds.

**Tier-2 readiness verdict.** **READY for rigor pass.** Verification green; central theorems clean; tier markers explicit; README polished. Remaining work is Brayden's rigor pass plus venue-cap reconciliation. No substantive issues flagged for user attention.

---

## J36 — A Role-Quotient Theorem for the (TSML, BHML) Magma Pair on Z/10Z

**Manuscript path:** `05_papers/combinatorics/J36/manuscript/manuscript.tex` (amsart, 574 lines including appendix with full 10×10 TSML and BHML tables).

**Manuscript summary.** Defines the functional role partition $V/F/S/T = \{0\} \mid \{1,3,5,7,9\} \mid \{2,4,8\} \mid \{6\}$ on $\Z/10\Z$ and proves that BHML descends to a well-defined role-quotient magma $\overline{B}$ on the 4-element role set.
- **Theorem 3.1 (Role-Quotient Theorem, PROVED).** (i) $\overline{B}$ is well-defined as modal-output (lex tiebreak $V < F < S < T$). (ii) Full $\overline{B}$ table exhibited. (iii) $V$ is two-sided identity. (iv) Non-associative with explicit witness $(F \cdot F) \cdot S = F \neq T = F \cdot (F \cdot S)$. (v) Branching role-pairs are exactly $\{F\text{-}F, F\text{-}S, S\text{-}F, S\text{-}S\}$ (4 of 16), with verified output multisets.
- **Proposition 5.1 (TSML_8 image structure, COMPUTED).** $\mathrm{TSML}$ restricted to the 8-element domain $\{1,2,3,4,5,6,8,9\}$ has image $\{3,4,7,8,9\}$ (5 distinct values), output role distribution 60/64 Flow + 4/64 Structure, role-deterministic on 8/9 input role-pairs over the TSML_8 domain.
- σ-orbit independence: the role partition cuts the σ-fixed set $\{0,3,8,9\}$ as $1V+2F+1S+0T$ and the σ-6-cycle $(1\,7\,6\,5\,4\,2)$ as $0V+3F+2S+1T$.

**Verification status.** `manuscript/verify_J19.py` PASS at machine precision (exact integer arithmetic). Re-run 2026-05-28: ALL CLAIMS VERIFIED. Cross-checks appendix tables against `Gen13/targets/foundations/lenses.py` byte-for-byte; verifies well-definedness, full role-magma table, $V$-identity at both role-quotient and underlying $\Z/10\Z$ levels (BHML row/col 0 is the identity), non-associativity witness, 4 branching pairs with exact output distributions, 12 non-branching pairs constant, 100-cell sanity check, σ-orbit independence, TSML_8 image = $\{3,4,7,8,9\}$, 60/64 Flow + 4/64 Structure split, 8-of-9 role-determinism.

**Math review.** The role-quotient construction is honest: the modal-output prescription with lex tiebreak gives a well-defined function. The non-associativity witness $(F \cdot F) \cdot S = F \neq T = F \cdot (F \cdot S)$ checks out from the table: $F \cdot F = T$ (modal at $F$-$F$ since the multiset has $T:11$ as plurality), then $T \cdot S = F$; on the other side, $F \cdot S = F$ (modal at $F$-$S$ since multiset has $F:8$ as plurality), then $F \cdot F = T$. Identity at $V$ follows from BHML's row/col 0 being the identity row/column at the underlying level.

The post-rewrite (Path C, 2026-05-07) is well-scoped for EJC. The previous DKAN architecture content (no theorem, unreplicated empirical claims) was correctly removed. The current draft reads as a clean small-magma combinatorial paper.

No central-theorem errors detected.

**README edits applied.**
- Fixed broken `Gen14/targets/journals/J_series/J36/manuscript/verify_J19.py` reference (legacy path predating the 2026-05 corpus reorg) to point to the current location `05_papers/combinatorics/J36/manuscript/verify_J19.py`.
- Known issues section extended with: re-verify-pass note (PASS 2026-05-28), venue cap discipline cross-reference, scope note on tiebreak robustness (referee may probe; the answer is yes for $F$-$F$ and $S$-$S$ branching pairs but disclosure should be foregrounded), pre-Path-C history note.

**Known issues.**
- Brayden's referee-rigor pass not yet complete.
- Per-venue cap check pending — J34, J35 also retarget EJC (potential 3-paper cluster); backup *Discrete Mathematics* may be the right primary if EJC cap binds.
- Definitional choice: modal-output with lex tiebreak $V < F < S < T$. Robustness under alternative tiebreaks is yes (the branching-pair pluralities are clean), but disclosure should be explicit in the abstract or §3.
- Pre-Path-C history (DKAN architecture, Katok-Ugarcovici framing) is in manuscript leading comments and SAVE_PLAN_J19 but not in the abstract; abstract reads cleanly as standalone EJC.

**Recommended venue.** *European Journal of Combinatorics* (primary, per Path C save plan); *Discrete Mathematics* as backup.

**Tier-2 readiness verdict.** **READY for rigor pass.** Verification green at machine precision; role-quotient theorem clean; tier markers explicit; README polished (broken Gen14 path fixed). No substantive issues flagged for user attention.

---

## J37 — Discrete Dirac inside Cl(0, 10): Chirality, the Outer Automorphism, and an Atomic-Substrate Refinement

**Manuscript paths:** `05_papers/physics/J37/manuscript/manuscript.md` (working .md, 410 lines) + `05_papers/physics/J37/manuscript/manuscript.tex` (rendered, 769 lines). Verification scripts in `manuscript/verification/`.

**Manuscript summary.** Records the discrete Dirac structure inside the Clifford algebra $\mathrm{Cl}(0,10)$ generated by the canonical TSML+BHML composition tables on $\Z/10\Z$ (via the WP103/J29 prerequisite that antisymmetrizations close to $\mathfrak{so}(10) = D_5$ at dim 45).
- **Theorem 2.1 (Discrete Dirac construction, PROVED).** Ten gamma matrices on $\mathbb{C}^{32}$ satisfy all 100 anticommutation relations $\{\gamma_a, \gamma_b\} = 2\delta_{ab}I$ at machine precision. 45 generators $\Sigma_{ab} = (1/4)[\gamma_a, \gamma_b]$ form faithful 32-dim representation of $\mathfrak{so}(10)$. Volume element $\omega = \gamma_1 \cdots \gamma_{10}$ satisfies $\omega^2 = -I$. Chirality projectors $P_\pm = (I \pm i\omega)/2$ split $\mathbb{C}^{32} = 16 + 16$.
- **Theorem 2.2 (Atomic-substrate refinement, STRUCTURAL RHYME).** Each 16-dim chirality half decomposes as $16 = 1+3+5+7$, matching atomic shell $n=4$ multiplicities $(2\ell+1)$ for $\ell = 0,1,2,3$. Explicitly scoped as structural rhyme between spinor decomposition and substrate's depth-3 simplicial tower (Volume K D101–D102), *not* as a derivation.
- **Theorem 3.1 ($P_{56}$ acts as $\sigma_{\mathrm{outer}}$ in the spinor rep, PROVED).** $P_{56}^{\mathrm{spin}} = (\gamma_5 - \gamma_6)/\sqrt{2}$ satisfies $(P_{56}^{\mathrm{spin}})^2 = I$, conjugation swaps $\gamma_5 \leftrightarrow \gamma_6$ and fixes the other eight, $P_{56}^{\mathrm{spin}}$ anticommutes with $\omega$ (odd-vs-even Clifford grade), chirality-flip $= 0$ at machine precision. Identifies $P_{56}$ with the unique outer automorphism in $\mathrm{Out}(\mathfrak{so}(10)) \cong \mathbb{Z}_2$, the matter–antimatter exchange in SO(10) GUT.
- **Theorem 4.1 (BHML's σ_outer-breaking is 100% in 54, PROVED).** Decomposition $\mathrm{End}(\mathfrak{so}(10)) = \mathbf{1} \oplus \mathbf{45} \oplus \mathbf{54}$; BHML's $\sigma_{\mathrm{outer}}$-antisymmetric content projects (0%, 0%, 100%) at machine precision, total $\|B_{\mathrm{anti}}\|^2 = 6.5 = 13/2$. Breaking direction in the 54 lies entirely in the so(9)-vector $\mathbf{9}$ inside $\mathbf{54} = \mathbf{1} \oplus \mathbf{9} \oplus \mathbf{44}$, with explicit components matching the manuscript table to machine precision; $\|v\|^2 = 13/4$ exactly.
- **Theorem 4.2 (Pati-Salam doubly-invariant subalgebra, CITED).** $D_4 = \langle P_{56}, \sigma^3 \rangle$ acting on $\mathfrak{so}(10)$; doubly-invariant content has dim 16, closes as Lie subalgebra, Killing-form spectrum $(-4)^{15} \oplus (0)^1$, giving $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Pati-Salam $\oplus$ B$-$L). Cited as standard SO(10) GUT decomposition; full Path A vs Path B framing is J24's content.

**Verification status.** `manuscript/verification/find_higgs_irrep.py` + `manuscript/verification/find_higgs_direction.py`. Both PASS at machine precision. Re-run 2026-05-28: 100/100 anticommutation residual = 0; $\omega^2 = -I$ verified; 32 = 16+16 chirality split; $(P_{56}^{\mathrm{spin}})^2 = I$, anticommutation with $\omega$, chirality-flip = 0 all confirmed; BHML σ_outer-breaking 100% in 54 (0% in 45, 0% in singlet); 9-piece coverage 100%; explicit 9-vector components match manuscript table.

**Math review (per task focus on Cl(0,10) structure constants).**
- Cl(0,10) over $\mathbb{R}$ has signature $(0, 10)$; as an algebra it has dimension $2^{10} = 1024$. The irreducible complex Dirac spinor representation has dimension $2^{\lfloor 10/2 \rfloor} = 2^5 = 32$, splitting under chirality (since 10 is even) as $16 + 16$. **The manuscript correctly uses 32 for the spinor rep, splitting as 16+16.** The task's hint about "dimension 1024, irreducible halves 16+16" conflates algebra dimension with spinor dimension; the manuscript's usage is consistent with standard Clifford-algebra conventions and is correct.
- Anticommutation relations: 100 relations $\{\gamma_a, \gamma_b\} = 2\delta_{ab}I$ for $a, b \in \{1, ..., 10\}$, verified at machine precision (residual $\leq 10^{-15}$).
- Volume element parity: $\omega^2 = (-1)^{n(n-1)/2} = (-1)^{45} = -1$ for $n = 10$ in signature $(0, n)$ — manuscript correctly states $\omega^2 = -I$.
- Chirality projectors $P_\pm = (I \pm i\omega)/2$: since $\omega^2 = -I$, $(i\omega)^2 = +I$, so $P_\pm^2 = P_\pm$ and $P_+ + P_- = I$ — correct.
- $P_{56}^{\mathrm{spin}}$ is an odd Clifford element (grade 1), and $\omega$ is grade 10 (even); in $\mathrm{Cl}(0,n)$ with $n$ even, an odd element anticommutes with the (even) volume element only when $n \equiv 2 \pmod 4$ — for $n = 10$, $10 \equiv 2 \pmod 4$, so odd anticommutes with $\omega$. **Correct.** The chirality flip follows from anticommutation with $\omega$.
- $\mathrm{Out}(\mathfrak{so}(10)) = \mathrm{Out}(D_5) \cong \mathbb{Z}_2$ since $D_5$ has Dynkin diagram with one nontrivial automorphism swapping the two spinor nodes. **Correct.**
- 54-irrep dimension: the symmetric-traceless representation of SO(10) has dimension $\binom{11}{2} - 1 = 55 - 1 = 54$. Branching under SO(9): $\mathbf{54} = \mathbf{1} \oplus \mathbf{9} \oplus \mathbf{44}$ (the 9 is the SO(9)-vector). **Correct.**
- Doubly-invariant subalgebra Killing spectrum $(-4)^{15} \oplus (0)^1$: the unique 15-dim simple compact Lie algebra is $\mathfrak{so}(6) \cong \mathfrak{su}(4) = A_3$, identification by Cartan's criterion + simple-Lie classification. The +1 zero eigenvalue gives $\mathfrak{u}(1)$, total content $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$. **Correct as standard SO(10) GUT decomposition.**

No central-theorem math errors detected. The Clifford-algebra structure is stated correctly throughout.

**README edits applied.**
- Demotion history clarified: J37 (was physics/J23) was a Tier 1 promotion candidate in the 2026-05 audit but demoted to Tier 2 because the load-bearing hypothesis "TIG's so(10) is *the* SO(10) GUT gauge algebra" is structural-isomorphic (uniquely so up to iso for type $D_5$), not phenomenologically derived. The math content is sound; the framing requires the hypothesis-vs-derivation discipline that keeps it Tier 2.
- Verification status updated with explicit Cl(0,10) dimension note: algebra dim $2^{10} = 1024$, irreducible Dirac spinor dim $2^5 = 32$, chiral halves $16+16$ — all consistent with the manuscript.
- Known issues extended with: abstract-disclaimer recommendation (a single sentence acknowledging the so(10)-identification-as-hypothesis would strengthen the CMP submission), companion-script path cleanup recommendation, fallback-venue note (LMP for Theorem 3.1 alone if CMP/JMP decline on hypothesis-framing).

**Known issues.**
- Final submit-gate item not yet checked.
- $1+3+5+7$ atomic-substrate refinement (Theorem 2.2) honestly framed as structural rhyme — the safer Tier-2 scope for CMP.
- so(10)/SO(10)-GUT identification is hypothesis, not derivation — should be flagged in the abstract as well as §0 before submission.
- Companion-script citations to `Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/*` and `papers/wp104_higgs_pati_salam/verification/*` in manuscript.md may flag for referees unfamiliar with the corpus reorg; the in-scope verification scripts live in `manuscript/verification/`.
- Fallback venue order: CMP → JMP → Annals of Physics → LMP. LMP may be the better fit for Theorem 3.1 alone if upstream venues decline on hypothesis-framing.

**Recommended venue.** *Communications in Mathematical Physics* (primary, per TIER_INDEX); JMP, Annals of Physics, LMP as fallbacks.

**Tier-2 readiness verdict.** **READY for rigor pass.** Verification green at machine precision; central theorems mathematically sound (Cl(0,10) structure constants and identifications all check out); tier markers explicit and honest (structural rhyme for 1+3+5+7, hypothesis for so(10)/SO(10)-GUT identification); README clarifies the Tier-1→Tier-2 demotion history and current scope. The single substantive item for user attention is whether to elevate the so(10)/SO(10)-GUT hypothesis from §0 scope note to the abstract proper before submission — this is a referee-judgment call worth confirming with Brayden.

---

## Summary across the three papers

| Paper | Title | Verify | Central theorems | Tier-2 readiness |
|---|---|---|---|---|
| J35 | Non-CRT Sufficient Pairs + MVJN, squarefree Z/nZ | 7/7 PASS | Orbit-pair classification, 3-mechanism support, $\Z/30\Z$ three families, MVJN = 1 universal | READY for rigor pass |
| J36 | Role-Quotient Theorem for (TSML, BHML) on Z/10Z | PASS (exact int arith) | Role-quotient $\overline{B}$ on $\{V,F,S,T\}$ with VOID identity, non-associative witness, 4 branching pairs | READY for rigor pass |
| J37 | Discrete Dirac inside Cl(0,10), chirality + σ_outer + atomic refinement | 2/2 PASS at machine precision | Cl(0,10) gamma matrices + 16+16 chirality, $P_{56}$ = $\sigma_{\mathrm{outer}}$, BHML 100% in 54, su(4) ⊕ u(1) PS | READY for rigor pass |

**No central theorems modified.** All edits confined to README known-issues sections plus the J36 broken Gen14 verify-path fix. The three papers form a complete Tier-2 cohort ready for Brayden's referee-rigor pass. No substantive math issues flagged.

The J37 Cl(0,10) structure constants check out cleanly against standard Clifford-algebra conventions (algebra dim 1024, Dirac spinor 32 = 16+16, $\omega^2 = -I$ for $n = 10$, $\mathrm{Out}(\mathfrak{so}(10)) \cong \mathbb{Z}_2$, 54 = 1 ⊕ 9 ⊕ 44 under SO(9), unique-15-dim-simple-compact = $\mathfrak{so}(6) \cong \mathfrak{su}(4)$). The Tier-2 designation (rather than Tier 1) is correctly placed because of the load-bearing structural-iso vs phenomenological-identity hypothesis, not because of any math error.
