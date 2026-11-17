# The C5 graph star, checked by the Lean kernel

[`C5MagicSet.lean`](C5MagicSet.lean) proves in Lean 4, with no Mathlib, that the 16-observable C5 graph star
([`../ms5_16.json`](../ms5_16.json), [`../THEOREM.md`](../THEOREM.md)) is a magic set:

1. every one of its 7 contexts consists of pairwise commuting Pauli operators;
2. every context multiplies to its stated sign times the identity: one to −I, six to +I;
3. no assignment of values ±1 to the 16 observables makes every context's product of values equal its sign.

Parts 1 and 2 are finite computations on Pauli strings, evaluated by the kernel (`decide`). Part 3 is the parity
argument, proved once: the flattened context list is a permutation of a list made of adjacent pairs (checked by
`decide`), so the product over all contexts of their value products is +1, while the signs multiply to −1.

**Status (2026-11-17).** It compiles with Lean v4.36.0 (`lean C5MagicSet.lean`, about 3 seconds), with no
warnings. `#print axioms` reports only Lean's standard axioms, propext, Classical.choice and Quot.sound: no `sorry`,
and no `native_decide`, which would trust compiled code. The compiled module was also replayed by `leanchecker`,
which exits 0.

**What it does not check.** That the set is *genuine* (no Pauli realisation on four qubits or fewer), and that 16
is the minimum, are not formalized. Both still rest on the written proofs and on computer searches checked only by
AI-written code.

**Run it.** Install Lean with [elan](https://github.com/leanprover/elan), then run:

    lean C5MagicSet.lean
