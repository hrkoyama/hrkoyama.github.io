# SPH kernel reconstruction / SPHカーネル再構成

Status: educational-example

Read about SPH kernel reconstruction, follow the original references and inspect related educational code and checks.

「SPHカーネル再構成」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: SPH法, smoothed particle hydrodynamics, 平滑化粒子法, SPH kernel interpolation

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particles-sph/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particles-sph/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py

- Reference: https://doi.org/10.1093/mnras/181.3.375 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1086/112164 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Only the named fixed examples in this five-case protocol. Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

固定された5ケース群のうち当該手法に対応する限定例です。 Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

- Sod-type particle shock tube with Gaussian-convolution GSPH: https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/
- Uniform pressure and acoustics: particle-layout effects in SPH/GSPH: https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json

Common execution records: [{"id": "gsph-sod", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "sph-pressure-acoustics", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; sod, sph-pressure-acoustics)

#### 問題の図 (`method-problems-ja`)

##### [Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) (`sod`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#code-ja)

- [Gaussian畳込みGSPHによるSod型粒子衝撃管](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja) (`gsph-sod`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。

##### [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja) (`sph-pressure-acoustics`)

![規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja#code-ja)

- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja) (`sph-pressure-acoustics`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。


#### 厳密解・参照解 (`method-references-ja`)

##### [Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#references-ja) (`sod`)

- [Euler／Sod問題](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja) (`euler-sod`; 関連モデルの参照; 半解析参照)

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-sod)

- [Gaussian畳込みGSPHによるSod型粒子衝撃管](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gsph-sod-ja) (`gsph-sod`; 同じ問題の参照; 半解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。

[既存の参照図](/numerical-methods-atlas/validation/gsph-sod/?lang=ja#gsph-sod-ja-measurements)

##### [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja#references-ja) (`sph-pressure-acoustics`)

- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sph-pressure-acoustics-ja) (`sph-pressure-acoustics`; 同じ問題の参照; 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

[既存の参照図](/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particles-sph/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Gaussian畳込みGSPHによるSod型粒子衝撃管 (`gsph-sod`)

[Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。

##### 一様圧力と線形音波：SPH/GSPHの粒子配置依存 (`sph-pressure-acoustics`)

[一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; sod, sph-pressure-acoustics)

#### Problem figures (`method-problems-en`)

##### [Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) (`sod`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#code-en)

- [Sod-type particle shock tube with Gaussian-convolution GSPH](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en) (`gsph-sod`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

##### [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en) (`sph-pressure-acoustics`)

![Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en#code-en)

- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en) (`sph-pressure-acoustics`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.


#### Exact / reference solutions (`method-references-en`)

##### [Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#references-en) (`sod`)

- [Euler / Sod](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en) (`euler-sod`; Related-model reference; Semi-analytic reference)

γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-sod)

- [Sod-type particle shock tube with Gaussian-convolution GSPH](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gsph-sod-en) (`gsph-sod`; Same-problem reference; Semi-analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.

[Existing reference profile](/numerical-methods-atlas/validation/gsph-sod/?lang=en#gsph-sod-en-measurements)

##### [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en#references-en) (`sph-pressure-acoustics`)

- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sph-pressure-acoustics-en) (`sph-pressure-acoustics`; Same-problem reference; Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

[Existing reference profile](/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particles-sph/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Sod-type particle shock tube with Gaussian-convolution GSPH (`gsph-sod`)

[Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

##### Uniform pressure and acoustics: particle-layout effects in SPH/GSPH (`sph-pressure-acoustics`)

[Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py
```
