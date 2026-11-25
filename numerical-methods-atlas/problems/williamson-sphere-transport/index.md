# Williamson型の球面固体回転輸送：傾いた軸と極通過 / Williamson-type spherical rotation: tilted axes and pole crossing

https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/

## 日本語

[所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/#williamson-sphere-transport) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#williamson-sphere-transport)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [球面上の所与速度スカラー移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#sphere-scalar-advection-ja)

$$
q_t+\mathbf v\cdot\nabla_{\mathbb S^2}q=0,\quad q(\mathbf r,t)=q_0(R_{\mathbf n}(-2\pi t/T)\mathbf r)
$$

$$
\mathbf n=(-\sin\alpha,0,\cos\alpha),\quad q_0(r)=\tfrac12[1+\cos(\pi r/R)]\ (r<R),\quad q_0=0\ (r\ge R)
$$

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

### 厳密解・参照解

固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

#### [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-measurements)

解析解 · 同じ問題の参照

q_t+\mathbf v\cdot\nabla_{\mathbb S^2}q=0,\quad q(\mathbf r,t)=q_0(R_{\mathbf n}(-2\pi t/T)\mathbf r); \mathbf n=(-\sin\alpha,0,\cos\alpha),\quad q_0(r)=\tfrac12[1+\cos(\pi r/R)]\ (r<R),\quad q_0=0\ (r\ge R)

単位球上の規定スカラー剛体回転に限定します。W92原著の式は未読で、Nair著者資料の選択式から規約を照合。両格子で整合しない位相の11回再配置を用います。双線形補間は非保存なので質量変動を報告し、時間収束や非線形の全球浅水コアは主張しません。

固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

#### Williamson型の球面固体回転輸送：傾いた軸と極通過

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja)

### 計算法

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

- [セミラグランジュ法：所与球面回転の限定例](https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja)

補助実行例

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

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

[Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/#williamson-sphere-transport) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#williamson-sphere-transport-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Prescribed scalar advection on a sphere](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#sphere-scalar-advection-en)

$$
q_t+\mathbf v\cdot\nabla_{\mathbb S^2}q=0,\quad q(\mathbf r,t)=q_0(R_{\mathbf n}(-2\pi t/T)\mathbf r)
$$

$$
\mathbf n=(-\sin\alpha,0,\cos\alpha),\quad q_0(r)=\tfrac12[1+\cos(\pi r/R)]\ (r<R),\quad q_0=0\ (r\ge R)
$$

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

### Exact and reference solutions

Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

#### [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-measurements)

Analytic reference · Reference for the same problem

q_t+\mathbf v\cdot\nabla_{\mathbb S^2}q=0,\quad q(\mathbf r,t)=q_0(R_{\mathbf n}(-2\pi t/T)\mathbf r); \mathbf n=(-\sin\alpha,0,\cos\alpha),\quad q_0(r)=\tfrac12[1+\cos(\pi r/R)]\ (r<R),\quad q_0=0\ (r\ge R)

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

#### Williamson-type spherical rotation: tilted axes and pole crossing

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en)

### Numerical methods

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

- [Semi-Lagrangian transport: a limited prescribed sphere rotation](https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en)

Supplementary execution example

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)
