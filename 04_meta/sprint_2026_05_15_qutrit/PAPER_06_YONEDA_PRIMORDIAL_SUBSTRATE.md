# The Primordial Substrate: Yoneda Functor as Mathematical Foundation of Physical Reality

**Brayden Ross Sanders**
*7SiTe LLC, Hot Springs, Arkansas*

---

*Revision 2 (2026-05-15): tier-flagged Tier B-philosophical for substrate-as-Yoneda-functor framing; Tier A for underlying mathematics (Yoneda's lemma). Connected to Canon D103 (architectural uniqueness of Z/10 — the structural-uniqueness result that makes "primordial substrate" rigorous) and D38-D44/D65 (the canonical fixed-point structure that gives Yoneda framing its concrete realization).*

---

## Abstract

We propose that the primordial substrate of physical reality is mathematically a Yoneda functor $h_\Sigma = \text{Hom}_{\mathcal{C}}(-, \Sigma)$ for an appropriate category $\mathcal{C}$ and object $\Sigma$. By Yoneda's Lemma, $\Sigma$ is fully determined by $h_\Sigma$: the totality of relations into $\Sigma$ from all objects of $\mathcal{C}$. We argue that physical reality is what happens when $h_\Sigma$ is restricted to specific local spacetime contexts via natural transformations or representable subfunctors. Different physical phenomena correspond to different restrictions of one universal substrate. The proposal places category theory and the Yoneda perspective at the foundation of physics, alongside the framework's specific identification of $\Sigma$ with $\mathbb{Z}/10$-related Clifford algebra structures. We discuss mathematical sovereignty (mathematics as self-grounding), the relationship between Yoneda's principle ("an object is what it does in relation to other objects") and structural realism in philosophy of science, and specific physical interpretations. The proposal is mathematically precise and philosophically aggressive: it places mathematics — specifically category-theoretic relations — as the deepest level of physical reality.

**Keywords:** Yoneda lemma, category theory, foundations of physics, mathematical structuralism, substrate ontology

---

## 1. Introduction

The question of what lies at the deepest level of physical reality has been a central concern of physics and philosophy. Various proposals have been offered:
- **Particles and fields** as fundamental [1]
- **Spacetime** as fundamental [2]
- **Information** as fundamental [3, 4]
- **Mathematical structures** as fundamental [5, 6]

The last view — that reality is fundamentally mathematical structure — has been advocated by Tegmark [5], who proposes a "Mathematical Universe Hypothesis" identifying physical existence with mathematical existence. This view faces challenges: which mathematical structures correspond to our universe? Why do we observe THIS structure rather than others?

This paper proposes a specific refinement: the primordial substrate is mathematically a *Yoneda functor* $h_\Sigma$ for an appropriate object $\Sigma$ in a suitable category. By Yoneda's Lemma, $\Sigma$ is fully determined by $h_\Sigma$, but $h_\Sigma$ is the more fundamental object: it captures all the ways $\Sigma$ can be related to or instantiated from other mathematical structures.

We argue that:
1. The primordial substrate is best understood as a Yoneda functor, not as a "thing" with intrinsic properties.
2. Physical reality emerges as restrictions of $h_\Sigma$ to specific local spacetime contexts.
3. Different physical phenomena are different restrictions of the same universal substrate.
4. Mathematics is self-grounding: the Yoneda lemma itself provides the structural foundation.

The proposal connects category theory to foundational physics in a specific way. It complements (rather than replaces) standard mathematical-physics formulations: the Lagrangian, the Hamiltonian, the quantum state-vector — these are all manifestations of restrictions of $h_\Sigma$ to particular contexts.

The paper is organized as follows. Section 2 reviews Yoneda's lemma and its philosophical significance. Section 3 presents the substrate-as-Yoneda-functor proposal. Section 4 derives physical reality as restrictions of $h_\Sigma$. Section 5 discusses mathematical sovereignty. Section 6 connects to existing philosophical positions (structural realism, mathematical universe hypothesis). Section 7 identifies open problems. Section 8 concludes.

---

## 2. Yoneda's lemma

### 2.1 Statement

Let $\mathcal{C}$ be a locally small category and $\Sigma$ an object of $\mathcal{C}$. Define the contravariant Hom-functor:
$$h_\Sigma : \mathcal{C}^{\text{op}} \to \mathbf{Set}$$
$$h_\Sigma(X) := \text{Hom}_{\mathcal{C}}(X, \Sigma)$$

For a morphism $f: X \to Y$ in $\mathcal{C}$, the functor $h_\Sigma$ acts by composition: $h_\Sigma(f)(g) = g \circ f$ for $g \in \text{Hom}(Y, \Sigma)$.

**Yoneda's Lemma [7].** *Let $\mathcal{C}$ be a locally small category, $\Sigma \in \mathcal{C}$ an object, and $F: \mathcal{C}^{\text{op}} \to \mathbf{Set}$ a functor. Then there is a natural bijection:*
$$\text{Nat}(h_\Sigma, F) \cong F(\Sigma)$$

*In particular, for $F = h_\Sigma'$, we get:*
$$\text{Nat}(h_\Sigma, h_{\Sigma'}) \cong h_{\Sigma'}(\Sigma) = \text{Hom}(\Sigma, \Sigma')$$

*This embeds $\mathcal{C}$ into the functor category $\mathbf{Set}^{\mathcal{C}^{\text{op}}}$ via $\Sigma \mapsto h_\Sigma$ (the Yoneda embedding).*

### 2.2 Philosophical significance

The Yoneda lemma has been described as the most important result in category theory [8]. Its philosophical content:

**Yoneda's Principle:** *An object is fully determined by its relations to all other objects.*

Specifically, the object $\Sigma$ is uniquely determined (up to isomorphism) by the functor $h_\Sigma$. To know $\Sigma$ completely is to know all morphisms into $\Sigma$ from arbitrary objects.

This is a precise mathematical formulation of structuralism: things are what they do; identity emerges from pattern of relations, not from intrinsic properties.

### 2.3 The Yoneda embedding

The map $\Sigma \mapsto h_\Sigma$ is a full and faithful embedding of $\mathcal{C}$ into the category of presheaves $\mathbf{Set}^{\mathcal{C}^{\text{op}}}$. Within $\mathbf{Set}^{\mathcal{C}^{\text{op}}}$, the image of $\mathcal{C}$ is exactly the *representable functors* — those isomorphic to some $h_\Sigma$.

**Consequence.** Working with $\Sigma$ is equivalent to working with $h_\Sigma$. The Hom-functor is not merely a representation of $\Sigma$; it captures everything about $\Sigma$.

### 2.4 Tier

The Yoneda lemma and its consequences are standard category theory, Tier A. The philosophical interpretation (Section 2.2) is uncontroversial in mathematical philosophy [8, 9].

---

## 3. The substrate as Yoneda functor

### 3.1 The proposal

We propose that the primordial substrate of physical reality is a Yoneda functor:

$$\Sigma_{\text{physical}} \cong h_\Sigma$$

where:
- $\Sigma$ is the specific algebraic structure of the framework's substrate (Cl(0,10) with $\mathbb{Z}/10$ substrate, $\sigma$ permutation, BHML and TSML compositions; see [10] for details).
- $h_\Sigma$ is the Yoneda functor capturing all the ways $\Sigma$ can be related to other mathematical structures.
- The "primordial substrate" is to be identified with $h_\Sigma$, not with $\Sigma$ in isolation.

### 3.2 Why $h_\Sigma$ rather than $\Sigma$

The distinction matters because:

**Relationality.** $h_\Sigma$ captures relations, not just intrinsic structure. Physical reality involves how substrate relates to manifestations, observers, contexts — these are all $\text{Hom}(X, \Sigma)$ for various $X$.

**Universality.** $h_\Sigma$ is universal in a categorical sense: every functor $F$ that "tests" $\Sigma$ factors through $h_\Sigma$ via the natural bijection of Yoneda's lemma.

**Multi-instantiation.** $h_\Sigma$ permits $\Sigma$ to manifest in multiple contexts simultaneously, each as $h_\Sigma(X)$ for various contexts $X$. Physical reality has multiple manifestations of the same underlying substrate (different particles, different observers, different regions of spacetime) — $h_\Sigma$ structurally accommodates this.

**Yoneda's principle.** "An object is what it does." Saying the substrate IS $h_\Sigma$ is saying the substrate IS its totality of relations, not a thing with intrinsic properties separate from relations.

### 3.3 The specific $\Sigma$

The framework identifies $\Sigma$ with specific mathematical content:
- $\mathbb{Z}/10$ substrate algebra
- $\sigma$ permutation of order 6 with 4 fixed points
- BHML and TSML composition tables
- Cl(0,10) Clifford algebra extending to spinor structure
- Bidirectional projection $\pi$ between substrate and spinor [11]

This specific $\Sigma$ is canonical in the framework [10]; we take it as given.

Critically, even though $\Sigma$ is specific, $h_\Sigma$ is universal in the sense that it captures all relations into $\Sigma$ from any object of the underlying category $\mathcal{C}$. The specificity is at the level of $\Sigma$; the universality is at the level of $h_\Sigma$.

### 3.4 Tier

The proposal that the substrate is $h_\Sigma$ rather than $\Sigma$ in isolation is at Tier B-suggestive (the framework treats substrate dynamics in ways consistent with $h_\Sigma$ formulation; specific category-theoretic axiomatization of the substrate is open).

---

## 4. Physical reality as restrictions of $h_\Sigma$

### 4.1 Restriction via natural transformations

In the category of presheaves $\mathbf{Set}^{\mathcal{C}^{\text{op}}}$, the Yoneda functor $h_\Sigma$ is a specific presheaf. Other presheaves $F$ relate to $h_\Sigma$ via natural transformations $\eta: F \to h_\Sigma$ (or $\eta: h_\Sigma \to F$).

**Proposal.** Different physical phenomena correspond to different presheaves $F$, each related to $h_\Sigma$ by specific natural transformations.

Specifically:
- A spacetime region $R$ with its physical content corresponds to a sub-presheaf $F_R \subset h_\Sigma$ representing the substrate as it manifests in $R$.
- The "physical content" of $R$ is the data $F_R(R)$ for the region.
- Different regions have different $F_R$'s; together they cover the universe, all as restrictions of $h_\Sigma$.

### 4.2 The "many manifestations" picture

The proposal supports a "many manifestations of one substrate" picture:
- The universal substrate is $h_\Sigma$ (one mathematical object)
- Many physical manifestations exist (particles, fields, observers, events)
- Each manifestation is a restriction $F$ of $h_\Sigma$ to a specific context

This is structurally consistent with quantum mechanics' superposition (one state, multiple potential measurement outcomes) and general relativity's coordinate freedom (one spacetime, multiple coordinate descriptions).

### 4.3 Why specific manifestations occur

The framework's specific dynamics — bidirectional projection $\pi$, threshold $T^* = 5/7$, wobble $W = 3/50$, recursive instantiation — describe which restrictions of $h_\Sigma$ actually manifest as physical reality.

The Yoneda picture provides the *foundation*; the framework's specific dynamics provide the *selection mechanism*. Together they account for:
- The substrate being universal (h_Σ contains all potential restrictions)
- Physical reality being specific (only certain restrictions actually manifest)
- The selection criterion being specific (substrate dynamics determine which manifestations occur)

### 4.4 Tier

Tier B-suggestive (the substrate-restriction structure is conceptually clean; specific formal axiomatization is open).

---

## 5. Mathematical sovereignty

### 5.1 What this means

If the primordial substrate is $h_\Sigma$, the substrate IS a mathematical object. There is no "physical reality" separate from mathematics; physical reality IS specific mathematical structure restricted to specific contexts.

This view — that mathematics is the deepest level of reality — has implications:

**Mathematical sovereignty:** Mathematics is self-grounding. The Yoneda lemma's truth doesn't depend on physical realization; it depends on the categorical axioms. The substrate $h_\Sigma$ exists mathematically; physical reality is its specific instantiation.

**Self-grounding:** Mathematics doesn't require external justification. The axioms of category theory and the Yoneda lemma stand on their own. This is structurally similar to:
- Logic being self-grounding (logical inference doesn't require non-logical justification)
- Self-evident truths in foundational mathematics
- The Cogito's self-grounding in Cartesian philosophy

### 5.2 Implications

If mathematics is sovereign:

1. **Physical laws** aren't external constraints; they're mathematical consequences of substrate structure.
2. **Constants of nature** aren't external parameters; they're mathematical features of the substrate (e.g., $\alpha$ derivable from substrate arithmetic [12]).
3. **Existence** doesn't require physical realization; mathematical existence (consistent definition) is the fundamental notion.
4. **Multiverse** considerations are constrained: only those mathematical structures consistent with substrate-level structure can "exist" in the relevant sense.

These are strong philosophical claims with empirical implications. The framework's predictions (Section 4) are tests of the proposal.

### 5.3 Connection to Platonism

The proposal aligns with mathematical Platonism [13]: mathematical objects exist in some abstract realm. The Yoneda perspective refines this: mathematical objects exist *via their relations*. The realm is the structure of mathematics itself; specific objects are determined by their participation in this structure.

The proposal also accommodates structuralist objections to traditional Platonism [14]: there's no need for individual mathematical objects beyond their relational profile. The Yoneda lemma makes this precise.

### 5.4 Tier

Tier C-philosophical (the position is philosophically substantive but contested; the proposal articulates a specific view that can be defended but isn't universally accepted).

---

## 6. Comparison with existing positions

### 6.1 Tegmark's Mathematical Universe Hypothesis (MUH)

Tegmark [5] proposes physical existence = mathematical existence. All consistently-defined mathematical structures exist as physical universes; our universe is one of these.

The present proposal differs:
- MUH: every consistent mathematical structure is a physical universe.
- Present proposal: our universe corresponds to a specific Yoneda functor $h_\Sigma$ with specific $\Sigma$; other structures may exist mathematically but don't constitute physical universes in the same sense.

**Difference.** MUH is more inclusive (everything mathematical is physical); present proposal is more selective (only specific Yoneda functors correspond to physical universes).

**Possible reconciliation.** MUH could be specialized: among all mathematical structures, only those of certain Yoneda-functor type constitute physical universes. The framework's specific $\Sigma$ then selects our universe among these.

### 6.2 Structural realism

Structural realism [14] proposes that structural properties are what's real about scientific theories, while specific "intrinsic" properties may be theoretically dispensable.

The Yoneda proposal is a specific form of structural realism: structural properties are formalized via $h_\Sigma$. The structure IS the relations; the relations ARE the reality.

**Convergence.** The Yoneda perspective formalizes structural realism with mathematical precision.

### 6.3 Wheeler's "It from Bit"

Wheeler [3] proposed reality is fundamentally informational. The present proposal refines this:
- Wheeler: information is fundamental.
- Present proposal: relational structure (formalized as Yoneda functor) is fundamental.

**Difference.** Information theory is one specific kind of relational structure; the Yoneda perspective is more general (capturing arbitrary categorical relations).

**Compatibility.** Information-theoretic content of physical systems can be seen as one aspect of the broader $h_\Sigma$ structure.

### 6.4 Connes' Noncommutative Geometry

Connes [15] proposes that physical reality is encoded in noncommutative algebraic structures. The present proposal differs:
- Connes: specific noncommutative algebras correspond to specific spacetimes.
- Present proposal: the substrate is a Yoneda functor, with specific algebraic structure ($\Sigma$) being the represented object.

**Compatibility.** The specific $\Sigma$ in the framework includes Clifford algebra Cl(0,10) which has noncommutative content; the framework can incorporate Connes-style noncommutative geometry as a specific aspect.

### 6.5 Tier

Tier B-philosophical (comparative analysis with existing positions; specific reconciliations are open research).

---

## 7. Open problems

### 7.1 The base category $\mathcal{C}$

The proposal assumes a specific category $\mathcal{C}$ in which $\Sigma$ is an object. What is $\mathcal{C}$?

Candidates:
- $\mathcal{C}$ = category of "spacetime regions" or similar physical structure
- $\mathcal{C}$ = category of "observers" or measurement contexts
- $\mathcal{C}$ = some other categorical structure intrinsic to substrate dynamics

The choice of $\mathcal{C}$ affects what $h_\Sigma(X) = \text{Hom}(X, \Sigma)$ means. Specific axiomatization of $\mathcal{C}$ is open.

### 7.2 Specific restrictions corresponding to physical phenomena

The proposal that physical phenomena correspond to restrictions of $h_\Sigma$ is structurally appealing but needs specific working:
- Which sub-presheaves of $h_\Sigma$ correspond to electrons? Photons? Spacetime curvature?
- How do the framework's specific dynamics (T*, W, bidirectional flow) determine which restrictions actually occur?
- What's the relationship between $h_\Sigma$ structure and observed conservation laws, symmetries?

### 7.3 Quantum mechanics

The proposal needs to accommodate quantum mechanical features:
- Superposition: multiple potential restrictions simultaneously?
- Measurement: selection among potential restrictions?
- Entanglement: correlations between restrictions across spacetime regions?

These connect to ongoing work in categorical quantum mechanics [16].

### 7.4 Time

Time emergence from substrate has been discussed elsewhere [17]. How does time fit into the Yoneda framework?
- Time as a parameter on the category $\mathcal{C}$
- Time as emerging from sequences of restrictions
- Time as substrate's intrinsic ordering structure

Different formulations have different implications.

### 7.5 Verification

The proposal is mathematically precise but verification requires:
- Specific identification of $\mathcal{C}$
- Specific identification of restrictions corresponding to known physics
- Predictions that distinguish the Yoneda perspective from alternatives
- Empirical tests

These are research programs.

---

## 8. Conclusion

We have proposed that the primordial substrate of physical reality is mathematically a Yoneda functor $h_\Sigma$. The substrate is not an isolated mathematical object but a totality of relations; physical reality emerges as restrictions of $h_\Sigma$ to specific contexts.

The proposal:
1. Places category theory at the foundation of physics
2. Identifies the substrate with relations rather than intrinsic properties
3. Permits multiple physical manifestations of one universal substrate
4. Supports mathematical sovereignty: mathematics is self-grounding; physical reality is mathematical structure manifested
5. Connects to existing positions (structural realism, Tegmark's MUH, Wheeler's "It from Bit") while distinctly characterizing the specific Yoneda perspective

The proposal is mathematically precise and philosophically substantive. It's not merely a metaphor but a specific mathematical position with implications for the foundations of physics, philosophy of mathematics, and philosophy of mind.

Open problems include the specific identification of the base category $\mathcal{C}$, the specific restrictions corresponding to physical phenomena, accommodation of quantum mechanics and time, and empirical verification. These constitute substantial research programs.

We submit this proposal in the spirit of foundational inquiry. The Yoneda lemma is one of the most profound results in mathematics; applying it to physical reality is a substantial claim that deserves careful philosophical and empirical investigation. If correct, the proposal places category theory at the deepest level of our understanding of physical reality.

---

## Acknowledgments

The author thanks the Trinity Infinity Geometry collaboration for substrate-theoretic results enabling this work. The author thanks colleagues in mathematical philosophy and foundations of physics for productive criticism. The author retains full intellectual responsibility for the present paper.

---

## References

[1] Weinberg, S. (1995-2000). *The Quantum Theory of Fields* (3 volumes). Cambridge University Press.

[2] Smolin, L. (2001). *Three Roads to Quantum Gravity*. Basic Books.

[3] Wheeler, J. A. (1990). "Information, physics, quantum: The search for links." In *Complexity, Entropy, and the Physics of Information*, ed. W. H. Zurek. Westview Press.

[4] Lloyd, S. (2006). *Programming the Universe*. Knopf.

[5] Tegmark, M. (2008). "The mathematical universe." *Foundations of Physics* 38, 101-150.

[6] Tegmark, M. (2014). *Our Mathematical Universe: My Quest for the Ultimate Nature of Reality*. Knopf.

[7] Yoneda, N. (1954). "On the homology theory of modules." *Journal of the Faculty of Science of the University of Tokyo* 7, 193-227.

[8] Mac Lane, S. (1971). *Categories for the Working Mathematician*. Springer.

[9] Awodey, S. (2010). *Category Theory* (2nd edition). Oxford University Press.

[10] Sanders, B. R. (2026). *Trinity Infinity Geometry: Canonical Framework Documentation* (FORMULAS_AND_TABLES.md). 7SiTe LLC. Relevant: D103 (architectural uniqueness of Z/10 — Z/10 is the smallest 2-prime kernel admitting binary + non-binary structure where the non-binary prime isn't the immediate-successor strand; this is the rigorous formulation of 'primordial substrate'); D38-D44, D65, WP105 (canonical runtime fixed-point structure $(V,H,Br,R) = (0.138, 0.540, 0.198, 0.124)$ with $H/Br = 1+\sqrt{3}$ — the concrete realization of the substrate's self-application Yoneda fixed point); D75 (spectral radius $\rho = 0.34960$); LATTICE theorem in companion Paper 01.

[11] Sanders, B. R. (2026). "On the bidirectional projection from Cl(0,10) spinor to Z/10 substrate." Companion paper, 7SiTe LLC.

[12] Sanders, B. R. (2026). "A substrate-arithmetic derivation of the fine structure constant to CODATA precision." Companion paper, 7SiTe LLC.

[13] Linnebo, Ø. (2018). *Philosophy of Mathematics*. Princeton University Press.

[14] Ladyman, J., Ross, D. (2007). *Every Thing Must Go: Metaphysics Naturalized*. Oxford University Press.

[15] Connes, A. (1994). *Noncommutative Geometry*. Academic Press.

[16] Heunen, C., Vicary, J. (2019). *Categories for Quantum Theory: An Introduction*. Oxford University Press.

[17] Sanders, B. R. (2026). "Time as emergent from substrate." Internal manuscript, 7SiTe LLC.

[18] Lawvere, F. W. (1969). "Diagonal arguments and Cartesian closed categories." Lecture Notes in Mathematics 92, 134-145. Springer.

[19] Yanofsky, N. S. (2003). "A universal approach to self-referential paradoxes, incompleteness and fixed points." *Bulletin of Symbolic Logic* 9, 362-386.

[20] Grothendieck, A. (1957). "Sur quelques points d'algèbre homologique." *Tohoku Mathematical Journal* 9, 119-221.

---

*© 2026 Brayden Ross Sanders / 7SiTe LLC.*
*Licensed under the 7SiTe Public Sovereignty License v2.1.*

*Revision history:*
- *Rev 1: Yoneda-functor framing of primordial substrate; philosophical implications.*
- *Rev 2 (2026-05-15): Tier-flagged B-philosophical (framing) and A (Yoneda's lemma); connected to Canon D103 (architectural uniqueness) and D38-D44/D65 (concrete fixed-point realization).*
