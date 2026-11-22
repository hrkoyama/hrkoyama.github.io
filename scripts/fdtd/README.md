# Yee FDTD: TMz/TEz, interfaces, PML and dispersive loss / 界面・PML・損失分散
Revision r6 contains eight fixed inputs, adding normal-incidence Ohmic and
passive Lorentz slabs with directly measured absorption. The first sections retain the original
TMz vacuum examples; see each revision section for its added scope.
All five earlier frozen editions are preserved.

Original educational **two-dimensional TMz** Maxwell solver. Python 3.12;
NumPy performs the update, Matplotlib draws saved results, pytest runs tests.
Normalized units: epsilon=mu=c=1, unit electric-field amplitude, lengths
Lx=1 and Ly=1.5. No external solver supplies the numerical solution.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs/periodic-wave.json --output output-wave
python run.py --input inputs/pec-cavity.json --output output-cavity
```

Use a new or empty output directory. Exit status: 0 all numerical criteria pass,
1 numerical acceptance failed, 2 invalid input/runtime error. Fixed inputs
contain meshes, budgets and acceptance tolerances. Each execution saves
`result.json` (input SHA-256, environment, metrics, decisions, termination),
`convergence.csv`, `energy.csv`, `solution.csv` and `summary.png`.
The numerical field and analytic field in solution.csv are the final
**accuracy-time** electric fields, not the later end of the energy run.

## Model and staggered update / モデル・変数配置

The source-free equations are

    Hx_t = -Ez_y,  Hy_t = Ez_x,  Ez_t = Hy_x - Hx_y.

Ez lives at integer x,y nodes and integer times; Hx at (x,y+dy/2), Hy at
(x+dx/2,y), both at half times. A state contains E(n dt) and H((n-1/2)dt).
Update H first from spatial forward differences of E, then E from backward
differences of the new H. Periodic arrays wrap without duplicate endpoints.
For the cavity, E includes the wall nodes, which are exactly zero; normal H
wall values are zero for the chosen mode. The spatial inner product uses
cell-area quadrature and half weights on the cavity's boundary nodes.

The strict input condition is dt sqrt(dx^-2+dy^-2)<1. The equality endpoint
is rejected, so the modified-energy quadratic form remains coercive. Rejection
of an invalid time step is not an experimental measurement of unstable growth.

## Independent continuum solutions / 連続解析解

For the periodic traveling wave, k=(2 pi/Lx,2 pi/Ly), omega=|k|:

    Ez = cos(kx x+ky y-omega t)
    Hx = (ky/omega) cos(kx x+ky y-omega t)
    Hy = -(kx/omega) cos(kx x+ky y-omega t).

For the PEC standing wave, k=(pi/Lx,pi/Ly), omega=|k|:

    Ez = sin(kx x) sin(ky y) cos(omega t)
    Hx = -(ky/omega) sin(kx x) cos(ky y) sin(omega t)
    Hy = (kx/omega) cos(kx x) sin(ky y) sin(omega t).

Initial H is sampled from these continuum solutions at -dt/2, separately at
the Hx and Hy positions. Compare all components at their own staggered
positions/times after **1.1 analytic periods**. Meshes 16x24,32x48,64x96
and Courant factor 0.7 refine both space and time. The time step is reduced
slightly to reach the same physical accuracy end time on each mesh. Combined
L2 error is normalized by the constant continuum total field norm: Area for
the periodic wave, Area/4 for the cavity. Report E and H errors with that
same common normalization, avoiding divisions by temporal nodes of E or H.

Field refinement checks at least order1.8 and finest error<=0.01. The source
also measures frequency from the evolved electric-mode amplitude a(n) through

    cos(Omega dt) = sum a(n)[a(n-1)+a(n+1)] / [2 sum a(n)^2].

This is an oscillator-recurrence measurement, not an FFT estimate or an
independent field solver. Compare it separately with the continuum omega and
the exact Yee dispersion relation

    sin(Omega dt/2)^2/dt^2
      = sin(kx dx/2)^2/dx^2 + sin(ky dy/2)^2/dy^2.

The discrete-frequency identity is not the physical accuracy criterion:
physical frequency error and its second-order refinement are separate checks.

## Energy and divergence / エネルギー・発散

Run **12 analytic periods** at every mesh. With H-=H(n-1/2), H+=H(n+1/2),
the source-free periodic/PEC scheme conserves the modified discrete energy

    U* = (||E(n)||^2 + <H-,H+>)/2.

The physical-energy diagnostic reconstructs H at E's time:

    Hbar=(H-+H+)/2,
    Ucentered=(||E(n)||^2+||Hbar||^2)/2,
    Ucentered-U* = ||H+-H-||^2/8.

Thus Ucentered is generally **not exactly conserved**. Compare it with
the continuum integrated energy Area/2 (periodic unit traveling wave) or
Area/8 (PEC unit standing wave). Check maximum absolute relative energy
error and its grid/time refinement; the span is reported separately and
may superconverge for a traveling mode. Acceptance: modified-energy relative
drift<=2e-11, finest physical-energy error<=0.003, physical-energy error
refinement>=1.8. The normalized model has no source or boundary energy flux.

The scheme preserves the **initial discrete divergence**. Sampling continuous
oblique H generally gives an initial O(h^2) discrete divergence residual;
the result reports it and checks its subsequent absolute change<=2e-10.
Do not read this as absolute magnetic divergence zero. Separate exact
discrete-mode tests use discrete derivative symbols in H amplitudes and
verify divergence near roundoff. Random multimode periodic/PEC tests check
the energy and divergence identities beyond a single eigenmode.

## 日本語の要点

真空・一様媒質の2次元TMzに範囲を限定します。周期境界の斜め平面波と、
完全導体長方形空洞の定在波を、同じYee更新で計算します。連続解析解との差、
格子と時間の同時細分化、実測した振動数、離散分散関係、12周期のエネルギーを
別々に判定します。電場・磁場の位置と時刻のずれを参照解にも反映します。

厳密に保存される離散修正エネルギーと、磁場を同時刻へ平均した物理エネルギーを
区別します。初期離散発散の保存は、発散の絶対値がゼロという主張ではありません。
各許容値はJSON入力で固定し、失敗を成功として記録しません。

初版の真空2例はPML・媒質界面を含みません。以下の第2版の追加範囲を参照してください。
分散媒質、電荷・電流、TEz、3次元、任意形状、一般励起や実験比較は未検証です。

## Sources and terms / 出典・利用条件

- K. S. Yee (1966), original staggered-grid formulation:
  https://doi.org/10.1109/TAP.1966.1138693 . Bilingual atlas cites the paper;
  no third-party article text is included in this source package.
- F. Bekmambetova, X. Zhang, P. Triverio, *A Dissipation Theory for
  Three-Dimensional FDTD with Application to Stability Analysis and
  Subgridding*: https://arxiv.org/html/1705.02274v2 , Section III, equation26
  (modified discrete energy) and equation35 (strict CFL). The current 2D
  specialization is verified independently by random-field tests.

Original code: MIT, see LICENSE. Inputs, generated outputs, figures and prose
retain item-specific terms at https://hrkoyama.github.io/rights/ . Dependencies
retain their own licenses. This is an educational implementation with the
scope above, not a general electromagnetic simulation package.

## Revision r2: dielectric interface and x-PML / 第2版：媒質界面とPML

The original two vacuum recipes above remain byte-for-byte identical in their
solver, runner, tests and fixed inputs. The following **separate** educational
extension uses `scattering.py` and `run_scattering.py`:

```sh
python -m pytest -q test_fdtd.py test_scattering.py
python run_scattering.py --input inputs/dielectric-interface.json --output output-interface
python run_scattering.py --input inputs/pml-pulse.json --output output-pml
```

The previous exclusions above describe the original vacuum recipes. This
revision additionally implements a lossless, nonmagnetic dielectric interface
at **normal incidence**, and a genuine Berenger split-field PML on the two
**x sides** of a 2D TMz strip periodic in y. It does not implement oblique
material-interface Fresnel scattering, y-side/corner PML, dispersive matter,
gain, general sources, TEz, three-dimensional geometries or experimental data.

For epsilon1=1, epsilon2=4 and mu=1, the analytic electric-field coefficients
are r=-1/3 and t=2/3; power/packet-energy coefficients are R=1/9 and T=8/9.
The electric node on the interface uses the arithmetic permittivity average.
Reflected and transmitted packet energies and amplitude errors are measured
separately against the continuum Gaussian/Fresnel solution. R+T=1 and the
closed-domain modified-energy invariant provide distinct balance checks.

The PML evolves E=Ex+Ey with x-directed damping on Ex and Hy, with matched
rates sigma_e/epsilon=sigma_m/mu=gamma(x), and trapezoidal damping in time.
This is an anisotropic split-field matched layer, not an isotropic lossy
sponge. Layer physical thickness, profile order and strength stay fixed under
refinement; increasing cell count alone does not change their physical values.
The fixed pulse spectrum has positive longitudinal wave numbers and ky=0 or8;
its carrier kx=12 gives angles0 and approximately33.690 degrees. A finite-band
pulse is not a single-angle monochromatic wave. The straight interface example
is y-invariant; the ky=4 PML example exercises the full two-dimensional update.

PML reflected signals are compared with a larger same-grid lossless reference
whose boundaries do not return within the measurement window. This isolates
boundary error, but is not an independent external FDTD solver. Early fields
also have an independently evaluated finite superposition of continuum Fourier modes.
The final PML meshes are384x16,768x32,1536x64; reflected-waveform phase error
was nonasymptotic on coarser trials, which were retained as diagnostics.
Interface field/reflected-amplitude errors approachsecondorder; transmission
amplitude has leading-error cancellation, so all its pairwise orders are
reported rather than assuming each is2.
The finite PEC-backed layer also has an analytic single-bounce reflected
Fourier-packet reference: each kx mode has electric reflection factor
-exp[-2 (kx/omega) G], where G=gamma_max*thickness/(order+1).
Raw return amplitude can converge to a nonzero physical finite-layer value;
grid refinement is checked for the waveform error against this analytic
return, rather than requiring raw reflection to converge to zero.
The code reports reflection amplitude separately from a squared-amplitude
power diagnostic; these are distinct from the interface's integrated packet
energy fractions. Consult fixed inputs and result JSON for the exact windows,
normalization, convergence series and acceptance thresholds.

The PML work is computed directly from old/new electric split fields and
three consecutive magnetic half times. It is **not defined as minus the
energy change**. Electric split-field work can be locally signed; it must not
be called pointwise positive physical Ohmic heating. The discrete modified
energy plus accumulated signed electric/magnetic PML work is checked against
its initial value. A separate physical-domain Poynting-flux diagnostic checks
outgoing energy. The vacuum coercivity claim above is not automatically a
positivity theorem for arbitrary strongly damped auxiliary split fields.

第2版では、初版の真空2例を保持したまま、垂直入射の誘電体界面と、y周期の
2次元TMz帯領域の左右x方向PMLを追加しています。界面では振幅r,tと
パケットエネルギーR,Tを区別し、解析的Fresnel解・R+T・格子収束を確認します。
PMLでは垂直・斜めのパルスを使い、広い領域の同じYee法との差から境界反射を
測ります。別の連続Maxwell方程式の有限Fourierモード和との比較も行い、境界誤差と伝播誤差を分けます。

PML厚さ・減衰強度は物理単位で固定して格子を細分化します。PMLの電場・磁場の
仕事は場と係数から独立に集計し、修正離散エネルギーとの収支を照合します。
符号付きの計算上の仕事を媒質の正の発熱とは呼びません。四辺・角のPML、
媒質界面への斜め入射、分散媒質・3次元への一般化は別の検証が必要です。

Additional sources, with access-depth notes in the bilingual chapter:

- J.-P. Berenger (1994), *A Perfectly Matched Layer for the Absorption of
  Electromagnetic Waves*, https://doi.org/10.1006/jcph.1994.1159 . Bibliography
  and abstract checked; original full text was not inspected.
- S. G. Johnson (2021), *Notes on Perfectly Matched Layers (PMLs)*,
  https://arxiv.org/html/2108.05348v1 , selected sections4 and7 inspected.
- M. Zahn, *Electromagnetic Field Theory: A Problem Solving Approach*,
  2003 corrected reprint, Chapter7 sections7-6-1/7-6-2 (MIT OpenCourseWare).
  Textbook exposition of normal-incidence continuity and power normalization.

## Revision r3: four-side and corner PML / 第3版：四辺と角のPML

The original vacuum, dielectric-interface and x-PML code, tests and four fixed
inputs are retained unchanged from r2. The added `corner.py`, `run_corner.py`
and `test_corner.py` implement a vacuum TMz square with matched split PML
on all four sides, simultaneous x/y damping in corners, and outer PEC caps.

```sh
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py
python run_corner.py --input inputs/pml-corners.json --output output-corners
```

E=Ex+Ey uses auxiliary electric splits: Ex damps at gamma_x and Ey at gamma_y;
Hy damps at gamma_x and Hx at gamma_y. Each rate is sampled at that component's
own Yee location. Magnetic updates precede the electric update; damping uses
the trapezoidal rule. Both directional rates are active in the overlap corners.
The work identity separately tallies electric x/y and magnetic x/y terms from
fields and coefficients. It is not obtained by defining work as energy loss.
As in r2, signed auxiliary-field work is not pointwise physical Ohmic heating.

Separate outgoing-packet families test ordinary sides and oblique corner paths.
Reported checks distinguish early-field accuracy, boundary-return error, work
balance, physical-interior Poynting flux and grid refinement. The input JSON
fixes layer thickness/strength, packet spectrum, grids, windows and numerical
acceptance criteria; result.json records every decision and reference scope.
Read the bilingual chapter for the controlled reference and measured errors.
Finite thickness, initial tails and finite observation time limit any claim of
reflectionlessness; corners do not make the PML an exact discrete absorber.

第3版では、四辺すべてにPMLを置き、四つの角でx・y両方向の減衰を同時に適用します。
辺へ向かう波と角へ向かう斜め波を区別し、反射・エネルギー仕事・内側領域の流束・
格子収束を別に判定します。旧4入力は変更せず、新しい固定入力pml-corners.jsonを
追加します。四辺の外端はPECで、分散媒質、媒質界面への斜め入射、3次元への拡張は
この例で検証したことにはしません。

Johnson's PML notes, section3.4, explicitly discuss independent directional
coordinate stretches and simultaneous conductivities at corners:
https://arxiv.org/html/2108.05348v1 . The current discrete updates and work
identity are independently tested; no external FDTD solver is bundled.

## Revision r4: oblique dielectric incidence / 第4版：媒質界面への斜め入射

The new `oblique.py`, `run_oblique.py` and `test_oblique.py` extend the
interface validation to finite-band oblique packets. All earlier numerical
source, tests and five fixed inputs remain byte-for-byte unchanged. The
existing lossless Yee update in `scattering.py` supplies the numerical fields.

```sh
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py
python run_oblique.py --input inputs/dielectric-oblique.json --output output-oblique
```

The interface is normal to x, periodic in y, with positive constant epsilon
on each side and mu=1. Ez is perpendicular to the xy plane of incidence:
this TMz convention corresponds to optical **s/TE polarization**, not the
optical p polarization. A normal-incidence packet is a separate control.
The x caps are PEC and the chosen observation window precedes their main
return; this experiment does not combine material scattering with PML loss.

For each positive incident longitudinal wave number k and fixed transverse
wave number ky, frequency and ky agree across the interface:

    omega = sqrt((k^2+ky^2)/epsilon1)
    q = sqrt(epsilon2*omega^2-ky^2)
    r_s = (k-q)/(k+q),  t_s = 2*k/(k+q)
    R_s = r_s^2,  T_s = (q/k)*t_s^2,  R_s+T_s=1.

These formulas assume propagating transmitted waves. Electric and magnetic
fields are evaluated as a Fresnel spectral superposition at their own Yee
positions and times. The finite quadrature is a continuum reference, not
another time-stepping solver. Its doubled quadrature period controls sampling
error at the final field-comparison time and in the packet-energy integrals;
it does not make the refracted packet periodic in x.

For A(k)=width/sqrt(2*pi)*exp[-width^2*(k-k0)^2/2], coefficients
a_m=A(k_m)*dk and dk=2*pi/P, incident energy is
Uinc=pi*epsilon1*Ly*integral_0^infinity |A(k)|^2 dk, approximated by
(epsilon1*Ly*P/2)*sum_m a_m^2.

Packet energy R and T use incident spectral-energy weights. They differ from
the coefficients at the carrier angle. The transmitted-coordinate Jacobian
dq/dk=(epsilon2/epsilon1)*k/q gives the same T_s factor above. Saved results
distinguish carrier r/t and Snell angles, broadband template gains (whose
analytic target is 1), field-shape errors, and integrated packet energies.
The reference R/T quadrature and finite-box field-energy checks have distinct
roles. Consult the input and chapter for actual parameters and tolerances.

The checks separately assess continuum field error, reflected/transmitted
packet energies and their refinement, global modified-energy conservation,
physical-region Poynting-flux balance, reference quadrature and initial/cap
tails. A small R+T closure error alone does not establish agreement with
Fresnel scattering. The interface electric node retains the arithmetic
permittivity average. Grid and time refinement preserve the physical packet.

第4版では、無損失・非磁性の平面誘電体界面へ有限帯域の波束を斜めに入射させます。
このTMz配置のEzは光学のs偏光です。Fresnel解析解を各スペクトル成分へ適用し、
中心角の係数、波束全体の反射・透過エネルギー、解析波形に対する振幅倍率と形の
誤差を分けます。連続参照の場・格子収束・修正離散エネルギー・Poynting流束に加え、
参照積分の細分化と初期場・外端の微小な裾も確認します。旧5入力と旧3配布版を保持します。

Scope is the selected s-polarized, propagating, lossless/nonmagnetic packets
and finite time window. Optical p polarization, Brewster-angle behavior,
total internal reflection, lossy/dispersive matter and 3D need separate tests.
Zahn's textbook, Chapter7 section7-9-1 (pp538–540), supplies the oblique
boundary conditions, Snell law and s-polarized amplitudes; notation is adapted
so lowercase r/t denote amplitudes and uppercase R/T denote energy fractions.

Primary textbook section inspected for r4:
https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/85a1dfee83863a0bad0dee5c7305ec30_MITRES_6_002S08_chapter7.pdf#page=52

## Revision r5: p polarization, Brewster and TIR / 第5版：p偏光・Brewster角・全反射

The new `polarization.py`, `run_polarization.py` and `test_polarization.py`
implement TEz (Hz,Ex,Ey). Hz is perpendicular to the xy incidence plane,
so this convention corresponds to optical **p polarization**. All earlier
TMz numerical source, tests and six fixed inputs are retained unchanged.

```sh
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py
python run_polarization.py --input inputs/p-polarization.json --output output-p
```

The full 2D Yee update places Hz at cell centers and integer times, and Ex/Ey
on their respective edges at half times. A planar dielectric interface uses
native material permittivity at normal Ex edges and arithmetic permittivity
averaging at the interface's tangential Ey edge. The interface inverse
permittivity is the harmonic mean of the two side inverse permittivities. x caps are PEC; y is periodic.

For the fixed experiments, an exact single-ky Fourier reduction executes the
same Yee stencil. Its transverse derivative uses Ky=2*sin(ky*dy/2)/dy, not
the continuum ky. Full 2D comparisons test equivalence, while the fixed runs
refine both dx and dy. For resolved positive ky, the real field's y integral
is Ly/2 times the complex-amplitude inner product. This restricted benchmark
does not exercise arbitrary transverse spectra or a general two-dimensional
material geometry.

The time convention is exp[i(kx*x+ky*y-omega*t)], with mu=1. For incident k>0:

    omega^2 = (k^2+ky^2)/epsilon1
    q = sqrt(epsilon2*omega^2-ky^2), Re(q)>=0, Im(q)>=0
    r_H = (k/epsilon1-q/epsilon2)/(k/epsilon1+q/epsilon2)
    t_H = 1+r_H
    R = |r_H|^2
    T = (epsilon1/epsilon2)*Re(q)/k*|t_H|^2.

These are **Hz amplitude** coefficients. Electric components follow
Ex=-ky*Hz/(omega*epsilon), Ey=kx*Hz/(omega*epsilon), with signed or complex
kx for reflected or evanescent fields. This avoids confusing a tangential
electric-component sign with the chosen p-polarization amplitude convention.

At the monochromatic Brewster angle tan(theta_B)=sqrt(epsilon2/epsilon1),
r_H=0. A finite-band packet with its carrier at this angle generally has
nonzero integrated reflection. The source records its actual spectrum and
compares packet diagnostics with the spectral Fresnel reference separately
from the carrier's zero.

The TIR input has explicitly compact spectral support wholly beyond the
critical angle. Every transmitted mode uses q=i*kappa and decays into medium2.
Its monochromatic normal time-average transmission is zero, although its
evanescent field and transient stored energy are nonzero. Finite-window right
energy is not labeled transmittance. Phase, decay and signed transient flux
are distinct diagnostics; consult the saved input and result for windows and
reference controls.

The magnetic-packet incident Parseval energy is
Uinc=pi*Ly*integral |A_H(k)|^2 dk, with **no epsilon1 factor**. The global
modified energy uses H at an integer time and the epsilon-weighted product
of adjacent E half times. Centered physical energy and directly evaluated
Sx=Ey*Hz supply a separate approximate flux balance. No PML is used here.

Numerical reflected fields are isolated with a homogeneous-medium run of the
same Yee stencil; this removes ordinary incident-wave dispersion from a weak
Brewster return. Continuum Fresnel fields and fluxes remain a separate
analytic comparison. Finite-window fluence and Fourier diagnostics include
controls for temporal truncation, initial tails and outer-cap effects.
Field accuracy is assessed at a saved time during interface interaction;
the fluence and energy run continues to a later end time. The end-time field
error remains a diagnostic. Fourier-amplitude and evanescent-decay refinement
use the continuum reference evaluated through the same finite window, with
its difference from the ideal carrier coefficient recorded separately.
The nearly zero TIR net-transmission error can reach a cancellation/tail floor;
its raw errors and apparent orders remain recorded. Refinement acceptance for
TIR instead uses the signed transient transmitted-flux waveform's relative L2
error, alongside the unchanged net-transmission accuracy check. Propagating
transmission retains the fluence-fraction refinement check.

第5版はTEz（Hz,Ex,Ey）を追加し、光学のp偏光を扱います。固定例はy周期の
単一接線波数へ厳密に縮約したYee更新で実行し、一般の2次元更新との一致を別に
検査します。Brewster角の単色波のゼロと有限帯域波束の残留反射、全反射での
エバネッセント場・一時的な蓄積エネルギー・正味法線流束を区別します。
既存のTMzの6入力と4配布版は変更しません。

Scope is the selected lossless, nonmagnetic planar-interface packets and
single transverse Fourier modes. Loss/dispersion, anisotropic media, arbitrary
transverse spectra, 3D and evanescent PML absorption need separate validation.
Zahn Chapter7 sections7-9-3/7-9-4 (printed pp541–544) provide the critical
angle, evanescent-field interpretation, p-polarized amplitudes and Brewster
condition. Its time convention is adapted explicitly in the formulas above.

## Revision r6: Ohmic loss and Lorentz dispersion / 第6版：損失・分散媒質

This addition is a **one-dimensional, normal-incidence**, nonmagnetic,
linear passive vacuum–slab–vacuum benchmark. It evolves Ez, Hy and, inside
an optional single-resonance Lorentz material, polarization P and current J.
Distant PEC caps close the domain; this addition does not combine dispersive
material with a PML or claim arbitrary two-dimensional material support.
The seven earlier inputs, numerical sources/tests and five frozen releases
remain unchanged.

With time dependence exp(-i omega t), normalized mu=epsilon0=1, the model is

    eps_inf E_t = H_x - sigma E - J,  H_t = E_x,
    P_t = J,  J_t = f E - omega0^2 P - gamma J,
    f = delta_eps * omega0^2,
    eps(omega) = eps_inf + f/(omega0^2-omega^2-i gamma omega)
                         + i sigma/omega.

Here sigma is the conventional **E-current conductivity**, not Meep's
D-conductivity parameter. eps_inf>0, sigma>=0, f>=0 and gamma>=0 define
passive inputs. With f=0, P=J=0 and the material-energy term is omitted.
The square-root refractive index has nonnegative real and imaginary parts.
A finite slab uses both interface reflections, its internal phase and damping;
a single-interface Fresnel coefficient does not describe its total R/T.
Both external media are vacuum, so R=|r|^2 and T=|t|^2. A separate spatial
integral of the analytic internal-field dissipation checks A=1-R-T.

E,P,J occupy integer times; H occupies half times. After the explicit Yee H
update, a **local implicit midpoint** solve advances the coupled E,P,J.
Material coefficients at an interface E node use half-volume averaging;
P/J are polarization/current densities on the same control volume. The
strict Yee CFL uses the minimum eps_inf. Energy passivity of this midpoint
oscillator does not remove its time-resolution requirement.

For complex quadrature fields, squared norms below mean modulus squares and
products mean real Hermitian products. These fields represent a pair of real
quadratures; all energies and fluxes use the same convention. With H- and H+
adjacent to E^n, the closed-domain identity is

    U* = (||E||_eps_inf^2 + Re <H-,H+>)/2
           + sum_active (|J|^2+omega0^2 |P|^2)/(2f) dx,
    W_sigma += dt sum sigma |E_mid|^2 dx,
    W_gamma += dt sum_active gamma |J_mid|^2/f dx,
    U*(t) + W_sigma(t) + W_gamma(t) = U*(0).

Each W is accumulated **directly from the midpoint fields**, independently
of the energy deficit or R/T. Material storage is the positive oscillator
energy, not absorbed energy. Centering H gives a physical field-energy
diagnostic that differs from U* by ||H+-H-||^2/8. Physical local Poynting
balances therefore have a discretization residual separate from the exact
modified-energy/work identity.

The saved finite-band incident spectrum is propagated through the complex
slab solution for the continuum comparison. Monochromatic coefficients,
packet-weighted asymptotic R/T/A, finite observation windows and residual
stored energy are distinguished. A same-Yee vacuum control isolates the
reflected packet. Fixed inputs specify all meshes, clocks, quadrature and
acceptance criteria; CSVs retain the measured fields/work and errors rather
than only pass/fail labels. Spatial/time refinement, normalization, initial
and outer-cap tails and reference controls are separate checks. See the
input, result JSON and bilingual chapter for the exact measured limits.

```sh
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py test_dispersive.py
python run_dispersive.py --input inputs/loss-dispersion.json --output output-loss
```

第6版は真空に挟まれた有限厚の媒質板への垂直入射を扱う一次元検証です。
導電電流sigma Eと単一共鳴Lorentz分極を局所陰的中点法で更新します。
反射・透過の流束、電場と分極電流から直接積算した二種類の散逸、媒質内部の
振動子エネルギーを別々に記録します。解析的な板の多重反射解、内部場の散逸積分、
修正離散エネルギー恒等式と物理Poynting収支を照合し、格子・時間収束を調べます。
一般の分散媒質、斜め入射、分散媒質とPMLの併用、Drudeモデル、異方性や3次元の
包括的な検証ではありません。旧7入力と過去5配布版は保持します。

Reference access: Meep developers, *Materials*, official documentation,
“Material Dispersion”, “Loss and Gain”, and “Conductivity and Complex ε”
(HTML consulted 2026-11-22), https://meep.readthedocs.io/en/latest/Materials/ .
This supplies the Lorentz model and sign conventions, not an external solver
comparison or the midpoint algorithm used here. Zahn Chapter7 sections7-2-1
and7-6-3 supply supporting conductivity/complex-wave and conducting-interface
context. The implemented midpoint update and its discrete balance are derived
and independently tested for this benchmark.
