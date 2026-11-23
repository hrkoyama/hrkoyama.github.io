# FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照

2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-algorithm)

独自RK4を刻み0.1/0.05/0.025で使用し、パルスの不連続点で時間区間を厳密に分割します。出力刻み0.1でピークと休止状態からの距離も測定します。

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja) (`fitzhugh-nagumo`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-validation)

別実装SciPy DOP853のrtol1e-11と1e-13を比較して参照の感度を確認し、厳しい参照への最大解誤差と時間次数を評価します。ピーク時刻は出力格子上の精度です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

無次元a=0.7,b=0.8,tau=12.5。I=0の休止平衡からt=10〜20だけI=0.8を与え、t=80まで進めます。生理学的な物理単位への較正はしません。

## 採用した計算法

独自RK4を刻み0.1/0.05/0.025で使用し、パルスの不連続点で時間区間を厳密に分割します。出力刻み0.1でピークと休止状態からの距離も測定します。

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

## 比較・検証

別実装SciPy DOP853のrtol1e-11と1e-13を比較して参照の感度を確認し、厳しい参照への最大解誤差と時間次数を評価します。ピーク時刻は出力格子上の精度です。

## 確認の限界

FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。

## 保存実測値と判定

```json
{
  "metrics": {
    "reference_tolerance_difference": 1.673639005161931e-10,
    "finest_max_error": 6.469538016418142e-08,
    "minimum_temporal_order": 4.06818366368244,
    "peak_v": 2.099845449002621,
    "peak_v_error": 2.613303262677391e-08,
    "peak_time_error": 0.0,
    "recovery_distance": 2.3590633279280127e-05
  },
  "checks": {
    "reference_tolerance": true,
    "solution_error": true,
    "time_order": true,
    "excitation": true,
    "peak_voltage": true,
    "peak_time": true,
    "recovery": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- R. FitzHugh (1961). Impulses and Physiological States in Theoretical Models of Nerve Membrane. https://pubmed.ncbi.nlm.nih.gov/19431309/; review_level=official-abstract-and-metadata
PubMedの原著抄録・書誌を確認。2変数の興奮・不応期の縮約という役割を参照し、HH全系や実測膜電位の再現とは区別します。

- J. Nagumo, S. Arimoto and S. Yoshizawa (1962). An Active Pulse Transmission Line Simulating Nerve Axon. https://ieeexplore.ieee.org/abstract/document/4066548; review_level=publisher-abstract-and-metadata
IEEE出版社の抄録・巻号・頁・DOIを確認。縮約した膜興奮と回路の歴史的な原著として参照し、空間的な伝送線路や回路実験を今回再現したとは扱いません。

- The SciPy community (2024). SciPy1.14.1 solve_ivp reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-api-documentation
公式のDOP853、dense_output、許容誤差、successの仕様を確認。独立数値参照の実装資料です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference

Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en#fitzhugh-nagumo-en-algorithm)

Use original RK4 with steps 0.1/0.05/0.025, splitting time intervals exactly at pulse discontinuities. At output spacing 0.1, measure the peak and distance from rest.

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en) (`fitzhugh-nagumo`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en#fitzhugh-nagumo-en-validation)

Compare separate SciPy DOP853 at rtol=1e-11 and 1e-13 to check reference sensitivity; measure maximum solution error and time order against the tighter reference. Peak time is resolved only on the output grid.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Dimensionless a=0.7,b=0.8,tau=12.5. Start at resting equilibrium for I=0, apply I=0.8 only during t=10..20 and integrate to t=80. No calibration to physiological physical units.

## Adopted numerical method

Use original RK4 with steps 0.1/0.05/0.025, splitting time intervals exactly at pulse discontinuities. At output spacing 0.1, measure the peak and distance from rest.

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

## References and validation

Compare separate SciPy DOP853 at rtol=1e-11 and 1e-13 to check reference sensitivity; measure maximum solution error and time order against the tighter reference. Peak time is resolved only on the output grid.

## Limits

Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.

## Stored measurements and decisions

```json
{
  "metrics": {
    "reference_tolerance_difference": 1.673639005161931e-10,
    "finest_max_error": 6.469538016418142e-08,
    "minimum_temporal_order": 4.06818366368244,
    "peak_v": 2.099845449002621,
    "peak_v_error": 2.613303262677391e-08,
    "peak_time_error": 0.0,
    "recovery_distance": 2.3590633279280127e-05
  },
  "checks": {
    "reference_tolerance": true,
    "solution_error": true,
    "time_order": true,
    "excitation": true,
    "peak_voltage": true,
    "peak_time": true,
    "recovery": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- R. FitzHugh (1961). Impulses and Physiological States in Theoretical Models of Nerve Membrane. https://pubmed.ncbi.nlm.nih.gov/19431309/; review_level=official-abstract-and-metadata
Original-paper abstract and bibliography in PubMed checked. Supports the two-variable excitable/refractory reduction; no full HH or measured membrane-voltage reproduction is claimed.

- J. Nagumo, S. Arimoto and S. Yoshizawa (1962). An Active Pulse Transmission Line Simulating Nerve Axon. https://ieeexplore.ieee.org/abstract/document/4066548; review_level=publisher-abstract-and-metadata
IEEE publisher abstract, volume, pages and DOI checked. Historical source for reduced excitation and its circuit analogue; no spatial transmission-line or hardware-experiment reproduction is claimed.

- The SciPy community (2024). SciPy1.14.1 solve_ivp reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-api-documentation
Official DOP853, dense output, tolerance and success specifications checked. Implementation documentation for the separate numerical reference.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
