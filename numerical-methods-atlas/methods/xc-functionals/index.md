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

Common execution records: [{"id": "helium-ground-state", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#helium-ground-state-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#helium-ground-state-en"}}, {"id": "periodic-he-dft", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-dft-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-dft-en"}}]

Next: Document functional, grid, basis and primary references.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
