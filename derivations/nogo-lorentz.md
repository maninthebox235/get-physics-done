# No-Go Argument B: Lorentz Invariance

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, regularization_scheme=zeta, casimir_force_sign=F<0_attractive, casimir_energy_sign=E<0_bounded, work_sign=W_net>0_extraction

## Assumptions

The following assumptions are required for this argument. Each is numbered for explicit reference and loophole identification.

- **B1 (Poincaré invariance of the vacuum):** The vacuum state $|0\rangle$ is the unique state annihilated by all annihilation operators of the quantum field theory, and is invariant under the full Poincaré group: $U(\Lambda, a)|0\rangle = |0\rangle$ for all proper orthochronous Lorentz transformations $\Lambda$ and spacetime translations $a^\mu$.

- **B2 (No boundaries or external fields):** The spacetime is Minkowski space $\mathbb{R}^{3,1}$ with no boundaries, defects, or background fields that would break translational or rotational invariance. The quantum fields propagate freely.

- **B3 (Well-defined stress-energy tensor):** The renormalized vacuum expectation value $\langle 0|T^{\mu\nu}(x)|0\rangle$ is a well-defined, finite, Lorentz-covariant quantity. Any regularization scheme used to define it preserves the Poincaré symmetry of the vacuum.

- **B4 (Local Poincaré-covariant QFT):** The system is described by a local quantum field theory satisfying the Wightman axioms (or equivalent). In particular, the stress-energy tensor $T^{\mu\nu}(x)$ transforms as a rank-2 symmetric tensor under Lorentz transformations: $U(\Lambda)T^{\mu\nu}(x)U(\Lambda)^{-1} = \Lambda^{\mu}{}_{\rho}\Lambda^{\nu}{}_{\sigma}T^{\rho\sigma}(\Lambda x)$.

## Derivation of the Vacuum Stress-Energy Tensor

### Step 1: Poincaré Invariance Constrains $\langle 0|T^{\mu\nu}|0\rangle$

By assumption **B1**, the vacuum is Poincaré-invariant. By assumption **B4**, $T^{\mu\nu}$ transforms as a Lorentz tensor. Consider the vacuum expectation value:

$$
\langle 0|T^{\mu\nu}(x)|0\rangle
\tag{B.1}
$$

**Translation invariance** (from B1 and B2): Under a spacetime translation $x \to x + a$, the vacuum is invariant, so

$$
\langle 0|T^{\mu\nu}(x + a)|0\rangle = \langle 0|U(a)^{-1}T^{\mu\nu}(x+a)U(a)|0\rangle = \langle 0|T^{\mu\nu}(x)|0\rangle
\tag{B.2}
$$

for all $a^\mu$. Therefore $\langle 0|T^{\mu\nu}(x)|0\rangle$ is independent of $x$: it is a constant tensor.

$$
\langle 0|T^{\mu\nu}(x)|0\rangle = C^{\mu\nu} = \text{const.}
\tag{B.3}
$$

**Dimensional check:** $[T^{\mu\nu}] = [\text{energy}/\text{volume}] = [\text{length}^{-4}]$ in natural units. $C^{\mu\nu}$ must have these dimensions. Correct — it can be proportional to $g^{\mu\nu}$ times a dimensionful constant $\rho_{\text{vac}}$ with $[\rho_{\text{vac}}] = [\text{length}^{-4}]$.

### Step 2: Lorentz Invariance Determines the Tensor Structure

**Lorentz invariance** (from B1 and B4): Under a Lorentz transformation $\Lambda$:

$$
\langle 0|T^{\mu\nu}(x)|0\rangle = \langle 0|U(\Lambda)^{-1}T^{\mu\nu}(\Lambda x)U(\Lambda)|0\rangle = \Lambda^{\mu}{}_{\rho}\Lambda^{\nu}{}_{\sigma}\langle 0|T^{\rho\sigma}(\Lambda x)|0\rangle
\tag{B.4}
$$

Since $C^{\mu\nu}$ is a constant (independent of $x$ by Step 1), this gives:

$$
C^{\mu\nu} = \Lambda^{\mu}{}_{\rho}\Lambda^{\nu}{}_{\sigma}C^{\rho\sigma} \quad \forall\ \Lambda \in SO^+(1,3)
\tag{B.5}
$$

This states that $C^{\mu\nu}$ is an **invariant tensor** of the Lorentz group. We must identify all rank-2 symmetric tensors invariant under $SO^+(1,3)$.

**Claim:** The only rank-2 symmetric Lorentz-invariant tensor is proportional to the metric tensor $g^{\mu\nu}$.

**Proof:** The Lorentz group $SO^+(1,3)$ is a simple Lie group. A symmetric rank-2 tensor can be decomposed into irreducible representations of the Lorentz group:
- A trace part (scalar): $\sim g^{\mu\nu}$
- A traceless symmetric part: 9-dimensional representation

An invariant tensor must transform trivially (as a singlet). Only the trace part $g^{\mu\nu}$ is a singlet — the traceless symmetric part transforms non-trivially. To verify: under a boost in the $z$-direction with rapidity $\phi$, the component $C^{03}$ transforms as $C^{03} \to \cosh\phi\,\sinh\phi\,(C^{00} + C^{33}) + (\cosh^2\phi + \sinh^2\phi)C^{03}$. For this to equal $C^{03}$ for all $\phi$, we need $C^{00} + C^{33} = 0$ and $C^{03} = 0$. Similarly, examining rotations and other boosts forces $C^{\mu\nu} \propto g^{\mu\nu}$.

Therefore:

$$
\langle 0|T^{\mu\nu}|0\rangle = \rho_{\text{vac}}\, g^{\mu\nu}
\tag{B.6}
$$

where $\rho_{\text{vac}}$ is the vacuum energy density (a single number).

**Verification of Eq. (B.6):** Check that $g^{\mu\nu}$ itself is Lorentz-invariant: $\Lambda^{\mu}{}_{\rho}\Lambda^{\nu}{}_{\sigma}g^{\rho\sigma} = g^{\mu\nu}$ by the defining property of Lorentz transformations. Confirmed.

**Reference:** This result follows the argument in Weinberg, *The Quantum Theory of Fields*, Vol. 1, §11.2 (ref-weinberg-qft).

**SELF-CRITIQUE CHECKPOINT (step 1):**
1. SIGN CHECK: No sign ambiguity in Eq. (B.6) yet — just a proportionality constant $\rho_{\text{vac}}$.
2. FACTOR CHECK: No factors of $2$, $\pi$, $\hbar$, or $c$ introduced. Pure group theory argument.
3. CONVENTION CHECK: Using mostly-minus metric $g^{\mu\nu} = \text{diag}(+1,-1,-1,-1)$. Consistent with convention lock.
4. DIMENSION CHECK: $[\rho_{\text{vac}} \cdot g^{\mu\nu}] = [\text{length}^{-4}] \cdot [\text{dimensionless}] = [\text{length}^{-4}]$. Matches $[T^{\mu\nu}]$. Correct.

### Step 3: Equation of State of the Vacuum

From Eq. (B.6), read off the components in the rest frame with $g^{\mu\nu} = \text{diag}(+1,-1,-1,-1)$:

**Energy density:**

$$
\langle 0|T^{00}|0\rangle = \rho_{\text{vac}} \cdot g^{00} = +\rho_{\text{vac}}
\tag{B.7}
$$

**Pressure:** The stress-energy tensor for a perfect fluid at rest is $T^{\mu\nu} = \text{diag}(\rho, p, p, p)$ in the rest frame (with mostly-minus metric, $T^{ii} = -p \cdot g^{ii} \cdot g^{ii}$... let us be careful).

For a perfect fluid: $T^{\mu\nu} = (\rho + p)u^\mu u^\nu - p\, g^{\mu\nu}$ where $u^\mu = (1,0,0,0)$ in the rest frame. This gives:

$$
T^{00} = \rho + p - p \cdot g^{00} = \rho + p - p = \rho
$$

$$
T^{ii} = -p \cdot g^{ii} = -p \cdot (-1) = p \quad (i = 1,2,3)
\tag{B.8}
$$

Wait — let me be more careful with the metric convention. With $g^{\mu\nu} = \text{diag}(+1,-1,-1,-1)$:

The perfect fluid stress-energy tensor is:

$$
T^{\mu\nu} = (\rho + p)u^\mu u^\nu + p\, g^{\mu\nu}
$$

Note the sign: the standard form has $+p\,g^{\mu\nu}$, not $-p\,g^{\mu\nu}$, when the pressure appears with the metric. (The alternative form $T_{\mu\nu} = (\rho+p)u_\mu u_\nu + p\,g_{\mu\nu}$ applies for the lowered-index version with either signature convention.) In the rest frame $u^\mu = (1,0,0,0)$:

$$
T^{00} = (\rho + p) \cdot 1 + p \cdot (+1) = \rho + 2p
$$

This gives the wrong result. Let me re-derive carefully.

The standard perfect fluid form with $g_{\mu\nu} = \text{diag}(+1,-1,-1,-1)$ is:

$$
T^{\mu\nu} = (\rho + p)u^\mu u^\nu - p\, g^{\mu\nu}
$$

In the rest frame:

$$
T^{00} = (\rho + p)(1)(1) - p(+1) = \rho + p - p = \rho
$$

$$
T^{11} = 0 - p(-1) = p
$$

$$
T^{22} = p, \quad T^{33} = p
$$

So $T^{\mu\nu} = \text{diag}(\rho, p, p, p)$. This is the standard result.

Now comparing with the vacuum form $T^{\mu\nu} = \rho_{\text{vac}}\,g^{\mu\nu} = \text{diag}(\rho_{\text{vac}}, -\rho_{\text{vac}}, -\rho_{\text{vac}}, -\rho_{\text{vac}})$:

$$
T^{00} = \rho_{\text{vac}} = \rho \quad \Rightarrow \quad \rho = \rho_{\text{vac}}
$$

$$
T^{11} = -\rho_{\text{vac}} = p \quad \Rightarrow \quad p_{\text{vac}} = -\rho_{\text{vac}}
\tag{B.9}
$$

$$
\boxed{p_{\text{vac}} = -\rho_{\text{vac}}}
\tag{B.10}
$$

This is the equation of state of a cosmological constant: $w = p/\rho = -1$.

**SELF-CRITIQUE CHECKPOINT (step 2):**
1. SIGN CHECK: $p_{\text{vac}} = -\rho_{\text{vac}}$. For positive $\rho_{\text{vac}}$ (positive vacuum energy), the pressure is negative. This is the standard dark energy equation of state. Correct.
2. FACTOR CHECK: No numerical factors introduced.
3. CONVENTION CHECK: $g^{\mu\nu} = \text{diag}(+1,-1,-1,-1)$ used consistently. Mostly-minus per convention lock.
4. DIMENSION CHECK: $[p] = [\text{energy}/\text{volume}] = [\rho]$. The equation $p = -\rho$ is dimensionally consistent.

### Step 4: Non-Extractability of Vacuum Energy

Consider attempting to extract work from the vacuum by a piston-like process — compressing or expanding a volume $V$ of vacuum.

For a fluid with equation of state $p = -\rho$, the first law of thermodynamics gives:

$$
dU = -p\,dV = +\rho_{\text{vac}}\,dV
\tag{B.11}
$$

Since $U = \rho_{\text{vac}} V$ for a uniform energy density:

$$
dU = \rho_{\text{vac}}\,dV
\tag{B.12}
$$

Equations (B.11) and (B.12) are consistent: the vacuum energy density remains constant as the volume changes. The vacuum "fills in" behind any expansion, maintaining uniform $\rho_{\text{vac}}$ everywhere.

The work done by the vacuum on a piston during expansion $dV > 0$:

$$
\delta W = p_{\text{vac}}\,dV = -\rho_{\text{vac}}\,dV
\tag{B.13}
$$

The energy change of the vacuum:

$$
dU = \rho_{\text{vac}}\,dV
\tag{B.14}
$$

Therefore the total energy budget is:

$$
dU + \delta W = \rho_{\text{vac}}\,dV + (-\rho_{\text{vac}}\,dV) = 0
\tag{B.15}
$$

The vacuum replenishes its energy exactly. No net work can be extracted from or deposited into a $p = -\rho$ medium through volume changes. Over any closed cycle:

$$
\boxed{W_{\text{net}} = \oint p_{\text{vac}}\,dV = 0 \quad \text{(Lorentz-invariant vacuum)}}
\tag{B.16}
$$

**Physical interpretation:** A medium with $p = -\rho$ has the remarkable property that its energy density is unchanged by expansion or compression. It is thermodynamically "inert" — there is no way to extract energy from it by mechanical work, because any work done by the pressure is exactly compensated by the change in internal energy. This is precisely the behavior of the cosmological constant in general relativity.

**SELF-CRITIQUE CHECKPOINT (step 3):**
1. SIGN CHECK: $W_{\text{net}} = 0$. No extraction. Consistent with no-go claim.
2. FACTOR CHECK: No new factors.
3. CONVENTION CHECK: $W_{\text{net}} > 0$ = extraction convention maintained. Result is $W_{\text{net}} = 0$, not positive.
4. DIMENSION CHECK: $[p\,dV] = [\text{energy/volume}][\text{volume}] = [\text{energy}]$. Correct.

## Critical Caveat: Failure for Bounded Systems

**This argument does NOT apply to the Casimir configuration.**

The key assumption **B2** requires no boundaries. In a Casimir cavity:

1. **Translational invariance is broken** by the presence of the plates. The vacuum expectation value $\langle 0|T^{\mu\nu}(x)|0\rangle$ depends on the position $x$ relative to the plates — it is NOT a constant tensor.

2. **The stress-energy tensor between the plates** is anisotropic: the pressure perpendicular to the plates differs from the pressure parallel to them. Specifically, for ideal plates at separation $a$ (Boyer, 1968; Brown & Maclay, 1969):

$$
\langle T^{00}\rangle = -\frac{\pi^2}{720\,a^4}, \quad
\langle T^{zz}\rangle = +\frac{\pi^2}{240\,a^4}, \quad
\langle T^{xx}\rangle = \langle T^{yy}\rangle = -\frac{\pi^2}{720\,a^4}
\tag{B.17}
$$

(Here $z$ is perpendicular to the plates, and the components are given after subtraction of the free-space divergent contribution.)

**Dimensional check on Eq. (B.17):** All components have $[\text{length}^{-4}]$. Correct.

**Sign check on Eq. (B.17):** The perpendicular pressure $\langle T^{zz}\rangle > 0$ acts to push the plates together (in our convention where the outward normal points toward increasing $a$, a positive $T^{zz}$ inside corresponds to an attractive force). The energy density $\langle T^{00}\rangle < 0$ is negative, as expected from our energy sign convention (E < 0 for bounded configuration).

Note that $\langle T^{\mu\nu}\rangle$ is NOT proportional to $g^{\mu\nu}$ between the plates: $T^{00} \neq T^{xx}$ in magnitude, and $T^{zz}$ has a different sign from $T^{00}$. Lorentz invariance is broken by the boundary conditions.

3. **The Casimir force exists precisely because** the vacuum between plates is NOT Lorentz-invariant. The modification of the mode structure by boundaries creates a non-trivial, position-dependent vacuum energy that gives rise to a measurable force.

**Connection to loopholes:** The boundary condition loophole (to be analyzed in Phase 05, loophole class R3.1) targets assumption **B2** directly. The Casimir effect is the prototypical example of boundary conditions creating vacuum energy differences, and Argument B is the prototypical example of a no-go that fails for bounded systems.

**Reference:** Jaffe, Phys. Rev. D 72, 021301 (2005) (ref-jaffe) argues that the Casimir effect can be understood entirely in terms of relativistic van der Waals forces between the plate material, without any reference to vacuum energy. This perspective is consistent with Argument B: the "vacuum energy" between the plates is an artifact of the boundary conditions, not a property of the vacuum itself.

## Summary of Argument B

| Element | Content |
|---|---|
| **Conclusion** | $W_{\text{net}} = 0$ for any process attempting to extract energy from the free (unbounded) Lorentz-invariant vacuum |
| **Method** | Poincaré invariance $\Rightarrow$ $\langle 0|T^{\mu\nu}|0\rangle = \rho_{\text{vac}} g^{\mu\nu}$ $\Rightarrow$ $p = -\rho$ $\Rightarrow$ no net work extraction |
| **Assumptions** | B1--B4 (numbered above) |
| **Key loophole** | B2 (no boundaries) — the Casimir effect exists precisely because boundaries break this assumption |
| **Strength** | Elegant, fundamental, connects to cosmological constant problem |
| **Weakness** | Does not apply to bounded systems (the physically interesting Casimir case) |
| **References** | Weinberg, QFT Vol. 1, §11.2 (ref-weinberg-qft); Jaffe (2005) (ref-jaffe) |
