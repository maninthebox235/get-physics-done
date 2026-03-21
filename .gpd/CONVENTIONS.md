---
gpd_role: conventions
version: 1
---

# Conventions: Zero-Point Energy Extraction Analysis

## Standard Conventions

| Convention | Value | Rationale |
|-----------|-------|-----------|
| Natural units | ℏ = c = k_B = 1 | Standard for QFT; restore units in final numerical results |
| Metric signature | (+, -, -, -) (mostly-minus) | Standard particle physics convention |
| Fourier convention | Physics: f(x) = ∫ dk/(2π) f̃(k) e^{ikx} | Consistent with standard QFT references |
| Regularization | Zeta function | Natural for Casimir mode sums; cross-check with cutoff |

## Project-Specific Conventions

| Convention | Value | Rationale |
|-----------|-------|-----------|
| Casimir force sign | F < 0 for attractive | Plates pulled together = negative force (toward smaller a) |
| Casimir energy sign | E < 0 for bounded < unbounded | Configuration with plates has lower energy than without |
| Force-energy relation | F = -∂E/∂a | Standard thermodynamic derivative convention |
| Matsubara sum | Primed sum Σ' with l=0 at half weight | Standard Lifshitz convention: F = (k_BT/2π)[½I₀ + Σ_{l≥1} I_l] |
| Matsubara frequencies | ξ_l = 2πk_BT l/ℏ | Standard thermal field theory |
| Work sign | W_net > 0 = energy extracted | W_net ≤ 0 is the no-go claim we test |
| Plate separation | a > 0, with a_min < a_max | Cycle: close from a_max to a_min, then open back |

## Not Set (Irrelevant for This Project)

The following standard QFT conventions are not needed for Casimir effect calculations and are left unset:
gauge choice, renormalization scheme, spin basis, coupling convention, gamma matrices,
covariant derivative sign, Levi-Civita sign, generator normalization, creation/annihilation ordering.

These will be set if needed during stretch goals (e.g., dynamic Casimir may need creation/annihilation ordering).

## Convention Lock

Machine-readable lock stored in `.gpd/state.json` field `convention_lock`.
Validate with: `mcp__gpd-conventions__convention_lock_status`
