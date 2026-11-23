# gravity-dynamics

Fixed lightweight original scientific source, currently pre-run/unexecuted.

```sh
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-results
```

Three exact direct dependency pins; Matplotlib is plotting-only. Pytest plus all fixed inputs share one120second deadline. Runner requires unchanged frozen input/source and fresh output. Partial case/checkpoints and available failed candidates are retained. No tolerance repair or hidden state floor. Every successful case writes nonempty finite CSV and the strict public result envelope. NPZs retain full actual arrays. Plotting reads saved arrays only. Source read depth and original-paper access limits are explicit under references/. No external numerical package is required.

- gravity-kepler: G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.
- gravity-plummer-short: Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening. Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

First frozen execution passed18/18 tests and78/78 gates (Kepler31,cold47),nine primary trajectories and two independent referenceIVPs within4.409seconds combined. Actual public result/finiteCSV policy passed. No numerical failure/revision or acceptance change. Two saved-array PNG/SVG/PDF/previews rendered separately.

For the density recipe, Phi=-GM/sqrt(r²+a²) implies enclosed M(r)=r²Phi_prime/G and F(r)=r³/(r²+a²)^(3/2). This supplies radial quantiles only; velocities are coldzero, not sampled from an equilibrium distribution function.
