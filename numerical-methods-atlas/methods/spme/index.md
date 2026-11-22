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

variant: The executed example adopts Essmann-style SPME with cardinal B-splines. It is a PME-family variant, not an implementation of the original1993 Lagrange-interpolation form.

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

## Small fixed-input validation supplement

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
