# 反応拡散：空間2次と時間4次を分けて測る

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

## 前提・単位・境界

周期区間[0,2pi)、D=0.1、r=0.1、初期cos(2x)、終了t=2。格子16/32/64と、別の固定格子で刻み0.5/0.25/0.125を用います。

## 採用した計算法

周期中心2階差分と独自RK4で進めます。空間系列は小さな同一時間刻み、時間系列は同じ空間演算子を用います。

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

## 比較・検証

連続固有値r-Dk²への最大誤差で空間次数、半離散固有値r-4Dsin²(kdx/2)/dx²への最大誤差で時間次数を測ります。独立した解析参照であり同じ実装の細格子値を参照にしません。

## 確認の限界

線形・周期・滑らかな単一モードだけを検証します。非線形のFisher前線、複雑境界、空間生態系や一般の反応ネットワークの検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "spatial_finest_error": 0.0014105590121191725,
    "spatial_minimum_order": 1.9995467358065582,
    "temporal_finest_error": 4.109141582553377e-09,
    "temporal_minimum_order": 4.0421093675761
  },
  "checks": {
    "space_error": true,
    "space_order": true,
    "time_error": true,
    "time_order": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  公式の行列指数APIとPadé/scaling-and-squaring法の記載を確認。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Reaction-diffusion: separate second-order space and fourth-order time

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

## Assumptions, units and boundaries

Periodic[0,2pi), D=0.1,r=0.1, initial cos(2x), final t=2. Use grids 16/32/64 and a separate fixed-grid timestep sequence 0.5/0.25/0.125.

## Adopted numerical method

Advance original periodic second-centered differences with RK4. The spatial sequence uses one small time step; the temporal sequence fixes the spatial operator.

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

## References and validation

Measure spatial order against r-Dk² and temporal order against r-4Dsin²(kdx/2)/dx². Both are independent analytic references, rather than a finer-grid run of the same solver.

## Limits

Only a linear, periodic, smooth single mode is verified. Nonlinear Fisher fronts, complex boundaries, spatial ecosystems and general reaction networks remain outside scope.

## Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_finest_error": 0.0014105590121191725,
    "spatial_minimum_order": 1.9995467358065582,
    "temporal_finest_error": 4.109141582553377e-09,
    "temporal_minimum_order": 4.0421093675761
  },
  "checks": {
    "space_error": true,
    "space_order": true,
    "time_error": true,
    "time_order": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  Official matrix-exponential API and description of the Pade/scaling-and-squaring method checked.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
