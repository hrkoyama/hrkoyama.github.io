# Reference and theory scope

The fixed example inherits the existing atlas Euler double rarefaction:
`rho_L=rho_R=1`, `u_L=-2`, `u_R=2`, `p_L=p_R=.4`, `gamma=1.4`,
`x in [0,1]`, initial interface `.5`, final time `.15`.
This is a **non-vacuum** expansion with a small positive central state. It is
different from the actual-vacuum input in Zhang–Shu (2010), section 4.3.
No unique original inventor is attributed to the fixed numerical values.

`double_rarefaction.py` is a separately derived analytic evaluator. Write
`c0=sqrt(gamma*p0/rho0)`, `U=2`, and
`b=1-(gamma-1)*U/(2*c0)>0`. Symmetry gives `u_star=0`, and the rarefaction
Riemann invariants give `c_star=c0*b`, `rho_star=rho0*b**(2/(gamma-1))` and
`p_star=p0*b**(2*gamma/(gamma-1))`. The four fan fronts travel at
`[-U-c0,-c_star,c_star,U+c0]`. Inside the right fan,
`u=2/(gamma+1)*(xi+(gamma-1)*U/2-c0)` and
`c=(2*c0-(gamma-1)*U+(gamma-1)*xi)/(gamma+1)`; the left fan follows by
reflection. These formulas follow from the official Clawpack Riemann
invariants, whose specific illustrated inputs differ from ours.

The reference stores **conserved cell means**, using quadrature split at
every fan boundary. At gamma=1.4 the fan conserved fields have polynomial
degree at most seven; split Gauss8 is exact in real arithmetic. Float64
quadrature and evaluation error remain and are checked against Gauss16.
The plotted/comparison pressure is `p(q_mean)`; this is different from
the cell mean of pointwise pressure.

`numart_reference_riemann.py` is an unchanged MIT copy from the existing
immutable atlas release. Its bracketed logarithmic-pressure root and
general fan evaluation provide a separate algebraic calculation. Source
SHA and license are in `../source-provenance.json` and
`NUMART-LICENSE.txt`. This is not an independent PDE simulation. The
current evaluator needs no ExactPack call and does not copy/run Clawpack.

For the limited P1 finite-volume update, the two endpoint Lobatto weights
are both `1/2`. Zhang–Shu theorem 2.1 and remark 2.4 give the sufficient
forward-Euler mean-positivity condition `dt*a/dx <= 1/2` for a global
Lax–Friedrichs flux, provided `a` bounds `abs(u)+c` at **every** admissible
endpoint used by the flux. SSPRK(3,3) consists of forward-Euler updates and
convex combinations, so the reconstruction is scaled and the speed/CFL
bounds are checked at every actual substep. Remark 2.7 warns that predicting
all stage speed maxima from the first state is nontrivial: the fixed `a`
and runtime checks here certify the recorded run, not an a priori bound
for arbitrary inputs. This is a P1 **finite-volume** reconstruction, not
DG time evolution, and positivity alone does not establish TVD, entropy
stability or a convergence theorem.

`citations.json` distinguishes the positivity method, time discretization,
Riemann formula/background, existing test input and actually executed
reference evaluator, with the review scope recorded individually.
