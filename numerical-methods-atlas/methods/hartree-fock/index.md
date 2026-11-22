# Hartree–Fock / Hartree–Fock法

Status: educational-example

Find an exchange-containing mean field in a single Slater determinant. The released implementation is restricted to spherical closed-shell helium 1s² and uses the local reduction valid for one occupied spatial orbital.

単一Slater行列式により交換を含む平均場を求める。公開実装は球対称He 1s²の閉殻解に限り、1個の空間軌道で成立する局所交換への簡約を用いる。

The local exchange reduction cannot be transferred unchanged to multi-orbital, open-shell, molecular or periodic systems. The atomic edition does not implement UHF/ROHF, molecular integrals or orbital-stability analysis. Saved PySCF RHF references are independent finite-Gaussian-basis calculations, not exact correlated helium energies. Separate grid, domain and SCF convergence from physical model error. H₂ uses a separate molecular-integral implementation. Molecular DFT, general multicenter molecules, open shells and orbital-stability analysis remain unimplemented.

Other names: HF, RHF, UHF, ROHF, ハートリー・フォック

Comparison notes: HF solutions need not be unique. SCF termination does not prove basis convergence, orbital stability or the desired electronic state. Bond dissociation can expose single-reference limitations.

HFの解は一般に一意とは限りません。SCFが停止しても基底収束・軌道安定性・正しい電子状態の確認が必要です。分子解離では単一参照の限界が現れます。


## 条件と確認範囲 (ja)

problem: 交換を含む単一行列式近似のHe閉殻基底状態を求める。 別実装のH₂分子RHFも学ぶ。

variant: 同一1s空間軌道を2電子が占有する動径HF。占有軌道上での交換簡約によりv_eff=−2/r+v_H/2。 H₂側の分子積分・行列SCFは別配布版。

use_when:
- He 1s²で直接項・交換項・二重計数補正の関係を学ぶ。
- 同じ非相対論RHFモデルの格子解と独立Gaussian基底参照を比較する。

avoid_when:
- 多軌道、開殻、分子、周期系へ局所交換−v_H/2を流用する。
- 相関エネルギーや多参照性をこのHF値で説明する。

assumptions [specified]:
- 従来の原子例：Z=2の孤立He、無限質量の点核、非相対論。逆スピンの2電子が同じ球対称1s空間軌道を占有する。
- 従来の原子例：∫|u|²dr=1とし、p=2|u|²=4πr²n、∫p dr=2と定義する。
- 従来の原子例：この占有軌道に限り有効場は−2/r+v_H/2、交換エネルギーはE_x=−E_H/2に簡約される。一般の非局所Fock演算子は実装していない。
- 従来の原子例：単一行列式の交換を含み、電子相関を含まない。
- 別の分子例：H₂の有限s型Gaussian基底RHF。自作の1・2電子積分と行列SCFを用い、公差・収束はH₂入力と検証結果で確認する。
helium('hf')の占有・p=2u²・交換簡約を確認。

units [specified]:
原子単位系（ℏ=mₑ=e=4πε₀=1）。rはbohr、エネルギー・有効ポテンシャルはhartree、規格化した縮約軌道uはbohr⁻¹ᐟ²。正の電子数密度n(r)はbohr⁻³、動径電子数密度p(r)=4πr²n(r)はbohr⁻¹、∫p dr=N。pは符号付き電荷密度ではありません。 分子側：3次元AOはbohr^(−3/2)で規格化。重なり行列・AO密度行列・電子数は無次元、直交化したFock交換子はhartree。分子側の公差は別に記載。
u、p、nとエネルギー成分の規約を確認。

boundary_conditions [specified]:
He縮約軌道にu(0)=u(r_max)=0（基本r_max=16 bohr、別途4/8/12/16 bohrの領域検査）。Hartree場は原点で有限、密度の外ではN/rへ接続し、r_maxで0には固定しません。 別のH₂側は孤立分子の全空間Gaussian解析積分で、有限の動径箱は設けない。
軌道Dirichlet条件と孤立系Hartree境界を区別。

limitations [specified]:
この局所交換の簡約を多軌道・開殻・分子・周期系へそのまま拡張できない。原子版ではUHF/ROHF・分子積分・軌道安定性解析を扱わない。保存PySCF RHF参照は独立な有限Gaussian基底計算であり、相関を含むHeの厳密エネルギーではない。格子・箱幅・SCF収束と物理モデル誤差を区別する。 H₂では別の分子積分実装を用いる。分子DFT・一般多中心分子・開殻・軌道安定性解析は未実装。
一般Fock解法・相関・安定性解析を検証したと読めない範囲を明示。

Review: 従来の原子コード点検の記録：既存公開版の実装・検査・保存結果を読んだ点検であり、この点検では再実行していません。helium('hf')、エネルギー会計恒等式・格子依存・初期値比較の検査、保存PySCF RHF比較と参照生成コードを確認。 H₂の新しい実行・独立参照・収束記録は別配布版を参照。

Not checked:
- 従来の点検時：新規再実行、一般の交換積分・開殻HF・分子の検証は行っていない。
- 従来の点検時：初期値の比較は全停留解の列挙や軌道安定性の証明ではない。

Evidence:
- helium(model='hf'); E_H/2 and E_x=-E_H/2 reduction: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_helium_scf_and_independent_reference; test_alternative_start_and_explicit_nonconvergence: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- calculate: independent PySCF RHF Gaussian-basis reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference_pyscf.py
- Saved RHF energies, basis convergence and environment: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- helium.refinement; helium.independent_comparison; energy-accounting and convergence checks: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [original-method / primary-research] Fock, V. (1930). Näherungsmethode zur Lösung des quantenmechanischen Mehrkörperproblems. — https://doi.org/10.1007/BF01340294
  行列式の対称性と交換項を含む平均場の原論文。He用局所簡約の今回の根拠は公開コードの点検と区別する。
  abstract-and-metadata (2026-11-22); Publisher Zusammenfassung and bibliographic record; subscription full text not read; https://link.springer.com/article/10.1007/BF01340294
- [context / primary-research] Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. — https://doi.org/10.1103/RevModPhys.23.69
  分子の基底展開によるHFとの関係を示す。公開する動径Heコードの実装方式ではない。
  metadata (2026-11-22); Publisher bibliographic record; abstract/full paper not available in retrieved view; https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.23.69
- [reference-solution / primary-research] Sun, Q. et al. (2020). Recent developments in the PySCF program package. — https://doi.org/10.1063/5.0006074
  独立参照ソフトウェアの論文。特定のHe参照値・実行版は保存JSONと参照スクリプトに記録。
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract/bibliography and author preprint abstract https://arxiv.org/abs/2002.12531; full paper not read; https://pubs.aip.org/aip/jcp/article-abstract/153/2/024109/1061482/Recent-developments-in-the-PySCF-program-package?redirectedFrom=fulltext

## Conditions and review scope (en)

problem: Find the closed-shell helium ground state in a single-determinant approximation with exchange. A separate H₂ molecular RHF example extends the scope.

variant: Radial HF for two electrons occupying one common 1s spatial orbital; exchange acting on that orbital reduces v_eff to -2/r+v_H/2. Molecular integrals/matrix SCF for H₂ are in a separate edition.

use_when:
- Study Coulomb, exchange and double-counting terms in helium 1s².
- Compare the grid solution with an independent Gaussian-basis reference for the same nonrelativistic RHF model.

avoid_when:
- Reusing local exchange -v_H/2 for multi-orbital, open-shell, molecular or periodic systems.
- Using this HF value to describe correlation energy or multireference physics.

assumptions [specified]:
- Atomic branch: Nonrelativistic isolated He with Z=2, an infinite-mass point nucleus and two opposite-spin electrons occupying the same spherical 1s spatial orbital.
- Atomic branch: Normalize integral |u|^2 dr=1 and define p=2|u|^2=4 pi r^2 n, so integral p dr=2.
- Atomic branch: For this occupied orbital only, the Fock equation reduces to the effective field -2/r+v_H/2 and E_x=-E_H/2; no general nonlocal Fock operator is implemented.
- Atomic branch: Single-determinant exchange is included; electron correlation is omitted.
- Separate molecular branch: H2 RHF in finite s-Gaussian spaces, analytic one-/two-electron integrals and matrix SCF; see the H2 input and measured checks for its own tolerances.
Checked occupations, p=2u^2 and the exchange reduction in helium('hf').

units [specified]:
Atomic units (hbar=m_e=e=4 pi epsilon_0=1): r in bohr, energies/effective potentials in hartree, and normalized reduced orbitals u in bohr^(-1/2). Positive electron-number density n(r) is in bohr^(-3); radial number density p(r)=4 pi r^2 n(r) is in bohr^(-1), with integral p dr=N. p is not signed charge density. Molecular branch: normalized 3D AO functions in bohr^(-3/2); overlap, AO density matrix and electron count dimensionless; transformed Fock commutator in hartree. Molecular tolerances are stated separately.
Checked conventions for u, p, n and energy components.

boundary_conditions [specified]:
Helium reduced orbital: u(0)=u(r_max)=0, baseline r_max=16 bohr with a separate 4/8/12/16-bohr domain study. The Hartree field is finite at the origin and joins N/r outside the density; it is not fixed to zero at r_max. Separate H2 branch: isolated molecule, analytic whole-space Gaussian integrals; no finite radial box.
Distinguished orbital Dirichlet conditions from isolated Hartree boundaries.

limitations [specified]:
The local exchange reduction cannot be transferred unchanged to multi-orbital, open-shell, molecular or periodic systems. The atomic edition does not implement UHF/ROHF, molecular integrals or orbital-stability analysis. Saved PySCF RHF references are independent finite-Gaussian-basis calculations, not exact correlated helium energies. Separate grid, domain and SCF convergence from physical model error. H₂ uses a separate molecular-integral implementation. Molecular DFT, general multicenter molecules, open shells and orbital-stability analysis remain unimplemented.
Explicitly excludes claims of a general Fock solver, correlation or stability analysis.

Review: Historical atomic-code inspection: This inspection reads the released implementation, tests and saved results; it does not rerun the calculation. Inspected helium('hf'), tests for energy accounting, grid refinement and alternative starts, saved PySCF RHF comparisons and the independent reference generator. New H₂ execution, independent-reference and convergence receipts are supplied separately.

Not checked:
- At the earlier inspection: No new run or validation of general exchange integrals, open-shell HF or molecules.
- At the earlier inspection: Alternative starts do not enumerate all stationary solutions or prove orbital stability.

Evidence:
- helium(model='hf'); E_H/2 and E_x=-E_H/2 reduction: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_helium_scf_and_independent_reference; test_alternative_start_and_explicit_nonconvergence: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- calculate: independent PySCF RHF Gaussian-basis reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference_pyscf.py
- Saved RHF energies, basis convergence and environment: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json
- helium.refinement; helium.independent_comparison; energy-accounting and convergence checks: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [original-method / primary-research] Fock, V. (1930). Näherungsmethode zur Lösung des quantenmechanischen Mehrkörperproblems. — https://doi.org/10.1007/BF01340294
  Original exchange-containing mean-field formulation; the released helium-specific reduction is established separately by code inspection.
  abstract-and-metadata (2026-11-22); Publisher Zusammenfassung and bibliographic record; subscription full text not read; https://link.springer.com/article/10.1007/BF01340294
- [context / primary-research] Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. — https://doi.org/10.1103/RevModPhys.23.69
  Context for basis-expanded molecular HF, not the implementation used by the released radial helium code.
  metadata (2026-11-22); Publisher bibliographic record; abstract/full paper not available in retrieved view; https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.23.69
- [reference-solution / primary-research] Sun, Q. et al. (2020). Recent developments in the PySCF program package. — https://doi.org/10.1063/5.0006074
  Identifies the independent reference software; specific helium values and versions come from the saved JSON and reference script, not this paper.
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract/bibliography and author preprint abstract https://arxiv.org/abs/2002.12531; full paper not read; https://pubs.aip.org/aip/jcp/article-abstract/153/2/024109/1061482/Recent-developments-in-the-PySCF-program-package?redirectedFrom=fulltext


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#hartree-fock
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#hartree-fock



- Reference: https://doi.org/10.1007/BF01340294 — Original exchange-containing mean-field formulation; the released helium-specific reduction is established separately by code inspection.
- Reference: https://doi.org/10.1103/RevModPhys.23.69 — Context for basis-expanded molecular HF, not the implementation used by the released radial helium code.
- Reference: https://doi.org/10.1063/5.0006074 — Identifies the independent reference software; specific helium values and versions come from the saved JSON and reference script, not this paper.

Scoped example: Only spherical helium with one doubly occupied 1s spatial orbital; the local HF exchange reduction is specific to this two-electron problem. A separate edition adds H₂ RHF in finite s-Gaussian bases.

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

Molecular scope: New H₂ closed-shell RHF example: original s-Gaussian integrals, independent PySCF comparisons, SCF residuals and basis refinement. Limited to finite s-type subspaces; does not validate general molecules, molecular DFT, periodic systems or correct dissociation.

{
  "release": {
    "family": "molecular-hf",
    "version": "2026-11-22",
    "download": "https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip",
    "sha256": "293988ec209a867491cf8356f12ce5cb8484a51d5c1d444acd5f217062b5ba79",
    "manifest": "https://hrkoyama.github.io/code/molecular-hf/2026-11-22/source-manifest.json",
    "manifest_sha256": "ca34057ae326169d84f70974b8f324555482fdd4afe57a69b56efef5c3008df2",
    "verification": "https://hrkoyama.github.io/code/molecular-hf/2026-11-22/verification.json",
    "archive_directory": "molecular-hf-2026-11-22"
  },
  "code_base": "https://hrkoyama.github.io/code/molecular-hf/2026-11-22/",
  "examples": [
    "h2-rhf"
  ],
  "run_commands": [
    "python run.py --input inputs.json --output output"
  ],
  "scope": {
    "ja": "新しいH₂の閉殻RHF例：自作s型Gaussian積分、独立PySCF比較、SCF残差・基底拡大を確認。有限のs型部分空間に限定し、一般分子・分子DFT・周期系・正しい解離極限は検証しません。",
    "en": "New H₂ closed-shell RHF example: original s-Gaussian integrals, independent PySCF comparisons, SCF residuals and basis refinement. Limited to finite s-type subspaces; does not validate general molecules, molecular DFT, periodic systems or correct dissociation."
  }
}

Common execution records: [{"id": "helium-ground-state", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#helium-ground-state-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#helium-ground-state-en"}}, {"id": "h2-rhf", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#h2-rhf-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#h2-rhf-en"}}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`; helium-ground-state, h2-rhf)
- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`; helium-ground-state)
- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`; h2-rhf)

#### 問題の図 (`method-problems-ja`)

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja) (`helium-ground-state`) · [コードZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

![固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

- [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja) (`h2-rhf`) · [コードZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。


#### 厳密解・参照解 (`method-references-ja`)

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) (`helium-ground-state`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#references-ja) (`h2-rhf`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#hartree-fock)
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

##### H₂分子RHF：独立参照・SCF・s型基底拡大 (`h2-rhf`)

[H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/inputs.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### 関連ソース

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)
- [/code/molecular-hf/2026-11-22/molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular_hf.py)
- [/code/molecular-hf/2026-11-22/run.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/run.py)

###### 配布版のテスト

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`; helium-ground-state, h2-rhf)
- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`; helium-ground-state)
- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`; h2-rhf)

#### Problem figures (`method-problems-en`)

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en) (`helium-ground-state`) · [Code ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

![Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

- [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en) (`h2-rhf`) · [Code ZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.


#### Exact / reference solutions (`method-references-en`)

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) (`helium-ground-state`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en) (`h2-rhf`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#hartree-fock)
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

##### H₂ molecular RHF: independent reference, SCF and s-basis refinement (`h2-rhf`)

[H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/inputs.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

[Related code edition / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### Related source

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)
- [/code/molecular-hf/2026-11-22/molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular_hf.py)
- [/code/molecular-hf/2026-11-22/run.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/run.py)

###### Package tests

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```
