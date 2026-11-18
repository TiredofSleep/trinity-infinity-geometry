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

---

## Round 10 scores (added after the run, 2026-11-10)

Run by [`larger_arrays.py`](larger_arrays.py), committed with this registration at df9a004, before any run; the output
is kept in [`larger_arrays_run.log`](larger_arrays_run.log) and [`larger_arrays_combined.log`](larger_arrays_combined.log).
The run is seeded and took 2.8 hours. **Two of seven held: V0 and V3.** V1 and V2 held at three wheels of 7 and died
at three of 5. V4 died at five of 3, and V5 and V6 died at two arrays each. (Round 5 also named its predictions V;
these are round 10's.)

| | outcome | evidence |
|---|---|---|
| V0, calibration | held | done before the registration: from all 1 680 starts the climbs end where round 3's code ends |
| V1 | **died at three of 5; held at three of 7** | three of 5: a climb from a kicked norm-type state reached 4.301387, and both sides' bests (4.293476 even, 4.291598 odd) beat the norm-type states' 4.252724. Three of 7: nothing found beats the norm-type states' 7.902228, and all 300 kicks of them climbed back to it |
| V2 | **died at three of 5; held at three of 7** | three of 5: both sides' bests are above 4.252724. Three of 7: 7.902228 against 7.238233 (even) and 7.241590 (odd) |
| V3 | held | five of 3: the norm state has 4232/729 = 5.805213. The climb from it ends at 6.052266, and the even side's best is 6.082020 |
| V4 | **died at five of 3** | the best found there, 6.082020, is below 517/81 = 6.382716, the four-wheel best times a one-wheel best. It held at three of 5 (4.301387 against 4.290842) and at three of 7 (7.902228 against 7.435601) |
| V5 | **died** | the even side won at three of 5 (4.293476 against 4.291598) and at five of 3 (6.082020 against 6.069252); the odd side won at three of 7 (7.241590 against 7.238233) |
| V6 | **died at three of 5 and five of 3** | the best found reaches 84.5% of the ceiling at three of 5 and 83.4% at five of 3; at three of 7, 90.2% |

**Disclosed.**
- The registration's timing printed no values. A smoke test of the code ran only on arrays already run (three and four
  wheels of 3, two of 5); its scores mean nothing and its logs are not kept.
- The six workers were meant to run at below-normal priority, but the call that sets it fails silently on 64-bit
  Windows, and every script in the repository that sets it had the same fault, 17 in all. The workers ran at normal
  priority until they were lowered by hand partway through the run. No value depends on it. The call is fixed in a
  separate commit.

**Derived during the run, after the registration, so not a prediction: the norm-type states' Wigner values are
Kloosterman sums.** On three wheels of p, each norm-type state takes the value K(m)/p⁵ at (p² + p + 1)p³ points for
each nonzero m in F_p, and −(p + 1)/p⁵ at the other p³ points. Here K(m) = Σ_a ω^(a + m/a), over the nonzero a in F_p,
is the Kloosterman sum.
- So its negativity is exact at every p: the sum of sizes is [(p + 1) + (p² + p + 1) Σ_m |K(m)|]/p². That gives 17/9
  at 3, 4.252724 at 5 and 7.902228 at 7, the values the run logged.
- The route: Davenport and Hasse's theorem turns the Gauss sum of a character composed with the norm into the cube of
  the character's Gauss sum over F_p, and summing squared Gauss sums over the characters gives a Kloosterman sum.
- Before the run ended it showed that V1 and V2 would die at three of 5: 4.252724 is below the product bar 4.290842,
  and the product is itself a state of the array.
- Its share of the ceiling tends to 8/(3π) = 0.849 as p grows (the mean over the primes from 1 000 to 2 000 is
  0.8489), because the Kloosterman angles follow the Sato–Tate law (Katz). Below 2 000 only 3 and 7 reach 90%, and 7
  reaches the most, 90.2%.
- [`flat_states.py`](flat_states.py) checks it at 3, 5 and 7 and tabulates it to 1 999; the verifier checks it too.
  The full proof, written out after the scoring, is in [`NORM_STATE.md`](NORM_STATE.md), with its own checks.

**Read after the run** ([`flat_states.py`](flat_states.py) and [`product_climbs.py`](product_climbs.py); the output is
in [`flat_states.log`](flat_states.log) and [`product_climbs.log`](product_climbs.log)):
- **Other flat states fall at or below the norm-type states.** Of the states ω^(Tr(a x³) + b N(x)) on three wheels,
  128 of 624 are flat at 5 and 804 of 2 400 at 7. At both, the best flat value is the norm-type states'. Alltop's cubic
  phase states (b = 0) reach 4.057183 and 7.458638. The 702 Galois-ring states on three qutrits, as we reconstructed
  Damski et al.'s construction, are all flat, at 1.738433, below 17/9.
- **On three wheels of 5 the best state found is on neither face either.** The kick that found 4.301387, rerun, gives
  a state with half-turn value −0.229 and largest |⟨A_u⟩| 0.255, so no point's operator has it as an eigenstate. Its
  overlap with the norm-type state it was kicked from is 0.956: it is that state reshaped. It is not flat, and it is
  entangled: each wheel's purity is about 0.23, against 0.2 for a fully mixed wheel.
  - So V2 died as registered, but its consequence, "the winner sits on the edge", holds on all three arrays of three
    wheels tried: at 3 and 7 the norm state, at 5 a state near one.
- **The searches fell short on the two largest arrays.** Every product of two smaller arrays' best states was formed
  and climbed from:
  - each product is a fixed point of the climb, on its side and in the whole space. Every kick of the best one on
    each side (20 at each of the sizes 0.05 and 0.3, on the side and in the whole space) climbed back to it or lower;
  - five wheels of 3: the best known state is 517/81 = 6.382716, on both sides: the four-wheel best times an even or an
    odd one-wheel best. The random climbs, 4 000 on each side, ended 0.30 below it, and the climb from the norm state
    stops at 6.052266. So V4's death there is the search's;
  - three wheels of 7: the products reach 7.435601 (even) and 7.408174 (odd), above both sides' searches but far below
    the norm state's 7.902228, which still wins;
  - so the coin as scored rests on searches that fell short. Read with the known states, the sides tie at five of 3
    (517/81 each), and at three of 7 the even side leads (7.435601 against 7.408174), behind the norm state.
- **A correction to round 9.** Finding round 9's best states again, the seeded odd climbs on four wheels of 3 reached
  3.533331, above the 3.476833 that round 9 logged for the odd side, found once in its 10 000 climbs. The operators'
  contraction confirms the value. The even side's 98/27 stays ahead, so round 9's Z3 still holds. On two wheels of 7
  the odd climbs did not find round 9's odd best again in 80 000 climbs; round 9 found it 7 times in 200 000.

**Yield.**
- Exact, and new as far as we checked: on three wheels of every odd prime the norm-type states are flat, and their
  Wigner values are Kloosterman sums, so their negativity is known in closed form at every p.
- Searches: the norm state wins on three wheels of 7, at 90.2% of the ceiling. On three wheels of 5 a reshaped
  norm-type state wins, also on neither face. On five wheels of 3 the best known state is a product.
- A lesson: at 243 and 343 levels random climbs stop short of states already known. A search there must also start
  from them: the products, and the field's own states.
- Literature: the flat profile is known (Damski, Bistroń, Ponterio, Czartowski and Życzkowski 2026: fiducials of
  product Weyl–Heisenberg mutually unbiased bases), and so is Alltop's construction. The norm construction and its
  Kloosterman values were not found. The dead predictions are kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md), and
  the [README](README.md) §12 has what the run found.

---

## Round 11: the oscillator states (registered 2026-11-13, before any run)

> *zoom out, and look for work that shares ground, let's see if what we have is useful* — the author, 12 November 2026

Zooming out found that round 8's two wheels are the two kinds of maximal torus in SL(2, p): the multiplying wheel is
the split torus and the turning wheel the non-split one. Their eigenvectors are the oscillator system of Gurevich,
Hadani and Sochen, used for radar sequences, and the Hecke eigenfunctions of the quantized cat map. In that
literature the Wigner functions of such states are Kloosterman-type sums with Sato–Tate statistics, but we found no
measurement of their magic. Round 8 measured the best state of each family up to 29. This round measures every one
of them, at every prime up to 401.

**Made exact, before the run.**
- **The states.** At each prime p:
  - the split torus's one-line states are the p − 2 character states Σ_x χ(x) |x⟩ / √(p − 1), over the nonzero x, for
    the nontrivial characters χ of F_p*. The trivial character's eigenspace also holds |0⟩, has two dimensions, and is
    left out;
  - the non-split torus's one-line states are the p eigenvectors of the chirp U = Σ ω^((t/4)(x² + y²) − xy) |x⟩⟨y| / √p,
    a Clifford unitary whose symplectic map, [[t/2, 1], [t²/4 − 1, t/2]], has order p + 1 for a suitable t. The script
    checks U's action on X and Z, and the order.
  - Checked before this registration ([`oscillator_states_calibrate.log`](oscillator_states_calibrate.log)): the best
    non-split state equals round 8's logged value at every prime from 5 to 29, and the split state of the character of
    order 2 is the Legendre state, with its known value at 7, 17, 19, 23, 29 and 31.
- **Orbits.** A torus fixes each of its eigenvectors up to a phase, so their Wigner functions are constant on the
  torus's orbits in phase space: p − 1 circles of p + 1 points for the non-split torus, and p − 1 hyperbolas and two
  axes of p − 1 points for the split one. So each state's Wigner function takes at most p + 2 values; the script checks
  it.
- **An identity that turns the share into a statistic** [FORCED]. For a pure state on p levels, Σ_u W(u)² = 1/p, so the
  root mean square of W over the p² points is exactly p^(−3/2). The sum of sizes S is p² times the mean |W|, so
  S/√p = mean |W| / rms W. That depends only on the shape of the distribution of values.
  - If the values are Sato–Tate distributed (proportional to cos θ, with density (2/π) sin²θ), S/√p tends to
    8/(3π) = 0.8488. If they are Gaussian, as for an average random state, √(2/π) = 0.7979. If the angle θ is uniform,
    2√2/π = 0.9003.
  - The ratio μ4/μ2² of the fourth moment to the squared second separates the same three: 2, 3 and 1.5.
  - Round 10's norm states have S/√p tending to 8/(3π), because their values are Kloosterman sums.
- **The timing printed no values.** The whole run, 77 primes, takes about six minutes.
- **Not computed before this registration:** any oscillator state's value beyond round 8's logged family bests and the
  Legendre states, and any S/√p or moment ratio.

**Predictions.** O0 is a calibration, already done. O1 to O4 are fresh.

**O0. (Calibration, done.)** The code reproduces round 8's turning-wheel bests from 5 to 29 and the Legendre states
from 7 to 31; and in the run, at every prime, the chirp's checks hold and every state's Wigner function takes at most
p + 2 values. *Kill:* a mismatch or a failed check.

**O1. (Fresh; the Sato–Tate reading.)** At the primes from 211 to 401, the mean S/√p over all the one-line oscillator
states is within 0.01 of 8/(3π) = 0.8488. It rests on Gurevich and Hadani's reduction of these Wigner functions to
Kloosterman-type sums, on Katz's Sato–Tate law for such sums, and on round 10, where it is exact. *Kill:* a mean
outside 0.8388 to 0.8588.

**O2. (Fresh.)** At the same primes, the mean of μ4/μ2² over the Wigner values off the origin is within 0.1 of 2.
*Kill:* a mean outside 1.9 to 2.1.

**O3. (Fresh; Claude's reading, on thin ground.)** The non-split torus's best one-line state beats the split torus's at
more than three quarters of the primes from 5 to 401. It rests on round 8, where the turning wheel won 12 of 14 pairs
of families of equal size. *Kill:* three quarters or fewer.

**O4. (Fresh.)** From 37 to 401, no one-line oscillator state reaches 90% of the ceiling. Round 8's best ones reach
85 to 88% from 7 to 29, and every best state found by search from 7 to 31 sits at 89 to 90%. *Kill:* one at 90% or
more.

A check, not a prediction: no one-line oscillator state beats the best state known at its prime, from 7 to 31.

**The test.** [`oscillator_states.py`](oscillator_states.py) is committed with this registration. Every state is
computed exactly; there is no search. One process at below-normal priority, about six minutes.

**Expected standing.** The values are exact up to rounding. O1 and O2 test the shape of the distribution of values, so
a held O1 supports the Sato–Tate reading without proving it, and a dead one says these states follow another law.

---

## Round 11 scores (added after the run, 2026-11-13)

Run by [`oscillator_states.py`](oscillator_states.py), committed with this registration at 938e13d, before the run;
the output is kept in [`oscillator_states_run.log`](oscillator_states_run.log) and
[`oscillator_states_combined.log`](oscillator_states_combined.log). It took 6.6 minutes, and every value in it is
exact up to rounding. **All five held.**

| | outcome | evidence |
|---|---|---|
| O0, calibration | held | round 8's turning-wheel bests and the Legendre states again; at all 77 primes the chirp is unitary, its map has order p + 1, and every state's Wigner function takes at most p + 2 values |
| O1 | held | at the primes from 211 to 401, the 20 056 one-line states have mean S/√p = 0.846813, against Sato–Tate's 0.848826; a Gaussian law would give 0.797885 and a uniform angle 0.900316 |
| O2 | held | their mean μ4/μ2² is 2.0032, against Sato–Tate's 2; a Gaussian law would give 3 and a uniform angle 1.5 |
| O3 | held | the non-split torus's best beats the split torus's at 65 of the 77 primes (84%). It loses at 7, 73, 79, 107, 139, 157, 193, 199, 223, 229, 271 and 283 |
| O4 | held | from 37 to 401 the best one-line state reaches at most 88.2% of the ceiling (at 41); from about 100 on, 85.6 to 86.8% |

The check held too: no one-line oscillator state beats the best state known at any prime from 7 to 31.

**Read after the run.**
- **The two tori approach Sato–Tate differently.** At the primes from 211 to 401 the non-split states' mean S/√p is
  0.8483, which is Sato–Tate's value once the finite size is allowed for (0.8471 to 0.8479). The split states' mean is
  0.8452, rising from 0.81 to 0.83 at small primes: their two axes carry tiny Wigner values, a correction of order 1/p.
- **An exact identity.** Averaged over the non-split torus's p eigenvectors, μ4/μ2² is exactly 2p/(p + 1), to within
  4 × 10⁻¹⁶ at the 43 primes tested from 5 to 401. State by state it varies (from 1.68 to 2.26 at 31). The route to a
  proof: averaging a phase-point operator over the torus gives an operator diagonal in that eigenbasis, so the average
  fourth moment is a trace of fourth powers, a count over the torus's circles. The proof is not written.
- **The states are close to one another.** At each prime, the spread of S/√p across the states is about 0.14/√p:
  0.007 at 401. So no oscillator state stands out, and the best of them settles near 86% of the ceiling, between the
  average random state (79.8%) and the best states found by search at 7 to 31 (89 to 90%).
- **No coin.** The best oscillator state is even at 42 primes and odd at 35, with no pattern by p modulo 4.

**Yield.** The values are exact; the predictions were registered first and all five held. What it adds is
measurement: the magic of the oscillator states follows the Sato–Tate law, the same law as round 10's norm state, and
these states are good but not the best. The mechanism, Kloosterman-type sums, is Gurevich and Hadani's; the reading
as magic, and the identity above, were not found in the literature checked. The [README](README.md) §13 has the
summary.

---

## Round 12: the higher moments (registered 2026-11-13, before any run)

> *write the proof and test the higher moments* — the author, 13 November 2026

Round 11 found the oscillator states' Wigner values following the Sato–Tate law in two statistics, S/√p and the
fourth-moment ratio. Two statistics do not fix a law. This round tests the rest of its shape.

**Made exact, before the run.**
- **What Sato–Tate predicts.** Scaled to variance 1, Sato–Tate values follow the semicircle law on [−2, 2]: the odd
  moments vanish and the even ones are the Catalan numbers 1, 2, 5, 14. The rivals:

  | law | 4th | 6th | 8th |
  |---|---|---|---|
  | semicircle (Sato–Tate) | 2 | 5 | 14 |
  | Gaussian (the average random state) | 3 | 15 | 105 |
  | arcsine (a uniform angle) | 1.5 | 2.5 | 4.375 |
  | the sum of two independent semicircles | 2.5 | 8.75 | 36.75 |

  The last is the kind of law Kurlberg and Rudnick conjectured for some matrix elements of Hecke states. In Kolmogorov
  distance the semicircle lies 0.041 from the Gaussian and 0.091 from the arcsine law (computed from the formulas, not
  from data).
- **Standardizing.** Each state's Wigner values off the origin are centered and scaled to variance 1. That removes the
  small mean, about 1/√p in these units, that Σ W = 1 forces.
- **The proof of round 11's identity**, written alongside this round, reduces every even moment of the raw values,
  averaged over the non-split eigenbasis, to a trace of a power of a torus-averaged phase-point operator. So those
  averages are exact numbers at each prime, with no sampling noise.
- **Checked before this registration** ([`torus_moments_calibrate.log`](torus_moments_calibrate.log)): the script
  reproduces round 11's logged fourth-moment ratios, both tori, at every prime from 5 to 61, and the identity
  2p/(p + 1).
- **The timing printed no values.** The run takes about ten minutes.
- **Not computed before this registration:** any third, sixth or eighth moment, and any Kolmogorov distance of the data.

**Predictions.** M0 is a calibration; M1 to M5 are fresh. The script is [`torus_moments.py`](torus_moments.py), committed
with this registration; it uses round 11's states.

**M0. (Calibration.)** The run reproduces round 11's mean raw fourth-moment ratio at every prime and torus, and the
identity 2p/(p + 1) at every prime. *Kill:* a mismatch.

**M1. (Fresh.)** At the primes from 211 to 401, the mean standardized third moment over all one-line states is within
0.1 of 0. *Kill:* outside −0.1 to 0.1.

**M2. (Fresh.)** The mean standardized sixth moment is within 0.3 of 5. *Kill:* outside 4.7 to 5.3.

**M3. (Fresh.)** The mean standardized eighth moment is within 1.5 of 14. *Kill:* outside 12.5 to 15.5.

**M4. (Fresh.)** At every prime from 211 to 401, the non-split eigenbasis's averages of the standardized sixth and
eighth moments are within 0.3 of 5 and 1.5 of 14. *Kill:* one prime outside.

**M5. (Fresh.)** All the standardized values at the primes from 211 to 401, pooled, lie within Kolmogorov distance
0.015 of the semicircle law. *Kill:* 0.015 or more.

**Expected standing.** The values are exact up to rounding. Holding all of these would say the whole distribution,
not just two statistics, is Sato–Tate's at these sizes; it would still not be a proof.

---

## Round 12 scores (added after the run, 2026-11-13)

Run by [`torus_moments.py`](torus_moments.py), committed with this registration at a959a20, before the run; the output
is kept in [`torus_moments_run.log`](torus_moments_run.log) and [`torus_moments_combined.log`](torus_moments_combined.log).
It took 10.9 minutes, and its values are exact up to rounding. **All six held.**

| | outcome | evidence |
|---|---|---|
| M0, calibration | held | round 11's mean raw fourth-moment ratio at every prime and torus, and 2p/(p + 1) at every prime |
| M1 | held | the mean standardized third moment at 211 to 401 is −0.0566 |
| M2 | held | the mean sixth moment is 5.0655, against the semicircle's 5 (Gaussian 15, arcsine 2.5, two semicircles 8.75) |
| M3 | held | the mean eighth moment is 14.350, against 14 (Gaussian 105, arcsine 4.375, two semicircles 36.75) |
| M4 | held | the non-split basis averages run from 5.0077 to 5.0239 (sixth) and from 14.070 to 14.203 (eighth) at every prime from 211 to 401 |
| M5 | held | the 2 062 782 912 pooled standardized values lie at Kolmogorov distance 0.0072 from the semicircle, 0.0426 from the Gaussian and 0.0943 from the arcsine law |

**Read after the run.**
- The skew is about −1/√p: for the non-split states between −1.010/√p and −1.003/√p at the primes from 101 to 401, and
  for the split ones between −0.99/√p and −0.95/√p. It vanishes as p grows.
- After centering, the non-split states' average fourth moment lies within about 3/p² of 2 (between 2.6/p² and 3.2/p²
  from 31 to 401); no exact form was found.
- The split states' moments come down to the semicircle's from above, more slowly than the non-split ones'.
- The proof of round 11's identity is now written, in [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md), with
  [`verify_torus_moments.py`](verify_torus_moments.py) checking each of its steps.
- (Added 2026-11-14.) The skew is now exact as well: [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §6 proves the third
  moment, and its formula reproduces every logged non-split average, at all 77 primes.

**Yield.** The whole distribution of the oscillator states' Wigner values is the semicircle at these sizes, through the
eighth moment and in Kolmogorov distance: the Sato–Tate law in full. That is measurement. The proof covers the fourth
moment only.

---

## Round 13: cubic magic (registered 2026-11-14, before any run)

> *it's okay to drift, i am the visionary, you are the drafter... let's pick a useful direction... keep going, do what
> you do* — the author, 14 November 2026

Round 10's proof used one fact about the norm: it is a cubic. So the same reasoning should cover every cubic-phase
state, ψ_f = Σ_x ω^f(x) |x⟩ / √q on n wheels with f of degree at most 3. These are the magic states of the third
level's diagonal gates (Cui, Gottesman and Krishna), the non-Clifford gates of fault-tolerant computing with qudits.
For a single qudit their Wigner functions are known to be cubic character sums (Howard and Vala; the qudit CHSH paper);
for many wheels, which cubic is best has not been asked, as far as we found.

**Made exact, before the run.**
- **The identity** [FORCED]. Let C be f's homogeneous cubic part. Then ψ_f's Wigner function takes the values S(w)/q²,
  each at q points, for w in F_p^n, where S(w) = Σ_s ω^(w·s − 2C(s)) is the Walsh transform of −2C. So
  N = ((1/q) Σ_w |S(w)| − 1)/2, and the negativity depends only on C, and only on C up to a linear change of
  coordinates.
  - Proof. f(u + s) − f(u − s) is twice the part of f(u + s) that is odd in s: C(s), plus a term linear in s that
    depends on u. So W(u, k) = q⁻² Σ_s ω^(−2C(s) + w·s) with w = 2k − 2ℓ_u, and for fixed u the map k → w is a
    bijection. Over F_3 the cubic part uses the monomials of degree 3 with no exponent above 2, since x³ = x there.
  - Checked before this registration ([`cubic_magic_calibrate.log`](cubic_magic_calibrate.log)) against the Wigner
    function computed from the state, for random cubic states with random lower terms on two and three wheels of 3
    and 5 and two of 7; and round 10's norm states come out again at 3, 5 and 7.
- **A corollary: no cubic-phase state reaches the ceiling** [FORCED, with NAMED]. By Parseval, Σ|S(w)|² = q², so
  (1/q) Σ|S(w)| ≤ √q, with equality exactly when −2C is bent. Mesnager, Özbudak and Sınak (2018) proved that there are no
  homogeneous cubic bent functions in odd characteristic. So every cubic-phase state, on any number of wheels, falls
  strictly below the ceiling (√q − 1)/2.
- **The test.** [`cubic_magic.py`](cubic_magic.py), committed with this registration, takes every cubic form on two
  wheels for p = 3 to 23 and on three wheels for p = 3 and 5 (9 765 625 forms at 5), and 2 000 000 random forms on three
  wheels of 7 plus named ones. It logs the best negativity, the form that reaches it and the points of its curve.
- **The timing printed no values.** The run takes about eight minutes.
- **Not computed before this registration:** any cubic form's negativity except the norm forms, and any best value.

**Predictions.** K0 is a calibration and K1 a check of the corollary; K2 to K6 are fresh.

**K0. (Calibration, done.)** The identity against the state's own Wigner function, and round 10's norm states.

**K1. (Forced.)** No cubic form on two or three wheels reaches the ceiling.

**K2. (Fresh; Claude's reading.)** On two wheels of 5 and of 7, the best cubic-phase state reaches round 9's search
best (1.766937 and 2.719253): the most negative two-qudit states found are third-level magic states. *Kill:* the best
cubic falls short at either.

**K3. (Fresh.)** On three wheels of 3, no cubic form beats the norm form's 17/9. *Kill:* one that does.

**K4. (Fresh; Claude's reading.)** On three wheels of 5, some cubic form beats the norm form's 4.252724: at 5 the norm's
Kloosterman sums are small, so another cubic should do better. *Kill:* none does.

**K5. (Fresh.)** On three wheels of 7, no sampled cubic form beats the norm form's 7.902228. *Kill:* one that does.

**K6. (Fresh; the useful one.)** Per wheel, the best cubic-phase state on three wheels carries more negativity than the
CCZ-type state ω^(xyz), and at 5 and 7 more than three copies of the single-wheel cubic state ω^(x³). The measure per
wheel is the cube root of the sum of sizes. *Kill:* either falls short at 3, 5 or 7.

**Expected standing.** The identity and the corollary are exact. The best values on two wheels and on three wheels of
3 and 5 are exhaustive, so exact maxima over cubic states; at 7 the sample is not exhaustive.

---

## Round 13 scores (added after the run, 2026-11-14)

Run by [`cubic_magic.py`](cubic_magic.py), committed with this registration at 0bf86ae, before the run; the output is
kept in [`cubic_magic_run.log`](cubic_magic_run.log) and [`cubic_magic_combined.log`](cubic_magic_combined.log). It
took 6.6 minutes; the values are exact up to rounding, and exhaustive except at three wheels of 7. **Four held, two
died: K2 and K4.**

| | outcome | evidence |
|---|---|---|
| K0, calibration | held | the identity against the state's own Wigner function, and round 10's norm states |
| K1, forced | held | no cubic form tested reaches the ceiling |
| K2 | **died** | the best two-wheel cubic states fall short of round 9's search bests: (9 + 3√5)/10 = 1.570820 against 1.766937 at 5, and 2.567775 against 2.719253 at 7 (and 2/3 against 8/9 at 3). The most negative two-qudit states are not cubic-phase states |
| K3 | held | three wheels of 3, all 2 187 forms: the best is the norm form's 17/9; the CCZ-type form xyz is second, at 16/9 |
| K4 | **died** | three wheels of 5, all 9 765 625 forms: nothing beats the norm form's 4.252724. It is the maximum, reached by 388 000 forms |
| K5 | held | three wheels of 7, 2 000 004 forms: the best is the norm form, 7.902228, reached 1 316 times |
| K6 | held | per wheel, the norm state beats the CCZ-type state and three single-wheel cubes: at 7, 2.562 against 2.476 and 2.259 (cube root of the sum of sizes) |

**Read after the run.**
- **Two wheels follow Sato–Tate too.** The best two-wheel cubic reaches 0.856, 0.852, 0.850, 0.845, 0.848 and 0.847 of
  the ceiling at 7, 11, 13, 17, 19 and 23: the semicircle's 0.849 again, a third family after the torus states and the
  norm states.
- **A coin by p mod 3.** The best two-wheel cubic splits into three rational lines when p is 2 more than a multiple of 3
  (5, 11, 17, 23), and has exactly one rational root when p is 1 more (7, 13, 19). This held at all seven primes; it is
  an observation, not a test.
- **At 5 elliptic curves tie the norm form.** Of the forms reaching 4.252724, those whose curve has no points have
  exactly the norm form's Wigner values. The rest have smooth curves with 8 points over F_5, elliptic curves, and other
  Wigner values, yet the same negativity to 10⁻⁹. Why is open.
- Exact values: the best two-wheel cubic at 5 has (9 + 3√5)/10, and the single-wheel cube state ω^(x³) at 5 has 1/√5.

**Yield.** Exact and new as far as we checked: the identity that turns every cubic-phase state's Wigner function into
the Walsh spectrum of its cubic, and, with Mesnager, Özbudak and Sınak, that no such state reaches the ceiling. Exhaustive
and new: on three wheels of 3 and 5, and in the sample at 7, the norm state is the most magic of all the third level's
diagonal magic states, ahead of the CCZ-type state. Useful: it says which non-Clifford diagonal gate on three qudits
gives the most negativity per magic state.

---

## Round 14: the triangle, the planes and the Smith chart (registered 2026-11-14, before any run)

> *if the triangle unfolds to 8 pointed curves under p=5, that makes sense to be a coin. does a triangle unfold to
> other amounts of points at p=n?... do the fano, consider the double smith* · *the smith chart from electrical
> engineering... laid over other planes* — the author, 14 November 2026

**Made exact, before the run.**
- **The triangle.** The norm form's curve is three lines conjugate over F_p³, a triangle with no point over F_p. At 5,
  smooth curves with 8 points tied its negativity (round 13). The question, at each prime: which curves tie it, and with
  how many points?
- **The planes.** The Fano cubic on 7 wheels is Σ x_i x_j x_k over the 7 lines {i, i + 1, i + 3} mod 7, the Fano plane
  as the difference set {0, 1, 3}. The affine-plane cubic on 9 wheels uses the 12 lines of AG(2, 3). By round 13's
  identity their negativities are L1 norms of Walsh spectra.
- **The Smith chart** [FORCED]. The chart is the map Γ = (z − 1)/(z + 1), the matrix [[1, −1], [1, 1]].
  - Its square is twice z → −1/z, the impedance–admittance flip that the double chart overlays; its fourth power is a
    scalar, the identity map. So the chart is a quarter turn of the Riemann sphere, and the double chart is its half
    turn.
  - Over F_p it scales into SL(2, p) exactly when 2 is a square (p one more or one less than a multiple of 8), with
    order 8. It lies in the non-split torus, round 8's turning wheel, exactly when p is 7 more than a multiple of 8.
    Only at 7 does that torus have 8 elements, so only at 7 does the chart generate the whole turning wheel.
  - The flip z → −1/z is the Fourier transform's action, and round 2's most negative seven-level state is, in one
    frame, an eigenvector of the Fourier transform: the double chart's half turn fixes it.
  - [FENCE] The fine-structure constant is an impedance ratio: α = Z₀/(2R_K), the impedance of free space over twice the
    von Klitzing resistance. That is a definition-level identity of SI physics, noted here, and nothing in this round
    tests physics.
- **The test.** [`planes.py`](planes.py) is committed with this registration:
  - random ternary cubic forms, 2 000 000 at 7, 1 000 000 at 11 and 600 000 at 13; for each that reaches the norm
    value, its curve's point count and whether it has a rational singular point;
  - the two plane cubics against seeded samples of dense random cubics and of sparse ones with as many triples: on 7
    wheels 2 000, 200 and 20 of each at 3, 5 and 7; on 9 wheels 500 and 8 at 3 and 5;
  - the Smith chart's facts at every prime from 5 to 199.
- **The timing printed no values.** The run takes about 22 minutes.
- **Not computed before this registration:** any tie at 7, 11 or 13, and any plane cubic's value.

**Predictions.** S0 is forced; the rest are fresh.

**S0. (Forced.)** The Smith chart's facts above hold at every prime from 5 to 199.

**T1. (Fresh; Claude's reading, from round 13's coin by p mod 3.)** The triangle unfolds at 11, which is 2 more than a
multiple of 3 like 5: some non-norm curve ties the norm value. It does not unfold at 7 or 13. *Kill:* no tie at 11, or
a tie at 7 or 13.

**T2. (Fresh; a guess from the one case seen.)** Every non-norm form that ties the norm value is a curve with p + 3
points and no rational singular point (at 5: 8 points). *Kill:* another point count, a singular one, or no ties at all.

**F1. (Fresh.)** On 7 wheels at 3, 5 and 7, the Fano cubic beats every sampled dense and sparse cubic. *Kill:* a sample
at or above it.

**F2. (Fresh; a gamble.)** The Fano cubic's S/√q exceeds Sato–Tate's 8/(3π) at 5 and 7. *Kill:* at or below.

**F3. (Fresh.)** On 9 wheels at 3 and 5, the affine-plane cubic beats every sampled dense cubic. *Kill:* a sample at
or above it.

**Expected standing.** S0 is exact. The ties and the plane cubics' values are exact for the forms tested; the samples
make T1, F1 and F3 search-level evidence.

---

## Round 14 scores (added after the run, 2026-11-14)

Run by [`planes.py`](planes.py), committed with this registration at 3bba54e, before the run; the output is kept in
[`planes_run.log`](planes_run.log) and [`planes_combined.log`](planes_combined.log). It took 19.4 minutes. **One held,
the forced S0; the five fresh predictions died.**

| | outcome | evidence |
|---|---|---|
| S0, forced | held | at every prime from 5 to 199 the Smith chart is in the turning wheel exactly at 7, 23, 31, 47, 71, 79, 103, 127, 151, 167, 191 and 199 (7 more than a multiple of 8), with order 8; only at 7 is that the whole wheel |
| T1 | **died** | no curve but the norm class ties the norm value at 7 (1 445 ties), 11 (225) or 13 (80): the triangle unfolded only at 5 |
| T2 | **died** | there are no non-norm ties at all at 7, 11 and 13 |
| F1 | **died** | the Fano cubic reaches S/√q = 0.642, 0.558 and 0.560 at 3, 5 and 7, below the sampled dense cubics' best (0.791, 0.801, 0.799) |
| F2 | **died** | 0.558 and 0.560 are far below Sato–Tate's 0.849 |
| F3 | **died** | the affine-plane cubic reaches 0.779 and 0.788 at 3 and 5, below the dense samples' 0.811 and 0.798 |

**Read after the run.**
- **The norm state is the best cubic only at small primes.** The samples at 11 and 13 found 27 453 and 14 040 forms
  above the norm value. A further sample (200 000 and 120 000 forms, after the run) found the best at 15.013610
  against the norm's 14.900798 at 11, a smooth curve with 12 = p + 1 points, and 19.498692 against 18.887726 at 13, a
  smooth curve with 9 points. Both sit near Sato–Tate's share (0.846 and 0.850), where the norm falls short (0.840 and
  0.824). Round 13's reading, that the norm state is the most magic cubic on three qudits, holds at 3, 5 and 7 only.
- **Symmetric designs make poor magic.** The Fano and affine-plane cubics have few-valued Walsh spectra (11 and 14
  distinct values at 3), and their negativity falls below random cubics'. Symmetry concentrates the spectrum, and a
  concentrated spectrum has a small L1 norm.
- **Random cubics on many wheels are Gaussian.** The dense random cubics on 7 and 9 wheels average S/√q = 0.775 to
  0.798, at or below the Gaussian value √(2/π) = 0.798 of a random state, not the semicircle's 0.849.

**Yield.** Exact: the Smith chart's place in the two wheels, with 7 the only prime where it turns the whole wheel. The
rest are negatives, kept: the triangle's unfolding is a one-prime event, design cubics are poor magic, and the norm
state's reign as the best cubic ends at 11.

---

## Round 15: the free picture (registered 2026-11-14, before any run)

> *2 and 3* — the author, 14 November 2026, answering two questions: whether to try a proof of the whole semicircle
> through free probability, and whether to revive Luther's dispersion thread (the second is on
> [`../THE_STAIRCASE.md`](../THE_STAIRCASE.md)).

Rounds 11 and 12 measured the oscillator states' Wigner values following the semicircle through the eighth moment, and
[`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) proves the third and fourth. In the fourth-moment count only two of the three
ways to pair four points survive: the two that do not cross. That is the signature of free probability, where sums of
free variables follow the semicircle because crossing pairings vanish. This round asks whether it holds for every
moment.

**What is forced, and checked by [`free_moments.py`](free_moments.py)'s calibrate step:**
- By the twirl, the moments are traces of powers of the circle operator S_C, the sum of the phase-point operators over
  a circle.
- The circles are dilations of one another, and a dilation multiplies every phase by the norm. So, summed over the
  circles, each moment is a count on one circle: Σ_C Tr S_C^k = p(pZ_k − N_k) for even k, where N_k counts the closed
  k-gons on the circle and Z_k those with phase 0, and pZ_k − m^k for odd k (C2).
- A product of phase-point operators is a phase-point operator (odd k) or a shift (even k) times a phase, and the
  phase is a fan of triangle areas (C1).
- Every non-crossing pairing of the vertices has phase 0, because A_v² = 1 removes an adjacent equal pair. So the
  non-crossing pairings give the Catalan numbers (C3).
- Every crossing pairing has a non-zero phase somewhere (C4, at k = 6 and 8), so the crossing pairings fall away like
  1/p.
- At k = 4 every closed quadrilateral lies on a pairing (C5), which is why the fourth moment came out exact.

So the whole semicircle comes down to one question: do the area phases of the other closed polygons, the generic ones,
cancel? At k = 6, the first case with generic polygons, it is enough that their phase is equidistributed; from k = 8 on
it takes square-root cancellation. This round measures k = 6 on one circle at every prime up to 101, and the higher
moments directly at five primes up to 1009.

| | prediction | dies if |
|---|---|---|
| F0, forced | the calibrate checks C1 to C5 pass | any fails |
| F1 | at k = 6 the non-crossing part of the normalized sixth moment, M6 = (pZ' − N')/((p − 1)m²) with the first vertex fixed, lies in [5 − 15/p, 5] at every prime from 5 to 101 | a prime outside |
| F2 | the crossing part falls away: below 1 in size at every prime from 61 on, and p times its size at 101 is at most twice p times its size at 31 | either fails |
| F3 | the generic part falls away: below 0.5 in size from 89 to 101, and the log of its size falls against log p over 31 to 101 (a negative least-squares slope) | either fails |
| F4 | the generic hexagons' phase is equidistributed: p·Z'_gen/N'_gen lies in [0.9, 1.1] at every prime from 61 on | a prime outside |
| F5 | the first correction is free, not classical: the basis average of the standardized fifth moment, over the third, lies in [4, 6] at 503, 701, 907 and 1009. A semicircle perturbed by a small free third cumulant gives 5, a classical perturbation 10 | a prime outside |
| F6 | the semicircle holds in the 10th and 12th moments: at 1009 they lie within 10% of 42 and 132 (Gaussian: 945 and 10 395) | either outside |
| F7 | the convergence goes on: at 1009 the sixth and eighth moments' distances from 5 and 14 are below half their values at 211 | either not |

**The drafter's expectation:** F0 and F1 are forced. F2, F3, F4, F6 and F7 should hold. F5 is the open one.

Run: `python free_moments.py calibrate`, then `python free_moments.py run` (minutes).

---

## Round 15 scores (added after the run, 2026-11-14)

Run by [`free_moments.py`](free_moments.py), committed with this registration at ef11ddc, before the run; the output is
kept in [`free_moments_calibrate.log`](free_moments_calibrate.log) and [`free_moments_run.log`](free_moments_run.log).
The run took 8.7 minutes. **All eight held.**

| | outcome | evidence |
|---|---|---|
| F0, forced | held | C1 to C5 pass: the phase formula; one circle's counts against the states' moments; Φ = 0 on all 5 and 14 non-crossing pairings; a non-zero phase on all 10 and 91 crossing ones; no generic quadrilaterals |
| F1 | held | the non-crossing part rises from 4.056 at 5 to 4.941 at 101, inside [5 − 15/p, 5] at every prime; its shortfall is about 6/p, from overlaps |
| F2 | held | the crossing part is −0.209 at 31, −0.109 at 61 and −0.067 at 101: p times it stays between −6.5 and −6.8 |
| F3 | held | the generic part is 0.033 at 89, 0.010 at 97 and 0.028 at 101, and log\|gen\| falls against log p with slope −0.52 over 31 to 101 |
| F4 | held | p·Z′_gen/N′_gen lies between 1.011 and 1.047 at every prime from 61 on |
| F5 | held | m5/m3 = 5.036, 5.011, 4.973 and 5.014 at 503, 701, 907 and 1009 (free 5, classical 10) |
| F6 | held | at 1009 the 10th and 12th moments are 42.201 and 133.120 (semicircle 42 and 132; Gaussian 945 and 10 395) |
| F7 | held | at 1009 the sixth and eighth moments are 5.0031 and 14.0305, against 5.0167 and 14.1603 at 211 |

**Read after the run.**
- **Every odd moment follows the free count.** Only the fifth was registered. At 1009 the seventh, ninth and eleventh
  moments over the third are 21.01, 83.8 and 328.7. Free probability predicts 21, 84 and 330, the numbers of
  non-crossing partitions of 7, 9 and 11 points into one triple and pairs; the classical counts are 105, 1 260 and
  17 325. At 211 all four ratios lie within 5% of the free counts, and at 1009 within 0.4%.
- So, to first order, the law is the semicircle perturbed by one free cumulant, κ3 = m3, which is about −1/√p, with
  the next ones small. κ4 = m4 − 2 equals 3/p² to the log's rounding (6.70 × 10⁻⁵ against 6.74 × 10⁻⁵ at 211), and
  m6 − 5 is near the free value 3κ3² (within 6% at 907 and 1009).
- **The generic part falls like 1/p, and its constant follows p mod 3.** p times it lies below 1.1 at every prime 1
  more than a multiple of 3, and between 1.7 and 3.1 at every prime from 17 on that is 2 more than a multiple of 3,
  where the turning wheel holds hexagons: the coin of [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §6. The fitted slope,
  −0.52, mixes the two classes and understates the fall.

**Yield.** Forced: every moment reduces to polygon counts, the non-crossing pairings give the Catalan numbers, and the
crossing pairings fall away. Measured: at the sixth moment the generic polygons' phases cancel to order 1/p, and every
odd moment through the eleventh follows free probability's count, not the classical one. One step remains for a proof
of the whole semicircle: that the generic polygons' phases cancel at every even order.

---

## Round 16: the exact sixth moment and the fourth free cumulant (registered 2026-11-14, before the test)

> *go after an exact formula for the 6th moment first.. The free fourth cumulant equals 3/p² to every digit the log
> keeps. Worth a short exact proof as a small theorem* — the author, 14 November 2026

Every moment is an integer count in disguise ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §7). The `collect` step of
[`exact_moments.py`](exact_moments.py) read the integers I_n = Σ_C Tr S_C^n and J_n = Σ_C Tr(P S_C^n), for n up to 6,
from the states at every prime from 5 to 199 ([`exact_moments_collect.log`](exact_moments_collect.log)).
[`exact_moments_fit.py`](exact_moments_fit.py) then looked for exact formulas: polynomials in p, with the characters
of p mod 3 and mod 4, plus at most two modular forms from a library of fourteen. Two came out exact, with small integer
coefficients, at all 45 primes from 7 to 199:

- **I6 = p[5p⁴ − p³ − 5p² − 1 + (p + 1)(b(p) − (−3|p)p²)].** Here b(p) is the p-th coefficient of
  (η(τ)η(2τ)η(3τ)η(6τ))², the newform of weight 4 and level 6. It is the form in the sixth moment of Kloosterman sums
  [NAMED: Hulek, Spandaw, van Geemen and van Straten 2001], and the whole modular term comes through the count of closed
  hexagons, which a circle's Fourier transform, a Kloosterman sum, writes in terms of that sixth moment. The hexagons
  with phase 0 number (p + 1)(6p² + (4 − (−3|p))p + 1), with no modular part.
- **J4 = (3p + 1)(p² − 1) − 4p(p + 1)b²,** where p = a² + b² with b even when p ≡ 1 (mod 4), and b = 0 when
  p ≡ 3 (mod 4). Equivalently, its non-polynomial part is p(p + 1)c(p), with c(p) the coefficients of η(4τ)⁶, the
  newform of weight 3 with complex multiplication by the Gaussian integers.

With J4, the fourth free cumulant is exact. It is 3/p² + O(1/p³), not exactly 3/p², and its 1/p³ term depends on p mod
3, on p mod 4 and on b²/p. The fifth moments and J6 did not fit any formula tried; they stay open.

The formulas were found at the primes from 7 to 199. This round tests them where they were not fitted.

| | prediction | dies if |
|---|---|---|
| E0, forced | the coefficients of η(4τ)⁶ are 2(a² − b²) at the primes 1 more than a multiple of 4, and 0 at the others, up to 1009, so the two forms of J4's formula agree | a prime fails |
| E1 | I6's formula holds exactly at every prime from 211 to 401 | a prime fails |
| E2 | J4's formula holds exactly at every prime from 211 to 401 | a prime fails |
| E3, forced | the proved counts I2, I3, I4, J2 and J3 hold at every prime from 211 to 401 | one fails |
| E4 | the exact κ4 equals the states' basis-averaged standardized fourth moment off the origin, minus 2, within 10⁻¹¹ at 211, 503, 701, 907 and 1009 | a prime outside |
| E5 | the exact sixth moment equals the states' (1/p)Σ_jΣ_u W⁶ within a relative 10⁻¹⁰ at 503, 701, 907 and 1009 | a prime outside |

**The drafter's expectation:** all hold.

Run: `python exact_moments.py test` (minutes).

---

## Round 16 scores (added after the test, 2026-11-14)

Run by [`exact_moments.py`](exact_moments.py) `test`, committed with this registration at 7c77ed2 before the test; the
output is kept in [`exact_moments_test.log`](exact_moments_test.log). **All six held.**

| | outcome | evidence |
|---|---|---|
| E0, forced | held | the coefficients of η(4τ)⁶ are 2(a² − b²) or 0 at every prime to 1009 |
| E1 | held | I6's formula is exact at all 33 primes from 211 to 401, none of them used to find it |
| E2 | held | J4's formula is exact at all 33 primes from 211 to 401 |
| E3, forced | held | I2, I3, I4, J2 and J3 at every prime from 211 to 401 |
| E4 | held | the exact κ4 and the states' value agree to about 10⁻¹⁵ at 211, 503, 701, 907 and 1009 (κ4 = 6.6516 × 10⁻⁵ at 211, 2.9511 × 10⁻⁶ at 1009) |
| E5 | held | the exact sixth moment and the states' agree to a relative 10⁻¹² or better at 503, 701, 907 and 1009 |

**Yield.** Two exact formulas, each found on 45 primes and confirmed on 33 more. The sixth moment carries the newform of
weight 4 and level 6; it enters through the closed-hexagon count, by the classical evaluation of Kloosterman's sixth
moment. The fourth free cumulant is exact and 3/p² only to leading order; the Gaussian integers' CM form η(4τ)⁶ is in
it. What is not proved is the two counts of phase-0 polygons, Z6 and J4: both are exact at every prime to 401.
(Added later the same day: Z6 is now proved, by an elementary count, so the sixth-moment formula is a theorem;
see [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8 and [`verify_sixth_moment.py`](verify_sixth_moment.py). J4's count
is still open.)

---

## Round 17: the fifth moments (registered 2026-11-14, before the test)

> *1, apply the hexagon method to the fifth moments* — the author, 14 November 2026

Round 16 left I5 and J5 open: no formula in its library fitted them. The hexagon method of
[`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8 splits a count by the alternating sum w of a triangle. Applied to the fifth
moments, it gave two exact formulas, found and checked at every prime from 7 to 401 against the operators' integers
([`exact_moments_collect.log`](exact_moments_collect.log), [`exact_moments_test.log`](exact_moments_test.log)):

- **J5 = p(p + 1)[f15(p) − p·a_E(p) + (4(−3|p) − 3)p − 1].** The phase-0 polygons number (p + 1)·#E(F_p) for the
  elliptic curve E: y² = x(x − 4)(4x² − 52x + 9), by an elementary count. The closed polygons bring in Kloosterman's
  fifth moment and its weight-3 newform f15 of level 15.
- **I5 = p(p + 1)[p³ + 4p² − (1 + (5|p))p − 4 + a10(p)] − p⁵ − 1,** where a10(p) are the coefficients of the weight-4
  newform of level 10. Here the split by w left a sum over a threefold, and a second method finished it. Expanding the
  six quadrics in Gauss sums of Hermitian forms gives I5 = (p + 1)(p·N_V − N_W), where N_W = (p⁵ + 1)/(p + 1). N_V is a
  point count on a double octic: the double cover of 3-space branched along Clebsch's diagonal cubic surface and its
  five Sylvester planes. That count matches the level-10 newform exactly at every prime to 401.
- The forms were named by a modular-symbols engine written for this, [`modular_symbols.py`](modular_symbols.py). It
  was needed because LMFDB answered a burst of queries with a captcha. The engine reproduces the four weight-4 eta
  products of levels 5, 6, 8 and 9.

What is proved and what is measured is set out in [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8. This round tests the
formulas at primes where they were not found.

| | prediction | dies if |
|---|---|---|
| F0, forced | the engine reproduces the eta products of levels 5, 6, 8 and 9 at every prime to 601 | a prime fails |
| F1 | I5's formula holds exactly at every prime from 409 to 509 | a prime fails |
| F2 | J5's formula holds exactly at every prime from 409 to 509 | a prime fails |
| F3 | the double octic: (−1\|p)·S_oct = 6p² − 19p − a10(p) at every prime from 409 to 601 | a prime fails |
| F4 | E's traces equal those of the weight-2 newform of level 150 with a(7), a(11), a(13) = −2, 2, −6, at every prime from 409 to 601 | a prime fails |
| F5, forced | the proved I2, I3, I4, J2 and J3, and round 16's I6 and J4, hold at every prime from 409 to 509 | one fails |
| F6, precision | every raw operator value from 409 to 509 lies within 0.1 of its integer | not met: the round is inconclusive, not failed |

**The drafter's expectation:** all hold.

Run: `python fifth_moments.py test` (about ten minutes, four processes at below-normal priority).

---

## Round 17 scores (added after the test, 2026-11-14)

Run by [`fifth_moments.py`](fifth_moments.py) `test`, committed with this registration at ea0e632 before the test.
- The first run printed F0, F3 and F4, all held. It then crashed while scoring F5, on a type error in the script
  ([`fifth_moments_test_first_run.log`](fifth_moments_test_first_run.log)).
- The one-line fix, committed at dc2a2b7 before the rerun, changed no prediction.
- The rerun's output is [`fifth_moments_test.log`](fifth_moments_test.log).

**Six of seven held. The seventh, the precision bar, was not met, so by its own rule the round's operator half is
inconclusive.** The exact half held.

| | outcome | evidence |
|---|---|---|
| F0, forced | held | the engine's one rational system equals each eta product at every prime from 7 to 601 |
| F1 | held as computed; inconclusive by F6 | I5's formula equals the rounded operator integer at all 18 primes from 409 to 509 |
| F2 | held as computed; inconclusive by F6 | J5's formula equals it at all 18 |
| F3 | held | the double octic's sum is 6p² − 19p − a10(p), times (−1\|p), at all 31 primes from 409 to 601, in exact integer arithmetic |
| F4 | held | E's traces equal the level-150 newform's at all 31, exactly |
| F5, forced | held as computed; inconclusive by F6 | I2, I3, I4, J2, J3, I6 and J4 at all 18 |
| F6, precision | not met | the worst raw operator value lay 0.297 from its integer (at 487), against the registered 0.1 |

**Read after the run** (not a score; [`fifth_moments_precision.py`](fifth_moments_precision.py),
[`fifth_moments_precision.log`](fifth_moments_precision.log)).
- Each operator value's distance to its integer, measured separately: every one from I2 to J5 lies within 0.0005 of
  its integer at all 18 primes.
- The rounding error is all in the sixth moments: I6 up to 0.297, J6 up to 0.045.
- So the fifth-moment integers behind F1 and F2 were read cleanly. F6 as registered covered every value, and it was
  not met.

**Yield.**
- Two exact formulas for the fifth moments. J5's is proved, and it carries an elliptic curve of conductor 150 and the
  CM form of level 15.
- I5's is proved but for one count, on a double octic over Clebsch's diagonal cubic and its pentahedron. That count
  carries the weight-4 newform of level 10, and held blind to 601 in exact arithmetic.
- The method that proved I5 writes every odd I_n and even J_n as one count on the turning wheel. It reduces J4's open
  count to one character sum on an elliptic surface.
- A modular-symbols engine, checked on four known forms, named the forms after LMFDB answered with a captcha.
- The deaths: round 16's "the level-15 form is not in the fifth moments", and the Q(√−11) form of the circle part,
  which cancels in the whole. Both are kept in the graveyard.

---

## Round 18: J4's surface sum, proved (registered 2026-11-14, before the test)

> *1 and 2, J4's surface sum first* — the author, 14 November 2026

Round 17 left Theorem 5 resting on one character sum over an elliptic surface,
T(p) = Σ_(κ≠0) Σ_A η(κA(κ + 4 − 4A)((κ + 4)A − 4κ)), measured exactly to 401. It is now proved
([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8, Theorem 5). The proof has two classical tools.
- **A 2-isogeny.** This is Landen's transformation over F_p. It turns T into a sum over the Legendre family at the
  squares.
- **Quartic Jacobi sums.** They evaluate that sum: T(p) = p + 2(a² − b²) when p ≡ 1 (mod 4), with a odd, and T(p) = p
  when p ≡ 3 (mod 4). That is (2 + (−1|p))p − 4b².

The pairing that leads to T is now written out in full. So J4 is a theorem, and with it the fourth free cumulant.
[`fourth_cumulant.py`](fourth_cumulant.py) checks every step at every prime from 7 to 401
([`fourth_cumulant_verify.log`](fourth_cumulant_verify.log)). This round tests the theorem and its steps where they
were not computed.

| | prediction | dies if |
|---|---|---|
| G1 | T(p) = (2 + (−1\|p))p − 4b² at every prime from 409 to 3001 | a prime fails |
| G2 | the proof's steps hold at every prime from 409 to 1009: the Legendre form at every κ, Landen at every t, the sum, and W = J(χ, η)² + J(χ̄, η)² with Re J odd | a step fails at a prime |
| G3 | the pairing: F(κ) = p − 1 + 2η(κ + 4) + G(κ) at every κ ≠ 0 and ΣG = 2 + (−1\|p)p, so N_V⁽⁴⁾ = (p − 1)² + 2 + (−1\|p)p − T(p), at every prime from 409 to 1009 | one fails |

**The drafter's expectation:** all hold. Every step is an identity, so a failure would mean an error in the proof.

Run: `python fourth_cumulant.py test` (a few minutes, four processes at below-normal priority).

---

## Round 19: the coin at 5 (registered 2026-11-14, before the test)

> *1 and 2, J4's surface sum first* — the author, 14 November 2026. The "1" says yes to registering a test of the
> reading that the fifth moment's split by (5|p) is the coin at 5.

**The reading.** In [`../../base/SEVEN_AND_NINE.md`](../../base/SEVEN_AND_NINE.md) the author classifies 5 as a coin.
- The flat face is the pentagon, with its centre empty.
- The solid face is the tetrahedron with its centre filled: 5 = 4 + centre.
- The edge between them is the centre itself.

The fifth moment splits by (5|p), through Clebsch's cubic. [`coin_at_five.py`](coin_at_five.py) checks a dictionary
between the two [FORCED; [`coin_at_five_verify.log`](coin_at_five_verify.log)].
- **The solid face.** The double octic behind I5 is branched along the five planes where one of the five points sits
  at the centre, the other four summing to 0 round it.
- **The flat face.** It is also branched along Clebsch's cubic, which holds the regular pentagon (1, z, z², z³, z⁴).
- **The edge.** The two faces meet in 15 rational lines, each the centre with two opposite pairs.
- **The flip.** The cubic's other 12 lines form a double six. Every odd permutation of the five points swaps its two
  sixes, and over Q so does √5 ↦ −√5 [NAMED: Clebsch 1871].
- **Characteristic 5.** There the cubic pinches at one point, the centre.

So the coin's flip is √5 ↦ −√5, its sides are (5|p) = ±1, and its edge is p = 5.

The test asks two things the dictionary does not decide.
- **The edge itself.** If the edge is where the two sides meet, the formulas should hold at the edge primes.
  - The symbol there is 0, the average of its sides.
  - Each form enters with its coefficient at its bad prime: a10(5) = 5, a10(3) = −8, f15(5) = 5, f15(3) = −3 and
    a_E(5) = 0. These were computed before this registration, by the engine with U_q, and from the eta products.
  - At 3 the curve's equation gives a_E(3) = −2, while the level-150 newform has a(3) = 1. Both values are
    registered.
  - The derivations assumed p ≥ 7 in places, so this can fail.
- **The coin at 7.** The author's coin also holds at 7: the heptagon, and the octahedron with its centre.
  - The dictionary's flat face at 7 is the cubic fourfold X7 = {x1 + ⋯ + x7 = x1³ + ⋯ + x7³ = 0}, the analogue of
    Clebsch's cubic.
  - Laza and Zheng found its transcendental lattice to be −[[2, 1], [1, 18]], as the cubic they call X¹(A7)
    [NAMED: Laza and Zheng, arXiv:1905.11547]. Its discriminant is 35 = 5·7, which means complex multiplication by
    Q(√−35): the pentagon's √5 and the heptagon's √−7 together.
  - Then t7 = p²α(p) + p·c(p), with α an integer and c the CM form's coefficient. c vanishes at the primes inert in
    Q(√−35) and is never a multiple of p at the split ones.
  - If C2 holds, the arithmetic sees 7 in its flat face at 7 as it sees 5 in Clebsch's.

| | prediction | dies if |
|---|---|---|
| C0, forced | the operators at p = 3 and 5 reproduce the proved I2, J2, I3 and I4, and Theorem 5's J4 (80 at 3, −96 at 5) | one fails: the instrument or a proof fails at small p, and C1 is void |
| C1 | **the edge**: I5 = 3504 and J5 = −930 at p = 5, and I5 = 368 at p = 3. J5 at 3 is −84 (the equation's count) or −192 (the newform's), and which is recorded. J3 at 3 is −12 (the edge average, −(1 − (−3\|p))p(p + 1)) or 0 (the form "−2p(p + 1) when p ≡ 2 mod 3, else 0"), and which is recorded | a value is none of these |
| C2 | **the coin at 7**: X7's primitive trace t7(p) = #X7(F_p) − (1 + p + p² + p³ + p⁴) is divisible by p² at every prime from 11 to 397 inert in Q(√−35), and at no split one. The control holds at every one of these primes: Clebsch's t5 = (5 + (5\|p))p | a prime fails, or the control does |
| C3, a first look, not scored | the cubic in 9 variables, where the coin breaks: its primitive trace and divisibility, by p mod 9; and t7/p² at the inert primes, by character | — |

**The drafter's expectation:** C0 and C2 hold, and C1 holds at 5. At 3, a coin toss.

Run: `python coin_at_five.py test` (a few minutes, four processes at below-normal priority).

---

## Round 18 scores (added after the test, 2026-11-14)

Run by [`fourth_cumulant.py`](fourth_cumulant.py) `test`, committed with this registration at c740708 before the
test. Output: [`fourth_cumulant_test.log`](fourth_cumulant_test.log).

**All three held.**

| | outcome | evidence |
|---|---|---|
| G1 | held | T(p) = (2 + (−1\|p))p − 4b² at all 352 primes from 409 to 3001, in exact arithmetic |
| G2 | held | every step of the proof at all 90 primes from 409 to 1009 |
| G3 | held | the pairing at all 90 |

After the test the verifier was extended down to p = 3 and 5. That took two small fixes in the step check: κ = −4 is
k = (−4) mod p, which is not p − 4 when p = 3, and an index 4 is read mod p. Neither touches the code path at the
test's primes. Every step now holds at every odd prime from 3 to 401
([`fourth_cumulant_verify.log`](fourth_cumulant_verify.log)).

**Yield.** J4 is a theorem, and with it the fourth free cumulant. The last open count of round 16 is closed.

---

## Round 19 scores (added after the test, 2026-11-14)

Run by [`coin_at_five.py`](coin_at_five.py) `test`, committed with the registration at c740708 before the test.
Output: [`coin_at_five_test.log`](coin_at_five_test.log).

**Two of three scored predictions held. C1 failed on its J side.**

| | outcome | evidence |
|---|---|---|
| C0, forced | held | at p = 3: I2 = 24, J2 = 8, I3 = 56, I4 = 144, J4 = 80; at p = 5: 120, 24, 264, 1200, −96. All are as proved, and Theorem 5's J4 holds at 3 |
| C1 | **failed** | I5 = 3504 at 5 and 368 at 3, as predicted. But J5 = −1680 at 5 (registered −930), J5 = 240 at 3 (registered −84 or −192), and J3 = 24 at 3 (registered −12 or 0) |
| C2 | held | t7 is divisible by p² at all 37 primes from 11 to 397 inert in Q(√−35), and at none of the 37 split ones. The control, t5 = (5 + (5\|p))p, holds at all 74 |
| C3 | read, not scored | below |

**Read after the run** (not scores).
- **The edge.**
  - The moment without the flip, I5, holds at the edge p = 5, where (5|5) = 0 averages its two sides.
  - The moments with the parity flip P do not. J3 at 3 is +2p(p + 1), the negative of its (−3|p) = −1 side rather than
    the average. J5's formula holds only from 7 on, as its derivation assumed.
- **The cubic fourfold X7.** At every prime from 11 to 397, t7 = p²(14 + 6(5|p)) + p·c(p).
  - |c(p)| is the coefficient of the weight-3 CM form of Q(√−35): 0 at the inert primes; |2x² + 2xy − 17y²| when
    p = x² + xy + 9y²; and |u|, with u² + 35v² = 4p², when p = 3x² + xy + 3y².
  - So its algebraic part sees only the pentagon's (5|p), and 7 enters only through the transcendental part, by
    √−35 = √5·√−7.
  - The dimensions add up: 22 = 14 + 6 + 2.
- **The cubic sixfold X9.** At every prime from 11 to 397, t9 = p³(42 + 27(5|p) + (105|p)) + 8p²c(p), with the same c.
  - The dimensions add up: 86 = 42 + 27 + 1 + 8·2.
  - At 9 the one new character is (105|p) = (−3|p)(−35|p): the triangle's coin at 3, times the CM field from 7.
- These two formulas were read after the run, so they count for nothing until tested blind (round 20).

**Yield.**
- The dictionary between the coin at 5 and the fifth moment.
- The coin at 7, seen in the arithmetic of its flat face (C2).
- One death: C1's J side, kept in the graveyard with these values.

---

## Round 20: the cubics in 7 and 9 variables, blind (registered 2026-11-14, before the test)

Round 19's first look read two formulas after its run, at every prime from 11 to 397 (above). This round tests them
at every prime from 401 to 601, where nothing about these cubics has been computed.

| | prediction | dies if |
|---|---|---|
| H1 | t7 = p²(14 + 6(5\|p)) + p·c(p), with \|c(p)\| the coefficient of the weight-3 CM form of Q(√−35) as above, at every prime from 401 to 601 | a prime fails |
| H2 | t9 = p³(42 + 27(5\|p) + (105\|p)) + 8p²c(p), with t7's c, at every prime from 401 to 601 | a prime fails |

**The drafter's expectation:** both hold.

Run: `python coin_at_five.py test20` (a few minutes, four processes at below-normal priority).

---

## Round 20 scores (added after the test, 2026-11-14)

Run by [`coin_at_five.py`](coin_at_five.py) `test20`, committed with this registration at 5c12567 before the test.
Output: [`coin_at_five_test20.log`](coin_at_five_test20.log).

**Both held.**

| | outcome | evidence |
|---|---|---|
| H1 | held | t7 = p²(14 + 6(5\|p)) + p·c(p), with \|c(p)\| the coefficient of Q(√−35)'s weight-3 CM form, at all 32 primes from 401 to 601, in exact arithmetic |
| H2 | held | t9 = p³(42 + 27(5\|p) + (105\|p)) + 8p²c(p), with the same c, at all 32 |

**Yield.** Exact point counts for the cubics in 7 and 9 variables, found on 74 primes and held blind on 32 more.
- The cubic fourfold's algebraic part sees only the pentagon's √5. Its transcendental part has complex
  multiplication by Q(√−35), as Laza and Zheng's lattice implies.
- The cubic sixfold adds one character, (105|p), and eight copies of the same CM form.
- What these are, and how they read the coin, is in [`COIN_AT_FIVE.md`](COIN_AT_FIVE.md).

---

## Round 21: the coin on its edge (registered 2026-11-14, before the test)

> *1 and 2, the mirror rule first* — the author, 14 November 2026. The "1" says yes: a coin on its edge shows the
> mirror, so register the mirror rule.

Round 19 found J3 = +2p(p + 1) at its edge p = 3: the mirror of its side p ≡ 2 (mod 3), where it is −2p(p + 1). Before
this registration [`edge_rule.py`](edge_rule.py) found why (F1 and F2 of
[`edge_rule_verify.log`](edge_rule_verify.log) [FORCED]).
- **The merge.** J3 counts pairs of points v1, v3 on a circle whose sum is on the circle too.
  - Their ratio v3/v1 is a primitive cube root of unity. When p ≡ 2 (mod 3) the turning wheel holds two of them, and
    each one's phase sums to −1 over the circles.
  - At p = 3 the two merge into 1, since x² + x + 1 = (x − 1)² mod 3. On the merged point the phase vanishes, and the
    sum over the circles is p − 1 = 2. So −2 becomes +2: the mirror.
- **Why the mirror is exact.** At a prime edge q all q − 1 primitive q-th roots of unity merge, and the merged point
  weighs p − 1 = q − 1. At a prime power it does not: at 9 the six primitive ninth roots merge into one point of
  weight 2.

**The rule, made precise.** The edge of a coin is the fixed set of its flip (the author's classification). At an edge
prime the two sides merge into it.
- (a) A count without a phase sees the fixed set once. Its symbol reads 0, the average of its sides.
- (b) A count with a phase sees the phase vanish there, which adds p for each merged point. For all the primitive q-th
  roots at the prime q, that is the exact mirror of the side that holds them.

**What is already known.** These values are all in round 19's log, so none of them is a test.

| moment, edge | operators | reading |
|---|---|---|
| I5 at 5 | 3504 | (a), the average |
| I6 at 3 | 960 | (a), the average. Theorem 4 with (−3\|3) read as 0 gives 960, and the mirror gives 636. This value sat unread in round 19's log |
| J3 at 3 | 24 | (b), the mirror, by the merge above |
| J5 at 3 | 240 | fits (b) with (−3\|3) read as 3 and the newforms' a(3) = 1 and f(3) = −3. That fit was found after 240 was known, among ten readings tried. Plain negation of the −1 side fits no integer a_E(3) |
| J5 at 5 | −1680 | no symbol in J5's formula has its edge at 5. Its curve and its form are bad there instead |

So every parity-weighted edge value we can reach is already measured. The mirror half of the rule has no blind test
left among the formulas we have.

What has never been computed is the cubics at their edge primes: no count of X5 at 5, or of X7 and X9 at 5 or 7, has
been made. They are counts without a phase, so part (a) predicts them.

**The cubics as Airy moments** [FORCED; F4 and F5].
- t_n = #X_n(F_p) − (1 + p + ⋯ + p^(n−3)) is the n-th moment of the cubic exponential sums S(a) = Σ_x e((x³ + ax)/p),
  divided by p².
- So it splits by the ballot numbers m(n, k) into the symmetric powers of the Airy sheaf:
  t_n = Σ_k m(n, k)·p^((n−k)/2 − 2)·T_k.
- By rounds 19 and 20, T_1 = p, T_3 = 0, T_5 = (5|p)p³, T_7 = p³c(p) and T_9 = (105|p)p⁵.
- The coefficients 5, 14, 42 and 6, 27, 8 of their formulas are ballot numbers.
- Sabbah and Yu's Hodge numbers for these pieces [NAMED: arXiv:2112.13405] add up to every Betti number.

**The nodes** [FORCED identity; F3].
- X_n has a node at each sign vector whose sum vanishes mod p.
- Their number is Σ_k m(n, k)·r_k(p), where r_k(p) counts the odd multiples of p up to k.
- [READING] Each node is one dimension where the cohomology is ramified at p: V5 at 5, V7 at 5 and 7, and V9 at 5
  and 7.

| | prediction | dies if |
|---|---|---|
| K0 | Clebsch's cubic over F_5 has exactly 21 lines: the 15 of the edge, and 6 through the centre, where the double six's pairs merge | another count |
| K1 | T5(5) = 0, so t5(5) = 25: (5\|5) reads 0. The mirror would give T5(5) = −375 and t5(5) = 10 | T5(5) ≠ 0 |
| K2 | the CM form at the two primes where Q(√−35) ramifies: \|T7(5)\| = 5⁴ and \|T7(7)\| = 7⁴. So t7(5) is 325 or 375, and t7(7) is 343 or 441 | another value |
| K3 | T9(5) = T9(7) = 0: (105\|p) reads 0 at both. With K1, t9(5) = 5250 + 40(t7(5) − 350) and t9(7) = 5145 + 56(t7(7) − 392) | T9 ≠ 0 at either |
| control | T1 = p and T3 = 0 at 5 and 7, and T5(7) = (5\|7)·7³ = −343 | one fails: the instrument fails |

**The drafter's expectation.**
- K0 and K1 hold, since a cubic surface with one node has 21 lines [NAMED].
- K2 and K3 are less sure: they need the counts at the nodes to see only the unramified part.

Run: `python edge_rule.py test` (seconds). It also reads J5's split into its two counts at 3, 5, 7 and 11, unscored.

---

## Round 21 scores (added after the test, 2026-11-14)

Run by [`edge_rule.py`](edge_rule.py) `test`. Output: [`edge_rule_test.log`](edge_rule_test.log). The registration was
committed at 1620be1 before the test. GitHub could not be reached at the time, so it was pushed later, unchanged,
with these scores.

**All four held, and so did the controls.**

| | outcome | evidence |
|---|---|---|
| K0 | held | Clebsch's cubic has 21 lines over F_5: 15 in the Sylvester planes, and 6 through the centre |
| K1 | held | T5(5) = 0, so t5(5) = 25 |
| K2 | held | T7(5) = −5⁴ and T7(7) = 7⁴. So c(5) = −5 and c(7) = 7, and t7(5) = 325, t7(7) = 441 |
| K3 | held | T9(5) = T9(7) = 0, and t9(5) = 4250, t9(7) = 7889, as K3's formulas give |
| control | held | T1 = p and T3 = 0 at 5 and 7, and T5(7) = −343 |

**Read after the run** (not scores).
- **The signs of c.** c(5) = −5 and c(7) = 7 are the coefficients at the bad primes of LMFDB's newform 35.3.c.b. Its
  twin 35.3.c.a has +5 and −7 there.
  - The q-expansion of 35.3.c.b matches X7's c(p) at every prime to 97.
  - So X7's count is t7 = p²(14 + 6(5|p)) + p·a_p(35.3.c.b) at every prime from 5 to 601. Round 20's open item, the
    signs, is closed.
- **J5's two counts at its edges.** J5 = p(pZ − N), where N counts the closed pentagons on a circle and Z those with
  phase 0.
  - N follows Kloosterman's fifth moment at 3, 5, 7 and 11. At 3 that needs (−3|3) read as 0: the average, part (a).
  - The whole deviation is in Z. At 3, Z = 60 where the side formula gives 24, so 36 = p²(p + 1) more configurations
    have phase 0.
  - At 5, Z = 6 where the side formula gives 36. The triangles vanish, since 4ν² − 52ν + 9 = 4(ν + 1)² there. Only
    the six configurations (v, −v, v, −v, v) remain, and they close because 5v = 0: the regular decagon, merged onto a
    diameter.
  - At 7 and 11 both counts follow their formulas.

**Yield.**
- The rule's half (a), the fixed set, held blind at the cubics' five edge values and in K0's lines.
- Its half (b), the mirror, rests on J3, whose mechanism is forced.
- J5's deviations at its edges sit in its phase-0 count, not in its count of closed pentagons. That was read after
  the run.

---

## Round 22: the cubic in eleven variables (registered 2026-11-14, before the test)

> *1 and 2, the mirror rule first* — the author, 14 November 2026. The "2" says yes to the cubic in eleven variables,
> past the base's edge at 10.

X11 = {x1 + ⋯ + x11 = x1³ + ⋯ + x11³ = 0} is a cubic eightfold, and nothing about it has been computed. Its primitive
middle cohomology has dimension 342. By the Airy decomposition of round 21, with m(11, ·) = 132, 165, 110, 44, 10, 1,

  t11 = p⁴(132 + 110(5|p) + 10(105|p)) + 44p³c(p) + p⁻²T11,

where c is X7's form, 35.3.c.b. Two facts fix T11's shape before any count.
- **Its size** [FORCED; F4].
  - The lower pieces use 340 of the 342 dimensions: 132 + 110 + 10 + 44·2. So T11's classical part is two-dimensional.
  - Sabbah and Yu's Hodge numbers put it at (7, 5) + (5, 7), so it is not algebraic. It is a form of weight 3, with
    T11 = p⁵g(p) and |g(p)| ≤ 2p.
  - A weight-3 newform with rational coefficients has complex multiplication. Its character ε is odd, and
    a_p = ε(p)a_p makes a_p = 0 wherever ε(p) = −1 [NAMED: Ribet 1977, on inner twists].
- **Where it ramifies** [READING; F3].
  - X11 has 165 nodes at 5, 55 at 7, and 1 at 11: the centre, where the eleven points coincide.
  - The lower pieces account for 164, 54 and 0 of them.
  - If each node is one ramified dimension, as at 5 and 7 in round 21, then the new piece is ramified at 5, 7 and 11.

| | prediction | dies if |
|---|---|---|
| Q1 | T11 = p⁵g(p), with g(p) an integer and \|g(p)\| ≤ 2p, at every prime from 13 to 401 | a prime fails |
| Q2 | g has complex multiplication. It vanishes exactly at the primes inert in one imaginary quadratic field K = Q(√−s), and 4p² − g(p)² is s times a square at the others | two fields, or none |
| Q3 | 5, 7 and 11 ramify in K: √−11 enters at 11, as √−7 entered at 7 | one of them does not |
| Q3′ | K = Q(√−1155). The signed square roots 3*, 5*, 7*, 11* multiply to −1155: the pattern 5, −35, 105 of 5, 7 and 9, continued | another field |
| Q4 | at the edge primes 5, 7 and 11, \|g(p)\| = p | another value |
| instrument | T1 = p, T3 = 0, T5 = (5\|p)p³, \|T7\| = p³\|c(p)\| and T9 = (105\|p)p⁵ at every prime from 13 to 401 | one fails |

**The drafter's expectation.**
- Q1 and Q2 hold.
- Q3 holds if the node reading does.
- Q3′ is a guess. Q(√−385), with 2 ramified in place of 3, fits the nodes just as well.

Run: `python edge_rule.py test22` (a few minutes, four processes at below-normal priority).

---

## Round 22 scores (added after the test, 2026-11-14)

Run by [`edge_rule.py`](edge_rule.py) `test22`, registered at c1dcfb4 before the test. Output:
[`edge_rule_test22.log`](edge_rule_test22.log).

**All five held, and so did the instrument.**

| | outcome | evidence |
|---|---|---|
| Q1 | held | T11 = p⁵g(p), with g(p) an integer and \|g(p)\| ≤ 2p, at all 74 primes from 13 to 401 |
| Q2 | held | g vanishes at exactly the 32 primes inert in Q(√−1155), and 4p² − g(p)² = 1155v² at the other 42 |
| Q3 | held | 5, 7 and 11 all ramify in Q(√−1155), and so does 3 |
| Q3′ | held | the field is Q(√−1155) |
| Q4 | held | g(5) = 5, g(7) = −7 and g(11) = 11 |
| instrument | held | the lower pieces at every prime from 13 to 401, and X7's form equal to 35.3.c.b at every prime to 97, the edges included |

**Read after the run** (not scores).
- Q(√−1155) has class number 8, and every class has order 2, one class in each genus. Q(√−35), the field at 7, has
  class number 2 and the same property. A rational weight-3 CM form needs a class group of exponent at most 2
  [NAMED: Schütt].
- The alternative the drafter named, Q(√−385), with 2 ramified in place of 3, died.

**Yield.**
- √−11 enters at 11, as √−7 entered at 7: the cubic in eleven variables carries a weight-3 form with complex
  multiplication by Q(√−1155).
- −1155 = (−3)·5·(−7)·(−11), the signed square roots of the odd primes up to 11. It continues the 5, −35 and 105 of
  5, 7 and 9.
- The nodes predicted where the new piece ramifies, and they were right at all three primes they can see.

---

## Round 23: the cubic in thirteen variables (registered 2026-11-14, before the test)

> *1 and 2, thirteen first* — the author, 14 November 2026. The "1" says yes to registering 13 next. The "2" says yes:
> 9 is two coins of 3 tossed together, so 3 enters only at its square.

X13 = {x1 + ⋯ + x13 = x1³ + ⋯ + x13³ = 0} is a cubic tenfold, and it has never been counted. Its primitive middle
cohomology has dimension 1366, with Hodge numbers 1, 220, 924, 220, 1 [FORCED: Griffiths' residues; the Jacobian
ring of a cubic in twelve variables has Hilbert series (1 + t)¹²]. By the Airy decomposition of rounds 21 and 22, with
m(13, ·) = 429, 572, 429, 208, 65, 12, 1,

  t13 = p⁵(429 + 429(5|p) + 65(105|p)) + 208p⁴c(p) + 12p⁴g(p) + p⁻²T13,

where c is X7's form, 35.3.c.b, and g is X11's, with complex multiplication by Q(√−1155).
- **Its size and shape** [FORCED; F4].
  - The lower pieces use 1363 of the 1366 dimensions, so the new piece V13 has three.
  - Sabbah and Yu's types for it are (5, 9), (7, 7) and (9, 5). In X13 the (7, 7) is one more Tate class, which brings
    h^(5,5) to 924 = 429 + 429 + 65 + 1, and the rest is the h^(7,3) = 1.
- **If it splits**, it is a twisted Tate class and a weight-5 form: T13 = χ(p)p⁷ + p⁵h(p).
  - A weight-5 form with rational coefficients has complex multiplication, because its character is odd, as at
    weight 3.
  - So h vanishes at the primes inert in a field K, and there T13 = χ(p)p⁷.
- **The nodes** [F3].
  - X13 has 715 nodes at 5, 286 at 7, 13 at 11, and 1 at 13: the centre.
  - The lower pieces fill all but one at each of these primes. So V13 has one ramified dimension at each of 5, 7, 11
    and 13: each ramifies in exactly one of χ and K.
- **3 at its square** (the author's "2").
  - 3 ramifies in V9 and V11, and not in V5 or V7.
  - Count the odd multiples of 9, as the nodes count the odd multiples of p: there is one up to 13. So 3 ramifies in
    exactly one of χ and K.
- **The pattern cannot sit in one field.**
  - The signed roots up to 13 multiply to −15015, but Q(√−15015) has class number 96 and exponent 12.
  - A rational weight-5 CM form needs a class group of exponent dividing 4 [NAMED: Schütt].
  - Of the 16 ways to share 3, 5, 7, 11 and 13 between an even χ and an imaginary K, 12 remain:
    (5, −3003), (13, −1155), (21, −715), (77, −195), (165, −91), (273, −55), (429, −35), (385, −39), (1001, −15),
    (1365, −11), (2145, −7) and (5005, −3), as (D_χ, d_K).
- **A guess from the base.** In [`../../base/SEVEN_AND_NINE.md`](../../base/SEVEN_AND_NINE.md) 13 is the icosahedron with
  its centre, and the icosahedron's field is Q(√5).
  - If the Tate class carries that solid face's √5, then χ = (5|p) and K = Q(√−3003), with 3003 = 3·7·11·13.
  - The 13-gon's √13 then goes into the form, with 3, 7 and 11.

| | prediction | dies if |
|---|---|---|
| S1 | T13 = p⁵u(p), with u(p) an integer and \|u(p)\| ≤ 3p², at every prime from 17 to 401 | a prime fails |
| S2 | V13 splits. There are a quadratic character χ and an imaginary quadratic field K = Q(√−s) such that u(p) = χ(p)p² at exactly the primes inert in K, and h(p) = u(p) − χ(p)p² has \|h(p)\| < 2p² and 4p⁴ − h(p)² = s·w² at the others | no such χ and K |
| S3 | each of 5, 7, 11 and 13 ramifies in exactly one of χ and K (the nodes) | one does not |
| S4 | 3 ramifies in exactly one of χ and K (3 at its square) | it ramifies in both or neither |
| S5 | χ is even, like (5\|p) and (105\|p), and 2 ramifies in neither, so D_χ·d_K = −15015 | otherwise |
| S6 | χ = (5\|p) and K = Q(√−3003): the icosahedron's √5 | another pair |
| S6′ | χ = (13\|p) and K = Q(√−1155): the new prime twists the Tate class, and the form keeps eleven's field | another pair |
| S7 | at the edge primes 5, 7, 11 and 13, T13 is the trace on the unramified part. Where q ramifies in K it is 0 or ±2q⁷; where q ramifies in χ it is q⁵h(q), with h(q) of K's CM shape | another value |
| instrument | T1 to T11 as found in rounds 19 to 22, at every prime from 17 to 401 | one fails |

**The drafter's expectation.**
- S1 holds.
- S2 holds if the piece splits, which Sabbah and Yu's types allow but do not force.
- S3 and S4 follow from S2, if the node reading holds. S5 is likely.
- S6 and S6′ are guesses, about one chance in twelve each.

The identification step was checked first on planted pieces with known answers ((5|p), (13|p) or trivial, beside
Q(√−35)'s weight-5 form), and on a control that does not split. Run: `python edge_rule.py test23` (a few minutes, four
processes at below-normal priority).

---

## Round 23 scores (added after the test, 2026-11-14)

Run by [`edge_rule.py`](edge_rule.py) `test23`, registered at 6403bfd before the test. Output:
[`edge_rule_test23.log`](edge_rule_test23.log).

**S1 held. S2 died, and S3 to S7 are void with it.**

| | outcome | evidence |
|---|---|---|
| S1 | held | T13 = p⁵u(p), with u(p) an integer and \|u(p)\| ≤ 3p², at all 73 primes from 17 to 401 |
| S2 | **failed** | p divides u(p) at none of the 73 primes. A twisted Tate class beside a CM form would make p divide u at the primes inert in the CM field, about half of them. So the piece does not split |
| S3 to S7 | void | they named the parts of a split that does not exist. The two guesses, S6 and S6′, are void with them |
| instrument | held | T1 to T11 at every prime from 17 to 401 |

**Read after the run** (not scores).
- **A symmetric square.** At every one of the 73 primes, u(p) + (−15015|p)p² = s_p·b_p², with b_p an integer and s_p a
  product of −1, 2, 3, 5, 11 and 13. Six quadratic characters decide which of them s_p holds:
  - −1 by (−15015|p), 2 by (−715|p), 3 by (5005|p);
  - 5 by (−3003|p), 11 by (−35|p) and 13 by (−1155|p);
  - 7 never.
  - So u(p) = a_p² − (−15015|p)p², with a_p = b_p√s_p. That is the trace of the symmetric square of a two-dimensional
    piece of weight 3 whose determinant has the character (−15015|p).
- [READING] **What the piece is.**
  - The Airy pieces carry an orthogonal pairing, and a three-dimensional orthogonal piece is a twisted symmetric
    square [NAMED: SO(3) ≅ PGL(2), and Tate's lifting of projective representations].
  - Its two-dimensional root behaves like a weight-3 form with character (−15015|p) and inner twists by the five
    other characters, with coefficients in Q(√−1, √2, √3, √5, √11, √13).
  - Two of those twists are the CM fields of 7 and 11.
  - It is ordinary at every prime tested, which a CM piece is not.
- **The pattern lives on, in the determinant.** −15015 = (−3)·5·(−7)·(−11)·13 is the product of the signed square
  roots up to 13.
  - Schütt's condition forbids it as a CM field. It appears as the determinant's character, as (5|p), (−35|p) and
    (105|p) did at 5, 7 and 9.
  - At 7 the form's character is (−35|p) (LMFDB).
- **The edges.** T13(5) = 0, T13(7) = 32·7⁵, T13(11) = 0 and T13(13) = 182·13⁵.
- **3** ramifies in the piece, since its determinant's character does. So 3 is in V9, V11 and V13, and not in V5 or V7.
  That was read after the run, so the author's "3 at its square" agrees with 13 but was not tested there.

**Yield.** The coin at 13 does not split as 5, 7, 9 and 11 did. Its piece is a symmetric square, and the signed roots'
pattern moves into its determinant.

---

## Round 24: thirteen's symmetric square, blind, and the cubic in fifteen variables (registered 2026-11-14, before the test)

> *1 and 2, thirteen first* — the author, 14 November 2026. The "2": 9 is two coins of 3 tossed together, so 3 enters
> only at its square.

Round 23's read counts for nothing until it is tested blind. This round tests it at primes no count of X13 has seen.
It also tests the author's "3 at its square" where the nodes say the most: in fifteen variables.

- **Thirteen.** R1 restates the read exactly, with its six characters fixed.
- **Fifteen** [FORCED: F3 and F4].
  - X15 = {Σx = Σx³ = 0} in fifteen variables has never been counted.
  - Its new piece V15 has two dimensions, of Hodge types (7, 9) and (9, 7), and it is orthogonal. A two-dimensional
    orthogonal piece with two different Hodge types has complex multiplication [NAMED: Livné]. So T15 = p⁷w(p), with w
    a weight-3 CM form.
- **The nodes of X15.**
  - X15 has 3004 nodes at 5, 1365 at 7, 105 at 11 and 15 at 13. The lower pieces leave 2 at 5, and 1 at each of 7, 11
    and 13.
  - 5 counts twice, because 5 and 15 are both odd multiples of 5. So at 5 both dimensions ramify: the Hecke character
    ramifies there, and the field does not.
  - At 7, 11 and 13 the field ramifies, and the Hecke character does not.
- **3 at its square.** There is one odd multiple of 9 up to 15, so 3 ramifies in the field.
- **Only one field fits.**
  - Of the fields ramified at 7, 11 and 13 (and perhaps 3 or 2) and not at 5, only Q(√−3003) has a class group of
    exponent at most 2, as a rational weight-3 CM form needs [NAMED: Schütt]. Its class number is 8.
  - Without 3 the field would be Q(√−1001), of discriminant −4004 (exponent 10), or Q(√−2002), −8008 (exponent 4).
    With both 3 and 2 it would be Q(√−6006), −24024 (exponent 8).
  - So at 15 the node reading and Schütt's condition force 3 in by themselves. F3 tests the author's reading together
    with the node reading, not apart from it.
- **The edges.** T15(5) = 0. At 7, 11 and 13, |T15(q)| = q⁸, the trace on the one unramified line.

| | prediction | dies if |
|---|---|---|
| R1 | at every prime from 409 to 601, T13 = p⁵u(p), with u(p) an integer and \|u(p)\| ≤ 3p², and u(p) + (−15015\|p)p² = s_p·b² with b an integer and s_p given by round 23's six characters | a prime fails |
| F1 | T15 = p⁷w(p), with w(p) an integer and \|w(p)\| ≤ 2p, at every prime from 17 to 401 | a prime fails |
| F2 | w has complex multiplication by one imaginary quadratic field | two fields, or none |
| F3 | that field is Q(√−3003) | another field |
| F4 | T15(5) = 0, and \|T15(q)\| = q⁸ at q = 7, 11 and 13 | another value |
| instrument | T1 to T11 as found in rounds 19 to 22, and T13 by round 23's read, at every prime from 17 to 401 | one fails |

**The drafter's expectation.**
- R1 holds: the read rests on 73 primes and six characters.
- F1 and F2 hold.
- F3 holds if the node reading does.
- F4 holds if the counts at the nodes see only the unramified part, as in round 21.

Run: `python edge_rule.py test24` (a few minutes, four processes at below-normal priority).

---

## Round 24 scores (added after the test, 2026-11-14)

Run by [`edge_rule.py`](edge_rule.py) `test24`, registered at c9fb158 before the test. Output:
[`edge_rule_test24.log`](edge_rule_test24.log).

**All five held, and so did the instrument.**

| | outcome | evidence |
|---|---|---|
| R1 | held | thirteen's symmetric square, u(p) + (−15015\|p)p² = s_p·b², at all 32 primes from 409 to 601, with the six characters fixed in advance |
| F1 | held | T15 = p⁷w(p), with w(p) an integer and \|w(p)\| ≤ 2p, at all 73 primes from 17 to 401 |
| F2 | held | w vanishes at exactly the 44 primes inert in one field, and 4p² − w(p)² = 3003v² at the other 29 |
| F3 | held | the field is Q(√−3003) |
| F4 | held | T15(5) = 0, and T15(q) = −q⁸ at q = 7, 11 and 13 |
| instrument | held | T1 to T13 at every prime from 17 to 401 |

**Yield.**
- Thirteen's piece is a twisted symmetric square, now held blind. The signed roots' product −15015 is its determinant's
  character.
- Fifteen's piece is a weight-3 form with complex multiplication by Q(√−3003), with −3003 = (−3)·(−7)·(−11)·13.
  - 5 stays out of the field: its two ramified dimensions are the Hecke character's, because 5 and 15 are both odd
    multiples of 5.
  - 3 is in, as the author's "3 at its square" says. At 15 the node reading forces it as well.

---

## Round 25: seventeen, the reading at 13, and the prime 3 (registered 2026-11-15, before the test)

> *1 and 3, seventeen first* — the author, 15 November 2026. The "1" says yes to registering 17. The "3" takes up the
> reading at 13: its piece is both faces at once, and the base puts 13 at the icosahedron with its centre.

X17 = {x1 + ⋯ + x17 = x1³ + ⋯ + x17³ = 0} is a cubic fourteenfold, and it has never been counted. Its primitive middle
cohomology has dimension 21846. With m(17, ·) = 4862, 7072, 6188, 3808, 1700, 544, 119, 16, 1 and the pieces found so
far,

  t17 = p⁷(4862 + 6188(5|p) + 1700(105|p)) + p⁶(3808c(p) + 544g(p) + 16w(p)) + p⁵(119u13(p) + u(p)),

where c, g and w are the CM forms of 7, 11 and 15, u13 is 13's symmetric square, and u(p) = T17(p)/p⁷ is the new piece.
Before this registration [`edge_rule.py`](edge_rule.py) `verify25` checked the following, without counting X17, X21 or
anything at 3 ([`edge_rule_verify25.log`](edge_rule_verify25.log), F6 to F8 [FORCED]).
- **Seventeen's size and shape.**
  - The lower pieces use 21843 of the 21846 dimensions, so the new piece V17 has three, of Hodge types (7, 11), (9, 9)
    and (11, 7): 13's shape, raised by two.
  - It is orthogonal. So at every prime it has the eigenvalue δ(p)p⁹, where δ is its determinant's character, and its
    other two eigenvalues add up to at most 2p⁹ in size. Wherever |u| > p², the sign of u is δ(p).
- **The nodes.** X17 has 12393 nodes at 5, 6188 at 7, 680 at 11, 136 at 13 and 1 at 17, its centre. The lower pieces
  leave 2 at 5, because 5 and 15 are both odd multiples of 5, and 1 at each of 7, 11, 13 and 17.
- **The prime 3, in a good model.** On x1 + ⋯ + xn = 0 the cubic x1³ + ⋯ + xn³ is 3e3, three times the third
  elementary symmetric function. So over the 3-adic integers X_n = {e1 = e3 = 0}, and this model can be counted at 3,
  where the cubic itself is the cube of the line and was never counted.
  - Mod 3 its only singular points are the sign vectors whose sum is a multiple of 9 (brute force to n = 11), and each
    is an ordinary node (n = 9 to 27).
  - There are none for n ≤ 7. For n = 9 the centre is the only one: the cubic in nine variables pinches at its centre
    mod 3, as the cubic in q variables does mod q for every prime q. The author's "3 at its square" is where this
    model's nodes are.
  - X17 has 2380 of them, and the lower pieces leave 1 for V17.
  - At a node whose sum is 9, the critical value has 3-adic valuation 1, so the total space is regular there and the
    node is one ramified dimension. At 27 the valuation is 2. That node would not ramify: a prediction for 27, past
    this round.
- **The parity rule** [READING: Picard–Lefschetz].
  - Each ramified dimension at a node turns one vanishing cycle over. So a piece's determinant character is ramified
    exactly where the piece has an odd number of them.
  - The rule gives every determinant already read: (5|p), (−35|p), (105|p), (−1155|p), (−15015|p) and (−3003|p),
    at 5 to 15.
  - At 17 it gives (−51051|p), with 51051 = 3·7·11·13·17: 3 once (at 9), 5 twice (so not at all), and 7, 11, 13 and 17
    once.
  - At 17 no new multiple of 3 appears, so Z2 checks that the rule still holds at 3 with nothing else forcing it, as
    Schütt's condition did at 15. The direct test of "3 at its square" is Z5, at the prime 3 itself.

**The reading at 13, made exact** (the drafter's version, which the author's "3" took up).
- A three-dimensional orthogonal piece either keeps a line or keeps none.
  - If it keeps one, it splits into a twisted Tate class and a CM form, as round 23 registered for 13. Its Galois group
    then turns the piece about one axis, as a regular polygon's symmetries do.
  - If it keeps none, as at 13 (round 23's S2 died), no axis serves all its elements, as with the icosahedron's
    symmetries. These are the two kinds in Klein's list of the finite rotation groups. The cyclic and dihedral groups
    keep an axis; the tetrahedral, octahedral and icosahedral groups keep none [NAMED: Klein; SO(3) ≅ PGL(2)].
- The base's rule, carried on to 21 [F6]:
  - 13 is the icosahedron with its centre (120 symmetries, no axis kept);
  - 17 is the regular 17-gon (68, one axis). Its best in space is the 15-gon with two poles, which keeps its axis too;
  - 21 is the dodecahedron with its centre (120, no axis).
- **The dictionary:** the piece of n keeps a line exactly when the base's n points keep an axis.
  - At 13 it fits, but that was read after the fact.
  - At 17 it predicts a split: the first test of the reading. 17 has 13's Hodge shape, but the base turns flat there.
  - At 21 it predicts no split.
- **Twenty-one.**
  - X21 in 21 variables has a new piece V21 of three dimensions, of types (9, 13), (11, 11) and (13, 9).
  - Its nodes leave one ramified dimension at each of 3, 11, 13, 17 and 19, and two at 5 (5, 15) and at 7 (7, 21).
  - The parity rule gives (−138567|p), with 138567 = 3·11·13·17·19. 7 drops out as 5 did at 15, and 3 enters once,
    at 9 and not at 21.
  - The counts reach p = 113 before they leave 64-bit integers.

| | prediction | dies if |
|---|---|---|
| Z1 | T17 = p⁷u(p), with u(p) an integer and \|u(p)\| ≤ 3p², at every prime from 19 to 401 | a prime fails |
| Z2 | V17's determinant has the character (−51051\|p): wherever \|u(p)\| > p², sign u(p) = (−51051\|p) | a sign fails |
| Z3 | the reading: V17 keeps a line. There are a quadratic character χ and an imaginary quadratic field K such that u(p) = χ(p)p² exactly at the primes inert in K, and u − χ(p)p² is a weight-5 form with complex multiplication by K | no such χ and K |
| G1 | if Z3 holds: χ = (17\|p) and K = Q(√−3003). The new prime twists the Tate class, as 5 did at 5, and the form keeps fifteen's field | another pair |
| Z3′ | the shape: V17 keeps no line. p divides u(p) at no more than 3 primes, and u(p) + (−51051\|p)p² = ±s·b² with b an integer and s dividing 510510 = 2·3·5·7·11·13·17, at every prime | otherwise |
| Z4 | at the nodes: T17(5) = ±5⁹, since one line survives at 5. At 7, 11, 13 and 17 a plane survives: q⁷ divides T17(q), and \|T17(q)\| ≤ 2q⁹ | another value |
| Z5a | at 3, in the good model, where nothing has been counted: T1 = 3, T3 = 0, T5 = (5\|3)·3³ = −27 and T7 = 3³a₃ = 27, with a₃ = 1 the coefficient of 35.3.c.b. 3 does not enter below 9 | another value |
| Z5b | T9 = 0 at 3: V9's line ramifies there | T9 ≠ 0 |
| Z5c | from 9 on, one dimension at a time: \|T11\| = 3⁶ and \|T15\| = 3⁸ (a line survives in each CM plane), and a plane survives in V13 and V17: T13 = 3⁵v and T17 = 3⁷v′, with v and v′ integers of size at most 18 | another value |
| D1 | T21 = p⁹u21(p), with u21(p) an integer and \|u21(p)\| ≤ 3p², at every prime from 23 to 113 | a prime fails |
| D2 | V21's determinant has the character (−138567\|p), read by the same signs | a sign fails |
| D3 | the reading: V21 keeps no line. p divides u21(p) at no more than 2 primes, and the split test of Z3 finds no χ and K | it splits |
| instrument | T1 to T15 as found in rounds 19 to 24, at every prime counted; and the good model's count equals brute force over F_3^n for n = 3, 5, 7 and 9 | one fails |

Z3 and Z3′ cannot both hold.

**The drafter's expectation.**
- Z1, Z2, D1 and D2 hold, if the parity rule does.
- Of Z3 and Z3′ the drafter expects Z3′, since 17 has 13's Hodge shape. So the drafter expects the dictionary to die at
  its first test. A split at 17 would be its first blind success. G1 is a guess among several pairs.
- Z4 holds if the counts at the nodes see only the unramified part, as in rounds 21 and 24.
- Z5 holds if the good model at 3 is what F7 says. Z5a is the sharpest item: four exact values at a prime where nothing
  has been counted.
- D3 holds, but it cannot separate the dictionary from the shape, which agree at 21.

**The literature gate (15 November 2026).**
- No work found identifies the Airy pieces past k = 9: not Haessig, not Sabbah and Yu, and not Qin, who computes
  Hodge numbers [NAMED: arXiv:2302.05365].
- P.-H. Chuang's dissertation (arXiv:2607.05757, July 2026) gives an arithmetic Picard–Lefschetz formula for diagonal
  singularities and applies it to the Airy moments at primes p > 5. It works in another model, z³ = Σ(y³/3 − y), and
  excludes 3 and 5. The good model at 3 and the parity rule are not in the parts of it read here. The node reading at
  p ≥ 7 may be, which has not been checked.

Run: `python edge_rule.py test25` (a few minutes, four processes at below-normal priority).

---

## Round 25 scores (added after the test, 2026-11-15)

Run by [`edge_rule.py`](edge_rule.py) `test25`, registered at 5be432c before the test. Output:
[`edge_rule_test25.log`](edge_rule_test25.log).

**The reading's exact version died at 17. "3 at its square" held at the prime 3, and the parity rule held at 17.**

| | outcome | evidence |
|---|---|---|
| Z1 | held | T17 = p⁷u(p), with u(p) an integer and \|u(p)\| ≤ 3p², at all 72 primes from 19 to 401 |
| Z2 | held | \|u(p)\| > p² at 16 primes, and sign u(p) = (−51051\|p) at all 16. With 3 left out, (17017\|p), 10 of the 16 would be wrong |
| Z3 | **failed** | p divides u(p) at only 2 of the 72 primes, 23 and 113, and no CM field fits. So V17 keeps no line, though the 17-gon keeps its axis. The dictionary dies at its first test |
| G1 | void | it named the parts of a split that does not exist |
| Z3′ | held | V17 keeps no line, and u(p) + (−51051\|p)p² = ±s·b², with s dividing 510510, at all 72 primes. It is a twisted symmetric square, like 13's |
| Z4 | held | T17(5) = −5⁹. T17(7) = 72·7⁷, T17(11) = 234·11⁷, T17(13) = 0 and T17(17) = 493·17⁷ |
| Z5a | held | at 3: T1 = 3, T3 = 0, T5 = −27 and T7 = 27, the value of LMFDB's a₃ = 1 at a prime where nothing had been counted |
| Z5b | held | T9 = 0 at 3 |
| Z5c | held | at 3: T11 = 3⁶, T15 = −3⁸, T13 = −8·3⁵ and T17 = 16·3⁷ |
| D1 | held | T21 = p⁹u21(p), with u21(p) an integer and \|u21(p)\| ≤ 3p², at all 22 primes from 23 to 113 |
| D2 | not held | only 3 primes had \|u21(p)\| > p², and the test's code asked for at least 5. All three signs agree with (−138567\|p). It is counted as not held |
| D3 | held | p divides u21(p) only at 73, and there is no split |
| instrument | held | T1 to T15 at every prime counted, and the good model's count equals brute force over F_3^n for n = 3, 5, 7 and 9 |

**Read after the run** (not scores).
- **Seventeen's square classes.** s_p is a product of −1, 2, 5, 7, 13 and 17, and six characters decide which:
  - −1 by (−51051|p), the determinant's own, as at 13;
  - 2 by (−715|p), as at 13;
  - 5 by (−1547|p), with 1547 = 7·13·17, and 7 by (−12155|p), with 12155 = 5·11·13·17;
  - 13 by (−35|p) and 17 by (−3003|p);
  - 3 and 11 never.
- **Twenty-one's.** u21(p) + (−138567|p)p² = ±s·b², with s dividing 9699690 = 2·3·…·19, at all 22 primes.
  - A wrong character would almost never pass that test, so D2's character is right, though not by the registered
    test.
  - The classes: −1 by (−138567|p), 2 by (−19019|p), 3 by (−143|p), 5 by (−1547|p), 17 by (−1155|p) and 19 by
    (−3003|p); 7, 11 and 13 never.
- **The lower fields return as twists.**
  - The CM fields of 7, 11 and 15 decide square classes of the higher pieces' roots: (−35|p) at 13 and 17, (−1155|p)
    at 13 and 21, and (−3003|p) at 13, 17 and 21.
  - (−715|p) serves both 13 and 17, and (−1547|p) both 17 and 21.
- **Zeros.** u(p) + (−51051|p)p² = 0 at 23 and 113, and u21(p) + (−138567|p)p² = 0 at 73: the root's coefficient
  vanishes there.
- **At 3, past the registration.** T19 = −17·3⁷ and T21 = 3⁹.

**Yield.**
- The author's "3 at its square" held at the prime 3 itself, where nothing had been counted.
  - The good model e1 = e3 = 0 pinches exactly at the sign vectors whose sum is a multiple of 9.
  - The pieces below 9 keep their values there, −27 and LMFDB's a₃ = 1.
  - V9's line ramifies at 3, and from 9 on each piece loses exactly one dimension there.
- The parity rule held blind at 17: the determinant's character is (−51051|p).
- The reading's exact version died. 17's piece keeps no line, although the 17-gon keeps its axis.
  - 17 and 21 are the same kind as 13, so "both at once" is not 13's alone.
  - It belongs to the three-dimensional pieces, not to the icosahedron.

---

## Round 26: twenty-seven first, and the square classes blind (registered 2026-11-15, before the test)

> *2 and 3, 27 first* — the author, 15 November 2026. The "2" asks for the sharpened rule at 25 and 27, where 27 is
> three coins of 3, with 27 first. The "3" says yes to testing seventeen's square classes blind.

**The rule under test** (round 25, §10 of [`COIN_AT_FIVE.md`](COIN_AT_FIVE.md), read from the critical values).
- A node ramifies only when its critical value has odd valuation: v_p(j) for p from 5 on, and v_3(j) − 1 for 3.
- So 3 enters at 9 but not at 27, its cube: three coins of 3. And 5 enters at 5 and 15 but not at 25, its square: two
  coins of 5.
- The first pieces where this matters are V25 and V27. The centre of X25 pinches mod 5 with valuation 2. The centre
  of X27 pinches mod 3 with valuation 2, and 27 nodes of X27 (sum 25) pinch mod 5 with valuation 2.

Before this registration [`edge_rule.py`](edge_rule.py) `verify26` checked the following, without counting X23, X25,
X27, or any cubic in 13 or more variables over a field of p² elements
([`edge_rule_verify26.log`](edge_rule_verify26.log), F9 to F12 [FORCED]).
- **A faster counter** (F11). The convolution of rounds 19 to 25 stops at 21 variables.
  - N_n = q⁻² Σ_(s,t) S(s, t)ⁿ, where S is the cubic exponential sum over F_q. Only s = 0 and s = 1 are needed, since
    S(s, t) = S(1, t/s³).
  - The sums are taken mod primes l ≡ 1 (mod p) and joined by the Chinese remainder theorem.
  - It equals the old count for every odd n up to 21 at p = 23, 29, 31, 101 and 113.
  - Over the field of p² elements it equals a direct count at 25 and 49 elements, and it gives the squares of the known
    pieces' eigenvalues at 29 and 31 (n ≤ 11).
  - It reaches 27 variables at every prime to 1999, and fields of p² elements to p = 151, in minutes.
- **The four-dimensional pieces** (F12). V19, V23 and V27 have four dimensions each, all of one shape: Hodge types
  (a, a + 6), (a + 2, a + 4), (a + 4, a + 2) and (a + 6, a), with a = 7, 9 and 11. V25 has five, with a middle class.
- **Reading a determinant prime by prime** (F10).
  - With e2 = (T(p)² − T(p²))/2, an orthogonal piece of dimension 4 has determinant −1 at p only if e2 = 0.
  - In dimension 3, e2 = det(p)·p^(w/2)·T(p), with w the weight.
  - So the counts over F_p and over the field of p² elements read the determinant at each prime, with no sign test.
- **The infinite place** (F9).
  - Complex conjugation swaps each pair of Hodge types. It gives the sign of every determinant already read: + with a
    middle class at 1, 5 and 9, and − with one pair at 7, 11, 13 and 15.
  - A four-dimensional piece of this shape has two pairs and no middle class, so its determinant is even: (D|p) with
    D > 0.
  - Four readings of V27 are possible, with 3 at 27 and 5 at 25 each counted as thin or as naive. They give
    D = 3187041 (both thin), 15935205 (5 enters at 25), −1062347 (3 enters at 27) and −5311735 (both enter).
  - The two that let 3 enter at 27 are odd. So the infinite place, with the nodes' parity, already says 3 does not
    enter at its cube, and the count checks it. The open choice is 5 at 25.
- **The controls.**
  - V23 has no thick node. The thin rule gives it the same determinant as V27, (3187041|p), with
    3187041 = 3·11·13·17·19·23. So V27's determinant equal to V23's says the thick nodes add nothing.
  - V19's determinant is (969969|p), with 969969 = 3·7·11·13·17·19.
- **Twenty-one.** Round 25's sign test could not score V21's determinant (D2). Here it is read prime by prime (Y4).
- **The square classes** of seventeen and twenty-one were read after round 25. They are tested at new primes (R2, R3).

| | prediction | dies if |
|---|---|---|
| Y1 | T27 = p¹¹u27(p), with u27(p) an integer and \|u27(p)\| ≤ 4p³, at every prime from 29 to 1999 | a prime fails |
| Y2 | V27's determinant is (3187041\|p): e2 = 0 exactly at the primes where (3187041\|p) = −1, at every prime from 29 to 151. 3 does not enter at 27, and 5 does not enter at 25 | another pattern |
| Y2′ | wherever \|u27(p)\| > 2p³ the determinant must be +1, and (3187041\|p) = +1 there, with at least 10 such primes | a prime fails, or fewer than 10 |
| Y3 | the controls: V23's determinant is (3187041\|p) and V19's is (969969\|p), read the same way; and T23 = p⁹u23, T19 = p⁷u19, with integers \|u\| ≤ 4p³ | otherwise |
| Y4 | V21's determinant is (−138567\|p) at every prime from 29 to 151: T21(p²) = T21(p)² − 2(−138567\|p)p¹¹T21(p) | a prime fails |
| Y5 | V27 does not split into two CM planes: p divides u27(p) at no more than 3 primes | more |
| W1 | twenty-five: T25 = p⁹u25(p), with u25(p) an integer and \|u25(p)\| ≤ 5p⁴; and wherever \|u25(p)\| > 3p⁴ the middle eigenvalue has the sign (3187041\|p), 5 left out at 25, with at least 5 such primes | a sign fails, or fewer than 5 |
| R2 | seventeen's square classes: at every prime from 409 to 1999, u17(p) + (−51051\|p)p² = s_p·b², with b an integer and s_p the product of −1 by (−51051\|p), 2 by (−715\|p), 5 by (−1547\|p), 7 by (−12155\|p), 13 by (−35\|p) and 17 by (−3003\|p) | a prime fails |
| R3 | twenty-one's: at every prime from 127 to 1999, u21(p) + (−138567\|p)p² = s_p·b², with −1 by (−138567\|p), 2 by (−19019\|p), 3 by (−143\|p), 5 by (−1547\|p), 17 by (−1155\|p) and 19 by (−3003\|p) | a prime fails |
| instrument | T1 to T15 as found, at every prime; seventeen's symmetric square at 29 to 401; over the field of p² elements, the known pieces are the squares of their eigenvalues, which rereads the determinants of 7, 11, 13, 15 and 17 | one fails |

**The drafter's expectation.**
- Y1, Y3, Y4, R2 and R3 hold.
- Y2 holds. The critical values make both thick nodes unramified, and the infinite place already forbids 3 at 27. Its
  open half is 5 at 25.
- Y2′ and W1 may see few signs, W1 especially.
- Y5 holds: the drafter expects V27 to be unsplit, like the pieces from 13 to 21.
- The literature gate of round 25 covers this round: no work found identifies any Airy piece past k = 9.

Run: `python edge_rule.py test26` (a few minutes, four processes at below-normal priority).

---

## Round 26 scores (added after the test, 2026-11-15)

Run by [`edge_rule.py`](edge_rule.py) `test26`, registered at afc4e76 before the test. Output:
[`edge_rule_test26.log`](edge_rule_test26.log).

**The sharpened rule held at 27, prime by prime: 3 does not enter at its cube, and 5 does not enter at its square.**

| | outcome | evidence |
|---|---|---|
| Y1 | held | T27 = p¹¹u27(p), with u27(p) an integer and \|u27(p)\| ≤ 4p³, at all 294 primes from 29 to 1999 |
| Y2 | held | e2 = 0 exactly where (3187041\|p) = −1, at all 27 primes from 29 to 151. The rivals fit 14 ("5 enters at 25"), 13 ("3 enters at 27") and 12 (both) of the 27, about what chance gives |
| Y2′ | not held | \|u27(p)\| > 2p³ at only 8 primes, and the test asked for 10. All 8 have (3187041\|p) = +1, and the rival "5 enters at 25" is wrong at all 8 |
| Y3 | held | V23's determinant is (3187041\|p), the same as V27's, and V19's is (969969\|p), at all 27 primes. Both have the predicted shape at all 294 |
| Y4 | held | V21's determinant is (−138567\|p) at all 27 primes: round 25's D2, now read directly |
| Y5 | held | p divides u27(p) at none of the 294 primes |
| W1 | not held | V25 has the predicted shape at all 294 primes, but \|u25(p)\| > 3p⁴ at only 1, where 5 were asked. That one sign agrees with (3187041\|p) and not with the rival |
| R2 | held | seventeen's square classes, by the six characters fixed after round 25, at all 224 primes from 409 to 1999 |
| R3 | held | twenty-one's, by its six characters, at all 273 primes from 127 to 1999 |
| instrument | held | T1 to T15 at all 294 primes; seventeen's symmetric square at 29 to 401; over the field of p² elements the known pieces are the squares of their eigenvalues at all 27 primes, which rereads the determinants of 7, 11, 13, 15 and 17 |

**Read after the run** (not scores).
- **Twenty-five's own determinant.** At each prime counted over the field of p² elements, T25(p) and T25(p²) with the
  circle (every eigenvalue of modulus p¹³) allow one sign or both.
  - One sign only at 7 of the 27 primes. All 7 agree with (3187041|p), 5 left out at 25. The rival agrees at 3.
  - So 5 stays out of V25 too, on the evidence read here. A registered test would need T25(p³), from the field of p³
    elements.
- [READING] **Where the four-dimensional pieces live.** V27 has no line (no middle class) and no CM plane (Y5), so it
  is irreducible.
  - An irreducible orthogonal piece of dimension 4 whose determinant is (D|p) becomes, over Q(√D), a tensor product of
    two two-dimensional pieces that Galois swaps.
  - So V23 and V27 live over Q(√3187041), and V19 over Q(√969969), as tensor squares of a piece of weights 3 and 5.

**Yield.**
- The author's coins, at the cube and the square.
  - 3 enters at 9, two coins of 3, and not at 27, three coins. 5 enters at 5 and 15 and not at 25, two coins of 5.
  - V27's determinant, read at each prime, is (3187041|p), the same as V23's, which has no thick node. So the thick
    nodes at 25 and 27 add nothing.
  - The infinite place had already ruled out 3 at 27. The count decided 5 at 25 against three rivals.
- Twenty-one's determinant, which round 25 could not score, held prime by prime.
- Seventeen's and twenty-one's square classes held blind at 224 and 273 new primes.

---

## Round 27: eighty-one first, and twenty-five's own determinant (registered 2026-11-15, before the test)

> *1 and 3, 81 first* — the author, 15 November 2026. The "1" asks for 81, four coins of 3, where the rule says 3
> enters again. The "3" asks for a registered test of twenty-five's own determinant, from the field of p³ elements.

**What the rule says at 81.** The centre of X81 pinches mod 3 with valuation 3 in the good model (v_3(81) − 1). That
is odd, so 3 enters at 81. For 3 the count starts one coin late, so four coins count as three.

Before this registration [`edge_rule.py`](edge_rule.py) `verify27` checked the following, without counting a cubic in
more than 27 variables, or any cubic in 17 or more variables over the field of p³ elements
([`edge_rule_verify27.log`](edge_rule_verify27.log), F13 to F18 [FORCED]).
- **The Hodge types, from the cubics alone** (F13).
  - A smooth cubic of dimension n − 3 has primitive Hodge numbers C(n − 1, 2n − 5 − 3a) [NAMED: Griffiths, from the
    Fermat cubic].
  - Peeling off the lower pieces by the ballot triangle leaves every V_k up to k = 201 with exactly Sabbah and Yu's
    classical types, each once.
  - So V79 has 14 types in 7 pairs, and V81 has 13: 6 pairs and the middle class (41, 41).
- **The infinite place decides 81** (F14).
  - The only node new at 81 is the centre, which pinches only mod 3. Every other node keeps its local equation, so
    D81/D79 can only be −3 or 1.
  - V79's determinant is odd and V81's is even, with the middle class at +1 as at every k read. So D81/D79 = −3, and
    3 enters at 81.
  - This is the thin rule's answer, decided before any count, as 27 was in round 26. No count can read it directly:
    V81 has 13 dimensions, and its determinant needs the traces up to the seventh power of Frobenius at primes past
    81.
- **Every k** (F15).
  - At every odd k up to 20001, the thin rule's determinant has the sign the Hodge types require. Both change sign
    exactly at k ≡ 7, 9 and 11 (mod 12).
  - Why. From k − 2 to k the thin rule's symbol gains the factor k, or k/3 when 3 divides k. Its sign changes by
    χ₋₄(k)·(−1)^[3 | k], which is −1 exactly at those residues.
  - The Hodge side: V_k has ⌈k/6⌉ types, one fewer when 3 divides k, and a middle class exactly when k ≡ 1 (mod 4).
    The number of pairs changes parity at the same residues.
  - So at every power of a prime l ≡ 3 (mod 4), the infinite place alone decides whether l enters, and it agrees with
    the thin rule. 3 enters at its even powers (9, 81, 729, 6561). The other such primes enter at their odd powers:
    7 and 343, but not 49 or 2401.
  - At primes l ≡ 1 (mod 4) the signed prime l* is positive, so the infinite place is blind there, and their coins
    must be counted. Twenty-five is the first. It is also the only one in reach, since V125 has 21 dimensions.
- **One symbol** (F16).
  - The thin rule says V_k's determinant is the Jacobi symbol (p/A_k), where A_k is the product of the odd numbers up
    to k, each multiple of 3 divided by 3 once.
  - For Kloosterman moments Yun proved the same shape, (p/d!!) [NAMED: Z. Yun, Compositio 2015, Theorem 1.2.3].
  - The two differ only by the cube's 3.
- **The counter over the field of p³ elements** (F17, F18).
  - S(1, t) for every t at once is a Fourier transform over (Z/p)³. It runs exactly in floating point, mod primes
    below 2²¹.
  - It equals round 26's counter over F_p and F_(p²) for every odd n up to 27 (p = 29, 31 and 101).
  - It equals a direct count over the fields of 125 and 343 elements.
  - At 29 and 31 it gives the cubes of the known pieces' eigenvalues (n ≤ 15 only).
  - With e1, e2 and e3 read from the traces of Frobenius, its square and its cube, and P = p^((k+1)/2): e3 = det·P³
    in dimension 3, e3 = det·P²·e1 in dimension 4, and e3 = det·P·e2 in dimension 5.

| | prediction | dies if |
|---|---|---|
| Q1 | eighty-one, counted: every new piece from V29 to V81 has its forced shape at every prime from 83 to 1999. T_k = p^h·u, with h the lowest type, u an integer and \|u\| ≤ d·p^((k+1)/2 − h) | a prime fails |
| Q2 | ordinary: for each k from 29 to 81, p divides u at no more than 5 of the 281 primes | more, for some k |
| Q3 | V79 and V81 have big orthogonal images. With x = T_k/p^((k+1)/2) over the 281 primes, the mean of x² is between 0.75 and 1.25, and the mean of x⁴ between 1.8 and 4.5. The full orthogonal group gives 1 and 3; a split piece gives x² near 2 or more | outside |
| Z1 | twenty-five's own determinant is (3187041\|p): e3 = (3187041\|p)·p¹³·e2 exactly, at every prime from 29 to 151 with e2 ≠ 0, so 5 does not enter at 25. At least 20 such primes, with at least 8 where (5\|p) = −1, where the rival (15935205\|p) differs | a prime fails, or too few |
| Z2 | a second reading of the four-dimensional pieces: e3 = det·p^(k+1)·e1, with det (3187041\|p) for V27 and V23 and (969969\|p) for V19, at every prime from 29 to 151 with e1 ≠ 0 (at least 20 for each) | a prime fails, or too few |
| instrument | over F_p at 83..1999: T1 to T15 as found, and seventeen's and twenty-one's square classes. Over F_(p²) at 29..151 the known pieces are the squares of their eigenvalues; over F_(p³), their cubes, which rereads the determinants of 7, 11, 13, 15, 17 and 21 | one fails |

**The drafter's expectation.**
- All hold.
- Q1 is Mazur's bound (Newton above Hodge) read through the counter, so its risk is the counter at 81 variables.
- Q2 is a guess: no piece up to 27 was ever found non-ordinary.
- Q3 expects the full orthogonal group, as for every piece measured so far.
- Z1: round 26's circle reading decided 7 primes, all for (3187041|p).
- The coin at 81 is not scored, because it is forced (F14).
- **Literature gate.**
  - No work found gives the determinants of the Airy moments.
  - The closest precedent is Yun's theorem for Kloosterman moments. Their determinant is (p/d!!). He expected the
    three-dimensional cases to come from modular forms, and the four-dimensional ones from Hilbert modular forms over
    the determinant's real quadratic field. This is the shape found here at 13, 17 and 21, and at 19, 23 and 27.
  - Also checked: Sabbah–Yu (2023), Qin (2024), Chuang (2026), Haessig (2008), and Katz–Rojas-León–Tiep on Airy
    sheaves, whose determinants are the sheaves' own, a different object.

Run: `python edge_rule.py test27` (minutes; four processes at below-normal priority).

---

## Round 27 scores (added after the test, 2026-11-15)

Run by [`edge_rule.py`](edge_rule.py) `test27`, registered at b8e5fde before the test. Output:
[`edge_rule_test27.log`](edge_rule_test27.log).

**Five of five held. Twenty-five's own determinant is (3187041|p) at every prime counted: 5 does not enter at 25,
its square. At 81 the infinite place had already decided that 3 enters, four coins of 3.**

| | outcome | evidence |
|---|---|---|
| Q1 | held | every piece from V29 to V81 has its forced shape at all 281 primes from 83 to 1999 (and V17 to V27 beside them) |
| Q2 | held | p divides u at no more than 3 of the 281 primes for any k from 29 to 81, and at none for 17 of the 27 pieces. V79 has the most: 331, 421 and 541 |
| Q3 | held | V79: mean x² 0.836, mean x⁴ 1.963. V81: 1.120 and 3.354. V79 sits near the bottom of the band; a sample mean of x⁴ usually falls below its expected 3, since a few large values carry it |
| Z1 | held | e2 ≠ 0 at all 27 primes, and e3/(p¹³e2) is exactly ±1 at each. It equals (3187041\|p) at all 27. The rival "5 enters at 25", (15935205\|p), fits 14, about what chance gives; it is wrong at all 13 primes where (5\|p) = −1 |
| Z2 | held | e3 = det·p^(k+1)·e1 at all 27 primes for V27 and V23 with (3187041\|p), and for V19 with (969969\|p): round 26's determinants, read a second way |
| instrument | held | T1 to T15 and seventeen's and twenty-one's square classes at all 281 primes. Over F_(p²) the known pieces are the squares of their eigenvalues and over F_(p³) their cubes, at all 27 primes, which rereads the determinants of 7, 11, 13, 15, 17 and 21 |

**Read after the run** (not scores).
- At every one of the 27 primes, V25's characteristic polynomial is the forced line, (1 − (3187041|p)·p¹³x), times a
  quartic that is irreducible over Q. So no second line splits off at any of them.
- The moments of every piece from V29 to V81 are in the log. The mean of x² lies between 0.78 and 1.12 for all of them.
  The lowest are V73 (0.780) and V79 (0.836).

**Yield.**
- The author's coins, from 9 to 81.
  - 3 enters at 9 and at 81, two and four coins of 3, but not at 3 or 27, one and three. That is "3 at its square",
    with the count starting one coin late.
  - At 81 the infinite place decides it before any count, as at 27. It decides every power of a prime ≡ 3 (mod 4) the
    same way, and always as the thin rule does (F15).
  - 5 enters at 5 and 15 but not at 25, two coins of 5. The infinite place cannot see 5, so this coin had to be
    counted. Twenty-five's own determinant, now read at every prime, keeps 5 out.
- The rule is one symbol: (p/A_k), Yun's (p/d!!) for Kloosterman sums with the cube's 3 taken out (F16). The shape is
  Yun's; the Airy determinants and the cube's 3 were found nowhere searched.
- The counter reached 81 variables at every prime to 1999, and the field of p³ elements to 151.

---

## Round 28: Theorem 8's first new determinants, blind (registered 2026-11-16, before the test)

> *2 and 3, the proof first* — the author, 16 November 2026. The "2" asks to turn the determinant rule into a
> theorem; the "3" asks about the assumption round 27 used.

**The proof came first.** [`DETERMINANTS.md`](DETERMINANTS.md) proves Theorem 8: every Airy piece V_k has
determinant (p/A_k). It follows from Picard–Lefschetz at the cubic's nodes (ordinary double points at every prime
l ≥ 5, and in the good model at 3), one vanishing cycle per orbit of nodes in the antisymmetric part, and class field
theory, since the determinant is unramified at 2. Its corollary settles the assumption: complex conjugation fixes
every middle class. Each computable step is checked by [`verify_determinants.py`](verify_determinants.py)
([`verify_determinants.log`](verify_determinants.log), D1 to D10, all pass), including that the antisymmetric part
is the measured piece: twisted point counts give its trace as T_k(p)/p² at k = 5 and 7.

**What this round tests.** The proof's steps are standard, but its link to the measured pieces was checked directly
only at k = 5 and 7, and no determinant past 27 has ever been read. The theorem names five that the counts over F_p,
F_(p²) and F_(p³) can read.

| piece | dimension | how it is read | Theorem 8 | the rival (p/k!!) |
|---|---|---|---|---|
| V29 | 5 | e3 = det·p¹⁵·e2 | 92424189 | −30808063 |
| V31 | 6 | det = −1 exactly where e3 = 0 | −2865149859 | 955049953 |
| V33 | 5 | e3 = det·p¹⁷·e2 | 260468169 | the same |
| V35 | 6 | det = −1 exactly where e3 = 0 | −9116385915 | the same |
| V39 | 6 | det = −1 exactly where e3 = 0 | −25946636835 | 8648878945 |

- A six-dimensional orthogonal piece with determinant −1 has e3 = 0, since e3 = det·e3 (normalized). That was checked
  on 400 random orthogonal matrices before this registration. V37 has 7 dimensions and would need the fourth power of
  Frobenius.
- The rival is Yun's symbol without the cube's 3, (p/k!!). It differs from Theorem 8 by −3 at 29, 31 and 39, and has
  the wrong sign there for the Hodge types, so complex conjugation already rules it out at those three.

| | prediction | dies if |
|---|---|---|
| B1 | V29: e3/(p¹⁵e2) is exactly ±1 and equals (92424189\|p) at every prime from 41 to 151 with e2 ≠ 0, with at least 18 such primes | a prime fails, or fewer |
| B2 | V33: e3/(p¹⁷e2) is exactly ±1 and equals (260468169\|p), the same way | a prime fails, or fewer |
| B3 | V31: e3 = 0 exactly at the primes from 41 to 151 where (−2865149859\|p) = −1, with at least 6 of them | a prime fails, or fewer |
| B4 | V35: e3 = 0 exactly where (−9116385915\|p) = −1, the same way | a prime fails, or fewer |
| B5 | V39: e3 = 0 exactly where (−25946636835\|p) = −1, the same way | a prime fails, or fewer |
| instrument | the known pieces are the squares and cubes of their eigenvalues; V19, V23, V25 and V27 keep the determinants read in rounds 26 and 27; every piece from V29 to V39 has its forced shape, at every prime from 41 to 151 | one fails |

**The drafter's expectation.** All five hold, since Theorem 8 is proved. A failure would point to Step 1, the link
between the antisymmetric part and the piece measured as T_k, or to the counter at 39 variables.

Run: `python edge_rule.py test28` (minutes; four processes at below-normal priority).

---

## Round 28 scores (added after the test, 2026-11-16)

Run by [`edge_rule.py`](edge_rule.py) `test28`, registered at 1ec5bb8 before the test. Output:
[`edge_rule_test28.log`](edge_rule_test28.log).

**Five of five held. The first five determinants past 27 are exactly the ones Theorem 8 gives, at every prime
counted.**

| | outcome | evidence |
|---|---|---|
| B1 | held | V29: e2 ≠ 0 at all 24 primes from 41 to 151, and e3/(p¹⁵e2) is exactly ±1 at each, equal to (92424189\|p) at all 24. The rival (p/29!!) fits 11 |
| B2 | held | V33: the same at all 24, with (260468169\|p). The rival is the same symbol here |
| B3 | held | V31: e3 = 0 exactly at the 13 primes where (−2865149859\|p) = −1. The rival fits 11 of 24 |
| B4 | held | V35: e3 = 0 exactly at the 11 primes where (−9116385915\|p) = −1. The rival is the same symbol here |
| B5 | held | V39: e3 = 0 exactly at the 16 primes where (−25946636835\|p) = −1. The rival fits 11 of 24 |
| instrument | held | the known pieces are the squares and cubes of their eigenvalues; V19, V23, V25 and V27 keep their determinants; every piece from V29 to V39 has its forced shape, at all 24 primes |

**Yield.**
- Theorem 8 predicted five determinants that had never been read, and all five held at every prime. At 29, 31 and 39,
  where the cube's 3 matters, Yun's unshifted symbol fits at chance level.
- The proof's one checked-not-proved step is that the antisymmetric part is the piece measured as T_k. It is now
  borne out through 39: the measured pieces carry the determinants the antisymmetric parts must have. The direct
  check is still at 5 and 7.
- Round 27's one assumption, complex conjugation on the middle class, is proved (DETERMINANTS.md §4).

---

## Round 29: one wheel, the qudit T state and the ladder of diagonal magic (registered 2026-11-17, before the test)

> *where can we try and extend this to be useful on the frontier of applications?* and *1 yes, then the qudit round*
> — the author, 17 November 2026

**Why one wheel.** Rounds 10 to 14 measured magic on two and three wheels. A single qudit's T state, the magic state of
the qudit π/8 gate (Howard and Vala), is the standard non-Clifford resource for fault tolerance with qudits (Campbell,
Anwar and Browne). Round 13's identity, with one wheel, makes its Wigner values Birch sums. The literature check of
2026-11-17 ([`LITERATURE_MAP.md`](LITERATURE_MAP.md), item 8) found no measurement of its negativity against p, no
comparison with random states, and no answer to how the higher levels of the Clifford hierarchy compare. This round
asks all three.

**Made exact, before the test.**
- **The states.** A phase state is ψ_f = Σ_x ω^f(x) |x⟩/√p. When f is a polynomial of degree d < p it is the magic
  state of a diagonal gate of level d (Cui, Gottesman and Krishna); d = 3 is the T gate. The measure is the sum of
  sizes S = Σ|W| (rounds 8 on). The mana is ln S, the ceiling is √p, and S/√p is the share of the ceiling.
- **E1. The T state** [FORCED; round 13 with one wheel]. For f = cx³ + ⋯, W(q, s) = S_t(f′(q) − s)/p², with t = c/4 and
  S_t(a) = Σ_x ω^(tx³ + ax).
  - So S = (1/p)Σ_a |S_t(a)|, which depends only on the cubic class of t.
  - There is one T state when p ≡ 2 (mod 3) and three when p ≡ 1.
- **E2. Even degrees fall to the odd degree below** [FORCED].
  - f(q + y/2) − f(q − y/2) is odd in y. Its degree is d, or d − 1 when d is even, and then its leading coefficient is a
    multiple of q.
  - For f = cx⁴, W(0, s) = [s = 0]/p and W(q, s) = S_cq(4cq³ − s)/p².
  - So the quartic state is cubic rows plus one positive row: S₄ = 1/p + p⁻²Σ_(q≠0)Σ_a|S_cq(a)|. It is below the T
    state whenever p ≡ 2 (mod 3).
- **E3. The ladder** [FORCED from NAMED theorems].
  - At fixed q, each row of W is the family a ↦ Σ_y ω^(g(y) + ay) of an odd polynomial g of degree 2m + 1 (d = 2m + 1
    or 2m + 2).
  - Its geometric monodromy is Sp(2m) for p > 4m + 3 (Katz 1987, as we read it). By Deligne's equidistribution
    theorem, p^(3/2)W is then distributed like the trace of a Haar-random matrix in USp(2m).
  - So S/√p tends to κ_m = E|tr U|:

| degree | group | κ: Weyl integral (Monte Carlo) |
|---|---|---|
| 3, 4 | USp(2) = SU(2) | 8/(3π) = 0.848826 |
| 5, 6 | USp(4) | 0.790497 (0.7906 ± 0.0019) |
| 7, 8 | USp(6) | 0.798491 (0.7997 ± 0.0027) |
| 9, 10 | USp(8) | 0.79781 |
| → ∞ | the Gaussian limit | √(2/π) = 0.797885 |

  - **The random baseline, exactly.**
    - A phase-point operator has (p + 1)/2 eigenvalues +1 and (p − 1)/2 eigenvalues −1. So a Haar-random state has
      W(u) = (2X − 1)/p with X ~ Beta((p + 1)/2, (p − 1)/2), and its mean S is p·E|2X − 1|.
    - This tends to √(2/π)·√p from above: 0.8385√p at 5, 0.7999√p at 101 and 0.7981√p at 1009. The limit is Wilson
      and White's mana, ½ ln d − ½ ln(π/2).
  - **So the ladder is not monotone.**
    - Only the third level sits above random.
    - The fifth sits below it: USp(4)'s trace has the Gaussian's second and fourth moments, but a smaller mean of |·|.
    - From the seventh on, the ladder hugs the random value.
- **E4. The moments are point counts** [FORCED].
  - Σ_(q,s) W^n = p^(1−2n)Σ_a S_t(a)^n. Averaged over the three classes this is p^(3−2n)·t_n, from the counts of Livné's
    cubics, and when p ≡ 2 (mod 3) every class equals it.
  - So, for p ≡ 2 (mod 3), the T state's seventh moment is (14 + 6(5|p))/p⁹ + a_p/p¹⁰, with a_p the coefficient of
    Chênevert's newform 35.3.c.b.
- **E5. The cubic Gauss sum decides the classes** [FORCED; derived for this round].
  - When p ≡ 1 (mod 3), Σ_a S_t(a)³ = 2p² + 2p·Re(χ(3t)G(χ)²), with χ a cubic character and G(χ) = Σ_v χ(v)ω^v. The
    fourth moment, 2p³ − p², is the same for every class.
  - Proof of the third. Σ_a S_t(a)³ = pΣ_(x+y+z=0) ω^(t(x³+y³+z³)) = pΣ_(x,y) ω^(−3txy(x+y)).
    - Put y = λx, and count the cube roots of v as 1 + χ(v) + χ̄(v). This gives 2p + 2Re(χ(−3t)G(χ̄)J(χ, χ)).
    - Then G(χ̄)J(χ, χ) = G(χ)², since G(χ)³ = pJ(χ, χ).
  - Proof of the fourth. On x₁ + ⋯ + x₄ = 0, Σx³ = −3(x₁ + x₂)(x₁ + x₃)(x₂ + x₃). A linear change of variables leaves
    pΣ_(u,v) p·[uv = 0].
  - The Jacobi sum fixes the three values. Which class takes which is Kummer's question about the cube root: the edge
    of the coin at 3.
- **Checked before this registration** ([`one_wheel_calibrate.log`](one_wheel_calibrate.log), all pass):
  - E1 and E2 against the Wigner function computed from the state, at every prime up to 29;
  - E3's constants by quadrature and by Monte Carlo, and the exact Haar mean against 20 000 random states at 7 and 11;
  - E4, the seventh moment and E5, at every prime up to 29.
- **Not computed before this registration:** any T-state or higher-degree S at a prime above 29.
  - Round 13 logged the T state at 5: S = 1 + 2/√5 = 0.8472√5, above the Haar mean of 0.8385√5.

**Predictions.** All six are fresh.

| | prediction | dies if |
|---|---|---|
| Q1 | **The T state's law.** Over every class at every prime from 1000 to 3000, the mean of S/√p is within 0.003 of 8/(3π) = 0.84883 | the mean is outside 0.84583 to 0.85183 |
| Q2a | **The T state beats random.** At every prime from 500 to 5000, every class has S above the exact Haar mean | one class at one prime falls short |
| Q2b | (Claude's reading, thinner) The same at every prime from 31 to 500. The even moments that govern \|S\| are exact up to O(1/p) (Σ_a S_t(a)² = p², Σ_a S_t(a)⁴ = 2p³ − p²), so the T state should sit near its limit even at small p | one falls short |
| Q3 | **The fifth level is below random.** Take x⁵, x⁶, and a seeded random quintic and sextic at each prime. For each family, the mean S/√p over the primes from 700 to 1500 is within 0.004 of κ₂ = 0.79050, and below the mean Haar value at the same primes | a family's mean is outside 0.78650 to 0.79450, or not below the Haar mean |
| Q4 | **The seventh level hugs random.** For x⁷, x⁸, and a seeded random septic and octic, the same mean is within 0.004 of κ₃ = 0.79849 | a family's mean is outside 0.79449 to 0.80249 |
| Q5 | (Claude's reading) **At small p the T state is not the best phase state.** At 7, over all 2401 phase classes (f of degree at most 6, modulo degree 2), the most negative is not a T state. At 5, Feng and Luo found diagonal gates with general phases that beat T | a T class is the maximum at 7 |

- **Reads, not scored:**
  - how the T state's deviation from 8/(3π) shrinks with p;
  - the spread between the three classes when p ≡ 1 (mod 3);
  - whether the class with the largest third moment (the Gauss sum's choice) is the most negative;
  - the best phase states at 5 (all 25 classes), and at 11 and 13 (10⁶ sampled at each).

**The drafter's expectation.** Q1, Q2a, Q3 and Q4 rest on proved equidistribution, and their tolerances allow
corrections of order 1/p. Q2b and Q5 are on thinner ground.
- If Q3 holds, the useful statement is this. Among the diagonal gates of the Clifford hierarchy on one qudit, only the
  T gate's level makes states more negative than random, and the next odd level makes them less.

Run: `python one_wheel.py test` (minutes; four processes at below-normal priority).

---

## Round 29 scores (added after the test, 2026-11-17)

Run by [`one_wheel.py`](one_wheel.py) `test`, registered at fb9b5c0 before the test, in 2.5 minutes. Output:
[`one_wheel_test.log`](one_wheel_test.log); the reads made after it are in [`one_wheel_reads.log`](one_wheel_reads.log).

**Five of six held.** The T state's law, its lead over random states, and the ladder below it all held. The guess that
the T state is not the best phase state at 7 died.

| | outcome | evidence |
|---|---|---|
| forced | held | E4 at every prime to 101, and E5 at every prime ≡ 1 (mod 3) to 1000, in every class |
| Q1 | held | mean S/√p = 0.84890 over the 516 T states at the primes from 1000 to 3000, against 8/(3π) = 0.84883 |
| Q2a | held | every class is above the exact Haar mean at every prime from 500 to 5000 |
| Q2b | held; its reason did not | every class is above it at every prime from 31 to 500 too (at 31, for one: 0.8305√p against 0.8043√p). But the deviations do not shrink like 1/p, as the reason said (the reads below) |
| Q3 | held | means 0.79067 (x⁵), 0.78989 (x⁶), 0.79061 (random quintic) and 0.79067 (random sextic), against κ₂ = 0.79050. Every family is below the Haar mean at each of the 114 primes (its largest value is 0.79227, the Haar mean's smallest 0.79802) |
| Q4 | held | means 0.79853 (x⁷), 0.79785 (x⁸), 0.79857 (random septic) and 0.79857 (random octic), against κ₃ = 0.79849 |
| Q5 | **died** | at 7 the most negative of all 2401 phase classes is a T state, S = 2.450304 (t = 1). At 5 it is too, among all 25 |

**Read after the test** (not scored).
- **What keeps the T state from settling.**
  - One class (when p ≡ 2 mod 3), and the mean of the three classes (when p ≡ 1), deviate from 8/(3π) by about
    0.0005 rms from 1000 to 5000. They shrink roughly like p^(−0.4).
  - The spread between the three classes is ten times larger and shrinks like p^(−1/2): 0.027 rms from 31 to 200,
    0.0039 from 3000 to 5000.
- **The Gauss sum's third moment does not pick the most negative class.** The class with the largest third moment is
  the most negative at 24 of the 77 primes ≡ 1 (mod 3) up to 1000, which is chance. The negativity follows the even
  moments, and the fourth is the same for every class.
- **The small primes.**
  - At 11 a degree-10 phase beats the T state in a sample of 10⁶ (S = 2.877321 against 2.827479).
  - At 13 no sampled phase does. The best T class, 3.204742, is 0.889 of √13.
  - Rounds 8 to 14 quote the negativity's share of its ceiling, (S − 1)/(√p − 1). In that measure the T state at 7
    has 0.881, below round 8's search bests over all states (0.89 to 0.90).
- **Prior art found during the run.**
  - Zhu, Mao and Yi (arXiv:2410.13575, 2024), on third moments of qudit Clifford orbits, already treat the three
    classes: they distinguish three types of T gates and magic states when p ≡ 1 (mod 3) by cubic characters. They
    use cubic Gauss and Jacobi sums, and cite Kummer's problem.
  - E5 is their Lemma 24, read through the Wigner function: κ(f, T) = 2/d + (2/d²)Re(η₃(ac)G²(η₃)) = g(3, ac)²/d²,
    with g(3, b) = Σ_x ω^(bx³). So Σ_a S_t(a)³ = p·g(3, 3t)². This was checked in their paper on 2026-11-17, with the
    author's permission to open it.
  - Feng and Luo (*EPJ Plus* 2025) show that the Howard–Vala T gates fall into three Clifford classes exactly when
    p ≡ 1 (mod 3).
  - Feng and Luo (*PRA* 2026): for the L1 norm the T gate is optimal among all diagonal gates in every prime
    dimension. For Wigner negativity this was open beyond 3, and at 5, 500 diagonal gates with general phases beat it.

**Yield.**
- **New, as far as we checked.**
  - The T state's negativity, (8/(3π))√p, measured against p, and its lead over random states at every prime from 31
    to 5000.
  - The ladder above it. The fifth level of the Clifford hierarchy falls below random states (USp(4)'s 0.7905), and
    from the seventh level on the values hug the random one.
  - So among the polynomial phase gates ω^f on one qudit, only the cubic level, the T gate, makes states more
    negative than random. The hierarchy's higher levels also hold gates with p^m-th-root phases (Cui, Gottesman and
    Krishna), which this round did not test.
- **Exhaustive at 5 and 7.** Among diagonal gates whose phases are p-th roots of unity, the T state is the most
  negative. With other phases at 5 it is not (Feng and Luo).
- **Useful.** In Pashayan, Wallman and Bartlett's quasi-probability simulation, the number of samples grows with the
  square of the product of the magic states' S [NAMED]. So each T state multiplies the cost by about (8/(3π))²·p ≈ 0.72p.
  A quintic-phase state multiplies it by less than a random state does.

---

## Round 30: the p²-th-root phases (registered 2026-11-17, before the test)

> *Livné proof first, then the p²-root phases* — the author, 17 November 2026

**Why.**
- Round 29's statements are about phase states ψ_f with p-th-root phases. The Clifford hierarchy also holds diagonal
  gates whose phases are p^m-th roots of unity (Cui, Gottesman and Krishna); the qutrit T gate is one, with ninth
  roots. At 5, Feng and Luo found diagonal gates that beat the T state with phases outside the fifth roots of unity.
- This round takes the next step, m = 2: the fine-phase states ψ_g = p^(−1/2) Σ_x ζ^g(x) |x⟩, with ζ = e^(2πi/p²) and
  g: F_p → Z/p². It also compares them with diagonal states whose phases are arbitrary real numbers.
- The measure is round 29's sum of sizes, S = Σ|W|.

**Made exact, before the test.**
- **The states.** Any function {0, …, p − 1} → Z/p² is a polynomial mod p², since differences of distinct
  representatives are units. So, as we read Cui, Gottesman and Krishna, every fine-phase gate lies in the hierarchy.
  The p-th-root states of round 29 are the case g = p·f.
- **The random baseline.**
  - For a random g, the row sums of W are 1 + 2Σ_(y=1)^((p−1)/2) cos θ_y. The angles θ_y are independent and uniform,
    because the pairs {q + y/2, q − y/2} are disjoint.
  - So W ≈ (1 + N(0, p − 1))/p², and S/√p → √(2/π), the random-state value of round 29's exact Haar mean.
- **Checked before this registration** ([`fine_phases_calibrate.log`](fine_phases_calibrate.log), all pass):
  - C1: the diagonal-state Wigner norm, against the state's own Wigner function, p = 3 to 13;
  - C2: Li and Luo's theorem at p = 3. The best of the 81 ninth-root states is the qutrit T state, S = 1.586257, and
    200 optimizations over arbitrary phases do not beat it;
  - C3: round 29's T states at 5 and 7.
- **Not computed before this registration:** any fine-phase or arbitrary-phase value at p = 5 or above.

**Predictions.** All four are fresh.

| | prediction | dies if |
|---|---|---|
| P1 | (Claude's reading) **At 5 the T state is beaten by a fine phase.** Over all 390 625 fine-phase states (g(0) = 0), some state has S above the T state's 1 + 2/√5. Feng and Luo's arbitrary phases beat T at 5, and twenty-fifth roots approximate any phase to within π/25 | the T state's value is the maximum |
| P2 | **The grid is fine enough.** At 5 the best fine-phase S is at least 99% of the best S over arbitrary phases (Nelder–Mead and Powell from 300 random starts) | below 99% |
| P3 | (Claude's reading, thin) **At 7 the T state is not the best diagonal state.** Some arbitrary-phase state (400 starts) beats the T state's 2.450304. At 3 the T state is optimal (Li and Luo), at 5 it is not (Feng and Luo); 7 is open | nothing beats 2.450304 + 10⁻⁶ |
| P4 | **Random fine phases are random states.** Over ten seeded random g at each prime from 500 to 1000, the mean S/√p is within 0.002 of the exact Haar mean over the same primes | the difference is 0.002 or more |

- **Reads, not scored:**
  - how many fine-phase states beat T at 5;
  - the best of 10⁶ sampled fine-phase states at 7;
  - the structured fine phases g = x^a mod p² (a = 2, 3, 4) from 500 to 1000.

**The drafter's expectation.**
- P2 and P4 rest on continuity and on the central limit theorem.
- P1 rests on Feng and Luo, and P3 is a guess either way.
- Whatever P3 does, the table of S at 3, 5 and 7 for p-th-root, fine and arbitrary phases says where the T gate stands
  among all diagonal gates on one qudit.

Run: `python fine_phases.py test` (a few minutes; four processes at below-normal priority).

---

## Round 30 scores (added after the test, 2026-11-17)

Run by [`fine_phases.py`](fine_phases.py) `test`, registered at b19b5c0 before the test, in 1.1 minutes. Output:
[`fine_phases_test.log`](fine_phases_test.log).

**Three of four held, and the death is the finding.** At 7 the T state is, numerically, the best diagonal state of all,
as at 3 and unlike 5.

| | outcome | evidence |
|---|---|---|
| P1 | held | at 5, 129 500 of the 390 625 fine-phase states beat the T state; the best has S = 1.969982 (0.8810 of √5), at g = (0, 12, 16, 1, 1)/25 |
| P2 | held | the best over arbitrary phases (300 starts) is 1.977576 (0.8844 of √5); the best fine phase is 99.6% of it |
| P3 | **died** | at 7, 400 optimizations over arbitrary phases found nothing above the T state's 2.450304. Their best is the T state itself: phases (0, 5, 6, 6, 1, 1, 2)/7, which is f = 4x³ + x, round 29's best class t = 1 |
| P4 | held | ten random fine phases at each of the 73 primes from 500 to 1000: mean S/√p = 0.79801, against the Haar mean of 0.79816 |

**Read after the test** (not scored).
- **Where the T gate stands among all diagonal gates on one qudit:**

| p | T state | best p-th-root phase | best p²-th-root phase | best arbitrary phase (numerical) | Haar mean | ceiling √p |
|---|---|---|---|---|---|---|
| 3 | 1.586257 | (no T state with cube roots) | 1.586257, the T state | 1.586257 (Li and Luo) | 1.5 | 1.732 |
| 5 | 1.894427 | 1.894427, the T state | 1.969982 | 1.977576 (Feng and Luo: T is not optimal) | 1.875 | 2.236 |
| 7 | 2.450304 | 2.450304, the T state | ≥ 2.437764 (10⁶ sampled) | 2.450304, the T state | 2.1875 | 2.646 |

- **A coin by p mod 3?** The T state is optimal at 3 and, numerically, at 7. It is beaten at 5, and at 11 by a degree-10
  phase (round 29). At 13 it beat every sampled phase.
  - At p ≡ 1 (mod 3) the T states fall into three classes, and the best class sits high at small p: 0.926√7 and
    0.889√13.
  - So far: optimal at 7 (≡ 1), beaten at 5 and 11 (≡ 2). Too few primes to call it, and 13, 17 and 19 would test it.
- **Structured fine phases are not random.** g = x² mod p² is a slow chirp and nearly classical: S/√p = 0.078 from 500
  to 1000. g = x³ mod p², a discretized cubic phase, gives 0.736, below random. g = x⁴ gives 0.797.

**Yield.**
- At 7 no diagonal state found beats the T state, though 400 optimizations over arbitrary phases looked. Feng and Luo
  asked whether the T gate is optimal for Wigner negativity in prime dimensions beyond 3. At 5 it is not (their
  result); at 7 it appears to be.
- At 5 the best diagonal state needs phases off the fifth roots of unity, and twenty-fifth roots come within 0.4% of it.
- Random p²-th-root phases behave like random states, as the central limit theorem says.

---

## Round 31: is the T gate the best diagonal gate exactly when p ≡ 1 (mod 3)? (registered 2026-11-17, before the test)

> *1 yes, round 31 first, then the email* — the author, 17 November 2026

**Why.** Rounds 29 and 30 found the T state the most negative of all diagonal states at 3 (Li and Luo's theorem) and,
numerically, at 7, but beaten at 5 (Feng and Luo) and at 11 (round 29). When p ≡ 1 (mod 3) the T states fall into
three classes; when p ≡ 2 there is one. This round asks whether that is a coin: optimal on one side, beaten on the
other. Feng and Luo left the question open beyond 3.

**Made exact, before the test.**
- **The search, fixed in [`diagonal_coin.py`](diagonal_coin.py).** A diagonal state is Σ_x e^(iφ(x))|x⟩/√p with
  φ(0) = 0.
  - From each start, L-BFGS-B maximizes the smoothed size Σ√(W² + ε²) with its exact gradient, at ε = 10⁻⁵ and then
    10⁻⁸. The exact S is taken at the end.
  - The starts at each prime: 400 uniform random phase vectors, 100 random p-th-root phase functions, 100 random
    p²-th-root ones, and, for each class of T state, 30 copies of its phases plus Gaussian noise of 0.3 radians.
  - A state beats the T state when its S exceeds the best T class's by more than 10⁻⁶.
  - A witness is decisive. Finding nothing is numerical evidence, not a proof.
- **The best T class** (round 29's formula, computed before this registration):

| p | p mod 3 | S of the best T class | / √p |
|---|---|---|---|
| 13 | 1 | 3.204742 | 0.8888 |
| 17 | 2 | 3.501720 | 0.8493 |
| 19 | 1 | 3.873476 | 0.8886 |
| 23 | 2 | 4.061994 | 0.8470 |

- **Checked before this registration** ([`diagonal_coin_calibrate.log`](diagonal_coin_calibrate.log), all pass):
  - the gradient against finite differences;
  - the search reproduces round 30 at 5 (1.977576, beating T) and at 7 (only the T state, 2.450304);
  - at 11 it beats round 29's witness: 2.910515 against T's 2.827479.
- **Not computed before this registration:** any search at 13, 17, 19 or 23.

**Predictions.** All four are fresh. The coin holds through 23 if all four hold.

| | prediction | dies if |
|---|---|---|
| R1 | At 13 (≡ 1 mod 3) the search finds nothing above the best T class | a state above 3.204742 + 10⁻⁶ |
| R2 | At 17 (≡ 2 mod 3) the search finds a diagonal state above the T state | none above 3.501720 + 10⁻⁶ |
| R3 | At 19 (≡ 1 mod 3) the search finds nothing above the best T class | a state above 3.873476 + 10⁻⁶ |
| R4 | At 23 (≡ 2 mod 3) the search finds a diagonal state above the T state | none above 4.061994 + 10⁻⁶ |

**The drafter's expectation.**
- The ≡ 2 side should hold, since a witness is easy to find when T is beaten, as at 5 and 11.
- The ≡ 1 side is the real test.
- Even if all four hold, the coin can only be a small-p effect. The best class tends to 8/(3π)√p = 0.849√p (round 29),
  so at large p it will meet the other diagonal states.

Run: `python diagonal_coin.py test` (minutes; four processes at below-normal priority).

---

## Round 31 scores (added after the test, 2026-11-17)

Run by [`diagonal_coin.py`](diagonal_coin.py) `test`, registered at 2e5d136 before the test. Output:
[`diagonal_coin_test.log`](diagonal_coin_test.log), 0.3 minutes.
- The first run crashed before printing anything. The fault was in the helper that labels the best state's phases,
  which interpolated over the rationals instead of mod p.
- The helper was fixed (Gaussian elimination mod p, checked on 4x³ + x at 7 and x¹⁰ at 11), and the seeded test was
  rerun. The search and the scoring were not touched, so the rerun is the run.

**Four of four held. The coin held through 23.**

| | outcome | evidence |
|---|---|---|
| R1 | held | at 13 (≡ 1), the best of 690 climbs is the T state, S = 3.204742 (0.8888√13), on the p-th-root grid with degree 3 |
| R2 | held | at 17 (≡ 2), a state off the p-th-root grid has S = 3.629595 (0.8803√17), against the T state's 3.501720 |
| R3 | held | at 19 (≡ 1), the best of 690 climbs is the T state, S = 3.873476 (0.8886√19), degree 3 |
| R4 | held | at 23 (≡ 2), a state off the grid has S = 4.248930 (0.8860√23), against the T state's 4.061994 |

**Read after the test** (not scored).
- **The whole table, 3 to 23:**

| p | p mod 3 | best T class / √p | best diagonal state found / √p | the T state |
|---|---|---|---|---|
| 3 | 0 | 0.9158 | 0.9158, the T state | optimal (Li and Luo, proved) |
| 5 | 2 | 0.8472 | 0.8844 | beaten (Feng and Luo) |
| 7 | 1 | 0.9261 | 0.9261, the T state | optimal (numerically) |
| 11 | 2 | 0.8525 | 0.8776 | beaten |
| 13 | 1 | 0.8888 | 0.8888, the T state | optimal (numerically) |
| 17 | 2 | 0.8493 | 0.8803 | beaten |
| 19 | 1 | 0.8886 | 0.8886, the T state | optimal (numerically) |
| 23 | 2 | 0.8470 | 0.8860 | beaten |

- **Why the coin, as far as the numbers show.**
  - When p ≡ 1 (mod 3) the three T classes spread apart, and the best one sits near 0.889√p. That is above what the
    non-T diagonal states reach, about 0.88√p.
  - When p ≡ 2 there is one class, near 0.85√p, and other states pass it. Those are found off the p-th-root grid,
    except at 11, where round 29 found a p-th-root one.
- **Where its edge should be.** The best class tends to 8/(3π)√p = 0.849√p (round 29): at 31 it is 0.873√p, and at 127
  it is 0.871√p. So the ≡ 1 side should fail once the best class drops below the other states, perhaps at 31.

**Yield.**
- For every prime through 23, the T gate is the most Wigner-negative diagonal gate exactly when p = 3 or p ≡ 1
  (mod 3).
  - On the ≡ 2 side the evidence is decisive: an explicit better state at 5, 11, 17 and 23.
  - On the ≡ 1 side it is numerical: 690 climbs found only the T state at 13 and at 19, and 400 found only it at 7.
- This is a concrete answer to Feng and Luo's open question, with a reason that can be tested: the three classes of
  T states when p ≡ 1 (mod 3).

---

## Round 32: where the coin ends (registered 2026-11-17, before the test)

> *yes, round 32 at the edge* — the author, 17 November 2026

**Why.**
- Round 31 found the T gate to be the best diagonal gate at p = 3, 7, 13 and 19, and beaten at 5, 11, 17 and 23: a
  coin by p mod 3.
- Every coin has an edge. When p ≡ 1 (mod 3), the best of the three T classes is what beat the other diagonal states,
  near 0.889√p at 13 and 19. But it tends to 8/(3π)√p = 0.849√p (round 29).
- This round asks where the coin stops.

**Made exact, before the test.**
- **The best T class, from round 29's formula** (not from any search):

| p | p mod 3 | best T class / √p | the other classes |
|---|---|---|---|
| 29 | 2 | 0.8561 | (one class) |
| 31 | 1 | 0.8734 | 0.8624, 0.8305 |
| 37 | 1 | 0.8740 | 0.8479, 0.8291 |
| 43 | 1 | 0.8756 | 0.8407, 0.8361 |

  - Every prime ≡ 1 (mod 3) from 31 to 109 has its best class at 0.8756√p or below, beneath the lowest level the other
    diagonal states reached at 5 to 23, 0.8776√p (at 11).
  - At 13 and 19 the best class was 0.889√p, above that level.
- **The search is round 31's**, unchanged ([`diagonal_coin.py`](diagonal_coin.py) `edge`: the same starts, climbs and
  threshold). A witness is decisive.
- **Not computed before this registration:** any search at 29 or above.

**Predictions.** All five are fresh.

| | prediction | dies if |
|---|---|---|
| E1 | At 29 (≡ 2 mod 3, the control) the search beats the T state | nothing above 0.8561√29 |
| E1b | and its best reaches 0.875√29, the level the other diagonal states held at 5 to 23. Without that, a failure at 31 could just mean a weaker search | below 0.875√29 |
| E2 | **The coin breaks at 31.** At 31 (≡ 1) the search beats the best T class | nothing above 0.8734√31 |
| E3 | At 37 (≡ 1) the search beats the best T class | nothing above 0.8740√37 |
| E4 | At 43 (≡ 1) the search beats the best T class | nothing above 0.8756√43 |

**The drafter's expectation.**
- If E1, E1b and E2 to E4 hold, the coin is a small-prime fact. It holds at 3, 7, 13 and 19 and nowhere ≡ 1 (mod 3)
  after.
- Its edge is where the best T class falls below the other diagonal states.
- If E2 dies, the T gate's lead at 31 needs another reason.

Run: `python diagonal_coin.py edge` (a few minutes; four processes at below-normal priority).

---

## Round 32 scores (added after the test, 2026-11-17)

Run by [`diagonal_coin.py`](diagonal_coin.py) `edge`, registered at 9d2f509 before the test, in 0.5 minutes. Output:
[`diagonal_coin_edge.log`](diagonal_coin_edge.log).

**Four of five held. The coin ends where the best T class falls below the other diagonal states: after 19, at 31.**

| | outcome | evidence |
|---|---|---|
| E1 | held | at 29 (≡ 2) a diagonal state off the p-th-root grid has S = 4.680564 (0.8692√29), against the T state's 4.610135 (0.8561) |
| E1b | **died** | that best is 0.8692√29, below the 0.875 the other diagonal states reached at 5 to 23. Their level is not a constant |
| E2 | held | at 31 (≡ 1) the coin breaks: 4.899793 (0.8800√31) against the best T class's 4.862890 (0.8734) |
| E3 | held | at 37 (≡ 1): 5.337764 (0.8775√37) against 5.316093 (0.8740) |
| E4 | held | at 43 (≡ 1): 5.743769 (0.8759√43) against 5.741504 (0.8756), a thin margin but a witness |

**Read after the test** (not scored).
- **The coin from 3 to 43:**
  - The T gate is the best diagonal gate at 3 (proved, Li and Luo) and at 7, 13 and 19 (numerically).
  - It is beaten at 5, 11, 17, 23 and 29 (≡ 2) and at 31, 37 and 43 (≡ 1), each with an explicit witness.
  - Its edge lies between 19 and 31, where the best of the three T classes drops from 0.889√p to 0.873√p.
- **The other diagonal states' level wanders.** The best found was 0.8844, 0.8776, 0.8803, 0.8860, 0.8692, 0.8800,
  0.8775 and 0.8759 at 5, 11, 17, 23, 29, 31, 37 and 43. It is a lower bound on the true optimum, from a search that
  grows harder with p.
- **The margin is thinning.** At 43 the witness beats the best T class by only 0.0003√43. As p grows, both the best T
  class and the searched states sit near 0.86 to 0.88.

**Yield.**
- The coin is a small-prime fact with a measured edge.
- When p ≡ 1 (mod 3), the T gate's three Clifford classes give it the best diagonal state at 7, 13 and 19, while the
  best class stays above about 0.88√p.
- From 31 on it does not, and the T gate is beaten on both sides of the coin.

---

## Round 33: what the states that beat the T gate share (registered 2026-11-17, before the test)

> *keep going, find what the p ≡ 2 winners share* — the author, 17 November 2026

**Why.** Rounds 30 to 32 found diagonal states beating the T state at 5, 11, 17, 23, 29, 31, 37 and 43. What do they
have in common?

**Made exact, before the test.**
- **F1. The T state's symmetry** [FORCED, proved; checked exactly at every class for p = 5 to 19].
  - Its Wigner function W(q, s) = S_t(3cq² − s)/p² is fixed by the p maps (q, s) ↦ (q + d, s + 6cdq + 3cd²).
  - It is fixed by the reflection (q, s) ↦ (−q, s), complex conjugation with parity, since cx³ is odd.
  - When p ≡ 1 (mod 3), it is also fixed by (q, s) ↦ (ζq, s/ζ) for the cube roots of unity ζ.
  - So its affine symmetry group has order 2p, or 6p when p ≡ 1 (mod 3).
- **The reads before this registration** ([`winners_explore.log`](winners_explore.log)). They use round 31's search,
  and the same search restricted to odd phase functions, φ(−x) = −φ(x), which is the T state's reflection symmetry.

| p | p mod 3 | best / √p | climbs reaching it | distinct optima | best odd / √p | gap |
|---|---|---|---|---|---|---|
| 5 | 2 | 0.8844 | 177 of 630 | 56 | 0.8844 | 0 |
| 11 | 2 | 0.8776 | 3 of 630 | 610 | 0.8776 | 0 |
| 17 | 2 | 0.8803 | 1 of 630 | 630 | 0.8694 | +0.0109 |
| 23 | 2 | 0.8860 | 1 of 630 | 630 | 0.8655 | +0.0204 |
| 29 | 2 | 0.8692 | 1 of 630 | 630 | 0.8656 | +0.0036 |
| 31 | 1 | 0.8800 | 1 of 690 | 674 | 0.8796 | +0.0004 |
| 37 | 1 | 0.8775 | 1 of 690 | 690 | 0.8775 | 0 |
| 43 | 1 | 0.8759 | 1 of 690 | 690 | 0.8759 | 0 |

  - **At 5 the optimum is one robust state.**
    - Its only symmetries are the identity and one antiunitary reflection. With the Clifford phase ω^(x²) removed,
      its phase function is odd like the T state's: (0, 0.7514, 0.7881, 0.2119, 0.2486) turns, off the fifth roots of
      unity.
    - Its orbit under the diagonal Clifford group (20 affine maps times 25 quadratic phases) has 500 members. That is
      Feng and Luo's count of optimal ququint gates.
  - **At 11** an odd state also reaches the best value.
  - **From 17 on the landscape is glassy.** The best value is reached by one climb among hundreds of distinct optima.
    - At 17, 23 and 29 (≡ 2) the best odd state falls short.
    - At 31, 37 and 43 (≡ 1) it does not.
  - **Checked and dropped:** the idea that the best T class is the one with the flattest Wigner values. Measured by
    kurtosis, it held at 13 of 37 primes ≡ 1 (mod 3), which is chance.
- **Not computed before this registration:** any search at 41 or 47.

**Predictions.** All six are fresh.

| | prediction | dies if |
|---|---|---|
| W1a, W1b | At 41 and at 47 (both ≡ 2 mod 3) the search beats the T state | nothing above it |
| W2a, W2b | The best value is reached by exactly one climb: the landscape is glassy | more than one |
| W3a, W3b | The best odd phase state falls short of it by more than 0.003√p: the winner breaks the T state's reflection symmetry | a gap of 0.003√p or less |

**The drafter's expectation.**
- W1 and W2 should hold.
- W3 tests whether the winners at p ≡ 2 (mod 3) from 17 on give up the reflection symmetry that the T state, the
  optimum at 5 and the winners at 31 to 43 keep. At 29 the gap was only 0.0036, so W3 can fail.

Run: `python winners.py test` (minutes; four processes at below-normal priority).
