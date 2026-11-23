# DSMC衝突成分：有限N平衡・保存則・統計誤差

有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja#dsmc-statistics-ja-algorithm)

ランダムな完全対合と球面一様の散乱で、各対の運動量・エネルギーを保持します。別の標本生成ではGaussianを重心ゼロ部分空間へ射影し、半径を固定します。

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![DSMC衝突成分：有限N平衡・保存則・統計誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja) (`maxwell-collisions`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja#dsmc-statistics-ja-validation)

全roundの運動量・エネルギーの最大保存誤差は決定論的な許容値で検査します。最初の6roundの異方性、4点のエネルギーCDF、4次モーメントと有限NのBeta参照との差は、独立seed間の標準誤差で測ります。NによるCDF標準誤差の減少と、有限NからMaxwellへの偏りを分けます。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

等質・等質量・等方散乱のMaxwell分子、N=16/64/256、独立64seed、運動量0、sum|v|²=3N。二つのビームから24round衝突させ、roundは物理時間へ換算しません。

**編集上の補足**

保存量を固定した有限N平衡のBeta分布と独立な球面標本を使います。粒子間相関があるので独立seed間の誤差を測り、衝突roundを物理時刻や剛体球輸送へ読み替えません。

## 採用した計算法

ランダムな完全対合と球面一様の散乱で、各対の運動量・エネルギーを保持します。別の標本生成ではGaussianを重心ゼロ部分空間へ射影し、半径を固定します。

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

## 比較・検証

全roundの運動量・エネルギーの最大保存誤差は決定論的な許容値で検査します。最初の6roundの異方性、4点のエネルギーCDF、4次モーメントと有限NのBeta参照との差は、独立seed間の標準誤差で測ります。NによるCDF標準誤差の減少と、有限NからMaxwellへの偏りを分けます。

## 確認の限界

固定した64seedの統計的診断であり、全seedの保証ではありません。同一seed内の粒子は保存量で相関し、IIDのKS p値へ読み替えません。空間輸送、衝突セル、剛体球の速度依存衝突選択・輸送係数は含みません。

## 保存実測値と判定

```json
{
  "metrics": {
    "momentum_error": 2.983724378680108e-16,
    "relative_energy_error": 7.401486830834378e-16,
    "anisotropy_standard_errors": 1.6562460503431053,
    "cdf_standard_errors": 2.244491479985008,
    "independent_equilibrium_standard_errors": 1.7114389804398267,
    "fourth_standard_errors": 1.4292752287239299,
    "maximum_finite_n_maxwell_cdf_bias": 0.01377529224707158,
    "cdf_seed_standard_error_reduction": 3.996517498915623
  },
  "checks": {
    "momentum": true,
    "energy": true,
    "analytic_anisotropy": true,
    "exact_finite_n_cdf": true,
    "independent_equilibrium": true,
    "finite_n_fourth_moment": true,
    "finite_n_distinct_from_maxwell": true,
    "statistical_error_scaling": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/index.json

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

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## 出典と確認範囲

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
Sandiaの公式DSMC記念文書とDOI書誌を確認。出版社本文は取得できず、原著の剛体球モデルを再現したとは主張しません。

- E. Scalas, A. T. Gabriel, E. Martin and G. Germano (2015). Velocity and energy distributions in microcanonical ensembles of hard spheres. https://arxiv.org/abs/1207.3505; review_level=primary-abstract-and-selected-theory; separate center-of-mass sphere derivation
初期設計は原著抄録を確認し、その後の追加レビューで有限系分布の理論の一部を参照。ここでの運動量0の球面・周辺Beta則は明示的に導出し、原著の分子動力学データを再利用したとはしません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# DSMC collision component: finite-N equilibrium, invariants and statistical error

Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-algorithm)

Uniform random complete matchings and isotropic pair scattering preserve pair momentum/energy. An independent sampler projects Gaussian vectors into the zero-center-of-mass subspace and fixes their radius.

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![DSMC collision component: finite-N equilibrium, invariants and statistical error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) (`maxwell-collisions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en#dsmc-statistics-en-validation)

Check maximum momentum/energy errors over all rounds against deterministic tolerances. Use independent-seed standard errors for six-round anisotropy, four energy-CDF points and fourth moments against the finite-N beta reference. Separate decreasing CDF sampling error with N from finite-N Maxwell bias.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Homogeneous equal-mass isotropic Maxwell collisions; N=16/64/256, 64 independent seeds, zero momentum and sum|v|²=3N. Start with two beams and run 24 collision rounds; rounds are not calibrated physical time.

**Editorial clarification**

Use the finite-N equilibrium beta law and independent sphere samples at fixed invariants. Account for particle correlation via independent-seed error; collision rounds are not calibrated time or hard-sphere transport.

## Adopted numerical method

Uniform random complete matchings and isotropic pair scattering preserve pair momentum/energy. An independent sampler projects Gaussian vectors into the zero-center-of-mass subspace and fixes their radius.

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

## References and validation

Check maximum momentum/energy errors over all rounds against deterministic tolerances. Use independent-seed standard errors for six-round anisotropy, four energy-CDF points and fourth moments against the finite-N beta reference. Separate decreasing CDF sampling error with N from finite-N Maxwell bias.

## Limits

Statistical diagnostics cover fixed 64-seed ensembles, not every seed. Conservation correlates particles within a seed; do not use IID KS p-values. No spatial streaming, collision cells, speed-dependent hard-sphere selection or transport coefficients.

## Stored measurements and decisions

```json
{
  "metrics": {
    "momentum_error": 2.983724378680108e-16,
    "relative_energy_error": 7.401486830834378e-16,
    "anisotropy_standard_errors": 1.6562460503431053,
    "cdf_standard_errors": 2.244491479985008,
    "independent_equilibrium_standard_errors": 1.7114389804398267,
    "fourth_standard_errors": 1.4292752287239299,
    "maximum_finite_n_maxwell_cdf_bias": 0.01377529224707158,
    "cdf_seed_standard_error_reduction": 3.996517498915623
  },
  "checks": {
    "momentum": true,
    "energy": true,
    "analytic_anisotropy": true,
    "exact_finite_n_cdf": true,
    "independent_equilibrium": true,
    "finite_n_fourth_moment": true,
    "finite_n_distinct_from_maxwell": true,
    "statistical_error_scaling": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/index.json

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

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## Sources and review scope

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
Official Sandia DSMC commemorative document and DOI metadata checked; publisher text unavailable and the original hard-sphere model is not claimed as reproduced.

- E. Scalas, A. T. Gabriel, E. Martin and G. Germano (2015). Velocity and energy distributions in microcanonical ensembles of hard spheres. https://arxiv.org/abs/1207.3505; review_level=primary-abstract-and-selected-theory; separate center-of-mass sphere derivation
Initial design reviewed the abstract; subsequent additional review consulted selected finite-system theory. Explicitly derive the zero-momentum sphere marginal here; no original molecular-dynamics data are reused.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
