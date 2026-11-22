# FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照 / FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference

https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/

## 日本語

[無次元の2変数FHN型ODEにt=10〜20の電流パルス。DOP853参照とRK4の興奮・回復、刻み0.1/0.05/0.025の収束と全出力点の差を保存結果から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#fitzhugh-nagumo) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#fitzhugh-nagumo)

### 方程式・問題の定義

公開固定入力は空間拡散を含まない2変数ODEの極限です。一般の伝播PDEを検証したという意味ではありません。

#### [FitzHugh–Nagumoの興奮と回復](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fitzhugh-nagumo-ja)

$$
v_t=D\Delta v+v-v^3/3-w+I
$$

$$
w_t=\epsilon(v+a-bw)
$$

高速の興奮と低速の回復を結ぶ規格化した代表形。係数・符号・空間拡張には複数の規約があります。 限定した実行例：公開実行例はD=0の空間なしの縮約ODEです。FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。

#### FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照

補助実行例 · 実行例の定義・検証式

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。

### 厳密解・参照解

電流パルスを与えた2変数縮約ODEを独立DOP853参照と比較し、全出力時刻の誤差・時間収束・回復を確認します。

#### FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照

別実装SciPy DOP853のrtol1e-11と1e-13を比較して参照の感度を確認し、厳しい参照への最大解誤差と時間次数を評価します。ピーク時刻は出力格子上の精度です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja)

補助実行例

2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。

無次元a=0.7,b=0.8,tau=12.5。I=0の休止平衡からt=10〜20だけI=0.8を与え、t=80まで進めます。生理学的な物理単位への較正はしません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)

## English

[A dimensionless two-variable FHN-type ODE with a t=10..20 current pulse: stored RK4/DOP853 excitation and recovery, steps 0.1/0.05/0.025 and all-output-time differences.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#fitzhugh-nagumo) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#fitzhugh-nagumo-en)

### Equations and problem definitions

The published fixed input is the two-variable ODE limit without spatial diffusion; it does not validate the general propagation PDE.

#### [FitzHugh–Nagumo excitation and recovery](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fitzhugh-nagumo-en)

$$
v_t=D\Delta v+v-v^3/3-w+I
$$

$$
w_t=\epsilon(v+a-bw)
$$

A normalized fast excitation/slow recovery model for pulses, refractoriness and spiral waves when extended in space. This is a common normalized variant; cubic coefficients, recovery signs and nondimensionalization differ between formulations. Scoped executed example: The executed case has D=0 and no spatial coordinate. Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.

#### FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference

Supplementary execution example · Example definition or validation formula

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.

### Exact and reference solutions

Compare the two-variable reduced ODE under a current pulse with an independent DOP853 reference, checking all-output-time errors, temporal refinement and recovery.

#### FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference

Compare separate SciPy DOP853 at rtol=1e-11 and 1e-13 to check reference sensitivity; measure maximum solution error and time order against the tighter reference. Peak time is resolved only on the output grid.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en)

Supplementary execution example

Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.

Dimensionless a=0.7,b=0.8,tau=12.5. Start at resting equilibrium for I=0, apply I=0.8 only during t=10..20 and integrate to t=80. No calibration to physiological physical units.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
