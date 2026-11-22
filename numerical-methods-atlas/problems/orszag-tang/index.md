# Orszag–Tang渦（CT・GLM・発散誤差摂動を統合） / Orszag–Tang vortex (CT/GLM/error variants merged)

https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/

## 日本語

[CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#orszag-tang)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。

#### Orszag–Tang：CT・GLMと独立Athena++比較

補助実行例 · 実行例の定義・検証式

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

### 厳密解・参照解

保存則・各離散配置に対応する磁場発散と、別実行のAthena++数値参照を確認します。この非線形MHD問題の厳密解を提供するものではありません。

#### Orszag–Tang：CT・GLMと独立Athena++比較

16²/32²/64²で密度とByのL1誤差、質量・エネルギードリフト、正値性を測定。独立参照は128²/256²でも収束を確認し、細胞平均を保存的に制限します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja)

補助実行例

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

単位正方形、γ=5/3、μ₀=1、vz=Bz=0、t=0.05。rho=25/(36π)、p=5/(12π)、v=(-sin2πy,sin2πx)、B=(-sin2πy,sin4πx)/sqrt(4π)。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

CTの面上divergenceとGLMの中心差分divergenceは異なる演算子です。共通cell演算子の値も別記します。Athenaの初期磁場はベクトルポテンシャルの差分による面平均で、同じ連続場の離散化差を含みます。短時間の平面MHD比較であり、衝撃波・3D・UCTやCTUの検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)

## English

[Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#orszag-tang-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests.

#### Orszag–Tang: CT, GLM and independent Athena++

Supplementary execution example · Example definition or validation formula

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

### Exact and reference solutions

Check conservation, divergence appropriate to each discrete layout, and separately run Athena++ numerical references. These are not exact solutions of the nonlinear MHD problem.

#### Orszag–Tang: CT, GLM and independent Athena++

Measure density/By L1 error, mass/energy drift and positivity on 16²/32²/64². Check the independent 128²/256² reference and conservatively restrict its fine-cell averages.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en)

Supplementary execution example

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

Unit square, gamma=5/3, mu0=1, vz=Bz=0, t=0.05. rho=25/(36pi), p=5/(12pi), v=(-sin2piy,sin2pix), B=(-sin2piy,sin4pix)/sqrt(4pi).

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Face CT divergence and centered GLM divergence use different operators; common cell-centered diagnostics are also reported. Athena initializes face-averaged magnetic fields by differencing a vector potential, so comparison includes discretization differences of identical continuous data. This is a short planar test, not validation of shocks, 3D, UCT or CTU.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)
