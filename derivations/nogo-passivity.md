# No-Go Argument C: Quantum Passivity (Pusz-Woronowicz)

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, regularization_scheme=zeta, casimir_force_sign=F<0_attractive, casimir_energy_sign=E<0_bounded, work_sign=W_net>0_extraction

## Assumptions

The following assumptions are required for this argument. Each is numbered for explicit reference and loophole identification.

- **C1 (Time-independent Hamiltonian):** The Hamiltonian $H$ of the system is time-independent throughout the cyclic operation. The potential energy landscape, including boundary conditions and material properties, does not change during the process.

- **C2 (Cyclic operation):** The operation is cyclic: the system's Hamiltonian at the end of the process is identical to the Hamiltonian at the beginning. The unitary evolution operator $U$ generates a transformation after which the system is governed by the same $H$.

- **C3 (Non-degenerate ground state):** The vacuum $|0\rangle$ is the unique ground state of $H$. That is, $H|0\rangle = E_0|0\rangle$ and $E_n > E_0$ for all excited states $|n\rangle$ with $n \geq 1$. There is no ground-state degeneracy.

- **C4 (Quantum mechanical framework):** The system is described by quantum mechanics with a well-defined Hamiltonian $H$ acting on a separable Hilbert space $\mathcal{H}$. The spectrum of $H$ is bounded below.

- **C5 (Same Hilbert space):** The unitary operator $U$ acts on the same Hilbert space $\mathcal{H}$ as $H$. No degrees of freedom are added or removed during the operation.

## Definition of Passivity

### The Concept

A quantum state $\rho$ of a system with Hamiltonian $H$ is called **passive** if no cyclic unitary operation can extract energy from it. Formally:

> **Definition (Passivity).** A state $\rho$ is passive with respect to Hamiltonian $H$ if for every unitary operator $U$ on $\mathcal{H}$:

$$
\text{Tr}(\rho\, H) \leq \text{Tr}(U\rho U^\dagger\, H)
\tag{C.1}
$$

Equivalently, the energy change under any unitary transformation is non-negative:

$$
\Delta E \equiv \text{Tr}(U\rho U^\dagger\, H) - \text{Tr}(\rho\, H) \geq 0
\tag{C.2}
$$

**Physical interpretation:** In a cyclic process (one that returns the Hamiltonian to its original form), the work extracted equals minus the energy change of the system: $W_{\text{extracted}} = -\Delta E$. Passivity means $W_{\text{extracted}} = -\Delta E \leq 0$: no work can be extracted.

$$
W_{\text{net}} = -\Delta E \leq 0 \quad \text{for a passive state}
\tag{C.3}
$$

**Dimensional check:** $[\text{Tr}(\rho H)] = [\text{energy}]$ since $\rho$ is dimensionless (density matrix) and $H$ has dimensions of energy. Correct.

## The Pusz-Woronowicz Theorem

### Statement

**Theorem (Pusz & Woronowicz, 1978).** A state $\rho$ is passive with respect to $H$ if and only if $\rho$ can be written as a decreasing function of $H$:

$$
\rho = f(H), \quad \text{where } f \text{ is non-increasing}
\tag{C.4}
$$

In the energy eigenbasis $H|n\rangle = E_n|n\rangle$ with $E_0 \leq E_1 \leq E_2 \leq \ldots$, this means:

$$
\langle n|\rho|n\rangle \geq \langle m|\rho|m\rangle \quad \text{whenever } E_n \leq E_m
\tag{C.5}
$$

Higher-energy states have equal or lower populations.

**Corollary:** The following states are passive:
- (a) The ground state $\rho = |0\rangle\langle 0|$ (zero temperature)
- (b) Any Gibbs (thermal) state $\rho = e^{-\beta H}/Z$ for $\beta \geq 0$
- (c) Any mixture of energy eigenstates with non-increasing populations

**Reference:** Pusz, W. & Woronowicz, S.L., *Passive states and KMS states for general quantum systems*, Commun. Math. Phys. **58**, 273--290 (1978) (ref-pusz-woronowicz).

**Independent confirmation:** Lenard, A., *Thermodynamical proof of the Gibbs formula for elementary quantum systems*, J. Stat. Phys. **19**, 575--586 (1978) (ref-lenard).

### Proof Sketch for Ground State Passivity

We prove directly that the ground state $|0\rangle$ is passive, without invoking the full Pusz-Woronowicz theorem.

**Given:** $H|n\rangle = E_n|n\rangle$ with $E_0 \leq E_1 \leq E_2 \leq \ldots$ and $\rho = |0\rangle\langle 0|$.

**Claim:** For any unitary $U$, $\langle 0|U^\dagger H U|0\rangle \geq E_0$.

**Proof:**

Let $|\psi\rangle = U|0\rangle$. Since $U$ is unitary, $|\psi\rangle$ is a normalized state: $\langle\psi|\psi\rangle = 1$.

Expand in the energy eigenbasis:

$$
|\psi\rangle = U|0\rangle = \sum_n c_n |n\rangle, \quad c_n = \langle n|U|0\rangle
\tag{C.6}
$$

Unitarity of $U$ guarantees normalization:

$$
\sum_n |c_n|^2 = \langle 0|U^\dagger U|0\rangle = \langle 0|0\rangle = 1
\tag{C.7}
$$

The energy expectation value in the transformed state is:

$$
\langle 0|U^\dagger H U|0\rangle = \langle\psi|H|\psi\rangle = \sum_n |c_n|^2 E_n
\tag{C.8}
$$

Since $E_n \geq E_0$ for all $n$ (by definition of the ground state):

$$
\sum_n |c_n|^2 E_n \geq E_0 \sum_n |c_n|^2 = E_0 \cdot 1 = E_0
\tag{C.9}
$$

Therefore:

$$
\Delta E = \langle 0|U^\dagger H U|0\rangle - \langle 0|H|0\rangle = \sum_n |c_n|^2 E_n - E_0 \geq 0
\tag{C.10}
$$

$$
\boxed{\Delta E \geq 0 \quad \Rightarrow \quad W_{\text{net}} = -\Delta E \leq 0 \quad \text{(ground state passivity)}}
\tag{C.11}
$$

**QED.** $\square$

**SELF-CRITIQUE CHECKPOINT (step 1):**
1. SIGN CHECK: $\Delta E \geq 0$ means energy increases under any unitary. $W_{\text{net}} = -\Delta E \leq 0$ means no work extraction. Signs consistent with the convention $W_{\text{net}} > 0$ = extraction.
2. FACTOR CHECK: No numerical factors in the proof — pure inequality from eigenvalue bounds.
3. CONVENTION CHECK: Using $W_{\text{net}} > 0$ = extraction per convention lock. Consistent.
4. DIMENSION CHECK: $[\Delta E] = [\text{energy}]$. $[W_{\text{net}}] = [\text{energy}]$. Correct.

**Equality condition:** $\Delta E = 0$ if and only if $|\psi\rangle = U|0\rangle = e^{i\phi}|0\rangle$ for some phase $\phi$. That is, $U$ acts trivially on the ground state (it at most introduces a global phase). Any non-trivial unitary that mixes the ground state with excited states strictly increases the energy.

### Limiting Case Verification

**Two-level system:** Consider $H = \text{diag}(E_0, E_1)$ with $E_0 < E_1$ and ground state $|0\rangle = (1, 0)^T$.

For a general $2\times 2$ unitary $U = \begin{pmatrix} \cos\theta\,e^{i\alpha} & -\sin\theta\,e^{i\beta} \\ \sin\theta\,e^{-i\beta} & \cos\theta\,e^{-i\alpha} \end{pmatrix}$:

$$
\langle 0|U^\dagger H U|0\rangle = \cos^2\theta\, E_0 + \sin^2\theta\, E_1 = E_0 + \sin^2\theta\,(E_1 - E_0)
\tag{C.12}
$$

Since $\sin^2\theta \geq 0$ and $E_1 - E_0 > 0$:

$$
\Delta E = \sin^2\theta\,(E_1 - E_0) \geq 0
\tag{C.13}
$$

Confirmed: the ground state is passive. Any rotation that mixes in the excited state increases the energy by exactly $\sin^2\theta\,(E_1 - E_0)$.

## Application to the QFT Vacuum

The QFT vacuum $|0\rangle$ is the ground state of the field Hamiltonian $H$. By assumption **C4**, $H$ is bounded below and has a well-defined spectrum. By assumption **C3**, $|0\rangle$ is the unique ground state.

Applying the ground state passivity result (Eq. C.11):

$$
W_{\text{net}} \leq 0 \quad \text{for any cyclic unitary applied to the QFT vacuum}
\tag{C.14}
$$

under assumptions C1--C5.

**Note on the value of $E_0$:** The absolute value of the vacuum energy $E_0 = \langle 0|H|0\rangle$ is irrelevant for the passivity argument. Whether $E_0$ is zero, positive, or negative (after renormalization), the inequality $\Delta E \geq 0$ holds. Passivity depends only on $|0\rangle$ being the state of lowest energy, not on the value of that energy.

This is an important distinction from the Lorentz invariance argument (Argument B), which discusses the vacuum energy density $\rho_{\text{vac}}$ as a specific quantity. Here, $\rho_{\text{vac}}$ cancels out.

## Complete Passivity (Stronger Result)

### Definition

A state $\rho$ is **completely passive** if $N$ copies of the state, $\rho^{\otimes N}$, are simultaneously passive for all $N$:

$$
\text{Tr}(\rho^{\otimes N}\, H_{\text{tot}}) \leq \text{Tr}(U_N\, \rho^{\otimes N}\, U_N^\dagger\, H_{\text{tot}}) \quad \forall\ U_N,\ \forall\ N
\tag{C.15}
$$

where $H_{\text{tot}} = \sum_{i=1}^N H_i$ is the total Hamiltonian for $N$ non-interacting copies.

### Significance

**Pusz-Woronowicz (1978):** A state $\rho$ is completely passive if and only if it is a Gibbs state $\rho = e^{-\beta H}/Z$ for some $\beta \geq 0$, or the ground state ($\beta \to \infty$).

The vacuum $|0\rangle$ is the ground state, hence it is completely passive. This rules out extraction schemes that:

- Use multiple copies of the vacuum state
- Correlate different spatial regions of the vacuum
- Exploit entanglement between subsystems of the vacuum

Complete passivity is strictly stronger than passivity: there exist passive states that are NOT completely passive (non-thermal states with decreasing populations). These can yield work if multiple copies are processed jointly. But the vacuum, being a ground state (equivalently, a Gibbs state at $\beta \to \infty$), does not have this vulnerability.

**SELF-CRITIQUE CHECKPOINT (step 2):**
1. SIGN CHECK: Complete passivity strengthens the no-go. $W_{\text{net}} \leq 0$ for $N$-copy operations. Consistent.
2. FACTOR CHECK: No numerical factors.
3. CONVENTION CHECK: Work sign convention maintained.
4. DIMENSION CHECK: $H_{\text{tot}}$ has dimensions of energy. Correct.

## Critical Gap: Time-Dependent Hamiltonian

The passivity argument requires assumption **C1** (time-independent $H$). When Casimir plates move, the Hamiltonian changes in time:

$$
H(t) = H(a(t))
\tag{C.16}
$$

where $a(t)$ is the plate separation as a function of time. The Pusz-Woronowicz theorem does **not** directly apply to this situation.

### What Happens with Time-Dependent $H$

1. **Instantaneous ground state:** At each time $t$, $H(a(t))$ has an instantaneous ground state $|0(t)\rangle$ with energy $E_0(a(t))$.

2. **Actual state evolution:** The actual state $|\psi(t)\rangle$ evolves by the Schrödinger equation:

$$
i\frac{\partial}{\partial t}|\psi(t)\rangle = H(a(t))|\psi(t)\rangle
\tag{C.17}
$$

If the process starts in the ground state $|\psi(0)\rangle = |0(t=0)\rangle$, the actual state generally does NOT remain the instantaneous ground state: $|\psi(t)\rangle \neq |0(t)\rangle$.

3. **Adiabatic limit:** If $a(t)$ changes slowly compared to the gap $\Delta E(a) = E_1(a) - E_0(a)$, the adiabatic theorem guarantees $|\psi(t)\rangle \approx e^{i\phi(t)}|0(t)\rangle$ up to exponentially small corrections. In this limit, the system tracks the instantaneous ground state and no excitations are produced.

4. **Non-adiabatic regime (Dynamic Casimir Effect):** If $a(t)$ changes rapidly (on a timescale $\sim 1/\Delta E$ or faster), excitations are produced: photons are created from the vacuum. This is the **dynamic Casimir effect** (Moore, 1970; Fulling & Davies, 1976; experimentally observed by Wilson et al., 2011).

### Energy Accounting for the Dynamic Casimir Effect

The key question is: where does the energy for the created photons come from?

**Answer:** The energy comes from the mechanical work done by the agent moving the plates, not from the vacuum itself.

The work done by the external agent is:

$$
W_{\text{agent}} = \int_0^T \dot{a}(t)\, F_{\text{total}}(a(t), |\psi(t)\rangle)\, dt
\tag{C.18}
$$

where $F_{\text{total}}$ includes both the Casimir force and the radiation reaction force. By energy conservation:

$$
W_{\text{agent}} = \underbrace{E_{\text{Cas}}(a(T)) - E_{\text{Cas}}(a(0))}_{\text{Casimir energy change}} + \underbrace{E_{\text{photons}}}_{\text{created photons}} + \underbrace{E_{\text{excitations}}}_{\text{residual field excitations}}
\tag{C.19}
$$

For a cyclic process ($a(T) = a(0)$), the Casimir energy change vanishes, and:

$$
W_{\text{agent}} = E_{\text{photons}} + E_{\text{excitations}} \geq 0
\tag{C.20}
$$

The external agent must input at least as much energy as the photons carry away. This is consistent with $W_{\text{net}} \leq 0$ (the system does not yield net work to the agent), but the mechanism is different from the static passivity argument.

**Open question:** Can the gap between $|\psi(t)\rangle$ and $|0(t)\rangle$ ever be exploited for net energy extraction? The adiabatic theorem says no in the slow limit; the dynamic Casimir analysis says the agent pays for the photons in the fast limit. But a rigorous proof covering all intermediate regimes remains open. This is the central question for Phase 06 (dynamic Casimir loophole analysis).

**SELF-CRITIQUE CHECKPOINT (step 3):**
1. SIGN CHECK: $W_{\text{agent}} \geq 0$ means the agent puts in work, not extracts. Consistent with $W_{\text{net}} \leq 0$ for the agent.
2. FACTOR CHECK: No numerical factors in the energy accounting.
3. CONVENTION CHECK: $W_{\text{net}} > 0$ = extraction. $W_{\text{agent}} \geq 0$ = agent inputs energy. These are consistent: the agent does NOT extract net work.
4. DIMENSION CHECK: $[W_{\text{agent}}] = [\text{energy}]$, $[E_{\text{photons}}] = [\text{energy}]$. Correct.

## Connection to Work Extraction Theory

**Allahverdyan, Balian, and Nieuwenhuizen (2004)** showed that the maximum work extractable from a quantum system in state $\rho$ by cyclic unitary operations is:

$$
W_{\max} = \text{Tr}(\rho H) - \text{Tr}(\pi(\rho) H)
\tag{C.21}
$$

where $\pi(\rho)$ is the **passive counterpart** of $\rho$ — the state obtained by rearranging the eigenvalues of $\rho$ in decreasing order with respect to the energy eigenstates.

For the vacuum $\rho = |0\rangle\langle 0|$, which is already passive ($\rho = \pi(\rho)$):

$$
W_{\max} = \text{Tr}(\rho H) - \text{Tr}(\rho H) = 0
\tag{C.22}
$$

No work can be extracted because the vacuum is already in its optimal (passive) configuration. There is no "rearrangement" that would lower its energy.

## Summary of Argument C

| Element | Content |
|---|---|
| **Conclusion** | $W_{\text{net}} \leq 0$ for any cyclic unitary operation on the QFT vacuum with fixed Hamiltonian |
| **Method** | Ground state passivity: $\sum_n |c_n|^2 E_n \geq E_0$ by spectral bound. Complete passivity rules out multi-copy schemes. |
| **Assumptions** | C1--C5 (numbered above) |
| **Key loophole** | C1 (time-independent $H$) — violated when Casimir plates move, leading to the dynamic Casimir effect |
| **Strength** | Most rigorous: applies to ALL cyclic unitaries, not just quasi-static processes. Ground state passivity proof is elementary and exact. |
| **Weakness** | Requires fixed $H$; the time-dependent case (moving boundaries) is the physically relevant Casimir scenario |
| **References** | Pusz & Woronowicz (1978) (ref-pusz-woronowicz); Lenard (1978) (ref-lenard); Allahverdyan et al. (2004) |
