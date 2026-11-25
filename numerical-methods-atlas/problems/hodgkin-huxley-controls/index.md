# Hodgkin–Huxley：電位固定・静止平衡・発火 / Hodgkin–Huxley: clamps, rest and firing

https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/

## 日本語

[固定電位の解析ゲート解と、区分電流下の4状態系を照合します。 1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-ode-controls/#hodgkin-huxley-controls) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#hodgkin-huxley-controls)

### 方程式・問題の定義

6.3°C、ms/mV/µA cm⁻²。NEURON8.2.6の解析的な絶対電位規約を固定し、4電位×3刻み、静止20 ms、10–11 msの電流パルスを扱います。

#### [Hodgkin–Huxley膜動態](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-hodgkin-huxley-ja)

$$
C_m\dot V=I_{app}-\bar g_{Na}m^3h(V-E_{Na})-\bar g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

電位とゲート変数z=m,h,nの膜モデル。元のイカ軸索モデルと、人心筋や空間ケーブルへの拡張を区別します。 全モデル族の実装ではありません。今回の固定例：Hodgkin–Huxley：電位固定・静止平衡・発火

#### Hodgkin–Huxley：電位固定・静止平衡・発火

補助実行例 · 実行例の定義・検証式

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

固定電位の解析ゲート解と、区分電流下の4状態系を照合します。

### 厳密解・参照解

全採用時刻のゲート誤差、電位・ゲート範囲、採用端点の新しい微分を使うHermite発火時刻を保存。元の1e-8ゲート目標も未達を含めて表示します。

#### [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja#hodgkin-huxley-controls-ja-measurements)

半解析解 · 同じ問題の参照

C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L);\quad \dot z=\alpha_z(V)(1-z)-\beta_z(V)z

6.3°C、NEURON8.2.6の解析的な絶対電位規約を固定し、時間ms・電位mV・電流密度μA/cm²を用います。4固定電位、3刻み、20msの静止と10–11msの電流パルスを比較。ゲートは無次元で、空間一様な1細胞膜の電位固定または区分電流の初期値問題です。

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。

#### Hodgkin–Huxley：電位固定・静止平衡・発火

全採用時刻のゲート誤差、電位・ゲート範囲、採用端点の新しい微分を使うHermite発火時刻を保存。元の1e-8ゲート目標も未達を含めて表示します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja)

### 計算法

古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja)

補助実行例

固定電位の解析ゲート解と、区分電流下の4状態系を照合します。

6.3°C、ms/mV/µA cm⁻²。NEURON8.2.6の解析的な絶対電位規約を固定し、4電位×3刻み、静止20 ms、10–11 msの電流パルスを扱います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/hh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/hh.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)

## English

[Compare analytic clamp gates and a four-state system with segment-owned current. This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-ode-controls/#hodgkin-huxley-controls) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#hodgkin-huxley-controls-en)

### Equations and problem definitions

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.

#### [Hodgkin–Huxley membrane dynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-hodgkin-huxley-en)

$$
C_m\dot V=I_{app}-\bar g_{Na}m^3h(V-E_{Na})-\bar g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

Voltage and gating variables z=m,h,n describe an ionic excitable membrane. A cable extension adds spatial axial current. The original squid-axon model is not a calibrated human cardiac model. No single rate parameter set is selected by this survey. Not implementation of the entire model family. Fixed cases: Hodgkin–Huxley: clamps, rest and firing

#### Hodgkin–Huxley: clamps, rest and firing

Supplementary execution example · Example definition or validation formula

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

Compare analytic clamp gates and a four-state system with segment-owned current.

### Exact and reference solutions

Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.

#### [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-measurements)

Semi-analytic reference · Reference for the same problem

C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L);\quad \dot z=\alpha_z(V)(1-z)-\beta_z(V)z

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse. ms, mV, microampere/cm², 6.3°C; dimensionless gates. Spatially uniform single membrane; voltage clamp or segment-current initial-value problem.

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.

#### Hodgkin–Huxley: clamps, rest and firing

Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en)

### Numerical methods

Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en)

Supplementary execution example

Compare analytic clamp gates and a four-state system with segment-owned current.

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/hh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/hh.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)
