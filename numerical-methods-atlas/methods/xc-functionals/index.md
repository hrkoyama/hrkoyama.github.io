# LDA, GGA and hybrid functionals / LDA・GGA・hybrid汎関数

Status: educational-example

Distinguish functional ingredients and model error. Isolated He uses Dirac exchange only; the fixed periodic-He example uses LDA_X plus VWN5 correlation. GGA, meta-GGA and hybrids remain reading only.

交換相関近似の入力依存性とモデル誤差を区別する。孤立He例はDirac交換のみ、固定周期He例はLDA_X＋VWN5相関。GGA・meta-GGA・hybridは解説のみ。

Atomic/molecular example scope: No correlation, spin polarization, density gradients, kinetic-energy-density ingredients or nonlocal exchange. PBE, SCAN and hybrid methods are not implemented or validated here. Agreement with an independent implementation of the same functional or grid convergence does not establish model accuracy, eliminate self-interaction error or guarantee experimental agreement. Distinguish Dirac's historical Thomas-atom approximation from this KS orbital solver. A separate PySCF periodic-He driver additionally uses VWN5 correlation and periodic k-point quadrature.

Other names: LDA, GGA, meta-GGA, hybrid, PBE, PBE0, SCAN, B3LYP, 交換相関汎関数

Comparison notes: Basis, grid and SCF convergence do not remove functional error. Assess self-interaction, charge transfer, strong correlation and dispersion for the chosen system and approximation.

基底・格子・SCFが収束しても汎関数の近似誤差は消えません。自己相互作用、電荷移動、強相関、分散の扱いは対象と近似に応じて評価します。


## 条件と確認範囲 (ja)

problem: 電子状態計算で不足する交換相関エネルギーを指定し、対応する有効ポテンシャルを整合して求める。

variant: スピン非偏極Dirac交換のみ（LDA_X）。E_c=0、p=4πr²nを介した動径積分でE_xとv_xを同時に返す。

use_when:
- 同じ密度・スピン規約でエネルギーと汎関数微分の整合を学ぶ。
- 交換のみという同一条件で独立実装と照合し、数値誤差とモデル誤差を分ける。

avoid_when:
- 相関を含む汎関数、スピン分極、GGA・meta-GGA・hybridの結果が必要。
- HeのLDA_X参照一致を、汎関数全般や分子・固体への精度保証に使う。

assumptions [specified]:
- 原子・分子の実行例：両スピンを合計した正の電子数密度n=n_up+n_downを用い、n_up=n_down=n/2のスピン非偏極を仮定。動径例ではn=p/(4πr²)。
- 原子・分子の実行例：実装はE_x=−(3/4)(3/π)¹ᐟ³∫n⁴ᐟ³d³r、v_x=δE_x/δn=−(3n/π)¹ᐟ³で、E_x=(3/4)∫p v_x dr。
- 原子・分子の実行例：E_c=v_c=0を明示する。相関のパラメータ化を追加したLDAでも、係数不明のSlater Xαでもない。
- 原子・分子の実行例：公開実行は球対称・閉殻He 1s²。独立参照もxc='LDA_X,'と指定し、同じ交換のみ近似を比較する。
- 固定した1原子単純立方Heセルの周期KS-DFT。PySCFを使う教育用ワークフローで、Γ点／k点、Gaussian軌道基底、FFT補助格子、SCF公差を別々に検査し、同じGTHパラメータ・LDA交換＋VWN5相関のDFTK平面波計算と比較。平衡He結晶や一般物質・金属の検証ではありません。
lda_exchangeのn=p/(4πr²)、交換係数、E_c=0と参照のLDA_X指定を確認。

units [specified]:
原子・分子の実行例：原子単位系。全電子数密度nはbohr⁻³、動径密度pはbohr⁻¹、局所v_xと積分したE_xはhartree。エネルギー汎関数とその微分で密度・スピンの規約をそろえる。 周期He：bohr・逆bohr・中性基本セル当たりhartree、逆格子での分率k座標。
nとpを区別し、汎関数微分と全エネルギーに同じ規約を適用。

boundary_conditions [not-applicable]:
原子・分子の実行例：局所交換汎関数自体には空間境界条件はない。密度・軌道の問題が孤立Heの箱と規格化を与える。勾配項・非局所交換・周期系の境界処理は実装対象外。 周期He：固定1原子単純立方セルの3次元Bloch境界。
局所汎関数は密度を評価するだけで、空間境界はHeの軌道問題が供給。

limitations [specified]:
原子・分子の実行例の範囲：相関、スピン分極、密度勾配、運動エネルギー密度、非局所交換を含まない。PBE・SCAN・hybridを実装・検証したという意味ではない。同一汎関数の独立実装との一致や格子収束は、交換相関モデルの精度・自己相互作用誤差・実験への一致を保証しない。Dirac原論文のThomas原子近似と本例のKS軌道解法を区別する。 周期He側では別のPySCFドライバーがVWN5相関と周期k点積分を扱う。
採用したLDA_Xと文献上のGGA/meta-GGA/hybridを区別。

Review: 既存公開版の実装・検査・保存結果を読んだ点検であり、この点検では再実行していません。lda_exchange、同一エネルギーの汎関数微分を摂動で調べる検査、保存済みLDA_X独立比較と明示的な参照汎関数指定を確認。 周期Heの新しいライブラリ実行検証は別記録に掲載。

Not checked:
- 新規再実行、相関・GGA・meta-GGA・hybrid・スピン分極の実装検証はない。
- Dirac公式PDFは関連箇所の本文を読んだ範囲であり、原論文の全導出や係数の全式照合をしたわけではない。

Evidence:
- lda_exchange; helium Ec=0 accounting: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_lda_exchange_is_functional_derivative_of_the_same_energy: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- calculate: explicit exchange-only LDA_X, specification: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference_pyscf.py
- Stored functional and independent radial-density/energy reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- helium.independent_comparison for lda_x: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [adopted-variant / primary-research] Dirac, P. A. M. (1930). Note on Exchange Phenomena in the Thomas Atom. — https://doi.org/10.1017/S0305004100016108
  採用する局所交換の歴史的原型。現代原子単位系の係数は公開コードと独立参照の指定を別途確認。
  full-text (2026-11-22); Selected text on pp. 381–385: Coulomb versus exchange operators around (12)–(13), energy accounting, and local phase-space reduction through (18)–(20); not an equation-by-equation derivation audit; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C5FF7297CD96F49A8B8E9E3EA50E412/S0305004100016108a.pdf/note_on_exchange_phenomena_in_the_thomas_atom.pdf
- [context / primary-research] Perdew, J. P. and Burke, K. and Ernzerhof, M. (1996). Generalized Gradient Approximation Made Simple. — https://doi.org/10.1103/PhysRevLett.77.3865
  GGAとの比較用の一次文献。公開例にはPBEを採用していない。
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper and erratum not read; https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.3865
- [context / primary-research] Sun, J. and Ruzsinszky, A. and Perdew, J. P. (2015). Strongly Constrained and Appropriately Normed Semilocal Density Functional. — https://doi.org/10.1103/PhysRevLett.115.036402
  meta-GGAとの比較用の一次文献。公開例にはSCANを採用していない。
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; functional derivation and constraint proofs not read; https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.115.036402

## Conditions and review scope (en)

problem: Specify approximate exchange-correlation energy and obtain a consistent effective potential in electronic-structure calculations.

variant: Spin-unpolarized Dirac exchange only (LDA_X), E_c=0; radial integration through p=4 pi r^2 n returns consistent E_x and v_x.

use_when:
- Study consistency between energy and its functional derivative under one density/spin convention.
- Compare independent implementations of the same exchange-only model and separate numerical from model errors.

avoid_when:
- Requiring correlation, spin polarization, GGA, meta-GGA or hybrid results.
- Using helium LDA_X agreement as a general functional or molecular/solid accuracy guarantee.

assumptions [specified]:
- Atomic/molecular examples: Use the total spin-unpolarized positive number density n=n_up+n_down, with n_up=n_down=n/2; in the radial example n=p/(4 pi r^2).
- Atomic/molecular examples: The implemented exchange is E_x=-(3/4)(3/pi)^(1/3) integral n^(4/3) d^3r and v_x=delta E_x/delta n=-(3n/pi)^(1/3), hence E_x=(3/4) integral p v_x dr.
- Atomic/molecular examples: Set E_c=v_c=0 explicitly. This is not LDA plus a correlation parameterization and not Slater X-alpha with an unspecified coefficient.
- Atomic/molecular examples: The public execution uses spherical closed-shell He 1s² and independently compares the same exchange-only choice against PySCF with xc='LDA_X,'.
- Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals.
Checked n=p/(4 pi r^2), exchange coefficient, E_c=0 and reference LDA_X settings.

units [specified]:
Atomic/molecular examples: Atomic units: total number density n in bohr^(-3), radial p in bohr^(-1), local v_x in hartree, and integrated E_x in hartree. The energy functional and its derivative use the same density and spin convention. Periodic He: bohr, inverse bohr and hartree per neutral primitive cell; reciprocal-lattice fractional k coordinates.
Distinguished n/p and used one convention for the functional derivative and total energy.

boundary_conditions [not-applicable]:
Atomic/molecular examples: The local exchange functional itself has no spatial boundary condition. The density/orbital problem supplies the isolated helium box and normalization. Gradient, nonlocal-exchange or periodic-functional boundaries are outside this implementation. Periodic He: three-dimensional Bloch boundaries in the fixed one-atom simple-cubic cell.
The local functional evaluates a supplied density; the helium orbital problem supplies boundaries.

limitations [specified]:
Atomic/molecular example scope: No correlation, spin polarization, density gradients, kinetic-energy-density ingredients or nonlocal exchange. PBE, SCAN and hybrid methods are not implemented or validated here. Agreement with an independent implementation of the same functional or grid convergence does not establish model accuracy, eliminate self-interaction error or guarantee experimental agreement. Distinguish Dirac's historical Thomas-atom approximation from this KS orbital solver. A separate PySCF periodic-He driver additionally uses VWN5 correlation and periodic k-point quadrature.
Distinguished adopted LDA_X from literature-only GGA/meta-GGA/hybrid coverage.

Review: This inspection reads the released implementation, tests and saved results; it does not rerun the calculation. Inspected lda_exchange, a perturbation test of the same energy's functional derivative, saved independent LDA_X comparisons and explicit reference-functional settings. New library-backed periodic-He validation is recorded separately.

Not checked:
- No new run or implementation validation of correlation, GGA, meta-GGA, hybrids or spin polarization.
- Dirac's official PDF was read in selected relevant passages, not audited equation by equation or through every historical coefficient.

Evidence:
- lda_exchange; helium Ec=0 accounting: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_lda_exchange_is_functional_derivative_of_the_same_energy: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- calculate: explicit exchange-only LDA_X, specification: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference_pyscf.py
- Stored functional and independent radial-density/energy reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- helium.independent_comparison for lda_x: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [adopted-variant / primary-research] Dirac, P. A. M. (1930). Note on Exchange Phenomena in the Thomas Atom. — https://doi.org/10.1017/S0305004100016108
  Historical origin of the adopted local exchange; modern atomic-unit coefficients are checked separately in code and reference settings.
  full-text (2026-11-22); Selected text on pp. 381–385: Coulomb versus exchange operators around (12)–(13), energy accounting, and local phase-space reduction through (18)–(20); not an equation-by-equation derivation audit; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C5FF7297CD96F49A8B8E9E3EA50E412/S0305004100016108a.pdf/note_on_exchange_phenomena_in_the_thomas_atom.pdf
- [context / primary-research] Perdew, J. P. and Burke, K. and Ernzerhof, M. (1996). Generalized Gradient Approximation Made Simple. — https://doi.org/10.1103/PhysRevLett.77.3865
  Primary context for GGA; PBE is not adopted by the released example.
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper and erratum not read; https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.3865
- [context / primary-research] Sun, J. and Ruzsinszky, A. and Perdew, J. P. (2015). Strongly Constrained and Appropriately Normed Semilocal Density Functional. — https://doi.org/10.1103/PhysRevLett.115.036402
  Primary context for meta-GGA; SCAN is not adopted by the released example.
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; functional derivation and constraint proofs not read; https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.115.036402


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#xc-functionals
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#xc-functionals



- Reference: https://doi.org/10.1017/S0305004100016108 — Historical origin of the adopted local exchange; modern atomic-unit coefficients are checked separately in code and reference settings.
- Reference: https://doi.org/10.1103/PhysRevLett.77.3865 — Primary context for GGA; PBE is not adopted by the released example.
- Reference: https://doi.org/10.1103/PhysRevLett.115.036402 — Primary context for meta-GGA; SCAN is not adopted by the released example.

Scoped example: Only spin-unpolarized Dirac exchange energy and its functional derivative are verified; LDA correlation, GGA, meta-GGA and hybrids remain reading-only.

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

Periodic scope: Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals.

{
  "release": {
    "family": "periodic-dft",
    "version": "2026-11-22",
    "download": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip",
    "sha256": "f331515e3ad419b5435dbf851553c6b853b28b2432801fc13c84109faa362df8",
    "manifest": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/source-manifest.json",
    "manifest_sha256": "1ac7fe2531934a598b7d9b69930c5a8a83f6b5bf2a67ae9f0616f35aa63f34fd",
    "verification": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json",
    "archive_directory": "periodic-dft-2026-11-22"
  },
  "code_base": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/",
  "examples": [
    "periodic-he-dft"
  ],
  "run_commands": [
    "python run.py --input inputs.json --output output"
  ],
  "scope": {
    "ja": "固定した1原子単純立方Heセルの周期KS-DFT。PySCFを使う教育用ワークフローで、Γ点／k点、Gaussian軌道基底、FFT補助格子、SCF公差を別々に検査し、同じGTHパラメータ・LDA交換＋VWN5相関のDFTK平面波計算と比較。平衡He結晶や一般物質・金属の検証ではありません。",
    "en": "Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals."
  },
  "implementation": "Original educational workflow using PySCF; independent reference uses DFTK."
}

Force scope: Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

{
  "release": {
    "family": "periodic-forces",
    "version": "2026-11-22",
    "download": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip",
    "sha256": "137d7981769d503d231b0c4bcc60a2ca61746faaadd0ee39d544dcf4efa07b19",
    "manifest": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/source-manifest.json",
    "manifest_sha256": "57f7180fcaf148dcffa60f2a689e7e39b2938fb4083c642d3ac7cc1813cccbc8",
    "verification": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/verification.json",
    "archive_directory": "periodic-forces-2026-11-22"
  },
  "code_base": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/",
  "examples": [
    "periodic-he-forces"
  ],
  "run_commands": [
    "python run.py --input inputs.json --output output"
  ],
  "scope": {
    "ja": "非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。",
    "en": "Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated."
  },
  "implementation": "Original PySCF force-validation workflow with independent DFTK reference; BOMD adapter is locally checked, not a validated production trajectory."
}

Common execution records: [{"id": "helium-ground-state", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#helium-ground-state-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#helium-ground-state-en"}}, {"id": "periodic-he-dft", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-dft-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-dft-en"}}, {"id": "periodic-he-forces", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-forces-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-forces-en"}}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`; helium-ground-state)
- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`; helium-ground-state, periodic-he-dft, periodic-he-forces)
- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`; helium-ground-state)

#### 問題の図 (`method-problems-ja`)

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

##### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja) (`periodic-he-dft`)

![固定Heセルの周期LDA：Γ点とkメッシュ、Gaussian軌道基底・FFT格子・SCFを分離。DFTK平面波参照の打切り収束と差も表示。](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#code-ja)

- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja) (`periodic-he-dft`) · [コードZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

##### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) (`periodic-he-forces`)

![非対称He₂の解析力をエネルギー有限差分とDFTK参照で比較。力のk点・基底・FFT・SCF収束とBOMDの局所接続確認。](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja)

- [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja) (`periodic-he-forces`) · [コードZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。


#### 厳密解・参照解 (`method-references-ja`)

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) (`helium-ground-state`)

- [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja) (`atomic-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-measurements)

##### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja) (`periodic-he-dft`)

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

[既存の参照図](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-measurements)

##### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja) (`periodic-he-forces`)

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

[既存の参照図](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#xc-functionals)
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

##### 周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF (`periodic-he-dft`)

[周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

##### 周期He₂の原子間力：解析力・有限差分・BOMD接続 (`periodic-he-forces`)

[周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### 関連ソース

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)
- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)

###### 配布版のテスト

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`; helium-ground-state)
- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`; helium-ground-state, periodic-he-dft, periodic-he-forces)
- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`; helium-ground-state)

#### Problem figures (`method-problems-en`)

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

##### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en) (`periodic-he-dft`)

![Periodic LDA for fixed He: separate Gamma/k sampling, Gaussian orbital basis, FFT grid and SCF. Includes independently converged DFTK plane-wave reference differences.](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#code-en)

- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en) (`periodic-he-dft`) · [Code ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

##### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) (`periodic-he-forces`)

![Asymmetric-He₂ analytic forces versus energy finite differences and DFTK reference. Force k-point, basis, FFT and SCF refinement, plus a local BOMD interface check.](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en)

- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en) (`periodic-he-forces`) · [Code ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.


#### Exact / reference solutions (`method-references-en`)

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) (`helium-ground-state`)

- [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en) (`atomic-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

[Existing reference profile](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-measurements)

##### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en) (`periodic-he-dft`)

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

[Existing reference profile](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-measurements)

##### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en) (`periodic-he-forces`)

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

[Existing reference profile](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#xc-functionals)
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

##### Periodic-He KS-LDA: Gamma, k meshes, basis and SCF (`periodic-he-dft`)

[Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

##### Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface (`periodic-he-forces`)

[Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

[Related code edition / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### Related source

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)
- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)

###### Package tests

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```
