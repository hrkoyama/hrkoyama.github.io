# Sedov–Taylorの点爆発 / Sedov–Taylor point blast

https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/

## 日本語

[1次元球対称Eulerの保存済み半径密度を中心断面に表示。γ=5/3、E=ρ0=1、p0=0、t=.05、512球殻、有限投入半径.03。半解析的な点源参照との違いと衝撃層の誤差を残した図で、実2D Cartesian計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-sedov/#sedov-blast) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#sedov)

### 方程式・問題の定義

無次元の球半径対称Euler系。1D半径方向の密度・運動量・全エネルギーを体積重み付きで発展させます。

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

#### Sedov–Taylor点爆発：球対称の軽量検証

補助実行例 · 実行例の定義・検証式

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

### 厳密解・参照解

エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

#### [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-measurements)

半解析解 · 同じ問題の参照

R_s(t)=beta*(E0*t^2/rho0)^(1/5), beta≈1.15166641793; D=2*R_s/(5*t); rho=rho0*G(r/R_s), u=D*V(r/R_s), p=rho0*D^2*P(r/R_s).

理想気体Eulerの球半径対称、γ=5/3、周囲密度1・圧力0、爆発エネルギー1、r∈[0,1]、t=0.05。自己相似参照は瞬間的な理想点源を表しますが、有限体積計算は半径0.03の内部へ投入し、同じ最細格子で半径0.015も比較します。参照は相似ODEの数値積分、小さな中心域の正則漸近形、衝撃位置で分割する球殻求積を含む半解析解であり、閉形式の厳密セル平均ではありません。ギャラリー図は1次元球半径データの中心断面で、2D Cartesian計算ではありません。固定投入半径での誤差には点源とのモデル差が含まれ、その傾きは純粋な空間収束次数ではなく、投入半径の変更も感度診断に留まります。

エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

#### Sedov–Taylor点爆発：球対称の軽量検証

入力・数値ソース・受入基準・22テストを初回計算前にhash固定し、22単体検査と全4計算・48判定が初回から合格しました。参照は独立な相似ODEのDOP853積分、エネルギー規格化、中心ξ<.001の正則漸近形と衝撃位置で分割する殻求積です。16/32点求積・中心cutoff/ODE公差を別々に確認。固定commitの未改変ExactPackを6001/12001点で別実行し、中心とジャンプから離れた点を事前基準5e-4で照合しました。β=1.15166641793、Rs(.05)=.34746791233。原点・衝撃波を含むr≤1.2Rsの体積重み密度L1は.17257/.12785/.07458、圧力L1は.18148/.13939/.07615。512セルの衝撃位置誤差は1.096セル、最大離散収支残差は約1.34e-15です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja)

### 計算法

区分定数のRusanov有限体積流束とSSPRK2/Heunを使う限定した球半径例です。

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja)

補助実行例

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

無次元、γ=5/3、初期密度1・速度0・背景圧力0、半径[0,1]、総注入エネルギー1、T=.05。球内一様の熱エネルギーを各殻の切断体積で正確に配分します。注入半径0.03を3格子で共通にし、512セルでは半径0.015の別実行も保存します。原点は鏡映、外端は流出境界で、実際の境界流束を収支へ含めます。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/atlas-sedov-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

有限の注入球と理想点爆発は初期条件が異なり、報告誤差には注入モデルと離散化の両方が含まれます。傾きは純粋な空間精度次数ではありません。同じ512セルで注入半径を半分にした密度差は約.000451、圧力差は約.000619ですが、点爆発参照への誤差は僅かに悪化し、改善や点源極限の証明とは扱いません。圧力誤差は数値p(保存量のセル平均)と参照の物理圧力平均を比較し、参照平均保存量からの圧力と区別します。中心密度・圧力・最大誤差を除外せず保存します。最細密度ピークは約2.918で厳密ジャンプ4を解像しきりません。冷たい裾の極小波速では局所CFL比が浮動小数点overflowで∞になりますが、制限しない比として扱い、選ばれる全体刻みの有限性・正値性を検査します。原点漸近部は近似で、ExactPack点照合もξ<.15を除きます。2D/3D Cartesian、一般摂動・非球対称性、高次精度は未検証です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/sedov/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/run.py)
- [/code/validated-examples/2026-11-23/sedov/sedov_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/sedov_solver.py)
- [/code/validated-examples/2026-11-23/sedov/reference_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/reference_sedov.py)
- [/code/validated-examples/2026-11-23/sedov/test_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/test_sedov.py)

## English

[A central-section view of saved one-dimensional spherical-radial Euler density:gamma5/3,E=rho0=1,p0=0,t=.05,512 shells and finite deposition radius.03. Point-source reference differences and shock errors remain visible; this is not an actual2D Cartesian computation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-sedov/#sedov-blast) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#sedov-en)

### Equations and problem definitions

Nondimensional spherical-radial Euler flow, evolving radial density, momentum and total energy with volume weighting.

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

#### Sedov–Taylor point blast: lightweight spherical-radial validation

Supplementary execution example · Example definition or validation formula

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

### Exact and reference solutions

An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.

#### [Sedov–Taylor point blast: energy-normalized spherical similarity solution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-measurements)

Semi-analytic reference · Reference for the same problem

R_s(t)=beta*(E0*t^2/rho0)^(1/5), beta≈1.15166641793; D=2*R_s/(5*t); rho=rho0*G(r/R_s), u=D*V(r/R_s), p=rho0*D^2*P(r/R_s).

Ideal-gas Euler in spherical radial symmetry, gamma=5/3, ambient rho0=1 and p0=0, explosion energy E0=1, r in [0,1], t=0.05. The similarity reference describes ideal instantaneous point deposition. Finite-volume runs instead deposit energy inside radius 0.03, with a paired radius-0.015 sensitivity calculation. The reference uses a numerical similarity-ODE integration, a tiny-core regular asymptote and split shell quadrature; it is semi-analytic, not closed-form exact cell means. The gallery picture is a central section of one-dimensional spherical-radial data, not a two-dimensional Cartesian computation. Fixed-radius errors include point-source model discrepancy, so their refinement slope is not a pure spatial order; the paired-radius calculation is only a sensitivity diagnostic.

An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.

#### Sedov–Taylor point blast: lightweight spherical-radial validation

Inputs, numerical sources, acceptance and22 tests were hash-locked before the first FV execution. All22 unit tests and48 gates on four calculations passed on the first attempt. The independent reference integrates the similarity ODE with DOP853, normalizes energy, uses a regular asymptote for xi<.001 and split shell quadrature at the shock. Orders16/32, core cutoff and ODE tolerance are checked separately. The unmodified pinned ExactPack evaluator was independently run at6001/12001 points and compared away from the center/jump with its preregistered5e-4 criterion. Beta=1.15166641793, Rs(.05)=.34746791233. Origin/shock-inclusive volume-weighted density L1 within r<=1.2Rs is.17257/.12785/.07458 and pressure L1 is.18148/.13939/.07615. Finest shock error is1.096 cells; maximum relative discrete-budget residual is about1.34e-15.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en)

### Numerical methods

A scoped spherical-radial example using piecewise-constant Rusanov finite-volume fluxes and SSPRK2/Heun.

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en)

Supplementary execution example

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

Nondimensional gamma=5/3, ambient density1, velocity0, pressure0, radius[0,1], deposited energy1, T=.05. Uniform thermal energy inside a sphere is assigned using exact cut-shell volumes. Deposition radius0.03 is shared by all three grids; a separate512-cell run uses0.015. The origin is reflecting and the outer boundary is outflow; actual boundary fluxes enter measured budgets.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/atlas-sedov-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A finite deposition sphere and an ideal point blast have different initial data; reported errors combine deposition-model and discretization effects. The refinement slope is not a pure spatial order. Halving the source radius at the same512 cells changes density by about.000451 and pressure by.000619, but point-reference errors become slightly worse; no improvement or point-source-limit proof is claimed. Pressure compares numerical p(mean conserved U) with reference mean physical pressure, distinct from p(mean reference U). Center values and maximum errors remain reported. The finest density peak is about2.918 versus the exact jump4. Extremely small cold-tail wave speeds can overflow a local CFL ratio to infinity; it is unrestrictive, and the chosen global timestep is checked finite. The regular tiny-core continuation is approximate, and ExactPack point probes exclude xi<.15. Cartesian2D/3D, general perturbations/asymmetry and high-order accuracy are unverified.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/sedov/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/run.py)
- [/code/validated-examples/2026-11-23/sedov/sedov_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/sedov_solver.py)
- [/code/validated-examples/2026-11-23/sedov/reference_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/reference_sedov.py)
- [/code/validated-examples/2026-11-23/sedov/test_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/test_sedov.py)
