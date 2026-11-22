# FMM：直接和・解析配置と展開次数・木の深さ

96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。

## 前提・単位・境界

自由空間のphi=−sum(q log r)、自己項なし。単位正方形は木の包囲領域で、壁・周期境界ではありません。3次元Coulomb核とは別です。

**編集上の補足**

自由空間2次元対数核の展開次数・木の深さ・回転平行移動の影響を測ります。深さで単調に改善するとは仮定せず、3次元Coulomb核や最適計算量へ広げません。

## 採用した計算法

P2M/M2M/M2L/L2Lと近接P2Pを保ち、次数2/4/8/12、深さ2/3を比較します。別のCartesian直接和、二点電荷の閉形式、正多角形の中心力と遠方ポテンシャルを参照にします。

$$
\phi_i=-\sum_{j\ne i}q_j\log|z_i-z_j|,\qquad\mathbf F_i=q_i\mathbf E_i
$$

$$
\epsilon_E=\max_i\|\mathbf E_i^{\rm FMM}-\mathbf E_i^{\rm direct}\|_{\infty}
$$

## 比較・検証

ポテンシャル・場の最大絶対誤差、実際の遠方移動演算、回転・平行移動誤差、電荷を掛けた力の合計を測ります。粗い展開の失敗対照も確認します。

## 確認の限界

木の深さによる相互作用の分割は変わるので、一定次数で深さに対する単調収束は要求しません。対象粒子ごとの展開は厳密な作用反作用を保証せず、3次元・適応木・周期FMM・計算量スケーリングは未検証です。

## 保存実測値と判定

```json
{
  "metrics": {
    "fine_potential_error": 1.6153974611299304e-06,
    "fine_field_error": 0.00013124381103546412,
    "order_refinement_ratio": 7.213976104507879e-05,
    "depth2_field_error": 0.00010463275822658602,
    "net_force_relative": 8.766244233276265e-08,
    "net_force_absolute": 0.00011622325026383606,
    "direct_net_force": 7.283063041541027e-14,
    "coarse_control_field_error": 1.8192992204874692,
    "translation_potential_error": 1.612941820106073e-06,
    "translation_field_error": 0.0004069109892306244,
    "rotation_potential_error": 1.614394697035948e-06,
    "rotation_field_error": 0.00015204244904776232,
    "analytic_direct_potential_error": 0.0,
    "analytic_direct_field_error": 0.0,
    "symmetric_field_error": 6.770015090751258e-06,
    "multipole_potential_error": 1.3839596135767351e-11,
    "multipole_field_error": 1.0251124393789723e-09
  },
  "checks": {
    "fine_potential_error": true,
    "fine_field_error": true,
    "order_refinement_ratio": true,
    "depth2_field_error": true,
    "translation_potential_error": true,
    "translation_field_error": true,
    "rotation_potential_error": true,
    "rotation_field_error": true,
    "net_force_relative": true,
    "analytic_direct_potential_error": true,
    "analytic_direct_field_error": true,
    "symmetric_field_error": true,
    "multipole_potential_error": true,
    "multipole_field_error": true,
    "coarse_control_detected": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_pairs_subset": true,
    "multipole_probe_has_far_translation": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## 出典と確認範囲

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
  著者所属機関の再録PDFで対数核、モーメント、3つの移動演算、上下走査を確認。再録版の掲載年1997と原著1987を区別。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# FMM: direct and analytic references, order and tree depth

Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.

## Assumptions, units and boundaries

Free-space phi=−sum(q log r), excluding self terms. The unit square bounds the tree and is not a wall or periodic boundary; this is separate from a 3D Coulomb kernel.

**Editorial clarification**

Measure order, tree-depth and rotation/translation effects for the free-space 2D logarithmic kernel. Do not assume monotone depth improvement or generalize to 3D Coulomb kernels or optimal complexity.

## Adopted numerical method

Retain P2M/M2M/M2L/L2L and near P2P; compare orders 2/4/8/12 and depths two/three. References include independent Cartesian direct sums, a closed-form charge pair and regular-polygon radial/far-field identities.

$$
\phi_i=-\sum_{j\ne i}q_j\log|z_i-z_j|,\qquad\mathbf F_i=q_i\mathbf E_i
$$

$$
\epsilon_E=\max_i\|\mathbf E_i^{\rm FMM}-\mathbf E_i^{\rm direct}\|_{\infty}
$$

## References and validation

Measure maximum absolute potential/field errors, actual far translations, rotation/translation differences and net charge-weighted force. Detect an inaccurate low-order control.

## Limits

Interaction repartition changes with depth, so fixed-order depth refinement is not assumed monotone. Target-wise expansions need not preserve exact action/reaction. No 3D, adaptive/periodic FMM or complexity-scaling claim.

## Stored measurements and decisions

```json
{
  "metrics": {
    "fine_potential_error": 1.6153974611299304e-06,
    "fine_field_error": 0.00013124381103546412,
    "order_refinement_ratio": 7.213976104507879e-05,
    "depth2_field_error": 0.00010463275822658602,
    "net_force_relative": 8.766244233276265e-08,
    "net_force_absolute": 0.00011622325026383606,
    "direct_net_force": 7.283063041541027e-14,
    "coarse_control_field_error": 1.8192992204874692,
    "translation_potential_error": 1.612941820106073e-06,
    "translation_field_error": 0.0004069109892306244,
    "rotation_potential_error": 1.614394697035948e-06,
    "rotation_field_error": 0.00015204244904776232,
    "analytic_direct_potential_error": 0.0,
    "analytic_direct_field_error": 0.0,
    "symmetric_field_error": 6.770015090751258e-06,
    "multipole_potential_error": 1.3839596135767351e-11,
    "multipole_field_error": 1.0251124393789723e-09
  },
  "checks": {
    "fine_potential_error": true,
    "fine_field_error": true,
    "order_refinement_ratio": true,
    "depth2_field_error": true,
    "translation_potential_error": true,
    "translation_field_error": true,
    "rotation_potential_error": true,
    "rotation_field_error": true,
    "net_force_relative": true,
    "analytic_direct_potential_error": true,
    "analytic_direct_field_error": true,
    "symmetric_field_error": true,
    "multipole_potential_error": true,
    "multipole_field_error": true,
    "coarse_control_detected": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_pairs_subset": true,
    "multipole_probe_has_far_translation": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## Sources and review scope

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
  Institution-hosted reprint consulted for the log kernel, moments, three translations and up/down passes; 1997 reprint distinguished from 1987 original.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
