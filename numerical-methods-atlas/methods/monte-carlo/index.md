# Monte Carlo integration / Monte Carlo積分

Status: educational-example

Connect random samples, variance and integration error.

乱数・標本数・分散と積分誤差をつなぐ。

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

Other names: モンテカルロ法, モンテカルロ積分, Monte Carlo method, Monte Carlo integration

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/monte-carlo/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/monte-carlo/



- Reference: https://doi.org/10.1080/01621459.1949.10483310 — Method-specific source; see the detailed reading for source role and actual review depth.

Scoped example: Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

Code: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py
Tests: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py
Download: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json

Common execution records: [{"id": "mc-integral", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#mc-integral-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#mc-integral-en"}}]

Next: Add validation against another reference problem before extending application scope.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
