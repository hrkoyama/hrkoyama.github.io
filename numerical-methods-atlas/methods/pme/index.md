# Particle mesh Ewald / PME / Particle Mesh Ewald（PME）

Status: planned

Original PME approximates the reciprocal Ewald contribution using Lagrange interpolation and FFT-based mesh convolutions. Distinguish its kernel, interpolation and force definition from gravitational PM and B-spline SPME.

Ewaldの逆空間項をLagrange補間・格子上の畳み込み・FFTで近似する原PMEです。一般の粒子格子重力法やB-spline版SPMEとは、核と補間・力の定義を区別します。

Under construction. No dedicated implementation or verification result is provided yet. Dispersion terms, intramolecular exclusions, general cells, slab corrections and timing comparisons remain unverified.

Other names: PME法, particle mesh Ewald, 粒子メッシュEwald法


## 条件と確認範囲 (ja)

problem: 周期像を含む中性点電荷のCoulombエネルギーと力。孤立重力や電子密度のHartree場とは区別します。

variant: 実装前の比較仕様：Dardenら（1993）のLagrange版。実空間項・自己補正・表面規約は同条件のEwald基準と一致させます。

use_when:
- 3次元周期Coulomb問題の逆空間評価を格子化し、同条件のEwald和と誤差を比較する場合。
- 格子密度・補間次数・分割係数を明記して力とエネルギーを評価できる場合。

avoid_when:
- 既存のCIC重力PMを、そのまま電荷のPME実装とみなす場合。
- 格子上の勾配を補間した力を、補間エネルギーの厳密な解析微分と同一視する場合。
- 自己項・分子内除外・境界項を揃えない別ソフトとの比較。

assumptions [specified]:
- 最初の検証仕様は、立方体セル内の重なりのない点電荷と3次元周期Coulomb相互作用です。総電荷はゼロとし、一様中和背景は含めません。
- 同一粒子の同一セル項（i=j, n=0）のみを除外し、自己の周期像との相互作用は残します。自己エネルギー補正を別に扱います。
- 分割係数・実空間打切り・逆空間または格子条件を明示します。静電ポテンシャルの平均をゼロにする選択と、巨視的な表面項の境界規約は別です。
- 元のPMEとして、区分Lagrange補間とFFT畳み込みを採ります。補間次数・格子数・格子上の勾配評価を比較条件に含めます。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

units [specified]:
比較仕様：長さℓ₀、電荷q₀、Coulomb係数kₑを固定。エネルギー単位はkₑq₀²/ℓ₀、力はkₑq₀²/ℓ₀²、分割係数は長さの逆数です。kₑ=1の無次元化とSIを混ぜず、周期重力PMの符号・規約を流用しません。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

boundary_conditions [specified]:
3次元周期・中性セル。最初の比較では外部導体（tin-foil）規約で巨視的表面項をゼロとし、平均ポテンシャルを別途固定します。真空外部・slab・孤立境界の結果とは直接比較しません。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

limitations [specified]:
Under construction。専用の実装・検証結果はまだありません。条件と原典を整理した段階で、長距離分散力や分子内除外、一般格子、slab補正、実行速度の比較は未確認です。
文献整理と専用実装・数値検証の完了を区別します。

Review: 原典の該当箇所と既存台帳の実装予定状態を照合しました。アトラスに専用の実装・実行入力・数値検証結果はなく、今回も計算は実行していません。

Not checked:
- 実装コード・固定入力・数値残差・収束率・性能は未検証。
- 原論文の全導出と全数値例の再現は行っていません。

Evidence:


References:
- [original-method / primary-research] Darden, T.; York, D.; Pedersen, L. (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. — https://doi.org/10.1063/1.464397
  Lagrange補間による格子電荷と逆空間エネルギー・力の畳み込みを確認。元のPMEであり、B-spline版とは区別します。
  full-text (2026-11-22); Introduction and Method, printed pp. 10089–10090, Eqs. (2)–(9); https://theory.rutgers.edu/resources/pdfs/1.464397.pdf
- [context / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  原PMEのLagrange補間と、B-spline版・解析的勾配への変更を区別するための比較原典です。
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf

## Conditions and review scope (en)

problem: Coulomb energy and forces for neutral point charges and periodic images, distinct from isolated gravity or an electron-density Hartree field.

variant: Pre-implementation comparison: the Darden et al. (1993) Lagrange variant, matching direct Ewald real terms, self corrections and surface conventions.

use_when:
- Meshing the reciprocal contribution of a 3D periodic Coulomb problem for comparison with the same Ewald formulation.
- Energy and force checks with explicit mesh density, interpolation order and splitting parameter.

avoid_when:
- Equating the existing CIC gravitational PM example with electrostatic PME.
- Equating interpolation of grid gradients with exact analytic differentiation of the interpolated energy.
- Comparing packages without matching self, intramolecular-exclusion and boundary corrections.

assumptions [specified]:
- The initial validation specification is noncoincident point charges in a cubic, triply periodic Coulomb cell with zero net charge and no uniform neutralizing background.
- Omit only i=j in the same cell (n=0); retain periodic self images and account separately for the self-energy correction.
- Specify splitting, real cutoff and reciprocal/mesh parameters. The mean-potential gauge and the macroscopic surface convention are different choices.
- The original PME uses piecewise Lagrange interpolation and FFT convolution; specify interpolation order, mesh sizes and the grid-gradient convention.
Specified here as a pre-implementation comparison convention, not an executed setup.

units [specified]:
Comparison convention: fixed length ℓ₀, charge q₀ and Coulomb prefactor kₑ; energy unit kₑq₀²/ℓ₀ and force unit kₑq₀²/ℓ₀². The splitting coefficient has inverse-length units. Do not mix reduced kₑ=1 and SI conventions or reuse gravitational-PM signs.
Specified here as a pre-implementation comparison convention, not an executed setup.

boundary_conditions [specified]:
Triply periodic neutral cell; the initial comparison specifies a conducting (tin-foil) exterior with zero macroscopic surface term and separately fixes the mean-potential gauge. Vacuum-exterior, slab and isolated-boundary results are different problems.
Specified here as a pre-implementation comparison convention, not an executed setup.

limitations [specified]:
Under construction. No dedicated implementation or verification result is provided yet. Dispersion terms, intramolecular exclusions, general cells, slab corrections and timing comparisons remain unverified.
Source curation is separate from completion of implementation and numerical validation.

Review: Checked relevant source passages and the catalog’s planned status. The atlas has no dedicated implementation, runnable input or numerical validation result for this entry; no calculation was run in this review.

Not checked:
- No implementation, fixed inputs, numerical residuals, convergence rates or performance have been verified.
- Not a reproduction of every derivation or numerical example in the original papers.

Evidence:


References:
- [original-method / primary-research] Darden, T.; York, D.; Pedersen, L. (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. — https://doi.org/10.1063/1.464397
  Original PME: Lagrange weights, gridded charges and convolution-based reciprocal energies and forces, distinct from B-spline SPME.
  full-text (2026-11-22); Introduction and Method, printed pp. 10089–10090, Eqs. (2)–(9); https://theory.rutgers.edu/resources/pdfs/1.464397.pdf
- [context / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  Primary comparison distinguishing original Lagrange PME from B-spline interpolation and analytic gradients.
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf






- Reference: https://doi.org/10.1063/1.464397 — Original PME: Lagrange weights, gridded charges and convolution-based reciprocal energies and forces, distinct from B-spline SPME.
- Reference: https://doi.org/10.1063/1.470117 — Primary comparison distinguishing original Lagrange PME from B-spline interpolation and analytic gradients.

Next: A same-condition Ewald comparison and reproducible reference-code inputs.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
