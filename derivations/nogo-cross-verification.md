# Cross-Verification of No-Go Arguments A, B, C

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, regularization_scheme=zeta, casimir_force_sign=F<0_attractive, casimir_energy_sign=E<0_bounded, work_sign=W_net>0_extraction

This document cross-verifies the three independent no-go arguments against cyclic zero-point energy extraction:

- **Argument A (Thermodynamic):** derivations/nogo-thermodynamic.md
- **Argument B (Lorentz Invariance):** derivations/nogo-lorentz.md
- **Argument C (Passivity):** derivations/nogo-passivity.md

## 1. Dimensional Consistency

### Argument A (Thermodynamic)

| Equation | LHS Dimensions | RHS Dimensions | Status |
|---|---|---|---|
| (A.1) $E_{\text{Cas}}/\mathcal{A} = -\pi^2/(720\,a^3)$ | $[\text{energy}/\text{length}^2] = [\text{length}^{-3}]$ | $[\text{length}^{-3}]$ | Correct |
| (A.2) $F_{\text{Cas}}/\mathcal{A} = -\pi^2/(240\,a^4)$ | $[\text{force}/\text{area}] = [\text{length}^{-4}]$ | $[\text{length}^{-4}]$ | Correct |
| (A.5) $W_{\text{net}} = \oint F\,da$ | $[\text{energy}/\text{area}]$ | $[\text{length}^{-4}][\text{length}] = [\text{length}^{-3}]$ | Correct |
| (A.7) $W_{\text{net}} \leq 0$ | $[\text{energy}]$ | dimensionless inequality | Correct |

### Argument B (Lorentz Invariance)

| Equation | LHS Dimensions | RHS Dimensions | Status |
|---|---|---|---|
| (B.6) $\langle 0|T^{\mu\nu}|0\rangle = \rho_{\text{vac}} g^{\mu\nu}$ | $[\text{length}^{-4}]$ | $[\text{length}^{-4}][\text{dimensionless}]$ | Correct |
| (B.9) $p_{\text{vac}} = -\rho_{\text{vac}}$ | $[\text{energy}/\text{volume}]$ | $[\text{energy}/\text{volume}]$ | Correct |
| (B.15) $dU + \delta W = 0$ | $[\text{energy}]$ | $[\text{energy}]$ | Correct |
| (B.16) $W_{\text{net}} = 0$ | $[\text{energy}]$ | — | Correct |
| (B.17) Components of $\langle T^{\mu\nu}\rangle$ | $[\text{length}^{-4}]$ | $[\text{length}^{-4}]$ | Correct |

### Argument C (Passivity)

| Equation | LHS Dimensions | RHS Dimensions | Status |
|---|---|---|---|
| (C.2) $\Delta E = \text{Tr}(U\rho U^\dagger H) - \text{Tr}(\rho H)$ | $[\text{energy}]$ | $[\text{energy}] - [\text{energy}]$ | Correct |
| (C.3) $\mathcal{W} = \text{Tr}(\rho H) - \min_U \text{Tr}(U\rho U^\dagger H)$ | $[\text{energy}]$ | $[\text{energy}] - [\text{energy}]$ | Correct |
| (C.7) $\langle\psi|H|\psi\rangle = \sum_n |c_n|^2 E_n$ | $[\text{energy}]$ | $[\text{dimensionless}][\text{energy}]$ | Correct |
| (C.11) Two-level check | $[\text{energy}]$ | $[\text{energy}]$ | Correct |
| (C.17) Adiabatic condition | $[\text{time}^{-1}]$ | $[\text{energy}^2]/[\text{energy}] = [\text{energy}] = [\text{time}^{-1}]$ | Correct |

**Verdict:** All three derivations are dimensionally consistent. No dimensional errors found.

## 2. Internal Logic Verification

### Argument A: Logical Chain

1. **Premise:** Casimir force $F(a)$ depends only on separation $a$ (A2, A3) $\checkmark$
2. **Step:** $F = -\partial E/\partial a$ is therefore a conservative force $\checkmark$
3. **Step:** Line integral of conservative force over closed path vanishes: $\oint F\,da = 0$ $\checkmark$
4. **Conclusion:** $W_{\text{net}} = 0$ for quasi-static cycles $\checkmark$
5. **Generalization:** Kelvin-Planck (A4) gives $W_{\text{net}} \leq 0$ for any cyclic process $\checkmark$

**Gap check:** No logical gaps. The conservative force argument is mathematically rigorous. The second law generalization is a standard thermodynamic argument. The chain is complete.

### Argument B: Logical Chain

1. **Premise:** Vacuum $|0\rangle$ is Poincare-invariant (B1) $\checkmark$
2. **Step:** Translation invariance $\Rightarrow$ $\langle T^{\mu\nu}\rangle$ is constant (B.2-B.3) $\checkmark$
3. **Step:** Lorentz invariance $\Rightarrow$ $C^{\mu\nu}$ is invariant tensor $\Rightarrow$ $C^{\mu\nu} \propto g^{\mu\nu}$ (B.4-B.6) $\checkmark$
4. **Step:** Read off components: $p = -\rho$ equation of state (B.9-B.10) $\checkmark$
5. **Step:** First law with $p = -\rho$: $dU + \delta W = 0$ (B.11-B.15) $\checkmark$
6. **Conclusion:** $W_{\text{net}} = 0$ for Lorentz-invariant vacuum $\checkmark$
7. **Caveat:** Argument fails for bounded systems (B2 violated) $\checkmark$

**Gap check:** No logical gaps. The uniqueness of $g^{\mu\nu}$ as a Lorentz-invariant rank-2 symmetric tensor is verified by the boost argument in the derivation. The chain is complete.

### Argument C: Logical Chain

1. **Premise:** Vacuum is ground state of $H$ (standard QFT) $\checkmark$
2. **Definition:** Passivity defined via Eq. (C.1) $\checkmark$
3. **Step:** Pusz-Woronowicz theorem: ground state satisfies passivity conditions (a) and (b) $\checkmark$
4. **Step:** Elementary proof: $\sum |c_n|^2 E_n \geq E_0 \sum |c_n|^2 = E_0$ (C.5-C.9) $\checkmark$
5. **Conclusion:** $\Delta E \geq 0$, equivalently $W_{\text{net}} \leq 0$ $\checkmark$
6. **Strengthening:** Complete passivity rules out multi-copy schemes $\checkmark$
7. **Caveat:** Fails for time-dependent $H$ (C1 violated by moving plates) $\checkmark$

**Gap check:** No logical gaps. The elementary proof is self-contained and uses only the definition of ground state and unitarity. The Pusz-Woronowicz theorem is stated with reference. The chain is complete.

**Verdict:** All three arguments have complete logical chains with no gaps.

## 3. Assumption Independence

### Assumption Sets

| Argument | Assumptions | Domain |
|---|---|---|
| **A** (Thermodynamic) | A1 (closed system), A2 (conservative force), A3 (fixed materials), A4 (second law at T=0), A5 (cyclic) | Classical thermodynamics of Casimir system |
| **B** (Lorentz) | B1 (Poincare-invariant vacuum), B2 (no boundaries), B3 (well-defined $T^{\mu\nu}$), B4 (local Poincare-covariant QFT) | Relativistic QFT in free space |
| **C** (Passivity) | C1 (time-independent $H$), C2 (cyclic), C3 (non-degenerate ground state), C4 (QM framework), C5 (same Hilbert space) | Quantum mechanics / quantum thermodynamics |

### Independence Analysis

**Are A's assumptions a subset of B's?** No.
- A requires specific thermodynamic structure (second law, closed system, conservative force). B requires Poincare symmetry and covariant QFT. Neither set implies the other.
- A applies to bounded systems (Casimir plates); B explicitly does NOT (requires B2: no boundaries).

**Are A's assumptions a subset of C's?** No.
- A operates at the thermodynamic level (forces, work, heat). C operates at the quantum state level (unitaries, Hilbert space).
- A allows time-dependent processes (second law generalization); C requires fixed $H$ (C1).
- A requires cyclicity of configuration (A5); C requires cyclicity of Hamiltonian (C2). These are related but distinct.

**Are B's assumptions a subset of C's?** No.
- B requires Poincare invariance (spacetime symmetry). C requires only quantum mechanics with a ground state.
- B is a field-theoretic argument about the vacuum stress-energy tensor. C is a state-level argument about energy eigenvalues.
- B applies to free space only. C applies to any system with a ground state (including bounded systems, as long as $H$ is fixed).

**Are any pair's assumptions contradictory?** No --- see Section 4.

**Verdict:** The three assumption sets are genuinely independent. No argument's assumptions are a subset of another's.

## 4. Mutual Consistency of Assumptions

We check whether any assumption from one argument contradicts an assumption from another.

### Potentially Overlapping Assumptions

| Pair | Overlap | Contradiction? |
|---|---|---|
| A5 (cyclic process) vs. C2 (cyclic Hamiltonian) | Both require cyclicity, but at different levels: A5 requires the system configuration to return; C2 requires the Hamiltonian to return. These are compatible --- a cyclic configuration change gives a cyclic Hamiltonian. | No |
| A1 (closed system) vs. C5 (same Hilbert space) | Both require no external degrees of freedom to enter or leave. Compatible. | No |
| B1 (Poincare invariance) vs. A2 (conservative force on plates) | B1 describes the free vacuum; A2 describes the force between plates. B1 is a property of the vacuum state; A2 is a property of the force derived from the vacuum energy in the presence of plates. They refer to different physical situations (free space vs. bounded). | No |
| B2 (no boundaries) vs. A2 (force depends on plate separation) | A requires plates (boundaries); B requires no plates. These assumptions are incompatible in the sense that they apply to **different physical scenarios**. This is not a logical contradiction --- it means A and B cover different regimes. | No (complementary, not contradictory) |
| C1 (fixed $H$) vs. A5 (cyclic process) | A cyclic process in Argument A involves moving plates, which changes $H(t)$. C1 requires $H$ to be fixed. These assumptions are again **complementary**: Argument A applies to the physical Casimir cycle (moving plates), while Argument C applies to the idealized case of fixed plates. Both are valid in their respective domains. | No (complementary) |

### Assessment

The assumptions are **mutually consistent** in the following sense:
- No pair of assumptions creates a logical contradiction.
- Some assumption pairs apply to non-overlapping physical scenarios (e.g., B2 vs. A's plate system, or C1 vs. A's moving-plate cycle). This is by design: the three arguments cover different aspects of the no-go, and their complementarity is a feature, not a bug.

**Verdict:** No contradictions between assumption sets. The assumptions are consistent.

## 5. Coverage Map

### Which Physical Scenarios Does Each Argument Cover?

| Scenario | Argument A | Argument B | Argument C |
|---|---|---|---|
| Quasi-static cycle, fixed materials | **Covers** ($W_{\text{net}} = 0$) | Does not apply (boundaries present) | Covers only if adiabatic (reduces to A) |
| Quasi-static cycle, changing materials | A3 violated --- **loophole** | Does not apply | C1 may be violated (H changes) |
| Free vacuum, no boundaries | Trivially applies (no force, $W = 0$) | **Covers** ($W_{\text{net}} = 0$) | Covers ($H$ is fixed free-field $H$) |
| Fixed plates, arbitrary unitary | A applies to mechanical work only | Does not apply (boundaries) | **Covers** ($\Delta E \geq 0$) |
| Moving plates, non-adiabatic (dynamic Casimir) | A4 gives $W_{\text{net}} \leq 0$ | Does not apply | C1 violated --- **gap** |
| Multiple cavities, joint operations | A applies to each independently | Does not apply | Complete passivity covers this |

### Overlap and Complementarity

- **A and B overlap** for the trivial case of free vacuum (no plates). Both give $W_{\text{net}} = 0$.
- **A and C overlap** for quasi-static (adiabatic) cycles with fixed materials. Both give $W_{\text{net}} \leq 0$.
- **B and C overlap** for the free vacuum with fixed Hamiltonian. Both give $W_{\text{net}} = 0$.
- **No single argument** covers the dynamic Casimir regime (rapidly moving plates) with full rigor. This is the shared gap that motivates Phase 06.

### Key Loopholes by Argument

| Argument | Key Loophole | Target Assumption | Downstream Phase |
|---|---|---|---|
| A | Material property switching | A3 (fixed materials) | Phase 05 (Pinto's proposal) |
| B | Boundaries break Lorentz invariance | B2 (no boundaries) | Phase 05 (boundary loophole R3.1) |
| C | Time-dependent Hamiltonian | C1 (fixed $H$) | Phase 06 (dynamic Casimir) |

## 6. Convention Consistency

All three derivations use identical conventions as declared in their ASSERT_CONVENTION lines:

| Convention | Value | A | B | C |
|---|---|---|---|---|
| Natural units | $\hbar = c = k_B = 1$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| Metric signature | $(+,-,-,-)$ (mostly minus) | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| Casimir force sign | $F < 0$ attractive | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| Casimir energy sign | $E < 0$ bounded | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| Work sign | $W_{\text{net}} > 0$ = extraction | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| Regularization | Zeta function | $\checkmark$ | $\checkmark$ | $\checkmark$ |

**Verdict:** No convention mismatches across the three derivations.

## 7. Reference Coverage

| Reference | Required Action | Argument A | Argument B | Argument C |
|---|---|---|---|---|
| ref-pusz-woronowicz | read, cite | --- | --- | Cited (theorem statement) |
| ref-weinberg-qft | read, cite | --- | Cited ($T^{\mu\nu}$ argument) | --- |
| ref-lenard | cite | --- | --- | Cited (independent passivity result) |
| ref-scandurra | cite | Cited (conservative force proof) | --- | --- |
| ref-jaffe | cite | --- | Cited (Casimir without vacuum energy) | --- |

All must-surface references (ref-pusz-woronowicz, ref-weinberg-qft) are cited in the appropriate derivations.

## Summary

| Check | Status |
|---|---|
| Dimensional consistency (all 3 derivations) | **PASSED** |
| Internal logic (no gaps in any argument) | **PASSED** |
| Assumption independence (no subset relations) | **PASSED** |
| Mutual consistency (no contradictions) | **PASSED** |
| Convention consistency (all use same conventions) | **PASSED** |
| Reference coverage (all must-surface refs cited) | **PASSED** |

**Overall verdict:** The three no-go arguments are dimensionally consistent, logically complete, based on independent assumptions, and mutually non-contradictory. They provide complementary coverage of the no-go landscape, with identified gaps (notably the dynamic Casimir regime) that motivate subsequent phases of analysis.
