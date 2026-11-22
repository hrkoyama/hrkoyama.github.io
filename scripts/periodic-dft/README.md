# Periodic He KS-LDA validation workflow

This is an original reproducibility and validation **driver using PySCF**, not a
new electronic-structure engine. PySCF provides integrals, crystalline Gaussian
orbitals, FFT density fitting, Libxc and SCF. A separate DFTK Julia script supplies
an independently implemented plane-wave reference; the scientific model is the
same but finite orbital representations differ.

The case is an **artificial pedagogical insulator**: one neutral two-electron He
pseudopotential in a fixed simple-cubic 4-bohr cell. It is not an equilibrium
solid-helium prediction. Born–Oppenheimer, nonrelativistic, spin-unpolarized
Kohn–Sham LDA uses Dirac exchange plus VWN5 correlation (Libxc `lda_x` and
`lda_c_vwn`). The exact local GTH/Pade parameters are recorded in inputs.json.
Geometry, electron number, pseudopotential coefficients and XC must match the
independent reference; no constant energy shift is fitted.

Install the fixed Python dependencies and run:

    python -m pip install -r requirements.txt
    python -m pytest -q
    python run.py --input inputs.json --output output

A new or empty output directory is required. Outputs are result.json,
solution.csv and scf.csv. Exit codes: 0 all acceptance criteria pass, 1 numerical
criteria unmet, 2 invalid input/runtime error. JSON retains full SCF histories,
physical conventions, actual library versions, input/reference SHA-256 and
termination. CSV uses numeric case/basis indices mapped by the JSON/input.
Each case's duration_seconds measures its SCF kernel; verification.json records
the complete independently extracted runner runtime including residual checks.
The first history energy difference has no predecessor; its CSV flag is zero
and its numeric placeholder zero is not a convergence claim.

All k-point triples and equal weights are explicit fractional reciprocal-lattice
coordinates. PySCF converts them to physical inverse-bohr units. Gamma and
2/3/4 meshes are compared. Each mesh samples an indirect **Kohn–Sham** gap at
those points only, not a global Brillouin-zone or fundamental many-body gap.
No metals, smearing, spin polarization or symmetry reduction is validated.
Unoccupied-band convergence is not established: the finite Gaussian and
plane-wave sampled gaps differ appreciably at the 2-mesh. The independent
agreement criterion applies to ground-state total energies, not band gaps.

K-point convergence, optimized Gaussian orbital-basis families, and FFT meshes
are varied separately. The FFT mesh controls auxiliary density/Coulomb and XC
quadrature precision, not the Gaussian orbital basis. Gaussian families are not
a nested variational sequence. The last energy change is a stated stopping
criterion, not a complete-basis error bound. SCF tolerance is swept at fixed
sampling/basis/grid; final-density commutator, electron count, orbital
orthogonality and reconstructed energy are checked separately. Electron number
is an imposed consistency check, not independent physical evidence.

Large Gaussian overlap condition numbers can occur at zone-boundary points;
minimum eigenvalues, condition numbers and residuals are recorded. This workflow
rejects eigenvalues below its fixed floor and does not silently remove AOs.
Agreement within an explicit finite-basis budget with a cutoff-converged
independent plane-wave calculation is stronger evidence than a small SCF energy
change alone. It is still not certification of general periodic DFT or physical
accuracy of LDA/pseudopotentials.

Original Python/Julia driver source is MIT (LICENSE). PySCF, DFTK, Libxc,
Gaussian basis datasets and the GTH pseudopotential retain their upstream terms;
no third-party software source is bundled. Saved inputs, numerical results,
figures and prose retain the site's item-specific terms:
https://hrkoyama.github.io/rights/ . Scientific provenance is stated in
provenance.json and the bilingual reading.
