# J10 — $D_4$-Equivariant Orbits on the Non-Associative Locus of a Finite Commutative Magma on $\mathbb{Z}/10\mathbb{Z}$

**Status:** REWRITE 2026-05-12 — promotes the $D_4$-equivariant arity-3 orbit-structure finding (WP109 + WP112, machine-verified 2026-04-25 / 2026-04-26; corrected 2026-05-07 for the $D_4$ order-$8$ and the $(44,7,4,10,2)$ orbit distribution) to the central theorem. Standalone, self-contained `verify_J32_d4_orbits.py` added; all 6 claims PASS at machine precision in $<1$ s. 2026-05-28 polish: title and body language updated from decorative "operadic" framing to "$D_4$-equivariant arity-3" framing (the content is finite-group-action on a subset of a cube + bracketing-pair coherence, not operad theory in the May–Markl–Loday sense); Theorem B's strengthening to $\{a,b,c,L,R\}$-valued $\Phi$ has its proof expanded to a full intersection-empty argument.
**Phase:** Phase 3.
**Target venue:** *Communications in Algebra* (lead, per Wave 4 referee report 05). Fallback (in priority order): *Journal of Algebra*; *Algebraic Combinatorics*; *Algebras and Representation Theory*.
**Author lane:** Sanders + Gish only.
**Tier:** 2 (draft (REWRITE 2026-05-12; $D_4$-equivariant arity-3 obstruction))
**WP source:** WP109 ($D_4$ obstruction) + WP112 (P$_{56}$ canonical fuse).

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md`.

**Central theorem (Theorem A).** The diagonal action of $D_4=\langle P_{56},\sigma^3\rangle$ (order $8$) on the non-associative locus $\mathcal{N}\subset(\mathbb{Z}/10\mathbb{Z})^3$ of the canonical TSML_RAW table partitions $\mathcal{N}$ into exactly $\mathbf{67}$ restricted orbits, with size distribution $(44,7,4,10,2)$ at sizes $(1,2,3,4,8)$; size-weighted sum $44+14+12+40+16=126=|\mathcal{N}|$.

**Theorem B (obstruction).** Exactly $\mathbf{16}$ of the $67$ orbits fail bracketing-pair coherence. Hence no $\{a,b,c,L,R\}$-valued $D_4$-equivariant assignment $\Phi:\mathcal{N}\to\mathbb{Z}/10\mathbb{Z}$ exists.

**Theorem C ($\langle P_{56}\rangle$ sharpening).** Under $\langle P_{56}\rangle$ alone, $\mathcal{N}$ partitions into $\mathbf{98}$ orbits ($70$ singletons + $28$ doubletons), all coherent. The structural obstruction is therefore located precisely at the $\sigma^3$ generator.

**Theorem D (4-core arity-3 closure).** The $4$-core $\mathcal{C}=\{0,7,8,9\}$ is closed under both arity-$3$ bracketings $L,R$ on all $4^3=64$ triples of $\mathcal{C}^3$; $8$ of the $64$ are non-associative.

## §2 — Verification scripts

**Primary (standalone):** `manuscript/verification/verify_J32_d4_orbits.py` — pure standard-library Python; runtime $<1$ s; deterministic; CC-BY-4.0 license header. Covers all 6 load-bearing claims:

1. $|\mathcal{N}|=126$ (with optional cross-check against bundled `manuscript/nonassoc_triples.json`).
2. $|D_4|=|\langle P_{56},\sigma^3\rangle|=8$ with the correct order spectrum $\{1:1,\,2:5,\,4:2\}$.
3. $67$ restricted orbits with size distribution $(44,7,4,10,2)$, size-weighted sum $126$.
4. Exactly $16$ bracketing-pair incoherent orbits among the $67$.
5. $98$ $\langle P_{56}\rangle$-orbits ($70$ singletons + $28$ doubletons), all coherent.
6. $4$-core arity-$3$ closure: $64$ in-core / $0$ out-of-core / $8$ non-associative.

**Secondary (legacy, retained for the WP-source audit trail):**

- `manuscript/verification/d4_orbit_decomposition.py` — original $D_4$ orbit decomposition with bracketing-coherence test (WP109 reproduction).
- `manuscript/verification/p56_canonical_fuse.py` — original $\langle P_{56}\rangle$ orbit decomposition with the canonical Family-H fuse-table construction (WP112 reproduction).
- `manuscript/verification/rule_families.py` — 8-family rule survey (P$_{56}$ vs $\sigma^3$ equivariance breakdown).
- `manuscript/verification/fuse_table.py` — module-level TSML table, bracketing functions, $P_{56}$ / $\sigma^3$ permutation definitions.

Run all four legacy scripts plus the primary standalone for full reproduction of the WP109 + WP112 figures.

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J01** (Sanders + Gish 2026, *J. Algebra*) — binary joint-closure / closed-form attractor / Galois-$D_4$ centerpiece; cited in §1, §5, §6.
- **J12** (Sanders + Gish 2026, *Comm. Alg.*) — standalone Galois proof on the quartic; cited in §6.
- **J11** (Sanders + Gish 2026, *J. Algebra*) — Wedderburn $D_4$-isotypic decomposition of $[T,B]\in M_{10}(\mathbb{Z})$; cited in §6.
- **J45** (Sanders + Gish 2026, *Comm. Alg.*) — $\langle P_{56}\rangle$-equivariant arity-3 fuse-rule survey; cited in §1, §7.

## §4 — Cover letter

See `cover_letter.md` in this folder. Target *J. Algebra*; per-venue cap transparency explicit (this is the **4th** *J. Algebra* submission of the 2026 cycle, following J01, J11, and J12-into-*Comm.-Alg.*); fallback priority order documented (*Comm. Alg.* → *Algebraic Combinatorics* → *Algebras and Representation Theory*).

## §5 — Notes

- **Status (2026-05-12 rewrite + 2026-05-28 polish):** SUBMISSION-READY. Manuscript rewritten end-to-end as the $D_4$-equivariant arity-3 orbit-structure paper. Standalone verification script bundled (`verify_J32_d4_orbits.py`); all 6 PASS at machine precision in $<1$ s. The 2026-05-28 polish replaces decorative "operadic" framing with "$D_4$-equivariant arity-3" terminology per Wave 4 referee report 05.
- **Per-venue cap:** Now targeting *Comm. Alg.* (lead) per Wave 4 referee report — *J. Algebra* fallback is still available. Honest disclosure to editor.
- **Tier classification:** Tier-B forced by direct enumeration on $1000$ triples and the $8$ elements of $D_4$.
- **Lens scope:** TSML_RAW (the canonical asymmetric table); TSML_SYM has $128$ non-associative triples instead of $126$ and is not addressed here. The $4$-core arity-$3$ closure is lens-invariant.
- **Differentiation from companion papers:** J01 is binary joint closure + binary attractor + Galois bundle; J10 is arity-3 orbit decomposition (no overlap). J11 is matrix decomposition of $[T,B]$; J10 is set-partition combinatorics on $\mathcal{N}\subset(\mathbb{Z}/10\mathbb{Z})^3$ (no overlap). J12 is the standalone Galois proof; J10 is a finite-group-action result on a combinatorial subset (no overlap).
- **Math-fix lineage:** The corrected $D_4$ order ($8$, not $12$) and corrected orbit distribution $(44,7,4,10,2)$ replace the prior draft that had reported $(5,35,19,3)$ summing to $175$ — an error in the WP109 working draft that was traced to confusing the *full* orbit decomposition in $(\mathbb{Z}/10\mathbb{Z})^3$ with the *restricted* orbit decomposition on $\mathcal{N}$. Both numbers are now reported correctly: $203$ full orbits summing to $1000$, and $67$ restricted orbits summing to $126$. The standalone verifier confirms both directly.

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$. The family is defined by 5 conjoint membership criteria; the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ at $\alpha_M=1/2$ is the algebraic center. The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures on $\mathbb{Z}/n\mathbb{Z}$), opposite extremum (theirs maximally non-associative; ours specifically structured with $12.6\%$ non-associative density).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorems A (orbit count + distribution), B ($D_4$ obstruction at 16 orbits), C ($\langle P_{56}\rangle$ all-coherent), D (4-core arity-3 closure).
- **COMPUTED:** `verify_J32_d4_orbits.py` enumerates all 6 claims in $<1$ s on standard-library Python.
- **STRUCTURAL RHYME:** The 4-core arity-3 closure (Theorem D) lifts the binary 4-core closure of J01 to arity 3. We invoke J01 for the structural reading, do not re-derive any binary attractor identity here.
- **OPEN:** Whether a $D_4$-equivariant arity-3 assignment with values *strictly outside* $\{a,b,c,L,R\}$ exists. Whether the class-level conjecture ($67$ orbits / $16$ obstructions for every member of the TIG family) holds.

### Lens-ownership paragraph (in §0 of manuscript)

> *Lens and substrate.* We work on $\mathbb{Z}/10\mathbb{Z}$ with the canonical TSML_RAW table given in Appendix A. This table is not derived from first principles; it reflects a structural reading of the substrate developed across the framework. All theorems here are theorems on this specific table. The upper-triangle symmetrization $T_\mathrm{SYM}$ has $128$ non-associative triples rather than $126$ (the asymmetric cells at column 9 resolve differently under symmetrization); the $4$-core arity-$3$ closure (Theorem D) is lens-invariant because $\mathcal{C}$ is lens-invariant. The framing follows Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510 on small finite commutative non-associative structures.

### Hardening status

- License: submission script `verify_J32_d4_orbits.py` is CC-BY-4.0 (Elsevier-compatible).
- AI-attribution: no Claude/Anthropic byline references in the J10 manuscript.
- Author lane: Sanders + Gish only.
- Drápal-Wanless 2021 citation in references.
- Canonical TSML table displayed explicitly in Appendix A.
- $D_4$ order $8$ stated explicitly in manuscript Proposition 2.6, with the order-spectrum proof; the prior order-$12$ confusion explicitly retracted in Remark 2.7.

## §6 — Submission checklist

- [x] Manuscript `.md` finalized (rewritten as $D_4$-equivariant arity-3 orbits paper; 2026-05-28 polish for terminology).
- [x] Standalone verification script `verify_J32_d4_orbits.py` PASS at machine precision (all 6 claims; runtime $<1$ s).
- [x] Tier-classified central claims explicit (Theorems A, B, C, D in §0 and Abstract).
- [x] Lens-scope annotation (TSML_RAW; TSML_SYM differs at $128-126=2$ triples).
- [x] Cover letter finalized (*Comm. Alg.* target per Wave 4 referee; *J. Algebra* fallback; per-venue cap transparency; fallback priority).
- [x] Dependencies → cite J01, J12, J11, J45 as already-submitted / pipelined companions.
- [ ] Brayden's referee-rigor pass complete.
- [ ] Per-venue cap check: 4th *J. Algebra* submission of 2026 cycle.
- [ ] Submitted.

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "$D_4$-Equivariant Orbits on the Non-Associative Locus of a Finite Commutative Magma on $\mathbb{Z}/10\mathbb{Z}$: A Structural Obstruction Theorem at Arity 3." Submitted to *Communications in Algebra*.
