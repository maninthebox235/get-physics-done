"""
Test suite for ideal parallel-plate Casimir force at T=0.

Contract acceptance tests for plan 02-01:
  - test-casimir-benchmark: mode sum reproduces F/A = -pi^2/(240 a^4) to < 10^{-6}
  - test-dimensions: [F/A] = [length^{-4}] via scaling
  - test-force-energy: F/A = -d(E/A)/da to < 10^{-8}

Additional tests:
  - Sign convention: F < 0 (attractive)
  - Numerical cross-check: Abel-Plana integral agrees independently
  - Order of magnitude: ~1.3 mPa at 1 um in SI

Reference: H.B.G. Casimir, Proc. K. Ned. Akad. Wet. 51, 793 (1948)

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    regularization_scheme=zeta
ASSERT_CONVENTION: F < 0 for attractive Casimir force
ASSERT_CONVENTION: [F/A] = length^{-4}, [E/A] = length^{-3}
"""

import sys
import os
import numpy as np

# Ensure the code directory is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from code.casimir_ideal import (
    casimir_energy_ideal,
    casimir_force_ideal,
    mode_sum_zeta,
    mode_sum_zeta_force,
    mode_sum_numerical,
    mode_sum_numerical_force,
    force_per_area_si,
)


# ---------------------------------------------------------------------------
# Contract acceptance test: test-casimir-benchmark
# ---------------------------------------------------------------------------

def test_benchmark_casimir_1948():
    """
    Primary contract acceptance test (test-casimir-benchmark).

    Verify that the zeta-regularized mode summation reproduces the Casimir
    (1948) analytical result F/A = -pi^2/(240 a^4) to relative error < 10^{-6}
    at five test separations.

    The separations are chosen in natural units. Since the formula is
    scale-free (pure power law in a), the choice of a values does not
    affect the relative error -- but we test multiple values to confirm
    no implementation bugs at different scales.
    """
    # Test separations (arbitrary natural-unit values spanning several decades)
    # These correspond to physical separations of ~100 nm to ~10 um
    # when the natural length unit is identified appropriately.
    test_separations = [0.1, 0.5, 1.0, 5.0, 10.0]

    for a in test_separations:
        F_exact = casimir_force_ideal(a)
        F_zeta = mode_sum_zeta_force(a)
        rel_err = abs(F_zeta - F_exact) / abs(F_exact)
        assert rel_err < 1e-6, (
            f"Benchmark FAILED at a={a}: "
            f"F_exact={F_exact:.10e}, F_zeta={F_zeta:.10e}, "
            f"rel_err={rel_err:.2e} > 1e-6"
        )

    # Also check energy
    for a in test_separations:
        E_exact = casimir_energy_ideal(a)
        E_zeta = mode_sum_zeta(a)
        rel_err = abs(E_zeta - E_exact) / abs(E_exact)
        assert rel_err < 1e-6, (
            f"Energy benchmark FAILED at a={a}: "
            f"E_exact={E_exact:.10e}, E_zeta={E_zeta:.10e}, "
            f"rel_err={rel_err:.2e} > 1e-6"
        )


# ---------------------------------------------------------------------------
# Contract acceptance test: test-dimensions
# ---------------------------------------------------------------------------

def test_dimensional_analysis():
    """
    Contract acceptance test (test-dimensions).

    Verify [F/A] = [length^{-4}] and [E/A] = [length^{-3}] by checking
    the scaling relation:
      F(lambda*a) / F(a) = lambda^{-4}
      E(lambda*a) / E(a) = lambda^{-3}
    """
    a = 1.0
    lambdas = [2.0, 3.0, 0.5, 0.1, 10.0]

    for lam in lambdas:
        # Force scaling: a^{-4}
        ratio_F = casimir_force_ideal(lam * a) / casimir_force_ideal(a)
        expected_F = lam**(-4)
        assert abs(ratio_F - expected_F) / abs(expected_F) < 1e-14, (
            f"Force scaling FAILED for lambda={lam}: "
            f"ratio={ratio_F}, expected={expected_F}"
        )

        # Energy scaling: a^{-3}
        ratio_E = casimir_energy_ideal(lam * a) / casimir_energy_ideal(a)
        expected_E = lam**(-3)
        assert abs(ratio_E - expected_E) / abs(expected_E) < 1e-14, (
            f"Energy scaling FAILED for lambda={lam}: "
            f"ratio={ratio_E}, expected={expected_E}"
        )

    # Also check zeta functions scale correctly
    for lam in [2.0, 0.5]:
        ratio_F = mode_sum_zeta_force(lam * a) / mode_sum_zeta_force(a)
        expected_F = lam**(-4)
        assert abs(ratio_F - expected_F) / abs(expected_F) < 1e-10, (
            f"Zeta force scaling FAILED for lambda={lam}: "
            f"ratio={ratio_F}, expected={expected_F}"
        )


# ---------------------------------------------------------------------------
# Contract acceptance test: test-force-energy
# ---------------------------------------------------------------------------

def test_force_energy_consistency():
    """
    Contract acceptance test (test-force-energy).

    Verify F/A = -d(E/A)/da numerically using central difference at
    multiple separations. Assert agreement to < 10^{-8} relative error.
    """
    test_separations = [0.1, 0.5, 1.0, 5.0, 10.0]

    for a in test_separations:
        # Central difference with step da = a * 1e-6
        da = a * 1e-6
        dEda_num = (casimir_energy_ideal(a + da) - casimir_energy_ideal(a - da)) / (2 * da)
        F_analytical = casimir_force_ideal(a)

        # F = -dE/da, so F + dE/da should be ~0
        rel_err = abs(F_analytical + dEda_num) / abs(F_analytical)
        assert rel_err < 1e-8, (
            f"Force-energy consistency FAILED at a={a}: "
            f"F={F_analytical:.10e}, -dE/da={-dEda_num:.10e}, "
            f"rel_err={rel_err:.2e} > 1e-8"
        )

    # Also check zeta implementations
    for a in [0.5, 1.0, 5.0]:
        da = a * 1e-6
        dEda_num = (mode_sum_zeta(a + da) - mode_sum_zeta(a - da)) / (2 * da)
        F_zeta = mode_sum_zeta_force(a)
        rel_err = abs(F_zeta + dEda_num) / abs(F_zeta)
        assert rel_err < 1e-8, (
            f"Zeta force-energy consistency FAILED at a={a}: "
            f"F_zeta={F_zeta:.10e}, -dE_zeta/da={-dEda_num:.10e}, "
            f"rel_err={rel_err:.2e} > 1e-8"
        )


# ---------------------------------------------------------------------------
# Sign convention test
# ---------------------------------------------------------------------------

def test_sign_convention():
    """
    Verify F/A < 0 (attractive) and E/A < 0 (bound lower than free)
    at all test separations, for both analytical and zeta implementations.
    """
    test_separations = [0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 100.0]

    for a in test_separations:
        # Analytical
        assert casimir_force_ideal(a) < 0, (
            f"Force should be negative (attractive) at a={a}, "
            f"got F={casimir_force_ideal(a)}"
        )
        assert casimir_energy_ideal(a) < 0, (
            f"Energy should be negative at a={a}, "
            f"got E={casimir_energy_ideal(a)}"
        )

        # Zeta
        assert mode_sum_zeta(a) < 0, (
            f"Zeta energy should be negative at a={a}"
        )
        assert mode_sum_zeta_force(a) < 0, (
            f"Zeta force should be negative at a={a}"
        )


# ---------------------------------------------------------------------------
# Numerical cross-check (independent method)
# ---------------------------------------------------------------------------

def test_numerical_crosscheck():
    """
    Verify that the Abel-Plana numerical integration (independent of
    mpmath.zeta) agrees with the analytical result to < 10^{-4}.

    This test uses the numerical mode sum which computes zeta(-3) via
    direct numerical integration of t^3/(e^{2*pi*t} - 1), providing
    a genuinely independent check.
    """
    a = 1.0
    E_exact = casimir_energy_ideal(a)
    E_num = mode_sum_numerical(a)
    rel_err = abs(E_num - E_exact) / abs(E_exact)

    # The Abel-Plana integral is computed to very high precision by mpmath.quad,
    # so we expect much better than 10^{-4}. But the contract only requires 10^{-4}.
    assert rel_err < 1e-4, (
        f"Numerical cross-check FAILED at a={a}: "
        f"E_exact={E_exact:.10e}, E_num={E_num:.10e}, "
        f"rel_err={rel_err:.2e} > 1e-4"
    )

    # Check at another separation
    a = 5.0
    E_exact = casimir_energy_ideal(a)
    E_num = mode_sum_numerical(a)
    rel_err = abs(E_num - E_exact) / abs(E_exact)
    assert rel_err < 1e-4, (
        f"Numerical cross-check FAILED at a={a}: "
        f"E_exact={E_exact:.10e}, E_num={E_num:.10e}, "
        f"rel_err={rel_err:.2e} > 1e-4"
    )


# ---------------------------------------------------------------------------
# Order-of-magnitude check in SI
# ---------------------------------------------------------------------------

def test_order_of_magnitude():
    """
    At a = 1 um, F/A in SI units should be approximately -1.3e-3 N/m^2.

    The exact value:
      F/A = -pi^2 * hbar * c / (240 * a^4)
          = -pi^2 * 1.0546e-34 * 2.998e8 / (240 * (1e-6)^4)
          = -pi^2 * 3.162e-26 / (240 * 1e-24)
          = -pi^2 * 3.162e-26 / 2.4e-22
          = -pi^2 * 1.318e-4
          = -1.300e-3 Pa

    We allow a factor-of-2 window for order-of-magnitude check.
    """
    F_si = force_per_area_si(1e-6)  # 1 um separation

    # Check sign
    assert F_si < 0, f"SI force should be negative, got {F_si}"

    # Check order of magnitude: should be ~ -1.3e-3 Pa
    assert abs(F_si) > 1e-4, (
        f"SI force too small: {F_si:.2e} Pa (expected ~1e-3 Pa)"
    )
    assert abs(F_si) < 1e-2, (
        f"SI force too large: {F_si:.2e} Pa (expected ~1e-3 Pa)"
    )

    # More precise check: within 10% of -1.3e-3 Pa
    expected = -1.3e-3
    rel_err = abs(F_si - expected) / abs(expected)
    assert rel_err < 0.1, (
        f"SI force {F_si:.4e} Pa differs from expected {expected:.1e} Pa "
        f"by {rel_err*100:.1f}%"
    )

    # Also check at a = 100 nm (should be ~1.3e5 times larger: (1e-6/1e-7)^4 = 1e4)
    F_100nm = force_per_area_si(1e-7)
    ratio = F_100nm / F_si
    expected_ratio = (1e-6 / 1e-7)**4  # = 10000
    assert abs(ratio - expected_ratio) / expected_ratio < 1e-10, (
        f"Scaling from 1um to 100nm: ratio={ratio}, expected={expected_ratio}"
    )


# ---------------------------------------------------------------------------
# Run all tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tests = [
        ("test_benchmark_casimir_1948", test_benchmark_casimir_1948),
        ("test_dimensional_analysis", test_dimensional_analysis),
        ("test_force_energy_consistency", test_force_energy_consistency),
        ("test_sign_convention", test_sign_convention),
        ("test_numerical_crosscheck", test_numerical_crosscheck),
        ("test_order_of_magnitude", test_order_of_magnitude),
    ]

    passed = 0
    failed = 0
    for name, test_fn in tests:
        try:
            test_fn()
            print(f"PASS: {name}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {name} -- {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR: {name} -- {e}")
            failed += 1

    print(f"\n{passed}/{passed+failed} tests passed")
    if failed > 0:
        sys.exit(1)
