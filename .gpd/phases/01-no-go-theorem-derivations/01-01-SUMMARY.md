---
phase: 01-no-go-theorem-derivations
plan: 01
depth: full
one-liner: "Derived three independent no-go arguments (thermodynamic, Lorentz invariance, passivity) with numbered assumptions, proving W_net <= 0 for cyclic ZPE extraction under complementary conditions"
subsystem: derivation
tags:
  - casimir-effect
  - no-go-theorem
  - passivity
  - lorentz-invariance
  - thermodynamics
  - vacuum-energy

requires:
  - phase: none
    provides: first phase — no prior dependencies

provides:
  - Three formal no-go derivations with numbered assumptions (A1-A5, B1-B4, C1-C5)
  - Cross-verification confirming assumption independence and mutual consistency
  - Coverage gap identification (time-dependent H with boundaries)
  - Loophole map connecting to Phases 05-06

affects:
  - 05-loophole-analysis (boundary condition and material property loopholes target A3, B2, C1)
  - 06-dynamic-casimir (dynamic Casimir targets C1 time-dependent H gap)

methods:
  added:
    - Conservative force argument for cyclic work
    - Lorentz group representation theory for vacuum stress-energy tensor
    - Pusz-Woronowicz passivity theorem with elementary proof
  patterns:
    - Number all assumptions explicitly for loophole traceability
    - Self-critique checkpoints after every 3-4 derivation steps

key-files:
  created:
    - derivations/nogo-thermodynamic.md
    - derivations/nogo-lorentz.md
    - derivations/nogo-passivity.md
    - derivations/nogo-cross-verification.md

key-decisions:
  - "Used elementary proof of ground state passivity rather than full C*-algebraic Pusz-Woronowicz proof — sufficient for the claim and more transparent"
  - "Included Casimir cavity stress tensor (B.17) in Lorentz argument to explicitly show WHERE the argument breaks down"

conventions:
  - "hbar = c = k_B = 1 (natural units)"
  - "metric = (+,-,-,-) (mostly-minus)"
  - "F < 0 for attractive Casimir force"
  - "E < 0 for bounded < unbounded"
  - "W_net > 0 means extraction; W_net <= 0 is the no-go claim"
  - "Regularization: zeta function"

plan_contract_ref: ".gpd/phases/01-no-go-theorem-derivations/01-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-nogo-consistency:
      status: passed
      summary: "Three independent no-go arguments derived with explicit numbered assumptions; cross-verification confirms assumptions form a consistent set with no mutual contradictions"
      linked_ids: [deliv-nogo-derivation, test-nogo-consistency, test-assumptions-numbered]
      evidence:
        - verifier: self
          method: cross-verification document
          confidence: high
          claim_id: claim-nogo-consistency
          deliverable_id: deliv-nogo-derivation
          acceptance_test_id: test-nogo-consistency
          evidence_path: "derivations/nogo-verification.md"
  deliverables:
    deliv-nogo-derivation:
      status: passed
      path: derivations/
      summary: "Three derivation files with numbered assumptions: nogo-thermodynamic.md (A1-A5), nogo-lorentz.md (B1-B4), nogo-passivity.md (C1-C5), plus cross-verification document"
      linked_ids: [claim-nogo-consistency, test-nogo-consistency, test-assumptions-numbered]
  acceptance_tests:
    test-nogo-consistency:
      status: passed
      summary: "Cross-verification confirms no mutual contradictions between assumption sets A, B, C; coverage gap identified for time-dependent H with boundaries"
      linked_ids: [claim-nogo-consistency, deliv-nogo-derivation]
    test-assumptions-numbered:
      status: passed
      summary: "All assumptions explicitly numbered: A1-A5 (thermodynamic), B1-B4 (Lorentz), C1-C5 (passivity); no implicit assumptions found"
      linked_ids: [claim-nogo-consistency, deliv-nogo-derivation]
  references:
    ref-pusz-woronowicz:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Pusz-Woronowicz passivity theorem cited as foundation for Argument C; theorem statement and proof sketch included"
    ref-weinberg-qft:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Weinberg QFT Vol 1 §11.2 cited for vacuum stress-energy tensor derivation in Argument B"
    ref-lenard:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Lenard (1978) cited as independent confirmation of passivity result"
    ref-scandurra:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Scandurra (2001) cited for rigorous proof that Casimir force is conservative"
    ref-jaffe:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Jaffe (2005) cited for alternative interpretation of Casimir effect without vacuum energy"
  forbidden_proxies:
    fp-citation-only:
      status: rejected
      notes: "All three arguments are derived with explicit assumptions and proof steps, not merely cited"
    fp-attractive-force:
      status: rejected
      notes: "No argument uses attractive force as evidence against extraction; all prove W_net <= 0 through independent reasoning"
  uncertainty_markers:
    weakest_anchors:
      - "Passivity argument applied to QFT vacuum with boundaries not explicitly in Pusz-Woronowicz (1978) — the time-dependent H gap is acknowledged"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 5min
completed: 2026-03-22
---

# Plan 01-01: No-Go Theorem Derivations Summary

**Derived three independent no-go arguments (thermodynamic, Lorentz invariance, passivity) with numbered assumptions, proving W_net <= 0 for cyclic ZPE extraction under complementary conditions**

## Performance

- **Duration:** 5 min
- **Started:** 2026-03-22T02:14:44Z
- **Completed:** 2026-03-22T02:20:05Z
- **Tasks:** 4 (Task 1 previously committed; Tasks 2-4 executed in this session)
- **Files modified:** 4

## Key Results

- **Thermodynamic (A):** Conservative Casimir force gives $W_{\text{net}} = 0$ for quasi-static cycles; second law gives $W_{\text{net}} \leq 0$ for any cycle. Key loophole: material property changes (A3). [CONFIDENCE: HIGH]
- **Lorentz invariance (B):** Poincaré invariance constrains $\langle 0|T^{\mu\nu}|0\rangle = \rho_{\text{vac}} g^{\mu\nu}$, giving $p = -\rho$ equation of state and $W_{\text{net}} = 0$. Key loophole: boundaries (B2). [CONFIDENCE: HIGH]
- **Passivity (C):** Ground state passivity proven elementarily: $\sum_n |c_n|^2 E_n \geq E_0$. Complete passivity rules out multi-copy schemes. Key loophole: time-dependent $H$ (C1). [CONFIDENCE: HIGH]
- **Cross-verification:** Assumptions are independent, non-contradictory, and provide overlapping coverage with a well-defined gap (time-dependent $H$ with boundaries and material changes).

## Task Commits

Each task was committed atomically:

1. **Task 1: Thermodynamic no-go argument** - `f827b48` (derive) — previously committed
2. **Task 2: Lorentz invariance no-go argument** - `c363257` (derive)
3. **Task 3: Passivity no-go argument (Pusz-Woronowicz)** - `f4d1ee2` (derive)
4. **Task 4: Cross-verification** - `bb87511` (validate)

## Files Created/Modified

- `derivations/nogo-thermodynamic.md` — Argument A: conservative force + second law
- `derivations/nogo-lorentz.md` — Argument B: Poincaré invariance → p = -ρ
- `derivations/nogo-passivity.md` — Argument C: ground state passivity
- `derivations/nogo-cross-verification.md` — Cross-verification of all three arguments

## Next Phase Readiness

- Three no-go derivations ready for downstream loophole analysis (Phases 05-06)
- Assumption numbering enables precise loophole targeting: A3 (material changes), B2 (boundaries), C1 (time-dependent H)
- Coverage gap clearly identified: time-dependent H with boundaries and material changes

## Contract Coverage

- Claim IDs advanced: claim-nogo-consistency -> passed
- Deliverable IDs produced: deliv-nogo-derivation -> derivations/ (passed)
- Acceptance test IDs run: test-nogo-consistency -> passed, test-assumptions-numbered -> passed
- Reference IDs surfaced: ref-pusz-woronowicz (read, cite), ref-weinberg-qft (read, cite), ref-lenard (cite), ref-scandurra (cite), ref-jaffe (cite)
- Forbidden proxies rejected: fp-citation-only (rejected), fp-attractive-force (rejected)

## Equations Derived

**Eq. (01.1) — Casimir energy per unit area (T=0, ideal plates):**

$$
\frac{E_{\text{Cas}}(a)}{\mathcal{A}} = -\frac{\pi^2}{720\, a^3}
$$

**Eq. (01.2) — Casimir force per unit area:**

$$
\frac{F_{\text{Cas}}(a)}{\mathcal{A}} = -\frac{\pi^2}{240\, a^4}
$$

**Eq. (01.3) — Vacuum stress-energy tensor (Lorentz invariance):**

$$
\langle 0|T^{\mu\nu}|0\rangle = \rho_{\text{vac}}\, g^{\mu\nu} \quad \Rightarrow \quad p_{\text{vac}} = -\rho_{\text{vac}}
$$

**Eq. (01.4) — Ground state passivity:**

$$
\Delta E = \sum_n |c_n|^2 E_n - E_0 \geq 0 \quad \Rightarrow \quad W_{\text{net}} = -\Delta E \leq 0
$$

## Validations Completed

- Dimensional analysis: all equations verified in natural units [length^{-4}] for forces, [length^{-3}] for energies per area
- Limiting case (Argument A): $\oint F\,da = 0$ verified explicitly for ideal plates
- Limiting case (Argument C): two-level system passivity verified: $\Delta E = \sin^2\theta(E_1 - E_0) \geq 0$
- Symmetry check (Argument B): $g^{\mu\nu}$ verified as unique rank-2 symmetric Lorentz-invariant tensor via boost/rotation constraints
- Cross-verification: 7 checks passed (dimensional, logic, independence, consistency, coverage, signs, references)

## Decisions & Deviations

None — plan executed exactly as written.

## Open Questions

- Can the time-dependent H gap in Argument C be closed by a generalized passivity result? (Relevant to Phase 06)
- The Casimir cavity stress tensor Eq. (B.17) shows anisotropy — does this anisotropy enable any cycle that the isotropic free-vacuum cannot support? (Relevant to Phase 05)

## Self-Check: PASSED

- [x] derivations/nogo-thermodynamic.md exists
- [x] derivations/nogo-lorentz.md exists
- [x] derivations/nogo-passivity.md exists
- [x] derivations/nogo-cross-verification.md exists
- [x] Commit f827b48 exists (Task 1)
- [x] Commit c363257 exists (Task 2)
- [x] Commit f4d1ee2 exists (Task 3)
- [x] Commit bb87511 exists (Task 4)
- [x] All equations dimensionally consistent
- [x] All derivations use identical convention assertions
- [x] Forbidden proxies rejected (no citation-only, no attractive-force-as-evidence)

---

_Phase: 01-no-go-theorem-derivations_
_Completed: 2026-03-22_
