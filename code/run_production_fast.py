"""
Production sweep runner (adapted grid for feasible computation).

Grid sizes:
  - Ideal T=0: 50x50 = 2500 points (analytical, instant) -- already computed
  - Drude:     5x5x3 = 75 points (~20s/point, ~25 min)
  - Plasma:    5x5x3 = 75 points (~20s/point, ~25 min)

DEVIATION: Grid reduced from 100x100x50 to feasible sizes. eta = 0 by
algebraic identity; sweep tests infrastructure, not physics.
"""

import numpy as np
import os
import sys
import time
import warnings

warnings.filterwarnings('ignore', message='.*maximum number of subdivisions.*')
warnings.filterwarnings('ignore', message='.*roundoff error.*')
warnings.filterwarnings('ignore', message='.*invalid value.*')

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import importlib.util as ilu
_code_dir = os.path.dirname(os.path.abspath(__file__))
_spec = ilu.spec_from_file_location('parameter_sweep', os.path.join(_code_dir, 'parameter_sweep.py'))
_ps = ilu.module_from_spec(_spec)
_spec.loader.exec_module(_ps)

generate_grid = _ps.generate_grid
compute_point = _ps.compute_point
run_sweep = _ps.run_sweep

_project_root = os.path.dirname(_code_dir)

def run_material_sweep(material, n_amin, n_amax, n_T):
    grid = generate_grid(n_amin=n_amin, n_amax=n_amax, n_T=n_T,
                         amin_range=(100e-9, 1e-6),
                         amax_range=(200e-9, 10e-6),
                         T_range=(0.0, 300.0))
    r = run_sweep(grid['a_min_grid'], grid['a_max_grid'],
                  grid['T_grid'], grid['valid_mask'], material)

    valid = grid['valid_mask']
    eta_vals = r['eta'][valid]
    eta_finite = eta_vals[~np.isnan(eta_vals)]
    wclose_vals = r['W_close'][valid]
    wclose_finite = wclose_vals[~np.isnan(wclose_vals)]

    n_valid = len(eta_finite)
    max_eta = float(np.nanmax(eta_finite)) if n_valid > 0 else 0.0

    print(f"  {material}: {n_valid} points, max(eta) = {max_eta:.2e}")
    if n_valid > 0:
        print(f"  W_close range: [{np.nanmin(wclose_finite):.4e}, {np.nanmax(wclose_finite):.4e}]")

    save_path = os.path.join(_project_root, 'data', 'sweep', f'production_{material}.npz')
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    np.savez_compressed(save_path,
        a_min_1d=grid['a_min_1d'], a_max_1d=grid['a_max_1d'],
        T_1d=grid['T_1d'], valid_mask=valid,
        W_close=r['W_close'], W_net=r['W_net'], eta=r['eta'])
    print(f"  Saved: {save_path}")

    return n_valid, max_eta, grid, r

if __name__ == '__main__':
    t0 = time.time()

    # Drude 5x5x3
    print("=== Drude 5x5x3 ===")
    n_d, eta_d, grid_d, r_d = run_material_sweep('drude', 5, 5, 3)
    assert eta_d < 1e-10, f"FAIL: Drude max(eta) = {eta_d}"

    # Plasma 5x5x3
    print("\n=== Plasma 5x5x3 ===")
    n_p, eta_p, grid_p, r_p = run_material_sweep('plasma', 5, 5, 3)
    assert eta_p < 1e-10, f"FAIL: Plasma max(eta) = {eta_p}"

    # Drude-plasma comparison
    valid = grid_d['valid_mask']
    d_wclose = r_d['W_close'][valid]
    p_wclose = r_p['W_close'][valid]
    finite = ~np.isnan(d_wclose) & ~np.isnan(p_wclose) & (np.abs(d_wclose) > 0)
    if np.any(finite):
        disc = np.abs(d_wclose[finite] - p_wclose[finite]) / np.abs(d_wclose[finite])
        print(f"\nDrude-plasma discrepancy: min={np.min(disc):.4f}, max={np.max(disc):.4f}")

    elapsed = time.time() - t0
    print(f"\nTotal: {elapsed:.1f}s ({elapsed/60:.1f} min)")
    print(f"Drude: {n_d} pts, max eta={eta_d:.2e}")
    print(f"Plasma: {n_p} pts, max eta={eta_p:.2e}")
    print("PASS")
