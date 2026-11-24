# RK45の埋込み推定・補間・イベント

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。

**使用手法**

- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-algorithm)

実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

- [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja) (`linear-evolution-system`)

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。


**問題の図**

![RK45の埋込み推定・補間・イベント：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja) (`rk45-dense-events`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-validation)

解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。

- [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rk45-dense-events-ja) (`rk45-dense-events`; 同じ問題の参照 · 解析参照)

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。
## 前提・単位・境界

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。

**編集上の補足**

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

## 比較・検証

解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。

## 確認の限界

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_dense_error": 6.136827199998418e-05,
    "maximum_event_time_error": 1.4618863214188593e-05,
    "actual_RHS_evaluations": 2162,
    "rejected_trials": 40,
    "scope": "Analytic state/simple crossings; accepted-full endpoint versus terminal dense-root state distinct. No global guarantee inferred from localtol."
  },
  "checks": {
    "rk45-loose-hmax0.4:completion-and-work": true,
    "rk45-loose-hmax0.4:endpoint-error": true,
    "rk45-loose-hmax0.4:offmesh-error": true,
    "rk45-loose-hmax0.4:event-time-and-set": true,
    "rk45-loose-hmax0.4:event-residual": true,
    "rk45-loose-hmax0.1:completion-and-work": true,
    "rk45-loose-hmax0.1:endpoint-error": true,
    "rk45-loose-hmax0.1:offmesh-error": true,
    "rk45-loose-hmax0.1:event-time-and-set": true,
    "rk45-loose-hmax0.1:event-residual": true,
    "rk45-medium-hmax0.4:completion-and-work": true,
    "rk45-medium-hmax0.4:endpoint-error": true,
    "rk45-medium-hmax0.4:offmesh-error": true,
    "rk45-medium-hmax0.4:event-time-and-set": true,
    "rk45-medium-hmax0.4:event-residual": true,
    "rk45-medium-hmax0.1:completion-and-work": true,
    "rk45-medium-hmax0.1:endpoint-error": true,
    "rk45-medium-hmax0.1:offmesh-error": true,
    "rk45-medium-hmax0.1:event-time-and-set": true,
    "rk45-medium-hmax0.1:event-residual": true,
    "rk45-tight-hmax0.4:completion-and-work": true,
    "rk45-tight-hmax0.4:endpoint-error": true,
    "rk45-tight-hmax0.4:offmesh-error": true,
    "rk45-tight-hmax0.4:event-time-and-set": true,
    "rk45-tight-hmax0.4:event-residual": true,
    "rk45-tight-hmax0.1:completion-and-work": true,
    "rk45-tight-hmax0.1:endpoint-error": true,
    "rk45-tight-hmax0.1:offmesh-error": true,
    "rk45-tight-hmax0.1:event-time-and-set": true,
    "rk45-tight-hmax0.1:event-residual": true,
    "rk45-terminal-direction-1:completion-and-work": true,
    "rk45-terminal-direction-1:endpoint-error": true,
    "rk45-terminal-direction-1:offmesh-error": true,
    "rk45-terminal-direction-1:event-time-and-set": true,
    "rk45-terminal-direction-1:event-residual": true,
    "rk45-terminal-direction1:completion-and-work": true,
    "rk45-terminal-direction1:endpoint-error": true,
    "rk45-terminal-direction1:offmesh-error": true,
    "rk45-terminal-direction1:event-time-and-set": true,
    "rk45-terminal-direction1:event-residual": true,
    "hmax0.4:actual-tolerance-response": true,
    "hmax0.1:actual-tolerance-response": true,
    "rejected-trial-actually-exercised": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/index.json

![減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- SciPy1.14.1 RK45 coefficient and dense-output source [accessed 2026-11-24]. https://github.com/scipy/scipy/blob/v1.14.1/scipy/integrate/_ivp/rk.py; review_level=official-release-source-selected-functions
C/A/B/E/P、段階・受理/棄却時FSAL更新、quartic補間を確認。原Dormand–Prince1980/Shampine1986論文は書誌参照のみで全文未読。係数由来のBSD通知を同梱。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# RK45: embedded errors, dense output and events

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.

**Methods used**

- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-algorithm)

Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

- [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en) (`linear-evolution-system`)

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.


**Problem figure**

![RK45: embedded errors, dense output and events: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en) (`rk45-dense-events`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-validation)

Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.

- [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rk45-dense-events-en) (`rk45-dense-events`; Same-problem reference · Analytic reference)

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.
## Assumptions, units and boundaries

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.

**Editorial clarification**

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

## References and validation

Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.

## Limits

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_dense_error": 6.136827199998418e-05,
    "maximum_event_time_error": 1.4618863214188593e-05,
    "actual_RHS_evaluations": 2162,
    "rejected_trials": 40,
    "scope": "Analytic state/simple crossings; accepted-full endpoint versus terminal dense-root state distinct. No global guarantee inferred from localtol."
  },
  "checks": {
    "rk45-loose-hmax0.4:completion-and-work": true,
    "rk45-loose-hmax0.4:endpoint-error": true,
    "rk45-loose-hmax0.4:offmesh-error": true,
    "rk45-loose-hmax0.4:event-time-and-set": true,
    "rk45-loose-hmax0.4:event-residual": true,
    "rk45-loose-hmax0.1:completion-and-work": true,
    "rk45-loose-hmax0.1:endpoint-error": true,
    "rk45-loose-hmax0.1:offmesh-error": true,
    "rk45-loose-hmax0.1:event-time-and-set": true,
    "rk45-loose-hmax0.1:event-residual": true,
    "rk45-medium-hmax0.4:completion-and-work": true,
    "rk45-medium-hmax0.4:endpoint-error": true,
    "rk45-medium-hmax0.4:offmesh-error": true,
    "rk45-medium-hmax0.4:event-time-and-set": true,
    "rk45-medium-hmax0.4:event-residual": true,
    "rk45-medium-hmax0.1:completion-and-work": true,
    "rk45-medium-hmax0.1:endpoint-error": true,
    "rk45-medium-hmax0.1:offmesh-error": true,
    "rk45-medium-hmax0.1:event-time-and-set": true,
    "rk45-medium-hmax0.1:event-residual": true,
    "rk45-tight-hmax0.4:completion-and-work": true,
    "rk45-tight-hmax0.4:endpoint-error": true,
    "rk45-tight-hmax0.4:offmesh-error": true,
    "rk45-tight-hmax0.4:event-time-and-set": true,
    "rk45-tight-hmax0.4:event-residual": true,
    "rk45-tight-hmax0.1:completion-and-work": true,
    "rk45-tight-hmax0.1:endpoint-error": true,
    "rk45-tight-hmax0.1:offmesh-error": true,
    "rk45-tight-hmax0.1:event-time-and-set": true,
    "rk45-tight-hmax0.1:event-residual": true,
    "rk45-terminal-direction-1:completion-and-work": true,
    "rk45-terminal-direction-1:endpoint-error": true,
    "rk45-terminal-direction-1:offmesh-error": true,
    "rk45-terminal-direction-1:event-time-and-set": true,
    "rk45-terminal-direction-1:event-residual": true,
    "rk45-terminal-direction1:completion-and-work": true,
    "rk45-terminal-direction1:endpoint-error": true,
    "rk45-terminal-direction1:offmesh-error": true,
    "rk45-terminal-direction1:event-time-and-set": true,
    "rk45-terminal-direction1:event-residual": true,
    "hmax0.4:actual-tolerance-response": true,
    "hmax0.1:actual-tolerance-response": true,
    "rejected-trial-actually-exercised": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/index.json

![Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- SciPy1.14.1 RK45 coefficient and dense-output source [accessed 2026-11-24]. https://github.com/scipy/scipy/blob/v1.14.1/scipy/integrate/_ivp/rk.py; review_level=official-release-source-selected-functions
Read C, A, B, E, P, stage evaluation, accepted/rejected FSAL updates and quartic evaluation. The original Dormand–Prince 1980 and Shampine 1986 papers remain unread beyond bibliography. The adapted coefficient BSD notice is retained.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
