# 振り子の指数低減・拘束ドリフト・明示安定化

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

**使用手法**

- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) (`dae`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-algorithm)

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

- [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja) (`constrained-pendulum`)

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。


**問題の図**

![振り子の指数低減・拘束ドリフト・明示安定化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-validation)

Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja) (`high-index-pendulum`; 同じ問題の参照 · 半解析参照)

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja) (`shake-rattle-pendulum`; 同じ問題の参照 · 半解析参照)

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
## 前提・単位・境界

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。

**編集上の補足**

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

## 比較・検証

Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。

## 確認の限界

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "pendulum-consistent-underlying-2000:state": 1.6288695170452172e-08,
    "pendulum-consistent-underlying-2000:energy": 1.1849681791353817e-08,
    "pendulum-consistent-stabilized-2000:state": 2.182399358452436e-09,
    "pendulum-consistent-stabilized-2000:energy": 1.2245648939313014e-10,
    "pendulum-radial-underlying-2000:C-law": 1.0557027235041927e-08,
    "pendulum-radial-underlying-2000:D-law": 1.037474827401963e-09,
    "pendulum-radial-underlying-2000:work-ledger": 4.06214124837323e-11,
    "pendulum-radial-stabilized-2000:C-law": 1.058986416895176e-10,
    "pendulum-radial-stabilized-2000:D-law": 1.113360997362714e-10,
    "pendulum-radial-stabilized-2000:work-ledger": 1.2632772794691789e-09,
    "underlying-consistent-fourth-order": [
      3.997663875510909,
      3.999093883138539
    ],
    "visible-unstabilized-drift": 0.019999989442972765,
    "stabilized-drift-ratio": 8.89400134498285e-10,
    "finest_consistent_state_error": 1.6288695170452172e-08,
    "observed_orders": [
      3.997663875510909,
      3.999093883138539
    ],
    "stabilized_to_unstabilized_drift_ratio": 8.89400134498285e-10,
    "reference_solver_counters": [
      {
        "id": "angular-reference-0",
        "method": "DOP853",
        "nfev": 1373,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      },
      {
        "id": "angular-reference-1",
        "method": "DOP853",
        "nfev": 2273,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      }
    ],
    "original_targets_met": 45,
    "original_targets_total": 45
  },
  "checks": {
    "reference:Jacobi-angular-agreement": true,
    "reference:angular-tolerance-agreement": true,
    "reference:Jacobi-initial": true,
    "reference:Jacobi-invariants": true,
    "reference:AGM-K": true,
    "reference:Decimal-remainder-qualification": true,
    "reference:constraint-identity-False": true,
    "reference:constraint-work-False": true,
    "reference:constraint-identity-True": true,
    "reference:constraint-work-True": true,
    "default-consistency-rejection": true,
    "pendulum-consistent-underlying-500:finite": true,
    "pendulum-consistent-underlying-500:radius": true,
    "pendulum-consistent-underlying-1000:finite": true,
    "pendulum-consistent-underlying-1000:radius": true,
    "pendulum-consistent-underlying-2000:finite": true,
    "pendulum-consistent-underlying-2000:radius": true,
    "pendulum-consistent-underlying-2000:state": true,
    "pendulum-consistent-underlying-2000:energy": true,
    "pendulum-consistent-stabilized-2000:finite": true,
    "pendulum-consistent-stabilized-2000:radius": true,
    "pendulum-consistent-stabilized-2000:state": true,
    "pendulum-consistent-stabilized-2000:energy": true,
    "pendulum-radial-underlying-500:finite": true,
    "pendulum-radial-underlying-500:radius": true,
    "pendulum-radial-underlying-1000:finite": true,
    "pendulum-radial-underlying-1000:radius": true,
    "pendulum-radial-underlying-2000:finite": true,
    "pendulum-radial-underlying-2000:radius": true,
    "pendulum-radial-underlying-2000:C-law": true,
    "pendulum-radial-underlying-2000:D-law": true,
    "pendulum-radial-underlying-2000:work-ledger": true,
    "pendulum-radial-stabilized-500:finite": true,
    "pendulum-radial-stabilized-500:radius": true,
    "pendulum-radial-stabilized-1000:finite": true,
    "pendulum-radial-stabilized-1000:radius": true,
    "pendulum-radial-stabilized-2000:finite": true,
    "pendulum-radial-stabilized-2000:radius": true,
    "pendulum-radial-stabilized-2000:C-law": true,
    "pendulum-radial-stabilized-2000:D-law": true,
    "pendulum-radial-stabilized-2000:work-ledger": true,
    "underlying-consistent-fourth-order": true,
    "visible-unstabilized-drift": true,
    "stabilized-drift-ratio": true,
    "eleven-record-identities": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/index.json

![位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。

![保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-diagnostics.png)

保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- NIST DLMF section22.19(i), pendulum [accessed 2026-11-24]. https://dlmf.nist.gov/22.19; review_level=official-reference-selected-equations
Selected pendulum formulas, phase and modulus convention. Authored Cartesian conversion uses K-t; SciPy takes parameter m=k². No full chapter reading claimed.

- NIST DLMF section19.8(i), arithmetic-geometric mean [accessed 2026-11-24]. https://dlmf.nist.gov/19.8; review_level=official-reference-selected-equations
Selected AGM/K identity; independent Decimal Machin pi and sine with explicit finite remainders qualify a single fixed modulus.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Index reduction, constraint drift and explicit stabilization for a pendulum

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

**Methods used**

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) (`dae`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-algorithm)

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages.

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

- [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en) (`constrained-pendulum`)

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.


**Problem figure**

![Index reduction, constraint drift and explicit stabilization for a pendulum: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-validation)

Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets.

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en) (`high-index-pendulum`; Same-problem reference · Semi-analytic reference)

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en) (`shake-rattle-pendulum`; Same-problem reference · Semi-analytic reference)

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
## Assumptions, units and boundaries

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.

**Editorial clarification**

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages.

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

## References and validation

Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets.

## Limits

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

## Stored measurements and decisions

```json
{
  "metrics": {
    "pendulum-consistent-underlying-2000:state": 1.6288695170452172e-08,
    "pendulum-consistent-underlying-2000:energy": 1.1849681791353817e-08,
    "pendulum-consistent-stabilized-2000:state": 2.182399358452436e-09,
    "pendulum-consistent-stabilized-2000:energy": 1.2245648939313014e-10,
    "pendulum-radial-underlying-2000:C-law": 1.0557027235041927e-08,
    "pendulum-radial-underlying-2000:D-law": 1.037474827401963e-09,
    "pendulum-radial-underlying-2000:work-ledger": 4.06214124837323e-11,
    "pendulum-radial-stabilized-2000:C-law": 1.058986416895176e-10,
    "pendulum-radial-stabilized-2000:D-law": 1.113360997362714e-10,
    "pendulum-radial-stabilized-2000:work-ledger": 1.2632772794691789e-09,
    "underlying-consistent-fourth-order": [
      3.997663875510909,
      3.999093883138539
    ],
    "visible-unstabilized-drift": 0.019999989442972765,
    "stabilized-drift-ratio": 8.89400134498285e-10,
    "finest_consistent_state_error": 1.6288695170452172e-08,
    "observed_orders": [
      3.997663875510909,
      3.999093883138539
    ],
    "stabilized_to_unstabilized_drift_ratio": 8.89400134498285e-10,
    "reference_solver_counters": [
      {
        "id": "angular-reference-0",
        "method": "DOP853",
        "nfev": 1373,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      },
      {
        "id": "angular-reference-1",
        "method": "DOP853",
        "nfev": 2273,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      }
    ],
    "original_targets_met": 45,
    "original_targets_total": 45
  },
  "checks": {
    "reference:Jacobi-angular-agreement": true,
    "reference:angular-tolerance-agreement": true,
    "reference:Jacobi-initial": true,
    "reference:Jacobi-invariants": true,
    "reference:AGM-K": true,
    "reference:Decimal-remainder-qualification": true,
    "reference:constraint-identity-False": true,
    "reference:constraint-work-False": true,
    "reference:constraint-identity-True": true,
    "reference:constraint-work-True": true,
    "default-consistency-rejection": true,
    "pendulum-consistent-underlying-500:finite": true,
    "pendulum-consistent-underlying-500:radius": true,
    "pendulum-consistent-underlying-1000:finite": true,
    "pendulum-consistent-underlying-1000:radius": true,
    "pendulum-consistent-underlying-2000:finite": true,
    "pendulum-consistent-underlying-2000:radius": true,
    "pendulum-consistent-underlying-2000:state": true,
    "pendulum-consistent-underlying-2000:energy": true,
    "pendulum-consistent-stabilized-2000:finite": true,
    "pendulum-consistent-stabilized-2000:radius": true,
    "pendulum-consistent-stabilized-2000:state": true,
    "pendulum-consistent-stabilized-2000:energy": true,
    "pendulum-radial-underlying-500:finite": true,
    "pendulum-radial-underlying-500:radius": true,
    "pendulum-radial-underlying-1000:finite": true,
    "pendulum-radial-underlying-1000:radius": true,
    "pendulum-radial-underlying-2000:finite": true,
    "pendulum-radial-underlying-2000:radius": true,
    "pendulum-radial-underlying-2000:C-law": true,
    "pendulum-radial-underlying-2000:D-law": true,
    "pendulum-radial-underlying-2000:work-ledger": true,
    "pendulum-radial-stabilized-500:finite": true,
    "pendulum-radial-stabilized-500:radius": true,
    "pendulum-radial-stabilized-1000:finite": true,
    "pendulum-radial-stabilized-1000:radius": true,
    "pendulum-radial-stabilized-2000:finite": true,
    "pendulum-radial-stabilized-2000:radius": true,
    "pendulum-radial-stabilized-2000:C-law": true,
    "pendulum-radial-stabilized-2000:D-law": true,
    "pendulum-radial-stabilized-2000:work-ledger": true,
    "underlying-consistent-fourth-order": true,
    "visible-unstabilized-drift": true,
    "stabilized-drift-ratio": true,
    "eleven-record-identities": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/index.json

![Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays.

![Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-diagnostics.png)

Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- NIST DLMF section22.19(i), pendulum [accessed 2026-11-24]. https://dlmf.nist.gov/22.19; review_level=official-reference-selected-equations
Selected pendulum formulas, phase and modulus convention. Authored Cartesian conversion uses K-t; SciPy takes parameter m=k². No full chapter reading claimed.

- NIST DLMF section19.8(i), arithmetic-geometric mean [accessed 2026-11-24]. https://dlmf.nist.gov/19.8; review_level=official-reference-selected-equations
Selected AGM/K identity; independent Decimal Machin pi and sine with explicit finite remainders qualify a single fixed modulus.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
