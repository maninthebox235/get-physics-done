---
gpd_role: requirements
version: 1
approved: true
---

# Research Requirements: Zero-Point Energy Extraction Analysis

## R1. Analytical Derivations (Essential)

### R1.1 Thermodynamic No-Go Argument
- **Deliverable:** Formal derivation showing W_net ≤ 0 for any cyclic Casimir process at thermal equilibrium
- **Assumptions to state:** Second law of thermodynamics; vacuum as T=0 equilibrium state; quasi-static process
- **Validation:** Recover known result that conservative Casimir force gives ∮F·da = 0
- **Acceptance criterion:** Complete derivation with all assumptions numbered and explicitly stated

### R1.2 Lorentz Invariance No-Go Argument
- **Deliverable:** Argument from ⟨0|T^{μν}|0⟩ ∝ g^{μν} that vacuum energy is not extractable
- **Assumptions to state:** Unbroken Poincaré symmetry; no external fields or boundaries
- **Caveat to include:** Boundaries break translational invariance → Casimir effect exists
- **Acceptance criterion:** Clear statement of where the argument fails for bounded systems

### R1.3 Passivity No-Go Argument (Pusz-Woronowicz)
- **Deliverable:** Statement and proof sketch of vacuum passivity for fixed Hamiltonian
- **Assumptions to state:** KMS state at β=∞; fixed Hamiltonian; cyclic unitary operations
- **Key open question:** Behavior when Hamiltonian changes (time-dependent boundaries)
- **Acceptance criterion:** Rigorous statement with clear identification of the gap for time-dependent H

### R1.4 Assumption Comparison Table
- **Deliverable:** Table comparing all three no-go arguments
- **Columns:** Argument name | Key assumptions | What it proves | Known loopholes | Strength rating
- **Acceptance criterion:** Complete, internally consistent table

### R1.5 Conservative Force Proof
- **Deliverable:** Formal proof that Casimir force is conservative for fixed material properties
- **Method:** Show F = -∇V where V depends only on configuration (plate separation, geometry)
- **Acceptance criterion:** Proof complete with explicit conditions for conservativeness

## R2. Numerical Computation (Essential)

### R2.1 Casimir Force Benchmarks
- **Ideal plates T=0:** Reproduce F/A = -π²ℏc/(240a⁴) to relative error < 10⁻⁶
- **Finite T (Drude):** Reproduce Lifshitz formula values against Bordag et al. (2009)
- **Finite T (Plasma):** Same, with plasma model
- **Acceptance criterion:** All three benchmarks within stated tolerance; results documented with code

### R2.2 Quasi-Static Cycle Energy Budget
- **Deliverable:** Complete energy accounting for plate close-open cycle
- **Components:** W_close, W_open, W_net, ΔE_vacuum, Q (heat exchange if finite T)
- **Acceptance criterion:** Energy conservation verified to < 10⁻⁸ relative error

### R2.3 W_net Parameter Sweep
- **Variables:** a_min ∈ [10nm, 1μm], a_max ∈ [100nm, 10μm], T ∈ [0, 300K]
- **Grid:** 100 × 100 × 50 = 500k points
- **Deliverable:** 3D visualization of W_net(a_min, a_max, T); confirm W_net = 0 for conservative case
- **Acceptance criterion:** W_net/|W_close| < 10⁻¹⁰ across entire parameter space (verified with high precision)

## R3. Loophole Analysis (Essential)

### R3.1 Boundary Condition Change Loophole
- **Scenario:** Pinto-type cycle — change reflectivity mid-cycle to reduce separation cost
- **Analysis:** Include energy cost of reflectivity change; show total W_net ≤ 0
- **Reference:** Scandurra (2001)
- **Acceptance criterion:** Complete energy budget including material property change cost

### R3.2 Topology Change Loophole
- **Scenario:** Create cavity → extract Casimir energy → destroy cavity
- **Analysis:** Compute energy cost of cavity creation/destruction; compare to extracted energy
- **Acceptance criterion:** Complete energy budget; clear statement of net result

### R3.3 Non-Equilibrium State Loophole
- **Scenario:** Squeezed or excited vacuum states near boundaries
- **Analysis:** Check passivity of non-vacuum states; compute extractable work if any
- **Acceptance criterion:** Clear statement of whether non-equilibrium states evade passivity

### R3.4 Dynamic Casimir Loophole
- **Scenario:** Oscillating mirror creates real photons
- **Analysis:** Compute E_photons and W_mechanical; verify E_photons ≤ W_mechanical
- **Acceptance criterion:** Energy accounting to < 10⁻⁶ relative error; clear statement

## R4. Stretch Goals

### R4.1 Time-Dependent Hamiltonian Passivity
- **Extension of R1.3:** Formal treatment of passivity when boundaries modulate H(t)
- **Question:** Can boundary cycling create non-passive states?
- **Status:** Stretch — only if core phases complete ahead of schedule

### R4.2 Sphere-Plate Geometry (PFA)
- **Extension of R2.1:** Compute Casimir force for sphere-plate using proximity force approximation
- **Benchmark:** Compare against exact results in limiting cases
- **Status:** Stretch

### R4.3 Dynamic Casimir Computation
- **Extension of R3.4:** Full Bogoliubov coefficient computation for parametrically driven cavity
- **Deliverable:** Photon spectrum, total energy, comparison to drive energy
- **Status:** Stretch — desirable for completeness of loophole analysis

### R4.4 Atom Pumping Mechanism
- **New analysis:** Atoms traversing Casimir cavity with modified Lamb shift
- **Question:** Can modified atomic transitions extract net energy from vacuum?
- **Status:** Stretch — noted in literature as "not obviously thermodynamically forbidden"

## Traceability

| Requirement | Addresses | Phase | Status |
|-------------|-----------|-------|--------|
| R1.1 | Q1 (feasibility), Q2 (assumptions) | Phase 01 | Pending |
| R1.2 | Q1 (feasibility), Q2 (assumptions) | Phase 01 | Pending |
| R1.3 | Q1 (feasibility), Q2 (assumptions) | Phase 01 | Pending |
| R1.4 | Q2 (assumptions), Q3 (loopholes) | Phase 01 | Pending |
| R1.5 | Q1 (feasibility) | Phase 03 | Pending |
| R2.1 | Computational anchor | Phase 02 | Pending |
| R2.2 | Q1 (quantitative) | Phase 03 | Pending |
| R2.3 | Q1 (quantitative), Q2 (bounds) | Phase 04 | Pending |
| R3.1 | Q3 (loopholes) | Phase 05 | Pending |
| R3.2 | Q3 (loopholes) | Phase 05 | Pending |
| R3.3 | Q3 (loopholes) | Phase 06 | Pending |
| R3.4 | Q3 (loopholes) | Phase 06 | Pending |
| R4.1 | Extension (passivity) | Stretch | -- |
| R4.2 | Extension (geometry) | Stretch | -- |
| R4.3 | Extension (dynamic Casimir) | Stretch | -- |
| R4.4 | Extension (atom pumping) | Stretch | -- |
