# Yee finite-difference time-domain method

Yee FDTD: implemented periodic plane-wave and PEC-cavity checks

This original educational implementation evolves 2D TMz fields (Ez, Hx, Hy) in dimensionless homogeneous vacuum without current or charge sources. Periodic plane waves and a rectangular perfect-electric-conductor (PEC) cavity are compared with continuum analytic solutions. Grid refinement, numerical dispersion, a discrete invariant and an approximation to physical energy are measured separately.

Model, units and scope


$$
\partial_t E_z=\partial_xH_y-\partial_yH_x,\qquad \partial_tH_x=-\partial_yE_z,\qquad \partial_tH_y=\partial_xE_z,\quad \epsilon=\mu=c=1.
$$
Length, time and fields are normalized so ε=μ=c=1. The rectangle has Lx=1 and Ly=1.5, with mode indices (m,l)=(1,1). An oblique periodic mode on a rectangular domain exercises both spatial derivatives and magnetic-field signs. Dispersive media, losses, dielectric interfaces and driven sources are outside this edition.

Yee placement and staggered time update


$$
\begin{aligned}H_{x,i,j+1/2}^{n+1/2}&=H_{x,i,j+1/2}^{n-1/2}-\frac{\Delta t}{\Delta y}(E_{i,j+1}^{n}-E_{i,j}^{n}),\\H_{y,i+1/2,j}^{n+1/2}&=H_{y,i+1/2,j}^{n-1/2}+\frac{\Delta t}{\Delta x}(E_{i+1,j}^{n}-E_{i,j}^{n}),\\E_{i,j}^{n+1}&=E_{i,j}^{n}+\Delta t\left(\frac{H_{y,i+1/2,j}^{n+1/2}-H_{y,i-1/2,j}^{n+1/2}}{\Delta x}-\frac{H_{x,i,j+1/2}^{n+1/2}-H_{x,i,j-1/2}^{n+1/2}}{\Delta y}\right).\end{aligned}
$$
Ez lives at nodes and integer times; Hx is displaced by half a y cell and Hy by half an x cell, both at half-integer times. Each step advances H first and then E. Initial E at time zero and H at −Δt/2 are sampled from analytic fields; assigning both fields time zero would introduce a first-order initialization error.

Periodic arrays omit duplicate endpoints and wrap differences. PEC walls fix tangential Ez=0 and update only interior electric nodes. Half weights for boundary magnetic samples make the weighted inner products compatible with discrete summation by parts and the energy identity.

Continuum periodic plane wave


$$
\begin{gathered}k_x=2\pi m/L_x,\quad k_y=2\pi l/L_y,\quad\omega=\sqrt{k_x^2+k_y^2},\quad\phi=k_xx+k_yy-\omega t,\\ E_z=\cos\phi,\quad H_x=(k_y/\omega)\cos\phi,\quad H_y=-(k_x/\omega)\cos\phi.\end{gathered}
$$
Evaluate the electric and both magnetic fields at their own spatial locations and times. Frequency supplies a phase-speed error separate from field error. A sampled continuum magnetic field need not have exactly zero discrete divergence, so the continuum-initialized run checks preservation of its initial divergence.

Continuum PEC cavity eigenmode


$$
\begin{gathered}k_x=m\pi/L_x,\quad k_y=l\pi/L_y,\quad\omega=\sqrt{k_x^2+k_y^2},\\E_z=\sin(k_xx)\sin(k_yy)\cos(\omega t),\\H_x=-\frac{k_y}{\omega}\sin(k_xx)\cos(k_yy)\sin(\omega t),\quad H_y=\frac{k_x}{\omega}\cos(k_xx)\sin(k_yy)\sin(\omega t).\end{gathered}
$$
This standing wave has Ez=0 on all four walls. It uses a different boundary implementation from the periodic wave, with checks of maximum wall electric field, eigenfrequency and field error. The cavity here is a z-invariant two-dimensional section; it does not cover the full three-dimensional cavity spectrum.

CFL condition and discrete dispersion


$$
\frac{\sin^2(\omega_h\Delta t/2)}{\Delta t^2}=\frac{\sin^2(k_x\Delta x/2)}{\Delta x^2}+\frac{\sin^2(k_y\Delta y/2)}{\Delta y^2},\qquad S=\Delta t\sqrt{\Delta x^{-2}+\Delta y^{-2}}The fixed input sets a Courant-number ceiling of 0.7; S≥1 is rejected. Rounding the required step count upward and choosing Δt from that count reaches the prescribed 1.1-period comparison time exactly, with actual S at or slightly below 0.7. Refining the grid also refines the time step, so measured orders describe coupled spatial and temporal refinement. They are not separate experimental estimates of spatial order and temporal order.

A three-time-level recurrence for evolved modal projection coefficients measures frequency. Its convergence toward continuum ω is separate from agreement with discrete ωh. Additional tests initialize magnetic amplitudes with the discrete wave numbers and check the exact discrete eigenmode to roundoff accuracy.

Discrete invariant versus physical energy


$$
\begin{aligned}U_*^n&=\frac12\lVert E^n\rVert_h^2+\frac12\langle H^{n-1/2},H^{n+1/2}\rangle_h=\mathrm{constant},\\\bar H^n&=(H^{n-1/2}+H^{n+1/2})/2,\\ U_{\rm sync}^n&=\tfrac12(\lVert E^n\rVert_h^2+\lVert\bar H^n\rVert_h^2),\\ U_*^n&=U_{\rm sync}^n-\frac{\Delta t^2}{8}\lVert\operatorname{curl}_h E^n\rVert_h^2.\end{aligned}
$$
Inner products include cell area and the appropriate PEC boundary weights. U*, containing magnetic fields from two different half times, is conserved up to roundoff in the closed periodic/PEC systems. The strict CFL inequality also ensures positivity of this modified energy. Usync, using magnetic fields averaged to an integer time, is a second-order approximation to physical energy but is not exactly invariant.

For unit-amplitude continuum fields the total energies are LxLy/2 for the traveling periodic wave and LxLy/8 for the cavity standing wave. Twelve periods are used to track relative U* drift and the variation of Usync; the error against the analytic physical energy must decrease at approximately second order under grid/time refinement. Tests also check U* conservation with compatible random fields, beyond single eigenmodes.

Fixed inputs and measured results


$$
e_h=\left(\frac{\lVert E_h-E\rVert_h^2+\lVert H_h-H\rVert_h^2}{\mathcal N^2}\right)^{1/2},\qquad p=\frac{\log(e_h/e_{h/2})}{\log 2}.
$$
Grids are 16×24, 32×48 and 64×96. Continuum field errors are evaluated exactly at the prescribed 1.1-period target, reached by adjusting the time step to an integer step count. H is compared at its actual half step before E. The combined-field denominator 𝒩² is the constant continuum modal norm (LxLy for the periodic wave, LxLy/4 for the cavity). Separate electric and magnetic errors are retained in JSON.

Fixed-input measurements. Field and frequency errors use continuum analytic solutions.CaseGrid Nx × NyRelative field L² errorObserved orderRelative frequency errorMaximum relative modified-energy driftPeriodic wave16 × 240.021645—0.00312712.22e-16Periodic wave32 × 480.00539262.00490.000779622.22e-16Periodic wave64 × 960.00133092.01860.000192442.22e-16PEC cavity16 × 240.0055511—0.000779624.441e-16PEC cavity32 × 480.00135142.03830.000192444.441e-16PEC cavity64 × 960.000333262.01974.7804e-052.22e-16Periodic plane wave · [JSON](/code/fdtd/2026-11-22/results/periodic-wave/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/periodic-wave/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/periodic-wave/energy.csv)PEC cavity · [JSON](/code/fdtd/2026-11-22/results/pec-cavity/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/pec-cavity/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/pec-cavity/energy.csv)Acceptance tolerances are saved in each fixed input. Separate checks require field error ≤0.01, observed orders ≥1.8, relative frequency error ≤0.002, discrete-dispersion identity error ≤10⁻⁹ and relative U* drift ≤2×10⁻¹¹. Separate checks require zero wall electric field, preservation of initial magnetic divergence, maximum Usync error against the analytic total energy ≤0.003, and approximately second-order refinement of that error. The Usync variation span is retained as a diagnostic.

Code, fixed inputs and reproduction

The immutable ZIP was extracted into an independent directory. All tests and both inputs were rerun without network access or the source checkout, reproducing saved numerical metrics and CSVs. This is a dedicated supplement, separate from the existing 22-example common execution registry and its historical receipts.

[Code, inputs and results ZIP](/code/fdtd/2026-11-22/fdtd-2026-11-22.zip)

[Bilingual setup and execution](/code/fdtd/2026-11-22/README.md)

[solver.py](/code/fdtd/2026-11-22/solver.py)

[run.py](/code/fdtd/2026-11-22/run.py)

[test_fdtd.py](/code/fdtd/2026-11-22/test_fdtd.py)

[File manifest / SHA-256](/code/fdtd/2026-11-22/source-manifest.json)

[24 tests passed / independent-extraction receipt](/code/fdtd/2026-11-22/verification.json)



Fixed input: periodic-wave

[inputs/periodic-wave.json](/code/fdtd/2026-11-22/inputs/periodic-wave.json) · [Numerical acceptance and results JSON](/code/fdtd/2026-11-22/results/periodic-wave/result.json) · [Field CSV](/code/fdtd/2026-11-22/results/periodic-wave/solution.csv)

Fixed input: pec-cavity

[inputs/pec-cavity.json](/code/fdtd/2026-11-22/inputs/pec-cavity.json) · [Numerical acceptance and results JSON](/code/fdtd/2026-11-22/results/pec-cavity/result.json) · [Field CSV](/code/fdtd/2026-11-22/results/pec-cavity/solution.csv)

python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py
python run.py --input inputs/periodic-wave.json --output output-periodic
python run.py --input inputs/pec-cavity.json --output output-cavityNonempty output directories are refused. Exit codes are 0 for accepted numerical checks, 1 for failed numerical checks and 2 for input/runtime errors. JSON records the input SHA-256, environment, error/refinement/invariant metrics, individual checks and termination reason. Original code uses the bundled MIT License; prose, figures and data follow the site’s item-specific terms.

## Publication scope

Educational fixed-input validation of 2D TMz homogeneous-vacuum periodic waves and a rectangular PEC cavity. References are continuum analytic solutions and separately derived discrete modes/invariants; no independent external FDTD-library comparison is claimed. PML, reflection/transmission, scatterers, charges/currents, dispersive media and general three-dimensional geometries remain unimplemented and unvalidated.

## Sources

- Kane Yee (1966). Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. https://doi.org/10.1109/tap.1966.1138693
- Fadime Bekmambetova and Xinyue Zhang and Piero Triverio (2017). A Dissipation Theory for Three-Dimensional FDTD with Application to Stability Analysis and Subgridding. https://arxiv.org/abs/1705.02274v2
