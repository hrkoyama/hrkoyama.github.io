# 一様圧力と線形音波：SPH/GSPHの粒子配置依存 / Uniform pressure and acoustics: particle-layout effects in SPH/GSPH

https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/

## 日本語

[規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/#sph-pressure-acoustics) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#sph-pressure-acoustics)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

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

### 厳密解・参照解

固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

#### [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-measurements)

解析解 · 同じ問題の参照

\rho=1+A\sin[2\pi(x-t)],\quad v=A\sin[2\pi(x-t)],\quad p=1/\gamma+A\sin[2\pi(x-t)]; A=10^{-3},\quad c=1,\quad\text{linearized reference only; nonlinear remainder }O(A^2)

t=0.2、位置を揺らした128粒子のGSPHです。初期kernel再構成誤差は0.011834に達し、音波振幅0.001を上回って左の密度波形に残ります。右図はその初期誤差です。合格条件は基本Fourierモードの位相・振幅と固定した保存検査であり、各点の高精度や一般的な優位性ではありません。

固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

#### 一様圧力と線形音波：SPH/GSPHの粒子配置依存

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja)

### 計算法

GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

- [Godunov SPH／GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [SPHカーネル再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja)

補助実行例

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

## English

[Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/#sph-pressure-acoustics) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#sph-pressure-acoustics-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

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

### Exact and reference solutions

Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

#### [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-measurements)

Analytic reference · Reference for the same problem

\rho=1+A\sin[2\pi(x-t)],\quad v=A\sin[2\pi(x-t)],\quad p=1/\gamma+A\sin[2\pi(x-t)]; A=10^{-3},\quad c=1,\quad\text{linearized reference only; nonlinear remainder }O(A^2)

GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

#### Uniform pressure and acoustics: particle-layout effects in SPH/GSPH

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en)

### Numerical methods

GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

- [Godunov SPH / GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [SPH kernel reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en)

Supplementary execution example

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)
