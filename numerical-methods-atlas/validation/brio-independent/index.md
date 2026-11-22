# Brio–Wu：別実装HLLDとの照合

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。

## 前提・単位・境界

1D、[0,1]、t=0.1、γ=2、Bx=0.75。左右(rho,p,By)=(1,1,1)/(0.125,0.1,-1)、速度ゼロ、流出境界。

## 採用した計算法

アトラス側はMC再構成とSSPRK2、参照は独立C++のHLLD・PLM・RK3。異なる実装ですがHLLDという数値流束の系列は共有します。

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

## 比較・検証

128/256/512セルを、2048/4096セルで再実行した独立参照の保存的細胞平均と比較。rho/ByのL1誤差、格子改善、密度・圧力正値性を判定します。

## 確認の限界

Brio–Wuの複合波を含む数値解との照合であり、一般MHD Riemann問題の唯一の厳密解とは呼びません。参照の再生成にはC++コンパイルが必要で、通常Python実行は同梱参照を使います。

## 保存実測値と判定

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.00048642415115017165,
    "reference_finest_n": 4096,
    "finest_density_l1": 0.0018299450752667257
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true,
    "magnetic_error": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- M. Brio and C. C. Wu (1988). An upwind differencing scheme for the equations of ideal magnetohydrodynamics. https://doi.org/10.1016/0021-9991(88)90120-9; review_level=bibliographic identity and official Athena test definition

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Brio–Wu against an independent HLLD implementation

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.

## Assumptions, units and boundaries

1D, [0,1], t=0.1, gamma=2, Bx=0.75; left/right (rho,p,By)=(1,1,1)/(0.125,0.1,-1), zero velocity, outflow boundaries.

## Adopted numerical method

Atlas uses MC reconstruction and SSPRK2; the independent C++ reference uses HLLD, PLM and RK3. Implementations differ while sharing the HLLD flux family.

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

## References and validation

Compare 128/256/512 cells with conservative averages of independently rerun 2048/4096-cell references. Check density/By L1 errors, refinement and positive density/pressure.

## Limits

This compares numerical solutions including the Brio–Wu compound wave; it is not a claim of a unique exact solution for arbitrary MHD Riemann problems. Reference regeneration requires C++ compilation; routine Python runs use the stored reference.

## Stored measurements and decisions

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.00048642415115017165,
    "reference_finest_n": 4096,
    "finest_density_l1": 0.0018299450752667257
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true,
    "magnetic_error": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- M. Brio and C. C. Wu (1988). An upwind differencing scheme for the equations of ideal magnetohydrodynamics. https://doi.org/10.1016/0021-9991(88)90120-9; review_level=bibliographic identity and official Athena test definition

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
