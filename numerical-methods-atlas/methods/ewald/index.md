# Ewald summation / Ewald法

Status: planned

Split a periodic Coulomb sum into real, reciprocal and self-correction terms. This record defines neutral-cell, unit, zero-mode and surface conventions for a future reference calculation.

周期Coulomb和を実空間・逆空間・自己補正に分けます。中性セル、単位、ゼロモードと表面規約を揃えるための基準を整理した段階です。

Under construction. No dedicated implementation or verification result is provided yet. Cutoff convergence and numerical energy/force/self-term comparisons remain future work.

Other names: Ewald summation, エワルド法, エバルト法, エワルド和


## 条件と確認範囲 (ja)

problem: 周期像を含む中性点電荷のCoulombエネルギーと力。孤立重力や電子密度のHartree場とは区別します。

variant: 実装前の検証仕様：中性3D点電荷、まず立方体・tin-foil境界、直接Ewald和。メッシュ近似を導入する前に打切り収束を確認します。

use_when:
- 周期像を含むCoulombエネルギーと力を、明示した境界規約で評価したい場合。
- 小さな中性系で、PME/SPMEと比較する打切り収束済みの基準を用意する場合。

avoid_when:
- 孤立・2次元周期・slab、または中和背景を指定していない非中性系。
- 有限打切りの値を収束済みの厳密値と扱う場合。実空間と逆空間の誤差を別々に調べる必要があります。

assumptions [specified]:
- 最初の検証仕様は、立方体セル内の重なりのない点電荷と3次元周期Coulomb相互作用です。総電荷はゼロとし、一様中和背景は含めません。
- 同一粒子の同一セル項（i=j, n=0）のみを除外し、自己の周期像との相互作用は残します。自己エネルギー補正を別に扱います。
- 分割係数・実空間打切り・逆空間または格子条件を明示します。静電ポテンシャルの平均をゼロにする選択と、巨視的な表面項の境界規約は別です。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

units [specified]:
比較仕様：長さℓ₀、電荷q₀、Coulomb係数kₑを固定。エネルギー単位はkₑq₀²/ℓ₀、力はkₑq₀²/ℓ₀²、分割係数は長さの逆数です。kₑ=1の無次元化とSIを混ぜず、周期重力PMの符号・規約を流用しません。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

boundary_conditions [specified]:
3次元周期・中性セル。最初の比較では外部導体（tin-foil）規約で巨視的表面項をゼロとし、平均ポテンシャルを別途固定します。真空外部・slab・孤立境界の結果とは直接比較しません。
ここでは実装前の比較仕様として記載し、計算済みの条件とは区別します。

limitations [specified]:
Under construction。専用の実装・検証結果はまだありません。条件と原典を整理した段階で、打切り収束・エネルギーと力・自己項を含む数値比較は今後の作業です。
文献整理と専用実装・数値検証の完了を区別します。

Review: 原典の該当箇所と既存台帳の実装予定状態を照合しました。アトラスに専用の実装・実行入力・数値検証結果はなく、今回も計算は実行していません。

Not checked:
- 実装コード・固定入力・数値残差・収束率・性能は未検証。
- 原論文の全導出と全数値例の再現は行っていません。

Evidence:


References:
- [original-method / primary-research] Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. — https://doi.org/10.1002/andp.19213690304
  実空間・逆空間へ分解する原法の書誌。1921年原文の全導出は今回監査していません。
  metadata (2026-11-22); Publisher record: author, title, year, volume 369, pp. 253–287; https://onlinelibrary.wiley.com/doi/10.1002/andp.19213690304
- [formulation / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  今回の比較仕様に必要な中性条件、自己補正と表面項を本文で確認した定式化です。
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf

## Conditions and review scope (en)

problem: Coulomb energy and forces for neutral point charges and periodic images, distinct from isolated gravity or an electron-density Hartree field.

variant: Pre-implementation specification: neutral 3D point charges, initially cubic/tin-foil boundaries and direct Ewald summation, with cutoff convergence before introducing a mesh approximation.

use_when:
- A periodically replicated Coulomb problem with explicitly stated boundary conventions.
- A small neutral reference for same-convention PME/SPME energy and force comparisons.

avoid_when:
- Isolated, two-dimensionally periodic or slab systems, or nonneutral cells without an explicit background model.
- Treating finite cutoffs as an exact reference without separate real- and reciprocal-space convergence checks.

assumptions [specified]:
- The initial validation specification is noncoincident point charges in a cubic, triply periodic Coulomb cell with zero net charge and no uniform neutralizing background.
- Omit only i=j in the same cell (n=0); retain periodic self images and account separately for the self-energy correction.
- Specify splitting, real cutoff and reciprocal/mesh parameters. The mean-potential gauge and the macroscopic surface convention are different choices.
Specified here as a pre-implementation comparison convention, not an executed setup.

units [specified]:
Comparison convention: fixed length ℓ₀, charge q₀ and Coulomb prefactor kₑ; energy unit kₑq₀²/ℓ₀ and force unit kₑq₀²/ℓ₀². The splitting coefficient has inverse-length units. Do not mix reduced kₑ=1 and SI conventions or reuse gravitational-PM signs.
Specified here as a pre-implementation comparison convention, not an executed setup.

boundary_conditions [specified]:
Triply periodic neutral cell; the initial comparison specifies a conducting (tin-foil) exterior with zero macroscopic surface term and separately fixes the mean-potential gauge. Vacuum-exterior, slab and isolated-boundary results are different problems.
Specified here as a pre-implementation comparison convention, not an executed setup.

limitations [specified]:
Under construction. No dedicated implementation or verification result is provided yet. Cutoff convergence and numerical energy/force/self-term comparisons remain future work.
Source curation is separate from completion of implementation and numerical validation.

Review: Checked relevant source passages and the catalog’s planned status. The atlas has no dedicated implementation, runnable input or numerical validation result for this entry; no calculation was run in this review.

Not checked:
- No implementation, fixed inputs, numerical residuals, convergence rates or performance have been verified.
- Not a reproduction of every derivation or numerical example in the original papers.

Evidence:


References:
- [original-method / primary-research] Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. — https://doi.org/10.1002/andp.19213690304
  Bibliographic origin of the real/reciprocal decomposition; the complete 1921 derivation was not audited.
  metadata (2026-11-22); Publisher record: author, title, year, volume 369, pp. 253–287; https://onlinelibrary.wiley.com/doi/10.1002/andp.19213690304
- [formulation / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  Full-text formulation used here to check neutrality, self corrections and surface conventions.
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf






- Reference: https://doi.org/10.1002/andp.19213690304 — Bibliographic origin of the real/reciprocal decomposition; the complete 1921 derivation was not audited.
- Reference: https://doi.org/10.1063/1.470117 — Full-text formulation used here to check neutrality, self corrections and surface conventions.

Next: A neutral small-system reference with explicit self, zero-mode and boundary conventions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
