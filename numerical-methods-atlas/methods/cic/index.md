# Cloud-in-cell assignment and interpolation / Cloud-in-cellの割当てと補間

Status: educational-example

Existing releases: Read about Cloud-in-cell assignment and interpolation, follow the original references and inspect related educational code and checks. Additional fixed examples: Warm PIC linear Landau damping, Warm PIC two-stream initial growth. See each release for assumptions and checked scope. Additional fixed examples: Independently coded PIC spatial pipeline. See each release for assumptions and checked scope.

既存配布版：「Cloud-in-cellの割当てと補間」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：温かいPICの線形Landau減衰、温かいPICの二流初期成長。条件と検証範囲は各配布版で確認してください。 追加固定例：PIC空間演算の独立実装照合。条件と検証範囲は各配布版で確認してください。

Limits of existing releases: See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established. Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established. Additional fixed examples: Independent coding check of discrete spatial operators. It does not change the time integrator/continuum model, establish continuum convergence, or reproduce the cold-plasma oscillation reference. A related supplement of cold-plasma-pic; the finite warm velocity spread is explicit.

Other names: CIC法, cloud in cell

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py

- Reference: https://doi.org/10.1038/324446a0 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(87)90140-9 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://arxiv.org/abs/astro-ph/0505010 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Additional fixed examples: Warm PIC linear Landau damping, Warm PIC two-stream initial growth. See each release for assumptions and checked scope. Additional fixed examples: Independently coded PIC spatial pipeline. See each release for assumptions and checked scope.

追加固定例：温かいPICの線形Landau減衰、温かいPICの二流初期成長。条件と検証範囲は各配布版で確認してください。 追加固定例：PIC空間演算の独立実装照合。条件と検証範囲は各配布版で確認してください。

- Warm PIC linear Landau damping: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/
- Warm PIC two-stream initial growth: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json

- Independently coded PIC spatial pipeline: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/result.json

Common execution records: [{"id": "periodic-particles", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-particles-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-particles-en"}}, {"id": "thermal-landau-damping", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "thermal-two-stream", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "pic-independent-spatial", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`; periodic-particles)
- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; periodic-particles, cold-plasma-pic)
- [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja) (`vlasov-poisson`; cold-plasma-pic, thermal-landau-damping, thermal-two-stream)

#### 問題の図 (`method-problems-ja`)

##### [周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja) (`periodic-particles`)

![共有図の周期PM部分。孤立ツリーの比較は別問題です。](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#code-ja)

- [周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja) (`periodic-particles`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

![1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja) (`pic-independent-spatial`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。

##### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`)

![実際に動かした粒子の初期(x,v)に対する速度変化δv/α。空間2D流体図ではなく1D1V位相空間の応答です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#code-ja)

- [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。

##### [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) (`thermal-two-stream`)

![実粒子のT40での速度変化δv/αを初期(x,v)に表示。1D1V位相空間の後期診断で、成長率を検証する固定窓\[12,20\]とは分けます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#code-ja)

- [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja) (`thermal-two-stream`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#references-ja) (`periodic-particles`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja) (`cold-plasma-pic`)

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja) (`pic-independent-spatial`; 関連モデルの参照; 有限格子の数値参照)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

[既存の参照図](/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-measurements)

##### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#references-ja) (`thermal-landau-damping`)

- [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-landau-damping-ja) (`thermal-landau-damping`; 同じ問題の参照; 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

[既存の参照図](/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-measurements)

##### [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#references-ja) (`thermal-two-stream`)

- [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-two-stream-ja) (`thermal-two-stream`; 同じ問題の参照; 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

[既存の参照図](/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 周期PM粒子群：質量・内力・格子場 (`periodic-particles`)

[周期PM粒子群の質量・内力](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。

##### PIC空間演算の独立実装照合 (`pic-independent-spatial`)

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json)

ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。

##### 温かいPICの線形Landau減衰 (`thermal-landau-damping`)

[温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。

##### 温かいPICの二流初期成長 (`thermal-two-stream`)

[温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：温かいPICの線形Landau減衰、温かいPICの二流初期成長。条件と検証範囲は各配布版で確認してください。 追加固定例：PIC空間演算の独立実装照合。条件と検証範囲は各配布版で確認してください。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py)
- [/code/validated-examples/2026-11-23/warm-pic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/run.py)
- [/code/validated-examples/2026-11-23/warm-pic/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/primary.py)
- [/code/validated-examples/2026-11-23/warm-pic/loading.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/loading.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/linear.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/estimate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/estimate.py)
- [/code/validated-examples/2026-11-23/warm-pic/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/experiments.py)
- [/code/validated-examples/2026-11-23/pic-spatial/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/run.py)
- [/code/validated-examples/2026-11-23/pic-spatial/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/primary.py)
- [/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)
- [/code/validated-examples/2026-11-23/warm-pic/test_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/test_pic.py)
- [/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_particle_gravity.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`; periodic-particles)
- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; periodic-particles, cold-plasma-pic)
- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`; cold-plasma-pic, thermal-landau-damping, thermal-two-stream)

#### Problem figures (`method-problems-en`)

##### [Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en) (`periodic-particles`)

![Periodic-PM part of a shared figure; isolated-tree comparisons are a separate problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#code-en)

- [Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en) (`periodic-particles`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

![One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en) (`pic-independent-spatial`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.

##### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) (`thermal-landau-damping`)

![Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#code-en)

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en) (`thermal-landau-damping`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

##### [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) (`thermal-two-stream`)

![Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over\[12,20\].](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#code-en)

- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en) (`thermal-two-stream`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#references-en) (`periodic-particles`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en) (`cold-plasma-pic`)

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en) (`pic-independent-spatial`; Related-model reference; Finite-grid numerical reference)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

[Existing reference profile](/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-measurements)

##### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#references-en) (`thermal-landau-damping`)

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en) (`thermal-landau-damping`; Same-problem reference; Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

[Existing reference profile](/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-measurements)

##### [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#references-en) (`thermal-two-stream`)

- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en) (`thermal-two-stream`; Same-problem reference; Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

[Existing reference profile](/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Periodic PM particles: mass, internal force and mesh field (`periodic-particles`)

[Periodic PM particle mass and internal force](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.

##### Independently coded PIC spatial pipeline (`pic-independent-spatial`)

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json)

Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.

##### Warm PIC linear Landau damping (`thermal-landau-damping`)

[Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

##### Warm PIC two-stream initial growth (`thermal-two-stream`)

[Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: Warm PIC linear Landau damping, Warm PIC two-stream initial growth. See each release for assumptions and checked scope. Additional fixed examples: Independently coded PIC spatial pipeline. See each release for assumptions and checked scope.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py)
- [/code/validated-examples/2026-11-23/warm-pic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/run.py)
- [/code/validated-examples/2026-11-23/warm-pic/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/primary.py)
- [/code/validated-examples/2026-11-23/warm-pic/loading.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/loading.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/linear.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/estimate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/estimate.py)
- [/code/validated-examples/2026-11-23/warm-pic/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/experiments.py)
- [/code/validated-examples/2026-11-23/pic-spatial/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/run.py)
- [/code/validated-examples/2026-11-23/pic-spatial/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/primary.py)
- [/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)
- [/code/validated-examples/2026-11-23/warm-pic/test_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/test_pic.py)
- [/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_particle_gravity.py
```
