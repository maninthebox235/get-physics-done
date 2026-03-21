---
gpd_role: phase-research
phase: 01
phase_name: No-Go Theorem Derivations
---

# Research: Phase 01 — No-Go Theorem Derivations

## 1. Three No-Go Arguments: Mathematical Frameworks

### Argument A: Thermodynamic (Second Law)

**Framework:** Classical thermodynamics applied to quantum vacuum
**Core logic:**
1. The quantum vacuum at T=0 is the ground state — the state of minimum free energy
2. For any cyclic process returning the system to its initial state: W_net ≤ -ΔF = 0
3. The Clausius inequality for a cyclic process at T=0: ∮ δQ/T ≤ 0 → W_net ≤ 0

**Key assumptions to number:**
- A1: The vacuum is a well-defined thermodynamic equilibrium state
- A2: The system (Casimir plates + vacuum) forms a closed system during the cycle
- A3: The second law of thermodynamics applies to quantum systems at T=0
- A4: The process is quasi-static (can be relaxed to any cyclic process)
- A5: The initial and final states are identical (cycle closes)

**Derivation approach:**
- Start from Helmholtz free energy F(a, T) for parallel plates
- For quasi-static cycle: W_net = ∮ F_Casimir · da where F_Casimir = -∂F/∂a
- If F_Casimir is conservative (depends only on a), then ∮ F · da = 0 identically
- Even for non-conservative generalization: second law gives W_net ≤ 0

**Key reference:** Standard thermodynamics; the application to Casimir is essentially the observation that a conservative force cannot do net work over a cycle. Formally related to the Kelvin-Planck statement.

**Strength:** Intuitive and robust, but assumes thermal equilibrium and quasi-static processes
**Weakness:** Does not apply to non-equilibrium processes or systems with time-dependent Hamiltonians

### Argument B: Lorentz Invariance

**Framework:** Relativistic QFT, vacuum expectation values
**Core logic:**
1. The vacuum |0⟩ is Poincaré-invariant: U(Λ)|0⟩ = |0⟩
2. Therefore ⟨0|T^{μν}|0⟩ must be a Lorentz-invariant tensor
3. The only rank-2 Lorentz-invariant tensor is g^{μν}: ⟨0|T^{μν}|0⟩ = ρ_vac g^{μν}
4. This gives equation of state p = -ρ (cosmological constant form)
5. A medium with p = -ρ cannot do work on an external system in a standard thermodynamic cycle

**Key assumptions to number:**
- B1: Poincaré invariance of the vacuum state
- B2: No boundaries or external fields (free vacuum)
- B3: T^{μν} is well-defined (regularization-independent for the vacuum)
- B4: The system can be described by a local QFT

**Derivation approach:**
- Start from Poincaré invariance of |0⟩
- Prove ⟨0|T^{μν}|0⟩ = ρ_vac g^{μν} using the transformation properties of T^{μν}
- Show that p = -ρ_vac means the vacuum "pushes back" on any extraction attempt
- For a piston in vacuum: W = ∫ p dV but the vacuum pressure is isotropic and uniform → no differential to exploit

**Critical caveat:** Boundaries break translational invariance! The Casimir effect exists precisely because boundaries create a non-trivial vacuum structure. This argument applies to the unbounded vacuum but NOT directly to a Casimir cavity.

**Key references:**
- Weinberg, "The Quantum Theory of Fields" Vol 1, §11.2 — vacuum energy and Lorentz invariance
- Jaffe, Phys. Rev. D 72, 021301 (2005) — "Casimir effect and the quantum vacuum" — argues Casimir force can be understood without reference to vacuum energy

**Strength:** Elegant and fundamental
**Weakness:** Does not apply to bounded systems (which is exactly the Casimir configuration)

### Argument C: Quantum Passivity (Pusz-Woronowicz)

**Framework:** C*-algebraic quantum mechanics, KMS states
**Core logic:**
1. A state ρ is **passive** if no cyclic unitary operation can extract work: Tr(ρH) ≤ Tr(UρU†H) for all unitaries U
2. **Theorem (Pusz-Woronowicz 1978):** A state ρ is passive if and only if it is a Gibbs state ρ = e^{-βH}/Z or a ground state (β→∞)
3. The vacuum |0⟩ is the ground state of the QFT Hamiltonian → it is passive
4. Therefore: no cyclic unitary operation on the vacuum can extract positive work

**Key assumptions to number:**
- C1: The Hamiltonian H is fixed (time-independent) throughout the cycle
- C2: The operation is cyclic: the unitary U satisfies U(T) = 1 at the end of the cycle
- C3: The vacuum is the ground state of H (no degeneracy issues)
- C4: The system is described by a quantum mechanical framework with well-defined H

**Proof sketch:**
- Let H|0⟩ = E_0|0⟩ be the ground state
- For any unitary U: ⟨0|U†HU|0⟩ = Σ_n |⟨n|U|0⟩|² E_n ≥ E_0 Σ_n |⟨n|U|0⟩|² = E_0
- Therefore: ΔE = ⟨0|U†HU|0⟩ - ⟨0|H|0⟩ ≥ 0
- Interpretation: the energy of the system can only increase → work was put IN, not extracted

**Critical gap:** Assumption C1 (fixed H). When boundaries move, the Hamiltonian changes: H = H(a(t)). The Pusz-Woronowicz theorem applies to fixed H. For time-dependent H, one needs the concept of **complete passivity** and the analysis becomes more subtle.

**Key references:**
- Pusz & Woronowicz, Commun. Math. Phys. 58, 273 (1978) — original passivity theorem
- Lenard, J. Stat. Phys. 19, 575 (1978) — independent passivity result
- Allahverdyan, Balian, Nieuwenhuizen, Europhys. Lett. 67, 565 (2004) — work extraction from quantum systems
- Gallego, Eisert, Wilming, New J. Phys. 18, 103017 (2016) — thermodynamic work from operational principles

**Strength:** Most rigorous of the three — applies to any cyclic unitary, not just quasi-static
**Weakness:** Requires fixed Hamiltonian; the gap for time-dependent H is the key open question

## 2. Comparison Table Structure

The comparison table should have columns:
| Argument | Key Assumptions | What It Proves | Known Loopholes | Strength Rating |

**Overlap analysis:**
- All three assume the vacuum is a special state (ground/equilibrium/Poincaré-invariant)
- Thermodynamic and passivity both assume cyclic process
- Lorentz invariance is the only one that doesn't require a cycle — but it fails for bounded systems
- Passivity is strongest (covers non-quasi-static) but requires fixed H
- Thermodynamic is most practical but weakest (quasi-static, equilibrium)

**Consistency check:**
- No contradictions found: the three arguments make different but compatible assumptions
- They are genuinely complementary: each covers cases the others don't
- The "gap" where none applies: time-dependent H with boundaries (dynamic Casimir regime)

## 3. Derivation Strategy

### Recommended approach for each argument:

**Argument A (Thermodynamic):**
1. State the second law for cyclic processes at T=0
2. Define the Casimir system: plates at separation a, vacuum field between them
3. Define the cycle: close plates (a_max → a_min), open plates (a_min → a_max)
4. Show W_net = ∮ F(a) da = 0 for conservative F(a)
5. Generalize: even for non-conservative processes, W_net ≤ 0 by Kelvin-Planck
6. Number all assumptions explicitly

**Argument B (Lorentz Invariance):**
1. State Poincaré invariance of |0⟩
2. Derive ⟨0|T^{μν}|0⟩ = ρ_vac g^{μν}
3. Show p = -ρ_vac (equation of state)
4. Argue this prohibits work extraction from uniform vacuum
5. Explicitly identify where the argument fails for bounded systems
6. Number all assumptions

**Argument C (Passivity):**
1. Define passivity: Tr(ρ[H - U†HU]) ≤ 0 for all U
2. State Pusz-Woronowicz theorem (cite, proof sketch)
3. Verify vacuum satisfies conditions (ground state of fixed H)
4. Conclude: no cyclic unitary on vacuum extracts work
5. Explicitly identify the gap: what happens when H = H(t)?
6. Number all assumptions

**Comparison table:**
- Compile after all three derivations
- Check each assumption pair for consistency
- Identify the "coverage diagram" — which physical scenarios each argument covers

## 4. Key References (Targeted)

1. **Pusz & Woronowicz (1978)** — Commun. Math. Phys. 58, 273 — Passivity theorem (MUST READ)
2. **Lenard (1978)** — J. Stat. Phys. 19, 575 — Independent passivity result
3. **Ford (1993)** — Phys. Rev. D 48, 776 — Quantum restrictions on energy extraction
4. **Jaffe (2005)** — Phys. Rev. D 72, 021301 — Casimir effect without vacuum energy
5. **Allahverdyan et al. (2004)** — Europhys. Lett. 67, 565 — Work extraction from quantum systems
6. **Weinberg, QFT Vol 1** — §11.2 for Lorentz invariance of vacuum energy-momentum tensor
7. **Scandurra (2001)** — hep-th/0104127 — Conservative nature of Casimir force (relevant for Argument A)

## 5. Dimensional Analysis and Scales

**Key energy scale:** Casimir energy per unit area E/A = -π²/(720 a³) in natural units
- At a = 100 nm: E/A ≈ -1.3 × 10⁻³ J/m² = -1.3 mJ/m²
- Force per unit area: F/A = -π²/(240 a⁴)
- At a = 100 nm: F/A ≈ -1.3 × 10⁻³ N/m² ≈ -1 Pa

**Thermal scale:** k_BT at 300K ≈ 0.026 eV; thermal wavelength λ_T = ℏc/(k_BT) ≈ 7.6 μm
- For a << λ_T: quantum regime (T=0 analysis sufficient)
- For a >> λ_T: classical regime (thermal corrections dominate)
- Phase 01 primarily works in the T=0 or formal limit

## 6. Risks and Mitigations

| Risk | Probability | Mitigation |
|------|-------------|------------|
| Passivity theorem literature too abstract for concrete Casimir application | MEDIUM | Focus on the proof sketch in §3 above; cite rather than reproduce the full C*-algebraic proof |
| Lorentz invariance argument appears trivially inapplicable to bounded systems | LOW | This is expected — the value is in explicitly identifying WHERE it fails, which maps to loopholes |
| Comparison table reveals tension between arguments | LOW | This would be a finding, not a problem — document carefully |
| Derivations are "too easy" (just citing known results) | MEDIUM | Add value by: (a) numbering assumptions, (b) identifying gaps, (c) mutual consistency check |

## RESEARCH COMPLETE
