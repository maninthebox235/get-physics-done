---
gpd_role: research
phase: "03"
phase_name: "Conservative Force Proof and Cycle Analysis"
research_mode: balanced
---

# Phase 03 Research: Conservative Force Proof and Cycle Analysis

## 1. Mathematical Framework

### 1.1 Conservative Force from Free Energy

The Casimir force between parallel plates is conservative for fixed material properties because it derives from a potential — the Helmholtz free energy F(a, T):

**At T = 0 (pure vacuum energy):**
$$F_{\text{Casimir}}(a) = -\frac{\partial E_{\text{vac}}(a)}{\partial a}$$

where E_vac(a) is the regularized vacuum energy. Since E_vac depends only on plate separation a (and material/geometry parameters that are fixed during the cycle), the force is the gradient of a scalar potential → conservative.

**At finite T (Lifshitz framework):**
$$F_{\text{Casimir}}(a, T) = -\frac{\partial \mathcal{F}(a, T)}{\partial a}\bigg|_T$$

where F(a, T) is the Helmholtz free energy of the electromagnetic field between plates. The key thermodynamic identity:

$$\mathcal{F}(a, T) = E(a, T) - T S(a, T)$$

The force is conservative if and only if the material properties (ε(ω), μ(ω)) do not change during the process. If material properties are temperature-dependent and temperature changes during the cycle, the force may no longer derive from a single-valued potential.

### 1.2 Conditions for Conservativeness

The Casimir force is conservative under these conditions:
- **A1:** Fixed material response functions ε(ω) and μ(ω) — independent of plate separation and unchanged during the cycle
- **A2:** Quasi-static process — system in thermal equilibrium at each step
- **A3:** Fixed temperature T (isothermal process) — or if T varies, material response is T-independent
- **A4:** Fixed geometry class — parallel plates remain parallel (no tilting, no topology change)

**When conservativeness breaks down:**
- Material properties change with T and T varies during cycle
- Non-equilibrium (dynamic Casimir effect — plates move too fast for adiabatic following)
- Topology changes (creating/destroying a cavity)
- Boundary condition changes (switching between Dirichlet/Neumann/Robin)

### 1.3 Work in a Quasi-Static Cycle

For a closed cycle a₁ → a₂ → a₁ at fixed T with fixed materials:

$$W_{\text{net}} = \oint F(a, T) \, da = \int_{a_1}^{a_2} F(a, T) \, da + \int_{a_2}^{a_1} F(a, T) \, da = 0$$

This is exact when F = -∂F/∂a|_T is single-valued (conservative). The net work vanishes identically.

### 1.4 Energy Budget Components

For a quasi-static isothermal cycle at temperature T:

| Component | Definition | Sign convention |
|-----------|-----------|-----------------|
| W_close | Work done on plates during closing: W = ∫_{a_max}^{a_min} F(a) da | W_close > 0 if plates attract (F < 0, moving in direction of force) → work extracted |
| W_open | Work done on plates during opening: W = ∫_{a_min}^{a_max} F(a) da | W_open < 0 (must push against attractive force) → work input |
| W_net | W_close + W_open | = 0 for conservative force |
| ΔE_vac | Change in vacuum energy over cycle | = 0 for closed cycle |
| Q | Heat exchanged with reservoir (finite T) | = 0 for isothermal cycle with conservative force |

**Sign convention (from project conventions):**
- W_net > 0 would mean energy extracted (the no-go claim is W_net ≤ 0)
- F < 0 means attractive force
- Work done BY the Casimir force when plates close: W_close = -∫_{a_max}^{a_min} F(a) da = ∫_{a_min}^{a_max} (-F(a)) da > 0

**Careful sign tracking:**
Work done by external agent to move plates quasi-statically:
- W_ext = -F_Casimir · da (external force balances Casimir force)
- Closing (da < 0, F < 0): W_ext = -F·da = -(negative)(negative) < 0 → external agent receives energy
- Opening (da > 0, F < 0): W_ext = -F·da = -(negative)(positive) > 0 → external agent does work

Net work extracted by external agent = W_ext,close + W_ext,open = ∮(-F)da = -∮F da = 0

## 2. Computational Strategy

### 2.1 Available Code from Phase 02

The following validated functions are available in `.gpd/phases/02-casimir-force-computation-framework/`:

1. **casimir_ideal.py:**
   - `casimir_force_ideal(a)`: F/A = -π²/(240a⁴) in natural units
   - `casimir_energy_ideal(a)`: E/A = -π²/(720a³) in natural units

2. **lifshitz.py:**
   - `lifshitz_force(a, T, material_model)`: Full Lifshitz formula with Matsubara summation
   - `lifshitz_force_T0(a, material_model)`: T=0 Lifshitz with material corrections
   - Material models: `drude_epsilon(xi, omega_p, gamma)`, `plasma_epsilon(xi, omega_p)`
   - Reflection coefficients: `r_TE(kperp, xi, eps)`, `r_TM(kperp, xi, eps)`

### 2.2 Integration Strategy for Cycle Work

**Numerical quadrature for work integrals:**

W_close = ∫_{a_max}^{a_min} F(a, T) da (numerically: negative of ∫_{a_min}^{a_max})

Use scipy.integrate.quad with tight tolerances:
- epsabs = 1e-15, epsrel = 1e-14
- This gives W_net/|W_close| precision well below 10⁻¹⁰

**Verification strategy:**
1. Compute W_close and W_open separately
2. Verify W_net = W_close + W_open ≈ 0 to 10⁻¹⁰ relative precision
3. Cross-check: W_close = ΔE_vac = E(a_min) - E(a_max) (T=0 case)
4. At finite T: W_close = ΔF = F(a_min, T) - F(a_max, T)

### 2.3 Energy Budget Verification

**T = 0 case (simplest):**
- W_close = E_vac(a_min) - E_vac(a_max) = -∫_{a_max}^{a_min} F(a) da
- W_open = E_vac(a_max) - E_vac(a_min) = -∫_{a_min}^{a_max} F(a) da
- W_net = 0 (exact)
- ΔE_vac = 0 (cycle returns to initial state)
- Q = 0 (no thermal bath)
- Energy conservation: W_net = ΔE_vac + Q → 0 = 0 + 0 ✓

**Finite T case:**
- W = -∫ F da where F = -∂F/∂a|_T (Helmholtz free energy)
- Must integrate the Lifshitz force (includes thermal Matsubara contributions)
- Energy budget: W_net = ΔE_internal + Q where Q = TΔS (isothermal)
- For closed cycle: ΔE_internal = 0, ΔS = 0, Q = 0, W_net = 0

### 2.4 Numerical Precision Requirements

From the success criteria:
- Energy conservation: |W_net - (ΔE_vac + Q)| / |W_close| < 10⁻⁸
- Net work cancellation: |W_net| / |W_close| < 10⁻¹⁰

The second is more stringent. Achievable with:
- Gaussian quadrature (scipy.integrate.quad) with epsrel = 1e-14
- Or analytical integration for the T=0 ideal case (exact)

### 2.5 Test Configurations

| Config | a_min | a_max | T | Material | Expected W_net |
|--------|-------|-------|---|----------|----------------|
| 1 | 100 nm | 1 μm | 0 | Ideal | 0 (exact) |
| 2 | 100 nm | 1 μm | 300 K | Ideal | 0 |
| 3 | 100 nm | 1 μm | 300 K | Drude (Au) | 0 |
| 4 | 100 nm | 1 μm | 300 K | Plasma (Au) | 0 |
| 5 | 50 nm | 5 μm | 300 K | Drude (Au) | 0 |
| 6 | 200 nm | 2 μm | 77 K | Drude (Au) | 0 |

## 3. Key Literature

### 3.1 Essential References

1. **Casimir (1948)** — Original derivation of the Casimir effect for ideal conductors. Establishes E(a) = -π²ℏc A / (720 a³). [ref-casimir-1948]

2. **Lifshitz (1956)** — Generalization to real materials with frequency-dependent dielectric response. [ref-lifshitz-1956]

3. **Bordag, Klimchitskaya, Mohideen, Mostepanenko (2009)** — "Advances in the Casimir Effect" — comprehensive textbook treatment of Casimir thermodynamics, free energy, entropy. Chapter 5 covers the thermal Casimir effect systematically.

4. **Milonni (1994)** — "The Quantum Vacuum" — pedagogical treatment of the connection between vacuum energy, Casimir force, and thermodynamics.

5. **Ford (2010)** — "Casimir Effect" review, covers energy extraction impossibility arguments for the conservative case.

### 3.2 Relevant Physics

**Why conservative force → no energy extraction:**

The argument is thermodynamic and does not depend on the microscopic details:
1. For fixed material properties, F(a, T) is a state function (depends only on current separation and temperature)
2. F = -∂F/∂a|_T where F is a state function (Helmholtz free energy)
3. Therefore ∮ F da = 0 for any closed path in configuration space
4. W_net = 0 for any quasi-static cycle

This is the same argument that proves you cannot extract net energy from gravity by raising and lowering a mass — the gravitational force is conservative.

**The key distinction from Phase 01:**
Phase 01 proved the no-go theorem abstractly (assumptions A1-A5). Phase 03 demonstrates it concretely by computing the actual numbers for specific cycles, using the validated Phase 02 code. The numerical verification (W_net/|W_close| < 10⁻¹⁰) provides a computational cross-check of the analytical proof.

## 4. Limiting Cases

### 4.1 T = 0 Ideal Plates (Analytical)

W_close = E(a_min) - E(a_max) = -π²/(720) · (1/a_min³ - 1/a_max³) per unit area

This can be computed exactly — no numerical integration needed. W_net = 0 is exact.

### 4.2 High-T Classical Limit

F(a, T) → -ζ(3) T / (4πa³) per unit area for ideal conductor
F(a, T) → -ζ(3) T / (8πa³) per unit area for Drude model

Both are conservative: F = -∂/∂a [-ζ(3)T/(8πa²)] etc.

### 4.3 Large Separation (a → ∞)

F → 0, so W_close → 0 as a_max → ∞. Consistent with E(∞) = 0 as reference.

## 5. Dimensional Analysis

**Work integral:** [W/A] = [F/A] × [a] = [energy/length³] × [length] = [energy/length²] ✓ (energy per unit area)

In natural units (ℏ = c = k_B = 1):
- [F/A] = [length⁻⁴] → [W/A] = [length⁻³] (same dimension as E/A) ✓
- W_close = ΔE = E(a_min) - E(a_max), both have dimension [length⁻³] ✓

**At finite T:**
- [T] = [length⁻¹] in natural units
- [F/A] at high T: [T/a³] = [length⁻¹ · length⁻³] = [length⁻⁴] ✓

## 6. Potential Difficulties

1. **Numerical precision at finite T:** The Matsubara sum may introduce numerical noise. Use high-precision quadrature and verify with analytical expressions where available.

2. **Sign conventions:** Must be extremely careful with signs. The work done BY the Casimir force vs. work done ON the system have opposite signs. Our convention: W_net > 0 means extraction.

3. **Drude model at high T:** The l=0 TE mode issue (Drude gives zero, plasma gives finite) affects the absolute force but not the conservativeness argument. Both models give W_net = 0 for a cycle.

4. **Energy vs. free energy:** At T=0, energy and free energy coincide. At finite T, must use free energy F = E - TS for isothermal work calculations.

## 7. Plan Structure Recommendation

**Plan 03-01: Conservative Force Proof + T=0 Cycle (Wave 1)**
- Formal proof: F = -∂V/∂a, state conditions
- T=0 ideal cycle: analytical W_net = 0
- T=0 numerical cycle: verify with quadrature
- 4-5 tasks

**Plan 03-02: Finite-T Energy Budget + Full Verification (Wave 2)**
- Finite-T Lifshitz cycle for Drude and plasma models
- Complete energy budget: W_close, W_open, W_net, ΔE, Q
- Energy conservation verification to < 10⁻⁸
- Multiple test configurations
- 4-5 tasks

This split allows Plan 01 to be purely analytical + simple numerics, while Plan 02 handles the more complex finite-T thermodynamics.

## RESEARCH COMPLETE
