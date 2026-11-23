# Algebraic multigrid / AMG / 代数的マルチグリッド（AMG）

Status: educational-example

Existing releases: Matrix-based AMG: distinguish residual and solution error: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution. AMG: conditioning, anisotropy, residual and forward error: Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error. Additional fixed examples: Checkerboard diffusion: shared flux, MG and AMG, Rotated diffusion: full-tensor Q1, MG and AMG. See each release for assumptions and checked scope.

既存配布版：行列から粗視化するAMG：残差と解誤差を分ける: 正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。 AMGの条件数・異方性・残差と前進誤差: 49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。 追加固定例：係数ジャンプ拡散：共有流束とMG・AMG、回転異方性拡散：完全テンソルQ1とMG・AMG。条件と検証範囲は各配布版で確認してください。

Limits of existing releases: Matrix-based AMG: distinguish residual and solution error: Only three fixed scalar grids are checked. Large coefficient jumps, strong anisotropy, elasticity, arbitrary unstructured meshes, optimal complexity and mesh-independent convergence are not certified. A small residual alone does not prove a small solution error. AMG: conditioning, anisotropy, residual and forward error: Only a small constant-coefficient family is checked. Arbitrary coefficient jumps, unstructured grids, indefinite systems, optimal complexity and uniform convergence are outside scope. No claim that anisotropy necessarily increases κ₂ or monotonically worsens convergence. Additional fixed examples: Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted. One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

Other names: AMG法, algebraic multigrid, 代数マルチグリッド, 代数的多重格子法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/amg/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/amg/



- Reference: https://doi.org/10.1137/1.9781611971057.ch4 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Matrix-based AMG: distinguish residual and solution error: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution. AMG: conditioning, anisotropy, residual and forward error: Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.

行列から粗視化するAMG：残差と解誤差を分ける: 正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。 AMGの条件数・異方性・残差と前進誤差: 49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。

- Matrix-based AMG: distinguish residual and solution error: https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json

- AMG: conditioning, anisotropy, residual and forward error: https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json

- Checkerboard diffusion: shared flux, MG and AMG: https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/
- Rotated diffusion: full-tensor Q1, MG and AMG: https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json

Common execution records: [{"id": "sa-amg", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "amg-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "checkerboard-diffusion", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "rotated-anisotropic-diffusion", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-sine)
- [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja) (`tensor-diffusion`; checkerboard-diffusion, rotated-anisotropic-diffusion)

#### 問題の図 (`method-problems-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

- [行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja) (`sa-amg`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

##### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#code-ja)

- [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。

##### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#code-ja)

- [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) (`poisson-2d-sine`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照; 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

[既存の参照図](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

##### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#references-ja) (`checkerboard-diffusion`)

- [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-checkerboard-diffusion-ja) (`checkerboard-diffusion`; 同じ問題の参照; 有限格子の数値参照)

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-measurements)

##### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#references-ja) (`rotated-anisotropic-diffusion`)

- [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rotated-anisotropic-diffusion-ja) (`rotated-anisotropic-diffusion`; 同じ問題の参照; 製造解)

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

[既存の参照図](/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/amg/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 行列から粗視化するAMG：残差と解誤差を分ける (`sa-amg`)

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

##### 係数ジャンプ拡散：共有流束とMG・AMG (`checkerboard-diffusion`)

[係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。

##### 回転異方性拡散：完全テンソルQ1とMG・AMG (`rotated-anisotropic-diffusion`)

[回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。

##### 問題図との対応付けとは別の登録実行・検査例

- [amg-conditioning](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja) (`amg-conditioning`)

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

行列から粗視化するAMG：残差と解誤差を分ける: 正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。 AMGの条件数・異方性・残差と前進誤差: 49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-sine)
- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`; checkerboard-diffusion, rotated-anisotropic-diffusion)

#### Problem figures (`method-problems-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

- [Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en) (`sa-amg`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

##### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#code-en)

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

##### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#code-en)

- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.


#### Exact / reference solutions (`method-references-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) (`poisson-2d-sine`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference; Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

[Existing reference profile](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

##### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#references-en) (`checkerboard-diffusion`)

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en) (`checkerboard-diffusion`; Same-problem reference; Finite-grid numerical reference)

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

[Existing reference profile](/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-measurements)

##### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#references-en) (`rotated-anisotropic-diffusion`)

- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en) (`rotated-anisotropic-diffusion`; Same-problem reference; Manufactured solution)

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

[Existing reference profile](/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/amg/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Matrix-based AMG: distinguish residual and solution error (`sa-amg`)

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

##### Checkerboard diffusion: shared flux, MG and AMG (`checkerboard-diffusion`)

[Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

##### Rotated diffusion: full-tensor Q1, MG and AMG (`rotated-anisotropic-diffusion`)

[Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.

##### Registered executions and checks separate from problem-figure links

- [amg-conditioning](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en) (`amg-conditioning`)

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Matrix-based AMG: distinguish residual and solution error: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution. AMG: conditioning, anisotropy, residual and forward error: Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py)

###### Package tests

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
