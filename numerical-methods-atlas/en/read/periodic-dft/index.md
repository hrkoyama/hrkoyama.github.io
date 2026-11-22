# Periodic DFT: Γ points, k-point integration, basis sets, SCF and an independent reference

A small periodic cell containing one He atom connects Bloch’s theorem, k-point integration, periodic Gaussian bases, auxiliary FFT grids and SCF iteration. A PySCF-backed example is compared with an independent plane-wave DFTK reference, exposing the conventions needed to solve the same model with different discretizations.

This educational periodic problem uses nonrelativistic, spin-unpolarized LDA for a fixed simple-cubic He cell. The implementation is a driver using PySCF, rather than a DFT engine written from scratch. It does not optimize crystal structure or predict equilibrium solid helium.

## The fixed physical model and the numerical errors being tested

The input is a simple-cubic cell of side 4 bohr containing one He atom at the origin. A local GTH–PADE pseudopotential supplies two valence electrons for a closed-shell, spin-unpolarized Kohn–Sham problem. This He potential has no nonlocal projectors. One example therefore does not validate general multielement crystals or nonlocal pseudopotentials. The geometry is fixed as a teaching configuration for convergence experiments.

The exchange-correlation functional is specified explicitly as Libxc LDA_X plus LDA_C_VWN (VWN5). The label LDA alone does not align choices such as VWN and Perdew–Wang correlation. GTH–PADE names the chosen pseudopotential; it does not assert that its generation approximation is identical to the VWN5 used here. Both engines receive the same pseudopotential coefficients and exchange-correlation choice.

Atomic units are used, with lattice lengths in bohr and energies in hartree. Total energies are compared per unit cell, including electronic terms and periodic ion–ion interactions. SCF solution error, k-point quadrature, the orbital basis and the auxiliary density/potential grid are varied separately. Reducing these numerical effects does not measure the physical error of LDA or the pseudopotential approximation.

$$
\left[-\tfrac12\nabla^2+V_{\mathrm{loc}}+V_H[n]+V_{\mathrm{xc}}[n]\right]\psi_{n\mathbf k}=\varepsilon_{n\mathbf k}\psi_{n\mathbf k}
$$

## Bloch’s theorem and the units of a k point

For a periodic potential, an orbital can be written as a plane-wave phase times a lattice-periodic function. The periodic function u and the Bloch orbital ψ are distinct: u is periodic across cell boundaries, whereas ψ satisfies a k-dependent phase boundary condition. Γ is the special point k=0, where this phase is one.

Here A contains direct lattice vectors as columns and B contains reciprocal vectors as columns, with AᵀB=2πI. Fractional coordinates κ give the physical wavevector k=Bκ. The coordinates κ are dimensionless; k is in bohr⁻¹ when the lattice is in bohr. PySCF stores cell vectors as rows and passes physical wavevectors to SCF. A shared input lattice and fractional k-point list prevent confusion with DFTK’s column convention.

$$
\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r),\qquad u_{n\mathbf k}(\mathbf r+\mathbf R)=u_{n\mathbf k}(\mathbf r),\qquad\psi_{n\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{n\mathbf k}(\mathbf r)
$$

$$
A=(\mathbf a_1,\mathbf a_2,\mathbf a_3),\qquad B=2\pi A^{-\mathsf T},\qquad\mathbf k=B\boldsymbol\kappa,\qquad\Omega=|\det A|
$$

## Γ points and k meshes: quadrature versus band paths

Densities and energies of an infinite crystal involve integrals over the Brillouin zone. A finite set of k points and weights approximates these integrals. This example explicitly lists all points of a uniform mesh containing Γ and equal weights summing to one. Γ is included even for even subdivisions. This convention is not automatically identical to software defaults or the half-grid displacement of an even Monkhorst–Pack mesh. Fractional k points differing by an integer reciprocal vector represent the same point.

A Γ-only calculation is a one-point quadrature of the Brillouin zone. It can be adequate for some large real-space cells or localized orbitals, but adequacy for this small cell must be measured. Γ-only and several meshes are compared with the same orbital basis, auxiliary grid and SCF settings. Different meshes need not be nested, and monotonically decreasing energy differences are not assumed.

A band path joins high-symmetry points to visualize dispersion. Giving its points equal weights generally does not produce a Brillouin-zone quadrature. This example tests integrated energy and density; drawing a band path does not replace k-point convergence.

$$
\frac{1}{|\mathrm{BZ}|}\int_{\mathrm{BZ}}f(\mathbf k)\,d\mathbf k\simeq\sum_{q=1}^{N_k}w_qf(\mathbf k_q),\qquad\sum_qw_q=1,\qquad n(\mathbf r)=2\sum_qw_q\sum_{n\in\mathrm{occ}}|\psi_{n\mathbf k_q}(\mathbf r)|^2
$$

$$
\boldsymbol\kappa_{\mathbf j}=\left(\frac{j_1}{N_1},\frac{j_2}{N_2},\frac{j_3}{N_3}\right)\bmod\mathbb Z^3,\quad j_i=0,\ldots,N_i-1,\quad w_{\mathbf j}=\frac{1}{N_1N_2N_3}
$$

## The orbital basis and auxiliary FFT grid are separate convergence axes

The PySCF orbitals expand Bloch sums of Gaussian functions. Results retain basis names such as gth-dzv, the actual function count and overlap conditioning. Increasing a basis’s zeta label does not prove a complete-basis limit; bases with different contractions and polarization functions are not necessarily mathematically nested. Basis differences measure sensitivity within the published finite sequence.

FFT density fitting (FFTDF) is an auxiliary plane-wave/FFT representation used for quantities such as density and Coulomb potentials. Refining its mesh does not enlarge the Gaussian orbital space. Conversely, enlarging only the orbital basis cannot remove errors from a coarse auxiliary grid. The PySCF auxiliary grid, DFTK orbital plane-wave cutoff and its associated density grid are distinct, and hartree must not be confused with rydberg.

The periodic Coulomb G=0 component is handled with a convention combining electrons, the local pseudopotential and periodic ionic terms. A change in the mean potential also shifts the orbital eigenvalue origin. Even the same physical model needs aligned G=0 constants, pseudopotential corrections, Ewald terms and per-cell versus per-atom units for direct total-energy comparison. Conventions and energy components are checked rather than adding an empirical constant to force agreement.

$$
\chi_{\mu\mathbf k}(\mathbf r)=\sum_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}\chi_\mu(\mathbf r-\mathbf R),\qquad\psi_{n\mathbf k}=\sum_\mu C_{\mu n}(\mathbf k)\chi_{\mu\mathbf k}
$$

$$
\Delta_kE,\qquad\Delta_{\mathrm{orbital\ basis}}E,\qquad\Delta_{\mathrm{auxiliary\ grid}}E,\qquad E_{\tau}-E_{\mathrm{tight}},\qquad E_{\mathrm{PySCF}}-E_{\mathrm{DFTK}}
$$

## SCF residuals, electron count and a sampled KS gap

The Kohn–Sham potential depends on density, so an eigenproblem and density update are iterated. Energy changes are supplemented by a commutator residual built from the final density, orbital-equation residuals, orthogonality and electron count. The commutator measure is the maximum over k points of the Frobenius norm of X(FPS−SPF)X, with symmetric orthogonalization X=S⁻¹ᐟ². Orbital residuals use the same final-density F. Results retain iteration histories, stopping reasons and tolerances. Reaching an iteration cap is not labeled convergence.

A tolerance sweep changes only SCF settings at fixed discretization and measures the energy difference from a tight solution. This checks the remaining nonlinear solution error. SCF convergence is separate from sufficient orbital bases, auxiliary grids and k points, and from physical-model accuracy.

For closed-shell occupations, a sampled KS gap is obtained from the largest occupied and smallest unoccupied eigenvalues over all calculated k points. A positive value indicates separated occupations on that mesh. It neither guarantees the true minimum over the full Brillouin zone nor equals the many-body fundamental gap defined by adding/removing an electron or an experimental optical gap. Unoccupied states also depend on the orbital basis. A visible difference remains between the Gaussian and plane-wave sampled gaps in this example. The independent comparison validates total energies; gap convergence or agreement is not established.

$$
F_{\mathbf k}C_{\mathbf k}=S_{\mathbf k}C_{\mathbf k}\varepsilon_{\mathbf k},\qquad C_{\mathbf k}^{\dagger}S_{\mathbf k}C_{\mathbf k}=I,\qquad\sum_qw_q\operatorname{Tr}(P_{\mathbf k_q}S_{\mathbf k_q})=N_e=2
$$

$$
E_{g,\mathcal K}^{\mathrm{KS}}=\min_{\mathbf k\in\mathcal K,n\in\mathrm{unocc}}\varepsilon_{n\mathbf k}-\max_{\mathbf k\in\mathcal K,n\in\mathrm{occ}}\varepsilon_{n\mathbf k}
$$

## Comparison with an independent DFTK reference in a different basis

The example uses PySCF’s periodic integrals, FFTDF and SCF. The independent Julia package DFTK supplies a plane-wave Kohn–Sham reference without calling the teaching PySCF solver. Merely changing an auxiliary representation within PySCF would not be an independent-implementation comparison. Both engines use Libxc for exchange-correlation evaluation, so that component is not independently implemented in this comparison.

The lattice, atomic positions, valence count, spin, pseudopotential coefficients, LDA_X plus LDA_C_VWN, fractional k points and weights are aligned. Plane-wave cutoff and SCF convergence are checked on the DFTK side. Gaussian and plane-wave calculations use different finite spaces, so machine-precision agreement is not demanded between their finite-basis energies. Agreement is assessed against the published acceptance width alongside Gaussian-basis and auxiliary-grid sensitivities and reference-cutoff dependence. Meeting this width establishes neither a rigorous bound on true error nor chemical accuracy.

Ordinary reproduction against the saved reference and reference regeneration in Julia are separate operations. Input, reference and source hashes and dependency versions are fixed, and execution from an independently extracted ZIP is checked. The release exposes numerical differences, acceptance criteria and convergence sequences as well as the result JSON’s pass flag.

## First-principles MD: Born–Oppenheimer and Car–Parrinello methods

First-principles molecular dynamics (AIMD) moves nuclei using electronic-structure calculations. Born–Oppenheimer molecular dynamics (BOMD) converges the electronic ground state at each nuclear configuration, then integrates classical nuclear motion using forces on that energy surface. E_BO below includes ionic interactions. The 1927 Born–Oppenheimer paper is cited for electronic–nuclear separation, not as the publication of a modern BOMD program.

In BOMD, SCF tolerances must control forces and trajectory reproducibility as well as energies. Atom-centered finite Gaussian bases require force contributions from basis-position dependence (Pulay terms). Finite-difference force checks, timestep refinement and energy drift in unthermostatted NVE trajectories are separate tests. Predicting an electronic initial guess does not remove the requirement to optimize each configuration to adequate accuracy.

Car–Parrinello molecular dynamics (CPMD) propagates nuclear coordinates and electronic orbitals together through an extended Lagrangian. The fictitious orbital mass μ is a numerical parameter, rather than the physical electron mass. Lagrange multipliers Λ enforce orthonormality. The displayed convention uses a μ/2 orbital-velocity term at fixed cell and occupations. Generalization to periodic k sampling must consistently include weights and occupations in electronic terms.

CPMD orbital propagation does not represent real electronic excitations as in TDDFT. Electronic fictitious motion must remain separated in timescale from nuclear motion, keeping orbitals near the BO surface. Vary μ, timestep and orthogonality tolerance while monitoring fictitious kinetic energy and energy transfer to nuclei. Distinguish the ideal unthermostatted extended-system conserved energy E_ext from nuclear kinetic plus BO energy. These statements do not establish applicability to narrow-gap systems or metals.

This section is reading only. The fixed-He example validates static total energies and quadrature, basis, auxiliary-grid and SCF convergence. It does not execute or validate atomic forces, BOMD/CPMD trajectories, time integration or thermostatting. A future implementation should first compare multiatom forces with independent references, then test MD conservation and sensitivity to timestep, SCF tolerances and μ.

$$
E_{\mathrm{BO}}(\mathbf R)=\min_{\langle\psi_i|\psi_j\rangle=\delta_{ij}}E_{\mathrm{KS}}[\{\psi_i\};\mathbf R],\qquad M_I\ddot{\mathbf R}_I=\mathbf F_I=-\nabla_{\mathbf R_I}E_{\mathrm{BO}}(\mathbf R)
$$

$$
L_{\mathrm{CP}}=\frac12\sum_I M_I|\dot{\mathbf R}_I|^2+\frac{\mu}{2}\sum_i\langle\dot\psi_i|\dot\psi_i\rangle-E_{\mathrm{KS}}+\sum_{ij}\Lambda_{ij}\bigl(\langle\psi_i|\psi_j\rangle-\delta_{ij}\bigr)
$$

$$
\langle\psi_i|\psi_j\rangle=\delta_{ij},\qquad K_{\mathrm{fict}}=\frac{\mu}{2}\sum_i\langle\dot\psi_i|\dot\psi_i\rangle,\qquad E_{\mathrm{ext}}=\sum_I\frac{M_I}{2}|\dot{\mathbf R}_I|^2+E_{\mathrm{KS}}+K_{\mathrm{fict}}
$$

## Stored measurements

- max_reference_energy_error: 4.71162763809e-05
- max_scf_commutator: 3.48433764277e-07
- max_orbital_residual: 7.43065453612e-07
- max_electron_count_error: 4.4408920985e-16
- max_orthogonality_error: 4.86132023525e-10
- max_energy_reconstruction_error: 0
- min_sampled_ks_gap: 0.656519700269
- max_overlap_condition: 508833030.474
- min_overlap_eigenvalue: 4.14810500792e-09
- max_tight_scf_commutator: 1.00490076615e-08
- kpoint_last_change: 0.000525013074401
- basis_last_change: 3.34202303871e-05
- auxiliary_last_change: 2.52654341004e-07
- scf_last_change: 1.86517468137e-14

https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json

## Execution

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en

## Sources

- Felix Bloch (1929). Über die Quantenmechanik der Elektronen in Kristallgittern. https://link.springer.com/article/10.1007/BF01339455 — Publisher bibliography and abstract consulted, distinguishing receipt in 1928 from publication in 1929. No full-paper reproduction or audit claimed.
- P. Hohenberg and W. Kohn (1964). Inhomogeneous Electron Gas. https://doi.org/10.1103/PhysRev.136.B864 — Original bibliography and DOI checked against the existing Atlas. Cited for the theoretical foundation, not as a proof of the theorem by this finite-basis calculation.
- W. Kohn and L. J. Sham (1965). Self-Consistent Equations Including Exchange and Correlation Effects. https://doi.org/10.1103/PhysRev.140.A1133 — Original bibliography and DOI checked against the existing Atlas. Cited as the Kohn–Sham source without claiming numerical reproduction of the entire paper.
- H. J. Monkhorst and J. D. Pack (1976). Special points for Brillouin-zone integrations. https://doi.org/10.1103/PhysRevB.13.5188 — Original bibliography and DOI checked against the existing Atlas. The example’s Γ-containing mesh convention is specified in the text/input rather than equated with every mesh in the paper.
- S. H. Vosko, L. Wilk and M. Nusair (1980). Accurate spin-dependent electron liquid correlation energies for local spin density calculations: a critical analysis. https://doi.org/10.1139/p80-159 — Original DOI and bibliography checked through official Libxc documentation identifying LDA_C_VWN as VWN5. Publisher text was inaccessible; no full-text or table audit was performed.
- S. Goedecker, M. Teter and J. Hutter (1996). Separable dual-space Gaussian pseudopotentials. https://journals.aps.org/prb/abstract/10.1103/PhysRevB.54.1703 — Publisher bibliography and abstract consulted. Actual He coefficients are aligned through the packaged data and libraries, not presented as a full-precision transcription from the paper’s tables.
- Qiming Sun et al. (2020). Recent developments in the PySCF program package. https://doi.org/10.1063/5.0006074 — Publisher bibliography/abstract and the existing Atlas entry consulted. The periodic APIs used here are additionally checked against official documentation and pinned code.
- M. F. Herbst, A. Levitt and E. Cancès (2021). DFTK: A Julian approach for simulating electrons in solids. https://proceedings.juliacon.org/papers/10.21105/jcon.00069 — Publisher bibliography and the introduction of the open paper consulted. The reference calculation is a separate numerical check, not a reproduction of all paper examples.
- PySCF developers (2026). Crystal structure. https://pyscf.org/user/pbcgto.html — Relevant sections on lattice vectors, units, GTH basis/pseudopotential pairing and k-point generation consulted; distinct from an original-method publication.
- PySCF developers (2026). Periodic SCF and density fitting. https://pyscf.org/user/pbc/scf.html — Relevant sections on periodic SCF, DFT, FFTDF, cutoffs and Coulomb-divergence handling consulted.
- DFTK developers (2026). DFTK API and pseudopotentials. https://docs.dftk.org/stable/api/ — Relevant lattice, k-point, functional and SCF APIs and the official pseudopotential discussion consulted. The release separately pins the versions actually executed.
- Libxc developers (2026). Libxc functionals: LDA_X and LDA_C_VWN. https://libxc.gitlab.io/functionals/ — Identities and original-source links for LDA_X (id 1) and LDA_C_VWN (id 7, VWN5) checked. Identified as an evaluation library shared by both engines.
- M. Born and R. Oppenheimer (1927). Zur Quantentheorie der Molekeln. https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002 — Publisher bibliography and DOI checked. Cited for the historical basis of Born–Oppenheimer separation, without claiming a full-text audit or reproduction of a modern MD implementation.
- R. Car and M. Parrinello (1985). Unified Approach for Molecular Dynamics and Density-Functional Theory. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471 — Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.
- Quantum ESPRESSO developers (2026). cp.x input description: electron dynamics, emass and orthogonalization. https://www.quantum-espresso.org/Doc/INPUT_CP.html — Selected input entries on fictitious mass, electronic/ionic dynamics, timestep, orthogonalization and adiabaticity consulted. No execution of the software is claimed.
