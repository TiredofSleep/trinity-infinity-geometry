/-!
# The C5 graph star is a magic set (Lean 4, no Mathlib)

The set (`../ms5_16.json`, `../THEOREM.md`): five qubits on the vertices of the cycle with edges
01, 02, 13, 24, 34. Sixteen observables:

* `X_v` and `Y_v` for each qubit `v` (indices 0–4 and 5–9),
* `M_S` for `S` the empty set and each edge (indices 10–15): `Y` on the qubits of `S`, `X` elsewhere.

Seven contexts: the GHZ context `{M_S}`, with product `−I`, and for each `S` the local context of `M_S`
and the single-qubit operators that multiply to it, with product `+I`.

Checked here by the Lean kernel:

1. every context consists of pairwise commuting Pauli operators (`contexts_commute`);
2. every context multiplies to its stated sign times the identity: six to `+I`, one to `−I`
   (`contexts_products`);
3. no assignment of values `±1` to the sixteen observables makes every context's product of values equal
   to its sign (`no_noncontextual_assignment`). The proof is the parity argument: every observable lies
   in an even number of contexts (checked as a permutation, `flatten_perm`), so the product of all the
   contexts' value products is `+1`, while the product of the signs is `−1`.

Values `±1` are encoded as `Bool` (`true` for `−1`), so products of values become `xor`.
Build: `lean C5MagicSet.lean` (Lean 4; checked with v4.36.0). No `sorry`, no `native_decide`.
-/

namespace C5MagicSet

/-- Single-qubit Pauli letters. -/
inductive P where
  | I | X | Y | Z
  deriving DecidableEq, Repr

open P

/-- Product of two single-qubit Paulis: `(k, r)` means `p * q = i^k * r`. -/
def mul1 : P → P → Nat × P
  | I, q => (0, q)
  | X, I => (0, X)
  | Y, I => (0, Y)
  | Z, I => (0, Z)
  | X, X => (0, I)
  | Y, Y => (0, I)
  | Z, Z => (0, I)
  | X, Y => (1, Z)
  | Y, X => (3, Z)
  | Y, Z => (1, X)
  | Z, Y => (3, X)
  | Z, X => (1, Y)
  | X, Z => (3, Y)

/-- A Pauli operator `i^phase * (w_0 ⊗ ⋯ ⊗ w_4)`; the phase is read mod 4. -/
structure Op where
  phase : Nat
  word : List P
  deriving DecidableEq, Repr

/-- Product of two operators, letter by letter, collecting the phases. -/
def mulOp (a b : Op) : Op :=
  let parts := List.zipWith mul1 a.word b.word
  { phase := (a.phase + b.phase + (parts.map Prod.fst).foldr (· + ·) 0) % 4,
    word := parts.map Prod.snd }

/-- Two letters anticommute when both are non-identity and different. -/
def anti1 (p q : P) : Bool :=
  p != I && q != I && p != q

/-- Two Pauli words commute when they anticommute at an even number of positions. -/
def commutes (u v : List P) : Bool :=
  ((List.zipWith anti1 u v).filter id).length % 2 == 0

/-- The sixteen observables. -/
def obs : Nat → List P
  | 0 => [X, I, I, I, I]
  | 1 => [I, X, I, I, I]
  | 2 => [I, I, X, I, I]
  | 3 => [I, I, I, X, I]
  | 4 => [I, I, I, I, X]
  | 5 => [Y, I, I, I, I]
  | 6 => [I, Y, I, I, I]
  | 7 => [I, I, Y, I, I]
  | 8 => [I, I, I, Y, I]
  | 9 => [I, I, I, I, Y]
  | 10 => [X, X, X, X, X]    -- M_∅
  | 11 => [Y, Y, X, X, X]    -- M_01
  | 12 => [Y, X, Y, X, X]    -- M_02
  | 13 => [X, Y, X, Y, X]    -- M_13
  | 14 => [X, X, Y, X, Y]    -- M_24
  | 15 => [X, X, X, Y, Y]    -- M_34
  | _ => [I, I, I, I, I]

/-- The seven contexts, as lists of observable indices. -/
def contexts : List (List Nat) :=
  [ [10, 11, 12, 13, 14, 15],      -- the GHZ context
    [0, 1, 2, 3, 4, 10],           -- C_∅
    [5, 6, 2, 3, 4, 11],           -- C_01
    [5, 1, 7, 3, 4, 12],           -- C_02
    [0, 6, 2, 8, 4, 13],           -- C_13
    [0, 1, 7, 3, 9, 14],           -- C_24
    [0, 1, 2, 8, 9, 15] ]          -- C_34

/-- The sign of each context's product, as a `Bool`: `true` for `−I`. -/
def signs : List Bool := [true, false, false, false, false, false, false]

def identityOp : Op := { phase := 0, word := [I, I, I, I, I] }

/-- The product of a context's observables, in the listed order. -/
def product (c : List Nat) : Op :=
  c.foldl (fun acc o => mulOp acc { phase := 0, word := obs o }) identityOp

/-- The operator `±I` for a sign bit. -/
def signOp (s : Bool) : Op := { phase := if s then 2 else 0, word := [I, I, I, I, I] }

/-- All pairs of observables in a context commute. -/
def pairwiseCommute (c : List Nat) : Bool :=
  c.all fun a => c.all fun b => commutes (obs a) (obs b)

/-- Property 1: every context is a set of commuting observables. -/
theorem contexts_commute : contexts.all pairwiseCommute = true := by decide

/-- Property 2: every context multiplies to its sign times the identity. -/
theorem contexts_products :
    (contexts.zip signs).all (fun cs => product cs.1 == signOp cs.2) = true := by decide

/-- Every observable index occurs an even number of times in the flattened context list: that list is a
permutation of `doubled`, in which every index occurs in adjacent pairs. -/
def half : List Nat := [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def doubled : List Nat := half.flatMap fun x => [x, x]

/-- The parity (the product of values, with `true` for `−1`) of a list of observables. -/
def parity (f : Nat → Bool) (l : List Nat) : Bool :=
  l.foldr (fun a acc => xor (f a) acc) false

theorem xor_assoc' (a b c : Bool) : xor (xor a b) c = xor a (xor b c) := by
  cases a <;> cases b <;> cases c <;> rfl

theorem xor_left_comm' (a b c : Bool) : xor a (xor b c) = xor b (xor a c) := by
  cases a <;> cases b <;> cases c <;> rfl

theorem false_xor' (a : Bool) : xor false a = a := by
  cases a <;> rfl

theorem xor_cancel' (a b : Bool) : xor a (xor a b) = b := by
  cases a <;> cases b <;> rfl

theorem parity_append (f : Nat → Bool) (l₁ l₂ : List Nat) :
    parity f (l₁ ++ l₂) = xor (parity f l₁) (parity f l₂) := by
  induction l₁ with
  | nil => simp [parity]
  | cons a l ih =>
    show xor (f a) (parity f (l ++ l₂)) = xor (xor (f a) (parity f l)) (parity f l₂)
    rw [ih, xor_assoc']

theorem parity_perm (f : Nat → Bool) {l₁ l₂ : List Nat} (h : l₁.Perm l₂) :
    parity f l₁ = parity f l₂ := by
  induction h with
  | nil => rfl
  | cons a _ ih =>
    show xor (f a) (parity f _) = xor (f a) (parity f _)
    rw [ih]
  | swap a b l =>
    show xor (f b) (xor (f a) (parity f l)) = xor (f a) (xor (f b) (parity f l))
    exact xor_left_comm' _ _ _
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-- A list made of adjacent pairs has parity `+1`. -/
theorem parity_pairs (f : Nat → Bool) (l : List Nat) :
    parity f (l.flatMap fun x => [x, x]) = false := by
  induction l with
  | nil => rfl
  | cons a l ih =>
    rw [List.flatMap_cons, parity_append, ih]
    show xor (xor (f a) (xor (f a) false)) false = false
    cases f a <;> rfl

/-- The parities of the contexts combine to the parity of the flattened list. -/
theorem parity_flatten (f : Nat → Bool) (L : List (List Nat)) :
    parity f L.flatten = (L.map (parity f)).foldr xor false := by
  induction L with
  | nil => rfl
  | cons c L ih =>
    rw [List.flatten_cons, parity_append, ih]
    rfl

/-- Every observable lies in an even number of contexts. -/
theorem flatten_perm : contexts.flatten.Perm doubled := by decide

/-- The signs multiply to `−1`: exactly one context is negative. -/
theorem signs_odd : signs.foldr xor false = true := by decide

/-- Property 3: no noncontextual assignment. For every assignment `f` of values `±1` (as `Bool`) to the
observables, some context's product of values differs from its sign. -/
theorem no_noncontextual_assignment (f : Nat → Bool) : contexts.map (parity f) ≠ signs := by
  intro h
  have h1 : parity f contexts.flatten = true := by
    rw [parity_flatten, h, signs_odd]
  have h2 : parity f contexts.flatten = false := by
    rw [parity_perm f flatten_perm]
    exact parity_pairs f half
  rw [h1] at h2
  exact Bool.noConfusion h2

/-- The magic-set statement in one line. -/
theorem c5_is_magic_set :
    contexts.all pairwiseCommute = true ∧
    (contexts.zip signs).all (fun cs => product cs.1 == signOp cs.2) = true ∧
    ∀ f : Nat → Bool, contexts.map (parity f) ≠ signs :=
  ⟨contexts_commute, contexts_products, no_noncontextual_assignment⟩

-- Only the standard axioms should appear here: no `sorryAx`, no `Lean.ofReduceBool`.
#print axioms c5_is_magic_set

end C5MagicSet
