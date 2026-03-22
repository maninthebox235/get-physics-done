---
gpd_role: roadmap
version: 1
depth: standard
research_mode: balanced
milestone: "Feasibility Analysis"
phases: 7
---

# Roadmap: Zero-Point Energy Extraction via the Casimir Effect

## Overview

This project investigates whether zero-point energy of the quantum vacuum can be extracted as usable work through cyclic processes involving boundary condition changes. The roadmap proceeds from formal no-go theorem derivations through quantitative Casimir engine analysis to a systematic examination of four loophole classes, culminating in a unified feasibility verdict with complete energy accounting at every stage.

## Contract Overview

| Contract Item | Type | Advanced By Phase(s) | Status |
| --- | --- | --- | --- |
| claim-cycle-work: W_net <= 0 for cyclic Casimir processes | claim | 02, 03, 04, 07 | Planned |
| claim-nogo-consistency: Three no-go arguments consistent | claim | 01, 07 | Planned |
| claim-loophole-analysis: Four loopholes classified | claim | 05, 06, 07 | Planned |
| deliv-energy-budget: Complete energy budget table | deliverable | 03, 04 | Planned |
| deliv-param-sweep: W_net parameter sweep figure | deliverable | 04 | Planned |
| deliv-nogo-derivation: No-go derivations + assumption table | deliverable | 01 | Planned |
| deliv-loophole-report: Loophole verdicts with energy accounting | deliverable | 05, 06, 07 | Planned |
| deliv-casimir-reproduction: Casimir force benchmark figure | deliverable | 02 | Planned |
| ref-casimir-1948: Casimir (1948) ideal plate benchmark | anchor | 02 | Planned |
| ref-lifshitz-1956: Lifshitz (1956) finite-T/material benchmark | anchor | 02 | Planned |
| fp-attractive-force: Attractive force alone is NOT extraction | forbidden proxy | 02, 03 | Active |
| fp-static-energy: Static E(a) without cycle is NOT extraction | forbidden proxy | 03, 04 | Active |
| fp-one-shot: One-shot collapse without separation cost is NOT extraction | forbidden proxy | 03, 04, 05 | Active |

## Phases

**Phase Numbering:**

- Integer phases (01, 02, ...): Planned research work
- Decimal phases (02.1, 02.2): Urgent insertions if needed (marked with INSERTED)

**Milestone 1: Feasibility Analysis**

- [x] **Phase 01: No-Go Theorem Derivations** - Derive three independent no-go arguments with explicit numbered assumptions and comparison table
- [x] **Phase 02: Casimir Force Computation Framework** - Implement and benchmark Casimir force for ideal plates (T=0) and realistic materials (Lifshitz, Drude/plasma)
- [x] **Phase 03: Conservative Force Proof and Cycle Analysis** - Prove Casimir force is conservative for fixed materials; compute complete energy budget for quasi-static cycles
- [ ] **Phase 04: W_net Parameter Sweep** - Sweep W_net over (a_min, a_max, T) parameter space; confirm W_net=0 across full range
- [ ] **Phase 05: Loophole Analysis -- Boundary and Topology** - Analyze boundary condition change (Pinto-type) and topology change loopholes with full energy accounting
- [ ] **Phase 06: Loophole Analysis -- Non-Equilibrium and Dynamic Casimir** - Analyze non-equilibrium state loophole and dynamic Casimir loophole
- [ ] **Phase 07: Synthesis and Conclusions** - Synthesize all results into unified analysis with final feasibility verdict

**Stretch Goals (not in main roadmap):**

- R4.1: Time-dependent Hamiltonian passivity (extends R1.3)
- R4.2: Sphere-plate geometry via proximity force approximation (extends R2.1)
- R4.3: Full dynamic Casimir Bogoliubov computation (extends R3.4)
- R4.4: Atom pumping mechanism analysis (new loophole class)

## Phase Details

### Phase 01: No-Go Theorem Derivations

**Goal:** Three independent no-go arguments (thermodynamic, Lorentz invariance, passivity) are derived with explicit numbered assumptions, and a comparison table reveals their overlapping and distinct hypotheses
**Depends on:** Nothing (entry point; consumes literature survey)
**Requirements:** R1.1, R1.2, R1.3, R1.4
**Contract Coverage:**
- Advances: claim-nogo-consistency
- Deliverables: deliv-nogo-derivation (three derivations + assumption comparison table)
- Anchor coverage: Pusz-Woronowicz (1978) passivity theorem; identify definitive reference
- Forbidden proxies: None specific to this phase
- Stop/rethink: If three arguments require mutually contradictory assumptions, that is itself a major result -- document and reassess scope
**Success Criteria** (what must be TRUE):

1. Thermodynamic no-go argument derived with all assumptions numbered; shows W_net <= 0 for any cyclic Casimir process at thermal equilibrium
2. Lorentz invariance argument derived showing <0|T^{mu nu}|0> proportional to g^{mu nu} implies non-extractability; failure mode for bounded systems explicitly identified
3. Passivity argument stated with proof sketch: vacuum as KMS state at beta = infinity is passive under cyclic unitaries for fixed Hamiltonian; gap for time-dependent H explicitly identified
4. Comparison table complete with columns: argument name, key assumptions, what it proves, known loopholes, strength rating
5. All three assumption sets checked for mutual consistency; any overlap or tension documented

**Backtracking trigger:** If passivity theorem literature is insufficient to state the argument rigorously, Phase 01 may need a targeted literature extension before proceeding

**Plans:** TBD

Plans:

- [x] 01-01: Three no-go theorem derivations + cross-verification
- [x] 01-02: Comparison table + consistency analysis + strength assessment

### Phase 02: Casimir Force Computation Framework

**Goal:** Casimir force calculations are implemented and benchmarked against exact analytical results for ideal plates and against published tabulated values for realistic materials
**Depends on:** Phase 01 (sign and factor conventions established during no-go derivations)
**Requirements:** R2.1
**Contract Coverage:**
- Advances: claim-cycle-work (computational foundation)
- Deliverables: deliv-casimir-reproduction (F(a) vs known result, relative error, ideal + realistic)
- Anchor coverage: ref-casimir-1948 (reproduce F = -pi^2 hbar c / (240 a^4) to < 10^{-6}); ref-lifshitz-1956 (reproduce Lifshitz formula for Drude and plasma models against Bordag et al. 2009)
- Forbidden proxies: fp-attractive-force (attractive force alone does not imply extraction)
**Success Criteria** (what must be TRUE):

1. Ideal parallel plates at T=0: computed F/A matches -pi^2 hbar c / (240 a^4) with relative error < 10^{-6}
2. Finite-T Drude model: Lifshitz formula results match Bordag et al. (2009) tabulated values within stated numerical precision
3. Finite-T plasma model: same benchmark reproduced independently
4. All computed forces have correct dimensions [force/area] = [energy/length^4] in natural units
5. Limiting cases verified: T -> 0 recovers ideal result; a -> infinity gives vanishing force; epsilon -> infinity recovers perfect conductor

**Backtracking trigger:** If mode summation and Lifshitz formula disagree in overlapping regime by more than numerical tolerance, debug before proceeding

**Plans:** 3 plans

Plans:

- [x] 02-01-PLAN.md -- Ideal plates T=0: analytical formula + zeta-regularized mode summation benchmark (< 10^{-6})
- [x] 02-02-PLAN.md -- Lifshitz formula infrastructure: material models (Drude/plasma) + Matsubara summation framework
- [x] 02-03-PLAN.md -- Full benchmarking: cross-validate ideal via Lifshitz, Drude/plasma at T=300K, all 5 limiting cases

### Phase 03: Conservative Force Proof and Cycle Analysis

**Goal:** The Casimir force is formally proven conservative for fixed material properties, and a complete energy budget is computed for quasi-static plate separation cycles demonstrating W_net = 0
**Depends on:** Phase 02 (validated force computation code)
**Requirements:** R1.5, R2.2
**Contract Coverage:**
- Advances: claim-cycle-work (core result)
- Deliverables: deliv-energy-budget (W_close, W_open, W_net, Delta E_vacuum, Q for finite T)
- Anchor coverage: Conservative force implies closed-loop integral vanishes; energy conservation verified to < 10^{-8}
- Forbidden proxies: fp-static-energy (must analyze complete cycle, not static E(a)); fp-one-shot (cycle must close); fp-attractive-force (attractive force alone is not extraction)
- Stop/rethink: If W_net > 0 found for any parameter point in quasi-static regime, STOP and verify before claiming loophole
**Success Criteria** (what must be TRUE):

1. Formal proof that F = -dV/da where V depends only on plate separation (and material properties and T), hence F is conservative for fixed materials
2. Explicit conditions for conservativeness stated (fixed material response, quasi-static process, thermal equilibrium maintained)
3. Complete energy budget computed: W_close + W_open = W_net, with Delta E_vacuum and Q (heat) tracked separately at finite T
4. Energy conservation verified: |W_net - (Delta E_vacuum + Q)| / |W_close| < 10^{-8} for all tested configurations
5. W_net / |W_close| < 10^{-10} numerically for conservative-force cycles (verifying exact cancellation to high precision)

**Backtracking trigger:** If energy conservation check fails at > 10^{-8}, indicates numerical error in Phase 02 code -- return and fix

**Plans:** 2 plans

Plans:

- [x] 03-01-PLAN.md -- Conservative force proof + T=0 cycle (analytical + numerical W_net = 0)
- [x] 03-02-PLAN.md -- Finite-T energy budget: 6 configurations (ideal/Drude/plasma), energy conservation verification

### Phase 04: W_net Parameter Sweep

**Goal:** W_net is mapped over the full (a_min, a_max, T) parameter space, confirming W_net = 0 everywhere for the conservative-force case and providing the definitive parameter sweep figure
**Depends on:** Phase 03 (cycle energy budget code)
**Requirements:** R2.3
**Contract Coverage:**
- Advances: claim-cycle-work (decisive quantitative evidence)
- Deliverables: deliv-param-sweep (3D visualization of W_net vs (a_min, a_max, T); 500k grid points; ideal + realistic)
- Anchor coverage: Energy budget and parameter sweep must agree on sign of W_net (test-energy-budget-consistency)
- Forbidden proxies: fp-static-energy (sweep is over complete cycles); fp-one-shot (every point is a closed cycle)
- Stop/rethink: Any point with W_net > 0 triggers immediate investigation
**Success Criteria** (what must be TRUE):

1. Parameter sweep covers a_min in [10 nm, 1 um], a_max in [100 nm, 10 um], T in [0, 300 K] with 100 x 100 x 50 = 500k grid points
2. W_net / |W_close| < 10^{-10} confirmed at every grid point for conservative-force (fixed materials) case
3. 3D visualization (heatmap/contour) produced showing W_net across parameter space
4. Both ideal conductor and realistic material (Drude + plasma) cases swept
5. No anomalous sign changes or unexpected structure in W_net landscape; any numerical artifacts identified and explained

**Backtracking trigger:** If systematic drift in W_net/|W_close| correlates with parameter regime (e.g., grows near thermal crossover), return to Phase 02/03 to check thermal corrections

**Plans:** TBD

Plans:

- [ ] 04-01: TBD

### Phase 05: Loophole Analysis -- Boundary and Topology

**Goal:** The boundary condition change (Pinto-type) and topology change loopholes are analyzed with complete energy accounting, showing W_net <= 0 when all costs are included
**Depends on:** Phase 03 (energy budget framework), Phase 01 (no-go assumption lists to identify which assumptions each loophole targets)
**Requirements:** R3.1, R3.2
**Contract Coverage:**
- Advances: claim-loophole-analysis (two of four loopholes)
- Deliverables: deliv-loophole-report (boundary change and topology change sections with verdicts)
- Anchor coverage: Scandurra (2001) for Pinto-type cycle analysis
- Forbidden proxies: fp-one-shot (Pinto cycle must include reflectivity change cost); fp-static-energy (topology change must include creation/destruction cost)
**Success Criteria** (what must be TRUE):

1. Pinto-type cycle analyzed: reflectivity change mid-cycle with energy cost of material property modification explicitly included in budget
2. Complete energy budget for boundary condition change scenario shows W_net <= 0
3. Topology change scenario analyzed: cavity creation energy + Casimir energy extraction + cavity destruction energy fully accounted
4. Complete energy budget for topology change scenario shows W_net <= 0
5. Each loophole mapped to the specific no-go assumption it targets; verdict stated (genuine loophole vs apparent loophole with explanation)

**Backtracking trigger:** If boundary condition change analysis requires material response functions not implemented in Phase 02, return to extend the code

**Plans:** TBD

Plans:

- [ ] 05-01: TBD
- [ ] 05-02: TBD

### Phase 06: Loophole Analysis -- Non-Equilibrium and Dynamic Casimir

**Goal:** The non-equilibrium state loophole and dynamic Casimir loophole are analyzed: passivity of non-vacuum states near boundaries is assessed, and the energy source for dynamic Casimir photon production is identified
**Depends on:** Phase 01 (passivity framework and no-go assumptions), Phase 02 (force computation for dynamic analysis)
**Requirements:** R3.3, R3.4
**Contract Coverage:**
- Advances: claim-loophole-analysis (remaining two loopholes)
- Deliverables: deliv-loophole-report (non-equilibrium and dynamic Casimir sections with verdicts)
- Anchor coverage: Wilson et al. (2011) for experimental dynamic Casimir; Pusz-Woronowicz (1978) for passivity framework
- Forbidden proxies: None specific beyond general false-progress guards
- Open contract question: Is dynamic Casimir photon production genuinely ZPE extraction or powered by the mirror's kinetic energy?
**Success Criteria** (what must be TRUE):

1. Passivity analysis of non-vacuum states (squeezed, excited) near boundaries completed; clear statement of whether these evade the passivity no-go
2. If non-passive states exist: quantify maximum extractable work and identify the actual energy source (not ZPE)
3. Dynamic Casimir effect energy budget computed: E_photons vs W_mechanical for oscillating mirror
4. E_photons <= W_mechanical verified to < 10^{-6} relative error (photon energy sourced from mechanical work, not vacuum)
5. Each loophole mapped to the specific no-go assumption it targets; verdict stated with quantitative energy accounting

**Backtracking trigger:** If passivity analysis reveals that boundary-modulated Hamiltonians create genuinely non-passive states, this is a significant finding -- document carefully and assess whether it constitutes actual ZPE extraction or energy transfer from the modulation source

**Plans:** TBD

Plans:

- [ ] 06-01: TBD
- [ ] 06-02: TBD

### Phase 07: Synthesis and Conclusions

**Goal:** All results from Phases 01-06 are synthesized into a unified analysis that definitively answers the three core research questions with evidence and confidence levels
**Depends on:** All prior phases (01-06)
**Requirements:** All (synthesis)
**Contract Coverage:**
- Advances: claim-cycle-work, claim-nogo-consistency, claim-loophole-analysis (final assembly)
- Deliverables: All deliverables finalized and cross-referenced; unified analysis document
- Anchor coverage: All anchors cited; all benchmarks referenced in final verdict
- Forbidden proxies: All forbidden proxies checked against final claims
- Stop/rethink: If synthesis reveals inconsistencies between no-go arguments and numerical results, return to relevant phase
**Success Criteria** (what must be TRUE):

1. Research question Q1 answered: "Does a complete quasi-static Casimir plate cycle yield W_net <= 0?" with quantitative evidence from Phases 03-04
2. Research question Q2 answered: "Do the three no-go arguments require consistent assumptions?" with analysis from Phase 01
3. Research question Q3 answered: "Which loopholes are genuine vs apparent?" with verdicts and energy accounting from Phases 05-06
4. Comprehensive document produced with: executive summary, per-question evidence, confidence levels, and remaining open questions (including stretch goal directions)
5. All contract claims addressed: claim-cycle-work, claim-nogo-consistency, claim-loophole-analysis each have a definitive status (confirmed/refuted/inconclusive with explanation)

**Backtracking trigger:** If cross-referencing reveals that Phase 05/06 verdicts contradict Phase 01 no-go assumptions, revisit the inconsistent phases

**Plans:** TBD

Plans:

- [ ] 07-01: TBD

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
| --- | --- | --- | :---: |
| 01 - No-Go Theorem Derivations | -- | 02, 05, 06 | Yes |
| 02 - Casimir Force Computation | 01 | 03, 06 | Yes |
| 03 - Conservative Force Proof | 02 | 04, 05 | Yes |
| 04 - W_net Parameter Sweep | 03 | 07 | Yes |
| 05 - Boundary and Topology Loopholes | 01, 03 | 07 | No (parallel with 04, 06) |
| 06 - Non-Equilibrium and Dynamic Casimir | 01, 02 | 07 | No (parallel with 04, 05) |
| 07 - Synthesis | 04, 05, 06 | -- | Yes |

**Critical path:** 01 -> 02 -> 03 -> 04 -> 07 (5 sequential phases)

**Parallelizable after Phase 03 completes:**
- Phase 04 (parameter sweep), Phase 05 (boundary/topology loopholes), and Phase 06 (non-eq/dynamic loopholes) can run concurrently once their respective dependencies are met
- Phase 06 can begin after Phases 01 + 02 (does not need Phase 03)

**Execution order (respecting dependencies):**

```
Wave 1: Phase 01
Wave 2: Phase 02
Wave 3: Phase 03, Phase 06 (06 needs only 01+02)
Wave 4: Phase 04, Phase 05 (05 needs 01+03; 04 needs 03)
Wave 5: Phase 07
```

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | :---: | :---: | --- |
| 01 | Passivity theorem reference insufficient for rigorous QFT statement | MEDIUM | MEDIUM | Identify Pusz-Woronowicz (1978), Lenard (1978); if gap remains, state argument with explicit caveat |
| 02 | Catastrophic cancellation in Matsubara sum at large separations | MEDIUM | LOW | Use high-precision arithmetic (mpmath); verify against asymptotic expansion |
| 03 | Numerical W_net not exactly zero due to floating-point limits | LOW | LOW | Use relative tolerance 10^{-10}; verify convergence with increasing precision |
| 04 | 500k-point sweep computationally expensive | LOW | LOW | Vectorize; coarse scan first then refine near any anomalies |
| 05 | Energy cost of reflectivity change poorly constrained | MEDIUM | HIGH | Bound from below using thermodynamic minimum; if inconclusive, state as conditional result |
| 06 | Dynamic Casimir energy accounting requires full Bogoliubov computation | MEDIUM | MEDIUM | Use established parametric results first; full computation is stretch goal R4.3 |
| 07 | Inconsistency between no-go arguments and numerical results | LOW | HIGH | This would be a genuine discovery; document rigorously and verify independently |

## Progress

**Execution Order:**
Phases execute in numeric order: 01 -> 02 -> 03 -> (04, 05, 06 parallel where possible) -> 07

| Phase | Plans Complete | Status | Completed |
| --- | --- | --- | --- |
| 01. No-Go Theorem Derivations | 2/2 | Complete ✓ | 2026-03-22 |
| 02. Casimir Force Computation | 3/3 | Complete ✓ | 2026-03-22 |
| 03. Conservative Force Proof | 2/2 | Complete ✓ | 2026-03-22 |
| 04. W_net Parameter Sweep | 0/TBD | Not started | - |
| 05. Boundary and Topology Loopholes | 0/TBD | Not started | - |
| 06. Non-Equilibrium and Dynamic Casimir | 0/TBD | Not started | - |
| 07. Synthesis and Conclusions | 0/TBD | Not started | - |
