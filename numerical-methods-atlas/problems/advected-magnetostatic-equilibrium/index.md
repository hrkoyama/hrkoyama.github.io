# CT・GLM：移動する磁気静力学平衡の格子・時間収束 / CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium

https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/

## 日本語

[非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd-convergence/#ct-glm-smooth-convergence) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#advected-magnetostatic-equilibrium)

### 方程式・問題の定義

周期単位正方形・γ=5/3・μ0=1の平面理想MHDを扱います。構成した磁気静力学平衡を一定速度で移流する厳密解で、外力による製造解や標準円偏光Alfvén波とは異なります。GLMの補助方程式と具体的な保存変数セル平均は、実行例の式・入力・コードを参照してください。

#### [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。

#### CT・GLM：移動する磁気静力学平衡の格子・時間収束

補助実行例 · 実行例の定義・検証式

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

非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。

### 厳密解・参照解

構成厳密解の保存変数セル平均と格子誤差を比較します。固定した空間RHSを独立DOP853時間積分で解いた参照は時間誤差の確認用であり、別の空間ソルバーとは呼びません。18件の既存参照解ライブラリにはこの構成解のカードがないため、別問題の参照カードを流用せず、該当実行例の式・結果・ソースへ案内します。

#### CT・GLM：移動する磁気静力学平衡の格子・時間収束

16²/32²/64²の保存変数L1/L2/L∞誤差と観測次数を測ります。最細格子の刻み倍増差を空間誤差の.1以下と比較。時間収束は固定8²で16/32/64/128刻みを、許容誤差・最大刻みを二重に細分したDOP853へ照合します。質量・E、正値性、native CT divと共通cell div、ψも記録します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja)

### 計算法

この問題に明示的に対応するct-glm-smooth-convergence配布例のCTとGLMです。同じLLF係数と時間刻みを使っても、磁場配置・角電場平均・法線場の扱いが異なる離散系全体の比較です。この発散ゼロの物理例を、別の非物理制約対照で測った能動的なcleaning性能と同一視しません。

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja)

補助実行例

非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。

周期単位正方形、γ=5/3、μ₀=1、平面MHD。A=.05[cos2π(x−.3t)+cos2π(y−.2t)]、B=(Ay,−Ax)、ρ=1、v=(.3,.2)、p=.1+(2π)²A²/2、t=.1。保存変数の解析的セル平均を比較します。公刊の標準問題名を借りない構成検証例です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

定数LLF粘性・周期中心演算子では、GLMのdiv=ψ=0部分空間は丸めまで保たれます。本例は結合MHDの精度を調べ、能動的cleaningは別の非物理診断対照で調べます。p(q平均)はpの厳密平均と同一ではありません。DOP853は時間だけ独立で空間RHSは共有します。刻み倍増差は経験的汚染目安で厳密誤差上界ではなく、CT/GLMの内部表現差を含む有限離散化全体の比較です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/mhd-convergence/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/solver.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/experiments.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/run.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py)

## English

[Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-convergence/#ct-glm-smooth-convergence) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#advected-magnetostatic-equilibrium-en)

### Equations and problem definitions

Planar ideal MHD on a periodic unit square with gamma=5/3 and mu0=1. The exact solution translates a constructed magnetostatic equilibrium at constant velocity; it is neither a forced manufactured solution nor the standard circularly polarized Alfvén wave. The execution example supplies the GLM auxiliary equation and explicit conserved cell averages.

#### [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests.

#### CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium

Supplementary execution example · Example definition or validation formula

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

Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.

### Exact and reference solutions

Compare spatial errors against conserved cell averages of the constructed exact solution. Independent DOP853 integration of the same fixed spatial RHS checks temporal error and is not a separate spatial solver. The existing 18-case reference-solution library has no card for this constructed solution, so use the bound example’s equations, results and source rather than borrowing another problem’s reference card.

#### CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium

Measure conserved-variable L1/L2/Linf errors and observed orders at16²/32²/64². Compare finest-grid step doubling with.1 of the spatial error. At fixed8², compare16/32/64/128 steps with doubly refined DOP853 tolerances/max steps. Record mass/E, positivity, native CT divergence, common cell divergence and psi.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en)

### Numerical methods

CT and GLM are explicitly bound by the ct-glm-smooth-convergence release example. Matching LLF coefficients and time steps still compares whole discretizations with different magnetic placement, corner EMF averaging and normal-field handling. This solenoidal physical example is distinct from active-cleaning measurements in the separate nonphysical constraint control.

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en)

Supplementary execution example

Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.

Periodic unit square, gamma5/3, mu0=1, planar MHD. A=.05[cos2pi(x−.3t)+cos2pi(y−.2t)], B=(Ay,−Ax), rho1, v=(.3,.2), p=.1+(2pi)²A²/2 at t=.1. Compare analytic conserved cell averages. This is a constructed verification case, not a claimed published standard benchmark.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

With constant LLF viscosity and periodic centered operators, the GLM div=psi=0 subspace remains invariant up to roundoff. This tests coupled-MHD accuracy; a separate nonphysical control activates cleaning. p(q-average) is not the exact averaged p. DOP853 is independent in time only and shares the spatial RHS. Step differences are empirical contamination indicators, not rigorous bounds; face/cell representation differences remain part of the comparison.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/mhd-convergence/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/solver.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/experiments.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/run.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py)
