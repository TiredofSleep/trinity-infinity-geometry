# The coin — the second lens

*Paradox classification, not resolution.* Every coin has two sides and an edge. A **flip** is a move
that, done twice, changes nothing. Its **sides** are what it swaps, and its **edge** is what it leaves
in place. The paradox lives on the edge, and this program classifies it rather than resolving it.

The [base](../base/README.md) is where you stand. The [towers](../towers/README.md) climb. The coin
is what every floor turns over.

> **Run the checks** (Python 3.10+, numpy):
>
> ```
> python verify_coins.py            # every [FORCED] line of THE_COIN.md (69 checks)
> python verify_paradox_types.py    # every [FORCED] line of PARADOX_TYPES.md (11 checks)
> ```

| file | what it is |
|---|---|
| [`THE_COIN.md`](THE_COIN.md) | **Start here.** It covers the following: <ul><li>What a coin is, and the rule that every linear flip splits each thing into an edge part and a side part: real + imaginary, cos + *i* sin, symmetric + skew.</li><li>The author's three coins — positive/negative, real/imaginary, finite/infinite — as the three half-turns of the sphere of numbers about the axes of the octahedron 0, ∞, ±1, ±*i*.</li><li>The missing edges where the paradoxes live (√2, *i*), and the keystone made exact.</li><li>One cube seen through two lenses.</li><li>The centre inhabited or empty, which classifies 5, 7 and 9: oddness forces the centre in a solid.</li><li>The whole coin: 27 = 8 + 12 + 6 + 1.</li><li>Every tower's coin.</li></ul> |
| [`PARADOX_TYPES.md`](PARADOX_TYPES.md) | **The author's four kinds of paradox** (with Ben Mayes, April 2026), read through the coin. Each type pairs with a part of the coin: <ul><li>Type I, insufficient coverage (Zeno) — two lenses; the author's Theorem 0 says when views suffice.</li><li>Type II, a missing invariant (Banach–Tarski, Gödel) — a missing edge.</li><li>Type III, inadmissible (Russell, the Liar, Cantor) — a flip with no edge, plus self-reference; give "not" an edge and the Liar lands on it (Kripke).</li><li>Type IV, time-consistency (the Unexpected Hanging) — open.</li></ul> |
