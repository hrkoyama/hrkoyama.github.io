# Mach2 planar shock with hard-sphere DSMC

For a1D-space,3D-velocity open-reservoir shock,distinguish RH far states from independent numerical internal-profile references.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Hard-sphere DSMC Mach2 planar shock

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-algorithm)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time. Open-reservoir macro counts use unbiased floor(mean)+Bernoulli(fraction) per face/species/half-stream to reduce artificial sampling variance; no Poisson number-fluctuation or thermodynamic-fluctuation reproduction claim. Retain the original four seeds and append the next eight consecutive seeds; uniform permutation/stable integer sorting preserves the ideal within-cell matching law,not RNG consumption or bit-identical trajectories. Edition2026-11-24 only reuses immutable reservoir coefficients and an inverse-CDF residual at unchanged v,fuses concatenation in unchanged keep-left-right order,and reversibly narrows range-checked integer sort keys to uint8 before the same stable sort. Original permutation/RNG calls,equal-key particle order,collision pairs and scientific inputs remain unchanged. The first three changes passed163component checks; a separate348check study qualifies the sort-key composition with exact byte/RNG comparisons. Neither is a new main run; full saved-science equality remains pending.

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [Hard-sphere Boltzmann transport,walls and reservoirs](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en) (`hard-sphere-boltzmann`)

{"kind":"shock","cells":192,"length":16,"weight":0.005208333333333333,"dt":0.01,"burn_in":20,"sample_time":20,"blocks":5,"bins":64,"sample_every":10,"hist_velocity":[-4,7]} Twelve independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.


**Problem figure**

![Hard-sphere DSMC Mach2 planar shock: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-validation)

Predeclare20pytest per group and15new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run. Preserve all81old gates and add48new-run gates=129. Primary12seed t95 usesdf11,reference4seed usesdf3; descriptive approximate-normal whole-seed intervals,not unconditional adaptive-study coverage. This new edition main has not run at contract freeze. Retain all20pytest,15runs,129gates and the original shared120s outer deadline,then compare every saved scientific array/history/metric with the immutable successful Nov23baseline. No independent reference is regenerated.

- [Mach2 planar hard-sphere shock](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-planar-shock-en) (`dsmc-planar-shock`; Same-problem reference · Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.
### Assumptions, units and boundaries

{"kind":"shock","cells":192,"length":16,"weight":0.005208333333333333,"dt":0.01,"burn_in":20,"sample_time":20,"blocks":5,"bins":64,"sample_every":10,"hist_velocity":[-4,7]} Twelve independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

**Editorial clarification**

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.

### Adopted numerical method

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time. Open-reservoir macro counts use unbiased floor(mean)+Bernoulli(fraction) per face/species/half-stream to reduce artificial sampling variance; no Poisson number-fluctuation or thermodynamic-fluctuation reproduction claim. Retain the original four seeds and append the next eight consecutive seeds; uniform permutation/stable integer sorting preserves the ideal within-cell matching law,not RNG consumption or bit-identical trajectories. Edition2026-11-24 only reuses immutable reservoir coefficients and an inverse-CDF residual at unchanged v,fuses concatenation in unchanged keep-left-right order,and reversibly narrows range-checked integer sort keys to uint8 before the same stable sort. Original permutation/RNG calls,equal-key particle order,collision pairs and scientific inputs remain unchanged. The first three changes passed163component checks; a separate348check study qualifies the sort-key composition with exact byte/RNG comparisons. Neither is a new main run; full saved-science equality remains pending.

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

### References and validation

Predeclare20pytest per group and15new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run. Preserve all81old gates and add48new-run gates=129. Primary12seed t95 usesdf11,reference4seed usesdf3; descriptive approximate-normal whole-seed intervals,not unconditional adaptive-study coverage. This new edition main has not run at contract freeze. Retain all20pytest,15runs,129gates and the original shared120s outer deadline,then compare every saved scientific array/history/metric with the immutable successful Nov23baseline. No independent reference is regenerated.

### Limits

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.

### Stored measurements and decisions

```json
{
  "metrics": {
    "profile_comparison": {
      "0": {
        "error": 0.009874127472267416,
        "combined_3se": 0.04946478705678961,
        "primary_3se": 0.03145643911579176,
        "reference_3se": 0.038174043494605424
      },
      "1": {
        "error": 0.006192836083404945,
        "combined_3se": 0.04640157562693747,
        "primary_3se": 0.03069818659770613,
        "reference_3se": 0.03479551063391386
      },
      "4": {
        "error": 0.008787013676147464,
        "combined_3se": 0.04976037231809162,
        "primary_3se": 0.035488922267584475,
        "reference_3se": 0.03488023866776783
      },
      "5": {
        "error": 0.008767734324833546,
        "combined_3se": 0.04646188409882251,
        "primary_3se": 0.03146941765264155,
        "reference_3se": 0.034181609479602165
      }
    },
    "stationarity": {
      "profile_equivalence": {
        "0": 0.051237907861461617,
        "1": 0.042550439680933805,
        "4": 0.052530861424159206,
        "5": 0.04623394154519991
      },
      "centroid_blocks": [
        [
          8.215335648148148,
          8.242578124999998,
          8.37534722222222,
          8.264756944444443,
          8.092187500000001
        ],
        [
          7.8806278935185174,
          7.732971643518519,
          7.8655381944444445,
          7.8228009259259235,
          7.707146990740742
        ],
        [
          8.088237847222222,
          8.194574652777776,
          8.386284722222221,
          8.335546875,
          8.221412037037037
        ],
        [
          7.609114583333332,
          7.680005787037035,
          7.577416087962962,
          7.347829861111112,
          7.23622685185185
        ],
        [
          7.620153356481483,
          7.693475115740742,
          7.670992476851854,
          7.572149884259257,
          7.589872685185185
        ],
        [
          8.473075810185184,
          8.567361111111111,
          8.567766203703703,
          8.53627025462963,
          8.390943287037034
        ],
        [
          8.005295138888886,
          8.019574652777777,
          7.905338541666666,
          7.990509259259259,
          7.868880208333332
        ],
        [
          8.190827546296296,
          8.03587962962963,
          8.154369212962964,
          8.220095486111111,
          8.337774884259257
        ],
        [
          8.411805555555553,
          8.436414930555557,
          8.455353009259259,
          8.48381076388889,
          8.650708912037034
        ],
        [
          8.18292824074074,
          8.153153935185184,
          8.265668402777775,
          8.268706597222222,
          8.303443287037037
        ],
        [
          7.841840277777777,
          7.737731481481482,
          7.718084490740742,
          7.826649305555556,
          7.872829861111111
        ],
        [
          7.868981481481481,
          7.905135995370369,
          7.91607349537037,
          8.006915509259258,
          7.7184895833333345
        ]
      ],
      "centroid_drift_bound": 0.1299701694340089
    },
    "sensitivities": {
      "fixed_weight_mesh": {
        "0": 0.04919268505889352,
        "1": 0.052838812527762305,
        "4": 0.0623901833211318,
        "5": 0.05359743514641371
      },
      "double_particles": {
        "0": 0.06216354691255698,
        "1": 0.06013078079263267,
        "4": 0.06006763400021631,
        "5": 0.06186520180345716
      },
      "half_dt": {
        "0": 0.03506052657485229,
        "1": 0.034593071784548436,
        "4": 0.0371459702067488,
        "5": 0.03752041004610139
      }
    },
    "primary_independent_seeds": 12,
    "primary_t95_degrees_of_freedom": 11,
    "primary_t95_multiplier": 2.200985160082949,
    "reference_independent_seeds": 4,
    "reference_t95_degrees_of_freedom": 3,
    "reference_t95_multiplier": 3.182446305284263,
    "far_states": {
      "upstream_n": {
        "relative_error": 0.0027311197916668473,
        "relative_3se": 0.004734773179813632
      },
      "upstream_ux": {
        "relative_error": 0.00226178222693619,
        "relative_3se": 0.004417322646908852
      },
      "upstream_T": {
        "relative_error": 0.00856692867855613,
        "relative_3se": 0.00919577401692969
      },
      "downstream_n": {
        "relative_error": 0.0007166883680555791,
        "relative_3se": 0.008778472486905992
      },
      "downstream_ux": {
        "relative_error": 0.0006619790814905539,
        "relative_3se": 0.011133999868080233
      },
      "downstream_T": {
        "relative_error": 0.0006120131785834495,
        "relative_3se": 0.0057144250470660685
      },
      "flux_mass": {
        "relative_error": 0.0009975883698689597,
        "relative_3se": 0.0029103940695329165
      },
      "flux_momentum": {
        "relative_error": 0.0013333838218918732,
        "relative_3se": 0.0028882793828942516
      },
      "flux_energy": {
        "relative_error": 0.0009104591488130677,
        "relative_3se": 0.00428618985183569
      }
    }
  },
  "checks": {
    "dsmc-planar-shock-base-371001/finite": true,
    "dsmc-planar-shock-base-371001/boundary budget": true,
    "dsmc-planar-shock-base-371001/physical collisions": true,
    "dsmc-planar-shock-base-371001/collision probability": true,
    "dsmc-planar-shock-base-371001/maxwell time resolution": true,
    "dsmc-planar-shock-base-371001/mean free path resolution": true,
    "dsmc-planar-shock-base-371002/finite": true,
    "dsmc-planar-shock-base-371002/boundary budget": true,
    "dsmc-planar-shock-base-371002/physical collisions": true,
    "dsmc-planar-shock-base-371002/collision probability": true,
    "dsmc-planar-shock-base-371002/maxwell time resolution": true,
    "dsmc-planar-shock-base-371002/mean free path resolution": true,
    "dsmc-planar-shock-base-371003/finite": true,
    "dsmc-planar-shock-base-371003/boundary budget": true,
    "dsmc-planar-shock-base-371003/physical collisions": true,
    "dsmc-planar-shock-base-371003/collision probability": true,
    "dsmc-planar-shock-base-371003/maxwell time resolution": true,
    "dsmc-planar-shock-base-371003/mean free path resolution": true,
    "dsmc-planar-shock-base-371004/finite": true,
    "dsmc-planar-shock-base-371004/boundary budget": true,
    "dsmc-planar-shock-base-371004/physical collisions": true,
    "dsmc-planar-shock-base-371004/collision probability": true,
    "dsmc-planar-shock-base-371004/maxwell time resolution": true,
    "dsmc-planar-shock-base-371004/mean free path resolution": true,
    "dsmc-planar-shock-base-371005/finite": true,
    "dsmc-planar-shock-base-371005/boundary budget": true,
    "dsmc-planar-shock-base-371005/physical collisions": true,
    "dsmc-planar-shock-base-371005/collision probability": true,
    "dsmc-planar-shock-base-371005/maxwell time resolution": true,
    "dsmc-planar-shock-base-371005/mean free path resolution": true,
    "dsmc-planar-shock-base-371006/finite": true,
    "dsmc-planar-shock-base-371006/boundary budget": true,
    "dsmc-planar-shock-base-371006/physical collisions": true,
    "dsmc-planar-shock-base-371006/collision probability": true,
    "dsmc-planar-shock-base-371006/maxwell time resolution": true,
    "dsmc-planar-shock-base-371006/mean free path resolution": true,
    "dsmc-planar-shock-base-371007/finite": true,
    "dsmc-planar-shock-base-371007/boundary budget": true,
    "dsmc-planar-shock-base-371007/physical collisions": true,
    "dsmc-planar-shock-base-371007/collision probability": true,
    "dsmc-planar-shock-base-371007/maxwell time resolution": true,
    "dsmc-planar-shock-base-371007/mean free path resolution": true,
    "dsmc-planar-shock-base-371008/finite": true,
    "dsmc-planar-shock-base-371008/boundary budget": true,
    "dsmc-planar-shock-base-371008/physical collisions": true,
    "dsmc-planar-shock-base-371008/collision probability": true,
    "dsmc-planar-shock-base-371008/maxwell time resolution": true,
    "dsmc-planar-shock-base-371008/mean free path resolution": true,
    "dsmc-planar-shock-base-371009/finite": true,
    "dsmc-planar-shock-base-371009/boundary budget": true,
    "dsmc-planar-shock-base-371009/physical collisions": true,
    "dsmc-planar-shock-base-371009/collision probability": true,
    "dsmc-planar-shock-base-371009/maxwell time resolution": true,
    "dsmc-planar-shock-base-371009/mean free path resolution": true,
    "dsmc-planar-shock-base-371010/finite": true,
    "dsmc-planar-shock-base-371010/boundary budget": true,
    "dsmc-planar-shock-base-371010/physical collisions": true,
    "dsmc-planar-shock-base-371010/collision probability": true,
    "dsmc-planar-shock-base-371010/maxwell time resolution": true,
    "dsmc-planar-shock-base-371010/mean free path resolution": true,
    "dsmc-planar-shock-base-371011/finite": true,
    "dsmc-planar-shock-base-371011/boundary budget": true,
    "dsmc-planar-shock-base-371011/physical collisions": true,
    "dsmc-planar-shock-base-371011/collision probability": true,
    "dsmc-planar-shock-base-371011/maxwell time resolution": true,
    "dsmc-planar-shock-base-371011/mean free path resolution": true,
    "dsmc-planar-shock-base-371012/finite": true,
    "dsmc-planar-shock-base-371012/boundary budget": true,
    "dsmc-planar-shock-base-371012/physical collisions": true,
    "dsmc-planar-shock-base-371012/collision probability": true,
    "dsmc-planar-shock-base-371012/maxwell time resolution": true,
    "dsmc-planar-shock-base-371012/mean free path resolution": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/finite": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/boundary budget": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/physical collisions": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/collision probability": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/maxwell time resolution": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/mean free path resolution": true,
    "dsmc-planar-shock-double_particles-371001/finite": true,
    "dsmc-planar-shock-double_particles-371001/boundary budget": true,
    "dsmc-planar-shock-double_particles-371001/physical collisions": true,
    "dsmc-planar-shock-double_particles-371001/collision probability": true,
    "dsmc-planar-shock-double_particles-371001/maxwell time resolution": true,
    "dsmc-planar-shock-double_particles-371001/mean free path resolution": true,
    "dsmc-planar-shock-half_dt-371001/finite": true,
    "dsmc-planar-shock-half_dt-371001/boundary budget": true,
    "dsmc-planar-shock-half_dt-371001/physical collisions": true,
    "dsmc-planar-shock-half_dt-371001/collision probability": true,
    "dsmc-planar-shock-half_dt-371001/maxwell time resolution": true,
    "dsmc-planar-shock-half_dt-371001/mean free path resolution": true,
    "profile error/0": true,
    "primary precision/0": true,
    "reference precision/0": true,
    "profile error/1": true,
    "primary precision/1": true,
    "reference precision/1": true,
    "profile error/4": true,
    "primary precision/4": true,
    "reference precision/4": true,
    "profile error/5": true,
    "primary precision/5": true,
    "reference precision/5": true,
    "stationarity/0": true,
    "stationarity/1": true,
    "stationarity/4": true,
    "stationarity/5": true,
    "centroid stationarity": true,
    "RH far or full flux/upstream_n": true,
    "RH precision/upstream_n": true,
    "RH far or full flux/upstream_ux": true,
    "RH precision/upstream_ux": true,
    "RH far or full flux/upstream_T": true,
    "RH precision/upstream_T": true,
    "RH far or full flux/downstream_n": true,
    "RH precision/downstream_n": true,
    "RH far or full flux/downstream_ux": true,
    "RH precision/downstream_ux": true,
    "RH far or full flux/downstream_T": true,
    "RH precision/downstream_T": true,
    "RH far or full flux/flux_mass": true,
    "RH precision/flux_mass": true,
    "RH far or full flux/flux_momentum": true,
    "RH precision/flux_momentum": true,
    "RH far or full flux/flux_energy": true,
    "RH precision/flux_energy": true,
    "half step sensitivity/0": true,
    "half step sensitivity/1": true,
    "half step sensitivity/4": true,
    "half step sensitivity/5": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/index.json

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock-preview.png)

Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/atlas-dsmc-shock-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Sandia SPARTA developers (2026). SPARTA, pinned official HS collision/boundary implementation and independently evolved fields. https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399; review_level=primary-source-selected-functions-and-actual-reference-execution
Read selected official HS rate,boundary and moment definitions; execute36independent runs and87qualifiers. No full-original-book or whole-source audit claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
