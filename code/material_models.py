"""
Dielectric response functions and Fresnel reflection coefficients for
the Lifshitz formula computation of the Casimir force.

Reference: E.M. Lifshitz, Sov. Phys. JETP 2, 73 (1956);
           Bordag, Klimchitskaya, Mohideen, Mostepanenko (2009), Ch. 12-14.

All functions accept numpy arrays for vectorized integration.
"""
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus
# ASSERT_CONVENTION: [omega_p] = [gamma] = [length^{-1}] in natural units
# ASSERT_CONVENTION: Reflection coefficients for semi-infinite dielectric slab
# ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive

import numpy as np

# ---------------------------------------------------------------------------
# Unit conversion
# ---------------------------------------------------------------------------
# hbar*c = 197.3269804 MeV*fm = 197.3269804e-15 m * 1e6 eV
# => 1 eV = 1 / (hbar*c in eV*m) = 1 / (197.3269804e-9 m) = 5.067730759e6 m^{-1}
HBAR_C_EV_M = 197.3269804e-9  # hbar*c in eV*m
EV_TO_INV_M = 1.0 / HBAR_C_EV_M  # 1 eV in m^{-1} ~ 5.0677e6


def ev_to_natural(E_eV):
    """Convert energy in eV to natural units (inverse meters).

    In natural units hbar = c = 1, energy has dimensions of [length^{-1}].
    1 eV = 1/(hbar*c) in inverse length.
    With hbar*c = 197.3269804 MeV*fm = 197.3269804e-9 eV*m,
    1 eV = 5.067730759e6 m^{-1}.
    """
    return E_eV * EV_TO_INV_M


# ---------------------------------------------------------------------------
# Gold material parameters (Lambrecht & Reynaud values, widely used)
# ---------------------------------------------------------------------------
GOLD_OMEGA_P_EV = 9.0       # eV
GOLD_GAMMA_EV = 0.035       # eV
GOLD_OMEGA_P = ev_to_natural(GOLD_OMEGA_P_EV)  # m^{-1}
GOLD_GAMMA = ev_to_natural(GOLD_GAMMA_EV)      # m^{-1}


# ---------------------------------------------------------------------------
# Dielectric functions at imaginary frequency i*xi
# ---------------------------------------------------------------------------
def epsilon_drude(xi, omega_p, gamma):
    """Drude model dielectric function evaluated at imaginary frequency i*xi.

    epsilon_D(i*xi) = 1 + omega_p^2 / (xi * (xi + gamma))

    Parameters
    ----------
    xi : float or ndarray
        Imaginary frequency (>= 0).  [length^{-1}]
    omega_p : float
        Plasma frequency.  [length^{-1}]
    gamma : float
        Drude relaxation rate.  [length^{-1}]

    Returns
    -------
    float or ndarray
        Dielectric function value (dimensionless, >= 1 for xi > 0).
        Returns np.inf at xi = 0 (metallic screening).
    """
    xi = np.asarray(xi, dtype=float)
    result = np.empty_like(xi)
    zero_mask = (xi == 0.0)
    pos_mask = ~zero_mask
    result[zero_mask] = np.inf
    if np.any(pos_mask):
        x = xi[pos_mask]
        result[pos_mask] = 1.0 + omega_p**2 / (x * (x + gamma))
    return result


def epsilon_plasma(xi, omega_p):
    """Plasma model dielectric function evaluated at imaginary frequency i*xi.

    epsilon_P(i*xi) = 1 + omega_p^2 / xi^2

    This is the gamma -> 0 limit of the Drude model.

    Parameters
    ----------
    xi : float or ndarray
        Imaginary frequency (>= 0).  [length^{-1}]
    omega_p : float
        Plasma frequency.  [length^{-1}]

    Returns
    -------
    float or ndarray
        Dielectric function value (dimensionless, >= 1 for xi > 0).
        Returns np.inf at xi = 0 (metallic screening).
    """
    xi = np.asarray(xi, dtype=float)
    result = np.empty_like(xi)
    zero_mask = (xi == 0.0)
    pos_mask = ~zero_mask
    result[zero_mask] = np.inf
    if np.any(pos_mask):
        x = xi[pos_mask]
        result[pos_mask] = 1.0 + omega_p**2 / x**2
    return result


def make_drude(omega_p, gamma):
    """Return a callable epsilon(xi) for the Drude model.

    Parameters
    ----------
    omega_p : float
        Plasma frequency.  [length^{-1}]
    gamma : float
        Drude relaxation rate.  [length^{-1}]

    Returns
    -------
    callable
        epsilon(xi) -> dielectric function at imaginary frequency.
    """
    def eps(xi):
        return epsilon_drude(xi, omega_p, gamma)
    return eps


def make_plasma(omega_p):
    """Return a callable epsilon(xi) for the plasma model.

    Parameters
    ----------
    omega_p : float
        Plasma frequency.  [length^{-1}]

    Returns
    -------
    callable
        epsilon(xi) -> dielectric function at imaginary frequency.
    """
    def eps(xi):
        return epsilon_plasma(xi, omega_p)
    return eps


# ---------------------------------------------------------------------------
# Wave vectors (kappa) computation
# ---------------------------------------------------------------------------
def compute_kappas(k_perp, xi, epsilon_val):
    """Compute perpendicular wave vectors kappa_0 and kappa.

    kappa_0 = sqrt(k_perp^2 + xi^2)          (vacuum)
    kappa   = sqrt(k_perp^2 + epsilon * xi^2) (medium)

    Parameters
    ----------
    k_perp : float or ndarray
        Transverse wave vector magnitude.  [length^{-1}]
    xi : float
        Imaginary frequency.  [length^{-1}]
    epsilon_val : float
        Dielectric function value (dimensionless).

    Returns
    -------
    (kappa_0, kappa) : tuple of float or ndarray
        Both have dimensions [length^{-1}].
    """
    k_perp = np.asarray(k_perp, dtype=float)
    kappa_0 = np.sqrt(k_perp**2 + xi**2)
    kappa = np.sqrt(k_perp**2 + epsilon_val * xi**2)
    return kappa_0, kappa


# ---------------------------------------------------------------------------
# Reflection coefficients (general l > 0)
# ---------------------------------------------------------------------------
def reflection_TE(kappa_0, kappa):
    """TE (s-polarization) Fresnel reflection coefficient.

    r_TE = (kappa_0 - kappa) / (kappa_0 + kappa)

    For a semi-infinite dielectric slab with vacuum gap.
    Note: |r_TE| <= 1 for kappa_0, kappa >= 0.
    When epsilon = 1 (vacuum): kappa = kappa_0, so r_TE = 0.
    When epsilon -> inf: kappa -> inf, so r_TE -> -1.

    Parameters
    ----------
    kappa_0 : float or ndarray
        Vacuum perpendicular wave vector.  [length^{-1}]
    kappa : float or ndarray
        Medium perpendicular wave vector.  [length^{-1}]

    Returns
    -------
    float or ndarray
        Reflection coefficient (dimensionless).
    """
    return (kappa_0 - kappa) / (kappa_0 + kappa)


def reflection_TM(kappa_0, kappa, epsilon):
    """TM (p-polarization) Fresnel reflection coefficient.

    r_TM = (epsilon * kappa_0 - kappa) / (epsilon * kappa_0 + kappa)

    For a semi-infinite dielectric slab with vacuum gap.
    Note: |r_TM| <= 1 for physical inputs.
    When epsilon = 1: r_TM = 0.
    When epsilon -> inf: r_TM -> 1.

    Parameters
    ----------
    kappa_0 : float or ndarray
        Vacuum perpendicular wave vector.  [length^{-1}]
    kappa : float or ndarray
        Medium perpendicular wave vector.  [length^{-1}]
    epsilon : float
        Dielectric function value (dimensionless).

    Returns
    -------
    float or ndarray
        Reflection coefficient (dimensionless).
    """
    return (epsilon * kappa_0 - kappa) / (epsilon * kappa_0 + kappa)


# ---------------------------------------------------------------------------
# l = 0 special case reflection coefficients
# ---------------------------------------------------------------------------
# These are crucial for the Drude vs plasma controversy.
# At l = 0: xi_0 = 0, so both kappa_0 and kappa need careful limits.

def r_TE_l0_drude(k_perp, omega_p, gamma):
    """TE reflection coefficient at l = 0 (xi -> 0) for the Drude model.

    Returns 0.

    Physical reason: As xi -> 0, epsilon_D ~ omega_p^2/(xi*gamma) -> inf,
    but kappa = sqrt(k_perp^2 + epsilon*xi^2) -> sqrt(k_perp^2 + omega_p^2*xi/gamma).
    In the limit xi -> 0, kappa -> k_perp (same as kappa_0 -> k_perp).
    Therefore r_TE = (kappa_0 - kappa)/(kappa_0 + kappa) -> 0.

    Parameters
    ----------
    k_perp : float or ndarray
        Transverse wave vector.  [length^{-1}]
    omega_p : float
        Plasma frequency.  [length^{-1}]  (unused, kept for API symmetry)
    gamma : float
        Drude relaxation rate.  [length^{-1}]  (unused, kept for API symmetry)

    Returns
    -------
    float or ndarray
        Zero (dimensionless).
    """
    k_perp = np.asarray(k_perp, dtype=float)
    return np.zeros_like(k_perp)


def r_TE_l0_plasma(k_perp, omega_p):
    """TE reflection coefficient at l = 0 (xi -> 0) for the plasma model.

    Returns (k_perp - sqrt(k_perp^2 + omega_p^2)) /
            (k_perp + sqrt(k_perp^2 + omega_p^2))

    This is NONZERO -- the essential Drude vs plasma distinction.

    Physical reason: For the plasma model, epsilon_P ~ omega_p^2/xi^2,
    so kappa = sqrt(k_perp^2 + omega_p^2 * xi^2/xi^2) = sqrt(k_perp^2 + omega_p^2).
    This finite limit for kappa (while kappa_0 -> k_perp) gives a nonzero r_TE.

    Parameters
    ----------
    k_perp : float or ndarray
        Transverse wave vector.  [length^{-1}]
    omega_p : float
        Plasma frequency.  [length^{-1}]

    Returns
    -------
    float or ndarray
        Nonzero, negative reflection coefficient (dimensionless).
    """
    k_perp = np.asarray(k_perp, dtype=float)
    kappa_plasma = np.sqrt(k_perp**2 + omega_p**2)
    return (k_perp - kappa_plasma) / (k_perp + kappa_plasma)


def r_TM_l0(k_perp):
    """TM reflection coefficient at l = 0 (xi -> 0) for metallic models.

    Returns 1 for both Drude and plasma models.

    Physical reason: As xi -> 0, epsilon -> inf, so
    r_TM = (epsilon*kappa_0 - kappa)/(epsilon*kappa_0 + kappa) -> 1
    since epsilon*kappa_0 dominates kappa.

    Parameters
    ----------
    k_perp : float or ndarray
        Transverse wave vector.  [length^{-1}]

    Returns
    -------
    float or ndarray
        One (dimensionless).
    """
    k_perp = np.asarray(k_perp, dtype=float)
    return np.ones_like(k_perp)
