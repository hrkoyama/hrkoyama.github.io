# Coulomb and Hartree potentials / Coulomb・Hartreeポテンシャル

Status: educational-example

Compute the repulsive Hartree field and energy from positive electron-number density. The released implementation evaluates spherical Coulomb integrals using inward/outward cumulative sums, not a general three-dimensional Poisson solver.

正の電子数密度から電子間反発のHartree場とエネルギーを求める。公開実装は球対称密度のCoulomb積分を内側・外側の累積和で評価し、汎用の3次元Poissonソルバーは用いない。

An integral evaluator for spherical isolated densities truncated in a finite box. It does not treat nonspherical/general boundaries, periodicity, Ewald/background charges or singular point-charge self-energies. Avoiding a double-counted same-radius sample is quadrature bookkeeping, not removal of DFT self-interaction; the helium-HF cancellation comes from the separate exchange reduction.

Other names: Hartree potential, 電子密度, Coulomb

Comparison notes: Check the Poisson residual, integrated electron number, far-field behavior and the one-half double-counting factor separately. A charged periodic cell does not directly give an isolated-system energy.

Poisson解の残差、積分した電子数、遠方の挙動、二重計数の1/2を別々に確かめます。周期セルの帯電系を孤立系のエネルギーとして解釈しません。


## 条件と確認範囲 (ja)

problem: 与えた球対称電子数密度が作る孤立系Coulomb反発場とHartreeエネルギーを求める。

variant: 動径密度pに対する内側・外側積分の累積求積。Poisson式は符号と境界の等価な記述で、専用PDE反復解法ではない。

use_when:
- 球対称の滑らかな電子密度でv_HとE_Hを評価する。
- 解析的指数密度と遠方の電子数/rでCoulomb場の符号・境界・会計を確認する。

avoid_when:
- 非球対称・周期系にこの1次元Coulomb積分をそのまま適用する。
- 同じ求積の標本を1回にする処理を、点電荷自己エネルギー除去や交換と混同する。

assumptions [specified]:
- 非負・球対称の電子数密度n(r)を仮定。p(r)=4πr²n(r)、∫p dr=Nと定義し、公開He例はN=2。
- 孤立系のv_H(r)=∫₀ᴿp(s)/max(r,s)dsとE_H=(1/2)∫p(r)v_H(r)drを評価する。
- 一様格子の累積求積を用い、両端p=0、有限箱外の密度は0とする。同じ半径の求積標本を1回だけ数える。
- v_Hは正の電子間反発で、原子単位系で∇²v_H=−4πn。符号付き電子電荷密度は−nであり、v_Hは負電荷が作る静電ポテンシャルそのものではなく電子のポテンシャルエネルギー。
hartree_potentialの入力は符号付き電荷ではなくp=4πr²n。

units [specified]:
原子単位系。rはbohr、nはbohr⁻³、pはbohr⁻¹、Nは電子数、v_HとE_Hはhartree。正の電子数密度という規約とPoisson式の符号を組にする。
数密度・動径密度・反発ポテンシャルの単位と符号を指定。

boundary_conditions [specified]:
孤立・球対称Coulomb境界。v_Hは原点で有限、切断した密度の外側ではN/r。r_maxで0とするDirichlet条件ではない。端点p=0は縮約軌道から与え、周期系の中性化・背景電荷の規約は実装していない。
原点有限・密度外N/rを確認。軌道のu=0境界とは異なる。

limitations [specified]:
球対称・孤立・有限箱で切断した密度用の積分評価。非球対称、一般の境界形状、周期系、Ewaldや背景電荷、点電荷の特異自己エネルギーは扱わない。同半径標本の重複回避は求積の会計であり、DFTの物理的自己相互作用を除去する操作ではない。He HFでの自己相互作用相殺は別の交換簡約に由来する。
球対称求積、求積の対角標本、物理的自己相互作用を区別。

Review: 既存公開版の実装・検査・保存結果を読んだ点検であり、この点検では再実行していません。hartree_potentialと解析的指数密度・Hartreeエネルギー・遠方電荷の検査を確認。Heの保存エネルギー会計も参照。

Not checked:
- 新規再実行、3次元Poisson残差、非球対称・周期系・点電荷は未検証。
- 解析密度の検査は任意の密度・領域に対する誤差保証ではない。

Evidence:
- hartree_potential; helium Hartree energy accounting: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_hartree_analytic_exponential_density_and_single_counted_diagonal: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- helium.refinement and checks.helium_energy_identity: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [context / primary-research] Hartree, D. R. (1928). The Wave Mechanics of an Atom with a Non-Coulomb Central Field. Part I. Theory and Methods. — https://doi.org/10.1017/S0305004100011919
  原子の中心場・動径問題の歴史的な入口。原論文のshootingを累積和実装の出典としない。
  abstract-and-metadata (2026-11-22); Publisher Extract and bibliographic record; historical radial shooting described in extract; full paper not read; https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/wave-mechanics-of-an-atom-with-a-noncoulomb-central-field-part-i-theory-and-methods/C9417AC1CEC84B934C1EA4C4B8401FEF
- [formulation / primary-research] Dirac, P. A. M. (1930). Note on Exchange Phenomena in the Thomas Atom. — https://doi.org/10.1017/S0305004100016108
  Coulombの直接項と交換項を区別する定式化の資料。公開する球対称求積とは区別する。
  full-text (2026-11-22); Selected text on pp. 381–385: Coulomb versus exchange operators around (12)–(13), energy accounting, and local phase-space reduction through (18)–(20); not an equation-by-equation derivation audit; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C5FF7297CD96F49A8B8E9E3EA50E412/S0305004100016108a.pdf/note_on_exchange_phenomena_in_the_thomas_atom.pdf
- [formulation / primary-research] Kohn, W. and Sham, L. J. (1965). Self-Consistent Equations Including Exchange and Correlation Effects. — https://doi.org/10.1103/PhysRev.140.A1133
  電子の自己無撞着有効場におけるHartree項の位置づけ。
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133

## Conditions and review scope (en)

problem: Find the isolated repulsive Coulomb field and Hartree energy of a specified spherical electron-number density.

variant: Cumulative inner/outer radial quadrature in p; Poisson's equation provides the equivalent sign/boundary interpretation, not a separate iterative PDE solver.

use_when:
- Evaluate v_H and E_H for smooth spherical electron densities.
- Check sign, boundaries and accounting against analytic exponential density and the N/r far field.

avoid_when:
- Applying this one-dimensional Coulomb integral directly to nonspherical or periodic systems.
- Confusing quadrature sample counting with point-charge self-energy removal or exchange.

assumptions [specified]:
- A nonnegative spherically symmetric electron-number density n(r), with p(r)=4 pi r^2 n(r) and integral p dr=N; released helium uses N=2.
- For an isolated system, v_H(r)=integral_0^R p(s)/max(r,s) ds and E_H=(1/2) integral p(r)v_H(r) dr.
- The code uses uniform-grid cumulative quadrature with p=0 at the two endpoints and zero density outside the finite box; the same-radius quadrature sample is counted once.
- v_H is positive electron repulsion and satisfies Laplacian(v_H)=-4 pi n in atomic units. Signed electronic charge density is -n; v_H is electron potential energy, not the electrostatic potential generated by that negative charge.
hartree_potential takes p=4 pi r^2 n, not signed charge.

units [specified]:
Atomic units: r in bohr, n in bohr^(-3), p in bohr^(-1), N an electron number, v_H and E_H in hartree. The positive-number-density convention fixes the Poisson sign.
Specified number/radial density and repulsive-potential units/sign.

boundary_conditions [specified]:
Isolated spherical Coulomb boundary: v_H is finite at the origin and equals N/r outside the truncated density support. It is not a zero-Dirichlet condition at r_max. Endpoint p=0 is inherited from the reduced orbital; no periodic neutrality/background convention is implemented.
Checked finite-origin/N/r behavior, distinct from the orbital's u=0 boundaries.

limitations [specified]:
An integral evaluator for spherical isolated densities truncated in a finite box. It does not treat nonspherical/general boundaries, periodicity, Ewald/background charges or singular point-charge self-energies. Avoiding a double-counted same-radius sample is quadrature bookkeeping, not removal of DFT self-interaction; the helium-HF cancellation comes from the separate exchange reduction.
Distinguished spherical quadrature, diagonal samples and physical self-interaction.

Review: This inspection reads the released implementation, tests and saved results; it does not rerun the calculation. Inspected hartree_potential and analytic exponential-density, Hartree-energy and far-field-charge tests, plus saved helium energy accounting.

Not checked:
- No new run or validation of three-dimensional Poisson residuals, nonspherical/periodic systems or point charges.
- The analytic-density test is not an error guarantee for arbitrary densities/domains.

Evidence:
- hartree_potential; helium Hartree energy accounting: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_hartree_analytic_exponential_density_and_single_counted_diagonal: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- helium.refinement and checks.helium_energy_identity: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [context / primary-research] Hartree, D. R. (1928). The Wave Mechanics of an Atom with a Non-Coulomb Central Field. Part I. Theory and Methods. — https://doi.org/10.1017/S0305004100011919
  Historical context for atomic central-field radial problems; its shooting method is not the cumulative-sum implementation.
  abstract-and-metadata (2026-11-22); Publisher Extract and bibliographic record; historical radial shooting described in extract; full paper not read; https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/wave-mechanics-of-an-atom-with-a-noncoulomb-central-field-part-i-theory-and-methods/C9417AC1CEC84B934C1EA4C4B8401FEF
- [formulation / primary-research] Dirac, P. A. M. (1930). Note on Exchange Phenomena in the Thomas Atom. — https://doi.org/10.1017/S0305004100016108
  Formulation distinguishing direct Coulomb and exchange terms, separate from the released spherical quadrature.
  full-text (2026-11-22); Selected text on pp. 381–385: Coulomb versus exchange operators around (12)–(13), energy accounting, and local phase-space reduction through (18)–(20); not an equation-by-equation derivation audit; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C5FF7297CD96F49A8B8E9E3EA50E412/S0305004100016108a.pdf/note_on_exchange_phenomena_in_the_thomas_atom.pdf
- [formulation / primary-research] Kohn, W. and Sham, L. J. (1965). Self-Consistent Equations Including Exchange and Correlation Effects. — https://doi.org/10.1103/PhysRev.140.A1133
  Places the Hartree term within electronic self-consistent effective fields.
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#hartree-poisson
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#hartree-poisson



- Reference: https://doi.org/10.1017/S0305004100011919 — Historical context for atomic central-field radial problems; its shooting method is not the cumulative-sum implementation.
- Reference: https://doi.org/10.1017/S0305004100016108 — Formulation distinguishing direct Coulomb and exchange terms, separate from the released spherical quadrature.
- Reference: https://doi.org/10.1103/PhysRev.140.A1133 — Places the Hartree term within electronic self-consistent effective fields.

Scoped example: Cumulative Coulomb quadrature for isolated spherical densities, checked against analytic exponential densities; not a general 3D or periodic Poisson implementation.

[
  {
    "id": "helium-ground-state",
    "section": "helium",
    "name": {
      "ja": "He基底状態：閉殻HF・交換のみLDA",
      "en": "Helium ground state: closed-shell HF and exchange-only LDA"
    },
    "result_pointer": "/helium/refinement",
    "figure": "helium.png",
    "reading": {
      "ja": "https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/#helium",
      "en": "https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#helium"
    }
  }
]

Download: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip
Verification: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json
Source: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
Results: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json
Commands (from extracted atomic edition):

python -m pytest -q
python run.py --input inputs.json --output output --figures

Common execution records: [{"id": "helium-ground-state", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#helium-ground-state-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#helium-ground-state-en"}}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`; helium-ground-state)
- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`; helium-ground-state)
- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`; helium-ground-state)

#### 問題の図 (`method-problems-ja`)

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。


#### 厳密解・参照解 (`method-references-ja`)

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) (`helium-ground-state`)

- [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja) (`atomic-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#hartree-poisson)
- 独立参照: [独立参照の保存データ](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### He：閉殻HF・交換のみLDA (`helium-ground-state`)

[He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[固定入力](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### 関連ソース

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)

###### 配布版のテスト

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`; helium-ground-state)
- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`; helium-ground-state)
- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`; helium-ground-state)

#### Problem figures (`method-problems-en`)

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.


#### Exact / reference solutions (`method-references-en`)

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) (`helium-ground-state`)

- [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en) (`atomic-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

[Existing reference profile](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#hartree-poisson)
- Independent reference: [Saved independent-reference data](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Helium: closed-shell HF and exchange-only LDA (`helium-ground-state`)

[Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[Fixed input](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

[Related code edition / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### Related source

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)

###### Package tests

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```
