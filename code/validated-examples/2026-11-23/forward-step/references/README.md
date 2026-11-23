# Independent C++ forward-facing-step reference

This directory contains a separately implemented C++17 MUSCL/HLL/Heun reference for the same fixed uncorrected-corner Euler problem as the primary first-order Python example. It imports no primary or Numart operator. The HLL flux and Heun time-integrator families are shared; it is not an external-code/experimental validation.

The reference is newly executed for this edition, unlike the preceding Double Mach example that reused saved RKDG-kit arrays. Run `run-reference.py --scratch NEW_ABSOLUTE_SCRATCH_DIRECTORY` only under the project disk guard after freezing `pre-run-contract.json`. It compiles `reference.cpp` with `/usr/bin/c++ -std=c++17 -O3 -Wall -Wextra -Werror`, runs algebra/geometry/budget self-tests, and computes Ny80 and Ny160 once. `convert.py` saves the exact raw double arrays as compressed NPZ plus execution metadata and grid-difference diagnostics. The `independent-execution.json` receipt records compiler version, full commands, timings and stdout/stderr. Ordinary public Python verification reuses these saved arrays; it does not compile C++ or rerun the reference PDE.

No entropy/enthalpy reset is applied near the step corner. This differs from the specially treated corner in Woodward--Colella's reference calculation; corner entropy errors and downstream numerical layers remain a limitation. See `definition.json` and `citations.json`. The finite-grid reference is neither an exact solution nor an error bound. No special state floors, state repairs or rejected-step retries are allowed. Directional primitive slope rescaling preserves each conserved cell average and is counted separately. Both updated RK stages must have finite positive density and pressure. Actual wall pressure tractions are included in the Heun-weighted flux budget.

MIT license: see `REFERENCE-LICENSE.txt`.

## Preserved first reference attempt

Attempt01 compiled and passed the algebra/geometry/budget self-tests, then completed Ny80 in27.20s with positive density/pressure and no floors, retries or slope rescalings. Ny160 exceeded the predeclared120-second process limit. Its actual failed execution receipt, driver traceback, frozen source/contract and completed Ny80 arrays/metadata remain under `attempts/01/`. No completed Ny160 state exists for that attempt.

Before a second execution, revision02 changes only the type of the diagnostic `require` message argument from `const std::string&` to `const char*`, removing repeated long-string construction on successful checks. The numerical arithmetic, initial/boundary conditions, limiter, CFL, two grids, final time, scientific acceptance criteria and120-second timeout are unchanged. The new contract honestly records that an earlier reference execution has already occurred. This is a performance correction, not a relaxed scientific criterion.
