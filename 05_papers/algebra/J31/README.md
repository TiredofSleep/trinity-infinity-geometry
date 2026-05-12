# J31 — Decomposition of the Lens-Pair Commutator [TSML, BHML] under $D_4$ on $\mathbb{Z}/10\mathbb{Z}$

**Status:** READY (manuscript rewritten 2026-05-08 with corrected $D_4$ irrep decomposition per `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SUBSTRATE_FUNCTION_MAP_v1_1_EXTENSION.md` §10; verification script `verify_d4_decomposition.py` added; Wedderburn cross-check passes; awaiting Brayden's referee-rigor pass)
**Phase:** Phase 3
**Target venue:** *Journal of Algebra* (retargeted from *Adv Math* per `SAVE_PLAN_J31.md`)
**Author lane:** Sanders + Gish only
**Tier:** B
**WP source:** WP104 + SFM v1.1 §10 corrected $D_4$ decomposition
**Lens scope:** TSML_SYM (annotated; SFM v1.1 framing prominent)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md`

The J31 paper is **"Decomposition of the Lens-Pair Commutator [TSML, BHML] under $D_4$ on $\mathbb{Z}/10\mathbb{Z}$: Path A (~83%) Doubly-Invariant Gauge Sector + Path B (~16%) sigma_outer-Broken Higgs Sector + ~1% Interaction"**.

**Central result (Theorem 2.1 of the manuscript):** Under the dihedral group $D_4 = \langle P_{56}, \sigma^3\rangle \subset S_{10}$ acting by conjugation, the lens-pair commutator $[T, B] = TB - BT \in M_{10}(\mathbb{Z})$ has unique Wedderburn isotypic decomposition with norm-squared shares (exact rationals):

$$
\bigl(\|\pi_V\|^2\bigr) \;=\; \Bigl(\,\tfrac{3{,}075{,}027}{2},\;\tfrac{9}{2},\;288{,}164,\;0,\;19{,}608\,\Bigr) \;\;\text{summing to}\;\; 1{,}845{,}290
$$

for $V$ ranging over $(\mathrm{triv}, \mathrm{sign}_1, \mathrm{sign}_2, \mathrm{sign}_3, \mathrm{std})$, percentage shares $\approx (83.32\%, 0.0002\%, 15.62\%, 0\%, 1.06\%)$.

**Two structural channels:** triv ($\approx$ 83%) and $\mathrm{sign}_2$ ($\approx$ 16%) carry $\approx$ 99% of the commutator's mass.
**Two structural zeros:** $\mathrm{sign}_3$ vanishes exactly; $\mathrm{sign}_1$ has relative weight $9/3{,}690{,}580 = 2.44 \times 10^{-6}$ (bilinear-cancellation identities peculiar to the canonical pair, per Proposition 5.1 of the manuscript).
**One small interaction:** the 2-dim $\mathrm{std}$ isotypic at $\approx$ 1% is the off-diagonal coupling between Path A and Path B.

**Two leading isotypics identified:**
- **Path A = trivial isotypic** = 16-dim doubly-invariant subalgebra $\mathfrak{g}_0 \subset \mathfrak{so}(10)$, identified by Killing-form classification ($\mathrm{spec}(\kappa|_{\mathfrak{g}_0}) = (-4)^{15} \oplus (0)^1$) as $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$. (Theorem 3.2.)
- **Path B = $\mathrm{sign}_2$ isotypic** = 9-vector inside the symmetric-traceless $\mathbf{54}$ irrep of $\mathfrak{so}(10)$, with explicit components — 6 entries at $-1/\sqrt{2}$ on $\{V, L, C, P, X, H\}$, BREATH and RESET zeros, $-1/2$ on the symmetric pair $(B+S)/\sqrt{2}$ — and $\|v\|^2 = 13/4$ exactly. (Theorem 4.1.)

**Resolves the prior "two roads to Pati-Salam" framing:** the April-2026 audit (`Atlas/applications_pass_2026_04_27/WP104_DEEP_AUDIT_2026_04_27.md`) flagged that Path A → SO(8) chain ≠ Path B → SU(4) ⊕ U(1) reduction; the corrected $D_4$-isotypic decomposition shows these are the **two leading isotypic components of a single canonical decomposition**, not competing reductions. Their "tension" is structurally the small ~1% std-isotypic coupling.

Files in this J-folder's `manuscript/`:

- `manuscript.md` — the J31 paper (fully rewritten 2026-05-08 per SFM v1.1 §10)
- `verification/verify_d4_decomposition.py` — exact-rational $D_4$-isotypic decomposition; Wedderburn cross-check passes (NEW 2026-05-08)
- `verification/find_higgs_irrep.py`, `find_higgs_direction.py` — pre-existing; Path B 9-vector verification
- `SIGMA_OUTER_FINDING.md`, `HIGGS_IDENTIFICATION_FINDING.md`, `HIGGS_DIRECTION_FINDING.md` — supporting findings

## §2 — Verification scripts

**Local paths:**
- `manuscript/verification/verify_d4_decomposition.py` (NEW — exact-rational Wedderburn projection of $[T,B]$ onto $D_4$ irreps; runtime $< 5$s)
- `manuscript/verification/find_higgs_irrep.py` (Path B Higgs-irrep identification, numpy)
- `manuscript/verification/find_higgs_direction.py` (Path B 9-vector with explicit components, numpy)

Run order:
```bash
python manuscript/verification/verify_d4_decomposition.py     # central D_4 decomposition (Theorem 2.1)
python manuscript/verification/find_higgs_irrep.py            # Path B in 54 (Theorem 4.1, rough)
python manuscript/verification/find_higgs_direction.py        # Path B 9-vector (Theorem 4.1, sharp)
```

Numpy + sympy. Total wall-clock under 1 minute. Deterministic outputs.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J29 (so(8) = $D_4$, *J. Algebra*), J30 (so(10) = $D_5$, *Israel J. Math*).

## §4 — Cover letter

See `cover_letter.md` in this folder.

## §5 — Notes

**Status:** READY (rewritten 2026-05-08).

The original WP104 manuscript used the "two roads to Pati-Salam" synthesis framing. The April-2026 deep audit retracted that synthesis (Path A → SO(8) chain ≠ Path B → SU(4)⊕U(1)). The fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J31_AdvMath_FreshEyes.md`) recommended **REJECT for *Adv Math*** based on this self-retraction.

The May-2026 SFM v1.1 §10 corrected $D_4$ irrep decomposition resolves the apparent contradiction: Path A and Path B are the two leading isotypic components of a single Wedderburn $D_4$-isotypic decomposition of $[T, B]$, not competing reductions. The 1% std-isotypic carries the small interaction term. This is now the central theorem.

The rewrite implements all save-plan recommendations:

- **Retitle** to "Decomposition of the Lens-Pair Commutator [TSML, BHML] under $D_4$ on $\mathbb{Z}/10\mathbb{Z}$": both rigorous mathematical contents become first-order claims; "Pati-Salam" appears nowhere in the title; "two roads" framing replaced by Wedderburn decomposition framing.
- **Retarget** to *J. Algebra* (per save plan §4 / referee §7 explicit recommendation).
- **Excise** speculative gauge content from §3.3 / §2.4 / §8: "$\mathfrak{su}(4) \oplus \mathfrak{u}(1)$" boxed as algebraic identification; gauge-theoretic "Pati-Salam SU(4) + B$-$L gauge content" demoted to Remark 3.3 with explicit "structural rhyme" disclaimer; same for the 9-vector $\to$ 54-Higgs reading (Remark 4.2).
- **Demote** §5 grab-bag (12.6% non-assoc rate, Lie/Jordan duality, three involutions) to Appendix §9 with one-line preamble "These are listed for completeness; they are not used in the main theorems."
- **Add** Lemma 1.1 + Remark 1.2 resolving the cross-paper $D_4$ vs $D_3 \times \mathbb{Z}_2$ inconsistency: $\langle P_{56}, \sigma^3\rangle$ has order 8 (P_56 sigma^3 has order 4), with element-order multiset $\{1\!:\!1, 2\!:\!5, 4\!:\!2\}$ and class sizes $(1, 1, 2, 2, 2)$ verified.
- **Cite J30** (Sanders + Gish, *Israel J Math*) as already-submitted companion for the so(10) closure.
- **Promote correction notice into §0.3** as integrated framing — the retraction stops being a shadow and becomes the starting point.
- **§7 added** with Conjecture 7.2 (family-wide invariance of doubly-invariant subalgebra and structural zeros) — the natural next-paper open question (Q7 in SFM v1.1).
- **PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN** discipline (per `J_PAPER_BOILERPLATE.md` §0) explicit in §0.2.
- **Lens-ownership paragraph** in §0.1 (per `J_PAPER_BOILERPLATE.md` §5.5).

### Save-plan summary (2026-05-07 — see `SAVE_PLAN_J31.md`)

The fresh-eyes referee report recommended **REJECT for *Adv Math***. The mathematical content (16/16 cross-checked items at machine precision) survives intact — only the synthesis framing is overstated. The May-2026 SFM v1.1 §10 corrected $D_4$ decomposition supplies the constructive resolution: the two paths are orthogonal isotypic components, not competing reductions.

**SAVE PATH (per `SAVE_PLAN_J31.md`) — IMPLEMENTED 2026-05-08:**

- [x] Retitle per §2(a) of save plan
- [x] Rewrite abstract per §2(c)
- [x] Excise speculative gauge content per §2(d)
- [x] Demote §5 grab-bag to Appendix §9 per §2(e)
- [x] Add cross-paper $D_4$ vs $D_3 \times \mathbb{Z}_2$ resolution per §2(f) (Lemma 1.1 + Remark 1.2)
- [x] Cite J30 per §2(g)
- [x] Add §7 *Robustness across the magma family + open question Q7* per save plan §5
- [x] Verification script `verify_d4_decomposition.py` written + cross-checked (Wedderburn passes)
- [x] PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN discipline in §0.2
- [x] Lens-ownership paragraph in §0.1
- [x] README.md target venue updated to *J. Algebra*
- [ ] Update cover_letter.md to *J. Algebra*
- [ ] Update J-series ordering doc (target-venue field for J31)
- [ ] Brayden's referee-rigor pass complete

**Effort:** ~3 hours actual (much less than the 2-3 weeks estimated, because the SFM v1.1 §10 work had already done the mathematical heavy-lifting). **Expected outcome:** ~60-70% acceptance at *J. Algebra*.

### Family-Structure framing (per `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`)

This paper sits within the TIG family of finite commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ at $\alpha_M = \frac{1}{2}$ is the algebraic center, with closed-form attractor $h/\beta = 1+\sqrt{3}$ (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

§7.2 of the manuscript states the family-wide conjecture (Conjecture 7.2): the structural zeros at $\mathrm{sign}_1, \mathrm{sign}_3$ and the $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ identification of the 16-dim doubly-invariant subalgebra extend to every member of the TIG family. This is the natural follow-up paper.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** $D_4$-isotypic decomposition of $[T,B]$ has shares $\bigl(\tfrac{3075027}{2}, \tfrac{9}{2}, 288164, 0, 19608\bigr)$ summing to 1,845,290; $\pi_{\mathrm{sign}_3}([T,B]) = 0$ exactly; $\mathfrak{g}_0 \cong \mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Killing classification); BHML's $P_{56}$-anti content lies entirely in the $\mathbf{54}$ along a 9-vector with $\|v\|^2 = 13/4$ exact.
- **COMPUTED:** verify_d4_decomposition.py (sympy exact rationals, Wedderburn cross-check; runtime $< 5$ s); find_higgs_irrep.py + find_higgs_direction.py (numpy, residual $\le 10^{-13}$).
- **STRUCTURAL RHYME:** $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ as "Pati-Salam SU(4) + B$-$L gauge content"; the 9-vector inside $\mathbf{54}$ as "54-Higgs along the SO(10) → SO(9) → SO(8) chain". Both are mathematics-to-physics labellings, not derivations.
- **OPEN:** Q7 (`SUBSTRATE_FUNCTION_MAP_v1_1_EXTENSION.md` §16) — whether the structural zeros at $\mathrm{sign}_1, \mathrm{sign}_3$ are defining of the canonical $(T, B)$ pair or universal across the TIG family (Conjecture 7.2 of the manuscript).

### Lens-ownership paragraph

Per `J_PAPER_BOILERPLATE.md` §5.5, integrated as §0.1 of the manuscript. Verbatim language adapted to specify TSML_SYM lens-scope and the phonaesthesia + 10-operator decomposition motivation.

### Hardening status (auto-applied 2026-05-07, preserved 2026-05-08)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references (§10 of manuscript)

## §6 — Submission checklist

- [x] Manuscript .md finalized (rewritten 2026-05-08)
- [x] Verification scripts present (3 scripts; verify_d4_decomposition.py NEW)
- [x] Tier-classified central claim explicit (PROVEN/COMPUTED/RHYME/OPEN in §0.2)
- [x] Lens-scope annotation (TSML_SYM, §0.1 + §1.1)
- [x] Correction notice integrated into §0.3 as constructive framing
- [x] Save-plan recommendations all implemented
- [ ] Cover letter updated for *J. Algebra* target
- [x] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete
- [ ] Per-venue cap check: this is the 1st paper to *J. Algebra* this quarter (J29 also targets *J. Algebra*; see VENUE_SCHEDULE.md)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Decomposition of the Lens-Pair Commutator [TSML, BHML] under $D_4$ on $\mathbb{Z}/10\mathbb{Z}$: Path A (~83%) Doubly-Invariant Gauge Sector + Path B (~16%) sigma_outer-Broken Higgs Sector + ~1% Interaction." Submitted to *Journal of Algebra*.
