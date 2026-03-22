# No-Go Argument A: Thermodynamic (Second Law)

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, regularization_scheme=zeta, casimir_force_sign=F<0_attractive, casimir_energy_sign=E<0_bounded, work_sign=W_net>0_extraction

## Assumptions

The following assumptions are required for this argument. Each is numbered for explicit reference and loophole identification.

- **A1 (Closed system):** The vacuum electromagnetic field plus the Casimir plates form a closed thermodynamic system. No external energy source couples to the system during the cycle.

- **A2 (Conservative force):** The Casimir force $F_{\text{Cas}}(a)$ depends only on the instantaneous plate separation $a$ (and on fixed material properties and temperature $T$). It is therefore a conservative force in the configuration space parameterized by $a$.

- **A3 (Fixed material properties):** The material properties of the plates (permittivity $\varepsilon(\omega)$, conductivity, geometry) remain unchanged throughout the cycle. The plates do not undergo phase transitions, chemical reactions, or structural changes.

- **A4 (Second law at $T = 0$):** The second law of thermodynamics, in the Kelvin--Planck form, applies to quantum systems at zero temperature. No cyclic process exists whose sole result is the conversion of heat from a single reservoir into work.

- **A5 (Cyclic process):** The process is cyclic: the system returns to its exact initial configuration at the end of one cycle. The plate separation, material state, and field state all return to their initial values.

## Setup

Consider two parallel, perfectly conducting plates of area $\mathcal{A}$ separated by a distance $a$ in the $z$-direction. The quantum electromagnetic field is confined between and around the plates.

At zero temperature, the Casimir energy per unit area for ideal parallel plates is (Casimir, 1948):

$$
\frac{E_{\text{Cas}}(a)}{\mathcal{A}} = -\frac{\pi^2}{720\, a^3}
\tag{A.1}
$$

**Dimensional check:** In natural units ($\hbar = c = 1$), $[E/\mathcal{A}] = [\text{energy}/\text{length}^2] = [\text{length}^{-3}]$. Since $[\pi^2/(720\,a^3)] = [\text{length}^{-3}]$, Eq. (A.1) is dimensionally correct.

The Casimir force per unit area is:

$$
\frac{F_{\text{Cas}}(a)}{\mathcal{A}} = -\frac{\partial}{\partial a}\frac{E_{\text{Cas}}(a)}{\mathcal{A}} = -\frac{\pi^2}{240\, a^4}
\tag{A.2}
$$

**Sign check:** $F_{\text{Cas}} < 0$ (negative = attractive, pulling plates together), consistent with the convention $F < 0$ for attractive. The force acts to decrease $a$.

**Dimensional check:** $[F/\mathcal{A}] = [\text{force}/\text{area}] = [\text{length}^{-4}]$ in natural units. Since $[\pi^2/(240\,a^4)] = [\text{length}^{-4}]$, Eq. (A.2) is dimensionally correct.

## Cycle Definition

Define a quasi-static cycle consisting of two stages:

**Stage 1 (Closing):** Plates are moved quasi-statically from separation $a_{\max}$ to $a_{\min}$ (with $a_{\min} < a_{\max}$). The external agent does work against the Casimir attraction. Since $F_{\text{Cas}} < 0$ acts to close the plates, closing the plates *along* the force direction means the Casimir force does positive work on the plates:

$$
W_{\text{close}} = \int_{a_{\max}}^{a_{\min}} F_{\text{Cas}}(a)\, da > 0
\tag{A.3}
$$

(The integral is negative times a negative displacement, giving positive work *by* the Casimir force. Equivalently, the field gives up energy $\Delta E = E_{\text{Cas}}(a_{\min}) - E_{\text{Cas}}(a_{\max}) < 0$ to the mechanical system.)

**Stage 2 (Opening):** Plates are moved quasi-statically from $a_{\min}$ back to $a_{\max}$. The external agent must now push against the attractive Casimir force:

$$
W_{\text{open}} = \int_{a_{\min}}^{a_{\max}} F_{\text{Cas}}(a)\, da < 0
\tag{A.4}
$$

(The Casimir force opposes the motion, doing negative work on the plates. The mechanical agent must input this energy.)

## Conservative Force Argument

**SELF-CRITIQUE CHECKPOINT (step 1):**
1. SIGN CHECK: $W_{\text{close}} > 0$, $W_{\text{open}} < 0$. Expected: opposite signs. Actual: confirmed.
2. FACTOR CHECK: No factors of $2$, $\pi$, etc. introduced beyond the Casimir force formula itself.
3. CONVENTION CHECK: Using $F < 0$ attractive, $W_{\text{net}} > 0$ = extraction. Consistent with convention lock.
4. DIMENSION CHECK: $[W] = [\text{energy}/\text{area}] = [\text{length}^{-3}]$ in natural units. Correct.

By assumption **A2**, the Casimir force $F_{\text{Cas}}(a)$ is a function of $a$ alone (at fixed $T$ and material properties, guaranteed by **A3**). It is therefore a conservative force in the one-dimensional configuration space.

The net work done by the Casimir force over one complete cycle is:

$$
W_{\text{net}} = \oint F_{\text{Cas}}(a)\, da = \int_{a_{\max}}^{a_{\min}} F_{\text{Cas}}(a)\, da + \int_{a_{\min}}^{a_{\max}} F_{\text{Cas}}(a)\, da = 0
\tag{A.5}
$$

This vanishes identically because the line integral of a conservative force over any closed path is zero. Equivalently, $F_{\text{Cas}} = -\partial E_{\text{Cas}}/\partial a$ is the gradient of a potential, and the net work equals the change in potential over a closed path, which is zero.

$$
\boxed{W_{\text{net}} = 0 \quad \text{(conservative force, quasi-static cycle)}}
\tag{A.6}
$$

**Limiting case check:** For ideal plates at $T = 0$:
$$
W_{\text{net}} = \int_{a_{\max}}^{a_{\min}} \left(-\frac{\pi^2}{240\,a^4}\right) da + \int_{a_{\min}}^{a_{\max}} \left(-\frac{\pi^2}{240\,a^4}\right) da = 0
$$
The two integrals cancel term by term. Confirmed.

## Second Law Generalization

The conservative force argument gives $W_{\text{net}} = 0$ for quasi-static cycles. We now generalize to *any* cyclic process, including non-equilibrium, rapid, or dissipative ones.

**Kelvin--Planck statement of the second law (A4):** No cyclic process exists whose *sole* result is the absorption of heat from a single thermal reservoir and its complete conversion to work.

At $T = 0$, the quantum vacuum is the unique thermal reservoir available (it is the lowest-temperature state). Any cyclic process operating between the system and this single reservoir must satisfy:

$$
W_{\text{net}} \leq 0
\tag{A.7}
$$

If $W_{\text{net}} > 0$ were possible, the cycle would extract energy from the $T = 0$ reservoir and convert it entirely to work, violating Kelvin--Planck.

More formally, for a cyclic process the Clausius inequality gives:

$$
\oint \frac{\delta Q}{T} \leq 0
\tag{A.8}
$$

At $T = 0$, any heat flow $\delta Q > 0$ from the reservoir would give a divergent positive contribution, violating the inequality unless $\delta Q \leq 0$ everywhere. By the first law for a cyclic process ($\Delta U = 0$, hence $W_{\text{net}} = Q_{\text{total}}$), we obtain $W_{\text{net}} \leq 0$.

**SELF-CRITIQUE CHECKPOINT (step 2):**
1. SIGN CHECK: $W_{\text{net}} \leq 0$ means no extraction. Consistent with no-go claim convention.
2. FACTOR CHECK: No new factors introduced.
3. CONVENTION CHECK: $W_{\text{net}} > 0$ = extraction throughout. Consistent.
4. DIMENSION CHECK: All work quantities have dimension $[\text{energy}]$. Correct.

$$
\boxed{W_{\text{net}} \leq 0 \quad \text{(any cyclic process, second law)}}
\tag{A.9}
$$

## Loophole Identification

The thermodynamic no-go argument fails if any of its assumptions are violated:

| Assumption | Violation Scenario | Physical Example |
|---|---|---|
| **A1** (Closed system) | External energy input not accounted for | Battery-powered actuator; laser illumination |
| **A2** (Conservative force) | $F_{\text{Cas}}$ depends on path, not just $a$ | Hysteresis due to irreversible material changes |
| **A3** (Fixed materials) | Material properties change mid-cycle | **Pinto's proposal**: switching plate conductivity between stages |
| **A4** (Second law at $T=0$) | Second law fails for quantum vacuum | No known mechanism |
| **A5** (Cyclic process) | System does not return to initial state | One-shot energy release (not a perpetual cycle) |

The most physically relevant loophole is **A3**: if one could change the reflectivity of a plate between the closing and opening stages, the Casimir force would differ in the two half-cycles, potentially yielding $W_{\text{net}} > 0$. This is the basis of Pinto's proposal (1999), analyzed in Phase 05. However, the energy cost of changing the material properties must be accounted for — this is the subject of the energy budget analysis in Phase 03.

**Cross-reference:** Scandurra (2001, hep-th/0104127) proved rigorously that the Casimir force between bodies with fixed material properties is conservative, providing mathematical support for assumption **A2**.

## Summary of Argument A

| Element | Content |
|---|---|
| **Conclusion** | $W_{\text{net}} \leq 0$ for any cyclic process involving Casimir plates with fixed material properties |
| **Method** | Conservative force $\Rightarrow$ $\oint F \cdot da = 0$ (quasi-static); Kelvin--Planck $\Rightarrow$ $W_{\text{net}} \leq 0$ (general) |
| **Assumptions** | A1--A5 (numbered above) |
| **Key loophole** | A3 (fixed materials) — violated by material property switching proposals |
| **References** | Casimir (1948), Scandurra (2001), standard thermodynamics |
