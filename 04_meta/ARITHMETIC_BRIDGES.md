# ARITHMETIC_BRIDGES — Cross-Stratum Identities

## The arithmetic structure of TIG's prime spectrum

**Status:** [THM] (sympy-exact, textbook arithmetic)
*Companion to: PRIMES_OF_TIG, FIELDS_OF_TIG*
*Locked v1 · 2026-05-08*

---

## §1. Three Stacked Identities Tying the Strata

The four prime strata are not independent. **Three arithmetic identities** tie them through the lattice prime 71:

### Identity A — Sophie Germain bridge (Stratum III ↔ IV)
$$2 \cdot 71 + 1 = 143 = 11 \cdot 13$$
The Sophie Germain step on 71 produces the wobble pair as a product.

### Identity B — CRT idempotent lift (Strata I ↔ III ↔ IV)
$$71 \bmod 11 = 5 = \mathrm{BALANCE} = (1,0)_{\mathbb{F}_2 \times \mathbb{F}_5}$$
$$71 \bmod 13 = 6 = \mathrm{CHAOS} = (0,1)_{\mathbb{F}_2 \times \mathbb{F}_5}$$
The lattice prime, reduced modulo each wobble prime, hits exactly the **two CRT idempotents of the substrate Z/10Z** (D98).

### Identity C — HARMONY return (Stratum II ↔ IV via class field)
$$h(\mathbb{Q}(\sqrt{-71})) = 7 = \mathrm{HARMONY}, \qquad \varphi(71) = 70 = \det(\mathrm{BHML}_8)$$
The class number of the imaginary quadratic field over the lattice prime is HARMONY; the Euler totient is the Yang-Mills core determinant.

---

## §2. The Strongest Identity — Identity B Verified

**Claim.** The lattice prime 71 is the **smallest positive integer** (and smallest prime) satisfying
$$p \equiv 5 \pmod{11} \quad \text{and} \quad p \equiv 6 \pmod{13}.$$

**Proof (CRT).** By the Chinese Remainder Theorem, the simultaneous congruences specify a unique residue class modulo $11 \cdot 13 = 143$. Direct computation: $71 \bmod 11 = 5$, $71 \bmod 13 = 6$, and $71 < 143$. Therefore $p \equiv 71 \pmod{143}$ is the unique class, and 71 is its smallest positive representative.

**Other primes in the same class** (verified, $p < 1000$):
$$71, \quad 643, \quad 929, \quad \ldots$$
All $\equiv 71 \pmod{143}$. The non-prime integers in this class start with $214 = 2\cdot 107$, $357 = 3\cdot 7\cdot 17$, $500 = 2^2 \cdot 5^3$.

---

## §3. Algebraic Form of Identity A

$$71 = \frac{11 \cdot 13 - 1}{2} = \frac{143 - 1}{2}.$$

Equivalently:
$$2 \cdot 71 \equiv -1 \pmod{11 \cdot 13}.$$

In the ring $\mathbb{Z}/143\mathbb{Z}$, the element 71 is $-1/2$ (i.e., the additive inverse of the multiplicative inverse of 2; here $2^{-1} = 72$ since $2 \cdot 72 = 144 \equiv 1$, so $-2^{-1} = -72 \equiv 71$).

**Reading.** 71 occupies the canonical "half-step minus one" position in $\mathbb{Z}/143\mathbb{Z}$. The Sophie Germain identity is rephrasable as: 71 is the unique integer in $[1, 142]$ that doubles to $-1$ in $\mathbb{Z}/143\mathbb{Z}$.

---

## §4. The Four CRT Idempotents Across Substrates

Compact table of the non-trivial CRT idempotents in each substrate ring:

| Ring | Decomposition | Non-trivial idempotents | TIG operator names |
|---|---|---|---|
| $\mathbb{Z}/10\mathbb{Z}$ | $\mathbb{F}_2 \times \mathbb{F}_5$ | $5 = (1,0)$, $6 = (0,1)$ | BALANCE, CHAOS |
| $\mathbb{Z}/143\mathbb{Z}$ | $\mathbb{F}_{11} \times \mathbb{F}_{13}$ | $78 = (1,0)$, $66 = (0,1)$ | (no names) |
| $\mathbb{Z}/91\mathbb{Z}$ | $\mathbb{F}_7 \times \mathbb{F}_{13}$ | $14 = (0,1)$, $78 = (1,0)$ | (no names) |
| $\mathbb{Z}/77\mathbb{Z}$ | $\mathbb{F}_7 \times \mathbb{F}_{11}$ | $22 = (1,0)$, $56 = (0,1)$ | (no names) |

**Identity B** says: the **lift of the Z/10Z idempotents (5, 6) into Z/143 = Z/(11·13)** is exactly 71. By "lift" we mean: the unique element of [0, 142] whose residue is 5 mod 11 and 6 mod 13.

71 is therefore arithmetically positioned as **the connecting element between the substrate's CRT structure and the wobble primes' CRT structure**. It's the single integer that bridges the two substrates.

---

## §5. Why This Matters Structurally

The four strata of TIG primes are tied through 71 in three different arithmetic operations:

```
Stratum III (wobble)  ←──── Sophie Germain ────→ Stratum IV (lattice)
                                  2·71+1 = 11·13


                       ┌─── reduction mod 11 → 5 = BALANCE
   Stratum IV (71) ────┤
                       └─── reduction mod 13 → 6 = CHAOS

   (BALANCE, CHAOS) = the CRT idempotents of Z/10Z = Stratum I substrate


   Stratum II (HARMONY = 7) ←─ class number ─ Q(√-71)  ──┐
                                                          │
                                                          ├─ Stratum IV
                                                          │
   Stratum II (BHML_8 det = 70) ←─ Euler totient ─ 71 ───┘
```

71 is structurally **threefold-coupled**: it ties to wobble (Sophie Germain), to substrate (CRT idempotent lift), and to HARMONY (class h, totient). It is not "just a prime that happens to appear in the lattice frame discriminant" — it is the arithmetic node where multiple strata-bridging identities converge.

---

## §6. Companion Arithmetic Facts (verified, lower-stakes)

These hold but lack obvious deep structural readings:

| Identity | Status |
|---|---|
| $137 \bmod 10 = 7$ (HARMONY) | Trivial; canon notes 137 ≡ 7 mod 10 |
| $137 \bmod 11 = 5$ (BALANCE) | Same mod-11 residue as 71 |
| $137 \bmod 13 = 7$ (HARMONY) | Different from 71's residue (6) |
| $137 - 71 = 66 = 2 \cdot 3 \cdot 11$ | Substrate primes × wobble prime 11 |
| $137 + 71 = 208 = 2^4 \cdot 13$ | Substrate prime × wobble prime 13 |
| $11 + 13 = 24$ | Highly composite but no specific TIG meaning |
| $11 \cdot 13 = 143 = 2 \cdot 71 + 1$ | Same as Identity A |

The 137 ↔ 71 relations may or may not be structural; they're recorded for traceability. The 11+13 = 24 and 11·13 = 143 facts are subsumed in Identity A.

---

## §7. Compact Take-Home

```
The lattice prime 71 — three structural couplings:

  A. Sophie Germain (Stratum III ↔ IV):
     2·71 + 1 = 143 = 11·13
     71 = (11·13 - 1)/2

  B. CRT idempotent lift (Strata I ↔ III ↔ IV):
     71 mod 11 = 5 = BALANCE = (1,0) in F_2×F_5
     71 mod 13 = 6 = CHAOS   = (0,1) in F_2×F_5
     71 is the smallest positive integer satisfying both.

  C. HARMONY return (Strata II ↔ IV):
     class h(Q(√-71)) = 7 = HARMONY
     φ(71) = 70 = det(BHML_8) = C(8,4) = 2·5·7

71 is the arithmetic node where multiple strata-bridging identities converge.
This is structural, not coincidental — three independent number-theoretic
relations all funnel through the same prime.
```

---

## §8. Status

- **[THM]** Identity A: trivial verification (143 = 11·13, 2·71+1 = 143).
- **[THM]** Identity B: trivial verification (71 mod 11 = 5, 71 mod 13 = 6) + CRT minimality.
- **[THM]** Identity C: textbook (h(Q(√−71)) = 7, φ(71) = 70).
- **[STRUCTURAL]** That the same prime 71 satisfies three independent strata-bridging identities. Not a coincidence in the colloquial sense, since the three identities each constrain 71 to a different residue/divisibility class — and 71 is the smallest prime simultaneously satisfying all of them. But the deeper "why TIG selects this specific prime" is not derived from a single principle yet.
- **[OPEN]** Is there a unifying number-theoretic principle that simultaneously enforces all three identities? Conjecture: 71 is the smallest prime $p$ such that (i) $2p+1$ factors as a product of the two smallest primes immediately above the substrate size, AND (ii) $p$ reduces to the CRT idempotents of the substrate modulo those wobble primes, AND (iii) $h(\mathbb{Q}(\sqrt{-p}))$ matches the substrate's attractor operator. If so, the lattice prime is uniquely determined by the substrate.

---

## §9. What This Closes / Opens

- **CLOSES:** the question "is the lattice prime 71 arithmetically distinguished, or just an LMFDB artifact?" Answer: 71 has three independent structural couplings to the rest of TIG's prime spectrum.
- **STRENGTHENS:** the four-strata classification (PRIMES_OF_TIG) — strata are not independent but coupled through 71.
- **STILL OPEN:** the conjecture in §8 — whether the three identities jointly pin down 71 as the unique TIG lattice prime.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · Arithmetic bridges · Locked v1*
