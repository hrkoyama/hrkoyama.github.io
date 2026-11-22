# Radiation transport and moment methods / 放射輸送・モーメント法

Status: educational-example

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

Multiple scattering, thermal emission, frequency redistribution, moving media and radiation–fluid coupling are unimplemented. This does not reproduce full DISORT functionality/stabilization.

Other names: 放射輸送法, radiative transfer, radiation transport, 放射モーメント法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/radiation-transport/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/radiation-transport/



- Reference: https://doi.org/10.1016/0022-4073(84)90112-2 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplement

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

- Discrete-ordinate radiation transport through an absorbing slab: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

Common execution records: [{"id": "radiation-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
