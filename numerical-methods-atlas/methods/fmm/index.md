# Fast multipole translations / 高速多重極法の移動演算

Status: educational-example

Existing releases: 2D logarithmic FMM with M2M, M2L and L2L: Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums. FMM: direct and analytic references, order and tree depth: Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors. Additional fixed examples: Actual3D1/r FMM: multilevel translations, force and ownership. See each release for assumptions and checked scope.

既存配布版：2次元対数核のM2M・M2L・L2Lを持つFMM: 自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。 FMM：直接和・解析配置と展開次数・木の深さ: 96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。 追加固定例：真3D 1/r FMM：多段変換・力・適応所有権。条件と検証範囲は各配布版で確認してください。

Limits of existing releases: 2D logarithmic FMM with M2M, M2L and L2L: No 3D 1/r kernel, adaptive tree, periodic FMM, singular quadrature or empirical complexity/scaling study. Evidence applies to this 2D free-space educational implementation. FMM: direct and analytic references, order and tree depth: Interaction repartition changes with depth, so fixed-order depth refinement is not assumed monotone. Target-wise expansions need not preserve exact action/reaction. No 3D, adaptive/periodic FMM or complexity-scaling claim. Additional fixed examples: Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

Other names: FMM法, fast multipole method, 高速多重極法, 高速多重極展開法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/



- Reference: https://doi.org/10.1016/0021-9991(87)90140-9 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

2D logarithmic FMM with M2M, M2L and L2L: Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums. FMM: direct and analytic references, order and tree depth: Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.

2次元対数核のM2M・M2L・L2Lを持つFMM: 自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。 FMM：直接和・解析配置と展開次数・木の深さ: 96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。

- 2D logarithmic FMM with M2M, M2L and L2L: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

- FMM: direct and analytic references, order and tree depth: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json

- Actual3D1/r FMM: multilevel translations, force and ownership: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/result.json

Common execution records: [{"id": "fmm", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fmm-convergence", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fmm3d-inverse-r", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; logarithmic-particles)
- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`; fmm3d-inverse-r)

#### 問題の図 (`method-problems-ja`)

##### [2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja) (`logarithmic-particles`)

![固定seedの128粒子、2次元自由空間の対数核。FMMの展開次数2/4/8/12を独立した全対直接和と比べたポテンシャル・電場誤差の保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#code-ja)

- [2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja) (`fmm`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

- [FMM：直接和・解析配置と展開次数・木の深さ](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja) (`fmm-convergence`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。

##### [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

P2M/M2M/M2L/L2Lと局所基底の物理勾配、近接P2P。全非自己対を一意に割当て、非零の全変換経路を記録。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#code-ja)

- [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#references-ja) (`logarithmic-particles`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#references-ja) (`fmm3d-inverse-r`)

- [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fmm3d-inverse-r-ja) (`fmm3d-inverse-r`; 同じ問題の参照; 有限格子の数値参照)

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

[既存の参照図](/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 2次元対数核のM2M・M2L・L2Lを持つFMM (`fmm`)

[2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

##### FMM：直接和・解析配置と展開次数・木の深さ (`fmm-convergence`)

[2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。

##### 真3D 1/r FMM：多段変換・力・適応所有権 (`fmm3d-inverse-r`)

[真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/verification.json)

非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

2次元対数核のM2M・M2L・L2Lを持つFMM: 自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。 FMM：直接和・解析配置と展開次数・木の深さ: 96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [/code/validated-examples/2026-11-22/particle-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-23/fmm3d/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/run.py)
- [/code/validated-examples/2026-11-23/fmm3d/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/fmm.py)
- [/code/validated-examples/2026-11-23/fmm3d/references/direct.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/references/direct.py)
- [/code/validated-examples/2026-11-23/fmm3d/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/experiments.py)
- [/code/validated-examples/2026-11-23/fmm3d/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/protocol.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [/code/validated-examples/2026-11-23/fmm3d/test_fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/test_fmm.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; logarithmic-particles)
- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`; fmm3d-inverse-r)

#### Problem figures (`method-problems-en`)

##### [2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) (`logarithmic-particles`)

![Stored potential/field errors for 128 fixed-seed particles with a 2D free-space log kernel: FMM orders 2/4/8/12 versus a separate all-pairs sum.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#code-en)

- [2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en) (`fmm`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

- [FMM: direct and analytic references, order and tree depth](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en) (`fmm-convergence`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.

##### [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

Actual upward/downward translations, physical local-basis gradients and near P2P; audit unique nonself ownership and nonzero complete translation contributions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#code-en)

- [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.


#### Exact / reference solutions (`method-references-en`)

##### [2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en#references-en) (`logarithmic-particles`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#references-en) (`fmm3d-inverse-r`)

- [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fmm3d-inverse-r-en) (`fmm3d-inverse-r`; Same-problem reference; Finite-grid numerical reference)

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

[Existing reference profile](/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### 2D logarithmic FMM with M2M, M2L and L2L (`fmm`)

[2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

##### FMM: direct and analytic references, order and tree depth (`fmm-convergence`)

[2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.

##### Actual3D1/r FMM: multilevel translations, force and ownership (`fmm3d-inverse-r`)

[Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/verification.json)

Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

2D logarithmic FMM with M2M, M2L and L2L: Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums. FMM: direct and analytic references, order and tree depth: Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [/code/validated-examples/2026-11-22/particle-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-23/fmm3d/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/run.py)
- [/code/validated-examples/2026-11-23/fmm3d/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/fmm.py)
- [/code/validated-examples/2026-11-23/fmm3d/references/direct.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/references/direct.py)
- [/code/validated-examples/2026-11-23/fmm3d/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/experiments.py)
- [/code/validated-examples/2026-11-23/fmm3d/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/protocol.py)

###### Package tests

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [/code/validated-examples/2026-11-23/fmm3d/test_fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/test_fmm.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
