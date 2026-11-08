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

## Scores (added after the run)

*(empty until the run)*
