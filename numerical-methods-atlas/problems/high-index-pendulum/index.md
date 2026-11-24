# 拘束付き振り子 / Constrained planar pendulum

https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/

## 日本語

[位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dae-controls/#high-index-pendulum) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#high-index-pendulum)

### 方程式・問題の定義

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

#### [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja)

$$
\dot q=p,\quad\dot p=(0,-1)-\lambda q,\quad q^Tq=1,\quad q^Tp=0
$$

元の位置拘束DAE、微分した拘束に基づくODE、SHAKE/RATTLEの離散写像を区別します。

#### [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

#### 振り子の指数低減・拘束ドリフト・明示安定化

補助実行例 · 実行例の定義・検証式

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

#### SHAKEとRATTLE：拘束と運動量の違い

補助実行例 · 実行例の定義・検証式

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。

### 厳密解・参照解

Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。 独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。

#### [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-measurements)

半解析解 · 同じ問題の参照

C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q);\quad Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

#### [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-measurements)

半解析解 · 同じ問題の参照

C(q)=\tfrac12(q^Tq-1)=0;\quad q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n;\quad q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

#### 振り子の指数低減・拘束ドリフト・明示安定化

Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja)

#### SHAKEとRATTLE：拘束と運動量の違い

独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja)

### 計算法

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [SHAKE拘束積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [RATTLE拘束積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja)

補助実行例

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

#### [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja)

補助実行例

単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)

## English

[Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dae-controls/#high-index-pendulum) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#high-index-pendulum-en)

### Equations and problem definitions

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

#### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en)

$$
\dot q=p,\quad\dot p=(0,-1)-\lambda q,\quad q^Tq=1,\quad q^Tp=0
$$

Distinguish the original position-constrained DAE, an underlying ODE based on differentiated constraints, and the SHAKE/RATTLE discrete maps.

#### [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

#### Index reduction, constraint drift and explicit stabilization for a pendulum

Supplementary execution example · Example definition or validation formula

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

#### SHAKE and RATTLE: constraints and momentum ownership

Supplementary execution example · Example definition or validation formula

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.

### Exact and reference solutions

Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets. A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.

#### [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-measurements)

Semi-analytic reference · Reference for the same problem

C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q);\quad Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

#### [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-measurements)

Semi-analytic reference · Reference for the same problem

C(q)=\tfrac12(q^Tq-1)=0;\quad q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n;\quad q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

#### Index reduction, constraint drift and explicit stabilization for a pendulum

Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en)

#### SHAKE and RATTLE: constraints and momentum ownership

A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en)

### Numerical methods

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [SHAKE constrained integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [RATTLE constrained integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en)

Supplementary execution example

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

#### [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en)

Supplementary execution example

Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.

L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)
