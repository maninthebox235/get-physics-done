"""
Test suite verifying W_net = 0 for T=0 Casimir cycles.

Tests both analytical and numerical cycle work computations.
Validates sign conventions, dimensional consistency, and energy budget.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus
ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive
ASSERT_CONVENTION: work_sign=W_net > 0 means extraction; no-go claim: W_net <= 0
"""

import sys
import os
import numpy as np
import pytest

# Add code directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import importlib.util as _ilu

# Import casimir_cycle
_spec = _ilu.spec_from_file_location(
    'casimir_cycle',
    os.path.join(os.path.dirname(__file__), '..', 'casimir_cycle.py')
)
_cc = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_cc)

cycle_work_ideal_analytical = _cc.cycle_work_ideal_analytical
cycle_work_ideal_numerical = _cc.cycle_work_ideal_numerical
energy_budget = _cc.energy_budget


# =========================================================================
# Test 1: Analytical W_net = 0 exactly
# =========================================================================

class TestWnetAnalyticalZero:
    """Verify cycle_work_ideal_analytical returns W_net = 0.0 exactly."""

    @pytest.mark.parametrize("a_min,a_max", [
        (1.0, 10.0),
        (0.5, 5.0),
        (100.0, 1000.0),
    ])
    def test_wnet_analytical_zero(self, a_min, a_max):
        result = cycle_work_ideal_analytical(a_min, a_max)
        assert result['W_net'] == 0.0, \
            f"W_net should be exactly 0.0, got {result['W_net']}"


# =========================================================================
# Test 2: Numerical W_net precision
# =========================================================================

class TestWnetNumericalPrecision:
    """Verify |W_net|/|W_close| < 1e-14 from numerical quadrature."""

    def test_wnet_numerical_precision(self):
        """Canonical test: a_min=1.0, a_max=10.0 in natural units."""
        result = cycle_work_ideal_numerical(1.0, 10.0)
        ratio = abs(result['W_net']) / abs(result['W_close'])
        assert ratio < 1e-14, \
            f"|W_net|/|W_close| = {ratio:.2e}, should be < 1e-14"

    def test_wnet_numerical_precision_wide_cycle(self):
        """Wide cycle: a_min=0.5, a_max=50.0."""
        result = cycle_work_ideal_numerical(0.5, 50.0)
        ratio = abs(result['W_net']) / abs(result['W_close'])
        assert ratio < 1e-14, \
            f"|W_net|/|W_close| = {ratio:.2e}, should be < 1e-14"

    def test_wnet_numerical_precision_narrow_cycle(self):
        """Narrow cycle: a_min=1.0, a_max=1.1."""
        result = cycle_work_ideal_numerical(1.0, 1.1)
        ratio = abs(result['W_net']) / abs(result['W_close'])
        assert ratio < 1e-14, \
            f"|W_net|/|W_close| = {ratio:.2e}, should be < 1e-14"


# =========================================================================
# Test 3: Analytical vs numerical agreement
# =========================================================================

class TestAnalyticalVsNumerical:
    """Verify analytical and numerical W_close agree to < 1e-12."""

    @pytest.mark.parametrize("a_min,a_max", [
        (1.0, 10.0),
        (0.5, 5.0),
        (2.0, 20.0),
    ])
    def test_analytical_vs_numerical(self, a_min, a_max):
        anal = cycle_work_ideal_analytical(a_min, a_max)
        numer = cycle_work_ideal_numerical(a_min, a_max)

        rel_error = abs(anal['W_close'] - numer['W_close']) / abs(anal['W_close'])
        assert rel_error < 1e-12, \
            f"Analytical vs numerical W_close relative error = {rel_error:.2e}"


# =========================================================================
# Test 4: Dimensional consistency
# =========================================================================

class TestDimensions:
    """Verify [W/A] = [length^{-3}] by checking W_close * a^3 is O(1)."""

    @pytest.mark.parametrize("a_min,a_max", [
        (1.0, 10.0),
        (0.1, 1.0),
        (10.0, 100.0),
    ])
    def test_dimensions(self, a_min, a_max):
        result = cycle_work_ideal_analytical(a_min, a_max)
        W_close = result['W_close']

        # W_close has dimensions [length^{-3}].
        # W_close * a_min^3 should be O(1) (dimensionless, order unity).
        # Specifically: W_close = (pi^2/720)*(1/a_min^3 - 1/a_max^3)
        # W_close * a_min^3 = (pi^2/720)*(1 - (a_min/a_max)^3)
        dimensionless = W_close * a_min**3
        expected = (np.pi**2 / 720.0) * (1.0 - (a_min / a_max)**3)
        assert abs(dimensionless - expected) < 1e-14, \
            f"Dimensionless check: got {dimensionless}, expected {expected}"
        # Should be O(1), specifically O(pi^2/720) ~ 0.0137
        assert 0 < dimensionless < 1.0, \
            f"Dimensionless W_close * a_min^3 = {dimensionless}, expected O(1)"


# =========================================================================
# Test 5: Sign conventions
# =========================================================================

class TestSignConventions:
    """Verify signs are consistent with conventions."""

    def test_sign_conventions(self):
        result = cycle_work_ideal_analytical(1.0, 10.0)

        # W_close > 0: closing under attractive force extracts energy
        assert result['W_close'] > 0, \
            f"W_close should be > 0 (closing extracts), got {result['W_close']}"

        # W_open < 0: opening against attractive force costs energy
        assert result['W_open'] < 0, \
            f"W_open should be < 0 (opening costs), got {result['W_open']}"

        # W_close = -W_open
        assert result['W_close'] == -result['W_open'], \
            f"W_close should equal -W_open"

        # W_net = 0
        assert result['W_net'] == 0.0, \
            f"W_net should be 0, got {result['W_net']}"

    def test_numerical_signs(self):
        """Same sign checks for numerical computation."""
        result = cycle_work_ideal_numerical(1.0, 10.0)

        assert result['W_close'] > 0, \
            f"Numerical W_close should be > 0, got {result['W_close']}"
        assert result['W_open'] < 0, \
            f"Numerical W_open should be < 0, got {result['W_open']}"


# =========================================================================
# Test 6: Trivial cycle
# =========================================================================

class TestTrivialCycle:
    """Verify W_close = W_open = W_net = 0 when a_min = a_max."""

    def test_trivial_cycle(self):
        result = cycle_work_ideal_analytical(5.0, 5.0)
        assert result['W_close'] == 0.0, \
            f"Trivial cycle: W_close should be 0, got {result['W_close']}"
        assert result['W_open'] == 0.0, \
            f"Trivial cycle: W_open should be 0, got {result['W_open']}"
        assert result['W_net'] == 0.0, \
            f"Trivial cycle: W_net should be 0, got {result['W_net']}"


# =========================================================================
# Test 7: Energy budget at T=0
# =========================================================================

class TestEnergyBudgetT0:
    """Verify energy budget conservation check < 1e-14."""

    def test_energy_budget_t0_analytical(self):
        """Analytical cycle: perfect energy conservation."""
        cycle = cycle_work_ideal_analytical(1.0, 10.0)
        budget = energy_budget(
            a_min=1.0, a_max=10.0, T=0.0,
            W_close=cycle['W_close'],
            W_open=cycle['W_open'],
            W_net=cycle['W_net'],
            Delta_E_vac=0.0, Q=0.0,
        )
        assert budget['relative_precision'] < 1e-14, \
            f"Energy budget residual = {budget['relative_precision']:.2e}"
        assert budget['budget_consistent'] is True

    def test_energy_budget_t0_numerical(self):
        """Numerical cycle: energy conservation to quadrature precision."""
        cycle = cycle_work_ideal_numerical(1.0, 10.0)
        budget = energy_budget(
            a_min=1.0, a_max=10.0, T=0.0,
            W_close=cycle['W_close'],
            W_open=cycle['W_open'],
            W_net=cycle['W_net'],
            Delta_E_vac=0.0, Q=0.0,
        )
        assert budget['relative_precision'] < 1e-14, \
            f"Energy budget residual = {budget['relative_precision']:.2e}"
        assert budget['budget_consistent'] is True


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
