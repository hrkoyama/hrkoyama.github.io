# Yee finite-difference time-domain method / Yee FDTD

Status: educational-example

Validate 2D TMz vacuum, oblique Fresnel interfaces and four-side/corner PML with fixed inputs.

2次元TMzの真空・斜めFresnel界面・四辺と角のPMLを固定入力で検証。

Educational 2D TMz: retained vacuum modes, normal dielectric interface, x-PML and four-side/corner PML; r4 validates selected s-polarized oblique packets at a lossless nonmagnetic interface using Fresnel fields, packet R/T, flux balance and refinement. Not blanket validation of p polarization, total internal reflection, loss/dispersion, general media or 3D.

Other names: FDTD法, finite difference time domain, 有限差分時間領域法, Yee法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/



- Reference: https://doi.org/10.1109/tap.1966.1138693 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://arxiv.org/abs/1705.02274v2 — Research preprint v2; energy Eq26 and strict CFL Eq35 consulted. Not a claim to implement its subgridding method.
- Reference: https://doi.org/10.1006/jcph.1994.1159 — Original split-field PML publication: bibliographic identity and abstract checked. Original full text was not available for inspection. The implemented reduction and discrete balance are derived and tested separately; consult Johnson for the matched-layer interpretation.
- Reference: https://arxiv.org/abs/2108.05348v1 — Author notes, selected sections 4.1–4.2 and 7.1–7.3: matching electric and magnetic damping, anisotropic interpretation, discretization reflections and incidence limitations. Not a complete audit of every PML formulation.
- Reference: https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/ — Author textbook, selected sections 7-6-1 and 7-6-2, printed pages 522–524 (PDF pages 36–38): tangential E/H continuity, normal-incidence field reflection/transmission and impedance weighting of power. A textbook exposition, not an original Fresnel publication.

2D TMz Yee FDTD supplement: vacuum periodic/PEC modes, lossless dielectric Fresnel scattering and matched PML cases. The reading distinguishes normal/oblique interface incidence, s-polarization, x-directed strip and four-side/corner configurations actually included in the current edition. Analytic fields, reflection/transmission energies, grid refinement and independent energy/work/flux budgets are checked separately.

- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/solver.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/run.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/scattering.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/run_scattering.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/corner.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/run_corner.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/oblique.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/run_oblique.py

- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/test_fdtd.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/test_scattering.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/test_corner.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/test_oblique.py

Download: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/fdtd-2026-11-22-r4.zip
Manifest: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/source-manifest.json
Verification: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/verification.json

- periodic-wave: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/results/periodic-wave/result.json
- pec-cavity: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/results/pec-cavity/result.json
- dielectric-interface: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/results/dielectric-interface/result.json
- pml-pulse: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/results/pml-pulse/result.json
- pml-corners: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/results/pml-corners/result.json
- dielectric-oblique: https://hrkoyama.github.io/code/fdtd/2026-11-22-r4/results/dielectric-oblique/result.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py
python run.py --input inputs/periodic-wave.json --output rerun-periodic-wave
python run.py --input inputs/pec-cavity.json --output rerun-pec-cavity
python run_scattering.py --input inputs/dielectric-interface.json --output rerun-dielectric-interface
python run_scattering.py --input inputs/pml-pulse.json --output rerun-pml-pulse
python run_corner.py --input inputs/pml-corners.json --output rerun-pml-corners
python run_oblique.py --input inputs/dielectric-oblique.json --output rerun-dielectric-oblique
```

Next: Separately validate p polarization, total internal reflection, loss/dispersion and 3D.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
