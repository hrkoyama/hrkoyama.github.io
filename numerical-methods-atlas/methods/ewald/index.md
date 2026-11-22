# Ewald summation / Ewald法

Status: educational-example

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

No charged-cell/background correction, triclinic cell, finite-dielectric surface term, slab correction, stress or material-specific force field.

Other names: Ewald summation, エワルド法, エバルト法, エワルド和


## 条件と確認範囲 (ja)

problem: 周期像を含む中性点電荷のCoulombエネルギーと力。孤立重力や電子密度のHartree場とは区別します。

variant: 公開例は中性3D点電荷・立方体・tin-foil境界の直接Ewald和です。実空間・逆空間・自己項を含み、打切り・分割パラメータ、エネルギー有限差分の力と独立theta積分を検査しています。

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
非中性セル、背景補正、非直交セル、誘電率が有限の表面項、スラブ補正、応力、物質固有の力場は扱いません。
文献整理と専用実装・数値検証の完了を区別します。

Review: 原典・採用形の整理に加え、新しい専用補助配布版をZIP独立展開し、固定入力と数値判定を実行しました。採用変種と確認範囲は下の専用例・検証記録で確認できます。

Not checked:
- 非中性セル、背景補正、非直交セル、誘電率が有限の表面項、スラブ補正、応力、物質固有の力場は扱いません。

Evidence:
- Fixed-input measured checks / 固定入力の実測判定: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
- Independent ZIP-extraction receipt / ZIP独立展開の記録: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

References:
- [original-method / primary-research] Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. — https://doi.org/10.1002/andp.19213690304
  実空間・逆空間へ分解する原法の書誌。1921年原文の全導出は今回監査していません。
  metadata (2026-11-22); Publisher record: author, title, year, volume 369, pp. 253–287; https://onlinelibrary.wiley.com/doi/10.1002/andp.19213690304
- [formulation / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  今回の比較仕様に必要な中性条件、自己補正と表面項を本文で確認した定式化です。
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf

## Conditions and review scope (en)

problem: Coulomb energy and forces for neutral point charges and periodic images, distinct from isolated gravity or an electron-density Hartree field.

variant: The released example is direct Ewald summation for neutral 3D point charges in a cubic cell with tin-foil boundaries. It includes real/reciprocal/self terms and checks cutoffs, splitting, energy-difference forces and an independent theta integral.

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
No charged-cell/background correction, triclinic cell, finite-dielectric surface term, slab correction, stress or material-specific force field.
Source curation is separate from completion of implementation and numerical validation.

Review: In addition to original-source and variant curation, independently extracted the new dedicated supplement ZIP and actually ran its fixed inputs and numerical checks. Dedicated examples and receipts state the adopted variant and scope.

Not checked:
- No charged-cell/background correction, triclinic cell, finite-dielectric surface term, slab correction, stress or material-specific force field.

Evidence:
- Fixed-input measured checks / 固定入力の実測判定: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
- Independent ZIP-extraction receipt / ZIP独立展開の記録: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

References:
- [original-method / primary-research] Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. — https://doi.org/10.1002/andp.19213690304
  Bibliographic origin of the real/reciprocal decomposition; the complete 1921 derivation was not audited.
  metadata (2026-11-22); Publisher record: author, title, year, volume 369, pp. 253–287; https://onlinelibrary.wiley.com/doi/10.1002/andp.19213690304
- [formulation / primary-research] Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. (1995). A smooth particle mesh Ewald method. — https://doi.org/10.1063/1.470117
  Full-text formulation used here to check neutrality, self corrections and surface conventions.
  full-text (2026-11-22); Sections II–IV, Eqs. (2.1)–(2.5), (4.1)–(4.8), and Appendix A surface-term discussion; https://biomolmd.org/mw/images/e/e0/Spme.pdf


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/ewald/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/ewald/



- Reference: https://doi.org/10.1002/andp.19213690304 — Bibliographic origin of the real/reciprocal decomposition; the complete 1921 derivation was not audited.
- Reference: https://doi.org/10.1063/1.470117 — Full-text formulation used here to check neutrality, self corrections and surface conventions.

## Small fixed-input validation supplements

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

- Neutral-cell Ewald sums and an independent theta integral: https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

Common execution records: [{"id": "ewald", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/
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

- [中性周期セルのEwald和と独立theta積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja) (`ewald`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#references-ja) (`neutral-periodic-charges`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/ewald/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 中性周期セルのEwald和と独立theta積分 (`ewald`)

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

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

- [Neutral-cell Ewald sums and an independent theta integral](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en) (`ewald`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.


#### Exact / reference solutions (`method-references-en`)

##### [Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#references-en) (`neutral-periodic-charges`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/ewald/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Neutral-cell Ewald sums and an independent theta integral (`ewald`)

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

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
