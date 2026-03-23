"""
Test suite for parameter sweep infrastructure.

Verifies grid generation, constraint masking, reference values,
eta < 10^{-10} at all valid points, and cross-method consistency.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    regularization_scheme=zeta
ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive
ASSERT_CONVENTION: work_sign=W_net > 0 means extraction; no-go claim: W_net <= 0
"""

import numpy as np
import pytest
import os
import sys

# Add code directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from parameter_sweep import (
    generate_grid, compute_point, KB_OVER_HBAR_C,
    cycle_work_lifshitz_double_integral,
    make_drude, make_plasma, GOLD_OMEGA_P, GOLD_GAMMA,
)


# =========================================================================
# a. Grid generation tests
# =========================================================================

class TestGridGeneration:
    """Tests for generate_grid function."""

    def test_grid_shapes(self):
        """Verify grid arrays have correct shapes."""
        grid = generate_grid(n_amin=10, n_amax=8, n_T=5)
        assert grid['a_min_grid'].shape == (10, 8, 5)
        assert grid['a_max_grid'].shape == (10, 8, 5)
        assert grid['T_grid'].shape == (10, 8, 5)
        assert grid['valid_mask'].shape == (10, 8, 5)
        assert grid['a_min_1d'].shape == (10,)
        assert grid['a_max_1d'].shape == (8,)
        assert grid['T_1d'].shape == (5,)

    def test_logarithmic_spacing(self):
        """Verify a_min and a_max are logarithmically spaced."""
        grid = generate_grid(n_amin=10, n_amax=10, n_T=3,
                             amin_range=(100e-9, 1e-6))
        a_min = grid['a_min_1d']
        # Check ratio between consecutive elements is constant
        ratios = a_min[1:] / a_min[:-1]
        np.testing.assert_allclose(ratios, ratios[0], rtol=1e-10)

    def test_mask_correctness(self):
        """All unmasked points satisfy a_min < a_max strictly."""
        grid = generate_grid(n_amin=15, n_amax=15, n_T=5)
        valid = grid['valid_mask']
        a_min = grid['a_min_grid'][valid]
        a_max = grid['a_max_grid'][valid]
        assert np.all(a_min < a_max), "Some valid points have a_min >= a_max"


# =========================================================================
# b. Constraint masking
# =========================================================================

def test_constraint_masking():
    """All unmasked points satisfy a_min < a_max strictly."""
    grid = generate_grid(n_amin=20, n_amax=20, n_T=10)
    valid = grid['valid_mask']
    diff = grid['a_max_grid'][valid] - grid['a_min_grid'][valid]
    assert np.all(diff > 0), "Found unmasked point with a_max <= a_min"
    # Also check that invalid points have a_min >= a_max
    invalid = ~valid
    if np.any(invalid):
        diff_inv = grid['a_max_grid'][invalid] - grid['a_min_grid'][invalid]
        assert np.all(diff_inv <= 0), \
            "Found masked point with a_max > a_min (should be unmasked)"


# =========================================================================
# c. Ideal T=0 reference
# =========================================================================

def test_ideal_t0_reference():
    """compute_point at (100nm, 1um, T=0, ideal) matches analytical W_close."""
    r = compute_point(100e-9, 1e-6, 0.0, 'ideal')
    expected = np.pi**2 / 720.0 * (1.0/(100e-9)**3 - 1.0/(1e-6)**3)
    np.testing.assert_allclose(r['W_close'], expected, rtol=1e-12,
                               err_msg="Ideal T=0 W_close mismatch")
    assert r['W_net'] == 0.0, "Ideal T=0 W_net not exactly 0"
    assert r['eta'] == 0.0, "Ideal T=0 eta not exactly 0"


# =========================================================================
# d. Drude reference
# =========================================================================

@pytest.mark.slow
def test_drude_reference():
    """compute_point at (100nm, 1um, 300K, drude) matches Phase 03 value."""
    r = compute_point(100e-9, 1e-6, 300.0, 'drude')
    phase03_ref = 6.970e18  # m^{-3}
    rel_err = abs(r['W_close'] - phase03_ref) / phase03_ref
    assert rel_err < 1e-4, \
        f"Drude W_close = {r['W_close']:.4e} vs Phase 03 ref = {phase03_ref:.4e}, " \
        f"rel err = {rel_err:.2e}"


# =========================================================================
# e. Plasma reference
# =========================================================================

@pytest.mark.slow
def test_plasma_reference():
    """compute_point at (100nm, 1um, 300K, plasma) matches Phase 03 value."""
    r = compute_point(100e-9, 1e-6, 300.0, 'plasma')
    phase03_ref = 7.189e18  # m^{-3}
    rel_err = abs(r['W_close'] - phase03_ref) / phase03_ref
    assert rel_err < 1e-4, \
        f"Plasma W_close = {r['W_close']:.4e} vs Phase 03 ref = {phase03_ref:.4e}, " \
        f"rel err = {rel_err:.2e}"


# =========================================================================
# f-h. Coarse eta tests (use saved data from coarse validation)
# =========================================================================

@pytest.fixture
def coarse_data():
    """Load coarse validation data if available."""
    data_path = os.path.join(os.path.dirname(__file__), '..', '..',
                             'data', 'sweep', 'coarse_validation.npz')
    if not os.path.exists(data_path):
        pytest.skip("Coarse validation data not yet generated")
    return dict(np.load(data_path))


def test_coarse_eta_ideal(coarse_data):
    """All valid ideal T=0 points have eta < 1e-10."""
    eta = coarse_data['ideal_eta']
    valid = ~np.isnan(eta)
    if not np.any(valid):
        pytest.skip("No ideal points in coarse data")
    max_eta = np.nanmax(eta[valid])
    assert max_eta < 1e-10, f"Ideal max(eta) = {max_eta:.2e} >= 1e-10"


def test_coarse_eta_drude(coarse_data):
    """All valid Drude points have eta < 1e-10."""
    eta = coarse_data['drude_eta']
    valid = ~np.isnan(eta)
    if not np.any(valid):
        pytest.skip("No Drude points in coarse data")
    max_eta = np.nanmax(eta[valid])
    assert max_eta < 1e-10, f"Drude max(eta) = {max_eta:.2e} >= 1e-10"


def test_coarse_eta_plasma(coarse_data):
    """All valid plasma points have eta < 1e-10."""
    eta = coarse_data['plasma_eta']
    valid = ~np.isnan(eta)
    if not np.any(valid):
        pytest.skip("No plasma points in coarse data")
    max_eta = np.nanmax(eta[valid])
    assert max_eta < 1e-10, f"Plasma max(eta) = {max_eta:.2e} >= 1e-10"


# =========================================================================
# i. Spot-check with double integral (3 points for speed)
# =========================================================================

@pytest.mark.slow
def test_spot_check_double_integral():
    """Verify at selected points using independent double integral method."""
    test_points = [
        (200e-9, 2e-6, 300.0, 'drude'),
        (300e-9, 3e-6, 150.0, 'plasma'),
        (500e-9, 5e-6, 300.0, 'drude'),
    ]

    for a_min, a_max, T_K, material in test_points:
        T_nat = T_K * KB_OVER_HBAR_C

        if material == 'drude':
            eps_func = make_drude(GOLD_OMEGA_P, GOLD_GAMMA)
            mat_type = 'drude'
            gamma = GOLD_GAMMA
        else:
            eps_func = make_plasma(GOLD_OMEGA_P)
            mat_type = 'plasma'
            gamma = None

        r_double = cycle_work_lifshitz_double_integral(
            a_min, a_max, T_nat, eps_func,
            material_type=mat_type,
            omega_p=GOLD_OMEGA_P, gamma=gamma)

        W_close_double = r_double['W_close']
        W_net_double = r_double['W_net']

        if abs(W_close_double) > 0:
            eta_double = abs(W_net_double) / abs(W_close_double)
        else:
            eta_double = 0.0

        # Single-integral result
        r_single = compute_point(a_min, a_max, T_K, material)
        eta_single = r_single['eta']

        # Both should give eta < 1e-8
        assert eta_double < 1e-8, \
            f"Double integral eta = {eta_double:.2e} at " \
            f"({a_min:.0e}, {a_max:.0e}, {T_K}K, {material})"

        # And they should agree
        assert abs(eta_single - eta_double) < 1e-8, \
            f"|eta_single - eta_double| = {abs(eta_single - eta_double):.2e} " \
            f"at ({a_min:.0e}, {a_max:.0e}, {T_K}K, {material})"


# =========================================================================
# j. W_close positive
# =========================================================================

def test_w_close_positive():
    """W_close > 0 at several valid points (attractive force does positive work)."""
    test_points = [
        (100e-9, 1e-6, 0.0, 'ideal'),
        (200e-9, 2e-6, 0.0, 'ideal'),
        (500e-9, 5e-6, 0.0, 'ideal'),
    ]
    for a_min, a_max, T, mat in test_points:
        r = compute_point(a_min, a_max, T, mat)
        assert r['W_close'] > 0, \
            f"W_close = {r['W_close']:.4e} <= 0 at ({a_min:.0e}, {a_max:.0e}, {T}K, {mat})"


@pytest.mark.slow
def test_w_close_positive_drude():
    """W_close > 0 for Drude material (attractive force)."""
    r = compute_point(200e-9, 2e-6, 300.0, 'drude')
    assert r['W_close'] > 0, f"Drude W_close = {r['W_close']:.4e} <= 0"


# =========================================================================
# k. W_close monotonic in a_max
# =========================================================================

def test_w_close_monotonic():
    """For fixed a_min, W_close increases with a_max (ideal T=0)."""
    a_min = 100e-9
    a_max_vals = [200e-9, 500e-9, 1e-6, 2e-6, 5e-6]
    w_close_vals = []
    for a_max in a_max_vals:
        r = compute_point(a_min, a_max, 0.0, 'ideal')
        w_close_vals.append(r['W_close'])

    for i in range(len(w_close_vals) - 1):
        assert w_close_vals[i+1] > w_close_vals[i], \
            f"W_close not monotonic: W_close({a_max_vals[i]:.0e}) = " \
            f"{w_close_vals[i]:.4e} >= W_close({a_max_vals[i+1]:.0e}) = " \
            f"{w_close_vals[i+1]:.4e}"


# =========================================================================
# l. Unit conversion
# =========================================================================

def test_unit_conversion():
    """Verify T=300K converts correctly to natural units."""
    T_nat = 300.0 * KB_OVER_HBAR_C
    expected = 1.310e5  # m^{-1} (approximate)
    rel_err = abs(T_nat - expected) / expected
    assert rel_err < 0.01, \
        f"T_nat(300K) = {T_nat:.4e} vs expected ~{expected:.3e}, " \
        f"rel err = {rel_err:.2e}"


# =========================================================================
# Additional: NaN handling for invalid points
# =========================================================================

def test_invalid_point_nan():
    """compute_point returns NaN when a_min >= a_max."""
    r = compute_point(1e-6, 100e-9, 300.0, 'drude')
    assert np.isnan(r['W_close'])
    assert np.isnan(r['eta'])

    r2 = compute_point(100e-9, 100e-9, 0.0, 'ideal')
    assert np.isnan(r2['W_close'])


# =========================================================================
# Additional: Data file completeness
# =========================================================================

def test_data_file_completeness(coarse_data):
    """Verify coarse_validation.npz contains all expected arrays."""
    required_keys = [
        'a_min_grid', 'a_max_grid', 'T_grid', 'valid_mask',
        'ideal_W_close', 'ideal_W_net', 'ideal_eta',
        'drude_W_close', 'drude_W_net', 'drude_eta',
        'plasma_W_close', 'plasma_W_net', 'plasma_eta',
    ]
    for key in required_keys:
        assert key in coarse_data, f"Missing key in coarse data: {key}"
