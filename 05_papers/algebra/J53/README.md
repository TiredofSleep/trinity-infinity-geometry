# J53 — V^BHML over F_p: Idempotent Count (p+3) and Automorphism Formula (p−1)²

**Status:** PRESENT — SUBMISSION-READY. The manuscript (`manuscript/manuscript.md`), cover letter, and `manuscript/verify_J53.py` are all present in this folder; the earlier "pending recovery / folder deleted" status is **stale** (the files were recovered/re-extracted). The two theorems are canon **D161/D162** (also cited at D173/D179).
**Target venue:** *Algebra Universalis*
**Author lane:** Sanders + Gish
**Tier:** 1

---

## The two theorems (preserved in canon, D161 + D162)

**Theorem 1 (idempotent count).** For every odd prime $p$, $|\mathrm{idem}(V^{\mathrm{BHML}} \otimes \mathbb{F}_p)| = p + 3$ (and $= 2$ at $p = 2$). Verified by brute-force enumeration at 24 primes $3 \le p \le 97$. Structural proof via reduction of the idempotency system to $b^2 + c^2 = b$, $c(2b-1) = 0$, $d(2c-1) = 0$ with a clean case split.

**Theorem 2 (automorphism formula).** For every prime $p \ge 2$, $|\mathrm{Aut}(V^{\mathrm{BHML}} \otimes \mathbb{F}_p)| = (p-1)^2$, with group structure $\mathrm{Aut} \cong \mathbb{F}_p^* \times \mathbb{F}_p^*$ — two independent scalar factors on the annihilator direction $\mathrm{span}(e_0)$ and the nilpotent direction $\mathrm{span}(e_4)$. No prime is structurally distinguished. (Supersedes an earlier retracted $p(p^2-1)$ / $p=5$-anomaly claim, which traced to an algebra confusion.)

## Reconstruction checklist — DONE

- [x] Manuscript present (`manuscript/manuscript.md`)
- [x] `verify_J53.py` present (2 checks: idempotent enumeration + automorphism constraint-propagation at p ∈ {3,5,7,11,13})
- [x] Cover letter present

*(The folder is complete; this checklist is retained as history.)*
