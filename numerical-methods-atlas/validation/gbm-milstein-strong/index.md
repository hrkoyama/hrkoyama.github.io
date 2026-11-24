# 同じBrownian経路のMilstein・EM strong比較

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
## 前提・単位・境界

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

**編集上の補足**

L2終端誤差を扱い、原著のL1定義と区別。GBM以外の非Lipschitz系・正値性の一般保証はしません。既存gbm-sdeへの手法追加です。

## 採用した計算法

Milsteinは.5σ²X(dW²-h)を追加。全法・刻みでfine driverと厳密端点1配列を共有。負状態を修復しません。

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

## 比較・検証

相殺を含む解析MSEをDecimal80/120と独立1step GHで資格。二乗誤差の5SE校正、固定3段RMS率、最細段の優位性を判定。相関を保つ64pathblock jackknifeで率の不確実性を記述。

## 確認の限界

L2終端誤差を扱い、原著のL1定義と区別。GBM以外の非Lipschitz系・正値性の一般保証はしません。既存gbm-sdeへの手法追加です。

## 保存実測値と判定

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

# Milstein and EM on identical Brownian paths

Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.

**Methods used**

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) (`sde`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-algorithm)

Milstein adds.5sigma²X(dW²-h). All methods/levels share the fine driver and one exact terminal array. No state repair.

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.


**Problem figure**

![Milstein and EM on identical Brownian paths: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-validation)

Qualify cancellation-prone analytic MSE by Decimal80/120and independent one-step GH. Gate squared-error5SE calibration,fixed-three-level RMS rates and finest advantage.64paired path-block jackknife describes slope uncertainty.

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en) (`gbm-weak-moments`; Related-model reference · Analytic reference)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en) (`gbm-milstein-strong`; Related-model reference · Analytic reference)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
## Assumptions, units and boundaries

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

**Editorial clarification**

EndpointL2error is distinct from the selected paper L1definition. No general non-Lipschitz/positivity guarantee. This extends existinggbm-sde rather than adding a physical problem.

## Adopted numerical method

Milstein adds.5sigma²X(dW²-h). All methods/levels share the fine driver and one exact terminal array. No state repair.

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

## References and validation

Qualify cancellation-prone analytic MSE by Decimal80/120and independent one-step GH. Gate squared-error5SE calibration,fixed-three-level RMS rates and finest advantage.64paired path-block jackknife describes slope uncertainty.

## Limits

EndpointL2error is distinct from the selected paper L1definition. No general non-Lipschitz/positivity guarantee. This extends existinggbm-sde rather than adding a physical problem.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/index.json

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong-preview.png)

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
