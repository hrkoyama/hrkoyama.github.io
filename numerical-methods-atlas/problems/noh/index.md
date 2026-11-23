# Noh衝撃波：初期圧力ゼロの平面・円筒対称計算 / Noh shocks: zero-pressure planar and cylindrical flow

https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/

## 日本語

[内向きに収束する流れが、外向きに進む衝撃波を作ります。円筒対称の1次元有限体積密度を回転表示し、厳密なセル平均と比較します。独立した2次元Euler計算ではありません。初期圧力ゼロ、γ=5/3、512セル、t=0.6。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-noh/#noh-shock) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#noh)

### 方程式・問題の定義

理想気体Eulerの平面(d=1)・円筒対称半径方向(d=2)のNoh流入問題。幾何源・冷たい外境界・反射原点と真のp0=0の扱いは実行例で確認できます。

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

#### Noh衝撃波：初期圧力ゼロの平面・円筒対称計算

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
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。

### 厳密解・参照解

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

#### [Nohの冷たい流入衝撃波：平面・円筒対称](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements)

解析解 · 同じ問題の参照

s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.

理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)と円筒対称の半径方向(d=2)の有限体積計算で、圧力の床は使いません。カラー図は1次元の半径方向解を回転表示したもので、Cartesianの2次元計算ではありません。

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

#### Noh衝撃波：初期圧力ゼロの平面・円筒対称計算

入力・受入基準・hashを初回実行前に保存。セル平均圧力p_iΔAを使った初回は平面のみ合格し、円筒はshock不形成で不合格。そのソース・全系列結果を保持し、同じ閾値でinterface-stress版を再実行しました。厳密保存量セル平均は衝撃をまたぐ積分を解析的に分割し、p(U平均)と圧力の体積平均を別列に保存。独立LANL ExactPack固定版から点値・分割求積平均を別実行して照合。全域の相対体積重みL1/L2/Linfと、原点・衝撃・plateauのマスク別診断、shock半値位置、密度増幅4^d（衝撃自体の跳躍は4）、SSPRK2各段の境界流入を積算した保存収支を検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja)

### 計算法

新しい専用配布版は区分定数Rusanov流束とSSPRK2/Heunを使用します。旧Eulerモジュールを圧力床で変更したものではなく、半径方向の面応力を用いる独自の整合的一次源項を検証します。

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja)

補助実行例

圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。

無次元r∈[0,1]、gamma=5/3、rho0=1、u0=-1、p0=0、T=.6。平面d=1と円筒半径対称d=2だけをPDE実行し、衝撃半径は.2。外側はrho(1,t)=1+tの円筒低温流入（平面は1）。原点は反射、体積測度r^(d-1)dr、角度因子は全ての収支から共通に省きます。球対称の解析参照検査とCartesian 2D Euler計算を混同しません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

空間一次・衝撃捕獲の教育用ソルバーです。最細円筒でもplateau密度誤差と原点過熱が残り、中心最大誤差のゼロ収束・正値性の一般証明・高次精度・Cartesian多次元・球対称PDE・任意gammaの独立照合を主張しません。全域誤差から原点を除外せず、中心過熱を合格のために隠しません。質量/エネルギー収支だけでは解の正しさを証明できないことを初回失敗で示します。ExactPackは解析参照の独立実装であり、独立PDEエンジンではありません。 円筒の全域密度L∞はこの系列では単調減少しません。収束の合格判定は事前に指定した体積重みL1で行い、L∞も隠さず保存します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23-r3/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/run.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/test_noh.py)

## English

[Inward converging flow generates an outward moving shock. Revolved density from a 1D cylindrical-radial finite-volume calculation, compared with exact cell means. This is not an independent 2D Euler calculation. Zero initial pressure, gamma=5/3, 512 cells, t=0.6.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh/#noh-shock) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#noh-en)

### Equations and problem definitions

Planar(d=1) and cylindrical-radial(d=2) ideal-gas Euler Noh inflow, with geometric source, cold outer boundary, reflecting origin and exactly p0=0 as specified in the example.

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

#### Noh shocks: zero-pressure planar and cylindrical flow

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
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.

### Exact and reference solutions

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

#### [Noh cold-inflow shock: planar and cylindrical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements)

Analytic reference · Reference for the same problem

s=(gamma-1)/2=1/3; rho2=4^d; u2=0; p2=4^d/3; r_s=t/3; upstream rho=(1+t/r)^(d-1), u=-1, p=0.

Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1) and cylindrically symmetric radial (d=2) finite-volume calculations; no pressure floor. The radial color image is a revolved one-dimensional solution, not a two-dimensional Cartesian computation.

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

#### Noh shocks: zero-pressure planar and cylindrical flow

Inputs, acceptance criteria and hashes were saved before the first run. The initial cell-pressure p_i delta A source passed planar checks but failed cylindrical shock formation; its source and full refinement results are retained. The interface-stress revision is tested against the SAME thresholds. Analytic conservative cell means split shock-crossing integrals, storing p(mean U) separately from the physical mean pressure. Pinned independent LANL ExactPack was separately executed for points and split-quadrature means. Checks include full-domain volume-weighted relative L1/L2/Linf, explicit center/shock/plateau masks, pressure half-height shock location, initial density amplification 4^d (shock jump 4), and stage-weighted SSPRK2 boundary-inflow budgets.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en)

### Numerical methods

The new dedicated edition uses piecewise-constant Rusanov flux with SSPRK2/Heun. It does not alter the older Euler module with a pressure floor; it checks an original consistent first-order radial face-stress source.

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en)

Supplementary execution example

A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.

Nondimensional r in [0,1], gamma=5/3, rho0=1, u0=-1, p0=0 and T=.6. PDE executions are only planar d=1 and cylindrical-radial d=2, with shock radius .2. Outer cold density is 1+t for cylindrical flow, 1 for planar flow. Reflecting origin, measure r^(d-1)dr, with the same angular factor omitted throughout. Neither geometry-3 analytic-reference checks nor a revolved display are Cartesian 2D Euler simulations.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

An educational first-order-space shock-capturing solver. Plateau density error and origin heating remain even on the finest cylindrical grid. No claim of vanishing center maximum error, a general positivity proof, high-order accuracy, Cartesian multidimensional or spherical PDE execution, or independent validation for arbitrary gamma. The center remains in full-domain errors and heating is not hidden to pass. The retained initial failure shows why mass/energy balance alone does not prove the solution correct. ExactPack is an independent implementation of the analytic reference, not an independent PDE engine. Full-domain cylindrical density Linf does not decrease monotonically in this series. The convergence gate uses the predeclared volume-weighted L1; Linf is retained without concealment.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23-r3/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/run.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r3/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r3/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/test_noh.py)
