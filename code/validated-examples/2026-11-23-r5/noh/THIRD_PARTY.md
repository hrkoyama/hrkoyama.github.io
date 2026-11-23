# Third-party provenance

The PDE finite-volume solver and analytic volume-integral reference are original
educational code. They do not import LANL ExactPack. The normal PDE runner is
offline and compares with the local analytic reference and saved independent
snapshot.

Independent reference software: **LANL ExactPack**, version 1.7.11, commit
`9bacc477eb791e959c9621e771fc7a725db755fa`.

- Repository: https://github.com/lanl/ExactPack
- Fixed code: https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa
- Noh module: `exactpack/solvers/noh/noh1.py`
- License: BSD-3-Clause, copyright ©2023 Triad National Security, LLC.
- Official license: https://github.com/lanl/ExactPack/blob/9bacc477eb791e959c9621e771fc7a725db755fa/LICENSE.txt

Unmodified hash-checked upstream Noh/base/package files were separately fetched
into a reference-only directory, executed, and used for saved point and
shock-split Gauss-quadrature checks. Upstream solver code and the paper's
figures/text are not silently vendored. The optional reference generator takes
that separately supplied pinned directory as `--upstream`; its receipt checks
all executable dependency hashes. See `exactpack-reference.json` for detailed
license, access depth, actual usage, citation and restrictions.

Software citation: J. Thrussell and J. M. Ferguson (2023), **ExactPack: A python
library of exact analytic solutions**, SoftwareX 24, article 101560,
https://doi.org/10.1016/j.softx.2023.101560 . LANL report LA-UR-23-25048.
The article license is CC BY-NC-ND 4.0, distinct from the BSD software license;
no assertion that its article text/figures are BSD-licensed is made.

Original physical problem: W. F. Noh (1987), **Errors for calculations of strong
shocks using an artificial viscosity and an artificial heat flux**, Journal of
Computational Physics 72(1), 78–120,
https://doi.org/10.1016/0021-9991(87)90074-X . Publisher metadata/abstract were
checked; the original full text was not accessed. This problem citation is
separate from the software citation and is not a claim that our particular
interface-stress discretization reproduces Noh's numerical method.

The independent snapshot is restricted to gamma=5/3, rho0=1 and u0=-1. The
upstream Noh module's pressure expression is not generalized in gamma although
its API accepts gamma. The saved gamma=1.4 diagnostic deliberately detects that
limitation. Geometry-3 reference samples must not be counted as spherical PDE
executions. No upstream validation suite or separate PDE engine was run.
