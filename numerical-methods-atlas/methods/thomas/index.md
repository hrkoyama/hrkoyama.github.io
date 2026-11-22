# Thomas tridiagonal elimination / Thomas法／三重対角消去

Status: educational-example

Read about Thomas tridiagonal elimination, follow the original references and inspect related educational code and checks.

「Thomas法／三重対角消去」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: Thomas algorithm, トーマス法, トーマスアルゴリズム, 三重対角行列算法, TDMA

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py

- Reference: https://doi.org/10.1017/S0305004100023197 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1090/S0025-5718-1977-0431719-X — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1137/1.9780898719505 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Common execution records: [{"id": "poisson-1d-dirichlet", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#poisson-1d-dirichlet-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#poisson-1d-dirichlet-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
