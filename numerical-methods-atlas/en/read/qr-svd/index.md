# QR, SVD and least squares

Least squares, low-rank approximation and conditioning call for different matrix decompositions. QR reduces a problem to orthogonal transformations and a triangular solve; SVD exposes singular values and resolvable directions.

## Problem and representative equations

For a real m×n matrix with m≥n, thin QR has QᵀQ=I and upper triangular R. Full column rank gives the least-squares solve Rx=Qᵀb. SVD has nonnegative singular values σᵢ. Truncating small σᵢ in a pseudoinverse regularizes the problem and can change the solution being sought.

$$
A=QR=U\Sigma V^T,\qquad \min_x\|Ax-b\|_2,\qquad A^+b=\sum_{\sigma_i>\tau}\frac{u_i^Tb}{\sigma_i}v_i\quad\text{(truncated)}.
$$

## Algorithm

Householder QR eliminates subdiagonal entries with reflections and generally maintains orthogonality better than classical Gram–Schmidt. Consider column pivoting or SVD for rank diagnosis. Classical SVD algorithms reduce to bidiagonal form using orthogonal transformations rather than explicitly forming normal equations.

## Conditions and pitfalls

For full column rank, κ₂(AᵀA)=κ₂(A)². A small residual can coexist with uncertain coefficients under ill-conditioning or noise. Choose a numerical-rank threshold relative to scale, rounding and measurement uncertainty, and consider column scaling when variables have different units.

## What to check

Check relative factorization residuals, orthogonality and Aᵀ(Ax−b). Test prescribed singular values and rank-deficient cases, and compare solution changes under controlled data perturbations.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- Alston S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://doi.org/10.1145/320941.320947
- G. H. Golub and C. Reinsch (1970). Singular value decomposition and least squares solutions. https://doi.org/10.1007/bf02163027
