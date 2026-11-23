# SRMHDの有限振幅円偏極Alfvén波

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。

**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-algorithm)

D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

- [特殊相対論的理想MHD（SRMHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja) (`srmhd`)

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。


**問題の図**

![SRMHDの有限振幅円偏極Alfvén波：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) (`srmhd-alfven`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-validation)

非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。

- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja) (`srmhd-alfven`; 同じ問題の参照 · 解析参照)

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。
## 前提・単位・境界

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。

**編集上の補足**

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

## 採用した計算法

D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

## 比較・検証

非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。

## 確認の限界

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

## 保存実測値と判定

```json
{
  "metrics": {
    "alfven_speed": 0.3819660112501051,
    "period": 2.6180339887498953,
    "finest_transverse_relative_l1": 0.0032808347423469524,
    "observed_orders": [
      1.8810822553983044,
      1.8033064216647157
    ],
    "exact_scope": "Nonlinear finite-amplitude circular polarization; not linear passive transport or a generic RMHD Riemann reference."
  },
  "checks": {
    "n64: fixed final time": true,
    "n64: five saved times": true,
    "n64: four records per SSP step": true,
    "n64: all stored arrays finite": true,
    "n64: positive stage density": true,
    "n64: positive stage pressure": true,
    "n64: subluminal stages": true,
    "n64: positive reconstructed face density": true,
    "n64: positive reconstructed face pressure": true,
    "n64: subluminal reconstructed faces": true,
    "n64: conserved finite-volume boundary budget": true,
    "n64: physical root residual": true,
    "n64: full conserved primitive roundtrip": true,
    "n64: no state floor or retry": true,
    "n64: actual magnetic wave present": true,
    "n64: intermediate wave errors": true,
    "n128: fixed final time": true,
    "n128: five saved times": true,
    "n128: four records per SSP step": true,
    "n128: all stored arrays finite": true,
    "n128: positive stage density": true,
    "n128: positive stage pressure": true,
    "n128: subluminal stages": true,
    "n128: positive reconstructed face density": true,
    "n128: positive reconstructed face pressure": true,
    "n128: subluminal reconstructed faces": true,
    "n128: conserved finite-volume boundary budget": true,
    "n128: physical root residual": true,
    "n128: full conserved primitive roundtrip": true,
    "n128: no state floor or retry": true,
    "n128: actual magnetic wave present": true,
    "n128: intermediate wave errors": true,
    "n256: fixed final time": true,
    "n256: five saved times": true,
    "n256: four records per SSP step": true,
    "n256: all stored arrays finite": true,
    "n256: positive stage density": true,
    "n256: positive stage pressure": true,
    "n256: subluminal stages": true,
    "n256: positive reconstructed face density": true,
    "n256: positive reconstructed face pressure": true,
    "n256: subluminal reconstructed faces": true,
    "n256: conserved finite-volume boundary budget": true,
    "n256: physical root residual": true,
    "n256: full conserved primitive roundtrip": true,
    "n256: no state floor or retry": true,
    "n256: actual magnetic wave present": true,
    "n256: intermediate wave errors": true,
    "finest transverse L1": true,
    "finest wave phase": true,
    "finest wave amplitude": true,
    "minimum observed grid order": true,
    "wave refinement 1": true,
    "wave refinement 2": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/index.json

![最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- L. Del Zanna, O. Zanotti, N. Bucciantini and P. Londrillo (2007). ECHO: a Eulerian Conservative High Order scheme for general relativistic magnetohydrodynamics and magnetodynamics. https://arxiv.org/abs/0704.3206; review_level=primary-original-selected-section-and-rendered-pages
大学リポジトリの原著4.1節・式82–85を読み、原著プレプリント9–10頁の式・規格化・周期を描画して目視確認。ECHO法自体の再現ではありません。

- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
公式の著者レビュー3.1–3.2節、テンソル式49–51と変換式68–69を直接確認。平坦時空の実装に使用します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# SRMHD finite-amplitude circularly polarized Alfvén wave

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-algorithm)

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

- [Special-relativistic ideal MHD (SRMHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en) (`srmhd`)

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.


**Problem figure**

![SRMHD finite-amplitude circularly polarized Alfvén wave: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-validation)

Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.

- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en) (`srmhd-alfven`; Same-problem reference · Analytic reference)

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.
## Assumptions, units and boundaries

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.

**Editorial clarification**

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

## Adopted numerical method

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

## References and validation

Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.

## Limits

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

## Stored measurements and decisions

```json
{
  "metrics": {
    "alfven_speed": 0.3819660112501051,
    "period": 2.6180339887498953,
    "finest_transverse_relative_l1": 0.0032808347423469524,
    "observed_orders": [
      1.8810822553983044,
      1.8033064216647157
    ],
    "exact_scope": "Nonlinear finite-amplitude circular polarization; not linear passive transport or a generic RMHD Riemann reference."
  },
  "checks": {
    "n64: fixed final time": true,
    "n64: five saved times": true,
    "n64: four records per SSP step": true,
    "n64: all stored arrays finite": true,
    "n64: positive stage density": true,
    "n64: positive stage pressure": true,
    "n64: subluminal stages": true,
    "n64: positive reconstructed face density": true,
    "n64: positive reconstructed face pressure": true,
    "n64: subluminal reconstructed faces": true,
    "n64: conserved finite-volume boundary budget": true,
    "n64: physical root residual": true,
    "n64: full conserved primitive roundtrip": true,
    "n64: no state floor or retry": true,
    "n64: actual magnetic wave present": true,
    "n64: intermediate wave errors": true,
    "n128: fixed final time": true,
    "n128: five saved times": true,
    "n128: four records per SSP step": true,
    "n128: all stored arrays finite": true,
    "n128: positive stage density": true,
    "n128: positive stage pressure": true,
    "n128: subluminal stages": true,
    "n128: positive reconstructed face density": true,
    "n128: positive reconstructed face pressure": true,
    "n128: subluminal reconstructed faces": true,
    "n128: conserved finite-volume boundary budget": true,
    "n128: physical root residual": true,
    "n128: full conserved primitive roundtrip": true,
    "n128: no state floor or retry": true,
    "n128: actual magnetic wave present": true,
    "n128: intermediate wave errors": true,
    "n256: fixed final time": true,
    "n256: five saved times": true,
    "n256: four records per SSP step": true,
    "n256: all stored arrays finite": true,
    "n256: positive stage density": true,
    "n256: positive stage pressure": true,
    "n256: subluminal stages": true,
    "n256: positive reconstructed face density": true,
    "n256: positive reconstructed face pressure": true,
    "n256: subluminal reconstructed faces": true,
    "n256: conserved finite-volume boundary budget": true,
    "n256: physical root residual": true,
    "n256: full conserved primitive roundtrip": true,
    "n256: no state floor or retry": true,
    "n256: actual magnetic wave present": true,
    "n256: intermediate wave errors": true,
    "finest transverse L1": true,
    "finest wave phase": true,
    "finest wave amplitude": true,
    "minimum observed grid order": true,
    "wave refinement 1": true,
    "wave refinement 2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/index.json

![Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- L. Del Zanna, O. Zanotti, N. Bucciantini and P. Londrillo (2007). ECHO: a Eulerian Conservative High Order scheme for general relativistic magnetohydrodynamics and magnetodynamics. https://arxiv.org/abs/0704.3206; review_level=primary-original-selected-section-and-rendered-pages
Read original journal section4.1 equations82–85 via the university repository; rendered and visually inspected original preprint pages9–10, including normalization and period. No ECHO-algorithm reproduction.

- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
Read official author-review sections3.1–3.2, stress tensor49–51 and recovery68–69; flat-spacetime use only.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
