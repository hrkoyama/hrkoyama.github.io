# 結合した2周波数系と共鳴の有限窓 / Coupled frequencies and finite-window resonance

https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/

## 日本語

[保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-geometric-controls/#multifrequency-resonance) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#multifrequency-resonance)

### 方程式・問題の定義

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

#### [二周波数の結合調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja)

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+q_1q_2
$$

連続正規モード、理想分割写像、保存した浮動小数点係数の写像、実際の反復丸めを区別します。

#### [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

#### 結合した2周波数系と共鳴の有限窓

補助実行例 · 実行例の定義・検証式

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

### 厳密解・参照解

116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。

#### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-measurements)

半解析解 · 同じ問題の参照

H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2;\quad \Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2};\quad \chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。

#### 結合した2周波数系と共鳴の有限窓

116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja)

### 計算法

全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja)

補助実行例

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)

## English

[Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-geometric-controls/#multifrequency-resonance) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#multifrequency-resonance-en)

### Equations and problem definitions

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

#### [Coupled two-frequency harmonic oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coupled-harmonic-oscillators-en)

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+q_1q_2
$$

Separate continuous normal modes, the ideal split map, a map with stored floating-point coefficients, and repeated rounded updates.

#### [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

#### Coupled frequencies and finite-window resonance

Supplementary execution example · Example definition or validation formula

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

### Exact and reference solutions

The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.

#### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-measurements)

Semi-analytic reference · Reference for the same problem

H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2;\quad \Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2};\quad \chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

#### Coupled frequencies and finite-window resonance

The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en)

### Numerical methods

Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en)

Supplementary execution example

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)
