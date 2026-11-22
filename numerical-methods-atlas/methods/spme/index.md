# Smooth particle mesh Ewald / SPME / Smooth PME（SPME）

Status: educational-example

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

Finite-mesh aliasing permits nonzero net force for this energy-gradient variant; that diagnostic is reported. No exact momentum conservation, long MD, original PME, optimized P³M or slab validation is claimed.

Other names: SPME法, smooth PME, smooth particle mesh Ewald


## 条件と確認範囲 (ja)

problem: 周期像を含む中性点電荷のCoulombエネルギーと力。孤立重力や電子密度のHartree場とは区別します。

variant: 今回の実行例はcardinal B-splineによるEssmann型SPMEです。PME族の採用変種として示し、1993年のLagrange補間による原法を実装したとは呼びません。

use_when:
- 原PMEとの補間差を明らかにし、滑らかなエネルギー・力を同条件で比較したい場合。
- 補間次数・格子密度・力の評価法を固定し、直接Ewaldの収束値と比較できる場合。

avoid_when:
- 「PME」と呼ぶだけで、B-spline次数・窓の補正・FFT規格化・微分法を省略する場合。
- 解析的な力を用いれば、有限格子で運動量とエネルギーの双方が厳密保存すると仮定する場合。
- 孤立・slab・非中性系を、同じ3D中性仕様のまま扱う場合。

assumptions [specified]:
- 最初の検証仕様は、立方体セル内の重なりのない点電荷と3次元周期Coulomb相互作用です。総電荷はゼロとし、一様中和背景は含めません。
- 同一粒子の同一セル項（i=j, n=0）のみを除外し、自己の周期像との相互作用は残します。自己エネルギー補正を別に扱います。
- 分割係数・実空間打切り・逆空間または格子条件を明示します。静電ポテンシャルの平均をゼロにする選択と、巨視的な表面項の境界規約は別です。
- 構造因子をcardinal B-splineで近似し、補間のFourier補正とFFT規格化を揃えます。最初の比較候補は4次（3次多項式）補間ですが、未実装です。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

units [specified]:
比較仕様：長さℓ₀、電荷q₀、Coulomb係数kₑを固定。エネルギー単位はkₑq₀²/ℓ₀、力はkₑq₀²/ℓ₀²、分割係数は長さの逆数です。kₑ=1の無次元化とSIを混ぜず、周期重力PMの符号・規約を流用しません。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

boundary_conditions [specified]:
3次元周期・中性セル。最初の比較では外部導体（tin-foil）規約で巨視的表面項をゼロとし、平均ポテンシャルを別途固定します。真空外部・slab・孤立境界の結果とは直接比較しません。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

limitations [specified]:
有限格子のaliasingにより、エネルギー勾配型の合力は厳密にはゼロでなく、その診断量を保存します。運動量保存・長時間MD・原法PME・最適化P³M・スラブ補正の検証ではありません。
文献整理と専用実装・数値検証の完了を区別します。

Review: 原典・採用形の整理に加え、新しい専用補助配布版をZIP独立展開し、固定入力と数値判定を実行しました。採用変種と確認範囲は下の専用例・検証記録で確認できます。

Not checked:
- 有限格子のaliasingにより、エネルギー勾配型の合力は厳密にはゼロでなく、その診断量を保存します。運動量保存・長時間MD・原法PME・最適化P³M・スラブ補正の検証ではありません。

Evidence:
- Fixed-input measured checks / 固定入力の実測判定: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
- Independent ZIP-extraction receipt / ZIP独立展開の記録: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

References:
- [original-method / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  中性点電荷のEwald項と補正、cardinal B-splineによる構造因子、滑らかなエネルギーと力の評価を確認。
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf
- [context / primary-research] Darden, T.; York, D.; Pedersen, L. (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. — https://doi.org/10.1063/1.464397
  置き換えられるLagrange版PMEの原典です。B-splineを用いる本文献の採用形とは区別します。
  full-text (2026-11-22); Introduction and Method, printed pp. 10089–10090, Eqs. (2)–(9); https://theory.rutgers.edu/resources/pdfs/1.464397.pdf

## Conditions and review scope (en)

problem: Coulomb energy and forces for neutral point charges and periodic images, distinct from isolated gravity or an electron-density Hartree field.

variant: The executed example adopts Essmann-style SPME with cardinal B-splines. It is a PME-family variant, not an implementation of the original 1993 Lagrange-interpolation form.

use_when:
- Comparing interpolation choices with original PME while seeking smooth energy and forces.
- Checking specified spline order, mesh density and force differentiation against a converged direct-Ewald reference.

avoid_when:
- Leaving spline order, interpolation-window correction, FFT normalization or differentiation unspecified under a generic PME label.
- Assuming analytic forces alone guarantee both exact momentum and energy conservation on a finite mesh.
- Applying the neutral 3D specification unchanged to isolated, slab or nonneutral systems.

assumptions [specified]:
- The initial validation specification is noncoincident point charges in a cubic, triply periodic Coulomb cell with zero net charge and no uniform neutralizing background.
- Omit only i=j in the same cell (n=0); retain periodic self images and account separately for the self-energy correction.
- Specify splitting, real cutoff and reciprocal/mesh parameters. The mean-potential gauge and the macroscopic surface convention are different choices.
- Approximate structure factors with cardinal B-splines and matching Fourier correction/FFT normalization. Fourth-order (cubic) interpolation is an initial comparison candidate, not implemented code.
Specified here as a pre-implementation comparison convention, not an executed setup.

units [specified]:
Comparison convention: fixed length ℓ₀, charge q₀ and Coulomb prefactor kₑ; energy unit kₑq₀²/ℓ₀ and force unit kₑq₀²/ℓ₀². The splitting coefficient has inverse-length units. Do not mix reduced kₑ=1 and SI conventions or reuse gravitational-PM signs.
Specified here as a pre-implementation comparison convention, not an executed setup.

boundary_conditions [specified]:
Triply periodic neutral cell; the initial comparison specifies a conducting (tin-foil) exterior with zero macroscopic surface term and separately fixes the mean-potential gauge. Vacuum-exterior, slab and isolated-boundary results are different problems.
Specified here as a pre-implementation comparison convention, not an executed setup.

limitations [specified]:
Finite-mesh aliasing permits nonzero net force for this energy-gradient variant; that diagnostic is reported. No exact momentum conservation, long MD, original PME, optimized P³M or slab validation is claimed.
Source curation is separate from completion of implementation and numerical validation.

Review: In addition to original-source and variant curation, independently extracted the new dedicated supplement ZIP and actually ran its fixed inputs and numerical checks. Dedicated examples and receipts state the adopted variant and scope.

Not checked:
- Finite-mesh aliasing permits nonzero net force for this energy-gradient variant; that diagnostic is reported. No exact momentum conservation, long MD, original PME, optimized P³M or slab validation is claimed.

Evidence:
- Fixed-input measured checks / 固定入力の実測判定: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
- Independent ZIP-extraction receipt / ZIP独立展開の記録: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

References:
- [original-method / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  Neutral-charge Ewald terms and corrections, cardinal B-spline structure factors and smooth energy/force evaluation.
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf
- [context / primary-research] Darden, T.; York, D.; Pedersen, L. (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. — https://doi.org/10.1063/1.464397
  Original Lagrange PME being modified; distinct from the B-spline formulation specified here.
  full-text (2026-11-22); Introduction and Method, printed pp. 10089–10090, Eqs. (2)–(9); https://theory.rutgers.edu/resources/pdfs/1.464397.pdf


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spme/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/spme/



- Reference: https://doi.org/10.1063/1.470117 — Neutral-charge Ewald terms and corrections, cardinal B-spline structure factors and smooth energy/force evaluation.
- Reference: https://doi.org/10.1063/1.464397 — Original Lagrange PME being modified; distinct from the B-spline formulation specified here.

## Small fixed-input validation supplements

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

- Mesh/order convergence of B-spline smooth PME: https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

Common execution records: [{"id": "spme", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; neutral-periodic-charges)

#### 問題の図 (`method-problems-ja`)

##### [中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

![中性立方セルの非対称8点電荷。Ewaldの実空間・逆空間打切りに対する力の差を保存値から表示。smooth PMEの格子・Bスプライン次数比較は同じ問題の補助例へ接続。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

- [Bスプラインsmooth PMEの格子・次数収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja) (`spme`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。


#### 厳密解・参照解 (`method-references-ja`)

##### [中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#references-ja) (`neutral-periodic-charges`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spme/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Bスプラインsmooth PMEの格子・次数収束 (`spme`)

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; neutral-periodic-charges)

#### Problem figures (`method-problems-en`)

##### [Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

![Asymmetric eight-charge neutral cubic cell: saved force differences over Ewald real/reciprocal cutoffs. The same problem links to a smooth-PME mesh/B-spline-order supplement.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

- [Mesh/order convergence of B-spline smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en) (`spme`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.


#### Exact / reference solutions (`method-references-en`)

##### [Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#references-en) (`neutral-periodic-charges`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/spme/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Mesh/order convergence of B-spline smooth PME (`spme`)

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)

###### Package tests

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
