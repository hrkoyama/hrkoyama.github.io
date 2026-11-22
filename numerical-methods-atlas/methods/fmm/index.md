# Fast multipole translations / 高速多重極法の移動演算

Status: educational-example

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

No 3D 1/r kernel, adaptive tree, periodic FMM, singular quadrature or empirical complexity/scaling study. Evidence applies to this 2D free-space educational implementation.

Other names: FMM法, fast multipole method, 高速多重極法, 高速多重極展開法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/



- Reference: https://doi.org/10.1016/0021-9991(87)90140-9 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

- 2D logarithmic FMM with M2M, M2L and L2L: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

Common execution records: [{"id": "fmm", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
