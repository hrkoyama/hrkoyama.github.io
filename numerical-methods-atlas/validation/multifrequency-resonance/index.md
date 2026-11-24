# 結合した2周波数系と共鳴の有限窓

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-algorithm)

全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

- [二周波数の結合調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja) (`coupled-harmonic-oscillators`)

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。


**問題の図**

![結合した2周波数系と共鳴の有限窓：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-validation)

116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。

- [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-multifrequency-resonance-ja) (`multifrequency-resonance`; 同じ問題の参照 · 半解析参照)

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。
## 前提・単位・境界

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

**編集上の補足**

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

## 比較・検証

116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。

## 確認の限界

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "verlet_observed_orders": [
      2.0006335257949495,
      2.0004237164828513
    ],
    "impulse_observed_orders": [
      2.000688773919643,
      2.0001158542645605
    ],
    "evolution_count": 18,
    "probe_steps": 64,
    "ideal_pi_separate_from_actual_float": true,
    "maximum_frozen_map_relative_error": 2.432468376162801e-15
  },
  "checks": {
    "w10-verlet-1p0-finite-cap": true,
    "w10-verlet-1p0-completed": true,
    "w10-verlet-1p0-discrete-reference": true,
    "w10-verlet-1p0-roundoff": true,
    "w10-verlet-1p0-symplectic": true,
    "w10-verlet-1p0-classification": true,
    "w10-verlet-1p8-finite-cap": true,
    "w10-verlet-1p8-completed": true,
    "w10-verlet-1p8-discrete-reference": true,
    "w10-verlet-1p8-roundoff": true,
    "w10-verlet-1p8-symplectic": true,
    "w10-verlet-1p8-classification": true,
    "w10-verlet-2p2-finite-cap": true,
    "w10-verlet-2p2-completed": true,
    "w10-verlet-2p2-discrete-reference": true,
    "w10-verlet-2p2-roundoff": true,
    "w10-verlet-2p2-symplectic": true,
    "w10-verlet-2p2-classification": true,
    "w10-impulse-0p9-finite-cap": true,
    "w10-impulse-0p9-completed": true,
    "w10-impulse-0p9-discrete-reference": true,
    "w10-impulse-0p9-roundoff": true,
    "w10-impulse-0p9-symplectic": true,
    "w10-impulse-0p9-classification": true,
    "w10-impulse-1p0-finite-cap": true,
    "w10-impulse-1p0-completed": true,
    "w10-impulse-1p0-discrete-reference": true,
    "w10-impulse-1p0-roundoff": true,
    "w10-impulse-1p0-symplectic": true,
    "w10-impulse-1p0-classification": true,
    "w10-impulse-1p1-finite-cap": true,
    "w10-impulse-1p1-completed": true,
    "w10-impulse-1p1-discrete-reference": true,
    "w10-impulse-1p1-roundoff": true,
    "w10-impulse-1p1-symplectic": true,
    "w10-impulse-1p1-classification": true,
    "w20-verlet-1p0-finite-cap": true,
    "w20-verlet-1p0-completed": true,
    "w20-verlet-1p0-discrete-reference": true,
    "w20-verlet-1p0-roundoff": true,
    "w20-verlet-1p0-symplectic": true,
    "w20-verlet-1p0-classification": true,
    "w20-verlet-1p8-finite-cap": true,
    "w20-verlet-1p8-completed": true,
    "w20-verlet-1p8-discrete-reference": true,
    "w20-verlet-1p8-roundoff": true,
    "w20-verlet-1p8-symplectic": true,
    "w20-verlet-1p8-classification": true,
    "w20-verlet-2p2-finite-cap": true,
    "w20-verlet-2p2-completed": true,
    "w20-verlet-2p2-discrete-reference": true,
    "w20-verlet-2p2-roundoff": true,
    "w20-verlet-2p2-symplectic": true,
    "w20-verlet-2p2-classification": true,
    "w20-impulse-0p9-finite-cap": true,
    "w20-impulse-0p9-completed": true,
    "w20-impulse-0p9-discrete-reference": true,
    "w20-impulse-0p9-roundoff": true,
    "w20-impulse-0p9-symplectic": true,
    "w20-impulse-0p9-classification": true,
    "w20-impulse-1p0-finite-cap": true,
    "w20-impulse-1p0-completed": true,
    "w20-impulse-1p0-discrete-reference": true,
    "w20-impulse-1p0-roundoff": true,
    "w20-impulse-1p0-symplectic": true,
    "w20-impulse-1p0-classification": true,
    "w20-impulse-1p1-finite-cap": true,
    "w20-impulse-1p1-completed": true,
    "w20-impulse-1p1-discrete-reference": true,
    "w20-impulse-1p1-roundoff": true,
    "w20-impulse-1p1-symplectic": true,
    "w20-impulse-1p1-classification": true,
    "w10-verlet-accuracy-500-finite": true,
    "w10-verlet-accuracy-500-completed": true,
    "w10-verlet-accuracy-500-state": true,
    "w10-verlet-accuracy-500-energy": true,
    "w10-verlet-accuracy-500-mode": true,
    "w10-verlet-accuracy-500-discrete-reference": true,
    "w10-verlet-accuracy-1000-finite": true,
    "w10-verlet-accuracy-1000-completed": true,
    "w10-verlet-accuracy-1000-state": true,
    "w10-verlet-accuracy-1000-energy": true,
    "w10-verlet-accuracy-1000-mode": true,
    "w10-verlet-accuracy-1000-discrete-reference": true,
    "w10-verlet-accuracy-2000-finite": true,
    "w10-verlet-accuracy-2000-completed": true,
    "w10-verlet-accuracy-2000-state": true,
    "w10-verlet-accuracy-2000-energy": true,
    "w10-verlet-accuracy-2000-mode": true,
    "w10-verlet-accuracy-2000-discrete-reference": true,
    "w10-impulse-accuracy-500-finite": true,
    "w10-impulse-accuracy-500-completed": true,
    "w10-impulse-accuracy-500-state": true,
    "w10-impulse-accuracy-500-energy": true,
    "w10-impulse-accuracy-500-mode": true,
    "w10-impulse-accuracy-500-discrete-reference": true,
    "w10-impulse-accuracy-1000-finite": true,
    "w10-impulse-accuracy-1000-completed": true,
    "w10-impulse-accuracy-1000-state": true,
    "w10-impulse-accuracy-1000-energy": true,
    "w10-impulse-accuracy-1000-mode": true,
    "w10-impulse-accuracy-1000-discrete-reference": true,
    "w10-impulse-accuracy-2000-finite": true,
    "w10-impulse-accuracy-2000-completed": true,
    "w10-impulse-accuracy-2000-state": true,
    "w10-impulse-accuracy-2000-energy": true,
    "w10-impulse-accuracy-2000-mode": true,
    "w10-impulse-accuracy-2000-discrete-reference": true,
    "verlet-state-order": true,
    "verlet-fine-state": true,
    "verlet-fine-relative-H": true,
    "verlet-fine-coordinate-energy": true,
    "impulse-state-order": true,
    "impulse-fine-state": true,
    "impulse-fine-relative-H": true,
    "impulse-fine-coordinate-energy": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/index.json

![保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Coupled frequencies and finite-window resonance

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-algorithm)

Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

- [Coupled two-frequency harmonic oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coupled-harmonic-oscillators-en) (`coupled-harmonic-oscillators`)

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.


**Problem figure**

![Coupled frequencies and finite-window resonance: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) (`multifrequency-resonance`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-validation)

The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.

- [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-multifrequency-resonance-en) (`multifrequency-resonance`; Same-problem reference · Semi-analytic reference)

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.
## Assumptions, units and boundaries

alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.

**Editorial clarification**

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

## References and validation

The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.

## Limits

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

## Stored measurements and decisions

```json
{
  "metrics": {
    "verlet_observed_orders": [
      2.0006335257949495,
      2.0004237164828513
    ],
    "impulse_observed_orders": [
      2.000688773919643,
      2.0001158542645605
    ],
    "evolution_count": 18,
    "probe_steps": 64,
    "ideal_pi_separate_from_actual_float": true,
    "maximum_frozen_map_relative_error": 2.432468376162801e-15
  },
  "checks": {
    "w10-verlet-1p0-finite-cap": true,
    "w10-verlet-1p0-completed": true,
    "w10-verlet-1p0-discrete-reference": true,
    "w10-verlet-1p0-roundoff": true,
    "w10-verlet-1p0-symplectic": true,
    "w10-verlet-1p0-classification": true,
    "w10-verlet-1p8-finite-cap": true,
    "w10-verlet-1p8-completed": true,
    "w10-verlet-1p8-discrete-reference": true,
    "w10-verlet-1p8-roundoff": true,
    "w10-verlet-1p8-symplectic": true,
    "w10-verlet-1p8-classification": true,
    "w10-verlet-2p2-finite-cap": true,
    "w10-verlet-2p2-completed": true,
    "w10-verlet-2p2-discrete-reference": true,
    "w10-verlet-2p2-roundoff": true,
    "w10-verlet-2p2-symplectic": true,
    "w10-verlet-2p2-classification": true,
    "w10-impulse-0p9-finite-cap": true,
    "w10-impulse-0p9-completed": true,
    "w10-impulse-0p9-discrete-reference": true,
    "w10-impulse-0p9-roundoff": true,
    "w10-impulse-0p9-symplectic": true,
    "w10-impulse-0p9-classification": true,
    "w10-impulse-1p0-finite-cap": true,
    "w10-impulse-1p0-completed": true,
    "w10-impulse-1p0-discrete-reference": true,
    "w10-impulse-1p0-roundoff": true,
    "w10-impulse-1p0-symplectic": true,
    "w10-impulse-1p0-classification": true,
    "w10-impulse-1p1-finite-cap": true,
    "w10-impulse-1p1-completed": true,
    "w10-impulse-1p1-discrete-reference": true,
    "w10-impulse-1p1-roundoff": true,
    "w10-impulse-1p1-symplectic": true,
    "w10-impulse-1p1-classification": true,
    "w20-verlet-1p0-finite-cap": true,
    "w20-verlet-1p0-completed": true,
    "w20-verlet-1p0-discrete-reference": true,
    "w20-verlet-1p0-roundoff": true,
    "w20-verlet-1p0-symplectic": true,
    "w20-verlet-1p0-classification": true,
    "w20-verlet-1p8-finite-cap": true,
    "w20-verlet-1p8-completed": true,
    "w20-verlet-1p8-discrete-reference": true,
    "w20-verlet-1p8-roundoff": true,
    "w20-verlet-1p8-symplectic": true,
    "w20-verlet-1p8-classification": true,
    "w20-verlet-2p2-finite-cap": true,
    "w20-verlet-2p2-completed": true,
    "w20-verlet-2p2-discrete-reference": true,
    "w20-verlet-2p2-roundoff": true,
    "w20-verlet-2p2-symplectic": true,
    "w20-verlet-2p2-classification": true,
    "w20-impulse-0p9-finite-cap": true,
    "w20-impulse-0p9-completed": true,
    "w20-impulse-0p9-discrete-reference": true,
    "w20-impulse-0p9-roundoff": true,
    "w20-impulse-0p9-symplectic": true,
    "w20-impulse-0p9-classification": true,
    "w20-impulse-1p0-finite-cap": true,
    "w20-impulse-1p0-completed": true,
    "w20-impulse-1p0-discrete-reference": true,
    "w20-impulse-1p0-roundoff": true,
    "w20-impulse-1p0-symplectic": true,
    "w20-impulse-1p0-classification": true,
    "w20-impulse-1p1-finite-cap": true,
    "w20-impulse-1p1-completed": true,
    "w20-impulse-1p1-discrete-reference": true,
    "w20-impulse-1p1-roundoff": true,
    "w20-impulse-1p1-symplectic": true,
    "w20-impulse-1p1-classification": true,
    "w10-verlet-accuracy-500-finite": true,
    "w10-verlet-accuracy-500-completed": true,
    "w10-verlet-accuracy-500-state": true,
    "w10-verlet-accuracy-500-energy": true,
    "w10-verlet-accuracy-500-mode": true,
    "w10-verlet-accuracy-500-discrete-reference": true,
    "w10-verlet-accuracy-1000-finite": true,
    "w10-verlet-accuracy-1000-completed": true,
    "w10-verlet-accuracy-1000-state": true,
    "w10-verlet-accuracy-1000-energy": true,
    "w10-verlet-accuracy-1000-mode": true,
    "w10-verlet-accuracy-1000-discrete-reference": true,
    "w10-verlet-accuracy-2000-finite": true,
    "w10-verlet-accuracy-2000-completed": true,
    "w10-verlet-accuracy-2000-state": true,
    "w10-verlet-accuracy-2000-energy": true,
    "w10-verlet-accuracy-2000-mode": true,
    "w10-verlet-accuracy-2000-discrete-reference": true,
    "w10-impulse-accuracy-500-finite": true,
    "w10-impulse-accuracy-500-completed": true,
    "w10-impulse-accuracy-500-state": true,
    "w10-impulse-accuracy-500-energy": true,
    "w10-impulse-accuracy-500-mode": true,
    "w10-impulse-accuracy-500-discrete-reference": true,
    "w10-impulse-accuracy-1000-finite": true,
    "w10-impulse-accuracy-1000-completed": true,
    "w10-impulse-accuracy-1000-state": true,
    "w10-impulse-accuracy-1000-energy": true,
    "w10-impulse-accuracy-1000-mode": true,
    "w10-impulse-accuracy-1000-discrete-reference": true,
    "w10-impulse-accuracy-2000-finite": true,
    "w10-impulse-accuracy-2000-completed": true,
    "w10-impulse-accuracy-2000-state": true,
    "w10-impulse-accuracy-2000-energy": true,
    "w10-impulse-accuracy-2000-mode": true,
    "w10-impulse-accuracy-2000-discrete-reference": true,
    "verlet-state-order": true,
    "verlet-fine-state": true,
    "verlet-fine-relative-H": true,
    "verlet-fine-coordinate-energy": true,
    "impulse-state-order": true,
    "impulse-fine-state": true,
    "impulse-fine-relative-H": true,
    "impulse-fine-coordinate-energy": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/index.json

![Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
