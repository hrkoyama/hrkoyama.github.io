# Fixed small models: pre-execution protocol

This is the main pre-execution freeze. The separate reference stage has passed
92 checks; primary pytest, training, trajectories and plots have not yet run.
Python 3.12 and the exact
three requirements pins are used. No GPU, neural framework or new dependency is
required. One primary group has five scientific cases for logical candidates
84, 85 and 87; bibliographic candidate 86 adds **zero numerical cases**.

## Inputs, fields and work

Poisson: -u_xx=pi^2 sin(pi x), x in[0,1], homogeneous Dirichlet, all dimensionless.
The hard-boundary ansatz x(1-x)(b_out+sum a_j tanh(w_j x+b_j)) has49 real
parameters in w,b,a,out order. Three PCG64 seeds8401..8403 draw16wN(0,1), then
16bN(0,.5), then16aN(0,.25); outputbias0. Sixty-four training points j/65,
j1..64, are separate from257 midpoint evaluation points. Three FD2 baselines
have31/63/127 unknowns. Analytic parameter Jacobian is mandatory; no numerical
fallback, retries or test-set selection. The optimizer receives q=r/8,
r=(-u_xx-f)/pi^2, so reported L=mean(r^2)=2*SciPy cost. Actual fun and Jacobian
calls have separate hard300 caps, and optimizer status0..4 is recorded under the R2 rules below. Callback trials are not mislabeled accepted TRF steps.

FNO: u_t=nu u_xx on[0,2pi), periodic, T=.25. Forty-six complete functions use
PCG64(problemID), drawing three a then three b uniformly in[-1,1], each divided
by mode k. Exact input IDs and nu cycling are in data_family.py:24 training,
6 validation(reporting only),8 unseen ID tests,4 nu-OOD and4 spectrum-OOD.
The input channels are u0 and constant nu. Lift6 + two blocks42 each +
projection3 =93 real parameters. Each block has local W, bias, real DC R and
complex R for k1..4, followed by native-grid tanh. There is **no padding or
dealiasing**. ForwardFFT is unnormalized/inverse1N. High harmonics from local
and nonlinear branches remain. The same weights and physical frequencies are
evaluated at32 and64 points; restriction discrepancy is not continuum error.
Two PCG64 model seeds8501/8502 draw93N(0,.15). L-BFGS-B has maxiter120,
maxfun300,maxcor5,maxls20,ftol1e-12,gtol1e-8, no bounds. Actual combined
loss/gradient calls are counted independently of iteration count. Native optimizer convergence is an actual study goal, distinct from a normal
fixed-budget return. All last
returned models are retained, no seed/checkpoint/hyperparameter selection.
RMS means sqrt(mean(z^2)); relativeL2 applies only if exact RMS>1e-12.
Zero and1e-14 amplitude controls use absolute error and explicit relative NA,
with blank numeric CSV cells. OOD is diagnostic, without promised success,
worsening or arbitrary-distribution generalization.

Enzyme: all four S,C,E,P obey mass action E+S <-> C -> E+P, k1=10,
km1=kcat=1,S0=1,C0=P0=0,E0=.01/.002. Km=.2 and adopted epsilon is1/120 or
1/600. These are scale assumptions, not rigorous approximation error bounds.
Theta=E0*t, finaltheta=.5. Output is theta=j/200,j0..100, plus physical
1/12,5/12,20/12, exact floating union. Both original initial-layer and
all-time comparisons remain; theta>=.02 is a declared reporting window,
not a certified layer-end time. Each E0 has two adaptive SDIRK2 runs:
(rtol,atol)=(1e-6,1e-10)/(1e-8,1e-12). gamma=1-1/sqrt2. Stage Newton uses
fixed weights atol+rtol*abs(stage_start), same weightedLinf for true residual
and Armijo, tolerance1e-3 in that scaled norm; max10 updates and8 backtracks.
Each correction builds one actual4x4 factor/solve, no fictitious reuse.
Step doubling accepts two halfsteps, error=(two-full)/3, weightedLinf with
atol+rtol*max(abs(old),abs(two)). Safety.8/exponent-1/3/factors[.2,2], no growth
after rejection; ratio0factor2. Initialh=1/96, maxh=.005/E0; output endpoint
clipping is recorded. Caps20000 attempts/30 consecutive rejects. Failed
nonlinear stages are failures, not silent smaller-step retries. No clipping,
normalization or mass projection. Two separate reduced scalar RK4 runs use
200/400 theta steps; they are reused for both E0 comparisons, not counted twice.

LV: xdot=x(1-y),ydot=y(x-1), initial(1.2,.8), T20 and400/800/1600 RK4steps.
H=x-logx+y-logy is monitored only for positive states. No attracting limit
cycle claim. SEIR: beta=.6,sigma=.3,gamma=.2,N1, initial(E,I)=(eta,eta),
eta1e-4/5e-5,S=1-2eta,R0. T20 and400/800/1600 RK4steps. All four states
are evolved. The early reference includes the full2x2 exp(A t),
A=[[-.3,.6],[.3,-.2]], not a single dominant eigenmode. Nonlinear reference
and linearization use201 fixed points in[0,1]. Native RK4 points are not
silently interpolated. The two eta values are consistency diagnostics, not
statistical coverage. Overall15 biological primary trajectories are4full
zyme+2reduced+3LV+6SEIR. PINN3+FD3+FNO2 yield23 high-level main records.
FNO additionally saves116 per-problem/grid prediction rows.

## Separate reference and component stage:92 checks,30 seconds

The five full ODE systems use separately authored RHS/Jacobians, with LV in
log coordinates and SEIR in scaled deviation coordinates, and two Radau plus two variableBDF propagations each:
20 solves total. Tolerances1e-11/1e-13 then2e-12/2e-14. For SEIR these control
z=((S-1)/eta,E/eta,I/eta,R/eta), initially(-2,1,1,0). Its equations are
zS'=-.6(1+eta*zS)zI, zE'=.6(1+eta*zS)zI-.3zE,
zI'=.3zE-.2zI, zR'=.2zI. The scaled invariant is sum(z)=0;
zS is allowed to be negative. Only the transformed physical populations are
subject to positivity and sum-one checks. Physical conversion adds binary64
rounding near S=1; the same numerical tolerances in scaled variables give
finer effective physical resolution, not bit-equivalent old trajectories.
Every reference
Jacobian first passes independent complex-step at the fixed initial state.
Returned solver nodes/states and requested samples are saved before checks.
On an unexpected monolithic solve exception, last owned RHS/Jacobian callback
is saved; unreturned accepted history cannot be recovered. Max absolute
refinement/cross-engine difference1e-8, and SEIR additional difference
<=min(1e-10,1e-3*eta^2). Independent scalar Brent roots of
S+.2logS=1-theta qualify the reduced solution. Full2x2 analytic exponential
is checked against scipy.linalg.expm. Exact sine Poisson mode and actual
linear residual qualify FD; no reference borrows trained outputs.

Every49 PINN residual-Jacobian and loss-gradient coordinate is independently
complex-stepped at two fixed moderate/saturated fixtures; loss continuation
uses r*r, never abs/conjugation. Five endpoint/interior points and full64point
loss are distinct checks. Primary x derivatives are checked against an
independent exp-based expression. A five-point second difference at h=2^-9
on moderate parameters has frozen absolute allowance2e-6; using broad real
tanh derivative bounds 2^m*m! and the stated moderate weights gives a
sixth-derivative truncation allowance far below this threshold. The float
allowance is a fixed engineering check, not an interval certificate.

For FNO all93 REAL coordinate loss gradients use central differences at
h=2^-15 and2^-16 times max(1,abs(theta_j)), at two fixed small fixtures, plus
two normalized directions. Frozen scaled allowance5e-5 accounts for O(h^2)
truncation/roundoff; two steps are both required, not selected afterwards.
No universal correctly-rounded/AD proof is claimed. Full direct-DFT sums
independently qualify the native discrete Fourier block on two grids and six
fixtures, including phase/channel/highmode/DC/local/bias behavior. DC is
real, interior conjugate pairs have their real-coordinate contributions,
and generic complex-step through rfft/irfft is explicitly prohibited.
Negative sign/normalization/channel/column/product/half-cost controls remain.

The92 IDs are fixed in inputs.json: PINN11,FNO23,bio42,FD6,MM2,SEIRexp4,
LV3,split1. These counts are not primary gates or pytest counts. The cache
is installed only after92/92PASS with input/acceptance/seven dependency
hashes and every installed artifact SHA. Main and ZIP runs never regenerate
these references. Reference qualification imports the two neural primitives
for COMPONENT comparisons; it never calls their training functions or the
primary biological evolvers.

## Goals, reporting and evidence

Accuracy goals in acceptance.json are predeclared study targets, retained as
actual TRUE/FALSE values and measured/limit pairs. No expected-failure mask
is allowed and no small training loss substitutes for independent accuracy.
Required reproduction checks are qualified cache, complete finite records,
actual optimizer completion/work, split identity and finite raw data.
An abnormal optimizer failure, unreturned vector or actual hard-call-cap
overflow remains a required-check FAIL; a normal fixed-budget return is
classified explicitly below. A reporting PASS is
not a claim every numerical study goal was met. This policy is defined
BEFORE any measurement, not a post-failure waiver. Original inputs/goals
are never tuned after failed runs. Completed candidates and written checkpoints
are retained. Neural/enzyme exception handlers flush their owned contexts;
RK4 loop exceptions can lose unflushed state since the last 32-event checkpoint.
Recovery of every live stage/library internal is not guaranteed. SIGKILL
preserves only already written data.
The source main+tests share one externally enforced120-second budget;
reference30s and saved-data plotting60s are separate. Primary and plot runtimes
are UNMEASURED at this freeze. The separate successful reference attempt used
1.608417917 seconds; its 92 component checks are not main reproduction checks.

## R2 premeasurement optimizer policy (supersedes R1 success-required wording)

Before any numerical execution root reviewed this fixed-budget learning study.
All input/seeds/maxiter120/maxfun300/optimizer tolerances and accuracy goals
are unchanged. PINN permits status0..4 only and requires success==(status>0);
status0 must have actually consumed nfev300. FNO permits status0/success or
status1/no-success only when an explicit limit message and actual nit120 or
nfev300 establish the normal budget reason. Abnormal line search/status2,
negative status, exceptions, missing final vectors or actual callback-cap
overflow remain FAIL. Every native success boolean is saved as its own study
goal, including FALSE; a fixed-budget return is never called convergence.
This is a design revision before measurements, not a post-failure waiver.
The exact R1 source/11dependencies/plan/policy are preserved privately.
