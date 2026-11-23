# Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算 / Noh shocks: zero-pressure planar, cylindrical and spherical flow

https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/

## 日本語

[内向き流入から外向きに進むNoh衝撃波。球対称1Dの密度セル平均を中心断面として表示し、厳密セル平均と比較します。Cartesianの3D計算ではありません。γ=5/3、初期圧力ゼロ、512セル、t=0.6。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-noh/#noh-shock) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#noh)

### 方程式・問題の定義

理想気体Eulerの平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)のNoh流入問題。幾何源、冷たい流入、反射原点、p0=0と境界時間求積は実行例で定義します。

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

#### Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算

補助実行例 · 実行例の定義・検証式

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

### 厳密解・参照解

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

#### [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements)

解析解 · 同じ問題の参照

s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.

理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)の有限体積計算で、圧力の床は使いません。球のカラー図は1次元半径データの中心断面で、Cartesianの3次元計算ではありません。

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

#### Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算

旧平面・円筒の受入基準と59判定を保持し、球の追加基準・入力・ソースhashを初回の球PDE実行前に保存します。初回の円筒不合格はソース・全8本の診断ログ・不合格サマリーを保持し、同じ基準で面応力版を再検証した履歴です。厳密保存量セル平均は衝撃をまたぐ積分を分割し、p(平均U)と平均pを分けます。固定版LANL ExactPackの独立解析照合はd=1/2/3を含みます。球の新規PDE系列では全域r²重みL1/L2/L∞、原点を含むr≤.70rsの密度L1、原点・衝撃・plateauを別測定。各段の境界流入による離散保存収支と、連続解析総量との差を分け、M_h−M_exact=Σdt³/6、E_h−E_exact=Σdt³/12というSSPRK2境界求積の恒等式を検査します。 最初の球対称実行は旧算術平均源のまま105条件中2条件で不合格（最細衝撃位置3.923セル、plateau密度誤差11.03%）となり、全結果を保存しました。第2試行は球の面応力求積だけを変更しましたが、同じ2条件が未達（衝撃位置3.919セル、密度誤差11.018%）でした。第3試行はその求積を保ち、球だけMUSCL・minmod再構築を加えて、同じ105条件で比較します。 第3試行は28検査と全12格子計算を完了し、105条件すべてに合格しました。球N=512では全域密度L1=.0114343、衝撃位置誤差1.98856セル、plateau密度誤差5.2533%、原点込みcore密度L1=.0549503です。一方、中心最大比内部エネルギーの相対過剰は20.59%で、第2試行の15.52%より悪化しており、全指標の改善は主張しません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja)

### 計算法

全系列でRusanov流束とHeunを使います。平面・円筒は区分定数、球だけ体積重心でのMUSCL/minmodと線形面応力の球殻求積を使用し、同じ105条件で不合格の定数再構築2系列とも比較します。

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja)

補助実行例

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

無次元r∈[0,1]、γ=5/3、ρ0=1、u0=-1、p0=0、T=.6。平面d=1・円筒半径対称d=2・球半径対称d=3をPDE実行し、衝撃半径は.2。外側密度は(1+t)^(d-1)、原点は反射、体積測度r^(d-1)dr。角度因子をすべての収支から共通に省き、球の解析総量はM=512/375、E=256/375です。球の図は1D半径解の中心断面で、Cartesianの2D/3D計算や角度方向の対称性破れの検証ではありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

平面・円筒は空間一次、球はMUSCL型の制限線形再構築を使う教育用計算です。原点過熱と有限格子のplateau誤差が残り、全域誤差から原点を除外しません。r²重みで中心欠陥が小さく見えるため、原点を含む固定coreの誤差と拡大図も示します。L∞や中心最大誤差のゼロ収束、滑らかな球問題での方式全体の高次精度、幾何源付き全RK段階の一般の正値性保証、Cartesian多次元、任意γの独立照合は検証していません。円筒L∞は旧系列で単調減少せず、球のL2/L∞と過熱も診断値として保持します。球の離散質量・エネルギー収支が丸め誤差でも、解析総量との差は境界時間求積のO(dt²)となります。半径方向の運動量には幾何源があり、保存されるCartesian運動量とは異なります。ExactPackは解析評価器の独立実装で、別の数値PDEエンジンではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)

## English

[Inward flow generates an outward Noh shock. A central section of spherical 1D density cell means is compared with exact cell means. This is not a Cartesian 3D calculation. Gamma=5/3, zero initial pressure, 512 cells, t=0.6.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh/#noh-shock) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#noh-en)

### Equations and problem definitions

Planar(d=1), cylindrical-radial(d=2) and spherical-radial(d=3) ideal-gas Euler Noh inflow. The example defines the geometric source, cold inflow, reflecting origin, exactly p0=0 and boundary-time quadrature.

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

#### Noh shocks: zero-pressure planar, cylindrical and spherical flow

Supplementary execution example · Example definition or validation formula

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

### Exact and reference solutions

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

#### [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements)

Analytic reference · Reference for the same problem

s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.

Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1), cylindrical-radial (d=2) and spherical-radial (d=3) finite-volume calculations without a pressure floor. The spherical color picture is a central section of one-dimensional radial data, not a Cartesian three-dimensional computation.

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

#### Noh shocks: zero-pressure planar, cylindrical and spherical flow

Retain the planar/cylindrical acceptance file and all 59 original decisions, and save spherical criteria, inputs and source hashes before the first spherical PDE run. The initial cylindrical failure retains its source, all eight diagnostic logs and failed summary; the face-stress revision was tested against the same gates. Analytic conserved means split shock-crossing integrals and distinguish p(mean U) from mean p. The pinned independent LANL ExactPack analytic comparison includes d=1/2/3. New spherical PDE refinements separately measure full-domain r^2-weighted L1/L2/Linf, density L1 in r<=.70rs including the origin, and center/shock/plateau diagnostics. Discrete stage-weighted inflow budgets are distinct from continuous analytic totals; SSPRK2 boundary quadrature is checked through M_h-M_exact=sum(dt^3)/6 and E_h-E_exact=sum(dt^3)/12. The first spherical run retained arithmetic source quadrature and failed two of 105 gates (finest shock-position error 3.923 cells, plateau-density error 11.03%); all results are retained. A second attempt changed only spherical stress quadrature, but still failed the same two gates (3.919 cells and 11.018% density error). A third attempt retains that quadrature and adds MUSCL/minmod reconstruction only for spherical runs, against the same 105 criteria. The third attempt completed 28 tests and all 12 grid runs, passing all 105 gates. At spherical N=512 the whole-domain density L1 is .0114343, shock error 1.98856 cells, plateau-density error 5.2533%, and origin-inclusive core-density L1 .0549503. Maximum center specific-internal-energy excess is 20.59%, worse than the second attempt's 15.52%; not every diagnostic improves.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en)

### Numerical methods

All series use Rusanov flux and Heun. Planar/cylindrical reconstruction is piecewise constant; spherical runs use volume-centroid MUSCL/minmod and radial quadrature of face-linear stress, compared with two failed constant-reconstruction baselines under the same 105 gates.

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en)

Supplementary execution example

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

Nondimensional r in [0,1], gamma=5/3, rho0=1, u0=-1, p0=0, T=.6. PDE runs use planar d=1, cylindrical-radial d=2 and spherical-radial d=3, with shock radius .2. Outer density is (1+t)^(d-1), the origin reflects, and the measure is r^(d-1)dr. The same angular factor is omitted throughout; spherical analytic totals are M=512/375 and E=256/375. Its figure is a central section of a 1D radial solution, not a Cartesian 2D/3D calculation or a test of angular symmetry breaking.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

An educational calculation: first-order space in planar/cylindrical flow and MUSCL-type limited linear reconstruction in spherical flow. Origin heating and finite-grid plateau errors remain; the center is never removed from whole-domain error. Because r^2 weighting can make central defects appear small, an origin-inclusive fixed-core norm and enlarged view are also shown. Vanishing Linf/center maximum error, high order for the complete method on smooth spherical problems, general stage positivity with the geometric source, Cartesian multidimensional flow and independent arbitrary-gamma validation are not established. Cylindrical Linf was not monotone in the old series; spherical L2/Linf and heating are retained as diagnostics. Roundoff-scale discrete mass/energy balance coexists with O(dt^2) spherical boundary-time-quadrature error against analytic totals. Radial momentum has a geometric source and is not a conserved Cartesian momentum component. ExactPack independently implements the analytic evaluator, not another numerical PDE engine.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)
