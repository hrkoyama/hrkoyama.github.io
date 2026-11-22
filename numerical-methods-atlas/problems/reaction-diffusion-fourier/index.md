# 反応拡散：空間2次と時間4次を分けて測る / Reaction-diffusion: separate second-order space and fourth-order time

https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/

## 日本語

[周期Fourierモードの線形反応拡散。16/32/64格子の連続解誤差と、固定格子での半離散厳密解に対する時間誤差を分けた保存収束図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#reaction-diffusion-fourier) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#reaction-diffusion-fourier)

### 方程式・問題の定義

線形反応拡散u_t=D u_xx+r u（公開入力はD=0.1、r=0.1）です。熱方程式へのリンクは拡散部分で、反応項を含む固有値r-Dk²で比較します。

#### [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja)

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

#### 反応拡散：空間2次と時間4次を分けて測る

補助実行例 · 実行例の定義・検証式

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

### 厳密解・参照解

線形反応拡散の連続Fourier解と半離散Fourier解を分け、空間2次・時間4次の収束を確認します。純拡散カードの指数率をそのまま使いません。

#### 反応拡散：空間2次と時間4次を分けて測る

連続固有値r-Dk²への最大誤差で空間次数、半離散固有値r-4Dsin²(kdx/2)/dx²への最大誤差で時間次数を測ります。独立した解析参照であり同じ実装の細格子値を参照にしません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja)

補助実行例

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

周期区間[0,2pi)、D=0.1、r=0.1、初期cos(2x)、終了t=2。格子16/32/64と、別の固定格子で刻み0.5/0.25/0.125を用います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

線形・周期・滑らかな単一モードだけを検証します。非線形のFisher前線、複雑境界、空間生態系や一般の反応ネットワークの検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)

## English

[Stored linear periodic Fourier reaction–diffusion refinement separates continuum errors on 16/32/64 grids from temporal errors against a fixed-grid semidiscrete exact solution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#reaction-diffusion-fourier) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#reaction-diffusion-fourier-en)

### Equations and problem definitions

Linear reaction-diffusion u_t=D u_xx+r u, with published D=0.1 and r=0.1. The heat link covers diffusion; compare using the eigenvalue r-Dk² including reaction.

#### [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en)

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

#### Reaction-diffusion: separate second-order space and fourth-order time

Supplementary execution example · Example definition or validation formula

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

### Exact and reference solutions

Separate continuous and semidiscrete Fourier solutions of linear reaction-diffusion to check second-order space/fourth-order time. Do not reuse the pure-diffusion card's decay rate unchanged.

#### Reaction-diffusion: separate second-order space and fourth-order time

Measure spatial order against r-Dk² and temporal order against r-4Dsin²(kdx/2)/dx². Both are independent analytic references, rather than a finer-grid run of the same solver.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en)

Supplementary execution example

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

Periodic[0,2pi), D=0.1,r=0.1, initial cos(2x), final t=2. Use grids 16/32/64 and a separate fixed-grid timestep sequence 0.5/0.25/0.125.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Only a linear, periodic, smooth single mode is verified. Nonlinear Fisher fronts, complex boundaries, spatial ecosystems and general reaction networks remain outside scope.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
