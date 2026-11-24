# GN・LMと有界最小二乗のBratu比較 / Bratu comparisons of GN, LM and bounded least squares

https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/

## 日本語

[保存した2変数の反復点・残差評価点です。SciPy曲線は受理反復だけでなく残差評価を含み、これは2D物理空間の流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-inverse-optimization/#bratu-gn-lm-bounds) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#bratu-gn-lm-bounds)

### 方程式・問題の定義

無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。

#### [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

#### GN・LMと有界最小二乗のBratu比較

補助実行例 · 実行例の定義・検証式

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。

### 厳密解・参照解

独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。

#### [Bratu逆最小二乗の独立Thomas局所参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

F_h(u,a,b)=A_hu-(a+b(2x-1))\odot e^u=0,\quad \mathcal L=\tfrac12\|Hu-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2,\quad K=-HF_u^{-1}F_\theta.

1D零Dirichlet Bratuの31内点と5観測を用いる2係数逆問題。既存合成観測を再利用し、物理boxはa∈[1,2.8],b∈[-.5,.5]。目的正則化γ、LM減衰μ、変数尺度は別です。

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。

#### GN・LMと有界最小二乗のBratu比較

独立Thomas状態・感度と4局所参照fit。最終状態残差、物理勾配または投影勾配、目的値差、データのみのSVD、活性境界を検査。非有界法の共通参照は内点かつ非有界停留が条件です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja)

### 計算法

独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja)

補助実行例

同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。

無次元1D Bratu、31内点、u(0)=u(1)=0。既存の2係数モデルと保存済み観測を再利用。正則化γとLM減衰μを別に扱います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/model.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/model.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)

## English

[Saved two-parameter iterates and residual evaluations. SciPy paths include residual evaluations, not only accepted iterates; these are parameter coordinates, not a two-dimensional physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-inverse-optimization/#bratu-gn-lm-bounds) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#bratu-gn-lm-bounds-en)

### Equations and problem definitions

A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.

#### [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

#### Bratu comparisons of GN, LM and bounded least squares

Supplementary execution example · Example definition or validation formula

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.

### Exact and reference solutions

Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.

#### [Independent Thomas-based local references for Bratu inverse least squares](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-measurements)

Finite-grid numerical reference · Reference for the same problem

F_h(u,a,b)=A_hu-(a+b(2x-1))\odot e^u=0,\quad \mathcal L=\tfrac12\|Hu-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2,\quad K=-HF_u^{-1}F_\theta.

A two-coefficient inverse problem uses 31 interior nodes and five observations of the one-dimensional zero-Dirichlet Bratu model. Reuse existing synthetic data; the physical box is a in[1,2.8],b in[-.5,.5]. Objective regularization gamma, LM damping mu and variable scaling are distinct.

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.

#### Bratu comparisons of GN, LM and bounded least squares

Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en)

### Numerical methods

Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en)

Supplementary execution example

Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.

A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/model.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/model.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)
