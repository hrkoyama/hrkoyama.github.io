# Langevin温度制御：正準分布・刻み偏り・時間相関

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

**使用手法**

- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-algorithm)

力B・ドリフトAの半ステップと厳密OUノイズ更新OをB-A-O-A-Bで合成。サンプルの共分散・3種のCDF・エネルギー平均/分散・位置相関を記録します。

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Langevin温度制御：正準分布・刻み偏り・時間相関：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-validation)

SciPy離散Lyapunov解および調和系の明示共分散diag(T/omega²,T(1-h²omega²/4))で照合。運動量の刻み2次偏りと有限標本誤差を分離し、burn過渡を写像で評価。連続相関は別の行列指数で算出します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

質量・Boltzmann定数・角振動数・摩擦・温度は1。独立32768複製、burn時間20、刻み0.4/0.2/0.1、相関lag時間2。h*omega<2を要求します。

## 採用した計算法

力B・ドリフトAの半ステップと厳密OUノイズ更新OをB-A-O-A-Bで合成。サンプルの共分散・3種のCDF・エネルギー平均/分散・位置相関を記録します。

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

## 比較・検証

SciPy離散Lyapunov解および調和系の明示共分散diag(T/omega²,T(1-h²omega²/4))で照合。運動量の刻み2次偏りと有限標本誤差を分離し、burn過渡を写像で評価。連続相関は別の行列指数で算出します。

## 確認の限界

調和ポテンシャル・固定seedの分布検証です。位置分散が正確でも運動量には有限刻み偏りがあります。他のサーモスタット、一般分子系、長時間の第一原理MDへ検証を移しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_covariance_sampling_error": 0.010793938239005096,
    "maximum_correlation_sampling_error": 0.007859497657203701,
    "maximum_lyapunov_residual": 1.1102230246251565e-16,
    "maximum_burn_transient_covariance_error": 3.9116795872649285e-09,
    "minimum_covariance_bias_order": 1.9999999999999882,
    "finest_covariance_bias": 0.0024999999999999467,
    "energy_cdf_error": 0.004375986814703525,
    "position_cdf_error": 0.005928788756380088,
    "momentum_cdf_error": 0.0068938107115509295,
    "energy_mean_error": 0.009281722112660762,
    "energy_variance_error": 0.03054847700744423
  },
  "checks": {
    "finite": true,
    "stationary_reference": true,
    "burn_transient": true,
    "covariance_sampling": true,
    "correlation_sampling": true,
    "bias_refinement": true,
    "finest_bias": true,
    "canonical_energy_cdf": true,
    "canonical_position_cdf": true,
    "canonical_momentum_cdf": true,
    "canonical_energy_mean": true,
    "canonical_energy_variance": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- B. Leimkuhler and C. Matthews (2013). Rational Construction of Stochastic Numerical Methods for Molecular Sampling. https://arxiv.org/abs/1203.5428; review_level=author-manuscript-selected-appendix
  著者稿の抄録、Langevin式、付録のBAOAB更新式（印刷22ページ）を確認。一般分子の超収束や原著の長時間計算を再現したとは主張しません。
- The SciPy community (2024). SciPy1.14.1 solve_discrete_lyapunov reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.solve_discrete_lyapunov.html; review_level=official-api-documentation
  公式の離散Lyapunov方程式AXA^H-X+Q=0の符号と返却仕様を確認。
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  公式の行列指数APIとPadé/scaling-and-squaring法の記載を確認。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Langevin thermostat: canonical distributions, timestep bias and correlation

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

**Methods used**

- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en#langevin-harmonic-en-algorithm)

Compose force B and drift A half steps with exact OU noise O in B-A-O-A-B order. Record covariance, three CDFs, energy mean/variance and position correlation.

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Langevin thermostat: canonical distributions, timestep bias and correlation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en#langevin-harmonic-en-validation)

Check against a SciPy discrete-Lyapunov solve and explicit harmonic covariance diag(T/omega²,T(1-h²omega²/4)). Separate second-order momentum bias from sampling error and evaluate burn transients from the map. A separate matrix exponential gives continuous correlation.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Mass, Boltzmann constant, frequency, friction and temperature are one. Use 32768 replicas, burn time 20, steps 0.4/0.2/0.1 and correlation lag 2; require h*omega<2.

## Adopted numerical method

Compose force B and drift A half steps with exact OU noise O in B-A-O-A-B order. Record covariance, three CDFs, energy mean/variance and position correlation.

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

## References and validation

Check against a SciPy discrete-Lyapunov solve and explicit harmonic covariance diag(T/omega²,T(1-h²omega²/4)). Separate second-order momentum bias from sampling error and evaluate burn transients from the map. A separate matrix exponential gives continuous correlation.

## Limits

Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_covariance_sampling_error": 0.010793938239005096,
    "maximum_correlation_sampling_error": 0.007859497657203701,
    "maximum_lyapunov_residual": 1.1102230246251565e-16,
    "maximum_burn_transient_covariance_error": 3.9116795872649285e-09,
    "minimum_covariance_bias_order": 1.9999999999999882,
    "finest_covariance_bias": 0.0024999999999999467,
    "energy_cdf_error": 0.004375986814703525,
    "position_cdf_error": 0.005928788756380088,
    "momentum_cdf_error": 0.0068938107115509295,
    "energy_mean_error": 0.009281722112660762,
    "energy_variance_error": 0.03054847700744423
  },
  "checks": {
    "finite": true,
    "stationary_reference": true,
    "burn_transient": true,
    "covariance_sampling": true,
    "correlation_sampling": true,
    "bias_refinement": true,
    "finest_bias": true,
    "canonical_energy_cdf": true,
    "canonical_position_cdf": true,
    "canonical_momentum_cdf": true,
    "canonical_energy_mean": true,
    "canonical_energy_variance": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- B. Leimkuhler and C. Matthews (2013). Rational Construction of Stochastic Numerical Methods for Molecular Sampling. https://arxiv.org/abs/1203.5428; review_level=author-manuscript-selected-appendix
  Author manuscript abstract, Langevin equation and BAOAB update in the appendix (printed page 22) checked. The original long molecular runs and general-system superconvergence are not reproduced here.
- The SciPy community (2024). SciPy1.14.1 solve_discrete_lyapunov reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.solve_discrete_lyapunov.html; review_level=official-api-documentation
  Official equation AXA^H-X+Q=0, signs and output specification checked.
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  Official matrix-exponential API and description of the Pade/scaling-and-squaring method checked.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
