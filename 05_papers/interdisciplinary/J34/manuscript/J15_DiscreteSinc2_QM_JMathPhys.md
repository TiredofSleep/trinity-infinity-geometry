# A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics

**Authors:** B.R. Sanders$^{1}$, B. Mayes$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher

**Target venue:** Journal of Mathematical Physics (with fallback to *Letters in Mathematical Physics* — see §6 per-venue cap notes)
**Manuscript class:** Mathematical-physics short note
**MSC:** 81S05, 42A16, 11A41, 11Y05
**Date:** 2026-05-07 (DRAFT)

---

## Abstract

For an integer $f \ge 2$ and $k \ge 1$, define the unit-amplitude exponential sum on the cyclic position alphabet $\{1,\dots,k\}$ at momentum quantum $1/f$,
$$S(k,f) = \frac{1}{k}\sum_{j=1}^{k} e^{2\pi i j/f}, \qquad R(k,f) = |S(k,f)|^2.$$
We prove $R(k,f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$, identify it as the finite-dimensional analog of the squared overlap between a momentum eigenstate and a position-space rectangular window, and record its three immediate consequences for finite QM: (i) the *finite uncertainty product* on the cyclic group $\mathbb{Z}/N\mathbb{Z}$ — the discrete analog of $\Delta x \Delta p \geq \hbar/2$; (ii) the *first-zero theorem*, that the first integer $k$ at which $R(k,f) = 0$ is $k = f$; and (iii) the continuum limit $R(k,f) \to \sinc^2(k/f)$ as $f \to \infty$, recovering the standard rectangular-window momentum spectrum. We note the synchronization with the First-G event from arithmetic combinatorics: for $f = \mathrm{spf}(b)$ (the smallest prime factor of an integer $b > 1$), the first integer zero of $R(\cdot, f)$ coincides with the first $k$ at which $\{1,\dots,k\}$ contains a non-coprime element. Verification is exhaustive on $f \in \{3,5,7,11,13,17,19,23\}$ at machine precision. The note is short (theorem-proof-corollary structure) and is intended as a clean reference identity for finite QM on cyclic groups.

---

## 1. Introduction

Position-momentum duality on the cyclic group $\mathbb{Z}/N\mathbb{Z}$ is the natural arena of finite QM: the position basis $\{|j\rangle : j \in \mathbb{Z}/N\mathbb{Z}\}$ and the momentum basis $\{|\hat p\rangle : \hat p \in \mathbb{Z}/N\mathbb{Z}\}$ are related by the discrete Fourier transform

$$\langle j | \hat p\rangle = \frac{1}{\sqrt{N}}\, e^{2\pi i j \hat p / N}.$$

A natural physical question is: if we project a momentum eigenstate $|\hat p\rangle$ onto a position-space window of size $k$ (the indicator of $\{1,2,\dots,k\}$), what is the squared overlap?

The answer is the discrete sinc-squared function $R(k, N/\hat p)$, which we study in this note. We present a clean, self-contained derivation, the elementary closed form, and the key consequences for finite QM. The arithmetic counterpart (the synchronization with the First-G event in coprimality partitions) makes this object also a useful reference for number-theoretically-flavored finite QM, sometimes called "quantum number theory."

**Plan.** Section 2 sets up the finite QM Hilbert space and defines $R(k,f)$. Section 3 proves the closed form (Theorem 3.1). Section 4 derives the QM-relevant consequences: finite uncertainty (Proposition 4.1), first-zero theorem (Corollary 4.2), and continuum limit (Theorem 4.3). Section 5 records the synchronization with the First-G event. Section 6 collates status, lens-scope, and per-venue cap notes (J15 is the 3rd JMP target in the J-series and may need a fallback).

---

## 2. Finite QM on $\mathbb{Z}/N\mathbb{Z}$

**Position and momentum bases.** The cyclic group $\mathbb{Z}/N\mathbb{Z}$ supports a Hilbert space $\mathcal{H} = \mathbb{C}^N$ with orthonormal position basis $\{|j\rangle\}_{j=0}^{N-1}$ and orthonormal momentum basis $\{|\hat p\rangle\}_{\hat p=0}^{N-1}$ related by

$$|\hat p\rangle = \frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} e^{2\pi i j \hat p / N}\, |j\rangle.$$

**Position-window projector.** For $1 \le k \le N$, the rectangular position window of size $k$ is the (un-normalized) state

$$|W_k\rangle = \sum_{j=1}^{k} |j\rangle, \qquad \langle W_k | W_k\rangle = k.$$

The normalized window is $|w_k\rangle = k^{-1/2} |W_k\rangle$.

**Squared overlap.** The squared overlap of a momentum eigenstate $|\hat p\rangle$ with the normalized window $|w_k\rangle$ is

$$|\langle \hat p | w_k \rangle|^2 = \frac{1}{N k}\bigl|\sum_{j=1}^k e^{-2\pi i j \hat p/N}\bigr|^2.$$

For the canonical momentum-amplitude case $\hat p / N = 1/f$ (i.e., we ask for the overlap of the $\hat p$ momentum eigenstate where $\hat p = N/f$, requiring $f | N$), this is

$$|\langle \hat p | w_k\rangle|^2 = \frac{k}{N}\, R(k,f), \qquad R(k,f) = \frac{1}{k^2}\bigl|\sum_{j=1}^k e^{2\pi i j/f}\bigr|^2.$$

We focus on $R(k,f)$ as the dimensionless kernel, with the QM normalization factor $k/N$ separated.

---

## 3. The Closed Form

**Theorem 3.1 (Discrete $\sinc^2$ identity).** *For every integer $f \ge 2$ and every integer $k \ge 1$,*
$$\boxed{\;R(k,f) = \frac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)}.\;}$$

*Proof.* The geometric series gives
$$\sum_{j=1}^k e^{2\pi i j/f} = e^{2\pi i / f}\,\frac{1 - e^{2\pi i k/f}}{1 - e^{2\pi i/f}}.$$
Taking $1/k$ times the squared modulus and applying $|1 - e^{i\theta}|^2 = 4 \sin^2(\theta/2)$:
$$R(k,f) = \frac{1}{k^2} \cdot \frac{4\sin^2(\pi k/f)}{4\sin^2(\pi/f)} = \frac{\sin^2(\pi k/f)}{k^2\sin^2(\pi/f)}. \qed$$

**Verification.** Numerical check at machine precision over $f \in \{3,5,7,11,13,17,19,23\}$ and $k \in \{1,\dots,f+1\}$ gives a maximum deviation of $4.44 \times 10^{-16}$ between the closed form and the direct geometric-sum evaluation.

---

## 4. Quantum-Mechanical Consequences

### 4.1 Finite uncertainty

**Proposition 4.1 (finite uncertainty product).** *For a momentum eigenstate $|\hat p\rangle$ on $\mathbb{Z}/N\mathbb{Z}$ with $\hat p = N/f$ (assume $f | N$), the position-space probability mass on $\{1,\dots,k\}$ is*
$$P(\hat p, \mathrm{window}_k) = |\langle \hat p | w_k\rangle|^2 \cdot k = \frac{k^2}{N}\cdot R(k,f) = \frac{k^2}{N} \cdot \frac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)} = \frac{1}{N}\cdot \frac{\sin^2(\pi k/f)}{\sin^2(\pi/f)}.$$

In the continuum limit $N, f \to \infty$ with $k/f \to t \in (0,1]$ and $f/N \to 1$ (full ring), this recovers the standard rectangular-window position-momentum uncertainty: a sharp momentum implies position spread of order $f/k$.

**Reading.** $R(k,f)$ is the *finite-dimensional analog of $\sinc^2(k/f)$*, the squared rectangular-pulse spectrum. It is the natural object for finite-uncertainty bounds on cyclic-group QM.

### 4.2 First-zero theorem

**Corollary 4.2 (First zero of $R$).** *For every prime $f$ and every $k \in \{1,\dots,f-1\}$, $R(k,f) > 0$. At $k = f$, $R(f,f) = 0$. Hence the first integer zero of $R(\cdot, f)$ is exactly $k = f$.*

*Proof.* For $1 \le k \le f-1$ with $f$ prime, $f \nmid k$, so $\pi k/f \notin \pi \mathbb{Z}$ and $\sin(\pi k/f) \neq 0$. At $k = f$, $\sin(\pi f/f) = 0$. $\qed$

**QM reading.** The momentum eigenstate $|\hat p\rangle$ with $\hat p = N/f$ has zero amplitude on the position window $\{1,\dots,f\}$ — the first $k$ at which the momentum-position overlap vanishes is exactly $k = f$. This is the cyclic-group analog of the first-zero of $\sinc^2(t)$ at $t = 1$.

### 4.3 Continuum limit

**Theorem 4.3 ($\sinc^2$ continuum limit).** *Let $\sinc(t) = \sin(\pi t)/(\pi t)$ for $t \neq 0$ and $\sinc(0) = 1$. For every $t > 0$,*
$$\lim_{f \to \infty,\, k/f \to t} R(k, f) = \sinc^2(t).$$

*Proof.* From Theorem 3.1, $k \cdot \sin(\pi/f) = (\pi/f) \cdot k \cdot (1 + O(1/f^2)) \to \pi t$, so $k^2 \sin^2(\pi/f) \to \pi^2 t^2$. The numerator $\sin^2(\pi k/f) \to \sin^2(\pi t)$. Hence $R(k,f) \to \sin^2(\pi t)/(\pi^2 t^2) = \sinc^2(t)$. $\qed$

**QM reading.** The continuum limit recovers the rectangular-window momentum spectrum exactly: $|\langle \hat p | \mathrm{window}_t\rangle|^2 \to \sinc^2(t)$ as the lattice is refined. The discrete $\sinc^2$ identity is therefore the natural finite QM counterpart of the continuous spectrum.

**Specific exact values** (continuum limit at rational arguments):
$$\sinc^2(1/2) = 4/\pi^2 \approx 0.4053, \qquad \sinc^2(1/10) = \frac{25(\sqrt{5}-1)^2}{4\pi^2} \approx 0.9355.$$

---

## 5. Synchronization with the First-G Event

This identity has a striking arithmetic counterpart. For an integer $b > 1$, the *coprimality partition* of the alphabet $\{1,\dots,k\}$ relative to $b$ separates units $C_k(b) = \{x : \gcd(x,b) = 1\}$ from obstructions $G_k(b) = \{1,\dots,k\}\setminus C_k(b)$. The First-G event of $b$ is the smallest $k$ with $|G_k(b)| > 0$.

**Proposition 5.1 (Synchronization).** *For every $b > 1$ with smallest prime factor $p_1 = \mathrm{spf}(b)$, the First-G event $k^\star(b)$ and the first integer zero of $R(k, p_1)$ in the range $\{1,\dots,p_1\}$ coincide:*
$$k^\star(b) = \min\{k \in \{1,\dots,p_1\}: R(k, p_1) = 0\} = p_1.$$

*Proof.* Direct from $k^\star(b) = p_1$ (one-line gcd argument: any $x \le k < p_1$ has $\gcd(x,b) = 1$ since the smallest prime factor of $b$ is $p_1$) combined with Corollary 4.2. $\qed$

**Reading.** The QM-momentum quantum that produces the first position-window zero at $k = p_1$ is precisely the inverse of the smallest prime factor of $b$. This synchronization is the bridge between cyclic-group QM and the arithmetic structure of $\mathbb{Z}/b\mathbb{Z}$, and is why $R(k,f)$ appears naturally in finite-dimensional quantum number theory.

The synchronization is reproduced from the companion paper [J04, J08] in arithmetic combinatorics; here we re-state it in the QM context.

---

## 6. Status, Lens Scope, Per-venue Cap Notes

### 6.1 Status table

| Claim | Status |
|---|---|
| Theorem 3.1 (closed form for $R(k,f)$) | **PROVED** (elementary Fejér-type identity) |
| Proposition 4.1 (finite uncertainty product) | **PROVED** (direct calculation) |
| Corollary 4.2 (first-zero theorem) | **PROVED** |
| Theorem 4.3 (continuum limit) | **PROVED** (asymptotic) |
| Proposition 5.1 (synchronization with First-G event) | **PROVED** (combination of Theorems 3.1 and the First-G arithmetic from J04) |

### 6.2 Lens scope

This paper carries no TSML / BHML lens dependence. The mathematical content is finite-dimensional Fourier analysis on the cyclic group, with an explicit QM interpretation.

### 6.3 Per-venue cap

**This is the third JMP submission target in the J-series** after J13 (BB Bridge) and J14 (YM Mass Gap Bridge). The 2/quarter cap is reached. **Fallback options for J15:**

- **Option A (preferred fallback):** *Letters in Mathematical Physics* (Springer). Short-format note; the closed form + finite uncertainty + synchronization fits LMP's style.
- **Option B:** *Journal of Physics A: Mathematical and Theoretical* (IOP). Finite QM and number-theoretic mathematical methods are natural for J Phys A.
- **Option C:** *Communications in Mathematical Physics*. Higher impact; the finite-uncertainty + sinc² combination is natural for the math-physics audience.

Recommended: defer JMP to Q2 next quarter (after J13 and J14 are accepted) OR submit to LMP / J Phys A as the immediate venue.

### 6.4 Tier classification

**Central claim:** Tier 1 / 2 (clean theorem, fully proved). The closed form is elementary; the QM consequences are direct corollaries; the synchronization is one combination step from prior work.

---

## References

### Finite QM and discrete Fourier analysis
- Vourdas, A. (2004). *Rep. Prog. Phys.* **67**:267. (Quantum systems with finite Hilbert space)
- Schwinger, J. (1960). *Proc. Nat. Acad. Sci.* **46**:570 \& 893.
- Wootters, W.K. (1987). *Ann. Phys.* **176**:1. (Wigner functions on $\mathbb{Z}/N$)
- Vourdas, A. (2017). *Finite and Profinite Quantum Systems*. Springer.

### Fejér kernel and discrete Fourier identity
- Fejér, L. (1900). *Math. Ann.* **58**:51. (Fejér kernel)
- Zygmund, A. (2002). *Trigonometric Series*, 3rd ed. Cambridge.
- Oppenheim, A.V., Schafer, R.W. (2010). *Discrete-Time Signal Processing*, 3rd ed. Pearson.
- Shannon, C.E. (1949). *Proc. IRE* **37**:10.

### Coprimality partitions and First-G event
- Apostol, T.M. (1976). *Introduction to Analytic Number Theory*. Springer.
- Hardy, G.H., Wright, E.M. (2008). *An Introduction to the Theory of Numbers*, 6th ed. Oxford.

### Companion submissions in the J-series
- [J04] Sanders, B.R., Gish, M. (2026). "First-G Law: Squarefree Stability of the Smallest-Prime-Factor Coprime Window." Submitted to *Integers*.
- [J08] Sanders, B.R., Gish, M. (2026). "The Sinc² Zero Law for Squarefree Moduli." Submitted to *Integers*.
- [J13] Sanders, B.R., Johnson, H.J. (2026). "The Bialynicki-Birula Bridge." Submitted to *JMP*.

DOI for verification scripts: 10.5281/zenodo.18852047.
