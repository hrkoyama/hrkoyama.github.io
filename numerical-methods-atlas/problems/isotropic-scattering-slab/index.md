# 等方散乱平板の反射・透過・吸収 / Isotropic scattering in a finite slab

https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/

## 日本語

[保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-scattering/#isotropic-scattering-slab) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#isotropic-scattering-slab)

### 方程式・問題の定義

光学厚さ.5/3、単一散乱albedo.5/.9の4入力。左の等方入射I1、右入射0。64/128/256セル、32角と独立64角probe。

#### [静止媒質の灰色輻射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja)

$$
\epsilon\partial_t I+\boldsymbol\Omega\cdot\nabla I+(\kappa_a+\kappa_s)I=\kappa_sJ+\kappa_aV+Q
$$

$$
J=\langle I\rangle_\Omega,\quad\partial_t V=\kappa_a(J-V)\quad(\mathrm{linear\ exchange})
$$

正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを輻射・物質の両交換項に掛けます。

#### 等方散乱平板の反射・透過・吸収

補助実行例 · 実行例の定義・検証式

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。

### 厳密解・参照解

独立参照78項目はmain前に合格。主18計算では収支・正値・残差と、別々の空間・角度差、純吸収・保存散乱controlを判定します。

#### [等方散乱平板：連続角Fredholm流束参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-measurements)

半解析解 · 同じ問題の参照

J(x)=.5*E2(x)+omega/2*integral_0^L E1(|x-y|)J(y)dy; R=2omega*integral J E2(x)dx; T=2E3(L)+2omega*integral J E2(L-x)dx; A=4(1-omega)*integral J dx.

平行平板の定常な光学厚さ座標を用い、左の入射輻射輝度は1、右の入射は真空、等方散乱の単一散乱アルベドを固定します。入射半球流束はπ、符号付き角度の平均はJ=(1/2)∫I dμです。

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

#### 等方散乱平板の反射・透過・吸収

独立参照78項目はmain前に合格。主18計算では収支・正値・残差と、別々の空間・角度差、純吸収・保存散乱controlを判定します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja)

### 計算法

保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。

- [輻射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja)

補助実行例

正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。

光学厚さ.5/3、単一散乱albedo.5/.9の4入力。左の等方入射I1、右入射0。64/128/256セル、32角と独立64角probe。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/radiation-scattering/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/run.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/slab.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py)

## English

[Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-scattering/#isotropic-scattering-slab) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#isotropic-scattering-slab-en)

### Equations and problem definitions

Four fixed inputs L=.5/3,albedo=.5/.9;unit left incoming radiance,right vacuum incoming.64/128/256cells at32signed angles and a separate64angle probe.

#### [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en)

$$
\epsilon\partial_t I+\boldsymbol\Omega\cdot\nabla I+(\kappa_a+\kappa_s)I=\kappa_sJ+\kappa_aV+Q
$$

$$
J=\langle I\rangle_\Omega,\quad\partial_t V=\kappa_a(J-V)\quad(\mathrm{linear\ exchange})
$$

Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa.

#### Isotropic scattering in a finite slab

Supplementary execution example · Example definition or validation formula

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.

### Exact and reference solutions

Independent reference78checks passed before main.18primary/control solves test budget,positivity,residuals,separate space/angle changes,pure absorption and conservative scattering.

#### [Isotropically scattering slab: continuous-angle Fredholm flux reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-measurements)

Semi-analytic reference · Reference for the same problem

J(x)=.5*E2(x)+omega/2*integral_0^L E1(|x-y|)J(y)dy; R=2omega*integral J E2(x)dx; T=2E3(L)+2omega*integral J E2(L-x)dx; A=4(1-omega)*integral J dx.

Plane-parallel steady optical-depth slab, unit incoming radiance on the left,vacuum incoming on the right,isotropic single-scattering albedo. Incoming hemispherical flux pi; signed-angle J=.5*integral I.

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

#### Isotropic scattering in a finite slab

Independent reference78checks passed before main.18primary/control solves test budget,positivity,residuals,separate space/angle changes,pure absorption and conservative scattering.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en)

### Numerical methods

Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en)

Supplementary execution example

Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.

Four fixed inputs L=.5/3,albedo=.5/.9;unit left incoming radiance,right vacuum incoming.64/128/256cells at32signed angles and a separate64angle probe.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/radiation-scattering/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/run.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/slab.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py)
