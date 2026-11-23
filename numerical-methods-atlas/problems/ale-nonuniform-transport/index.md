# 非一様移動格子で実際に運ぶALEスカラー / ALE scalar transport on genuinely nonuniform moving cells

https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/

## 日本語

[実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-moving-waves/#ale-nonuniform-transport) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#ale-nonuniform-transport)

### 方程式・問題の定義

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。

#### [移動セル上のALEスカラー保存式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja)

$$
q_t+a q_x=0,\quad m_i(t)=\int_{x_{i-1/2}(t)}^{x_{i+1/2}(t)}q(x,t)\,dx
$$

$$
\dot m_i=-[(a-w)q]_{i-1/2}^{i+1/2},\qquad \dot V_i=w_{i+1/2}-w_{i-1/2}
$$

$$
x(\xi,t)=\xi+\frac{.2}{2\pi}\sin(2\pi\xi)\sin(2\pi t),\quad a=.7
$$

指定した非一様格子の面位置とセル質量を同じHeun段で更新し、幾何保存則と非一様な波の輸送を別々に評価します。Euler流体のLagrange/remap法ではありません。

#### 非一様移動格子で実際に運ぶALEスカラー

補助実行例 · 実行例の定義・検証式

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。

### 厳密解・参照解

解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。

#### [ALE：実際の移動セル上の解析積分と時間参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-measurements)

解析解 · 同じ問題の参照

x(xi,t)=xi+.2*sin(2*pi*xi)*sin(2*pi*t)/(2*pi); m_i=integral_[x_i,x_(i+1)](1+.2*sin(2*pi*(x-.7*t)))dx.

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。解析解q(x,t)=1+.2sin[2π(x−.7t)]を、主計算が保存した実際の面位置の間で積分します。解析面位置との幾何誤差を別記し、時間検査は同じFV ODEを二公差の独立DOP853で解きます。

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

#### 非一様移動格子で実際に運ぶALEスカラー

解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja)

### 計算法

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

- [ALE一様状態・幾何保存モデル](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja)

補助実行例

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

## English

[Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/#ale-nonuniform-transport) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#ale-nonuniform-transport-en)

### Equations and problem definitions

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.

#### [ALE scalar conservation on moving cells](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en)

$$
q_t+a q_x=0,\quad m_i(t)=\int_{x_{i-1/2}(t)}^{x_{i+1/2}(t)}q(x,t)\,dx
$$

$$
\dot m_i=-[(a-w)q]_{i-1/2}^{i+1/2},\qquad \dot V_i=w_{i+1/2}-w_{i-1/2}
$$

$$
x(\xi,t)=\xi+\frac{.2}{2\pi}\sin(2\pi\xi)\sin(2\pi t),\quad a=.7
$$

Prescribed nonuniform face positions and cell masses share Heun stages. Evaluate geometric conservation and nonuniform-wave transport separately; this is not an Euler-fluid Lagrange/remap scheme.

#### ALE scalar transport on genuinely nonuniform moving cells

Supplementary execution example · Example definition or validation formula

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.

### Exact and reference solutions

Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.

#### [ALE: analytic moving-cell integrals and separate time reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-measurements)

Analytic reference · Reference for the same problem

x(xi,t)=xi+.2*sin(2*pi*xi)*sin(2*pi*t)/(2*pi); m_i=integral_[x_i,x_(i+1)](1+.2*sin(2*pi*(x-.7*t)))dx.

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps. Integrate q(x,t)=1+.2sin[2pi(x-.7t)] between the actual saved primary faces. Separately record geometry error against analytic face positions. Time checks use independent DOP853 at two tolerances for the same FV ODE.

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

#### ALE scalar transport on genuinely nonuniform moving cells

Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en)

### Numerical methods

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

- [ALE uniform-state / geometric-conservation model](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en)

Supplementary execution example

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
