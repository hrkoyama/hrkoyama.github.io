# 2次元対数核のM2M・M2L・L2Lを持つFMM

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

## 前提・単位・境界

単位正方形内の有限点電荷ですが、境界は壁でなく木を作る包囲領域です。核はphi=−sum(q log r)、電場は−grad(phi)。自己項を除外し、周期像はありません。

## 採用した計算法

葉でP2M、上向きのM2M、相互作用リスト上のM2L、下向きのL2L、局所多項式の評価と近接P2Pを実装します。遠方を粒子ごとに開くBarnes–Hutへ置き換えず、移動演算回数と近接対数を記録します。

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

## 比較・検証

固定seedの128粒子で次数2・4・8・12を走査し、別の全対直接和とポテンシャル・電場の全成分を照合します。2点の符号、順序不変性、ポテンシャル微分も検査します。

## 確認の限界

3次元1/r核、適応木、周期FMM、特異積分、実測の計算量スケーリングは未検証です。2次元自由空間の教育用実装として表示します。

## 保存実測値と判定

```json
{
  "metrics": {
    "potential_max_error": 5.953093840105339e-07,
    "field_max_error": 6.36492158818669e-05,
    "finest_to_coarsest_ratio": 3.419465787735687e-05
  },
  "checks": {
    "potential_max_error": true,
    "field_max_error": true,
    "finest_to_coarsest_ratio": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_field_is_subset": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
  著者所属機関の再録PDFで対数核、モーメント、3つの移動演算、上下走査を確認。再録版の掲載年1997と原著1987を区別。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# 2D logarithmic FMM with M2M, M2L and L2L

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

## Assumptions, units and boundaries

Particles lie in a unit-square bounding box, not a physical wall boundary. The kernel is phi=−sum(q log r), with field −grad(phi); self terms are excluded and no periodic images are used.

## Adopted numerical method

Implement leaf P2M, upward M2M, interaction-list M2L, downward L2L, local-polynomial evaluation and near-field P2P. Record translation and near-pair counts; this is not a Barnes–Hut traversal relabeled as FMM.

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

## References and validation

For 128 fixed-seed particles, sweep orders 2/4/8/12 and compare every potential/field component with a separate all-pairs calculation. Also check two-source signs, permutation invariance and potential derivatives.

## Limits

No 3D 1/r kernel, adaptive tree, periodic FMM, singular quadrature or empirical complexity/scaling study. Evidence applies to this 2D free-space educational implementation.

## Stored measurements and decisions

```json
{
  "metrics": {
    "potential_max_error": 5.953093840105339e-07,
    "field_max_error": 6.36492158818669e-05,
    "finest_to_coarsest_ratio": 3.419465787735687e-05
  },
  "checks": {
    "potential_max_error": true,
    "field_max_error": true,
    "finest_to_coarsest_ratio": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_field_is_subset": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
  Institution-hosted reprint consulted for the log kernel, moments, three translations and up/down passes; 1997 reprint distinguished from 1987 original.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
