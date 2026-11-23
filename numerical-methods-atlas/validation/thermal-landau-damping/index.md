# 温かいPICの線形Landau減衰

熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。

**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) (`cic`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-algorithm)

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja) (`vlasov-poisson`)

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。


**問題の図**

![温かいPICの線形Landau減衰：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-validation)

31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。

- [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-landau-damping-ja) (`thermal-landau-damping`; 同じ問題の参照 · 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
## 前提・単位・境界

vth=ωp=λD=1、k=.5、L=4π、α=.01、格子32、256空間層×128速度節点、dt=.04、T16、固定窓[4,12]。シード33001–33004。 空間粒子層だけ512へ倍増する独立companionも固定します。

**編集上の補足**

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

## 採用した計算法

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

## 比較・検証

31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。

## 確認の限界

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "mean_rate": -0.15488075370071888,
    "seed_standard_error": 1.4514731389084198e-05,
    "conditional_t95_lower": -0.15492694605400026,
    "conditional_t95_upper": -0.1548345613474375,
    "dielectric_rate": -0.15335946690960467,
    "volterra_fixed_window_rate": -0.1536475740216858,
    "root_window_relative_bias": 0.0018786392381694443,
    "mean_linear_curve_relative_rms": 0.02092398393973105,
    "three_noise_to_minimum_envelope": 5.222378053852797e-12,
    "mesh_rate_fraction": 0.005387063405092717,
    "time-half_rate_fraction": 9.14827746356337e-05,
    "velocity_rate_fraction": 0.0001972171817183033,
    "amplitude-half_rate_fraction": 0.0009187020274627366,
    "amplitude_scaled_curve_gap": 0.004375529905721923,
    "mean_frequency": 1.4127212133462208,
    "frequency_seed_se": 3.853831828103487e-05,
    "dielectric_frequency": 1.4156618886045371,
    "spatial_strata_rate_fraction": 6.62744989007398e-05,
    "spatial_strata_scaled_curve_gap": 0.001153705277393216
  },
  "checks": {
    "independent root and fixed-window Volterra qualified": true,
    "nine fixed full-f calculations": true,
    "ten declared Landau full-f calculations": true,
    "thermal-landau-damping-seed33001 all fields and histories finite": true,
    "thermal-landau-damping-seed33001 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33001 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33001 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33001 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33001 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33002 all fields and histories finite": true,
    "thermal-landau-damping-seed33002 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33002 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33002 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33002 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33002 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33003 all fields and histories finite": true,
    "thermal-landau-damping-seed33003 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33003 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33003 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33003 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33003 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33004 all fields and histories finite": true,
    "thermal-landau-damping-seed33004 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33004 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33004 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33004 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33004 resolved fixed-window rate fit": true,
    "thermal-landau-damping-mesh all fields and histories finite": true,
    "thermal-landau-damping-mesh fixed time and five snapshots": true,
    "thermal-landau-damping-mesh charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-mesh positive full-f weights without repair": true,
    "thermal-landau-damping-mesh joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-mesh resolved fixed-window rate fit": true,
    "thermal-landau-damping-time-half all fields and histories finite": true,
    "thermal-landau-damping-time-half fixed time and five snapshots": true,
    "thermal-landau-damping-time-half charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-time-half positive full-f weights without repair": true,
    "thermal-landau-damping-time-half joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-time-half resolved fixed-window rate fit": true,
    "thermal-landau-damping-velocity all fields and histories finite": true,
    "thermal-landau-damping-velocity fixed time and five snapshots": true,
    "thermal-landau-damping-velocity charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-velocity positive full-f weights without repair": true,
    "thermal-landau-damping-velocity joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-velocity resolved fixed-window rate fit": true,
    "thermal-landau-damping-amplitude-half all fields and histories finite": true,
    "thermal-landau-damping-amplitude-half fixed time and five snapshots": true,
    "thermal-landau-damping-amplitude-half charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-amplitude-half positive full-f weights without repair": true,
    "thermal-landau-damping-amplitude-half joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-amplitude-half resolved fixed-window rate fit": true,
    "thermal-landau-damping-noise all fields and histories finite": true,
    "thermal-landau-damping-noise fixed time and five snapshots": true,
    "thermal-landau-damping-noise charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-noise positive full-f weights without repair": true,
    "thermal-landau-damping-noise joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-spatial-strata all fields and histories finite": true,
    "thermal-landau-damping-spatial-strata fixed time and five snapshots": true,
    "thermal-landau-damping-spatial-strata charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-spatial-strata positive full-f weights without repair": true,
    "thermal-landau-damping-spatial-strata joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-spatial-strata resolved fixed-window rate fit": true,
    "conditional rate precision": true,
    "mean rate versus dielectric pole": true,
    "mean rate versus linear IVP fixed-window estimator": true,
    "mean field curve versus linear continuum": true,
    "quiet-equilibrium noise versus fitted envelope": true,
    "mesh separate rate sensitivity": true,
    "time-half separate rate sensitivity": true,
    "velocity separate rate sensitivity": true,
    "amplitude-half separate rate sensitivity": true,
    "amplitude-halving scaled field linearity": true,
    "mean frequency versus dielectric pole": true,
    "spatial-strata separate rate sensitivity": true,
    "spatial-strata scaled field sensitivity": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/index.json

![実際に動かした粒子の初期(x,v)に対する速度変化δv/α。空間2D流体図ではなく1D1V位相空間の応答です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

実際に動かした粒子の初期(x,v)に対する速度変化δv/α。空間2D流体図ではなく1D1V位相空間の応答です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
原著の規格化方程式、再帰・雑音、Landauと二流の線形窓の議論を選択して確認。原著の計算値は転用しません。

- PlasmaPy developers (2026). Plasma dispersion function: official API mathematics. https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html; review_level=official-mathematical-definition-read
公式のZ関数の定義を確認。PlasmaPy実行値を参照したものではありません。

- SciPy developers (2024). SciPy1.14.1 roots_hermitenorm. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html; review_level=official-pinned-version-definition-read
公式1.14.1文書の重みと多項式積分次数を確認。初期粒子重みだけに用います。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Warm PIC linear Landau damping

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-algorithm)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`)

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.


**Problem figure**

![Warm PIC linear Landau damping: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) (`thermal-landau-damping`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-validation)

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en) (`thermal-landau-damping`; Same-problem reference · Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
## Assumptions, units and boundaries

vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.

**Editorial clarification**

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

## Adopted numerical method

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

$$
\partial_t f+v\partial_x f-E\partial_v f=0,\quad\partial_x E=1-\int f\,dv,\quad\langle E\rangle=0
$$

$$
D(\omega,k)=1+\frac{1}{k^2}\sum_s a_s[1+\zeta_s Z(\zeta_s)],\quad\zeta_s=\frac{\omega-ku_s}{\sqrt2 k}
$$

$$
e(t)=\Phi(t)-\int_0^t s\Phi(s)e(t-s)\,ds,\quad\Phi(t)=e^{-k^2t^2/2}\cos(kut)
$$

## References and validation

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

## Limits

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

## Stored measurements and decisions

```json
{
  "metrics": {
    "mean_rate": -0.15488075370071888,
    "seed_standard_error": 1.4514731389084198e-05,
    "conditional_t95_lower": -0.15492694605400026,
    "conditional_t95_upper": -0.1548345613474375,
    "dielectric_rate": -0.15335946690960467,
    "volterra_fixed_window_rate": -0.1536475740216858,
    "root_window_relative_bias": 0.0018786392381694443,
    "mean_linear_curve_relative_rms": 0.02092398393973105,
    "three_noise_to_minimum_envelope": 5.222378053852797e-12,
    "mesh_rate_fraction": 0.005387063405092717,
    "time-half_rate_fraction": 9.14827746356337e-05,
    "velocity_rate_fraction": 0.0001972171817183033,
    "amplitude-half_rate_fraction": 0.0009187020274627366,
    "amplitude_scaled_curve_gap": 0.004375529905721923,
    "mean_frequency": 1.4127212133462208,
    "frequency_seed_se": 3.853831828103487e-05,
    "dielectric_frequency": 1.4156618886045371,
    "spatial_strata_rate_fraction": 6.62744989007398e-05,
    "spatial_strata_scaled_curve_gap": 0.001153705277393216
  },
  "checks": {
    "independent root and fixed-window Volterra qualified": true,
    "nine fixed full-f calculations": true,
    "ten declared Landau full-f calculations": true,
    "thermal-landau-damping-seed33001 all fields and histories finite": true,
    "thermal-landau-damping-seed33001 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33001 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33001 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33001 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33001 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33002 all fields and histories finite": true,
    "thermal-landau-damping-seed33002 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33002 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33002 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33002 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33002 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33003 all fields and histories finite": true,
    "thermal-landau-damping-seed33003 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33003 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33003 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33003 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33003 resolved fixed-window rate fit": true,
    "thermal-landau-damping-seed33004 all fields and histories finite": true,
    "thermal-landau-damping-seed33004 fixed time and five snapshots": true,
    "thermal-landau-damping-seed33004 charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-seed33004 positive full-f weights without repair": true,
    "thermal-landau-damping-seed33004 joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-seed33004 resolved fixed-window rate fit": true,
    "thermal-landau-damping-mesh all fields and histories finite": true,
    "thermal-landau-damping-mesh fixed time and five snapshots": true,
    "thermal-landau-damping-mesh charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-mesh positive full-f weights without repair": true,
    "thermal-landau-damping-mesh joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-mesh resolved fixed-window rate fit": true,
    "thermal-landau-damping-time-half all fields and histories finite": true,
    "thermal-landau-damping-time-half fixed time and five snapshots": true,
    "thermal-landau-damping-time-half charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-time-half positive full-f weights without repair": true,
    "thermal-landau-damping-time-half joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-time-half resolved fixed-window rate fit": true,
    "thermal-landau-damping-velocity all fields and histories finite": true,
    "thermal-landau-damping-velocity fixed time and five snapshots": true,
    "thermal-landau-damping-velocity charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-velocity positive full-f weights without repair": true,
    "thermal-landau-damping-velocity joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-velocity resolved fixed-window rate fit": true,
    "thermal-landau-damping-amplitude-half all fields and histories finite": true,
    "thermal-landau-damping-amplitude-half fixed time and five snapshots": true,
    "thermal-landau-damping-amplitude-half charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-amplitude-half positive full-f weights without repair": true,
    "thermal-landau-damping-amplitude-half joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-amplitude-half resolved fixed-window rate fit": true,
    "thermal-landau-damping-noise all fields and histories finite": true,
    "thermal-landau-damping-noise fixed time and five snapshots": true,
    "thermal-landau-damping-noise charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-noise positive full-f weights without repair": true,
    "thermal-landau-damping-noise joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-spatial-strata all fields and histories finite": true,
    "thermal-landau-damping-spatial-strata fixed time and five snapshots": true,
    "thermal-landau-damping-spatial-strata charge momentum resolvedGauss and energy": true,
    "thermal-landau-damping-spatial-strata positive full-f weights without repair": true,
    "thermal-landau-damping-spatial-strata joint load and Gaussian quadrature qualified": true,
    "thermal-landau-damping-spatial-strata resolved fixed-window rate fit": true,
    "conditional rate precision": true,
    "mean rate versus dielectric pole": true,
    "mean rate versus linear IVP fixed-window estimator": true,
    "mean field curve versus linear continuum": true,
    "quiet-equilibrium noise versus fitted envelope": true,
    "mesh separate rate sensitivity": true,
    "time-half separate rate sensitivity": true,
    "velocity separate rate sensitivity": true,
    "amplitude-half separate rate sensitivity": true,
    "amplitude-halving scaled field linearity": true,
    "mean frequency versus dielectric pole": true,
    "spatial-strata separate rate sensitivity": true,
    "spatial-strata scaled field sensitivity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/index.json

![Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
Selected original equations and diagnostic limitations inspected; independently derived continuum references are evaluated here.

- PlasmaPy developers (2026). Plasma dispersion function: official API mathematics. https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html; review_level=official-mathematical-definition-read
Official Z definition inspected; no PlasmaPy execution.

- SciPy developers (2024). SciPy1.14.1 roots_hermitenorm. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html; review_level=official-pinned-version-definition-read
Pinned official quadrature definition read; initialization only.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
