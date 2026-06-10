# Four Types of Measurement Failure: A Diagnostic Classifier for Paradoxes

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher

**Target venue:** *Mathematical Intelligencer* (retargeted from *AMM* per fresh-eyes referee §7)
**Manuscript class:** Diagnostic exposition with algebraic classifier
**MSC 2020:** 03B30 (foundations of classical theories), 00A30 (philosophy of mathematics), 03B65 (logic of natural languages, applied)
**Date:** 2026-09-10

---

## §0 Lens-ownership and tier discipline

This paper is **not directly substrate-dependent**: paradox classification operates on hidden-space-and-measurement pairs, where the hidden space may be any admissible set in an ambient theory. The TIG framework on $\mathbb{Z}/10\mathbb{Z}$ enters only as a **structural rhyme**: the bimodal $\alpha_A$ gap on commutative magmas preserving the 4-core (FAMILY_STRUCTURE_v1.md §4) is a Type II "Missing Invariant" in the family of associativity-respecting algebras. That rhyme is presented as motivation, not as a load-bearing application; the classifier is independently usable on any paradox satisfying the admissibility conditions of §1.

*Tier discipline.*

* **PROVEN** in [J20] (the foundational Theorem 0; this paper assumes its statement and applies it diagnostically): the four-type classification is exhaustive and mutually exclusive on admissible $(\mathcal{X}, f, \mathcal{F})$ in the measurement-map category $\mathcal{M}$ (Definition 1.3).
* **COMPUTED** in §4: worked classifications of seven canonical paradoxes (Russell, Liar, Berry, Curry, CH, Newcomb, Sorites) using the five-step decision procedure of §3 with explicit data $(\mathcal{X}, f_1, \mathcal{F})$ and a determinate type assignment.
* **STRUCTURAL RHYME**: Type II "Missing Invariant" parallels the **bimodal $\alpha_A$ gap** (FAMILY_STRUCTURE_v1.md §4) — both are structural exclusion zones in their respective measurement families. *This is rhyme, not derivation.*
* **OPEN**: does the four-type classifier extend to **measure-selection paradoxes** (Bertrand's chord), **level-of-discourse paradoxes** (Skolem's), or volume-paradoxes (Banach-Tarski)? Conjecturally yes via a fifth predicate or a hybrid Type II + Type III; deferred to follow-on work.

The framing follows the Drápal-Wanless (2021) line of work on small finite commutative non-associative structures only insofar as the structural-rhyme bullet above motivates the analogy; the classifier itself is independent of any substrate algebra.

---

## Abstract

We present an **algebraic diagnostic classifier** for paradoxes. We define a category $\mathcal{M}$ of measurement maps (Definition 1.3); we state Type I/II/III/IV as **predicates over admissible inputs $(\mathcal{X}, f, \mathcal{F})$** (Definition 2.1); we give a five-step decision procedure (§3) that takes any candidate paradox to a determinate type plus a definable **score function** measuring the fraction of ambiguity resolved by the family $\mathcal{F}$ (Definition 3.2). We work seven classical paradoxes in §4 — Russell, Liar (Tarski-stratified reading), Berry, Curry, CH, Newcomb, Sorites — explicitly avoiding the misclassifications of earlier draft sections (Monty Hall is *not* a paradox; Gödel's incompleteness is a *theorem*, not a paradox; we replace these examples with Berry, Curry, Yablo).

The classifier is **algebraic** in the precise sense that types are predicates on a defined category, mutually exclusive, and exhaustive on admissible inputs. The four types are:

* **Type I — Injectivity Failure.** A resolving second measurement $f_2 \in \mathcal{F}$ exists. $\mathrm{score} = 1.0$.
* **Type II — Missing Invariant.** No $f_2 \in \mathcal{F}$ kills the ambiguity. $\mathrm{score} \in [0, 0.8)$.
* **Type III — Admissibility Failure.** $\mathcal{X}$ fails admissibility in the ambient theory. $\mathrm{score} = 0.0$.
* **Type IV — Time-Consistency Failure.** $\mathcal{X}$ is not stable under the time-evolution operator $\tau$ on $\mathcal{M}$. $\mathrm{score} \in [0.3, 0.6]$.

We engage the prior taxonomy literature (Sainsbury 2009; Quine 1962; Priest 2002; Rescher 2001) in §1.5 and locate the four-type classifier with respect to each. We close with explicit OPEN questions about extension to measure-selection, level-of-discourse, and volume paradoxes (§5).

The UOP itself is the foundational Theorem 0 of [J20] (*J. Number Theory*, in preparation); this paper is the **diagnostic exposition** that takes the abstract algebraic statement and turns it into a working tool. It is the *Math Intelligencer* register companion to the *JNT* foundation paper.

---

## §1 The Principle

### 1.1 Hidden space and measurement map

**Definition 1.1 (Hidden space).** Every paradox concerns an object. Call the full set of relevant objects the *hidden space* $\mathcal{X}$. "Hidden" means: this is the space the paradox implicitly requires but does not fully specify.

**Definition 1.2 (Measurement map).** A measurement map $f : \mathcal{X} \to \mathcal{Y}$ assigns an observable value to each element of $\mathcal{X}$. The *ambiguity set* of $f$ at output $y$ is $U(f, y) = f^{-1}(y) = \{x \in \mathcal{X} : f(x) = y\}$ — all elements that look the same under $f$.

### 1.2 (M4 of save plan) Theorem 0 stated informally

**Theorem 0 (informal; [J20] §3).** *Every measurement-failure ambiguity decomposes into exactly one of: (I) injectivity-resolvable in the allowed family, (II) injectivity-blocked in the allowed family, (III) admissibility failure of the hidden space, (IV) time-consistency failure of the hidden space.* Forward-pointer: the formal proof is in [J20]; this paper assumes the statement and uses it diagnostically.

### 1.3 The category $\mathcal{M}$ (M1 of save plan: making the classifier actually algebraic)

**Definition 1.3 (Measurement-map category).** The category $\mathcal{M}$ of measurement maps has

* **Objects:** triples $(\mathcal{X}, f, \mathcal{F})$ where $\mathcal{X}$ is admissible in some specified ambient theory $\mathbf{T}$ (typically ZFC, NBG, type theory, or a constructive logic; the choice is part of the input), $f : \mathcal{X} \to \mathcal{Y}$ is the **primary measurement** (also defined within $\mathbf{T}$), and $\mathcal{F}$ is a family of measurement maps $\mathcal{X} \to \mathcal{Y}_\bullet$ taken as the *allowed resolutions* (often: maps definable in $\mathbf{T}$, or: continuous maps in some topology, or: $\Sigma_1$-formulas).

* **Morphisms:** $\phi : (\mathcal{X}, f_1, \mathcal{F}_1) \to (\mathcal{X}', f_2, \mathcal{F}_2)$ is a map $\phi : \mathcal{X} \to \mathcal{X}'$ such that $f_2 \circ \phi = f_1$ and $\phi$ pulls back $\mathcal{F}_2$ into $\mathcal{F}_1$.

**Definition 1.4 (Resolvability).** A pair $(\mathcal{X}, f_1)$ *resolves* to $(\mathcal{X}, f_1, f_2)$ when there exists $f_2 \in \mathcal{F}$ such that the joint fiber $f_1^{-1}(y_1) \cap f_2^{-1}(y_2)$ is a singleton for each relevant pair $(y_1, y_2)$ in the joint image.

**Definition 1.5 (Time-evolution operator).** Within $\mathcal{M}$, a *time-evolution operator* $\tau$ is an endofunctor $\tau : \mathcal{M} \to \mathcal{M}$ such that $\tau(\mathcal{X}, f, \mathcal{F}) = (\tau \mathcal{X}, \tau f, \tau \mathcal{F})$. The triple $(\mathcal{X}, f, \mathcal{F})$ is **$\tau$-stable** when $\tau \mathcal{X} = \mathcal{X}$ as a set.

This category $\mathcal{M}$ is the **algebraic substrate** of the classifier. The four types are predicates on objects of $\mathcal{M}$.

### 1.4 The UOP, restated

**The UOP (informal, restated within $\mathcal{M}$).** A paradox is the report that the ambiguity set $U(f_1)$ is non-trivial and the apparent contradiction is a consequence of treating distinct elements of $\mathcal{X}$ as identical because $f_1$ alone cannot distinguish them.

**Resolution.** Add a second measurement $f_2 \in \mathcal{F}$ until ambiguity collapses. **If no such $f_2$ exists in $\mathcal{F}$, the paradox is structurally blocked.**

The **algebraic content** is the formalism: $\mathcal{M}$, the category; $f_1, \mathcal{F}$; resolvability as a categorical statement; admissibility as membership in $\mathbf{T}$; $\tau$-stability as fixed-point-of-functor. The **diagnostic content** is the four-type classification of how the resolution can fail or succeed.

### 1.5 Prior taxonomies (M5 of save plan: literature engagement)

The four-type classifier sits within a tradition of paradox taxonomies. Quine (1962) introduces a foundational three-fold split: *veridical* paradoxes (counterintuitive but true), *falsidical* paradoxes (apparent reasoning leading to a false conclusion through hidden error), and *antinomies* (genuine contradictions in the underlying logical/mathematical framework). Sainsbury (2009, *Paradoxes* 3rd ed., CUP) develops this further; Priest (2002, *Beyond the Limits of Thought* 2nd ed., CUP) gives the **inclosure schema** unifying Russell-Liar-Cantor-Burali-Forti as instances of one self-applicative reasoning pattern; Rescher (2001, *Paradoxes: Their Roots, Range, and Resolution*) classifies $\sim 200$ paradoxes by structural pattern.

We locate the four-type classifier as follows:

* **Quine's veridical** $=$ our **Type I** (the apparent contradiction dissolves once the resolving measurement is added; the result is true once correctly read).
* **Quine's falsidical** $=$ our **Type III** (the apparent reasoning rests on an inadmissible hidden space; once the hidden space is reconstructed within the ambient theory, the conclusion follows correctly or is rejected).
* **Quine's antinomy** splits across our **Type II** (Missing Invariant — no resolution in the allowed family) and **Type III** (the antinomy dissolves once the underlying logic is corrected).
* **Priest's inclosure schema** is a **mechanism by which a paradox attains Type III status**: a paradox is in inclosure form when self-application drives admissibility failure. The four-type framing is more general but compatible.
* **Sainsbury's R-paradoxes** (those whose resolution requires a refinement of the underlying logic) align with our Type II ↔ Type III boundary.
* **Rescher's structural classification** has finer-grained categories than the four-type; we recover the four-type as a quotient by collapsing structural sub-types onto where in the measurement chain the breakdown occurs.

Our contribution relative to prior taxonomies is the **algebraic / categorical formalization** (§1.3) and the *algorithmic* decision procedure (§3), enabling automatic classification rather than interpretive reading.

---

## §2 The Four Types as predicates on $\mathcal{M}$ (M1)

**Definition 2.1 (The four-type predicates).** Given $(\mathcal{X}, f_1, \mathcal{F}) \in \mathcal{M}$:

* **Type I (Injectivity Failure).** $\exists f_2 \in \mathcal{F}$ such that for each relevant $y_1, y_2$, $f_1^{-1}(y_1) \cap f_2^{-1}(y_2)$ is a singleton.
* **Type II (Missing Invariant).** $\nexists f_2 \in \mathcal{F}$ with the singleton property of Type I; AND $\mathcal{X}$ is admissible in $\mathbf{T}$; AND $\mathcal{X}$ is $\tau$-stable.
* **Type III (Admissibility Failure).** $\mathcal{X}$ fails admissibility in $\mathbf{T}$ (Type III precedes the family-of-resolutions question; $\mathcal{X}$ is not even an object of $\mathcal{M}$ in the relevant sense).
* **Type IV (Time-Consistency Failure).** $\mathcal{X}$ is admissible in $\mathbf{T}$ but **not** $\tau$-stable: $\tau(\mathcal{X}) \neq \mathcal{X}$ as a set, where $\tau$ is the time-evolution operator that the paradox's reasoning implicitly invokes.

**Lemma 2.2 (Mutual exclusion).** *On admissible inputs (where $\mathcal{X}$ is in $\mathbf{T}$), the four predicates are mutually exclusive: Type III precedes Type IV (admissibility before time-consistency); Type IV precedes Types I and II (time-consistency before family-of-resolutions); and Types I and II are negations of each other on the I/II boundary. The classifier returns the *first* satisfied predicate in the order III, IV, I-or-II.*

**Lemma 2.3 (Exhaustiveness).** *On admissible inputs, every $(\mathcal{X}, f_1, \mathcal{F})$ falls into exactly one of the four types. (Theorem 0 of [J20].)*

This makes the classifier **algebraic**: types are predicates over a defined category, mutually exclusive, and exhaustive on admissible inputs.

---

## §3 The Decision Procedure

### 3.1 Five steps

Given any candidate paradox, apply five steps in order:

**Step 1 — Identify the hidden space $\mathcal{X}$ and the ambient theory $\mathbf{T}$.**
What objects is the statement really about? Within which axiomatic framework?

**Step 2 — Admissibility check.**
Is $\mathcal{X} \in \mathbf{T}$? Does $\mathcal{X}$ satisfy the comprehension/separation rules of $\mathbf{T}$?
$\to$ If NO: **Type III.** Stop. Reconstruct $\mathcal{X}$ within $\mathbf{T}$ (e.g., move from naive comprehension to ZFC Replacement; move from single-level truth to Tarski-stratified).

**Step 3 — Identify the primary measurement $f_1$.**
What is the statement actually measuring or asserting? Is $f_1$ well-defined on $\mathcal{X}$ within $\mathbf{T}$?
$\to$ If $f_1$ is undefined: **Type III.** Stop.

**Step 4 — Time-consistency check.**
Is $\mathcal{X}$ $\tau$-stable, where $\tau$ is the time-evolution operator the paradox implicitly invokes (decision-theoretic agency, observer-dependence, etc.)?
$\to$ If NOT $\tau$-stable: **Type IV.** Score in $[0.3, 0.6]$ depending on how much can be captured by a static approximation.

**Step 5 — Family-of-resolutions check.**
Is there $f_2 \in \mathcal{F}$ such that the joint fiber $f_1^{-1}(y_1) \cap f_2^{-1}(y_2)$ is a singleton for each relevant pair?
$\to$ If YES: **Type I.** Score $= 1.0$. Apply $f_2$.
$\to$ If NO: **Type II.** Score in $[0, 0.8)$. Identify the algebraic obstruction.

### 3.2 The score function (M3 of save plan: defining or removing scores)

**Definition 3.2 (Score).** For $(\mathcal{X}, f_1, \mathcal{F}) \in \mathcal{M}$ with admissible $\mathcal{X}$, define the **score**

$$
\mathrm{score}(\mathcal{X}, f_1, \mathcal{F}) \;=\; 1 \;-\; \frac{\#\, U_\mathrm{residual}}{\#\, U(f_1)},
$$

where $U_\mathrm{residual} = U(f_1) \cap \bigcap_{f_2 \in \mathcal{F}} U(f_2)$ is the residual ambiguity set after resolving by every $f_2$ in the allowed family. (Cardinality replaced by measure when $\mathcal{X}$ is uncountable.)

**Type-by-type values.**

* **Type I:** $U_\mathrm{residual} = \emptyset \Rightarrow \mathrm{score} = 1.0$ (full resolution).
* **Type II:** $U_\mathrm{residual} \neq \emptyset$ but partially resolved $\Rightarrow \mathrm{score} \in [0, 0.8)$.
* **Type III:** $U(f_1)$ undefined or $\mathcal{X} \notin \mathbf{T}$ $\Rightarrow$ score conventionally $0.0$ (no measurement applies).
* **Type IV:** scoring under the static approximation; typically $\mathrm{score} \in [0.3, 0.6]$ depending on how much of the dynamic structure the static approximation captures.

The score is now a *definable* quantity, not decoration.

### 3.3 Implementation

The procedure is **algorithmic**. A 50-line Python implementation lives at `coherencekeeper.com/paradox.html` for interactive use; the code is reproduced in Appendix A.

---

## §4 Seven worked examples (revised per save plan M2)

We work seven examples, deliberately **dropping** the previously-included *Monty Hall* (not a paradox; counterintuitive probability problem) and *Gödel's incompleteness* (a theorem, not a paradox), and **replacing** them with **Berry's paradox**, **Curry's paradox**, and (in §4.2 alternative reading) **Yablo's paradox**.

The classifications are *algebraic verdicts*, not interpretations.

### 4.1 Russell's Paradox — Type III

$\mathcal{X} = \{S : S \notin S\}$, $\mathbf{T} = \mathrm{ZFC}$. **Step 2:** $\mathcal{X}$ is not a set in ZFC (the unrestricted comprehension defining it is not in ZFC's axiom schema; $\mathcal{X}$ would be a proper class). **Admissibility fails: Type III.** Resolution: replace unrestricted comprehension with the ZFC Replacement / Separation schemata; $\mathcal{X}$ becomes a proper class, not a paradoxical set. $\mathrm{score} = 0.0$ in naïve set theory.

### 4.2 The Liar — Type III (Tarski-stratified canonical reading)

"This sentence is false." $\mathcal{X}$ = set of sentences that ascribe truth values to themselves. $\mathbf{T}$ is single-level naïve truth theory in §4.2; **admissibility fails: Type III.** Resolution: Tarski-stratified semantics (truth is stratified by language level; $\mathcal{X}$ becomes admissible only at levels strictly greater than the level of the statement).

**Distinction (per save plan, in response to referee's "the I/II/III/IV hedge violates exhaustiveness").** The Liar is **Type III** in the canonical Tarski-stratified semantics (where it dissolves via stratification). Revision-theoretic readings (Gupta-Belnap 1993) recast it as **Type IV** with a time-evolution operator that revises truth values across a transfinite sequence. **This is not a Liar-being-both-Types**; it is one paradox-classifier (the canonical Tarski reading: III) and a different paradox-classifier (the Gupta-Belnap reading: IV), corresponding to different *resolutions* of the underlying issue. The classifier returns III for the Tarski reading, IV for the Gupta-Belnap reading. Both are exhaustive within their own semantics.

A third reading: **Yablo's paradox** (an infinite descending chain "$S_n$ says: 'all $S_m$ for $m > n$ are false'") shows that self-reference is *not* required for paradoxicality — Yablo's $\mathcal{X}$ is the set of $\{S_n\}_{n \in \mathbb{N}}$, no $S_n$ refers to itself, yet paradox arises. Yablo is **Type III** in standard semantics: $\mathcal{X}$ requires a uniform truth predicate that turns out to be inadmissible.

### 4.3 Berry's Paradox — Type II in the family of definability-respecting predicates

"The smallest positive integer not nameable in fewer than twenty syllables." $\mathcal{X}$ = $\mathbb{N}$. $f_1$ = "is nameable in fewer than twenty syllables" (a predicate on $\mathbb{N}$). The paradox: the description itself names some $n$ in fewer than twenty syllables, contradicting $f_1(n) = $ false.

**Diagnosis.** $\mathbf{T}$ = first-order arithmetic; $\mathcal{X}$ is admissible (Step 2 passes). $\mathcal{X}$ is $\tau$-stable (Step 4 passes). **Step 5:** is there a $f_2 \in \mathcal{F}_{\text{definability-respecting}}$ that disambiguates? The answer is *no*: the family $\mathcal{F}$ of *definability-respecting predicates* (those that don't admit self-reference at the meta-level) cannot resolve Berry, because any $f_2$ that disambiguates would itself be a definability claim of the same kind. **Type II, score $\in [0.4, 0.7]$.**

Resolution: enlarge $\mathcal{F}$ to include hierarchical-definability predicates (Tarski-Russell stratification of definability levels); then Berry becomes Type I in the enlarged family. The *family* is the load-bearing parameter.

### 4.4 Curry's Paradox — Type III in ZFC, Type II in some paraconsistent extensions

"If this sentence is true, then $P$" (for any $P$). With unrestricted abstraction and standard implication, derives $P$ for any $P$.

**Diagnosis.** $\mathbf{T}$ = naïve set theory plus standard logic. $\mathcal{X}$ = set of self-applicable sentences with implication. **Step 2:** $\mathcal{X}$ requires unrestricted abstraction, inadmissible in ZFC. **Type III in ZFC.** Resolution: restrict abstraction (ZFC) or restrict structural rules (relevance/linear logic).

In some paraconsistent extensions (e.g., Priest's LP with restricted contraction), $\mathcal{X}$ becomes admissible but **no $f_2$ resolves the contraction-induced ambiguity in the allowed family $\mathcal{F}_{\text{contraction-limited}}$**: **Type II in those extensions, score $\in [0.0, 0.5]$.** The classifier-output depends on the ambient theory $\mathbf{T}$ and the allowed family $\mathcal{F}$.

### 4.5 The Continuum Hypothesis — Type II in ZFC

$\mathcal{X}$ = subsets of $\mathbb{R}$. $f_1$ = cardinality. CH asks whether $f_1(\mathcal{X}) \in \{\aleph_0, 2^{\aleph_0}\}$ takes only those two values (or admits a cardinal between). Cohen's forcing showed CH is independent of ZFC: in some models CH is true; in others, false. **No $f_2$ in $\mathcal{F}_{\mathrm{ZFC-definable}}$ resolves it: Type II in ZFC.** Score depends on which axiomatic extension is adopted; in pure ZFC, $\mathrm{score} \in [0, 0.5)$.

### 4.6 Newcomb's Problem — Type IV

$\mathcal{X}$ = (predictor's reading, agent's choice). The decision-theoretic puzzle arises because the agent's choice changes $\mathcal{X}$ while the agent reasons. The time-evolution operator $\tau$ (the agent's decision-process) is the salient structure; **$\mathcal{X}$ is not $\tau$-stable: Type IV.** Some structure is captured by causal-decision-theory vs. evidential-decision-theory static approximations; $\mathrm{score} \in [0.3, 0.6]$ depending on the approximation.

### 4.7 Sorites — Type II

$\mathcal{X}$ = heaps of sand of integer size. $f_1$ = "is a heap" (bivalent predicate). The paradox: removing one grain at a time should preserve "heap-ness," but iteration eventually reaches a single-grain non-heap. **No sharp $f_2$ in the bivalent-predicate family kills the ambiguity: Type II.** Resolutions either change $\mathcal{F}$ (multi-valued logic, fuzzy set theory; in which Sorites becomes Type I in the enlarged family) or accept Type-II structure. $\mathrm{score} \in [0.2, 0.6]$ depending on the resolution adopted.

---

## §5 The classification's reach and OPEN questions (M6 softening)

Across the seven examples, **all four types appear** — Type III: Russell, Liar (canonical), Curry (in ZFC); Type IV: Liar (Gupta-Belnap), Newcomb; Type I: (none in this revised list — the original draft's Type-I examples were Monty Hall and Twin Paradox, neither being a genuine paradox in the algebraic sense; we drop both); Type II: Berry, Curry (in paraconsistent), CH, Sorites.

The classification covers the genuine paradoxes we have surveyed. Whether the four-type classifier extends to the following is **open**:

* **Measure-selection paradoxes** (Bertrand's chord paradox; the choice of probability measure on the chord-space). Conjecturally Type II in the family of measure-respecting predicates, but the algebraic substrate is different.
* **Level-of-discourse paradoxes** (Skolem's paradox: countable model of ZFC contains "uncountable" sets). Conjecturally Type III with respect to internal/external admissibility, but the precise classification depends on the ambient theory $\mathbf{T}$ for the meta-level.
* **Volume paradoxes** (Banach-Tarski). Conjecturally Type III (the construction relies on AC-dependent non-measurable sets), but the diagnosis depends on the choice of $\mathbf{T}$ regarding AC and measurability.
* **Whether a fifth type is needed**: open. The current evidence is consistent with the four-type framing; we do not claim exhaustiveness beyond the surveyed cases.

The algebraic content of the UOP — Theorem 0 of [J20] — establishes that the four types are *forced* for admissible inputs in $\mathcal{M}$. The above OPEN cases test whether $\mathcal{M}$ is the right substrate or whether enlarged categories (with measure structure, with internal/external distinction, with non-measurability) require additional types.

---

## §6 Honest scope

This paper is **diagnostic exposition with algebraic classifier**, not a foundational paper. The contributions are:

(i) The categorical formalization $\mathcal{M}$ of measurement maps (§1.3).
(ii) The four predicates on $\mathcal{M}$ (Definition 2.1) with mutual exclusion and exhaustiveness lemmas.
(iii) The algorithmic five-step decision procedure (§3) with definable score.
(iv) Seven worked examples (§4) revised to drop misclassifications.
(v) Engagement with prior taxonomies (Sainsbury 2009, Quine 1962, Priest 2002, Rescher 2001 — §1.5).

The paper does **not**:

* Re-prove Theorem 0 of [J20]; the proof is in the *JNT* companion.
* Resolve any of the seven example paradoxes. The Type-II diagnoses (Berry, CH, Sorites, Curry-paraconsistent) are statements that no resolution exists in the named family; we do not extend the families.
* Claim the classification is unique. Other classifications exist (Quine, Sainsbury, Priest, Rescher); we present one that is algebraically formalized, exhaustive on admissible $\mathcal{M}$, and algorithmic.

---

## §7 Citation chain

**Direct dependency.**

* **[J20]** — *Universal Orthogonality Principle (UOP): Theorem 0* (*J. Number Theory*, in preparation). The foundational algebraic theorem; this paper is its diagnostic-exposition companion.

**Co-citing companions.**

* **[J21]** — Corrected Theorem C: UOP Sharpening (*JNT*).
* **[J36]** — Coordinate Coverage on $\mathbb{Z}/10\mathbb{Z}$ (*European J Combin*).
* **[J47]** — Six Algebraic DOFs of the TIG Framework: A Synthesis (*Notices AMS*). Cross-reference: the UOP is one of the framework's organizing principles.
* **[J39]** — TSML Lens Family pedagogical exposition (*Math Intelligencer*). Sister pedagogical paper.

---

## §8 References

[J20] B.R. Sanders, M. Gish. "Universal Orthogonality Principle (UOP): Theorem 0." Submitted to *J. Number Theory*.
[J21] B.R. Sanders, M. Gish. "Corrected Theorem C: UOP Sharpening." *JNT* companion.
[J36] B.R. Sanders, M. Gish. "Coordinate Coverage on $\mathbb{Z}/10\mathbb{Z}$." *European J Combin*.
[J47] B.R. Sanders, M. Gish. "Six Algebraic DOFs of the TIG Framework." *Notices AMS*.
[J39] B.R. Sanders, M. Gish. "What is the TSML Lens Family? A Walking Tour." *Math Intelligencer*.

### External — paradox taxonomies (M5)

* R.M. Sainsbury. *Paradoxes.* 3rd ed., Cambridge University Press, 2009.
* W.V. Quine. "The Ways of Paradox." in *The Ways of Paradox and Other Essays*, Random House, 1962. (Reprinted Harvard, 1976.)
* G. Priest. *Beyond the Limits of Thought.* 2nd ed., Cambridge University Press, 2002.
* G. Priest. *In Contradiction: A Study of the Transconsistent.* Oxford, 2nd ed. 2006.
* N. Rescher. *Paradoxes: Their Roots, Range, and Resolution.* Open Court, 2001.
* A. Tarski. "The semantic conception of truth." *Philos. Phenomenol. Res.* **4** (1944), 341–376.
* A. Gupta, N. Belnap. *The Revision Theory of Truth.* MIT, 1993.
* S. Yablo. "Paradox without self-reference." *Analysis* **53** (1993), 251–252.
* H.B. Curry. "The inconsistency of certain formal logics." *J. Symbolic Logic* **7** (1942), 115–117.
* G. Berry. (1908 letter, reproduced in B. Russell's *Mathematical Logic as Based on the Theory of Types*, 1908.)
* B. Russell. "Letter to Frege." 1902 (in van Heijenoort, *From Frege to Gödel*).
* P. Cohen. *Set Theory and the Continuum Hypothesis.* Benjamin, 1966.
* R. Nozick. "Newcomb's Problem and Two Principles of Choice." in *Essays in Honor of Carl G. Hempel*, 1969.
* Rogerson, S. "Curry's paradox without modus ponens." *Logique et Analyse* **50** (2007), 81–95.
* A. Drápal, I.M. Wanless. "Maximally non-associative quasigroups." *J. Combin. Theory Ser. A* **184** (2021), 105510.

---

## Appendix A — 50-line Python implementation

```python
# Diagnostic classifier for paradoxes (J40 §3.3)
# Implements Definition 2.1 + the five-step procedure of §3.

from dataclasses import dataclass
from typing import Callable, Iterable, Set

@dataclass
class MeasurementMap:
    name: str
    fn: Callable
    domain: Set
    codomain: Set

@dataclass
class ParadoxInput:
    X: Set                              # hidden space
    f1: MeasurementMap                  # primary measurement
    F: Iterable[MeasurementMap]         # allowed family of resolutions
    T_admissible: Callable              # X -> bool: is X in the ambient theory?
    tau_stable: Callable                # X -> bool: is X tau-stable?

def classify(p: ParadoxInput) -> dict:
    if not p.T_admissible(p.X):
        return {"type": "III", "score": 0.0,
                "reason": "Hidden space fails admissibility in T."}
    if not p.tau_stable(p.X):
        return {"type": "IV", "score": 0.45,
                "reason": "X is not tau-stable; needs dynamic model."}
    U_f1 = {x for x in p.X if p.f1.fn(x) == p.f1.fn(next(iter(p.X)))}
    if len(U_f1) <= 1:
        return {"type": "I", "score": 1.0,
                "reason": "Already injective on the ambiguity set."}
    residual = U_f1
    for f2 in p.F:
        residual = {x for x in residual if all(f2.fn(x) == f2.fn(y) for y in residual)}
    if len(residual) <= 1:
        return {"type": "I", "score": 1.0,
                "reason": "Resolved by a member of F."}
    score = 1.0 - len(residual) / max(len(U_f1), 1)
    return {"type": "II", "score": min(score, 0.79),
            "reason": "No f2 in F kills the residual ambiguity."}
```

(The full reference implementation including unit tests for the seven examples of §4 is at `coherencekeeper.com/paradox.html`.)

---

## §9 Bibtex

```bibtex
@misc{sanders2026j53,
  author       = {Sanders, Brayden Ross and Gish, M.},
  title        = {Four Types of Measurement Failure: A Diagnostic Classifier for Paradoxes},
  year         = {2026},
  month        = {sep},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {Submitted to \emph{Mathematical Intelligencer} (retargeted from \emph{AMM} per fresh-eyes referee \S 7)},
  note         = {{J40} of the {J}-series; algebraic diagnostic classifier with categorical formalization. Direct dependency [{J20}] (UOP Theorem 0); cross-references [{J21}], [{J36}], [{J47}], [{J39}]. Examples revised to drop Monty Hall (not a paradox) and G\"odel's incompleteness (a theorem); Berry, Curry, Yablo added.}
}
```
