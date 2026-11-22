# Yee finite-difference time-domain method / Yee FDTD

Status: educational-example

Connect staggered Maxwell fields and time updates.

Maxwell方程式の格子上の変数配置と時間更新を扱う。

Educational fixed-input validation of 2D TMz homogeneous-vacuum periodic waves and a rectangular PEC cavity. References are continuum analytic solutions and separately derived discrete modes/invariants; no independent external FDTD-library comparison is claimed. PML, reflection/transmission, scatterers, charges/currents, dispersive media and general three-dimensional geometries remain unimplemented and unvalidated.

Other names: FDTD法, finite difference time domain, 有限差分時間領域法, Yee法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/



- Reference: https://doi.org/10.1109/tap.1966.1138693 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://arxiv.org/abs/1705.02274v2 — Research preprint v2; energy Eq26 and strict CFL Eq35 consulted. Not a claim to implement its subgridding method.

2D TMz Yee FDTD supplement: source-free dimensionless vacuum, periodic oblique plane wave and rectangular PEC cavity. Analytic fields, grid refinement, dispersion and modified discrete energy are checked separately.

- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22/solver.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22/run.py

- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22/test_fdtd.py

Download: https://hrkoyama.github.io/code/fdtd/2026-11-22/fdtd-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/fdtd/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/fdtd/2026-11-22/verification.json

- periodic-wave: https://hrkoyama.github.io/code/fdtd/2026-11-22/results/periodic-wave/result.json
- pec-cavity: https://hrkoyama.github.io/code/fdtd/2026-11-22/results/pec-cavity/result.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py
python run.py --input inputs/periodic-wave.json --output rerun-periodic-wave
python run.py --input inputs/pec-cavity.json --output rerun-pec-cavity
```

Next: Separately validate interface reflection/transmission and absorption/PML reflection error.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
