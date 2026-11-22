# Periodic sine advection: upwind and analytic transport / 周期正弦波の線形移流：風上法と解析解

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: advection-sine

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-h2.json

## ja

周期正弦波の輸送を解析的な平行移動と比べ、格子細分化・平均値保存・最大値原理を確認する。

### scope

長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

### assumptions

一定速度a=1、平均1、振幅0.2、基本モード。既存difference_stepを前進Eulerで呼び、実際の|C|≤0.5になる等間隔時間刻みを使う。入力で速度・正弦波・区間・格子を指定できるが、非ゼロ速度、正振幅、十分なモード解像とCFL条件を検査する。

### units

x・時間・移流量qは無次元。速度は区間長/時間、Courant数は無次元。

### boundaries

np.rollによる周期境界。平均値保存と初期標本の値域を超えないことを別々に検査する。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/advection-sine.json
Input SHA-256: c2f31548c6df3db8cb6a5e3eb14e0b1130738e8144d6757a2a44c9cdaa356ccc
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/advection-sine.json --output output-advection-sine
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/solution.csv

CSVは128点の格子中心に1行ずつ配置し、同じ時刻・位置で解析値を評価する。平均の保存と最大値原理には丸め誤差許容値10^-12を用いる。

### Numerical acceptance

- analytic-error / 解析移流解に対する平均絶対誤差が0.02以下（振幅0.2の10%）。: /metrics/density_l1_error_fine; value ≤ 0.02
- refinement / 格子倍増で解析解誤差が減る（1次風上法の実測比較、形式次数の証明ではない）。: /metrics/fine_to_coarse_error_ratio; value ≤ 0.65
- periodic-conservation / 周期境界の平均値を丸め誤差の範囲で保存する。: /metrics/mean_conservation_error; value ≤ 1e-12
- maximum-principle / CFL制限内で初期標本の値域を超えない。: /metrics/maximum_principle_excess; value ≤ 1e-12
- stable-courant / 実際のCourant数の絶対値が1以下。: /metrics/courant_abs; value ≤ 1
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = c2f31548c6df3db8cb6a5e3eb14e0b1130738e8144d6757a2a44c9cdaa356ccc
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

この滑らかな一定速度・周期問題だけの判定。0.02のL1基準は振幅0.2の10%であり、1次法の拡散を許容する。格子倍増の誤差比は実測指標で、一般の次数・非周期境界・非線形保存則の保証ではない。無効な入力や判定不合格は失敗として返す。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/

### References

- CSVは128点の格子中心に1行ずつ配置し、同じ時刻・位置で解析値を評価する。平均の保存と最大値原理には丸め誤差許容値10^-12を用いる。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json
- 風上差分の歴史的な一次文献。解析参照はq(x,t)=q(x−at,0)を直接評価し、論文図や保存済み出力には依存しない。: https://doi.org/10.1002/cpa.3160050303

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare periodic sine transport with analytic translation; check refinement, mean conservation and the maximum principle.

### scope

Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

### assumptions

Constant speed a=1, mean 1, amplitude 0.2 and the fundamental mode. Existing difference_step is called with forward Euler and equal time steps with actual |C|≤0.5. Inputs expose the speed, sine, interval and grids, with nonzero speed, positive amplitude, mode resolution and CFL checks.

### units

x, time and transported scalar q are nondimensional; speed is interval length/time and the Courant number is dimensionless.

### boundaries

Periodic boundaries via np.roll. Mean conservation and preservation of the initial sampled range are checked separately.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/advection-sine.json
Input SHA-256: c2f31548c6df3db8cb6a5e3eb14e0b1130738e8144d6757a2a44c9cdaa356ccc
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/advection-sine.json --output output-advection-sine
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/solution.csv

CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.

### Numerical acceptance

- analytic-error / Mean absolute error against analytic transport is at most 0.02 (10% of the 0.2 amplitude).: /metrics/density_l1_error_fine; value ≤ 0.02
- refinement / Doubling the grid reduces analytic-reference error (an observed comparison for first-order upwind, not a formal-order proof).: /metrics/fine_to_coarse_error_ratio; value ≤ 0.65
- periodic-conservation / The periodic mean is conserved to rounding accuracy.: /metrics/mean_conservation_error; value ≤ 1e-12
- maximum-principle / The update remains inside the initial sampled range under the CFL restriction.: /metrics/maximum_principle_excess; value ≤ 1e-12
- stable-courant / The actual absolute Courant number is at most one.: /metrics/courant_abs; value ≤ 1
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = c2f31548c6df3db8cb6a5e3eb14e0b1130738e8144d6757a2a44c9cdaa356ccc
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Acceptance is limited to this smooth constant-speed periodic problem. The 0.02 L1 threshold is 10% of the 0.2 amplitude and permits first-order diffusion. The grid-doubling ratio is empirical, not a general order, nonperiodic-boundary or nonlinear-conservation-law guarantee. Invalid inputs and failed acceptance are reported as failures.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/

### References

- CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json
- Historical primary source for upstream differencing. The reference directly evaluates q(x,t)=q(x−at,0), independent of paper figures or saved outputs.: https://doi.org/10.1002/cpa.3160050303

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
