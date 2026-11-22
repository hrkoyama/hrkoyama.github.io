# Operator splitting: Lie–Trotter and Strang on the same reaction–diffusion problem

Compare short-time nonlinear Schnakenberg reaction–diffusion with the same initial field, grid, subsolvers and observation times. This lightweight addition checks temporal convergence and numerical-reference sensitivity while retaining existing spatial and long-time pattern records.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

**Methods used**

- [Lie–Trotter splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en) (`lie-trotter`)
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en#reaction-diffusion-splitting-en-algorithm)

Lie–Trotter uses diffusion(h) then reaction(h); Strang uses diffusion(h/2), reaction(h), diffusion(h/2), always passing the updated state. Both apply the exact exponential of the centered-FD diffusion matrix by FFT and the same implicit-midpoint reaction/Newton tolerance 2e−13 with at most 12 residual evaluations. The reaction flow is a second-order approximation, not exact. No clipping, adaptive steps or fallback; nonconvergence is failure.

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en#reaction-diffusion-splitting-en-validation)

The reference independently assembles the SAME FD semidiscretization with a real-space sparse matrix and separately written reaction RHS, then integrates it unsplit with Radau. Tighter Radau and separate DOP853 runs measure reference sensitivity relative to the finest Strang error. Norms are per-species mean L1, RMS L2 and maximum L∞, then the worse species; refinement uses the maximum across the four common positive observation times. Also record Newton-tolerance sensitivity, positive tested substeps, reaction source/sink balance and reversed-Lie ordering.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Nondimensional 1D periodic [0,2pi), N=32, a=.1, b=.9, D=(.01,1). The initial fields u₀=1+.08cos2x+.01cos4x and v₀=.9−.03cos2x−.002cos4x match the earlier finite-amplitude example. This new run ends at T=1, uses 16/32/64/128 steps and common output times 0/.25/.5/.75/1. The fixed input is reflection-even and pi-periodic.

### Adopted numerical method

Lie–Trotter uses diffusion(h) then reaction(h); Strang uses diffusion(h/2), reaction(h), diffusion(h/2), always passing the updated state. Both apply the exact exponential of the centered-FD diffusion matrix by FFT and the same implicit-midpoint reaction/Newton tolerance 2e−13 with at most 12 residual evaluations. The reaction flow is a second-order approximation, not exact. No clipping, adaptive steps or fallback; nonconvergence is failure.

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

### References and validation

The reference independently assembles the SAME FD semidiscretization with a real-space sparse matrix and separately written reaction RHS, then integrates it unsplit with Radau. Tighter Radau and separate DOP853 runs measure reference sensitivity relative to the finest Strang error. Norms are per-species mean L1, RMS L2 and maximum L∞, then the worse species; refinement uses the maximum across the four common positive observation times. Also record Newton-tolerance sensitivity, positive tested substeps, reaction source/sink balance and reversed-Lie ordering.

### Limits

This measures temporal error of the adopted compositions at fixed space, including splitting and midpoint-reaction discretization errors. It is not an exact continuum solution, spatial convergence check or independent PDE-engine comparison. Reactions do not conserve u+v; positivity is observed only for the fixed input. Work is reported as actual subflow calls, without runtime rankings or universal Strang superiority. This additional comparison of the existing Schnakenberg problem changes neither physical-problem counts, the common 22 examples, old release criteria nor success history. Long-time patterns, 2D and general boundaries are outside scope.

### Stored measurements and decisions

```json
{
  "metrics": {
    "grid": 32,
    "final_time": 1.0,
    "lie_finest_l2": 0.00048048614019260814,
    "strang_finest_l2": 3.554231191703374e-06,
    "lie_last_observed_order": 1.002936574094834,
    "strang_last_observed_order": 1.9991038173822453,
    "reference_tolerance_linf": 1.98463467881993e-12,
    "reference_algorithm_linf": 2.205471361094169e-10,
    "reference_to_strang_error_ratio": 6.205199499240203e-05,
    "newton_sensitivity_linf": 0.0,
    "reverse_order_l2_difference": 0.007637419068950036,
    "minimum_concentration": 0.8490853839816418,
    "maximum_reaction_balance_error": 1.5942108744226857e-15
  },
  "checks": {
    "lie_error_decreases": true,
    "strang_error_decreases": true,
    "lie_first_order": true,
    "strang_second_order": true,
    "lie_finest_error": true,
    "strang_finest_error": true,
    "strang_improves_this_input": true,
    "reference_tolerance": true,
    "reference_independent_time_algorithm": true,
    "reference_error_separated": true,
    "newton_error_separated": true,
    "reaction_converged": true,
    "reaction_source_balance": true,
    "positive_on_tested_substeps": true,
    "noncommuting_order_control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs-initial.json

### Sources and review scope

- H. F. Trotter (1959). On the product of semi-groups of operators. https://doi.org/10.1090/S0002-9939-1959-0108732-6; review_level=metadata
  AMS bibliographic record checked. Original semigroup product-limit reference; no audit of unbounded-operator hypotheses. Finite-dimensional order calculations are derived in the chapter.
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://doi.org/10.1137/0705041; review_level=metadata
  Publisher bibliography checked for this addition. The original symmetric splitting reference is distinct from the Hairer lecture consulted for compositions and order. No fresh full-paper audit.
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=full-text
  Author-hosted Lecture 2, section 5, printed pp.12–14, equations (23)–(27), and exact versus numerical subflows: Lie–Trotter, symmetric second-order composition and separable Hamiltonians. Selected passages, not a full-lecture audit.
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliography-and-publisher-indexed-abstract
  Checked official PubMed bibliography/DOI and publisher-indexed abstract. Full text returned403. Historical source for the reaction family, not a claim to reproduce original coefficients or experiments.
- The SciPy community (2024). SciPy1.14.1 solve_ivp reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-documentation-selected-methods-and-tolerances
  Consulted SciPy 1.14.1 methods and rtol/atol documentation. Radau order five and DOP853 order eight are independent time algorithms for the same spatial system, not exact continuum solutions.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
