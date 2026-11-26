# 可変エディントン因子：周期1D散乱源の固定検証 / Variable Eddington factor: a periodic 1D scattering-source control

https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/

## 日本語

[形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-variable-eddington-controls/#vef-fourier-scattering1d) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#vef-fourier-scattering1d)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [静止灰色輻射のVEF・VETモーメント閉包](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja)

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_t I=\sigma_s E+q,\quad E=\langle I\rangle
$$

$$
\nabla\cdot\boldsymbol H+\sigma_aE=q,\quad\sigma_t\boldsymbol H+\nabla\cdot(\mathsf D E)=0
$$

$$
\mathsf D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^{\mathsf T}I\rangle}{\langle I\rangle},\quad\sigma_a=\sigma_t-\sigma_s
$$

c=1、角度平均はdΩ/(4π)。1Dのスカラー因子と、2D空間・3D角度の全テンソルを同じモーメント系の変種として扱います。公開例は正の等方輻射源・一定係数・周期境界に限定します。

#### 可変エディントン因子：周期1D散乱源の固定検証

補助実行例 · 実行例の定義・検証式

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

### 厳密解・参照解

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

#### [本例のために導出した周期1D VEFの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-measurements)

解析解 · 同じ問題の参照

For k>0: R=atan(k/st)/k, A=b/(1-ss*R), B=(1-st*R)/k, C=st*(1-st*R)/k^2, T=(R-C)/2. E=E0+Re(sum A*R*exp(i*k.x)); H=Re(sum -i*A*B*khat*exp(i*k.x)); K=E0*I3/3+Re(sum A*(T*I3+(C-T)*khat*khat^T)*exp(i*k.x)); D=K/E; E0=qmean/(st-ss).

静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

#### 可変エディントン因子：周期1D散乱源の固定検証

N=33/65と固定32点角度則、N=65の64点角度プローブを分けます。解析場・複素モード・保存・実現可能性・反復残差・誤符号等の負制御、別のN=9一定源行を照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja)

### 計算法

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

- [可変Eddington因子（1D VEF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja)

補助実行例

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)

## English

[Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-variable-eddington-controls/#vef-fourier-scattering1d) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#vef-fourier-scattering1d-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Static grey VEF/VET moment closure](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en)

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_t I=\sigma_s E+q,\quad E=\langle I\rangle
$$

$$
\nabla\cdot\boldsymbol H+\sigma_aE=q,\quad\sigma_t\boldsymbol H+\nabla\cdot(\mathsf D E)=0
$$

$$
\mathsf D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^{\mathsf T}I\rangle}{\langle I\rangle},\quad\sigma_a=\sigma_t-\sigma_s
$$

c=1 with angular measure dOmega/(4pi). The scalar 1D factor and full tensor in 2D space/3D angle are variants of the same moment system. Released examples are limited to positive isotropic sources, constant coefficients and periodic boundaries.

#### Variable Eddington factor: a periodic 1D scattering-source control

Supplementary execution example · Example definition or validation formula

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

### Exact and reference solutions

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

#### [Authored continuum Fourier response for periodic 1D VEF](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-measurements)

Analytic reference · Reference for the same problem

For k>0: R=atan(k/st)/k, A=b/(1-ss*R), B=(1-st*R)/k, C=st*(1-st*R)/k^2, T=(R-C)/2. E=E0+Re(sum A*R*exp(i*k.x)); H=Re(sum -i*A*B*khat*exp(i*k.x)); K=E0*I3/3+Re(sum A*(T*I3+(C-T)*khat*khat^T)*exp(i*k.x)); D=K/E; E0=qmean/(st-ss).

Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu. Positive prescribed isotropic source; physical angle space remains S2.

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

#### Variable Eddington factor: a periodic 1D scattering-source control

Separate N=33/65 refinement at32 angular points from a64-point probe at N=65. Check analytic fields and complex modes, conservation, realizability, iteration residuals, negative controls and a separate N=9 constant-source row.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en)

### Numerical methods

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

- [Variable Eddington factor (1D VEF)](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en)

Supplementary execution example

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)
