# Self-consistent field iteration / SCF / 自己無撞着場反復（SCF）

Status: educational-example

Find a fixed point consistent with its effective field. Isolated He uses linear density mixing, H₂ an original RHF iteration, and periodic He PySCF SCF; each example checks residuals, iteration histories and termination.

密度と有効場が整合する固定点を求める。孤立Heでは線形密度混合、H₂では独自RHF反復、周期HeではPySCFのSCFを使い、各例で残差・反復履歴・終了理由を確認する。

Atomic/molecular example scope: Energy change alone is insufficient. Electron number staying at two is an imposed consistency check, not independent physical validation. Agreement from alternative starts does not prove uniqueness, orbital stability or a global energy minimum. The Pulay reference is context for an unimplemented acceleration method, not the source of the simple density-mixing implementation. H₂ uses a separate molecular-integral implementation. Molecular DFT, general multicenter molecules, open shells and orbital-stability analysis remain unimplemented. A separate PySCF periodic-He driver additionally uses VWN5 correlation and periodic k-point quadrature.

Other names: 自己無撞着場, self consistency, density mixing

Comparison notes: A small energy change alone is insufficient. Convergence also does not establish the lowest-energy stable electronic solution.

小さいエネルギー変化だけで収束を宣言しません。収束した解が最低エネルギーの安定な電子状態である保証も別に検査します。


## 条件と確認範囲 (ja)

problem: 指定した電子密度依存ハミルトニアンと密度の自己整合固定点を求め、未収束を識別する。 別実装のH₂分子RHFも学ぶ。

variant: 単純線形密度混合。密度L1差・エネルギー変化・出力密度で再構成した軌道残差のAND条件、履歴保存、反復上限による明示的未収束。 H₂側の分子積分・行列SCFは別配布版。

use_when:
- 小さなHeモデルで混合率・初期値・停止基準を比較する。
- 正常終了と数値収束を区別し、反復上限1回の意図的な未収束を扱う。

avoid_when:
- 金属・難収束系や汎用分子SCFで、この混合率と公差が常に適切とみなす。
- 反復が停止した事実だけで安定性・最低エネルギー・物理精度を保証する。

assumptions [specified]:
- 原子・分子の実行例：従来の原子例：固定点写像は公開する球対称He 1s²のHFまたは交換のみLDA動径モデルであり、汎用の分子・周期系SCF実装ではない。
- 原子・分子の実行例：従来の原子例：入力・出力の動径電子数密度をp_next=(1−α)p_in+αp_out（0<α≤1）で混合。公開基本値α=0.35、別の初期値では0.7も用いる。
- 原子・分子の実行例：従来の原子例：各固有値問題でuを規格化しp_out=2|u|²とするため、電子数の規格化は反復内で課している。
- 原子・分子の実行例：従来の原子例：密度の入出力L1差<10⁻⁹電子数、|エネルギー変化|<10⁻¹⁰hartree、出力密度で再構成した軌道残差<10⁻⁷hartreeをすべて要求。最大300反復。
- 原子・分子の実行例：従来の原子例：アトラス側の反復にDIIS・Anderson・Newton加速は未採用。独立PySCF参照は独自のソルバーを使いうる。
- 原子・分子の実行例：別の分子例：H₂の有限s型Gaussian基底RHF。自作の1・2電子積分と行列SCFを用い、公差・収束はH₂入力と検証結果で確認する。
- 固定した1原子単純立方Heセルの周期KS-DFT。PySCFを使う教育用ワークフローで、Γ点／k点、Gaussian軌道基底、FFT補助格子、SCF公差を別々に検査し、同じGTHパラメータ・LDA交換＋VWN5相関のDFTK平面波計算と比較。平衡He結晶や一般物質・金属の検証ではありません。
heliumの密度更新式、停止の3条件と反復上限を確認。

units [specified]:
原子・分子の実行例：混合率αと反復回数は無次元。pはbohr⁻¹、∫|p_out−p_in|drは電子数、エネルギー変化と規格化した軌道残差はhartree。公開公差はこの規格化とモデルに対する値。 分子側：3次元AOはbohr^(−3/2)で規格化。重なり行列・AO密度行列・電子数は無次元、直交化したFock交換子はhartree。分子側の公差は別に記載。 周期He：bohr・逆bohr・中性基本セル当たりhartree、逆格子での分率k座標。
混合率の無次元性と残差ごとの単位・規格化を明記。

boundary_conditions [not-applicable]:
原子・分子の実行例：SCF混合そのものに空間境界条件はない。与えたHe固定点写像が縮約軌道u(0)=u(r_max)=0と、原点で有限・遠方N/rの孤立Hartree場を規定する。HF・KS・Hartree項目を参照。 別のH₂側は孤立分子の全空間Gaussian解析積分で、有限の動径箱は設けない。 周期He：固定1原子単純立方セルの3次元Bloch境界。
混合アルゴリズム自体には境界がなく、Heの固定点写像が空間境界を与える。

limitations [specified]:
原子・分子の実行例の範囲：エネルギー変化だけで収束を宣言しない。電子数が2に保たれることは実装の整合性検査であり、独立な物理検証ではない。異なる初期値での一致も解の一意性・軌道安定性・大域的最低エネルギーを証明しない。Pulay文献は未採用の加速法の文脈用で、単純密度混合の実装出典ではない。 H₂では別の分子積分実装を用いる。分子DFT・一般多中心分子・開殻・軌道安定性解析は未実装。 周期He側では別のPySCFドライバーがVWN5相関と周期k点積分を扱う。
DIIS未実装、正規化と独立検証の差、収束と安定性の差を明記。

Review: 従来の原子コード点検の記録：既存公開版の実装・検査・保存結果を読んだ点検であり、この点検では再実行していません。heliumの入力密度混合・3条件の収束判定、初期値比較とmax_iterationsの検査、保存反復履歴・意図的未収束を確認。 H₂の新しい実行・独立参照・収束記録は別配布版を参照。 周期Heの新しいライブラリ実行検証は別記録に掲載。

Not checked:
- 従来の点検時：新規再実行、DIIS・Anderson・Newton法や周期金属系の収束挙動は検証していない。
- 従来の点検時：固定点の全解・軌道安定性を網羅する解析はない。

Evidence:
- helium: linear input-density mixing; joint stopping conditions; reason/max_iterations: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_alternative_start_and_explicit_nonconvergence; test_helium_scf_and_independent_reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- helium mixing, alternative start, three tolerances and iteration limit: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json
- helium.scf_histories; helium.alternative_starts; helium.expected_nonconvergence: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [formulation / primary-research] Kohn, W. and Sham, L. J. (1965). Self-Consistent Equations Including Exchange and Correlation Effects. — https://doi.org/10.1103/PhysRev.140.A1133
  密度依存有効場の自己無撞着方程式の文脈。公開混合率・停止公差の出典ではない。
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133
- [context / primary-research] Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. — https://doi.org/10.1103/RevModPhys.23.69
  分子軌道SCFの書誌的な入口。公開する動径He反復そのものではない。
  metadata (2026-11-22); Publisher bibliographic record; abstract/full paper not available in retrieved view; https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.23.69
- [context / primary-research] Pulay, P. (1980). Convergence acceleration of iterative sequences. The case of SCF iteration. — https://doi.org/10.1016/0009-2614(80)80396-4
  DIIS系の収束加速との比較用。公開Heソルバーでは採用していない。
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; subsequent direct open returned HTTP 403; full paper not read; https://www.sciencedirect.com/science/article/pii/0009261480803964

## Conditions and review scope (en)

problem: Find a self-consistent fixed point of a specified density-dependent Hamiltonian and identify failure. A separate H₂ molecular RHF example extends the scope.

variant: Simple linear density mixing; joint density-L1, energy-change and output-density-rebuilt orbital-residual criteria, saved histories and explicit iteration-limit failure. Molecular integrals/matrix SCF for H₂ are in a separate edition.

use_when:
- Compare mixing rates, starts and stopping criteria in a small helium model.
- Distinguish process completion from convergence, including an intentional one-iteration failure.

avoid_when:
- Assuming the same mixing and tolerances are generally suitable for metals, difficult systems or molecular SCF.
- Using iteration termination alone to establish stability, minimum energy or physical accuracy.

assumptions [specified]:
- Atomic/molecular examples: Earlier helium branch: The fixed-point map is the released spherical He 1s² HF or exchange-only LDA radial model, not a general molecular or periodic SCF implementation.
- Atomic/molecular examples: Earlier helium branch: Mix input and output radial number densities: p_next=(1-alpha)p_in+alpha p_out, 0<alpha<=1; released baseline alpha=0.35 and an alternative start uses 0.7.
- Atomic/molecular examples: Earlier helium branch: Each eigenproblem normalizes u and sets p_out=2|u|^2, so the electron-number normalization is imposed within the iteration.
- Atomic/molecular examples: Earlier helium branch: Convergence requires input/output density L1<1e-9 electrons, |energy change|<1e-10 hartree, and the output-density-rebuilt orbital residual<1e-7 hartree; maximum 300 iterations.
- Atomic/molecular examples: Earlier helium branch: The atlas iteration implements no DIIS, Anderson or Newton acceleration. An independent PySCF reference may use its own solver algorithms.
- Atomic/molecular examples: Separate molecular branch: H2 RHF in finite s-Gaussian spaces, analytic one-/two-electron integrals and matrix SCF; see the H2 input and measured checks for its own tolerances.
- Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals.
Inspected helium's density update, three stopping criteria and iteration cap.

units [specified]:
Atomic/molecular examples: Mixing alpha and iteration number are dimensionless. Radial p is in bohr^(-1), integral |p_out-p_in| dr is electron number, and energy changes/normalized orbital residuals are in hartree. Published tolerances belong to this normalization and model. Molecular branch: normalized 3D AO functions in bohr^(-3/2); overlap, AO density matrix and electron count dimensionless; transformed Fock commutator in hartree. Molecular tolerances are stated separately. Periodic He: bohr, inverse bohr and hartree per neutral primitive cell; reciprocal-lattice fractional k coordinates.
Specified dimensionless mixing and normalization/units of each residual.

boundary_conditions [not-applicable]:
Atomic/molecular examples: SCF mixing itself imposes no spatial boundary condition. The supplied helium fixed-point map uses reduced-orbital u(0)=u(r_max)=0 and an isolated finite-origin, N/r Hartree field; see the HF/KS/Hartree records. Separate H2 branch: isolated molecule, analytic whole-space Gaussian integrals; no finite radial box. Periodic He: three-dimensional Bloch boundaries in the fixed one-atom simple-cubic cell.
Mixing has no intrinsic spatial boundary; the helium fixed-point map supplies it.

limitations [specified]:
Atomic/molecular example scope: Energy change alone is insufficient. Electron number staying at two is an imposed consistency check, not independent physical validation. Agreement from alternative starts does not prove uniqueness, orbital stability or a global energy minimum. The Pulay reference is context for an unimplemented acceleration method, not the source of the simple density-mixing implementation. H₂ uses a separate molecular-integral implementation. Molecular DFT, general multicenter molecules, open shells and orbital-stability analysis remain unimplemented. A separate PySCF periodic-He driver additionally uses VWN5 correlation and periodic k-point quadrature.
Distinguished absent DIIS, imposed normalization versus independent checks, and convergence versus stability.

Review: Historical atomic-code inspection: This inspection reads the released implementation, tests and saved results; it does not rerun the calculation. Inspected helium's input-density mixing and joint stopping test, alternative-start/max_iterations tests, saved histories and intentional nonconvergence. New H₂ execution, independent-reference and convergence receipts are supplied separately. New library-backed periodic-He validation is recorded separately.

Not checked:
- At the earlier inspection: No new run or verification of DIIS/Anderson/Newton methods or periodic-metal convergence.
- At the earlier inspection: No exhaustive stationary-solution or orbital-stability analysis.

Evidence:
- helium: linear input-density mixing; joint stopping conditions; reason/max_iterations: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_alternative_start_and_explicit_nonconvergence; test_helium_scf_and_independent_reference: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- helium mixing, alternative start, three tolerances and iteration limit: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json
- helium.scf_histories; helium.alternative_starts; helium.expected_nonconvergence: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [formulation / primary-research] Kohn, W. and Sham, L. J. (1965). Self-Consistent Equations Including Exchange and Correlation Effects. — https://doi.org/10.1103/PhysRev.140.A1133
  Self-consistent density-dependent equations; not the source of the released mixing parameter or stopping tolerances.
  abstract-and-metadata (2026-11-22); Publisher Abstract and bibliographic record; full paper not read; https://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133
- [context / primary-research] Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. — https://doi.org/10.1103/RevModPhys.23.69
  Bibliographic entry point for molecular-orbital SCF, not the released radial helium iteration.
  metadata (2026-11-22); Publisher bibliographic record; abstract/full paper not available in retrieved view; https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.23.69
- [context / primary-research] Pulay, P. (1980). Convergence acceleration of iterative sequences. The case of SCF iteration. — https://doi.org/10.1016/0009-2614(80)80396-4
  Context for DIIS-type convergence acceleration; not adopted by the released helium solver.
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; subsequent direct open returned HTTP 403; full paper not read; https://www.sciencedirect.com/science/article/pii/0009261480803964


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#scf
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#scf



- Reference: https://doi.org/10.1103/PhysRev.140.A1133 — Self-consistent density-dependent equations; not the source of the released mixing parameter or stopping tolerances.
- Reference: https://doi.org/10.1103/RevModPhys.23.69 — Bibliographic entry point for molecular-orbital SCF, not the released radial helium iteration.
- Reference: https://doi.org/10.1016/0009-2614(80)80396-4 — Context for DIIS-type convergence acceleration; not adopted by the released helium solver.

Scoped example: Helium linear density mixing with density/energy/orbital-residual checks, alternative starts/mixing and explicit failure; no DIIS. A separate edition adds H₂ RHF in finite s-Gaussian bases.

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

Common execution records: [{"id": "helium-ground-state", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#helium-ground-state-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#helium-ground-state-en"}}, {"id": "h2-rhf", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#h2-rhf-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#h2-rhf-en"}}, {"id": "periodic-he-dft", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-dft-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-dft-en"}}, {"id": "periodic-he-forces", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-forces-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-forces-en"}}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`; helium-ground-state, h2-rhf)
- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`; helium-ground-state, periodic-he-dft, periodic-he-forces)
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

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#references-ja) (`h2-rhf`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja) (`periodic-he-dft`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja) (`periodic-he-forces`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#scf)
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
- [/code/molecular-hf/2026-11-22/molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular_hf.py)
- [/code/molecular-hf/2026-11-22/run.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/run.py)
- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)

###### 配布版のテスト

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)
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

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`; helium-ground-state, h2-rhf)
- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`; helium-ground-state, periodic-he-dft, periodic-he-forces)
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

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en) (`h2-rhf`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en) (`periodic-he-dft`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en) (`periodic-he-forces`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#scf)
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
- [/code/molecular-hf/2026-11-22/molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular_hf.py)
- [/code/molecular-hf/2026-11-22/run.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/run.py)
- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)

###### Package tests

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)
- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```
