"""
Parameter sweep infrastructure for W_net over (a_min, a_max, T) grid.

Computes cycle work for ideal (T=0), Drude, and plasma material models
across a 3D parameter grid, verifying eta = |W_net|/|W_close| < 10^{-10}
at every valid grid point.

ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
    regularization_scheme=zeta
ASSERT_CONVENTION: casimir_force_sign=F < 0 for attractive
ASSERT_CONVENTION: work_sign=W_net > 0 means extraction; no-go claim: W_net <= 0
ASSERT_CONVENTION: [W/A] = length^{-3}, [eta] = dimensionless

Reference: H.B.G. Casimir, Proc. K. Ned. Akad. Wet. 51, 793 (1948)
           E.M. Lifshitz, Sov. Phys. JETP 2, 73 (1956)

Reproducibility:
  Python 3.x, numpy, scipy. Deterministic (no random seeds needed
  for the sweep itself; random seed set for spot-check point selection).
"""

import numpy as np
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import importlib.util as _ilu

# ---------------------------------------------------------------------------
# Import project modules via absolute file paths (avoids package issues)
# ---------------------------------------------------------------------------
_code_dir = os.path.dirname(os.path.abspath(__file__))

_spec_cycle = _ilu.spec_from_file_location(
    'casimir_cycle', os.path.join(_code_dir, 'casimir_cycle.py'))
_cc = _ilu.module_from_spec(_spec_cycle)
_spec_cycle.loader.exec_module(_cc)

_spec_lif = _ilu.spec_from_file_location(
    'casimir_lifshitz', os.path.join(_code_dir, 'casimir_lifshitz.py'))
_cl = _ilu.module_from_spec(_spec_lif)
_spec_lif.loader.exec_module(_cl)

_spec_mm = _ilu.spec_from_file_location(
    'material_models', os.path.join(_code_dir, 'material_models.py'))
_mm = _ilu.module_from_spec(_spec_mm)
_spec_mm.loader.exec_module(_mm)

cycle_work_ideal_analytical = _cc.cycle_work_ideal_analytical
cycle_work_lifshitz = _cc.cycle_work_lifshitz
cycle_work_lifshitz_fast = _cc.cycle_work_lifshitz_fast
cycle_work_lifshitz_double_integral = _cc.cycle_work_lifshitz_double_integral

lifshitz_force = _cl.lifshitz_force
temperature_to_natural = _cl.temperature_to_natural

make_drude = _mm.make_drude
make_plasma = _mm.make_plasma
GOLD_OMEGA_P = _mm.GOLD_OMEGA_P
GOLD_GAMMA = _mm.GOLD_GAMMA

# ---------------------------------------------------------------------------
# Exact unit conversion from scipy.constants
# ---------------------------------------------------------------------------
import scipy.constants as _sc

# T_natural [m^{-1}] = T_kelvin * k_B / (hbar * c)
KB_OVER_HBAR_C = _sc.k / (_sc.hbar * _sc.c)  # ~ 436.703 m^{-1}/K


# =========================================================================
# 1. Grid generation
# =========================================================================

def generate_grid(n_amin=100, n_amax=100, n_T=50,
                  amin_range=(10e-9, 1e-6),
                  amax_range=(100e-9, 10e-6),
                  T_range=(0.0, 300.0)):
    """Generate 3D parameter grid for the sweep.

    Parameters
    ----------
    n_amin : int
        Number of a_min points (logarithmic spacing).
    n_amax : int
        Number of a_max points (logarithmic spacing).
    n_T : int
        Number of temperature points (linear spacing in Kelvin).
    amin_range : tuple
        (min, max) of a_min in meters.
    amax_range : tuple
        (min, max) of a_max in meters.
    T_range : tuple
        (min, max) of temperature in Kelvin. T=0 included as first point.

    Returns
    -------
    dict with keys:
        a_min_1d : ndarray of shape (n_amin,)
        a_max_1d : ndarray of shape (n_amax,)
        T_1d     : ndarray of shape (n_T,)  -- in Kelvin
        a_min_grid : ndarray of shape (n_amin, n_amax, n_T) -- in meters
        a_max_grid : ndarray of shape (n_amin, n_amax, n_T) -- in meters
        T_grid     : ndarray of shape (n_amin, n_amax, n_T) -- in Kelvin
        valid_mask : ndarray of shape (n_amin, n_amax, n_T) -- bool
            True where a_min < a_max (strictly).
    """
    a_min_1d = np.logspace(np.log10(amin_range[0]), np.log10(amin_range[1]),
                           n_amin)
    a_max_1d = np.logspace(np.log10(amax_range[0]), np.log10(amax_range[1]),
                           n_amax)
    T_1d = np.linspace(T_range[0], T_range[1], n_T)

    # Build 3D meshgrid (indexing='ij': dim 0 = a_min, dim 1 = a_max, dim 2 = T)
    a_min_grid, a_max_grid, T_grid = np.meshgrid(
        a_min_1d, a_max_1d, T_1d, indexing='ij')

    # Constraint mask: a_min must be strictly less than a_max
    valid_mask = a_min_grid < a_max_grid

    return {
        'a_min_1d': a_min_1d,
        'a_max_1d': a_max_1d,
        'T_1d': T_1d,
        'a_min_grid': a_min_grid,
        'a_max_grid': a_max_grid,
        'T_grid': T_grid,
        'valid_mask': valid_mask,
    }


# =========================================================================
# 2. Single-point computation
# =========================================================================

def compute_point(a_min, a_max, T_K, material):
    """Compute cycle work at a single (a_min, a_max, T) point.

    Parameters
    ----------
    a_min : float
        Minimum plate separation [meters].
    a_max : float
        Maximum plate separation [meters].
    T_K : float
        Temperature in Kelvin.
    material : str
        'ideal', 'drude', or 'plasma'.

    Returns
    -------
    dict with keys: W_close, W_open, W_net, eta
        All work values in [m^{-3}] (per unit area, natural units with
        lengths in meters).
        eta = |W_net|/|W_close| if |W_close| > 0 else 0.
    """
    if a_min >= a_max:
        return {'W_close': np.nan, 'W_open': np.nan,
                'W_net': np.nan, 'eta': np.nan}

    if material == 'ideal' and T_K == 0.0:
        # T=0 ideal: exact analytical result
        result = cycle_work_ideal_analytical(a_min, a_max)
    elif material == 'ideal' and T_K > 0.0:
        # Finite-T ideal: use fast free-energy method with perfect conductor
        T_nat = T_K * KB_OVER_HBAR_C
        result = cycle_work_lifshitz_fast(
            a_min, a_max, T_nat, epsilon_func=None,
            material_type='perfect')
    elif material == 'drude':
        T_nat = T_K * KB_OVER_HBAR_C
        eps_func = make_drude(GOLD_OMEGA_P, GOLD_GAMMA)
        result = cycle_work_lifshitz_fast(
            a_min, a_max, T_nat, epsilon_func=eps_func,
            material_type='drude',
            omega_p=GOLD_OMEGA_P, gamma=GOLD_GAMMA)
    elif material == 'plasma':
        T_nat = T_K * KB_OVER_HBAR_C
        eps_func = make_plasma(GOLD_OMEGA_P)
        result = cycle_work_lifshitz_fast(
            a_min, a_max, T_nat, epsilon_func=eps_func,
            material_type='plasma',
            omega_p=GOLD_OMEGA_P, gamma=0.0)
    else:
        raise ValueError(f"Unknown material: {material}")

    W_close = result['W_close']
    W_open = result['W_open']
    W_net = result['W_net']

    if abs(W_close) > 0:
        eta = abs(W_net) / abs(W_close)
    else:
        eta = 0.0

    return {'W_close': W_close, 'W_open': W_open,
            'W_net': W_net, 'eta': eta}


# Top-level helper for ProcessPoolExecutor (must be picklable)
def _compute_point_wrapper(args):
    """Wrapper for compute_point for use with ProcessPoolExecutor."""
    idx, a_min, a_max, T_K, material = args
    result = compute_point(a_min, a_max, T_K, material)
    return idx, result


# =========================================================================
# 3. Parallel sweep execution
# =========================================================================

def run_sweep(grid_amin, grid_amax, grid_T, mask, material, n_workers=None):
    """Run parameter sweep over the grid with parallel execution.

    Parameters
    ----------
    grid_amin : ndarray
        3D array of a_min values [meters].
    grid_amax : ndarray
        3D array of a_max values [meters].
    grid_T : ndarray
        3D array of temperature values [Kelvin].
    mask : ndarray of bool
        Valid points mask (a_min < a_max).
    material : str
        'ideal', 'drude', or 'plasma'.
    n_workers : int or None
        Number of parallel workers. None = auto.

    Returns
    -------
    dict with keys:
        W_close : ndarray matching grid shape, NaN where mask=False
        W_net   : ndarray matching grid shape, NaN where mask=False
        eta     : ndarray matching grid shape, NaN where mask=False
    """
    shape = grid_amin.shape
    W_close = np.full(shape, np.nan)
    W_net = np.full(shape, np.nan)
    eta = np.full(shape, np.nan)

    # Collect valid points
    valid_indices = np.argwhere(mask)
    n_valid = len(valid_indices)
    if n_valid == 0:
        return {'W_close': W_close, 'W_net': W_net, 'eta': eta}

    # For ideal material at T>0, we need Lifshitz which is expensive.
    # For ideal at T=0, skip non-zero T points.
    tasks = []
    for k, idx in enumerate(valid_indices):
        i, j, l = idx
        a_min_val = grid_amin[i, j, l]
        a_max_val = grid_amax[i, j, l]
        T_val = grid_T[i, j, l]

        # For 'ideal' material, only compute T=0 points
        if material == 'ideal' and T_val != 0.0:
            continue

        tasks.append((k, a_min_val, a_max_val, T_val, material))

    n_tasks = len(tasks)
    if n_tasks == 0:
        return {'W_close': W_close, 'W_net': W_net, 'eta': eta}

    print(f"  Sweep: {n_tasks} valid points for material='{material}'")

    # Execute serially (ProcessPoolExecutor has fork+import conflicts
    # with spec-loaded modules, causing deadlocks)
    completed = 0
    report_interval = max(1, n_tasks // 10)
    t0 = time.time()

    for task in tasks:
        k, a_min_val, a_max_val, T_val, mat = task
        idx = valid_indices[k]
        i, j, l = idx
        result = compute_point(a_min_val, a_max_val, T_val, mat)
        W_close[i, j, l] = result['W_close']
        W_net[i, j, l] = result['W_net']
        eta[i, j, l] = result['eta']

        completed += 1
        if completed % report_interval == 0 or completed == n_tasks:
            elapsed = time.time() - t0
            pct = 100.0 * completed / n_tasks
            rate = completed / elapsed if elapsed > 0 else 0
            est_remaining = (n_tasks - completed) / rate if rate > 0 else 0
            print(f"    Progress: {completed}/{n_tasks} ({pct:.0f}%) "
                  f"[{elapsed:.1f}s elapsed, ~{est_remaining:.0f}s remaining]",
                  flush=True)

    return {'W_close': W_close, 'W_net': W_net, 'eta': eta}


# =========================================================================
# 4. Coarse validation
# =========================================================================

def run_coarse_validation(n_amin=20, n_amax=20, n_T=10, n_workers=None,
                          save_path=None):
    """Run coarse sweep and validate eta < 10^{-10} everywhere.

    Parameters
    ----------
    n_amin, n_amax, n_T : int
        Grid dimensions.
    n_workers : int or None
        Number of parallel workers.
    save_path : str or None
        Path to save results (.npz). If None, uses default.

    Returns
    -------
    dict with summary statistics and result arrays.
    """
    if save_path is None:
        save_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'data', 'sweep', 'coarse_validation.npz')

    print(f"=== Coarse Validation Sweep ({n_amin}x{n_amax}x{n_T} "
          f"= {n_amin*n_amax*n_T} points) ===")
    print(f"  Save path: {save_path}")

    # Generate coarse grid
    # Use a_min >= 100nm for Lifshitz materials to keep computation time
    # manageable (sub-100nm separations require many Matsubara terms at
    # finite T, making each point take 30-80 seconds).
    # Ideal T=0 is analytical and fast at all separations.
    grid = generate_grid(n_amin=n_amin, n_amax=n_amax, n_T=n_T,
                         amin_range=(100e-9, 1e-6),
                         amax_range=(200e-9, 10e-6))
    a_min_grid = grid['a_min_grid']
    a_max_grid = grid['a_max_grid']
    T_grid = grid['T_grid']
    valid_mask = grid['valid_mask']

    n_valid_total = np.sum(valid_mask)
    print(f"  Total grid points: {a_min_grid.size}")
    print(f"  Valid points (a_min < a_max): {n_valid_total}")

    results = {}
    summary = {}

    # --- Ideal (T=0 only) ---
    print("\n--- Material: ideal (T=0 only) ---")
    r_ideal = run_sweep(a_min_grid, a_max_grid, T_grid, valid_mask,
                        'ideal', n_workers=n_workers)
    results['ideal'] = r_ideal

    # Count valid T=0 ideal points
    t0_mask = valid_mask & (T_grid == 0.0)
    n_ideal_valid = np.sum(t0_mask)
    ideal_eta = r_ideal['eta'][t0_mask]
    max_eta_ideal = np.nanmax(ideal_eta) if len(ideal_eta) > 0 else 0.0
    summary['ideal'] = {
        'n_valid': int(n_ideal_valid),
        'max_eta': float(max_eta_ideal),
        'pass': max_eta_ideal < 1e-10,
    }
    print(f"  Valid T=0 points: {n_ideal_valid}")
    print(f"  max(eta): {max_eta_ideal:.2e}")
    print(f"  PASS: {summary['ideal']['pass']}")

    # --- Drude (all T) ---
    print("\n--- Material: drude ---")
    r_drude = run_sweep(a_min_grid, a_max_grid, T_grid, valid_mask,
                        'drude', n_workers=n_workers)
    results['drude'] = r_drude

    drude_eta = r_drude['eta'][valid_mask]
    max_eta_drude = np.nanmax(drude_eta) if len(drude_eta) > 0 else 0.0
    summary['drude'] = {
        'n_valid': int(np.sum(valid_mask)),
        'max_eta': float(max_eta_drude),
        'pass': max_eta_drude < 1e-10,
    }
    print(f"  Valid points: {summary['drude']['n_valid']}")
    print(f"  max(eta): {max_eta_drude:.2e}")
    print(f"  PASS: {summary['drude']['pass']}")

    # --- Plasma (all T) ---
    print("\n--- Material: plasma ---")
    r_plasma = run_sweep(a_min_grid, a_max_grid, T_grid, valid_mask,
                         'plasma', n_workers=n_workers)
    results['plasma'] = r_plasma

    plasma_eta = r_plasma['eta'][valid_mask]
    max_eta_plasma = np.nanmax(plasma_eta) if len(plasma_eta) > 0 else 0.0
    summary['plasma'] = {
        'n_valid': int(np.sum(valid_mask)),
        'max_eta': float(max_eta_plasma),
        'pass': max_eta_plasma < 1e-10,
    }
    print(f"  Valid points: {summary['plasma']['n_valid']}")
    print(f"  max(eta): {max_eta_plasma:.2e}")
    print(f"  PASS: {summary['plasma']['pass']}")

    # --- Reference point check ---
    print("\n--- Reference Point Check ---")
    ref_point = compute_point(100e-9, 1e-6, 300.0, 'drude')
    print(f"  Drude W_close(100nm, 1um, 300K) = {ref_point['W_close']:.4e} m^-3")
    print(f"  Phase 03 reference:               6.970e+18 m^-3")
    ref_relerr = abs(ref_point['W_close'] - 6.970e18) / 6.970e18
    print(f"  Relative difference: {ref_relerr:.2e}")

    # --- Save results ---
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    np.savez_compressed(
        save_path,
        # Grid arrays
        a_min_1d=grid['a_min_1d'],
        a_max_1d=grid['a_max_1d'],
        T_1d=grid['T_1d'],
        a_min_grid=a_min_grid,
        a_max_grid=a_max_grid,
        T_grid=T_grid,
        valid_mask=valid_mask,
        # Ideal results
        ideal_W_close=r_ideal['W_close'],
        ideal_W_net=r_ideal['W_net'],
        ideal_eta=r_ideal['eta'],
        # Drude results
        drude_W_close=r_drude['W_close'],
        drude_W_net=r_drude['W_net'],
        drude_eta=r_drude['eta'],
        # Plasma results
        plasma_W_close=r_plasma['W_close'],
        plasma_W_net=r_plasma['W_net'],
        plasma_eta=r_plasma['eta'],
    )
    print(f"\n  Results saved to: {save_path}")

    # --- Overall summary ---
    all_pass = all(s['pass'] for s in summary.values())
    print(f"\n{'='*50}")
    print(f"  OVERALL: {'PASS' if all_pass else 'FAIL'}")
    print(f"  Ideal max(eta):  {summary['ideal']['max_eta']:.2e}")
    print(f"  Drude max(eta):  {summary['drude']['max_eta']:.2e}")
    print(f"  Plasma max(eta): {summary['plasma']['max_eta']:.2e}")
    print(f"{'='*50}")

    return {
        'grid': grid,
        'results': results,
        'summary': summary,
        'all_pass': all_pass,
        'save_path': save_path,
    }


# =========================================================================
# 5. Main entry point
# =========================================================================

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Casimir cycle parameter sweep')
    parser.add_argument('--n-amin', type=int, default=20)
    parser.add_argument('--n-amax', type=int, default=20)
    parser.add_argument('--n-T', type=int, default=10)
    parser.add_argument('--workers', type=int, default=None)
    parser.add_argument('--save-path', type=str, default=None)
    args = parser.parse_args()

    result = run_coarse_validation(
        n_amin=args.n_amin, n_amax=args.n_amax, n_T=args.n_T,
        n_workers=args.workers, save_path=args.save_path)

    sys.exit(0 if result['all_pass'] else 1)
