# Lie–Trotter splitting / Lie–Trotter分割

Status: reading-only

First-order integration by composing two full subflows. Compare formulas, commutators, local/global errors and a small noncommuting example with Strang splitting.

右辺を2つの部分流に分け、全刻みずつ順に合成する1次の時間積分法。Strangとの公式・交換子・局所と大域の誤差・非可換な小例を比較する。

The smooth finite-dimensional illustration does not validate shocks, stiff PDEs or general boundaries. Exact subflows do not remove composition stability restrictions. The illustration script is not a general solver release.

Other names: Lie-Trotter splitting, Lie Trotter splitting, Lie splitting, Trotter splitting, Lie–Trotter分割法, リー・トロッター分割, リートロッター分割, リー・トロッタ分割, 1次作用素分割

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/



- Reference: https://doi.org/10.1090/S0002-9939-1959-0108732-6 — AMS bibliographic record checked. Original semigroup product-limit reference; no audit of unbounded-operator hypotheses. Finite-dimensional order calculations are derived in the chapter.
- Reference: https://www.unige.ch/~hairer/poly_geoint/week2.pdf — Author-hosted Lecture 2, section 5, printed pp.12–14, equations (23)–(27), and exact versus numerical subflows: Lie–Trotter, symmetric second-order composition and separable Hamiltonians. Selected passages, not a full-lecture audit.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
