# Yee finite-difference time-domain method

Yee FDTD: foundations and verified examples

The Yee method advances Maxwell equations with staggered electric and magnetic fields. Start with the basic equations, then select a verification example. The latest r6 addition covers one-dimensional lossy and Lorentz-dispersive media.

[Basic model](#model) · [Loss and dispersion](#interface-loss-dispersion) · [Fresnel interfaces](#interface) · [Side/corner PML](#pml-corners) · [Oblique incidence](#interface-oblique) · [p polarization, Brewster and TIR](#interface-p-polarization)

This original educational implementation evolves 2D TMz fields (Ez, Hx, Hy) with original vacuum cases in dimensionless homogeneous vacuum without current or charge sources. The original periodic plane waves and rectangular perfect-electric-conductor (PEC) cavity are compared with continuum analytic solutions. Grid refinement, numerical dispersion, a discrete invariant and an approximation to physical energy are measured separately.

Model, units and scope


$$
\partial_t E_z=\partial_xH_y-\partial_yH_x,\qquad \partial_tH_x=-\partial_yE_z,\qquad \partial_tH_y=\partial_xE_z,\quad \epsilon=\mu=c=1.
$$
Length, time and fields are normalized so ε=μ=c=1. The rectangle has Lx=1 and Ly=1.5, with mode indices (m,l)=(1,1). An oblique periodic mode on a rectangular domain exercises both spatial derivatives and magnetic-field signs. These initial vacuum examples exclude dispersion, loss, interfaces and external excitation; later examples cover their stated additional scopes.

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

Revision r6: lossy and dispersive media

A one-dimensional packet is normally incident on a finite slab surrounded by vacuum. Two examples use Ohmic conductivity and one damped Lorentz resonance. Ez, polarization P and polarization current J occupy integer times; Hy occupies half times. A Yee magnetic step is followed by a local implicit-midpoint E/P/J solve.


$$
\begin{gathered}\epsilon_\infty\partial_t E=\partial_xH-\sigma E-J,\quad\partial_tH=\partial_xE,\\\partial_tP=J,\quad\partial_tJ=fE-\omega_0^2P-\gamma J,\quad f=\Delta\epsilon\,\omega_0^2,\\\epsilon(\omega)=\epsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega},\quad e^{-i\omega t}.\end{gathered}
$$
σ multiplies the conventional current σE. When f=0, P=J=0 and oscillator terms are omitted. Distant PEC caps close the domain, with no PML in this example. Interface electric control volumes use half-volume averages of ε∞, σ and f.

The analytic solution includes internal multiple reflections and a complex wavenumber, weighted by the actual incident spectrum. Numerical R/T come from exterior Poynting fluences; A comes from directly accumulated conductive and polarization damping work. Absorption and transient material storage are separated, with energy budgets and spatial/temporal refinement checked.

Finest-grid finite-window measurements and spectrum-weighted analytic values.SlabNumerical RNumerical TDirect AAnalytic R / T / Aohmic0.04217920.1631050.7947160.0422517 / 0.163222 / 0.794527lorentz0.1210680.05543760.8234950.121356 / 0.0555188 / 0.823125[](/numerical-methods-atlas/assets/fdtd-loss-dispersion.png)[Results and all acceptance checks](/code/fdtd/2026-11-22-r6/results/loss-dispersion/result.json) · [convergence.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/convergence.csv) · [Open full-size figure](/numerical-methods-atlas/assets/fdtd-loss-dispersion.png)[Revision-r6 code ZIP: loss/dispersion plus seven retained inputs](/code/fdtd/2026-11-22-r6/fdtd-2026-11-22-r6.zip) · [Bilingual execution guide](/code/fdtd/2026-11-22-r6/README.md)

Scope is linear, isotropic, nonmagnetic 1D normal incidence, with the stated spectrum and finite window. Drude, multiple resonances, oblique dispersive incidence, dispersive media combined with PML, and general 2D/3D are unvalidated.

Open derivation, full refinement results and reproduction material
$$
\begin{gathered}n=\sqrt{\epsilon},\quad\Re n\ge0,\quad\Im n\ge0,\quad\rho=\frac{1-n}{1+n},\quad z=e^{2in\omega d},\\r=\frac{\rho(1-z)}{1-\rho^2z},\quad t=\frac{(1-\rho^2)e^{in\omega d}}{1-\rho^2z},\\R=|r|^2,\quad T=|t|^2,\quad A=1-R-T,\\A_{\rm volume}=\int_0^d\!\left(\sigma+\frac{\gamma\omega^2f}{|\omega_0^2-\omega^2-i\gamma\omega|^2}\right)|E(x)|^2\,dx.\end{gathered}
$$
t is the electric amplitude at the exit face. Both exteriors are vacuum, so T=|t|². E(x) in the volume integral has unit incident amplitude. Analytic A=1−R−T is checked against this separate internal-field dissipation integral. Carrier coefficients, spectral averages and finite-window DFT differences are retained separately.


$$
\begin{gathered}U_*^n=\tfrac12\|E^n\|_{\epsilon_\infty,h}^2+\tfrac12\Re\langle H^{n-1/2},H^{n+1/2}\rangle_h+U_{\rm mat}^n,\\U_{\rm mat}=\sum_{f_j>0}\frac{|J_j|^2+\omega_0^2|P_j|^2}{2f_j}\Delta x,\\\Delta W_\sigma=\Delta t\sum_j\sigma_j|\bar E_j|^2\Delta x,\quad\Delta W_\gamma=\Delta t\sum_{f_j>0}\frac{\gamma|\bar J_j|^2}{f_j}\Delta x,\\U_*^n+W_\sigma^n+W_\gamma^n=U_*^0.\end{gathered}
$$
Complex fields represent two real quadratures, consistently across energies and fluxes. Wσ/Wγ are computed from midpoint fields, independently of energy deficits and 1−R−T. The modified discrete energy identity and physical local Poynting budget with centered H have separate criteria. Midpoint inner products cancel E–J exchange, and paired discrete curls cancel at PEC caps, giving the identity. The strict CFL uses ε∞, rather than static permittivity: Δt/Δx<min(1,√ε∞). Oscillator storage is not added to absorption.

Three grids at matched physical clocks.SlabNxField relative L2R errorT errorA errorPhysical flux residualohmic30720.120280.001165190.001887640.003052830.00215611ohmic61440.03010150.0002903310.0004686340.0007589650.00053856ohmic122880.0075267.2522e-050.0001169550.0001894770.000134611lorentz30720.104430.004686770.001302980.005989750.00215381lorentz61440.02633820.001157060.0003250520.001482110.000537989lorentz122880.006597650.0002883548.12193e-050.0003695730.000134468Finest-grid Lorentz polarization P and current J relative L2 errors are 0.011884 and 0.0124923.

ohmic observed orders: field 1.99849, 1.99988; R 2.0048, 2.00121; T 2.01005, 2.0025; A 2.00804, 2.00201; complex r 2.00255, 2.00077; complex t 2.00708, 2.0018; physical flux budget 2.00126, 2.00032; physical energy 2.00565, 2.00141; fixed-space time-halving self-convergence order: 2.00388

lorentz observed orders: field 1.9873, 1.99713; R 2.01813, 2.00455; T 2.00307, 2.00078; A 2.01484, 2.00372; complex r 1.99893, 2.00058; complex t 2.00077, 2.00052; physical flux budget 2.00124, 2.00031; physical energy 2.00952, 2.00236; P 2.02312, 2.00687; J 2.02239, 2.00672; fixed-space time-halving self-convergence order: 2.00371

Separate conservation, loss, residual storage and reference controls.SlabMaximum modified balance residual|R+T+A−1|Final material storage / incidentReference window fluence gapReference period-doubling field gapohmic1.64405e-133.04201e-1403.33067e-161.28307e-09lorentz1.76686e-131.09499e-103.10325e-126.24744e-111.92765e-09Field accuracy is measured at the saved interaction clock; flux/loss integration continues to the later end time. Initial E is the incident packet, H is half-time aligned using the Yee dispersion relation, and P=J=0. A same-Yee vacuum control isolates reflection. Omitted continuum scattering/polarization tails, caps, omitted frequency tails, doubled reference period/spatial quadrature and finite-window DFT gaps are recorded in JSON. Temporal self-convergence concerns the fixed spatial discretization, rather than comparison with an external PDE solver.

[dispersive.py](/code/fdtd/2026-11-22-r6/dispersive.py) · [run_dispersive.py](/code/fdtd/2026-11-22-r6/run_dispersive.py) · [test_dispersive.py](/code/fdtd/2026-11-22-r6/test_dispersive.py) · [Fixed input and tolerances](/code/fdtd/2026-11-22-r6/inputs/loss-dispersion.json) · [energy.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/energy.csv) · [solution.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/solution.csv) · [spectrum.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/spectrum.csv) · [waveforms-ohmic.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/waveforms-ohmic.csv) · [waveforms-lorentz.csv](/code/fdtd/2026-11-22-r6/results/loss-dispersion/waveforms-lorentz.csv) · [SHA-256 manifest](/code/fdtd/2026-11-22-r6/source-manifest.json) · [Earlier-source provenance](/code/fdtd/2026-11-22-r6/provenance.json) · [108 tests passed / extraction rerun](/code/fdtd/2026-11-22-r6/verification.json)

python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py test_dispersive.py
python run_dispersive.py --input inputs/loss-dispersion.json --output output-lossIndependent ZIP extraction reran all tests and all eight inputs with identical metrics and every CSV. Numerical sources/tests of the seven earlier inputs and all five earlier releases remain unchanged. This supplement does not increment other execution registries. Selected official Meep documentation supplies Lorentz-model context; its conductivity convention and explicit ADE differ from this implementation.

Detailed initial evidence: periodic wave and PEC cavityFixed inputs and measured results


$$
e_h=\left(\frac{\lVert E_h-E\rVert_h^2+\lVert H_h-H\rVert_h^2}{\mathcal N^2}\right)^{1/2},\qquad p=\frac{\log(e_h/e_{h/2})}{\log 2}.
$$
Grids are 16×24, 32×48 and 64×96. Continuum field errors are evaluated exactly at the prescribed 1.1-period target, reached by adjusting the time step to an integer step count. H is compared at its actual half step before E. The combined-field denominator 𝒩² is the constant continuum modal norm (LxLy for the periodic wave, LxLy/4 for the cavity). Separate electric and magnetic errors are retained in JSON.

Fixed-input measurements. Field and frequency errors use continuum analytic solutions.CaseGrid Nx × NyRelative field L² errorObserved orderRelative frequency errorMaximum relative modified-energy driftPeriodic wave16 × 240.021645—0.00312712.22e-16Periodic wave32 × 480.00539262.00490.000779622.22e-16Periodic wave64 × 960.00133092.01860.000192442.22e-16PEC cavity16 × 240.0055511—0.000779624.441e-16PEC cavity32 × 480.00135142.03830.000192444.441e-16PEC cavity64 × 960.000333262.01974.7804e-052.22e-16Periodic plane wave · [JSON](/code/fdtd/2026-11-22/results/periodic-wave/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/periodic-wave/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/periodic-wave/energy.csv)PEC cavity · [JSON](/code/fdtd/2026-11-22/results/pec-cavity/result.json) · [convergence.csv](/code/fdtd/2026-11-22/results/pec-cavity/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22/results/pec-cavity/energy.csv)Acceptance tolerances are saved in each fixed input. Separate checks require field error ≤0.01, observed orders ≥1.8, relative frequency error ≤0.002, discrete-dispersion identity error ≤10⁻⁹ and relative U* drift ≤2×10⁻¹¹. Separate checks require zero wall electric field, preservation of initial magnetic divergence, maximum Usync error against the analytic total energy ≤0.003, and approximately second-order refinement of that error. The Usync variation span is retained as a diagnostic.

Detailed r2 evidence: interface and x PMLDielectric interface: Fresnel amplitudes and energy


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

Detailed r3 evidence: sides and cornersRevision r3: four-side and corner PML

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

Revision r3 covers the specified vacuum 2D TMz packets, square and finite time window. Oblique material-interface incidence is tested separately in r4 below. General grazing incidence, dispersive/anisotropic matter, 3D and curved PML geometries need separate validation.

Detailed r4 evidence: oblique incidenceRevision r4: oblique incidence at a dielectric interface

TMz, s polarization and Fresnel coefficients

Two lossless, nondispersive, nonmagnetic dielectrics meet at x=a. Ez is perpendicular to the xy incidence plane, so this TMz convention corresponds to optical s/TE polarization. The y direction is periodic. This case uses distant PEC x caps and an observation window before their main return; no PML loss is included.


$$
\omega^2=(k^2+k_y^2)/\epsilon_1,\quad q=\sqrt{\epsilon_2\omega^2-k_y^2},\quad n_1\sin\theta_i=n_2\sin\theta_t,\quad\mu_1=\mu_2=1.
$$

$$
r_s(k)=\frac{k-q}{k+q},\quad t_s(k)=\frac{2k}{k+q},\quad R_s=|r_s|^2,\quad T_s=\frac{q}{k}|t_s|^2,\quad R_s+T_s=1.
$$
Frequency ω and tangential wave number ky are shared across the interface for each positive incident normal wave number k. The selected low-to-high index cases have propagating transmitted waves. Lowercase r,t are signed electric amplitudes; uppercase R,T are normal energy-flux fractions. Transmittance includes q/k and is distinct from t².

Analytic reference for a finite-band packet


$$
\begin{aligned}E_i&=\Re\int_0^\infty A(k)e^{i[k(x-c)+k_y y-\omega t]}\,dk,\\E_r&=\Re\int_0^\infty A(k)r_s(k)e^{i[k(2a-x-c)+k_y y-\omega t]}\,dk,\\E_t&=\Re\int_0^\infty A(k)t_s(k)e^{i[k(a-c)+q(x-a)+k_y y-\omega t]}\,dk.\end{aligned}
$$

$$
\begin{aligned}R_{\rm packet}&=\frac{\int_0^\infty |A(k)|^2R_s(k)\,dk}{\int_0^\infty |A(k)|^2\,dk},\\T_{\rm packet}&=\frac{\int_0^\infty |A(k)|^2T_s(k)\,dk}{\int_0^\infty |A(k)|^2\,dk},\qquad\frac{dq}{dk}=\frac{\epsilon_2 k}{\epsilon_1 q}.\end{aligned}
$$

$$
A(k)=\frac{w}{\sqrt{2\pi}}e^{-w^2(k-k_0)^2/2},\quad a_m=A(k_m)\Delta k,\quad\Delta k=2\pi/P,\quad n_j=\sqrt{\epsilon_j},\qquad U_{\rm inc}=\pi\epsilon_1 L_y\int_0^\infty |A(k)|^2\,dk\approx\frac{\epsilon_1 L_yP}{2}\sum_m a_m^2.
$$
Each mode of a positive-k packet centered initially at c uses its Fresnel solution. Magnetic amplitudes are Hx=(ky/ω)E and Hy=−(kx/ω)E with signed kx; E and H are evaluated at their own Yee positions and times. A finite quadrature evaluates the Gaussian-weighted spectral integral. Halving its spacing and integrating reference energy in the finite box control the approximation. Since refracted q values are nonuniform, quadrature period P does not imply that the transmitted packet is periodic in x.

Carrier-angle monochromatic coefficients are distinguished from packet R,T, which weight Fresnel coefficients by |A(k)|². The transmitted-wave-number Jacobian produces the same q/k factor for packet energy. Numerical R,T divide the left/right physical energies by the incident packet Parseval quadrature; the initial numerical energy ratio is recorded separately.


$$
g_r=\frac{\sum_{xa,y}E_{\rm num}E_{t,\rm ref}}{\sum_{x>a,y}E_{t,\rm ref}^2},\qquad g_r,g_t\to1.
$$
Amplitude diagnostics project the final numerical Ez separately onto the signed analytic reflected/transmitted templates. The target gain is 1; these gains are distinct from measured carrier r,t. Separate L2 waveform errors retain phase and shape discrepancies.

Independent energy and flux checks


$$
\begin{gathered}U_*^n=\tfrac12\bigl(\langle E^n,\epsilon E^n\rangle_h+\langle H^{n-1/2},H^{n+1/2}\rangle_h\bigr),\quad U_*^n=U_*^0,\\S_x=-E_zH_y,\quad U_{[x_L,x_R]}(t)-U_{[x_L,x_R]}(0)+\int_0^t\!\int_0^{L_y}[S_x(x_R,y,\tau)-S_x(x_L,y,\tau)]\,dy\,d\tau=0.\end{gathered}
$$
The full domain checks conservation of modified discrete energy with permittivity weighting. Physical energy averages H to integer times; two faces of an interior slab straddling the interface provide directly evaluated Poynting flux, integrated by the trapezoidal rule. Flux is not defined from an energy difference. This approximate physical balance is distinct from the exact discrete invariant. The interface electric node retains the arithmetic permittivity average.

Fixed input and measured refinement

ε₁=1, ε₂=4; box 32×1.5708, initial center c=8, interface a=16, width 1.2, carrier kx=6. ky=0, 4; grids 1024×16, 2048×32, 4096×64; end time 18. Flux slab: [12.0, 20.0].

Reference quadrature uses P=64, Δk=0.0981748, and actual kmax=14.039 after rounding requested cutoff 14 to the nearest mode.

All three grids. R/T errors use the spectral Fresnel reference for the same input.kyGridRelative field L2 errorNumerical RNumerical TLocal flux budget residual01024×160.3666450.1069330.8913670.0022301702048×320.09196090.1100750.88950.00056024104096×640.02297510.1108530.8890410.00014023341024×160.5483710.1503810.8471720.0024363942048×320.1385210.1558540.8435330.00061187744096×640.03462150.1572090.8426380.000153143Carrier-angle coefficients are distinct from finite-band packet fractions.Carrier incidence°Carrier refraction°Carrier rCarrier tCarrier RPacket reference RPacket reference T00-0.3333330.6666670.1111110.1111110.88888933.690116.1021-0.3956610.6043390.1565480.1576590.842341ky=0: observed orders, field 1.99529, 2.00095; reflected energy 2.01165, 2.0029; transmitted energy 2.02059, 2.00515; flux budget 1.99303, 1.99822. Finest template gains (gᵣ,gₜ)=(0.998868, 0.999845).

ky=4: observed orders, field 1.98505, 2.00037; reflected energy 2.01151, 2.00285; transmitted energy 2.01829, 2.00455; flux budget 1.99343, 1.99836. Finest template gains (gᵣ,gₜ)=(0.998485, 0.999572).

Maximum full-domain modified-energy drift over all grids: 4.44089e-16. At the final comparison time, doubling quadrature density changes reference fields over all meshes by at most 5.30355e-13 relatively; finite-box reference R/T differ from spectral integrals by at most 8.66989e-11. The initial secondary-field squared weighted staggered-norm fraction is at most 2.30339e-21; maximum analytic cap Ez is 1.24222e-06. Staggered field norms are distinguished from same-time physical energy.

Initial PEC clipping changes the squared weighted staggered field norm by a fraction at most 2.29928e-22. Same-time continuum initial energy / incident quadrature differs from 1 by at most 2.22045e-16. The final reference interface Ez maximum 1.4462e-05 records the remaining interface field during the left/right energy partition.

ky=0: initial numerical physical energy / incident quadrature 0.999894; final |R+T−1| 0.000106367.

ky=4: initial numerical physical energy / incident quadrature 0.999847; final |R+T−1| 0.000153186.

The small R+T closure difference includes the mismatch between initial numerical physical energy and analytic incident quadrature. This case has no absorption or PML, and modified discrete energy is conserved. Refining physical-energy interpolation/quadrature error is distinct from physical dissipation.

Download and reproduce revision r4

[](/numerical-methods-atlas/assets/fdtd-dielectric-oblique.png)[Oblique-interface result JSON](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/result.json) · [spectrum.csv](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/spectrum.csv) · [convergence.csv](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22-r4/results/dielectric-oblique/energy.csv)[Revision-r4 ZIP: retained five cases plus oblique dielectric incidence](/code/fdtd/2026-11-22-r4/fdtd-2026-11-22-r4.zip)

[Bilingual setup and execution](/code/fdtd/2026-11-22-r4/README.md)

[oblique.py](/code/fdtd/2026-11-22-r4/oblique.py)

[run_oblique.py](/code/fdtd/2026-11-22-r4/run_oblique.py)

[test_oblique.py](/code/fdtd/2026-11-22-r4/test_oblique.py)

[Fixed input and acceptance criteria](/code/fdtd/2026-11-22-r4/inputs/dielectric-oblique.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r4/source-manifest.json)

[Unchanged earlier sources / provenance](/code/fdtd/2026-11-22-r4/provenance.json)

[71 tests passed / independent-extraction record](/code/fdtd/2026-11-22-r4/verification.json)



python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py
python run_oblique.py --input inputs/dielectric-oblique.json --output output-obliqueIndependent ZIP extraction reran all tests and all six inputs with identical metrics and CSVs. The old five inputs, numerical sources/tests and three frozen editions are retained. This dedicated FDTD supplement is separate from the common execution registry and other fields’ verification counts.

Revision r4 covers the specified lossless/nonmagnetic s-polarized packets with propagating transmission, three grids and finite time. The p-polarized Brewster and TIR cases are tested separately in r5 below. Loss/dispersion and 3D remain separate tasks. References are analytic modes and quadrature, not an external FDTD solver.

Detailed r5 evidence: p polarization, Brewster and TIRRevision r5: p polarization, Brewster condition and TIR

TEz staggering and optical p polarization


$$
\partial_t H_z=\partial_yE_x-\partial_xE_y,\qquad\epsilon\partial_tE_x=\partial_yH_z,\qquad\epsilon\partial_tE_y=-\partial_xH_z,\quad\mu=1.
$$
The new TEz update places Hz at cell centers and integer times, with Ex/Ey on their own edges at half times. H is perpendicular to the xy incidence plane, corresponding to optical p polarization. Here Ex/Ey are physical electric components; the earlier TMz-PML used those names for auxiliary splits of Ez. Tangential interface Ey uses arithmetic permittivity averaging; normal Ex uses its cell’s material value. The interface inverse permittivity 2/(ε₁+ε₂) is the harmonic mean of the two side inverse permittivities. x caps are PEC, y is periodic, and this case uses no PML.


$$
\begin{gathered}\partial_y\longmapsto iK_y,\qquad K_y=\frac{2}{\Delta y}\sin\frac{k_y\Delta y}{2},\\\int_0^{L_y}\Re(Ae^{ik_yy})\Re(Be^{ik_yy})\,dy=\frac{L_y}{2}\Re(AB^*),\\k_yL_y=2\pi m,\qquad 0Fixed runs use an exact reduction to one positive ky mode. The derivative is the Yee symbol iKy, not the continuum iky. Separate tests establish equivalence with the full 2D array update; fixed runs refine both dx and dy. They do not time-step full Nx×Ny arrays in each benchmark.

Magnetic Fresnel amplitudes and the two special angles


$$
\begin{gathered}\omega^2=(k^2+k_y^2)/\epsilon_1,\quad q=\sqrt{\epsilon_2\omega^2-k_y^2},\quad\Re q\ge0,\ \Im q\ge0,\\Y_1=k/\epsilon_1,\quad Y_2=q/\epsilon_2,\quad r_H=\frac{Y_1-Y_2}{Y_1+Y_2},\quad t_H=1+r_H,\\R=|r_H|^2,\qquad T=\frac{\Re Y_2}{Y_1}|t_H|^2,\quad E_x=-\frac{k_y}{\epsilon\omega}H_z,\quad E_y=\frac{k_x}{\epsilon\omega}H_z.\end{gathered}
$$

$$
\tan\theta_B=\sqrt{\epsilon_2/\epsilon_1},\quad r_H(\theta_B)=0;\qquad\theta_c=\sin^{-1}\sqrt{\epsilon_2/\epsilon_1}\quad(\epsilon_1>\epsilon_2).
$$
The convention is exp[i(kx x+ky y−ωt)]. rH,tH are Hz amplitude coefficients; reflected E uses signed kx=−k and transmitted E uses kx=q. The tangential Ey reflection sign is distinguished from the polarization-basis amplitude convention. TIR takes q=iκ with κ>0, so fields decay to the right.


$$
\begin{gathered}u=(k-k_0)/b,\\A_H(k)=\begin{cases}C\exp\!\left[-\frac{w^2(k-k_0)^2}{2}-\frac{u^8}{1-u^2}\right],&|u|The input supplies a compact positive-k band with the smooth weight above; each mode uses its Fresnel solution. The fixed inputs use C=1; actual quadrature coefficients are saved in spectrum CSVs. This Hz-normalized incident energy has no ε₁ factor, unlike the preceding Ez packet. A carrier at the analytic Brewster angle generally leaves nonzero finite-band R∞. This validates a known Brewster condition, rather than independently locating the zero through an angular search.

Isolating weak returns and finite-window measurements


$$
\begin{gathered}\Phi_X(t)=\frac{L_y}{2}\Re\!\left[E_{y,X}^{\rm centred}(t)H_X(t)^*\right],\\R_{\cal W}=-\frac{\int_{\cal W}\Phi_{\rm ref}\,dt}{\int_{\cal W}\Phi_{\rm inc}\,dt},\qquad T_{\cal W}=\frac{\int_{\cal W}\Phi_{\rm tr}\,dt}{\int_{\cal W}\Phi_{\rm inc}\,dt}.\end{gathered}
$$
Interface and homogeneous-medium runs use the same Yee update. Subtracting their H/E at the left monitor isolates the reflected component, avoiding ordinary incident dispersion obscuring a weak Brewster return. Incident/reflected left flux and transmitted right flux are integrated in time. H is spatially averaged to each face and E centered to integer time. Finite-window ratios are recorded separately from their gaps to asymptotic spectral R∞,T∞.


$$
\begin{gathered}\widehat H(\omega_0)=\int_{\cal W}H(t)e^{i\omega_0t}\,dt,\\r_{H,h}^{\rm DFT}=\frac{\widehat H_{\rm ref}}{\widehat H_{\rm inc}}e^{-2ik_hd},\\\kappa_h=-\frac{\log|\widehat H(x_2)/\widehat H(x_1)|}{x_2-x_1}.\end{gathered}
$$

$$
\begin{gathered}\Omega_0=\frac{2}{\Delta t}\sin(\omega_0\Delta t/2),\\k_h=\frac{2}{\Delta x}\sin^{-1}\!\left[\frac{\Delta x}{2}\sqrt{\epsilon_1\Omega_0^2-K_y^2}\right].\end{gathered}
$$
The left monitor is distance d from the interface. Complex reflection is deembedded with kh from the same discrete dispersion relation; transmission also corrects the face-averaged H factor. TIR κ is measured from temporal Fourier components at two right-side probes. Refinement compares with continuum Fresnel data through the same finite window. Its gaps to ideal carrier coefficients and ideal κ remain visible, separating window error from grid error.

TIR fields, stored energy and net flux

The complete TIR support lies beyond the critical angle: every mode has R=1 and zero normal time-average T. Evanescent fields and transient stored energy still exist on the right. Signed incoming/outgoing transient flux, maximum right-side storage and final storage are recorded separately; right-side stored energy is not called transmittance.


$$
\begin{gathered}U_*^n=\tfrac12\bigl(\|H^n\|_h^2+\langle E^{n-1/2},\epsilon E^{n+1/2}\rangle_h\bigr),\quad U_*^n=U_*^0,\\\bar E^n=(E^{n-1/2}+E^{n+1/2})/2,\quad U_{\rm phys}^n-U_*^n=\tfrac18\|E^{n+1/2}-E^{n-1/2}\|_{\epsilon,h}^2,\\\Delta U_{[x_L,x_R]}+\int(\Phi_{x_R}-\Phi_{x_L})\,dt=0.\end{gathered}
$$
Modified discrete energy is distinct from physical energy using centered E. Interior flux is evaluated directly from fields, not reconstructed from energy loss. Splitting interface Ey energy assigns ε₁/2 and ε₂/2 to the two sides, retaining the global averaged coefficient. Field accuracy is assessed at a fixed interaction time; energy and flux continue to a later end time. End-time field error is reported separately.

Fixed inputs and saved measurements

Reference quadrature parameter P=256, Δk=0.0245437, Courant factor 0.65. Field-comparison times and later fluence/energy end times are listed separately; result JSON records the actual saved clocks.

propagating: ε₁=1→ε₂=4, box 80×3.14159, initial center 36, interface 48, (k₀,ky)=(3,2), carrier incidence 33.6901°, k band [0.5, 5.5], w=2, b=2.5. Field time 18, fluence end 48, monitor distance d=3, budget slab [42.0, 54.0], grids 1280×64, 2560×128, 5120×256.

brewster: ε₁=1→ε₂=4, box 112×3.14159, initial center 40, interface 56, (k₀,ky)=(2,4), carrier incidence 63.4349°, k band [0.3, 3.7], w=4, b=1.7. Field time 44, fluence end 96, monitor distance d=2, budget slab [52.0, 60.0], grids 1792×64, 3584×128, 7168×256.

tir: ε₁=4→ε₂=1, box 80×3.14159, initial center 28, interface 40, (k₀,ky)=(4,4), carrier incidence 45°, k band [1.5, 6.5], w=1.2, b=2.5. Field time 40, fluence end 100, monitor distance d=0.75, budget slab [37.0, 43.0], grids 1280×64, 2560×128, 5120×256.

All three grids. Field errors are relative L2; flux ratios use numerical incident fluence from the homogeneous control.CaseGridField clockInteraction field errorEnd-time field errorR_WT_W, signedComplex rH error / window referencepropagating1280×64180.1474550.8705790.06595690.9340430.00909874propagating2560×128180.03683170.2266380.06964630.9303540.00222338propagating5120×256180.009204090.05672690.07055870.9294410.000552736brewster1792×64440.4963441.832030.001378760.9986220.0131163brewster3584×128440.1253730.5825640.001156280.9988440.00318401brewster7168×256440.03132320.1474880.001139560.9988610.000790283tir1280×64400.2421050.5859371-1.22848e-090.0101086tir2560×128400.06073630.1494281-1.22624e-090.00250989tir5120×256400.0151880.03740621-1.22729e-090.00062594Asymptotic spectral values, finite-window continuum data and numerical targets remain distinct.CaseReference R∞Reference T∞Reference window R_WReference window T_WReference DFT→ideal rH gapNumerical DFT→ideal rH errorpropagating0.0708620.9291380.0708620.9291386.9802e-070.00055212brewster0.001137230.9988630.001137230.9988637.30357e-060.000786266tir101-1.23752e-090.000187080.00055515propagating observed orders: field: 2.00125, 2.0006; reflected fluence: 2.01258, 2.00318; transmitted fluence: 2.01258, 2.00318; complex rH / finite window: 2.03291, 2.00809; complex tH / finite window: 2.03288, 2.00808; local flux budget: 1.99738, 1.99935; transient transmitted-flux waveform: 2.03289, 2.00826.

brewster observed orders: field: 1.98512, 2.00092; reflected fluence: 3.66482, 3.03245; transmitted fluence: 3.66482, 3.03245; complex rH / finite window: 2.04244, 2.0104; complex tH / finite window: 2.03468, 2.00847; local flux budget: 2.00677, 2.00163; transient transmitted-flux waveform: 2.05672, 2.01386.

tir observed orders: field: 1.995, 1.99963; reflected fluence: 2.22383, 3.59628; complex rH / finite window: 2.00988, 2.00353; complex tH / finite window: 2.00848, 2.00541; local flux budget: 1.99629, 1.99909; κ / finite window: 2.00522, 2.03305; transient transmitted-flux waveform: 2.00779, 2.00251.

These orders are observations for the selected three grids, packets and windows. Small errors or cancellation do not change the formal order of the update.

Numerical Brewster and TIR evidence

Brewster case: at carrier incidence 63.4349°, finest-grid |rH,DFT|=0.000786266, finite-band reflected-fluence fraction 0.00113956, and spectral Fresnel reference 0.00113723. The monochromatic null and nonzero packet reflection are separate observations.

TIR case: carrier incidence 45°, critical angle 30°, and every input-band angle exceeds 31.6075°. Numerical rH=-0.777569-0.629054i. Right probes are x=40.75 and 41.5. Numerical κ=2.82793, finite-window reference κ=2.82867, ideal monochromatic κ=2.82843.

TIR net-T reference errors: 9.05206e-12, 1.12867e-11, 1.02261e-11; raw apparent orders: -0.318305, 0.142363. No order criterion is imposed on this tiny error floor. The signed transient transmitted-flux waveform has relative L2 errors 0.160827, 0.0399902, 0.0099802 and a separate refinement criterion.

Finest-grid maximum right stored energy / analytic incident energy is 0.0577621 at t=33.6529. The continuum reference at that time is 0.0577265, relative difference 0.000616712; final storage is 6.10545e-09. Right-monitor flux / incident energy ranges from -0.000223958 to 0.000220947, retaining its incoming/outgoing signs.

Finest-grid invariant, physical budget and normalization are distinct checks.CaseModified-energy driftLocal flux residual|R_W+T_W−1|Incident fluence / analytic energy errorpropagating5.55112e-166.40756e-058.52962e-120.000128161brewster6.66134e-167.98332e-053.80685e-070.000195978tir8.88178e-163.93668e-052.07714e-077.96698e-05Maximum relative reference-field change after period doubling at interaction/end times is 7.11693e-12; initial secondary-field squared weighted-norm fraction is at most 7.50501e-08. The analytic cap-Ey audit uses up to 2049 sample times per run, with maximum 0.000266315. These controls concern the specified window, rather than arbitrary long times or all angles.

The initial PEC clipping changes the squared weighted grid-field norm by a fraction at most 5.78842e-13. Initial-field, reference-quadrature and finite-window controls are retained separately in result JSON.

Download and reproduce revision r5

[](/numerical-methods-atlas/assets/fdtd-p-polarization.png)[p-polarization and TIR result JSON](/code/fdtd/2026-11-22-r5/results/p-polarization/result.json) · [spectrum.csv](/code/fdtd/2026-11-22-r5/results/p-polarization/spectrum.csv) · [convergence.csv](/code/fdtd/2026-11-22-r5/results/p-polarization/convergence.csv) · [energy.csv](/code/fdtd/2026-11-22-r5/results/p-polarization/energy.csv)[Revision-r5 ZIP: retained six cases plus p polarization, Brewster and TIR](/code/fdtd/2026-11-22-r5/fdtd-2026-11-22-r5.zip)

[Bilingual setup and execution](/code/fdtd/2026-11-22-r5/README.md)

[polarization.py](/code/fdtd/2026-11-22-r5/polarization.py)

[run_polarization.py](/code/fdtd/2026-11-22-r5/run_polarization.py)

[test_polarization.py](/code/fdtd/2026-11-22-r5/test_polarization.py)

[Fixed input and acceptance criteria](/code/fdtd/2026-11-22-r5/inputs/p-polarization.json)

[SHA-256 manifest](/code/fdtd/2026-11-22-r5/source-manifest.json)

[Unchanged earlier sources / provenance](/code/fdtd/2026-11-22-r5/provenance.json)

[85 tests passed / independent-extraction record](/code/fdtd/2026-11-22-r5/verification.json)



Full-clock complex monitor CSVs: [propagating](/code/fdtd/2026-11-22-r5/results/p-polarization/waveforms-propagating.csv) · [brewster](/code/fdtd/2026-11-22-r5/results/p-polarization/waveforms-brewster.csv) · [tir](/code/fdtd/2026-11-22-r5/results/p-polarization/waveforms-tir.csv)

python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py
python run_polarization.py --input inputs/p-polarization.json --output output-pIndependent ZIP extraction reran all tests and all seven inputs with identical metrics and every CSV. Numerical sources/tests of the old six inputs and four earlier editions are retained. This dedicated FDTD supplement is separate from common execution records and other fields’ verification counts.

Scope is the selected lossless/nonmagnetic planar interfaces, one periodic-y mode, finite bands and windows. Revision r5 is lossless; normal-incidence loss/dispersion is tested separately in r6. Anisotropy, arbitrary transverse spectra, 3D and PML absorption of evanescent fields remain outside scope.

Initial-edition downloads and reproductionOriginal vacuum edition: code and reproduction

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

Educational Yee FDTD: retained vacuum/Fresnel/s-p/PML examples plus r6 1D normal-incidence Ohmic and passive Lorentz slabs. Spectral references, R/T, direct dissipation, material storage, modified/physical budgets and space/time refinement are separate checks. Not blanket validation of general dispersion, multiple resonances, oblique dispersive incidence, dispersive PML or general 2D/3D.

## Sources

- Kane Yee (1966). Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. https://doi.org/10.1109/tap.1966.1138693
- Fadime Bekmambetova and Xinyue Zhang and Piero Triverio (2017). A Dissipation Theory for Three-Dimensional FDTD with Application to Stability Analysis and Subgridding. https://arxiv.org/abs/1705.02274v2
- Jean-Pierre Bérenger (1994). A Perfectly Matched Layer for the Absorption of Electromagnetic Waves. https://doi.org/10.1006/jcph.1994.1159
- Steven G. Johnson (2021). Notes on Perfectly Matched Layers (PMLs). https://arxiv.org/abs/2108.05348v1
- Markus Zahn (2003). Electromagnetic Field Theory: A Problem Solving Approach. https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/
- Meep developers (2026). Materials — Meep Documentation. https://meep.readthedocs.io/en/latest/Materials/
