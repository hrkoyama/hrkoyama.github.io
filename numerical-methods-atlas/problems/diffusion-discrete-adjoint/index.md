# 時間離散拡散の随伴とcheckpoint / Discrete diffusion adjoint and checkpoint replay

https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/

## 日本語

[時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-adjoint/#diffusion-discrete-adjoint) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#diffusion-discrete-adjoint)

### 方程式・問題の定義

無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。

#### [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja)

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

#### 時間離散拡散の随伴とcheckpoint

補助実行例 · 実行例の定義・検証式

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。

### 厳密解・参照解

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。

#### [後退Euler離散モードと時間厳密半離散拡散の参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-measurements)

解析解 · 同じ問題の参照

\lambda_{\ell,h}=4h^{-2}\sin^2(\ell\pi h/2),\quad a_{\ell,k+1}=\frac{a_{\ell,k}+\Delta t\,\theta\beta_\ell}{1+\Delta t\,\kappa\lambda_{\ell,h}};\quad a_{\ell}^{\rm sd}(T)=a_{\ell,0}e^{-\kappa\lambda_{\ell,h}T}+\frac{\theta\beta_\ell}{\kappa\lambda_{\ell,h}}(1-e^{-\kappa\lambda_{\ell,h}T}).

無次元x∈[0,1]、同次Dirichlet、κ=.1、θ=.2、T=.1。内点7/15、時間step64/128/256。目的関数はh重み付き終端誤差と指定二次正則化です。

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

#### 時間離散拡散の随伴とcheckpoint

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja)

### 計算法

ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja)

補助実行例

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。

無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

## English

[Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-adjoint/#diffusion-discrete-adjoint) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#diffusion-discrete-adjoint-en)

### Equations and problem definitions

Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.

#### [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en)

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

#### Discrete diffusion adjoint and checkpoint replay

Supplementary execution example · Example definition or validation formula

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.

### Exact and reference solutions

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.

#### [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-measurements)

Analytic reference · Reference for the same problem

\lambda_{\ell,h}=4h^{-2}\sin^2(\ell\pi h/2),\quad a_{\ell,k+1}=\frac{a_{\ell,k}+\Delta t\,\theta\beta_\ell}{1+\Delta t\,\kappa\lambda_{\ell,h}};\quad a_{\ell}^{\rm sd}(T)=a_{\ell,0}e^{-\kappa\lambda_{\ell,h}T}+\frac{\theta\beta_\ell}{\kappa\lambda_{\ell,h}}(1-e^{-\kappa\lambda_{\ell,h}T}).

Dimensionless x in [0,1] with zero Dirichlet data, kappa = .1, theta = .2 and T = .1. Use 7/15 interior nodes and 64/128/256 time steps. The objective has an h-weighted terminal error and specified quadratic penalties.

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

#### Discrete diffusion adjoint and checkpoint replay

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en)

### Numerical methods

Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en)

Supplementary execution example

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.

Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)
