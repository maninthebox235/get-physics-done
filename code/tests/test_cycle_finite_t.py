"""
Finite-temperature cycle work tests for the Casimir force.

Tests W_net = 0 for quasi-static isothermal Casimir cycles with
ideal, Drude, and plasma material models at finite temperature.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    regularization_scheme=zeta
ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive
ASSERT_CONVENTION: work_sign=W_net > 0 means extraction; no-go claim: W_net <= 0

Reference: E.M. Lifshitz, Sov. Phys. JETP 2, 73 (1956);
           Bordag et al. (2009) Ch. 5, 12-14

Reproducibility:
  Python 3.11.14, numpy 2.4.3, scipy 1.17.1
  Deterministic (no random seeds).
"""

import os
import sys
import importlib.util

import numpy as np
import pytest

# ---------------------------------------------------------------------------
# Import project modules using importlib (no package install required)
# ---------------------------------------------------------------------------
_code_dir = os.path.join(os.path.dirname(__file__), '..')

def _load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_code_dir, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_mm = _load_module('material_models', 'material_models.py')
_cl = _load_module('casimir_lifshitz', 'casimir_lifshitz.py')
_cc = _load_module('casimir_cycle', 'casimir_cycle.py')

# Re-export needed functions
make_drude = _mm.make_drude
make_plasma = _mm.make_plasma
GOLD_OMEGA_P = _mm.GOLD_OMEGA_P
GOLD_GAMMA = _mm.GOLD_GAMMA

temperature_to_natural = _cl.temperature_to_natural

cycle_work_ideal_analytical = _cc.cycle_work_ideal_analytical
cycle_work_ideal_numerical = _cc.cycle_work_ideal_numerical
cycle_work_lifshitz = _cc.cycle_work_lifshitz
cycle_work_lifshitz_double_integral = _cc.cycle_work_lifshitz_double_integral
energy_budget = _cc.energy_budget


# ===========================================================================
# Test configuration parameters
# ===========================================================================
T_300K = temperature_to_natural(300.0)
T_77K = temperature_to_natural(77.0)

EPS_DRUDE = make_drude(GOLD_OMEGA_P, GOLD_GAMMA)
EPS_PLASMA = make_plasma(GOLD_OMEGA_P)


# ===========================================================================
# Precomputed results (populated by fixture)
# ===========================================================================
# Cache expensive Lifshitz computations across tests in this module.
_results_cache = {}


def _get_config_result(config_id):
    """Compute and cache cycle work for a given configuration."""
    if config_id in _results_cache:
        return _results_cache[config_id]

    configs = {
        1: dict(func='ideal_numerical', a_min=100e-9, a_max=1e-6),
        2: dict(func='lifshitz', a_min=100e-9, a_max=1e-6, T=T_300K,
                epsilon_func=None, material_type='perfect',
                omega_p=None, gamma=None, epsrel=1e-8),
        3: dict(func='lifshitz', a_min=100e-9, a_max=1e-6, T=T_300K,
                epsilon_func=EPS_DRUDE, material_type='drude',
                omega_p=GOLD_OMEGA_P, gamma=GOLD_GAMMA, epsrel=1e-8),
        4: dict(func='lifshitz', a_min=100e-9, a_max=1e-6, T=T_300K,
                epsilon_func=EPS_PLASMA, material_type='plasma',
                omega_p=GOLD_OMEGA_P, gamma=None, epsrel=1e-8),
        5: dict(func='lifshitz', a_min=50e-9, a_max=5e-6, T=T_300K,
                epsilon_func=EPS_DRUDE, material_type='drude',
                omega_p=GOLD_OMEGA_P, gamma=GOLD_GAMMA, epsrel=1e-8),
        6: dict(func='lifshitz', a_min=200e-9, a_max=2e-6, T=T_77K,
                epsilon_func=EPS_DRUDE, material_type='drude',
                omega_p=GOLD_OMEGA_P, gamma=GOLD_GAMMA, epsrel=1e-8),
    }

    cfg = configs[config_id]
    if cfg['func'] == 'ideal_numerical':
        result = cycle_work_ideal_numerical(cfg['a_min'], cfg['a_max'])
    else:
        result = cycle_work_lifshitz(
            cfg['a_min'], cfg['a_max'], cfg['T'],
            cfg['epsilon_func'], material_type=cfg['material_type'],
            omega_p=cfg['omega_p'], gamma=cfg['gamma'],
            epsrel=cfg['epsrel'],
        )

    _results_cache[config_id] = result
    return result


# ===========================================================================
# Task 1 tests: W_net = 0 for all configurations
# ===========================================================================

class TestRegressionT0:
    """Config 1: Regression against Plan 03-01 T=0 ideal result."""

    def test_regression_t0_ideal(self):
        """T=0 ideal numerical matches Plan 03-01 analytical to < 1e-14."""
        r_num = _get_config_result(1)
        r_ana = cycle_work_ideal_analytical(100e-9, 1e-6)

        # Numerical W_close should match analytical W_close
        rel_err = abs(r_num['W_close'] - r_ana['W_close']) / abs(r_ana['W_close'])
        assert rel_err < 1e-14, f"Regression failed: rel_err = {rel_err:.2e}"

        # W_net = 0 for both
        assert r_num['W_net'] == 0.0, f"Numerical W_net = {r_num['W_net']}"
        assert r_ana['W_net'] == 0.0, f"Analytical W_net = {r_ana['W_net']}"


class TestWnetIdeal300K:
    """Config 2: Ideal conductor at T = 300 K."""

    def test_wnet_ideal_300K(self):
        r = _get_config_result(2)
        ratio = abs(r['W_net']) / abs(r['W_close']) if r['W_close'] != 0 else 0
        assert ratio < 1e-10, f"|W_net|/|W_close| = {ratio:.2e}"


class TestWnetDrude300K:
    """Config 3: Drude gold at T = 300 K."""

    def test_wnet_drude_300K(self):
        r = _get_config_result(3)
        ratio = abs(r['W_net']) / abs(r['W_close']) if r['W_close'] != 0 else 0
        assert ratio < 1e-10, f"|W_net|/|W_close| = {ratio:.2e}"


class TestWnetPlasma300K:
    """Config 4: Plasma gold at T = 300 K."""

    def test_wnet_plasma_300K(self):
        r = _get_config_result(4)
        ratio = abs(r['W_net']) / abs(r['W_close']) if r['W_close'] != 0 else 0
        assert ratio < 1e-10, f"|W_net|/|W_close| = {ratio:.2e}"


class TestWnetDrudeWide:
    """Config 5: Drude gold, wide separation range, T = 300 K."""

    def test_wnet_drude_wide(self):
        r = _get_config_result(5)
        ratio = abs(r['W_net']) / abs(r['W_close']) if r['W_close'] != 0 else 0
        assert ratio < 1e-10, f"|W_net|/|W_close| = {ratio:.2e}"


class TestWnetDrudeLowT:
    """Config 6: Drude gold, low temperature (77 K)."""

    def test_wnet_drude_lowT(self):
        r = _get_config_result(6)
        ratio = abs(r['W_net']) / abs(r['W_close']) if r['W_close'] != 0 else 0
        assert ratio < 1e-10, f"|W_net|/|W_close| = {ratio:.2e}"


class TestSignConventions:
    """Sign consistency for all configurations."""

    @pytest.mark.parametrize("config_id", [1, 2, 3, 4, 5, 6])
    def test_wclose_positive(self, config_id):
        """W_close > 0 for all configs (attractive force, closing extracts)."""
        r = _get_config_result(config_id)
        assert r['W_close'] > 0, f"Config {config_id}: W_close = {r['W_close']}"

    @pytest.mark.parametrize("config_id", [1, 2, 3, 4, 5, 6])
    def test_wopen_negative(self, config_id):
        """W_open < 0 for all configs (must push against attraction)."""
        r = _get_config_result(config_id)
        assert r['W_open'] < 0, f"Config {config_id}: W_open = {r['W_open']}"


# ===========================================================================
# Task 2 tests: Energy budget and cross-checks
# ===========================================================================

class TestEnergyConservation:
    """Energy conservation for all configurations."""

    @pytest.mark.parametrize("config_id,T,a_min,a_max", [
        (1, 0.0, 100e-9, 1e-6),
        (2, T_300K, 100e-9, 1e-6),
        (3, T_300K, 100e-9, 1e-6),
        (4, T_300K, 100e-9, 1e-6),
        (5, T_300K, 50e-9, 5e-6),
        (6, T_77K, 200e-9, 2e-6),
    ])
    def test_energy_conservation_all(self, config_id, T, a_min, a_max):
        """Energy conservation |W_net - (Delta_E + Q)|/|W_close| < 1e-8."""
        r = _get_config_result(config_id)
        eb = energy_budget(a_min, a_max, T,
                           r['W_close'], r['W_open'], r['W_net'])
        assert eb['relative_precision'] < 1e-8, \
            f"Config {config_id}: conservation ratio = {eb['relative_precision']:.2e}"
        assert eb['budget_consistent'], \
            f"Config {config_id}: energy budget not consistent"


class TestDrudePlasmaDistinct:
    """Drude and plasma models give different W_close but both give W_net = 0."""

    def test_drude_plasma_wclose_differ(self):
        """W_close differs between Drude and plasma at T=300K."""
        r_drude = _get_config_result(3)
        r_plasma = _get_config_result(4)

        # They should differ -- plasma has extra TE l=0 contribution
        rel_diff = abs(r_drude['W_close'] - r_plasma['W_close']) / abs(r_drude['W_close'])
        assert rel_diff > 0.01, \
            f"Drude and plasma W_close too similar: rel_diff = {rel_diff:.6e}"

        # But both give W_net = 0
        assert r_drude['W_net'] == 0.0
        assert r_plasma['W_net'] == 0.0


class TestMonotonicity:
    """W_close increases with separation range."""

    def test_wclose_increases_with_range(self):
        """|W_close| for wide range (Config 5) > narrow range (Config 3)."""
        r_narrow = _get_config_result(3)
        r_wide = _get_config_result(5)

        assert abs(r_wide['W_close']) > abs(r_narrow['W_close']), \
            f"Wide |W_close|={abs(r_wide['W_close']):.4e} not > narrow |W_close|={abs(r_narrow['W_close']):.4e}"


# ===========================================================================
# Independent double-integration W_net test (closes verification gap)
# ===========================================================================

class TestDoubleIntegrationWnet:
    """
    Verify W_net = 0 by computing W_close and W_open as TWO independent
    integrals, not by setting W_open = -W_close algebraically.

    This closes the verification gap identified by the phase verifier:
    cycle_work_lifshitz makes W_net = 0 by construction, so the standard
    test is tautological. This test uses cycle_work_lifshitz_double_integral
    which integrates twice independently.
    """

    @pytest.mark.parametrize("material_type,epsilon_func,omega_p,gamma,T,label", [
        ('drude', EPS_DRUDE, GOLD_OMEGA_P, GOLD_GAMMA, T_300K, "Drude Au T=300K"),
        ('plasma', EPS_PLASMA, GOLD_OMEGA_P, None, T_300K, "Plasma Au T=300K"),
    ])
    def test_double_integral_wnet_zero(self, material_type, epsilon_func,
                                        omega_p, gamma, T, label):
        """W_net from two independent integrals is < 10^{-10} |W_close|."""
        a_min = 100e-9 * 5.068e6   # 100 nm in natural units
        a_max = 1e-6 * 5.068e6     # 1 um in natural units

        result = cycle_work_lifshitz_double_integral(
            a_min, a_max, T, epsilon_func,
            material_type=material_type,
            omega_p=omega_p, gamma=gamma,
            epsrel=1e-12,
        )

        W_close = result['W_close']
        W_net = result['W_net']

        assert W_close > 0, f"{label}: W_close should be positive, got {W_close}"

        if abs(W_close) > 0:
            ratio = abs(W_net) / abs(W_close)
            assert ratio < 1e-10, \
                f"{label}: |W_net|/|W_close| = {ratio:.2e} exceeds 1e-10"

    def test_double_integral_matches_single(self):
        """Double-integral W_close matches single-integral W_close."""
        a_min = 100e-9 * 5.068e6
        a_max = 1e-6 * 5.068e6

        r_single = cycle_work_lifshitz(
            a_min, a_max, T_300K, EPS_DRUDE,
            material_type='drude', omega_p=GOLD_OMEGA_P, gamma=GOLD_GAMMA,
        )
        r_double = cycle_work_lifshitz_double_integral(
            a_min, a_max, T_300K, EPS_DRUDE,
            material_type='drude', omega_p=GOLD_OMEGA_P, gamma=GOLD_GAMMA,
        )

        rel_err = abs(r_single['W_close'] - r_double['W_close']) / abs(r_single['W_close'])
        assert rel_err < 1e-10, \
            f"Single vs double W_close mismatch: rel_err = {rel_err:.2e}"
