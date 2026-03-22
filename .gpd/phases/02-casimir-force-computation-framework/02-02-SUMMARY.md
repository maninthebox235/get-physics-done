---
phase: 02-casimir-force-computation-framework
plan: 02
depth: full
one-liner: "Implemented Lifshitz formula framework with Drude/plasma material models, validated against exact Casimir result to 13 digits and all structural tests passing"
subsystem: numerics
tags: [casimir, lifshitz, drude, plasma, matsubara, reflection-coefficients]

requires:
  - phase: 01-no-go-theorem-derivations
    provides: [convention lock, sign conventions for F and E]
provides:
  - Lifshitz formula implementation (finite T and T=0)
  - Drude and plasma dielectric response functions
  - Fresnel reflection coefficients with l=0 special cases
  - Gold material parameters in natural units
  - Structural test suite for Casimir force infrastructure
affects: [02-casimir-force-computation-framework, 03-cycle-energy-analysis]

methods:
  added: [Matsubara frequency summation, Fresnel reflection coefficients, numerical quadrature (scipy.integrate)]
  patterns: [primed Matsubara sum with l=0 half weight, l=0 special case handling for Drude vs plasma]

key-files:
  created:
    - code/material_models.py
    - code/casimir_lifshitz.py
    - code/tests/test_lifshitz_structure.py

key-decisions:
  - "l=0 reflection coefficients implemented as separate special-case functions rather than limits of general formula (avoids 0/0 indeterminate forms)"
  - "Added vacuum and perfect conductor material_type branches for l=0 integrand (deviation Rule 4: missing component for vacuum test)"

patterns-established:
  - "Material models return callable epsilon(xi) via make_drude/make_plasma factory functions"
  - "File-path imports via importlib.util to avoid 'code' package name conflict"
  - "Convention assertion comments at top of every source file"

conventions:
  - "natural_units=natural (hbar=c=k_B=1)"
  - "metric_signature=mostly_minus (+,-,-,-)"
  - "casimir_force_sign=F < 0 for attractive"
  - "matsubara_prime_sum=l=0 term carries half weight"
  - "[F/A] = [length^{-4}], [omega_p] = [gamma] = [xi] = [length^{-1}]"

plan_contract_ref: ".gpd/phases/02-casimir-force-computation-framework/02-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-lifshitz-framework:
      status: passed
      summary: "Lifshitz formula correctly implements Matsubara summation, reflection coefficients, and material response for Drude and plasma models. T=0 perfect conductor reproduces F=-pi^2/(240*a^4) to relative error 1.87e-13."
      linked_ids: [deliv-lifshitz-code, deliv-material-code, deliv-structural-tests, test-reflection-limits, test-matsubara-structure, test-drude-plasma-relation, test-dimensions-lifshitz, ref-lifshitz-1956]
      evidence:
        - verifier: gpd-executor
          method: structural tests + benchmark reproduction
          confidence: high
          claim_id: claim-lifshitz-framework
          deliverable_id: deliv-lifshitz-code
          acceptance_test_id: test-dimensions-lifshitz
          reference_id: ref-lifshitz-1956
          evidence_path: "code/tests/test_lifshitz_structure.py"
  deliverables:
    deliv-material-code:
      status: passed
      path: code/material_models.py
      summary: "Drude and plasma dielectric functions, Fresnel reflection coefficients, l=0 special cases, gold parameters, eV-to-natural conversion"
      linked_ids: [claim-lifshitz-framework, test-reflection-limits, test-drude-plasma-relation]
    deliv-lifshitz-code:
      status: passed
      path: code/casimir_lifshitz.py
      summary: "Lifshitz force at finite T (Matsubara sum) and T=0 (double integral) with general material support"
      linked_ids: [claim-lifshitz-framework, test-matsubara-structure, test-dimensions-lifshitz]
    deliv-structural-tests:
      status: passed
      path: code/tests/test_lifshitz_structure.py
      summary: "7 structural tests covering reflection limits, Drude-plasma relation, convergence, half-weight, sign, vacuum, and T=0 scaling"
      linked_ids: [claim-lifshitz-framework]
  acceptance_tests:
    test-reflection-limits:
      status: passed
      summary: "|r_TE|,|r_TM|<=1; eps=1 gives r=0; eps->inf gives |r|->1; Drude l=0 r_TE=0; Plasma l=0 r_TE<0 nonzero; both l=0 r_TM=1"
      linked_ids: [claim-lifshitz-framework, deliv-material-code, deliv-lifshitz-code]
    test-matsubara-structure:
      status: passed
      summary: "xi_l=2*pi*l*T spacing verified; l=0 half weight confirmed by manual vs code comparison; sum converges by l_max=50 at T=300K, a=1um (rel change < 1e-13)"
      linked_ids: [claim-lifshitz-framework, deliv-lifshitz-code, deliv-structural-tests]
    test-drude-plasma-relation:
      status: passed
      summary: "epsilon_drude(gamma=1e-10*wp) matches epsilon_plasma to <5e-11 for xi>=omega_p; gamma=1e-20*wp matches to <5e-13 across all xi"
      linked_ids: [claim-lifshitz-framework, deliv-material-code]
    test-dimensions-lifshitz:
      status: passed
      summary: "F(2a)/F(a)=1/16 confirms [F/A]=[length^{-4}]; T=0 perfect conductor reproduces F=-pi^2/(240*a^4) to rel error 1.87e-13"
      linked_ids: [claim-lifshitz-framework, deliv-lifshitz-code]
  references:
    ref-lifshitz-1956:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "Lifshitz formula structure, reflection coefficient definitions, and Matsubara frequency prescription used as definitive framework for implementation"
  forbidden_proxies:
    fp-attractive-force:
      status: rejected
      notes: "This plan builds computational infrastructure only. Attractive Casimir force does not imply energy extraction -- that requires complete cycle analysis in Phase 03."
  uncertainty_markers:
    weakest_anchors: ["Drude l=0 TE limit requires careful analytic treatment (0/0 form) -- handled via separate r_TE_l0_drude function returning 0"]
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-lifshitz-framework
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-lifshitz-1956
    comparison_kind: benchmark
    metric: relative_error
    threshold: "<= 1e-6"
    verdict: pass
    recommended_action: "Proceed to Plan 02-03 for Bordag et al. benchmark validation"
    notes: "T=0 perfect conductor benchmark: F=-pi^2/(240*a^4) reproduced to rel error 1.87e-13, well within threshold"

duration: 15min
completed: 2026-03-22
---

# Plan 02-02: Lifshitz Formula Framework Summary

**Implemented Lifshitz formula framework with Drude/plasma material models, validated against exact Casimir result to 13 digits and all 7 structural tests passing**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-03-22
- **Completed:** 2026-03-22
- **Tasks:** 2
- **Files modified:** 5

## Key Results

- Lifshitz formula at T=0 with perfect conductor reproduces F/A = -pi^2/(240*a^4) to relative error 1.87e-13 [CONFIDENCE: HIGH]
- Drude l=0 TE reflection coefficient is exactly zero; plasma l=0 TE is nonzero and negative -- correctly captures the Drude-plasma controversy [CONFIDENCE: HIGH]
- Matsubara sum converges by l_max=50 at T=300K, a=1um with gold parameters (relative change < 1e-13) [CONFIDENCE: HIGH]
- Dimensional scaling F(2a)/F(a) = 1/16 confirmed to machine precision [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Material models and reflection coefficients** - `b499d97` (implement)
2. **Task 2: Lifshitz formula and structural tests** - `024f66e` (implement)

## Files Created/Modified

- `code/material_models.py` - Drude/plasma dielectric functions, Fresnel reflection coefficients, gold parameters
- `code/casimir_lifshitz.py` - Lifshitz formula (finite T and T=0), Matsubara summation
- `code/tests/test_lifshitz_structure.py` - 7 structural tests
- `code/__init__.py` - Package init
- `code/tests/__init__.py` - Package init

## Next Phase Readiness

- Lifshitz formula infrastructure ready for Bordag et al. benchmarking in Plan 02-03
- Material models (Drude/plasma) available for realistic Casimir force calculations
- Code infrastructure ready for Phases 03-06 (cycle analysis, parameter sweeps, etc.)

## Contract Coverage

- Claim IDs advanced: claim-lifshitz-framework -> passed
- Deliverable IDs produced: deliv-material-code -> code/material_models.py (passed), deliv-lifshitz-code -> code/casimir_lifshitz.py (passed), deliv-structural-tests -> code/tests/test_lifshitz_structure.py (passed)
- Acceptance test IDs run: test-reflection-limits (passed), test-matsubara-structure (passed), test-drude-plasma-relation (passed), test-dimensions-lifshitz (passed)
- Reference IDs surfaced: ref-lifshitz-1956 -> read, use, cite (completed)
- Forbidden proxies rejected: fp-attractive-force (rejected -- infrastructure only)
- Decisive comparison verdicts: claim-lifshitz-framework -> pass (T=0 benchmark rel error 1.87e-13)

## Equations Derived

**Eq. (02-02.1): Lifshitz formula (finite T)**

$$
F/A = -\frac{T}{\pi} \sideset{}{'}\sum_{l=0}^{\infty} \int_0^{\infty} dk_\perp \, k_\perp \, \kappa_0 \sum_{P=\text{TE,TM}} \frac{r_P^2 \, e^{-2\kappa_0 a}}{1 - r_P^2 \, e^{-2\kappa_0 a}}
$$

**Eq. (02-02.2): Drude dielectric function**

$$
\epsilon_D(i\xi) = 1 + \frac{\omega_p^2}{\xi(\xi + \gamma)}
$$

**Eq. (02-02.3): Fresnel reflection coefficients**

$$
r_{\text{TE}} = \frac{\kappa_0 - \kappa}{\kappa_0 + \kappa}, \qquad r_{\text{TM}} = \frac{\epsilon \kappa_0 - \kappa}{\epsilon \kappa_0 + \kappa}
$$

## Validations Completed

- T=0 perfect conductor F/A = -pi^2/(240*a^4) reproduced to 1.87e-13
- Dimensional scaling F(2a)/F(a) = 1/16 to machine precision
- Drude(gamma->0) = Plasma to < 5e-13 relative error
- All reflection coefficient limits correct (vacuum r=0, PC |r|->1, Drude/plasma l=0)
- Matsubara sum exponential convergence verified
- Vacuum (eps=1) gives F=0 exactly
- F < 0 (attractive) for all physical material configurations

## Decisions & Deviations

### Decisions

- l=0 reflection coefficients implemented as separate special-case functions to avoid 0/0 indeterminate forms in the general formula (this is standard practice per Bordag et al.)

### Auto-fixed Issues

**1. [Rule 4 - Missing Component] Added vacuum and perfect conductor material_type for l=0 integrand**

- **Found during:** Task 2 (vacuum gives zero test)
- **Issue:** l=0 special functions (r_TM_l0 = 1) are metal-specific; applying them to vacuum incorrectly gave F != 0
- **Fix:** Added 'vacuum' and 'perfect' branches in lifshitz_integrand l=0 handler
- **Files modified:** code/casimir_lifshitz.py
- **Verification:** test_vacuum_gives_zero passes (F = 0.0)
- **Committed in:** 024f66e (Task 2 commit)

---

**Total deviations:** 1 auto-fixed (Rule 4, missing component)
**Impact on plan:** Essential correctness for non-metallic materials. No scope creep.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Drude model | xi << interband transitions | O(interband corrections) | Interband transitions significant |
| Plasma model | Idealized free-electron | O(gamma/xi) vs Drude | Dissipation significant at low freq |
| Matsubara truncation at l_max | l_max such that |f(l_max)| < 1e-12 |f(0)| | Exponential convergence | T -> 0 (sum becomes integral) |

## Issues Encountered

None.

## Open Questions

- Quantitative comparison with Bordag et al. Table 14.1 benchmarks (deferred to Plan 02-03)
- Performance optimization for large l_max (current implementation uses sequential quad per term)

---

_Phase: 02-casimir-force-computation-framework_
_Plan: 02_
_Completed: 2026-03-22_
