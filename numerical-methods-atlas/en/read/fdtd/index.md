# Yee finite-difference time-domain method

Yee FDTD: vacuum, dielectric interfaces and four-side/corner PML

Revision r3 extends the PML to all four sides and corners. Separate packets aimed at sides and obliquely at corners test boundary returns, directional PML work, four-edge energy flux and grid refinement. Both earlier editions and their four inputs are retained.

Revision r2 adds a dielectric interface and left/right x-directed PML to the original two vacuum cases. The first part covers vacuum analytic modes; the extension covers normal-incidence Fresnel comparisons and boundary reflections of normal/oblique packets. The original code edition, figures and measurements are retained.

This original educational implementation evolves 2D TMz fields (Ez, Hx, Hy) with original vacuum cases in dimensionless homogeneous vacuum without current or charge sources. The original periodic plane waves and rectangular perfect-electric-conductor (PEC) cavity are compared with continuum analytic solutions. Grid refinement, numerical dispersion, a discrete invariant and an approximation to physical energy are measured separately.

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

Dielectric interface: Fresnel amplitudes and energy


$$
\eta_j=\sqrt{\mu_j/\epsilon_j},\quad r=\frac{\eta_2-\eta_1}{\eta_2+\eta_1},\quad t=\frac{2\eta_2}{\eta_1+\eta_2},\qquad R=|r|^2,\quad T=\frac{\eta_1}{\eta_2}|t|^2,\quad R+T=1.
$$
A Gaussian packet is normally incident on a flat interface between nonmagnetic, lossless, nondispersive media ε₁=1 and ε₂=4, μ=1. The interface x=8 coincides with an electric node, assigned the arithmetic mean permittivity. This is a y-invariant reduction of 2D TMz. Analytic values are r=−1/3, t=2/3, R=1/9 and T=8/9.

The domain is 16×1, initial center x=4, width 0.5, comparison time t=8, with 160/320/640 x cells and 4 y cells. Incident, reflected and transmitted packets have separate continuum formulas; electric amplitudes are measured by projection. Packet-energy R,T are integrated using ε|E|² and magnetic fields, separately from simply squaring amplitudes. The shared interface-node quadrature weight is split between left and right regions.

Fixed-input interface comparison. R,T are packet-energy fractions.NxRelative field L² errorMeasured rMeasured tIntegrated RIntegrated T|R+T−1|1600.075366-0.329790.665410.108750.890350.00090293200.0184-0.332490.666750.110530.889220.000251836400.0045536-0.333120.666710.110960.888976.5291e-05Observed orders: field 2.0342, 2.0146; reflection-amplitude error 2.0682, 2.0162; transmission-amplitude error 3.9033, 0.91765; energy closure 1.8421, 1.9475. Leading-error cancellation affects transmission amplitude; every metric is not claimed to exhibit the same second order on every pair.

Left/right x-PML: normal and oblique packets


$$
\begin{aligned}E_z&=E_x+E_y,\\\partial_t E_x+\gamma_E E_x&=\epsilon^{-1}\partial_xH_y,& \partial_t E_y&=-\epsilon^{-1}\partial_yH_x,\\\partial_t H_y+\gamma_H H_y&=\partial_xE_z,& \partial_t H_x&=-\partial_yE_z,\\\gamma_E&=\sigma_e/\epsilon,\quad\gamma_H=\sigma_m/\mu,\qquad\gamma_E(x)=\gamma_H(x),\quad\mu=1.\end{aligned}
$$

$$
\frac{u^{n+1}-u^n}{\Delta t}+\gamma\frac{u^{n+1}+u^n}{2}=D_hv,\qquad u^{n+1}=\frac{1-\gamma\Delta t/2}{1+\gamma\Delta t/2}u^n+\frac{\Delta t}{1+\gamma\Delta t/2}D_hv.
$$
Eₓ and Eᵧ are auxiliary splits of Ez, not physical x/y electric components. A Bérenger-type split-field PML on only the left/right x sides of a y-periodic TMz strip matches damping of the electric split Eₓ and magnetic Hy. Outer caps are PEC. This differs from an isotropic sponge that damps every field component equally.

Physical PML thickness 2, cubic damping profile and maximum rate 10 remain fixed across 384×16,768×32 and 1536×64 grids in a 12×π/4 domain. A Gaussian-weighted sum of 511 positive-kx continuum Fourier modes uses carrier kx=12 and ky=0 or 8. Carrier angles are 0° and about 33.690°, while finite bandwidth gives an angular spectrum. Every mode solves the continuum Maxwell equations exactly; the same finite superposition is the analytic reference.

Early fields are compared with the continuum mode sum to measure propagation-error refinement. Boundary reflection is isolated by subtracting a PML-free reference on a domain five times as long with identical grid spacing, time step and Yee update at the x=6 monitor. The wide-domain reference isolates boundary effects; it is not an independent external library solver.


$$
\rho_h=\frac{\max_{t\in\mathcal W}\|E_{\rm PML}(x_m,\cdot,t)-E_{\rm wide}(x_m,\cdot,t)\|_{\rm RMS,y}}{\max_t\|E_{\rm wide}(x_m,\cdot,t)\|_{\rm RMS,y}}.
$$
Reflection ρ is the peak returned electric-field RMS over y divided by the peak incident RMS. The fixed measurement window is t=8 through 18. Its square is a squared-amplitude diagnostic, not an upper bound on broadband integrated reflected energy. Refinement holds layer thickness, incident spectrum and the time window fixed.

Fixed physical PML thickness. Early error, returned waves and work are separate metrics.GridCarrier angle (deg)Early relative field errorReturn amplitude ρAnalytic return amplitudeReturn waveform errorModified-energy + work residualPhysical-region flux residual384 × 1600.0540893.9856e-054.5515e-052.5487e-051.2897e-150.0053219768 × 3200.0136064.4119e-054.5368e-056.7622e-064.1583e-150.00133991536 × 6400.00338484.509e-054.5412e-051.7049e-062.5538e-150.00033546384 × 1633.690.053840.000195850.000202720.000138368.0989e-160.0076616768 × 3233.690.0135210.0002010.000202773.5686e-052.5619e-150.00192441536 × 6433.690.00336250.000202340.000202798.9538e-061.9159e-150.00048154Observed orders at ky=0: early field 1.9911, 2.0071; reflected-waveform error 1.9142, 1.9878; physical-region flux balance 1.9898, 1.9979.

Observed orders at ky=8: early field 1.9935, 2.0076; reflected-waveform error 1.955, 1.9948; physical-region flux balance 1.9933, 1.9987.

The finite-layer return also has an analytic modal reference. With G=γmax d/(m+1), each longitudinal mode has round-trip attenuation exp[−2(kx/ω)G] and PEC electric reflection factor−1. Sum the phases of every reflected mode and normalize the maximum RMS waveform difference by incident amplitude. Raw returned amplitude is not required to converge to zero; its error against this analytic finite-layer waveform is refined. The check is limited to a single-bounce time window; initial layer energy and cap fields are recorded in JSON.


$$
\omega_k=\sqrt{k^2+k_y^2},\quad G=\int_{L-d}^{L}\gamma(x)\,dx=\frac{\gamma_{\max}d}{m+1},\quad E_{\rm ret}(x,y,t)=\operatorname{Re}\sum_{k>0}-A_k e^{i[k(2L-x-x_0)+k_y y-\omega_k t]}e^{-2(k/\omega_k)G}.
$$
Energy budgets and revision-r2 reproduction


$$
U_*^n=\tfrac12\lVert E_n\rVert_{\epsilon,h}^2+\tfrac12\langle H^{n-1/2},H^{n+1/2}\rangle_{\mu,h},\quad\mu=1.
$$

$$
\begin{aligned}\bar E_n&=(E_{n+1}+E_n)/2,\quad\bar E_{x,n}=(E_{x,n+1}+E_{x,n})/2,\\\bar H_{y,n}&=(H_y^{n-1/2}+H_y^{n+1/2})/2,\\W_n&=\Delta t\langle\bar E_n,\epsilon\gamma_E\bar E_{x,n}\rangle_h+\frac{\Delta t}{2}\langle H_y^{n+1/2},\gamma_H(\bar H_{y,n}+\bar H_{y,n+1})\rangle_h,\\U_*^{n+1}-U_*^n+W_n&=0.\end{aligned}
$$
Here U* is the modified discrete energy weighted by permittivity. Magnetic work uses three consecutive half times, while electric work uses averaged total and split electric fields. Both are tallied directly from fields and damping coefficients, not defined as minus an energy change, allowing an independent balance comparison. Electric split work can be locally signed and is not pointwise positive physical Ohmic heating. Vacuum CFL alone is not claimed to prove positivity for arbitrary strongly damped auxiliary fields.


$$
S_x=-E_zH_y,\qquad U_{\rm physical}(t)-U_{\rm physical}(0)+\int_0^t\!\int_0^{L_y}[S_x(x_R,y,\tau)-S_x(x_L,y,\tau)]\,dy\,d\tau=0.
$$
Coarse meshes did not enter the asymptotic regime for the long round-trip phase error. The final input therefore uses 384×16,768×32 and 1536×64 with unchanged physical layer and acceptance tolerances; earlier trial outcomes were not relabeled as successful.

A separate diagnostic measures interpolated physical energy and Poynting flux in the physical region outside the PML. It is distinguished from the exact discrete work identity over the complete capped computational domain, and includes flux/interpolation discretization errors. Fixed inputs store tolerances, windows, meshes and stopping budgets; JSON records individual numerical acceptance checks and reference conditions.

The revision-r2 ZIP was independently extracted; all four inputs, including both old cases, and all tests were rerun with identical numerical metrics and CSVs. Original vacuum solver, inputs and tests remain byte-for-byte unchanged. This supplement remains separate from the 22-example common execution registry and its historical receipts.

[Revision-r2 ZIP: code, inputs, figures and four cases](/code/fdtd/2026-11-22-r2/fdtd-2026-11-22-r2.zip)

[Bilingual setup and reproduction](/code/fdtd/2026-11-22-r2/README.md)

[scattering.py](/code/fdtd/2026-11-22-r2/scattering.py)

[run_scattering.py](/code/fdtd/2026-11-22-r2/run_scattering.py)

[test_scattering.py](/code/fdtd/2026-11-22-r2/test_scattering.py)

[Unchanged original sources / provenance](/code/fdtd/2026-11-22-r2/provenance.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r2/source-manifest.json)

[43 tests passed / independent-extraction receipt](/code/fdtd/2026-11-22-r2/verification.json)



[](/numerical-methods-atlas/assets/fdtd-dielectric-interface.png)[dielectric-interface result.json](/code/fdtd/2026-11-22-r2/results/dielectric-interface/result.json) · [fixed input](/code/fdtd/2026-11-22-r2/inputs/dielectric-interface.json) · [energy.csv](/code/fdtd/2026-11-22-r2/results/dielectric-interface/energy.csv) · [convergence.csv](/code/fdtd/2026-11-22-r2/results/dielectric-interface/convergence.csv)[](/numerical-methods-atlas/assets/fdtd-pml-pulse.png)[pml-pulse result.json](/code/fdtd/2026-11-22-r2/results/pml-pulse/result.json) · [fixed input](/code/fdtd/2026-11-22-r2/inputs/pml-pulse.json) · [energy.csv](/code/fdtd/2026-11-22-r2/results/pml-pulse/energy.csv) · [convergence.csv](/code/fdtd/2026-11-22-r2/results/pml-pulse/convergence.csv)python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py
python run_scattering.py --input inputs/dielectric-interface.json --output output-interface
python run_scattering.py --input inputs/pml-pulse.json --output output-pmlRevision r2 validates normal incidence at the material interface and left/right x-PML in a vacuum strip. Four-side/corner PML is added below in r3. Oblique material-interface incidence, grazing incidence, dispersive matter, general geometry and 3D remain separate tasks.

Revision r3: four-side and corner PML

Directional damping and corner overlap


$$
\begin{aligned}E_z&=E_x+E_y,\\\partial_t E_x+\gamma_{x,E}E_x&=\partial_xH_y,&\partial_t E_y+\gamma_{y,E}E_y&=-\partial_yH_x,\\\partial_t H_x+\gamma_{y,H}H_x&=-\partial_yE_z,&\partial_t H_y+\gamma_{x,H}H_y&=\partial_xE_z,\quad\epsilon=\mu=1.\end{aligned}
$$
In the implemented vacuum 2D TMz square, γx layers occupy the left/right sides and γy layers the bottom/top sides. All outer caps are PEC. Both directional rates are nonzero in the four overlap corners. Eₓ and Eᵧ are auxiliary splits of Ez, not physical x/y electric components. Each rate is sampled at its own electric or staggered magnetic location; damping uses the trapezoidal time update.

One packet family targets ordinary sides; another targets corners obliquely. Checks establish more than a decrease in global energy: all four outgoing fluxes and contributions in all four corners are recorded. Physical layer thickness, strength and shape stay fixed during refinement, so changing resolution does not change the physical layer.

Reference waveform and interpretation of reflection

A boundary-free Fourier-mode evolution of the same discrete Maxwell equations separates ordinary propagation dispersion from boundary effects. Its update and time staggering are checked against explicit Yee updates on a separate small periodic grid. Reference period and initial physical/auxiliary split-field tails inside the layers are separately audited to distinguish periodic images from reflected waves. This is not a comparison against an independent external solver library.

The reported boundary-induced probe error normalizes the difference between PML and boundary-free monitor fields by incident amplitude. It includes finite-layer and initial PML/auxiliary-tail effects and is not called a pure ideal-PML reflection coefficient. A finite PEC-backed layer can retain nonzero returns even at very fine resolution. Absolute return amplitude is distinguished from changes of the return waveform under refinement. No zero-reflection guarantee is made outside the observation window or for arbitrary incidence.

Initial fields are standing finite-Fourier packets. Axis carriers center on (±6, 0), (0, ±6); diagonal carriers center on (±4, ±4), producing four outgoing groups. Diagonal carrier directions are 45 degrees; the finite bandwidth is distinct from a single-angle monochromatic plane wave.

The four probes are (c±a,c),(c,c±a) for axis packets and (c±a,c±a) for diagonal packets, with c=8 and a=2. The formula uses each grid’s saved time set Tₕ; the self-convergence norm is likewise the maximum over the window of four-probe RMS.


$$
\begin{gathered}A_{\mathrm{inc},h}=\max_{t\in\mathcal T_h,\,0\le tIndependently evaluated work and four-edge flux


$$
\begin{aligned}W_n={}&\Delta t\langle\bar E_n,\gamma_{x,E}\bar E_{x,n}+\gamma_{y,E}\bar E_{y,n}\rangle_h\\&+\frac{\Delta t}{2}\langle H_x^{n+1/2},\gamma_{y,H}(\bar H_{x,n}+\bar H_{x,n+1})\rangle_h\\&+\frac{\Delta t}{2}\langle H_y^{n+1/2},\gamma_{x,H}(\bar H_{y,n}+\bar H_{y,n+1})\rangle_h,\\U_*^{n+1}-U_*^n+W_n={}&0.\end{aligned}
$$
The averaged fields and modified energy U* retain their definitions above, but work now includes all four electric-x/y and magnetic-x/y terms. Magnetic work uses three consecutive half times. Every term is tallied directly from fields and rates, not reconstructed from energy loss. Auxiliary work can be locally signed and is distinct from positive physical heating. This does not claim a new general stability theorem for arbitrary split fields.


$$
\begin{gathered}S_x=-E_zH_y,\quad S_y=E_zH_x,\\\Phi(t)=\int_{y_B}^{y_T}(S_x(x_R,y,t)-S_x(x_L,y,t))\,dy+\int_{x_L}^{x_R}(S_y(x,y_T,t)-S_y(x,y_B,t))\,dx,\\U_{\rm physical}(t)-U_{\rm physical}(0)+\int_0^t\Phi(\tau)\,d\tau=0.\end{gathered}
$$
The physical rectangle inside the PML sums right-minus-left and top-minus-bottom Poynting fluxes and compares them with interior energy change. Electric corner nodes use quarter quadrature weights and edge nodes half weights, avoiding double counting. The exact full-domain discrete work identity is checked separately from the interpolated/time-integrated physical-region balance.

Fixed input and saved measurements

The benchmark is a square of side 16, physical PML thickness 2, maximum damping rate 8 and profile order 3. Initial packet center is (8, 8), width 1. Grids are 128×128, 256×256, 512×512; the observation ends at t=24 and returned fields are evaluated from t=8.

The reference Fourier period is 64, with Δk=0.098175. Rounding requested cutoff 14 to the nearest mode gives actual per-axis kmax=14.039. The finite sum has 20736 coefficient slots with the DC component removed; it is distinct from an infinite-band exact Gaussian.

Revision-r3 fixed input. Individual acceptance decisions and reference information are stored in result JSON.Packet familyGridEarly relative field errorBoundary-induced probe errorEnergy + work residualFour-edge flux residualaxis128 × 1280.113280.000272455.8233e-160.029017axis256 × 2560.0302560.000338388.5458e-160.0075302axis512 × 5120.00758380.000362772.5493e-150.0019002diagonal128 × 1280.0392119.7478e-065.8085e-160.02655diagonal256 × 2560.0105171.0326e-058.5392e-160.0067585diagonal512 × 5120.00265931.0584e-058.4959e-160.0016973axis observed orders: early field 1.9046, 1.9962; four-edge flux balance 1.9461, 1.9865; return-waveform self-convergence 1.66. Doubling the reference period changes the trace by 8.6937e-11 relative to incident amplitude.

diagonal observed orders: early field 1.8986, 1.9836; four-edge flux balance 1.9739, 1.9935; return-waveform self-convergence 1.8964. Doubling the reference period changes the trace by 6.6332e-10 relative to incident amplitude.

Finest-grid cumulative outward flux per edge / initial physical-region energy.FamilyLeft edgeRight edgeBottom edgeTop edgeaxis0.249530.249530.249530.24953diagonal0.249580.249580.249580.24958Diagonal-family accumulated absolute corner work increments / initial total energy: SW=0.11008, SE=0.11008, NW=0.11008, NE=0.11008. Regional work is summed over cells/components before taking its absolute value at each step, then accumulated in time. This is distinct from integrating the pointwise absolute work density.

axis: zeroing the initial layer fields changes the finest-grid monitor trace by 3.4327e-09 relative to incident amplitude, or 9.4624e-06 of the standard return signal (criterion ≤ 0.01). This sensitivity control preserves the interior packet while perturbing tiny physical/auxiliary fields inside the layers. It is a different initial condition, not a rigorous error bound for the standard input.

diagonal: zeroing the initial layer fields changes the finest-grid monitor trace by 7.8814e-09 relative to incident amplitude, or 0.00074467 of the standard return signal (criterion ≤ 0.01). This sensitivity control preserves the interior packet while perturbing tiny physical/auxiliary fields inside the layers. It is a different initial condition, not a rigorous error bound for the standard input.

Return-waveform self-convergence orders are observations for this packet, layer profile and three-grid range. They do not establish the same order for all incidence or grid ranges.

Waveform differences across meshes are compared at common physical times. Self-convergence orders and any Richardson-type estimates are empirical diagnostics, not rigorous error bounds. They do not require every raw return to vanish.


$$
\delta_h=\|r_h-\mathcal I r_{h/2}\|_{\mathcal W},\qquad p_h=\frac{\log(\delta_h/\delta_{h/2})}{\log2}.
$$
Download and reproduce revision r3

[](/numerical-methods-atlas/assets/fdtd-pml-corners.png)[Four-side/corner result JSON](/code/fdtd/2026-11-22-r3/results/pml-corners/result.json) · [convergence.csv](/code/fdtd/2026-11-22-r3/results/pml-corners/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22-r3/results/pml-corners/energy.csv)[Revision-r3 ZIP: retained four cases plus four-side/corner PML](/code/fdtd/2026-11-22-r3/fdtd-2026-11-22-r3.zip)

[Bilingual setup and execution](/code/fdtd/2026-11-22-r3/README.md)

[corner.py](/code/fdtd/2026-11-22-r3/corner.py)

[run_corner.py](/code/fdtd/2026-11-22-r3/run_corner.py)

[test_corner.py](/code/fdtd/2026-11-22-r3/test_corner.py)

[Fixed input and acceptance criteria](/code/fdtd/2026-11-22-r3/inputs/pml-corners.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r3/source-manifest.json)

[Unchanged earlier sources / provenance](/code/fdtd/2026-11-22-r3/provenance.json)

[57 tests passed / independent extraction](/code/fdtd/2026-11-22-r3/verification.json)



python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py
python run_corner.py --input inputs/pml-corners.json --output output-cornersThe ZIP was independently extracted; all tests and all five inputs were rerun with identical numerical metrics and CSVs. Numerical sources, inputs and tests from the earlier editions remain byte-for-byte unchanged. This supplement is separate from the common 22-example / 67-problem inventory.

Scope is the specified vacuum 2D TMz packets, square and finite time window. Oblique material-interface incidence, general grazing incidence, dispersive/anisotropic matter, 3D and general curved PML geometries need separate validation.

Original vacuum edition: code and reproduction

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

Educational 2D TMz: original vacuum modes, r2 normal dielectric interface/x-PML, and r3 four-side/four-corner PML for specified packets, grids and observation windows. Continuum references, discrete Fourier references, self-convergence, independently tallied work and physical flux have distinct roles. Not blanket validation of general matter, arbitrary incidence or 3D.

## Sources

- Kane Yee (1966). Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. https://doi.org/10.1109/tap.1966.1138693
- Fadime Bekmambetova and Xinyue Zhang and Piero Triverio (2017). A Dissipation Theory for Three-Dimensional FDTD with Application to Stability Analysis and Subgridding. https://arxiv.org/abs/1705.02274v2
- Jean-Pierre Bérenger (1994). A Perfectly Matched Layer for the Absorption of Electromagnetic Waves. https://doi.org/10.1006/jcph.1994.1159
- Steven G. Johnson (2021). Notes on Perfectly Matched Layers (PMLs). https://arxiv.org/abs/2108.05348v1
- Markus Zahn (2003). Electromagnetic Field Theory: A Problem Solving Approach. https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/
