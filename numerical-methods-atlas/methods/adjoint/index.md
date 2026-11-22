# Implicit differentiation and adjoint methods / 陰関数微分・随伴法

Status: educational-example

Verify implicit state sensitivities and discrete-adjoint gradients on Bratu against analytic continuous sensitivities and finite differences with fresh nonlinear solves.

Bratu方程式のパラメータ感度で、陰関数の感度方程式・離散随伴勾配・解析的な連続感度・解き直した有限差分を検証する。

The sensitivity edition verifies the smooth Bratu lower branch and a small nonsymmetric linear example, using the Euclidean adjoint with explicit objective quadrature weights. A separate chapter and edition address the one-parameter synthetic-observation inverse problem. Time-dependent adjoints and shock sensitivities remain unimplemented.

Other names: 随伴法, 随伴解析, adjoint method, adjoint analysis, 陰関数微分, implicit differentiation, parameter sensitivity, パラメータ感度, Bratu, 随伴法・逆問題, Adjoint methods and inverse problems

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/adjoint/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/adjoint/



- Reference: https://doi.org/10.1007/bf01061285 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1007/bf01931367 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://jaxopt.github.io/stable/implicit_diff.html — Official explanation of root-equation differentiation versus unrolling; the local NumPy supplement is an independent implementation.
- Reference: https://papers.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html — Selected implicit-root and JVP/VJP passages support the formulation; no reproduction of the full paper is claimed.

Bratu implicit sensitivity and discrete-adjoint supplement. Includes analytic continuous sensitivity, finite differences with fresh nonlinear solves, grid refinement and a nonsymmetric transpose test.

- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/scripts/build_bratu_sensitivity.py

- Tests: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/tests/test_bratu_sensitivity.py

Download: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/bratu-sensitivity-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/docs/figures/bratu-sensitivity.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_sensitivity.py
python scripts/build_bratu_sensitivity.py
```

Next: Separate validation for time-dependent adjoints, multi-parameter inverse optimization and nonsmooth problems. A separate chapter provides the one-parameter synthetic-observation inverse case.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
