# Spectral elements: high-order finite elements and 2D Poisson

Spectral elements: high-order finite elements and 2D Poisson

The spectral element method (SEM) partitions a domain into elements and approximates the field with high-degree local polynomials. It connects finite-element assembly with high-order approximation of smooth functions. This chapter adopts a continuous Galerkin Legendre GLL variant and a small reproducible two-dimensional Poisson problem.

Connect high-order local polynomials


$$
u_h|_{K_e}(\xi,\eta)=\sum_{i,j=0}^{p}U^e_{ij}\ell_i(\xi)\ell_j(\eta),\qquad u_h\in C^0(\Omega)
$$
Map each square to reference coordinates in [−1,1]². Shared boundary degrees of freedom assemble a C0 field, without imposing continuous derivatives. SEM belongs to the high-order finite-element family; finite elements in general are not restricted to linear elements. Element-local polynomials also differ from a single global Fourier expansion.

Start from the Poisson weak form


$$
\int_\Omega\nabla v_h\cdot\nabla u_h\,d\Omega=\int_\Omega v_h f\,d\Omega,\qquad v_h|_{\partial\Omega}=0
$$
Multiply −Laplacian u=f by a test function and integrate by parts, transferring one derivative to each factor. Zero Dirichlet tests remove the boundary term. This implementation approximates the integrals with GLL quadrature for constant coefficients and affine squares.

GLL nodes, quadrature and matrices


$$
(1-\xi_i^2)P_p^\prime(\xi_i)=0,\qquad w_i=\frac{2}{p(p+1)P_p(\xi_i)^2},\qquad i=0,\ldots,p
$$

$$
D_{ij}=\ell_j^\prime(\xi_i),\quad W=\operatorname{diag}(w_i),\quad S=D^TWD,\quad K_e=\frac{h_y}{h_x}S\otimes W+\frac{h_x}{h_y}W\otimes S
$$

$$
b^e_{ij}=\frac{h_xh_y}{4}w_iw_jf(x_{e,i},y_{e,j}),\qquad KU=b
$$
The p+1 GLL nodes are the roots of the derivative of the degree-p Legendre polynomial plus both endpoints. The one-dimensional quadrature is exact through degree 2p−1. Nodal interpolation makes the quadrature mass diagonal, not exactly integrated for every degree-2p product. Two-dimensional stiffness also contains transverse products, so the quadrature convention matters. Assemble local tensor-product stiffness/load contributions, eliminate the boundary values and solve the sparse system.

Comparison with the existing P1 finite elements



Comparison with the existing P1 finite elements

| Aspect | Published P1 FEM | This GLL-SEM |
| --- | --- | --- |
| Local space | Linear polynomials on triangles | Tensor-product Qp polynomials on squares |
| Interface coupling | C0 continuity | C0 continuity |
| Quadrature | Gauss integration via a Duffy transform | GLL stiffness/load quadrature |
| Refinement | Primarily h refinement | Separate h and p refinement |
| Algebraic solver here | Existing Numart ILU(0)/GMRES | SciPy sparse direct solve |
| Matched controls | PDE, boundary, reference and free unknowns | Same controls; no speed ranking |

Small example:2D Poisson h/p refinement


$$
\Omega=(0,1)^2,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*,\quad u|_{\partial\Omega}=0
$$
At p=2, use 2/4/8 SEM elements per coordinate and 4/8/16 subdivisions for the existing triangular P1 FEM. Both have 9/49/225 free unknowns. Separately fix 2 x 2 elements and vary p=1..6. The comparison executes byte-identical modules from the published Numart distribution; that historical release remains unchanged.

[](/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)Actual saved fields and measurements. A nodal-error picture is distinct from an error norm integrated over element interiors.Distinguish residual, continuous error and observed order


$$
E_{L^2}=\left[\int_\Omega(u_h-u_*)^2\,d\Omega\right]^{1/2},\quad E_{H^1}=\left[\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right]^{1/2}
$$

$$
E_{L^2}\sim h^{p+1},\qquad E_{H^1}\sim h^p\quad\text{(smooth solution and resolved quadrature)}
$$
Integrate errors at separate higher-order Gauss points, not only at GLL nodes. A small linear-system residual alone does not imply a small continuous-PDE error. On the last h refinement, p2 SEM gives L2 order about 3.04 and H1-seminorm order 2.01; P1 FEM gives 1.97 and 0.99. At 225 free unknowns, L2 errors are about 2.49e−4 for SEM and 5.38e−3 for P1. At p6 on 2 x 2 elements, L2 error is about 3.78e−7.

These observations depend on smoothness, boundaries, element geometry, quadrature and solver choices. They establish neither universal p convergence near singularities nor a speed/accuracy ranking for all problems. Curved elements, mixed velocity/pressure spaces and fluid coupling are outside this execution.

Related implementations: Nek5000 and nekRS

[Nek5000](https://nek5000.github.io/NekDoc/theory.html) is a high-order spectral-element flow solver. [nekRS](https://github.com/Nek5000/nekRS) is the related CPU/GPU successor described by the [official project](https://nek5000.github.io/). Follow those links for their documentation and source. The small Python Poisson code does not execute or validate either flow solver or its performance. Patera’s original paper supplies historical bibliographic context; the implemented Legendre GLL variant is separately specified.

[Existing finite elements](/numerical-methods-atlas/en/read/fem/) · [Discontinuous FR/DG comparison](/numerical-methods-atlas/en/read/flux-reconstruction/)

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### 2D spectral-element Poisson: P1 FEM comparison and h/p refinement

Fixed-target computation

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

One smooth fixed problem only. Meshes, quadrature and algebraic solvers differ: no speed, complexity or universal-accuracy ranking. The diagonal GLL quadrature mass is not the exactly integrated mass of every product. No curved mesh, singular solution, incompressible flow or Nek5000/nekRS run.

[Input, results and acceptance](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-sem-fr/#sem-poisson-2d) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py) · [Code sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py) · [Code polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py) · [Code fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py) · [Code krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py) · [Code fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py) · [Code advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py) · [Code riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py) · [Code equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py) · [Code limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py) · [Tests test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py) · [ZIP](/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip) · [Results](/code/validated-examples/2026-11-23/sem-fr/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-23/sem-fr/verification.json)

## Publication scope

Dedicated small code, fixed inputs, saved fields and decisions are published with25 tests rerun from an independently extracted ZIP. Related external software is introduced from official documentation, without claiming installation or execution.

## Sources

- A. T. Patera (1984). A spectral element method for fluid dynamics: Laminar flow in a channel expansion. https://doi.org/10.1016/0021-9991(84)90128-1
- Nek5000 development team (2026). Nek5000 documentation: Theory and spectral-element basis (accessed 2026-11-23). https://nek5000.github.io/NekDoc/theory.html
- Nek5000/RS development team (2026). Nek5000/RS project: spectral-element solvers and related implementations (accessed 2026-11-23). https://nek5000.github.io/
