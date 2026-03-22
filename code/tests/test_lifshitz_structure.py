"""
Structural tests for the Lifshitz formula infrastructure.

Tests verify:
1. Reflection coefficient limits (vacuum, perfect conductor, Drude/plasma l=0)
2. Drude-plasma relation (gamma -> 0 limit)
3. Matsubara sum convergence
4. Primed sum half-weight convention
5. Sign convention (F < 0 for attractive)
6. Vacuum gives zero force
7. T=0 perfect conductor dimensional scaling (a^{-4})

Reference: Lifshitz (1956); Bordag et al. (2009) Ch. 12-14.

Note: matplotlib is NOT available. All tests use numerical assertions only.
"""
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus
# ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive
# ASSERT_CONVENTION: matsubara_prime_sum=l=0 term has half weight

import sys
import os
import importlib.util
import numpy as np

# Load modules by file path (avoids 'code' package name conflict)
def _load(name, relpath):
    path = os.path.join(os.path.dirname(__file__), '..', relpath)
    spec = importlib.util.spec_from_file_location(name, os.path.abspath(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

mm = _load('material_models', 'material_models.py')
cl = _load('casimir_lifshitz', 'casimir_lifshitz.py')


# ============================================================================
# Test 1: Reflection coefficient limits
# ============================================================================
def test_reflection_coefficient_limits():
    """Verify all reflection coefficient boundary values.

    Acceptance test: test-reflection-limits
    (1) |r_TE|, |r_TM| <= 1 for all inputs
    (2) epsilon=1 gives r=0
    (3) epsilon->inf gives |r|->1
    (4) Drude l=0: r_TE=0, r_TM=1
    (5) Plasma l=0: r_TE!=0, r_TM=1
    """
    k_test = np.logspace(-2, 5, 500)
    xi_val = 1e7

    # (1) Bounds: |r| <= 1 for physical inputs
    for eps_val in [1.5, 10.0, 100.0, 1e6]:
        k0, k = mm.compute_kappas(k_test, xi_val, eps_val)
        rTE = mm.reflection_TE(k0, k)
        rTM = mm.reflection_TM(k0, k, eps_val)
        assert np.all(np.abs(rTE) <= 1.0 + 1e-14), \
            f"|r_TE| > 1 at eps={eps_val}"
        assert np.all(np.abs(rTM) <= 1.0 + 1e-14), \
            f"|r_TM| > 1 at eps={eps_val}"

    # (2) Vacuum: epsilon=1 gives r=0
    k0_v, k_v = mm.compute_kappas(k_test, xi_val, 1.0)
    assert np.allclose(mm.reflection_TE(k0_v, k_v), 0, atol=1e-15), \
        "Vacuum r_TE != 0"
    assert np.allclose(mm.reflection_TM(k0_v, k_v, 1.0), 0, atol=1e-15), \
        "Vacuum r_TM != 0"

    # (3) Perfect conductor: epsilon->inf gives |r|->1
    eps_huge = 1e20
    k0_pc, k_pc = mm.compute_kappas(k_test, xi_val, eps_huge)
    assert np.allclose(np.abs(mm.reflection_TE(k0_pc, k_pc)), 1, atol=1e-5), \
        "|r_TE| not -> 1 for eps->inf"
    assert np.allclose(np.abs(mm.reflection_TM(k0_pc, k_pc, eps_huge)), 1, atol=1e-5), \
        "|r_TM| not -> 1 for eps->inf"

    # (4) Drude l=0: r_TE=0, r_TM=1
    k_l0 = np.logspace(-1, 5, 100)
    assert np.all(mm.r_TE_l0_drude(k_l0, mm.GOLD_OMEGA_P, mm.GOLD_GAMMA) == 0), \
        "Drude l=0 r_TE != 0"
    assert np.all(mm.r_TM_l0(k_l0) == 1), \
        "l=0 r_TM != 1"

    # (5) Plasma l=0: r_TE nonzero and negative, r_TM=1
    rTE_p = mm.r_TE_l0_plasma(k_l0, mm.GOLD_OMEGA_P)
    assert np.all(rTE_p != 0), "Plasma l=0 r_TE = 0"
    assert np.all(rTE_p < 0), "Plasma l=0 r_TE not negative"
    assert np.all(mm.r_TM_l0(k_l0) == 1), "l=0 r_TM != 1"

    print("PASS: test_reflection_coefficient_limits")


# ============================================================================
# Test 2: Drude(gamma -> 0) recovers plasma model
# ============================================================================
def test_drude_gamma_zero():
    """Verify epsilon_drude(xi, omega_p, gamma->0) = epsilon_plasma(xi, omega_p).

    Acceptance test: test-drude-plasma-relation

    The Drude-plasma difference is O(gamma/xi), so matching to 1e-10
    requires xi/gamma > 1e10. Two complementary checks:
    (a) gamma = 1e-10 * omega_p: match for xi >= omega_p (where xi/gamma >= 1e10)
    (b) gamma = 1e-20 * omega_p: match across full xi range (xi >= 1 m^{-1})

    Both verify the mathematical identity: lim_{gamma->0} epsilon_D = epsilon_P.
    """
    # (a) Plan-specified gamma = 1e-10 * omega_p, tested at xi >= omega_p
    gamma_a = 1e-10 * mm.GOLD_OMEGA_P
    xi_arr_a = np.logspace(np.log10(mm.GOLD_OMEGA_P), 12, 200)

    eps_d_a = mm.epsilon_drude(xi_arr_a, mm.GOLD_OMEGA_P, gamma_a)
    eps_p_a = mm.epsilon_plasma(xi_arr_a, mm.GOLD_OMEGA_P)
    rel_diff_a = np.max(np.abs(eps_d_a - eps_p_a) / eps_p_a)

    assert rel_diff_a < 1e-10, \
        f"Drude(gamma=1e-10*wp) != Plasma for xi>=wp: max rel diff = {rel_diff_a:.2e}"

    # (b) Smaller gamma for full xi range (conclusive mathematical test)
    gamma_b = 1e-20 * mm.GOLD_OMEGA_P
    xi_arr_b = np.logspace(0, 10, 200)

    eps_d_b = mm.epsilon_drude(xi_arr_b, mm.GOLD_OMEGA_P, gamma_b)
    eps_p_b = mm.epsilon_plasma(xi_arr_b, mm.GOLD_OMEGA_P)
    rel_diff_b = np.max(np.abs(eps_d_b - eps_p_b) / eps_p_b)

    assert rel_diff_b < 1e-10, \
        f"Drude(gamma=1e-20*wp) != Plasma: max rel diff = {rel_diff_b:.2e}"

    print(f"PASS: test_drude_gamma_zero (a: {rel_diff_a:.2e}, b: {rel_diff_b:.2e})")


# ============================================================================
# Test 3: Matsubara sum convergence
# ============================================================================
def test_matsubara_convergence():
    """Verify Matsubara sum converges at T=300K, a=1um.

    Acceptance test: test-matsubara-structure (part)
    Doubling l_max changes result by < 10^{-10}.
    """
    T_nat = cl.temperature_to_natural(300.0)
    a = 1e-6
    eps_drude = mm.make_drude(mm.GOLD_OMEGA_P, mm.GOLD_GAMMA)

    F_50 = cl.lifshitz_force(a, T_nat, eps_drude, 'drude',
                             mm.GOLD_OMEGA_P, mm.GOLD_GAMMA, l_max=50)
    F_100 = cl.lifshitz_force(a, T_nat, eps_drude, 'drude',
                              mm.GOLD_OMEGA_P, mm.GOLD_GAMMA, l_max=100)

    rel_change = abs(F_100 - F_50) / abs(F_100)
    assert rel_change < 1e-10, \
        f"Matsubara not converged: rel change = {rel_change:.2e}"

    print(f"PASS: test_matsubara_convergence (rel change = {rel_change:.2e})")


# ============================================================================
# Test 4: Matsubara half-weight (primed sum)
# ============================================================================
def test_matsubara_half_weight():
    """Verify l=0 term enters with factor 1/2.

    Compare lifshitz_force output against manually computed sum.
    """
    T_nat = cl.temperature_to_natural(300.0)
    a = 1e-6
    eps_drude = mm.make_drude(mm.GOLD_OMEGA_P, mm.GOLD_GAMMA)

    # Manually compute: F/A = -(T/pi) * (0.5*t0 + t1 + t2 + t3)
    terms = []
    for l in range(4):
        t = cl.matsubara_term(l, a, T_nat, eps_drude, 'drude',
                              mm.GOLD_OMEGA_P, mm.GOLD_GAMMA)
        terms.append(t)

    manual_sum = 0.5 * terms[0] + sum(terms[1:])
    F_manual = -(T_nat / np.pi) * manual_sum
    F_code = cl.lifshitz_force(a, T_nat, eps_drude, 'drude',
                               mm.GOLD_OMEGA_P, mm.GOLD_GAMMA, l_max=3)

    assert np.isclose(F_manual, F_code, rtol=1e-12), \
        f"Half-weight mismatch: manual={F_manual:.10e}, code={F_code:.10e}"

    # Also verify l=0 term is NOT zero (otherwise half-weight is trivial)
    assert terms[0] != 0, "l=0 term is zero; half-weight test is trivial"

    print(f"PASS: test_matsubara_half_weight (manual={F_manual:.6e}, code={F_code:.6e})")


# ============================================================================
# Test 5: Sign convention
# ============================================================================
def test_sign_convention():
    """Verify lifshitz_force returns F/A < 0 (attractive) for Drude gold."""
    T_nat = cl.temperature_to_natural(300.0)
    a = 1e-6
    eps_drude = mm.make_drude(mm.GOLD_OMEGA_P, mm.GOLD_GAMMA)

    F = cl.lifshitz_force(a, T_nat, eps_drude, 'drude',
                          mm.GOLD_OMEGA_P, mm.GOLD_GAMMA, l_max=50)
    assert F < 0, f"F/A = {F:.6e} is not negative (attractive)"

    print(f"PASS: test_sign_convention (F/A = {F:.6e} < 0)")


# ============================================================================
# Test 6: Vacuum gives zero force
# ============================================================================
def test_vacuum_gives_zero():
    """With epsilon=1, reflection coefficients are zero, so F=0."""
    T_nat = cl.temperature_to_natural(300.0)
    a = 1e-6

    def eps_vacuum(xi):
        return np.ones_like(np.asarray(xi, dtype=float))

    F = cl.lifshitz_force(a, T_nat, eps_vacuum, material_type='vacuum', l_max=10)
    assert abs(F) < 1e-30, f"Vacuum F/A = {F:.6e} != 0"

    print(f"PASS: test_vacuum_gives_zero (F/A = {F:.2e})")


# ============================================================================
# Test 7: T=0 perfect conductor dimensional scaling
# ============================================================================
def test_dimensional_scaling_T0():
    """At T=0 with perfect conductor, F(2a)/F(a) = 1/16 (a^{-4} scaling).

    Acceptance test: test-dimensions-lifshitz
    Also verifies [F/A] = [length^{-4}] via the scaling relation.
    """
    a1 = 1e-6
    a2 = 2e-6

    F1 = cl.lifshitz_force_T0(a1, material_type='perfect')
    F2 = cl.lifshitz_force_T0(a2, material_type='perfect')

    ratio = F2 / F1
    expected = 1.0 / 16.0

    assert abs(ratio - expected) / expected < 1e-8, \
        f"Scaling failed: F(2a)/F(a) = {ratio:.10f}, expected {expected:.10f}"

    # Also check against exact Casimir: F/A = -pi^2/(240*a^4)
    F_exact = -np.pi**2 / (240.0 * a1**4)
    rel_err = abs(F1 - F_exact) / abs(F_exact)
    assert rel_err < 1e-6, \
        f"T=0 perfect conductor: rel error = {rel_err:.2e} (> 1e-6)"

    print(f"PASS: test_dimensional_scaling_T0 "
          f"(ratio={ratio:.10f}, Casimir rel err={rel_err:.2e})")


# ============================================================================
# Run all tests
# ============================================================================
if __name__ == '__main__':
    tests = [
        test_reflection_coefficient_limits,
        test_drude_gamma_zero,
        test_matsubara_convergence,
        test_matsubara_half_weight,
        test_sign_convention,
        test_vacuum_gives_zero,
        test_dimensional_scaling_T0,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"FAIL: {test.__name__}: {e}")
            failed += 1

    print(f"\n{'='*60}")
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    if failed == 0:
        print("ALL TESTS PASSED")
    else:
        print("SOME TESTS FAILED")
        sys.exit(1)
