# 分布係数Bratuの行列非形成VJP / Matrix-free VJP for distributed Bratu coefficients

https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/

## 日本語

[分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-adjoint/#bratu-distributed-vjp) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#bratu-distributed-vjp)

### 方程式・問題の定義

内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。

#### [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

#### 分布係数Bratuの行列非形成VJP

補助実行例 · 実行例の定義・検証式

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

### 厳密解・参照解

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

#### [分布Bratu係数の独立dense感度と行列不要VJP](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

J_hU_\theta=\operatorname{diag}(e^u)B,\quad J_h^\top p=q,\quad \nabla_\theta\Psi=B^\top(e^u\odot p).

1D同次Dirichlet、63内点。a(x)=2+Bθは8/16/32個の線形hat制御で、主固定例は1.7≤a≤2.3。端点係数は零Dirichlet状態と異なり固定零にしません。

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

#### 分布係数Bratuの行列非形成VJP

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja)

### 計算法

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja)

補助実行例

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

## English

[Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-adjoint/#bratu-distributed-vjp) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#bratu-distributed-vjp-en)

### Equations and problem definitions

63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.

#### [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

#### Matrix-free VJP for distributed Bratu coefficients

Supplementary execution example · Example definition or validation formula

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

### Exact and reference solutions

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

#### [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-measurements)

Finite-grid numerical reference · Reference for the same problem

J_hU_\theta=\operatorname{diag}(e^u)B,\quad J_h^\top p=q,\quad \nabla_\theta\Psi=B^\top(e^u\odot p).

A one-dimensional zero-Dirichlet problem with 63 interior nodes. The coefficient a(x)=2+Btheta uses 8/16/32 linear-hat controls and stays between 1.7 and 2.3 in the fixed main cases. Endpoint coefficient controls are not zeroed like state Dirichlet values.

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

#### Matrix-free VJP for distributed Bratu coefficients

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en)

### Numerical methods

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en)

Supplementary execution example

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)
