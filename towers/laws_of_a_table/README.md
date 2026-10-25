# The laws of a table

**A side floor of the number tower** (ℝ → ℂ → ℍ → 𝕆, [`../THE_TOWERS.md`](../THE_TOWERS.md) §2). Each floor of
that tower gives up a law: ℍ gives up commutativity, and 𝕆 gives up associativity. This floor counts laws
exactly.

Its ruler is the catalog of the Equational Theories Project (ETP), the collaborative project led by Terence
Tao: every law with at most four operations, from x = x to laws such as associativity,
x·(y·z) = (x·y)·z, up to renaming the variables and swapping the two sides. There are 4,694 of them. The **profile** of a table (a
magma: a set with one binary operation, given by its multiplication table) is the set of catalog laws it
obeys.

| page | what it finds | status |
|---|---|---|
| [`THE_LAWS_OF_ZN.md`](THE_LAWS_OF_ZN.md) | x + y mod n obeys 32 laws for every n ≥ 5, and −(x + y) mod n obeys 294 for every n ≥ 7, with one exception at 6. Four operations can tell apart only the moduli 1 to 4 | known; teaching. Corrects the archived J05 |
| [`STEINER_SYSTEMS.md`](STEINER_SYSTEMS.md) | Every Steiner triple system with at least 3 points obeys the same 382 laws, the Fano plane among them, and the first law that tells two apart has five operations | **new**, small; proved |
| [`EIGHT_SPECIMENS.md`](EIGHT_SPECIMENS.md) | Eight closures of 14 laws, six of which an archived paper called "fossils", all have finite type specimens. The smallest have 3, 3, 5, 5, 6 and 6 elements, and 7 to 32 for the last two | **new**, small; computer-assisted. Corrects the archived J03 |
| [`../../coin/THE_MIRROR.md`](../../coin/THE_MIRROR.md) | Reading a table the other way round is a coin on the catalog: 84 laws on its edge, and 2,305 pairs on its sides | known; teaching |

These pages came from reading the archived ETP papers again on 2026-10-25
([`../../graveyard/j_series_reread/`](../../graveyard/j_series_reread/README.md)).

> **Run the checks** (numpy):
>
> ```
> python verify_zn_laws.py          # 23 checks, about ten seconds
> python verify_steiner.py          # 18 checks, about six seconds
> python verify_eight_specimens.py  # 24 checks, about 35 seconds; --order6 adds the six-element search (3 minutes)
> python independent_check.py       # 5 checks, about five seconds
> ```

The three verify scripts each rebuild the catalog from its definition, with no download, and check it
against laws whose ETP numbers are known. `independent_check.py` shares no code with them: its catalog
comes from the audit of the archived J29 (another author), and it recomputes the headline counts of all
four pages.

**Sources.** The Equational Theories Project, "The Equational Theories Project: advancing collaborative
mathematical research at scale", arXiv:2512.07087 (2025), and its repository,
[github.com/teorth/equational_theories](https://github.com/teorth/equational_theories). OEIS A376640 counts
the catalog's laws by number of operations: 2, 5, 39, 364 and 4284.
