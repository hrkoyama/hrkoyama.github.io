# 無軟化Kepler二体の時間誤差 / Unsoftened Kepler two-body time error

https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/

## 日本語

[固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-gravity-dynamics/#gravity-kepler) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#gravity-kepler)

### 方程式・問題の定義

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。

#### [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

#### 無軟化Kepler二体の時間誤差

補助実行例 · 実行例の定義・検証式

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

### 厳密解・参照解

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

#### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-measurements)

解析解 · 同じ問題の参照

E-e*sin(E)=n*t; r=a*(cos(E)-e,sqrt(1-e^2)*sin(E),0); v=a*n/(1-e*cos(E))*(-sin(E),sqrt(1-e^2)*cos(E),0).

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

#### 無軟化Kepler二体の時間誤差

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja)

### 計算法

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja)

補助実行例

非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)

## English

[Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-gravity-dynamics/#gravity-kepler) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#gravity-kepler-en)

### Equations and problem definitions

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.

#### [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

#### Unsoftened Kepler two-body time error

Supplementary execution example · Example definition or validation formula

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

### Exact and reference solutions

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

#### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-measurements)

Analytic reference · Reference for the same problem

E-e*sin(E)=n*t; r=a*(cos(E)-e,sqrt(1-e^2)*sin(E),0); v=a*n/(1-e*cos(E))*(-sin(E),sqrt(1-e^2)*cos(E),0).

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

#### Unsoftened Kepler two-body time error

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en)

### Numerical methods

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en)

Supplementary execution example

Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)
