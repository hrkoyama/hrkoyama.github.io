Selected sources and exact read scope are recorded in citations.json/source-review.json. No third-party solver was run or source copied. Derived analytic/manufactured fields are explicitly distinguished from historical benchmark reproduction.

Scalar PDE: q_t+0.7q_x=0, periodic x in[0,1], q0=1+0.2sin(2pi x).
The prescribed map is x(xi,t)=xi+0.2/(2pi)sin(2pi xi)sin(2pi t),
so w=x_t=0.2sin(2pi xi)cos(2pi t), J=1+0.2cos(2pi xi)sin(2pi t)>0.
The exact moving-cell integral is Delta x minus0.2/(2pi) times
the difference of cos(2pi(x-0.7t)). Actual unknowns are the cell
integrals, with flux(0.7-w) q_upwind. Geometry and integrals share
both Heun stages. For q=1 the flux difference equals the changing
cell width at both stages, establishing the discrete GCL without a
posterior repair. DOP853 independently integrates the same joint
geometry/FV ODE for the temporal probe; this is not a separate spatial
PDE engine. Its tolerances1e-10 and1e-12 must agree within the fixed
qualification bound. Spatial errors use the exact analytic integrals.

Linear rotating SWE: eta_t=-u_x-v_y, u_t=v-eta_x,
v_t=-u-eta_y, with g=H=f=1 on a periodic unit square. eta is at
cell centres, u at east faces, v at north faces. The RHS is evaluated
on actual2D arrays using C-grid differences and adjoint four-point
velocity interpolations. RK4 time-advances these arrays.
For a staggered Fourier amplitude the separate analytic matrix is
L=[[0,-ik,-il],[-ik,0,C],[-il,-C,0]], with
k=2Nsin(pi m/N), l=2Nsin(pi n/N), C=cos(pi m/N)cos(pi n/N).
Continuous reference instead uses k=2pi m,l=2pi n,C=1.
Only the reference uses a3x3 matrix exponential; no numerical field
is advanced by a symbol. Separate temporal refinement probes RK4
against the semidiscrete reference; spatial refinement compares the
actual field with the continuous PDE. Energy is0.5 mean(eta²+u²+v²),
and actual-stencil RHS adjointness is checked on both the runs and
unstructured random arrays. The discrete steady mode has amplitudes
[a,-il a/C,ik a/C]. The uniform mode probes f-plane inertial motion.
These are planar linear first-stage tests, not a nonlinear global
Williamson or ALE Saltzman calculation.
