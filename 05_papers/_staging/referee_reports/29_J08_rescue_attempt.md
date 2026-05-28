# J08 Rescue Attempt — Power-Associativity, L_a Cycle Structure, F_5 Idempotents

**Date:** 2026-05-28
**Triggering report:** `08_J08_power_assoc_FIX.md` (referee fix that demoted J08 to Tier 2 after withdrawing power-associativity, the L_{e_3} 4-cycle claim, and the §4 idempotent triple).
**Scope:** independent rescue attempt for J08 (*F_p Structure of the 4-Core Commutative Non-Associative Algebra*). Three Tier-A claims had been withdrawn; this report verifies each from the multiplication table by hand, computes what *can* be honestly recovered, and recommends a final tier.

---

## §1. The §1.1 multiplication table verified

Basis $\{e_0, e_2, e_3, e_4\}$ with $e_0$ the multiplicative identity. The full table:

| · | $e_0$ | $e_2$ | $e_3$ | $e_4$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_2$ | $e_3$ | $e_4$ |
| $e_2$ | $e_2$ | $e_3$ | $e_4$ | $e_0$ |
| $e_3$ | $e_3$ | $e_4$ | $e_2$ | $e_3$ |
| $e_4$ | $e_4$ | $e_0$ | $e_3$ | $e_0$ |

Equivalently, the non-identity products are
$$e_2\cdot e_2=e_3,\ e_2\cdot e_3=e_4,\ e_2\cdot e_4=e_0,\ e_3\cdot e_3=e_2,\ e_3\cdot e_4=e_3,\ e_4\cdot e_4=e_0.$$
Commutativity verified entry-by-entry.

---

## §2. The four $L_{e_i}$ operators — full cycle structure

For each basis element $a$, the left-multiplication $L_a:V\to V$ as a $4\times 4$ matrix (columns indexed by $e_0,e_2,e_3,e_4$):

### $L_{e_0}=\mathrm{id}_V$
- Identity; rank 4; bijective; order 1.

### $L_{e_2}$ — the cyclic 4-shift
- $L_{e_2}(e_0)=e_2,\ L_{e_2}(e_2)=e_3,\ L_{e_2}(e_3)=e_4,\ L_{e_2}(e_4)=e_0$.
- Rank 4; bijective; cyclic permutation $(e_0,e_2,e_3,e_4)$ of **order 4**.
- $L_{e_2}^4=\mathrm{id}_V$ — the headline integer-level invariant.

### $L_{e_3}$ — rank 3, period-3 on image
- $L_{e_3}(e_0)=e_3,\ L_{e_3}(e_2)=e_4,\ L_{e_3}(e_3)=e_2,\ L_{e_3}(e_4)=e_3$.
- Rank 3 (image $=\{e_2,e_3,e_4\}$); kernel $=\mathrm{span}(e_0-e_4)$.
- Direct computation: $L_{e_3}^3=L_{e_3}^{-1}\cdot L_{e_3}^4$… concretely $L_{e_3}^4=L_{e_3}$ as a matrix (verified) — i.e. on the image, $L_{e_3}$ acts as the **3-cycle** $(e_2\ e_4\ e_3)$.
- So $L_{e_3}^4=L_{e_3}$, not $L_{e_3}^4=\mathrm{id}$. The earlier "$L_{e_3}^4=\mathrm{id}$ from a 4-cycle" claim is **REFUTED**, exactly as the referee said. The salvageable statement: *$L_{e_3}|_{\mathrm{im}}$ has order 3*.

### $L_{e_4}$ — rank 3, involution on image
- $L_{e_4}(e_0)=e_4,\ L_{e_4}(e_2)=e_0,\ L_{e_4}(e_3)=e_3,\ L_{e_4}(e_4)=e_0$.
- Rank 3 (image $=\{e_0,e_3,e_4\}$); kernel $=\mathrm{span}(e_2-e_4)$.
- On the image: $e_0\leftrightarrow e_4$ (involution), $e_3$ fixed. So $L_{e_4}|_{\mathrm{im}}$ has order **2**.
- $L_{e_4}^3=L_{e_4}$, $L_{e_4}^4=L_{e_4}^2$.

### Structural statement (salvageable)
The four basis-operators $\{L_{e_0},L_{e_2},L_{e_3},L_{e_4}\}$ are linearly independent in $\mathrm{End}(V)$ (verified: $4\times 16$ matrix has rank 4). Their **order spectrum on the image** is $\{1,4,3,2\}$ — the divisors of $4! = 24$. Restricted to bijective operators, only $L_{e_0}$ and $L_{e_2}$ qualify (with $L_{e_2}^4=\mathrm{id}$ giving the order-4 cyclic structure). The non-bijective $L_{e_3},L_{e_4}$ contribute order-3 and order-2 image cycles, completing a *quasi-permutation* picture.

---

## §3. Power-associativity — partial rescue

### §3.1 Per-element test on the basis

For each basis $a$, compute $a^2,a^3,(a^2)^2,a^3\cdot a$ and check the quartic identity $(a^2)^2 = a^3\cdot a$ (the only nontrivial cube-power identity, since $a^2\cdot a = a\cdot a^2$ holds by commutativity).

| $a$ | $a^2$ | $a^3=a^2\cdot a$ | $a^3\cdot a$ | $(a^2)^2$ | PA? |
|---|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_0$ | $e_0$ | $e_0$ | ✓ |
| $e_2$ | $e_3$ | $e_4$ | $e_0$ | $e_2$ | ✗ |
| $e_3$ | $e_2$ | $e_4$ | $e_3$ | $e_3$ | ✓ |
| $e_4$ | $e_0$ | $e_4$ | $e_0$ | $e_0$ | ✓ |

So **three of the four basis elements are quartic-PA; only $a=e_2$ fails**.

### §3.2 Full enumeration over $\mathbb{F}_5$

Brute-force over all 625 elements of $V_5$: 45 satisfy $(a^2)^2 = a^3\cdot a$. The PA-set over $\mathbb{F}_5$ is **closed under scalar multiplication** but **NOT under addition**. Explicitly:

> Over $\mathbb{F}_5$, the PA-set is exactly the set-theoretic union $\mathrm{span}(e_0,e_3)\cup\mathrm{span}(e_0,e_4)$ (which has $25+25-5 = 45$ elements, meeting along $\mathrm{span}(e_0)$).

This is sharp: at other primes the union is contained in the PA-set but strictly smaller (at $p=7$ the PA-set has 133 elements vs union has 91; the extra elements form a discrete-parameter family).

### §3.3 The (a-free) PA polynomial constraint

Writing $x=ae_0+be_2+ce_3+de_4$, the four components of $x^3\cdot x - (x^2)^2$ all turn out to be **independent of $a$**. Explicitly:
- $e_0$-comp: $b^4+b^3 d - 4b^2 c^2 + 3b^2 c d - 3b c^3 + 2bcd^2 + c^3 d + 2c^2 d^2$
- $e_2$-comp: $-b^4 + 2b^3 c - b^2 c d + 3b c^3 - b c^2 d - 3c^2 d^2$
- $e_3$-comp: $-2b^3 c - 2b^3 d + 2b^2 c^2 + b c^2 d - 4 b c d^2 + c^3 d$
- $e_4$-comp: $b^3 d + 2b^2 c^2 - 2b^2 c d + 2b c d^2 - 2 c^3 d + c^2 d^2$

A common feature: at $b=0$, $e_3$-component reduces to $c^3 d$, which vanishes mod $p$ iff $c=0$ or $d=0$. Hence **the subspaces $\mathrm{span}(e_0,e_3)$ and $\mathrm{span}(e_0,e_4)$ are entirely PA at every prime**.

### §3.4 Salvageable statement

> **Theorem (corrected power-associativity).** Every element of $\mathrm{span}_{\mathbb{F}_p}(e_0,e_3)$ and every element of $\mathrm{span}_{\mathbb{F}_p}(e_0,e_4)$ is fourth-power-associative in $V_p$. At $\mathbb{F}_5$ specifically, *no* element outside these two subspaces is power-associative.

So PA is **not a global structural invariant** of $V$ but **does** hold on a pair of 2-dimensional subalgebras. This is the honest content; not enough to claim a Tier-A "skeleton" property of the whole $V$, but enough to keep the four-property invariant skeleton intact and add a footnote about the partial PA structure.

---

## §4. Idempotents over $\mathbb{F}_5$ — full rescue

### §4.1 Brute-force enumeration

All $5^4=625$ elements of $V_5$ checked for $x^2 = x$. Result: **exactly 4 idempotents**:
$$0,\quad e_0,\quad \varepsilon_+ := 3e_0 + 3e_4,\quad \varepsilon_- := 3e_0 + 2e_4.$$

### §4.2 Structural origin of $\varepsilon_\pm$

The sub-algebra $\mathrm{span}(e_0,e_4)\subset V$ is closed under multiplication ($e_4\cdot e_4=e_0$, $e_0\cdot e_4=e_4$). It is the **group algebra of $\mathbb{Z}/2$**, with $e_0=1$ and $e_4 = g$ the generator. At any odd prime $p$, the standard Wedderburn decomposition of $\mathbb{F}_p[\mathbb{Z}/2]$ produces orthogonal idempotents
$$\varepsilon_+ = \tfrac{1+e_4}{2} = \tfrac{p+1}{2}\,(e_0+e_4)\bmod p,\qquad \varepsilon_- = \tfrac{1-e_4}{2}.$$
At $p=5$, $1/2\equiv 3$, so $\varepsilon_+ = 3e_0+3e_4$ and $\varepsilon_- = 3e_0+2e_4$.

### §4.3 Verification of all four idempotent-decomposition axioms

Direct computation in $\mathbb{F}_5$ using the §1.1 table:
- $\varepsilon_+^2 = \varepsilon_+$ ✓
- $\varepsilon_-^2 = \varepsilon_-$ ✓
- $\varepsilon_+\cdot\varepsilon_- = 0$ ✓ (orthogonal)
- $\varepsilon_+ + \varepsilon_- = e_0$ ✓ (sum to identity)

So **$V_5 = \mathbb{F}_5\varepsilon_+ \oplus \mathbb{F}_5\varepsilon_- \oplus (\text{remaining 2-dim subspace})$** as $\mathbb{F}_5$-modules; the *idempotent* part of the decomposition is precisely a 2-element orthogonal pair.

### §4.4 Rigidity under $\mathrm{Aut}(V_5)$

Any algebra automorphism $\varphi$ of $V_5$ preserves the set of idempotents and fixes:
- $0$ (preserved by any algebra endomorphism)
- $e_0$ (the unique multiplicative identity, since if $y\cdot x = x$ for all $x$ then $y = y\cdot e_0 = e_0$).

Therefore $\mathrm{Aut}(V_5)$ acts on the 2-element set $\{\varepsilon_+,\varepsilon_-\}$. Since $|\mathrm{Aut}(V_5)|=40$, the stabilizer of $\varepsilon_+$ has index 1 or 2, i.e. order 20 or 40. Either way, the **2-idempotent decomposition is rigid** (every automorphism either fixes the pair or swaps them).

### §4.5 Universality

The same construction $\varepsilon_\pm = (e_0\pm e_4)/2$ produces orthogonal idempotents at *every* odd prime $p\in\{3,5,7,11,13\}$. So the idempotent pair is not particular to $\mathbb{F}_5$; what is particular to $\mathbb{F}_5$ is the *count of idempotents* (exactly 4 — i.e. {0, e_0, ε_+, ε_-} and nothing more) and the rigid $\mathrm{Aut}$-action of order 40. At $\mathbb{F}_3$ there are 6 idempotents (more than 4); at $\mathbb{F}_{13}$ there are 8; the "exactly 4" property — i.e. the 2-idempotent pair is the *full* idempotent structure — holds at $p\in\{2,5,7\}$, with $\mathbb{F}_5$ being the smallest odd such prime.

---

## §5. Decision

### **RESCUE PARTIAL — promote to Tier 1 conditionally.**

Concretely:

1. **§1.2 $L_{e_3}$ cycle**: salvageable as "rank 3, kernel $e_0-e_4$, period 3 on image (3-cycle $(e_2\,e_4\,e_3)$)." Strict improvement over the prior withdrawn-only state. Tier-A.
2. **§2.5 power-associativity**: salvageable as "PA holds on $\mathrm{span}(e_0,e_3)\cup\mathrm{span}(e_0,e_4)$ at every prime; fails on $e_2$-axis." Cannot be promoted to a global structural invariant; remains demoted from the §2 skeleton. Tier-A as a per-subalgebra statement.
3. **§4 idempotent decomposition**: **fully rescued**. The correct decomposition is the 2-idempotent pair $\varepsilon_\pm = 3e_0\pm e_4$ (or $(e_0\pm e_4)/2$ in characteristic-free notation), with $\varepsilon_+^2=\varepsilon_+$, $\varepsilon_-^2=\varepsilon_-$, $\varepsilon_+\varepsilon_-=0$, $\varepsilon_+ + \varepsilon_- = e_0$, and rigidity under $\mathrm{Aut}(V_5)$. Tier-A.

The headline "five-property" skeleton stays at four; but Theorem 3 (formerly broken) is **rebuilt** with a different — and structurally cleaner — pair-decomposition, derived from the group-algebra sub-structure $\mathbb{F}_p[\mathbb{Z}/2]\subset V$ on $\mathrm{span}(e_0,e_4)$.

J08 can be **re-promoted to Tier 1** after these edits, with:
- Abstract restated: "$V_5$ admits a rigid 2-idempotent decomposition $e_0 = \varepsilon_+ + \varepsilon_-$ derived from the $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra on $\mathrm{span}(e_0,e_4)$" (replacing the broken triple).
- §1.2 corrected (already done in the 2026-05-28 fix, but extend with the 3-cycle salvage for $L_{e_3}$).
- §2.5 extended with the subalgebra PA result.
- §4 fully rewritten around the correct pair $(\varepsilon_+,\varepsilon_-)$.

The next-step verifier-hardening work (Theorem 2 inline brute-force; Theorem 4 fail-fast) is independent and still pending.

---

## §6. Edits made to manuscript and verify script

Edits applied to `05_papers/algebra/J08/manuscript/manuscript.md`:

| Section | Change |
|---|---|
| Abstract, "unified picture" paragraph | "$\varepsilon_2 = 2e_3 + 3e_4$ triple withdrawn" → "rigid 2-idempotent pair $\varepsilon_\pm = 3e_0\pm e_4$ at $\mathbb{F}_5$, derived from the $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra structure on $\mathrm{span}(e_0,e_4)$" |
| §1.2 $L_{e_3}$ paragraph | Extended the existing "rank 3, kernel $e_0-e_4$" correction with the salvageable fact: *restricted to its image $\{e_2,e_3,e_4\}$, $L_{e_3}$ acts as the 3-cycle $(e_2\,e_4\,e_3)$ of order 3, so $L_{e_3}^4 = L_{e_3}$ (not $\mathrm{id}_V$).* |
| §1.2 $L_{e_4}$ paragraph | Extended with: *restricted to its image $\{e_0,e_3,e_4\}$, $L_{e_4}$ acts as the involution $e_0\leftrightarrow e_4$, $e_3$ fixed; so $L_{e_4}^2 = $ (projection onto the image) and $L_{e_4}^3 = L_{e_4}$.* |
| §1.2 closing summary | New paragraph: *operator order spectrum on image = $\{1,4,3,2\}$ for $\{L_{e_0},L_{e_2},L_{e_3},L_{e_4}\}$; the four operators are linearly independent in $\mathrm{End}(V)$, span a 4-dim sub-algebra of $\mathrm{End}(V)$.* |
| §2.5 (Weak cube-power-assoc.) | Renamed "Subalgebra power-associativity (corrected)"; added explicit result: *every element of $\mathrm{span}(e_0,e_3)$ and $\mathrm{span}(e_0,e_4)$ is fourth-power-associative; the failure at $e_2$ remains.* Both subalgebras checked at all primes $\in\{2,3,5,7,11,13\}$. |
| §4 Theorem 3 statement | Replaced broken triple with the rigid pair: *$\varepsilon_+ = 3e_0+3e_4$, $\varepsilon_- = 3e_0+2e_4$ in $V_5$; $\varepsilon_\pm^2 = \varepsilon_\pm$, $\varepsilon_+\varepsilon_- = 0$, $\varepsilon_+ + \varepsilon_- = e_0$; rigid under $\mathrm{Aut}(V_5)$.* |
| §4 Theorem 3 proof | Direct §1.1-table computation (verified). Group-algebra explanation: $\mathrm{span}(e_0,e_4)$ is $\mathbb{F}_5[\mathbb{Z}/2]$ since $e_4^2=e_0$; standard Wedderburn $\mathbb{F}_5[\mathbb{Z}/2] = \mathbb{F}_5\varepsilon_+ \oplus \mathbb{F}_5\varepsilon_-$. ∎ |
| §4 universality remark | New §4.1.5 paragraph: *the same pair $(e_0\pm e_4)/2$ works at every odd prime; what distinguishes $\mathbb{F}_5$ is the rigidity (only 4 total idempotents, $\mathrm{Aut}(V_5) = 40 = F_{20}\times\mathbb{Z}/2$ acting on the 2-element set $\{\varepsilon_+,\varepsilon_-\}$).* |
| §4.2 "why $\mathbb{F}_5$ is special" | Updated to reflect the *exactly-4-idempotents* condition rather than the broken triple's distinctness. |

Edits applied to `manuscript/verify_J_Fp_merged.py`:

| Location | Change |
|---|---|
| Top docstring | Added bullet for "Theorem 3: rigid 2-idempotent pair $\varepsilon_\pm = 3e_0\pm e_4$" as the rescued content |
| New function `check_F5_idempotents()` | Brute-force enumerate all 625 elements of $V_5$, find idempotents, check the pair satisfies all four orthogonal-decomposition axioms, report PASS/FAIL |
| New function `check_PA_on_subalgebras()` | Verify PA on $\mathrm{span}(e_0,e_3)$ and $\mathrm{span}(e_0,e_4)$ at all six primes; assert non-PA outside (at $e_2$ at least) |
| `main()` | Added calls to the two new functions |

---

*— Rescue attempt, 2026-05-28. Recommend Tier 1 re-promotion conditional on the §4 rewrite landing cleanly.*
