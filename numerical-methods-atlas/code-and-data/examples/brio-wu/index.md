# Brio–Wu: HLLD and a conservatively restricted numerical reference / Brio–Wu：HLLDと保存的に粗視化した数値参照

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: brio-wu

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json

## ja

HLLDの64/128セル解を512セル数値参照と比べ、密度・圧力・一定縦磁場・流束収支と切替回数を確認する。

### scope

γ=2、Bx=0.75の1次元理想MHD衝撃波管をt=0.1まで計算。HLLD＋MC＋SSPRK2の64/128セルを512セルの数値参照と比較し、密度・圧力・縦磁場・保存収支・切替回数を記録する。

### assumptions

μ0=1、左右(ρ,vx,vy,vz,p,Bx,By,Bz)=(1,0,0,0,1,0.75,1,0)/(0.125,0,0,0,0.1,0.75,−1,0)。初期不連続x=0.5をセル界面へ合わせる。既存solve_1dの固定定義とJSONの一致を検査し、変更した物理定義は拒否。CFL=0.35。

### units

すべて無次元。磁気エネルギーはB²/2（μ0=1）、熱エネルギーはp/(γ−1)。γ=5/3のOrszag–Tang例とは異なる。

### boundaries

端値外挿。波が端へ達しないt≤0.1で、8保存量の変化からT(F_left−F_right)を差し引く。全運動量が不変とは仮定しない。1次元で共通のBxを保つ。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/brio-wu.json
Input SHA-256: faf47e55ad28b23f154021809d351ac853c4145790b6f54692031c081c9c7f4b
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/brio-wu.json --output output-brio-wu
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/solution.csv

512セルの保存変数を64/128セルへ整数ブロック平均し、その後にprimitive変数へ変換する。CSVは128セルごとに計算値とそのセル平均に対応する参照値を配置。正値性、縦磁場10^-12、境界流束収支10^-10、経験的な誤差減少を別々に判定し、fallback回数を隠さない。

### Numerical acceptance

- numerical-reference-error / 512セル参照を保存変数でブロック平均した密度との差が平均0.03以下。厳密解ではない。: /metrics/density_l1_error_fine; value ≤ 0.03
- empirical-refinement / 64→128セルで高解像度参照との差が減る。形式次数は主張しない。: /metrics/fine_to_coarse_error_ratio; value ≤ 0.95
- longitudinal-field / 1次元で一定の縦磁場Bx=0.75を保存する。: /metrics/longitudinal_field_max_error; value ≤ 1e-12
- no-positivity-retry / この標準入力では正値性失敗による再試行がない。HLLE流束への切替回数は別途記録する。: /metrics/retried_steps; value ≤ 0
- positive-density / 最小密度が正である。: /metrics/minimum_density; value ≥ 1e-08
- positive-pressure / 最小圧力が正である。: /metrics/minimum_pressure; value ≥ 1e-08
- boundary-balance / 遠方の物理境界流束を差し引いた相対収支誤差。: /metrics/physical_boundary_balance_relative_defect; value ≤ 1e-10
- reached-time / 指定した終端時刻まで進んだ。: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = faf47e55ad28b23f154021809d351ac853c4145790b6f54692031c081c9c7f4b
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

512セル参照も同一solverで、厳密解・独立コード・MHD弱解の一意性の証明ではない。密度差0.03は左密度1に対する3%の平均絶対差を許す教材基準。正値性再試行とHLLE切替は数えるが、再構成の正値スケーリングの作動数は既存APIにない。正値出力だけから一般の保証やゼロ修正を主張しない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/

### References

- 512セルの保存変数を64/128セルへ整数ブロック平均し、その後にprimitive変数へ変換する。CSVは128セルごとに計算値とそのセル平均に対応する参照値を配置。正値性、縦磁場10^-12、境界流束収支10^-10、経験的な誤差減少を別々に判定し、fallback回数を隠さない。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json
- Brio–Wu理想MHD衝撃波管の原報。原報の全計算や厳密Riemann解は再現しない。: https://doi.org/10.1016/0021-9991(88)90120-9
- HLLD流束の原報。公開実装では無効な中間状態に対するHLLE切替を数える。: https://doi.org/10.1016/j.jcp.2005.02.017

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare 64/128-cell HLLD solutions with a 512-cell numerical reference; inspect density, pressure, constant longitudinal field, balances and fallbacks.

### scope

Evolve the one-dimensional γ=2 ideal-MHD shock tube with Bx=0.75 to t=0.1. Compare 64/128-cell HLLD/MC/SSPRK2 with a 512-cell numerical reference, recording density, pressure, longitudinal field, balances and fallback counts.

### assumptions

μ0=1, with left/right (ρ,vx,vy,vz,p,Bx,By,Bz)=(1,0,0,0,1,0.75,1,0)/(0.125,0,0,0,0.1,0.75,−1,0). The initial jump x=0.5 is face-aligned. JSON must match the unchanged solve_1d benchmark definition; altered physical definitions are rejected. CFL=0.35.

### units

All quantities are nondimensional. Magnetic energy is B²/2 with μ0=1 and thermal energy is p/(γ−1). This differs from the γ=5/3 Orszag–Tang case.

### boundaries

Edge extrapolation. For t≤0.1, before waves reach the ends, subtract T(F_left−F_right) from all eight conserved-integral changes. Total momentum is not assumed constant; the common one-dimensional Bx is retained.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/brio-wu.json
Input SHA-256: faf47e55ad28b23f154021809d351ac853c4145790b6f54692031c081c9c7f4b
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/brio-wu.json --output output-brio-wu
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/solution.csv

Restrict the 512-cell conserved variables by integer block averaging to 64/128 cells before converting to primitives. CSV pairs each 128-cell result with its corresponding restricted reference. Positivity, longitudinal-field error 10^-12, boundary-flux balance 10^-10 and empirical error decrease are separate checks; fallback counts remain visible.

### Numerical acceptance

- numerical-reference-error / Mean density discrepancy from the conservatively restricted 512-cell reference is at most 0.03; the reference is not exact.: /metrics/density_l1_error_fine; value ≤ 0.03
- empirical-refinement / The discrepancy with the higher-resolution reference decreases from 64 to 128 cells; no formal order is claimed.: /metrics/fine_to_coarse_error_ratio; value ≤ 0.95
- longitudinal-field / The constant one-dimensional longitudinal field Bx=0.75 is retained.: /metrics/longitudinal_field_max_error; value ≤ 1e-12
- no-positivity-retry / This standard input needs no positivity-failure time-step retry; HLLE flux fallbacks are separately reported.: /metrics/retried_steps; value ≤ 0
- positive-density / Minimum density remains positive.: /metrics/minimum_density; value ≥ 1e-08
- positive-pressure / Minimum gas pressure remains positive.: /metrics/minimum_pressure; value ≥ 1e-08
- boundary-balance / Relative integral balance defect after subtracting physical far-field boundary fluxes.: /metrics/physical_boundary_balance_relative_defect; value ≤ 1e-10
- reached-time / The requested final time is reached.: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = faf47e55ad28b23f154021809d351ac853c4145790b6f54692031c081c9c7f4b
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

The 512-cell reference uses the same solver and is neither exact nor independent, nor a proof of uniqueness of MHD weak solutions. Density difference 0.03 allows a mean absolute discrepancy of 3% of left density 1 for this educational test. Positivity retries and HLLE fallbacks are counted; reconstruction positivity-scaling activations are not exposed by the existing API. Positive output alone certifies neither general positivity nor absence of reconstruction changes.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/

### References

- Restrict the 512-cell conserved variables by integer block averaging to 64/128 cells before converting to primitives. CSV pairs each 128-cell result with its corresponding restricted reference. Positivity, longitudinal-field error 10^-12, boundary-flux balance 10^-10 and empirical error decrease are separate checks; fallback counts remain visible.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json
- Original Brio–Wu ideal-MHD shock-tube paper; its full experiments and an exact Riemann solution are not reproduced.: https://doi.org/10.1016/0021-9991(88)90120-9
- Original HLLD flux paper. The released implementation counts HLLE fallbacks for invalid intermediate states.: https://doi.org/10.1016/j.jcp.2005.02.017

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
