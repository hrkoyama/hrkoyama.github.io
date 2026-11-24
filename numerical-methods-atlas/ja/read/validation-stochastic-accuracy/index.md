# SDEの弱誤差・強誤差と標本誤差

解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## GBMのweak誤差とMonte Carlo標準誤差

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
### 前提・単位・境界

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

**編集上の補足**

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

### 採用した計算法

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

### 比較・検証

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

### 確認の限界

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- D. J. Higham (2001). An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations. https://epubs.siam.org/doi/10.1137/S0036144500378302; review_level=selected-primary-full-text-sections4-6
原著の線形SDE厳密解、strong/weak定義、EM、Milstein補正の選択節を確認。論文全体やMATLAB実験の再現ではありません。掲載strong定義L1と本例L2 RMSを区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## OUのweakモーメントと同時Brownian結合

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
### 前提・単位・境界

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

**編集上の補足**

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

### 採用した計算法

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

### 比較・検証

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

### 確認の限界

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- D. J. Higham (2001). An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations. https://epubs.siam.org/doi/10.1137/S0036144500378302; review_level=selected-primary-full-text-sections4-6
原著の線形SDE厳密解、strong/weak定義、EM、Milstein補正の選択節を確認。論文全体やMATLAB実験の再現ではありません。掲載strong定義L1と本例L2 RMSを区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 同じBrownian経路のMilstein・EM strong比較

補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。

**使用手法**

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) (`sde`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-algorithm)

Milsteinは.5σ²X(dW²-h)を追加。全法・刻みでfine driverと厳密端点1配列を共有。負状態を修復しません。

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。


**問題の図**

![同じBrownian経路のMilstein・EM strong比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-validation)

相殺を含む解析MSEをDecimal80/120と独立1step GHで資格。二乗誤差の5SE校正、固定3段RMS率、最細段の優位性を判定。相関を保つ64pathblock jackknifeで率の不確実性を記述。

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja) (`gbm-weak-moments`; 関連モデルの参照 · 解析参照)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja) (`gbm-milstein-strong`; 関連モデルの参照 · 解析参照)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
### 前提・単位・境界

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

**編集上の補足**

L2終端誤差を扱い、原著のL1定義と区別。GBM以外の非Lipschitz系・正値性の一般保証はしません。既存gbm-sdeへの手法追加です。

### 採用した計算法

Milsteinは.5σ²X(dW²-h)を追加。全法・刻みでfine driverと厳密端点1配列を共有。負状態を修復しません。

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

### 比較・検証

相殺を含む解析MSEをDecimal80/120と独立1step GHで資格。二乗誤差の5SE校正、固定3段RMS率、最細段の優位性を判定。相関を保つ64pathblock jackknifeで率の不確実性を記述。

### 確認の限界

L2終端誤差を扱い、原著のL1定義と区別。GBM以外の非Lipschitz系・正値性の一般保証はしません。既存gbm-sdeへの手法追加です。

### 保存実測値と判定

```json
{
  "metrics": {
    "methods": [
      {
        "method": "em",
        "fixed_last_three_level_order": 0.4998402424562693,
        "paired64block_jackknife_order_SE": 0.005081776686564279,
        "levels": [
          {
            "steps": 16,
            "sample_RMS": 0.03546853869286994,
            "analytic_RMS": 0.03587672817493905,
            "squared_error_SE": 2.097976302745995e-05,
            "RMS_nominal95": [
              0.03488406021479733,
              0.03604354057172545
            ]
          },
          {
            "steps": 32,
            "sample_RMS": 0.025165151018332176,
            "analytic_RMS": 0.02527327799108889,
            "squared_error_SE": 8.876035396356257e-06,
            "RMS_nominal95": [
              0.024817093223685645,
              0.025508460076567263
            ]
          },
          {
            "steps": 64,
            "sample_RMS": 0.017816206216199258,
            "analytic_RMS": 0.017835633497176234,
            "squared_error_SE": 4.05128352337309e-06,
            "RMS_nominal95": [
              0.0175919536760749,
              0.018037670962047978
            ]
          },
          {
            "steps": 128,
            "sample_RMS": 0.012585362493127097,
            "analytic_RMS": 0.01259894455771596,
            "squared_error_SE": 1.997492589267111e-06,
            "RMS_nominal95": [
              0.012428850934380906,
              0.012739951437025162
            ]
          }
        ],
        "scope": "L2endpoint RMS; uncertainty is first computed on complete-path squared error,not independent-level regression."
      },
      {
        "method": "milstein",
        "fixed_last_three_level_order": 0.9964533189042089,
        "paired64block_jackknife_order_SE": 0.003307644094798437,
        "levels": [
          {
            "steps": 16,
            "sample_RMS": 0.005694296746405224,
            "analytic_RMS": 0.00575637004554713,
            "squared_error_SE": 6.844976320449696e-07,
            "RMS_nominal95": [
              0.005575251091189529,
              0.005810904072726739
            ]
          },
          {
            "steps": 32,
            "sample_RMS": 0.0028808462540585045,
            "analytic_RMS": 0.002900680886555887,
            "squared_error_SE": 1.7007993941367778e-07,
            "RMS_nominal95": [
              0.0028223969571588184,
              0.0029381330288580335
            ]
          },
          {
            "steps": 64,
            "sample_RMS": 0.0014353709990780313,
            "analytic_RMS": 0.0014560370611600836,
            "squared_error_SE": 4.114602073259352e-08,
            "RMS_nominal95": [
              0.0014069986447226039,
              0.0014631932967784152
            ]
          },
          {
            "steps": 128,
            "sample_RMS": 0.0007237613790168262,
            "analytic_RMS": 0.0007294519104131344,
            "squared_error_SE": 1.035143974400747e-08,
            "RMS_nominal95": [
              0.0007096069931095287,
              0.0007376442115564449
            ]
          }
        ],
        "scope": "L2endpoint RMS; uncertainty is first computed on complete-path squared error,not independent-level regression."
      }
    ],
    "fine_driver_sha256": [
      "0794acba8cd8fdeb082cb9d29a72fb8e832fe7866188a764e8830287d2ab927f",
      "0b3d5dc28f3a8e4926bb77927716fd3e8a527bf6656c91df7c5cce5bd5f436d6",
      "fd6162c066179bc3a267b4a95fd6ffb025aca0ecee80a07719fe021df36bea20",
      "3930ed3f59a8122c2eb5ad97cf93df4880ecf303ca2851e5a33c61829fb95c88"
    ],
    "Brownian_association_error": 1.3322676295501878e-15,
    "same_exact_endpoint_role": "One stored fine terminal array reused by both methods and every level; sums under different associations need not be bit identical."
  },
  "checks": {
    "finite saved candidate arrays": true,
    "declared Brownian grouping roundoff": true,
    "em/n16/squared error calibration": true,
    "em/n32/squared error calibration": true,
    "em/n64/squared error calibration": true,
    "em/n128/squared error calibration": true,
    "em/sampled RMS order": true,
    "milstein/n16/squared error calibration": true,
    "milstein/n32/squared error calibration": true,
    "milstein/n64/squared error calibration": true,
    "milstein/n128/squared error calibration": true,
    "milstein/sampled RMS order": true,
    "finest Milstein advantage": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/index.json

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong-preview.png)

保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。

### 取得・実行

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

### 出典と確認範囲

- D. J. Higham (2001). An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations. https://epubs.siam.org/doi/10.1137/S0036144500378302; review_level=selected-primary-full-text-sections4-6
原著の線形SDE厳密解、strong/weak定義、EM、Milstein補正の選択節を確認。論文全体やMATLAB実験の再現ではありません。掲載strong定義L1と本例L2 RMSを区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
