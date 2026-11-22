# Chebyshev approximation

Chebyshev approximation uses endpoint-clustered nodes and a connection with trigonometric functions. Interpolation, weighted projection and best uniform approximation are distinct constructions.

## Problem and representative equations

Set Tₖ(cosθ)=cos(kθ) and approximate f on [−1,1] by ΣaₖTₖ. Lobatto nodes xⱼ=cos(jπ/n) allow interpolation coefficients to be computed by a discrete cosine transform. Orthogonality uses weight (1−x²)⁻¹/², not the unit weight of Legendre polynomials.

$$
T_0(x)=1,\quad T_1(x)=x,\quad T_{k+1}(x)=2xT_k(x)-T_{k-1}(x),\qquad x_j=\cos(j\pi/n).
$$

## Algorithm

Map the physical interval, sample the nodes, compute coefficients and evaluate the series by recurrence. Clenshaw–Curtis quadrature integrates the interpolant; its nodes and exactness properties are not identical to Gaussian quadrature.

## Conditions and pitfalls

Analytic functions can give rapid coefficient decay, while jumps cause Gibbs oscillations and finite smoothness slows decay. Differentiation amplifies coefficient errors. A small coefficient tail alone cannot rule out unresolved features between sampling nodes.

## What to check

Test reproduction of Tₖ, nodal interpolation and approximation of exp(x), then compare convergence for an absolute value or jump. Measure errors off the interpolation grid and verify derivative scaling under interval maps.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- C. W. Clenshaw and A. R. Curtis (1960). A method for numerical integration on an automatic computer. https://doi.org/10.1007/bf01386223
- F. W. J. Olver and A. B. Olde Daalhuis and D. W. Lozier and B. I. Schneider and R. F. Boisvert and C. W. Clark and B. R. Miller and B. V. Saunders and H. S. Cohl and M. A. McClain (eds.) (2010). NIST Digital Library of Mathematical Functions. https://dlmf.nist.gov/
