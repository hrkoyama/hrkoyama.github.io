# Monte Carlo integration

Monte Carlo integration estimates an integral as an expectation. Accuracy depends on the sampling distribution, weights and variance, not merely on using random numbers.

## Problem and representative equations

Draw independent samples Xᵢ from a density p covering the support of f and average Yᵢ=f(Xᵢ)/p(Xᵢ). With finite second moment, estimate standard error by s_Y/√N. Uniform sampling requires the domain-volume factor.

$$
I=\int f(x)\,dx=\mathbb E_p\!\left[\frac{f(X)}{p(X)}\right],\qquad \widehat I_N=\frac1N\sum_{i=1}^N\frac{f(X_i)}{p(X_i)},\quad\widehat{\operatorname{SE}}=s_Y/\sqrt N.
$$

## Algorithm

Specify the distribution and random generator, draw samples and compute the weighted mean and variance. Importance sampling concentrates p where contributions matter, while monitoring heavy tails of f/p. Record generator/version, seed and sample count for reproducibility.

## Conditions and pitfalls

The N⁻¹/² scale is statistical and conditional on assumptions such as independence and finite variance; it is not a deterministic bound for each run. Rare events and missed peaks can make variance estimates misleading. Correlated MCMC samples need a different uncertainty calculation.

## What to check

Use repeated independent runs on known integrals to examine N scaling and interval coverage. Record actual mean error separately from estimated uncertainty, and verify that changes in importance density preserve the target integral.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- Nicholas Metropolis and S. Ulam (1949). The Monte Carlo Method. https://doi.org/10.1080/01621459.1949.10483310
