# GLMの磁気単極子モード：解析的減衰

GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。

**使用手法**

- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-algorithm)

∂tBx=-∂xpsi、∂tpsi=-ch²∂xBx-κpsiを中心差分とRK4で積分。独立参照は連続Fourier記号の2×2行列指数です。

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![GLMの磁気単極子モード：解析的減衰：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-validation)

16/32/64点でL2誤差、空間2次収束、磁場divergenceモード振幅の減衰を判定します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

周期[0,1]、Bx=cos2πx、psi=0、ch=1、減衰κ=2、t=1。流体との結合を外した線形診断です。

## 採用した計算法

∂tBx=-∂xpsi、∂tpsi=-ch²∂xBx-κpsiを中心差分とRK4で積分。独立参照は連続Fourier記号の2×2行列指数です。

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

## 比較・検証

16/32/64点でL2誤差、空間2次収束、磁場divergenceモード振幅の減衰を判定します。

## 確認の限界

この線形モードの減衰を、非線形MHDの全divergenceや大域的な精度の保証とはしません。CTで表せない単極子モードをCTとの同条件比較には用いません。

## 保存実測値と判定

```json
{
  "metrics": {
    "observed_order": 2.001546730427675,
    "continuum_amplitude_ratio": 0.3619556718500278
  },
  "checks": {
    "analytic_expm_comparison": true,
    "spatial_order": true,
    "divergence_damping": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/index.json

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

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# GLM longitudinal mode: analytic damping

Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution.

**Methods used**

- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-algorithm)

Integrate Bx_t=-psi_x and psi_t=-ch² Bx_x-kappa psi with centered differences/RK4. The independent reference exponentiates the continuous 2x2 Fourier symbol.

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![GLM longitudinal mode: analytic damping: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-validation)

Check L2 error, second-order spatial refinement and damping of the divergence-mode amplitude at 16/32/64 points.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Periodic [0,1], Bx=cos2pix, psi=0, ch=1, damping kappa=2, t=1. This linear diagnostic omits fluid coupling.

## Adopted numerical method

Integrate Bx_t=-psi_x and psi_t=-ch² Bx_x-kappa psi with centered differences/RK4. The independent reference exponentiates the continuous 2x2 Fourier symbol.

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

## References and validation

Check L2 error, second-order spatial refinement and damping of the divergence-mode amplitude at 16/32/64 points.

## Limits

Linear-mode damping does not guarantee divergence control or global accuracy for every nonlinear MHD problem. A monopole mode that CT cannot represent is not used as a matched CT comparison.

## Stored measurements and decisions

```json
{
  "metrics": {
    "observed_order": 2.001546730427675,
    "continuum_amplitude_ratio": 0.3619556718500278
  },
  "checks": {
    "analytic_expm_comparison": true,
    "spatial_order": true,
    "divergence_damping": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/index.json

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

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
