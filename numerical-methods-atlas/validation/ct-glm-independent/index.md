# Orszag–Tang：CT・GLMと独立Athena++比較

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

## 前提・単位・境界

単位正方形、γ=5/3、μ₀=1、vz=Bz=0、t=0.05。rho=25/(36π)、p=5/(12π)、v=(-sin2πy,sin2πx)、B=(-sin2πy,sin4πx)/sqrt(4π)。

**編集上の補足**

採用GLMはch=3、減衰率κ=0.18 ch nです。nは各軸のセル数で、この減衰は格子依存です。同じ連続初期場・終了時刻・CFLを用いますが、CT/GLMで実ステップ数とdiv Bのnative演算子は異なります。

## 採用した計算法

公開済みの1次Rusanov/前進Eulerを再利用。CTは共有corner EMFの離散curl、GLMはcell中心Bと双曲・放物型cleaning。Athena++は別実装のHLLD+PLM+RK2。

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

## 比較・検証

16²/32²/64²で密度とByのL1誤差、質量・エネルギードリフト、正値性を測定。独立参照は128²/256²でも収束を確認し、細胞平均を保存的に制限します。

## 確認の限界

CTの面上divergenceとGLMの中心差分divergenceは異なる演算子です。共通cell演算子の値も別記します。Athenaの初期磁場はベクトルポテンシャルの差分による面平均で、同じ連続場の離散化差を含みます。短時間の平面MHD比較であり、衝撃波・3D・UCTやCTUの検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "reference_density_128_256_l1": 4.631344236627223e-05,
    "ct_glm_finest_density_l1": 0.0016910992352830488
  },
  "checks": {
    "independent_reference_refined": true,
    "ct_native_constraint_16": true,
    "ct_native_constraint_32": true,
    "ct_native_constraint_64": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_refinement": true,
    "conservation": true,
    "positive_states": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Orszag–Tang: CT, GLM and independent Athena++

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

## Assumptions, units and boundaries

Unit square, gamma=5/3, mu0=1, vz=Bz=0, t=0.05. rho=25/(36pi), p=5/(12pi), v=(-sin2piy,sin2pix), B=(-sin2piy,sin4pix)/sqrt(4pi).

**Editorial clarification**

The adopted GLM uses ch=3 and damping rate kappa=0.18 ch n, with n cells per axis: damping is grid dependent. Both use the same continuous initial field, final time and CFL, while actual step counts and native div B operators differ.

## Adopted numerical method

Reuse the published first-order Rusanov/forward-Euler solvers: shared corner-EMF discrete curl for CT and cell-centered hyperbolic/parabolic GLM cleaning. Independent Athena++ uses HLLD, PLM and RK2.

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

## References and validation

Measure density/By L1 error, mass/energy drift and positivity on 16²/32²/64². Check the independent 128²/256² reference and conservatively restrict its fine-cell averages.

## Limits

Face CT divergence and centered GLM divergence use different operators; common cell-centered diagnostics are also reported. Athena initializes face-averaged magnetic fields by differencing a vector potential, so comparison includes discretization differences of identical continuous data. This is a short planar test, not validation of shocks, 3D, UCT or CTU.

## Stored measurements and decisions

```json
{
  "metrics": {
    "reference_density_128_256_l1": 4.631344236627223e-05,
    "ct_glm_finest_density_l1": 0.0016910992352830488
  },
  "checks": {
    "independent_reference_refined": true,
    "ct_native_constraint_16": true,
    "ct_native_constraint_32": true,
    "ct_native_constraint_64": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_refinement": true,
    "conservation": true,
    "positive_states": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
