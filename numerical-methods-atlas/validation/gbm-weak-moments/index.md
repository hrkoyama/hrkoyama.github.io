# GBMのweak誤差とMonte Carlo標準誤差

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

**使用手法**

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) (`sde`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-algorithm)

fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。


**問題の図**

![GBMのweak誤差とMonte Carlo標準誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-validation)

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja) (`gbm-weak-moments`; 関連モデルの参照 · 解析参照)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja) (`gbm-milstein-strong`; 関連モデルの参照 · 解析参照)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
## 前提・単位・境界

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

**編集上の補足**

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

## 採用した計算法

fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

## 比較・検証

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

## 確認の限界

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "observables": [
      {
        "observable_power": 1,
        "sampled_paired_order": 0.9956027089190806,
        "analytic_order": 0.986850922673782,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": -0.024551175738827653,
            "paired_mean": -0.02390546859088743,
            "paired_MCSE": 0.000431509288625275,
            "analytic_expected_MCSE": 0.0004902247814460831,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 16,
            "analytic_bias": -0.012570260133504842,
            "paired_mean": -0.012073199459893005,
            "paired_MCSE": 0.0002494235153701287,
            "analytic_expected_MCSE": 0.0003179426227319547,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 32,
            "analytic_bias": -0.006361702102222466,
            "paired_mean": -0.006046178211109456,
            "paired_MCSE": 0.00014930108420397513,
            "analytic_expected_MCSE": 0.00021219706970143816,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 64,
            "analytic_bias": -0.0032003745435279854,
            "paired_mean": -0.0030367554342063926,
            "paired_MCSE": 0.0001452128976770314,
            "analytic_expected_MCSE": 0.0001450153280978437,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      },
      {
        "observable_power": 2,
        "sampled_paired_order": 0.9744925206389199,
        "analytic_order": 0.9752562657019691,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": -0.15410825623347305,
            "paired_mean": -0.14906616356143917,
            "paired_MCSE": 0.003147990583178188,
            "analytic_expected_MCSE": 0.003291189368314816,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 16,
            "analytic_bias": -0.08050123855537453,
            "paired_mean": -0.07770877547600556,
            "paired_MCSE": 0.0018030716808605054,
            "analytic_expected_MCSE": 0.001999254398523599,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          },
          {
            "steps": 32,
            "analytic_bias": -0.041175573785795776,
            "paired_mean": -0.03965375759547908,
            "paired_MCSE": 0.0009919791240891069,
            "analytic_expected_MCSE": 0.0012342295434882658,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          },
          {
            "steps": 64,
            "analytic_bias": -0.020827626619729842,
            "paired_mean": -0.02012644667453873,
            "paired_MCSE": 0.0007054106323910044,
            "analytic_expected_MCSE": 0.0007897816945465437,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      }
    ],
    "Brownian_association_error": 8.881784197001252e-16,
    "fine_driver_sha256": [
      "062cc28f1b5fc93039f27f4059ac1361e6d11682eb2435731d285d316f4aa823",
      "2d6f4757e5ad6fec57b5d63b1da982ea8f364ef0e7467bf075c5d78342e418ec",
      "211980ad2f8b1eb1d666d9f575765a1d33dd0f127690ebe0febd51f736cf9f4b",
      "9e847e310bb5c91aac72fe60ae3898c0774a54f284f0c96d1b661b1db4509ea9",
      "47ed94304c9637379f3605b34fc9285546d83dc9ac8ed989fccc1ae807baae0c",
      "f3017fb5c77c37ec260ddb326f1e746272ffaac77507eb0fd356c40e80e584ba",
      "44baac7402f08c0ddaaae154ae26f6c568fe73a8bf1d1db98e1db54073c949b7",
      "ea0164b72e67cd52ad0b56efc86884e7756c560c7a6ae48b2afe0d25d70f7cdb",
      "5e89673e3d79411f1605b0a87141c447779fbb0e0ba25f62f24c88a2db389ab0",
      "e32d50c91870002e9db7a4b0c251ecd997c681e26a877f7dc1774776cc6d9bd3",
      "bc6ec6e7a88fb142af33231a49c6a4952de8eee94aee6d675e3ed55a63da89fe",
      "ac8663af01ff7a5dd29873f8da7674438c0ce824d5a0d68c4361571e73556d6e",
      "658419fe6f33031525cd0f475b5b79a434fe0648b9dd219ce1827bac38c60a64",
      "723d7ed34394b933e3f577732aa4f6826dc48f41255294ce4f40ca60dcc34ebe",
      "32ba3a1d678327efa71fafd8775e54592d8c8ee2bcf700b91021d3a535ac4a2f",
      "b2d96051eefe7541c51ff53bc309b0562918977751f56f20948213b521a9f63b",
      "fc6f8bb229669f915d514fe451c366d3fdbf72f1279e5f9479e889574db08320",
      "cfce102e39422f655bbc1a3c332ce886e11dfd32fa492563a88bf7fd38af5383",
      "80adbe538b0f5f9b9c1caba2175d27cd3648e1f4acaaa8c7fc8a4422ba90c9a1",
      "0aa28d9838f8b4261821a718e7d10433e1a8843619075582bb9cd41a1e360cde",
      "bd7977d0290110397956f5c5aca3bd087181780f96dbd6bd4fd00ec473ae1b0f",
      "7d23d99637da04cd10a3aecc9a841cbbe5adacdcc5da018614cdf2255cf419d1",
      "ba997a851a487141e23fd1de6afca95f646279adca8e0ba52400c672d62e368b",
      "188fb1058a2c645eb9701b15efc1e44741c22b4b6492f87c01553c00d834c793",
      "b88b85f05d54af414a81b1951d5934f043ef20882b536234ebfecb5ae6b664a5",
      "7918daa0dc6fd330508bd29d816a051eaa47c0e680c47b2a399e5e268e1ca1f0",
      "9718d50375705d9fbb532ffe848f813a5652fbaf7c74e9627c078b31104f6afd",
      "f8b8d4fa2453cd347abd43c6e68cd80d5c780052a42440c4dc1386f850938a8c",
      "62486023170b5c8a56224f809204c0d727f81b10abcebe6da29a6859c2e399cc",
      "1d3cb939b24ce46e72d062d4ad56ed0fe1bffca70cb3a44d19421a303e93519a",
      "1ce008007caeaa391342596c98bcb6102c8b2b2ab77bbb2e275b98fe3d5b2b9b",
      "b8aa0ed98d5317954181d7433193f4ed3ebb6408ea3cea3a73dd6a4de7c20e8f"
    ],
    "completed_independent_seed_batches": 32
  },
  "checks": {
    "finite saved candidate arrays": true,
    "declared Brownian grouping roundoff": true,
    "power1/n8/paired mean calibration": true,
    "power1/n8/MCSE calibration": true,
    "power1/n16/paired mean calibration": true,
    "power1/n16/MCSE calibration": true,
    "power1/n32/paired mean calibration": true,
    "power1/n32/MCSE calibration": true,
    "power1/n32/resolved before slope": true,
    "power1/n64/paired mean calibration": true,
    "power1/n64/MCSE calibration": true,
    "power1/n64/resolved before slope": true,
    "power1/analytic weak order": true,
    "power1/sampled paired weak order": true,
    "power2/n8/paired mean calibration": true,
    "power2/n8/MCSE calibration": true,
    "power2/n16/paired mean calibration": true,
    "power2/n16/MCSE calibration": true,
    "power2/n32/paired mean calibration": true,
    "power2/n32/MCSE calibration": true,
    "power2/n32/resolved before slope": true,
    "power2/n64/paired mean calibration": true,
    "power2/n64/MCSE calibration": true,
    "power2/n64/resolved before slope": true,
    "power2/analytic weak order": true,
    "power2/sampled paired weak order": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/index.json

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments-preview.png)

保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- D. J. Higham (2001). An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations. https://epubs.siam.org/doi/10.1137/S0036144500378302; review_level=selected-primary-full-text-sections4-6
原著の線形SDE厳密解、strong/weak定義、EM、Milstein補正の選択節を確認。論文全体やMATLAB実験の再現ではありません。掲載strong定義L1と本例L2 RMSを区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# GBM weak bias and Monte Carlo error

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

**Methods used**

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) (`sde`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-algorithm)

Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.


**Problem figure**

![GBM weak bias and Monte Carlo error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-validation)

Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en) (`gbm-weak-moments`; Related-model reference · Analytic reference)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en) (`gbm-milstein-strong`; Related-model reference · Analytic reference)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
## Assumptions, units and boundaries

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

**Editorial clarification**

Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused.

## Adopted numerical method

Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

## References and validation

Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.

## Limits

Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused.

## Stored measurements and decisions

```json
{
  "metrics": {
    "observables": [
      {
        "observable_power": 1,
        "sampled_paired_order": 0.9956027089190806,
        "analytic_order": 0.986850922673782,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": -0.024551175738827653,
            "paired_mean": -0.02390546859088743,
            "paired_MCSE": 0.000431509288625275,
            "analytic_expected_MCSE": 0.0004902247814460831,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 16,
            "analytic_bias": -0.012570260133504842,
            "paired_mean": -0.012073199459893005,
            "paired_MCSE": 0.0002494235153701287,
            "analytic_expected_MCSE": 0.0003179426227319547,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 32,
            "analytic_bias": -0.006361702102222466,
            "paired_mean": -0.006046178211109456,
            "paired_MCSE": 0.00014930108420397513,
            "analytic_expected_MCSE": 0.00021219706970143816,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 64,
            "analytic_bias": -0.0032003745435279854,
            "paired_mean": -0.0030367554342063926,
            "paired_MCSE": 0.0001452128976770314,
            "analytic_expected_MCSE": 0.0001450153280978437,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      },
      {
        "observable_power": 2,
        "sampled_paired_order": 0.9744925206389199,
        "analytic_order": 0.9752562657019691,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": -0.15410825623347305,
            "paired_mean": -0.14906616356143917,
            "paired_MCSE": 0.003147990583178188,
            "analytic_expected_MCSE": 0.003291189368314816,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 16,
            "analytic_bias": -0.08050123855537453,
            "paired_mean": -0.07770877547600556,
            "paired_MCSE": 0.0018030716808605054,
            "analytic_expected_MCSE": 0.001999254398523599,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          },
          {
            "steps": 32,
            "analytic_bias": -0.041175573785795776,
            "paired_mean": -0.03965375759547908,
            "paired_MCSE": 0.0009919791240891069,
            "analytic_expected_MCSE": 0.0012342295434882658,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          },
          {
            "steps": 64,
            "analytic_bias": -0.020827626619729842,
            "paired_mean": -0.02012644667453873,
            "paired_MCSE": 0.0007054106323910044,
            "analytic_expected_MCSE": 0.0007897816945465437,
            "raw_EM_interval_coverage_for_discrete_truth": 0.90625,
            "coverage_binomial95": [
              0.7497730493162054,
              0.9802328198267152
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      }
    ],
    "Brownian_association_error": 8.881784197001252e-16,
    "fine_driver_sha256": [
      "062cc28f1b5fc93039f27f4059ac1361e6d11682eb2435731d285d316f4aa823",
      "2d6f4757e5ad6fec57b5d63b1da982ea8f364ef0e7467bf075c5d78342e418ec",
      "211980ad2f8b1eb1d666d9f575765a1d33dd0f127690ebe0febd51f736cf9f4b",
      "9e847e310bb5c91aac72fe60ae3898c0774a54f284f0c96d1b661b1db4509ea9",
      "47ed94304c9637379f3605b34fc9285546d83dc9ac8ed989fccc1ae807baae0c",
      "f3017fb5c77c37ec260ddb326f1e746272ffaac77507eb0fd356c40e80e584ba",
      "44baac7402f08c0ddaaae154ae26f6c568fe73a8bf1d1db98e1db54073c949b7",
      "ea0164b72e67cd52ad0b56efc86884e7756c560c7a6ae48b2afe0d25d70f7cdb",
      "5e89673e3d79411f1605b0a87141c447779fbb0e0ba25f62f24c88a2db389ab0",
      "e32d50c91870002e9db7a4b0c251ecd997c681e26a877f7dc1774776cc6d9bd3",
      "bc6ec6e7a88fb142af33231a49c6a4952de8eee94aee6d675e3ed55a63da89fe",
      "ac8663af01ff7a5dd29873f8da7674438c0ce824d5a0d68c4361571e73556d6e",
      "658419fe6f33031525cd0f475b5b79a434fe0648b9dd219ce1827bac38c60a64",
      "723d7ed34394b933e3f577732aa4f6826dc48f41255294ce4f40ca60dcc34ebe",
      "32ba3a1d678327efa71fafd8775e54592d8c8ee2bcf700b91021d3a535ac4a2f",
      "b2d96051eefe7541c51ff53bc309b0562918977751f56f20948213b521a9f63b",
      "fc6f8bb229669f915d514fe451c366d3fdbf72f1279e5f9479e889574db08320",
      "cfce102e39422f655bbc1a3c332ce886e11dfd32fa492563a88bf7fd38af5383",
      "80adbe538b0f5f9b9c1caba2175d27cd3648e1f4acaaa8c7fc8a4422ba90c9a1",
      "0aa28d9838f8b4261821a718e7d10433e1a8843619075582bb9cd41a1e360cde",
      "bd7977d0290110397956f5c5aca3bd087181780f96dbd6bd4fd00ec473ae1b0f",
      "7d23d99637da04cd10a3aecc9a841cbbe5adacdcc5da018614cdf2255cf419d1",
      "ba997a851a487141e23fd1de6afca95f646279adca8e0ba52400c672d62e368b",
      "188fb1058a2c645eb9701b15efc1e44741c22b4b6492f87c01553c00d834c793",
      "b88b85f05d54af414a81b1951d5934f043ef20882b536234ebfecb5ae6b664a5",
      "7918daa0dc6fd330508bd29d816a051eaa47c0e680c47b2a399e5e268e1ca1f0",
      "9718d50375705d9fbb532ffe848f813a5652fbaf7c74e9627c078b31104f6afd",
      "f8b8d4fa2453cd347abd43c6e68cd80d5c780052a42440c4dc1386f850938a8c",
      "62486023170b5c8a56224f809204c0d727f81b10abcebe6da29a6859c2e399cc",
      "1d3cb939b24ce46e72d062d4ad56ed0fe1bffca70cb3a44d19421a303e93519a",
      "1ce008007caeaa391342596c98bcb6102c8b2b2ab77bbb2e275b98fe3d5b2b9b",
      "b8aa0ed98d5317954181d7433193f4ed3ebb6408ea3cea3a73dd6a4de7c20e8f"
    ],
    "completed_independent_seed_batches": 32
  },
  "checks": {
    "finite saved candidate arrays": true,
    "declared Brownian grouping roundoff": true,
    "power1/n8/paired mean calibration": true,
    "power1/n8/MCSE calibration": true,
    "power1/n16/paired mean calibration": true,
    "power1/n16/MCSE calibration": true,
    "power1/n32/paired mean calibration": true,
    "power1/n32/MCSE calibration": true,
    "power1/n32/resolved before slope": true,
    "power1/n64/paired mean calibration": true,
    "power1/n64/MCSE calibration": true,
    "power1/n64/resolved before slope": true,
    "power1/analytic weak order": true,
    "power1/sampled paired weak order": true,
    "power2/n8/paired mean calibration": true,
    "power2/n8/MCSE calibration": true,
    "power2/n16/paired mean calibration": true,
    "power2/n16/MCSE calibration": true,
    "power2/n32/paired mean calibration": true,
    "power2/n32/MCSE calibration": true,
    "power2/n32/resolved before slope": true,
    "power2/n64/paired mean calibration": true,
    "power2/n64/MCSE calibration": true,
    "power2/n64/resolved before slope": true,
    "power2/analytic weak order": true,
    "power2/sampled paired weak order": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/index.json

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments-preview.png)

Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- D. J. Higham (2001). An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations. https://epubs.siam.org/doi/10.1137/S0036144500378302; review_level=selected-primary-full-text-sections4-6
Read selected original sections4-6 on linear SDEs,strong/weak definitions,EM and Milstein. No full-paper audit or reproduction of its MATLAB/logistic experiment. Its L1strong definition is distinguished from our L2RMS.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
