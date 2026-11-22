# Automatic differentiation / 自動微分

Status: educational-example

A shared foundation for the chain rule, forward/reverse modes and JVPs, with analytic, finite-difference and forward-AD verification on the same Bratu equation.

共通基盤として連鎖律・前進／逆モード・JVPを学び、同じBratu方程式で解析微分・有限差分・前進モード自動微分を検証する。

Limited to educational real forward mode and small dense-Newton Bratu comparisons. Reverse mode, HVPs, implicit sensitivities and matrix-free Newton–Krylov are explanatory only. This does not validate a general AD library or shock sensitivities.

Other names: AD, 自動微分法, automatic differentiation, アルゴリズム微分, Bratu, JVP, forward mode, 前進モード, 双対数

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/automatic-differentiation/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/automatic-differentiation/



- Reference: https://doi.org/10.1145/355586.364791 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1007/bf01931367 — Method-specific source; see the detailed reading for source role and actual review depth.

Forward-mode AD supplement: analytic/finite-difference/AD Bratu derivatives, Newton convergence and spatial refinement. Reverse-mode execution and implicit sensitivities are not implemented.

- Code: https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/autodiff/2026-11-22/scripts/build_autodiff.py

- Tests: https://hrkoyama.github.io/code/autodiff/2026-11-22/tests/test_autodiff.py

Download: https://hrkoyama.github.io/code/autodiff/2026-11-22/autodiff-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/autodiff/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/autodiff/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/autodiff/2026-11-22/docs/figures/autodiff-bratu.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_autodiff.py
python scripts/build_autodiff.py
```

Next: Separate executable verification for reverse mode, implicit sensitivities and adjoints.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
