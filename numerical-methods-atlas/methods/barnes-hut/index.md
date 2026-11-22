# Barnes–Hut octree / Barnes–Hut八分木

Status: educational-example

Approximate isolated 3D particle gravity with an octree. The public example uses G=1 and a Plummer-softened kernel, with a monopole or the same kernel's full second-moment term, compared with direct summation.

孤立した3次元粒子の重力加速度をoctreeで近似する。公開例はG=1のPlummer軟化核に対し、質量単極子または同じ軟化核の完全な二次モーメント項を使い、直接和と比較する。

A static-force educational example without time integration, expansion, periodic images or FMM. theta is not a rigorous error bound, and order=2 need not improve every configuration. Targetwise approximation does not guarantee exact action–reaction/total-momentum conservation. Interaction counts are not timings or empirical complexity guarantees for every distribution.

Other names: Barnes Hut, Barnes-Hut法, バーンズ・ハット法, Barnes Hut tree, BH tree


## 条件と確認範囲 (ja)

problem: 正質量粒子の孤立・Plummer軟化Newton重力加速度。

variant: Barnes–Hut octree、幾何開角s/d、単極子または軟化核の完全二次モーメント。theta=0で全て開く。

use_when:
- 孤立境界で静的な力と開角・近似次数の関係を調べるとき。
- 同じ位置・質量・軟化長で直接和と照合するとき。

avoid_when:
- 周期系を孤立直接和とそのまま比較したい場合。
- 近接衝突の非軟化力や厳密な対称相互作用を必要とする場合。

assumptions [specified]:
- 位置は有限の(N,3)配列、質量は正かつ有限、粒子数は1以上。softening=ε>0、theta≥0、orderは0または2。
- 節点の一辺s=2×half、質量中心までの距離dについて s/d<theta なら受理する。ただし対象粒子を含むセルは必ず開き、葉では自己項を除く。
- 加速度核は −m r/(r²+ε²)^(3/2)。order=2はS=Σmδδᵀの完全なTaylor項を加え、軟化された核に必要なtrace(S)項も保持する。
粒子入力、Plummer核、受理基準と二次項をコードで確認した。

units [specified]:
無次元のG=1。位置と軟化長は同じ長さ単位、質量には一貫した単位を使う。長さL₀・質量M₀で次元を戻す場合、加速度の尺度はGM₀/L₀²。
G=1と位置・質量・軟化の共通規約を固定例でも確認した。

boundary_conditions [specified]:
孤立境界で周期像を加えない。軟化核のポテンシャル −Gm/√(r²+ε²) は無限遠で零となる規約。周期PM・Ewald・TreePMとは異なる境界問題。
周期像なしの孤立直接和とtreeを同じ核で比較する。

limitations [specified]:
静的な力の教育例で、時間積分・宇宙膨張・周期境界・FMMを含まない。thetaは厳密な誤差上限ではなく、order=2がすべての配置で常に改善する保証もない。対象ごとの近似なので厳密な作用反作用・全運動量保存は保証せず、相互作用回数は実時間や全分布でのO(N log N)の実測ではない。
固定静的例とターゲット別の近似に限定した。

Review: tree_acceleration/direct_acceleration、自己項・theta=0・選択配置の二次項・重複位置の既存検査、192粒子の固定入力・実行部・保存済み2検査の結果を読んだ。保存結果の再実行は行っていない。

Not checked:
- 原論文本文にある開角・多重極の全詳細。
- 動的軌道、全粒子分布の誤差上限、実時間性能の新しい計算。

Evidence:
- tree_acceleration, _build, direct_acceleration: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py
- fully-open direct comparison, selected second moment and coincident-particle tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py
- fixed static direct-versus-tree runner: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py
- 192-particle isolated G=1, ε=0.03, theta=0.6, order=2: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json
- stored fixed force comparison; two recorded checks: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json

References:
- [original-method / primary-research] Barnes, J. & Hut, P. (1986). A hierarchical O(N log N) force-calculation algorithm. — https://doi.org/10.1038/324446a0
  立方体を八分割する階層的な力計算の出典。今回確認した抄録から、軟化核や二次モーメント式の細部まで確認済みとはしない。
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic metadata returned by web search; full article body not reviewed.; https://www.nature.com/articles/324446a0

## Conditions and review scope (en)

problem: Isolated Plummer-softened Newtonian acceleration from positive-mass particles.

variant: Barnes–Hut octree with geometric s/d opening, monopole or full softened second moment; theta=0 fully opens the tree.

use_when:
- Studying static isolated-force error versus opening angle and expansion order.
- Comparing against direct summation with identical positions, masses and softening.

avoid_when:
- Direct comparison of a periodic problem to isolated direct summation.
- Unsoftened close encounters or strictly symmetric pair interactions.

assumptions [specified]:
- Positions are finite (N,3), masses positive and finite, and N≥1; ε=softening>0, theta≥0 and order is 0 or 2.
- A node is accepted when s/d<theta, with s=2×half and d measured to its center of mass. Target-containing cells are always opened; leaves exclude self terms.
- The acceleration kernel is −m r/(r²+ε²)^(3/2). order=2 adds the full Taylor term from S=Σmδδᵀ, retaining trace(S) for the softened kernel.
Checked particle inputs, Plummer kernel, acceptance and second-order term in code.

units [specified]:
Dimensionless G=1. Positions and softening share a length unit and masses use one consistent unit. With scales L₀,M₀, acceleration is restored with GM₀/L₀².
Checked G=1 and common position/mass/softening conventions in the fixed example.

boundary_conditions [specified]:
Isolated boundaries without periodic images; the softened potential −Gm/√(r²+ε²) tends to zero at infinity. This is a different boundary problem from periodic PM, Ewald or TreePM.
The tree and isolated direct sum use the same kernel without periodic images.

limitations [specified]:
A static-force educational example without time integration, expansion, periodic images or FMM. theta is not a rigorous error bound, and order=2 need not improve every configuration. Targetwise approximation does not guarantee exact action–reaction/total-momentum conservation. Interaction counts are not timings or empirical complexity guarantees for every distribution.
Scoped to static cases and targetwise approximation.

Review: Inspected tree_acceleration/direct_acceleration, existing self-exclusion/fully-open/selected second-moment/coincident-particle tests, and the 192-particle fixed input, runner and stored two-check result; no rerun.

Not checked:
- All original-paper opening/multipole details beyond the reviewed abstract.
- New trajectory, all-distribution error-bound or wall-clock performance calculations.

Evidence:
- tree_acceleration, _build, direct_acceleration: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py
- fully-open direct comparison, selected second moment and coincident-particle tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py
- fixed static direct-versus-tree runner: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py
- 192-particle isolated G=1, ε=0.03, theta=0.6, order=2: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json
- stored fixed force comparison; two recorded checks: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json

References:
- [original-method / primary-research] Barnes, J. & Hut, P. (1986). A hierarchical O(N log N) force-calculation algorithm. — https://doi.org/10.1038/324446a0
  Supports hierarchical octree force evaluation; the reviewed abstract does not establish the atlas's softened second-moment formula.
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic metadata returned by web search; full article body not reviewed.; https://www.nature.com/articles/324446a0


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py

- Reference: https://doi.org/10.1038/324446a0 — Octree hierarchical force evaluation; does not by itself document the atlas's full second-moment expansion of a Plummer-softened kernel.

Common execution records: [{"id": "barnes-hut", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#barnes-hut-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#barnes-hut-en"}}]

Runnable example:

{
  "input": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json",
  "runner": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py",
  "reference": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json",
  "forces": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/forces.csv",
  "command": "python examples/barnes-hut/run.py --input examples/barnes-hut/input.json --output output-barnes-hut",
  "working_directory": "Extracted code edition directory"
}

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
