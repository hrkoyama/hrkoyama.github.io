# Periodic two-He DFT forces / 周期He₂のDFT原子間力

Original validation and BO-interface **driver backed by PySCF 2.11.0**, not a new
DFT engine. PySCF supplies KRKS, FFTDF, Libxc and analytic nuclear gradients,
including moving-Gaussian overlap/Pulay terms and ionic Ewald derivatives.
Independent DFTK 0.7.19 plane waves reproduce the same scientific model.

PySCFを用いた検証・BOMD受け渡し用の教育コードです。自作DFTエンジンではありません。
原子を動かすGaussian基底のPulay項とイオンEwald項を含む解析力を、全エネルギーの
中央差分および独立なDFTK平面波計算と照合します。

## Fixed model / 固定モデル

Artificial periodic **two-He, four-valence-electron** cell. Cubic lattice 5bohr;
Cartesian atom positions (bohr) `[.37,.61,.83]`, `[2.13,2.27,2.41]`. Nonrelativistic,
neutral, spin-unpolarized KS-LDA (`LDA_X,LDA_C_VWN`, VWN5), zero electronic
temperature, integer occupations, exact local He-GTH-PADE-q2 coefficients in
inputs.json. This displaced pedagogical insulator is **not an equilibrium helium
material prediction**. No fitted energy or force offsets are applied.

5bohr立方セルに非対称な位置のHeを2個置いた人工的な検証例です。価電子4個・非偏極
VWN5-LDA・局所GTHを使い、平衡He結晶や一般材料の物理精度を検証したとは主張しません。

## Run / 実行

    python -m pip install -r requirements.txt
    python -m pytest -q
    python run.py --input inputs.json --output output

The output directory must be new or empty. Outputs: result.json, solution.csv,
finite-difference.csv, scf.csv. Exit0: all criteria pass;1: a numerical criterion
fails;2: invalid input/runtime error. The optional plot is regenerated with:

    python -m pip install -r requirements-plotting.txt
    python plot_results.py --result output/result.json --output output/preview.png

## Validation scope / 検証範囲

- All six Cartesian force components against `-(E(R+h)-E(R-h))/(2h)` with
  h=.002bohr, plus a .008/.004/.002bohr scan on one component. Every displaced
  SCF is re-converged from the same undisplaced initial density, never accepted
  merely because the energy is finite.
- Separate force changes for Γ/2³/3³/4³ equal-weight explicit k meshes, Gaussian
  DZV/DZVP/TZV2P/QZV3P families, FFT31³/39³/47³ grids and SCF tolerances. The k
  sweep uses DZVP; orbital-basis sweeps occur at Γ **and**2³. These sampled last
  increments are stopping criteria, not rigorous complete-basis/error bounds.
- QZV3P analytic forces and unshifted per-cell energies against DFTK at Γ and2³.
  The independent reference contains90/120/180/240Ha cutoff convergence and its
  own all-six-component finite differences. `README-reference.txt` explains the
  separately pinned Julia environment. Python does not secretly import DFTK or
  regenerate reference numbers during acceptance.
- Electron number, overlap eigenvalues/condition, orbital orthogonality,
  reconstructed energy, final-density SCF commutators and sampled KS gaps.
  A positive sampled gap is not a fundamental gap/global-spectrum validation.
- An actual force-provider/velocity-Verlet smoke check: one8-atomic-time-unit
  step versus two half steps with freshly converged electronic forces. Atomic
  units are explicit; unconverged/nonfinite forces cannot advance nuclei.
  The integrator is separately checked for second-order convergence against an
  exact harmonic oscillator. **No long-time NVE trajectory, temperature
  distribution, thermostat, CPMD, stress or barostat is validated.**

全6成分の中央差分、独立平面波参照、基底・k点・FFT補助格子・SCFをそれぞれ変えた力の
収束を記録します。Γだけではこの力は収束しません。基底族は入れ子の変分列ではなく、
最後の差を完全基底誤差の厳密上界とはしません。BOMD接続は原子単位の力APIと短い
velocity-Verlet受け渡し試験までです。長時間のNVE、温度制御やCPMDの検証とは区別します。

## BO force callback / 力API

`periodic_forces.energy_and_forces(config,spec,positions_bohr)` returns a record
with `energy_per_cell` (Eh), `forces_cartesian` (2x3, Eh/bohr), `converged`,
`positions_bohr` and electronic diagnostics. The sign is **force = minus total
energy gradient**, including ions. It raises when SCF has not converged
sufficiently. An optional `density_guess=` changes only the initial iterate;
all electronic conditions/tolerances remain fixed. `bomd.velocity_verlet_step`
consumes this callback, Cartesian bohr velocities per atomic time and masses in
electron masses. It checks cached-force geometry before reuse.

## Rights / ライセンス

Original Python/Julia driver source: MIT (LICENSE). PySCF: Apache2.0; DFTK: MIT;
Libxc7: MPL2.0. Gaussian basis/GTH numerical data keep upstream provenance and
applicable terms; the driver MIT label does not relicense third-party data or
software. No third-party software source is bundled. Basis data are resolved
from the pinned PySCF installation and their hashes are documented in
provenance.json. Inputs/results/figures/prose follow the site's item-specific
terms: https://hrkoyama.github.io/rights/ .
