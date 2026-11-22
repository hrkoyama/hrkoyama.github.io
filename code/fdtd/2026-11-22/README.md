# Yee FDTD: periodic wave and PEC cavity / 周期波・完全導体空洞

Original educational **two-dimensional TMz** Maxwell solver. Python 3.12;
NumPy performs the update, Matplotlib draws saved results, pytest runs tests.
Normalized units: epsilon=mu=c=1, unit electric-field amplitude, lengths
Lx=1 and Ly=1.5. No external solver supplies the numerical solution.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs/periodic-wave.json --output output-wave
python run.py --input inputs/pec-cavity.json --output output-cavity
```

Use a new or empty output directory. Exit status: 0 all numerical criteria pass,
1 numerical acceptance failed, 2 invalid input/runtime error. Fixed inputs
contain meshes, budgets and acceptance tolerances. Each execution saves
`result.json` (input SHA-256, environment, metrics, decisions, termination),
`convergence.csv`, `energy.csv`, `solution.csv` and `summary.png`.
The numerical field and analytic field in solution.csv are the final
**accuracy-time** electric fields, not the later end of the energy run.

## Model and staggered update / モデル・変数配置

The source-free equations are

    Hx_t = -Ez_y,  Hy_t = Ez_x,  Ez_t = Hy_x - Hx_y.

Ez lives at integer x,y nodes and integer times; Hx at (x,y+dy/2), Hy at
(x+dx/2,y), both at half times. A state contains E(n dt) and H((n-1/2)dt).
Update H first from spatial forward differences of E, then E from backward
differences of the new H. Periodic arrays wrap without duplicate endpoints.
For the cavity, E includes the wall nodes, which are exactly zero; normal H
wall values are zero for the chosen mode. The spatial inner product uses
cell-area quadrature and half weights on the cavity's boundary nodes.

The strict input condition is dt sqrt(dx^-2+dy^-2)<1. The equality endpoint
is rejected, so the modified-energy quadratic form remains coercive. Rejection
of an invalid time step is not an experimental measurement of unstable growth.

## Independent continuum solutions / 連続解析解

For the periodic traveling wave, k=(2 pi/Lx,2 pi/Ly), omega=|k|:

    Ez = cos(kx x+ky y-omega t)
    Hx = (ky/omega) cos(kx x+ky y-omega t)
    Hy = -(kx/omega) cos(kx x+ky y-omega t).

For the PEC standing wave, k=(pi/Lx,pi/Ly), omega=|k|:

    Ez = sin(kx x) sin(ky y) cos(omega t)
    Hx = -(ky/omega) sin(kx x) cos(ky y) sin(omega t)
    Hy = (kx/omega) cos(kx x) sin(ky y) sin(omega t).

Initial H is sampled from these continuum solutions at -dt/2, separately at
the Hx and Hy positions. Compare all components at their own staggered
positions/times after **1.1 analytic periods**. Meshes 16x24,32x48,64x96
and Courant factor 0.7 refine both space and time. The time step is reduced
slightly to reach the same physical accuracy end time on each mesh. Combined
L2 error is normalized by the constant continuum total field norm: Area for
the periodic wave, Area/4 for the cavity. Report E and H errors with that
same common normalization, avoiding divisions by temporal nodes of E or H.

Field refinement checks at least order1.8 and finest error<=0.01. The source
also measures frequency from the evolved electric-mode amplitude a(n) through

    cos(Omega dt) = sum a(n)[a(n-1)+a(n+1)] / [2 sum a(n)^2].

This is an oscillator-recurrence measurement, not an FFT estimate or an
independent field solver. Compare it separately with the continuum omega and
the exact Yee dispersion relation

    sin(Omega dt/2)^2/dt^2
      = sin(kx dx/2)^2/dx^2 + sin(ky dy/2)^2/dy^2.

The discrete-frequency identity is not the physical accuracy criterion:
physical frequency error and its second-order refinement are separate checks.

## Energy and divergence / エネルギー・発散

Run **12 analytic periods** at every mesh. With H-=H(n-1/2), H+=H(n+1/2),
the source-free periodic/PEC scheme conserves the modified discrete energy

    U* = (||E(n)||^2 + <H-,H+>)/2.

The physical-energy diagnostic reconstructs H at E's time:

    Hbar=(H-+H+)/2,
    Ucentered=(||E(n)||^2+||Hbar||^2)/2,
    Ucentered-U* = ||H+-H-||^2/8.

Thus Ucentered is generally **not exactly conserved**. Compare it with
the continuum integrated energy Area/2 (periodic unit traveling wave) or
Area/8 (PEC unit standing wave). Check maximum absolute relative energy
error and its grid/time refinement; the span is reported separately and
may superconverge for a traveling mode. Acceptance: modified-energy relative
drift<=2e-11, finest physical-energy error<=0.003, physical-energy error
refinement>=1.8. The normalized model has no source or boundary energy flux.

The scheme preserves the **initial discrete divergence**. Sampling continuous
oblique H generally gives an initial O(h^2) discrete divergence residual;
the result reports it and checks its subsequent absolute change<=2e-10.
Do not read this as absolute magnetic divergence zero. Separate exact
discrete-mode tests use discrete derivative symbols in H amplitudes and
verify divergence near roundoff. Random multimode periodic/PEC tests check
the energy and divergence identities beyond a single eigenmode.

## 日本語の要点

真空・一様媒質の2次元TMzに範囲を限定します。周期境界の斜め平面波と、
完全導体長方形空洞の定在波を、同じYee更新で計算します。連続解析解との差、
格子と時間の同時細分化、実測した振動数、離散分散関係、12周期のエネルギーを
別々に判定します。電場・磁場の位置と時刻のずれを参照解にも反映します。

厳密に保存される離散修正エネルギーと、磁場を同時刻へ平均した物理エネルギーを
区別します。初期離散発散の保存は、発散の絶対値がゼロという主張ではありません。
各許容値はJSON入力で固定し、失敗を成功として記録しません。

PML・吸収境界、媒質界面、分散・損失、電荷・電流、TEz、3次元、任意形状、
一般励起や実験比較は今回の検証範囲に含みません。

## Sources and terms / 出典・利用条件

- K. S. Yee (1966), original staggered-grid formulation:
  https://doi.org/10.1109/TAP.1966.1138693 . Bilingual atlas cites the paper;
  no third-party article text is included in this source package.
- F. Bekmambetova, X. Zhang, P. Triverio, *A Dissipation Theory for
  Three-Dimensional FDTD with Application to Stability Analysis and
  Subgridding*: https://arxiv.org/html/1705.02274v2 , Section III, equation26
  (modified discrete energy) and equation35 (strict CFL). The current 2D
  specialization is verified independently by random-field tests.

Original code: MIT, see LICENSE. Inputs, generated outputs, figures and prose
retain item-specific terms at https://hrkoyama.github.io/rights/ . Dependencies
retain their own licenses. This is an educational implementation with the
scope above, not a general electromagnetic simulation package.
