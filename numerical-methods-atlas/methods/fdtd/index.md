# Yee finite-difference time-domain method / Yee FDTD

Status: educational-example

Validate Yee TMz/TEz, s/p Fresnel interfaces, Brewster/TIR and PML with fixed inputs.

Yee FDTDのTMz/TEz、s/p偏光のFresnel界面、Brewster・全反射とPMLを固定入力で検証。

Educational Yee FDTD: retained TMz vacuum/interface/PML cases plus r5 TEz p polarization, Brewster condition and TIR for specified single-transverse-mode packets. Full-2D equivalence, continuum Fresnel data, finite-window flux/amplitudes, evanescent decay/storage, discrete invariants and physical budgets have distinct roles. Not blanket validation of general media, multiple modes, loss/dispersion or 3D.

Other names: FDTD法, finite difference time domain, 有限差分時間領域法, Yee法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/



- Reference: https://doi.org/10.1109/tap.1966.1138693 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://arxiv.org/abs/1705.02274v2 — Research preprint v2; energy Eq26 and strict CFL Eq35 consulted. Not a claim to implement its subgridding method.
- Reference: https://doi.org/10.1006/jcph.1994.1159 — Original split-field PML publication: bibliographic identity and abstract checked. Original full text was not available for inspection. The implemented reduction and discrete balance are derived and tested separately; consult Johnson for the matched-layer interpretation.
- Reference: https://arxiv.org/abs/2108.05348v1 — Author notes, selected sections3.4,4.1–4.2 and7.1–7.3: independent x/y coordinate stretches and simultaneous corner damping, matching electric/magnetic rates, anisotropic interpretation, discretization reflections and incidence limitations. Not a complete audit of every PML formulation.
- Reference: https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/ — Author textbook, selected sections 7-6-1/7-6-2 (printed pp522–524), 7-9-1 (pp538–540), and 7-9-3/7-9-4 (pp541–544): normal/oblique Fresnel amplitudes, Snell and critical angles, evanescent fields, p-polarized Brewster condition and normal-power weighting. Field/sign conventions are adapted explicitly. Not an original Fresnel publication or a full-book audit.

2D Yee FDTD supplement: retained TMz vacuum modes, s-polarized dielectric interfaces and matched PML cases; selected TEz p-polarized Fresnel, Brewster and total-internal-reflection cases are distinguished in the current edition. Finite-band packet reflection, evanescent storage and normal transmitted flux have separate meanings. Analytic fields, grid refinement and independent energy/work/flux budgets are checked within each fixed input scope.

- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/solver.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/run.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/scattering.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/run_scattering.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/corner.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/run_corner.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/oblique.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/run_oblique.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/polarization.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/run_polarization.py

- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/test_fdtd.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/test_scattering.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/test_corner.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/test_oblique.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/test_polarization.py

Download: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/fdtd-2026-11-22-r5.zip
Manifest: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/source-manifest.json
Verification: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/verification.json

- periodic-wave: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/results/periodic-wave/result.json
- pec-cavity: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/results/pec-cavity/result.json
- dielectric-interface: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/results/dielectric-interface/result.json
- pml-pulse: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/results/pml-pulse/result.json
- pml-corners: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/results/pml-corners/result.json
- dielectric-oblique: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/results/dielectric-oblique/result.json
- p-polarization: https://hrkoyama.github.io/code/fdtd/2026-11-22-r5/results/p-polarization/result.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py
python run.py --input inputs/periodic-wave.json --output rerun-periodic-wave
python run.py --input inputs/pec-cavity.json --output rerun-pec-cavity
python run_scattering.py --input inputs/dielectric-interface.json --output rerun-dielectric-interface
python run_scattering.py --input inputs/pml-pulse.json --output rerun-pml-pulse
python run_corner.py --input inputs/pml-corners.json --output rerun-pml-corners
python run_oblique.py --input inputs/dielectric-oblique.json --output rerun-dielectric-oblique
python run_polarization.py --input inputs/p-polarization.json --output rerun-p-polarization
```

Next: Separately validate loss/dispersion, multimode interfaces and PML for evanescent fields.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
