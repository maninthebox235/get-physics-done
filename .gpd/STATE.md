# Research State

## Project Reference

See: .gpd/PROJECT.md

**Core research question:** Can zero-point energy of the quantum vacuum be extracted as usable work through cyclic processes involving boundary condition changes?
**Current focus:** Phase 01 complete; ready for Phase 02

## Current Position

**Current Phase:** 01 (complete)
**Current Phase Name:** No-Go Theorem Derivations
**Total Phases:** 7
**Current Plan:** 2/2 complete
**Total Plans in Phase:** 2
**Status:** Phase complete ✓
**Last Activity:** Phase 01 execution — all plans passed verification

**Progress:** [█░░░░░░░░░] 14%

## Active Calculations

None (Phase 01 was purely analytical).

## Intermediate Results

- **Thermodynamic no-go:** W_net ≤ 0 for cyclic processes at equilibrium with conservative Casimir force (assumptions A1-A5)
- **Lorentz invariance no-go:** ⟨0|T^μν|0⟩ = ρ_vac g^μν — uniform vacuum energy, no extractable gradient (assumptions B1-B4); boundaries break B2
- **Passivity no-go:** Ground state passive under cyclic unitaries for fixed H: ⟨ψ₀|U†HU|ψ₀⟩ ≥ E₀ (assumptions C1-C5); time-dependent H evades C1
- **Cross-verification:** 3 arguments dimensionally consistent, logically independent, mutually non-contradictory
- **Consistency analysis:** 65 assumption pairs checked, 0 contradictions, 3 informative tensions
- **Coverage gap:** Time-dependent H + boundaries + material changes = dynamic Casimir regime
- **Logical hierarchy:** Passivity (C) ⇒ Thermodynamic (A) ← Lorentz (B)

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

## Accumulated Context

### Decisions

- Used elementary proof of ground state passivity rather than full C*-algebraic Pusz-Woronowicz proof
- Used Weinberg QFT Vol 1 §11.2 approach for Lorentz invariance argument
- Extended comparison table from 5 to 7 columns for richer traceability

### Active Approximations

None (all Phase 01 arguments are exact).

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
**Stopped at:** Phase 01 complete, ready for Phase 02
**Resume file:** .gpd/phases/01-no-go-theorem-derivations/01-VERIFICATION.md
