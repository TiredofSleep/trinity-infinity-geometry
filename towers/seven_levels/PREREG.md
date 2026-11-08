# Seven levels: predictions, registered before any run

These were registered on 2026-11-07, before any computation below was run. They answer the author's question,
*"what extensions would this imply? test them?"*, which came after the sevenths of
[`../../base/SEVENTHS.md`](../../base/SEVENTHS.md) were put on a seven-level quantum system. There, the
shift and the clock are the adding face, the multiplier is the multiplying face, and the Fourier transform
joins them; its square is the half turn. Each prediction says what would kill it. Scores are added after
the run, below the line, and nothing above the line changes.

**Setting.** Seven levels |0⟩, …, |6⟩, with ω = e^(2πi/7).
- Shift X|k⟩ = |k + 1⟩; clock Z|k⟩ = ωᵏ|k⟩.
- Fourier transform F; multiplier M_a|k⟩ = |ak⟩.
- The half turn P|k⟩ = |−k⟩, which is F².
- The **Clifford group** is the set of unitaries that carry shifts and clocks to shifts and clocks, up to phase.
- The eight **bases** are the common eigenbases of the shifts and clocks lying along each of the eight lines
  through the origin of the 7 × 7 phase space:
  - the levels themselves (the clocks);
  - the Fourier basis (the shifts);
  - for each slope c = 1, …, 6, the eigenbasis of X Zᶜ.

---

**Q1. The classical part is the two faces.** Of the 5040 ways to permute the seven levels, exactly 42 are
Clifford operations. They are the maps k → ak + b: adding and multiplying together.
*Kill:* a different count, or a Clifford permutation of another form.

**Q2. The 168 again.** The Clifford group's geometric part, SL(2, 7), has 336 elements. Modulo ±1, its 168
elements have the same orders as the Fano plane's 168 symmetries: one of order 1, 21 of order 2, 56 of order
3, 42 of order 4 and 48 of order 7.
*Kill:* any difference.

**Q3. The eight bases sit like the cube's corners.**
- (a) The multipliers fix two of the eight bases, the levels and the Fourier basis. They split the other six by
  slope into the squares {1, 2, 4} and the others {3, 5, 6}.
- (b) The Fourier transform swaps the two fixed bases and swaps the two triples.
- (c) Every subgroup of the 168 shaped like the cube's rotation group (S₄) moves the eight bases exactly as the
  cube's rotations move its eight corners: one orbit, and the same number of fixed points for every kind of
  element.

*Kill:* any part fails.

**Q4. The magic subspace is Klein's space.** The states that change sign under the half turn span 3
dimensions, with basis (|j⟩ − |−j⟩)/√2 for the squares j = 1, 2, 4. The Clifford group carries them to
themselves.
- There the group acts through exactly 168 elements, up to scalars.
- The quadratic phase acts diagonally, with entries ω⁴, ω², ω.
- The multiplier ×2 permutes the three coordinates in a cycle.
- Klein's quartic x³y + y³z + z³x is invariant.

*Kill:* a different count, or no invariant quartic of that form.

**Q5. The octahedron acts on the magic subspace as it acts on our space.** Restricted to any of the S₄
subgroups, the magic representation has the character of the octahedron's rotations of ordinary space: 3, 0,
−1 and 1 on elements of orders 1, 3, 2 and 4. On elements of order 7 its trace is not real:
(−1 ± √−7)/2.
*Kill:* a different character.

**Q6. The octahedron's height is a magic state.** The Legendre state is +1 on the squares {1, 2, 4}, −1 on
{3, 5, 6} and 0 at the centre.
- It is an eigenvector of every multiplier: the eigenvalue is +1 or −1, by whether the multiplier is a square.
- It is an eigenvector of the Fourier transform, with eigenvalue i.
- It changes sign under the half turn, so its quasi-probability (Wigner value) at the centre is −1/7.

*Kill:* any part fails.

**Q7. (A guess.)** No seven-level state has more total Wigner negativity than the Legendre state.
*Kill:* a search from many random starts finds a state with more, by more than 10⁻⁶.

**Q8. The same coin at 5.** For five levels:
- exactly 20 permutations are Clifford, the maps k → ak + b;
- the geometric part, modulo ±1, has the element orders of the icosahedron's rotation group: 1, 15, 20 and 24
  elements of orders 1, 2, 3 and 5;
- the magic subspace has dimension 2 and carries 120 matrices with the element orders of the binary
  icosahedral group, which is the icosahedron's rotations lifted to spinors.

*Kill:* any part fails.

**Expected standing, stated before the run.** Q1–Q6 and Q8 rest on classical mathematics: Weyl, Wootters and
Fields, Gross, Klein and Galois. If they hold, what is claimed here is the reading, not the facts. Q7 is a guess.

---

## Scores (added after the run, 2026-11-07)

Run by [`verify_seven_levels.py`](verify_seven_levels.py); its output is kept in
[`verify_seven_levels.log`](verify_seven_levels.log). **7 of 8 held.**

| | outcome | evidence |
|---|---|---|
| Q1 | held | 42 of the 5040 permutations, exactly the maps k → ak + b |
| Q2 | held | the same orders for both: 1, 21, 56, 42, 48 elements of orders 1, 2, 3, 4, 7 |
| Q3 | held | (a) and (b) as stated; (c) 14 subgroups shaped like S₄, each with the cube's fixed points by element order, and one orbit |
| Q4 | held | 168 elements up to scalars; diag(ω⁴, ω², ω); a 3-cycle; the quartic invariant under every generator |
| Q5 | held | the exact group in SU(3) has 168 elements; 14 copies of S₄, each with character 3, −1, 0, 1; the order-7 traces are (−1 ± √−7)/2 |
| Q6 | held | every part; the value at the centre is −1/7 |
| Q7 | **died** | Legendre state 0.728262; a search from 125 starts found 0.732522, at a state that is not odd under the half turn (it is in the log to 8 decimals) |
| Q8 | held | 20 affine permutations; the icosahedral rotation group's orders; 120 matrices with the binary icosahedral group's orders |

**Yield.** As expected, Q1–Q6 and Q8 are classical, and they are credited in the [README](README.md). The one
guess, Q7, died, and it is kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md).

---

## Round 2: the most negative state (registered 2026-11-07, before its run)

Q7 died, so this round asks what the most negative seven-level state actually is. A state's total negativity
is the sum of its negative Wigner values, taken positive.

**The search.** Maximize the total negativity from random starts by Powell's method: 100 starts for three
levels and 400 for seven. Two states count as **the same up to symmetry** when a Clifford operation carries
one to the other, up to phase. The Clifford group of seven levels has 49 × 336 = 16 464 operations up to phase.

**R1. (Calibration.)** For three levels, the largest total negativity is 1/3, the value of the strange state
(|1⟩ − |2⟩)/√2.
*Kill:* a larger value, by more than 10⁻⁶, or a smaller maximum.

**R2.** For seven levels, the maximizers found (within 10⁻⁵ of the best) are all the same up to symmetry.
*Kill:* two of them that no Clifford operation carries one to the other.

**R3.** The seven-level maximizer has a symmetry: some Clifford operation other than the identity fixes it, up
to phase.
*Kill:* none does.

**R4.** The seven-level maximum is below 0.75.
*Kill:* 0.75 or more.

**R5.** The maximizer trades depth for breadth: its most negative Wigner value is above −1/7, the depth the
Legendre state reaches.
*Kill:* a maximizer with a value of −1/7.

---

## Round 2 scores (added after the run, 2026-11-07)

Run by [`most_negative.py`](most_negative.py); its output is kept in [`most_negative.log`](most_negative.log).
The search is seeded, so a rerun repeats it. **5 of 5 held.**

| | outcome | evidence |
|---|---|---|
| R1 | held | the best of 100 starts is 0.333333333, the strange state's value. The Norrell state reaches it too ([README](README.md) §4) |
| R2 | held | 3 of the 400 starts came within 10⁻⁵ of the best, 0.732522000, and Clifford operations carry them to one another |
| R3 | held | 4 Clifford operations fix the maximizer, of orders 1, 2, 4 and 4 |
| R4 | held | 0.732522000 |
| R5 | held | the maximizer's deepest value is −0.067999, against −1/7 ≈ −0.142857. It is negative at 16 of the 49 points |

**Yield.** R1 recovers a known value. The state behind R2–R5 does not appear in the literature we checked, which
covers three and five levels. It was found by search, so it is not proved to be the maximum. What it is, and the
coin it makes with the Legendre state, are in the [README](README.md) §4.
