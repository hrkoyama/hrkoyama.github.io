# 温かいPICの二流初期成長

温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。

**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) (`cic`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-algorithm)

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

各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。


**問題の図**

![温かいPICの二流初期成長：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) (`thermal-two-stream`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-validation)

31 pytest・19自己無撞着計算・140/140ケース判定・17/17独立線形参照資格判定が合格。pytest+mainは7.283秒。Landau粒子空間層256/512の曲線差.001154、振幅半減差.004376は固定.03以下。以前の64層版130/131（振幅差.05646>.03）は全データと元契約を保持した未達例です。入力の振幅と全許容値は維持しました。

- [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-two-stream-ja) (`thermal-two-stream`; 同じ問題の参照 · 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。
## 前提・単位・境界

各流の熱速度1、ドリフト±3、k=.2、L=10π、α=1e−5、格子32、64空間層×128総速度節点、dt=.05、T40、固定窓[12,20]。シード34001–34004。

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
    "mean_rate": 0.27311134290987144,
    "seed_standard_error": 0.00015934759074193113,
    "conditional_t95_lower": 0.27260422775845883,
    "conditional_t95_upper": 0.27361845806128404,
    "dielectric_rate": 0.2845096862049824,
    "volterra_fixed_window_rate": 0.27367842777159807,
    "root_window_relative_bias": 0.03806991100324323,
    "mean_linear_curve_relative_rms": 0.02389414539434425,
    "three_noise_to_minimum_envelope": 5.21270074929847e-09,
    "mesh_rate_fraction": 0.002014175281809955,
    "time-half_rate_fraction": 0.0017066353745795366,
    "velocity_rate_fraction": 0.0012636985750053421,
    "amplitude-half_rate_fraction": 9.699235024311375e-05,
    "amplitude_scaled_curve_gap": 0.0009509378138530034
  },
  "checks": {
    "independent root and fixed-window Volterra qualified": true,
    "nine fixed full-f calculations": true,
    "thermal-two-stream-seed34001 all fields and histories finite": true,
    "thermal-two-stream-seed34001 fixed time and five snapshots": true,
    "thermal-two-stream-seed34001 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34001 positive full-f weights without repair": true,
    "thermal-two-stream-seed34001 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34001 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34002 all fields and histories finite": true,
    "thermal-two-stream-seed34002 fixed time and five snapshots": true,
    "thermal-two-stream-seed34002 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34002 positive full-f weights without repair": true,
    "thermal-two-stream-seed34002 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34002 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34003 all fields and histories finite": true,
    "thermal-two-stream-seed34003 fixed time and five snapshots": true,
    "thermal-two-stream-seed34003 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34003 positive full-f weights without repair": true,
    "thermal-two-stream-seed34003 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34003 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34004 all fields and histories finite": true,
    "thermal-two-stream-seed34004 fixed time and five snapshots": true,
    "thermal-two-stream-seed34004 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34004 positive full-f weights without repair": true,
    "thermal-two-stream-seed34004 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34004 resolved fixed-window rate fit": true,
    "thermal-two-stream-mesh all fields and histories finite": true,
    "thermal-two-stream-mesh fixed time and five snapshots": true,
    "thermal-two-stream-mesh charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-mesh positive full-f weights without repair": true,
    "thermal-two-stream-mesh joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-mesh resolved fixed-window rate fit": true,
    "thermal-two-stream-time-half all fields and histories finite": true,
    "thermal-two-stream-time-half fixed time and five snapshots": true,
    "thermal-two-stream-time-half charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-time-half positive full-f weights without repair": true,
    "thermal-two-stream-time-half joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-time-half resolved fixed-window rate fit": true,
    "thermal-two-stream-velocity all fields and histories finite": true,
    "thermal-two-stream-velocity fixed time and five snapshots": true,
    "thermal-two-stream-velocity charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-velocity positive full-f weights without repair": true,
    "thermal-two-stream-velocity joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-velocity resolved fixed-window rate fit": true,
    "thermal-two-stream-amplitude-half all fields and histories finite": true,
    "thermal-two-stream-amplitude-half fixed time and five snapshots": true,
    "thermal-two-stream-amplitude-half charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-amplitude-half positive full-f weights without repair": true,
    "thermal-two-stream-amplitude-half joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-amplitude-half resolved fixed-window rate fit": true,
    "thermal-two-stream-noise all fields and histories finite": true,
    "thermal-two-stream-noise fixed time and five snapshots": true,
    "thermal-two-stream-noise charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-noise positive full-f weights without repair": true,
    "thermal-two-stream-noise joint load and Gaussian quadrature qualified": true,
    "conditional rate precision": true,
    "mean rate versus dielectric pole": true,
    "mean rate versus linear IVP fixed-window estimator": true,
    "mean field curve versus linear continuum": true,
    "quiet-equilibrium noise versus fitted envelope": true,
    "mesh separate rate sensitivity": true,
    "time-half separate rate sensitivity": true,
    "velocity separate rate sensitivity": true,
    "amplitude-half separate rate sensitivity": true,
    "amplitude-halving scaled field linearity": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/index.json

![実粒子のT40での速度変化δv/αを初期(x,v)に表示。1D1V位相空間の後期診断で、成長率を検証する固定窓\[12,20\]とは分けます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

実粒子のT40での速度変化δv/αを初期(x,v)に表示。1D1V位相空間の後期診断で、成長率を検証する固定窓[12,20]とは分けます。

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

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme [accessed 2026-11-23]. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
原著の規格化方程式、再帰・雑音、Landauと二流の線形窓の議論を選択して確認。原著の計算値は転用しません。

- PlasmaPy developers (2026). Plasma dispersion function: official API mathematics [accessed 2026-11-23]. https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html; review_level=official-mathematical-definition-read
公式のZ関数の定義を確認。PlasmaPy実行値を参照したものではありません。

- SciPy developers (2024). SciPy1.14.1 roots_hermitenorm [accessed 2026-11-23]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html; review_level=official-pinned-version-definition-read
公式1.14.1文書の重みと多項式積分次数を確認。初期粒子重みだけに用います。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Warm PIC two-stream initial growth

Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.

**Methods used**

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) (`pic`)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) (`cic`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-algorithm)

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

Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.


**Problem figure**

![Warm PIC two-stream initial growth: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) (`thermal-two-stream`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-validation)

31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.

- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en) (`thermal-two-stream`; Same-problem reference · Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
## Assumptions, units and boundaries

Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.

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
    "mean_rate": 0.27311134290987144,
    "seed_standard_error": 0.00015934759074193113,
    "conditional_t95_lower": 0.27260422775845883,
    "conditional_t95_upper": 0.27361845806128404,
    "dielectric_rate": 0.2845096862049824,
    "volterra_fixed_window_rate": 0.27367842777159807,
    "root_window_relative_bias": 0.03806991100324323,
    "mean_linear_curve_relative_rms": 0.02389414539434425,
    "three_noise_to_minimum_envelope": 5.21270074929847e-09,
    "mesh_rate_fraction": 0.002014175281809955,
    "time-half_rate_fraction": 0.0017066353745795366,
    "velocity_rate_fraction": 0.0012636985750053421,
    "amplitude-half_rate_fraction": 9.699235024311375e-05,
    "amplitude_scaled_curve_gap": 0.0009509378138530034
  },
  "checks": {
    "independent root and fixed-window Volterra qualified": true,
    "nine fixed full-f calculations": true,
    "thermal-two-stream-seed34001 all fields and histories finite": true,
    "thermal-two-stream-seed34001 fixed time and five snapshots": true,
    "thermal-two-stream-seed34001 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34001 positive full-f weights without repair": true,
    "thermal-two-stream-seed34001 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34001 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34002 all fields and histories finite": true,
    "thermal-two-stream-seed34002 fixed time and five snapshots": true,
    "thermal-two-stream-seed34002 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34002 positive full-f weights without repair": true,
    "thermal-two-stream-seed34002 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34002 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34003 all fields and histories finite": true,
    "thermal-two-stream-seed34003 fixed time and five snapshots": true,
    "thermal-two-stream-seed34003 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34003 positive full-f weights without repair": true,
    "thermal-two-stream-seed34003 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34003 resolved fixed-window rate fit": true,
    "thermal-two-stream-seed34004 all fields and histories finite": true,
    "thermal-two-stream-seed34004 fixed time and five snapshots": true,
    "thermal-two-stream-seed34004 charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-seed34004 positive full-f weights without repair": true,
    "thermal-two-stream-seed34004 joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-seed34004 resolved fixed-window rate fit": true,
    "thermal-two-stream-mesh all fields and histories finite": true,
    "thermal-two-stream-mesh fixed time and five snapshots": true,
    "thermal-two-stream-mesh charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-mesh positive full-f weights without repair": true,
    "thermal-two-stream-mesh joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-mesh resolved fixed-window rate fit": true,
    "thermal-two-stream-time-half all fields and histories finite": true,
    "thermal-two-stream-time-half fixed time and five snapshots": true,
    "thermal-two-stream-time-half charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-time-half positive full-f weights without repair": true,
    "thermal-two-stream-time-half joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-time-half resolved fixed-window rate fit": true,
    "thermal-two-stream-velocity all fields and histories finite": true,
    "thermal-two-stream-velocity fixed time and five snapshots": true,
    "thermal-two-stream-velocity charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-velocity positive full-f weights without repair": true,
    "thermal-two-stream-velocity joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-velocity resolved fixed-window rate fit": true,
    "thermal-two-stream-amplitude-half all fields and histories finite": true,
    "thermal-two-stream-amplitude-half fixed time and five snapshots": true,
    "thermal-two-stream-amplitude-half charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-amplitude-half positive full-f weights without repair": true,
    "thermal-two-stream-amplitude-half joint load and Gaussian quadrature qualified": true,
    "thermal-two-stream-amplitude-half resolved fixed-window rate fit": true,
    "thermal-two-stream-noise all fields and histories finite": true,
    "thermal-two-stream-noise fixed time and five snapshots": true,
    "thermal-two-stream-noise charge momentum resolvedGauss and energy": true,
    "thermal-two-stream-noise positive full-f weights without repair": true,
    "thermal-two-stream-noise joint load and Gaussian quadrature qualified": true,
    "conditional rate precision": true,
    "mean rate versus dielectric pole": true,
    "mean rate versus linear IVP fixed-window estimator": true,
    "mean field curve versus linear continuum": true,
    "quiet-equilibrium noise versus fitted envelope": true,
    "mesh separate rate sensitivity": true,
    "time-half separate rate sensitivity": true,
    "velocity separate rate sensitivity": true,
    "amplitude-half separate rate sensitivity": true,
    "amplitude-halving scaled field linearity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/index.json

![Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over\[12,20\].](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over[12,20].

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

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme [accessed 2026-11-23]. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
Selected original equations and diagnostic limitations inspected; independently derived continuum references are evaluated here.

- PlasmaPy developers (2026). Plasma dispersion function: official API mathematics [accessed 2026-11-23]. https://docs.plasmapy.org/en/stable/api/plasmapy.dispersion.dispersion_functions.plasma_dispersion_func.html; review_level=official-mathematical-definition-read
Official Z definition inspected; no PlasmaPy execution.

- SciPy developers (2024). SciPy1.14.1 roots_hermitenorm [accessed 2026-11-23]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.special.roots_hermitenorm.html; review_level=official-pinned-version-definition-read
Pinned official quadrature definition read; initialization only.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
