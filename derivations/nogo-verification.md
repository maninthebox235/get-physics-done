# Cross-Verification of No-Go Arguments A, B, C

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, regularization_scheme=zeta, casimir_force_sign=F<0_attractive, casimir_energy_sign=E<0_bounded, work_sign=W_net>0_extraction

This document verifies the consistency, independence, and completeness of the three no-go arguments derived in `nogo-thermodynamic.md` (A), `nogo-lorentz.md` (B), and `nogo-passivity.md` (C).

## 1. Dimensional Consistency

### Argument A (Thermodynamic)

| Equation | LHS Dimension | RHS Dimension | Status |
|---|---|---|---|
| (A.1) $E_{\text{Cas}}/\mathcal{A} = -\pi^2/(720\,a^3)$ | $[\text{energy}/\text{length}^2] = [\text{length}^{-3}]$ | $[\text{length}^{-3}]$ | PASS |
| (A.2) $F_{\text{Cas}}/\mathcal{A} = -\pi^2/(240\,a^4)$ | $[\text{force}/\text{area}] = [\text{length}^{-4}]$ | $[\text{length}^{-4}]$ | PASS |
| (A.5) $W_{\text{net}} = \oint F\,da$ | $[\text{energy}/\text{area}] = [\text{length}^{-3}]$ | $[\text{length}^{-4}][\text{length}] = [\text{length}^{-3}]$ | PASS |
| (A.6) $W_{\text{net}} = 0$ | $[\text{energy}/\text{area}]$ | $0$ (dimensionless) | PASS (zero is compatible with any dimension) |
| (A.9) $W_{\text{net}} \leq 0$ | $[\text{energy}/\text{area}]$ | inequality with $0$ | PASS |

### Argument B (Lorentz Invariance)

| Equation | LHS Dimension | RHS Dimension | Status |
|---|---|---|---|
| (B.6) $\langle 0|T^{\mu\nu}|0\rangle = \rho_{\text{vac}} g^{\mu\nu}$ | $[\text{length}^{-4}]$ | $[\text{length}^{-4}] \cdot [\text{dimensionless}]$ | PASS |
| (B.10) $p_{\text{vac}} = -\rho_{\text{vac}}$ | $[\text{energy}/\text{volume}]$ | $[\text{energy}/\text{volume}]$ | PASS |
| (B.15) $dU + \delta W = 0$ | $[\text{energy}]$ | $0$ | PASS |
| (B.16) $W_{\text{net}} = 0$ | $[\text{energy}]$ | $0$ | PASS |
| (B.17) $\langle T^{00}\rangle = -\pi^2/(720\,a^4)$ | $[\text{length}^{-4}]$ | $[\text{length}^{-4}]$ | PASS |

### Argument C (Passivity)

| Equation | LHS Dimension | RHS Dimension | Status |
|---|---|---|---|
| (C.2) $\Delta E = \text{Tr}(U\rho U^\dagger H) - \text{Tr}(\rho H)$ | $[\text{energy}]$ | $[\text{energy}] - [\text{energy}]$ | PASS |
| (C.8) $\langle 0|U^\dagger H U|0\rangle = \sum_n |c_n|^2 E_n$ | $[\text{energy}]$ | $[\text{dimensionless}] \cdot [\text{energy}]$ | PASS |
| (C.11) $W_{\text{net}} = -\Delta E \leq 0$ | $[\text{energy}]$ | $-[\text{energy}]$ | PASS |
| (C.22) $W_{\max} = 0$ | $[\text{energy}]$ | $0$ | PASS |

**Result: ALL equations in all three derivations are dimensionally consistent.** No dimensional errors found.

## 2. Internal Logic Verification

### Argument A: Logical Chain

1. **Premise:** Casimir force $F_{\text{Cas}}(a)$ is a well-defined function of separation $a$ alone (A2, A3).
2. **Inference:** Therefore $F_{\text{Cas}}$ is a conservative force in the 1D configuration space.
3. **Conclusion (quasi-static):** $W_{\text{net}} = \oint F\,da = 0$ for any closed path.
4. **Generalization (any cycle):** Kelvin-Planck (A4) gives $W_{\text{net}} \leq 0$ even for non-quasi-static.

**Logical gaps:** None. The conservative force argument (steps 1-3) is mathematically rigorous. The second law generalization (step 4) invokes A4 as an axiom — this is standard thermodynamics, not a derivation gap.

**Potential weakness:** The jump from "conservative force $\Rightarrow W_{\text{net}} = 0$" to "second law $\Rightarrow W_{\text{net}} \leq 0$" is a strengthening of the conclusion. The second law argument is more general but also more axiom-dependent (it requires the second law to hold at $T = 0$). The two parts are logically independent — the conservative force result stands even without the second law.

### Argument B: Logical Chain

1. **Premise:** $|0\rangle$ is Poincaré-invariant (B1); $T^{\mu\nu}$ transforms as a rank-2 tensor (B4).
2. **Inference (translation):** $\langle 0|T^{\mu\nu}(x)|0\rangle$ is independent of $x$.
3. **Inference (Lorentz):** The constant tensor $C^{\mu\nu}$ must be Lorentz-invariant $\Rightarrow$ $C^{\mu\nu} \propto g^{\mu\nu}$.
4. **Inference (EOS):** Comparing with perfect fluid form $\Rightarrow$ $p = -\rho$.
5. **Conclusion:** $dU + \delta W = 0$ for $p = -\rho$ medium $\Rightarrow$ $W_{\text{net}} = 0$.

**Logical gaps:** None in the formal derivation. The claim that $g^{\mu\nu}$ is the unique rank-2 symmetric Lorentz-invariant tensor is proved (verified by examining boost and rotation constraints on components). The identification $p = -\rho$ from $T^{\mu\nu} = \rho_{\text{vac}} g^{\mu\nu}$ is algebraically verified with careful attention to the mostly-minus metric convention.

**Critical self-limitation:** The argument correctly identifies that it fails for bounded systems (assumption B2). This is not a logical gap but a correctly delimited scope.

### Argument C: Logical Chain

1. **Premise:** $|0\rangle$ is the ground state of $H$ (C3, C4); $H$ is time-independent (C1).
2. **Inference:** Any unitary $U|0\rangle = \sum_n c_n |n\rangle$ with $\sum |c_n|^2 = 1$.
3. **Inference:** $\langle 0|U^\dagger H U|0\rangle = \sum |c_n|^2 E_n \geq E_0 \sum |c_n|^2 = E_0$.
4. **Conclusion:** $\Delta E \geq 0$, hence $W_{\text{net}} \leq 0$.

**Logical gaps:** None. The proof is elementary and exact — it uses only the spectral bound and unitarity. No approximations are made.

**Two-level limiting case:** Verified explicitly in Eq. (C.12)--(C.13). Consistent with the general proof.

**Result: ALL three arguments have complete logical chains with no gaps.**

## 3. Assumption Independence

### Assumption Sets

| Argument | Assumptions |
|---|---|
| A (Thermodynamic) | A1: closed system; A2: conservative force; A3: fixed materials; A4: second law at $T=0$; A5: cyclic process |
| B (Lorentz) | B1: Poincaré-invariant vacuum; B2: no boundaries; B3: well-defined $T^{\mu\nu}$; B4: local Poincaré-covariant QFT |
| C (Passivity) | C1: time-independent $H$; C2: cyclic operation; C3: non-degenerate ground state; C4: QM framework; C5: same Hilbert space |

### Independence Analysis

**Question:** Is any argument's assumption set a logical subset of another's?

**A vs B:** Argument A assumes a Casimir system (plates, force, cycle). Argument B assumes unbounded free vacuum (no plates). These are fundamentally different physical setups. A's assumptions A1-A5 concern thermodynamic properties of a bounded system; B's assumptions B1-B4 concern symmetry properties of the free vacuum. **Neither is a subset of the other.**

**A vs C:** Both assume a cyclic process (A5, C2). However:
- A assumes the force is conservative (A2) — this is a property of the force, not the quantum state
- C assumes the Hamiltonian is time-independent (C1) — this is a property of the dynamics, not the force
- A works with thermodynamic quantities (work, heat); C works with quantum states (unitaries, energy expectation values)
**Neither is a subset of the other.** They overlap on "cyclic process" but differ on everything else.

**B vs C:** Argument B concerns the free vacuum and its stress-energy tensor. Argument C concerns the ground state of any quantum system with fixed $H$.
- B requires Poincaré invariance (B1); C does not
- C requires fixed $H$ (C1); B does not (but implicitly assumes $H$ doesn't change since it considers the vacuum state at a single time)
- B applies to the free vacuum specifically; C applies to ANY ground state
**Neither is a subset of the other.** C is more general in scope (any ground state, not just the vacuum), while B provides specific structural information ($p = -\rho$) that C does not.

**Result: The three assumption sets are genuinely independent.** No argument's assumptions are a subset of another's.

## 4. Mutual Consistency Check

**Question:** Do any assumptions from different arguments contradict each other?

| Pair | Potential Tension | Resolution |
|---|---|---|
| A2 (conservative force) vs C1 (fixed $H$) | If $H$ changes, the force might not be conservative | Not a contradiction: A2 and C1 are both sufficient conditions for their respective conclusions. They can fail simultaneously (moving plates with changing material properties) without contradicting each other. |
| A1 (closed system) vs B2 (no boundaries) | A1 assumes plates exist; B2 assumes no boundaries | Not a contradiction: the arguments address different physical configurations. A applies to the Casimir system; B applies to the free vacuum. They are complementary, not contradictory. |
| B1 (Poincaré invariance) vs C1 (fixed $H$) | Poincaré invariance requires a specific $H$ (free field); C1 just requires $H$ to not change in time | Not a contradiction: B1 specifies which $H$ (the free-field Hamiltonian), while C1 requires time-independence of whatever $H$ is being used. If $H$ is the free-field Hamiltonian and it doesn't change in time, both are satisfied. |
| A4 (second law at $T=0$) vs C4 (QM framework) | Could quantum mechanics violate the second law? | Not a contradiction: the second law is emergent from quantum mechanics for macroscopic systems. At the microscopic level, passivity provides the quantum foundation for the second law. The two are consistent: passivity (C) provides a microscopic underpinning for the thermodynamic result (A). |

**Result: No contradictions found between any pair of assumptions from different arguments.**

## 5. Coverage Map

### Which Physical Scenarios Does Each Argument Cover?

| Physical Scenario | Arg A | Arg B | Arg C | Covered? |
|---|---|---|---|---|
| Quasi-static cycle, fixed materials, Casimir plates | YES | no (boundaries) | YES (if $H$ fixed at each $a$) | YES (A, C) |
| Free (unbounded) vacuum, any process | no (no plates) | YES | YES | YES (B, C) |
| Non-quasi-static cyclic process, fixed plates | YES (2nd law) | no (boundaries) | YES | YES (A, C) |
| Moving plates (time-dependent $H$) | YES (if force remains conservative) | no (boundaries) | **NO** (C1 fails) | Partial (A only) |
| Material property change mid-cycle | **NO** (A3 fails) | no (boundaries) | Depends on details | **GAP** |
| Multi-copy vacuum extraction | YES (2nd law) | YES | YES (complete passivity) | YES (all three) |

### The Critical Gap

The three arguments collectively leave a gap for:

**Time-dependent Hamiltonian with material property changes and boundaries:**

- Argument A fails if materials change (A3 violated)
- Argument B fails because boundaries exist (B2 violated)
- Argument C fails because $H$ changes in time (C1 violated)

This is precisely the scenario envisioned by:
- **Pinto's proposal (1999):** Change plate conductivity between closing and opening stages
- **Dynamic Casimir effect:** Rapidly oscillating boundaries producing photons
- **Topology change proposals:** Creating/destroying a cavity

These loopholes are the subject of Phase 05 (boundary condition and material property loopholes) and Phase 06 (dynamic Casimir analysis).

### Overlap Regions

The arguments overlap and provide mutual reinforcement in several regimes:

1. **Free vacuum, cyclic process:** All three arguments apply. Maximal redundancy.
2. **Fixed Casimir plates, quasi-static cycle:** Arguments A and C both apply. Mutual cross-check.
3. **Any system, ground state, fixed $H$:** Argument C applies universally (strongest single argument).

## 6. Sign Convention Consistency

| Convention | Argument A | Argument B | Argument C | Consistent? |
|---|---|---|---|---|
| $F < 0$ attractive | $F_{\text{Cas}} = -\pi^2/(240a^4) < 0$ | Casimir stress tensor $T^{zz} > 0$ (attractive in bounded case) | Not directly used | YES |
| $E < 0$ for bounded | $E_{\text{Cas}} = -\pi^2/(720a^3) < 0$ | $T^{00} < 0$ between plates | $E_0$ is the minimum (sign irrelevant) | YES |
| $W_{\text{net}} > 0$ extraction | $W_{\text{net}} = 0$ (conservative) or $\leq 0$ (2nd law) | $W_{\text{net}} = 0$ ($p = -\rho$ medium) | $W_{\text{net}} = -\Delta E \leq 0$ | YES |

**Result: All sign conventions are used consistently across all three arguments.**

## 7. Reference Cross-Check

| Reference | Used in Arg | Role |
|---|---|---|
| Casimir (1948) | A | Energy and force formulas |
| Scandurra (2001) | A | Conservative force proof |
| Weinberg, QFT Vol. 1, §11.2 | B | $\langle 0|T^{\mu\nu}|0\rangle = \rho_{\text{vac}} g^{\mu\nu}$ |
| Jaffe (2005) | B | Alternative interpretation of Casimir effect |
| Pusz & Woronowicz (1978) | C | Passivity theorem |
| Lenard (1978) | C | Independent passivity result |
| Allahverdyan et al. (2004) | C | Maximum extractable work |

Each argument cites independent references. No argument relies on the conclusions of another. The references are internally consistent.

## Summary

| Check | Result |
|---|---|
| Dimensional consistency | PASS — all equations in all three derivations |
| Internal logic | PASS — no gaps in any argument chain |
| Assumption independence | PASS — no argument's assumptions are a subset of another's |
| Mutual consistency | PASS — no contradictions between any assumption pairs |
| Coverage completeness | PARTIAL — gap exists for time-dependent $H$ with boundaries and material changes |
| Sign conventions | PASS — all three arguments use conventions consistently |
| Reference independence | PASS — each argument cites independent sources |

**Overall verdict:** The three no-go arguments are dimensionally consistent, logically complete, genuinely independent, and mutually non-contradictory. They provide overlapping but non-identical coverage of the physical parameter space. The identified gap (time-dependent $H$ with material/boundary changes) correctly maps to the planned loophole analyses in Phases 05-06.
