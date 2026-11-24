# PINNs and neural operators

A PINN fits a neural representation of a particular solution; a neural operator learns a map from input functions such as coefficients or initial data to solution functions. Their targets and validation protocols differ.

## Problem and representative equations

A PINN minimizes an empirical weighted loss of PDE, boundary and data residuals. N and B are differential/boundary operators and f,g are prescribed data. A representative FNO layer combines a Fourier-parameterized integral operator K with a local map W acting on feature functions v.

$$
\mathcal L(\theta)=\lambda_r\langle|\mathcal N[u_\theta]-f|^2\rangle_r+\lambda_b\langle|\mathcal B[u_\theta]-g|^2\rangle_b+\lambda_d\langle|u_\theta-u_{\rm obs}|^2\rangle_d.
$$

$$
v_{\ell+1}=\sigma\!\left(W_\ell v_\ell+\mathcal F^{-1}[K_\ell\,\mathcal Fv_\ell]\right).
$$

## Algorithm

For a PINN, scale coordinates/units, differentiate residuals, specify collocation points and boundary enforcement, and optimize. FNO trains an operator on input/reference-solution pairs and truncates Fourier modes. Cite the PINN and FNO papers as separate proposals.

## Conditions and pitfalls

Small training loss is not a bound on global solution error or conservation. Examine residual imbalance, shocks, stiff scales and out-of-distribution inputs. Transfer between discretizations is not a guarantee of physical correctness at arbitrary resolution.

## What to check

Compare against analytic or independently converged conventional solutions. Measure off-training L1/L2/L∞ errors, boundaries, conservation and multiple seeds. Split operator data by independent problems rather than nearby time slices alone, and report distribution-shift tests separately.

## Selected original sources and the present small examples

Selected section 2 of the 2017 PINN Part I preprint distinguishes residual loss from data and boundary losses. Sections 3–4 of FNO version 3 (2021) combine a local linear map, a Fourier integral map and nonlinear activation. The present small Poisson and periodic-heat inputs are separate educational choices. Neither the full 2019 JCP article nor the original large experiments or performance claims are reproduced.

## Publication scope

Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.

## Sources

- M. Raissi and P. Perdikaris and G.E. Karniadakis (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. https://doi.org/10.1016/j.jcp.2018.10.045
- Zongyi Li and Nikola Kovachki and Kamyar Azizzadenesheli and Burigede Liu and Kaushik Bhattacharya and Andrew Stuart and Anima Anandkumar (2021). Fourier Neural Operator for Parametric Partial Differential Equations. https://openreview.net/forum?id=c8P9NQVtmnO
- M. Raissi, P. Perdikaris and G. E. Karniadakis (2017). Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations. https://arxiv.org/pdf/1711.10561
- Z. Li et al. (2021). Fourier Neural Operator for Parametric Partial Differential Equations. https://arxiv.org/html/2010.08895v3
