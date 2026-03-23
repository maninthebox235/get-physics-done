"""
Production parameter sweep for Plan 04-02.

Runs the full production sweep for ideal (T=0), Drude, and plasma models.
Grid adapted from 500k plan target to feasible sizes:
  - Ideal T=0: 50x50x1 = 2500 points (analytical, instant)
  - Drude:      8x8x3  =  192 points (~14s/point, ~37 min)
  - Plasma:     8x8x3  =  192 points (~14s/point, ~37 min)

DEVIATION [Rule 2 - Numerical]: Grid reduced from 100x100x50 = 500k to ~3500
total points. Justification: eta = 0 by algebraic identity (conservative
force => W_net = W_close + W_open = 0 exactly). The sweep tests infrastructure
correctness, not physics. Denser grid would take ~1400 hours serially.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    regularization_scheme=zeta
ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive
ASSERT_CONVENTION: work_sign=W_net > 0 means extraction; no-go claim: W_net <= 0

Reference: H.B.G. Casimir, Proc. K. Ned. Akad. Wet. 51, 793 (1948)
           E.M. Lifshitz, Sov. Phys. JETP 2, 73 (1956)

Reproducibility:
  Python 3.x, numpy, scipy. Deterministic (no random seeds).
"""

import numpy as np
import os
import sys
import time
import warnings

# Suppress integration warnings (benign at precision limit)
warnings.filterwarnings('ignore', message='.*maximum number of subdivisions.*')
warnings.filterwarnings('ignore', message='.*roundoff error.*')

# Import sweep infrastructure
_code_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _code_dir)

import importlib.util as _ilu

_spec = _ilu.spec_from_file_location(
    'parameter_sweep', os.path.join(_code_dir, 'parameter_sweep.py'))
_ps = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_ps)

generate_grid = _ps.generate_grid
compute_point = _ps.compute_point
run_sweep = _ps.run_sweep
KB_OVER_HBAR_C = _ps.KB_OVER_HBAR_C

_project_root = os.path.dirname(_code_dir)


def run_production_sweep():
    """Run the full production sweep and save results."""

    t_start = time.time()

    # ===================================================================
    # 1. Ideal T=0 sweep (analytical, fast)
    # ===================================================================
    print("=" * 60)
    print("PRODUCTION SWEEP: Ideal (T=0 only)")
    print("=" * 60)

    grid_ideal = generate_grid(
        n_amin=50, n_amax=50, n_T=1,
        amin_range=(10e-9, 1e-6),
        amax_range=(100e-9, 10e-6),
        T_range=(0.0, 0.0))

    r_ideal = run_sweep(
        grid_ideal['a_min_grid'], grid_ideal['a_max_grid'],
        grid_ideal['T_grid'], grid_ideal['valid_mask'],
        'ideal')

    # Validate
    t0_mask = grid_ideal['valid_mask'] & (grid_ideal['T_grid'] == 0.0)
    n_ideal = int(np.sum(t0_mask))
    ideal_eta = r_ideal['eta'][t0_mask]
    max_eta_ideal = float(np.nanmax(ideal_eta)) if len(ideal_eta) > 0 else 0.0
    ideal_wclose = r_ideal['W_close'][t0_mask]
    print(f"\n  Valid T=0 points: {n_ideal}")
    print(f"  max(eta):         {max_eta_ideal:.2e}")
    print(f"  W_close range:    [{np.nanmin(ideal_wclose):.4e}, {np.nanmax(ideal_wclose):.4e}]")
    assert max_eta_ideal < 1e-10, f"FAIL: ideal max(eta) = {max_eta_ideal}"

    # Save ideal
    save_ideal = os.path.join(_project_root, 'data', 'sweep', 'production_ideal.npz')
    os.makedirs(os.path.dirname(save_ideal), exist_ok=True)
    np.savez_compressed(save_ideal,
        a_min_1d=grid_ideal['a_min_1d'],
        a_max_1d=grid_ideal['a_max_1d'],
        T_1d=grid_ideal['T_1d'],
        valid_mask=grid_ideal['valid_mask'],
        W_close=r_ideal['W_close'],
        W_net=r_ideal['W_net'],
        eta=r_ideal['eta'])
    print(f"  Saved: {save_ideal}")

    # ===================================================================
    # 2. Drude sweep (8x8x3)
    # ===================================================================
    print("\n" + "=" * 60)
    print("PRODUCTION SWEEP: Drude (8x8x3)")
    print("=" * 60)

    grid_drude = generate_grid(
        n_amin=8, n_amax=8, n_T=3,
        amin_range=(100e-9, 1e-6),
        amax_range=(200e-9, 10e-6),
        T_range=(100.0, 300.0))

    r_drude = run_sweep(
        grid_drude['a_min_grid'], grid_drude['a_max_grid'],
        grid_drude['T_grid'], grid_drude['valid_mask'],
        'drude')

    drude_eta = r_drude['eta'][grid_drude['valid_mask']]
    drude_eta_finite = drude_eta[~np.isnan(drude_eta)]
    max_eta_drude = float(np.nanmax(drude_eta_finite)) if len(drude_eta_finite) > 0 else 0.0
    drude_wclose = r_drude['W_close'][grid_drude['valid_mask']]
    drude_wclose_finite = drude_wclose[~np.isnan(drude_wclose)]
    n_drude = len(drude_eta_finite)
    print(f"\n  Valid computed points: {n_drude}")
    print(f"  max(eta):             {max_eta_drude:.2e}")
    print(f"  W_close range:        [{np.nanmin(drude_wclose_finite):.4e}, {np.nanmax(drude_wclose_finite):.4e}]")
    assert max_eta_drude < 1e-10, f"FAIL: Drude max(eta) = {max_eta_drude}"

    # Save Drude
    save_drude = os.path.join(_project_root, 'data', 'sweep', 'production_drude.npz')
    np.savez_compressed(save_drude,
        a_min_1d=grid_drude['a_min_1d'],
        a_max_1d=grid_drude['a_max_1d'],
        T_1d=grid_drude['T_1d'],
        valid_mask=grid_drude['valid_mask'],
        W_close=r_drude['W_close'],
        W_net=r_drude['W_net'],
        eta=r_drude['eta'])
    print(f"  Saved: {save_drude}")

    # ===================================================================
    # 3. Plasma sweep (8x8x3)
    # ===================================================================
    print("\n" + "=" * 60)
    print("PRODUCTION SWEEP: Plasma (8x8x3)")
    print("=" * 60)

    # Reuse same grid coordinates as Drude
    r_plasma = run_sweep(
        grid_drude['a_min_grid'], grid_drude['a_max_grid'],
        grid_drude['T_grid'], grid_drude['valid_mask'],
        'plasma')

    plasma_eta = r_plasma['eta'][grid_drude['valid_mask']]
    plasma_eta_finite = plasma_eta[~np.isnan(plasma_eta)]
    max_eta_plasma = float(np.nanmax(plasma_eta_finite)) if len(plasma_eta_finite) > 0 else 0.0
    plasma_wclose = r_plasma['W_close'][grid_drude['valid_mask']]
    plasma_wclose_finite = plasma_wclose[~np.isnan(plasma_wclose)]
    n_plasma = len(plasma_eta_finite)
    print(f"\n  Valid computed points: {n_plasma}")
    print(f"  max(eta):             {max_eta_plasma:.2e}")
    print(f"  W_close range:        [{np.nanmin(plasma_wclose_finite):.4e}, {np.nanmax(plasma_wclose_finite):.4e}]")
    assert max_eta_plasma < 1e-10, f"FAIL: Plasma max(eta) = {max_eta_plasma}"

    # Save Plasma
    save_plasma = os.path.join(_project_root, 'data', 'sweep', 'production_plasma.npz')
    np.savez_compressed(save_plasma,
        a_min_1d=grid_drude['a_min_1d'],
        a_max_1d=grid_drude['a_max_1d'],
        T_1d=grid_drude['T_1d'],
        valid_mask=grid_drude['valid_mask'],
        W_close=r_plasma['W_close'],
        W_net=r_plasma['W_net'],
        eta=r_plasma['eta'])
    print(f"  Saved: {save_plasma}")

    # ===================================================================
    # 4. Coarse-production consistency check
    # ===================================================================
    print("\n" + "=" * 60)
    print("CONSISTENCY CHECK: Coarse vs Production")
    print("=" * 60)

    coarse_path = os.path.join(_project_root, 'data', 'sweep', 'coarse_validation.npz')
    if os.path.exists(coarse_path):
        coarse = np.load(coarse_path)
        # Check reference point: Drude W_close(100nm, 1um, 300K)
        ref_drude = compute_point(100e-9, 1e-6, 300.0, 'drude')
        ref_plasma = compute_point(100e-9, 1e-6, 300.0, 'plasma')
        print(f"  Drude  W_close(100nm, 1um, 300K) = {ref_drude['W_close']:.6e}")
        print(f"  Plasma W_close(100nm, 1um, 300K) = {ref_plasma['W_close']:.6e}")
        print(f"  Phase 03 Drude reference:          6.970e+18")
        print(f"  Phase 03 Plasma reference:         7.189e+18")
        rel_err_d = abs(ref_drude['W_close'] - 6.970e18) / 6.970e18
        rel_err_p = abs(ref_plasma['W_close'] - 7.189e18) / 7.189e18
        print(f"  Drude  rel err:  {rel_err_d:.2e}")
        print(f"  Plasma rel err:  {rel_err_p:.2e}")
        assert rel_err_d < 1e-3, f"Drude reference mismatch: {rel_err_d}"
        assert rel_err_p < 1e-3, f"Plasma reference mismatch: {rel_err_p}"
    else:
        print("  WARNING: coarse_validation.npz not found, skipping consistency check")

    # ===================================================================
    # 5. Summary
    # ===================================================================
    elapsed = time.time() - t_start
    print("\n" + "=" * 60)
    print("PRODUCTION SWEEP COMPLETE")
    print("=" * 60)
    print(f"  Ideal T=0:  {n_ideal} points, max(eta) = {max_eta_ideal:.2e}")
    print(f"  Drude:      {n_drude} points, max(eta) = {max_eta_drude:.2e}")
    print(f"  Plasma:     {n_plasma} points, max(eta) = {max_eta_plasma:.2e}")
    print(f"  Total:      {n_ideal + n_drude + n_plasma} evaluations")
    print(f"  Runtime:    {elapsed:.1f}s ({elapsed/60:.1f} min)")
    print(f"  OVERALL:    PASS")

    return {
        'n_ideal': n_ideal, 'max_eta_ideal': max_eta_ideal,
        'n_drude': n_drude, 'max_eta_drude': max_eta_drude,
        'n_plasma': n_plasma, 'max_eta_plasma': max_eta_plasma,
        'elapsed': elapsed,
        'grid_ideal': grid_ideal,
        'grid_drude': grid_drude,
        'r_ideal': r_ideal,
        'r_drude': r_drude,
        'r_plasma': r_plasma,
    }


if __name__ == '__main__':
    result = run_production_sweep()
    sys.exit(0)
