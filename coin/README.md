# The coin — the second lens

*Paradox classification, not resolution.* Every coin has two sides and an edge. A **flip** is a move
that, done twice, changes nothing. Its **sides** are what it swaps, and its **edge** is what it leaves
in place. The paradox lives on the edge, and this program classifies it rather than resolving it.

The [base](../base/README.md) is where you stand. The [towers](../towers/README.md) climb. The coin
is what every floor turns over.

> **Run the checks** (Python 3.10+, numpy):
>
> ```
> python verify_coins.py            # every [FORCED] line of THE_COIN.md (68 checks)
> python verify_paradox_types.py    # every [FORCED] line of PARADOX_TYPES.md (12 checks)
> python verify_transpose_coin.py   # THE_TRANSPOSE_COIN.md (20 checks)
> python verify_two_readings.py     # TWO_READINGS_OF_ZN.md (23 checks, about twenty seconds)
> python verify_mirror.py           # THE_MIRROR.md (26 checks, about thirty seconds)
> ```

| file | what it is |
|---|---|
| [`THE_COIN.md`](THE_COIN.md) | **Start here.** It covers the following: <ul><li>What a coin is, and the rule that every linear flip splits each thing into an edge part and a side part: real + imaginary, cos + *i* sin, symmetric + skew.</li><li>The author's three coins — positive/negative, real/imaginary, finite/infinite — as the three half-turns of the sphere of numbers about the axes of the octahedron 0, ∞, ±1, ±*i*.</li><li>The missing edges where the paradoxes live (√2, *i*), and the keystone made exact.</li><li>One cube seen through two lenses.</li><li>The centre inhabited or empty, which classifies 5, 7 and 9: oddness forces the centre in a solid.</li><li>The whole coin: 27 = 8 + 12 + 6 + 1.</li><li>Every tower's coin.</li></ul> |
| [`PARADOX_TYPES.md`](PARADOX_TYPES.md) | **The author's four kinds of paradox** (with Ben Mayes, April 2026), read through the coin. Each type pairs with a part of the coin: <ul><li>Type I, insufficient coverage (Zeno) — two lenses; the author's Theorem 0 says when views suffice.</li><li>Type II, a missing invariant (Banach–Tarski, Gödel) — a missing edge.</li><li>Type III, inadmissible (Russell, the Liar, Cantor) — a flip with no edge, plus self-reference; give "not" an edge and the Liar lands on it (Kripke).</li><li>Type IV, time-consistency (the Unexpected Hanging) — open.</li></ul> |
| [`THE_TRANSPOSE_COIN.md`](THE_TRANSPOSE_COIN.md) | **The transpose's coin.** In a symmetric Latin square of odd order every symbol sits on the diagonal exactly once, by the parity that puts 5, 7 and 9 on their centres. It is why an odd round robin has one bye per round, and why the Lo Shu mod 3 is commutative only after a quarter turn. The easy case of Ryser's conjecture; classical, from the archived J29. |
| [`THE_MIRROR.md`](THE_MIRROR.md) | **The transpose on laws.** Reading a table the other way round mirrors every law it obeys. Of the 4,694 short laws of the Equational Theories Project, 84 are their own mirror (the edge), and the rest form 2,305 pairs (the sides). On profiles the edge widens. Classical duality, with the counts computed here. |
| [`TWO_READINGS_OF_ZN.md`](TWO_READINGS_OF_ZN.md) | **Theorem 0 at work on ℤ/n.** When do two readings (residues, orbits of units, the mirror) tell every number apart? Four criteria, settled level by level, and a trap at n = 15. Elementary; it corrects the archived J27, J34 and J35, whose headline theorems were false. |
