# Periodic Taylor–Green vortex: velocity, decay and divergence / 周期Taylor–Green渦：速度・散逸・発散

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: taylor-green

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-h2.json

## ja

周期渦の速度と粘性エネルギー減衰を解析解と比べ、離散発散・圧力ゲージ・格子と時間刻みへの依存を確認する。

### scope

既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

### assumptions

単位密度、[0,2π)²、ν=0.1、T=0.5。u₀=sin x cos y、v₀=−cos x sin y。既存ソルバーの移流・拡散安定性に基づくCFL=0.2、時間感度検査は0.1。

### units

無次元。速度振幅1、座標周期2π、粘性νの次元は長さ²/時間。圧力は単位密度での比圧力。平均運動エネルギーは〈u²+v²〉/2。

### boundaries

2方向周期、圧力平均0。u・vは異なるMAC面、圧力はセル中心。Poissonは連続k²ではなく離散DG記号を逆演算。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/taylor-green.json
Input SHA-256: b7c4a6d25801bce445bf047d0df4e8f3083b71b15bcf32f7ba171f5e364e764d
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/taylor-green.json --output output-taylor-green
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/solution.csv

CSVは(i,j)をC順に並べ、u面・v面・圧力中心それぞれの座標、数値解と解析解を別列に保存。MAC速度を同じ位置の成分と誤解しない。JSONにエネルギー履歴と時間感度を保存。

### Numerical acceptance

- analytic-velocity / 細格子の速度を各MAC座標で解析解と比較。: /metrics/velocity_rms_error; value ≤ 0.0001
- combined-refinement / 空間・安定時間刻みを共に細分化した速度の観測次数。: /metrics/minimum_observed_order; value ≥ 1.9
- divergence / 全時間履歴で離散発散を確認。: /metrics/maximum_divergence; value ≤ 1e-12
- pressure-gauge / 圧力平均0の規約。: /metrics/pressure_mean_absolute; value ≤ 1e-12
- energy / 解析的平均運動エネルギーの減衰と比較。: /metrics/relative_final_energy_error; value ≤ 0.001
- energy-monotonicity / 粘性系での時間履歴の運動エネルギー増加を検出。: /metrics/maximum_energy_increase; value ≤ 1e-13
- time-sensitivity / 同じ細格子でCFLを半分にした変化が元の解析解誤差の10%以下。誤差上界ではない。: /metrics/time_change_to_combined_error_ratio; value ≤ 0.1
- final-time / 指定した終端時刻に到達。: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = b7c4a6d25801bce445bf047d0df4e8f3083b71b15bcf32f7ba171f5e364e764d
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

非正粘性・終端時刻、CFL範囲外、倍増でない格子を拒否。安定時間刻みも変わる格子細分化は空間のみの次数証明ではない。固定格子のCFL半減は時間感度であり厳密誤差上界ではない。壁境界・乱流・任意Reynolds数への検証ではない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/

### References

- CSVは(i,j)をC順に並べ、u面・v面・圧力中心それぞれの座標、数値解と解析解を別列に保存。MAC速度を同じ位置の成分と誤解しない。JSONにエネルギー履歴と時間感度を保存。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json
- u=sin x cos y e^(−2νt)、v=−cos x sin y e^(−2νt)、p=(cos2x+cos2y)e^(−4νt)/4。平均運動エネルギーはe^(−4νt)/4。: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/
- 既存投影法項目のChorin文献。今回のMAC配置とSSPRK2の具体形は公開実装に固定。: https://doi.org/10.1090/S0025-5718-1968-0242392-2

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare periodic-vortex velocity and viscous energy decay with analytic references; inspect discrete divergence, pressure gauge and space/time sensitivity.

### scope

Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

### assumptions

Unit density, [0,2*pi)², nu=0.1 and T=0.5. u0=sin(x)cos(y), v0=-cos(x)sin(y). CFL=0.2 uses the solver's combined advection/diffusion stability estimate; temporal sensitivity uses 0.1.

### units

Nondimensional velocity amplitude one and coordinate period 2*pi; viscosity has length²/time units. Pressure is kinematic pressure at unit density. Mean kinetic energy is <u²+v²>/2.

### boundaries

Periodic in both axes, zero-mean pressure. u/v occupy different MAC faces and pressure cell centers. Poisson inverts the discrete DG symbol, not continuum k².

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/taylor-green.json
Input SHA-256: b7c4a6d25801bce445bf047d0df4e8f3083b71b15bcf32f7ba171f5e364e764d
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/taylor-green.json --output output-taylor-green
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/solution.csv

CSV uses C-order (i,j) rows with separate coordinates and numerical/analytic values for u faces, v faces and pressure centers; the components are not collocated. JSON includes energy histories and temporal sensitivity.

### Numerical acceptance

- analytic-velocity / Compare finest-grid velocity with the analytic solution at its MAC locations.: /metrics/velocity_rms_error; value ≤ 0.0001
- combined-refinement / Observed velocity order under combined spatial/stable-time-step refinement.: /metrics/minimum_observed_order; value ≥ 1.9
- divergence / Check discrete divergence over the whole time history.: /metrics/maximum_divergence; value ≤ 1e-12
- pressure-gauge / Zero-mean pressure gauge.: /metrics/pressure_mean_absolute; value ≤ 1e-12
- energy / Compare with analytic mean kinetic-energy decay.: /metrics/relative_final_energy_error; value ≤ 0.001
- energy-monotonicity / Detect kinetic-energy increases in the viscous time history.: /metrics/maximum_energy_increase; value ≤ 1e-13
- time-sensitivity / At fixed finest grid, halving CFL changes velocity by at most 10% of the original analytic error; not an error bound.: /metrics/time_change_to_combined_error_ratio; value ≤ 0.1
- final-time / Reach the specified final time.: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = b7c4a6d25801bce445bf047d0df4e8f3083b71b15bcf32f7ba171f5e364e764d
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Reject nonpositive viscosity/final time, invalid CFL and nondoubling grids. Grid refinement also changes the stable time step and is not a pure spatial-order proof. Fixed-grid CFL reduction measures sensitivity, not a rigorous error bound. No validation of walls, turbulence or arbitrary Reynolds number.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/

### References

- CSV uses C-order (i,j) rows with separate coordinates and numerical/analytic values for u faces, v faces and pressure centers; the components are not collocated. JSON includes energy histories and temporal sensitivity.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json
- u=sin(x)cos(y)e^(-2nu*t), v=-cos(x)sin(y)e^(-2nu*t), p=(cos(2x)+cos(2y))e^(-4nu*t)/4; mean kinetic energy e^(-4nu*t)/4.: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/
- Chorin reference already cited by the projection-method record; MAC placement and SSPRK2 details are fixed by the released implementation.: https://doi.org/10.1090/S0025-5718-1968-0242392-2

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
