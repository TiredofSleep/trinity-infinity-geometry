# Seven levels: the two faces of 7 on a quantum system

> *how can these viewpoints syncronize to our viewing space for quantum parts?* · *what extensions would this
> imply? test them?* — the author, 7 November 2026

### Tags: **[FORCED]** checked by [`verify_seven_levels.py`](verify_seven_levels.py) · **[NAMED]** a cited standard result · **[READING]** an interpretation · **[FENCE]** outside the mathematics.

**A side floor of the number tower**, built on the sevenths of [`../../base/SEVENTHS.md`](../../base/SEVENTHS.md).
- A quantum system with seven levels, |0⟩ to |6⟩, is indexed by the seven remainders mod 7, so both faces of 7
  act on it.
- This page says how, and says what our three-dimensional space can and cannot hold.
- Eight predictions were registered before the run ([`PREREG.md`](PREREG.md)). Seven held and one died.

---

## 1. The dictionary [FORCED; NAMED: Weyl, Schwinger, Gottesman]

| in the sevenths | on seven quantum levels |
|---|---|
| adding 1: the heptagon, base 7 | the **shift** X, which sends \|k⟩ to \|k + 1⟩ |
| the shift's Fourier partner | the **clock** Z, which gives \|k⟩ the phase ωᵏ, with ω = e^(2πi/7) |
| multiplying by 10: the octahedron turning round 0 | the **multiplier**, which sends \|k⟩ to \|3k⟩ and fixes \|0⟩ |
| the half turn, k → −k | the **parity**, which is the Fourier transform done twice |
| a seventh of a turn of our space | for spin 3, the seven f-orbitals, it is exactly the clock: its eigenvalues are the seven 7th roots of unity |

The **Clifford group**, which quantum computing is built on, is the set of operations that carry shifts and
clocks to shifts and clocks, up to phase.

## 2. What held

- **Q1. The classical part is the two faces.** Of the 5040 ways to permute the seven levels, exactly 42 are
  Clifford operations: the maps k → ak + b. The Fourier transform, which joins the two faces, is not a
  permutation of the levels at all.
- **Q2. The 168 again.** The Clifford group's geometric part, SL(2, 7), has 336 elements. Modulo ±1 its 168
  have the same orders as the Fano plane's 168 symmetries [NAMED: PSL(2, 7) ≅ GL(3, 2)].
- **Q3. The eight bases sit like the cube's corners.**
  - A seven-level system has eight mutually unbiased bases, the most it can have [NAMED: Wootters and Fields
    1989].
  - The multipliers fix two of them, the levels and the Fourier basis, and split the other six into {1, 2, 4}
    and {3, 5, 6}. The Fourier transform swaps the pair and swaps the triples.
  - The 168 contains 14 copies of the cube's rotation group, and each moves the eight bases exactly as the cube's
    rotations move its eight corners.
  - [READING] So the levels sit on the octahedron with its centre, and the bases on the cube: the polar pair of
    [`../../coin/THE_POLAR_COIN.md`](../../coin/THE_POLAR_COIN.md).
- **Q4. The magic subspace is Klein's space.**
  - Some states change sign under the half turn. Those are the states with negative quasi-probability at the
    centre of phase space, the resource that quantum computing needs.
  - They span three dimensions, one for each axis of the octahedron: (|j⟩ − |−j⟩)/√2 for j = 1, 2, 4.
  - The Clifford group acts there through exactly 168 matrices up to scalars. Its generators are Klein's own:
    diag(ω⁴, ω², ω) and a cycle of the three coordinates.
  - Klein's quartic x³y + y³z + z³x is invariant [NAMED: Klein 1878; this is the odd part of the Weil
    representation].
- **Q5. The octahedron acts on the magic subspace as on our space.** Each of the 14 copies of S₄ acts there
  with the character of the octahedron's rotations of ordinary space: 3, −1, 0 and 1 on elements of orders 1,
  2, 3 and 4. The elements of order 7 do not act like rotations: their traces are (−1 ± √−7)/2, the sum
  ω + ω² + ω⁴ over the squares and its conjugate.
- **Q6. The octahedron's height is a magic state.**
  - The Legendre state is +1 on the squares, −1 on the others and 0 at the centre. That is the height of each
    corner along the wheel's axis.
  - It is an eigenvector of every multiplier, and of the Fourier transform with eigenvalue i, which is Gauss's
    sum.
  - It changes sign under the half turn, and its quasi-probability at the centre is −1/7.
- **Q8. The same coin at 5.**
  - Five levels have 20 Clifford permutations, the maps k → ak + b.
  - The geometric part, modulo ±1, has the element orders of the icosahedron's rotation group.
  - The magic subspace, in two dimensions, carries the binary icosahedral group, 120 matrices: the icosahedron's
    rotations lifted to spinors.

## 3. What died

- **Q7. The Legendre state is not the most negative state.** A search from 125 starts found total negativity
  0.7325, against the Legendre state's 0.7283. The state it found is not even odd under the half turn: its
  parity expectation is +0.23. The guess is kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md), with the
  counterexample in the log to 8 decimals.

## 4. Our space, and what it cannot hold [FORCED; FENCE]

- In our three-dimensional space the two faces cannot be one rigid object, because no symmetry of the octahedron
  has order 7.
- Each face lives in space by itself. The heptagon's turns and flips act on a spin-3 system as rotations: a
  seventh of a turn is the clock, and half a turn about a perpendicular axis is the flip. The octahedron's
  rotoreflection turns its six corners.
- The faces meet only in the seven-dimensional space of states. There the Fourier transform joins them, and it
  is a quantum operation, not a motion of space.
- The magic subspace is a complex copy of three-space. The octahedron's rotations act there as on ordinary
  space, but the whole 168 cannot be a group of rotations: the finite rotation groups are the cyclic, the
  dihedral and the three polyhedral groups, and it is none of them [NAMED: Klein].
- [FENCE] All of this is standard finite-dimensional quantum mechanics and classical group theory. It says how
  the sevenths' two faces act on a seven-level system, and it claims nothing new about particles. A physical
  reading would go to [`../../lab/FENCED_READINGS.md`](../../lab/FENCED_READINGS.md), with the test that would
  decide it.

## 5. Standing

- **Known, and credited:**
  - the Weyl operators and the Clifford group;
  - the p + 1 mutually unbiased bases;
  - the discrete Wigner function, and its positivity on the states built from shifts and clocks (Wootters 1987;
    Gross 2006);
  - PSL(2, 7) ≅ GL(3, 2), and Klein's quartic with its three-dimensional representation, the odd part of the
    Weil representation;
  - SL(2, 5) as the binary icosahedral group;
  - Galois's subgroups of index 7, which are the 14 copies of S₄.
- **This repository's own:** the dictionary, and the reading that puts the sevenths' two faces, the octahedron
  with its centre, the cube and Klein's space into one picture.
- **The yield is mostly known.** That is the honest result of this round: seven classical facts confirmed, and
  one guess dead.

## Run it

```
python verify_seven_levels.py      # about half a minute (numpy + scipy)
```

It reruns all eight predictions and the page's other checks, and exits with 1 if the recorded score changes.

## Sources

- H. Weyl, *The Theory of Groups and Quantum Mechanics* (1931); J. Schwinger, "Unitary operator bases",
  *Proc. Natl. Acad. Sci.* **46** (1960).
- D. Gottesman, "Fault-tolerant quantum computation with higher-dimensional systems" (1999).
- W. K. Wootters, "A Wigner-function formulation of finite-state quantum mechanics", *Ann. Phys.* **176** (1987);
  W. K. Wootters and B. D. Fields, "Optimal state-determination by mutually unbiased measurements", *Ann. Phys.*
  **191** (1989).
- D. Gross, "Hudson's theorem for finite-dimensional quantum systems", *J. Math. Phys.* **47** (2006).
- M. Howard, J. Wallman, V. Veitch and J. Emerson, "Contextuality supplies the 'magic' for quantum computation",
  *Nature* **510** (2014).
- F. Klein, "Ueber die Transformation siebenter Ordnung der elliptischen Functionen", *Math. Ann.* **14** (1878);
  N. D. Elkies, "The Klein quartic in number theory", in *The Eightfold Way* (1999).
- É. Galois, letter to Auguste Chevalier (1832): PSL(2, p) has a subgroup of index p only for p ≤ 11.
