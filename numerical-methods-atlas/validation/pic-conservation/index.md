# PIC：格子・時間収束、保存量と粒子雑音

冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja#pic-conservation-ja-algorithm)

CIC割当て・同じ重みの場補間・スペクトルPoisson・速度Verlet。独立な時間積分法DOP853は同じ粒子格子RHSを積分し、参照自身の最大刻み感度を検査します。

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![PIC：格子・時間収束、保存量と粒子雑音：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja#pic-conservation-ja-validation)

16/32/64格子とdt=.2/.1/.05を別に精密化し、線形cos(t)と時間参照の誤差を分離します。実数奇微分のNyquist零モードはGauss残差から分けて記録。時刻0の64seed・N=256/1024/4096のCICモード電力を解析期待値と比較します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

長さ2pi、静止イオン密度1、電子q/m=−1、plasma frequency=1、微小正弦変位0.001、最終時刻1.6。格子系列は同じ2048粒子を使い、時間系列は同じ32格子・256粒子を使います。 w=2pi/Nは粒子重み、nは格子数です。

**編集上の補足**

DOP853参照は同じ粒子格子RHSを積分し、時間積分に限る独立参照です。quiet startの収束と時刻0のランダム粒子雑音を分け、エネルギーの厳密保存は主張しません。

## 採用した計算法

CIC割当て・同じ重みの場補間・スペクトルPoisson・速度Verlet。独立な時間積分法DOP853は同じ粒子格子RHSを積分し、参照自身の最大刻み感度を検査します。

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

## 比較・検証

16/32/64格子とdt=.2/.1/.05を別に精密化し、線形cos(t)と時間参照の誤差を分離します。実数奇微分のNyquist零モードはGauss残差から分けて記録。時刻0の64seed・N=256/1024/4096のCICモード電力を解析期待値と比較します。

## 確認の限界

DOP853は独立PIC空間実装ではありません。電荷・運動量の保持とエネルギーの近似保存を区別し、初期雑音のNスケーリングを時間発展した熱プラズマの保証としません。Landau減衰・電磁PIC・相対論・衝突は未検証です。

## 保存実測値と判定

```json
{
  "metrics": {
    "finest_mesh_mode_error": 0.0012829885842868122,
    "minimum_mesh_error_ratio": 3.982691594959013,
    "minimum_time_order": 2.0012021519229015,
    "finest_time_mode_error": 0.0001650650068896753,
    "reference_sensitivity": 6.217248937900877e-12,
    "charge_error": 7.847704120519421e-16,
    "momentum_error": 6.812243160173109e-19,
    "resolved_gauss_error": 2.58493941422823e-26,
    "nyquist_charge": 2.725250580759564e-15,
    "relative_energy_drift": 0.00997018843320538,
    "minimum_shot_scaled_power": 0.9441284361820317,
    "maximum_shot_scaled_power": 1.3013624563118524,
    "minimum_shot_rms_reduction": 1.7035241144134314
  },
  "checks": {
    "continuum_reference": true,
    "mesh_convergence": true,
    "time_convergence": true,
    "independent_time_reference": true,
    "charge": true,
    "momentum": true,
    "resolved_gauss": true,
    "nyquist_charge": true,
    "measured_energy_drift": true,
    "shot_noise_power": true,
    "shot_noise_scaling": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## 出典と確認範囲

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
  出版社配布プレビューの書誌・粒子モデルの導入と目次を確認。CICや冷たいプラズマの歴史的出典とし、全書の監査は主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# PIC: mesh/time convergence, invariants and particle noise

Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-algorithm)

CIC deposition/matched gathering, spectral Poisson and velocity Verlet. The independent time algorithm DOP853 integrates the same particle-grid RHS; compare its own maximum-step refinements.

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![PIC: mesh/time convergence, invariants and particle noise: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en#pic-conservation-en-validation)

Refine 16/32/64 grids and dt=.2/.1/.05 separately; distinguish continuum cos(t) from time-reference errors. Record the real odd derivative’s Nyquist null mode separately from Gauss residuals. Compare time-zero CIC mode power at 64 seeds and N=256/1024/4096 with its analytic expectation.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Length 2pi, stationary unit-density ions, electron q/m=−1, plasma frequency one, sinusoidal displacement 0.001 and final time 1.6. Mesh runs retain 2048 particles; time runs retain a 32-cell mesh and 256 particles. The particle weight is w=2pi/N and n is the grid count.

**Editorial clarification**

DOP853 integrates the same particle-grid RHS and is independent only as a time algorithm. Separate quiet-start refinement from random-load noise at time zero; do not claim exact energy conservation.

## Adopted numerical method

CIC deposition/matched gathering, spectral Poisson and velocity Verlet. The independent time algorithm DOP853 integrates the same particle-grid RHS; compare its own maximum-step refinements.

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

## References and validation

Refine 16/32/64 grids and dt=.2/.1/.05 separately; distinguish continuum cos(t) from time-reference errors. Record the real odd derivative’s Nyquist null mode separately from Gauss residuals. Compare time-zero CIC mode power at 64 seeds and N=256/1024/4096 with its analytic expectation.

## Limits

DOP853 is not an independent PIC spatial implementation. Distinguish charge/momentum preservation from approximate energy conservation. Initial-noise N scaling does not validate evolved warm plasmas. Landau damping, electromagnetic/relativistic PIC and collisions remain unvalidated.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest_mesh_mode_error": 0.0012829885842868122,
    "minimum_mesh_error_ratio": 3.982691594959013,
    "minimum_time_order": 2.0012021519229015,
    "finest_time_mode_error": 0.0001650650068896753,
    "reference_sensitivity": 6.217248937900877e-12,
    "charge_error": 7.847704120519421e-16,
    "momentum_error": 6.812243160173109e-19,
    "resolved_gauss_error": 2.58493941422823e-26,
    "nyquist_charge": 2.725250580759564e-15,
    "relative_energy_drift": 0.00997018843320538,
    "minimum_shot_scaled_power": 0.9441284361820317,
    "maximum_shot_scaled_power": 1.3013624563118524,
    "minimum_shot_rms_reduction": 1.7035241144134314
  },
  "checks": {
    "continuum_reference": true,
    "mesh_convergence": true,
    "time_convergence": true,
    "independent_time_reference": true,
    "charge": true,
    "momentum": true,
    "resolved_gauss": true,
    "nyquist_charge": true,
    "measured_energy_drift": true,
    "shot_noise_power": true,
    "shot_noise_scaling": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## Sources and review scope

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
  Publisher preview bibliography, introduction and contents checked; historical source for CIC/cold plasma, not a full-book audit.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
