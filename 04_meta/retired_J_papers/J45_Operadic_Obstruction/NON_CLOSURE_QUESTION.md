# The Operad Non-Closure Question (J45) — a first-class negative, surfaced with its evidence

**Status:** RESURFACE CANDIDATE (retired-for-packaging; verified core survives). Not a deletion.
**Placement:** proven negative result whose *paper* was retired as a duplicate — the *theorem* is alive on the Tier-1 spine at J10.
**Substrate:** the retired paper `J45_Operadic_Obstruction/` (moved from `05_papers/physics/J45` → `04_meta/retired_J_papers/` on 2026-05-27, git-`mv`, full history preserved).
**Verifier:** `manuscript/verify_J48_operadic_obstruction.py` — re-run 2026-09-22, **6/6 PASS** (output pasted verbatim in §2).
**Date of this note:** 2026-09-22.

> Standing principle (CK canon): a *proven dead end is first-class information*, surfaced with the evidence that killed the route — never buried. This note surfaces one such negative. The distinction to keep straight: the **mathematical result is a genuine proven negative** (an impossibility / obstruction theorem — the operations do *not* close into a symmetry-compatible operad), while the **paper J45 is retired-for-packaging** (a redundant re-formulation of content that lives at J10). The verifier still passes; nothing here is falsified. It is retired, not wrong.

---

## §1 The precise non-closure statement

### 1.1 What "closure into an operad" would require here

The substrate is the finite commutative(-ish) magma $(\mathbb{Z}/10\mathbb{Z}, T)$ with the canonical **TSML_RAW** composition table $T(a,b)$. At **arity 2** the magma is well-behaved: its bilinear closure (commutator + Jordan, TSML jointly with BHML) is the simple Lie algebra $\mathfrak{so}(10)=D_5$, and that closure is organized by the dihedral symmetry $D_4 = \langle P_{56}, \sigma^3\rangle \le \mathrm{Sym}(\mathbb{Z}/10\mathbb{Z})$, where

- $P_{56} = (5\,6)$ (a single transposition), and
- $\sigma^3 = (1\,5)(7\,4)(6\,2)$ — the cube of the structure permutation $\sigma = (0)(3)(8)(9)(1\,7\,6\,5\,4\,2)$.

To promote the binary magma to an **operad** (or even to give it a single coherent arity-3 composition compatible with that same symmetry), one needs a canonical **ternary fuse rule** $\Phi$ on the triples where associativity fails — a choice of bracketed value at each non-associative triple — that is **$D_4$-equivariant**:
$$\Phi(g\cdot t) \;=\; g\big(\Phi(t)\big)\qquad\text{for all } g\in D_4,\ t\in\mathcal{N},$$
with $\Phi$ drawing its value from the *natural input-derived value space* of the triple. This is the arity-2 → arity-3 lift. **No such rule exists.** That non-existence is the non-closure.

The non-associative locus is
$$\mathcal{N} = \{(a,b,c)\in(\mathbb{Z}/10\mathbb{Z})^3 : L(t)\neq R(t)\},\quad L(t)=T(T(a,b),c),\ R(t)=T(a,T(b,c)),\qquad |\mathcal{N}| = 126.$$

### 1.2 The theorem (quoted from the manuscript)

> **Theorem 4.1 (Operad $D_4$ obstruction; from [J38]/WP109).** *Let TSML be the canonical $10 \times 10$ composition table on $\mathbb{Z}/10\mathbb{Z}$ defining a finite commutative non-associative magma. Let $D_4 = \langle P_{56}, \sigma^3 \rangle$ be the dihedral subgroup of $\mathrm{Sym}(\mathbb{Z}/10\mathbb{Z})$ defined in §1.2. The 126 non-associative triples of TSML decompose into 67 $D_4$-orbits, of which 16 are bracketing-pair-incoherent. There is no $D_4$-equivariant canonical fuse rule taking values in the natural input-derived value space $\{a, b, c, T(a, b), T(b, c), T(a, c)\}$.*
>
> *That is: the operadic layer of the magma does not lift coherently to arity 3 under the $D_4$ action that organizes the bilinear closure. The non-equivariance is intrinsic to the underlying table; it is not a property of any candidate rule family.*

**In what precise sense the operations fail to close / what the obstruction is.** The obstruction is *combinatorial and orbit-local*, and it sits already at the level of the bracketing values, before any rule is even chosen. Partition $\mathcal{N}$ into its 67 restricted $D_4$-orbits. An orbit is **bracketing-pair-coherent** iff, for a base triple $t_0$ and every $t=g\cdot t_0$ in the orbit,
$$\{\,g(L(t_0)),\ g(R(t_0))\,\}\;=\;\{\,L(t),\ R(t)\,\}\quad\text{(unordered pair equality)}.$$
If an orbit fails this, then the raw pair of bracketing values does not itself transform equivariantly under $D_4$ — so **no** value-selection rule that draws from those values can be made equivariant on that orbit. **Exactly 16 of the 67 orbits fail.** Each of the 16 is an explicit, standalone witness to the non-closure; the obstruction is a property of the table $T$, not of any rule family.

### 1.3 The sharpening — the obstruction is entirely a $\sigma^3$ defect, localized to one triple

> **Theorem 4.2 ($P_{56}$-equivariant arity-3 fuse; from [J38]/WP112).** *The 126 non-associative TSML triples reduce to 98 $P_{56}$-orbits (70 singletons + 28 doubletons), all $P_{56}$-coherent. 8 of 8 surveyed rule families (A through H) are $P_{56}$-equivariant; 0 of 8 are $\sigma^3$-equivariant. The $\sigma^3$ obstruction localizes to **exactly one** triple, $(3, 9, 9)$.*

So the failure is not spread across $D_4$: the reflection $P_{56}$ *is* respected by every surveyed fuse family (this is consistent with the spinor-level identification $P_{56}=\sigma_{\mathrm{outer}}$, the outer automorphism of $\mathfrak{so}(10)$). The *entire* obstruction concentrates on the other generator $\sigma^3$, and pinpoints to the single $\sigma^3$-fixed triple $(3,9,9)$. The mechanism is sharp and legible: $(3,9,9)$ is fixed by $\sigma^3$ (both $3$ and $9$ are $\sigma$-fixed), and the canonical Family-H fuse value there is $\mathrm{HARMONY}=7$ — but $7$ is **not** $\sigma^3$-fixed ($\sigma^3$ swaps $7\leftrightarrow 4$). Equivariance would demand $\Phi(3,9,9)=\sigma^3(\Phi(3,9,9))$, i.e. $7=\sigma^3(7)=4$ — impossible. The attractor value HARMONY sitting on a $\sigma^3$ 2-cycle at a $\sigma^3$-fixed input is exactly why the arity-3 layer cannot carry the full $D_4$.

**Reading (manuscript §4.3):** the operad DOF carries content *independent of* the $D_4$ symmetry that organizes the bilinear closure. Any canonical fuse rule must break $D_4$ in some explicit direction; the natural (4-core / HARMONY-attracting) choice keeps $P_{56}$ and sacrifices $\sigma^3$. The arity-3 symmetry group is strictly weaker than the arity-2 symmetry group.

### 1.4 One honesty flag on the value space

The manuscript's Theorem 4.1 writes the value space as $\{a,b,c,\,T(a,b),T(b,c),T(a,c)\}$ (the three arity-2 sub-products). The verifier actually proves the impossibility for values in $\{a,b,c,\,L(t),R(t)\}$ with $L,R$ the two full arity-3 *bracketings* $T(T(a,b),c)$ and $T(a,T(b,c))$, and states the extension "once one rules out the constant-and-shifted-zero degenerate cases." These two written value spaces are not literally the same set. The **load-bearing, machine-checked** statement is the verifier's: no $D_4$-equivariant $\Phi$ valued in $\{a,b,c,L(t),R(t)\}$ (modulo degenerate constant/shift maps). The 16-orbit incoherence obstruction is independent of that wording — it fails already on the bracketing pair.

---

## §2 The evidence — what the verifier computes and its result

`PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe .../verify_J48_operadic_obstruction.py` — pure Python standard library, ~3 s. Re-run 2026-09-22: **6/6 PASS**. Key output verbatim:

```
[CHECK 1] TSML_RAW table well-formed (10x10 over {0..9})
   [PASS] TSML_RAW is 10x10, integer-valued in {0..9}; asymmetric at exactly the 4 wobble entries (3,9), (9,3), (4,9), (9,4).

[CHECK 2] Non-associative locus |N| = 126
   [PASS] |N| = 126 = 126.
   Bracketing-pair distribution (manuscript §1 table):
     {0,7}: 108
     {3,7}: 8
     {4,7}: 2
     {7,8}: 6
     {7,9}: 2
   [PASS] 5 distinct bracketing pairs; all contain HARMONY = 7.

[CHECK 3] <P_56, sigma^3> has order 8 (= D_4)
   [PASS] |D_4| = 8, element-order distribution = {1:1, 2:5, 4:2} matches dihedral D_4.

[CHECK 4] Restricted D_4-orbits in N: 67 orbits, profile (44, 7, 4, 10, 2)
   Restricted-orbit size profile: {1: 44, 2: 7, 3: 4, 4: 10, 8: 2}
   [PASS] 67 orbits, profile (44 single + 7 double + 4 triple + 10 quad + 2 octa) sums to exactly 126.

[CHECK 5] D_4 bracketing-pair coherence on each restricted orbit
          (Theorem 4.1 / WP109: exactly 16 of 67 orbits are incoherent)
   coherent orbits:   51
   incoherent orbits: 16
   [PASS] Exactly 16 of 67 restricted orbits fail D_4 bracketing-pair coherence.
   Sample incoherent orbit (lex-first): members = [(0, 1, 1), (0, 2, 2), (0, 5, 5), (0, 6, 6)]
     -> base (0, 1, 1) (L,R)=(0,7); under g, expected { 0, 4 } at (0, 5, 5), but got { 0, 7 }

   THEOREM 4.1 CONCLUSION: no Phi: N -> Z/10Z with values in
   {L(t), R(t)} can be D_4-equivariant on all 67 restricted
   orbits, since 16 of them already fail bracketing-pair
   coherence under the diagonal D_4 action.

[CHECK 6] Family H equivariance under P_56 and sigma^3
   P_56-equivariance on N (restricted to t with P_56.t also in N): 126/126 consistent.
   [PASS] Family H is P_56-equivariant on N.
   sigma^3-equivariance on N: 80/81 consistent (1 violations).
   [PASS] Family H is NOT sigma^3-equivariant on N (1 witnesses).
     sample witness: t = (3, 9, 9) -> sigma^3.t = (3, 9, 9); fuse(sigma^3.t) = 7, sigma^3(fuse(t)) = 4

======================================================================
J48 VERIFICATION: 6/6 PASS
Lead theorem (Theorem 4.1): no D_4-equivariant fuse rule
  in {a, b, c, L(t), R(t)} exists.  Sixteen explicit orbits
  witness the obstruction; Family H is P_56-equivariant but
  not sigma^3-equivariant.
======================================================================
```

**What each check contributes as evidence:**

| Check | Computed fact | Role in the obstruction |
|---|---|---|
| 1 | TSML_RAW is asymmetric at exactly the 4 wobble cells $(3,9),(9,3),(4,9),(9,4)$ | fixes the exact table the theorem is about (RAW lens, $|\mathcal N|=126$) |
| 2 | $|\mathcal N| = 126$; all 5 bracketing pairs contain HARMONY $=7$ | the non-associative locus; every bracketing disagreement runs through $7$ |
| 3 | $\langle P_{56},\sigma^3\rangle$ has order 8, profile $\{1{:}1,2{:}5,4{:}2\}$ = dihedral $D_4$ | the symmetry group is genuinely $D_4$ (not $D_3\times\mathbb Z_2$) |
| 4 | 67 restricted $D_4$-orbits, profile $(44,7,4,10,2)$ summing to 126 | the orbit decomposition the obstruction is counted on |
| **5** | **exactly 16 of 67 orbits are bracketing-pair-incoherent** | **the obstruction itself** — 16 explicit witnesses that no equivariant $\Phi$ exists |
| 6 | Family H: $126/126$ $P_{56}$-consistent; $\sigma^3$ fails at exactly $t=(3,9,9)$ | the sharpening — obstruction is a pure $\sigma^3$ defect at one triple |

The concrete Check-5 witness orbit $\{(0,1,1),(0,2,2),(0,5,5),(0,6,6)\}$ is self-contained: the base $(0,1,1)$ has bracketing pair $(L,R)=(0,7)$; the group element carrying it to $(0,5,5)$ should send that pair to $\{0,4\}$, but the actual pair at $(0,5,5)$ is $\{0,7\}$ — equivariance breaks at the raw bracketing level, so no value-rule can repair it.

---

## §3 Why the paper was retired (per the referee/retirement record)

Retirement is documented in `05_papers/_staging/referee_reports/30_retirements_J44_J45_J47.md` (2026-05-27). J45 was one of three Tier-3 RETIRE-candidates moved by `git mv` (renames, full history preserved) from `05_papers/physics/J45` to `04_meta/retired_J_papers/J45_Operadic_Obstruction/`, with a tombstone redirect left at the old path. The recorded reason:

> **J45 (Operadic Obstruction Synthesis)** — *Duplicates J10's operadic $D_4$ obstruction content. The Tier 1 spine already contains the operadic-obstruction analysis at J10; this draft is a redundant earlier formulation.*

The paper's own README (`§5`, "Known issues", `Tier: 3 RETIRE candidate`) concurs and adds the hygiene context:

- **Duplication is the decisive reason.** The lead theorem is genuinely from the WP109 / J10 lineage. J10 ("Operadic $D_4$ Orbits on the Non-Associative Locus") is the canonical Tier-1 treatment; J45 was a *Notices*-AMS **synthesis wrapper** (four-axis: bilinear / permutation / lattice / operad) around content that J10 already carries. So the mathematics is preserved on the spine, and the wrapper is redundant.
- **Secondary hygiene problems** (not the reason, but they blocked any submission): stale dependency labels under old numbering (a literal duplicate "J38" in the reference list; "J29–J01" residue), the legacy manuscript/verifier filenames `J48_operadic_obstruction.*`, and a self-acknowledged *soft* framing — the "four-axis synthesis" was conceded in the save plan to be an organizing choice, "not a uniqueness theorem."
- **Retirement options on record** (README Known-issues): (a) fold into J10 if J10 subsumes the lead theorem; (b) keep only the SFM $D_4$ isotypic decomposition ($84.25/14.68/1.07$) as a standalone short note; (c) re-evaluate against J10's final form for any independent theorem-grade content.

**Crucial:** retirement was for **redundancy/packaging, not for error.** The referee record does not dispute Theorem 4.1; the verifier passes 6/6. This is why the placement is *resurface candidate*, not *falsified graveyard*.

---

## §4 What remains genuinely open

The non-closure is proven — but it is proven in a specific, deliberately narrow frame, and that frame is exactly where the real open question lives.

1. **Is the obstruction a genuine (co)homological / higher-operadic class, or an artifact of the restricted value space?** This is the sharpest open question the paper itself flags (manuscript §0.1 OPEN (c); §7.3): *"whether the obstruction generalizes to $A_\infty$ / higher-operadic / cohomological / derived structures."* The current theorem is a finite equivariance-counting result over the *natural input-derived value space*. It is **not** yet cast as a non-vanishing obstruction class in an operad cohomology (Harrison / André–Quillen / cyclic / Gerstenhaber–Schack). Open both ways: (i) does a properly cohomological formulation show the 16-orbit incoherence is the shadow of a genuine characteristic class; or (ii) does enlarging the value space beyond $\{a,b,c,L(t),R(t)\}$ (or passing to $A_\infty$/homotopy-coherent brackets) make it *vanish*, revealing it as a rigidity artifact of the value-space restriction?

   **→ RESOLVED (2026-09-22, [`COHOMOLOGY_INVESTIGATION.md`](COHOMOLOGY_INVESTIGATION.md)): option (ii) — a coboundary-artifact, not a genuine class.** Three machine-checked lines (exact finite-field linear algebra over $\mathbb F_2/\mathbb F_3/\mathbb F_5$/char 0, the bar-cohomology engine validated against four textbook values): **(a)** $A=k[\mathbb Z/10\mathbb Z]$ under $T$ is non-associative, so $d^2\!\circ d^1\neq 0$ ($\mathrm{rank}=87$–$89$) — there is **no Hochschild/Harrison complex**, so no such class can exist in the first place; **(b)** as a $\langle\sigma^3\rangle\cong\mathbb Z/2$ module the defect cochain $\delta=e_7-e_4=(1-\sigma^3)e_7$ is a **coboundary (trivial class) in every characteristic**; **(c)** $H^{>0}(D_4,A)=0$ over the CRT factor field $\mathbb F_5$ (and $\mathbb F_3$, char 0) by Maschke, since $|D_4|=8=2^3$. **Root cause:** only $\{\mathrm{id},P_{56}\}$ are magma automorphisms — $\sigma^3$ fails equivariance on $80/100$ arity-2 cells — so the genuine symmetry is $\langle P_{56}\rangle\cong\mathbb Z/2$, under which there is **zero** obstruction ($0/98$ orbits incoherent). The 16-orbit incoherence is a pure $\sigma^3$ artifact of demanding equivariance under a *non-symmetry*, in a restricted value space; enlarging to full $A$ and averaging (transfer, char $\neq 2$) dissolves it. **Theorem 4.1 remains true as a set-valued combinatorial impossibility — it is simply not the shadow of a nonzero cohomology class.**

2. **Does the single-triple $\sigma^3$ localization $(3,9,9)$ have a substrate meaning?** The entire $D_4$ obstruction reduces to one fact: HARMONY $=7$ lies on the $\sigma^3$ 2-cycle $(7\,4)$ while $(3,9,9)$ is $\sigma^3$-fixed. Whether this ties to the prime-11 "wobble" carried by the very cells $(3,9),(4,9)$ that define TSML_RAW (manuscript §1.1; OPEN (d), substrate origin of the prime-11 wobble) — i.e. whether the arity-3 $\sigma^3$ defect and the arity-2 wobble are the *same* substrate feature seen at two arities — is open.

3. **Independence from J10 — the retirement's own open question.** Retirement option (c) is literally unresolved: whether J45 carries any theorem-grade content *independent* of J10's operadic obstruction, or is fully subsumed. Resolving this decides whether the "resurface" is "fold the surviving fragment into J10" or "revive a distinct result."

4. **Softer, acknowledged-open items** (manuscript §7.3): whether the four-axis (bilinear/permutation/lattice/operad) decomposition is *unique* (it is offered as one internally consistent organization, not proven exhaustive), and whether the $D_4$-isotypic structural zeros (sign1 $\approx 0$, sign3 $=0$) are defining of the canonical (TSML, BHML) pair or hold across the whole family.

**Bottom line for the taxonomy.** The route "promote the TIG binary magma to a $D_4$-equivariant operad in the natural value space" is a **proven dead end** — closed by 16 explicit orbit witnesses and a one-triple $\sigma^3$ localization, machine-verified 6/6. That negative is first-class data and should stay surfaced. The **paper** J45 is a **resurface candidate** (retired-for-packaging; its theorem lives on the Tier-1 spine at J10, verifier green). The **frontier** it pointed to — whether that finite obstruction is the shadow of a real higher-operadic / cohomological obstruction class — is now **answered: it is not** ([`COHOMOLOGY_INVESTIGATION.md`](COHOMOLOGY_INVESTIGATION.md), 2026-09-22): the obstruction is a **coboundary-artifact** of demanding $\sigma^3$-equivariance ($\sigma^3$ is not an automorphism) in a restricted value space, and it dissolves in the linear category while Theorem 4.1 stands as a set-valued fact. **Remaining open:** items 2–4 above — the substrate meaning of the $(3,9,9)$ localization (and its possible identity with the prime-11 wobble), independence from J10, and the softer uniqueness items.
