# H2 molecular restricted Hartree–Fock / H₂分子の閉殻HF

Python 3.12. Original educational analytic s-Gaussian integrals and RHF.

    python -m pip install -r requirements.txt
    python run.py --input inputs.json --output output
    python -m pytest -q

`output/result.json` contains all measured quantities, acceptance decisions,
SCF histories, stopping reasons, input/reference hashes and environment versions.
`solution.csv` contains the 24 geometry/basis results and `scf.csv` the SCF traces.
Both CSVs are numeric: basis_index is the zero-based basis_definitions index in
result.json. At the first iteration only, CSV delta_energy/density_change are
zero placeholders meaning “no preceding sample”; JSON stores null instead.

A nonempty output directory is preserved. Exit0: numerical criteria passed;
exit1: computed but unmet, including SCF cycle exhaustion; exit2: invalid input
or runtime error. To exercise a genuine convergence failure:

    python run.py --input inputs.json --output failed --max-cycles 1

The diagnostic override is recorded in execution_options; it does not change
the geometry, basis or independently saved reference. Output preserves the
unconverged states, residuals and termination='scf_not_converged'. Changing the
input JSON requires regenerating the independent reference (the input hash is
checked strictly). No physical or numerical acceptance value is fitted at run time.

## Model and finite-basis scope

Clamped H nuclei at z=±R/2, R=0.8,1.4,3.0 bohr; two electrons, spin-restricted
closed-shell RHF, isolated nonperiodic system; hartree/bohr atomic units.
All functions are real normalized atom-centered s Gaussians. The original
solver evaluates overlap, kinetic energy, nuclear attraction and two-electron
repulsion analytically with Boys F0. PySCF is never imported by the solver.

STO-3G is a separate minimal contracted baseline. The convergence sequence has
2,3,…,8 uncontracted s functions per H and is nested: every new level keeps all
old exponents. STO-3G is NOT assumed nested with that sequence. basis-provenance.json
records the independently checked BSE v1 H parameters and original publication.

The predeclared stopping target requires BOTH final adjacent additions (one
diffuse, one tight) to change total energy by ≤1e-3 hartree at every geometry.
This is stabilization in these prescribed finite s subspaces. The earlier tiny
step followed by a larger step illustrates why a single small increment is
insufficient. Passing this target is NOT a bound on the complete-basis error.
There are no p/d polarization functions, no angular convergence study, no
correlation treatment, no basis-set-superposition correction and no general
molecular/periodic solver. Restricted HF gives an incorrect dissociation limit;
R=3bohr is a stretched-bond test of the same restricted model, not a validated
bond-breaking or correlated-H2 calculation.

## SCF and independent checks

Symmetric overlap orthogonalization; an overlap eigenvalue≤1e-8 is rejected
without basis deletion. Condition(S) and minimum eigenvalue are recorded.
A controlled0.15radian mixing of the core-H occupied and first virtual orbitals
starts each SCF away from the symmetric stationary guess. Density mixing is0.5.
Convergence requires energy change≤1e-12Eh, density change≤1e-10 (AO Frobenius),
and orthonormal-basis FDS−SDF commutator norm≤1e-10 simultaneously. Reported
P is always reconstructed from an occupied orbital, not a fractional mixed
state. Rebuilt-F occupied/all-orbital residuals, C^TSC, trace(PS), PSP−2P and an
independent occupied-orbital energy formula are checked. Loose/medium/tight
SCF sweeps separate iterative error from the fixed finite-basis error.

reference_pyscf.py shares only the explicit input values and imports no educational
solver. PySCF2.11.0/libcint supplies its own integrals and SCF. It is run at the
same explicit geometries/bases, energy tolerance1e-13Eh and gradient1e-10.
Tests compare total energies and independent S/H eigenvalue spectra, which are
unchanged by AO permutation. These numerical finite-basis references are not
exact H2 energies. To regenerate the reference in a NEW directory:

    python -m pip install -r requirements-reference.txt
    python reference_pyscf.py --input inputs.json --output new-reference.json

The optional reference dependency is not required to rerun the saved comparison.
The archive verifier independently extracts the ZIP, runs all tests and fixed
inputs, checks a cycle-exhaustion failure, and records numerical reproduction.

## Figures

    python -m pip install -r requirements-plotting.txt
    python plot_results.py --input output/result.json --output figures

preview.png shows three sampled bond lengths joined only as visual guides and
basis-increment magnitudes. scf.png shows iterative energy error relative to the
final same-run value and the measured commutator, not error to an exact solution.

## Sources and reuse

- C.C.J.Roothaan (1951), New Developments in Molecular Orbital Theory,
  https://doi.org/10.1103/RevModPhys.23.69
- S.F.Boys (1950), Electronic Wave Functions.I.A General Method of Calculation
  for the Stationary States of Any Molecular System,
  https://doi.org/10.1098/rspa.1950.0036
- W.J.Hehre,R.F.Stewart,J.A.Pople (1969), Self-Consistent Molecular-Orbital
  Methods.I.Use of Gaussian Expansions of Slater-Type Atomic Orbitals,
  https://doi.org/10.1063/1.1672392
- B.P.Pritchard etal.(2019), A New Basis Set Exchange: An Open,Up-to-Date Resource
  for the Molecular Sciences Community, https://doi.org/10.1021/acs.jcim.9b00725
- Q.Sun etal.(2020), Recent developments in the PySCF program package,
  https://doi.org/10.1063/5.0006074

Original Python code: MIT / LICENSE. Inputs, numerical data, figures and prose
retain item-specific site terms at https://hrkoyama.github.io/rights/ . No paper
text or third-party software source is bundled; dependencies retain their licenses.
