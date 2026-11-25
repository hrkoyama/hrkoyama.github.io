# Schnakenberg：2D境界と初期モード / Schnakenberg:2D boundaries and initial modes

https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/

## 日本語

[2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。 短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-space-controls/#schnakenberg-2d-boundary-modes) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#schnakenberg-2d-boundary-modes)

### 方程式・問題の定義

[0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。

#### [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja)

$$
u_t=D_u\Delta u+a-u+u^2v
$$

$$
v_t=D_v\Delta v+b-u^2v
$$

自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。この旧1次元例だけから一般の模様選択、生物実験への較正、流体連成へ広げません。 全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード

#### Schnakenberg：2D境界と初期モード

補助実行例 · 実行例の定義・検証式

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。

### 厳密解・参照解

線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。

#### [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v

[0,2π]²、T=2、a=0.1、b=0.9、Du=0.01、Dv=1。(1,0.9)からの3摂動、12/24/48セルと固定非周期境界を比較します。Neumannの単一・混合モードと、平衡Dirichlet境界の単一モードを区別します。

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

#### Schnakenberg：2D境界と初期モード

線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja)

### 計算法

セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。

- [Crank–Nicolson法](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja)

補助実行例

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。

[0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

## English

[Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references. This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-space-controls/#schnakenberg-2d-boundary-modes) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#schnakenberg-2d-boundary-modes-en)

### Equations and problem definitions

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.

#### [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en)

$$
u_t=D_u\Delta u+a-u+u^2v
$$

$$
v_t=D_v\Delta v+b-u^2v
$$

A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. The earlier 1D case alone makes no general pattern-selection, biological-calibration or fluid-coupling claim. Not implementation of the entire model family. Fixed cases: Schnakenberg:2D boundaries and initial modes

#### Schnakenberg:2D boundaries and initial modes

Supplementary execution example · Example definition or validation formula

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.

### Exact and reference solutions

Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.

#### [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-measurements)

Finite-grid numerical reference · Reference for the same problem

u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions. Dimensionless square [0,2pi]², diffusion coefficients 0.01 and 1. Single/mixed Neumann modes and a single mode with equilibrium Dirichlet data.

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

#### Schnakenberg:2D boundaries and initial modes

Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en)

### Numerical methods

Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.

- [Crank–Nicolson](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en)

Supplementary execution example

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)
