# Operator splitting: Lie–Trotter and Strang

Operator splitting: Lie–Trotter and Strang


Operator splitting advances separate parts of an evolution equation and composes their solution maps. Lie–Trotter uses two full substeps; Strang surrounds one full substep with two half substeps. Even exact subproblem solutions leave a composition error when their order matters.


Run both on the same reaction–diffusion input: a 32-point, T=1 Schnakenberg system with matched initial fields, subsolvers and observation times. Four step sizes measure first-order Lie–Trotter and second-order Strang. Unsplit Radau/DOP853 references use the same FD semidiscretization; this is separate from spatial convergence and exact continuum solutions.

[Fixed input, results, code and the 16-test rerun receipt](/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en)

Split the evolution, define one time step



$$
\dot u=F(u)+G(u),\qquad \dot v=F(v)\ \Rightarrow\ \varphi_F^h,\qquad \dot w=G(w)\ \Rightarrow\ \varphi_G^h.
$$

Start with a sufficiently smooth autonomous finite-dimensional initial-value problem. Each φ is the exact flow of its subproblem, and h is one step for the summed equation. Compositions act from right to left. Advancing F for h and then G for h approximates one step of length h for the original equation, not 2h. Using only h/2 for each part would instead halve the leading vector field.


The approach uses tractable subproblems such as reaction and diffusion, transport and sources, or drift and force in a separable Hamiltonian. Splitting is a separate choice from spatial discretization and physical modeling. Matrix exponentials below apply to the linear specialization F(u)=Au, G(u)=Bu.


Lie–Trotter: two ordered full substeps



$$
u^{n+1}=L_h(u^n)=(\varphi_G^h\circ\varphi_F^h)(u^n),\qquad L_h=e^{hB}e^{hA}\quad(\dot u=(A+B)u).
$$

Our convention applies F first and G to the updated state. Reversing the order gives another first-order method, generally with a different value. Computing both substeps independently from the old state and adding their increments is a different update.



$$
e^{hB}e^{hA}-e^{h(A+B)}=\frac{h^2}{2}(BA-AB)+O(h^3),\qquad [A,B]=AB-BA.
$$

Expand both exponentials through h²: the commutator remains in the difference from the exact summed flow. Its sign here follows the chosen product and reverses with the substep order. The local defect means the one-step difference starting from an exact state: O(h²). Under stability and smoothness, accumulated error at a fixed final time is O(h). The product limit and a finite-step error estimate are separate statements.


Strang: a symmetric second-order composition



$$
u^{n+1}=S_h(u^n)=(\varphi_F^{h/2}\circ\varphi_G^h\circ\varphi_F^{h/2})(u^n),\qquad S_h=e^{hA/2}e^{hB}e^{hA/2}.
$$

Apply a half F step, a full G step and another half F step, each to the current state. G/2→F→G/2 is another valid Strang variant. The two variants generally produce different numerical solutions and error constants.



$$
S_{-h}=S_h^{-1},\qquad S_h-e^{h(A+B)}=O(h^3),\qquad [A,B]=0\ \Rightarrow\ L_h=S_h=e^{h(A+B)}.
$$

When inverse flows exist, replacing h by −h reverses the symmetric composition. Expansion through the quadratic term cancels the leading Lie–Trotter defect, leaving local O(h³) and global O(h²) errors; nested commutators enter the next error terms. For commuting finite matrices, both exact-subflow compositions equal the exact summed flow. Extending this statement to unbounded PDE operators requires domain and regularity conditions.


Compare order, symmetry and work




| Property | Lie–Trotter | Strang |
| --- | --- | --- |
| Application order | F(h), G(h) | F(h/2), G(h), F(h/2) |
| One-step local defect | O(h²) | O(h³) |
| Global error at fixed final time | O(h) | O(h²) |
| Time symmetry with exact subflows | Generally absent | Yes, for invertible flows |
| Subflow calls per standalone step | 2 | 3 |
| Asymptotic error reduction on halving h | About 2 | About 4 |



$$
E(h)=\|u_N-u(T)\|_2,\quad h=T/N,\qquad p_{\rm obs}=\log_2\frac{E(h)}{E(h/2)},\qquad E_L(h)=O(h),\ E_S(h)=O(h^2).
$$

A standalone Strang step calls one additional subflow. Over consecutive constant steps, adjacent half F steps can be merged when the exact flow has the group property (a positive-time semigroup suffices for diffusion). Lie–Trotter uses 2N subflow calls and merged Strang 2N+1. Actual work depends on each subproblem, output and boundary processing, and whether numerical subflows permit merging. Call counts are not measured runtimes.


Small noncommuting example with exact subflows



$$
u=\begin{pmatrix}q\\p\end{pmatrix},\quad A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad B=\begin{pmatrix}0&0\\-1&0\end{pmatrix},\quad u(0)=\begin{pmatrix}1\\0\end{pmatrix},\quad u(t)=\begin{pmatrix}\cos t\\-\sin t\end{pmatrix}.
$$


$$
\varphi_A^h(q,p)=(q+hp,p),\qquad\varphi_B^h(q,p)=(q,p-hq),\qquad [A,B]=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
$$


$$
L_hu_0=\begin{pmatrix}1\\-h\end{pmatrix},\quad S_hu_0=\begin{pmatrix}1-h^2/2\\-h\end{pmatrix},\quad u(h)=\begin{pmatrix}1-h^2/2+O(h^4)\\-h+h^3/6+O(h^5)\end{pmatrix}.
$$

This is a two-component harmonic oscillator with nondimensional q, p and time. Its subflows require only addition and multiplication; the reference is the analytic sine/cosine solution. The first-step formulas already expose the local defect orders. Use the norm of both components to avoid mistaking componentwise cancellation for higher order. This lightweight illustration uses no spatial grid, independent PDE implementation or quantum-chemistry calculation.




| N | h | Lie–Trotter E(h) | p | Strang E(h) | p |
| --- | --- | --- | --- | --- | --- |
| 8 | 0.125 | 5.220647e-02 | — | 2.075134e-03 | — |
| 16 | 0.0625 | 2.617930e-02 | 0.9958 | 5.176511e-04 | 2.0032 |
| 32 | 0.03125 | 1.311628e-02 | 0.9971 | 1.293422e-04 | 2.0008 |
| 64 | 0.015625 | 6.565750e-03 | 0.9983 | 3.233115e-05 | 2.0002 |


These saved values were recomputed for the fixed input u₀=(1,0), T=1 and N=8,16,32,64. The final global observed orders are 0.9983 for Lie–Trotter and 2.0002 for Strang. A separate single-step check from the exact initial state gives local orders near 2 and 3. Controls check that reversed Lie–Trotter remains first order with a different solution, and that commuting A=−I, B=−2I agrees with exp(−3T) to floating-point roundoff.


Conditions: order and stability can be lost


The stated orders assume a smooth solution, sufficiently small steps, a fixed finite interval and suitable stability. Shocks, stiff relaxation and nonsmooth initial data can invalidate those expectations. PDE subproblems and their stages need compatible boundary data. Check order reduction from inhomogeneous or time-dependent boundaries separately from spatial and nonlinear-solver errors.


A symmetric arrangement alone does not make approximate subflows second order. Standard Strang composition needs subsolvers with at least second-order consistency and sufficiently tight iteration tolerances to retain second order. Exact or symmetric subsolvers are needed to retain time symmetry as well. Direct substitution of forward or backward Euler generally reduces the order to one. Nonautonomous problems require a suitable extended system including time, or consistent subproblem time arguments; freezing everything at the old time is not enough.



$$
\det L_h=\det S_h=1,\quad\operatorname{tr}L_h=\operatorname{tr}S_h=2-h^2,\quad 0For this oscillator both update matrices have determinant 1 and trace 2−h², giving bounded oscillatory modes for 0<|h|<2. Exact subflows do not by themselves guarantee unconditional stability. Composition inherits only properties preserved by its submaps: Hamiltonian symplecticity does not imply positivity for arbitrary reactions or exact conservation of the full energy.


Existing Strang examples and the distinction from IMEX


The existing reaction–diffusion [finite-amplitude Schnakenberg](/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) and [saturated-pattern](/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) examples use exact half steps of centered-difference diffusion and a full implicit-midpoint reaction step in a Strang composition. Their published records give spatial and temporal checks for those fixed conditions. They are separate from this oscillator illustration, and their distributions, tolerances and results are preserved.


IMEX also separates parts of the right-hand side, but [IMEX time integration](/numerical-methods-atlas/en/read/stiff-integration/) combines explicit and implicit stage equations, whereas the splitting here composes subproblem flows. These are different updates. For the separable-Hamiltonian connection, see [symplectic integration](/numerical-methods-atlas/en/read/symplectic/).


Lightweight reproduction and publication scope


Python 3 standard libraries suffice to recompute the table, local defects, reversed ordering and commuting control. The script prints JSON; --check compares saved values. This fixed two-component reading illustration is not a general splitting-solver distribution or a new common execution-registry entry. The oscillator script remains a reading illustration. A separate dedicated lightweight reaction–diffusion release now executes both methods; their educational-code status is limited to that fixed input.


[Illustration reproduction script](/scripts/verify-operator-splitting.py) · [Fixed input and saved values / JSON](/numerical-methods-atlas/assets/operator-splitting.json)




```text
python3 verify-operator-splitting.py
python3 verify-operator-splitting.py --check operator-splitting.json
```

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input

Fixed-target computation

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

This measures temporal error of the adopted compositions at fixed space, including splitting and midpoint-reaction discretization errors. It is not an exact continuum solution, spatial convergence check or independent PDE-engine comparison. Reactions do not conserve u+v; positivity is observed only for the fixed input. Work is reported as actual subflow calls, without runtime rankings or universal Strang superiority. This additional comparison of the existing Schnakenberg problem changes neither physical-problem counts, the common 22 examples, old release criteria nor success history. Long-time patterns, 2D and general boundaries are outside scope.

[Input, results and acceptance](/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-splitting/#reaction-diffusion-splitting) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/run.py) · [Code splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/splitting.py) · [Code reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/reference.py) · [Tests test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py) · [ZIP](/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/splitting/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/splitting/verification.json)

## Publication scope

The two-component oscillator illustration is retained, with a new dedicated lightweight release comparing both methods on the same Schnakenberg reaction–diffusion input. The educational implementation is checked only for the 32-point, T=1 fixed case. Existing physical-problem counts, the common 22 examples, old releases, criteria and history are retained.

## Sources

- H. F. Trotter (1959). On the product of semi-groups of operators. https://doi.org/10.1090/S0002-9939-1959-0108732-6
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://doi.org/10.1137/0705041
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf
