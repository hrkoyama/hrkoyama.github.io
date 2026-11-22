# AUSM-family flux splitting / AUSM系列の流束分割

Status: educational-example

Read about AUSM-family flux splitting, follow the original references and inspect related educational code and checks.

「AUSM系列の流束分割」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: AUSM法, AUSM流束, advection upstream splitting method

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/shock-expansion/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/shock-expansion/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ppm_traced.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm_plus.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/ausm.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/rotated_flux.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/blunt_body.py

- Reference: https://doi.org/10.1016/0021-9991(84)90143-8 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://arxiv.org/abs/1410.4194 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1006/jcph.1996.0256 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2005.09.020 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2007.11.003 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
