# 可変エディントンテンソル：周期2D非平行源の固定検証 / Variable Eddington tensor: a periodic 2D nonparallel-source control

https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/

## 日本語

[非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-variable-eddington-controls/#vet-fourier-source2d) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#vet-fourier-source2d)

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

#### 可変エディントンテンソル：周期2D非平行源の固定検証

補助実行例 · 実行例の定義・検証式

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

### 厳密解・参照解

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

#### [本例のために導出した周期2D VETの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-measurements)

解析解 · 同じ問題の参照

For k>0: R=atan(k/st)/k, A=b/(1-ss*R), B=(1-st*R)/k, C=st*(1-st*R)/k^2, T=(R-C)/2. E=E0+Re(sum A*R*exp(i*k.x)); H=Re(sum -i*A*B*khat*exp(i*k.x)); K=E0*I3/3+Re(sum A*(T*I3+(C-T)*khat*khat^T)*exp(i*k.x)); D=K/E; E0=qmean/(st-ss).

静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。 正の指定等方輻射源を使い、角度空間は球面S²を保ちます。

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

#### 可変エディントンテンソル：周期2D非平行源の固定検証

17²/33²と12×48角度則、33²の16×64角度プローブを区別します。解析E/H/K/D、位相を含む複素モード、独立角度積分、テンソル制約、混合項の負制御、N=9²一定源を照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja)

### 計算法

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

- [可変Eddingtonテンソル（VET）](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja)

補助実行例

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)

## English

[Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-variable-eddington-controls/#vet-fourier-source2d) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#vet-fourier-source2d-en)

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

#### Variable Eddington tensor: a periodic 2D nonparallel-source control

Supplementary execution example · Example definition or validation formula

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

### Exact and reference solutions

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

#### [Authored continuum Fourier response for periodic 2D VET](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-measurements)

Analytic reference · Reference for the same problem

For k>0: R=atan(k/st)/k, A=b/(1-ss*R), B=(1-st*R)/k, C=st*(1-st*R)/k^2, T=(R-C)/2. E=E0+Re(sum A*R*exp(i*k.x)); H=Re(sum -i*A*B*khat*exp(i*k.x)); K=E0*I3/3+Re(sum A*(T*I3+(C-T)*khat*khat^T)*exp(i*k.x)); D=K/E; E0=qmean/(st-ss).

Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained. Positive prescribed isotropic source; physical angle space remains S2.

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

#### Variable Eddington tensor: a periodic 2D nonparallel-source control

Separate17x17/33x33 refinement at12x48 angles from the16x64 angular probe on33x33. Check analytic E/H/K/D, complex modes including phase, independent angular integration, tensor constraints, cross-term negative controls and a9x9 constant source.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en)

### Numerical methods

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

- [Variable Eddington tensor (VET)](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en)

Supplementary execution example

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)
