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

Common execution records: [{"id": "hydrogenic-atoms", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#hydrogenic-atoms-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#hydrogenic-atoms-en"}}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`; hydrogenic-atoms)

#### 問題の図 (`method-problems-ja`)

##### [水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`)

![公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#code-ja)

- [水素型原子：解析解と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja) (`hydrogenic-atoms`) · [コードZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。


#### 厳密解・参照解 (`method-references-ja`)

##### [水素型原子の動径固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#references-ja) (`hydrogenic-atoms`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

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

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`; hydrogenic-atoms)

#### Problem figures (`method-problems-en`)

##### [Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`)

![Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#code-en)

- [Hydrogenic atoms: analytic references and grid refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en) (`hydrogenic-atoms`) · [Code ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.


#### Exact / reference solutions (`method-references-en`)

##### [Hydrogenic radial eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#references-en) (`hydrogenic-atoms`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

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
