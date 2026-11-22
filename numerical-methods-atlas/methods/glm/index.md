# GLM divergence cleaning / GLM発散クリーニング

Status: educational-example

Read about GLM divergence cleaning, follow the original references and inspect related educational code and checks.

「GLM発散クリーニング」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: GLM法, GLM divergence cleaning, divergence cleaning, 発散クリーニング, div cleaning

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hlld.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py

- Reference: https://doi.org/10.1017/S002211207900210X — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1093/mnras/staa877 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1086/166684 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1006/jcph.2000.6519 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1006/jcph.2001.6961 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2005.02.017 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(88)90120-9 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://arxiv.org/abs/0911.3410 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplement

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++. Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution.

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。 GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。

- Orszag–Tang: CT, GLM and independent Athena++: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/
- GLM longitudinal mode: analytic damping: https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json

Common execution records: [{"id": "ct-glm-independent", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "glm-fourier-mode", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
