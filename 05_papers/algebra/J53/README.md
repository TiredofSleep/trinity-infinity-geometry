# J53 — V^BHML over F_p: Idempotent Count (p+3) and Automorphism Formula (p−1)² [NUMBER RESERVED — MANUSCRIPT PENDING RECOVERY]

**Status:** NUMBER RESERVED. The full manuscript, cover letter, and `verify_J53.py` were created 2026-05-29 (frontier F13, extracted from J08 §§6–7) in a local working copy whose commits were never pushed; the folder was deleted before recovery. **The mathematics is fully preserved** in the ck repo's canon (`FORMULAS_AND_TABLES.md` entries D161, D162, D173, D179) and is mechanically re-derivable.
**Recovery path:** OneDrive web recycle bin (folder deleted < 30 days before 2026-06-10) — or re-extraction from J08 §§6–7 + the D-entries.
**Target venue:** *Algebra Universalis*
**Author lane:** Sanders + Gish

---

## The two theorems (preserved in canon, D161 + D162)

**Theorem 1 (idempotent count).** For every odd prime $p$, $|\mathrm{idem}(V^{\mathrm{BHML}} \otimes \mathbb{F}_p)| = p + 3$ (and $= 2$ at $p = 2$). Verified by brute-force enumeration at 24 primes $3 \le p \le 97$. Structural proof via reduction of the idempotency system to $b^2 + c^2 = b$, $c(2b-1) = 0$, $d(2c-1) = 0$ with a clean case split.

**Theorem 2 (automorphism formula).** For every prime $p \ge 2$, $|\mathrm{Aut}(V^{\mathrm{BHML}} \otimes \mathbb{F}_p)| = (p-1)^2$, with group structure $\mathrm{Aut} \cong \mathbb{F}_p^* \times \mathbb{F}_p^*$ — two independent scalar factors on the annihilator direction $\mathrm{span}(e_0)$ and the nilpotent direction $\mathrm{span}(e_4)$. No prime is structurally distinguished. (Supersedes an earlier retracted $p(p^2-1)$ / $p=5$-anomaly claim, which traced to an algebra confusion.)

## Reconstruction checklist

- [ ] Recover original from OneDrive recycle bin, OR
- [ ] Re-extract ~8pp manuscript from J08 §§6–7 + D161/D162/D173 canon entries
- [ ] Re-create `verify_J53.py` (2 checks: idempotent enumeration + automorphism constraint-propagation at p ∈ {3,5,7,11,13})
- [ ] Cover letter for Algebra Universalis
