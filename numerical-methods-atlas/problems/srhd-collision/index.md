# SRHDの対称二衝撃波衝突 / SRHD symmetric two-shock collision

https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/

## 日本語

[最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-relativistic/#srhd-collision) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#srhd-collision)

### 方程式・問題の定義

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。

#### [特殊相対論的流体（SRHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja)

$$
\partial_\mu(\rho_0u^\mu)=0,\qquad\partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p\eta^{\mu\nu}
$$

c=1、平坦なCartesian時空の理想流体。γ則EOSと原始変数回復を使う穏やかな対称二衝撃波の固定例を追加。一般三波Riemann解、極端なLorentz因子、一般相対論を検証したとはしません。

#### SRHDの対称二衝撃波衝突

補助実行例 · 実行例の定義・検証式

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

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

### 厳密解・参照解

群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。

#### [相対論的対称衝突：特殊化した二衝撃波Taub参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-measurements)

半解析解 · 同じ問題の参照

h_b^2-h_a^2=(p_b-p_a)*(h_b/rho_b+h_a/rho_a); v0^2=(p_b-p_a)*(e_b-e_a)/((e_a+p_b)*(e_b+p_a)); shock positions=.5 +/- Vs*t.

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。Taub断熱式と相対速度式の圧力根から静止した同一星状態と衝撃波速度を求め、保存変数の区分一定厳密場をセル積分します。接触面は退化し、一般三波Riemannソルバーではありません。

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

#### SRHDの対称二衝撃波衝突

群全体25pytest、6固定計算、110判定と参照6検査を事前固定。全量境界収支、各段・再構築面の正値と亜光速、D/E細分化、星領域圧力、衝撃波位置、反射対称性を検査。実際の最終状態を独立なSRHD圧力根と流束でも照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja)

### 計算法

同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja)

補助実行例

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

c=1、γ=5/3、ρ=1、p=.1、左右v=±.3、B=0。区間[0,1]、初期不連続x=.5、t=.3、96/192/384セル。衝撃波が端へ届く前の外挿境界です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)

## English

[Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-relativistic/#srhd-collision) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#srhd-collision-en)

### Equations and problem definitions

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.

#### [Special-relativistic hydrodynamics (SRHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en)

$$
\partial_\mu(\rho_0u^\mu)=0,\qquad\partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=\rho_0h u^\mu u^\nu+p\eta^{\mu\nu}
$$

Ideal fluid in flat Cartesian spacetime,c=1. Add a mild fixed symmetric two-shock example with gamma-law EOS and primitive recovery; no general three-wave Riemann,extreme-Lorentz-factor or GR claim.

#### SRHD symmetric two-shock collision

Supplementary execution example · Example definition or validation formula

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

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

### Exact and reference solutions

Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.

#### [Relativistic symmetric collision: specialized two-shock Taub reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-measurements)

Semi-analytic reference · Reference for the same problem

h_b^2-h_a^2=(p_b-p_a)*(h_b/rho_b+h_a/rho_a); v0^2=(p_b-p_a)*(e_b-e_a)/((e_a+p_b)*(e_b+p_a)); shock positions=.5 +/- Vs*t.

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints. Solve the pressure root from Taub adiabat and relative-velocity relations for the identical resting star states and shock speeds, then integrate the piecewise-constant exact conserved field over cells. The contact degenerates; this is not a general three-wave Riemann solver.

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

#### SRHD symmetric two-shock collision

Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en)

### Numerical methods

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en)

Supplementary execution example

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)
