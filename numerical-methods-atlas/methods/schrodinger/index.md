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
