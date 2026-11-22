# Kohn–Sham density functional theory / DFT / Kohn–Sham密度汎関数法

Status: educational-example

Solve self-consistently for electron density using noninteracting orbitals and an exchange-correlation functional. The isolated-He example uses Dirac exchange only; the fixed periodic-He PySCF workflow adds VWN5 correlation.

非相互作用軌道と交換相関汎関数で電子密度を自己無撞着に求める。孤立HeはDirac交換のみ、固定周期HeはPySCFによるLDA交換＋VWN5相関の限定例を公開。

Atomic/molecular example scope: Separate exact-functional theory from the adopted Dirac exchange-only approximation. LDA correlation, GGA, meta-GGA, hybrids, spin polarization, molecules, periodic bands and excitations are not implemented. Grid convergence or agreement with an independent implementation of the same model does not establish functional accuracy. KS eigenvalues are not generally excitation energies. A separate PySCF periodic-He driver additionally uses VWN5 correlation and periodic k-point quadrature.

Other names: DFT, 密度汎関数法, 密度汎関数理論, コーン・シャム, density functional theory

Comparison notes: Distinguish exact-functional theory from calculations with approximate functionals. KS eigenvalues are not generally excitation energies; ground-state DFT alone does not guarantee excited-state accuracy.

正確な汎関数の理論と、近似汎関数による実計算を分けます。KS固有値を一般に励起エネルギーと同一視せず、基底状態DFTだけで励起状態まで保証しません。


## 条件と確認範囲 (ja)

problem: 選んだ近似汎関数の下でHeの基底状態密度とエネルギーを求める。

variant: Dirac交換のみ・スピン非偏極・球対称1s²のKS方程式。相関を追加した一般LDAではない。

use_when:
- 明示した交換汎関数からポテンシャルと全エネルギーを整合して求める。
- 同じ交換のみモデルで動径差分と独立PySCF RKS/Libxc参照を比較する。

avoid_when:
- このHe例をGGA・hybrid・分子・周期系・励起の検証済み実装として使う。
- 同じ近似同士の一致を実験や相関を含む厳密解への一致と解釈する。

assumptions [specified]:
- 原子・分子の実行例：基底状態・非相対論・孤立He、Z=2。同じ球対称1s Kohn–Sham空間軌道を2電子が占有する。
- 原子・分子の実行例：p=2|u|²=4πr²n、∫p dr=2。nは両スピンを合わせた正の電子数密度。
- 原子・分子の実行例：採用近似はE_x[n]=−(3/4)(3/π)¹ᐟ³∫n⁴ᐟ³d³r、v_x=−(3n/π)¹ᐟ³、E_c=v_c=0。
- 原子・分子の実行例：有効場−2/r+v_H+v_xを、動径2次差分と単純密度混合で解く限定モデル。
- 固定した1原子単純立方Heセルの周期KS-DFT。PySCFを使う教育用ワークフローで、Γ点／k点、Gaussian軌道基底、FFT補助格子、SCF公差を別々に検査し、同じGTHパラメータ・LDA交換＋VWN5相関のDFTK平面波計算と比較。平衡He結晶や一般物質・金属の検証ではありません。
Heの閉殻占有とlda_xの交換のみ近似を確認。

units [specified]:
原子・分子の実行例：原子単位系（ℏ=mₑ=e=4πε₀=1）。rはbohr、エネルギー・有効ポテンシャルはhartree、規格化した縮約軌道uはbohr⁻¹ᐟ²。正の電子数密度n(r)はbohr⁻³、動径電子数密度p(r)=4πr²n(r)はbohr⁻¹、∫p dr=N。pは符号付き電荷密度ではありません。 周期He：bohr・逆bohr・中性基本セル当たりhartree、逆格子での分率k座標。
全密度nと動径密度pを区別し、原子単位系を指定。

boundary_conditions [specified]:
原子・分子の実行例：He縮約軌道にu(0)=u(r_max)=0（基本r_max=16 bohr、別途4/8/12/16 bohrの領域検査）。Hartree場は原点で有限、密度の外ではN/rへ接続し、r_maxで0には固定しません。 周期He：固定1原子単純立方セルの3次元Bloch境界。
孤立Heの軌道とHartree場に異なる境界を使用。

limitations [specified]:
原子・分子の実行例の範囲：厳密汎関数の理論とDirac交換のみという近似を区別する。LDA相関、GGA、meta-GGA、hybrid、スピン分極、分子、周期バンド計算、励起は未実装。格子収束や独立な同一モデルとの一致は汎関数の物理精度を保証しない。KS固有値を一般の励起エネルギーと同一視しない。 周期He側では別のPySCFドライバーがVWN5相関と周期k点積分を扱う。
KSの一般定式化と実装した1近似・1対称性を区別。

Review: 既存公開版の実装・検査・保存結果を読んだ点検であり、この点検では再実行していません。helium('lda_x')・lda_exchange、汎関数微分・SCF・エネルギー会計の検査、保存RKS比較を確認。reference_pyscf.pyの'LDA_X,'を公式文法と照合。 周期Heの新しいライブラリ実行検証は別記録に掲載。

Not checked:
- 新規再実行、相関・スピン分極・分子・周期DFT・励起精度は点検対象外。
- 原論文の全導出を再現したものではない。

Evidence:
- helium(model='lda_x'); lda_exchange: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_lda_exchange_is_functional_derivative_of_the_same_energy; test_helium_scf_and_independent_reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- calculate: RKS with explicit LDA_X, and independently evaluated Gaussian integrals/Libxc: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference_pyscf.py
- Stored RKS functional, basis/grid convergence and versions: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- helium.independent_comparison and helium.refinement: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [formulation / primary-research] Hohenberg, P. and Kohn, W. (1964). Inhomogeneous Electron Gas. — https://doi.org/10.1103/PhysRev.136.B864
  基底状態の密度汎関数による定式化の基礎。具体的なDirac交換近似とは別。
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.136.B864
- [original-method / primary-research] Kohn, W. and Sham, L. J. (1965). Self-Consistent Equations Including Exchange and Correlation Effects. — https://doi.org/10.1103/PhysRev.140.A1133
  非相互作用軌道と交換相関有効場の自己無撞着定式化。
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133
- [adopted-variant / primary-research] Dirac, P. A. M. (1930). Note on Exchange Phenomena in the Thomas Atom. — https://doi.org/10.1017/S0305004100016108
  交換のみ局所密度項の原型。歴史的Thomas原子計算そのものを再現したのではない。
  full-text (2026-11-22); Selected text on pp. 381–385: Coulomb versus exchange operators around (12)–(13), energy accounting, and local phase-space reduction through (18)–(20); not an equation-by-equation derivation audit; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C5FF7297CD96F49A8B8E9E3EA50E412/S0305004100016108a.pdf/note_on_exchange_phenomena_in_the_thomas_atom.pdf
- [reference-solution / official-documentation] PySCF documentation: Density functional theory (DFT) — https://pyscf.org/user/dft.html
  独立参照側の汎関数指定を確認する資料。コンマの後を空にすると相関を含めない。
  full-text (2026-11-22); Theory; Predefined xc Functionals and Functional Aliases; Customizing xc functionals (comma-separated exchange/correlation grammar); https://pyscf.org/user/dft.html

## Conditions and review scope (en)

problem: Find helium ground-state density and energy for a specified approximate functional.

variant: Spin-unpolarized spherical 1s² KS equations with Dirac exchange only, not a general LDA including correlation.

use_when:
- Keep potentials and total energies consistent with an explicitly specified exchange functional.
- Compare radial differences against independent PySCF RKS/Libxc references for the same exchange-only model.

avoid_when:
- Treating this helium example as validated GGA/hybrid, molecular, periodic or excited-state software.
- Interpreting agreement within the same approximation as agreement with experiment or a correlated exact solution.

assumptions [specified]:
- Atomic/molecular examples: Ground-state nonrelativistic isolated He with Z=2 and one doubly occupied spherical 1s Kohn–Sham orbital.
- Atomic/molecular examples: p=2|u|^2=4 pi r^2 n and integral p dr=2, with n the total positive electron-number density of both spins.
- Atomic/molecular examples: The adopted approximation is E_x[n]=-(3/4)(3/pi)^(1/3) integral n^(4/3) d^3r, v_x=-(3n/pi)^(1/3), and E_c=v_c=0.
- Atomic/molecular examples: The effective field is -2/r+v_H+v_x; second-order radial differences and simple density mixing solve this restricted model.
- Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals.
Checked closed-shell helium occupations and exchange-only lda_x.

units [specified]:
Atomic/molecular examples: Atomic units (hbar=m_e=e=4 pi epsilon_0=1): r in bohr, energies/effective potentials in hartree, and normalized reduced orbitals u in bohr^(-1/2). Positive electron-number density n(r) is in bohr^(-3); radial number density p(r)=4 pi r^2 n(r) is in bohr^(-1), with integral p dr=N. p is not signed charge density. Periodic He: bohr, inverse bohr and hartree per neutral primitive cell; reciprocal-lattice fractional k coordinates.
Distinguished total density n from radial density p and specified atomic units.

boundary_conditions [specified]:
Atomic/molecular examples: Helium reduced orbital: u(0)=u(r_max)=0, baseline r_max=16 bohr with a separate 4/8/12/16-bohr domain study. The Hartree field is finite at the origin and joins N/r outside the density; it is not fixed to zero at r_max. Periodic He: three-dimensional Bloch boundaries in the fixed one-atom simple-cubic cell.
Specified distinct isolated-helium orbital and Hartree boundaries.

limitations [specified]:
Atomic/molecular example scope: Separate exact-functional theory from the adopted Dirac exchange-only approximation. LDA correlation, GGA, meta-GGA, hybrids, spin polarization, molecules, periodic bands and excitations are not implemented. Grid convergence or agreement with an independent implementation of the same model does not establish functional accuracy. KS eigenvalues are not generally excitation energies. A separate PySCF periodic-He driver additionally uses VWN5 correlation and periodic k-point quadrature.
Separated general KS theory from the implemented approximation and symmetry.

Review: This inspection reads the released implementation, tests and saved results; it does not rerun the calculation. Inspected helium('lda_x')/lda_exchange, functional-derivative, SCF and energy-accounting tests, and saved RKS comparisons. Checked the reference script's 'LDA_X,' against official syntax. New library-backed periodic-He validation is recorded separately.

Not checked:
- No new run or accuracy audit of correlation, spin polarization, molecular/periodic DFT or excitations.
- The original papers' complete derivations have not been reproduced.

Evidence:
- helium(model='lda_x'); lda_exchange: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_lda_exchange_is_functional_derivative_of_the_same_energy; test_helium_scf_and_independent_reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- calculate: RKS with explicit LDA_X, and independently evaluated Gaussian integrals/Libxc: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference_pyscf.py
- Stored RKS functional, basis/grid convergence and versions: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- helium.independent_comparison and helium.refinement: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [formulation / primary-research] Hohenberg, P. and Kohn, W. (1964). Inhomogeneous Electron Gas. — https://doi.org/10.1103/PhysRev.136.B864
  Ground-state density-functional foundation, distinct from the adopted Dirac exchange approximation.
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.136.B864
- [original-method / primary-research] Kohn, W. and Sham, L. J. (1965). Self-Consistent Equations Including Exchange and Correlation Effects. — https://doi.org/10.1103/PhysRev.140.A1133
  Self-consistent noninteracting-orbital formulation with exchange-correlation effective potentials.
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133
- [adopted-variant / primary-research] Dirac, P. A. M. (1930). Note on Exchange Phenomena in the Thomas Atom. — https://doi.org/10.1017/S0305004100016108
  Historical local-density exchange origin; the released code does not reproduce the historical Thomas-atom calculation.
  full-text (2026-11-22); Selected text on pp. 381–385: Coulomb versus exchange operators around (12)–(13), energy accounting, and local phase-space reduction through (18)–(20); not an equation-by-equation derivation audit; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C5FF7297CD96F49A8B8E9E3EA50E412/S0305004100016108a.pdf/note_on_exchange_phenomena_in_the_thomas_atom.pdf
- [reference-solution / official-documentation] PySCF documentation: Density functional theory (DFT) — https://pyscf.org/user/dft.html
  Documents exchange/correlation syntax in the reference engine; an empty part after the comma omits correlation.
  full-text (2026-11-22); Theory; Predefined xc Functionals and Functional Aliases; Customizing xc functionals (comma-separated exchange/correlation grammar); https://pyscf.org/user/dft.html


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#kohn-sham-dft
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#kohn-sham-dft



- Reference: https://doi.org/10.1103/PhysRev.136.B864 — Ground-state density-functional foundation, distinct from the adopted Dirac exchange approximation.
- Reference: https://doi.org/10.1103/PhysRev.140.A1133 — Self-consistent noninteracting-orbital formulation with exchange-correlation effective potentials.
- Reference: https://doi.org/10.1017/S0305004100016108 — Historical local-density exchange origin; the released code does not reproduce the historical Thomas-atom calculation.
- Reference: https://pyscf.org/user/dft.html — Documents the reference engine's exchange/correlation string syntax; LDA_X, leaves correlation empty. It does not validate the atlas implementation.

Scoped example: Spin-unpolarized exchange-only Dirac LDA for spherical helium; correlation, GGA, hybrids, molecules, periodic systems and excitations are not implemented.

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

Next: A small reproducible case with a specified exchange-correlation model.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
