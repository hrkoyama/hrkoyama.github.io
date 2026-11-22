# Strang splitting / Strang分割

Status: reading-only

Second-order integration using a symmetric half/full/half composition. Compare Lie–Trotter, subsolver order, boundaries and stability, with links to existing reaction–diffusion runs.

半刻み・全刻み・半刻みの対称合成による2次の時間積分法。Lie–Trotterとの違い、部分ソルバーの次数、境界条件と安定性、既存の反応拡散の実行例を解説する。

The smooth finite-dimensional illustration does not validate shocks, stiff PDEs or general boundaries. Exact subflows do not remove composition stability restrictions. The illustration script is not a general solver release.

Other names: Strang splitting, Strang splitting method, Strang分割法, ストラング分割, ストラング分割法, symmetric Strang splitting, Strang–Marchuk splitting, 2次作用素分割

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/



- Reference: https://doi.org/10.1137/0705041 — Publisher bibliography checked for this addition. The original symmetric splitting reference is distinct from the Hairer lecture consulted for compositions and order. No fresh full-paper audit.
- Reference: https://www.unige.ch/~hairer/poly_geoint/week2.pdf — Author-hosted Lecture 2, section 5, printed pp.12–14, equations (23)–(27), and exact versus numerical subflows: Lie–Trotter, symmetric second-order composition and separable Hamiltonians. Selected passages, not a full-lecture audit.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
