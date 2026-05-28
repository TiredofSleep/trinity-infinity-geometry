# J27 Theorem 4 (thm:pkernel) — Case B Proof Tightening

**Date:** 2026-05-28
**Manuscript:** `05_papers/algebra/J27/manuscript/manuscript.tex`
**Theorem:** Theorem 6.1 (`thm:pkernel`), "No joint-injective pair for prime powers"
**Scope of edit:** Lines 555-611 (Case B only). Theorem statement and Case A unchanged.
**Verify:** `manuscript/verify_joint_injectivity.py` — all 5 / 5 theorem checks still PASS (re-run after edit; prime-power obstruction tested over 325 (n, d, g) cases on n in {4, 8, 9, 16, 25, 27, 49, 125}).

---

## §1. Original Case B sketch (verbatim, pre-edit, lines 555-611)

```
\medskip\noindent\textit{Case B: $g \not\equiv 1 \pmod p$.} Then
$M_{g}$ acts non-trivially modulo $p$, hence shuffles $A_{p}$-fibers.
For the joint pair to fail, we exhibit two elements in the same
$A_{p^{a}}$-fiber whose orbits under $M_{g}$ coincide. Take
$x_{1} = p^{a}$ and $x_{2} = 2 p^{a}$ (both lying in $A_{p^{a}}^{-1}(0)$
since $p^{a}$ and $2 p^{a}$ are both $\equiv 0 \pmod{p^{a}}$). The
orbit of $p^{a}$ under $M_{g}$ is contained in $p^{a} \cdot
\langle g \rangle \pmod{p^{r}}$, which is a subset of $p^{a} \cdot
\Z/p^{r-a}\Z$ (since $p^{a}$ multiplied by anything stays in this
sub-ideal modulo $p^{r}$). Similarly for $2 p^{a}$. The orbits of
$p^{a}$ and $2 p^{a}$ under $M_{g}$ are distinct cosets of
$\langle g \rangle$ acting on $p^{a} \cdot \Z/p^{r-a}\Z$ generally,
\emph{but} when $\langle g \rangle$ has the right order they can
coincide --- specifically, when $g$ is a generator of
$(\Z/p^{r}\Z)^{\times}$ or a sufficient power thereof. The argument
is delicate; the cleanest formulation uses the kernel-of-reduction
structure:

By the decomposition \eqref{eq:prpunit-decomp}, $g = g_{0} \cdot
g_{1}$ with $g_{0} \in (\Z/p\Z)^{\times}$ and $g_{1} \in 1 + p\Z/p^{r}\Z$.
The orbit of any element under $M_{g}$ has length
$\mathrm{lcm}(\ord(g_{0}), \ord(g_{1}))$. The $A_{p^{a}}$-fibers
have size $p^{r-a}$. For the joint refinement $A_{p^{a}} \wedge
\pi_{\dyn}(g)$ to be discrete, the orbit of every element must
intersect each $A_{p^{a}}$-fiber in at most one point --- but the
orbit length is at most $|(\Z/p^{r}\Z)^{\times}| = p^{r-1}(p-1)$, and
it must visit $p^{r-a}$ fibers via at most $p^{r-1}(p-1)$ steps.
When $a \ge 1$, the constraint is satisfiable in principle; but the
\emph{kernel-of-reduction action} forces all orbits to satisfy
$y \equiv x \pmod p$ for every $y$ in the orbit of $x$ under $g_{1}$
alone (when $g_{0} = 1$, Case A) --- so the orbit cannot reach a
point in a different $A_{p}$-fiber (let alone a different
$A_{p^{a}}$-fiber for $a \ge 1$).

In Case B with $g_{0} \ne 1$, the orbit of any $x$ visits multiple
$A_{p}$-fibers via the $g_{0}$-action. However, the sub-orbits within
the same $A_{p^{a}}$-fiber are governed by powers $g^{t}$ for which
$g^{t} \equiv 1 \pmod{p}$ --- equivalently $g_{0}^{t} = 1$ in
$(\Z/p\Z)^{\times}$, i.e., $\ord(g_{0}) \mid t$. For such $t$,
$g^{t} = g_{0}^{t} \cdot g_{1}^{t} = 1 \cdot g_{1}^{t} \in
1 + p\Z/p^{r}\Z$, so $g^{t}$ acts as a kernel-of-reduction element.
By Case A applied to this kernel element (which is non-identity
because $g \ne 1$ and $\ord(g_{1}) > 1$ in the generic case, or by
considering a higher power), there is a pair $\{x, g^{t} x\} \in
U(A_{p^{a}}) \cap U(\pi_{\dyn}(g))$ with $g^{t} x \ne x$. Hence joint
injectivity fails in Case B as well.

(The edge case where $\ord(g_{1}) = 1$, i.e., $g_{1} = 1$, reduces
to $g = g_{0}$ acting purely on the $(\Z/p\Z)^{\times}$ component;
then $g$ acts on the multiplicative units of the residue field
$\F_{p}$ but cannot resolve the kernel-of-reduction direction at all,
so the joint with $A_{p^{a}}$ still fails to be injective whenever
$a < r$ --- a direct kernel-of-reduction argument: pick $x_{1} = 1$
and $x_{2} = 1 + p^{a}$. Both lie in the same $A_{p^{a}}$-fiber, and
$g^{t} \cdot 1 = g^{t}$ while $g^{t} \cdot (1 + p^{a}) = g^{t} +
g^{t} p^{a}$; the orbits coincide modulo $p^{a}$ regardless of $t$.)
```

### What was wrong with the original sketch

1. **`x_1 = p^a`, `x_2 = 2 p^a` was a red herring**: the paragraph asserted these two elements would give the witness pair when "$\langle g \rangle$ has the right order they can coincide ... specifically, when $g$ is a generator", with no explicit verification.
2. **Bookkeeping for `t` was implicit**: the kernel-of-reduction reduction said "$g^t$ is a kernel-of-reduction element... By Case A applied to this kernel element (which is non-identity because $g \ne 1$ and $\ord(g_1) > 1$ in the generic case, or by considering a higher power)" — the "or by considering a higher power" hand-waves around the $\ord(g_1) = 1$ edge case rather than splitting it out.
3. **The parenthetical for the $\ord(g_1) = 1$ edge case was mathematically wrong**: it proposed witness pair `{1, 1 + p^a}`, then verified only that `g^t * 1` and `g^t * (1 + p^a)` differ by `g^t * p^a` (which is `0 mod p^a`). But that shows the two **orbits** are pointwise congruent modulo `p^a` — it does **not** show `1` and `1 + p^a` lie in the **same** orbit. Direct check (p=3, r=2, a=1, g=8): orbit of `1` is `{1, 8}`, orbit of `4 = 1 + 3` is `{4, 5}` — these are **different** orbits, so `{1, 4}` is **not** an unresolved pair in `U(\pi_dyn(g))`.

---

## §2. Rewritten Case B (verbatim, post-edit, lines 555-620)

```
\medskip\noindent\textit{Case B: $g \not\equiv 1 \pmod p$.} By the
decomposition \eqref{eq:prpunit-decomp}, write $g = g_{0} \cdot g_{1}$
with $g_{0} \in (\Z/p^{r}\Z)^{\times}$ the canonical (Teichm\"uller)
lift of $g \bmod p \in (\Z/p\Z)^{\times}$ and $g_{1} \in 1 +
p\Z/p^{r}\Z$. The Case B hypothesis $g \not\equiv 1 \pmod p$ is
equivalent to $g_{0} \ne 1$. Since $\ord(g_{0}) \mid p - 1$ and
$\ord(g_{1}) \mid p^{r-1}$, the orders are coprime, so
\begin{equation}\label{eq:order-product}
  \ord(g) \;=\; \mathrm{lcm}(\ord(g_{0}), \ord(g_{1}))
  \;=\; \ord(g_{0}) \cdot \ord(g_{1}).
\end{equation}
We split into two sub-cases on $\ord(g_{1})$.

\smallskip\noindent\textit{Sub-case B1: $\ord(g_{1}) > 1$
(equivalently $g_{1} \ne 1$).} Set
\[
  t \;:=\; \ord(g_{0}).
\]
Then $g^{t} = g_{0}^{t} \cdot g_{1}^{t} = 1 \cdot g_{1}^{t} = g_{1}^{t}
\in 1 + p\Z/p^{r}\Z$, so $g^{t}$ is a kernel-of-reduction element. By
\eqref{eq:order-product}, $\ord(g) = t \cdot \ord(g_{1})$; since
$\ord(g_{1}) > 1$, we have $\ord(g) > t$, hence $g^{t} \ne 1$. Write
$g^{t} = 1 + p u^{*}$ with $u^{*} \in \Z/p^{r-1}\Z$, $u^{*} \ne 0$,
and set $v := v_{p}(u^{*}) \in \{0, 1, \ldots, r-2\}$. Choose
\[
  c \;:=\;
  \begin{cases}
    1 & \text{if } v \ge a-1, \\
    p^{a-1-v} & \text{if } v < a-1,
  \end{cases}
\]
and set $x := c$, $y := g^{t} \cdot c$. Then $y - x = (g^{t} - 1) c
= p u^{*} c$, so $v_{p}(y - x) = 1 + v + v_{p}(c)$. In both branches
$1 + v + v_{p}(c) \ge a$ (the first because $v \ge a-1$ and $v_{p}(c)
= 0$; the second because $v + v_{p}(c) = v + (a-1-v) = a-1$), so
$p^{a} \mid (y - x)$ and hence $A_{p^{a}}(x) = A_{p^{a}}(y)$. In
both branches $1 + v + v_{p}(c) \le r-1 < r$ (the first because $v
\le r-2$ and $v_{p}(c) = 0$; the second because $v + v_{p}(c) = a-1
\le r-2$), so $y - x \ne 0$ in $\Z/p^{r}\Z$, i.e., $y \ne x$.
Finally, $y = g^{t} x = g^{t} \cdot c$ lies in $\orb_{g}(x)$ because
$g^{t} \in \langle g \rangle$. Hence $\{x, y\} \in U(A_{p^{a}}) \cap
U(\pi_{\dyn}(g))$ with $x \ne y$.

\smallskip\noindent\textit{Sub-case B2: $\ord(g_{1}) = 1$
(equivalently $g_{1} = 1$, so $g = g_{0}$).} In this sub-case
$\ord(g) = \ord(g_{0})$ divides $p-1$, which is coprime to $p$. In
particular, no positive power of $g$ lies in the kernel of reduction
$1 + p\Z/p^{r}\Z$ except $g^{\ord(g)} = 1$, so the B1 reduction does
not apply. Instead we exhibit the witness pair directly in the
$p^{r-1}$-sub-ideal. Set
\[
  x \;:=\; p^{r-1}, \qquad y \;:=\; g \cdot p^{r-1}.
\]
Since $a \le r - 1$, we have $p^{a} \mid p^{r-1}$, so both $x$ and
$y - x = (g - 1) p^{r-1}$ are divisible by $p^{a}$ (the latter
because $p^{a} \mid p^{r-1}$). Hence $A_{p^{a}}(x) = 0 =
A_{p^{a}}(y)$. The Case B hypothesis $g \not\equiv 1 \pmod p$ gives
$v_{p}(g - 1) = 0$, so $v_{p}((g - 1) p^{r-1}) = r - 1 < r$;
therefore $y - x \ne 0$ in $\Z/p^{r}\Z$ and $y \ne x$. By
construction $y = g \cdot x \in \orb_{g}(x)$. Hence $\{x, y\} \in
U(A_{p^{a}}) \cap U(\pi_{\dyn}(g))$ with $x \ne y$.

\smallskip
In each sub-case of Case B we have exhibited the required
unresolved pair, completing the proof.
```

### What the rewrite does

1. **Decomposition first, dichotomy on `\ord(g_1)`.** The decomposition `g = g_0 g_1` from the standard Hensel-lift iso is set up at the top of Case B; orders coprime gives `\ord(g) = \ord(g_0) \cdot \ord(g_1)` (the new labelled equation `eq:order-product`); the two sub-cases are then `\ord(g_1) > 1` (B1) and `\ord(g_1) = 1` (B2).
2. **Sub-case B1 (`\ord(g_1) > 1`) — explicit `t` and explicit `c`.** Choose `t := \ord(g_0)`, then `g^t = g_1^t` is in the kernel of reduction. Non-triviality follows from `\ord(g) = t \cdot \ord(g_1) > t`. Write `g^t = 1 + p u^*` with `u^* != 0`, let `v := v_p(u^*) \in {0, ..., r-2}`. Choose `c = 1` if `v >= a-1`, else `c = p^{a-1-v}`. Both branches yield `v_p(y-x) \in [a, r-1]`, simultaneously ensuring `p^a | (y - x)` (so `A_{p^a}` collapses the pair) and `y != x` (so the pair is non-trivial). `y = g^t x` lies in `\orb_g(x)` because `g^t \in \langle g \rangle`.
3. **Sub-case B2 (`\ord(g_1) = 1`, i.e., `g_1 = 1`, `g = g_0` of order dividing `p-1`).** Explicit witness: `x = p^{r-1}`, `y = g p^{r-1}`. Both lie in the `A_{p^a}`-fiber of `0` because `p^a | p^{r-1}` (since `a <= r-1`). Distinctness: `v_p(g-1) = 0` from the Case B hypothesis, so `v_p((g-1) p^{r-1}) = r-1 < r`, hence `y - x != 0` in `Z/p^r Z`. `y \in \orb_g(x)` by construction.

### Empirical verification

The two new constructions were checked against the prime-power case sweep used in `verify_joint_injectivity.py` (Theorem 5 block, n in {4, 8, 9, 16, 25, 27, 49, 125}, 325 (n, d, g) cases with g != 1). For every Case B instance (i.e., every (n, d, g) with `g mod p != 1`), the B1 or B2 construction yields (x, y) such that:
- (i) x != y in Z/nZ,
- (ii) x ≡ y (mod p^a) [same A_{p^a}-fiber], and
- (iii) y \in orb_g(x) [same multiplicative orbit].

Every case verified. The existing 5/5 PASS suite is preserved (no changes to the script were needed; the script tests the conclusion of the theorem, not the construction).

---

## §3. Open issues / things needing user input

**None blocking ship.** The Case B proof is now rigorous and the witness pair is constructive in both sub-cases. Two notes the user may want to consider for future polish:

1. **Case A has a parallel sloppiness that is NOT in scope per task constraints.** Case A (lines 541-553, unmodified per task instruction "DO NOT modify Case A") states the framework for `g \equiv 1 \pmod p` but then specializes to `g = 1 + p^a` rather than handling an arbitrary `g \equiv 1 \pmod p`. The construction generalizes (same trick used in new sub-case B1: choose `c = p^{\max(0, a-1-v_p(u))}`), and the theorem is correct as stated; but a referee may also flag Case A. If/when Case A is tightened, the natural mirror is to replace the "to ensure such u exists, take g = 1 + p^a" sentence with the same explicit `c`-choice used in sub-case B1.

2. **The remark immediately following the proof (`rem:pkernel-essence`, lines 622-635) is unchanged and remains accurate.** It states the obstruction at the level of orbit structure; both sub-cases of the new proof bear this out (B1: the orbit of `x = c` under `M_{g^t}` stays in a single `A_{p^a}`-fiber because `g^t \in 1 + p\Z/p^r\Z`; B2: the orbit of `x = p^{r-1}` lives entirely in the `p^{r-1}`-sub-ideal, hence in a single `A_{p^a}`-fiber).

No mathematics was invented; all material was either present in the old sketch (B1's kernel-of-reduction reduction) or is the standard Teichmüller-decomposition argument (B2's explicit `p^{r-1}` witness).
