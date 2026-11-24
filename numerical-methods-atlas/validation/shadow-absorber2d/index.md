# 2D吸収影と保存的M1輸送

実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。

**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-algorithm)

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

- [静止媒質・平坦時空の灰色M1モーメント](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja) (`static-grey-m1`)

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。


**問題の図**

![2D吸収影と保存的M1輸送：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-validation)

独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。

- [円形吸収体の特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja) (`shadow-absorber2d`; 同じ問題の参照 · 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。
## 前提・単位・境界

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

**編集上の補足**

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

## 採用した計算法

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

## 比較・検証

独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。

## 確認の限界

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "M1_numerical_flux": "General directional localLF:max endpoint spectralradius,LFcone-splitting bound and absolute normal reducedflux;not a nonlinearRiemannfan bound",
    "completed_primary_and_control_runs": 8,
    "spatial_dimensions": 2,
    "angular_dimensions": 3,
    "Pzz_retained": true
  },
  "checks": {
    "shadow-sn-n24/all-stages-finite": true,
    "shadow-sn-n24/positive-energy": true,
    "shadow-sn-n24/realizability": true,
    "shadow-sn-n24/energy-budget": true,
    "shadow-sn-n24/full3D-pressure-trace": true,
    "shadow-sn-n24/five-fixed-snapshots": true,
    "shadow-sn-n48/all-stages-finite": true,
    "shadow-sn-n48/positive-energy": true,
    "shadow-sn-n48/realizability": true,
    "shadow-sn-n48/energy-budget": true,
    "shadow-sn-n48/full3D-pressure-trace": true,
    "shadow-sn-n48/five-fixed-snapshots": true,
    "shadow-sn-n96/all-stages-finite": true,
    "shadow-sn-n96/positive-energy": true,
    "shadow-sn-n96/realizability": true,
    "shadow-sn-n96/energy-budget": true,
    "shadow-sn-n96/full3D-pressure-trace": true,
    "shadow-sn-n96/five-fixed-snapshots": true,
    "shadow-m1-n24/all-stages-finite": true,
    "shadow-m1-n24/positive-energy": true,
    "shadow-m1-n24/realizability": true,
    "shadow-m1-n24/energy-budget": true,
    "shadow-m1-n24/full3D-pressure-trace": true,
    "shadow-m1-n24/five-fixed-snapshots": true,
    "shadow-m1-n48/all-stages-finite": true,
    "shadow-m1-n48/positive-energy": true,
    "shadow-m1-n48/realizability": true,
    "shadow-m1-n48/energy-budget": true,
    "shadow-m1-n48/full3D-pressure-trace": true,
    "shadow-m1-n48/five-fixed-snapshots": true,
    "shadow-m1-n96/all-stages-finite": true,
    "shadow-m1-n96/positive-energy": true,
    "shadow-m1-n96/realizability": true,
    "shadow-m1-n96/energy-budget": true,
    "shadow-m1-n96/full3D-pressure-trace": true,
    "shadow-m1-n96/five-fixed-snapshots": true,
    "shadow-sn-n96-half-dt/all-stages-finite": true,
    "shadow-sn-n96-half-dt/positive-energy": true,
    "shadow-sn-n96-half-dt/realizability": true,
    "shadow-sn-n96-half-dt/energy-budget": true,
    "shadow-sn-n96-half-dt/full3D-pressure-trace": true,
    "shadow-sn-n96-half-dt/five-fixed-snapshots": true,
    "shadow-m1-n96-half-dt/all-stages-finite": true,
    "shadow-m1-n96-half-dt/positive-energy": true,
    "shadow-m1-n96-half-dt/realizability": true,
    "shadow-m1-n96-half-dt/energy-budget": true,
    "shadow-m1-n96-half-dt/full3D-pressure-trace": true,
    "shadow-m1-n96-half-dt/five-fixed-snapshots": true,
    "shadow/sn/refinement-n48": true,
    "shadow/sn/refinement-n96": true,
    "shadow/sn/finest-reference": true,
    "shadow/sn/separate-time-sensitivity": true,
    "shadow/m1/refinement-n48": true,
    "shadow/m1/refinement-n96": true,
    "shadow/m1/finest-reference": true,
    "shadow/m1/separate-time-sensitivity": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/index.json

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

保存した実計算場の科学プレビュー。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Rosdahl etal. (2013). RAMSES-RT: Radiation hydrodynamics in the cosmological context [accessed 2026-11-24]. https://arxiv.org/html/1304.7126v2; review_level=primary-paper-selected-M1-equations-and-limitations
ReadSection2equations12-14and two-opposing-beams limitation text. Levermore1984original not read. Educational staticgrey cases/MMS here do not reproduce RAMSESastrophysical runs.

- M. A. Skinner and E. C. Ostriker (2013). A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method [accessed 2026-11-24]. https://arxiv.org/pdf/1306.0010; review_level=primary-selected-section-by-independent-mathematical-reviewer
Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Two-dimensional absorber shadow and M1 transport

Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-algorithm)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.


**Problem figure**

![Two-dimensional absorber shadow and M1 transport: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-validation)

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

- [Circular-absorber characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en) (`shadow-absorber2d`; Same-problem reference · Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
## Assumptions, units and boundaries

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

**Editorial clarification**

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

## Adopted numerical method

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

## References and validation

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

## Limits

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

## Stored measurements and decisions

```json
{
  "metrics": {
    "M1_numerical_flux": "General directional localLF:max endpoint spectralradius,LFcone-splitting bound and absolute normal reducedflux;not a nonlinearRiemannfan bound",
    "completed_primary_and_control_runs": 8,
    "spatial_dimensions": 2,
    "angular_dimensions": 3,
    "Pzz_retained": true
  },
  "checks": {
    "shadow-sn-n24/all-stages-finite": true,
    "shadow-sn-n24/positive-energy": true,
    "shadow-sn-n24/realizability": true,
    "shadow-sn-n24/energy-budget": true,
    "shadow-sn-n24/full3D-pressure-trace": true,
    "shadow-sn-n24/five-fixed-snapshots": true,
    "shadow-sn-n48/all-stages-finite": true,
    "shadow-sn-n48/positive-energy": true,
    "shadow-sn-n48/realizability": true,
    "shadow-sn-n48/energy-budget": true,
    "shadow-sn-n48/full3D-pressure-trace": true,
    "shadow-sn-n48/five-fixed-snapshots": true,
    "shadow-sn-n96/all-stages-finite": true,
    "shadow-sn-n96/positive-energy": true,
    "shadow-sn-n96/realizability": true,
    "shadow-sn-n96/energy-budget": true,
    "shadow-sn-n96/full3D-pressure-trace": true,
    "shadow-sn-n96/five-fixed-snapshots": true,
    "shadow-m1-n24/all-stages-finite": true,
    "shadow-m1-n24/positive-energy": true,
    "shadow-m1-n24/realizability": true,
    "shadow-m1-n24/energy-budget": true,
    "shadow-m1-n24/full3D-pressure-trace": true,
    "shadow-m1-n24/five-fixed-snapshots": true,
    "shadow-m1-n48/all-stages-finite": true,
    "shadow-m1-n48/positive-energy": true,
    "shadow-m1-n48/realizability": true,
    "shadow-m1-n48/energy-budget": true,
    "shadow-m1-n48/full3D-pressure-trace": true,
    "shadow-m1-n48/five-fixed-snapshots": true,
    "shadow-m1-n96/all-stages-finite": true,
    "shadow-m1-n96/positive-energy": true,
    "shadow-m1-n96/realizability": true,
    "shadow-m1-n96/energy-budget": true,
    "shadow-m1-n96/full3D-pressure-trace": true,
    "shadow-m1-n96/five-fixed-snapshots": true,
    "shadow-sn-n96-half-dt/all-stages-finite": true,
    "shadow-sn-n96-half-dt/positive-energy": true,
    "shadow-sn-n96-half-dt/realizability": true,
    "shadow-sn-n96-half-dt/energy-budget": true,
    "shadow-sn-n96-half-dt/full3D-pressure-trace": true,
    "shadow-sn-n96-half-dt/five-fixed-snapshots": true,
    "shadow-m1-n96-half-dt/all-stages-finite": true,
    "shadow-m1-n96-half-dt/positive-energy": true,
    "shadow-m1-n96-half-dt/realizability": true,
    "shadow-m1-n96-half-dt/energy-budget": true,
    "shadow-m1-n96-half-dt/full3D-pressure-trace": true,
    "shadow-m1-n96-half-dt/five-fixed-snapshots": true,
    "shadow/sn/refinement-n48": true,
    "shadow/sn/refinement-n96": true,
    "shadow/sn/finest-reference": true,
    "shadow/sn/separate-time-sensitivity": true,
    "shadow/m1/refinement-n48": true,
    "shadow/m1/refinement-n96": true,
    "shadow/m1/finest-reference": true,
    "shadow/m1/separate-time-sensitivity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

Scientific preview from the actual saved numerical fields.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Rosdahl etal. (2013). RAMSES-RT: Radiation hydrodynamics in the cosmological context [accessed 2026-11-24]. https://arxiv.org/html/1304.7126v2; review_level=primary-paper-selected-M1-equations-and-limitations
ReadSection2equations12-14and two-opposing-beams limitation text. Levermore1984original not read. Educational staticgrey cases/MMS here do not reproduce RAMSESastrophysical runs.

- M. A. Skinner and E. C. Ostriker (2013). A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method [accessed 2026-11-24]. https://arxiv.org/pdf/1306.0010; review_level=primary-selected-section-by-independent-mathematical-reviewer
Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
