# 円偏波Alfvén波 / Circularly polarized Alfvén wave

https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/

## 日本語

[保存済み円偏波Alfvén波の誤差・収束比較。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#circular-alfven)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

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

#### 円偏波Alfvén波：全成分の格子収束

補助実行例 · 実行例の定義・検証式

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。

### 厳密解・参照解

円偏光Alfvén波の解析解を、一定の全エネルギーを含む保存変数セル平均で評価します。 実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。

#### [円偏波Alfvén波：全保存変数の解析セル平均](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-measurements)

解析解 · 関連モデルの参照

sinc(h)=sin(pi*h)/(pi*h); theta=2*pi*(x-t); (Bybar,Bzbar)=.1*sinc(h)*(cos(theta),sin(theta)); (mybar,mzbar)=-(Bybar,Bzbar); rhobar=Bxbar=1; Ebar=.66.

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。横磁場と横運動量にはsinc(h)を掛け、E=.66を保ちます。独立Gauss16求積と照合します。図のx–tは1次元空間と保存時刻であり、斜め2次元伝播ではありません。

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

#### 円偏波Alfvén波：全成分の格子収束

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja)

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [HLLE／Einfeldt波速](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja)

補助実行例

全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。1次元整列波の次数であり、斜め2次元伝播の検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/run.py)
- [/code/validated-examples/2026-11-24/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-24/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py)
- [/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py)

## English

[Stored circularly polarized Alfvén-wave comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#circular-alfven-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

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

#### Circular Alfven wave: full-state refinement

Supplementary execution example · Example definition or validation formula

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

### Exact and reference solutions

Evaluate the analytic circularly polarized Alfvén wave using conserved cell averages, including its constant total energy. Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.

#### [Circular Alfven wave: analytic full-state conserved cell means](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-measurements)

Analytic reference · Related-model reference

sinc(h)=sin(pi*h)/(pi*h); theta=2*pi*(x-t); (Bybar,Bzbar)=.1*sinc(h)*(cos(theta),sin(theta)); (mybar,mzbar)=-(Bybar,Bzbar); rhobar=Bxbar=1; Ebar=.66.

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure. Apply sinc(h) to transverse magnetic fields and momenta, retaining E=.66, and qualify against independent Gauss16 quadrature. The x-t picture shows one spatial dimension and saved times, not oblique2D propagation.

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

#### Circular Alfven wave: full-state refinement

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en)

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [HLLE / Einfeldt wave speeds](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en)

Supplementary execution example

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. The observed order is for a 1D aligned wave, not oblique 2D propagation.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/run.py)
- [/code/validated-examples/2026-11-24/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-24/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py)
- [/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py)
