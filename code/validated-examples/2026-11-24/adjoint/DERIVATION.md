# Adjoint62–64: authored design derivations, unexecuted

All variables are dimensionless. h=1/(n+1), A_h=-Dxx with zero Dirichlet
state endpoints. Coordinate pairings are Euclidean; objective quadrature h is
included in q. Fixed boundary data have zero parameter derivative.

##62: reverse of the actual backward-Euler map

B=I+dt*kappa*A_h and u_(k+1)=B^-1(u_k+dt*theta*b).
p_N=h(u_N-d), z_k=B^-T*p_(k+1), p_k=z_k.
g_kappa=.01*kappa-dt*sum(z_k^T*A_h*u_(k+1));
g_theta=.02*theta+dt*sum(z_k^T*b).
The corresponding tangents solve B*S_kappa,next=S_kappa-dt*A_h*u_next
and B*S_theta,next=S_theta+dt*b. Initial tangents are zero.

The independent reference uses three nodal sine modes, with eigenvalues
lambda_l=4*h^-2*sin(l*pi*h/2)^2, not continuum(l*pi)^2. Their h-weighted
inner products are delta_lk/2. For q=kappa*lambda_l,r=(1+dt*q)^-1,
R=r^N,a_N=R*a0+theta*beta*(1-R)/q. Differentiate this closed formula
independently of the scalar BE/tangent recurrence; R_q=-N*dt*r^(N+1),
a_theta=beta*(1-R)/q and
a_kappa=lambda_l*(R_q*(a0-theta*beta/q)-theta*beta*(1-R)/q^2).
J=.25*sum(a_N-d_l)^2+.005*kappa^2+.01*theta^2, hence modal gradient
is .5*sum((a_N-d_l)*a_parameter) plus explicit penalty derivative.
The time-exact SEMIDISCRETE reference uses exp(-q*T) and stableexpm1.
Its positive terminal field error, not a signed gradient, defines BE ratios.

Checkpoint storage has two separately measured ownership windows. Full mode
holds its trajectory, saves/streams it, closes files and releases all aliases
before checkpoint mode starts. Checkpoint mode retains block16boundaries,
one block and endpoints,oneadjoint,RHS/solve scratch. It streams evidence;
no full-trajectory mmap/closure/reference array is hidden. Comparisons/NPZ
assembly may run afterward in an explicitly separate validation window;
the claim concerns owned numerical buffers,not processRSS. Count aliases by
owning root and count factorization/work arrays separately and in total.

##63: discrete fold and independent shooting

G=A_h*u-lambda*exp(u),J=A_h-diag(lambda*exp(u)),b=exp(u).
J*s=b,J^T*p=h*u;g=.05*lambda+(h*u)^T*s=.05*lambda+p^T*b.
The continuum cosh family and its fold are different from the discrete
states/folds. Stored discrete anchor decimals are only input coordinates;
qualify their distance from the independently computed discrete fold first.

Independent Decimal shooting starts u0=0,u1=a and propagates
u_(i+1)=2u_i-u_(i-1)-h^2*lambda*exp(u_i). Let z=u_a,w=u_lambda,
y=u_aa,t=u_a_lambda. Their starts are z0=0,z1=1 and all other starts0.
With C=2-h^2*lambda*exp(u_i):
z_next=C*z_i-z_prev;
w_next=C*w_i-w_prev-h^2*exp(u_i);
y_next=C*y_i-y_prev-h^2*lambda*exp(u_i)*z_i^2;
t_next=C*t_i-t_prev-h^2*exp(u_i)*z_i
       -h^2*lambda*exp(u_i)*w_i*z_i.
At the right boundary R=u_(n+1),fold equations are R=0,R_a=0,
with2x2NewtonJacobian[[z_end,w_end],[y_end,t_end]].
For a lower root at fixedlambda,a_lambda=-w_end/z_end and
s_i=w_i+z_i*a_lambda. This derivative reference does not solve the
primary Krylov equation. A second independent high-precision tridiagonal
Newton fromzero crosschecks all six states. n1 has exact DISCRETE fold
u1=1,lambda=8/e,an analytic oracle for the reference itself.

At the SAME float state define direct banded s_D,p_D,with
r_D=b-J*s_D,r_p=q-J^T*p_D,and candidate r=b-J*s_hat.
The finite-reference identity is
q^T(s_D-s_hat)-p_D^T*r = -p_D^T*r_D+r_p^T(s_D-s_hat).
Use this corrected identity and its triangle bound for the error relative
to the direct reference; keep reference defects visible. The theoretical
true-error bound ||q||*||r||/sigma_min(J) is reported using a floating
spectral estimate and labelled an estimate,not an interval-certified bound.
If an approximate adjoint is inserted into the exact identity,its omitted
cross term is r_p^T*J^-1*r. State-tolerance error changes J/q/b and is a
separate comparison with high-precision shooting,not the fixed-state identity.
The three predetermined FD-step curves are all saved; no optimal-step or
monotonic-order gate is inferred from them.

##64: distributed coefficient and implicit VJP

a=2+B*theta,where B are endpoint linear hats,partition of unity.
G_theta*v=-exp(u)*(Bv);J*delta_u=exp(u)*(B*delta_theta).
For each scalar objective,J^T*p=q and gradient=B^T*(exp(u)*p).
q=h*ones,midpoint unitvector,or h*u respectively. Direct gather/scatter
uses two local weights and indices per state node. Actual transpose rules
are independently tested on a nonsymmetric matrix; Bratu symmetry alone
cannot detect transposition errors. Dense B/full sensitivity is allowed
only in the independently labelled reference window.

Physical coefficient endpoints[a_old-b_old,a_old+b_old] correspond to
PERTURBATIONS theta=[a_old-b_old-2,a_old+b_old-2]. They are unrelated to
state Dirichlet values: u and du/dtheta vanish at endpoints,while coefficient
endpoint controls may be nonzero. One versus three objectives means one
versus three adjoint RHS at the same state;factor reuse/all work is recorded,
not converted into an unmeasured speedup. Krylov basis storage is permitted
and counted; an n-by-m parameter Jacobian/sensitivity is not.

##R2: requested tolerance versus finite-precision residual

The derivative magnitude near the discretefold can make stencil evaluation
roundoff larger than a requested1e-12relative residual. No achieved floor is
asserted before execution. Keep the GMRES numerical body,targetmax(1e-14,
rtol*normrhs),cap120 and exact returned candidate unchanged. Required1e-4
and1e-8targets must actually be met. Requested1e-12is an observational
diagnostic:target-unmet remains target-unmet even if independent gradient
accuracy succeeds. Record termination(maxiter/breakdown),actual residual and
a separate componentwisegamma12stencil roundoff SCALE ESTIMATE. Agreement
with10times that estimate only means consistent scale,cause unproven;it is
not interval certification and never changes a convergence flag. All input
solutions,tolerances and histories remain visible;no fallback/reference
substitution or chosen best iterate. Independent shooting-gradient accuracy
and corrected same-state residual identities keep their original thresholds.

For62,the40n limit covers unique evolving checkpoint/trajectory/current
state,adjoint,RHS,and Thomas eliminated-RHS/output scratch buffers. It does
not include STATIC factors,pivots,fixed model data or reference arrays;these
are explicitly reported and INCLUDED in the separate total-owned-numeric
bytes. The latter must also decrease atN256,with common factors counted in
both ownership windows. A hidden full trajectory/mmap/reference/evidence
buffer cannot be omitted from total accounting. Validation assembly happens
only after the claimed ownership window;this is not a processRSS claim.
