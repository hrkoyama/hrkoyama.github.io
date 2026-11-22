Independent periodic DFT reference
==================================
The reference is produced by DFTK 0.7.19 / Julia 1.12.2 using plane waves,
not by another PySCF density-fitting implementation. The two engines share
Libxc formulas (Libxc 7.0) for Dirac LDA exchange plus VWN5 correlation.
It is an implementation/discretization cross-check, not an independent
exchange-correlation functional or an experimental validation.

Physical model
--------------
One spin-restricted He atom (2 electrons) per simple-cubic cell, a=4 bohr.
This is an artificial pedagogical insulator, not equilibrium solid He.
Lattice, atom, explicit fractional k coordinates and exact GTH coefficients
are read from the common inputs.json. DFTK uses lattice-vector columns;
the input supplies rows. The script transposes the convention explicitly.
He.gth is the local-only GTH-PADE-q2 potential exported numerically from
PySCF 2.11.0; the script audits every coefficient against inputs.json.
Source coefficients: pyscf/pbc/gto/pseudo/gth-pade.dat, He GTH-PADE-q2.
No alternative default pseudopotential or default LDA functional is used.

Energy convention
-----------------
Native DFTK neutral-cell ionic Ewald plus native GTH G=0 correction;
complete SCF total energy per cell in Hartree. No fitted energy offset.
The fixed two converged bands allow a sampled KS gap; this is not proof
of the global band gap between the sampled k points.

Regeneration (separate from the fast Python CI)
----------------------------------------------
Keep Project.toml and Manifest.toml together in reference-environment/.
Use Julia 1.12.2; from the periodic-dft folder:

  JULIA_NUM_PRECOMPILE_TASKS=2 JULIA_NUM_THREADS=2 OPENBLAS_NUM_THREADS=1 \
    julia --project=reference-environment -e 'using Pkg; Pkg.instantiate()'
  JULIA_NUM_PRECOMPILE_TASKS=2 JULIA_NUM_THREADS=2 OPENBLAS_NUM_THREADS=1 \
    julia --project=reference-environment reference.jl inputs.json reference-dftk.json He.gth

A fresh run recomputes every case. ATLAS_REFERENCE_RESUME=1 explicitly
opts into reuse of matching records after physical/pseudo/version audits.
MPI is initialized even for this one-process calculation; some sandboxes
must allow a local socket. The reference uses no online scientific service.

Convergence and accepted scope
------------------------------
Cutoffs 60,90,120,180,240 Ha; explicit Gamma and 2x2x2 Gamma-centered meshes.
Density residual target 1e-9, >=2 bands converged, zero smearing.
The final 180->240 Ha total-energy increments are ~16.4 and17.4 microHa,
below the 0.1 mHa empirical cutoff-increment target (not a rigorous bound
on the unknown infinite-basis error). The finite Gaussian and plane-wave
results need not match to SCF precision. Reference JSON includes all
energies, coefficients identity, version/hash provenance, electron counts,
orthogonality, residuals, energy components and sampled eigenvalues.

Primary implementation sources
------------------------------
https://docs.dftk.org/stable/guide/tutorial/
https://docs.dftk.org/stable/examples/pseudopotentials/
https://docs.dftk.org/stable/api/
https://github.com/JuliaMolSim/DFTK.jl/tree/v0.7.19
https://github.com/pyscf/pyscf/blob/v2.11.0/pyscf/pbc/gto/pseudo/gth-pade.dat
https://libxc.gitlab.io/functionals/
