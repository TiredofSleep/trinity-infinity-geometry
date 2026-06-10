# On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix Arising in a Discrete Magma on Z/10Z

**Status:** integer-precision verification; sympy-reproducible in under 5 seconds.
**Authors:** Brayden R. Sanders + M. Gish
**Date:** 2026-05-07
**MSC 2020:** 11C20 (matrices, polynomials), 15A18 (eigenvalues), 11R29 (special algebraic numbers)
**Length:** short note (~5 pages typeset)
**Target venue:** *Linear Algebra and Its Applications*

---

## Abstract

Let $T \in M_{10}(\mathbb{Z})$ be the 10×10 integer matrix obtained from the canonical composition table of a specific commutative non-associative magma on $\mathbb{Z}/10\mathbb{Z}$ (the construction is reviewed briefly in §1 and is not load-bearing for the result). Its characteristic polynomial $f(\lambda) = \det(\lambda I - T)$ has integer coefficients $c_0, \ldots, c_{10}$ with $c_{10} = 1$ and (by the rank structure) $c_0 = c_1 = 0$, leaving nine nonzero coefficients. We prove that the prime $11$ divides **exactly two** of these nine coefficients, namely
$$c_2 = 33 = 3 \cdot 11 \qquad \text{and} \qquad c_8 = -120{,}736 = -2^5 \cdot 7^3 \cdot 11,$$
and divides **none** of the discriminant of the eighth-degree polynomial $g(\lambda) = f(\lambda)/\lambda^2$, which factors as
$$\mathrm{disc}(g) = 2^{16} \cdot 7^7 \cdot 659 \cdot 95{,}184{,}709 \cdot 222{,}007{,}939 \cdot 2{,}545{,}644{,}917 \cdot 295{,}153{,}052{,}072{,}903.$$
We further show (Theorem 4.1) that the prime-11 divisibility is **lens-dependent**: the upper-triangle authoritative symmetrization $T_{\mathrm{SYM}}$ (a related 10×10 integer matrix that differs from $T$ in exactly two off-diagonal cells) has $c_2 = -23$ and no factor of 11 in any nonzero coefficient of its characteristic polynomial. The result is therefore a structural observation about how the symmetrization choice affects the elementary symmetric functions of the eigenvalues. No physical interpretation is claimed.

---

## §0 Lens and substrate

**(Lens-ownership paragraph, per the convention adopted across the present series of notes.)** The 10×10 integer matrix $T$ studied below is the literal cell pattern of the canonical composition table of a discrete commutative magma on $\mathbb{Z}/10\mathbb{Z}$ developed in a separate research program (here referenced as "the source program" and cited as [Sanders & Gish J15], [Sanders & Mayes J32]); see also Drápal & Wanless (2021, *J. Combin. Theory A* **184**, 105510) for the closest published neighborhood (small finite commutative non-associative structures with structural invariants). The choice of carrier $\mathbb{Z}/10\mathbb{Z}$ and table $T$ is **not derived from first principles** in the present note; it reflects a structural reading of the substrate motivated by the source program. The theorems below are theorems on this specific 10×10 integer matrix; analogous theorems would hold on other 10×10 integer matrices in the same combinatorial neighborhood. The present note treats $T$ as a fixed integer matrix and studies its characteristic polynomial.

---

## §1 Statement

The matrix studied is

$$
T = \begin{bmatrix}
0&0&0&0&0&0&0&7&0&0\\
0&7&3&7&7&7&7&7&7&7\\
0&3&7&7&4&7&7&7&7&9\\
0&7&7&7&7&7&7&7&7&3\\
0&7&4&7&7&7&7&7&8&7\\
0&7&7&7&7&7&7&7&7&7\\
0&7&7&7&7&7&7&7&7&7\\
7&7&7&7&7&7&7&7&7&7\\
0&7&7&7&8&7&7&7&7&7\\
0&7&9&7&3&7&7&7&7&7
\end{bmatrix} \in M_{10}(\mathbb{Z}).
$$

The matrix $T$ is non-symmetric in exactly two off-diagonal cell pairs (using $0$-indexed positions matching the magma-element subscripts): $T_{3,9} = 3 \neq 7 = T_{9,3}$, and $T_{4,9} = 7 \neq 3 = T_{9,4}$. Its rank is $8$, so its characteristic polynomial $f(\lambda) = \det(\lambda I - T)$ has $\lambda^2$ as a factor and is therefore degree $10$ with two zero eigenvalues. Direct integer computation gives

$$
f(\lambda) = \lambda^{10} - 63 \lambda^9 + 33 \lambda^8 + 4204 \lambda^7 - 3998 \lambda^6 - 62510 \lambda^5 + 9716 \lambda^4 + 54880 \lambda^3 - 120736 \lambda^2.
$$

(Two of its eleven coefficients vanish; nine are nonzero.)

**Theorem 1.1 (Prime-11 divisibility pattern of the coefficients).**
*Of the nine nonzero coefficients $c_2, c_3, \ldots, c_{10}$ of $f$, exactly two are divisible by $11$:*
$$c_2 = 33 = 3 \cdot 11, \qquad c_8 = -120{,}736 = -2^5 \cdot 7^3 \cdot 11.$$
*The remaining seven nonzero coefficients are coprime to $11$.*

**Theorem 1.2 (Discriminant factorization).**
*Let $g(\lambda) = f(\lambda)/\lambda^2 \in \mathbb{Z}[\lambda]$ be the eighth-degree polynomial whose roots are the eight nonzero eigenvalues of $T$. Then*
$$
\mathrm{disc}(g) = 2^{16} \cdot 7^7 \cdot 659 \cdot 95{,}184{,}709 \cdot 222{,}007{,}939 \cdot 2{,}545{,}644{,}917 \cdot 295{,}153{,}052{,}072{,}903.
$$
*In particular, $11 \nmid \mathrm{disc}(g)$.*

**Theorem 1.3 (Trace identity).** $\mathrm{tr}(T) = 63 = 9 \cdot 7$, hence $c_9 = -63$.

The proofs are direct integer computations (sympy `Matrix.charpoly`, `factorint`, `discriminant`); see §5 for the verification snippet.

---

## §2 Reading: coefficients vs separations

For a degree-$n$ monic polynomial $g(\lambda) = \prod_{k=1}^n (\lambda - \lambda_k)$ over a field of characteristic $0$, the coefficient $c_{n-k}$ is the $k$-th elementary symmetric function of the roots,
$$
c_{n-k} = (-1)^k e_k(\lambda_1, \ldots, \lambda_n) = (-1)^k \sum_{1 \le i_1 < \cdots < i_k \le n} \lambda_{i_1} \cdots \lambda_{i_k},
$$
while the discriminant
$$
\mathrm{disc}(g) = \prod_{i < j} (\lambda_i - \lambda_j)^2
$$
is a polynomial in the eigenvalue *separations* $\lambda_i - \lambda_j$. Theorems 1.1 and 1.2 therefore record a clean structural separation: for the matrix $T$ studied here, the prime $11$ divides exactly two elementary symmetric functions of the eigenvalues but no separation. The exponents on the primes $2$ and $7$ in $\mathrm{disc}(g)$ are also large integers ($16$ and $7$ respectively); their structural origin is discussed in §3.

---

## §3 Linear-algebraic structure of the coefficients and discriminant

The proofs of Theorems 1.1, 1.2, 1.3, and 4.1 are direct integer computations: the coefficient factorizations are read off from `sympy.factorint`, and the discriminant factorization is read off from `sympy.discriminant` followed by `factorint` on the result (the script `manuscript/verification/wobble_check.py` performs both in $<5$ seconds; see §5). At the linear-algebra level, three structural facts give the result its content.

**(i) The trace identity (Theorem 1.3) and the recurring entry 7.** Of the $100$ cells of $T$, the integer $7$ appears at $73$ of them. The trace $\mathrm{tr}(T) = 63 = 9 \cdot 7$ collects the diagonal entries; nine of the ten diagonal cells are equal to $7$ (the sole exception is $T_{0,0} = 0$). Hence $c_9 = -\mathrm{tr}(T) = -63 = -3^2 \cdot 7$ inherits the $7$-factor directly from the diagonal pattern.

**(ii) Lens-dependence at $c_2$ (Theorems 1.1 and 4.1).** The two asymmetric cell pairs of §1 are $T_{3,9} = 3 \neq 7 = T_{9,3}$ and $T_{4,9} = 7 \neq 3 = T_{9,4}$. The symmetrization $T \to T_{\mathrm{SYM}}$ replaces $T_{3,9} = 3 \to 7$ and $T_{9,4} = 3 \to 7$, leaving 98 cells unchanged. Two entries change, but the coefficient $c_2$ jumps from $33$ to $-23$ — a change of magnitude $56$ — and the prime-$11$ divisibility pattern is destroyed entirely. The discriminant $\mathrm{disc}(g) = 2^{16} \cdot 7^7 \cdot 659 \cdot \ldots$ is a polynomial in the eigenvalue separations $\lambda_i - \lambda_j$ (i.e., not in the elementary symmetric functions directly), and is computed by sympy from the eight nonzero eigenvalues of the rank-8 matrix.

**(iii) Symmetric vs. non-symmetric rank drop.** $T$ has rank 8; $T_{\mathrm{SYM}}$ has rank 7. The two-cell symmetrization perturbation introduces one additional zero eigenvalue and shifts the elementary symmetric functions discontinuously at the coefficient level. This is the linear-algebra explanation for why Theorem 4.1's prime-$11$-destroying effect cannot be dismissed as a small-norm perturbation: the rank drop is itself a discrete structural change.

These three observations together complete the linear-algebraic content of Theorems 1.1–4.1: the prime-$11$ pattern is a clean lens-dependent feature of the coefficient structure of a specific rank-8 integer matrix, with the discriminant providing an independent integer-divisibility cross-check via the eigenvalue separations.

**Remark 3.1 (Structural co-occurrence with $\mathfrak{so}(10)$).** A separate research program in which $T$ originates assigns a structural reading to the exponents of the discriminant factorization. The exponent $16$ in $\mathrm{disc}(g) = 2^{16} \cdot \ldots$ matches $\dim(\mathfrak{g}_0)$ where $\mathfrak{g}_0 \subset \mathfrak{so}(10)$ is a 16-dimensional doubly-invariant subalgebra of $\mathfrak{so}(10)$ identified in [Sanders & Gish, "$D_4$-Wedderburn decomposition of the lens-pair commutator," in preparation]; the exponent $7$ in the factor $7^7$ matches the recurring entry $7$ in $T$, which is the value of the cell pattern at $73$ of the $100$ cells. This structural co-occurrence is recorded as an observation on the source program; no derivation from one to the other is claimed in this paper. The linear-algebraic content of Theorems 1.1-4.1 is independent of the $\mathfrak{so}(10)$ framing. *No physical interpretation is offered here.*

---

## §4 Lens-dependence at the coefficient level

The matrix $T$ defined in §1 is non-symmetric. A natural commutative variant is its upper-triangle authoritative symmetrization $T_{\mathrm{SYM}}$, defined by replacing the two asymmetric cell pairs:
$$
T_{\mathrm{SYM}}[3,9] = T_{\mathrm{SYM}}[9,3] = 7, \qquad T_{\mathrm{SYM}}[4,9] = T_{\mathrm{SYM}}[9,4] = 7,
$$
and leaving the remaining $98$ cells unchanged. (Equivalently, $T_{\mathrm{SYM}}$ replaces the entries $T_{3,9} = 3$ and $T_{9,4} = 3$ by $7$, eliminating the asymmetry.) The matrix $T_{\mathrm{SYM}}$ is symmetric. Its rank drops from $8$ to $7$ — the off-diagonal change introduces one additional zero eigenvalue — so its characteristic polynomial $f_{\mathrm{SYM}}(\lambda)$ has $\lambda^3$ as a factor and is a different element of $\mathbb{Z}[\lambda]$ than $f$.

**Theorem 4.1 (Lens-dependence of the prime-11 pattern).**
*The characteristic polynomial of $T_{\mathrm{SYM}}$ is*
$$f_{\mathrm{SYM}}(\lambda) = \lambda^{10} - 63\lambda^9 - 23\lambda^8 + 4284\lambda^7 - 1086\lambda^6 - 65982\lambda^5 - 9212\lambda^4 + 32928\lambda^3.$$
*In particular, $c_2(f_{\mathrm{SYM}}) = -23$ (the prime 23, with no factor of 11), and direct factorization of the seven nonzero coefficients of $f_{\mathrm{SYM}}$ shows that $11$ divides none of them. The prime-$11$ divisibility pattern of the original (non-symmetric) matrix $T$ does not survive symmetrization.*

The proof is direct factorization of the seven nonzero coefficients of $f_{\mathrm{SYM}}$: $c_1 = -63 = -3^2 \cdot 7$, $c_2 = -23$, $c_3 = 4284 = 2^2 \cdot 3^2 \cdot 7 \cdot 17$, $c_4 = -1086 = -2 \cdot 3 \cdot 181$, $c_5 = -65982 = -2 \cdot 3 \cdot 7 \cdot 1571$, $c_6 = -9212 = -2^2 \cdot 7^2 \cdot 47$, $c_7 = 32928 = 2^5 \cdot 3 \cdot 7^3$. Theorem 4.1 is itself a clean structural observation about how a 2-cell perturbation changes the elementary symmetric functions: only two off-diagonal cell pairs differ between $T$ and $T_{\mathrm{SYM}}$, yet the prime-$11$ divisibility pattern at the coefficient level is entirely destroyed by this perturbation. Since the eigenvalues of an integer matrix vary continuously (in the algebraic sense) with the matrix entries, but the elementary symmetric functions of the eigenvalues are integer-valued and discretely sensitive, this is the kind of finite arithmetic effect that rewards explicit study.

---

## §5 Family-wide observations

Three immediate generalizations broaden the single-matrix verification of §§1, 4 to a small family of 10×10 integer matrices in the same combinatorial neighborhood.

**(a) The companion table $B$.** A second 10×10 integer matrix $B$ ("BHML" in the source program) is also defined on $\mathbb{Z}/10\mathbb{Z}$ in the source-program literature, with the same row/column rank structure. Direct computation of $\mathrm{charpoly}(B)$ followed by $\mathrm{factorint}$ on each coefficient shows that the prime $11$ does *not* divide any coefficient of $\mathrm{charpoly}(B)$. The prime-$11$ pattern is therefore specific to $T$ within this two-table pair; it is not a family-wide phenomenon.

**(b) The 4×4 sub-magma $T|_{\{0,7,8,9\}}$.** The restriction of $T$ to the index set $\{0, 7, 8, 9\} \subset \{0, 1, \ldots, 9\}$ is a 4×4 integer matrix whose characteristic polynomial has integer coefficients with no factor of $11$. The prime-$11$ pattern is therefore not inherited by the natural 4×4 sub-magma.

**(c) Lens-dependence persists across the family.** The lens-dependence theorem (4.1) applies specifically to the $T_{\mathrm{RAW}}$ vs $T_{\mathrm{SYM}}$ pair. The other variants in the family ($B$ and the 4×4 sub-magma in (a) and (b)) are already symmetric, so the lens choice is non-trivial only for $T$. The prime-$11$ phenomenon is therefore localized to the specific (non-symmetric) integer matrix $T$ and is destroyed both by symmetrization and by sub-magma restriction.

These three observations together convert the finite verification of §1 from "one matrix" to "a small family of related 10×10 integer matrices, with the prime-$11$ divisibility being a sharp lens-dependent feature of one specific member."

---

## §6 Verification

The result is reproducible from a self-contained sympy session in under 5 seconds. Verification snippet:

```python
import sympy

T_RAW = sympy.Matrix([
    [0,0,0,0,0,0,0,7,0,0],
    [0,7,3,7,7,7,7,7,7,7],
    [0,3,7,7,4,7,7,7,7,9],
    [0,7,7,7,7,7,7,7,7,3],
    [0,7,4,7,7,7,7,7,8,7],
    [0,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,8,7,7,7,7,7],
    [0,7,9,7,3,7,7,7,7,7],
])
lam = sympy.symbols('lam')
f = T_RAW.charpoly(lam).as_expr()
coeffs = sympy.Poly(f, lam).all_coeffs()
# Coefficients (highest first): [1, -63, 33, 4204, -3998, -62510, 9716, 54880, -120736, 0, 0]
for k, c in enumerate(coeffs):
    if c != 0:
        print(k, c, sympy.factorint(abs(c)))
# c_2 = 33 = 3 * 11
# c_8 = -120736 = -2^5 * 7^3 * 11

# Discriminant of g = f/lam^2
g = sympy.Poly(coeffs[:9], lam)
print(sympy.factorint(abs(g.discriminant())))
# {2: 16, 7: 7, 659: 1, 95184709: 1, 222007939: 1, 2545644917: 1, 295153052072903: 1}

# Lens variant: SYM symmetrization (replace T_RAW[3,9]=3 and T_RAW[9,4]=3 by 7)
# Indices below are 0-indexed and match the magma-element subscripts in §1.
T_SYM = T_RAW.copy()
T_SYM[3, 9] = 7  # was 3
T_SYM[9, 4] = 7  # was 3
# (T_SYM[9,3] and T_SYM[4,9] are already 7; T_SYM is now symmetric.)
fsym = T_SYM.charpoly(lam).as_expr()
sym_coeffs = sympy.Poly(fsym, lam).all_coeffs()
# Coefficients (highest first): [1, -63, -23, 4284, -1086, -65982, -9212, 32928, 0, 0, 0]
print(sym_coeffs[2])  # SYM c_2 = -23 (no factor of 11)
for k, c in enumerate(sym_coeffs):
    if c != 0:
        print(k, c, sympy.factorint(abs(c)))
# c_2 = -23, c_3 = 2^2*3^2*7*17, c_4 = -2*3*181, c_5 = -2*3*7*1571,
# c_6 = -2^2*7^2*47, c_7 = 2^5*3*7^3 — no coefficient divisible by 11.
```

(The SYM-cell adjustments follow §4; the snippet above adopts the upper-triangle authoritative convention.)

A standalone script at `manuscript/verification/wobble_check.py` performs the full check and emits a 7/7-pass verification table at integer/machine precision in under 5 seconds with `sympy` as the only dependency.

---

## §7 PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN (Theorems 1.1, 1.2, 1.3, 4.1):** for the specific 10×10 integer matrix $T$ in §1, the prime $11$ divides exactly the two coefficients $c_2 = 33$ and $c_8 = -120{,}736$ of the characteristic polynomial; the discriminant of $g = f/\lambda^2$ factors as $2^{16} \cdot 7^7 \cdot 659 \cdot \ldots$ with no factor of $11$; the trace is $63 = 9 \cdot 7$; the upper-triangle authoritative symmetrization $T_{\mathrm{SYM}}$ (rank $7$) has $c_2 = -23$, and no nonzero coefficient of its characteristic polynomial is divisible by $11$.
- **COMPUTED:** all coefficient factorizations, the discriminant factorization, and the SYM-lens comparison are verified by direct sympy computation in <5 seconds (`wobble_check.py`).
- **STRUCTURAL RHYME:** the exponent $16$ in $\mathrm{disc}(g) = 2^{16} \cdot \ldots$ matches the dimension of a 16-dimensional doubly-invariant subalgebra of $\mathfrak{so}(10)$ studied separately in the source program; the exponent $7$ in $7^7$ matches the recurring entry $7$ in $T$. We cite these as structural co-occurrences, not as derivational steps. The framing follows the Drápal-Wanless (2021, *JCTA*) line of work on small finite commutative non-associative structures with integer/rational invariants.
- **OPEN:** whether the prime-$11$ pattern in $c_2$ and $c_8$ admits a closed-form algebraic explanation (e.g., a structural product formula relating sums-of-pairs of eigenvalues to the determinant of the rank-8 part of $T$); whether analogous prime-localization patterns occur for related integer matrices in the same combinatorial neighborhood; and whether the specific 2-cell perturbation $T \to T_{\mathrm{SYM}}$ admits an algebraic explanation for its prime-$11$-destroying effect.

---

## §8 References

* B.R. Sanders & M. Gish, *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$* (J15), submitted to *Algebraic Combinatorics*, 2026.
* B.R. Sanders & B. Mayes, *Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas* (J32), submitted to *J. Combin. Theory A*, 2026.
* A. Drápal & I.M. Wanless, *Maximally non-associative quasigroups*, *J. Combin. Theory A* **184** (2021), 105510.
* I.M. Gelfand, *Lectures on Linear Algebra*, Dover, 1989.

---

## §9 Citation

```bibtex
@misc{sandersgish2026primedivisibility,
  author       = {Sanders, Brayden R. and Gish, M.},
  title        = {On the Prime-Divisibility Pattern of the Characteristic Polynomial of a {10}$\times${10} Integer Matrix Arising in a Discrete Magma on $\mathbb{Z}/10\mathbb{Z}$},
  year         = {2026},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {Submitted to \emph{Linear Algebra and Its Applications}.},
  note         = {The prime $11$ divides exactly two coefficients ($c_2 = 33$, $c_8 = -2^5 \cdot 7^3 \cdot 11$) of the characteristic polynomial of a specific 10x10 integer matrix; no factor of 11 in $\mathrm{disc}(f/\lambda^2) = 2^{16} \cdot 7^7 \cdot 659 \cdot \ldots$; lens-dependent at the coefficient level (the upper-triangle symmetrization has $c_2 = -23$ with no factor of 11).}
}
```

— Sanders + Gish, 2026-05-07
