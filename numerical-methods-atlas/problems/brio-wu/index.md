# Brio–Wu衝撃波管 / Brio–Wu shock tube

https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/

## 日本語

[保存済みBrio–Wu衝撃波管の比較図。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/brio-wu.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#brio-wu)

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

#### Brio–Wu：HLLDと保存的に粗視化した数値参照

共通実行例 · 問題の式

$$
U_t+\partial_xF_{\rm MHD}(U)=0,\qquad\gamma=2,\quad B_x=0.75,\quad\mu_0=1
$$

$$
(\rho,p,B_y)_L=(1,1,1),\qquad(\rho,p,B_y)_R=(0.125,0.1,-1),\qquad\boldsymbol v_{L,R}=\boldsymbol0
$$

[0,1]、初期不連続x=0.5、t=0.1。HLLD・MC再構成・SSPRK2で、512セルの保存量をブロック平均して比較する。同一ソルバーの数値参照であり厳密MHD解ではない。

#### Brio–Wu：別実装HLLDとの照合

補助実行例 · 実行例の定義・検証式

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。

### 厳密解・参照解

同一コードの細格子数値参照と独立Athena++参照を区別します。共平面γ=2のBrio–Wuについて、厳密解や普遍的一意性を主張しません。

#### Brio–Wu：HLLDと保存的に粗視化した数値参照

512セルの保存変数を64/128セルへ整数ブロック平均し、その後にprimitive変数へ変換する。CSVは128セルごとに計算値とそのセル平均に対応する参照値を配置。正値性、縦磁場10^-12、境界流束収支10^-10、経験的な誤差減少を別々に判定し、fallback回数を隠さない。

- [512セルの保存変数を64/128セルへ整数ブロック平均し、その後にprimitive変数へ変換する。CSVは128セルごとに計算値とそのセル平均に対応する参照値を配置。正値性、縦磁場10^-12、境界流束収支10^-10、経験的な誤差減少を別々に判定し、fallback回数を隠さない。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=ja)

#### Brio–Wu：別実装HLLDとの照合

128/256/512セルを、2048/4096セルで再実行した独立参照の保存的細胞平均と比較。rho/ByのL1誤差、格子改善、密度・圧力正値性を判定します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Brio–Wu：HLLDと保存的に粗視化した数値参照](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=ja)

共通実行例

γ=2、Bx=0.75の1次元理想MHD衝撃波管をt=0.1まで計算。HLLD＋MC＋SSPRK2の64/128セルを512セルの数値参照と比較し、密度・圧力・縦磁場・保存収支・切替回数を記録する。

μ0=1、左右(ρ,vx,vy,vz,p,Bx,By,Bz)=(1,0,0,0,1,0.75,1,0)/(0.125,0,0,0,0.1,0.75,−1,0)。初期不連続x=0.5をセル界面へ合わせる。既存solve_1dの固定定義とJSONの一致を検査し、変更した物理定義は拒否。CFL=0.35。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/brio-wu.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/brio-wu.json --output output-brio-wu
python -m pytest -q tests/test_recipes.py
```

512セル参照も同一solverで、厳密解・独立コード・MHD弱解の一意性の証明ではない。密度差0.03は左密度1に対する3%の平均絶対差を許す教材基準。正値性再試行とHLLE切替は数えるが、再構成の正値スケーリングの作動数は既存APIにない。正値出力だけから一般の保証やゼロ修正を主張しない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [Brio–Wu：別実装HLLDとの照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja)

補助実行例

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。

1D、[0,1]、t=0.1、γ=2、Bx=0.75。左右(rho,p,By)=(1,1,1)/(0.125,0.1,-1)、速度ゼロ、流出境界。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Brio–Wuの複合波を含む数値解との照合であり、一般MHD Riemann問題の唯一の厳密解とは呼びません。参照の再生成にはC++コンパイルが必要で、通常Python実行は同梱参照を使います。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/mhd/legacy/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/hlld.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)

## English

[Stored Brio–Wu shock-tube comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/brio-wu.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#brio-wu-en)

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

#### Brio–Wu: HLLD and a conservatively restricted numerical reference

Common execution example · Problem definition

$$
U_t+\partial_xF_{\rm MHD}(U)=0,\qquad\gamma=2,\quad B_x=0.75,\quad\mu_0=1
$$

$$
(\rho,p,B_y)_L=(1,1,1),\qquad(\rho,p,B_y)_R=(0.125,0.1,-1),\qquad\boldsymbol v_{L,R}=\boldsymbol0
$$

[0,1], initial jump x=0.5, t=0.1. HLLD/MC/SSPRK2 is compared after conservative block averaging of the 512-cell result; this same-solver numerical reference is not an exact MHD solution.

#### Brio–Wu against an independent HLLD implementation

Supplementary execution example · Example definition or validation formula

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.

### Exact and reference solutions

Distinguish a finer-grid reference from the same code and an independent Athena++ reference. For coplanar γ=2 Brio–Wu, no exact solution or universal uniqueness is claimed.

#### Brio–Wu: HLLD and a conservatively restricted numerical reference

Restrict the 512-cell conserved variables by integer block averaging to 64/128 cells before converting to primitives. CSV pairs each 128-cell result with its corresponding restricted reference. Positivity, longitudinal-field error 10^-12, boundary-flux balance 10^-10 and empirical error decrease are separate checks; fallback counts remain visible.

- [Restrict the 512-cell conserved variables by integer block averaging to 64/128 cells before converting to primitives. CSV pairs each 128-cell result with its corresponding restricted reference. Positivity, longitudinal-field error 10^-12, boundary-flux balance 10^-10 and empirical error decrease are separate checks; fallback counts remain visible.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/brio-wu/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en)

#### Brio–Wu against an independent HLLD implementation

Compare 128/256/512 cells with conservative averages of independently rerun 2048/4096-cell references. Check density/By L1 errors, refinement and positive density/pressure.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Brio–Wu: HLLD and a conservatively restricted numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en)

Common execution example

Evolve the one-dimensional γ=2 ideal-MHD shock tube with Bx=0.75 to t=0.1. Compare 64/128-cell HLLD/MC/SSPRK2 with a 512-cell numerical reference, recording density, pressure, longitudinal field, balances and fallback counts.

μ0=1, with left/right (ρ,vx,vy,vz,p,Bx,By,Bz)=(1,0,0,0,1,0.75,1,0)/(0.125,0,0,0,0.1,0.75,−1,0). The initial jump x=0.5 is face-aligned. JSON must match the unchanged solve_1d benchmark definition; altered physical definitions are rejected. CFL=0.35.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/brio-wu.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/brio-wu.json --output output-brio-wu
python -m pytest -q tests/test_recipes.py
```

The 512-cell reference uses the same solver and is neither exact nor independent, nor a proof of uniqueness of MHD weak solutions. Density difference 0.03 allows a mean absolute discrepancy of 3% of left density 1 for this educational test. Positivity retries and HLLE fallbacks are counted; reconstruction positivity-scaling activations are not exposed by the existing API. Positive output alone certifies neither general positivity nor absence of reconstruction changes.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [Brio–Wu against an independent HLLD implementation](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en)

Supplementary execution example

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.

1D, [0,1], t=0.1, gamma=2, Bx=0.75; left/right (rho,p,By)=(1,1,1)/(0.125,0.1,-1), zero velocity, outflow boundaries.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This compares numerical solutions including the Brio–Wu compound wave; it is not a claim of a unique exact solution for arbitrary MHD Riemann problems. Reference regeneration requires C++ compilation; routine Python runs use the stored reference.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/mhd/legacy/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/hlld.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)
