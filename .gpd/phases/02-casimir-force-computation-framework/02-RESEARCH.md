# Phase 02 Research: Casimir Force Computation Framework

## 1. Mathematical Framework

### 1.1 Ideal Plates at T=0

The exact Casimir force per unit area between two perfectly conducting parallel plates separated by distance $a$ at zero temperature:

$$F/A = -\frac{\pi^2 \hbar c}{240 a^4} = -\frac{\pi^2}{240 a^4} \quad \text{(natural units)}$$

Derivation: mode summation with zeta function regularization, or equivalently via the Euler-Maclaurin formula applied to the vacuum energy density.

The Casimir energy per unit area:

$$E/A = -\frac{\pi^2}{720 a^3}$$

with $F/A = -\partial(E/A)/\partial a$.

### 1.2 Lifshitz Formula (General Framework)

The Lifshitz formula at imaginary (Matsubara) frequencies provides the unified framework for arbitrary materials and finite temperature:

$$F/A = -\frac{k_B T}{\pi} \sideset{}{'}\sum_{l=0}^{\infty} \int_0^\infty k_\perp \, dk_\perp \, \kappa_0 \sum_{P=\text{TE,TM}} \frac{r_P^2 \, e^{-2\kappa_0 a}}{1 - r_P^2 \, e^{-2\kappa_0 a}}$$

where:
- $\xi_l = 2\pi l k_B T / \hbar$ are Matsubara frequencies ($\xi_l = 2\pi l T$ in natural units)
- Prime on sum: $l=0$ term has half weight (matches our Matsubara prime sum convention)
- $\kappa_0 = \sqrt{k_\perp^2 + \xi_l^2}$ (vacuum wavevector)
- $\kappa = \sqrt{k_\perp^2 + \varepsilon(i\xi_l) \xi_l^2}$ (material wavevector)

Reflection coefficients for a semi-infinite dielectric slab:
- TE: $r_{\text{TE}} = \frac{\kappa_0 - \kappa}{\kappa_0 + \kappa}$
- TM: $r_{\text{TM}} = \frac{\varepsilon(i\xi_l)\kappa_0 - \kappa}{\varepsilon(i\xi_l)\kappa_0 + \kappa}$

### 1.3 Matsubara Sum Structure

For $T > 0$: sum over discrete $l = 0, 1, 2, \ldots$ with exponential convergence.

For $T = 0$: sum becomes integral via $k_B T \sum_l' \to \frac{\hbar}{2\pi} \int_0^\infty d\xi$.

The Abel-Plana formula connects these:
$$\sum_{l=0}^{\infty}{}' f(l) = \int_0^\infty f(t) \, dt + i \int_0^\infty \frac{f(it) - f(-it)}{e^{2\pi t} - 1} \, dt$$

## 2. Material Models

### 2.1 Drude Model

$$\varepsilon_D(i\xi) = 1 + \frac{\omega_p^2}{\xi(\xi + \gamma)}$$

Parameters for gold: $\omega_p = 9.0$ eV, $\gamma = 0.035$ eV.

**Critical l=0 behavior:**
- TE mode: $r_{\text{TE}}(l=0) \to 0$ as $\xi \to 0$ (because $\kappa \to \kappa_0$ when only dissipation drives $\varepsilon - 1$)
- TM mode: $r_{\text{TM}}(l=0) \to 1$ (metallic screening)

This is the origin of the Drude-plasma controversy: the TE contribution at $l=0$ vanishes for Drude but not for plasma.

### 2.2 Plasma Model

$$\varepsilon_P(i\xi) = 1 + \frac{\omega_p^2}{\xi^2}$$

**l=0 behavior:**
- TE mode: $r_{\text{TE}}(l=0) = \frac{\kappa_0 - \sqrt{\kappa_0^2 + \omega_p^2}}{\kappa_0 + \sqrt{\kappa_0^2 + \omega_p^2}} \neq 0$
- TM mode: $r_{\text{TM}}(l=0) \to 1$

### 2.3 Perfect Conductor Limit

$\varepsilon \to \infty$: both $r_{\text{TE}} \to -1$ and $r_{\text{TM}} \to 1$ (in magnitude). The Lifshitz formula reduces to the Casimir result at $T = 0$.

## 3. Benchmark Data

### 3.1 Primary Benchmarks

| Benchmark | Source | Target Precision |
|-----------|--------|-----------------|
| Ideal plates T=0 | Casimir (1948) | $< 10^{-6}$ relative error |
| Drude at T=300K | Bordag et al. (2009) Ch. 12-14 | Match tabulated values |
| Plasma at T=300K | Bordag et al. (2009) Ch. 12-14 | Match tabulated values |

### 3.2 Bordag et al. (2009) Reference Values

The book "Advances in the Casimir Effect" (Bordag, Klimchitskaya, Mohideen, Mostepanenko) contains:
- Table 12.3+: Lifshitz formula values for gold (Drude and plasma) at various separations
- Thermal correction ratios $\eta(a,T) = F(a,T)/F_{\text{Casimir}}(a)$
- Comparison between Drude and plasma predictions

Typical separation range: $a = 100$ nm to $10$ μm at $T = 300$ K.

### 3.3 Additional Cross-Checks

- Lambrecht & Reynaud (2000): Detailed numerical Casimir results for real metals
- Klimchitskaya, Mohideen, Mostepanenko (2009): Review with experimental comparison
- Thermal crossover: at $a_T = \hbar c / (2k_B T) \approx 3.8$ μm at room temperature

## 4. Computational Methods

### 4.1 Implementation Strategy

**Three-tier approach:**

1. **Tier 1 (T=0 ideal):** Analytical formula. Verify numerically via direct mode summation with zeta regularization. Use mpmath for arbitrary precision to achieve $< 10^{-6}$.

2. **Tier 2 (Finite-T ideal):** Matsubara sum with $r_P = \pm 1$ (perfect conductor). Sum truncated at $l_{\max}$ where contribution $< \varepsilon_{\text{target}}$. Verify T→0 limit recovers Tier 1.

3. **Tier 3 (Finite-T realistic):** Full Lifshitz with Drude/plasma $\varepsilon(i\xi)$. Same Matsubara sum structure. Verify ε→∞ limit recovers Tier 2.

### 4.2 Numerical Libraries

- **mpmath:** Arbitrary precision arithmetic for the ideal plate benchmark
- **scipy.integrate:** Numerical integration over $k_\perp$ (Gaussian quadrature)
- **numpy:** Vectorized Matsubara sum evaluation
- **Python 3:** Primary implementation language

### 4.3 Convergence Control

- Matsubara sum: exponential convergence for $T > 0$; truncate at $l_{\max}$ where $|f(l_{\max})| < 10^{-12} |f(0)|$
- $k_\perp$ integration: substitute $u = k_\perp a$ for dimensionless variable; integrand decays exponentially
- For T=0 (continuous integral): use adaptive quadrature with relative tolerance $10^{-10}$

### 4.4 Known Pitfalls

1. **l=0 term:** Must use half-weight convention consistently (primed sum notation)
2. **Drude l=0 TE:** The limit $\xi \to 0$ of $r_{\text{TE}}$ requires careful analysis; intermediate expressions can be indeterminate
3. **Dimensional consistency:** In natural units, $[F/A] = [\text{energy}/\text{length}^4] = [\text{length}^{-4}]$
4. **Sign conventions:** $F < 0$ for attractive (our convention); some references use $|F|$
5. **Large separations:** Thermal effects dominate; force transitions from $a^{-4}$ (quantum) to $a^{-3}$ (thermal) behavior

## 5. Limiting Cases

| Limit | Expected Result | Derivation |
|-------|----------------|------------|
| $T \to 0$ | $F/A \to -\pi^2/(240a^4)$ | Sum → integral; standard Casimir |
| $a \to \infty$ | $F/A \to 0$ | Exponential suppression in Matsubara sum |
| $\varepsilon \to \infty$ | Lifshitz → Casimir | $r_P \to \pm 1$; perfect conductor |
| $a \gg \lambda_T$ (high T) | $F/A \to -k_B T \zeta(3)/(8\pi a^3)$ | Only $l=0$ term survives |
| $\gamma \to 0$ (in Drude) | Drude → Plasma | Dissipation vanishes |

## 6. Dimensional Analysis

In natural units ($\hbar = c = k_B = 1$):
- $[a] = \text{length}$
- $[T] = \text{energy} = \text{length}^{-1}$
- $[F/A] = \text{force}/\text{area} = \text{energy}/\text{length}^3 = \text{length}^{-4}$
- $[\omega_p] = [\gamma] = \text{energy} = \text{length}^{-1}$
- The dimensionless combination governing thermal effects: $aT$ (or equivalently $a/\lambda_T$ where $\lambda_T = 1/(2\pi T)$)

## 7. Recommended Plan Structure

1. **Plan 1 (Wave 1):** Implement ideal plate T=0 computation + verify to $10^{-6}$
2. **Plan 2 (Wave 1, parallel):** Implement Lifshitz formula infrastructure with general reflection coefficients
3. **Plan 3 (Wave 2):** Benchmark against Drude and plasma models using Bordag et al. (2009) data; verify all limiting cases

## 8. Key References

1. Casimir, H.B.G. (1948). "On the attraction between two perfectly conducting plates." Proc. Kon. Ned. Akad. Wet. 51, 793.
2. Lifshitz, E.M. (1956). "The theory of molecular attractive forces between solids." Sov. Phys. JETP 2, 73.
3. Bordag, M., Klimchitskaya, G.L., Mohideen, U., Mostepanenko, V.M. (2009). "Advances in the Casimir Effect." Oxford University Press.
4. Lambrecht, A. & Reynaud, S. (2000). "Casimir force between metallic mirrors." Eur. Phys. J. D 8, 309.
5. Klimchitskaya, G.L., Mohideen, U., Mostepanenko, V.M. (2009). "The Casimir force between real materials: Experiment and theory." Rev. Mod. Phys. 81, 1827.
