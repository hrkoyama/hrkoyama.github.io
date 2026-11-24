# 時間離散拡散の随伴とcheckpoint

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。

**使用手法**

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) (`adjoint`)
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) (`backward-euler`)
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) (`thomas`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-algorithm)

ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。


**問題の図**

![時間離散拡散の随伴とcheckpoint：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-validation)

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。

- [後退Euler離散モードと時間厳密半離散拡散の参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-diffusion-discrete-adjoint-ja) (`diffusion-discrete-adjoint`; 同じ問題の参照 · 解析参照)

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。
## 前提・単位・境界

無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。

**編集上の補足**

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

## 採用した計算法

ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

## 比較・検証

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。

## 確認の限界

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "time_ratios": [
      {
        "n": 7,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.5007714700172587,
        "denominator": 0.00011295826203078933
      },
      {
        "n": 7,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.5003862639676856,
        "denominator": 5.6566274927753076e-05
      },
      {
        "n": 15,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.500801018633583,
        "denominator": 0.00011971557684064543
      },
      {
        "n": 15,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.500401075710245,
        "denominator": 5.99536828281022e-05
      }
    ],
    "principal_records": 6,
    "FD_forward_evolutions": 18,
    "ownership_scope": "Unique explicit scientific arrays; validation loaded after the separate ownership windows; serialization internals are not process RSS."
  },
  "checks": {
    "n7-N64-finite-boundary": true,
    "n7-N64-state-modal": true,
    "n7-N64-adjoint-modal": true,
    "n7-N64-tangent-modal": true,
    "n7-N64-adjoint-tangent": true,
    "n7-N64-replay-state": true,
    "n7-N64-replay-gradient": true,
    "n7-N64-exact-work": true,
    "n7-N128-finite-boundary": true,
    "n7-N128-state-modal": true,
    "n7-N128-adjoint-modal": true,
    "n7-N128-tangent-modal": true,
    "n7-N128-adjoint-tangent": true,
    "n7-N128-replay-state": true,
    "n7-N128-replay-gradient": true,
    "n7-N128-exact-work": true,
    "n7-N256-finite-boundary": true,
    "n7-N256-state-modal": true,
    "n7-N256-adjoint-modal": true,
    "n7-N256-tangent-modal": true,
    "n7-N256-adjoint-tangent": true,
    "n7-N256-replay-state": true,
    "n7-N256-replay-gradient": true,
    "n7-N256-exact-work": true,
    "n7-time-ratio-64-128": true,
    "n7-time-ratio-128-256": true,
    "n7-N256-storage": true,
    "n15-N64-finite-boundary": true,
    "n15-N64-state-modal": true,
    "n15-N64-adjoint-modal": true,
    "n15-N64-tangent-modal": true,
    "n15-N64-adjoint-tangent": true,
    "n15-N64-replay-state": true,
    "n15-N64-replay-gradient": true,
    "n15-N64-exact-work": true,
    "n15-N128-finite-boundary": true,
    "n15-N128-state-modal": true,
    "n15-N128-adjoint-modal": true,
    "n15-N128-tangent-modal": true,
    "n15-N128-adjoint-tangent": true,
    "n15-N128-replay-state": true,
    "n15-N128-replay-gradient": true,
    "n15-N128-exact-work": true,
    "n15-N256-finite-boundary": true,
    "n15-N256-state-modal": true,
    "n15-N256-adjoint-modal": true,
    "n15-N256-tangent-modal": true,
    "n15-N256-adjoint-tangent": true,
    "n15-N256-replay-state": true,
    "n15-N256-replay-gradient": true,
    "n15-N256-exact-work": true,
    "n15-time-ratio-64-128": true,
    "n15-time-ratio-128-256": true,
    "n15-N256-storage": true,
    "FD-direction0": true,
    "FD-direction1": true,
    "FD-direction2": true,
    "FD-all-finite": true,
    "qualified-cache": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/index.json

![時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。

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


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Discrete diffusion adjoint and checkpoint replay

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.

**Methods used**

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) (`adjoint`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) (`thomas`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-algorithm)

Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.


**Problem figure**

![Discrete diffusion adjoint and checkpoint replay: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-validation)

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.

- [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-diffusion-discrete-adjoint-en) (`diffusion-discrete-adjoint`; Same-problem reference · Analytic reference)

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.
## Assumptions, units and boundaries

Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.

**Editorial clarification**

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

## Adopted numerical method

Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

## References and validation

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.

## Limits

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

## Stored measurements and decisions

```json
{
  "metrics": {
    "time_ratios": [
      {
        "n": 7,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.5007714700172587,
        "denominator": 0.00011295826203078933
      },
      {
        "n": 7,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.5003862639676856,
        "denominator": 5.6566274927753076e-05
      },
      {
        "n": 15,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.500801018633583,
        "denominator": 0.00011971557684064543
      },
      {
        "n": 15,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.500401075710245,
        "denominator": 5.99536828281022e-05
      }
    ],
    "principal_records": 6,
    "FD_forward_evolutions": 18,
    "ownership_scope": "Unique explicit scientific arrays; validation loaded after the separate ownership windows; serialization internals are not process RSS."
  },
  "checks": {
    "n7-N64-finite-boundary": true,
    "n7-N64-state-modal": true,
    "n7-N64-adjoint-modal": true,
    "n7-N64-tangent-modal": true,
    "n7-N64-adjoint-tangent": true,
    "n7-N64-replay-state": true,
    "n7-N64-replay-gradient": true,
    "n7-N64-exact-work": true,
    "n7-N128-finite-boundary": true,
    "n7-N128-state-modal": true,
    "n7-N128-adjoint-modal": true,
    "n7-N128-tangent-modal": true,
    "n7-N128-adjoint-tangent": true,
    "n7-N128-replay-state": true,
    "n7-N128-replay-gradient": true,
    "n7-N128-exact-work": true,
    "n7-N256-finite-boundary": true,
    "n7-N256-state-modal": true,
    "n7-N256-adjoint-modal": true,
    "n7-N256-tangent-modal": true,
    "n7-N256-adjoint-tangent": true,
    "n7-N256-replay-state": true,
    "n7-N256-replay-gradient": true,
    "n7-N256-exact-work": true,
    "n7-time-ratio-64-128": true,
    "n7-time-ratio-128-256": true,
    "n7-N256-storage": true,
    "n15-N64-finite-boundary": true,
    "n15-N64-state-modal": true,
    "n15-N64-adjoint-modal": true,
    "n15-N64-tangent-modal": true,
    "n15-N64-adjoint-tangent": true,
    "n15-N64-replay-state": true,
    "n15-N64-replay-gradient": true,
    "n15-N64-exact-work": true,
    "n15-N128-finite-boundary": true,
    "n15-N128-state-modal": true,
    "n15-N128-adjoint-modal": true,
    "n15-N128-tangent-modal": true,
    "n15-N128-adjoint-tangent": true,
    "n15-N128-replay-state": true,
    "n15-N128-replay-gradient": true,
    "n15-N128-exact-work": true,
    "n15-N256-finite-boundary": true,
    "n15-N256-state-modal": true,
    "n15-N256-adjoint-modal": true,
    "n15-N256-tangent-modal": true,
    "n15-N256-adjoint-tangent": true,
    "n15-N256-replay-state": true,
    "n15-N256-replay-gradient": true,
    "n15-N256-exact-work": true,
    "n15-time-ratio-64-128": true,
    "n15-time-ratio-128-256": true,
    "n15-N256-storage": true,
    "FD-direction0": true,
    "FD-direction1": true,
    "FD-direction2": true,
    "FD-all-finite": true,
    "qualified-cache": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/index.json

![Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.

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


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
