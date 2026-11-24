# SHAKEとRATTLE：拘束と運動量の違い

単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。

**使用手法**

- [SHAKE拘束積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=ja) (`shake`)
- [RATTLE拘束積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=ja) (`rattle`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-algorithm)

独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

- [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja) (`constrained-pendulum`)

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。


**問題の図**

![SHAKEとRATTLE：拘束と運動量の違い：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-validation)

独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja) (`high-index-pendulum`; 同じ問題の参照 · 半解析参照)

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja) (`shake-rattle-pendulum`; 同じ問題の参照 · 半解析参照)

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
## 前提・単位・境界

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

**編集上の補足**

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

## 比較・検証

独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。

## 確認の限界

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "rattle_observed_orders": [
      2.0002044529735445,
      2.0000564458078465
    ],
    "shake_observed_orders": [
      2.000077432739235,
      2.0000041345609065
    ],
    "reduced_map_probes": [
      {
        "state": [
          0.7,
          0.0
        ],
        "symplectic_defect": 3.424459604772778e-10,
        "FD_difference": 1.7850310118916468e-10
      },
      {
        "state": [
          0.3,
          0.2
        ],
        "symplectic_defect": 3.746203347532173e-11,
        "FD_difference": 1.8735013540549517e-10
      },
      {
        "state": [
          -0.4,
          -0.3
        ],
        "symplectic_defect": 1.2937362292575472e-10,
        "FD_difference": 2.7755575615628914e-10
      }
    ],
    "evolution_count": 10,
    "centered_SHAKE_not_RATTLE_tangent": true,
    "maximum_constraint": 3.811062576630775e-12
  },
  "checks": {
    "rattle-tight-2500-finite": true,
    "rattle-tight-2500-completed": true,
    "rattle-tight-2500-constraint": true,
    "rattle-tight-2500-state": true,
    "rattle-tight-2500-energy": true,
    "rattle-tight-2500-solver": true,
    "rattle-tight-2500-tangent": true,
    "rattle-tight-5000-finite": true,
    "rattle-tight-5000-completed": true,
    "rattle-tight-5000-constraint": true,
    "rattle-tight-5000-state": true,
    "rattle-tight-5000-energy": true,
    "rattle-tight-5000-solver": true,
    "rattle-tight-5000-tangent": true,
    "rattle-tight-10000-finite": true,
    "rattle-tight-10000-completed": true,
    "rattle-tight-10000-constraint": true,
    "rattle-tight-10000-state": true,
    "rattle-tight-10000-energy": true,
    "rattle-tight-10000-solver": true,
    "rattle-tight-10000-tangent": true,
    "rattle-loose-2500-finite": true,
    "rattle-loose-2500-completed": true,
    "rattle-loose-2500-constraint": true,
    "rattle-loose-2500-state": true,
    "rattle-loose-2500-energy": true,
    "rattle-loose-2500-solver": true,
    "rattle-loose-2500-tangent": true,
    "rattle-reverse-finite": true,
    "rattle-reverse-steps": true,
    "rattle-reverse-recovery": true,
    "shake-tight-2500-finite": true,
    "shake-tight-2500-completed": true,
    "shake-tight-2500-constraint": true,
    "shake-tight-2500-state": true,
    "shake-tight-2500-energy": true,
    "shake-tight-2500-solver": true,
    "shake-tight-2500-finite-C-identity": true,
    "shake-tight-2500-centered-tangency": true,
    "shake-tight-5000-finite": true,
    "shake-tight-5000-completed": true,
    "shake-tight-5000-constraint": true,
    "shake-tight-5000-state": true,
    "shake-tight-5000-energy": true,
    "shake-tight-5000-solver": true,
    "shake-tight-5000-finite-C-identity": true,
    "shake-tight-5000-centered-tangency": true,
    "shake-tight-10000-finite": true,
    "shake-tight-10000-completed": true,
    "shake-tight-10000-constraint": true,
    "shake-tight-10000-state": true,
    "shake-tight-10000-energy": true,
    "shake-tight-10000-solver": true,
    "shake-tight-10000-finite-C-identity": true,
    "shake-tight-10000-centered-tangency": true,
    "shake-loose-2500-finite": true,
    "shake-loose-2500-completed": true,
    "shake-loose-2500-constraint": true,
    "shake-loose-2500-state": true,
    "shake-loose-2500-energy": true,
    "shake-loose-2500-solver": true,
    "shake-loose-2500-finite-C-identity": true,
    "shake-loose-2500-centered-tangency": true,
    "shake-reverse-finite": true,
    "shake-reverse-steps": true,
    "shake-reverse-recovery": true,
    "rattle-state-order": true,
    "shake-state-order": true,
    "reduced-map-0-symplectic-proxy": true,
    "reduced-map-0-FD-consistency": true,
    "reduced-map-1-symplectic-proxy": true,
    "reduced-map-1-FD-consistency": true,
    "reduced-map-2-symplectic-proxy": true,
    "reduced-map-2-FD-consistency": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/index.json

![保存したh=0.01の縮約位相軌道。SHAKEは内部点の中心化運動量、RATTLEは全時刻の接線運動量です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum-preview.png)

保存したh=0.01の縮約位相軌道。SHAKEは内部点の中心化運動量、RATTLEは全時刻の接線運動量です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Solving Differential Equations on Manifolds [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly-sde-mani.pdf; review_level=selected-primary-scope
Author-hosted lecture notes, selected printed page50, SectionV.5, equations5.1–5.3 and Theorem5.1 statement, rendered and visually read. Centered SHAKE momentum and RATTLE final tangency are explicit. The original1977 SHAKE and1983 RATTLE articles remain full-text unread; no full proof review is claimed.

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- DLMF22.4: Periods, Poles, and Zeros (version 1.2.8, released 2026-09-15) [accessed 2026-11-24]. https://dlmf.nist.gov/22.4; review_level=selected-primary-scope
Official Table22.4.1 selected real periods: sn and cn have4K, dn has2K. Version date is not an initial publication date. Common-period reduction and direct-library periodicity qualification are separate from the independent angular DOP853 state comparison.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# SHAKE and RATTLE: constraints and momentum ownership

Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.

**Methods used**

- [SHAKE constrained integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=en) (`shake`)
- [RATTLE constrained integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=en) (`rattle`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-algorithm)

Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

- [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en) (`constrained-pendulum`)

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.


**Problem figure**

![SHAKE and RATTLE: constraints and momentum ownership: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-validation)

A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en) (`high-index-pendulum`; Same-problem reference · Semi-analytic reference)

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en) (`shake-rattle-pendulum`; Same-problem reference · Semi-analytic reference)

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
## Assumptions, units and boundaries

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

**Editorial clarification**

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

## References and validation

A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.

## Limits

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

## Stored measurements and decisions

```json
{
  "metrics": {
    "rattle_observed_orders": [
      2.0002044529735445,
      2.0000564458078465
    ],
    "shake_observed_orders": [
      2.000077432739235,
      2.0000041345609065
    ],
    "reduced_map_probes": [
      {
        "state": [
          0.7,
          0.0
        ],
        "symplectic_defect": 3.424459604772778e-10,
        "FD_difference": 1.7850310118916468e-10
      },
      {
        "state": [
          0.3,
          0.2
        ],
        "symplectic_defect": 3.746203347532173e-11,
        "FD_difference": 1.8735013540549517e-10
      },
      {
        "state": [
          -0.4,
          -0.3
        ],
        "symplectic_defect": 1.2937362292575472e-10,
        "FD_difference": 2.7755575615628914e-10
      }
    ],
    "evolution_count": 10,
    "centered_SHAKE_not_RATTLE_tangent": true,
    "maximum_constraint": 3.811062576630775e-12
  },
  "checks": {
    "rattle-tight-2500-finite": true,
    "rattle-tight-2500-completed": true,
    "rattle-tight-2500-constraint": true,
    "rattle-tight-2500-state": true,
    "rattle-tight-2500-energy": true,
    "rattle-tight-2500-solver": true,
    "rattle-tight-2500-tangent": true,
    "rattle-tight-5000-finite": true,
    "rattle-tight-5000-completed": true,
    "rattle-tight-5000-constraint": true,
    "rattle-tight-5000-state": true,
    "rattle-tight-5000-energy": true,
    "rattle-tight-5000-solver": true,
    "rattle-tight-5000-tangent": true,
    "rattle-tight-10000-finite": true,
    "rattle-tight-10000-completed": true,
    "rattle-tight-10000-constraint": true,
    "rattle-tight-10000-state": true,
    "rattle-tight-10000-energy": true,
    "rattle-tight-10000-solver": true,
    "rattle-tight-10000-tangent": true,
    "rattle-loose-2500-finite": true,
    "rattle-loose-2500-completed": true,
    "rattle-loose-2500-constraint": true,
    "rattle-loose-2500-state": true,
    "rattle-loose-2500-energy": true,
    "rattle-loose-2500-solver": true,
    "rattle-loose-2500-tangent": true,
    "rattle-reverse-finite": true,
    "rattle-reverse-steps": true,
    "rattle-reverse-recovery": true,
    "shake-tight-2500-finite": true,
    "shake-tight-2500-completed": true,
    "shake-tight-2500-constraint": true,
    "shake-tight-2500-state": true,
    "shake-tight-2500-energy": true,
    "shake-tight-2500-solver": true,
    "shake-tight-2500-finite-C-identity": true,
    "shake-tight-2500-centered-tangency": true,
    "shake-tight-5000-finite": true,
    "shake-tight-5000-completed": true,
    "shake-tight-5000-constraint": true,
    "shake-tight-5000-state": true,
    "shake-tight-5000-energy": true,
    "shake-tight-5000-solver": true,
    "shake-tight-5000-finite-C-identity": true,
    "shake-tight-5000-centered-tangency": true,
    "shake-tight-10000-finite": true,
    "shake-tight-10000-completed": true,
    "shake-tight-10000-constraint": true,
    "shake-tight-10000-state": true,
    "shake-tight-10000-energy": true,
    "shake-tight-10000-solver": true,
    "shake-tight-10000-finite-C-identity": true,
    "shake-tight-10000-centered-tangency": true,
    "shake-loose-2500-finite": true,
    "shake-loose-2500-completed": true,
    "shake-loose-2500-constraint": true,
    "shake-loose-2500-state": true,
    "shake-loose-2500-energy": true,
    "shake-loose-2500-solver": true,
    "shake-loose-2500-finite-C-identity": true,
    "shake-loose-2500-centered-tangency": true,
    "shake-reverse-finite": true,
    "shake-reverse-steps": true,
    "shake-reverse-recovery": true,
    "rattle-state-order": true,
    "shake-state-order": true,
    "reduced-map-0-symplectic-proxy": true,
    "reduced-map-0-FD-consistency": true,
    "reduced-map-1-symplectic-proxy": true,
    "reduced-map-1-FD-consistency": true,
    "reduced-map-2-symplectic-proxy": true,
    "reduced-map-2-FD-consistency": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/index.json

![Saved reduced phase portraits at h=0.01. SHAKE uses interior centered momentum; RATTLE uses full-time tangent momentum.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum-preview.png)

Saved reduced phase portraits at h=0.01. SHAKE uses interior centered momentum; RATTLE uses full-time tangent momentum.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Solving Differential Equations on Manifolds [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly-sde-mani.pdf; review_level=selected-primary-scope
Author-hosted lecture notes, selected printed page50, SectionV.5, equations5.1–5.3 and Theorem5.1 statement, rendered and visually read. Centered SHAKE momentum and RATTLE final tangency are explicit. The original1977 SHAKE and1983 RATTLE articles remain full-text unread; no full proof review is claimed.

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- DLMF22.4: Periods, Poles, and Zeros (version 1.2.8, released 2026-09-15) [accessed 2026-11-24]. https://dlmf.nist.gov/22.4; review_level=selected-primary-scope
Official Table22.4.1 selected real periods: sn and cn have4K, dn has2K. Version date is not an initial publication date. Common-period reduction and direct-library periodicity qualification are separate from the independent angular DOP853 state comparison.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
