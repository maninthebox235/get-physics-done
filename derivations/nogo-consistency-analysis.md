# Mutual Consistency Analysis of No-Go Assumptions

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, regularization_scheme=zeta, casimir_force_sign=F<0_attractive, casimir_energy_sign=E<0_bounded, work_sign=W_net>0_extraction

This document systematically checks all pairs of assumptions across the three no-go arguments (A, B, C) for mutual consistency, identifies shared assumptions, and characterizes the coverage gap.

**Reference:** Pusz & Woronowicz, Commun. Math. Phys. 58, 273 (1978) --- passivity theorem underlying Argument C.

## 1. Assumption Inventory

| ID | Statement | Domain |
|----|-----------|--------|
| A1 | Closed system (no external energy input) | Thermodynamic |
| A2 | $F_{\text{Cas}}(a)$ is conservative (depends on $a$ alone) | Mechanical |
| A3 | Fixed material properties throughout cycle | Material |
| A4 | Second law (Kelvin--Planck) holds at $T = 0$ | Thermodynamic |
| A5 | Cyclic process (returns to initial state) | Process |
| B1 | Vacuum $|0\rangle$ is Poincare-invariant | Symmetry |
| B2 | No boundaries or external fields (Minkowski $\mathbb{R}^{3,1}$) | Geometry |
| B3 | Renormalized $\langle 0|T^{\mu\nu}|0\rangle$ is well-defined and Lorentz-covariant | QFT |
| B4 | Local Poincare-covariant QFT (Wightman axioms) | QFT |
| C1 | Time-independent Hamiltonian $H$ | Dynamical |
| C2 | Cyclic process ($H(t_f) = H(t_i)$) | Process |
| C3 | Non-degenerate ground state | Spectral |
| C4 | Quantum mechanical framework ($H$ self-adjoint, unitary evolution) | QM |
| C5 | Same Hilbert space throughout (no DOF added/removed) | QM |

## 2. Pairwise Consistency: A--B Pairs (20 pairs)

### A1 (closed system) vs B1--B4

| Pair | Verdict | Analysis |
|------|---------|----------|
| A1--B1 | **Compatible** | A1 requires no external energy source for the Casimir system. B1 requires vacuum Poincare invariance. These address different physical configurations (A: bounded system with plates; B: free vacuum). No logical tension --- one can have a closed Casimir system (A1) and separately the free vacuum be Poincare-invariant (B1). |
| A1--B2 | **Compatible (disjoint domains)** | A1 presupposes plates exist (thermodynamic system). B2 requires no boundaries. These cannot be simultaneously realized in a single physical scenario, but this is not a contradiction --- it means A and B address different regimes. The assumptions are logically independent, not contradictory. |
| A1--B3 | **Compatible** | A1 is about energy input; B3 is about renormalization of vacuum expectation values. No tension. |
| A1--B4 | **Compatible** | A1 is thermodynamic; B4 is about QFT axioms. No tension. |

### A2 (conservative force) vs B1--B4

| Pair | Verdict | Analysis |
|------|---------|----------|
| A2--B1 | **Compatible** | Conservative force (A2) is a mechanical property. Poincare invariance (B1) is a symmetry property of the vacuum. In fact, B1 supports A2: in a Poincare-invariant QFT, the Casimir force between fixed-material plates is derivable from a potential energy $E_{\text{Cas}}(a)$, making it conservative. |
| A2--B2 | **Compatible (disjoint domains)** | A2 requires plates (to have a force). B2 requires no plates. Same as A1--B2: the assumptions address different physical setups and do not conflict logically. |
| A2--B3 | **Compatible** | Both concern well-defined vacuum properties (force from energy, stress-energy tensor). No tension. |
| A2--B4 | **Compatible** | A2 is a consequence of QFT with fixed boundaries; B4 requires QFT axioms. A2 is weaker than B4 --- conservative force is a derived property, while Wightman axioms are foundational. |

### A3 (fixed materials) vs B1--B4

| Pair | Verdict | Analysis |
|------|---------|----------|
| A3--B1 | **Compatible** | Fixed materials (A3) constrain the plates. Poincare invariance (B1) constrains the vacuum. No overlap or tension. |
| A3--B2 | **Compatible (disjoint domains)** | A3 presupposes plates with materials. B2 requires no plates. |
| A3--B3 | **Compatible** | Fixed materials ensure the boundary conditions on the field are well-defined at each plate separation, which supports the well-definedness of $\langle T^{\mu\nu}\rangle$ near the plates. |
| A3--B4 | **Compatible** | A3 is a material constraint; B4 is a QFT axiom. No conflict. |

### A4 (second law at T=0) vs B1--B4

| Pair | Verdict | Analysis |
|------|---------|----------|
| A4--B1 | **Compatible** | The second law at $T = 0$ (A4) is a thermodynamic axiom. Poincare invariance (B1) is a symmetry statement. They operate in different domains. Moreover, the passivity of the vacuum (Argument C) provides a microscopic foundation for A4: the ground state cannot yield work, consistent with Kelvin--Planck. |
| A4--B2 | **Compatible** | A4 is universal thermodynamics; B2 is a geometric constraint. No tension. |
| A4--B3 | **Compatible** | The second law is consistent with having a well-defined stress-energy tensor. The vacuum energy density $\rho_{\text{vac}}$ being finite (B3) does not violate thermodynamics --- the $p = -\rho$ equation of state prevents extraction. |
| A4--B4 | **Compatible** | Standard QFT (B4) is consistent with the second law. In particular, the CPT theorem and unitarity in QFT enforce the KMS condition for thermal states, supporting thermodynamic laws. |

### A5 (cyclic process) vs B1--B4

| Pair | Verdict | Analysis |
|------|---------|----------|
| A5--B1 | **Compatible** | A cyclic process (A5) returns the system to its initial state. Poincare invariance (B1) of the vacuum is a static property. No tension. |
| A5--B2 | **Compatible (disjoint domains)** | A5 involves cycling plate separations (plates present). B2 requires no plates. |
| A5--B3 | **Compatible** | Cyclic processes are consistent with well-defined $\langle T^{\mu\nu}\rangle$. |
| A5--B4 | **Compatible** | Cyclic unitary evolution is standard in QFT. |

**A--B Summary:** All 20 pairs are compatible. Four pairs (A1--B2, A2--B2, A3--B2, A5--B2) involve assumptions from disjoint physical domains (bounded vs unbounded), which means they cannot be simultaneously applied to a single system but are not logically contradictory.

## 3. Pairwise Consistency: A--C Pairs (25 pairs)

### A1 (closed system) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| A1--C1 | **Compatible (C1 implies A1 in context)** | If $H$ is time-independent (C1), then in particular no external energy is coupled in (since external driving would modify $H$). C1 is stronger than A1: C1 $\Rightarrow$ A1 (in the context of a quantum system), but A1 $\not\Rightarrow$ C1 (a system can be closed yet have time-dependent internal dynamics). |
| A1--C2 | **Compatible** | Both involve cyclic processes in closed systems. No tension. |
| A1--C3 | **Compatible** | A closed system (A1) can have a non-degenerate ground state (C3). |
| A1--C4 | **Compatible** | Quantum mechanics (C4) is consistent with closed thermodynamic systems (A1). |
| A1--C5 | **Compatible** | No DOF addition (C5) is consistent with closed system (A1). In fact, C5 reinforces A1. |

### A2 (conservative force) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| A2--C1 | **Compatible (related)** | If $H$ is time-independent (C1), the force $F = -\partial E_0/\partial a$ is automatically conservative, since $E_0(a)$ is a well-defined function. C1 $\Rightarrow$ A2 (under the assumption that the force is derived from the ground state energy). A2 does not require C1 --- the force can be conservative even with time-dependent $H$, as long as the force at each $a$ depends only on $a$. |
| A2--C2 | **Compatible** | A conservative force (A2) and a cyclic process (C2) are independent constraints. Both contribute to $W_{\text{net}} = 0$. |
| A2--C3 | **Compatible** | Non-degenerate ground state (C3) ensures $E_0(a)$ is a smooth function of $a$ (level crossings are avoided), supporting the conservative force property (A2). |
| A2--C4 | **Compatible** | Conservative force is a derived property in quantum mechanics. |
| A2--C5 | **Compatible** | Same Hilbert space (C5) ensures the force is well-defined throughout the process. |

### A3 (fixed materials) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| A3--C1 | **Compatible (related)** | Fixed materials (A3) support time-independent $H$ (C1): if materials change, the boundary conditions change, and $H$ changes. However, A3 $\not\Rightarrow$ C1 in general, because moving plates change $H$ even with fixed materials. And C1 $\not\Rightarrow$ A3, since $H$ could be fixed while material properties are irrelevant (e.g., ideal conductors). They are related but logically independent. |
| A3--C2 | **Compatible** | Fixed materials (A3) support cyclic processes (C2): if materials are unchanged, the system can return to its initial state more easily. |
| A3--C3 | **Compatible** | Fixed materials do not affect ground state degeneracy. |
| A3--C4 | **Compatible** | Fixed materials is a classical constraint; QM framework is foundational. |
| A3--C5 | **Compatible** | Fixed materials means no new degrees of freedom introduced, supporting C5. |

### A4 (second law at T=0) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| A4--C1 | **Compatible (C provides microscopic foundation for A4)** | The passivity of the ground state (derived from C1--C5) provides a quantum-mechanical foundation for the second law at $T = 0$ (A4). The two are deeply connected: passivity IS the microscopic basis for Kelvin--Planck at zero temperature. |
| A4--C2 | **Compatible** | The second law applies to cyclic processes (A4); C2 requires the process to be cyclic. Mutually reinforcing. |
| A4--C3 | **Compatible** | Non-degenerate ground state ensures $T = 0$ is a well-defined, unique state. |
| A4--C4 | **Compatible** | The second law is consistent with quantum mechanics. Passivity provides the bridge. |
| A4--C5 | **Compatible** | No DOF changes (C5) is consistent with the Kelvin--Planck formulation (A4). |

### A5 (cyclic process) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| A5--C1 | **Compatible** | A5 (system returns to initial state) and C1 (fixed $H$) are independent requirements. A cyclic process is possible with or without fixed $H$; fixed $H$ is possible with or without a cyclic process. |
| A5--C2 | **Compatible (essentially equivalent)** | A5 and C2 both require cyclicity. A5 states the full thermodynamic state returns; C2 states $H(t_f) = H(t_i)$. C2 is weaker (the Hamiltonian returns, but the quantum state need not). A5 is stronger (everything returns). A5 $\Rightarrow$ C2, but C2 $\not\Rightarrow$ A5. |
| A5--C3 | **Compatible** | Cyclic processes are compatible with non-degenerate ground states. |
| A5--C4 | **Compatible** | Cyclic processes are standard in QM. |
| A5--C5 | **Compatible** | System returning to initial state (A5) requires the same Hilbert space (C5). A5 implies C5 in this context. |

**A--C Summary:** All 25 pairs are compatible. Several pairs reveal logical relationships:
- C1 $\Rightarrow$ A1 (fixed $H$ implies no external energy input)
- C1 $\Rightarrow$ A2 (fixed $H$ implies conservative ground-state-derived force)
- A5 $\Rightarrow$ C2 (full cyclic process implies Hamiltonian returns)
- A5 $\Rightarrow$ C5 (full return implies same Hilbert space)
- C1+C3+C4 provides microscopic foundation for A4 (passivity $\Rightarrow$ second law at $T=0$)

## 4. Pairwise Consistency: B--C Pairs (20 pairs)

### B1 (Poincare invariance) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| B1--C1 | **Compatible** | Poincare invariance (B1) specifies which vacuum/Hamiltonian (the free field). Time-independence (C1) requires $H$ to be constant. The free-field Hamiltonian is time-independent in the Heisenberg picture, so B1 and C1 are simultaneously satisfiable. |
| B1--C2 | **Compatible** | A cyclic process (C2) in a Poincare-invariant vacuum is permitted. |
| B1--C3 | **Compatible** | The free-field vacuum is unique (non-degenerate ground state) by the Reeh--Schlieder theorem and cluster decomposition. B1 supports C3. |
| B1--C4 | **Compatible** | Poincare-invariant QFT satisfies the QM framework. B4 and C4 are both foundational. |
| B1--C5 | **Compatible** | Poincare invariance does not change the Hilbert space. |

### B2 (no boundaries) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| B2--C1 | **Compatible** | No boundaries (B2) and fixed $H$ (C1) are independent geometric and dynamical constraints. |
| B2--C2 | **Compatible** | Cyclic processes (C2) are possible in unbounded space. |
| B2--C3 | **Compatible** | The free-field vacuum in unbounded space is non-degenerate. |
| B2--C4 | **Compatible** | QM framework applies in unbounded space. |
| B2--C5 | **Compatible** | No boundaries means the Hilbert space is fixed (Fock space of free fields). |

### B3 (well-defined $\langle T^{\mu\nu}\rangle$) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| B3--C1 | **Compatible** | Well-defined stress-energy (B3) and fixed $H$ (C1) are independent. Both are satisfiable in free QFT. |
| B3--C2 | **Compatible** | Well-defined $\langle T^{\mu\nu}\rangle$ is compatible with cyclic processes. |
| B3--C3 | **Compatible** | Non-degenerate ground state contributes to a well-defined $\langle T^{\mu\nu}\rangle$. |
| B3--C4 | **Compatible** | B3 is a regularity condition within the QM framework (C4). |
| B3--C5 | **Compatible** | Same Hilbert space ensures $\langle T^{\mu\nu}\rangle$ remains well-defined. |

### B4 (local Poincare-covariant QFT) vs C1--C5

| Pair | Verdict | Analysis |
|------|---------|----------|
| B4--C1 | **Compatible** | Wightman axioms (B4) are compatible with time-independent Hamiltonians (C1). The free-field Hamiltonian satisfies both. |
| B4--C2 | **Compatible** | Cyclic processes are permitted in QFT. |
| B4--C3 | **Compatible** | Wightman axioms imply a unique vacuum (cluster decomposition), supporting C3. |
| B4--C4 | **Compatible (B4 is stronger)** | Wightman axioms (B4) imply the QM framework (C4). B4 $\Rightarrow$ C4. |
| B4--C5 | **Compatible** | Wightman axioms work within a fixed Hilbert space (Fock space). |

**B--C Summary:** All 20 pairs are compatible. Key logical relationships:
- B1 + cluster decomposition $\Rightarrow$ C3 (Poincare-invariant vacuum is non-degenerate)
- B4 $\Rightarrow$ C4 (Wightman axioms imply QM framework)
- B2 supports C5 (no boundaries means a fixed Fock space)

## 5. Shared Assumptions (Overlap)

Several assumptions across the three arguments express related physical requirements:

| Shared Concept | Argument A | Argument B | Argument C | Relationship |
|----------------|-----------|-----------|-----------|--------------|
| **Cyclicity** | A5 (full thermodynamic return) | --- | C2 ($H$ returns) | A5 $\Rightarrow$ C2 (A5 is stronger) |
| **Vacuum is special** | A4 ($T=0$ reservoir, second law) | B1 (Poincare-invariant ground state) | C3 (non-degenerate ground state) | All assert uniqueness/minimality of the vacuum, from different perspectives |
| **No external input** | A1 (closed system) | B2 (no external fields) | C1 (fixed $H$), C5 (same Hilbert space) | Related: all exclude external perturbations |
| **Well-defined QFT** | (implicit in A2 via Scandurra) | B3, B4 (Wightman axioms) | C4 (QM framework) | B4 $\Rightarrow$ C4; A2 is a derived consequence |
| **Fixed system structure** | A3 (fixed materials) | B2 (fixed geometry: no boundaries) | C1 (fixed $H$), C5 (fixed Hilbert space) | All restrict changes to the system, but in different ways |

These overlaps are **compatible**, not contradictory. They reflect that the three arguments approach the same physical question (vacuum energy extraction) from different foundational perspectives, and the underlying physics naturally leads to overlapping requirements.

## 6. Consistency Verdict

$$
\boxed{\text{All 65 assumption pairs are mutually consistent. No contradictions found.}}
$$

**Summary of logical relationships discovered:**

| Implication | Direction | Physical Meaning |
|-------------|-----------|-----------------|
| C1 $\Rightarrow$ A1 | C implies A | Fixed $H$ implies no external energy coupling |
| C1 $\Rightarrow$ A2 | C implies A | Fixed $H$ implies the ground-state-derived force is conservative |
| A5 $\Rightarrow$ C2 | A implies C | Full thermodynamic return implies Hamiltonian return |
| A5 $\Rightarrow$ C5 | A implies C | Full return to initial state implies same Hilbert space |
| B4 $\Rightarrow$ C4 | B implies C | Wightman axioms imply the QM framework |
| B1 + decomposition $\Rightarrow$ C3 | B implies C | Poincare-invariant vacuum is non-degenerate |
| C1+C3+C4 $\Rightarrow$ A4 | C implies A | Passivity provides microscopic basis for second law at $T=0$ |

These implications demonstrate that Argument C (passivity) is in many ways the most fundamental: its assumptions imply several of Argument A's assumptions, placing the thermodynamic no-go on a rigorous quantum-mechanical footing.

## 7. Coverage Gap Analysis

### Which scenarios does each argument exclude?

| Regime | A applies? | B applies? | C applies? | Net coverage |
|--------|-----------|-----------|-----------|-------------|
| Equilibrium cycle, fixed materials, Casimir plates | YES | NO (B2) | YES (if $H$ fixed at each $a$) | Covered (A+C) |
| Free (unbounded) vacuum, any process | NO (no plates) | YES | YES | Covered (B+C) |
| Non-quasi-static cycle, fixed plates at fixed $a$ | YES (A4) | NO (B2) | YES | Covered (A+C) |
| Moving plates, adiabatic, fixed materials | YES (A2 holds) | NO (B2) | Marginal (C1 violated, but adiabatic limit recovers $W_{\text{net}} = 0$) | Covered (A) |
| Moving plates, non-adiabatic, fixed materials | YES (A2 holds) | NO (B2) | NO (C1 violated) | Partial (A only) |
| Material property switching mid-cycle | NO (A3) | NO (B2) | Depends (C1 may be violated if switching changes $H$) | **GAP** |
| Multi-copy extraction schemes | YES (A4) | YES (B) | YES (complete passivity) | Covered (all three) |

### The Critical Gap

The three arguments collectively fail to cover:

$$
\boxed{\text{Time-dependent } H \text{ with boundaries and material property changes}}
$$

Specifically, the gap is the intersection of three assumption violations:
- **A3 violated:** Material properties change during the cycle
- **B2 violated:** Boundaries (plates) are present
- **C1 violated:** Hamiltonian is time-dependent (due to moving plates and/or changing materials)

This gap corresponds to physically proposed extraction schemes:

| Proposal | Which assumptions violated | Phase for analysis |
|----------|---------------------------|-------------------|
| Pinto (1999): conductivity switching | A3 (material change) + B2 (boundaries) | Phase 05 |
| Dynamic Casimir effect | C1 (time-dependent $H$) + B2 (boundaries) | Phase 06 |
| Topology change (cavity creation/destruction) | A3 + B2 + C1 + C5 | Phase 05--06 |

### Gap Characterization

The gap is not a flaw in the no-go arguments --- it precisely delineates the boundary of what the arguments can constrain. The existence of this gap does not mean energy extraction IS possible in the uncovered regime; it means that different tools are needed to analyze those scenarios.

Key physics in the gap region:
1. **Energy cost of material changes (A3 violation):** Changing conductivity requires energy input (e.g., photoexcitation of carriers). The energy budget must include this cost. This is the focus of Phase 03 (conservative force proof) and Phase 05 (boundary loopholes).
2. **Photon production (C1 violation):** The dynamic Casimir effect produces photons when boundaries move non-adiabatically. But the photon energy comes from mechanical work on the boundaries, not from vacuum energy. Phase 06 analyzes whether the complete energy budget ever permits $W_{\text{net}} > 0$.
3. **Vacuum energy vs. interaction energy:** Argument B reminds us that "vacuum energy" between plates is really the interaction energy of the boundary conditions, not intrinsic vacuum energy. This reframing (Jaffe, 2005) is relevant to all gap scenarios.
