# SRHDの対称二衝撃波衝突

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-algorithm)

同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

- [特殊相対論的流体（SRHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja) (`srhd`)

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。


**問題の図**

![SRHDの対称二衝撃波衝突：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) (`srhd-collision`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-validation)

群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。

- [相対論的対称衝突：特殊化した二衝撃波Taub参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja) (`srhd-collision`; 同じ問題の参照 · 半解析参照)

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。
## 前提・単位・境界

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。

**編集上の補足**

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

## 採用した計算法

同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

## 比較・検証

群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。

## 確認の限界

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

## 保存実測値と判定

```json
{
  "metrics": {
    "exact_star": {
      "pressure": 0.35473854747189193,
      "density": 2.036718245233174,
      "enthalpy": 1.4354290883166312,
      "speed": 0.3181655418651244,
      "relative_velocity": 0.3,
      "taub_residual": -3.3306690738754696e-16
    },
    "finest_D_l1": 0.0054242304454669415,
    "finest_E_l1": 0.005207375513692991,
    "exact_scope": "Symmetric identical thermodynamics, opposite normal velocities: two shocks and resting identical star states; no nontrivial contact or general three-wave certification."
  },
  "checks": {
    "n96: fixed final time": true,
    "n96: five saved times": true,
    "n96: four records per SSP step": true,
    "n96: all stored arrays finite": true,
    "n96: positive stage density": true,
    "n96: positive stage pressure": true,
    "n96: subluminal stages": true,
    "n96: positive reconstructed face density": true,
    "n96: positive reconstructed face pressure": true,
    "n96: subluminal reconstructed faces": true,
    "n96: conserved finite-volume boundary budget": true,
    "n96: physical root residual": true,
    "n96: full conserved primitive roundtrip": true,
    "n96: no state floor or retry": true,
    "n96: reflection symmetry": true,
    "n96: independent SRHD zero B flux and recovery": true,
    "n192: fixed final time": true,
    "n192: five saved times": true,
    "n192: four records per SSP step": true,
    "n192: all stored arrays finite": true,
    "n192: positive stage density": true,
    "n192: positive stage pressure": true,
    "n192: subluminal stages": true,
    "n192: positive reconstructed face density": true,
    "n192: positive reconstructed face pressure": true,
    "n192: subluminal reconstructed faces": true,
    "n192: conserved finite-volume boundary budget": true,
    "n192: physical root residual": true,
    "n192: full conserved primitive roundtrip": true,
    "n192: no state floor or retry": true,
    "n192: reflection symmetry": true,
    "n192: independent SRHD zero B flux and recovery": true,
    "n384: fixed final time": true,
    "n384: five saved times": true,
    "n384: four records per SSP step": true,
    "n384: all stored arrays finite": true,
    "n384: positive stage density": true,
    "n384: positive stage pressure": true,
    "n384: subluminal stages": true,
    "n384: positive reconstructed face density": true,
    "n384: positive reconstructed face pressure": true,
    "n384: subluminal reconstructed faces": true,
    "n384: conserved finite-volume boundary budget": true,
    "n384: physical root residual": true,
    "n384: full conserved primitive roundtrip": true,
    "n384: no state floor or retry": true,
    "n384: reflection symmetry": true,
    "n384: independent SRHD zero B flux and recovery": true,
    "finest D L1": true,
    "finest total E L1": true,
    "finest star pressure": true,
    "finest shock position": true,
    "collision component 0 refinement 1": true,
    "collision component 4 refinement 1": true,
    "collision component 0 refinement 2": true,
    "collision component 4 refinement 2": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/index.json

![最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。

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

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- Luciano Rezzolla and Olindo Zanotti (2001). An Improved Exact Riemann Solver for Relativistic Hydrodynamics. https://arxiv.org/abs/gr-qc/0103005; review_level=primary-selected-mathematical-sections
  原著プレプリントの2–4節、状態方程式、相対速度式3.1とTaub二次式4.5を直接確認。対称二衝撃波への特殊化です。
- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
  公式の著者レビュー3.1–3.2節、テンソル式49–51と変換式68–69を直接確認。平坦時空の実装に使用します。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# SRHD symmetric two-shock collision

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-algorithm)

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

- [Special-relativistic hydrodynamics (SRHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en) (`srhd`)

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.


**Problem figure**

![SRHD symmetric two-shock collision: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-validation)

Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.

- [Relativistic symmetric collision: specialized two-shock Taub reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en) (`srhd-collision`; Same-problem reference · Semi-analytic reference)

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.
## Assumptions, units and boundaries

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.

**Editorial clarification**

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

## Adopted numerical method

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

## References and validation

Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.

## Limits

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

## Stored measurements and decisions

```json
{
  "metrics": {
    "exact_star": {
      "pressure": 0.35473854747189193,
      "density": 2.036718245233174,
      "enthalpy": 1.4354290883166312,
      "speed": 0.3181655418651244,
      "relative_velocity": 0.3,
      "taub_residual": -3.3306690738754696e-16
    },
    "finest_D_l1": 0.0054242304454669415,
    "finest_E_l1": 0.005207375513692991,
    "exact_scope": "Symmetric identical thermodynamics, opposite normal velocities: two shocks and resting identical star states; no nontrivial contact or general three-wave certification."
  },
  "checks": {
    "n96: fixed final time": true,
    "n96: five saved times": true,
    "n96: four records per SSP step": true,
    "n96: all stored arrays finite": true,
    "n96: positive stage density": true,
    "n96: positive stage pressure": true,
    "n96: subluminal stages": true,
    "n96: positive reconstructed face density": true,
    "n96: positive reconstructed face pressure": true,
    "n96: subluminal reconstructed faces": true,
    "n96: conserved finite-volume boundary budget": true,
    "n96: physical root residual": true,
    "n96: full conserved primitive roundtrip": true,
    "n96: no state floor or retry": true,
    "n96: reflection symmetry": true,
    "n96: independent SRHD zero B flux and recovery": true,
    "n192: fixed final time": true,
    "n192: five saved times": true,
    "n192: four records per SSP step": true,
    "n192: all stored arrays finite": true,
    "n192: positive stage density": true,
    "n192: positive stage pressure": true,
    "n192: subluminal stages": true,
    "n192: positive reconstructed face density": true,
    "n192: positive reconstructed face pressure": true,
    "n192: subluminal reconstructed faces": true,
    "n192: conserved finite-volume boundary budget": true,
    "n192: physical root residual": true,
    "n192: full conserved primitive roundtrip": true,
    "n192: no state floor or retry": true,
    "n192: reflection symmetry": true,
    "n192: independent SRHD zero B flux and recovery": true,
    "n384: fixed final time": true,
    "n384: five saved times": true,
    "n384: four records per SSP step": true,
    "n384: all stored arrays finite": true,
    "n384: positive stage density": true,
    "n384: positive stage pressure": true,
    "n384: subluminal stages": true,
    "n384: positive reconstructed face density": true,
    "n384: positive reconstructed face pressure": true,
    "n384: subluminal reconstructed faces": true,
    "n384: conserved finite-volume boundary budget": true,
    "n384: physical root residual": true,
    "n384: full conserved primitive roundtrip": true,
    "n384: no state floor or retry": true,
    "n384: reflection symmetry": true,
    "n384: independent SRHD zero B flux and recovery": true,
    "finest D L1": true,
    "finest total E L1": true,
    "finest star pressure": true,
    "finest shock position": true,
    "collision component 0 refinement 1": true,
    "collision component 4 refinement 1": true,
    "collision component 0 refinement 2": true,
    "collision component 4 refinement 2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/index.json

![Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.

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

This command executes every fixed case in the distribution group.

## Sources and review scope

- Luciano Rezzolla and Olindo Zanotti (2001). An Improved Exact Riemann Solver for Relativistic Hydrodynamics. https://arxiv.org/abs/gr-qc/0103005; review_level=primary-selected-mathematical-sections
  Read original preprint sections2–4: EOS, relative-velocity equation3.1 and Taub quadratic4.5. Restricted symmetric two-shock specialization.
- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
  Read official author-review sections3.1–3.2, stress tensor49–51 and recovery68–69; flat-spacetime use only.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
