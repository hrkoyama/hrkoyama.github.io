# Tiny neural PDE models and biological ODE controls

Five educational cases implement logical candidates 84, 85 and 87; candidate
86 is shared selected-source curation and adds no numerical example. At this
main pre-execution freeze, no primary training, trajectory or pytest has run.
The separate reference/component stage has passed all 92 checks with 20
independent ODE propagations. That does not establish primary accuracy or
optimizer convergence.
See PROTOCOL.md, inputs.json, acceptance.json and source-reading.json for exact
fixed inputs, independent roles and unread-source limits. No paper benchmark
speed, universal OOD guarantee or statistical coverage is claimed.

Use Python3.12 and the exact requirements pins; set BLAS/OMP thread counts to1.
The bundled results are saved examples; rerun into a NEW directory:

    python -B -W error -m pytest -q -p no:cacheprovider
    python -B -W error run.py --input inputs.json --output output
    python plot.py --results output/result.json --output output

Plotting additionally uses requirements-plotting.txt and reads stored data
only. Main never imports Matplotlib. Reproduction checks and original study
accuracy goals have separate boolean maps; unmet goals stay visibly unmet.
Actual source/ZIP verification will be in results/result.json and verification.json.

At the R2 premeasurement design review, normal fixed-budget learning returns
were separated from optimizer convergence. Native success remains an actual
TRUE/FALSE study outcome. A normal budget return is not called converged;
abnormal or unreturned runs remain failures. No input, seed, optimizer
tolerance, budget or accuracy goal was changed. See PROTOCOL.md for exact
PINN and FNO termination rules.

The first reference attempt retained an unmet SEIR cross-engine margin:
1.3287260181e-11 exceeded the original 1e-11 target. The revised independent
SEIR reference solves the same physical system in deviation coordinates
((S-1)/eta, E/eta, I/eta, R/eta). The numerical solver tolerances are applied
to those scaled variables, improving effective physical resolution; physical
acceptance thresholds remain unchanged. See history/reference-r2-failure/
for compact readable evidence. Complete original source, native trajectories
and failure receipts remain in the private archive; they are not all duplicated
in this compact public history. Main uses the qualified cache without reference
regeneration.

Failure evidence includes completed candidates and already written checkpoints.
It does not guarantee recovery of every unflushed live stage or library state.
In particular, an exception inside an RK4 loop can leave only the most recent
32-event checkpoint; successful complete trajectories are saved before later
diagnostics. SIGKILL can preserve only data already written to disk.
