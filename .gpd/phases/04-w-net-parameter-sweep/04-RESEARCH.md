# Phase 04 Research: W_net Parameter Sweep

## 1. Phase Objective

Map W_net over the full (a_min, a_max, T) parameter space — 500k grid points — confirming W_net = 0 everywhere for the conservative-force case (fixed material properties) and producing the definitive parameter sweep figure.

## 2. Mathematical Framework

### 2.1 Core Quantity

For each grid point (a_min, a_max, T), compute:

$$W_\text{net}(a_\text{min}, a_\text{max}, T) = \oint F(a, T) \, da = 0$$

This vanishes identically because F(a, T) is conservative (depends on position alone, not on direction of travel). The key numerical diagnostic is:

$$\eta(a_\text{min}, a_\text{max}, T) = \frac{|W_\text{net}|}{|W_\text{close}|}$$

which must satisfy η < 10⁻¹⁰ at every grid point.

### 2.2 Functions Available from Phase 03

From `code/casimir_cycle.py`:
- `cycle_work_ideal_analytical(a_min, a_max)` — T=0 ideal plates, exact
- `cycle_work_ideal_numerical(a_min, a_max)` — T=0 ideal plates, quad integration
- `cycle_work_lifshitz(a_min, a_max, T, epsilon_func, material_type, omega_p, gamma)` — finite-T with realistic materials, single-integral (exploits W_open = -W_close)
- `cycle_work_lifshitz_double_integral(...)` — independent double integration for genuine numerical test
- `energy_budget(...)` — energy conservation check

For the sweep, `cycle_work_lifshitz` is the workhorse (exploits conservative force structure). The `_double_integral` variant is 2x slower but provides independent verification.

### 2.3 Why W_net = 0 Exactly

Phase 03 proved: for fixed material properties (conditions A1-A4), F = -dV/da where V depends only on separation a. Therefore:

$$W_\text{net} = \oint_{a_\text{max} \to a_\text{min} \to a_\text{max}} F(a) \, da = V(a_\text{max}) - V(a_\text{min}) + V(a_\text{min}) - V(a_\text{max}) = 0$$

The sweep confirms this algebraic identity holds across the entire parameter space without numerical artifacts.

## 3. Parameter Space Design

### 3.1 Grid Specification (from R2.3)

| Parameter | Range | Points | Scale |
|-----------|-------|--------|-------|
| a_min | [10 nm, 1 μm] | 100 | Logarithmic |
| a_max | [100 nm, 10 μm] | 100 | Logarithmic |
| T | [0, 300 K] | 50 | Linear (with T=0 as first point) |

Total: 100 × 100 × 50 = 500,000 grid points.

### 3.2 Physical Constraints

**Constraint:** a_min < a_max must hold at every grid point. The grid should be generated such that only valid (a_min, a_max) pairs with a_min < a_max are computed. With logarithmic spacing, roughly half the 100×100 grid has a_min < a_max (upper triangular in log-log space). This gives ~5000 × 50 = ~250k valid points for each material case.

**Alternative:** Parameterize as (a_min, ratio = a_max/a_min) with ratio > 1. This avoids invalid pairs but changes the grid geometry.

**Recommendation:** Keep (a_min, a_max) grid with masking. The triangular structure is itself informative for visualization — the boundary a_min = a_max is where W_close → 0.

### 3.3 Unit Conversion

All code uses natural units (ℏ = c = k_B = 1):
- Separations in meters: a [m]
- Temperature: T [K] → T_nat = k_B T / (ℏc) [m⁻¹], with k_B = 8.617e-5 eV/K and ℏc = 197.3e-9 eV·m → k_B/(ℏc) = 4.367e5 K⁻¹m⁻¹ → T_nat = T × 4.367e-5 m⁻¹ ???

Let me be precise: k_B T in eV = T × 8.617e-5, then convert to m⁻¹ via ÷(ℏc in eV·m) = ÷(197.3e-9). So T_nat = T × 8.617e-5 / 197.3e-9 = T × 436.7 m⁻¹/K.

At T = 300 K: T_nat = 300 × 436.7 = 1.310e5 m⁻¹.

The thermal wavelength λ_T = 1/T_nat = 7.63 μm at 300 K. This is an important scale: when a ≫ λ_T, thermal corrections dominate; when a ≪ λ_T, quantum (T=0) contributions dominate.

### 3.4 Relevant Physical Scales

| Scale | Value | Significance |
|-------|-------|-------------|
| λ_T(300K) | 7.63 μm | Thermal wavelength |
| c/ω_p (gold) | 22 nm | Plasma skin depth |
| c/γ (gold) | 5.63 μm | Dissipation length |
| a_min range | 10 nm – 1 μm | Spans from sub-plasma to thermal crossover |
| a_max range | 100 nm – 10 μm | Spans from quantum to thermal regime |

## 4. Computational Strategy

### 4.1 Performance Estimate

Each Lifshitz force evaluation requires:
- Matsubara sum over l = 0, 1, ..., l_max terms (l_max depends on T and a)
- For each l: numerical integration over k_perp
- Typical cost: ~1-10 ms per force evaluation

Each cycle_work_lifshitz call requires ~20-50 force evaluations (quad adaptive).
At 500k points: 500k × 50 ms = ~25,000 s = ~7 hours for sequential execution.

**Parallelization strategy:** Use `multiprocessing.Pool` or `concurrent.futures.ProcessPoolExecutor` to distribute grid points across CPU cores. With 4 cores: ~1.75 hours. With NumPy vectorization of the inner loop: potentially faster.

### 4.2 Recommended Approach

1. **Coarse sweep first** (20 × 20 × 10 = 4000 points): Validate code, check for anomalies, estimate runtime
2. **Full sweep** (100 × 100 × 50): Production run with parallelization
3. **Spot-check with double_integral**: At ~100 randomly selected points, use the independent double-integral method to verify η < 10⁻¹⁰

### 4.3 Memory Requirements

Storing results for 500k points:
- W_close, W_open, W_net, η: 4 floats × 8 bytes × 500k = 16 MB per material case
- Total for 3 cases (ideal, Drude, plasma): ~48 MB — fits easily in memory

### 4.4 Handling T = 0

The T = 0 case requires special treatment in the Lifshitz code:
- Matsubara sum becomes integral over continuous imaginary frequency
- The `lifshitz_force` function should handle T = 0 via the appropriate limit
- For ideal plates at T = 0, use the exact analytical formula as ground truth

Check: Does the existing `lifshitz_force` function handle T = 0? From Phase 02 results, it was tested at T = 0 for perfect conductor. Need to verify it also works for T = 0 with Drude/plasma models, or if a small T (e.g., T = 0.01 K) should be used as a proxy.

## 5. Visualization Strategy

### 5.1 Primary Figure: deliv-param-sweep

For each material case, produce a 2D heatmap at selected T slices:
- **x-axis:** log10(a_min) [nm to μm]
- **y-axis:** log10(a_max) [nm to μm]
- **color:** log10(η) = log10(|W_net|/|W_close|)
- White/masked region where a_min ≥ a_max

Selected T values: T = 0, 77, 150, 300 K (4 slices per material case).

### 5.2 Secondary Figures

1. **W_close landscape:** log10(|W_close|) vs (a_min, a_max) — shows the scale of the work being done
2. **η vs T at fixed separations:** Line plots for selected (a_min, a_max) pairs showing η is uniformly small
3. **Max η per T slice:** Summary plot of max(η) vs T for each material case

### 5.3 matplotlib Configuration

Use matplotlib with:
- `pcolormesh` for 2D heatmaps
- `colorbar` with log scale
- Consistent color maps (e.g., `viridis` for W_close, `RdYlGn_r` for η with red = worse)
- Publication-quality font sizes and labels

## 6. Numerical Pitfalls and Mitigations

### 6.1 Small Separation Regime (a_min → 10 nm)

At very small separations:
- Casimir force is very large: F/A ~ a⁻⁴
- W_close is large, providing a stable denominator for η
- But the Lifshitz integrand can have sharp features requiring fine quadrature
- **Mitigation:** Use `limit=200` in quad for small separations

### 6.2 Large Separation Regime (a_max → 10 μm)

At large separations:
- Force is very small (falls off as a⁻⁴ or faster at finite T)
- W_close → 0 as a_min → a_max, making η = |W_net|/|W_close| numerically unstable
- **Mitigation:** When a_max/a_min < 1.1, η is unreliable; report absolute |W_net| instead

### 6.3 Thermal Crossover (a ~ λ_T)

At the thermal crossover (a ~ 7.63 μm at 300K):
- Matsubara sum convergence changes character
- Drude-plasma discrepancy is most pronounced
- **Mitigation:** Increase l_max for large a × T products

### 6.4 Drude l=0 TE Anomaly

The Drude model gives r_TE(l=0) = 0, while plasma gives r_TE(l=0) ≠ 0. This is a well-known controversy. Both models should give W_net = 0 (conservative force holds for both), but the absolute values of W_close differ. The sweep should confirm W_net = 0 independently for each model.

## 7. Literature Context

Key references for parameter sweep design:
1. **Bordag et al. (2009)** — Comprehensive reference for Lifshitz formula numerics
2. **Lambrecht & Reynaud (2000)** — Computational approach to Casimir force evaluation
3. **Klimchitskaya et al. (2009)** — Review of Casimir force experiments with Drude/plasma comparison
4. **Decca et al. (2003, 2005)** — Experimental Casimir force measurements providing benchmark values
5. **Genet et al. (2003)** — Thermal Casimir force computation methodology

## 8. Dimensional Analysis

All quantities per unit area:
- [W/A] = [F/A] × [length] = length⁻⁴ × length = length⁻³
- [η] = dimensionless
- [T_nat] = length⁻¹
- [a] = length

The diagnostic η = |W_net|/|W_close| is dimensionless by construction. ✓

## 9. Expected Outcomes

1. **η < 10⁻¹⁰ everywhere** — confirms conservative force structure across all parameter space
2. **W_close varies over many orders of magnitude** — from ~10⁻³ length⁻³ at large separations to ~10⁸ length⁻³ at small separations (in SI, from pJ/m² to GJ/m²)
3. **Drude-plasma discrepancy in W_close** — expected ~2-90% depending on regime, but both give W_net = 0
4. **No sign anomalies** — W_close > 0 everywhere (attractive force does positive work closing), W_net = 0 everywhere
5. **Smooth η landscape** — no unexpected structure, confirming this is an algebraic identity, not a numerical accident

## 10. Recommended Plan Structure

**Plan 01 (Wave 1):** Implement parameter sweep infrastructure
- Grid generation with constraint masking
- Parallelized sweep function
- Result storage (numpy arrays or HDF5)
- Coarse sweep validation (4000 points)

**Plan 02 (Wave 2):** Production sweep + visualization
- Full 500k-point sweep for ideal, Drude, plasma
- Generate all figures (heatmaps, line plots, summary)
- Spot-check with double_integral at ~100 points
- Compile results table and analysis

## RESEARCH COMPLETE
