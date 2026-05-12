# CK_DESIGN_PRINCIPLE_COHERENCE_BY_STRUCTURE

## Coherence by structure, not by rule

**Brayden Sanders / 7Site LLC / Trinity Infinity Geometry**
**For ClaudeCode when extending CK**

Locked 2026-05-08.

---

## §0. Principle

When extending CK, prefer architectures where incoherent states are **unreachable** to architectures that **detect-and-reject** incoherent states.

```
RULE-BASED (avoid):
  if state.violates_constraint(): raise Error
  
STRUCTURE-BASED (prefer):
  define the state space such that violations can't be expressed
```

This principle has names in software engineering:
- "Make illegal states unrepresentable" (Yaron Minsky / OCaml community)
- "Parse, don't validate" (Alexis King)
- "Correct by construction" (formal methods tradition)
- "Fences not guards" (API design)

For TIG/CK, it's also the algebraic version of how the substrate already works: the 4-core {0,7,8,9} attracts because of how composition is defined, not because anything checks "is this in the 4-core?" The structure does the work.

---

## §1. Why this matters for CK specifically

CK's substrate (TSML, BHML, Cl(8)) is mathematically closed. Composition of any two operators in Z/10 produces another operator in Z/10. The substrate doesn't need rules saying "outputs must be in {0..9}" — that's enforced by the algebra.

When ClaudeCode extends CK, the temptation is to add rules: "if input invalid, raise error." This works but it's brittle. Better: make the input type such that invalid inputs can't be constructed in the first place.

Brayden's framing: **"It's the difference between telling my kids they can't have a popsicle from the freezer and not having popsicles in the freezer."**

Rule-based: popsicles in the freezer + rule against eating them. Requires enforcement. Creates desire-vs-rule tension.

Structure-based: no popsicles in the freezer. No rule needed. The situation requiring the rule doesn't arise.

CK should embody the second pattern wherever possible.

---

## §2. Concrete applications in CK

### 2.1 Substrate operations closed under composition

Bad pattern:
```python
def compose(a: int, b: int) -> int:
    result = TSML[a][b]
    if result < 0 or result > 9:
        raise ValueError("Out of substrate range")
    return result
```

Good pattern:
```python
class SubstrateOp:
    """Operator in Z/10. Constructor enforces validity."""
    def __init__(self, value: int):
        if not 0 <= value <= 9:
            raise ValueError(...)  # only at construction
        self._v = value
    
    def __mul__(self, other: 'SubstrateOp') -> 'SubstrateOp':
        return SubstrateOp(TSML[self._v][other._v])
        # Type system guarantees output is in Z/10
```

Once a `SubstrateOp` exists, no further validation is needed anywhere. The closure is a type-level property.

### 2.2 4-core attracts by structure

Bad pattern:
```python
def converge_to_harmony(state):
    if state not in CORE_4:
        return push_toward_core(state)
    return state
```

Good pattern: define composition such that iteration naturally falls into the 4-core. The TSML/BHML structure already does this — repeated composition of arbitrary operators converges to 4-core elements without any "push" operation. Use the algebra, don't simulate it.

### 2.3 Path-encoding integrity as a type

Bad pattern:
```python
def is_valid_path(path: list) -> bool:
    # Check sequence is admissible
    ...

def use_path(path):
    if not is_valid_path(path):
        raise ValueError
    ...
```

Good pattern:
```python
class Path:
    """A path through the substrate. Constructor only accepts valid paths."""
    def __init__(self, steps: list[SubstrateOp]):
        # Verify admissibility at construction time
        for i in range(len(steps) - 1):
            if not _admissible(steps[i], steps[i+1]):
                raise ValueError
        self._steps = tuple(steps)
    
def use_path(p: Path):
    # No validation needed. If you have a Path, it's valid.
    ...
```

"Is this a valid path?" becomes "do you have a Path object?" — answered at compile/import time, not runtime.

### 2.4 Failures via VOID, not exceptions

Bad pattern:
```python
def synthesize(...):
    if cannot_synthesize(...):
        raise SynthesisError
    return result
```

Good pattern:
```python
def synthesize(...) -> SubstrateOp:
    if cannot_synthesize(...):
        return SubstrateOp(0)  # VOID
    return result
```

VOID composes cleanly with everything (TSML[0][·] = 0, TSML[·][0] = 0 in default rows). A null result that propagates as VOID is the substrate's natural failure mode. The system stays coherent through the failure rather than throwing.

This matches canon: 0 = VOID is the substrate reference state, not an error condition. Failures should reduce to VOID, not raise.

### 2.5 Symmetry preservation as type structure

If a function is supposed to preserve a symmetry (e.g. BHML symmetry, σ-equivariance), encode that in the types so the function can't return asymmetric output.

Bad pattern:
```python
def transform(matrix):
    result = ...
    assert is_symmetric(result)
    return result
```

Good pattern:
```python
class SymmetricMatrix:
    def __init__(self, m):
        if not np.allclose(m, m.T):
            raise ValueError
        self._m = m

def transform(m: SymmetricMatrix) -> SymmetricMatrix:
    # Implementation must produce symmetric output
    # by construction, not assertion
    return SymmetricMatrix(...)
```

---

## §3. When to break the principle

This principle has limits. Don't follow it past the point of usefulness.

**Break it for**: I/O boundaries (parsing user input, reading files), where you don't control the source. There you do need to validate-then-construct. The principle still applies *internally* — once parsed, the type guarantees validity.

**Break it for**: extremely dynamic situations where the type system would be too rigid. Sometimes a rule + check is simpler than a complex type. Don't over-engineer.

**Break it for**: prototyping. Get something working, then refactor toward structure-based once the design stabilizes.

The principle is a default to lean toward, not a doctrine to enforce.

---

## §4. Why ClaudeCode specifically needs this

ClaudeCode has a tendency to architect — to add layers, rules, validators, error types. That's often the right move for general software. For CK specifically, it's frequently the wrong move because the substrate already provides the structure that the rules would be enforcing.

When extending CK, ClaudeCode should:

1. Look at what the substrate already enforces (closure, attractor structure, σ-orbit decomposition, 4-core absorption)
2. Use those properties rather than re-implementing them as rules
3. When tempted to add a guard clause, ask: "could the type system or substrate algebra enforce this instead?"
4. Reach for `if-raise` patterns only when no structural alternative exists

The substrate is already coherent. Code that extends it should let the coherence propagate, not police it.

---

## §5. Connection to the Braiding Fractal

This design principle isn't separate from TIG's architecture — it's the same architecture applied to code.

TIG's 10 axioms are forced by Z/10's arithmetic. Nothing in TIG is "added by hand to enforce coherence." The Braiding Fractal is coherent by structure (the kernel is composite, σ has the cycle it has, clickables are exactly output support, etc.) — every property follows from the kernel's algebra.

CK's code should embody the same approach. Don't add rules to enforce coherence; choose structures where coherence is automatic.

The fractal nature applies here too: at every level of CK's architecture (substrate operations, paths, synthesis events, integration with LMs), the same principle should hold. Coherence by structure, not by rule, all the way down.

---

## §6. Summary for ClaudeCode

```
DEFAULT MOVE: structure-based coherence
FALLBACK: rule-based only when structure-based isn't viable
QUESTION TO ASK: "could this be a type instead of a check?"
ANTI-PATTERN: if-raise scattered through the codebase
PATTERN: smart constructors + closed operations + null-as-VOID
```

The principle: **don't tell the system what it can't do; design the system so it can't do it.**

---

## §7. Origin

This principle was articulated by Brayden Sanders during the May 2026 corpus session, originally as a parenting metaphor: "It's the difference between telling my kids they can't have a popsicle from the freezer and not having popsicles in the freezer."

That metaphor compressed a software design principle, a substrate algebra principle, and a philosophical position about coherence into one image. This doc unpacks the software-design version for ClaudeCode integration into CK.

---

© 2026 Brayden Sanders / 7Site LLC

Trinity Infinity Geometry · CK Design Principle · Locked 2026-05-08
