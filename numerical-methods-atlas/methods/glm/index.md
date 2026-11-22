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

## Small fixed-input validation supplements

Orszag–Tang: CT, GLM and independent Athena++: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++. GLM longitudinal mode: analytic damping: Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution. CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence. Orszag–Tang: matched CT/GLM and converged independent references: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated. Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem.

Orszag–Tang：CT・GLMと独立Athena++比較: 同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。 GLMの磁気単極子モード：解析的減衰: GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。 CT・GLM：移動する磁気静力学平衡の格子・時間収束: 非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。 Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束: 同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。 CTの初期制約保持とGLMの能動的cleaning：非物理診断対照: 故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。

- Orszag–Tang: CT, GLM and independent Athena++: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/
- GLM longitudinal mode: analytic damping: https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json

- CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/
- Orszag–Tang: matched CT/GLM and converged independent references: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/
- Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json

Common execution records: [{"id": "ct-glm-independent", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "glm-fourier-mode", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ct-glm-smooth-convergence", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ct-glm-ot-convergence", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ct-glm-constraint-control", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
