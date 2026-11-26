# 無軟化Kepler二体の時間誤差 / Unsoftened Kepler two-body time error

https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/

## 日本語

[固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-gravity-dynamics/#gravity-kepler) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#gravity-kepler)

### 方程式・問題の定義

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

#### [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

#### [Kepler二体問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kepler-two-body-ja)

$$
\dot q=p,\qquad\dot p=-q/\|q\|^3,\qquad H=\tfrac12p^Tp-1/\|q\|
$$

無次元化した平面楕円軌道で位相、角運動量、エネルギーと刻みの影響を分けます。

#### [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

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

#### 離心率を変えたKepler軌道と時間刻み

補助実行例 · 実行例の定義・検証式

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。

### 厳密解・参照解

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。

#### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-measurements)

解析解 · 同じ問題の参照

E-e*sin(E)=n*t; r=a*(cos(E)-e,sqrt(1-e^2)*sin(E),0); v=a*n/(1-e*cos(E))*(-sin(E),sqrt(1-e^2)*cos(E),0).

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。 位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。 1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

#### [離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-measurements)

半解析解 · 同じ問題の参照

\ddot q=-q/\|q\|^3;\quad E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E);\quad H=\tfrac12\|p\|^2-1/\|q\|

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。

#### 無軟化Kepler二体の時間誤差

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja)

#### 離心率を変えたKepler軌道と時間刻み

独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja)

### 計算法

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。 独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の動径速度での交差をbrentqで局在化。

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

#### [離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja)

補助実行例

e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)

## English

[Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-gravity-dynamics/#gravity-kepler) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#gravity-kepler-en)

### Equations and problem definitions

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

#### [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

#### [Kepler two-body problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kepler-two-body-en)

$$
\dot q=p,\qquad\dot p=-q/\|q\|^3,\qquad H=\tfrac12p^Tp-1/\|q\|
$$

Nondimensional planar ellipses separate phase, angular momentum, energy and step-selection effects.

#### [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

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

#### Kepler eccentricity and time-step controls

Supplementary execution example · Example definition or validation formula

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.

### Exact and reference solutions

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals. An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.

#### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-measurements)

Analytic reference · Reference for the same problem

E-e*sin(E)=n*t; r=a*(cos(E)-e,sqrt(1-e^2)*sin(E),0); v=a*n/(1-e*cos(E))*(-sin(E),sqrt(1-e^2)*cos(E),0).

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

#### [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-measurements)

Semi-analytic reference · Reference for the same problem

\ddot q=-q/\|q\|^3;\quad E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E);\quad H=\tfrac12\|p\|^2-1/\|q\|

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.

#### Unsoftened Kepler two-body time error

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en)

#### Kepler eccentricity and time-step controls

An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en)

### Numerical methods

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities. Original central-force KDK Verlet. Fixed, replayed and regenerated schedules are distinct. Positive radial crossings of cubic Hermite trajectories are localized by brentq.

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

#### [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en)

Supplementary execution example

Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)
