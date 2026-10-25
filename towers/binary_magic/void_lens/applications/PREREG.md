# Applications: the same counting, in fields that use it (pre-registration, 2026-10-24)

Purpose: test that each application uses the *same* mathematics as the void lens, not a resemblance. Each test
reproduces a published result with the lens's own move: a symmetry or sector count that forces a kernel, or a
(1 - w)-adic nonvanishing argument. All are *translation* tests of known results, so a failure means my mapping
is wrong.

| id | field | prediction (written before the code ran) | kill condition |
|---|---|---|---|
| A1 | nanographene magnetism (Sutherland 1986; Lieb 1989; Ovchinnikov 1978) | Hueckel graphs of phenalenyl, [3]- and [4]-triangulene have exactly N_A - N_B = 1, 2, 3 zero modes: sublattice imbalance forces the kernel, like the void index. | Other nullities. |
| A2 | same | Two phenalenyls (opposite majority sublattices) joined minority-to-minority: N_A = N_B but **2** zero modes survive (the Clar's-goblet mechanism: unforced kernels, like the 5 unexplained 5x5 squares). Joined majority-to-majority: **0**. | Other nullities. |
| A3 | structural engineering (Fowler & Guest 2000, symmetry-extended Maxwell rule) | Two mirror-image triangles joined by three bars across the mirror: 6 joints, 9 bars, Maxwell count 0. Mirror sector counts force one antisymmetric mechanism and one symmetric self-stress (rank 8, not 9). A generic, asymmetric perturbation is rigid (rank 9). | Rank 9 in the symmetric position, or wrong sector parities. |
| A4 | cryptanalysis (DES complementation property, 1977) | E_(not k)(not x) = not E_k(x) for 2,000 random keys and blocks. The complement is the reflection through the center of the value range, so one encryption tests two keys. | Any failure. |
| A5 | cryptanalysis (linear structures) | A random 8-bit Boolean function with f(x ^ a) = f(x) ^ 1 has zero Walsh coefficient at every u with u . a = 0: exactly half the spectrum (128 of 256), for 200 random functions. | Any nonzero coefficient there. |
| A6 | compressed sensing (Chebotarev; Tao 2005; Candes-Romberg-Tao 2006) | Every square minor of the 7-point DFT is nonzero, so any S-sparse signal is determined by any 2S Fourier samples at prime length. At n = 9 some minors vanish: the 3-sparse comb on {0, 3, 6} is invisible to 6 of the 9 frequencies. Same prime/composite split as the 8b theorem. | A zero minor at 7, or none at 9. |

## Scores (`run.log`; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| A1 | phenalenyl C13 7/6 -> 1 zero mode; [3]triangulene C22 12/10 -> 2; [4]triangulene C33 18/15 -> 3 | **held** |
| A2 | balanced 13/13 dimer: minority-to-minority bond -> 2 zero modes, majority-to-majority -> 0 | **held** |
| A3 | symmetric frame rank 8: 1 mechanism (antisymmetric) + 1 self-stress (symmetric); perturbed rank 9 | **held** |
| A4 | DES complementation holds on 2,000 random pairs | **held** |
| A5 | 200 functions: all 128 Walsh coefficients with u . a = 0 vanish | **held** |
| A6 | DFT_7: 3,431 minors, none zero (smallest 0.868); DFT_9: 3,420 of 48,619 zero; comb {0,3,6} invisible at 6 of 9 | **held** |

All translation tests; they do not count toward the running record of real predictions.
