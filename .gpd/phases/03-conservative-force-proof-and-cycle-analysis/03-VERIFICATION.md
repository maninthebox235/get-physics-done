---
phase: 03-conservative-force-proof-and-cycle-analysis
verified: 2026-03-22T17:15:00Z
status: gaps_found
score: 5/6 contract targets verified
consistency_score: 11/12 physics checks passed
independently_confirmed: 8/12 checks independently confirmed
confidence: medium
gaps:
  - subject_kind: acceptance_test
    subject_id: test-wnet-finite-t
    expectation: "|W_net|/|W_close| < 10^{-10} verified by independent numerical computation (two separate integrals)"
    expected_check: "W_close and W_open computed as independent integrals, W_net = W_close + W_open tested against zero"
    status: partial
    category: cross_check
    reason: "cycle_work_lifshitz computes W_close as a single integral, then sets W_open = -W_close algebraically (line 238 of casimir_cycle.py), making W_net = 0 by construction. The acceptance test test-wnet-finite-t reports |W_net|/|W_close| = 0.0, but this is a tautology, not an independent numerical test. The contract requires verifying W_net < 10^{-10} NUMERICALLY for Lifshitz forces. The ideal T=0 numerical case (cycle_work_ideal_numerical) also has the same structure (both integrals evaluate the same function over the same interval, so W_net = 0 is guaranteed by IEEE arithmetic)."
    computation_evidence: "Reading casimir_cycle.py lines 228-241: integral_val computed once, W_close = -integral_val, W_open = integral_val, W_net = W_close + W_open = 0.0 by IEEE arithmetic. No independent second integration is performed."
    artifacts:
      - path: "code/casimir_cycle.py"
        issue: "cycle_work_lifshitz sets W_open = -W_close algebraically; W_net = 0 is built in, not tested"
    missing:
      - "Compute W_close and W_open as two independent integrals (integrate F(a) from a_max to a_min AND from a_min to a_max separately) for at least one Lifshitz configuration, then verify |W_net|/|W_close| < 10^{-10}"
    severity: significant
comparison_verdicts:
  - subject_id: claim-conservative-force
    subject_kind: claim
    reference_id: ref-casimir-1948
    comparison_kind: benchmark
    verdict: pass
    metric: "analytical_match"
    threshold: "exact"
    notes: "F = -dE/da verified independently with E/A = -pi^2/(720 a^3). Sign chain, dimensions, and limiting cases all confirmed."
  - subject_id: claim-cycle-work-t0
    subject_kind: claim
    reference_id: ref-casimir-1948
    comparison_kind: benchmark
    verdict: pass
    metric: "relative_error"
    threshold: "<= 1e-10"
    notes: "W_net = 0.0 exactly (analytical). Numerical: |W_net|/|W_close| = 0.0 (but see gap note on tautological nature)."
  - subject_id: claim-cycle-work-finite-t
    subject_kind: claim
    reference_id: ref-lifshitz-1956
    comparison_kind: benchmark
    verdict: pass
    metric: "|W_net|/|W_close|"
    threshold: "<= 1e-10"
    notes: "W_net = 0 by construction in code. The analytical proof establishes conservativeness. W_close values are physically reasonable (Drude/Ideal ~ 0.51, Plasma > Drude). The claim is ANALYTICALLY verified but the NUMERICAL test is tautological."
  - subject_id: claim-energy-budget-complete
    subject_kind: claim
    reference_id: ref-lifshitz-1956
    comparison_kind: consistency
    verdict: pass
    metric: "conservation_ratio"
    threshold: "<= 1e-8"
    notes: "Energy conservation = 0.0 for all configs. For closed isothermal cycles Delta_E = Q = 0, so conservation reduces to |W_net|/|W_close|."
suggested_contract_checks:
  - check: "Add an acceptance test that computes W_close and W_open as two genuinely independent integrals for at least one Lifshitz configuration"
    reason: "The current cycle_work_lifshitz function makes W_net = 0 by construction. An independent double-integration test would provide genuine numerical evidence."
    suggested_subject_kind: acceptance_test
    suggested_subject_id: test-wnet-double-integration
    evidence_path: "code/casimir_cycle.py"
expert_verification: []
---

# Phase 03 Verification: Conservative Force Proof and Cycle Analysis

**Phase goal:** The Casimir force is formally proven conservative for fixed material properties, and a complete energy budget is computed for quasi-static plate separation cycles demonstrating W_net = 0.

**Verified:** 2026-03-22
**Status:** gaps_found (1 significant gap: tautological W_net numerical test)
**Confidence:** MEDIUM
**Score:** 5/6 contract targets verified; 1 partially verified

**Research mode:** balanced | **Autonomy:** balanced | **Profile:** standard

## Contract Coverage

| Contract ID | Kind | Status | Confidence | Evidence |
|---|---|---|---|---|
| claim-conservative-force | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Proof checked: F = -dV/da with V single-valued; sign chain, dimensions, limiting cases all verified |
| claim-cycle-work-t0 | claim | VERIFIED | INDEPENDENTLY CONFIRMED | W_net = 0 exact (algebraic); numerical W_close matches analytical to machine precision |
| claim-cycle-work-finite-t | claim | VERIFIED (analytical) / PARTIAL (numerical) | STRUCTURALLY PRESENT | Analytical proof correct; W_close values physically reasonable; but W_net = 0 numerical test is tautological |
| claim-energy-budget-complete | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Energy budget table complete with all required columns; conservation trivially satisfied |
| test-wnet-t0-analytical | acceptance_test | PASSED | INDEPENDENTLY CONFIRMED | W_net = 0 exactly for 3 (a_min, a_max) pairs |
| test-wnet-t0-numerical | acceptance_test | PASSED | INDEPENDENTLY CONFIRMED | |W_net|/|W_close| = 0.0; but tautological (same structure as Lifshitz case) |
| test-wnet-finite-t | acceptance_test | PARTIAL | STRUCTURALLY PRESENT | W_net = 0 by code construction, not independent numerical test |
| test-energy-conservation | acceptance_test | PASSED | INDEPENDENTLY CONFIRMED | Conservation = 0.0; but reduces to |W_net|/|W_close| which is zero by construction |
| ref-casimir-1948 | reference | COMPLETED | INDEPENDENTLY CONFIRMED | E/A = -pi^2/(720 a^3), F/A = -pi^2/(240 a^4) used and cited |
| ref-lifshitz-1956 | reference | COMPLETED | STRUCTURALLY PRESENT | Lifshitz formula cited; force values physically reasonable |
| fp-static-energy | forbidden_proxy | REJECTED | INDEPENDENTLY CONFIRMED | Code computes complete cycle (W_close + W_open) |
| fp-one-shot | forbidden_proxy | REJECTED | INDEPENDENTLY CONFIRMED | Both closing and opening work computed |
| fp-attractive-force | forbidden_proxy | REJECTED | INDEPENDENTLY CONFIRMED | Proof explicitly shows conservative F < 0 does not enable extraction |

## Required Artifacts

| Artifact | Expected | Status | Details |
|---|---|---|---|
| derivations/conservative_force_proof.tex | Formal proof with A1-A4 | EXISTS, SUBSTANTIVE | 409 lines, complete theorem + proof + corollary + analytical cycle + limiting cases |
| code/casimir_cycle.py | Cycle work computation | EXISTS, SUBSTANTIVE, INTEGRATED | 4 functions; used by test suites and energy budget |
| code/tests/test_cycle_t0.py | T=0 test suite | EXISTS, SUBSTANTIVE | 17 tests, all passing |
| code/tests/test_cycle_finite_t.py | Finite-T test suite | EXISTS, SUBSTANTIVE | 26 tests, all passing |
| artifacts/.../energy_budget_table.txt | Energy budget table | EXISTS, SUBSTANTIVE | 6 configurations, complete columns |

## Computational Verification Details

### 5.1 Dimensional Analysis (INDEPENDENTLY CONFIRMED)

Traced dimensions through all key equations:

```
E/A = -pi^2/(720 a^3)
  LHS: [energy/area] = [length^{-3}] in natural units
  RHS: [1/a^3] = [length^{-3}]  CONSISTENT

F/A = -pi^2/(240 a^4)
  LHS: [force/area] = [length^{-4}] in natural units
  RHS: [1/a^4] = [length^{-4}]  CONSISTENT

W_close/A = -pi^2/720 * (1/a_max^3 - 1/a_min^3)
  LHS: [work/area] = [length^{-3}]
  RHS: [1/length^3] = [length^{-3}]  CONSISTENT
```

Verified numerically: `E/A * a^3 = -pi^2/720 = -0.0137077839` (exact match).
`F/A * a^4 = -pi^2/240 = -0.0411233517` (exact match).

**Status: CONSISTENT**

### 5.2 Numerical Spot-Checks (INDEPENDENTLY CONFIRMED)

Computed W_close independently at (a_min=1.0, a_max=10.0):

```
My calculation:   W_close = 1.3694076107e-02
Code analytical:  W_close = 1.3694076107e-02
Code numerical:   W_close = 1.3694076107e-02
Relative error vs code: 0.00e+00
```

SI cross-check at a_min=100nm, a_max=1um:

```
My SI calculation: W_close/A = 4.3294e-07 J/m^2
Code natural units: W_close/A = 1.369408e+19 m^{-3}
After hbar*c conversion: 4.3294e-07 J/m^2  MATCH
```

Casimir pressure at 100nm: |F/A| = 13.0 Pa -- matches Casimir (1948) formula.
Casimir pressure at 1um: |F/A| = 1.3e-3 Pa -- consistent with literature.

**Status: ALL SPOT-CHECKS PASS**

### 5.3 Limiting Cases (INDEPENDENTLY CONFIRMED)

**Limit 1: Trivial cycle (a_min = a_max)**

```
W_close = W_open = W_net = 0.0 exactly.  PASS
```

**Limit 2: Infinite separation (a_max -> infinity)**

```
Exact limit: W_close -> pi^2/(720 * a_min^3) = -E(a_min)/A
Code (a_max=1e6): W_close = 1.3707783890e-02
Expected limit:    W_close = 1.3707783890e-02
Relative diff: 0.00e+00  PASS
```

**Limit 3: Small cycle (a0=5.0, delta=0.001)**

```
Code W_close:    6.5771052499e-08
Linear approx:   6.5797362674e-08
Relative diff:   3.9987e-04 ~ O(delta/a0) = 2.0e-04  PASS (correct order)
```

**Status: ALL LIMITS VERIFIED**

### 5.6 Symmetry Verification (INDEPENDENTLY CONFIRMED)

Sign conventions verified throughout all artifacts:
- F < 0 (attractive): Confirmed in formula and numerical output
- W_close > 0 (closing under attraction extracts energy): Confirmed for all 6 configs
- W_open < 0 (opening costs energy): Confirmed for all 6 configs
- W_net = 0 (conservative): Confirmed (analytically exact)

Convention assertions in all files match state.json convention_lock.

**Status: VERIFIED**

### 5.7 Conservation Law (INDEPENDENTLY CONFIRMED)

For a conservative force: energy conservation requires W_net = Delta_E_vac + Q.
For closed isothermal cycles: Delta_E_vac = 0, Q = 0, so W_net = 0.
Conservation residual = 0.0 for all 6 configurations.

**Status: VERIFIED**

### 5.8 Mathematical Consistency (INDEPENDENTLY CONFIRMED)

Sign chain verification:
```
E(a) = -pi^2/(720 a^3) < 0
dE/da = +3*pi^2/(720 a^4) = pi^2/(240 a^4) > 0  (energy increases with separation)
F = -dE/da = -pi^2/(240 a^4) < 0  (attractive)
```

Numerical derivative cross-check: F analytical vs central difference agrees to 3.07e-09.

Proof structure verified: Theorem + Conditions A1-A4 + Proof (T=0 and T>0 cases) + Corollary + Analytical cycle + Limiting cases + Violation scenarios.

**Status: CONSISTENT**

### 5.9 Numerical Convergence (INDEPENDENTLY CONFIRMED)

All 43 tests (17 T=0 + 26 finite-T) pass:
- T=0 tests: 17/17 passed
- Finite-T tests: 26/26 passed
- Integration warnings noted for ideal numerical case at high tolerance (1e-14) -- not blocking

**Status: CONVERGED**

### 5.10 Agreement with Literature (INDEPENDENTLY CONFIRMED)

| Quantity | Our Value | Literature | Agreement |
|---|---|---|---|
| F/A at 100nm | 13.0 Pa | Casimir (1948): pi^2*hbar*c/(240*a^4) = 13.0 Pa | Exact |
| F/A at 1um | 1.3e-3 Pa | Literature: ~1.3 mPa | Exact |
| E/A formula | -pi^2/(720 a^3) | Casimir (1948) | Exact |
| Drude/Ideal ratio | 0.509 | Lambrecht & Reynaud: ~0.4-0.6 for Au | Consistent |
| Plasma > Drude | 3.14% | Expected: TE l=0 contribution | Consistent |

**Status: AGREES**

### 5.11 Physical Plausibility (INDEPENDENTLY CONFIRMED)

- All W_close values positive (energy extracted during closing): PASS
- All W_open values negative (energy input during opening): PASS
- Drude W_close < Ideal W_close (real metals weaker): PASS
- Plasma W_close > Drude W_close (dissipationless limit stronger): PASS
- Wide range |W_close| > narrow range |W_close|: PASS
- Thermal correction at 300K negligible at 100nm (lambda_T >> a): PASS

**Status: PLAUSIBLE**

### 5.4 Independent Cross-Check (STRUCTURALLY PRESENT)

The analytical proof that F is conservative is structurally sound:
1. F(a,T) = -dF_free/da where F_free is Helmholtz free energy (state function)
2. State functions are single-valued by definition
3. Gradient of single-valued function in 1D is automatically conservative
4. Lifshitz formula manifestly depends only on a (for fixed T, epsilon, mu)

However, no independent numerical cross-check was performed that computes W_net via two separate integrals for the Lifshitz case. See gap below.

**Status: STRUCTURALLY PRESENT (analytical), UNABLE TO VERIFY (numerical independence)**

## Physics Consistency Summary

| Check | Status | Confidence | Notes |
|---|---|---|---|
| 5.1 Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All equations traced |
| 5.2 Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | W_close values match independent calculation |
| 5.3 Limiting cases | PASS | INDEPENDENTLY CONFIRMED | 3 limits re-derived and verified |
| 5.4 Cross-check | PARTIAL | STRUCTURALLY PRESENT | Analytical cross-check OK; numerical independence missing for Lifshitz |
| 5.6 Symmetry | VERIFIED | INDEPENDENTLY CONFIRMED | Sign conventions consistent |
| 5.7 Conservation | VERIFIED | INDEPENDENTLY CONFIRMED | Energy budget closes |
| 5.8 Math consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | Sign chain, derivative, proof structure |
| 5.9 Convergence | CONVERGED | INDEPENDENTLY CONFIRMED | 43/43 tests pass |
| 5.10 Literature | AGREES | INDEPENDENTLY CONFIRMED | Casimir (1948) and Lifshitz values match |
| 5.11 Plausibility | PLAUSIBLE | INDEPENDENTLY CONFIRMED | Signs, magnitudes, ordering all correct |
| 5.13 Thermodynamic | CONSISTENT | STRUCTURALLY PRESENT | F_free is state function by construction |
| Gate B Analytical-numerical | PASS | INDEPENDENTLY CONFIRMED | Analytical and numerical W_close agree to < 1e-14 |

**Overall physics assessment: SOUND with one structural gap**

## Forbidden Proxy Audit

| Proxy ID | Status | Evidence |
|---|---|---|
| fp-static-energy | REJECTED | All code computes complete cycles (W_close + W_open = W_net) |
| fp-one-shot | REJECTED | Both closing and opening work tracked in energy budget table |
| fp-attractive-force | REJECTED | Proof explicitly addresses: conservative F < 0 cannot extract over cycle |

## Discrepancies Found

| Severity | Location | Description | Evidence | Suggested Fix |
|---|---|---|---|---|
| significant | casimir_cycle.py:228-241 | cycle_work_lifshitz makes W_net = 0 by construction (W_open = -W_close algebraically) | Lines 234, 238: `W_close = -integral_val`, `W_open = integral_val` | Add a function that computes two separate integrals as an independent test |
| minor | casimir_cycle.py:146-155 | cycle_work_ideal_numerical also has W_net = 0 by construction (same integral evaluated twice with opposite signs) | W_close = -quad(F, a_min, a_max), W_open = quad(F, a_min, a_max) | Same fix: compute as genuinely separate integrals |
| info | energy_budget_table.txt:41 | "W_net = 0.0 EXACTLY" is stated as "not a numerical coincidence" which is correct (it IS algebraic), but it should note that the code enforces this by construction rather than testing it | Table observation #1 | Add note clarifying code structure |

## Comparison Verdict Ledger

| Subject ID | Comparison Kind | Verdict | Threshold | Notes |
|---|---|---|---|---|
| claim-conservative-force | benchmark vs Casimir (1948) | PASS | exact | F = -dE/da verified independently |
| claim-cycle-work-t0 | benchmark vs Casimir (1948) | PASS | <= 1e-10 | W_net = 0 exact (algebraic) |
| claim-cycle-work-finite-t | benchmark vs Lifshitz (1956) | PASS | <= 1e-10 | W_close values reasonable; W_net = 0 by construction |
| claim-energy-budget-complete | consistency | PASS | <= 1e-8 | Conservation = 0.0 |

## Requirements Coverage

| Requirement | Phase Coverage | Status |
|---|---|---|
| R1.5: Prove F conservative | Full | SATISFIED |
| R2.2: Complete energy budget | Full | SATISFIED |

## Anti-Patterns Found

| Category | Severity | Location | Description | Physics Impact |
|---|---|---|---|---|
| numerical | INFO | test_cycle_t0.py:60-64 | Integration warning about roundoff at epsrel=1e-14 | None (test still passes; warning is from pushing beyond machine precision) |
| design | significant | casimir_cycle.py:228-241 | W_net = 0 enforced by construction in cycle_work_lifshitz | Cannot detect non-conservative forces numerically |

## Confidence Assessment

**Overall: MEDIUM**

The analytical proof is rigorous and independently verified:
- The Casimir force derives from a potential (vacuum energy at T=0, Helmholtz free energy at T>0)
- Conditions A1-A4 are clearly stated and physically motivated
- The corollary (W_net = 0 for closed cycles) follows directly
- All limiting cases, signs, dimensions, and literature values check out

The numerical verification is PARTIALLY tautological:
- W_close values are correct and independently verified
- W_net = 0 is enforced by code construction, not tested by independent integration
- The claim |W_net|/|W_close| < 10^{-10} is technically true but trivially satisfied

The gap is SIGNIFICANT but not a BLOCKER because:
1. The analytical proof of conservativeness is correct and complete
2. W_close values are independently verified and physically reasonable
3. The mathematical argument that W_net = 0 for any 1D conservative force is trivially true
4. A genuine numerical test would confirm what is already proven analytically

Confidence would be HIGH if the gap were closed by adding an independent double-integration test.

## Gaps Summary

**One significant gap identified:**

The cycle_work_lifshitz function computes a single integral and sets W_open = -W_close, making W_net = 0 a tautology rather than a numerical test. The acceptance test test-wnet-finite-t therefore reports |W_net|/|W_close| = 0.0, but this is not an independent verification.

**Root cause:** Optimization in Plan 03-02 (computing one integral instead of two to halve computation time) conflated performance optimization with test independence.

**Fix:** Add a `cycle_work_lifshitz_double_integration` function (or a test-only function) that computes W_close and W_open as genuinely separate integrals, then verifies |W_close + W_open|/|W_close| < 10^{-10}. This would take ~6 additional minutes of compute time per configuration.

**Impact on phase goal:** The phase goal is SUBSTANTIALLY achieved. The analytical proof is correct and the energy budget is complete. The gap affects only the strength of the numerical evidence, not the validity of the result.
