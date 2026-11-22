# Markov-chain Monte Carlo / MCMC

MCMC constructs a Markov chain with a chosen invariant distribution when direct independent sampling is difficult. Invariance and adequate exploration in a finite run are separate requirements.

## Problem and representative equations

For an unnormalized target π and proposal q(y|x), use the Metropolis–Hastings acceptance probability. Unknown target normalization cancels. Proposal factors cancel only for symmetric proposals; omitting them for an asymmetric proposal changes the target.

$$
a(x,y)=\min\!\left(1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\right),\qquad N_{\rm eff}\approx\frac{N}{1+2\sum_{k\ge1}\rho_k}.
$$

## Algorithm

Propose y, accept or retain x, and keep rejected repetitions as samples. Assess initial transients and use dispersed initial states across chains. Interpret autocorrelation-based effective sample size only when stationarity and autocorrelation estimation are credible.

## Conditions and pitfalls

Detailed balance alone does not establish irreducibility or aperiodicity. Multimodality, correlations and boundaries can slow mixing. High acceptance can simply reflect tiny moves. Thinning is not a general way to increase information for a fixed computational budget.

## What to check

Check means, variances and quantiles for known targets, including asymmetric proposals and rejections. For multimodal cases report between-chain comparisons, autocorrelations, effective sample sizes and uncertainty; visually flat traces alone are not proof of convergence.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- Nicholas Metropolis and Arianna W. Rosenbluth and Marshall N. Rosenbluth and Augusta H. Teller and Edward Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://doi.org/10.1093/biomet/57.1.97
