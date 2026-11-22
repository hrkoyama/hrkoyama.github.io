# CTとGLM：同条件の独立照合・格子・時間収束

数値流束族・LLF係数・時間刻み・物理減衰率を固定し、CTとGLMの離散化を比較します。構成した滑らかな厳密解と独立Athena++参照を使い、格子誤差・時間積分誤差・参照自身の差を分けて確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## CT・GLM：移動する磁気静力学平衡の格子・時間収束

非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。

**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-algorithm)

両法とも区分定数・同じ固定Rusanov速度α=3・前進Eulerです。CTは面Bと共有算術corner EMF、GLMはcell B/ψとch=3・物理減衰率κ=2を使用。全格子で同じ384刻み、両法のdt列も同一です。CT面平均から復元した初期cell BとGLM初期Bが一致します。

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CT・GLM：移動する磁気静力学平衡の格子・時間収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja) (`advected-magnetostatic-equilibrium`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-validation)

16²/32²/64²の保存変数L1/L2/L∞誤差と観測次数を測ります。最細格子の刻み倍増差を空間誤差の.1以下と比較。時間収束は固定8²で16/32/64/128刻みを、許容誤差・最大刻みを二重に細分したDOP853へ照合します。質量・E、正値性、native CT divと共通cell div、ψも記録します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

周期単位正方形、γ=5/3、μ₀=1、平面MHD。A=.05[cos2π(x−.3t)+cos2π(y−.2t)]、B=(Ay,−Ax)、ρ=1、v=(.3,.2)、p=.1+(2π)²A²/2、t=.1。保存変数の解析的セル平均を比較します。公刊の標準問題名を借りない構成検証例です。

**編集上の補足**

この滑らかな移流平衡はアトラスで構成した厳密解です。保存量のセル平均を比較し、そのセル平均から回復する圧力と圧力自体の厳密なセル平均を区別します。同じ半離散空間演算子に別の時間積分を適用した参照は、時間誤差の照合であり独立PDEソルバーとは呼びません。

### 採用した計算法

両法とも区分定数・同じ固定Rusanov速度α=3・前進Eulerです。CTは面Bと共有算術corner EMF、GLMはcell B/ψとch=3・物理減衰率κ=2を使用。全格子で同じ384刻み、両法のdt列も同一です。CT面平均から復元した初期cell BとGLM初期Bが一致します。

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

### 比較・検証

16²/32²/64²の保存変数L1/L2/L∞誤差と観測次数を測ります。最細格子の刻み倍増差を空間誤差の.1以下と比較。時間収束は固定8²で16/32/64/128刻みを、許容誤差・最大刻みを二重に細分したDOP853へ照合します。質量・E、正値性、native CT divと共通cell div、ψも記録します。

### 確認の限界

定数LLF粘性・周期中心演算子では、GLMのdiv=ψ=0部分空間は丸めまで保たれます。本例は結合MHDの精度を調べ、能動的cleaningは別の非物理診断対照で調べます。p(q平均)はpの厳密平均と同一ではありません。DOP853は時間だけ独立で空間RHSは共有します。刻み倍増差は経験的汚染目安で厳密誤差上界ではなく、CT/GLMの内部表現差を含む有限離散化全体の比較です。

### 保存実測値と判定

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.030434862760674048,
    "ct_minimum_spatial_order": 0.8792002695252499,
    "ct_time_contamination_ratio": 0.00042240836130500326,
    "ct_finest_temporal_scaled_l2": 0.00028691666346522787,
    "ct_minimum_temporal_order": 1.003588237880181,
    "ct_time_reference_to_primary_ratio": 1.0480281669324549e-12,
    "glm_finest_spatial_error": 0.053272941712543334,
    "glm_minimum_spatial_order": 0.8519970902037858,
    "glm_time_contamination_ratio": 0.0002497746629066176,
    "glm_finest_temporal_scaled_l2": 0.0006005455648426271,
    "glm_minimum_temporal_order": 1.004074134741654,
    "glm_time_reference_to_primary_ratio": 4.049255315353574e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_order": true,
    "ct_continuum_error": true,
    "ct_common_divergence_bounded": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_order": true,
    "glm_continuum_error": true,
    "glm_common_divergence_bounded": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

### 出典と確認範囲

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
  通常のGLMのB/ψ式と減衰、エネルギー保存、追加のEGLM項との区別を原著の選択式で確認しました。全文監査ではありません。
- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
  面平均Bと共有corner EMFの構造を確認しました。今回の算術flux-CTを、論文のupwind CT・CTU実装そのものとは呼びません。
- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
  div B制約手法の比較という原著の主題と書誌を確認しました。今回の数値判定や新しい構成例の出典とはしません。
- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
  DOP853を別の時間積分器として実行します。空間RHSを共有するため、独立した空間離散化とは呼びません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束

同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja#ct-glm-ot-convergence-ja-algorithm)

主計算は固定α=ch=3のRusanovと前進Euler、GLMκ=2は格子に依存しません。独立C++ Athena++はHLLD・PLM・RK2・upwind CTです。同じ連続初期値を用いますが、Athenaのface/primitive離散化は主計算と完全同一ではありません。

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja#ct-glm-ot-convergence-ja-validation)

密度・磁場L1誤差、格子改善、正値性、保存量とdiv/ψを測定。Athena256²/512²はともにCFL=.15、512²のCFL=.3/.15差で参照の時間感度を確認し、両増分が主計算誤差の.1以下か判定します。主計算の固定16²での時間収束を別実行DOP853へ照合し、最細格子の刻み倍増差も確認します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

標準周期OT、γ=5/3、ρ=25/(36π)、p=5/(12π)、v=(−sin2πy,sin2πx)、B=(−sin2πy,sin4πx)/√(4π)、t=.05。16²/32²/64²の両法に192刻みを共用します。旧配布版を改変しない追加検証です。

**編集上の補足**

共通の数値流束族・速度上限・時間刻み・物理減衰率を固定しますが、CTの面磁場とGLMのセル磁場、法線磁場の扱いは異なります。離散化全体の比較であり、差のすべてを発散処理だけの効果とはしません。CT固有の面発散と共通のセル中心発散は別の演算子として報告します。

### 採用した計算法

主計算は固定α=ch=3のRusanovと前進Euler、GLMκ=2は格子に依存しません。独立C++ Athena++はHLLD・PLM・RK2・upwind CTです。同じ連続初期値を用いますが、Athenaのface/primitive離散化は主計算と完全同一ではありません。

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

### 比較・検証

密度・磁場L1誤差、格子改善、正値性、保存量とdiv/ψを測定。Athena256²/512²はともにCFL=.15、512²のCFL=.3/.15差で参照の時間感度を確認し、両増分が主計算誤差の.1以下か判定します。主計算の固定16²での時間収束を別実行DOP853へ照合し、最細格子の刻み倍増差も確認します。

### 確認の限界

短時間の滑らかなOTで、衝撃波後・3D・一般のcleaning性能の認証ではありません。独立Athena参照も有限格子数値解で、増分は誤差上界ではありません。旧128²/CFL.3は履歴だけで256²/CFL.15との組を純粋な格子次数に使いません。定数LLFによるGLMのdiv=ψ=0保存をcleaning成功とは呼びません。native面divと共通中心divを区別し、中心演算子のcheckerboard盲点も残します。

### 保存実測値と判定

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.04131948399815993,
    "ct_minimum_spatial_order": 0.7441584435125685,
    "ct_time_contamination_ratio": 0.005452472133120275,
    "ct_finest_temporal_scaled_l2": 0.0006451024853786959,
    "ct_minimum_temporal_order": 1.0051663785429696,
    "ct_time_reference_to_primary_ratio": 4.610829174194673e-13,
    "glm_finest_spatial_error": 0.06851242841151672,
    "glm_minimum_spatial_order": 0.6819406396313236,
    "glm_time_contamination_ratio": 0.003289333276474019,
    "glm_finest_temporal_scaled_l2": 0.0007617954701608142,
    "glm_minimum_temporal_order": 1.0056569861410107,
    "glm_time_reference_to_primary_ratio": 3.179752402329314e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "independent_reference_density_refinement": true,
    "independent_reference_magnetic_refinement": true,
    "independent_reference_time_refinement": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_refinement": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_independent_reference_resolved": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_independent_reference_resolved": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

### 出典と確認範囲

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
  通常のGLMのB/ψ式と減衰、エネルギー保存、追加のEGLM項との区別を原著の選択式で確認しました。全文監査ではありません。
- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
  面平均Bと共有corner EMFの構造を確認しました。今回の算術flux-CTを、論文のupwind CT・CTU実装そのものとは呼びません。
- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
  div B制約手法の比較という原著の主題と書誌を確認しました。今回の数値判定や新しい構成例の出典とはしません。
- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official source at pinned commit actually compiled/executed; paper metadata
  以前に別構築しハッシュを確認した公式commit1395e2f543f4368d448cb1a2cf92ba1f910e3416のC++バイナリーを再利用して新しい参照を実行し、入力・出力・binary/source SHAを保存しました。論文全文監査ではありません。
- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
  DOP853を別の時間積分器として実行します。空間RHSを共有するため、独立した空間離散化とは呼びません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## CTの初期制約保持とGLMの能動的cleaning：非物理診断対照

故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。

**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja#ct-glm-constraint-control-ja-algorithm)

同じ完全結合MHDコードを使用。y不変・By=vy=0ではGLMのBx/ψ系が流体応答から独立するため、離散Fourier記号の2×2行列と前進Euler行列冪を別に構成します。κ=2とκ=0を同じdt・LLF粘性で比較し、Bxだけの減少を物理減衰と取り違えません。

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CTの初期制約保持とGLMの能動的cleaning：非物理診断対照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja#ct-glm-constraint-control-ja-validation)

CT native divの初期違反保持、GLMのψ励起、Bx/ψ双方の独立FE参照一致、密度・圧力正値性、物理的総E/質量保存を確認。補助波エネルギーW=〈Bx²+ψ²/ch²〉のκ2/κ0比を判定し、半離散行列指数と連続Fourier解も区別して表示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

32²周期格子、t=.1、128刻み、ρ=p=1、v=0、By=ψ=0。CT face Bx=.01cos[2π(i+1)/32]、GLM cell Bxはその左右face平均と同一です。CT初期native div≠0は意図的に無効な物理初期値で、CTの正しい物理計算例とは区別します。

**編集上の補足**

発散制約を意図的に破った初期場を共通のセル磁場として与える診断です。正当な発散ゼロ初期条件のCT計算とは区別し、CTが初期制約誤差を保持する性質を確認します。GLMは減衰なしの対照とも比較し、磁場とpsiの波エネルギーを使って輸送の位相変化や数値拡散を物理減衰と混同しません。

### 採用した計算法

同じ完全結合MHDコードを使用。y不変・By=vy=0ではGLMのBx/ψ系が流体応答から独立するため、離散Fourier記号の2×2行列と前進Euler行列冪を別に構成します。κ=2とκ=0を同じdt・LLF粘性で比較し、Bxだけの減少を物理減衰と取り違えません。

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

### 比較・検証

CT native divの初期違反保持、GLMのψ励起、Bx/ψ双方の独立FE参照一致、密度・圧力正値性、物理的総E/質量保存を確認。補助波エネルギーW=〈Bx²+ψ²/ch²〉のκ2/κ0比を判定し、半離散行列指数と連続Fourier解も区別して表示します。

### 確認の限界

対照の合格は「期待したCTの非除去とGLMの線形応答を正しく検出した」という意味です。非零CT divを許す物理計算を推奨しません。Wは診断用ノルムで、ψを含まない物理的総エネルギーEとは別です。GLMのBx減少には位相交換とLLF拡散も含まれ、κ0対照なしに減衰成功とは呼びません。一般非線形・境界流出・衝撃波のcleaning性能へ広げません。

### 保存実測値と判定

```json
{
  "metrics": {
    "damped_to_undamped_B_psi_wave_energy_ratio": 0.797707175433604,
    "ct_native_divergence_linf_change": 0.0,
    "ct_common_divergence_linf_change": 1.457167719820518e-16,
    "initial_common_divergence_l2": 0.04393133573771591,
    "initial_cell_state_difference": 4.7704895589362195e-18
  },
  "checks": {
    "ct_preserves_initial_constraint_defect": true,
    "ct_does_not_clean_common_initial_defect": true,
    "ct_initial_constraint_is_deliberately_nonzero": true,
    "damped_independent_discrete_fourier_agreement": true,
    "damped_positive_states": true,
    "damped_conservative_mass_energy": true,
    "damped_psi_is_activated": true,
    "glm_final_B_divergence_reduced": true,
    "undamped_independent_discrete_fourier_agreement": true,
    "undamped_positive_states": true,
    "undamped_conservative_mass_energy": true,
    "undamped_psi_is_activated": true,
    "physical_damping_separated_from_phase_and_LLF_viscosity": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "matched_initial_cell_states": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

### 出典と確認範囲

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
  通常のGLMのB/ψ式と減衰、エネルギー保存、追加のEGLM項との区別を原著の選択式で確認しました。全文監査ではありません。
- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
  面平均Bと共有corner EMFの構造を確認しました。今回の算術flux-CTを、論文のupwind CT・CTU実装そのものとは呼びません。
- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
  div B制約手法の比較という原著の主題と書誌を確認しました。今回の数値判定や新しい構成例の出典とはしません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
