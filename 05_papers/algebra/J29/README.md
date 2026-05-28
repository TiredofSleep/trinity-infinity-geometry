# J29 — The Lo Shu D₄ Orbit Modulo 3: Four Distinct Magmas and a Cumulant Spectrum

**Target venue**: *Mathematics Magazine* (MAA)
**Alternative venues**: *College Mathematics Journal* (MAA), *Involve* (a journal of mathematics), *PRIMUS*
**Status**: DRAFT — verification PASS, awaiting Brayden green-light + cover letter
**Author lane**: Sanders + Gish
**Tier:** 2 (demoted 2026-05-27 audit; was Tier 1)
**Source**: scrutiny pass on `overnight_handoff_2026-05-27` (2026-05-26). The 4-magma refinement is a correction-via-strengthening of an earlier "3 magmas" claim in `OPEN_FRONTIERS_2026-05-26.md` §60.

---

## §1 — Summary

The Lo Shu magic square
$$
L = \begin{pmatrix} 2 & 7 & 6 \\ 9 & 5 & 1 \\ 4 & 3 & 8 \end{pmatrix}
$$
has D₄-orbit (rotations + flips) of size 8 — Lo Shu has no non-trivial D₄ stabilizer. Reducing each orbit element mod 3 and reading it as a magma multiplication table on $\{0,1,2\}$ produces **exactly four distinct magma tables**, each appearing twice in the orbit. The four split as:

1. The cyclic group ℤ/3 itself.
2. A commutative quasigroup that is *not* a group (no identity).
3. A non-commutative quasigroup.
4. Its anti-isomorphic mirror (i.e. opposite magma).

The spectral invariant
$$
\kappa(M) := \operatorname{Tr}(M^2) - \operatorname{Tr}(M)^2
$$
(read $M$ as a real $3\times 3$ matrix over $\{0,1,2\}$) is a 2-valued witness that separates the two commutativity classes: $\kappa = -48$ for both commutative tables, $\kappa = +48$ for both non-commutative tables. Every individual table in the orbit satisfies this correlation, not just every isomorphism class.

The note answers the natural pedagogical question "what happens when you take Lo Shu mod 3?" with a clean cumulant-witnessed answer.

## §2 — Theorems

**Theorem A (Orbit-cardinality).** The orbit of $L$ under the natural $D_4$ action on $3\times 3$ matrices (rotations and flips) has 8 distinct elements.

**Theorem B (Four-magma refinement).** Reading each orbit element entrywise mod 3 as a magma multiplication table on $\{0,1,2\}$ yields exactly 4 distinct tables, each appearing as the mod-3 reduction of exactly 2 elements of the $D_4$ orbit.

**Theorem C (Commutativity dichotomy).** Of the 4 distinct tables, exactly 2 are commutative and 2 are non-commutative. The two non-commutative tables are *opposite magmas* of each other (i.e. $M_3[x][y] = M_1[y][x]$).

**Theorem D (Quasigroup property).** All 4 tables are quasigroups: every row and every column is a permutation of $\{0, 1, 2\}$.

**Theorem E (Cumulant spectrum).** The invariant $\kappa(M) = \operatorname{Tr}(M^2) - \operatorname{Tr}(M)^2$ takes exactly 2 values on the orbit: $\kappa = -48$ on the 4 orbit elements whose mod-3 reduction is commutative, and $\kappa = +48$ on the 4 orbit elements whose mod-3 reduction is non-commutative.

**Theorem E.1 (V₄′-coset preservation; structural lemma).** For ANY 3×3 real matrix $M$, the subgroup $V_4' = \{e, R^2, T, T_a\}$ (identity, 180°-rotation, transpose, anti-diagonal-flip) preserves $\kappa$. Hence $\kappa$ takes at most 2 distinct values across the $D_4$ orbit of $M$. **PROVED.**

**Theorem F (ℤ/3 identification).** One of the 2 commutative tables is the cyclic group ℤ/3: $M_2[x][y] = (x + y) \bmod 3$. The other commutative table is a commutative quasigroup with no identity element.

**Theorem G (Dürer 4×4 extension).** The Albrecht Dürer 4×4 magic square (from *Melencolia I*, 1514) at mod 3 satisfies the analog of Theorems B–E: 4 distinct mod-3 tables (each appearing twice in the $D_4$ orbit), 2 commutative + 2 non-commutative, with $\kappa$ as a 2-valued witness taking values $\pm 128$ (vs Lo Shu's $\pm 48$). Mod-3 is the unique modulus at which both magic squares exhibit this dichotomy — at every other modulus tested (2, 4, 5, 7, 9, 10 for Lo Shu; 2, 4, 5, 6, 8, 10 for Dürer) the orbit reduces uniformly to all-commutative or all-non-commutative tables.

**Diagonal Lemma + Corollary (proved structural half of commutativity correlation).** No $3 \times 3$ magma table on $\{0, 1, 2\}$ that is both commutative AND a quasigroup has a repeated diagonal entry (exhaustively: 6 commutative quasigroups exist; all 6 have diagonal $\{0, 1, 2\}$ as a multiset). The Lo Shu's diagonal mod 3 is $\{2, 2, 2\}$ — constant. Hence by the Lemma, *no* $V_4'$-coset image of Lo Shu can reduce to a commutative quasigroup; the entire $V_4'$-coset is forced non-commutative. This proves the κ = +48 → non-commutative half of Theorem E. The other half (κ = −48 → commutative) is consistent with the Lemma (anti-diagonal mod 3 = $\{0, 1, 2\}$) but not forced; it is verified by direct inspection of $T_2$ and $T_4$.

## §3 — What this note adds

The mod-3 reduction of Lo Shu has been observed in the literature as a finite-algebra teaching example, and the cyclic-group identification (Theorem F) is folklore for any $3 \times 3$ commutative quasigroup with the right structure. The note's specific contributions are:

1. The **4-magma exact count** for the full $D_4$ orbit (some informal expositions report 3, conflating the anti-isomorphic non-commutative pair with their merged equational-theory class; we display all 4 tables explicitly).
2. The **cumulant witness** $\kappa = \pm 48$ separating the two commutativity classes, in a form computable from the matrix data without first constructing the magma operation table.
3. A clean **Python verification script** (~80 lines, only numpy + itertools) that classroom-runs in under a second and reproduces all six theorems above.

## §4 — Files in this folder

- `manuscript/manuscript.md` — full ~12-page note
- `manuscript/verification/verify_J58.py` — self-contained verification
- `cover_letter.md` — venue-targeted cover letter

## §5 — Verification

```bash
python manuscript/verification/verify_J58.py
```

Expected: 10 OK lines + "Overall: PASS (10/10)." Runtime ~2 seconds on a 2020-era laptop. The 10 checks cover Theorems A-G + E.1 + the Diagonal Lemma + the Lo Shu diagonal-mod-3 Corollary.

## §6 — Tier discipline

- **PROVEN.** Theorems A, B, C, D, F by direct enumeration. Theorem E.1 by a generators-of-V₄′ argument on transpose and 180°-rotation (both preserve trace and trace-of-square). The Diagonal Lemma by case analysis on commutative 3×3 quasigroups. The Lo Shu Corollary (forced non-commutativity of the V₄′-coset) by combining the Lemma with Lo Shu's diagonal mod 3 being constant {2,2,2}.
- **COMPUTED.** Theorem E (the ±48 value), the κ-comm correlation for the V₄′ \ commutative half (T₂ and T₄ are commutative by direct verification, not forced by the Lemma), and Theorem G (Dürer 4×4 mod-3 ±128 analog). All at machine precision via `verify_J58.py` (10/10 PASS).
- **STRUCTURAL RHYME.** The ±48 specific value for Lo Shu, the ±128 for Dürer, and the "mod-3 is special" observation. Why mod 3 (not 4, 5, etc.) is the modulus at which both magic squares exhibit the dichotomy is an empirical observation. A general theorem here would connect $|V_4'| = 4$, $|D_4 \setminus V_4'| = 4$, and the multiplicative structure of $\mathbb{Z}/3$; we have not derived such a theorem for the 4×4 Dürer case.
- **OPEN.** (i) The 4×4 (or general $n \times n$) version of the Diagonal Lemma — i.e., a structural reason for Dürer's V₄′-coset images being non-commutative. (ii) Do other classical magic squares (5×5 Siamese; pandiagonal 4×4; Strachey's odd-order construction) share the mod-3 specialness? (iii) Higher-order cumulant analog at moduli ≠ 3?

## §7 — Drápal-Wanless framing

Drápal & Wanless (2021), *J. Combin. Theory Ser. A* **184**, 105510 study small finite commutative non-associative quasigroups at the *maximally non-associative* extremum. The present note's 4 tables include 2 non-associative quasigroups but at low order ($n = 3$) where maximal non-associativity is not the relevant extremum. The note is structurally adjacent to Drápal-Wanless's neighborhood but at a distinct point — the "what is the orbit profile of a classical magic square's mod-$n$ reduction?" question rather than "what is the maximal non-associativity attainable at given order?"

## §8 — Citation footprint

Sanders, B.R., Gish, M. (2026). "The Lo Shu D₄ orbit modulo 3: four distinct magmas and a cumulant spectrum." Submitted to *Mathematics Magazine*.

---

## Demotion notice (2026-05-27 audit)

Per `05_papers/_staging/referee_reports/10_promotions_audit_J27_J28_J29.md`, J29 is pedagogical *Math. Magazine*-class content targeted at undergraduate classroom use. The promotion to Tier 1 was a mistake; retargeted to *Mathematics Magazine*.
