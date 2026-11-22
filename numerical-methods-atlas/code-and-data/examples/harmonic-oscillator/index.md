# Harmonic oscillator: Verlet phase error and energy / 調和振動子：Verletの位相誤差とエネルギー

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: harmonic-oscillator

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-domains-public.json

## ja

Verlet軌道を解析的な振動と比べ、状態誤差・元のエネルギーの偏差・時間反転を確認する。

### scope

既存の単位質量・単位角振動数の調和振動子をvelocity Verletで進める。20時間単位、200/400/800刻みの解析解比較、元のエネルギー偏差、時間反転を出力。

### assumptions

H=(q²+p²)/2、(q₀,p₀)=(1,0.2)。固定刻み、非散逸1自由度。初期値・終端時刻・刻み数は入力に明記。最大刻みh=0.1はhω<2の安定域。

### units

無次元化し質量m=1・角振動数ω=1。pはこの規約の正準運動量、エネルギーは(q²+p²)/2。

### boundaries

時間初期値問題。空間境界なし。出力時刻0〜20の両端を含む。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/harmonic-oscillator.json
Input SHA-256: b498106a876b71e8d6d3444c57b4e6cea0fd2a000d786a5ab3b91ec64804f4b4
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/harmonic-oscillator.json --output output-harmonic-oscillator
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/solution.csv

CSVは最細刻みの時刻ごとに数値・解析のq,pとエネルギーを整列。観測次数は終端状態誤差から、エネルギー偏差は全保存時刻から計算。

### Numerical acceptance

- analytic-state / 全時刻の位相空間誤差を解析解と比較。: /metrics/max_state_error; value ≤ 0.001
- refinement / 終端状態誤差の観測次数が2次に整合。: /metrics/minimum_observed_order; value ≥ 1.9
- energy-envelope / 元のHamiltonianの相対偏差を有限区間で測る。厳密保存とは呼ばない。: /metrics/max_relative_energy_deviation; value ≤ 0.0002
- time-reversal / 固定刻みを逆向きに戻した状態差。: /metrics/reversal_error; value ≤ 1e-11
- final-time / 指定した終端時刻に到達。: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = b498106a876b71e8d6d3444c57b4e6cea0fd2a000d786a5ab3b91ec64804f4b4
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

hω≥2、非有限入力、不明な方式・系、倍増でない刻み一覧を拒否。反転が良くても長時間位相誤差や元のHamiltonianの厳密保存を保証しない。非線形振動子・多体系への検証ではない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/

### References

- CSVは最細刻みの時刻ごとに数値・解析のq,pとエネルギーを整列。観測次数は終端状態誤差から、エネルギー偏差は全保存時刻から計算。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json
- 独立な解析式q=q₀cos t+p₀sin t、p=−q₀sin t+p₀cos t。数値解の細格子値を厳密解とは呼ばない。: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/
- 既存のVerlet手法項目の文献。今回の実行で原論文の全計算を再現するわけではない。: https://doi.org/10.1103/PhysRev.159.98

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare Verlet trajectories with analytic oscillation; inspect state error, original-energy deviation and time reversal.

### scope

Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.

### assumptions

H=(q²+p²)/2 and (q0,p0)=(1,0.2); one nondissipative degree of freedom, fixed steps. Inputs explicitly provide initial state, final time and counts. Largest h=0.1 lies in h*omega<2.

### units

Nondimensional unit mass m=1 and angular frequency omega=1; p is canonical momentum and energy is (q²+p²)/2.

### boundaries

Temporal initial-value problem with no spatial boundary; output includes times 0 and 20.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/harmonic-oscillator.json
Input SHA-256: b498106a876b71e8d6d3444c57b4e6cea0fd2a000d786a5ab3b91ec64804f4b4
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/harmonic-oscillator.json --output output-harmonic-oscillator
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/solution.csv

CSV aligns numerical/analytic q,p and energy on the finest time grid. Observed order uses endpoint-state errors; energy deviation uses all recorded times.

### Numerical acceptance

- analytic-state / Compare phase-space error with the analytic solution over all output times.: /metrics/max_state_error; value ≤ 0.001
- refinement / Endpoint-error refinement is consistent with second order.: /metrics/minimum_observed_order; value ≥ 1.9
- energy-envelope / Measure relative deviation of the original Hamiltonian over this finite interval; not exact conservation.: /metrics/max_relative_energy_deviation; value ≤ 0.0002
- time-reversal / State difference after reversing the same fixed steps.: /metrics/reversal_error; value ≤ 1e-11
- final-time / Reach the specified final time.: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = b498106a876b71e8d6d3444c57b4e6cea0fd2a000d786a5ab3b91ec64804f4b4
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Reject h*omega>=2, nonfinite inputs, unknown method/system and non-doubling counts. Accurate reversal does not establish long-time phase accuracy or exact original-Hamiltonian conservation. Not validation of nonlinear oscillators or many-body systems.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/

### References

- CSV aligns numerical/analytic q,p and energy on the finest time grid. Observed order uses endpoint-state errors; energy deviation uses all recorded times.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json
- Independent analytic q=q0*cos(t)+p0*sin(t), p=-q0*sin(t)+p0*cos(t); no fine numerical solution is called exact.: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/
- Existing Verlet-method reference; this run does not reproduce every calculation in the original paper.: https://doi.org/10.1103/PhysRev.159.98

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
