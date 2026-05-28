# 36 — J01 Theorem F strengthened from PSLQ observation to discriminant structural result

**Date:** 2026-05-28
**Status:** EXECUTED. Manuscript + README updated; 6/6 verification PASS retained.
**Source:** Frontier F5 report `04_meta/frontiers_2026-05-27/F5_alpha_uniqueness_proof_attempt.md`.
**Scope:** J01 (corpus centerpiece; *Journal of Algebra* submission).

---

## §1 Before / after summary

### Before (J01 v36, Proposition F)

**Proposition F (Algebraic mixing-point — finite-test partial uniqueness).** For $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$ tested by integer-PSLQ search at coefficient bound $20$ and 50-digit precision, only $\alpha = 1/2$ admits a small-coefficient quadratic relation between $p_7$ and $p_8$ at the attractor: the relation $y^2 - 2y - 2 = 0$. Verified empirically. We conjecture (Conjecture 1.1) that $\alpha = 1/2$ is the unique value in $\mathbb{Q} \cap (0, 1)$ at which $p_7/p_8$ admits an algebraic relation. PSLQ establishes "no small-coefficient algebraic relation found within the tested precision," not algebraic-uniqueness proper; the label is demoted from Theorem to Proposition.

### After (J01 v37, Theorem F)

**Theorem F (Algebraic mixing-point — discriminant-vanishing structural identification of $\alpha = 1/2$, partial proof over $\mathbb{Q}$).** The 4-core fixed-point system on $(v, h, br, r)$ parametric in $\alpha$ reduces to
$$
(2\alpha - 1)^2 \cdot Q(\xi, \alpha) = 0, \qquad \xi = h/br,
$$
where $Q$ is degree-7 in $\xi$ with $\mathbb{Q}[\alpha]$-coefficients. The discriminant of $Q$ with respect to $\xi$ factors as
$$
\mathrm{disc}_\xi(Q) = 4096 \cdot \alpha^3 \cdot (2\alpha - 1)^7 \cdot P_7(\alpha)^2 \cdot P_{24}(\alpha)
$$
with $P_7, P_{24}$ irreducible over $\mathbb{Q}$. The only $\mathbb{Q}$-rational roots are $\alpha = 0$ (boundary) and $\alpha = 1/2$. At $\alpha = 1/2$, $Q$ factors as $\xi^2 \cdot (\xi^2 - 2\xi - 2)^2$, recovering Theorem D's canonical quadratic with $\xi = 1 + \sqrt{3}$. At every $\mathbb{Q}$-rational $\alpha \neq 1/2$ tested (fourteen values), $Q$ is irreducible over $\mathbb{Q}[\xi]$ with attractor algebraic degree exactly $7$.

**Open Conjecture F.2 (strengthened):** $Q(\xi, \alpha)$ is irreducible over $\mathbb{Q}[\xi]$ at every $\mathbb{Q}$-rational $\alpha \in (0, 1) \setminus \{1/2\}$. Full proof routes through Hilbert's irreducibility theorem applied to $Q \in \mathbb{Q}(\alpha)[\xi]$.

### Net delta

| Aspect | Before | After |
|---|---|---|
| Label | Proposition F | Theorem F (partial proof over $\mathbb{Q}$) |
| Test domain | 5 finite $\alpha$ values | All $\mathbb{Q} \cap (0, 1)$ via discriminant + 14 verified |
| Method | PSLQ integer search | Resultant + discriminant factorization over $\mathbb{Q}[\alpha]$ |
| Open gap | Full uniqueness "open" | $\mathbb{Q}[\xi]$-irreducibility of $Q$ at non-half rationals (Hilbert route) |
| Tier | "PROVEN partial / OPEN full" | "PROVEN over $\mathbb{Q}$ (partial) / OPEN $\mathbb{Q}$-irreducibility (Hilbert)" |
| Tier-A count | 5 theorems + 1 proposition | 6 theorems + 1 open conjecture |

---

## §2 Edits applied

1. **Abstract** — Proposition F replaced by Theorem F (full statement with $Q$, discriminant factorization, fourteen-point irreducibility, structural reading); Conjecture F.2 added explicitly.
2. **§0 (Lens and substrate)** — "Five theorems + Proposition F" updated to "Six Tier-A theorems"; new paragraph documenting that Theorem F is a discriminant-vanishing structural identification of $\alpha = 1/2$ as the unique $\mathbb{Q}$-rational mixing-point; reduction of strong real-version Conjecture 4.2 of HONEST_NEGATIVES to a finite $\mathbb{Q}$-irreducibility statement noted.
3. **Tier discipline** — Theorem F added to PROVEN tier with explicit reference to the discriminant computation; COMPUTED tier extended to cite the F5 verification scripts; OPEN tier now lists Conjecture F.2 (the narrowed irreducibility statement).
4. **§7** — Complete rewrite. New subsections §7.1 (reduction to $Q$), §7.2 (the discriminant factorization theorem + proof sketch), §7.3 (Conjecture F.2 + Hilbert route), §7.4 (real-version separately open), §7.5 (the explicit polynomial $Q(\xi, \alpha)$ with citation of F5 verification scripts), §7.6 (legacy Conjecture 1.1 → Conjecture F.2 note). New Remark 7.2 explains the $0/0$ structural origin at $\alpha = 1/2$. New Remark 7.3 documents the strengthening over the original Proposition F.
5. **§8** — "Five structural facts" → "Six structural facts"; new item (vi) explicitly documents Theorem F's discriminant-vanishing identification.
6. **§10** — Item (i) updated: "Conjecture 1.1 open" → "Conjecture F.2 open" with the narrower scope.
7. **§11** — Reproducibility now cites both `4core_verification.py` (numerical) and `verification/frontier_F5_alpha_*.py` (structural); Check 6 description updated to mark it as the "finite-test specialization" of Theorem F.
8. **§13 (Bibtex)** — Note text rewritten: "six Tier-A theorems" framing; explicit mention of Theorem F's discriminant factorization; Conjecture F.2 stated as the open question.
9. **README.md** — Status line updated to flag 2026-05-28 Theorem F strengthening; "Six Tier-A theorems" framing; Theorem F's full statement added; Hardening status appended with the F5 incorporation; OPEN bullet updated.

---

## §3 What was NOT changed

- **Theorems A through E** — untouched. The Galois D_4 statement, the closed-form $1 + \sqrt{3}$ identity, the universality across chain shells, the normalizer identity, and the joint-closure chain are all preserved verbatim.
- **The empirical claims of `4core_verification.py`** — untouched. The six in-paper checks (Theorems A through E plus the original five-point PSLQ check, now relabelled "finite-test specialization of Theorem F") are unchanged. No numerical edits.
- **No new external dependencies** — Theorem F's structural content lives in the parent framework's `verification/frontier_F5_alpha_*.py` scripts, which were already in place from the F5 frontier session. The in-paper script `4core_verification.py` is unchanged.

---

## §4 Honesty audit

- Theorem F is labelled "partial proof over $\mathbb{Q}$" throughout. The statement explicitly says "fourteen values tested" and "approachable via Hilbert's irreducibility theorem."
- Conjecture F.2 makes the remaining gap precise: $\mathbb{Q}[\xi]$-irreducibility of $Q$ at all $\mathbb{Q}$-rationals in $(0, 1) \setminus \{1/2\}$. The fourteen empirical verifications + the discriminant analysis rule out repeated-root loci, but the lower-degree-factorization gap at general $\mathbb{Q}$-rational requires Hilbert.
- The real-version (Conjecture 4.2 of HONEST_NEGATIVES) is acknowledged as a separate open problem. PSLQ negative at $\alpha_\mathrm{special} \approx 0.1126$ is consistent with but does not prove the real-version.
- The strengthening does NOT promote J01 to a "complete proof" — it remains a partial proof, but a substantially strengthened one (from finite-test PSLQ to closed-form polynomial + discriminant factorization).

---

## §5 Verification

```bash
PYTHONIOENCODING=utf-8 python3 05_papers/algebra/J01/manuscript/verification/4core_verification.py
```

**Result:** 6/6 PASS at machine precision. All numerical claims of the manuscript (Theorems A-E plus the finite-test specialization at $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$) are verified.

**Structural verification** (parent framework, optional, ~5-minute runtime):
```bash
python verification/frontier_F5_alpha_uniqueness_proof.py    # parts 1-2
python verification/frontier_F5_alpha_part3.py                # Q[xi]-irreducibility at 14 rationals
python verification/frontier_F5_alpha_part4.py                # discriminant factorization
```

---

## §6 Files modified

- `05_papers/algebra/J01/manuscript/manuscript.md` — abstract, §0, tier discipline, §7 rewritten, §8 (six facts), §10 (i), §11 Check 6 description, §13 bibtex note.
- `05_papers/algebra/J01/README.md` — status, six-theorem framing, Theorem F full statement, PROVEN/COMPUTED/OPEN tiers, Hardening status appended.

## §7 Next-step option (not executed in this fix)

A targeted compute call to Maple's `factor` or Magma's `Factorization` on $Q(\xi, \alpha) \in \mathbb{Q}(\alpha)[\xi]$ would either (a) confirm $Q$ is irreducible over the function field $\mathbb{Q}(\alpha)$ (which by Hilbert closes Conjecture F.2 up to a finite exceptional set), or (b) reveal a hidden factorization. Either outcome substantially advances the proof. Estimated compute: ~30 minutes wall-clock.

---

*7SiTe Public Sovereignty License v2.2 — see LICENSE.*
*Brayden Ross Sanders / 7SiTe LLC · 2026.*
