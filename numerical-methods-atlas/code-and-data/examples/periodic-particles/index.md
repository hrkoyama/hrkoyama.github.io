# Periodic PM particles: mass, internal force and mesh field / 周期PM粒子群：質量・内力・格子場

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: periodic-particles

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json

## ja

固定19粒子のCIC質量・自己力・内力和・周期折返しを調べ、別の正弦密度で格子ポテンシャルと加速度を解析検証する。

### scope

入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。

### assumptions

3次元立方周期箱L=1、G=1、24³格子、正の質量で総和1。座標・質量は全値を入力に保存し、実行時の乱数生成はない。連続k²のFFT逆演算と同じCIC配置・補間を用いる。

### units

基準長L=1、総質量M=1、G=1。密度はM/L³、ポテンシャルはGM/L、加速度はGM/L²、力はGM²/L²。

### boundaries

3方向周期。∇²φ=4πG(ρ−〈ρ〉)、φ̂(0)=0。偶数格子の各微分軸のNyquist成分を0にする既存実装。孤立境界の直接和とは異なる。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json
Input SHA-256: 9b44288285eb833f8132411dc681ebee4272ff1f6ee041c2a5a35004645c8b9b
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/periodic-particles.json --output output-periodic-particles
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/solution.csv

CSVは粒子ごとの座標・質量・加速度・力。正弦密度の独立解析場検査はJSONの集計値に保存。PM格子細分化を粒子力の解析誤差として誤表示しない。

### Numerical acceptance

- mass / CIC格子へ沈着した総質量。: /metrics/mass_relative_error; value ≤ 1e-13
- internal-force / 質量重み付き内力和を力の大きさの総和で規格化。粒子力の精度とは別。: /metrics/internal_net_force_relative; value ≤ 1e-12
- self-force / 同じCIC配置・補間を使う単粒子の自己加速度。: /metrics/single_particle_self_acceleration; value ≤ 1e-12
- periodic-wrap-force / 整数箱長の移動で粒子加速度が不変。: /metrics/periodic_shift_acceleration_max_error; value ≤ 1e-11
- periodic-wrap-density / 整数箱長移動による沈着密度の相対差。: /metrics/periodic_shift_density_relative_error; value ≤ 1e-12
- gauge / 周期ポテンシャルの平均0の規約。: /metrics/potential_mean_absolute; value ≤ 1e-12
- analytic-mesh-potential / 別に与えた正弦密度の解析的格子ポテンシャルと比較。: /metrics/manufactured_potential_max_error; value ≤ 1e-12
- analytic-mesh-force / 同じ正弦密度の解析的格子加速度と比較。: /metrics/manufactured_acceleration_max_error; value ≤ 1e-12
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = 9b44288285eb833f8132411dc681ebee4272ff1f6ee041c2a5a35004645c8b9b
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

非正質量、非有限入力、G≠1、不適切な格子・正弦モード、非整数箱長移動を拒否。質量・内力和・自己力の一致だけでは個々の粒子力の精度を保証しない。周期直接和、短距離補正、Ewald・P3M・PME・SPME、粒子時間発展は実装しない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/

### References

- CSVは粒子ごとの座標・質量・加速度・力。正弦密度の独立解析場検査はJSONの集計値に保存。PM格子細分化を粒子力の解析誤差として誤表示しない。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json
- 別入力密度ρ=ρ₀+A cos(kx)に対するφ=−4πGA cos(kx)/k²、a_x=−4πGA sin(kx)/k。粒子群の厳密な周期力参照ではない。: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- 既存PM項目の文献。今回のCIC–FFT方式・境界・検査範囲は入力と実装に明示。: https://doi.org/10.1016/0021-9991(74)90044-8

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Inspect CIC mass, self-force, net internal force and wrapping for 19 fixed particles; separately check mesh potential/acceleration for a sinusoidal density.

### scope

Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.

### assumptions

Three-dimensional periodic cube L=1, G=1, 24³ mesh and positive masses summing to one. All positions/masses are stored explicitly; no runtime random generation. Continuum-k² FFT inversion with matched CIC assignment/interpolation.

### units

Reference length L=1, mass M=1 and G=1. Density: M/L³; potential: GM/L; acceleration: GM/L²; force: GM²/L².

### boundaries

Periodic in all three axes: Laplacian(phi)=4*pi*G*(rho-mean(rho)), phi_hat(0)=0. Existing implementation zeros the unpaired Nyquist derivative mode along each even-grid axis. This differs from isolated direct-sum boundaries.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json
Input SHA-256: 9b44288285eb833f8132411dc681ebee4272ff1f6ee041c2a5a35004645c8b9b
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/periodic-particles.json --output output-periodic-particles
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/solution.csv

CSV stores each particle's coordinates, mass, acceleration and force. Independent sinusoidal-field diagnostics are JSON metrics. No mesh refinement is misrepresented as analytic particle-force error.

### Numerical acceptance

- mass / Total mass deposited onto the CIC mesh.: /metrics/mass_relative_error; value ≤ 1e-13
- internal-force / Normalize net internal force by the sum of force magnitudes; separate from particle-force accuracy.: /metrics/internal_net_force_relative; value ≤ 1e-12
- self-force / Single-particle self-acceleration with matched CIC assignment/interpolation.: /metrics/single_particle_self_acceleration; value ≤ 1e-12
- periodic-wrap-force / Acceleration is invariant under integer-box translations.: /metrics/periodic_shift_acceleration_max_error; value ≤ 1e-11
- periodic-wrap-density / Relative deposited-density difference under integer-box translations.: /metrics/periodic_shift_density_relative_error; value ≤ 1e-12
- gauge / Zero-mean periodic potential gauge.: /metrics/potential_mean_absolute; value ≤ 1e-12
- analytic-mesh-potential / Compare a separate sinusoidal density with its analytic mesh potential.: /metrics/manufactured_potential_max_error; value ≤ 1e-12
- analytic-mesh-force / Compare the same sinusoidal density with its analytic mesh acceleration.: /metrics/manufactured_acceleration_max_error; value ≤ 1e-12
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = 9b44288285eb833f8132411dc681ebee4272ff1f6ee041c2a5a35004645c8b9b
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Reject nonpositive masses, nonfinite inputs, G!=1, invalid grids/sinusoidal modes and noninteger box shifts. Mass/net-force/self-force consistency alone does not establish individual particle-force accuracy. No periodic pair-sum reference, short-range correction, Ewald/P3M/PME/SPME or particle evolution.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/

### References

- CSV stores each particle's coordinates, mass, acceleration and force. Independent sinusoidal-field diagnostics are JSON metrics. No mesh refinement is misrepresented as analytic particle-force error.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json
- For separate rho=rho0+A*cos(k*x), phi=-4*pi*G*A*cos(k*x)/k² and ax=-4*pi*G*A*sin(k*x)/k. Not an exact periodic particle-force reference.: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Existing PM-method reference; this recipe explicitly fixes its CIC–FFT formulation, boundaries and check scope.: https://doi.org/10.1016/0021-9991(74)90044-8

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
