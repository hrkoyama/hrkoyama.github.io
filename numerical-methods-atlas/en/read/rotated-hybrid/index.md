# Rotated-hybrid Riemann solver

Rotated Riemann methods construct dissipation using directions beyond the face normal. Ren’s rotated Roe method (2003) and Nishikawa–Kitamura’s rotated-hybrid method (2008) are related but distinct.

## Problem and representative equations

For 2D Euler states U_L,U_R and unit face normal n, resolve n into orthogonal unit directions n₁,n₂ with weights αᵢ=n·nᵢ. The formula below defines this atlas’s educational HLLE/Roe experiment, not the optimized dissipation formula in the 2008 paper.

$$
\mathbf n=\alpha_1\mathbf n_1+\alpha_2\mathbf n_2,\qquad\widehat F(\mathbf n)=\alpha_1\widehat F_{\rm HLLE}(\mathbf n_1)+\alpha_2\widehat F_{\rm Roe}(\mathbf n_2).
$$

## Algorithm

The implementation aligns n₁ with the velocity jump, orienting directions to have nonnegative projections on the face normal. A tiny jump falls back to the face tangent. Rotate the same states into each frame, evaluate HLLE/Roe, rotate momentum fluxes back and combine. This differs from a pressure-sensor flux blend.

## Conditions and pitfalls

Roe (1981) supplies the component approximate solver. The 2003 rotated-method paper is by Y.-X. Ren; the 2008 rotated-hybrid paper is by Hiroaki Nishikawa and Keiichi Kitamura. Roe, Nishikawa, Ismail and Scalabrin (2005) is related carbuncle research, not the authorship/date of that 2008 paper. No universal carbuncle or positivity guarantee is claimed here.

## What to check

Check constant states, flux reversal under state/normal exchange and rotational covariance. Separate normal compression from pure tangential shear, then compare perturbed planar shocks and blunt-body cases under fixed conditions. Link the dated package’s actual tests/results without claiming a new reproduction of the papers.

## Publication scope

Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.

## Sources

- Yu-Xin Ren (2003). A robust shock-capturing scheme based on rotated Riemann solvers. https://doi.org/10.1016/s0045-7930(02)00114-7
- Nishikawa, Hiroaki and Kitamura, Keiichi (2008). Very simple, carbuncle-free, boundary-layer-resolving, rotated-hybrid Riemann solvers. https://doi.org/10.1016/j.jcp.2007.11.003
- Philip Roe and Hiroaki Nishikawa and Farzad Ismail and Leonardo Scalabrin (2005). On Carbuncles and Other Excrescences. https://doi.org/10.2514/6.2005-4872
- Roe, Philip L. (1981). Approximate Riemann solvers, parameter vectors, and difference schemes. https://doi.org/10.1016/0021-9991(81)90128-5
