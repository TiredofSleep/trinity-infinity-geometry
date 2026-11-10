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

---

## Round 3: the three open questions (registered 2026-11-08, before its run)

Round 2 left three questions open, and the author asked for all three:
- Is 0.732522 the seven-level maximum?
- Is the Legendre state the best odd state?
- Which side wins at eleven levels?

**The sides** are round 2's coin. An odd state, under the half turn, sits on the floor at the centre (−1/p); an
even one sits on the ceiling (+1/p).

**Two tools.** Both rest on one identity: the sum of a state's |W| is the largest value of Σ s_u W_u over sign
choices s_u = ±1, one for each phase-space point u.
- *The sign ascent.* Give each point the sign of the state's Wigner value there. Replace the state by the top
  eigenvector of Σ s_u A_u, where A_u is the point's Wigner operator. No step lowers the sum of |W|, so every start
  climbs to a local maximum. The starts are uniformly random states, seeded (20261108).
- *The exhaustive count.* If a Clifford operation g fixes a state, the state's signs are the same along each orbit
  of g in phase space. So the best state that g fixes is the best top eigenvector, inside g's eigenspaces, over the
  sign choices that are constant on g's orbits.
  - For the half turn at seven levels that is 2^24 sign choices on each side; every one is tried.
  - The centre's sign is forced: it is + on the even side and − on the odd side.

**Why the count reaches every symmetric state at seven levels.** If a Clifford operation other than the identity
fixes a state, then so does one of prime order: 2, 3 or 7, the primes dividing 16 464. Conjugate operations fix
conjugate states, with the same negativity, so one of each kind is enough:
- order 2: the half turn, the only kind;
- order 3: the multiplier ×2, since all subgroups of order 3 are conjugate (Sylow);
- order 7: up to conjugacy these all lie in the one group made of the shifts, the clocks and the shear's powers.
  That gives the shift, the shear, and the shears composed with a shift that fix no point; all of them are counted.

[`round3.py`](round3.py) is committed with these predictions, before its run.

**T1. (Calibration.)** At three levels the count gives 1/3 on both sides: the strange state on the odd side, the
Norrell state on the even side.
*Kill:* either side differs from 1/3 by more than 10⁻⁹.

**T2. (Calibration.)** At five levels nothing beats Jain and Prakash's maximum, (√5 − 2 + √(15 + 6√5))/10 ≈
0.556677 in total negativity. Neither the count on either side (2^12 sign choices each) nor 200 000 sign ascents in
the whole space finds more. Their state is even, so the best even state reaches the value exactly. (It is
fixed by the half turn, and its deepest value, −0.09, is above −1/5, so it is not odd.)
*Kill:* a larger value, by more than 10⁻⁹ in the count or 10⁻⁶ in the search; a search whose best falls short by
more than 10⁻⁶; or a best even state below the value.

**T3. (Question B.)** At seven levels the best odd state is the Legendre state, at
(4 cos(2π/7) − 4 cos(6π/7) − 1)/7 ≈ 0.728262.
*Kill:* an odd sign choice that gives more, by more than 10⁻⁹, or a best odd state that no Clifford operation
carries to the Legendre state.

**T4.** At seven levels the best even state is the round-2 record, 0.732522.
*Kill:* an even state above it by more than 10⁻⁹, or a best even state that is not the record up to symmetry.

**T5. (Question A, the symmetric states.)** No seven-level state that a Clifford operation other than the identity
fixes has more than 0.732522. So if the record is ever beaten, the winner has no symmetry at all.
*Kill:* a symmetric state above 0.732522, by more than 10⁻⁹.

**T6. (Question A, the rest.)** A million sign ascents from random seven-level states find nothing above 0.732522,
and at least one reaches it.
*Kill:* a larger value, by more than 10⁻⁹, or no start that reaches the record.

**T7. (Question C.)** At eleven levels the even side wins. A million sign ascents among the even states (6
dimensions) and a million among the odd ones (5 dimensions): the best even state beats the best odd state, by
more than 10⁻⁶. The Legendre state counts as an odd state.
*Kill:* the odd side comes within 10⁻⁶ of the even side, or passes it.

**T8. (Question B at eleven.)** The Legendre state is still the deepest odd state: no odd state found beats it.
*Kill:* an odd state found with more, by more than 10⁻⁶.

**T9.** At eleven levels the Legendre state is beaten: a million sign ascents in the whole space find a state
with more.
*Kill:* none beats it by more than 10⁻⁶.

**T10.** The best state found at eleven levels is even about one point, as the maxima at five and seven are. Its
largest Wigner value is +1/11, at exactly one point, and it never reaches −1/11.
*Kill:* anything else.

**Expected standing, stated before the run.** T1 recovers known values (Veitch et al. 2014). T2 recovers Jain and
Prakash's value, which came from a numerical search; the count would make its symmetric part exact. T3–T6 would
be new if they hold. T3–T5 are exhaustive, exact up to rounding; T6 is a search, so it is evidence, not proof.
T7–T10 are guesses about eleven levels, read off from three, five and seven; they rest on searches alone. The
literature checked has nothing on seven or eleven levels:
- Veitch et al. (2014);
- Wang, Wilde and Su (2020);
- Jain and Prakash (2020);
- Erew and Goldstein (2025). They show that a state fixed by a group of Clifford operations is stationary for
  mana, and they list such states for two, three and five levels;
- the OpenAI math release of October 2026.

---

## Round 3 scores (added after the run, 2026-11-08)

Run by [`round3.py`](round3.py); its output is kept in [`round3.log`](round3.log). The run is seeded, and a
second run repeated every scored line. **9 of 10 held.**

| | outcome | evidence |
|---|---|---|
| T1 | held | the count gives 1/3 on both sides |
| T2 | held | the best even state has 0.556677223351, Jain and Prakash's value to 12 decimals, and the best odd state 0.433070. Of the 200 000 climbs, 15 565 reach 0.556677 and none goes higher |
| T3 | held | of the 16 777 216 odd sign choices, the best gives the Legendre state's 0.728262097006. The 28 choices that reach it are all the Legendre state up to symmetry; the next value is 0.721570 |
| T4 | held | of the 16 777 216 even choices, the best gives the record's 0.732522000011. The 84 choices that reach it are all the record up to symmetry; the next value is 0.729722 |
| T5 | held | the best states fixed by the other kinds of symmetry: the multiplier ×2, 0.728262 (the Legendre state); the shift, 0; the shear, 0.320997; the 42 groups of shears with a shift, 0.725152 |
| T6 | held | 1460 of the million climbs reach the record, and none goes higher |
| T7 | held | even 1.032586, odd 1.029707 |
| T8 | **died** | the best odd state found has 1.029707, against the Legendre state's 0.787711. It has 24 symmetries, with the element orders of the binary tetrahedral group |
| T9 | held | 1.032586 against 0.787711 |
| T10 | held | the best state found touches +1/11 at one point and never −1/11. Its only symmetry is the half turn about that point |

**Yield.** T1 and T2 recover known values, and T2's count makes the symmetric part of Jain and Prakash's search
exact. T3–T5 are exhaustive, and new as far as we checked. T6 is a search. At eleven, three guesses held and one
died: the deepest odd state there is not the Legendre state. What the run found, and the coin across 3, 5, 7 and
11, are in the [README](README.md) §5. The dead guess is kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md).

---

## Round 4: toward a proof at seven, the maximum at eleven, the sides at thirteen (registered 2026-11-08, before its run)

The author asked for all three of round 3's next questions. [`round4.py`](round4.py) is committed with these
predictions, before its run. It uses round 3's two tools, and runs in three parts.

**A. Seven levels: toward a proof.** Round 3 proved that no state with a unitary symmetry beats the record. This
part closes in on the rest.

**U1.** No real seven-level state beats the record. Every one of the 2^28 sign choices symmetric under the mirror
(q, p) → (q, −p) is tried, and the best is the record. Every anti-unitary symmetry either squares to a unitary one,
which round 3 counted, or is conjugate to complex conjugation, whose fixed states are the real ones; the run
checks this. So, with round 3, no state with any symmetry, unitary or anti-unitary, would beat the record.
*Kill:* a mirror-symmetric choice above 0.732522 by more than 10⁻⁹, or a best real state that is not the record up
to symmetry or mirror.

**U2. (Forced.)** A state that beats the record has between 8 and 24 negative points. The Wigner operators of a
set of k points sum to an operator with trace k and squared norm 7k, so by Samuelson's inequality its lowest
eigenvalue is at least k/7 − √(6k(1 − k/49)). A state whose negative points are that set has total negativity at
most minus that eigenvalue over 7, and outside 8 ≤ k ≤ 24 this falls short of 0.732522.
*Kill:* an error in the bound; the run checks it on random sets.

**U3.** Ten million climbs from random states find nothing above 0.732522. The run also estimates, by Good and
Turing's rule, how much of the space belongs to tops it never reached.
*Kill:* a larger value, by more than 10⁻⁹.

**B. Eleven levels: the true maximum.** Round 3's best was 1.032586: an even state whose only symmetry is its half
turn.

**U4.** Nothing beats it. The run tries ten million climbs among even states, four million in the whole space, and
2000 kicks from each of the 20 highest tops.
*Kill:* a larger value, by more than 10⁻⁹.

**U5.** No state with a symmetry of order 4, 5, 6 or 11 beats it. Exhaustive counts: 2^30 sign choices in each
eigenspace of the quarter turn, 2^25 for order 5, 2^20 for order 6, and the shift, the shear and every group of
order 11 that fixes no point. States whose only symmetries have order 2 or 3 are beyond counting (2^60 and 2^40
choices).
*Kill:* a symmetric state above 1.032586, by more than 10⁻⁹.

**U6.** Ten million climbs among odd states: the tetrahedral state, 1.029707, stays the best odd state.
*Kill:* an odd state above it, by more than 10⁻⁹.

**U7.** Round 3 found samples of one top that no Clifford operation carries to each other. Such samples are
mirror images: complex conjugates, up to a Clifford operation.
*Kill:* two samples of one value that neither a Clifford operation nor a mirror joins.

**C. Thirteen levels: 1 more than a multiple of 4, like 5.** Here the Legendre state is even. Two readings
compete:
- *the size reading:* from 7 on, the two sides end close, and the winner is not fixed by its symmetries;
- *the Legendre-side reading:* when the Legendre state is even, the even side holds the most symmetric states,
  wins by a wide margin, and has a winner fixed by its symmetries, as at 5.

U9 and U13 follow the size reading; the other reading predicts the opposite of both.

**U8.** The even side wins at 13. The run tries three million climbs on each side, and the Legendre state counts
as even.
*Kill:* the odd side comes within 10⁻⁶ of the even side, or passes it.

**U9.** It wins by less than 0.01.
*Kill:* a margin of 0.01 or more, or U8 dying.

**U10.** The best state found in two million climbs in the whole space touches +1/13 at exactly one point, and
never −1/13.
*Kill:* anything else.

**U11.** The Legendre state of 13 is even (forced: (−1 | 13) = +1), and the best even state found beats it.
*Kill:* the Legendre state is the best even state found.

**U12. (Forced.)** Every state that a binary tetrahedral group fixes lies on the Legendre state's side.
- Such a group contains the half turn, and every character of the group is trivial on it.
- For p ≥ 5, SL(2, p) is perfect, so its operators have determinant 1. The half turn's operator is therefore
  (−1 | p) times the parity.
- So the fixed state's parity is (−1 | p): odd at 3, 7 and 11, and even at 13.

The tool was run at 3 and 11 while it was tested, before this registration. It found one odd state at 3, the
strange state, and two odd states at 11, at 1.029707 and 0.899019. The live checks are 7 and 13.
*Kill:* a fixed state on the other side.

**U13.** The winner at 13 is not fixed by its symmetries alone.
*Kill:* it is.

**Expected standing, stated before the run.** U1 and U5 are exhaustive. U2 and U12 are forced by the arguments
given. The others rest on searches. None of the literature checked (2026-11-07 to 09) treats eleven or thirteen
levels.

---

## Round 4 scores (added after the run, 2026-11-08)

Run by [`round4.py`](round4.py) in three parts; the output is kept in [`round4_seven.log`](round4_seven.log),
[`round4_eleven.log`](round4_eleven.log) and [`round4_thirteen.log`](round4_thirteen.log). The runs are seeded.
**12 of 13 held.**

| | outcome | evidence |
|---|---|---|
| U1 | held | of the 2^28 mirror-symmetric sign choices, the best gives the record, reached by 42 choices, all its images; the next value is 0.729722. All 392 anti-unitary involutions are conjugate to the mirror |
| U2 | held | the bound allows 8 to 24 negative points, and it held on 9600 random sets |
| U3 | held | 14 754 of the ten million climbs reach the record, and none goes higher; 52 348 tops, 3248 of them reached once (Good and Turing: about 3 × 10⁻⁴ unreached) |
| U4 | held | 158 331 of ten million even climbs and 745 of four million whole-space climbs reach 1.032586; 40 000 kicks find nothing higher |
| U5 | held | the best states fixed by a symmetry: order 4, 1.029707 (the tetrahedral state); order 5, 0.999307; order 6, 1.029707; order 11, at most 0.913740 |
| U6 | held | 34 706 of ten million odd climbs reach the tetrahedral state, and none goes higher |
| U7 | held | all 35 sample pairs that no Clifford operation joins are mirror images |
| U8 | held | even 1.168522, odd 1.151336 |
| U9 | **died** | the margin is 0.017, not under 0.01 |
| U10 | held | the best state found touches +1/13 at one point and never −1/13; its only symmetry is the half turn there |
| U11 | held | the Legendre state of 13 is even, at 0.933851, below the best even state found |
| U12 | held | the tetrahedral states: one at 3 (odd), none at 7, two at 11 (odd), one at 13 (even, 0.982303) |
| U13 | held | the winner at 13 is not fixed by its symmetries alone |

**Yield.** U1, U2 and U5 are exhaustive or forced, and new as far as we checked. So is U12's rule, though its
ingredient, the sign of the half turn's operator, is a standard fact about the Weil representation. The searches
held everywhere but one place: the margin at 13, where the size reading's guess died. The other reading's guess,
a winner fixed by its symmetries, failed too (U13 held). The coin across five primes is in the
[README](README.md) §6. The dead guess is kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md).

---

## Round 5: seventeen and nineteen (registered 2026-11-08, before its run)

The author asked for 17 and 19. [`round5.py`](round5.py) is committed with these predictions, before its run.

**The picture round 4 left.**
- The even side wins at every prime above 3.
- When p is 3 more than a multiple of 4 the two sides end within 0.005. When it is 1 more they end farther apart:
  0.124 at 5, 0.017 at 13.
- From 7 on, no winner is fixed by its symmetries.

Seventeen is 1 more than a multiple of 4 and nineteen is 3 more, so the pair tests all of it at once.

**The setting.**
- *Climbs* (the sign ascent from random states) in the even subspace, the odd subspace and the whole space:
  - at 17, three million on each side and 1.5 million in the whole space;
  - at 19, two million on each side and one million in the whole space.
  - The Legendre state counts on its own side.
- *The exceptional groups* (binary tetrahedral, octahedral and icosahedral) are found in SL(2, p), one from each
  conjugacy class, and the states each fixes are computed exactly.
- *Testing.* While the tool was tested, it was run at 11 and 13, where it repeated round 4's states, and its group
  search ran at 17 and 19 with the fixed states hidden. It found two classes each of tetrahedral and octahedral
  groups at 17, and one tetrahedral and two icosahedral classes at 19.

**V1.** The even side wins at 17.
*Kill:* the odd side comes within 10⁻⁶ of the even side, or passes it.

**V2.** The even side wins at 19.
*Kill:* the same.

**V3.** The two sides end closer at 19 than at 17: 3 more than a multiple of 4 is closer than 1 more, as 7 and 11
were against 5 and 13.
*Kill:* the margin at 19 is as large as at 17, or larger.

**V4a.** The margin at 17 is below 13's 0.017.
*Kill:* 0.017 or more.

**V4b.** The margin at 19 is below 11's 0.0029.
*Kill:* 0.0029 or more.

**V5a, V5b.** At 17, and at 19, the best state found touches the ceiling at exactly one point, never touches the
floor, and is not fixed by its symmetries alone.
*Kill:* anything else.

**V6.** At 19, the best odd state found has at least 12 symmetries: on the Legendre state's side a highly symmetric
state wins, as at 3, 7 and 11.
*Kill:* fewer than 12.

**V7a, V7b.** The Legendre state is beaten on its own side: at 17 by the best even state found, at 19 by the best
odd state found.
*Kill:* the Legendre state is the best state found there.

**V8a, V8b. (Forced.)** Every state that a binary tetrahedral, octahedral or icosahedral group fixes lies on the
Legendre state's side: even at 17, odd at 19.
- Each of these groups has the half turn inside its commutator subgroup, so all its characters are trivial there.
- The half turn's operator is (−1 | p) times the parity (round 4, U12).

*Kill:* a fixed state on the other side.

**Expected standing, stated before the run.** V8 is forced. The others are guesses from the pattern at 3 to 13,
and they rest on searches. V6 is the boldest: it says that the lesson of the strange state continues at 19.

---

## Round 5 scores (added after the run, 2026-11-08)

Run by [`round5.py`](round5.py); the output is kept in [`round5_seventeen.log`](round5_seventeen.log),
[`round5_nineteen.log`](round5_nineteen.log) and [`round5_combined.log`](round5_combined.log). The runs are seeded.
**7 of 12 held.**

| | outcome | evidence |
|---|---|---|
| V1 | held | at 17: even 1.402567, odd 1.371867 |
| V2 | **died** | at 19 the odd side wins: 1.507862 against 1.484879 |
| V3 | held | the gap is 0.023 at 19 and 0.031 at 17 |
| V4a | **died** | the margin at 17 is 0.031, not below 0.017 |
| V4b | **died** | at 19 there is no even lead to be small: the odd side leads by 0.023. The script's automatic line said held, because −0.023 is below 0.0029, but the prediction meant the even side's lead, as round 4's U9 did |
| V5a | held | the best state at 17 touches the ceiling once and never the floor, and its 6 symmetries do not fix it |
| V5b | **died** | the best state at 19 is odd: it sits on the floor at its centre |
| V6 | **died** | the best odd state at 19 has 4 symmetries. The tetrahedral state, with 24, has 1.495712, below it |
| V7a | held | the Legendre state of 17 has 1.250924, beaten by 1.402567 |
| V7b | held | the Legendre state of 19 has 1.356950, beaten by 1.507862 |
| V8a | held | at 17 every state of the tetrahedral and octahedral groups is even (values from 1.167172 to 1.388656) |
| V8b | held | at 19 the tetrahedral group's three states are odd, and the icosahedral groups fix none |

**Yield.** The forced prediction held at both primes. The guesses read off 3 to 13 did worse: the even side's
streak ended at 19, and the margins grew instead of shrinking. The dead guesses are kept in
[`../../GRAVEYARD.md`](../../GRAVEYARD.md), and the [README](README.md) §7 has what the run found.

---

## Round 6: the author's prediction (registered 2026-11-08, not yet run)

> *i'd predict that even only wins the lows, the odd wins the rest?* — the author, 8 November 2026, on seeing
> round 5's nineteen

Round 5 broke the even side's streak: the odd side won at 19. Two readings fit every prime so far, and they part
at 29.
- *The author's:* the even side wins only the low primes; from 19 on, the odd side wins.
- *The Legendre-side reading:* the side that the Legendre symbol picks wins. That side holds the Legendre state
  and the tetrahedral states: odd when p is 3 more than a multiple of 4, even when it is 1 more. It won at 5, 13,
  17 and 19, and lost only at 7 and 11, by less than 0.005.

**W1 (the author's prediction).** The odd side wins at 23 and at 29.
*Kill:* the even side wins at either.

**W2 (the rival reading).** The Legendre side wins: the odd side at 23, the even side at 29.
*Kill:* the other side wins at either.

At 23 the two agree, so 29 decides between them. The run will use round 5's machinery, with at least two million
climbs on each side at each prime; at 29 that takes hours. Its script will be committed before the run.

---

## Round 6 scores (added after the run, 2026-11-08)

Run by [`round6.py`](round6.py), committed at 66b4d0d before its run; the output is kept in
[`round6_twentythree.log`](round6_twentythree.log), [`round6_twentynine.log`](round6_twentynine.log) and
[`round6_combined.log`](round6_combined.log). The runs are seeded. **Both readings died.**

| | outcome | evidence |
|---|---|---|
| W1, the author's prediction | **died** | at 23 the even side wins, 1.700022 against 1.696423. At 29 the odd side wins, 1.963715 against 1.957461, as the author said |
| W2, the rival reading | **died** | the even side wins at 23 and the odd side at 29: the opposite of both its calls |

**Rechecks, not registered.** At 23, two million more odd climbs with a fresh seed, and kicks from the highest odd
tops, found the same odd best, 353 times, and nothing higher. At 29, two million more even climbs with a fresh
seed, and kicks from the highest even tops, found the same even best, 11 times, and nothing higher.

**Yield.** The author's prediction called 29 right and 23 wrong; the rival called neither. The even side has won at
5, 7, 11, 13, 17 and 23, and the odd side at 19 and 29. Both readings are kept in
[`../../GRAVEYARD.md`](../../GRAVEYARD.md), and the [README](README.md) §8 has what the run found.

---

## Round 7: the author's 7-wheel (registered 2026-11-08, not yet run)

> *it must be related to the wheel of numbers revolving around 7? i am thinking shor's with a 7 wheel
> conversion?* — the author, 8 November 2026, on seeing round 6

**Made exact.**
- For a prime p other than 7, turn the 7-wheel: the powers of 7 modulo p. Its period r is what Shor's algorithm
  finds.
- If r is even, the wheel passes through the half turn: 7^(r/2) ≡ −1 (mod p). That is the case Shor's algorithm
  checks for.
- If r is odd, the wheel never reaches the half turn.
- The half turn is the coin's edge: the centre's Wigner operator is the parity, k → −k.

**The rule.** The even side wins exactly when the 7-wheel passes through the half turn.

**Against the primes already run.** This is a retrodiction, not a test. The rule fits every one of them:
- 3: r = 1, so the wheel never reaches the half turn; the two sides tie;
- 5, 11, 13, 17 and 23: r is even, and the even side wins;
- 19 (r = 3) and 29 (r = 7): the wheel never reaches the half turn, and the odd side wins.

Of the bases 2 to 29, only 7 fits all eight primes. When p is 3 more than a multiple of 4, quadratic reciprocity
turns the rule into p's place on the sevenths' wheel. The odd side wins exactly when p leaves a remainder of 3, 5
or 6 on division by 7: the non-squares of the sevenths.

**Caution.** No mechanism is known: the negativity problem at p never mentions 7. Odd periods come at about a
third of the primes, so a rule fixed in advance would fit these eight by chance about one time in seventy. Round
6's observation, that the odd side's wins fell at primes 4 more than a multiple of 5, fits them too.

**X1 (the author's 7-wheel).** The odd side wins at 31 (r = 15) and at 37 (r = 9).
*Kill:* the even side wins at either.

**X2 (the rival observation).** The even side wins at 31 and at 37: neither is 4 more than a multiple of 5.
*Kill:* the odd side wins at either.

31 alone decides between them. The run will use round 6's machinery, with two million climbs on each side; at 31
that takes about three hours, at 37 about six. Its script will be committed before the run.

---

## Round 8: the two-wheels test (registered 2026-11-08, before its run)

The author asked for this test after a pause to look at the data from other angles.

**The reading.**
- The Clifford operations that fix the centre form SL(2, p). Two cyclic wheels run through it:
  - the multiplying wheel, k → ak, with p − 1 steps: the wheel of numbers, which at 7 is the sevenths' six;
  - the turning wheel, the rotations of phase space such as the Fourier transform, with p + 1 steps.
- The two wheels share only the half turn, which is the coin's edge.
- Every winner found so far has a symmetry from the turning wheel, or only the half turn. None has a symmetry from
  the multiplying wheel beyond the half turn. The Legendre state, which the whole multiplying wheel fixes, has not
  won since 3.

**The test.** For each prime p and each order m > 2 that divides p + 1 (turning) or p − 1 (multiplying):
- the states that the wheel's subgroup of order m fixes are the eigenvectors of its generator;
- in each eigenspace, the sign ascent finds the best state, with the same effort on both wheels: 3000 k² starts
  in an eigenspace of dimension k, at most 300 000;
- a one-line eigenspace is exact.

[`two_wheels.py`](two_wheels.py) is committed with these predictions, before its run. While it was tested it ran at
5 and 7, where the winners were known:
- at 5, the turning wheel's best is Jain and Prakash's state, 0.556677, and the multiplying wheel's best is
  0.554893;
- at 7, the turning wheel's best is the record, 0.732522, and the multiplying wheel's best is the Legendre state,
  0.728262.

The live test is 11 to 29.

**Y1.** At every prime from 11 to 29, the best turning-symmetric state beats the best multiplying-symmetric state.
*Kill:* a prime where the multiplying wheel's best is as good or better.

**Y2. (Calibration.)** At 17, 19 and 29, where the winner found so far has a turning symmetry, the turning search
reaches it, within 10⁻⁶.
*Kill:* it falls short at any of them.

**Y3.** The turning search finds nothing above the winners found so far, at any prime.
*Kill:* a higher state, which would be a new best.

**Expected standing, stated before the run.** This tests a reading from the angles, by search inside symmetric
families. The proposed mechanism, that a turning symmetry treats every direction of phase space alike, is not
tested here.

---

## Round 8 scores (added after the run, 2026-11-08)

Run by [`two_wheels.py`](two_wheels.py); the output is kept in [`two_wheels_A.log`](two_wheels_A.log),
[`two_wheels_B.log`](two_wheels_B.log) and [`two_wheels_combined.log`](two_wheels_combined.log). **2 of 3 held.**

| | outcome | evidence |
|---|---|---|
| Y1 | **died** | at 13 the multiplying wheel wins: its order-4 family reaches 1.167364, and the turning wheel, whose only orders there are 7 and 14, reaches 1.105229. That is exact on the turning side: the verifier counts every sign choice in its order-7 family. The turning wheel wins at 11, 17, 19, 23 and 29 |
| Y2 | held | the turning search reaches the winner at 17 (orders 3 and 6), 19 (order 4) and 29 (orders 5 and 10) |
| Y3 | held | no family goes above a winner found so far |

**What the death teaches.** The test compared the best of each wheel, and a small order fixes a large family: its
eigenspaces have dimension about p/m. So the test mostly measured which wheel offers a small order. At 13 the turning
wheel offers only 7 and 14, against the multiplying wheel's 3, 4, 6 and 12; at 23 it is the other way round. The
death at 13 is not a search's miss. [`verify_seven_levels.py`](verify_seven_levels.py) counts every sign choice
constant on the 25 orbits of the turning wheel's order 7, 2^25 in each eigenspace, and finds 1.105229 the best.

**Read after the run** (post hoc, not registered). The logs already hold 14 pairs of families of equal size, one on
each wheel, whose largest eigenspaces have the same dimension. The turning wheel wins 12 of them. It loses two:
- at 13 in dimension 2 (order 7 against order 12), by 0.010;
- at 19 in dimension 4 (order 5 against order 6), by 0.040.

So at equal size a turning symmetry is usually the better one, not always. At 7 and 19 the turning wheel's order-4
family also beat the multiplying wheel's larger order-3 family. The dead prediction is kept in
[`../../GRAVEYARD.md`](../../GRAVEYARD.md).

---

## Round 9: many wheels (registered 2026-11-09, before its full run; its pilots were seen first)

> *you are only spinning one wheel... imagine a 10x10 of wheels or larger?* — the author, 9 November 2026

**Made exact.**
- One wheel is one p-level system, the setting of rounds 1 to 8.
- An array of n wheels is n of them side by side. Its dimension is D = p^n, and its phase space has D² points.
  Each point's operator is the product of the wheels' operators.
  - So a product state's Wigner function is the product of the wheels' Wigner functions, and the sum of its sizes
    multiplies.
- The array's half turn is every wheel's half turn at once, the operator at the origin. The coin is even or odd under
  it, as before. The ceiling is (√D − 1)/2.
- Clifford operations keep the negativity and can entangle wheels, so an entangled state can carry exactly a
  product's value. The test that entanglement pays is to beat every product.

**Forced, before any search: the 10 × 10 array.** Computed by [`many_wheels.py`](many_wheels.py) `combine`.
- The best single-wheel state, repeated on every wheel, reaches a fraction fⁿ of the ceiling √D on the sum of sizes:
  f = 0.962 at 3 levels, 0.945 at 5 and 0.932 at 7.
- The average random state reaches √D · E|2B − 1|, with B ~ Beta((D + 1)/2, (D − 1)/2). That is exact, because
  each point's operator has (D + 1)/2 eigenvalues +1 and (D − 1)/2 eigenvalues −1. It falls from 0.866 at one
  wheel of 3 levels towards √(2/π) = 0.798.
- So the average random state beats the best product from 6 wheels on at 3 levels, and from 4 wheels on at 5 and 7.
- At 100 wheels the products reach 0.021, 0.0035 and 0.00085 of the ceiling; the average random state reaches 0.798.
- The best states of a 10 × 10 array are not built wheel by wheel, and not any Clifford image of such a product.

**Literature.**
- Liu and Winter (PRX Quantum 3, 020333, 2022) prove that typical many-qubit states are nearly maximally magic, for
  a range of measures.
- Knipfer, Roman, Matcheva and Matchev (arXiv:2607.07197, July 2026) use a different measure, the stabilizer Rényi
  entropy M₂. They find the two-qutrit maximum ln(81/17), a numerical peak ln(625/49) at two wheels of 5, and
  conjecture ln[d⁴/(2d² − 1)] for two wheels of any prime d.
- No maximum of the total Wigner negativity for two or more qudits was found.

**Pilots, seen before this registration.** While timing the machinery, short searches ran at every size below and
printed their values. They were meant as timing tests, and that was a mistake: they are pilots, so these sizes can
no longer be predicted fresh. The table gives the higher of the two pilot runs.

| array | pilot climbs per search | even | odd | whole |
|---|---|---|---|---|
| two wheels of 3 | 1 000 and 20 000 | 0.888889 | 0.888889 | 0.888889 |
| three wheels of 3 | 500 and 4 000 | 1.875593 | 1.886964 | 1.886964 |
| four wheels of 3 | 20 | 3.629630 (98/27) | 3.459175 | 3.278927 |
| two wheels of 5 | 500 and 4 000 | 1.766937 | 1.727386 | 1.732350 |
| two wheels of 7 | 200 and 1 000 | 2.718663 | 2.616966 | 2.573386 |

- Also seen: the best two-wheel states of 3 levels had purity below 1 on each wheel (0.68 and 0.5), and M₂ 1.461
  and 1.386, below Knipfer et al.'s 1.561. At four wheels of 3, the purities were 0.36 to 0.40 and M₂ 3.38 to 3.43.
- At 31, round 7's prime, a timing test of 2 000 climbs per side printed even 2.040380 and odd 2.017126. Round 7's
  predictions were registered at de3719d, so this changes nothing there. Its run of two million climbs per side decides.
- Not seen, only counted: whether the best two-wheel states of 3 levels have a product's Wigner values, and M₂ at two
  wheels of 5 and of 7.

**The test.** [`many_wheels.py`](many_wheels.py) is committed with this registration. It runs the sign ascent on the
even side, the odd side and the whole space, at 50 to 500 times the pilot's effort:

| array | climbs: even, odd, whole |
|---|---|
| one wheel of 3 and of 5 | 100 000 each |
| one wheel of 7 | 200 000, 200 000, 50 000 |
| two wheels of 3 | 1 000 000 each |
| three wheels of 3; two wheels of 5 | 500 000, 500 000, 100 000 |
| four wheels of 3 | 10 000, 10 000, 1 000 |
| two wheels of 7 | 200 000, 200 000, 20 000 |

Z0 to Z5 check whether the pilot's picture holds. Z6 and Z7 are fresh.

**Z0. (Calibration.)** One wheel reproduces the known bests: 1/3 on both sides at 3; 0.556677 even and 0.433070 odd
at 5; 0.732522 even and 0.728262 odd at 7.

**Z1. (Pilot.)** Two wheels of 3: nothing beats 8/9, the value of a product of two single-wheel bests.
*Kill:* a higher state.

**Z2. (Pilot.)** At three and four wheels of 3, two of 5 and two of 7, the best state beats every product of smaller
arrays' bests. *Kill:* an array where it doesn't.

**Z3. (Pilot.)** The pilot's coin holds: odd at three wheels of 3; even at four of 3, two of 5 and two of 7.
*Kill:* any side changes.

**Z4. (Pilot.)** Every best state from two wheels on reaches 88% of its ceiling. *Kill:* one below.

**Z5. (Pilot.)** Four wheels of 3: the best is 98/27, and nothing higher is found. *Kill:* a higher state.

**Z6. (Fresh.)** Two wheels of 3: every best state found has the Wigner values of a product of single-wheel bests, as
a Clifford image of a product would. *Kill:* a best state whose values are no product's.

**Z7. (Fresh.)** Two wheels of 5 and of 7: every best state found has M₂ below Knipfer et al.'s values, ln(625/49)
and ln(2401/97). *Kill:* one at or above them. A state above ln(2401/97) would also break their conjecture.

**What stays open.** The arrays nobody has run yet, such as three wheels of 5 (D = 125) or five of 3 (D = 243), need
code that never writes out all D² operators. Their predictions will be registered before any run, and their timing
done without printing a value.

**Expected standing.** The forced numbers are exact arithmetic on the best single-wheel states found. The searches
are reading-level evidence in small arrays. The 10 × 10 array itself stays out of reach of any search.

---

## Round 7 scores (added after the run, 2026-11-10)

Run by [`round7.py`](round7.py), committed at ad00f5a before its run; the output is kept in
[`round7_thirtyone.log`](round7_thirtyone.log) and [`round7_combined.log`](round7_combined.log). The run is seeded.
**The author's 7-wheel died at 31.**

| | outcome | evidence |
|---|---|---|
| X1, the author's 7-wheel | **died** | at 31 the 7-wheel has period 15 and never reaches the half turn, so the rule called the odd side. The even side wins, 2.045297 against 2.031473 |
| X2, the rival observation | **stands at 31** | the even side wins at 31, as it said. 37 was not run: with X1 dead, it no longer decides between them |

**The pilot.** A timing test of 2 000 climbs per side ran after this registration and before the full run. It
printed even 2.040380 and odd 2.017126, and round 9's registration discloses it. The full run found both sides
higher, in the same order.

**Recheck, not registered.** Two million more odd climbs with a fresh seed, and kicks from the ten highest odd tops,
found the same odd best, 2.031473, once again, and nothing higher. The odd side falls short of the even best
by 0.0138. Both searches reached that odd best only once, so its basin is tiny.

**Read after the run.**
- With 31's even win, no number wheel of any base from 2 to 30 fits every decided prime. Before 31, only 7 did.
- The rival observation fits all nine decided primes, but it rests on two odd wins, at 19 and 29.

**Yield.** The rule fitted the eight primes it was read from and missed the first prime it predicted. It is kept in
[`../../GRAVEYARD.md`](../../GRAVEYARD.md), and the [README](README.md) §10 has what the run found.

---

## Round 9 scores (added after the run, 2026-11-10)

Run by [`many_wheels.py`](many_wheels.py), committed with this registration at ad00f5a, before the full run; the
output is kept in [`many_wheels_three.log`](many_wheels_three.log), [`many_wheels_four.log`](many_wheels_four.log),
[`many_wheels_five.log`](many_wheels_five.log), [`many_wheels_seven.log`](many_wheels_seven.log) and
[`many_wheels_combined.log`](many_wheels_combined.log). The runs are seeded. **All eight held.** Z0 to Z5 only checked
what the pilots had shown, at 50 to 500 times their effort; Z6 and Z7 were fresh.

| | outcome | evidence |
|---|---|---|
| Z0, calibration | held | one wheel: 1/3 on both sides at 3; 0.556677 and 0.433070 at 5; 0.732522 and 0.728262 at 7 |
| Z1, pilot | held | two wheels of 3: 8/9 on the even side, the odd side and in the whole space, a million climbs each, and nothing higher |
| Z2, pilot | held | the best beats every product of smaller arrays' bests: 17/9 against 49/27 at three wheels of 3, 98/27 against 3.478273 at four, 1.766937 against 1.733134 at two of 5, and 2.719253 against 2.538221 at two of 7 |
| Z3, pilot | held | the odd side at three wheels of 3 (1.886964 against 1.875593); the even side at four of 3 (98/27 against 3.476833), two of 5 (1.766937 against 1.727386) and two of 7 (2.719253 against 2.633836) |
| Z4, pilot | held | the best states reach 88.4% (two of 5) to 90.7% (four of 3) of their ceilings |
| Z5, pilot | held | four wheels of 3: 98/27, reached 1 558 times in 10 000 even climbs, and nothing higher |
| Z6, fresh | held | two wheels of 3: every best state found has the Wigner values of a product of single-wheel bests (even with even, or even with odd), yet each is entangled: each wheel's purity is 0.625 or 0.5 |
| Z7, fresh | held | M₂ of the best states: 2.24 to 2.33 at two wheels of 5, against Knipfer et al.'s 2.546; 2.89 to 3.02 at two of 7, against their 3.209 |

**Read after the run.**
- **Three wheels of 3: the best state found is on neither face.** The whole-space search found 17/9, above both
  sides' bests, at half-turn value −1/9. A second whole-space search of 200 000 climbs with a fresh seed found 17/9
  again, 11 times, and nothing higher.
  - No phase-point operator has it as an eigenstate: |⟨A_u⟩| is at most 4/9 at every point, so it is not even or odd
    about any centre.
  - It is the **norm state** of the field with 27 elements, up to a Clifford operation: ψ = Σ ω^N(x) |x⟩ / √27, where
    x runs over the field, ω = e^(2πi/3), and N(x) = x·x³·x⁹ is the field's norm, which lies in the three-element
    field. [`edge_state.py`](edge_state.py) reruns the search and finds an explicit Clifford operation for each best
    state; its output is in [`edge_state.log`](edge_state.log).
  - Exact facts about it, checked by the verifier: its Wigner function takes three values, 2/243, −1/243 and −4/243,
    at 351, 351 and 27 points, so its negativity is exactly 17/9. It has 1 053 Clifford symmetries. Its M₂ is ln(729/53).
  - The half turn sends it to its complex conjugate. Its odd part, with weight 13/18, is the field's Legendre state:
    the quadratic character of the 27-element field, as amplitudes. Its even part, with weight 5/18, is |0⟩ minus half
    of every other basis state.
- Z2 compared each side's best. With 17/9, the best product at four wheels is 94/27 = 3.481481, still below 98/27.
- The whole-space searches at four wheels of 3, two of 5 and two of 7 had a tenth or less of the side searches'
  climbs and found less than the even side, so they cannot say whether a state on neither face wins there.
- **Four wheels of 3:** the best found, 98/27, is even. Its structure is open.
- **The field's other states do not reach the other bests** (checked after the run; the verifier checks them): the
  norm states at two wheels are stabilizer states; at four wheels of 3 the norm state gives 2000/729 ≈ 2.743; and the
  states of the field's multiplicative characters stay below every array's best (at most 0.807, 1.741, 3.433, 1.662
  and 2.576 at two, three and four wheels of 3, and two of 5 and of 7).

**Yield.** Mostly confirmation: the pilots' picture held at 50 to 500 times the effort. The forced numbers are exact.
New as far as we checked: the small arrays' best values, which are search results, not proofs; and one exact state,
the norm state at three wheels of 3, the best found there and on neither face. The web searches of 2026-11-10 found no
maximum of the total Wigner negativity for three or more qutrits, and no use of this state as a magic state.

---

## Round 10: the larger arrays (registered 2026-11-10, before any run)

> *you are only spinning one wheel... imagine a 10x10 of wheels or larger?* — the author, 9 November 2026

Round 9 left the larger arrays open: they need code that never writes out all D² operators. This round runs three of
them: three wheels of 5 (D = 125), five wheels of 3 (D = 243) and three wheels of 7 (D = 343).

**Made exact, before the run.**
- **The new code.** For a state ψ on n wheels of p levels, W(q, k) = (1/D) Σ_s ψ̄(q + s) ψ(q − s) ω^(2k·s), so for
  each q the Wigner function is one Fourier transform. The sign matrix Σ_u s_u A_u / D is the same transform of the
  signs, read at ((a + b)/2, a − b). A state on one side has W(−u) = W(u), so half the phase space suffices.
  - Checked before this registration against round 3's code on arrays already run: from all 1 680 starts, every climb
    ends at the same value ([`larger_arrays_calibrate.log`](larger_arrays_calibrate.log)).
  - The timing printed no values, following round 9's lesson. One climb takes 0.15 to 0.3 s on three wheels of 5;
    1.5 s on a side and 5.5 s in the whole space on five of 3; and 3 s and 11.5 s on three of 7.
- **The norm-type states.** For the field with q = pⁿ elements, ψ_c = Σ_x ω^(c·N(x)) |x⟩ / √q for c = 1, …, p − 1,
  where N is the field's norm to F_p. ψ₋c is ψ_c's complex conjugate, with the same values. Round 9's winner on three
  wheels of 3 is ψ₁ there, up to a Clifford operation.
- **A theorem, proved here; the verifier will check it at 3, 5 and 7.** On three wheels of any odd prime p, every
  norm-type state has expectation zero on the Z-type Weyl operators (a Lagrangian) and size exactly 1/√(p³) on every
  other one. It is even or odd about no centre, so it is on neither face, and the half turn sends it to its complex
  conjugate.
  - Proof. ⟨ψ|Z^b X^a|ψ⟩ is a character sum of N(x + a) − N(x). For a ≠ 0 its degree-2 part is the quadratic form
    Tr(a^(p²) x^(p+1)), whose polar form is Tr(y (a^p x^(p²) + a^(p²) x^p)).
  - That form is degenerate only if z^(p−1) = −1 for some z in the field. Then the order of z would divide 2(p − 1)
    but not p − 1, and that is impossible, since 2(p − 1) and p³ − 1 share only p − 1 (p² + p + 1 is odd).
  - A nondegenerate quadratic character sum over F_p³ has size p^(3/2). For a = 0 the sum vanishes unless b = 0.
  - About a centre q, the state is even or odd only if N(q + x) − N(q − x) is linear in x. But that difference is
    2N(x) plus a linear term, and N is not linear. And N(−x) = (−1)^(p² + p + 1) N(x) = −N(x), so the half turn
    sends the state to its complex conjugate.
  - So the flatness of round 9's winner is not an accident of p = 3. On five wheels the norm has degree 5, its
    differences are not quadratic, and the argument fails. On four wheels the norm state is even and fell short
    (2000/729 against 98/27).
- **Not computed before this registration:** any norm-type state's negativity on the new arrays, and any search value
  there.

**Predictions.** V0 is a calibration, already done. V1 to V6 are fresh.

**V0. (Calibration, done.)** The structured code ends where round 3's does, from all 1 680 starts, and it
reproduces the known norm states: 17/9 on three wheels of 3, 2000/729 on four, and 0 on two of 5.

**V1. (Fresh.)** On three wheels of 5 and of 7, nothing found beats the best norm-type state. That covers every climb:
from random states on either side and in the whole space, from the norm-type states themselves, and from their kicks.
*Kill:* a higher state.

**V2. (Fresh.)** On three wheels of 5 and of 7, the best norm-type state beats both sides' bests. So the winner sits on
the edge, as on three wheels of 3. *Kill:* a side's best at or above it.

**V3. (Fresh.)** On five wheels of 3, the norm state does not win: some climb beats it. *Kill:* nothing found above it.

**V4. (Fresh.)** Every new array's best beats every product of smaller arrays' bests (round 9's). The bars are
4.290842 on three wheels of 5 (two of 5 with one of 5), 517/81 = 6.382716 on five of 3 (four of 3 with one) and
7.435601 on three of 7 (two of 7 with one). *Kill:* an array where it doesn't.

**V5. (Fresh; Claude's reading, on thin ground.)** From two wheels on, the coin follows the number of wheels: with an
odd number the odd side wins. So the odd side wins on three wheels of 5, five of 3 and three of 7.
- It rests on one array: three wheels of 3 went odd. The three arrays with an even number of wheels (four of 3, two of
  5, two of 7) went even.
- Single wheels do not follow it: the even side wins at most primes.

*Kill:* the even side wins on any new array.

**V6. (Fresh.)** Every new array's best reaches 88% of its ceiling, as every array from two wheels on did in round 9
(Z4). The marks are 4.479350, 6.418921 and 7.708914. *Kill:* one below.

**The test.** [`larger_arrays.py`](larger_arrays.py) is committed with this registration. The run is seeded.

| array | D | climbs: even, odd, whole | kicks of each norm-type state, at each size |
|---|---|---|---|
| three wheels of 5 | 125 | 40 000, 40 000, 10 000 | 500, for c = 1 and 2 |
| five wheels of 3 | 243 | 4 000, 4 000, 800 | 100, for c = 1 |
| three wheels of 7 | 343 | 2 000, 2 000, 400 | 50, for c = 1, 2 and 3 |

- The searches are shorter than round 9's, because a climb here costs 10 to 100 times as much.
- A kick is a norm-type state plus a random vector of relative size 0.05 or 0.3. It climbs in the whole space.
  Together with the climb from the norm-type state itself, the kicks test whether a higher state sits nearby.
- The run takes about three hours on six worker processes at below-normal priority, one thread each.

**Not run.** Six wheels of 3 (D = 729): a climb would take about half a minute on a side, too long for a search that
says much. Round 9's forced numbers already settle the large arrays.

**Expected standing.** The norm-type states' values will be exact. The searches are reading-level evidence, shorter
than round 9's. A held V1 says only that nothing better was found.
