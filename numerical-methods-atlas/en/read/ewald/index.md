# Ewald summation

Ewald summation evaluates periodic Coulomb interactions through complementary real- and reciprocal-space sums. It defines a different boundary-value problem from simply truncating 1/r at a finite radius.

## Problem and representative equations

Consider point charges qᵢ in a neutral, triply periodic cell. Set rᵢⱼₙ=rᵢ−rⱼ+n, cell volume V, splitting parameter α>0 and reciprocal vector k. S(k) is the charge structure factor. The energy below uses unit Coulomb prefactor, omits k=0 and assumes a conducting macroscopic boundary. The prime excludes only i=j,n=0.

$$
\begin{aligned}S(\mathbf k)&=\sum_jq_j e^{i\mathbf k\cdot\mathbf r_j},\\E&=\frac12\sum_{i,j,\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2.\end{aligned}
$$

## Algorithm

Accumulate screened real-space pairs and Gaussian-damped reciprocal modes, then subtract the self energy. Restore the same Coulomb prefactor to every term in dimensional units. Changing α redistributes work between sums but cannot change their converged total. Derive forces from the same energy convention.

## Conditions and pitfalls

A net-charged cell requires an additional convention such as a compensating background. Specify potential gauge, surface term, periodic self images and molecular exclusions separately. A periodic gravitational Poisson solve changes the kernel/sign and mean-density treatment; it is not the same calculation.

## What to check

For a small neutral configuration, increase both cutoffs independently and test α independence. Compare forces with finite differences of energy, and check translation invariance and net force. Agreement between two unconverged sums is not independent validation.

## Publication scope

Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.

## Sources

- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
- Hockney, R. W. and Eastwood, J. W. (1981). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934
