# Euler二重膨張波 / Euler double rarefaction

https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/

## 日本語

[公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#double-rarefaction)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

#### Euler二重膨張波：段階ごとの正値性

補助実行例 · 実行例の定義・検証式

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。

### 厳密解・参照解

左右状態(1,-2,0.4)と(1,2,0.4)、γ=1.4の低密度中央状態を持つ半解析的Riemann解が基準です。真空生成の別初期値とは区別します。

#### [Euler／二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-double-rarefaction)

半解析解 · 関連モデルの参照

U(x,t) = R((x−x0)/t)

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

#### Euler二重膨張波：段階ごとの正値性

27単体検査と3格子73判定を実行前に固定します。スケーリング前に生じる負の端点圧力を保持し、制限後の端点・前進Euler平均・SSP凸結合平均、θ、全3保存量の境界流束収支を別々に測ります。閉形式の対称希薄波と既存の独立な対数圧力根探索を照合し、保存量のGauss8/16セル平均との誤差と格子細分化を記録します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja)

### 計算法

従来のGodunov／HLLEプレビューと、追加のMUSCL・Lax–Friedrichs・平均保存スケーリング・SSPRK(3,3)固定入力は別の実行例です。段階正値性の条件は追加版の説明・契約・全段ログに限定します。

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLE／Einfeldt波速](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Lax–Friedrichs法](https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [平均を保つ正値状態スケーリング](https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja)

補助実行例

既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。

γ1.4、x∈[0,1]、x0=.5、左右状態(ρ,u,p)=(1,−2,.4)/(1,2,.4)、T=.15を固定します。中心の密度・圧力は小さいものの正で、真空生成例ではありません。大域LF分離速度a=4、dt·a/dx≤.4を固定し、実際の全端点の|u|+c≤aと十分条件dt·a/dx≤1/2を確認します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

この一つのP1有限体積更新と固定入力の検証です。一般のMUSCL/WENO/DG、特性再構築、反射壁、真空生成、2D/3Dの正値性を認証しません。空間再構築は無制限中央傾きで、TVD・最大値原理・無振動性を保証しません。生の端点圧力は密度が正の端点だけで評価し、密度≤0は別に数えます。圧力参照は保存量セル平均から評価するp(q̄)で、平均圧力とは異なります。ギャラリー図は保存した1次元場のx–t表示であり、2次元流体計算ではありません。ExactPackや別のPDEエンジンを実行した例ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23-r2/euler-positivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/run.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_benchmark_default_horizon_smoke`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_numerics.py -k test_benchmark_default_horizon_smoke
```

## English

[Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#double-rarefaction-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

#### Euler double rarefaction: positivity at every stage

Supplementary execution example · Example definition or validation formula

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.

### Exact and reference solutions

Use the semi-analytic Riemann solution for states (1,-2,0.4) and (1,2,0.4), γ=1.4, with a low-density middle state. Distinguish the separate vacuum-generating data.

#### [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-double-rarefaction)

Semi-analytic reference · Related-model reference

U(x,t) = R((x−x0)/t)

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

#### Euler double rarefaction: positivity at every stage

Freeze 27 unit tests and 73 gates over three grids before execution. Retain negative raw endpoint pressures, then separately measure limited endpoints, FE means, SSP convex means, theta and all three boundary-flux conservation budgets. Cross-check the closed symmetric fan against the prior independent logarithmic-pressure root evaluator; record errors/refinement against conserved Gauss8/16 cell means.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en)

### Numerical methods

The earlier Godunov/HLLE preview and the new MUSCL/Lax–Friedrichs/mean-preserving-scaling/SSPRK(3,3) run are separate execution records. Stage-positivity conditions are scoped to the additional release, its contract and all-stage diagnostics.

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLE / Einfeldt wave speeds](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Lax–Friedrichs](https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Mean-preserving positive-state scaling](https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en)

Supplementary execution example

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.

Fix gamma1.4, x in [0,1], discontinuity x0=.5, outer primitive states(1,-2,.4)/(1,2,.4) and T=.15. The low-density central state remains strictly positive; this is not a vacuum-generating case. Use fixed global LF splitting speed a4 and dt*a/dx<=.4; assert every actual endpoint satisfies |u|+c<=a and the sufficient dt*a/dx<=1/2 condition.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Evidence covers this one P1 FV update and fixed input, not general MUSCL/WENO/DG, characteristic reconstruction, reflecting walls, vacuum generation or multidimensional positivity. Unlimited central slopes have no TVD, maximum-principle or nonoscillation guarantee. Raw pressure is evaluated only where raw density is positive; nonpositive raw density has its own count. Reference pressure is p(mean conserved q), not mean pressure. Gallery plots are saved one-dimensional x-t fields, not two-dimensional flow. No ExactPack or separate PDE engine is executed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23-r2/euler-positivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/run.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_benchmark_default_horizon_smoke`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_numerics.py -k test_benchmark_default_horizon_smoke
```
