# No-Go Arguments: Assumption Comparison Table

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, regularization_scheme=zeta, casimir_force_sign=F<0_attractive, casimir_energy_sign=E<0_bounded, work_sign=W_net>0_extraction

## Comparison Table

| Argument | Key Assumptions | What It Proves | Known Loopholes | Strength Rating |
|----------|----------------|----------------|-----------------|-----------------|
| **A: Thermodynamic (Second Law)** | **A1:** Closed system (no external energy source). **A2:** Casimir force $F_{\text{Cas}}(a)$ is conservative (depends only on separation $a$). **A3:** Fixed material properties throughout cycle. **A4:** Second law (Kelvin--Planck) holds at $T=0$. **A5:** Cyclic process (system returns to initial state). | **Quasi-static:** $W_{\text{net}} = \oint F_{\text{Cas}}\,da = 0$ (conservative force, closed path integral vanishes). **General:** $W_{\text{net}} \leq 0$ for any cyclic process (Kelvin--Planck at $T=0$ forbids $W_{\text{net}} > 0$). [Eqs. (A.6), (A.9)] | **A3 violated:** Material property changes mid-cycle (Pinto's conductivity-switching proposal). **A2 violated:** Hysteresis from irreversible material changes makes force non-conservative. **A1 violated:** External energy input (laser, battery). **A5 violated:** One-shot (non-cyclic) energy release. | **MODERATE** --- Robust for equilibrium cycles with fixed materials. Directly addresses the Casimir engine scenario. Limited by reliance on equilibrium thermodynamics; does not cover non-equilibrium or material-switching regimes. |
| **B: Lorentz Invariance** | **B1:** Vacuum $\lvert 0\rangle$ is Poincare-invariant. **B2:** Minkowski space with no boundaries or external fields. **B3:** Renormalized $\langle 0\lvert T^{\mu\nu}\rvert 0\rangle$ is well-defined, finite, and Lorentz-covariant. **B4:** Local Poincare-covariant QFT (Wightman axioms). | $\langle 0\lvert T^{\mu\nu}\rvert 0\rangle = \rho_{\text{vac}}\,g^{\mu\nu}$, implying the vacuum equation of state $p_{\text{vac}} = -\rho_{\text{vac}}$. For a $p = -\rho$ medium, $dU + \delta W = 0$ identically, so $W_{\text{net}} = 0$ for any volume change process. [Eqs. (B.10), (B.16)] | **B2 violated:** Boundaries break translational/Lorentz invariance --- this is precisely the Casimir configuration. Between plates, $\langle T^{\mu\nu}\rangle$ is anisotropic and position-dependent, NOT proportional to $g^{\mu\nu}$. **B1 violated:** Non-trivial backgrounds (curved spacetime, external fields). | **WEAK for Casimir** --- Elegant and fundamental, but fails for bounded systems (B2), which is the entire Casimir scenario. Provides conceptual insight into WHY vacuum energy exists near boundaries (mode structure modification), but does not constrain the bounded case. |
| **C: Passivity (Pusz--Woronowicz)** | **C1:** Time-independent Hamiltonian $H$ throughout operation. **C2:** Cyclic process ($H(t_f) = H(t_i)$). **C3:** Non-degenerate ground state. **C4:** Quantum mechanical framework (self-adjoint $H$, unitary evolution). **C5:** Same Hilbert space (no degrees of freedom added/removed). | Ground state $\lvert 0\rangle$ is passive: $\Delta E = \mathrm{Tr}(U\rho_{\text{vac}}U^\dagger H) - \mathrm{Tr}(\rho_{\text{vac}} H) \geq 0$ for ALL unitaries $U$. Ergotropy $\mathcal{W}(\rho_{\text{vac}}, H) = 0$. Complete passivity: even $N$ copies cannot be exploited. Hence $W_{\text{net}} \leq 0$. [Eqs. (C.4), (C.14), (C.19)] | **C1 violated:** Time-dependent $H$ (moving Casimir plates make $H = H(a(t))$). In the adiabatic limit, the system tracks the ground state and $W_{\text{net}} = 0$; in the non-adiabatic limit (dynamic Casimir effect), real photons are produced but their energy comes from mechanical work, not vacuum energy. **C3 violated:** Degenerate ground state (unusual but possible in systems with symmetry). | **STRONG** --- Mathematically rigorous, covers ALL cyclic unitaries (not just quasi-static), and extends to complete passivity (multi-copy). The proof is elementary (spectral bound + unitarity). Main limitation: requires fixed $H$, which excludes the physically relevant moving-plate scenario. |

## Strength Ranking Summary

1. **Passivity (C)** --- STRONG. Mathematically most rigorous. Covers the broadest class of cyclic operations (all unitaries, not just quasi-static). Complete passivity rules out multi-copy schemes.

2. **Thermodynamic (A)** --- MODERATE. Most practically relevant to the Casimir engine question. Directly addresses plate-based cycles. Limited to equilibrium with fixed materials.

3. **Lorentz Invariance (B)** --- WEAK (for Casimir). Elegant and fundamental for understanding the free vacuum, but inapplicable to bounded systems. The Casimir effect exists precisely because B2 is violated.

## Assumption Count and Coverage

| Argument | Assumption Count | Scope | Applicability to Casimir |
|----------|-----------------|-------|--------------------------|
| A | 5 (A1--A5) | Thermodynamic cycles with Casimir plates | Direct --- addresses the engine scenario |
| B | 4 (B1--B4) | Free (unbounded) Lorentz-invariant vacuum | Indirect --- inapplicable when plates present |
| C | 5 (C1--C5) | Any quantum system with fixed Hamiltonian | Conditional --- applies only if plates are stationary |

**Total distinct assumptions:** 14 (some with semantic overlap, analyzed in nogo-consistency-analysis.md).
