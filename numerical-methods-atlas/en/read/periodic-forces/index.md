# From DFT to atomic forces: finite differences, independent references, force convergence and the BOMD interface

Atomic forces are obtained as position derivatives of the total energy in a multiatom periodic He cell. Analytic gradients, finite differences of energies and an independent plane-wave calculation are compared, separating orbital-basis, k-point, auxiliary-grid and SCF effects on forces. The requirements for a BOMD force interface are distinguished from the additional validation of trajectories.

This educational verification uses a fixed cell, a local He GTH potential and spin-unpolarized LDA. It is an execution and validation driver using PySCF analytic nuclear gradients, rather than a new electronic-structure engine. Agreement for this configuration does not validate other elements, nonlocal pseudopotentials, stress, long BOMD trajectories or thermostats.

## Forces are negative gradients of the total energy

For a fixed lattice, electron count, functional and pseudopotential, the electronic ground state is solved at each atomic configuration. The Born–Oppenheimer energy is the total cell energy, including electronic and periodic ion–ion terms. The force on Cartesian component α of atom I is minus the total derivative with respect to that coordinate. Gradient and force signs must be distinguished: coordinates in bohr and energies in hartree give forces in hartree/bohr.

The input is a cubic cell of side 5 bohr with He positions (0.37, 0.61, 0.83) and (2.13, 2.27, 2.41) bohr: four valence electrons in a closed-shell fixed configuration. It avoids a check in which symmetry makes every force zero. Directions and all x, y and z components are compared, as well as magnitudes. Numerical agreement for this artificial arrangement does not predict an equilibrium helium crystal or establish chemical accuracy. Stress and pressure require cell derivatives, separate from atomic-position derivatives at fixed cell.

$$
E_{\mathrm{BO}}(\mathbf R;A)=\min_{\langle\psi_i|\psi_j\rangle=\delta_{ij}}E_{\mathrm{KS}}[\{\psi_i\};\mathbf R,A]
$$

$$
F_{I\alpha}=-\left.\frac{d E_{\mathrm{BO}}}{dR_{I\alpha}}\right|_{A,N_e},\qquad [F_{I\alpha}]=E_h/a_0
$$

## The Hellmann–Feynman theorem and Pulay terms from moving bases

For a normalized exact eigenstate, the energy derivative with respect to a parameter equals the expectation of the Hamiltonian derivative. This is the Hellmann–Feynman relation. Feynman’s 1939 paper is a historical primary source for evaluating molecular forces directly. The theorem alone does not make every force correct for an electronic state represented in a finite atom-centered basis. The H and Ψ below express the general theorem; they do not replace the Kohn–Sham total energy by a sum of orbital eigenvalues.

A Gaussian basis moving with the atoms changes its functions and overlap matrix when nuclei move. Even with variationally optimized orbital coefficients, derivatives of this basis dependence must be included when differentiating the discrete energy. These are Pulay terms. The overlap derivative contracted with an energy-weighted density in the generalized eigenproblem is one contribution. The driver uses PySCF analytic nuclear gradients; it does not substitute a bare electron–ion Coulomb force.

At fixed cell and cutoff, plane waves do not move with atomic positions. Finite-cutoff force errors nevertheless remain, and SCF and density-grid errors must still be controlled. The absence of moving-atom basis terms does not make plane-wave forces exact. Basis changes under cell deformation and Pulay stress are distinct from this fixed-cell test.

$$
H(\lambda)\Psi=E(\lambda)\Psi,\quad\langle\Psi|\Psi\rangle=1\quad\Longrightarrow\quad\frac{dE}{d\lambda}=\left\langle\Psi\left|\frac{\partial H}{\partial\lambda}\right|\Psi\right\rangle
$$

$$
F_{\mathbf k}C_{\mathbf k}=S_{\mathbf k}C_{\mathbf k}\varepsilon_{\mathbf k},\quad W_{\mathbf k}=C_{\mathbf k}f_{\mathbf k}\varepsilon_{\mathbf k}C_{\mathbf k}^{\dagger},\quad \left.\frac{dE}{dR_{I\alpha}}\right|_{\text{overlap term}}=-\sum_qw_q\operatorname{Tr}\!\left(W_{\mathbf k_q}\frac{\partial S_{\mathbf k_q}}{\partial R_{I\alpha}}\right)
$$

## Finite-difference checks: smaller displacements are not always better

One Cartesian component of one atom is displaced by ±h from the baseline configuration. At each displaced geometry the SCF is converged independently, and the resulting total energies give a central-difference force. The lattice, k points and weights, basis name, FFT grid, functional, pseudopotential and electron count are aligned. The atom-centered basis moves too, so this probes derivatives of the same discrete energy including basis-position dependence.

For a smooth energy surface, central-difference truncation is O(h²). SCF solution and roundoff errors in energies are divided by 2h, so very small displacements can increase errors. Several h values are retained to locate a stable agreement range with analytic forces. A clean U-shaped measured curve is not assumed. An input SCF energy tolerance is not interpreted as a rigorous bound on the error of each energy.

Agreement with finite differences from the same engine checks internal consistency, including signs, components and basis derivatives. Both use shared functional and pseudopotential implementations, so this alone is not an independent physical reference. A separate plane-wave DFTK implementation provides the independent comparison here.

$$
F^{\mathrm{FD}}_{I\alpha}(h)=-\frac{E(\mathbf R+h\mathbf e_{I\alpha})-E(\mathbf R-h\mathbf e_{I\alpha})}{2h}
$$

$$
F^{\mathrm{FD}}(h)-F=\mathcal O(h^2)+\mathcal O(\delta E/h)
$$

## Converge basis, k points, auxiliary grids and SCF for forces separately

A small energy change alone does not establish converged forces. The Gaussian orbital basis, Brillouin-zone mesh, auxiliary FFT grid and SCF stopping conditions are varied one at a time, comparing forces on the same atoms and Cartesian components. Atom ordering and axes are fixed. Summaries use an L∞-type maximum absolute component norm, distinct from a per-atom vector magnitude or a component average.

Increasing a basis’s zeta label does not necessarily produce nested spaces or monotonic force changes. Nor are all k meshes nested. The final pair of settings is compared with a published target, without presenting the increment as a rigorous complete-basis or infinite-k-point error bound. The auxiliary FFT representation of density and local potentials is a separate convergence axis from the Gaussian orbital space.

Incomplete SCF convergence also affects forces. Alongside termination flags and iteration counts, inspect stored electron-count, orbital and SCF residual diagnostics. Force sensitivity to tighter stopping conditions is measured directly, and an unconverged electronic state must not be returned to BOMD as an accepted force.

Each sweep varies one control while holding the finite basis, grid and k mesh specified in the input fixed. Basis sequences are checked separately at Γ and 2³, but no joint calculation combines 4³ sampling, the largest Gaussian basis and the finest FFT grid. Independent-reference agreement applies only to the designated Γ and 2³ cases.

$$
\|\Delta\mathbf F\|_{\infty}=\max_{I,\alpha\in\{x,y,z\}}|F^{(a)}_{I\alpha}-F^{(b)}_{I\alpha}|
$$

$$
\Delta_{\mathrm{basis}}\mathbf F,\quad\Delta_{\mathbf k}\mathbf F,\quad\Delta_{\mathrm{FFT}}\mathbf F,\quad\mathbf F_{\tau}-\mathbf F_{\mathrm{tight}}
$$

## Independent reference: the same model in a different discretization

PySCF uses a periodic Gaussian basis and FFTDF; the reference uses DFTK’s plane-wave Hamiltonian, SCF, periodic ion interactions and analytic forces. Lattice and all atomic positions, valence count, spin restriction and integer occupations, every local-GTH coefficient, Libxc LDA_X plus LDA_C_VWN (VWN5), fractional k points and weights are matched. No fitted energy offset or force correction is applied.

The DFTK plane-wave cutoff is increased separately and its final force increment is measured. This is not a rounding-error comparison of identical finite matrices. Different finite Gaussian and plane-wave spaces are assessed using the published acceptance width and convergence diagnostics on both sides. Both engines share Libxc, which limits the extent of implementation independence.

DFTK compute_forces returns a representation associated with fractional coordinates; the Cartesian API is compute_forces_cart. Coordinate and force transformations are different. Comparisons here use Cartesian components in hartree/bohr throughout. The generation script, pinned Julia environment, pseudopotential, input and result hashes are retained. Comparing against the saved reference in Python and regenerating the reference in Julia are distinct operations.

$$
\mathbf R=A\boldsymbol\xi,\qquad \mathbf F_{\mathrm{cart}}=-A^{-\mathsf T}\nabla_{\boldsymbol\xi}E
$$

## Check components, translation and nonzero forces

A configuration with nearly zero forces can pass even with a sign error. A multiatom configuration carrying nonzero forces is used, with componentwise comparisons of analytic forces, finite differences and the independent reference. A single force norm should not hide component permutations, atom-order mistakes or incorrect units.

In an ideal periodic system without external fields, uniform translation leaves the total energy unchanged and the sum of atomic forces vanishes. Finite real-space grids can numerically break this property; the remaining total force is a useful grid and differentiation diagnostic. Translation checks alone do not establish accurate relative forces, so energy differences and an independent reference are used alongside them.

$$
E(\{\mathbf R_I+\mathbf t\})=E(\{\mathbf R_I\})\quad\Longrightarrow\quad\sum_I\mathbf F_I=\mathbf 0
$$

## The BOMD interface and additional trajectory validation

The BOMD force provider energy_and_forces accepts positions_bohr and returns energy_per_cell and forces_cartesian from the same energy surface, together with SCF convergence and residual diagnostics. An unconverged electronic state is treated as a failure. Masses belong to nuclear time integration, not as factors multiplying the DFT potential energy or forces. Wrapped positions inside a periodic cell must be distinguished from a continuous trajectory record.

Velocity Verlet advances velocities by half a step, updates positions, solves the electronic problem again for the new forces, then completes the velocity update. Carrying an electronic guess from a previous step accelerates the calculation but does not replace SCF convergence. This verification focuses on atomic forces and the BOMD handoff; a single force evaluation or short interface smoke test is not counted as validation of long trajectories.

Accepting a practical trajectory additionally requires timestep refinement, tighter-SCF comparisons, total-energy and momentum checks in unthermostatted NVE, and time-reversal checks where appropriate. Thermostats can hide force or integration errors by absorbing energy changes, so unthermostatted checks come first. Small short-time drift does not guarantee long-time stability or a correct statistical distribution.

Car–Parrinello dynamics is a distinct formulation propagating fictitious electronic degrees of freedom alongside nuclei. A force provider on the Born–Oppenheimer surface is not a CPMD implementation. The cross-field navigation separately shows the executed scope of DFT, force evaluation, nuclear integration and temperature control.

$$
\mathbf v_{n+1/2}=\mathbf v_n+\frac{\Delta t}{2M}\mathbf F(\mathbf R_n),\quad\mathbf R_{n+1}=\mathbf R_n+\Delta t\,\mathbf v_{n+1/2},\quad\mathbf v_{n+1}=\mathbf v_{n+1/2}+\frac{\Delta t}{2M}\mathbf F(\mathbf R_{n+1})
$$

$$
\mathcal E_n=E_{\mathrm{BO}}(\mathbf R_n)+\sum_I\frac{M_I}{2}|\mathbf v_{I,n}|^2,\qquad \Delta\mathcal E_n=\mathcal E_n-\mathcal E_0
$$

## Stored measurements

- max_reference_force_error: 7.53824989575e-05
- max_reference_energy_error: 0.000171684168107
- finite_difference_max_error: 2.32234127207e-08
- finite_difference_scan_max_error: 1.8023756336e-07
- max_tight_scf_commutator: 3.04623403924e-09
- max_scf_commutator: 2.94441763031e-06
- max_electron_count_error: 2.6645352591e-15
- max_orthogonality_error: 4.93782792432e-11
- max_energy_reconstruction_error: 0
- min_sampled_ks_gap: 0.559054051286
- max_overlap_condition: 413148.516377
- finest_net_force: 3.18720265458e-09
- bomd_position_step_difference: 9.60193803634e-07
- bomd_full_step_energy_defect: 3.78557850844e-07
- bomd_two_half_steps_energy_defect: 9.46016402992e-08
- reference_cutoff_force_change: 1.69522172031e-06
- reference_finite_difference_max_error: 2.43217217838e-07
- kpoint_last_change: 2.84334958952e-05
- basis_last_change: 2.65239291374e-06
- basis-k2_last_change: 3.55179947748e-05
- auxiliary_last_change: 1.30328608255e-06
- scf_last_change: 5.64949656501e-10

https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/result.json

## Execution

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en

## Sources

- S. Goedecker, M. Teter and J. Hutter (1996). Separable dual-space Gaussian pseudopotentials. https://journals.aps.org/prb/abstract/10.1103/PhysRevB.54.1703 — Publisher bibliography and abstract consulted. Actual He coefficients are aligned through the packaged data and libraries, not presented as a full-precision transcription from the paper’s tables.
- S. H. Vosko, L. Wilk and M. Nusair (1980). Accurate spin-dependent electron liquid correlation energies for local spin density calculations: a critical analysis. https://doi.org/10.1139/p80-159 — Original DOI and bibliography checked through official Libxc documentation identifying LDA_C_VWN as VWN5. Publisher text was inaccessible; no full-text or table audit was performed.
- Qiming Sun et al. (2020). Recent developments in the PySCF program package. https://doi.org/10.1063/5.0006074 — Publisher bibliography/abstract and the existing Atlas entry consulted. The periodic APIs used here are additionally checked against official documentation and pinned code.
- M. F. Herbst, A. Levitt and E. Cancès (2021). DFTK: A Julian approach for simulating electrons in solids. https://proceedings.juliacon.org/papers/10.21105/jcon.00069 — Publisher bibliography and the introduction of the open paper consulted. The reference calculation is a separate numerical check, not a reproduction of all paper examples.
- DFTK developers (2026). DFTK API and pseudopotentials. https://docs.dftk.org/stable/api/ — Selected API descriptions of compute_forces, compute_forces_cart, coordinates, units and derivatives of discrete energies consulted. Reference generation uses the packaged pinned DFTK environment, whose source is also checked.
- M. Born and R. Oppenheimer (1927). Zur Quantentheorie der Molekeln. https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002 — Publisher bibliography and DOI checked. Cited for the historical basis of Born–Oppenheimer separation, without claiming a full-text audit or reproduction of a modern MD implementation.
- R. Car and M. Parrinello (1985). Unified Approach for Molecular Dynamics and Density-Functional Theory. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471 — Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.
- R. P. Feynman (1939). Forces in Molecules. https://journals.aps.org/pr/abstract/10.1103/PhysRev.56.340 — Publisher bibliography and abstract consulted. Cited as a historical primary source for the Hellmann–Feynman force relation, not as sole validation of finite-basis or pseudopotential gradient implementations.
- P. Pulay (1969). Ab initio calculation of force constants and equilibrium geometries in polyatomic molecules. I. Theory. https://www.tandfonline.com/doi/abs/10.1080/00268976900100941 — Publisher-page bibliography and abstract returned by the search tool consulted; opening the page returned HTTP 403. Cited for finite position-dependent basis derivatives, distinct from Pulay (1980) on DIIS. No full-text audit is claimed.
- PySCF developers (2026). pyscf.pbc.grad.krks: analytic nuclear gradients with k-point sampling. https://pyscf.org/_modules/pyscf/pbc/grad/krks.html — Official source documentation consulted for periodic KRKS analytic nuclear gradients, LDA XC derivatives and unsupported settings; executed calls are also checked in pinned PySCF 2.11.0.
- PySCF developers (2026). pyscf.pbc.grad.krhf: electronic, overlap, pseudopotential and nuclear gradient terms. https://pyscf.org/_modules/pyscf/pbc/grad/krhf.html — Relevant source sections for grad_elec, density and energy-weighted density, overlap derivatives, pseudopotential derivatives and periodic ionic terms consulted. Third-party source is not copied into the tutorial.
- PySCF developers (2026). Guidelines for PBC DFT Parameter Settings. https://pyscf.org/user/pbc/dft-settings.html — Selected discussion of FFTDF auxiliary plane waves, real-space grids and nuclear gradients consulted as implementation guidance distinguishing orbital-basis and auxiliary-grid convergence.
- J. M. Herbert and M. Head-Gordon (2005). Accelerated, energy-conserving Born–Oppenheimer molecular dynamics via Fock matrix extrapolation. https://pubs.rsc.org/en/content/articlelanding/2005/cp/b509494a — Publisher-page bibliography and abstract returned by the search tool consulted; opening the page returned HTTP 403. Used to distinguish SCF solution error, electronic guesses, forces and NVE drift; the paper’s extrapolation method and trajectories are not claimed as implemented or reproduced.
