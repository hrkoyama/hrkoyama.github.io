# 分布係数Bratuの行列非形成VJP

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

**使用手法**

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) (`adjoint`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-algorithm)

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。


**問題の図**

![分布係数Bratuの行列非形成VJP：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-validation)

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

- [分布Bratu係数の独立dense感度と行列不要VJP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja) (`bratu-distributed-vjp`; 同じ問題の参照 · 有限格子の数値参照)

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。
## 前提・単位・境界

内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。

**編集上の補足**

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

## 採用した計算法

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

## 比較・検証

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

## 確認の限界

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

## 保存実測値と判定

```json
{
  "metrics": {
    "principal_records": 3,
    "FD_state_solves": 18,
    "affine_error": 4.440892098500626e-16,
    "wrong_offset_error": 2.0000000000000004,
    "primary_scope": "Persistent named-array inventory and declared fixed Krylov workspace; not an RSS/peak-allocation measurement."
  },
  "checks": {
    "m8-state-residual": true,
    "m8-coefficient": true,
    "m8-duality": true,
    "m8-VJP-dense-reference": true,
    "m8-FD-finest": true,
    "m8-objective-count": true,
    "m8-allocation": true,
    "m8-finite-boundary": true,
    "m16-state-residual": true,
    "m16-coefficient": true,
    "m16-duality": true,
    "m16-VJP-dense-reference": true,
    "m16-FD-finest": true,
    "m16-objective-count": true,
    "m16-allocation": true,
    "m16-finite-boundary": true,
    "m32-state-residual": true,
    "m32-coefficient": true,
    "m32-duality": true,
    "m32-VJP-dense-reference": true,
    "m32-FD-finest": true,
    "m32-objective-count": true,
    "m32-allocation": true,
    "m32-finite-boundary": true,
    "nonsymmetric-transpose": true,
    "affine-offset": true,
    "qualified-cache": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/index.json

![分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
math.sumprodの公式API選択箇所を確認。閲覧日は出版年ではなく、一般の正丸め保証ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Matrix-free VJP for distributed Bratu coefficients

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

**Methods used**

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) (`adjoint`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-algorithm)

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.


**Problem figure**

![Matrix-free VJP for distributed Bratu coefficients: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-validation)

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en) (`bratu-distributed-vjp`; Same-problem reference · Finite-grid numerical reference)

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.
## Assumptions, units and boundaries

63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.

**Editorial clarification**

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

## Adopted numerical method

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

## References and validation

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

## Limits

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

## Stored measurements and decisions

```json
{
  "metrics": {
    "principal_records": 3,
    "FD_state_solves": 18,
    "affine_error": 4.440892098500626e-16,
    "wrong_offset_error": 2.0000000000000004,
    "primary_scope": "Persistent named-array inventory and declared fixed Krylov workspace; not an RSS/peak-allocation measurement."
  },
  "checks": {
    "m8-state-residual": true,
    "m8-coefficient": true,
    "m8-duality": true,
    "m8-VJP-dense-reference": true,
    "m8-FD-finest": true,
    "m8-objective-count": true,
    "m8-allocation": true,
    "m8-finite-boundary": true,
    "m16-state-residual": true,
    "m16-coefficient": true,
    "m16-duality": true,
    "m16-VJP-dense-reference": true,
    "m16-FD-finest": true,
    "m16-objective-count": true,
    "m16-allocation": true,
    "m16-finite-boundary": true,
    "m32-state-residual": true,
    "m32-coefficient": true,
    "m32-duality": true,
    "m32-VJP-dense-reference": true,
    "m32-FD-finest": true,
    "m32-objective-count": true,
    "m32-allocation": true,
    "m32-finite-boundary": true,
    "nonsymmetric-transpose": true,
    "affine-offset": true,
    "qualified-cache": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/index.json

![Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
Selectedofficial math.sumprod API read;accessdate is notpublicationyear,no globalcorrectrounding claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
