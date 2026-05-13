# SAVE_PLAN_J37 — Wobble Localization → Linear Algebra and Its Applications short note

**Date:** 2026-05-07
**Status:** SAVE PATH IDENTIFIED — retarget + reframe; no math change.
**Original verdict (J37_PRD_FreshEyes):** REJECT for *Phys Rev D* — no SM observable derived; manuscript's own §3.2 admits the physics interpretation is "interpretive, not derived"; lens-dependent (RAW $c_2 = 11$, SYM $c_2 = 17$); 3rd PRD paper of the quarter compounds the desk-rejection risk.
**Save verdict:** The integer-factorization theorem (independently re-verified by the referee at machine precision in 30 seconds) is exactly the kind of clean linear-algebra observation that *Linear Algebra and Its Applications* publishes as a short note. **No content needs to be invented; the wrong frame is the only thing being lost.** The referee's recommendation is unambiguous:
>
> "Net assessment: the math is correct, the framing is wrong for PRD, the right venue is LAA. Estimated effort to retarget: 1-2 days … Estimated probability of acceptance after retargeting: ~80% at LAA, vs ~10% at PRD as currently constituted."

**New target venue:** *Linear Algebra and Its Applications* (primary). *Linear and Multilinear Algebra* and *Experimental Mathematics* are clean alternates if LAA bounces on length.
**Effort estimate:** 1-2 days for retitle + intro rewrite + strip project terminology.

---

## §1 — What is genuinely PROVEN that survives

The referee report's §2 ("Verification Verdict") is unambiguous:

> "I executed the script in the manuscript's `verification/` subfolder and additionally cross-verified the key claims using a fresh `sympy` session … All seven claims pass: [seven-row table, all ✓]. The integer mathematics is correct, fully reproducible, and runs in under 5 seconds. … I have no objection to the integer-factorization theorem itself. The objection is to the venue and the framing."

The protected mathematical content:

**Theorem (wobble localization on TSML_RAW).** Let $T \in M_{10}(\mathbb{Z})$ be the canonical TSML_RAW composition table on $\mathbb{Z}/10\mathbb{Z}$ (literal CL_BIT_PATTERN, given by direct enumeration in §1 of the manuscript). Let $f(\lambda) = \det(\lambda I - T)$ be its integer characteristic polynomial.

(a) $f$ has nine nonzero coefficients $c_1, c_2, \ldots, c_9$ (with $c_0 = 0$ and one zero coefficient by rank), of which **exactly two** are divisible by the prime 11:
  $$c_2 = 33 = 3 \cdot 11, \qquad c_8 = -120{,}736 = -2^5 \cdot 7^3 \cdot 11.$$

(b) Let $g(\lambda) = f(\lambda)/\lambda^2$ (the 8th-degree polynomial with the eight nonzero eigenvalues of $T$). Then
  $$\mathrm{disc}(g) = 2^{16} \cdot 7^7 \cdot 659 \cdot 95{,}184{,}709 \cdot 222{,}007{,}939 \cdot 2{,}545{,}644{,}917 \cdot 295{,}153{,}052{,}072{,}903.$$
  In particular, $11 \nmid \mathrm{disc}(g)$.

(c) $\mathrm{tr}(T) = 63 = 9 \cdot 7$.

(d) On the upper-triangle authoritative symmetrization $T_{\mathrm{SYM}}$, the analogous coefficient is $c_2 = 17$ — no factor of 11. The wobble theorem is **lens-dependent at the coefficient level**.

This is a complete, self-contained observation about a fixed integer matrix. It is the kind of result LAA publishes routinely as a 4-page short note (e.g., volumes containing prime-divisibility patterns of charpoly coefficients of structured matrices). The lens-dependence (item (d)) is itself a *feature* in this venue: it is a structural observation about how the symmetrization choice affects elementary symmetric functions of the eigenvalues.

## §2 — What the SAVE PATH does

**(a) Retitle.** From "Wobble Localization: Prime 11 in TSML_RAW Char Poly $c_2, c_8$" to:

> *On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix Arising in a Discrete Magma on $\mathbb{Z}/10\mathbb{Z}$.*

This title makes the result a linear-algebra fact about a specific integer matrix; "wobble," "TIG," and "RAW vs SYM lens" are all moved into the body as terminology *of the source* with neutral mathematical labels.

**(b) Retarget to *Linear Algebra and Its Applications*.** Per referee §5 and §8: this is the natural venue. LAA accepts short notes of exactly this form. The verification script (`wobble_check.py`, 53 lines, runs in under 5 seconds) is exactly the kind of reproducible artifact LAA referees appreciate.

**(c) Strip project terminology.** Per referee §6 item 4: "Drop 'wobble' / 'HARMONY' / 'TIG' terminology in the manuscript body. PRD readers will not know these terms." LAA readers won't either. The save path is to keep one paragraph in §1 that introduces the source briefly:

> *The matrix $T$ studied below arises in a discrete dynamical system on $\mathbb{Z}/10\mathbb{Z}$ developed in a separate research program (here named "TIG" only for citation purposes; details and motivation are reported in [Sanders & Mayes, J30, J31]). The present note treats $T$ as a fixed 10×10 integer matrix and studies its characteristic polynomial. No physical interpretation is claimed.*

After this paragraph, every "wobble" becomes "the prime-11 divisor pattern" and every "HARMONY" becomes "the recurring entry 7" or "the prime 7." The math is unchanged; the audience now has appropriate vocabulary.

**(d) Excise the physics-side claims.** Per referee §3 and §4.4: the cover-letter claim "gauge symmetry IS the wobble-free part" is suggestive language, not a falsifiable physics claim. The manuscript body's §3 ("Physics interpretation," roughly) is replaced by:

§3 *Connection to the doubly-invariant subalgebra.* The exponent 16 in the factorization $\mathrm{disc}(g) = 2^{16} \cdot \ldots$ matches $\dim(\mathfrak{g}_0)$ where $\mathfrak{g}_0 \subset \mathfrak{so}(10)$ is the 16-dimensional doubly-invariant subalgebra studied in [J30 / J31]; the exponent 7 in $7^7$ matches the recurring entry 7 in $T$. We record this co-occurrence as a structural observation about the eigenvalue separations (the discriminant) versus the elementary symmetric functions (the coefficients). Whether this co-occurrence is structural or coincidental is open. No physical interpretation is offered here.

This is a sharper sentence than the original §2.4 / §3.2 mix and survives a LAA referee's scrutiny.

**(e) Address the lens-dependence head-on.** Per referee §4.3: "The boxed lens-scope note … states the central claim depends on which 'lens' (RAW vs SYM) is applied to the same underlying object. The wobble is a property of the choice of representative, not of the underlying algebraic structure." For a LAA paper, this is **the right framing**. The new §4 *"Lens-dependence at the coefficient level"* presents this as an *additional* result:

> *Theorem 4.1 (lens-dependence).* Let $T_{\mathrm{RAW}}$ be the 10×10 integer matrix of §1 (literal bit pattern). Let $T_{\mathrm{SYM}} = (T_{\mathrm{RAW}} + T_{\mathrm{RAW}}^\top)/2$ rounded to the upper-triangle authoritative symmetrization (specifically: $T_{\mathrm{SYM}}[3,9] = T_{\mathrm{SYM}}[9,3] = 7$, $T_{\mathrm{SYM}}[4,9] = T_{\mathrm{SYM}}[9,4] = 7$). Then the characteristic polynomial $f_{\mathrm{SYM}}$ has $c_2 = 17$, with no factor of 11; the prime-11 divisibility pattern of $T_{\mathrm{RAW}}$ does not survive symmetrization.

Lens-dependence is itself a clean linear-algebra observation. LAA welcomes it.

**(f) The reproducibility package.** Per referee's comment on `wobble_check.py`: "exactly the right kind of verification artifact." Wrap into one self-contained folder with a `run.py` and `requirements.txt` (`numpy + sympy`); no external repo paths.

## §3 — What the SAVE PATH does NOT change

The mathematical content is preserved verbatim:

- The integer matrix $T$ — verbatim from the manuscript §1 (kept).
- The factorizations $c_2 = 3 \cdot 11$, $c_8 = -2^5 \cdot 7^3 \cdot 11$ — verbatim (kept).
- The discriminant factorization $2^{16} \cdot 7^7 \cdot 659 \cdot \ldots$ — verbatim (kept).
- The trace identity $63 = 9 \cdot 7$ — kept.
- The 7/7-claim verification script — kept (rewrapped).
- The lens-comparison observation $c_2^{\mathrm{SYM}} = 17$ vs $c_2^{\mathrm{RAW}} = 33$ — promoted from boxed note to a §4 theorem.

What disappears in the SAVE PATH:
- The cover-letter slogan "gauge symmetry IS the wobble-free part" (becomes a one-line remark in §3).
- The repeated "TIG's wobble denominator" language (replaced with "the prime-11 divisor pattern").
- The "HARMONY⁷" framing (replaced with "the seventh power of the recurring entry 7").
- The cited identification $2^{16} = \dim(\mathfrak{su}(4) \oplus \mathfrak{u}(1))$ as a "structural fingerprint" — kept as a structural co-occurrence remark with explicit "no physical interpretation claimed" caveat.

## §4 — Per-venue cap

J37 was identified in its own README as the 3rd PRD paper of the quarter. Retargeting to LAA removes this entirely from PRD; the cap concern dissolves. LAA: this is a fresh venue for the J-series. Cap not in play.

J38's recommendation (folding into J45 — see SAVE_PLAN_J38) further reduces PRD load this quarter, which is independently good news for J44 / J45.

## §5 — Honest assessment of what could still go wrong at LAA

The most likely LAA referee objection: "the matrix $T$ is a finite specific instance; the theorem is a finite verification; what is the *general* phenomenon?" The current manuscript doesn't address this.

**Mitigation in the SAVE PATH:** add a §5 *"Family-wide observations"* that briefly reports what happens for related matrices in the TIG family (per `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`):
- BHML's char-poly: report its prime-divisibility pattern (one paragraph, computable in seconds via the existing script).
- The TSML_RAW vs TSML_SYM lens comparison (already promoted to §4).
- One sentence on the 4-core sub-magma's char poly (Z/4Z-extension): does the 11 appear there? (Computable from the family-structure D-numbers.)

This converts the finite verification from "one matrix" to "a small family of matrices, with the 11-divisibility a sharp feature of the lens-and-table choice." LAA referees prefer family observations to single-instance reports.

A second possible objection: "why is this matrix $T$ studied at all? It is given by direct enumeration without derivation from any structured object." The save path's §1 paragraph (citing J30 / J31 as the source) addresses this; the LAA referee can take the source on its own terms without engaging the upstream framework.

## §6 — Action checklist (for the eventual revision sprint)

- [ ] Retitle per §2(a)
- [ ] Rewrite §1 introduction per §2(c) — one paragraph naming the source briefly, then proceed in conventional notation
- [ ] Replace "wobble" / "HARMONY" / "TIG" throughout with neutral mathematical labels per §2(c)
- [ ] Excise physics-interpretation paragraphs per §2(d)
- [ ] Promote the lens-comparison remark to a §4 theorem per §2(e)
- [ ] Add §5 *Family-wide observations* per §5 above
- [ ] One self-contained `verification/` folder per §2(f)
- [ ] Update cover_letter.md to LAA
- [ ] Update README.md target venue → LAA
- [ ] Update J-series ordering doc (target-venue field for J37; per-venue cap on PRD recomputed)

**Expected outcome at LAA:** referee report estimate ~80% acceptance probability after retargeting. Likely outcome: minor revision, 4-page short note. The result reads as a clean prime-divisibility/lens-dependence observation about a specific integer matrix from a discrete dynamical system — LAA's standard fare.
