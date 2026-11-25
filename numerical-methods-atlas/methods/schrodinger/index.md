# Schrodinger eigenproblems / Schrödinger固有値問題

Status: educational-example

Study fixed-nucleus quantum eigenproblems. The released example solves isolated hydrogenic radial equations by second-order differences and compares eigenvalues and orbitals with analytic solutions.

固定核の量子固有値問題を扱う。公開例は孤立水素型原子の動径方程式を2次差分で解き、解析的固有値・軌道と比較する。

Not a general many-electron, time-dependent, molecular, periodic or relativistic solver; nuclear motion and spin–orbit effects are absent. Small discrete eigenpair residuals do not remove grid/domain error, and finite-difference eigenvalues are not guaranteed variational upper bounds to continuum energies.

Other names: シュレーディンガー, Schrödinger equation, electronic Hamiltonian

Comparison notes: Nuclear dynamics, relativity, spin–orbit coupling and external fields are outside this representative Hamiltonian. A small eigenpair residual does not establish domain or basis convergence.

核運動、相対論、スピン軌道相互作用、外場はこの代表式に含めません。固有値の残差が小さくても、領域・基底の誤差は残ります。


## 条件と確認範囲 (ja)

problem: 孤立した1電子Coulomb系の束縛エネルギーと規格化軌道を求める。

variant: 角運動量を分離した縮約動径方程式。2次中心差分を三重対角固有値解法で解き、E_n=−Z²/(2n²)と解析軌道を参照する。

use_when:
- 解析解を持つ束縛状態で格子誤差・領域誤差・固有値残差を分けて学ぶ。
- 公開入力に含まれるZ・(n,l)で規格化、直交性、Zによるエネルギーのスケーリングを調べる。

avoid_when:
- 電子間相互作用を含む多体波動関数や分子のエネルギーが必要。
- 散乱・連続状態、時間発展、強い相対論効果を扱う。

assumptions [specified]:
- 孤立・無限質量の点核によるCoulomb場−Z/r中の1電子。非相対論・外場なし。
- 角運動量lを分離し、∫|u|²dr=1で規格化した縮約動径軌道u(r)を解く。
- 公開入力はZ=1,2および(n,l)=(1,0),(2,0),(2,1),(3,2)。任意の多電子状態を検証したものではない。
- 一様な内部動径格子と、2次の運動エネルギー差分による実対称三重対角行列を用いる。
hydrogenic・eigenstateと公開Z・状態一覧を確認。

units [specified]:
原子単位系（ℏ=mₑ=e=4πε₀=1）。rはbohr、エネルギー・有効ポテンシャルはhartree、規格化した縮約軌道uはbohr⁻¹ᐟ²。
運動エネルギー−½∂²と−Z/rの原子単位系、uの規格化を確認。

boundary_conditions [specified]:
u(0)=u(r_max)=0。公開する水素型の格子検査はr_max=60 bohr。Z=1の1sは別途r_max=4,8,16,32 bohrを比較。原点の正則性と無限遠の減衰を有限箱のDirichlet条件で近似する。
端点を除く格子と両端のu=0、独立した箱幅検査を確認。

limitations [specified]:
一般の多電子Schrödinger方程式の直接解法、時間発展、分子、周期系、相対論・核運動・スピン軌道相互作用は未実装。小さい離散固有値残差だけでは格子・領域誤差は除けず、有限差分の固有値は連続問題の変分上界とは限らない。
1電子動径法と一般の多体方程式を区別。

Review: 既存公開版の実装・検査・保存結果を読んだ点検であり、この点検では再実行していません。hydrogenic・eigenstate、解析解・格子次数・規格化・領域・独立な密行列との比較を行う検査、および保存済みhydrogenic結果を確認。

Not checked:
- 新しい計算や調和振動子の実装は行っていない。
- 原論文本文の全式、および未公開の量子数・高Zへの適用精度は点検していない。

Evidence:
- hydrogenic, eigenstate, kinetic, radial_grid: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_hydrogenic_refinement_and_normalization; test_coulomb_charge_scaling_and_orthogonality; test_finite_domain_is_separate_from_grid_error; test_tridiagonal_solver_against_independent_dense_diagonalization: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- hydrogenic charges/states, grid and domain studies: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json
- hydrogenic.refinement; hydrogenic.domain_refinement; checks.hydrogenic_*: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [original-method / primary-research] Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. — https://doi.org/10.1002/andp.19263840404
  量子固有値問題の原論文。今回の確認は出版社の書誌情報までで、差分実装の出典ではない。
  metadata (2026-11-22); Publisher bibliographic record; full paper not read; https://onlinelibrary.wiley.com/doi/10.1002/andp.19263840404
- [context / primary-research] Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. — https://doi.org/10.1103/RevModPhys.23.69
  分子軌道の基底展開との比較用。公開する1電子動径差分法として採用した文献ではない。
  metadata (2026-11-22); Publisher bibliographic record; abstract/full paper not available in retrieved view; https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.23.69

## Conditions and review scope (en)

problem: Find bound-state energies and normalized orbitals of an isolated one-electron Coulomb system.

variant: Angular-momentum-separated reduced radial equation, second-order central differences and a tridiagonal eigensolver, referenced to E_n=-Z^2/(2n^2) and analytic orbitals.

use_when:
- Separate grid error, domain error and eigenpair residuals on analytically solvable bound states.
- Inspect normalization, orthogonality and charge scaling for the released Z and (n,l) cases.

avoid_when:
- A many-electron interacting wavefunction or molecular energy is required.
- Scattering/continuum states, time evolution or strong relativistic effects are required.

assumptions [specified]:
- One electron in the Coulomb potential -Z/r of an isolated, infinite-mass point nucleus; nonrelativistic and field-free.
- Separate angular momentum l and solve for the reduced radial orbital u(r), normalized by integral |u|^2 dr=1.
- Released inputs use Z=1,2 and (n,l)=(1,0),(2,0),(2,1),(3,2); these cases do not cover arbitrary many-electron states.
- A uniform interior radial grid and a real symmetric tridiagonal second-order kinetic operator are used.
Inspected hydrogenic/eigenstate and the released charges/state list.

units [specified]:
Atomic units (hbar=m_e=e=4 pi epsilon_0=1): r in bohr, energies/effective potentials in hartree, and normalized reduced orbitals u in bohr^(-1/2).
Checked atomic-unit kinetic/Coulomb terms and u normalization.

boundary_conditions [specified]:
u(0)=u(r_max)=0. Released hydrogenic refinement inputs use r_max=60 bohr; a separate Z=1 1s study uses r_max=4,8,16,32 bohr. Origin and infinity are approximated by regularity and finite-box Dirichlet conditions.
Checked interior grid, endpoint u=0 and separate domain study.

limitations [specified]:
Not a general many-electron, time-dependent, molecular, periodic or relativistic solver; nuclear motion and spin–orbit effects are absent. Small discrete eigenpair residuals do not remove grid/domain error, and finite-difference eigenvalues are not guaranteed variational upper bounds to continuum energies.
Distinguished the radial one-electron solver from general many-body equations.

Review: This inspection reads the released implementation, tests and saved results; it does not rerun the calculation. Inspected hydrogenic/eigenstate, tests for analytic solutions, refinement, normalization, domain effects and independent dense diagonalization, and saved hydrogenic results.

Not checked:
- No new run or harmonic-oscillator implementation.
- No full-equation audit of the original paper or accuracy check for unreleased quantum numbers/high Z.

Evidence:
- hydrogenic, eigenstate, kinetic, radial_grid: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py
- test_hydrogenic_refinement_and_normalization; test_coulomb_charge_scaling_and_orthogonality; test_finite_domain_is_separate_from_grid_error; test_tridiagonal_solver_against_independent_dense_diagonalization: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py
- hydrogenic charges/states, grid and domain studies: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json
- hydrogenic.refinement; hydrogenic.domain_refinement; checks.hydrogenic_*: https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json

References:
- [original-method / primary-research] Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. — https://doi.org/10.1002/andp.19263840404
  Original eigenproblem paper; publisher metadata checked, not the source of the released finite-difference discretization.
  metadata (2026-11-22); Publisher bibliographic record; full paper not read; https://onlinelibrary.wiley.com/doi/10.1002/andp.19263840404
- [context / primary-research] Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. — https://doi.org/10.1103/RevModPhys.23.69
  Context for molecular orbital basis expansions; not the adopted one-electron radial finite-difference method.
  metadata (2026-11-22); Publisher bibliographic record; abstract/full paper not available in retrieved view; https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.23.69


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#schrodinger
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#schrodinger



- Reference: https://doi.org/10.1002/andp.19263840404 — Original eigenproblem paper; publisher metadata checked, not the source of the released finite-difference discretization.
- Reference: https://doi.org/10.1103/RevModPhys.23.69 — Context for molecular orbital basis expansions; not the adopted one-electron radial finite-difference method.

Scoped example: Uniform radial-grid tests of isolated hydrogenic 1s, 2s, 2p and 3d states; not a direct general many-electron Schrödinger solver.

[
  {
    "id": "hydrogenic-atoms",
    "section": "hydrogenic",
    "name": {
      "ja": "水素型原子の動径固有値問題",
      "en": "Hydrogenic radial eigenproblems"
    },
    "result_pointer": "/hydrogenic/refinement",
    "figure": "hydrogenic.png",
    "reading": {
      "ja": "https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/#hydrogenic",
      "en": "https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#hydrogenic"
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

## Small fixed-input validation supplements

Restricted fixed examples: Hydrogenic formulas and immutable finite-basis helium reference cards, Small 1D box and quantum harmonic-oscillator eigenpairs, A three-wave periodic projector and Fermi-occupation model. Saved-reference audits are not new electronic calculations. No new SCF, external-reference regeneration, complete-basis or correlated-exact helium claim. No separate certified finite-wall/mesh decomposition for HO; raw nodal count is a diagnostic. HO0.003 is the fixed-input study target, not a proved finite-h bound. The authored rank-one kernel is not an element-fitted norm-conserving pseudopotential. No self-consistent Hartree/XC, real metal, general material or long-time MD success.

固定した小規模例に限定：H/Heの式・密度・固定参照カード、1次元箱型井戸・量子調和振動子、3平面波の非局所projectorと有限温度占有。保存参照監査は新しい電子計算ではありません。 有限基底HFや交換のみLDAを相関込みの厳密Heとは呼びません。独立参照の再生成は0回です。 HOの壁誤差と格子誤差の個別保証はありません。節の近零点・tailは診断、0.003は精度目標です。 元素に合わせたノルム保存擬ポテンシャルではありません。実金属、自己無撞着Hartree/XC、一般材料や長時間MDは未検証です。

- Hydrogenic formulas and immutable finite-basis helium reference cards: https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/
- Small 1D box and quantum harmonic-oscillator eigenpairs: https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/
- A three-wave periodic projector and Fermi-occupation model: https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json

Common execution records: [{"id": "hydrogenic-atoms", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#hydrogenic-atoms-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#hydrogenic-atoms-en"}}, {"id": "atomic-reference-cards", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "quantum-box-ho", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "periodic-projector-occupations", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`; hydrogenic-atoms, helium-ground-state, quantum-box-ho)
- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`; helium-ground-state)
- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`; helium-ground-state)
- [3平面波・非局所核と平均Fermi占有](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-projector-fermi-model-ja) (`finite-projector-fermi-model`; finite-projector-fermi)

#### 問題の図 (`method-problems-ja`)

##### [水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#code-ja)

- [水素型原子：解析解と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`) · [コードZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

- [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja) (`atomic-reference-cards`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。

##### [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja) (`quantum-box-ho`)

![1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。 8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

NumPyで8回全対角化し、native824固有対を保存して低24対を表示します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja#code-ja)

- [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja) (`quantum-box-ho`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。

##### [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja) (`finite-projector-fermi`)

![3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。 自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#code-ja)

- [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja) (`periodic-projector-occupations`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。


#### 厳密解・参照解 (`method-references-ja`)

##### [水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#references-ja) (`hydrogenic-atoms`)

- [水素型原子：解析解と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hydrogenic-coulomb-reference-ja) (`hydrogenic-coulomb-reference`; 同じ問題の参照; 解析参照)

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。

[既存の参照図](/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja)

- [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja) (`atomic-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-measurements)

##### [He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja) (`helium-ground-state`)

- [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja) (`atomic-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-measurements)

##### [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja#references-ja) (`quantum-box-ho`)

- [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quantum-box-ho-ja) (`quantum-box-ho`; 同じ問題の参照; 解析参照)

8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。

[既存の参照図](/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja#quantum-box-ho-ja-measurements)

##### [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#references-ja) (`finite-projector-fermi`)

- [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja) (`periodic-projector-occupations`; 同じ問題の参照; 半解析参照)

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

[既存の参照図](/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#schrodinger)
- 独立参照: [独立参照の保存データ](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 水素型原子：解析解と格子収束 (`hydrogenic-atoms`)

[水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[固定入力](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。

##### H/Heの式・密度・固定参照カード (`atomic-reference-cards`)

[He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。

##### 1次元箱型井戸・量子調和振動子 (`quantum-box-ho`)

[1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。

##### 3平面波の非局所projectorと有限温度占有 (`periodic-projector-occupations`)

[3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### 関連ソース

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### 配布版のテスト

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`; hydrogenic-atoms, helium-ground-state, quantum-box-ho)
- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`; helium-ground-state)
- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`; helium-ground-state)
- [Three-wave nonlocal kernel and mean Fermi occupations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-projector-fermi-model-en) (`finite-projector-fermi-model`; finite-projector-fermi)

#### Problem figures (`method-problems-en`)

##### [Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#code-en)

- [Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`) · [Code ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

- [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en) (`atomic-reference-cards`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.

##### [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en) (`quantum-box-ho`)

![Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity. Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en#code-en)

- [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en) (`quantum-box-ho`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.

##### [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en) (`finite-projector-fermi`)

![Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model. Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#code-en)

- [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en) (`periodic-projector-occupations`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.


#### Exact / reference solutions (`method-references-en`)

##### [Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#references-en) (`hydrogenic-atoms`)

- [Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hydrogenic-coulomb-reference-en) (`hydrogenic-coulomb-reference`; Same-problem reference; Analytic reference)

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.

[Existing reference profile](/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en)

- [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en) (`atomic-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

[Existing reference profile](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-measurements)

##### [Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en) (`helium-ground-state`)

- [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en) (`atomic-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

[Existing reference profile](/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-measurements)

##### [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en#references-en) (`quantum-box-ho`)

- [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quantum-box-ho-en) (`quantum-box-ho`; Same-problem reference; Analytic reference)

Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.

[Existing reference profile](/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-measurements)

##### [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#references-en) (`finite-projector-fermi`)

- [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-projector-occupations-en) (`periodic-projector-occupations`; Same-problem reference; Semi-analytic reference)

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

[Existing reference profile](/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#schrodinger)
- Independent reference: [Saved independent-reference data](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Hydrogenic atoms: analytic references and grid refinement (`hydrogenic-atoms`)

[Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[Fixed input](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.

##### Hydrogenic formulas and immutable finite-basis helium reference cards (`atomic-reference-cards`)

[Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.

##### Small 1D box and quantum harmonic-oscillator eigenpairs (`quantum-box-ho`)

[Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.

##### A three-wave periodic projector and Fermi-occupation model (`periodic-projector-occupations`)

[A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/verification.json)

###### Related source

- [/code/quantum-atoms/2026-11-21/atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/atomic_radial.py)
- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### Package tests

- [/code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output --figures
```
