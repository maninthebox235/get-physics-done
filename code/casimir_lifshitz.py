"""
Lifshitz formula for the Casimir force between parallel dielectric slabs
at finite temperature.

The force per unit area is:

  F/A = -(T/pi) * sum'_{l=0}^{l_max} int_0^inf dk_perp * k_perp * kappa_0
        * sum_{P=TE,TM} [ r_P^2 * exp(-2*kappa_0*a) / (1 - r_P^2 * exp(-2*kappa_0*a)) ]

where the prime on the sum means the l=0 term carries half weight.

Reference: E.M. Lifshitz, Sov. Phys. JETP 2, 73 (1956);
           Bordag et al. (2009) Ch. 12-14 for implementation details.

Reproducibility:
  Python 3.11.14, numpy 2.4.3, scipy 1.17.1
  Deterministic (no random seeds needed).
"""
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus
# ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive
# ASSERT_CONVENTION: matsubara_prime_sum=l=0 term has half weight
# ASSERT_CONVENTION: [F/A] = [length^{-4}]

import numpy as np
from scipy import integrate

# Import material models (use relative import-compatible path)
import importlib.util as _ilu
import os as _os
_spec = _ilu.spec_from_file_location(
    'material_models',
    _os.path.join(_os.path.dirname(__file__), 'material_models.py')
)
_mm = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_mm)

# Re-export needed functions and constants
from_material = _mm
compute_kappas = _mm.compute_kappas
reflection_TE = _mm.reflection_TE
reflection_TM = _mm.reflection_TM
r_TE_l0_drude = _mm.r_TE_l0_drude
r_TE_l0_plasma = _mm.r_TE_l0_plasma
r_TM_l0 = _mm.r_TM_l0

# Boltzmann constant for temperature conversion
K_B_EV = 8.617333262e-5  # eV/K
EV_TO_INV_M = _mm.EV_TO_INV_M


def temperature_to_natural(T_kelvin):
    """Convert temperature in Kelvin to natural units [m^{-1}].

    T_nat = k_B * T / (hbar * c)  [with hbar=c=1, T_nat = k_B * T in eV, then convert]
    """
    return T_kelvin * K_B_EV * EV_TO_INV_M


# ---------------------------------------------------------------------------
# Matsubara frequencies
# ---------------------------------------------------------------------------
def matsubara_frequencies(T, l_max):
    """Compute Matsubara frequencies xi_l = 2*pi*l*T for l = 0, ..., l_max.

    Parameters
    ----------
    T : float
        Temperature in natural units [length^{-1}].
    l_max : int
        Maximum Matsubara index.

    Returns
    -------
    ndarray of shape (l_max + 1,)
        Matsubara frequencies [length^{-1}].
    """
    return 2.0 * np.pi * np.arange(l_max + 1) * T


# ---------------------------------------------------------------------------
# Lifshitz integrand
# ---------------------------------------------------------------------------
def lifshitz_integrand(k_perp, a, xi_l, epsilon_val, is_l0=False,
                       material_type='drude', omega_p=None, gamma=None):
    """Integrand of the Lifshitz formula for a single Matsubara term.

    Returns: k_perp * kappa_0 * sum_P [ r_P^2 * e^{-2*kappa_0*a}
                                        / (1 - r_P^2 * e^{-2*kappa_0*a}) ]

    Parameters
    ----------
    k_perp : float or ndarray
        Transverse wave vector [length^{-1}].
    a : float
        Plate separation [length].
    xi_l : float
        Matsubara frequency for this term [length^{-1}].
    epsilon_val : float
        Dielectric function at xi_l (dimensionless).
    is_l0 : bool
        Whether this is the l=0 term (uses special reflection coefficients).
    material_type : str
        'drude' or 'plasma' (affects l=0 TE coefficient only).
    omega_p : float or None
        Plasma frequency [length^{-1}]. Required when is_l0=True.
    gamma : float or None
        Drude relaxation [length^{-1}]. Required when is_l0=True and material_type='drude'.

    Returns
    -------
    float or ndarray
        Integrand value [length^{-3}].
    """
    k_perp = np.asarray(k_perp, dtype=float)

    if is_l0:
        # Special l=0 case: xi_l = 0
        kappa_0 = np.abs(k_perp)  # sqrt(k_perp^2 + 0) = |k_perp|

        if material_type == 'vacuum':
            # Vacuum: epsilon=1 at all frequencies, so r_TE = r_TM = 0
            rTE = np.zeros_like(k_perp)
            rTM = np.zeros_like(k_perp)
        elif material_type == 'perfect':
            # Perfect conductor: r_TE = -1, r_TM = 1
            rTE = -np.ones_like(k_perp)
            rTM = np.ones_like(k_perp)
        else:
            # Metallic models (Drude, plasma)
            # TM: r_TM = 1 for both models (metallic screening as eps->inf)
            rTM = r_TM_l0(k_perp)

            # TE: model-dependent
            if material_type == 'drude':
                rTE = r_TE_l0_drude(k_perp, omega_p, gamma)
            elif material_type == 'plasma':
                rTE = r_TE_l0_plasma(k_perp, omega_p)
            else:
                raise ValueError(f"Unknown material_type: {material_type}")
    else:
        kappa_0, kappa = compute_kappas(k_perp, xi_l, epsilon_val)
        rTE = reflection_TE(kappa_0, kappa)
        rTM = reflection_TM(kappa_0, kappa, epsilon_val)

    # Compute the integrand: sum over TE and TM polarizations
    exp_factor = np.exp(-2.0 * kappa_0 * a)
    result = np.zeros_like(k_perp)

    for r_P in [rTE, rTM]:
        r2 = r_P**2
        denom = 1.0 - r2 * exp_factor
        # Avoid division by zero (should not happen for |r| < 1)
        with np.errstate(divide='ignore', invalid='ignore'):
            contrib = r2 * exp_factor / denom
        contrib = np.where(np.isfinite(contrib), contrib, 0.0)
        result += contrib

    return k_perp * kappa_0 * result


# ---------------------------------------------------------------------------
# Single Matsubara term (integrated over k_perp)
# ---------------------------------------------------------------------------
def matsubara_term(l, a, T, epsilon_func, material_type='drude',
                   omega_p=None, gamma=None):
    """Compute a single Matsubara term: integral over k_perp of the Lifshitz integrand.

    Uses the substitution u = k_perp * a for numerical stability, then
    integrates over u from 0 to infinity.

    Parameters
    ----------
    l : int
        Matsubara index (l >= 0).
    a : float
        Plate separation [length].
    T : float
        Temperature in natural units [length^{-1}].
    epsilon_func : callable
        Dielectric function epsilon(xi) -> dimensionless.
    material_type : str
        'drude' or 'plasma'.
    omega_p : float or None
        Plasma frequency [length^{-1}].
    gamma : float or None
        Drude relaxation [length^{-1}].

    Returns
    -------
    float
        Integral value [length^{-3}] (to be multiplied by T/pi with primed sum weight).
    """
    xi_l = 2.0 * np.pi * l * T
    is_l0 = (l == 0)

    if is_l0:
        epsilon_val = np.inf  # not used directly; l=0 special functions handle it
    else:
        epsilon_val = epsilon_func(np.array([xi_l]))[0]

    # Substitution: u = k_perp * a, dk_perp = du / a
    # The integrand in terms of u:
    # lifshitz_integrand(u/a, a, xi_l, eps) * (1/a)
    # But lifshitz_integrand has dimensions [length^{-3}], and dk_perp = du/a,
    # so the integral in u has an extra 1/a factor.
    def integrand_u(u):
        k_perp = u / a
        val = lifshitz_integrand(
            np.array([k_perp]), a, xi_l, epsilon_val,
            is_l0=is_l0, material_type=material_type,
            omega_p=omega_p, gamma=gamma
        )
        return val[0] / a  # Jacobian dk_perp/du = 1/a

    result, error = integrate.quad(integrand_u, 0, np.inf,
                                   limit=200, epsabs=1e-20, epsrel=1e-12)
    return result


# ---------------------------------------------------------------------------
# Lifshitz force (finite T)
# ---------------------------------------------------------------------------
def lifshitz_force(a, T, epsilon_func, material_type='drude',
                   omega_p=None, gamma=None, l_max=None):
    """Compute the Casimir force per unit area using the Lifshitz formula.

    F/A = -(T/pi) * sum'_{l=0}^{l_max} matsubara_term(l, ...)

    The prime means the l=0 term has factor 1/2.

    Parameters
    ----------
    a : float
        Plate separation [length].
    T : float
        Temperature in natural units [length^{-1}].
    epsilon_func : callable
        Dielectric function epsilon(xi) -> dimensionless.
    material_type : str
        'drude' or 'plasma'.
    omega_p : float or None
        Plasma frequency [length^{-1}].
    gamma : float or None
        Drude relaxation [length^{-1}].
    l_max : int or None
        Maximum Matsubara index. If None, auto-determine by convergence:
        increase until |term(l)| < 1e-12 * |term(1)|.

    Returns
    -------
    float
        F/A (negative for attractive) [length^{-4}].
    """
    # Compute l=0 term (half weight)
    term_0 = matsubara_term(0, a, T, epsilon_func, material_type,
                            omega_p, gamma)

    # Compute l=1 term for reference scale
    term_1 = matsubara_term(1, a, T, epsilon_func, material_type,
                            omega_p, gamma)

    if l_max is None:
        # Auto-determine l_max
        threshold = 1e-12 * abs(term_1) if term_1 != 0 else 1e-30
        total = 0.5 * term_0 + term_1
        l = 2
        while True:
            term_l = matsubara_term(l, a, T, epsilon_func, material_type,
                                    omega_p, gamma)
            total += term_l
            if abs(term_l) < threshold:
                break
            l += 1
            if l > 100000:  # Safety cutoff
                break
    else:
        total = 0.5 * term_0
        for l in range(1, l_max + 1):
            total += matsubara_term(l, a, T, epsilon_func, material_type,
                                    omega_p, gamma)

    # F/A = -(T/pi) * sum'
    return -(T / np.pi) * total


# ---------------------------------------------------------------------------
# Lifshitz force at T = 0 (sum -> integral over xi)
# ---------------------------------------------------------------------------
def lifshitz_force_T0(a, epsilon_func=None, material_type='perfect'):
    """Compute the Casimir force per unit area at T = 0.

    At T = 0, the Matsubara sum becomes an integral:
    F/A = -(1/(2*pi^2)) * int_0^inf dxi int_0^inf dk_perp * k_perp * kappa_0
          * sum_P [ r_P^2 * exp(-2*kappa_0*a) / (1 - r_P^2 * exp(-2*kappa_0*a)) ]

    For perfect conductor: r_TE = -1, r_TM = 1, both give r_P^2 = 1.

    Parameters
    ----------
    a : float
        Plate separation [length].
    epsilon_func : callable or None
        Dielectric function epsilon(xi). None for perfect conductor.
    material_type : str
        'perfect', 'drude', or 'plasma'.

    Returns
    -------
    float
        F/A (negative for attractive) [length^{-4}].
    """
    # Use substitution: u = k_perp * a, v = xi * a
    # Then kappa_0 * a = sqrt(u^2 + v^2)
    # exp(-2*kappa_0*a) = exp(-2*sqrt(u^2 + v^2))
    # Jacobian: dk_perp * dxi = du*dv / a^2

    if material_type == 'perfect':
        # Perfect conductor: r_TE^2 = r_TM^2 = 1
        # Integrand (in u, v): u * sqrt(u^2+v^2) * 2 * exp(-2*sqrt(u^2+v^2))
        #                      / (1 - exp(-2*sqrt(u^2+v^2)))
        # The factor 2 comes from summing TE + TM (both give same contribution).
        # Full expression: F/A = -(1/(2*pi^2*a^4)) * int int ...

        def integrand_v(v, u):
            rho = np.sqrt(u**2 + v**2)
            exp2r = np.exp(-2.0 * rho)
            # 2 polarizations, both with r^2 = 1
            return u * rho * 2.0 * exp2r / (1.0 - exp2r)

        result, error = integrate.dblquad(
            integrand_v,
            0, np.inf,     # u limits
            0, np.inf,     # v limits
            epsabs=1e-15, epsrel=1e-10
        )

        return -result / (2.0 * np.pi**2 * a**4)

    else:
        # General material: need epsilon(xi)
        def integrand_v(v, u):
            xi = v / a
            k_perp = u / a
            if xi < 1e-30:
                return 0.0  # skip xi=0 (measure zero)
            eps_val = epsilon_func(np.array([xi]))[0]
            kappa_0, kappa = compute_kappas(np.array([k_perp]), xi, eps_val)
            kappa_0 = kappa_0[0]
            kappa = kappa[0]
            rTE = reflection_TE(kappa_0, kappa)
            rTM = reflection_TM(kappa_0, kappa, eps_val)

            exp_factor = np.exp(-2.0 * kappa_0 * a)
            total = 0.0
            for r_P in [rTE, rTM]:
                r2 = r_P**2
                if r2 < 1e-30:
                    continue
                total += r2 * exp_factor / (1.0 - r2 * exp_factor)

            return (u / a) * (kappa_0) * total / a  # Jacobian: 1/a^2

        result, error = integrate.dblquad(
            integrand_v,
            0, np.inf,
            0, np.inf,
            epsabs=1e-20, epsrel=1e-8
        )

        return -result / (2.0 * np.pi**2)
