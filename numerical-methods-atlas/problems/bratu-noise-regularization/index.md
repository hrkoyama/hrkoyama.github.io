# 雑音・モデル差と有限γ経路の正則化 / Noise, model discrepancy and finite gamma paths

https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/

## 日本語

[保存した2変数推定値と固定γの局所1標準偏差楕円。楕円は選択事象で条件づけた区間でも、少数反復で保証した信頼領域でもありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-inverse-optimization/#bratu-noise-regularization) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#bratu-noise-regularization)

### 方程式・問題の定義

Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。

#### [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

#### 雑音・モデル差と有限γ経路の正則化

補助実行例 · 実行例の定義・検証式

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。

### 厳密解・参照解

42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。

#### [有限γ経路と局所線形雑音伝播のBratu参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

G=K^TWK+\gamma I,\quad C_\gamma=G^{-1}K^TW\Sigma WKG^{-T},\quad b_\gamma=-\gamma G^{-1}(\theta_*-\theta_0).

31内点、5観測、W=I/5、Σ=σ²I。既存の31/1023格子観測を再利用します。雑音の標準偏差σは1e-4と1e-3で、独立な基底雑音は2 seedです。尺度・格子文脈をまたぐ比較は同じ雑音ベクトルを共有します。γは固定5点です。

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

#### 雑音・モデル差と有限γ経路の正則化

42 fitの最終残差・物理KKT・実行完了、選択規則、明示的2×2代数による固定線形モデルの共分散・偏り・モデル差応答、対称PSDを検査。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja)

### 計算法

全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja)

補助実行例

2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。

Bratu推定は31内点、5観測、W=I/5、Σ=σ²I。既存1023格子のデータは保存値を使い再生成しません。σ=1e-4/1e-3、seed67001/67002、γの固定5点です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/inverse-optimization/regularization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/regularization.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)

## English

[Saved two-parameter estimates and fixed-gamma local one-standard-deviation ellipses. These are neither selection-conditional intervals nor confidence regions with coverage established by this small ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-inverse-optimization/#bratu-noise-regularization) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#bratu-noise-regularization-en)

### Equations and problem definitions

Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.

#### [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

#### Noise, model discrepancy and finite gamma paths

Supplementary execution example · Example definition or validation formula

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.

### Exact and reference solutions

Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.

#### [Bratu references for finite gamma paths and local linear noise propagation](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-measurements)

Finite-grid numerical reference · Reference for the same problem

G=K^TWK+\gamma I,\quad C_\gamma=G^{-1}K^TW\Sigma WKG^{-T},\quad b_\gamma=-\gamma G^{-1}(\theta_*-\theta_0).

Use 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Reuse existing 31/1023-grid observations. The noise standard deviations sigma are 1e-4 and 1e-3; two seeds provide independent base noises, while scaled/grid-context variants are paired. Gamma has five fixed values.

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

#### Noise, model discrepancy and finite gamma paths

Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en)

### Numerical methods

Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en)

Supplementary execution example

Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.

Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/inverse-optimization/regularization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/regularization.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)
