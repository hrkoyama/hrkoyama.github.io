# Closed-shell HF for H₂: independent references, SCF residuals and basis refinement

Solve two-electron H₂ at fixed proton positions using original s-Gaussian integrals and restricted closed-shell Hartree–Fock (RHF). Energy stabilization, satisfaction of the discrete SCF equations, changes under basis expansion and physical accuracy are separate questions.

## The model being solved

This is a Born–Oppenheimer electronic problem with the internuclear distance R fixed by the input. Atomic units are used: distances in bohr and energies in hartree. Relativistic effects, nuclear motion, vibration/rotation, solvent and periodic boundaries are excluded. Total energy including nuclear repulsion 1/R is recorded separately from electronic energy.

The two electrons occupy the same spatial orbital with opposite spins in closed-shell RHF. The same restriction is retained at stretched geometries. SCF convergence and agreement with another implementation do not establish the correct dissociation limit or recover electron correlation. This is not a switch to UHF, configuration interaction or DFT.

$$
\hat H_{\mathrm{el}}=\sum_{i=1}^{2}\left[-\tfrac12\nabla_i^2-\sum_{A=1}^{2}\frac{1}{|\mathbf r_i-\mathbf R_A|}\right]+\frac{1}{r_{12}},\qquad E_{\mathrm{tot}}=E_{\mathrm{el}}+\frac1R
$$

## Gaussian basis functions and original integrals

Normalized s-type Gaussians centered on the two nuclei form the basis. A contracted function combines several exponents and coefficients, with normalization also applied to the contraction. Three primitives in STO-3G describe one contracted s function, not three independent basis functions. Inputs and results retain exponents, coefficients and contractions. The STO-3G numerical convention is checked against Basis Set Exchange version 1, rather than presented as a direct transcription of the original paper’s printed digits.

The educational code computes overlap S, kinetic T, nuclear attraction V and electron-repulsion integrals, defining the one-electron matrix as h=T+V. The s-type Coulomb integrals involve the Boys function F₀, which tends to 1 as t approaches zero. Direct evaluation of erf(√t)/√t at zero would produce 0/0, so the limiting region needs a stable treatment. The chemists’ integral index convention and spin-summed density P determine the factor 1/2 in exchange.

$$
g_{\alpha A}(\mathbf r)=\left(\frac{2\alpha}{\pi}\right)^{3/4}e^{-\alpha|\mathbf r-\mathbf R_A|^2},\quad \chi_\mu=\sum_p d_{\mu p}g_{\alpha_{\mu p}A_\mu},\quad F_0(t)=\int_0^1e^{-tu^2}\,du
$$

$$
P_{\mu\nu}=2\sum_{i\in\mathrm{occ}} C_{\mu i}C_{\nu i},\quad F_{\mu\nu}=h_{\mu\nu}+\sum_{\lambda\sigma}P_{\lambda\sigma}\left[(\mu\nu|\lambda\sigma)-\tfrac12(\mu\lambda|\nu\sigma)\right]
$$

## How SCF convergence is judged

Symmetric orthogonalization converts the Roothaan equation to an ordinary eigenproblem. Occupied orbitals define a new density, which rebuilds the Fock matrix for the next iteration. Density mixing can stabilize iterations, but an intermediate mixed density need not satisfy the idempotency condition of a pure determinant. Final density, orbitals and Fock matrix are therefore checked in a consistent state.

A small energy change alone is insufficient. Energy change, the Frobenius norm of the AO-density change and the Frobenius norm of the orthonormal-coordinate commutator residual are compared with input thresholds. Orbital orthogonality, electron count Tr(PS)=2 and closed-shell idempotency PSP=2P are also measured. The matrix-trace energy with F[P] rebuilt from the final density is compared with a separate occupied-orbital/electron-repulsion-integral reconstruction.

The minimum overlap eigenvalue and condition number are recorded. Near-linear dependence makes S⁻¹ᐟ² amplify errors. Termination reasons and iteration limits are explicit; reaching the limit is not reported as convergence. A stationary solution also need not be a stable minimum, so residual checks do not replace a full RHF/UHF stability analysis.

$$
FC=SC\varepsilon,\qquad C^{\mathsf T}SC=I,\qquad X=S^{-1/2},\qquad XFX\widetilde C=\widetilde C\varepsilon,\quad C=X\widetilde C
$$

$$
E_{\mathrm{tot}}[P]=\frac12\sum_{\mu\nu}P_{\mu\nu}\bigl(h_{\mu\nu}+F_{\mu\nu}[P]\bigr)+\frac1R
$$

$$
\mathcal R=X(FPS-SPF)X,\qquad \operatorname{Tr}(PS)=2,\qquad PSP=2P
$$

## Basis refinement and its limits

SCF tolerance controls the remaining solution error within one fixed basis. A basis change changes the discrete problem itself. Basis comparisons retain tight SCF settings, geometry, nuclear repulsion and the RHF constraint. True RHF minima in nested variational spaces cannot increase in energy under expansion. Switching to a different local stationary branch would invalidate that simple comparison.

Refinement here is limited to the finite s-only sequence defined by the public input. Adjacent-basis energy changes are measured, but the absence of p and higher angular functions means this does not prove convergence to the complete-basis-set (CBS) limit or chemical accuracy. Unrelated basis sets and different contractions are not all treated as a nested sequence. For each separation, the final two additions are checked against the stated energy-change target. This is a stopping diagnostic for the published sequence, not an upper bound on true basis error.

The tolerance sweep changes only SCF thresholds and compares with a tighter solution. The basis sweep keeps SCF settings aligned. These differences and independent-implementation differences are separate outputs. A small final basis increment does not eliminate physical approximation error.

$$
V_n\subseteq V_{n+1}\ \Longrightarrow\ E_{n+1}^{\mathrm{RHF,min}}\le E_n^{\mathrm{RHF,min}},\qquad \Delta E_n=|E_{n+1}-E_n|
$$

$$
\underbrace{E_{n,\tau}-E_{n,\mathrm{tight}}}_{\text{SCF tolerance effect}},\qquad\underbrace{E_{n+1,\mathrm{tight}}-E_{n,\mathrm{tight}}}_{\text{basis-space change}},\qquad\underbrace{E_{n,\mathrm{tight}}-E_{n,\mathrm{PySCF}}}_{\text{independent-implementation difference}}
$$

## Independent reference and reproduction

The reference script supplies the same geometry, charge, spin and explicit Gaussian basis to PySCF, using its independent integral library and SCF procedure for RHF energies. It does not call the educational integral, Fock or SCF functions. Both calculations solve the same physical model in the same finite basis; the comparison is not against an exact correlated energy.

The release records input/reference hashes, dependency versions, total energies, reference differences, iteration histories and termination reasons. Extract the ZIP into another directory and run the same fixed input, checking residual/error values against criteria as well as the JSON pass flag. Regenerating the independent reference is separate from ordinary reruns using the saved reference.

## Stored measurements

- max_reference_energy_error: 2.53130849615e-14
- max_scf_commutator: 9.13387953717e-11
- max_orbital_residual: 5.00061911168e-11
- max_orthogonality_error: 3.697042672e-14
- max_electron_count_error: 3.10862446895e-15
- max_energy_consistency_error: 2.22044604925e-15
- max_idempotency_error: 1.77828610609e-15
- basis_energy_increase_max: 0
- last_basis_energy_change_max: 0.000355298306571
- last_two_basis_changes_max: 0.000355298306571
- scf_tolerance_energy_error_max: 2.1869092981e-07
- scf_tolerance_errors: [2.1869092980963956e-07, 6.483702463810914e-14, 0.0]
- max_overlap_condition_number: 3534.73030868

https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json

## Execution

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en

## Sources

- Boys, S. F. (1950). Electronic wave functions - I. A general method of calculation for the stationary states of any molecular system. https://doi.org/10.1098/rspa.1950.0036 — Original bibliographic identity and DOI checked against the existing Atlas. This implementation does not claim a full-paper reproduction or audit.
- Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. https://doi.org/10.1103/RevModPhys.23.69 — Original bibliographic identity and DOI checked against the existing Atlas. This implementation does not claim a full-paper reproduction or audit.
- C. A. Coulson and I. Fischer (1949). XXXIV. Notes on the molecular orbital treatment of the hydrogen molecule. https://doi.org/10.1080/14786444908521726 — Bibliographic identity and DOI checked as a historical source on molecular-orbital treatment and dissociation constraints; no full-text audit claimed.
- Qiming Sun et al. (2020). Recent developments in the PySCF program package. https://doi.org/10.1063/5.0006074 — Publisher bibliography/abstract and author-institution record consulted. Executing the reference code is a separate numerical check.
- PySCF developers (2026). Self-consistent field (SCF) methods. https://pyscf.org/user/scf.html — Relevant official documentation sections on SCF equations, convergence, stability and linear dependence consulted; distinct from an original-method paper.
- W. J. Hehre, R. F. Stewart and J. A. Pople (1969). Self-Consistent Molecular-Orbital Methods. I. Use of Gaussian Expansions of Slater-Type Atomic Orbitals. https://doi.org/10.1063/1.1672392 — Publisher-deposited bibliographic metadata and DOI checked. Cited as the STO-nG source, not as a claim that every coefficient digit was transcribed from this paper. No full-text audit performed.
- Basis Set Exchange (2018). STO-3G version 1: hydrogen basis data. https://www.basissetexchange.org/basis/sto-3g/format/json/?elements=1%2C2&version=1 — Hydrogen exponents and coefficients in official API version 1 checked against the input. The numerical convention is BSE v1 with Gaussian-derived precision, not a reproduction of the printed digits in the 1969 paper.
