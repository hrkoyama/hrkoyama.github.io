# Automatic differentiation: derivatives for numerical solvers

Automatic differentiation: derivatives for numerical solvers


Automatic differentiation (AD) evaluates derivatives by applying the chain rule
to the elementary operations in a program. It supplies Jacobians for Newton
iterations, directional derivatives for Krylov methods, and sensitivities for
parameter estimation. These are shared numerical foundations across many
physical models.


Implemented here: a small forward-mode dual-number engine and a comparison
of analytic differentiation, finite differences and AD on the existing Bratu
boundary-value problem. The experiment reuses the atlas's Armijo-damped Newton
solver. Reverse mode, implicit sensitivities and adjoints are explained as
connections; this exhibit does not implement them.


Four ways to obtain a derivative


An analytic derivative is derived mathematically and entered into the
solver by hand. It can expose structure and provide an independent reference,
but the derivative must be kept consistent with the residual implementation.
Symbolic differentiation manipulates expressions into another expression.
AD instead carries numerical derivative information through the evaluated
operations, without constructing a global symbolic formula.


Finite differences estimate a derivative from perturbed function values.
For a vector residual F and a direction v, forward and centered differences are



$$
D_\varepsilon^+F(u)v=\frac{F(u+\varepsilon v)-F(u)}{\varepsilon},
\qquad
D_\varepsilon^0F(u)v=\frac{F(u+\varepsilon v)-F(u-\varepsilon v)}{2\varepsilon}.
$$
For sufficiently smooth F, their truncation errors are first and second order
in ε. A very small ε amplifies cancellation and rounding in the residual
evaluations. The useful step depends on the state, direction, precision and
scaling of F. A finite-difference check should therefore sweep several steps.


AD has no finite-difference step or associated truncation error. It still uses
floating-point arithmetic: unstable formulas, overflow, underflow and rounding
can affect both values and derivatives. The differentiated object is the
composition of real-arithmetic operations represented by the executed program,
evaluated numerically. It is not the derivative of the discontinuous mapping
from one set of floating-point bit patterns to another.


Forward mode: carry a value and a direction


Seed the input with a direction v and propagate pairs consisting of a value
and its directional derivative. Dual-number notation makes the chain rule
visible:



$$
\widehat a=a+\eta\dot a,\qquad \eta^2=0,
\qquad
\widehat a\widehat b=ab+\eta(\dot a b+a\dot b),
\qquad
\exp(\widehat a)=\exp(a)+\eta\exp(a)\dot a.
$$
The nilpotent symbol η is an algebraic device, not a small numerical step.
The implementation stores the two arrays separately. It overloads the small
set of operations needed for this experiment, including elementwise
arithmetic, indexing, exponentiation and multiplication by a constant matrix.
Unsupported operations are outside this educational engine's scope.


For F from n inputs to m outputs, one seeded execution returns F(u) and J(u)v.
This Jacobian–vector product (JVP) avoids storing an m-by-n Jacobian. Seed
each coordinate basis vector in turn to assemble all n columns. The Bratu
comparison deliberately uses that transparent assembly; it does not exploit
sparsity coloring or provide a matrix-free Newton solver.


Reverse mode and the derivative you actually need


Reverse mode propagates an output weight w backwards through local derivative
rules to obtain J(u)ᵀw, often called a vector–Jacobian product (VJP). For
a scalar objective with many parameters, one reverse pass can produce its
gradient. An implementation commonly retains intermediate values or
recomputes them through checkpointing. Forward mode is attractive when only
a few input directions are required. The relevant dimensions are the numbers
of independent inputs and outputs, together with the requested products.


A Hessian–vector product for a smooth scalar objective can be obtained by
differentiating its gradient in a direction. Explicitly assembling a Hessian
is unnecessary when an optimization method only needs that product. See
[Baydin et al. (2018)](https://www.jmlr.org/papers/v18/17-468.html) for an AD
survey and the [JAX autodiff cookbook](https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html)
for practical JVP, VJP and higher-order constructions. JAX is a reading
reference; the local experiment requires only the atlas's existing NumPy
environment.


The existing Bratu problem


We retain the same sign convention, parameter and exact solution used in the
[sparse and nonlinear systems](/numerical-methods-atlas/en/read/sparse-nonlinear/) verification:



$$
-u''(x)-\lambda e^{u(x)}=0,\qquad 0Here n denotes the number of interior unknowns. The interval has n+1
uniform cells, with h=1/(n+1) and nodes x_i=ih. Centered differences give



$$
F_i(u)=\frac{2u_i-u_{i-1}-u_{i+1}}{h^2}-\lambda e^{u_i},
\qquad u_0=u_{n+1}=0,
$$

$$
J(u)=D-\lambda\operatorname{diag}(e^u),
\qquad D=\frac{1}{h^2}\operatorname{tridiag}(-1,2,-1).
$$
The analytic Jacobian is an independent formula. Finite differences and AD
both evaluate the same residual function. In particular, AD differentiates
the discrete residual F; it does not remove the centered stencil's spatial
discretization error. The exact continuous solution is used to check spatial
refinement, not as an exact root of the discrete equations.


Verification: hold the problem fixed





The [saved measurements and source hashes](/numerical-methods-atlas/assets/autodiff-bratu.json) separate
three checks so that accurate derivatives and accurate PDE solutions are not
confused.


The derivative check uses n=31 and the state u_*(x_i)+0.05 sin(3πx_i), away
from the exact continuous profile. Its direction is sin(2πx_i)+0.3 cos(5πx_i),
normalized to unit Euclidean length. The sweep contains 29 logarithmically
spaced, absolute perturbations from 1 down to 10⁻¹⁴; these are derivative
perturbations, not spatial mesh widths.



Differentiate at a fixed state. Compare the assembled forward-mode AD
Jacobian and its JVP against the analytic formula. Sweep finite-difference
steps at that same state, using both forward and centered differences.
Report relative Frobenius errors for matrices and relative Euclidean
errors for directional products. A deterministic smooth direction prevents
run-to-run changes in the comparison.


Solve the same discrete system. Start every Newton solve at zero, use
the same residual, Armijo search, dense linear solve and residual tolerance,
and change only how the Jacobian is supplied. The finite-difference run
uses a fixed centered-difference step recorded in the manifest. Measure
the true residual after each accepted iteration and compare the final
roots with the analytic-Jacobian solve.


Refine the mesh. Repeat the three methods for n=15, 31 and 63 interior
nodes. Compare their roots with u_* at the interior nodes using a nodal
maximum error. Approximately fourfold error reduction under halving h
identifies the centered scheme's second-order spatial behavior.



In the saved run, AD and the analytic Jacobian agree entry by entry, while
the relative JVP error is about 8×10⁻¹⁶. This exact matrix agreement is
specific to the operation ordering in this example, not a general guarantee
of bitwise agreement for AD. The finite-difference curves show the useful
range between truncation error and cancellation. All nine Newton solves
reach the common absolute residual Euclidean tolerance 10⁻¹⁰ in three
updates. The fixed centered-difference perturbation is 10⁻⁵; its final roots
agree with the analytic-Jacobian roots to less than 10⁻¹⁴ in nodal maximum
norm. The continuous nodal maximum errors are approximately 1.738×10⁻⁴,
4.337×10⁻⁵ and 1.084×10⁻⁵ on the three grids. Their factor-of-four reduction
remains after changing the derivative calculation: spatial discretization
sets the leading solution error here.


The matrix norm includes entries of size h⁻². A small relative matrix error
can therefore hide errors in smaller terms. The direct directional check is
reported separately, rather than relying only on a product of the assembled
finite-difference matrix.


The analytic derivative is a reference, not an assumption that every analytic
implementation is correct. The tests also check derivative rules on separate
functions and nontrivial directions, and check Bratu refinement against the
continuous solution. Agreement between two Jacobians alone would not validate
the boundary conditions or the PDE discretization.


The figure makes no speed ranking. Assembling a dense AD Jacobian here needs
n forward seeds; centered differences need two residual evaluations per
column. Counts describe these implementations, not equal-cost operations or
the best sparse AD strategy. For a large Newton–Krylov method, supplying Jv
directly can be preferable to constructing every column, while a suitable
preconditioner remains necessary.


Connections to implicit integration and parameter estimation


An [implicit ODE stage](/numerical-methods-atlas/en/read/stiff-integration/) has a residual involving the
state and time step. Its Newton matrix contains derivatives of the ODE
right-hand side, so the same AD construction can supply them. For parameter
estimation, derivatives of observations or an objective with respect to model
parameters connect a simulation to an optimization method. Derivative
availability does not itself choose a stable integrator, a well-conditioned
parameterization or a convergent optimization algorithm.


Suppose the converged discrete state satisfies F(u,θ)=0. At a differentiable
solution with nonsingular F_u, its parameter sensitivity satisfies



$$
F_u\frac{du}{d\theta}=-F_\theta.
$$
For a scalar objective L(u,θ), an adjoint solve gives



$$
F_u^T p=L_u^T,\qquad
\frac{dL}{d\theta}=L_\theta-p^TF_\theta.
$$
This differentiates the equation defining the solution. Differentiating a
fixed, finite sequence of Newton iterations instead gives the derivative of
that sequence, including its dependence on the initial guess. Stopping
criteria and line-search branches complicate that distinction. Near a
singular Jacobian, sensitivities can be large even when the primal residual
is small. Primal and derivative solve tolerances therefore need separate
checks. These sensitivity and adjoint equations are explanatory extensions;
the present Bratu exhibit compares Jacobians used in the primal solve.


Limits: smoothness, branches and numerical stability


AD applies the derivative rules of the operations that are executed. At a
branch boundary, an absolute-value corner or a limiter switch, the underlying
function may have no unique classical derivative; a library's chosen rule
does not establish one. Adaptive time-step decisions can change the executed
path under parameter perturbations. For shocks, a computed grid-value
derivative also needs interpretation in terms of shock motion and the
quantity being measured.


The discretized derivative should be checked for mesh and time-step
convergence when it is intended to approximate a continuous sensitivity.
Differentiating a discretized solver and discretizing continuous sensitivity
or adjoint equations require their own consistency analysis. Stable function
evaluation matters too: a formula that overflows in the primal calculation
is not repaired by applying the chain rule.


Reproduce the comparison


Extract the [November 22, 2026 release ZIP](/code/autodiff/2026-11-22/autodiff-2026-11-22.zip) into a new folder. Prepare a Python environment with NumPy, Matplotlib and pytest, and run from the extracted folder. See the [README](/code/autodiff/2026-11-22/README.md) for the complete instructions.


python -m pip install numpy matplotlib pytest
python scripts/build_autodiff.py
python -m pytest tests/test_autodiff.py

Read the [AD engine and Bratu residual](/code/autodiff/2026-11-22/numart/autodiff.py), [existing Newton solver](/code/autodiff/2026-11-22/numart/krylov.py), [figure and evidence builder](/code/autodiff/2026-11-22/scripts/build_autodiff.py), and [test source](/code/autodiff/2026-11-22/tests/test_autodiff.py) individually. An [independent-extraction verification record](/code/autodiff/2026-11-22/verification.json) and [source inventory and hashes](/code/autodiff/2026-11-22/source-manifest.json) accompany the package.


The builder writes the figure and a JSON manifest containing grids, parameters, finite-difference steps, stopping controls, norms, solver histories, the numerical environment and source SHA-256 hashes. Evidence is generated from the numerical implementation independently of the website build. The dated supplement includes the forward-mode engine, Bratu comparison, tests and saved results introduced here. Reverse-mode and adjoint solvers remain outside this implementation. Continue with [Newton and conditioning](/numerical-methods-atlas/en/read/sparse-nonlinear/#newton-and-conditioning), [stiff integration](/numerical-methods-atlas/en/read/stiff-integration/), or the [error-norm guide](/numerical-methods-atlas/en/read/accuracy-stability/).


[Implicit differentiation and adjoints: verified Bratu sensitivity](/numerical-methods-atlas/en/read/adjoint/)

Executable implicit state sensitivities and discrete adjoints are now provided in the separate Bratu parameter-sensitivity chapter. This does not expand the earlier forward-mode release; a separate dated supplement checks root sensitivity and total objective derivatives.

## Publication scope

An educational forward-mode dual-number, JVP and assembled-Jacobian implementation is checked against analytic and finite-difference derivatives for Bratu's equation. A separate November 22, 2026 supplement fixes its source, tests, figure and JSON evidence. Reverse mode, Hessian-vector products, implicit sensitivities and adjoints are reading connections rather than implemented solvers in this exhibit. Existing releases and measurements of other methods are preserved.

## Sources

- R. E. Wengert (1964). A simple automatic derivative evaluation program. https://doi.org/10.1145/355586.364791
- Seppo Linnainmaa (1976). Taylor expansion of the accumulated rounding error. https://doi.org/10.1007/bf01931367
- Atilim Gunes Baydin, Barak A. Pearlmutter, Alexey Andreyevich Radul and Jeffrey Mark Siskind (2018). Automatic Differentiation in Machine Learning: a Survey. https://www.jmlr.org/papers/v18/17-468.html
- The JAX authors (2026). The Autodiff Cookbook. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html
