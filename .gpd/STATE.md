# Research State

## Project Reference

See: .gpd/PROJECT.md

**Core research question:** Can zero-point energy of the quantum vacuum be extracted as usable work through cyclic processes involving boundary condition changes?
**Current focus:** Phase 02 complete; ready for Phase 03

## Current Position

**Current Phase:** 02 (complete)
**Current Phase Name:** Casimir Force Computation Framework
**Total Phases:** 7
**Current Plan:** 3/3 complete
**Total Plans in Phase:** 3
**Status:** Phase complete ✓
**Last Activity:** Phase 02 execution — all plans passed verification (5/5 contract targets, 23/23 tests)

**Progress:** [██░░░░░░░░] 29%

## Active Calculations

None (all Phase 02 code validated and tested).

## Intermediate Results

### Phase 01 (No-Go Theorems)

- **Thermodynamic no-go:** W_net ≤ 0 for cyclic processes at equilibrium with conservative Casimir force (assumptions A1-A5)
- **Lorentz invariance no-go:** ⟨0|T^μν|0⟩ = ρ_vac g^μν — uniform vacuum energy, no extractable gradient (assumptions B1-B4); boundaries break B2
- **Passivity no-go:** Ground state passive under cyclic unitaries for fixed H: ⟨ψ₀|U†HU|ψ₀⟩ ≥ E₀ (assumptions C1-C5); time-dependent H evades C1
- **Logical hierarchy:** Passivity (C) ⇒ Thermodynamic (A) ← Lorentz (B)

### Phase 02 (Casimir Force Computation)

- **Ideal Casimir force:** F/A = -π²/(240a⁴) verified by 3 independent methods (analytical, zeta-regularized, Abel-Plana) to relative error < 10⁻¹⁶
- **Lifshitz formula:** Implemented with Drude and plasma material models, Matsubara summation, TE/TM reflection coefficients
- **T=0 perfect conductor via Lifshitz:** Matches ideal result to 1.87e-13 relative error
- **Drude gold T=300K:** η = F_Drude/F_ideal ranges from 0.43 (100nm) to 0.79 (5μm)
- **Drude-plasma discrepancy:** 2.1% at 100nm growing to 94% at 5μm (l=0 TE mode)
- **Limiting cases:** All 5 verified (T→0, a→∞, ε→∞, γ→0, high-T classical)
- **High-T classical:** -Tζ(3)/(4πa³) for perfect conductor; -Tζ(3)/(8πa³) for Drude (TM only)
- **Bug fixed:** Jacobian in lifshitz_force_T0 material branch corrected

## Open Questions

- Which reference is the definitive formulation of the passivity theorem for QFT vacuum states?
- What is the correct energy accounting for the dynamic Casimir effect — is photon production from vacuum genuinely 'extraction'?
- Whether topology changes (creating/removing a cavity) constitute a distinct loophole or reduce to boundary condition changes
- Exact scope of Pusz-Woronowicz passivity in QFT with boundaries (open mathematical question)

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| Phase 01, Plan 01 | ~20 min | 4 | 4 |
| Phase 01, Plan 02 | ~15 min | 3 | 2 |
| Phase 02, Plan 01 | ~6 min | 2 | 4 |
| Phase 02, Plan 02 | ~15 min | 2 | 5 |
| Phase 02, Plan 03 | ~13 min | 2 | 4 |

## Accumulated Context

### Decisions

- Used elementary proof of ground state passivity rather than full C*-algebraic Pusz-Woronowicz proof
- Used Weinberg QFT Vol 1 §11.2 approach for Lorentz invariance argument
- Extended comparison table from 5 to 7 columns for richer traceability
- Used Abel-Plana formula instead of exponential regulator for numerical cross-check (better stability)
- l=0 reflection coefficients as separate special-case functions (avoids 0/0 indeterminate)
- High-T classical limit: -Tζ(3)/(4πa³) for perfect conductor, -Tζ(3)/(8πa³) for Drude

### Active Approximations

- Drude model: ε_D(iξ) = 1 + ω_p²/(ξ(ξ+γ)) — valid for metals with dissipation below interband transitions
- Plasma model: ε_P(iξ) = 1 + ω_p²/ξ² — dissipationless limit
- Matsubara truncation: l_max such that |f(l_max)| < 10⁻¹² |f(0)| — exponential convergence at finite T

**Convention Lock:**

- Metric signature: mostly-minus
- Fourier convention: physics
- Natural units: natural
- Regularization scheme: zeta

*Custom conventions:*
- Casimir Force Sign: F < 0 for attractive (plates pulled together)
- Casimir Energy Sign: E < 0 for bound configuration lower than unbounded
- Matsubara Prime Sum: l=0 term carries half weight in primed sum notation
- Work Sign: W_net > 0 means net energy extracted by the system; W_net <= 0 is the no-go claim

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

None

## Session Continuity

**Last session:** 2026-03-22
**Stopped at:** Phase 02 complete, ready for Phase 03
**Resume file:** .gpd/phases/02-casimir-force-computation-framework/02-VERIFICATION.md
