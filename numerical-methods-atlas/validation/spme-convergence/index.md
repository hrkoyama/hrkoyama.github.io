# SPME：格子・補間次数・格子位相と保存則

BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。

## 前提・単位・境界

同じ中性周期8電荷、alpha=5.6、実空間像3。PME族のEssmann型SPMEであり、1993年のLagrange補間の原法とは区別します。

**編集上の補足**

PME族のうちBスプラインSPMEのエネルギー勾配型を採用します。格子位相の依存と有限格子の合力を測り、厳密な運動量保存や原法Lagrange PMEの再現とはしません。

## 採用した計算法

16³/24³/40³格子と4/6次Bスプライン、3つの平行移動位相を用います。FFT逆空間エネルギーを割当て重みで位置微分し、実空間・自己項はEwald主計算と共有します。

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

## 比較・検証

独立thetaエネルギー・全力との差と、共有Ewald経路自体の誤差を明記します。分配の総和・導関数総和、電荷、エネルギー差分3成分、位相間の幅、有限格子の合力と粗い格子の対照を保存します。

## 確認の限界

エネルギー勾配型では有限格子のaliasingにより合力は一般にゼロではありません。厳密な運動量保存や任意配置での同じ誤差、長時間MD、原法PME、SPME全変種の検証とはしません。

## 保存実測値と判定

```json
{
  "metrics": {
    "fine_energy_error": 8.630229899608821e-07,
    "fine_force_error": 7.855116843202836e-06,
    "force_refinement_ratio": 0.005861182985296622,
    "phase_energy_spread": 1.1496225127416437e-07,
    "phase_force_spread": 1.447734647719301e-05,
    "charge_error": 2.4202861936828413e-14,
    "fine_net_force": 1.919342197087559e-05,
    "maximum_net_force_all_meshes": 0.15409275755368146,
    "shared_ewald_energy_error": 0.0,
    "shared_ewald_force_error": 3.197442310920451e-14,
    "partition_error": 2.8199664825478976e-14,
    "partition_derivative_error": 3.268496584496461e-13,
    "gradient_error": 2.401151921738176e-08,
    "coarse_control_force_error": 0.03526113281182308
  },
  "checks": {
    "fine_energy_error": true,
    "fine_force_error": true,
    "force_refinement_ratio": true,
    "phase_energy_spread": true,
    "phase_force_spread": true,
    "charge_error": true,
    "partition_error": true,
    "partition_derivative_error": true,
    "gradient_error": true,
    "shared_ewald_energy_error": true,
    "shared_ewald_force_error": true,
    "fine_net_force": true,
    "coarse_control_detected": true,
    "both_orders_refine": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/index.json

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

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
  原著PDFの冒頭と抄録を確認。歴史的なPME原法であり、実装したBスプライン変種とは区別。
- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
  原著PDFのBスプライン構造因子・FFT・解析勾配に関わる部分と抄録を確認。全ベンチマークの再現ではありません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# SPME: mesh, interpolation order, mesh phase and conservation

Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.

## Assumptions, units and boundaries

Same neutral periodic eight-charge cell, alpha=5.6 and three real-space image shells. This is Essmann-style SPME in the PME family, distinct from the original 1993 Lagrange interpolation.

**Editorial clarification**

Use the energy-gradient B-spline SPME variant of the PME family. Measure mesh-phase sensitivity and finite-mesh net force; do not claim exact momentum conservation or original Lagrange-PME reproduction.

## Adopted numerical method

Use 16³/24³/40³ meshes, orders four/six and three translations relative to the mesh. Differentiate FFT reciprocal energy through assignment weights; real/self terms share the primary Ewald implementation.

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

## References and validation

Report full energy/force errors against theta integration and explicitly check the shared Ewald path. Store assignment and derivative sums, charge, three finite-difference derivatives, phase spread, finite-mesh net force and a coarse-mesh control.

## Limits

Finite-mesh aliasing generally gives nonzero net force for this energy-gradient variant. No exact momentum conservation, arbitrary-configuration error bound, long MD, original PME or every SPME variant is certified.

## Stored measurements and decisions

```json
{
  "metrics": {
    "fine_energy_error": 8.630229899608821e-07,
    "fine_force_error": 7.855116843202836e-06,
    "force_refinement_ratio": 0.005861182985296622,
    "phase_energy_spread": 1.1496225127416437e-07,
    "phase_force_spread": 1.447734647719301e-05,
    "charge_error": 2.4202861936828413e-14,
    "fine_net_force": 1.919342197087559e-05,
    "maximum_net_force_all_meshes": 0.15409275755368146,
    "shared_ewald_energy_error": 0.0,
    "shared_ewald_force_error": 3.197442310920451e-14,
    "partition_error": 2.8199664825478976e-14,
    "partition_derivative_error": 3.268496584496461e-13,
    "gradient_error": 2.401151921738176e-08,
    "coarse_control_force_error": 0.03526113281182308
  },
  "checks": {
    "fine_energy_error": true,
    "fine_force_error": true,
    "force_refinement_ratio": true,
    "phase_energy_spread": true,
    "phase_force_spread": true,
    "charge_error": true,
    "partition_error": true,
    "partition_derivative_error": true,
    "gradient_error": true,
    "shared_ewald_energy_error": true,
    "shared_ewald_force_error": true,
    "fine_net_force": true,
    "coarse_control_detected": true,
    "both_orders_refine": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/index.json

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

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
  Original PDF opening and abstract checked; historical original PME is distinguished from the implemented B-spline variant.
- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
  Original PDF abstract and selected spline/structure-factor, FFT and analytic-gradient material checked; not a reproduction of every paper benchmark.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
