# 硬球DSMCの有限Kn Couette流 / Hard-sphere DSMC finite-Kn Couette flow

https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/

## 日本語

[保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dsmc-wall/#dsmc-couette) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#dsmc-couette)

### 方程式・問題の定義

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。

#### [剛体球Boltzmann輸送と壁・流入出](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja)

$$
\partial_t f+v_x\partial_x f=Q_{\rm HS}(f,f)
$$

$$
\sigma=1/\sqrt2,\quad\lambda(n)=1/(\sqrt2n\sigma)
$$

1D空間・3D速度の単原子気体。速度依存の剛体球衝突、壁の流束分布と開境界を実時間で扱います。

#### 硬球DSMCの有限Kn Couette流

補助実行例 · 実行例の定義・検証式

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

### 厳密解・参照解

各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。

#### [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja#dsmc-couette-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。 各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

#### 硬球DSMCの有限Kn Couette流

各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja)

### 計算法

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja)

補助実行例

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。壁温1、壁速度±.5。16セル、N=1024、dt=.02、burn20/sample40、4seed。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/dsmc-wall/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/run.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_core.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_core.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py)

## English

[Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-wall/#dsmc-couette) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#dsmc-couette-en)

### Equations and problem definitions

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,1],"speeds":[-0.5,0.5]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

#### [Hard-sphere Boltzmann transport,walls and reservoirs](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en)

$$
\partial_t f+v_x\partial_x f=Q_{\rm HS}(f,f)
$$

$$
\sigma=1/\sqrt2,\quad\lambda(n)=1/(\sqrt2n\sigma)
$$

1D space,3D velocity monatomic gas. Physical-time speed-dependent hard-sphere collisions,wall flux distributions and open reservoirs.

#### Hard-sphere DSMC finite-Kn Couette flow

Supplementary execution example · Example definition or validation formula

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

### Exact and reference solutions

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

#### [Finite-Kn hard-sphere Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-measurements)

Finite-grid numerical reference · Reference for the same problem

partial_t f+v_x partial_x f=Q_HS(f,f); sigma=pi*d^2=1/sqrt(2); lambda0=1; n,u,T,Pxx,Pxy,qx from pooled molecular moments.

H=2lambda0; diffuse Twalls1, tangential Uwalls+/-0.5; nonlinear viscous heating retained. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs.

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

#### Hard-sphere DSMC finite-Kn Couette flow

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en)

### Numerical methods

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en)

Supplementary execution example

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,1],"speeds":[-0.5,0.5]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/dsmc-wall/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/run.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_core.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_core.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py)
