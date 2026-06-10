# Tier-1 Promotability Audit — J23, J24, J25, J26, J27, J28, J29

**Audit date:** 2026-05-28
**Auditor role:** Independent portfolio-quality auditor (fresh-eyes pass; ship-readiness gate, not full per-line referee)
**Trigger:** Seven papers were promoted Tier 2 → Tier 1 on 2026-05-27 alongside the J01–J52 renumbering (commit `0d6d0f1`). The Tier 1 spine is intended to be ship-ready. Each promotion is aspirational and needs a sanity check.
**Method:** Read each manuscript, README, and supporting script; cross-checked the seven papers against each other for redundancy; checked the specific concerns flagged in the audit brief (J24-vs-J25 coordinate translation, J26 QM-application substance, J28 characterization-vs-example, J29 pedagogical-vs-research, J27 "Crossing Lemma" naming, J23 null-model robustness).
**Headline:** The seven promotions break down as **3 KEEP** (J24, J26, J27), **3 DEMOTE** (J23, J28, J29), and **1 MERGE** (J25 into J24). The Tier-1 spine should shrink by 4 slots after this audit.

---

## J23 — Mathieu M_{22} Substrate-Prime: Order-Factorization Coincidences

**Manuscript status:** Written (623 lines, amsart, complete).
**Promotion verdict:** **DEMOTE-to-Tier-2** (or accept as a *Math. Magazine* / *Math. Intelligencer*-class note, which is not Tier-1 research-spine material).
**Justification:** The paper proves one theorem — a binomial p-value of $1.19 \times 10^{-6}$ that 10 of M_{22}'s 12 irrep dimensions lie in the substrate-prime band $\mathcal{B} = \{m : \text{primes}(m) \subseteq \{2,3,5,7,11\}, \nu_2(m) \le 1\}$. The theorem is correctly proved, computationally verified (`m22_decomposition.py`, < 1 s), and the paper is exceptionally well-disciplined about what it does *not* claim. But it remains a single-observation paper whose substrate-prime distinction was partly reverse-engineered from $|M_{22}| = 2^7 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11$, with the prime-11 case explicitly acknowledged as "weakest of the five." It is not Tier-1 algebra-research material; it is a competent *Monthly*-style elegant-coincidence note.

### Manuscript-level issues
1. **Null-model robustness.** The brief specifically flags this. The paper acknowledges (§7 Q6) that conditioning on $\sum d_i^2 = 443\,520$ would give a different p-value, but does not compute it. The current uniform-on-$[1,385]$ null is the *most generous possible* null. Conditioning on the sum-of-squares constraint, or on $385$-divisors only, or on having exactly 12 irreducibles, will all weaken the p-value substantially. Without computing at least one alternative, the result is fragile to a single referee remark.
2. **Reverse-engineered prime-11 case.** §3 honestly admits "the case for $11$'s substrate-distinguishedness is weakest of the five." Prime 11 enters only as the denominator of the canonical-form wobble $W \cdot 11/11 = 33/550$. This is genuinely strained and a careful referee will flag it.
3. **Substrate dependence.** The paper rests on a substrate $(\mathbb{Z}/10\mathbb{Z}, \sigma, W)$ defined in J15. If J15 is not in print, J23 is uncitable.
4. **J06 supersession.** The README header notes that J06 already extends this work to all 24 Niemeier lattices and 26 sporadics. If J06 is in the spine, J23 is partly absorbed.

### Venue recommendation
*Mathematical Intelligencer* "Mathematical Gems" or *AMM Notes*. Tier-2 with an honest "*Monthly*-style elegant-observation note" designation, not Tier-1 research.

---

## J24 — The Discrete Fejér Quotient on Squarefree Moduli

**Manuscript status:** Written (879 lines, amsart, complete with 7 theorems + 4 corollaries + verification table).
**Promotion verdict:** **KEEP-Tier-1.**
**Justification:** This is the strongest of the seven and the only one that is genuinely Tier-1 spine material. Two scripts (`verify_J03.py` + `proof_first_g_event.py`) report 10/10 PASS, max deviation $4.44 \times 10^{-16}$ for the closed form, 22,367 (b,k) pairs zero counterexamples for First-G, 900/900 obstruction-zero cell matches, corridor-average deviation $4.8 \times 10^{-5}$ at $f = 1000$. The substantive contributions (spectral-product $f_b(k) = \prod_j R(k, p_j)$ as continuous-in-k indicator for $\gcd(k, b) > 1$; squarefree layered $2^j - 1$ count; closed-form $\mathrm{Si}(2\pi)/\pi$ corridor average) are honestly elementary but real, and the paper is honestly self-positioned (§1 explicitly calls Theorem 3.1 closed-form "classical Fejér material, included to make the paper self-contained").

### Manuscript-level issues
1. The Theorem 6.1 (squarefree layered $2^j - 1$ count) proof uses the Boolean lattice argument well. The non-squarefree extension (Remark 6.2) is honest about acquiring multiplicities.
2. The Si$(2\pi)/\pi$ derivation via integration by parts (Theorem 7.2 proof) is clean.
3. Honest accounting in §1: "classical Fejér material" for closed form, "one-line gcd argument" for First-G, with the genuine contributions clearly labeled.

### Venue recommendation
*Integers — Electronic Journal of Combinatorial Number Theory*. Correct fit. Backup: *Acta Arithmetica* or *Math. Magazine* (note-length). Ship after Brayden's rigor pass + Integers style-file conversion.

---

## J25 — First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Bases

**Manuscript status:** Written (866 lines, amsart, complete).
**Promotion verdict:** **MERGE-into-J24** (as an appendix or §5; retire J25 as a standalone Tier-1 paper).
**Justification:** The brief's specific concern is correct. J25 acknowledges this directly: §1.4 ("Honest accounting of novelty") states "The closed form is standard. The synchronization is a coordinate translation of the elementary fact '$p_1$ is the smallest positive multiple of $p_1$.' The $\omega$-blindness corollary is a one-line consequence of the closed form. The continuum identity is the standard discrete-to-continuum limit." Theorem 3.2/Remark 3.2 explicitly calls the synchronization "a tautology, recorded for clarity." Every theorem in J25 appears in J24:
- Lemma 3.1 (J25) = Theorem 3.1 (J24): closed form, identical statement, identical proof.
- Theorem 4.1 (J25) = Theorem 4.1 + Theorem 5.1 (J24): First-G localization + sync, identical.
- Corollary 4.2 (J25, $\omega$-blindness) is one-line consequence of J24's Theorem 3.1 (the closed form is a function of $k, f$ only).
- Theorem 5.1 (J25, continuum) = Theorem 7.1 (J24): identical.

The genuinely J25-specific content is (a) the 712-check verification harness packaging, (b) the Montgomery rectangular-window remark in §6, and (c) the $\omega$-blindness phrasing as a *corollary about ring-structure detection*. Items (a) and (b) belong as a J24 appendix; item (c) is one paragraph.

### Manuscript-level issues
1. **Self-admitted overlap with J24.** The honest-accounting subsection in §1.4 reads as a referee response, not as an introduction. A referee will read this and ask "why is this a separate paper?"
2. **712 vs 36,662 reconciliation.** Already addressed in §1.5, but its presence is a sign the paper has been bandaged rather than restructured.
3. **Montgomery remark (§6) is a coincidence-of-basis-functions observation** correctly disclaimed by the paper itself ("a coincidence of the rectangular-window basis function, not a mechanism").

### Venue recommendation
*None as a standalone paper.* Fold the verification harness + Montgomery remark + $\omega$-blindness corollary into J24 as a 2–3 page appendix. Retire J25 as a Tier-1 ship.

---

## J26 — A Discrete sinc² Identity in Finite-Dimensional Quantum Mechanics

**Manuscript status:** Written (496 lines, amsart, complete).
**Promotion verdict:** **KEEP-Tier-1** (conditional on hardening the QM framing).
**Justification:** The brief specifically asks whether the QM framing is concrete enough to justify the venue claim. The current §2 (QM Hilbert-space setup) + Proposition 4.1 (squared overlap with normalized window) + §4.1 "Note on interpretation" (disambiguating fidelity vs position marginal) are real QM content; the Schwinger-1960/Wootters-1987/Vourdas-2017 finite-QM lineage is cited correctly. Proposition 4.1 gives the explicit fidelity $|\langle \hat p | w_k \rangle|^2 = (k/N) R(k, f)$, which is a substantive identity. The closed-form $\sin^2(1/10) = 25(\sqrt{5}-1)^2/(4\pi^2)$ (Ptolemy pentagon at $f = 10$) and the cyclic-group first-zero theorem for every $f \ge 2$ (Corollary 4.3, no primality needed) are clean QM-on-$\mathbb{Z}/N\mathbb{Z}$ statements. But §5 (First-G synchronization) is essentially a citation back to J24/J25 and could be compressed to one paragraph. The Schwinger/Wootters/Vourdas citations are not engaged in the body of the paper, only in the bibliography.

### Manuscript-level issues
1. **QM-application strengthening.** The brief asks whether a concrete QM application is present. Proposition 4.1 *is* a concrete kinematic identity. To be Tier-1 at LMP, this should become a worked example with a specific finite-QM Hamiltonian (e.g., the cyclic-shift Hamiltonian on $\mathbb{Z}/N\mathbb{Z}$ + a position-window projector); the squared-overlap interpretation provides the natural scattering observable.
2. **Engage the Schwinger/Wootters/Vourdas literature in the body.** Currently cited but not engaged. Either show where in Vourdas 2017 this overlap appears (and explain why the present statement is new), or drop the citations.
3. **Strip AI-attribution.** Acknowledgments still mention "Anthropic Claude sessions in 2026" — the J24/J25 hardening directive (Claude byline removed) was not applied here.
4. **Venue cap.** Per-venue cap reached at JMP (3rd paper). LMP correctly identified as preferred submission target.

### Venue recommendation
*Letters in Mathematical Physics* (preferred) or *J. Phys. A: Mathematical and Theoretical* (backup). After QM-hardening + AI-attribution scrub + §5 compression. Ship after rigor pass.

---

## J27 — Joint Injectivity of Additive-Quotient and Multiplicative-Orbit Partitions on Z/nZ

**Manuscript status:** Written (807 lines, amsart, complete; replaces earlier "Crossing Lemma" draft).
**Promotion verdict:** **KEEP-Tier-1.**
**Justification:** The brief asks whether this is "actually a lemma in the J21-style integer sense, or a more substantive theorem." It is substantive. The paper is a clean partition-lattice paper on $\mathbb{Z}/n\mathbb{Z}$ with four theorems (3.3 sufficient condition for $\{A_d, \pi_{DYN}(g)\}$ joint injectivity on units; 4.1 M+M classification on units via $\langle g \rangle \cap \langle h \rangle = \{1\}$; 5.1 SPEC+DYN biconditional via $-1 \notin \langle g \bmod p \rangle$; 6.1 prime-power kernel-of-reduction obstruction) plus two falsifying examples showing the natural prime-action conjecture fails in *both* directions. The "Crossing Lemma" framing has been deliberately retitled (per SAVE_PLAN_J06) to avoid the Ajtai-Chvátal-Newborn-Szemerédi 1982 graph-theoretic title collision; the informal "crossing" reading survives only as Remark 3.4.

### Manuscript-level issues
1. **Theorem 6.1 (prime-power obstruction) Case B proof has soft spots.** "The argument is delicate; the cleanest formulation uses the kernel-of-reduction structure..." (lines 567–600) followed by a 24-line generic-case argument that should be a clean 8-line reduction "Replace $g$ by $g^{\ord(g_0)}$; this is non-identity since $g_1 \ne 1$ generically, and lies in $1 + p\mathbb{Z}/p^r\mathbb{Z}$, so Case A applies." Currently a referee will mark this.
2. **Folklore check on Theorem 4.1 (M+M on units).** The proof is one paragraph; the result may be folklore in cyclic-group orbit theory. Spot-check Ore 1942, Stanley EC2, or recent partition-lattice surveys before claiming novelty.
3. **Bibliography prune.** 16 entries listed; Greaves 2001 *Sieves* is not cited in the body; Bhargava-Shankar-Tsimerman 2013 is referenced in SAVE_PLAN README but not in the rewritten manuscript.
4. **Verification.** `verify_joint_injectivity.py` exists in `manuscript/`, runs all four theorems plus the falsifying examples; reasonable coverage (squarefree $n \le 77$ with $\omega(n) \ge 2$ for the sufficient condition; M+M for 11 squarefree $n$; SPEC+DYN for 11 squarefree $n$ up to 77; prime-power for 8 prime-power $n$).

### Venue recommendation
*Algebra Universalis* (preferred); *Order* or *Comm. Math. Univ. Carolinae* as backups. JCT-A correctly retargeted away from. Ship after Theorem 6.1 Case B tightening + folklore check + bibliography prune (12–20 hours).

---

## J28 — A Small Commutative Non-Associative Magma on Z/10Z with Role-Deterministic Boundary Behavior

**Manuscript status:** Written (696 lines, amsart, post-Path-B rewrite).
**Promotion verdict:** **DEMOTE-to-Tier-2.**
**Justification:** The brief specifically asks whether the paper has a characterization theorem or just an example. **Just an example.** The role partition $\{V, F, S, T\}$ is labeled by fiat (the paper says so explicitly, twice — §3 and the Open Questions section). Every "theorem" is direct verification on an explicit small table:
- Theorem 3.1 ($V$ is identity): 4-cell inspection of a $4 \times 4$ table.
- Theorem 3.2 (commutativity, non-associativity of $M_R$): table inspection plus one explicit non-associative witness.
- Theorem 4.1 (role-deterministic boundary): enumeration over the $10 \times 10$ table restricted to each role-pair.
- Lemma 5.1 ($\tau(n) = 7 - n$): direct iteration on the diagonal of $\BH$.

The honest content: $M_R$ is one specific 4-element commutative non-associative magma, presented via the specific 10-zone operation $\BH$, with a specific 4-block partition labeled by fiat. There is no characterization ("$M_R$ is the unique 4-element magma satisfying X"); the role partition is not a congruence of $\BH$ (Theorem 4.1 explicitly shows this fails on $\{F, S\}^2$). The "role-deterministic boundary" is not a recognized algebraic class — it is a description of this one table's behavior. Section 5 ($\Psi$ row-asymmetry summing to $21 = T_6$) is decorative; the paper itself flags it as "structural rhyme, not a theorem" and acknowledges that the natural Fibonacci decomposition does *not* hold.

### Manuscript-level issues
1. **Characterization missing.** This is the central Tier-1 gap. For Tier-1 promotion, the role partition needs to be derived from a structural property (e.g., as a congruence of a derived structure, or as the unique 4-element magma satisfying explicit axioms), not labeled by fiat.
2. **"Role-deterministic boundary" predicate is not a recognized class.** It is defined for this specific $\BH$. To be Tier-1, define a general class of "role-deterministic-boundary algebras" with multiple examples, *or* drop the framing and present this as a single-example case study (and re-tier).
3. **Drápal-Wanless asymmetry.** The paper says it is "in the Drápal-Wanless neighborhood" but the two extrema (maximally non-associative vs near-associative-with-role-determinism) are not in dialogue. A referee for *Algebra Universalis* will ask: what is the analog of D-W's main theorem for this object?
4. **§5 ($\Psi$ / 21 / $T_6$) is honest but decorative.** Cut entirely, or move to an appendix. Adds 1.5 pages of numerical decoration to a 12-page paper.

### Venue recommendation
*Algebra Universalis* (short note) is fine for the current content. Re-tier as Tier 2 expository / short-note ship. Not Tier-1 spine without substantive characterization work.

---

## J29 — The Lo Shu D₄ Orbit Modulo 3: Four Distinct Magmas and a Cumulant Spectrum

**Manuscript status:** Written (371 lines, markdown, complete).
**Promotion verdict:** **DEMOTE-to-Tier-2** (this is an MAA *Mathematics Magazine* pedagogical note, not Tier-1 research).
**Justification:** The brief specifically asks whether this is Math-Magazine-level or genuine Tier-1. **Math-Magazine-level.** The paper itself targets *Mathematics Magazine* (MAA) as the primary venue, and is correctly written for an undergraduate audience (§6 "Pedagogical use" explicitly: "a 50-minute classroom session in an undergraduate abstract algebra course"). The Diagonal Lemma (no $3 \times 3$ commutative quasigroup has a repeated diagonal entry) is a real small-but-correct algebraic observation with an honest 8-line proof. The $V_4'$-coset invariance of $\kappa(M) = \mathrm{Tr}(M^2) - \mathrm{Tr}(M)^2$ is a clean 2-line generators-on-transpose-and-180°-rotation argument. These are real lemmas — but a real Tier-1 paper would synthesize them into a structural result about magic-square mod-$n$ reductions; this note instead enumerates them on Lo Shu and verifies them on Dürer. The "Why mod 3 is special" empirical sweep across moduli (§7.1) is honestly recorded as an empirical observation, not derived.

### Manuscript-level issues
1. **README marks "Tier: 2 (draft)" while it sits in the J01–J31 Tier-1 band.** The README itself, the venue choice (*Mathematics Magazine*), the §6 pedagogical-use framing, and the §2.1 enumeration-by-direct-computation all signal pedagogical, not research, content. The Tier-1 promotion was a mistake.
2. **6/6 vs 10/10 verification mismatch.** Manuscript §5 says "Overall: PASS (6/6)" but the actual `verify_J58.py` script (per README §5) prints "Overall: PASS (10/10)" — 6 theorems + V₄′ random-matrix invariance + Dürer + Diagonal Lemma exhaustive enumeration + Lo Shu diagonal corollary. The manuscript text is stale.
3. **Script naming drift (J58 vs J29).** `verify_J58.py` reflects pre-renumbering nomenclature. Rename to `verify_J29.py` or add an inline note.
4. **MSC codes.** 20D60 (combinatorial problems on finite groups) is a stretch; replace with 08A05 (general algebraic structures) or 05B30 (combinatorial designs).
5. **The §7 extension to Dürer 4×4** with $\kappa = \pm 128$ is honest and pedagogically valuable but is COMPUTED only (commutativity correlation verified case-by-case, not derived).

### Venue recommendation
*Mathematics Magazine* (MAA) — correctly targeted as primary venue. Tier-2 expository. Not Tier-1 research-spine material.

---

## Summary table

| J# | Verdict | Action |
|---|---|---|
| J23 | DEMOTE-to-Tier-2 | Re-target as *Math. Intelligencer*-class note; compute one alternative null model; resolve prime-11 reverse-engineering concern |
| J24 | KEEP-Tier-1 | Ship after Brayden's rigor pass + *Integers* style-file conversion (4–8 hours) |
| J25 | MERGE-into-J24 | Fold harness + Montgomery remark + $\omega$-blindness corollary as 2–3 page appendix to J24; retire standalone |
| J26 | KEEP-Tier-1 (conditional) | Strengthen QM application with a worked Hamiltonian example; engage Schwinger/Wootters/Vourdas citations in body; strip AI-attribution; compress §5 |
| J27 | KEEP-Tier-1 | Tighten Theorem 6.1 Case B proof; folklore check on Theorem 4.1; bibliography prune (12–20 hours) |
| J28 | DEMOTE-to-Tier-2 | Lacks characterization theorem; "role-deterministic boundary" is not a recognized class; keep as *Algebra Universalis* short note |
| J29 | DEMOTE-to-Tier-2 | Pedagogical *Math. Magazine* note correctly targeted; never should have been Tier-1; fix 6/6 vs 10/10 stale text |

## Net effect on Tier-1 spine

Of the seven promotions:
- **3 KEEP** (J24, J26, J27) — confirmed Tier-1 capable
- **3 DEMOTE** (J23, J28, J29) — should return to Tier 2
- **1 MERGE** (J25 into J24) — should not exist as standalone

The Tier-1 J01–J31 band would shrink by 4 slots after applying this audit. J24 is the only paper in the seven that is genuinely ship-ready Tier-1 material today; J26 and J27 are within a rigor pass.
