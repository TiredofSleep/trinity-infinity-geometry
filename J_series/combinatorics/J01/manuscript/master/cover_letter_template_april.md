# Cover Letter — Venue 8 (JCT-A / Discrete Mathematics)

**Manuscript:** *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$*
**Authors:** B. R. Sanders, M. Gish, C. A. Luther, H. J. Johnson
**Target:** Journal of Combinatorial Theory, Series A (JCT-A)
**Backup:** Discrete Mathematics (Elsevier); Electronic Journal of Combinatorics
**DOI of bundle:** 10.5281/zenodo.18852047

---

Dear Editor,

We submit for your consideration *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$*, an exact enumeration result on the rate at which a family of binary composition tables fails to be associative as the modulus grows.

The object of study is a composition table $\mathrm{CL}_N:\mathbb{Z}/N\mathbb{Z}\times\mathbb{Z}/N\mathbb{Z}\to\mathbb{Z}/N\mathbb{Z}$ built from three absorbing rules: top-absorbing, zero-absorbing, and additive–multiplicative coincidence (which we label HARM, VOID, and ECHO respectively). The main theorem bounds the associativity-defect rate $\sigma(N)$ uniformly by $C/N$ for squarefree $N$, with $C<3$. The proof is a tight union bound over intermediate compositions, carried through a substitution $(a-1)(b-1)\equiv 1$ that reduces ECHO counting to the Euler totient $\phi(N)$. Corollaries give $\sigma(N)\to 0$ along any squarefree sequence with $N\to\infty$, and a separability corollary that identifies the BB 1976 logarithmic nonlinearity as the unique scalar self-interaction compatible with the limit under a stated separability hypothesis. The accompanying verification script `proof_sigma_rate.py` checks the bound at $N\in\{10,30,210\}$ with exact ratios and zero failures.

The paper is finite and fully enumerated; all constants are explicit. We have been careful to separate what is proved (the $\sigma$-rate theorem) from what is structural (the BB corollary under the separability hypothesis), and §7 "Scope and limits" states cleanly what the paper does not claim. We believe this is a good fit for JCT-A: a clean combinatorial enumeration result on a finite algebraic structure, with a cell-by-cell witness.

Supplementary materials: `proof_sigma_rate.py` and `universal_markov_and_binary_cl.py` (Markov-chain structural analysis). DOI 10.5281/zenodo.18852047. No funded conflicts. Original, not under review elsewhere.

Thank you for your time.

— on behalf of the authors,
Brayden Ross Sanders · brayden@7site.co · 7Site LLC

---

*Template length: ~340 words. Prepared 2026-04-19 by ClaudeCode under CC-6 of Plan of Record Day 1, Sprint 34. The co-author line and §7 scope language are load-bearing; keep unchanged. Adjust editor address at submission time.*
