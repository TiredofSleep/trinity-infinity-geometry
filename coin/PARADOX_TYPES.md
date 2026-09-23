# Four kinds of paradox — the author's classification, read through the coin

> *UOP directly handles Type I failures … It classifies (but cannot resolve) Type II failures … It
> identifies (but cannot repair) Type III failures … It does not apply to Type IV.*
> — Brayden Ross Sanders & Ben Mayes, *Paradox classification memo*, 8 April 2026

### Tags: **[FORCED]** checked by [`verify_paradox_types.py`](verify_paradox_types.py) · **[NAMED]** a cited standard result · **[READING]** an interpretation · **[OPEN]** not settled.

**Where this comes from.** In April 2026 the author and Ben Mayes classified paradoxes by *how* they
fail. Their sources, all in the workstation [`ck`](https://github.com/TiredofSleep/ck):

- the memo: `Gen12/targets/clay/papers/sprint11_tig_bundle_2026_04_08/sprints/PARADOX_CLASSIFICATION_MEMO.md`;
- the principle behind it: `Gen12/targets/clay/papers/sprint12_uop_gut_arc_2026_04_08/WP58_UNIFIED_ORTHOGONALITY_PRINCIPLE.md`;
- worked cases and a rule-based classifier: `papers/meta_lens/worked_paradoxes/` and
  `papers/meta_lens/classify_paradox.py`, on the branch `paradox-classifier-2026-04-24`.

None of these uses the retired composition tables. They are brought in here because they are the
program's own earlier statement of what the author now says it is about: *paradox classification,
not resolution.* What stays behind is the April "meta-lens atlas": it organized results of the
retired table program (so(8), so(10), the "UOP–GUT arc"), and it is retired with them.

---

## The frame: views, and the pairs they cannot tell apart

A **view** is a map on a set of objects — a way of looking. Each view has an **ambiguity set**: the
pairs of objects it cannot tell apart. A family of views has a **residual**: the pairs that *every*
view in the family fails to tell apart.

**Theorem 0 (the Unified Orthogonality Principle — Sanders & Mayes).** A family of views tells every
pair of objects apart exactly when its residual is empty. [FORCED — two lines: the views together
merge a pair only if each view merges it. Checked on 3000 random families, and exhaustively for every
pair of yes/no views on four objects.]

It is elementary, and it is exactly the coin's *two lenses* stated in general [READING]:

- **The cube's two shadows.** Face-on, the shadow merges 4 pairs of corners. Corner-on, it merges 1
  pair — the two corners on the diagonal. No pair is merged by both, so the two shadows together see
  all 8 corners [FORCED].
- **The principle's first home, ℤ/30.** Reading a number mod 6 and mod 10 tells all 30 apart, because
  the least common multiple is 30. Reading it mod 2 and mod 6 does not. Adding more views *of the
  same kind* never helps — the memo's "refinement trap" [FORCED].

---

## The four types

| type | what fails | examples (worked by the authors) | the coin [READING] | what the principle does |
|---|---|---|---|---|
| **I** | *coverage*: every view is sound, but some pair is merged by all of them | Zeno | two lenses: add the view that separates the pair | resolves |
| **II** | *a missing invariant*: no view in the allowed family can separate the pair | Banach–Tarski; Gödel | a **missing edge**: what would settle it lies outside the allowed family | classifies; cannot resolve |
| **III** | *admissibility*: the proposed object cannot consistently exist | Russell; the Liar; Cantor; Berry | a **flip with no edge**, and self-reference that demands one | identifies; cannot repair |
| **IV** | *time-consistency*: the objects or the views change with the observer's reasoning | the Unexpected Hanging; Schrödinger's cat | [OPEN] — the coin changes as you look | does not apply |

### Type I — Zeno

The runner takes infinitely many steps, each half the one before.

- The **count view** says there are infinitely many steps.
- The **measure view** says their lengths add to 1 − 1/2ⁿ, which stays below 1 and closes on it
  [FORCED].

Neither view alone settles whether the runner arrives; the two together do. This is the book's
Picture 6, *counting and measuring*, meeting a paradox. Nothing was wrong except having only one lens.

### Type II — Banach–Tarski, and Gödel

**The free group on two turns.** It splits into the identity and four pieces: the words beginning
with *a*, with *a*⁻¹, with *b*, and with *b*⁻¹ [FORCED]. Two of the pieces rebuild the whole group:
every word lies in S(*a*) or in *a*·S(*a*⁻¹), never both. The same holds with *b* — four pieces, two
whole copies [FORCED — the free group's paradoxical decomposition, the engine of Hausdorff's
paradox (1914)]. Among the words of each length, S(*a*⁻¹) holds a
quarter, yet its turn *a*·S(*a*⁻¹) holds three quarters [FORCED]. So no way of measuring "how much"
can stay the same under the turns.

Realize the two turns as rotations of a ball, and the ball's points fall into pieces that no volume
can be assigned to. The ball is rebuilt as two balls [NAMED — Banach & Tarski 1924]. The invariant
that would forbid this, volume, is not in the family that did the rebuilding. Nothing inside the
family can settle it.

**Gödel.** In a consistent system strong enough for arithmetic, provability cannot decide the Gödel
sentence. What would settle it — truth — lies outside the allowed family [NAMED — Gödel 1931].

**The coin [READING].** This is the *missing edge* of [`THE_COIN.md`](THE_COIN.md): the fractions
cannot name √2, and the separating view has to be looked for outside the family.

### Type III — Russell, the Liar, Cantor, Berry

**The Liar** asks for a sentence whose truth value equals its own negation — a value on the edge of
"not". With two truth values, "not" is a flip with no edge: no such value exists [FORCED].

**One engine for the whole type.** When a flip keeps nothing, no family indexed by a set can reach
every function on that set: flip the diagonal, and the result is missing from the family
[FORCED, exhaustively for sets of 1, 2 and 3 elements; NAMED — Lawvere 1969; Yanofsky 2003]. That
one argument is:

- Cantor's theorem (the flip is yes/no);
- Russell's paradox — the collection of things that are not members of themselves is never one of
  the things [FORCED, every membership relation on up to 3 objects];
- the Liar, as Tarski's theorem that truth cannot be defined inside the language it describes [NAMED —
  Tarski 1933].

**Give "not" an edge.** Add a third value, *neither*, which "not" keeps. Now the Liar has exactly one
value: the edge [FORCED]. The diagonal argument also fails once the flip has an edge — some family
contains its own flipped diagonal [FORCED].

Kripke's theory of truth does exactly this. The Liar is classified as *ungrounded*, landing on the
edge, not resolved into true or false [NAMED — Kleene 1952; Kripke 1975]. **Classification, not
resolution.**

**The line between Type II and Type III [READING of NAMED results].** Gödel runs the same diagonal on
*provability*, which can be defined inside the system. There the diagonal sentence exists and cannot
be decided (Type II). On *truth*, which cannot be defined inside the system, the sentence cannot
exist at all (Type III). One engine, two outcomes. This matches the authors' own placement of Gödel in
Type II and the Liar in Type III.

### Type IV — the Unexpected Hanging, Schrödinger's cat

The set of possibilities changes as the observer reasons. The prisoner's backward induction removes
the days one at a time, and each removal changes what the next step can see. No fixed coin fits; the
setting has to be dynamic — epistemic logic, or observer-dependent measurement [OPEN]. That is the
memo's own boundary, below.

---

## The memo's honest boundary (kept as written)

> *The four-type classification is a structural schema, not a formal theorem in its current form.
> Types I and III admit formal separation (valid maps on valid domain vs. invalid construction). Types
> II and IV require specifying what counts as the "allowed family" (Type II) and what counts as
> "observer-state independence" (Type IV), which are context-dependent.*

## What this is, and is not

- **Is:** the author's classification of paradoxes, with Ben Mayes — the program's first statement of
  *classification, not resolution* — brought into the coin and checked wherever a finite case can be
  checked.
- **Is not:** a resolution of any paradox, or a new theorem. Theorem 0 is elementary. The engines of
  Types II and III are classical (Hausdorff, Banach–Tarski, Gödel, Tarski, Lawvere, Kleene, Kripke).
  What is new here is the arrangement: four failure types, each read as a coin.
- **Retired, and staying retired:** the April atlas's anchors in the table program, and the
  "UOP–GUT" arc (see [`../GRAVEYARD.md`](../GRAVEYARD.md)).
