# Flux reconstruction (FR) / Flux Reconstruction法（FR法）

Status: educational-example

A high-order framework correcting element-local fluxes at interfaces. A small1D periodic-advection example checks Radau/DG agreement, conservation and convergence; PyFR is a related implementation.

要素内の流束に界面補正を加える高次離散化の枠組み。1D周期移流のRadau補正と既存DGの一致・保存・収束を軽量例で確かめ、PyFRを関連実装として紹介。

DG correspondence is for these Radau/Gauss choices, a constant linear flux and affine elements. No all-FR/all-DG equivalence, nonlinear flux, shock, limiter or multidimensional FR claim. Distinguish coupled h/dt refinement from the exponential spatial result; the exponential is not an independent spatial PDE solver. PyFR itself is not run.

Other names: FR, FR法, Flux Reconstruction, flux reconstruction method, 流束再構成法, CPR, correction procedure via reconstruction

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/flux-reconstruction/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/flux-reconstruction/



- Reference: https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf — Original 2007 title/author/AIAA number checked in the author's 2014 NASA report, printed p.27. The original AIAA text was not retrieved; correction formulas use the separately cited 2014 report.
- Reference: https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf — Selected original NASA passages: abstract, differential form/interface correction, printed pp.19–21 equations(6.2)–(6.13) for Radau/DG, and p.27 bibliography. No full-report audit or nonlinear experiment reproduction.
- Reference: https://www.pyfr.org/ — Official overview: FR spatial discretization, unstructured meshes and CPU/GPU platforms. PyFR is not installed, invoked or validated by this small Python example.

## Small fixed-input validation supplements

Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.

0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。

- 1D periodic FR advection: Radau correction and published DG comparison: https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json

Common execution records: [{"id": "fr-periodic-advection", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-sine)

#### 問題の図 (`method-problems-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

- [FR法の1D周期移流：Radau補正と既存DGの比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) (`fr-periodic-advection`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) (`advection-sine`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照; 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

[既存の参照図](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-measurements)

- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja) (`fr-periodic-advection`; 同じ問題の参照; 解析参照)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

[既存の参照図](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/flux-reconstruction/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### FR法の1D周期移流：Radau補正と既存DGの比較 (`fr-periodic-advection`)

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-23/sem-fr/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py)
- [/code/validated-examples/2026-11-23/sem-fr/fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py)
- [/code/validated-examples/2026-11-23/sem-fr/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py)
- [/code/validated-examples/2026-11-23/sem-fr/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py)
- [/code/validated-examples/2026-11-23/sem-fr/sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; advection-sine)

#### Problem figures (`method-problems-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

- [1D periodic FR advection: Radau correction and published DG comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) (`fr-periodic-advection`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) (`advection-sine`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference; Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

[Existing reference profile](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-measurements)

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference; Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

[Existing reference profile](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/flux-reconstruction/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### 1D periodic FR advection: Radau correction and published DG comparison (`fr-periodic-advection`)

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

###### Related source

- [/code/validated-examples/2026-11-23/sem-fr/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py)
- [/code/validated-examples/2026-11-23/sem-fr/fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py)
- [/code/validated-examples/2026-11-23/sem-fr/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py)
- [/code/validated-examples/2026-11-23/sem-fr/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py)
- [/code/validated-examples/2026-11-23/sem-fr/sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py)

###### Package tests

- [/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
