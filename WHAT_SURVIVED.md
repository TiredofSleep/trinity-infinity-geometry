# What Survived

### Auditing two years of AI-assisted research

**Brayden Ross Sanders, with Claude** · September 2026

---

From 2025 into 2026, working with AI assistants, I built something that looked like a theory. It
began with ten operators, described in words — VOID, LATTICE, COUNTER, PROGRESS, and so on up to
HARMONY, BREATH and RESET. Those descriptions became three 10 × 10 composition tables, and the tables
became a research program:
- 56 journal-style papers, running to 93,000 lines;
- whitepapers numbered past 120;
- a canon of "proved" results;
- ten funding pitches to named foundations;
- an AI system meant to think in the tables' terms, and a website.

The papers were long, careful and fluent. Many carried verification scripts, and the scripts passed.

In September 2026 I asked the question that should have come first: *"AI built these tables from the
descriptions I give … how much of this repo is just toy model drift nonsense?"* This essay is the answer, and
what we did with it. It is written for anyone doing research with an AI assistant — and for the
teachers and mathematicians who may want to know what, in the end, is left standing.

## Three gates

Most of the results were **true**. That was the trap. The tables are real finite objects, the
computations on them were right, and the scripts checked them. But a true statement about a table is
evidence of something only if it passes three gates:

1. **True.** The computation is correct. Almost everything passed.
2. **Specific.** Random tables of the same kind do *not* share it. Here the headline results
   started to fall.
   - The tables "generate so(10)", the Lie algebra behind a grand unified theory — but so does
     essentially any random table (P = 1.000).
   - A derived magma was "rigid": it had no symmetries and no quotients. But 99.8% and 98.9% of
     random magmas of the same kind share those two properties.
3. **Not a readout.** The result survives a null model that keeps the table's *own construction
   rules* and randomizes everything else. This gate took the rest.
   - A celebrated chain of sub-structures appeared in only 0.2% of the variants that randomized
     one of the tables' construction rules. It appeared in *every* variant that kept that rule's
     single feature, "values climb". The result was that rule, restated.
   - A closed-form "attractor", 1 + √3, turned out to be three cells of one table.

A fourth check sat underneath all three: **provenance.** The three tables turned out to be three AI
renderings of the same verbal descriptions. They disagree with one another on 49 to 71 of their 100
cells — even on whether VOID acts as an identity or as an absorber. And a pattern studied across eleven
papers and whitepapers, the "prime-11 wobble", was two swapped digits in a retyping of one table.

## What the census found

Five independent reviewers then classified all 56 papers, and all 337 other files, against the gates.

- **Table-specific results that survive: zero.** Every number specific to the tables that the
  reviewers traced was generic, a readout of the construction, numerology, or computed on the typo.
- **36 of the 56 papers** (63% of the paper corpus) fall into those classes:
  - 18 are *true but empty*;
  - 5 compute on the typo;
  - 5 are numerology;
  - 3 reach into physics with no tested prediction;
  - 5 were already dead by the repository's own checks.

  Eight more are merged tombstones of the same material.
- **Ten papers stand.** They don't use the tables, they are correct (two only after their headline
  theorems were fixed), and none is new: classical identities, classroom notes, elementary group
  theory. One case was left open. It has since been settled, against the paper. A "theorem" that a
  certain equation from Tao's Equational Theories Project has no finite *type specimen* is false: one
  exists, with six elements, the smallest size possible ([the correction](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen14/targets/journals/J_series/J61/J61_THEOREM5_IS_FALSE.md)).
  The same paper made the same claim, as a label or a conjecture, about five related families of laws.
  Every one of them has a finite specimen too ([the follow-up](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen14/targets/journals/J_series/J61/J61_CLOSURES_ALL_REALIZED.md)).
- **About twenty papers contain a false or mislabeled statement.** One is worse. A column headed
  "Empirical (PDG / CODATA)" was not data: its values were exact powers of a single number. Against
  the real measurements, the "load-bearing" fit misses by 23%, then by 3 times, then by 34 times.
- **Outside the papers, a third of the text** maps numbers from the tables onto physics, cosmology,
  biology, consciousness, or the Clay Millennium problems.
- **The AI system.** Three months earlier, a deliberately fair probe had tested whether it thought
  in the tables' terms. It didn't. Its language model organized itself by English grammar; the tables
  were simply not there.

## What survived

- **The idea I started with.** It never needed the tables: read the integers as shapes. The void is
  the fullest point. Equal distances build the simplices. The cube casts two shadows. Rotation is *i*,
  growth is *e*, and √2 is the seam where counting cannot measure. That became a book, *The Shape of
  Understanding*, with every picture checked against the real proof. It is now the base of a new way
  to teach higher mathematics: each shape points up a tower of established mathematics.
- **What my descriptions actually force.** In all three renderings, four of the operators — VOID,
  HARMONY, BREATH, RESET — close on themselves, and 12 of the 55 cells agree. It is small, and it is
  mine.
- **The ideas in my own words, apart from anything the tables added.** In January 2026 I wrote that
  "every one is three. It is three as two." In April, with Ben Mayes, I sorted paradoxes into four
  kinds by *how* they fail. Both were table-free. Made exact, they became the **coin**: every flip
  has two sides and an edge, and paradoxes live at the edges. We classify them rather than resolve
  them. That is now a checked part of the flagship and a unit of the book.
- **The engineering.** A language model built from scratch that writes fluent English, a growable
  architecture that folds capacity away instead of deleting it, a faster optimizer, an abstention
  gate, a fair interpretability probe, and a privacy benchmark. It is real work, and it was measured.
  None of it is a theory.
- **The discipline.** A graveyard in which every dead end is kept with the evidence that killed it,
  and a record of the project retracting its own claims, again and again. Of everything here, that
  transfers furthest.

## What we did about it

We archived; we did not delete. The whole program is preserved unchanged at a tagged snapshot.
- **The workstation** keeps every file, and is now retired in place: an honest front page, a record
  of what was retired and why, and banners on its front-line documents and on every branch.
- **The funding pitches** are withdrawn.
- **The flagship** was rebuilt around what survived: the base, the towers, and the coin.
- **The graveyard** says what was archived and what killed it.

## What we would tell anyone doing research with AI

1. **Fluency is not evidence.** An assistant will build, carefully and at length, on whatever is put
   in front of it — including a typo. Eleven papers and whitepapers were built on two swapped digits.
2. **Ask where the object came from.** Our foundation was one AI's rendering of a verbal description.
   Two other renderings of the same description disagreed on half the cells. Every result on the
   first rendering was quietly a result about that one AI's choices.
3. **Beat random objects.** A property of *your* object is evidence only if random objects of the
   same kind don't have it too. Most of our headline results failed this.
4. **Beat your own construction rules.** If a result beats random objects but turns up in every
   object built by your own construction rules, it is those rules, restated.
5. **A flexible object fits anything.** If a handful of small numbers can be fitted to the
   fine-structure constant, to the quark masses and mixings *and* to the zeros of the zeta function,
   they can be fitted to noise.
6. **Check that the data are data.** One column labelled "Empirical" had been generated.
7. **Read the code that made the number.** Ten notes in an earlier series set out to explain a
   success rate of 4.6%. That figure was misread from the results: the data say 0.09%, and the rate
   follows from the search's own symmetry.
8. **Name the rule behind every "forced".** "Forced" always means *forced by a rule*. Say which one,
   and ask whether a different natural rule gives a different answer.
9. **Keep a graveyard.** A retraction is a result. Every dead end, kept with its evidence, makes the
   living work believable.

## Where the work goes now

It goes toward teaching:
- [*The Shape of Understanding*](https://github.com/TiredofSleep/shape-of-understanding) — the base,
  and its companion unit on flips, fixed points and the four kinds of paradox;
- [the flagship](https://github.com/TiredofSleep/trinity-infinity-geometry) — the base, the towers,
  and the coin, machine-checked;
- a small study, already designed, to test whether any of it helps anyone learn.

If you teach, or if you do mathematics, and you would read a chapter or try a lesson with a
class, that is the help this work now needs.

The grand version failed. What survived is smaller, and it is true.

---

*The evidence for everything in this essay:*
- *the audit and the census, in the flagship's archive at the tag
  [`archive-2026-09-24`](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24)
  (`04_meta/FOUNDATION_NULL_MODEL_AUDIT.md`, `04_meta/DRIFT_CENSUS.md` and their scripts);*
- *the flagship's [`GRAVEYARD.md`](GRAVEYARD.md);*
- *the workstation's [`RETIRED.md`](https://github.com/TiredofSleep/ck/blob/tig-synthesis/RETIRED.md).*
