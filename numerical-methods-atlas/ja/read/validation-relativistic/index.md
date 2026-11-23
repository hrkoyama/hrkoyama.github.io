# SRHD衝突・SRMHD非線形Alfvén波

SRHDの対向衝突をTaub関係の二衝撃波解と、全7保存量SRMHDの有限振幅円偏波を独立テンソル式・保存量平均と比較します。空間は1次元で、図のx–t表示は2D流れではありません。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## SRHDの対称二衝撃波衝突

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
### 前提・単位・境界

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。

**編集上の補足**

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

### 採用した計算法

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

### 比較・検証

群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。

### 確認の限界

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Luciano Rezzolla and Olindo Zanotti (2001). An Improved Exact Riemann Solver for Relativistic Hydrodynamics. https://arxiv.org/abs/gr-qc/0103005; review_level=primary-selected-mathematical-sections
原著プレプリントの2–4節、状態方程式、相対速度式3.1とTaub二次式4.5を直接確認。対称二衝撃波への特殊化です。

- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
公式の著者レビュー3.1–3.2節、テンソル式49–51と変換式68–69を直接確認。平坦時空の実装に使用します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## SRMHDの有限振幅円偏極Alfvén波

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
### 前提・単位・境界

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。

**編集上の補足**

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

### 採用した計算法

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

### 比較・検証

非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。

### 確認の限界

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- L. Del Zanna, O. Zanotti, N. Bucciantini and P. Londrillo (2007). ECHO: a Eulerian Conservative High Order scheme for general relativistic magnetohydrodynamics and magnetodynamics. https://arxiv.org/abs/0704.3206; review_level=primary-original-selected-section-and-rendered-pages
大学リポジトリの原著4.1節・式82–85を読み、原著プレプリント9–10頁の式・規格化・周期を描画して目視確認。ECHO法自体の再現ではありません。

- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
公式の著者レビュー3.1–3.2節、テンソル式49–51と変換式68–69を直接確認。平坦時空の実装に使用します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
