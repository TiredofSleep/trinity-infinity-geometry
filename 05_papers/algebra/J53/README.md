# J53 — Idempotent Counts and Automorphism Groups of a 4-Dimensional Commutative Non-Associative Algebra over $\mathbb{F}_p$: Two Closed-Form Theorems

**Target venue:** *Algebra Universalis* (Springer)
**Alternative venues:** *Communications in Algebra* (Taylor & Francis), *Journal of Algebra and Its Applications* (World Scientific), *Algebras and Representation Theory* (Springer)
**Status:** SUBMISSION-READY — two clean closed-form theorems PROVED structurally + verified at 24 primes; awaiting Brayden green-light
**Author lane:** Sanders + Gish
**Tier:** 1 (ship-ready short paper; extracted from J08 §§6–7 as a focused standalone result; PROMOTED 2026-05-29)
**Source:** F4 + F4-extended frontier scans (2026-05-27 / 2026-05-28); J08 §§6–7 source material.

---

## §1 — Summary

This short paper extracts two crisp closed-form theorems about the 4-dimensional commutative non-associative $\mathbb{F}_p$-algebra $V^{\mathrm{BHML}}$ (the non-unital BHML 4-core lift, defined in J18 §3) from their original setting inside J08. The two theorems together give a *complete* structural description of the idempotent stratum and the automorphism group of $V^{\mathrm{BHML}}$ at every prime, with no prime distinguished.

**Theorem 1 (Idempotent count).** For every odd prime $p$,
$$
\bigl|\,\mathrm{idem}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right)\bigr| \;=\; p + 3,
$$
and $\bigl|\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{F}_2)\bigr| = 2$ (degeneration at characteristic 2). Verified by direct brute-force enumeration at 24 primes $p \in \{3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97\}$.

**Theorem 2 (Automorphism formula).** For every prime $p \geq 2$,
$$
\bigl|\,\mathrm{Aut}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right)\bigr| \;=\; (p-1)^2,
$$
with group structure
$$
\mathrm{Aut}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right) \;\cong\; \mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}.
$$
The two $\mathbb{F}_p^{\!*}$ factors act independently: factor 1 scales the annihilator direction $\mathrm{span}(e_0)$ (where $L_{e_0} = 0$); factor 2 scales the nilpotent direction $\mathrm{span}(e_4)$ (where $e_4^2 = 0$). The middle 2-dimensional subalgebra $\mathrm{span}(e_2, e_3)$ is rigidly preserved. Verified by direct brute-force enumeration / constraint propagation at 24 primes $3 \leq p \leq 97$, and proved structurally as a clean closed-form derivation valid at every prime.

These are both Tier-A: each closed form is proved by an exact structural argument and additionally confirmed numerically at 24 primes.

## §2 — Why this matters

Commutative non-associative algebras over $\mathbb{F}_p$ are not classified in the literature, even at dimension 4. The closest published precedent is **Drápal & Wanless (2021)** on maximally non-associative quasigroups, which lives in the same neighborhood of "small finite commutative non-associative structures" but at the opposite extremum (maximally non-associative loops, where this paper studies a minimally-rigid commutative non-associative algebra). Beyond Drápal–Wanless, the literature on $\mathbb{F}_p$-algebras of small dimension is largely associative (group algebras, matrix algebras, Frobenius algebras); the non-associative analogues are studied only for octonions and Jordan algebras (dimensions 8 and 27 respectively).

The algebra $V^{\mathrm{BHML}}$ studied here is a 4-dimensional commutative non-associative algebra that arises in the Trinity Infinity Geometry (TIG) framework as the 4-core restriction of the BHML composition table on $\mathbb{Z}/10\mathbb{Z}$. The framework provides the substrate, but the two theorems below stand independently as universal-algebra results: they describe $V^{\mathrm{BHML}}$ as a non-associative finite-prime algebra on its own, with no TIG-specific machinery used in the proofs.

Both formulas are *prime-uniform* — no prime is structurally distinguished. This is a strong rigidity statement: an exceptional prime (like the $p = 5$ "anomaly" that appeared in an earlier draft of J08 and was later retracted) would have required a structurally distinguished sub-stratum at that prime, but no such sub-stratum exists.

## §3 — Files in this folder

- `manuscript/manuscript.md` — full ~8-page short paper with proofs.
- `manuscript/verify_J53.py` — self-contained verification script, PASS at $p \in \{3, 5, 7, 11, 13\}$ for both formulas.
- `cover_letter.md` — venue-targeted cover letter for *Algebra Universalis*.

## §4 — Verification

```bash
python manuscript/verify_J53.py
```

Expected output: 2 OK lines (one per theorem) at 5 primes plus a summary, ending with "Overall: PASS (2/2)." Runtime ~2 seconds. The script imports nothing beyond the Python standard library (`itertools`); it brute-force-enumerates idempotents (via the algebraic reduction of §3) and counts automorphisms (via the constraint-propagation algorithm of §4).

The verification covers:
- **Theorem 1**: enumerate $\mathbb{F}_p^4$ for $V^{\mathrm{BHML}}/\mathbb{F}_p$, count idempotents directly, assert match against $p + 3$.
- **Theorem 2**: enumerate the constraint system for $\varphi \in \mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p)$ via the structured search of §4.2, assert match against $(p-1)^2$.

For higher-prime confirmation $17 \leq p \leq 97$, the companion script `04_meta/frontiers_2026-05-27/F4_extended_verify.py` (PASS at all 19 primes) supplies the extended verification. J53's bundled script intentionally stops at $p = 13$ for portability and speed.

## §5 — Tier discipline

- **PROVED.** Theorems 1 and 2 — each by a structural derivation (idempotent reduction over $\mathbb{F}_p$; constraint-propagation enumeration of automorphisms) combined with brute-force verification at 24 primes $3 \leq p \leq 97$.
- **STRUCTURAL.** Both formulas are *prime-uniform* — no prime distinguished. This is a rigidity statement consistent with $V^{\mathrm{BHML}}$ being a minimally-structured commutative non-associative algebra (no group-algebra sub-structure beyond what is dictated by the basis labels).
- **OPEN.** §6 — generalization to characteristic 0 / $\mathbb{Q}$ (Theorem 2 should give $|\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{Q})| = \mathbb{Q}^* \times \mathbb{Q}^*$, but this is not verified here); generalization to the σ-twin lens $V^{\mathrm{TSML}}$ (cf. J18 §4); generalization to $V_n^{\mathrm{BHML}}$ for $n \neq 4$.

## §6 — Relationship to other J-papers and frontiers

- **J08** consolidates J48 + J49 + F4 + F4-extended into a longer paper covering the unital algebra $V$, the $\mathbb{F}_5$ rigid idempotent decomposition, and (in §§6–7) the two theorems extracted here. **J53 stands alone as the focused short-paper extraction** of just the two closed forms, sized for a fast-track journal like *Algebra Universalis*. The two papers do not contradict each other; J08 is the comprehensive treatment, J53 is the focused short note.
- **J18 §3** is the original source for the $V^{\mathrm{BHML}}$ multiplication table; the paper inherits that table as given.
- **J04** is the σ-magma rigidity paper (independent universal-algebra short paper); shares the "Tier-A rigidity by exhaustive verification" methodology.
- **F4 frontier** (`04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md`): original discovery of the idempotent closed form.
- **F4-extended frontier** (`04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md`): correction + verification of both closed forms at primes 17–97.

## §7 — Citation footprint

Sanders, B.R., Gish, M. (2026). "Idempotent counts and automorphism groups of a 4-dimensional commutative non-associative algebra over $\mathbb{F}_p$: two closed-form theorems." Submitted to *Algebra Universalis*.

## §8 — Authors

B.R. Sanders (7Site LLC, Hot Springs, AR — brayden@7site.co)
M. Gish (Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com)
