# OUのweakモーメントと同時Brownian結合

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

**使用手法**

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) (`sde`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-algorithm)

fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
$$

- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。


**問題の図**

![OUのweakモーメントと同時Brownian結合：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-validation)

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja) (`ou-weak-moments`; 関連モデルの参照 · 解析参照)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
## 前提・単位・境界

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

**編集上の補足**

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

## 採用した計算法

fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
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
        "sampled_paired_order": 1.0028604920506838,
        "analytic_order": 1.0151029162857539,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": -0.016601525664882343,
            "paired_mean": -0.01629562931347308,
            "paired_MCSE": 0.00023909443711104658,
            "analytic_expected_MCSE": 0.00022102482847032208,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 16,
            "analytic_bias": -0.008065564380142496,
            "paired_mean": -0.007887561656949873,
            "paired_MCSE": 0.00010882818086019489,
            "analytic_expected_MCSE": 0.00010710329337130175,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 32,
            "analytic_bias": -0.003976653259526749,
            "paired_mean": -0.003939807047794929,
            "paired_MCSE": 5.3339993867843966e-05,
            "analytic_expected_MCSE": 5.2736853897338943e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 64,
            "analytic_bias": -0.0019746126237947625,
            "paired_mean": -0.0019640863979277275,
            "paired_MCSE": 2.572665329848958e-05,
            "analytic_expected_MCSE": 2.6169126824338754e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      },
      {
        "observable_power": 2,
        "sampled_paired_order": 1.0496248413875717,
        "analytic_order": 1.0389267433589098,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": 0.014129402163588095,
            "paired_mean": 0.01401542171183142,
            "paired_MCSE": 0.00024104357117435304,
            "analytic_expected_MCSE": 0.00026472839301117877,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 16,
            "analytic_bias": 0.006561607911553392,
            "paired_mean": 0.00647516245322562,
            "paired_MCSE": 0.00013154200960569608,
            "analytic_expected_MCSE": 0.00012695902474324364,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 32,
            "analytic_bias": 0.0031644575406652867,
            "paired_mean": 0.0031052169014772067,
            "paired_MCSE": 6.715510115001812e-05,
            "analytic_expected_MCSE": 6.22062303077159e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 64,
            "analytic_bias": 0.0015542255693837448,
            "paired_mean": 0.0015111707743697739,
            "paired_MCSE": 3.073670093533357e-05,
            "analytic_expected_MCSE": 3.0793830756280135e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      }
    ],
    "Brownian_association_error": 8.881784197001252e-16,
    "fine_driver_sha256": [
      "0d73f7e3fb6d4fb13a8fe0acf5b067cc7431e3342d5714438b195926ccb31bd6",
      "517a0733a44601dc5a390ac93942b07115b9445189b75a99f1b92cfd206ced8c",
      "c4b8023f47bf9ed3f0aa9eec01c7d637dc9ae0db3660cd466de7776d363056ab",
      "2895543ecc2a01393b4c7cec98641749aca4f9a06bc37e13c8bcbac76ae6d45a",
      "033b60984273a09b7f5e14f43e0d8fead742341211063ff321cf2abec09c42c0",
      "81f1e26e638fe732e2018c5eb5b86c40b6aff57bf40bcfecaf298c5e21276c69",
      "f86b03f661cf9206146b59d4cb3040097fd1c63431946ddbb7a19d4b5ef0e818",
      "66640fadaf7f5f9400389fa76894e4399a6960536fa45cc9e78a6bab399680d5",
      "a364057c053f3bf3a5bc2cce7ab69f8b996cb9b639bcc297c64b53a657e0977e",
      "cc08ec187a765b97cc878d0d18a1da339e92571828f7112043c32127e174870c",
      "75459ce05f29203347f60645c0eb1b9311e6dc5cb31742bc6cd1bc931a4650aa",
      "e2e0389256a8600f7865668d7495be7386a389a86ff661c3986fe87b7a156dcd",
      "e4bf8fe176ccc3e6906a384a2a7d7886c5119e02b944b4d785b019c31aac922a",
      "54b5bb78ee939b6aa5320805eec7287185b17a4544ddcbfa1ebc741ccfaca694",
      "86ff8a27f2343e59c38463c1ac403594b382d865baffc4cb225df796650d30dc",
      "904c4738321c84035196329704a459d23a6d497bd00427ae7bdf9c0434a8fbfd",
      "abfaa427b6bed41f959993b7750980045b29f758682924d55ff0b27f8309675d",
      "d21d24ab4375a6b1e73a4152582eb9df0bf463e777970cd1810cb28594fbea33",
      "b9dc500fbb43c9b6ae1e2bbc3111c311d128a3ba4fbaf19c5d66430bf68e6e6a",
      "1f623b10ba38ebeb0d21831e8f61e0e0edd2952c7421eb87326b35cedc73567a",
      "dc8427870eca1e02ba741dcc8ca42881d69b86a60153ccaf1845afc186b2ab76",
      "af8fb326a6540e78c5d79d6382c0882821fc17ac518b370cc7eba0765dee6e8c",
      "90f7a22a5a05a513c18b56c72ee17fe2e56adb126ad202483ac075cffdc9f407",
      "bedb31ee586f99e001eba8020550576196d237c3467da4fa26d5be437dc6cb1d",
      "5d01d5a09fb9570e91b645d447d4946017dd93725fa4c4d5b91eafeebcef87c8",
      "c704833cf3a478237eeed30edb1229bd91e551d6723be097cd01da19b0db5175",
      "a8e62ae7577e1d047a11ca69f8d045f798132b06dadf511c6733387769338ccf",
      "42503445b6f496bc8371c06e89ddfde8bd39fe61e4a8745c8f46e487ccab605b",
      "ff4e5d69c37ffb1e116ac90e4d3013010416f21a8b1aad910e636570f27f2d05",
      "7d71965364b0db48fa6cd0c5ed42ab1e770be594c6dcf6e9dd2b94ed882a8529",
      "f0e2d130c7cfee902ccad20215a5835e5e17e05b7e0bdd9900744f164ac9e5c1",
      "424e0c38ca4dc556b66825f94eb5f19190607740a16d53e91e3461a3d6fd609b"
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

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/index.json

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments-preview.png)

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

# OU weak moments with joint Brownian coupling

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

**Methods used**

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) (`sde`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-algorithm)

Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
$$

- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.


**Problem figure**

![OU weak moments with joint Brownian coupling: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-validation)

Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.

- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en) (`ou-weak-moments`; Related-model reference · Analytic reference)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
## Assumptions, units and boundaries

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

**Editorial clarification**

Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused.

## Adopted numerical method

Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
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
        "sampled_paired_order": 1.0028604920506838,
        "analytic_order": 1.0151029162857539,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": -0.016601525664882343,
            "paired_mean": -0.01629562931347308,
            "paired_MCSE": 0.00023909443711104658,
            "analytic_expected_MCSE": 0.00022102482847032208,
            "raw_EM_interval_coverage_for_discrete_truth": 0.9375,
            "coverage_binomial95": [
              0.7919305701049926,
              0.9923392636535436
            ]
          },
          {
            "steps": 16,
            "analytic_bias": -0.008065564380142496,
            "paired_mean": -0.007887561656949873,
            "paired_MCSE": 0.00010882818086019489,
            "analytic_expected_MCSE": 0.00010710329337130175,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 32,
            "analytic_bias": -0.003976653259526749,
            "paired_mean": -0.003939807047794929,
            "paired_MCSE": 5.3339993867843966e-05,
            "analytic_expected_MCSE": 5.2736853897338943e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 64,
            "analytic_bias": -0.0019746126237947625,
            "paired_mean": -0.0019640863979277275,
            "paired_MCSE": 2.572665329848958e-05,
            "analytic_expected_MCSE": 2.6169126824338754e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      },
      {
        "observable_power": 2,
        "sampled_paired_order": 1.0496248413875717,
        "analytic_order": 1.0389267433589098,
        "levels": [
          {
            "steps": 8,
            "analytic_bias": 0.014129402163588095,
            "paired_mean": 0.01401542171183142,
            "paired_MCSE": 0.00024104357117435304,
            "analytic_expected_MCSE": 0.00026472839301117877,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 16,
            "analytic_bias": 0.006561607911553392,
            "paired_mean": 0.00647516245322562,
            "paired_MCSE": 0.00013154200960569608,
            "analytic_expected_MCSE": 0.00012695902474324364,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 32,
            "analytic_bias": 0.0031644575406652867,
            "paired_mean": 0.0031052169014772067,
            "paired_MCSE": 6.715510115001812e-05,
            "analytic_expected_MCSE": 6.22062303077159e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          },
          {
            "steps": 64,
            "analytic_bias": 0.0015542255693837448,
            "paired_mean": 0.0015111707743697739,
            "paired_MCSE": 3.073670093533357e-05,
            "analytic_expected_MCSE": 3.0793830756280135e-05,
            "raw_EM_interval_coverage_for_discrete_truth": 0.96875,
            "coverage_binomial95": [
              0.8378290058184884,
              0.9992091314020475
            ]
          }
        ],
        "coverage_scope": "Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion."
      }
    ],
    "Brownian_association_error": 8.881784197001252e-16,
    "fine_driver_sha256": [
      "0d73f7e3fb6d4fb13a8fe0acf5b067cc7431e3342d5714438b195926ccb31bd6",
      "517a0733a44601dc5a390ac93942b07115b9445189b75a99f1b92cfd206ced8c",
      "c4b8023f47bf9ed3f0aa9eec01c7d637dc9ae0db3660cd466de7776d363056ab",
      "2895543ecc2a01393b4c7cec98641749aca4f9a06bc37e13c8bcbac76ae6d45a",
      "033b60984273a09b7f5e14f43e0d8fead742341211063ff321cf2abec09c42c0",
      "81f1e26e638fe732e2018c5eb5b86c40b6aff57bf40bcfecaf298c5e21276c69",
      "f86b03f661cf9206146b59d4cb3040097fd1c63431946ddbb7a19d4b5ef0e818",
      "66640fadaf7f5f9400389fa76894e4399a6960536fa45cc9e78a6bab399680d5",
      "a364057c053f3bf3a5bc2cce7ab69f8b996cb9b639bcc297c64b53a657e0977e",
      "cc08ec187a765b97cc878d0d18a1da339e92571828f7112043c32127e174870c",
      "75459ce05f29203347f60645c0eb1b9311e6dc5cb31742bc6cd1bc931a4650aa",
      "e2e0389256a8600f7865668d7495be7386a389a86ff661c3986fe87b7a156dcd",
      "e4bf8fe176ccc3e6906a384a2a7d7886c5119e02b944b4d785b019c31aac922a",
      "54b5bb78ee939b6aa5320805eec7287185b17a4544ddcbfa1ebc741ccfaca694",
      "86ff8a27f2343e59c38463c1ac403594b382d865baffc4cb225df796650d30dc",
      "904c4738321c84035196329704a459d23a6d497bd00427ae7bdf9c0434a8fbfd",
      "abfaa427b6bed41f959993b7750980045b29f758682924d55ff0b27f8309675d",
      "d21d24ab4375a6b1e73a4152582eb9df0bf463e777970cd1810cb28594fbea33",
      "b9dc500fbb43c9b6ae1e2bbc3111c311d128a3ba4fbaf19c5d66430bf68e6e6a",
      "1f623b10ba38ebeb0d21831e8f61e0e0edd2952c7421eb87326b35cedc73567a",
      "dc8427870eca1e02ba741dcc8ca42881d69b86a60153ccaf1845afc186b2ab76",
      "af8fb326a6540e78c5d79d6382c0882821fc17ac518b370cc7eba0765dee6e8c",
      "90f7a22a5a05a513c18b56c72ee17fe2e56adb126ad202483ac075cffdc9f407",
      "bedb31ee586f99e001eba8020550576196d237c3467da4fa26d5be437dc6cb1d",
      "5d01d5a09fb9570e91b645d447d4946017dd93725fa4c4d5b91eafeebcef87c8",
      "c704833cf3a478237eeed30edb1229bd91e551d6723be097cd01da19b0db5175",
      "a8e62ae7577e1d047a11ca69f8d045f798132b06dadf511c6733387769338ccf",
      "42503445b6f496bc8371c06e89ddfde8bd39fe61e4a8745c8f46e487ccab605b",
      "ff4e5d69c37ffb1e116ac90e4d3013010416f21a8b1aad910e636570f27f2d05",
      "7d71965364b0db48fa6cd0c5ed42ab1e770be594c6dcf6e9dd2b94ed882a8529",
      "f0e2d130c7cfee902ccad20215a5835e5e17e05b7e0bdd9900744f164ac9e5c1",
      "424e0c38ca4dc556b66825f94eb5f19190607740a16d53e91e3461a3d6fd609b"
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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/index.json

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments-preview.png)

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
