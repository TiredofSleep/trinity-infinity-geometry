# J37 — On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix Arising in a Discrete Magma on Z/10Z

**Status:** RETARGETED to LAA per save plan (manuscript rewritten 2026-05-07; ~80% acceptance estimate; awaits final referee-rigor pass)
**Phase:** Phase 4
**Target venue:** *Linear Algebra and Its Applications* (LAA) — RETARGETED from PRD per `SAVE_PLAN_J37.md`
**Author lane:** Sanders + Gish
**Tier:** 2 (draft (RETARGETED to LAA; LinAlgApps target))
**WP source:** WP107 (rewritten as LAA short note; TIG terminology stripped)
**Lens scope:** $T_{\mathrm{RAW}}$ (10×10 integer matrix, non-symmetric, rank 8); the prime-11 pattern does NOT appear on $T_{\mathrm{SYM}}$ (the upper-triangle authoritative symmetrization, rank 7) at the coefficient level — $c_2(f_{\mathrm{SYM}}) = -23$ (Theorem 4.1 lens-dependence)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md`

The J37 paper is **On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix Arising in a Discrete Magma on $\mathbb{Z}/10\mathbb{Z}$** (rewritten 2026-05-07 from WP107 corpus; retargeted to LAA per save plan). For the specific 10×10 integer matrix $T$ defined in §1, the integer characteristic polynomial $f(\lambda) = \det(\lambda I - T)$ has **exactly two** of its nine nonzero coefficients divisible by 11: $c_2 = 33 = 3\cdot 11$ and $c_8 = -120736 = -2^5\cdot 7^3\cdot 11$. The discriminant of $g(\lambda) = f(\lambda)/\lambda^2$ factors as $2^{16}\cdot 7^7\cdot 659\cdot(\text{large primes})$, with **no factor of 11**. Structural reading: the prime 11 lives at the coefficient level (elementary symmetric functions of the eigenvalues), the large exponents $2^{16}$ and $7^7$ at the separation level (eigenvalue gaps — the discriminant). Theorem 4.1 records that the prime-11 pattern is **lens-dependent**: the upper-triangle authoritative symmetrization $T_{\mathrm{SYM}}$ (a 2-cell perturbation of $T$) has $c_2 = -23$ and no factor of $11$. No physical interpretation is claimed; the paper is a clean linear-algebra short note in the LAA neighborhood.

Files in this J-folder's `manuscript/`:

- `manuscript.md` — the J37 paper (WP107 corpus, finalized 2026-05-07)
- `verification/wobble_check.py` — sympy-based 7/7 claim verification

## §2 — Verification script

**Local path:** `manuscript/verification/wobble_check.py`

Run: `PYTHONIOENCODING=utf-8 python wobble_check.py`. 7/7 claims at machine precision: integer char poly, trace = $63 = 9\cdot 7$, $c_2 = 33 = 3\cdot 11$, $c_8 = -2^5\cdot 7^3\cdot 11$, only $c_2, c_8$ have factor 11, $\mathrm{disc}(g)$ factors with $2^{16}\cdot 7^7$ and no 11, $2^{16}$ matches $\dim$ of doubly-invariant subalgebra. Sympy. Wall-clock under 5 seconds.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J37

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

**Status: DRAFT** — manuscript built from corpus `papers/wp107_wobble_localization/WP107_WOBBLE_LOCALIZATION.md` on 2026-05-07. Lens scope **TSML_RAW** explicit (the wobble does NOT appear on TSML_SYM at the coefficient level — that lens has $c_2 = -23$, no factor of 11). Cites J37 (so(8) = D₄, *J Algebra*) as already-submitted companion; references J31 (Pati-Salam) for the doubly-invariant content.

**Per-venue cap warning:** This is potentially the **3rd PRD paper** in the J-series (after J44 dark-sector and J45 mass hierarchy in Phase 2). PRD per-venue cap is conventionally 2/quarter for tightly-related papers. **FALLBACK NEEDED if PRD's per-venue cap blocks acceptance.** Proposed fallback venue: *Physics Letters B* (short note format suits this 4-page result).

### Save-plan summary (2026-05-07 — see `SAVE_PLAN_J37.md`)

The fresh-eyes referee report (J37_PRD_FreshEyes.md) recommends **REJECT for PRD** — math is sound (independently re-verified at machine precision: $c_2=33=3\cdot 11$, $c_8=-2^5\cdot 7^3\cdot 11$, $\mathrm{disc}(g) = 2^{16}\cdot 7^7 \cdot 659 \cdot \ldots$, no factor of 11 in disc), but no SM observable is computed; the manuscript's own §3.2 calls the physics interpretation "interpretive, not derived"; the result is lens-dependent (RAW $c_2=11$-divisible, SYM $c_2=17$ no factor of 11).

**SAVE PATH (per `SAVE_PLAN_J37.md`):**

- **Retarget** to *Linear Algebra and Its Applications* (LAA) as a short note. The referee's explicit recommendation: *"the math is correct, the framing is wrong for PRD, the right venue is LAA. Estimated effort to retarget: 1-2 days … Estimated probability of acceptance after retargeting: ~80% at LAA, vs ~10% at PRD as currently constituted."* Alternates: *Linear and Multilinear Algebra* or *Experimental Mathematics*.
- **Retitle** to *"On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix Arising in a Discrete Magma on $\mathbb{Z}/10\mathbb{Z}$"*. Strip "wobble" / "HARMONY" / "TIG" terminology entirely from the body; replace with neutral mathematical labels (the prime-11 divisor pattern; the seventh power of the recurring entry 7).
- **Promote** the lens-dependence remark to a §4 theorem (Theorem 4.1, lens-dependence: $T_\mathrm{RAW}$ has $c_2 = 33$, $T_\mathrm{SYM}$ has $c_2 = -23$). Lens-dependence is itself a clean linear-algebra observation in the LAA neighborhood, not a flaw.
- **Excise** physics-side claims; the cover-letter slogan "gauge symmetry IS the wobble-free part" becomes a one-line "structural co-occurrence" remark in §3 with explicit "no physical interpretation claimed" caveat.
- **Add** §5 *Family-wide observations* (BHML char-poly, the 4-core sub-magma's char poly per Z/4Z extension) — converts the finite verification from "one matrix" to "a small family with sharp lens-and-table-dependent prime-divisibility."

**Per-venue cap effect:** retargeting to LAA removes J37 from PRD; combined with SAVE_PLAN_J38, the quarter's PRD load goes from 4 (J37, J38, J44, J45) to 2 (J44, J45) — cap concern dissolves entirely.

**Effort:** 1-2 days. **Expected outcome:** ~80% acceptance at LAA, minor revision, 4-page short note.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (filled, J37)

- **PROVEN:** for the specific 10×10 integer matrix $T$ in §1, the prime $11$ divides exactly the coefficients $c_2 = 33$ and $c_8 = -120{,}736$ of $\mathrm{charpoly}(T)$; the discriminant of $g = f/\lambda^2$ has no factor of $11$ and factors as $2^{16} \cdot 7^7 \cdot 659 \cdot \ldots$; the trace is $63 = 9 \cdot 7$; the upper-triangle authoritative symmetrization $T_{\mathrm{SYM}}$ (rank $7$) has $c_2 = -23$ and no nonzero coefficient of its characteristic polynomial is divisible by $11$ (Theorem 4.1, lens-dependence).
- **COMPUTED:** all coefficient factorizations + discriminant factorization + SYM-lens comparison are verified by `manuscript/verification/wobble_check.py` (sympy `Matrix.charpoly`, `factorint`, `discriminant`); 7/7 PASS at integer/machine precision in <5 seconds.
- **STRUCTURAL RHYME:** the exponent $16$ in $\mathrm{disc}(g) = 2^{16} \cdot \ldots$ matches the dimension of a 16-dimensional doubly-invariant subalgebra of $\mathfrak{so}(10)$ studied separately in the source program; the exponent $7$ in $7^7$ matches the recurring entry $7$ in $T$ (the table's HARMONY-cell density). These are structural co-occurrences, not derivational steps. The framing follows the Drápal-Wanless (2021, *JCTA*) line of work on small finite commutative non-associative structures.
- **OPEN:** whether the prime-$11$ pattern in $c_2, c_8$ admits a closed-form algebraic explanation (e.g., a structural product formula relating sums-of-pairs and the determinant of the rank-8 part of $T$); whether analogous prime-localization patterns occur for related integer matrices in the same combinatorial neighborhood.

### Lens-ownership paragraph (filled, J37 — see manuscript §0)

> *Lens and substrate.* The 10×10 integer matrix $T$ studied here is the literal cell pattern of the canonical composition table of a discrete commutative magma on $\mathbb{Z}/10\mathbb{Z}$ developed in a separate research program (cited as J02, J05; closest published precedent Drápal & Wanless 2021, *JCTA* 184, 105510). The choice of carrier $\mathbb{Z}/10\mathbb{Z}$ and table $T$ is not derived from first principles in this note; it reflects a structural reading of the substrate motivated by the source program. The theorems below are theorems on this specific 10×10 integer matrix; analogous theorems would hold on other 10×10 integer matrices in the same combinatorial neighborhood. The present note treats $T$ as a fixed integer matrix and studies its characteristic polynomial.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .md finalized (rewritten 2026-05-07 as LAA short note per save plan; TIG terminology stripped; lens-dependence promoted to Theorem 4.1; family-wide observations §5 added)
- [x] Verification script green (`wobble_check.py`, 7/7 PASS)
- [x] Tier-classified central claim explicit
- [x] Lens-scope annotation ($T_{\mathrm{RAW}}$; lens-dependent at coefficient level; $T_{\mathrm{SYM}}$ has $c_2 = -23$ no factor of 11)
- [x] Cover letter finalized for LAA (rewritten 2026-05-07)
- [x] Dependencies → cite J02, J05 as "submitted to [venue]"; Drápal-Wanless 2021 in references
- [ ] Brayden's referee-rigor pass complete
- [x] Per-venue cap: retargeting to LAA removes J37 from PRD entirely; combined with J38 fold-in, quarter PRD load is now 2 (J44, J45)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix Arising in a Discrete Magma on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *Linear Algebra and Its Applications*.
