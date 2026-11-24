# Finite-Knudsen Couette and Fourier flows

Compare physical-time hard-sphere collisions,flux-weighted wall reemission and budgets with independent SPARTA references.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Hard-sphere DSMC finite-Kn Couette flow

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-algorithm)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

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

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,1],"speeds":[-0.5,0.5]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.


**Problem figure**

![Hard-sphere DSMC finite-Kn Couette flow: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en) (`dsmc-couette`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-validation)

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

- [Finite-Kn hard-sphere Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-couette-en) (`dsmc-couette`; Same-problem reference · Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.
### Assumptions, units and boundaries

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,1],"speeds":[-0.5,0.5]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

**Editorial clarification**

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

### Adopted numerical method

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

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

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

### Limits

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

### Stored measurements and decisions

```json
{
  "metrics": {
    "profile_comparison": {
      "2": {
        "error": 0.010200733750517737,
        "combined_3se": 0.018203904455731997,
        "primary_3se": 0.014988812559766168,
        "reference_3se": 0.01033042281233518
      },
      "4": {
        "error": 0.005173765945320263,
        "combined_3se": 0.01850394361570742,
        "primary_3se": 0.01567511391545536,
        "reference_3se": 0.009832941221769668
      },
      "0": {
        "error": 0.007959057017737909,
        "combined_3se": 0.013616367466408597,
        "primary_3se": 0.010491175758283632,
        "reference_3se": 0.008679901738445676
      }
    },
    "stationarity": {
      "profile_equivalence": {
        "2": 0.05759942531501381,
        "4": 0.0630869754804384,
        "0": 0.03964355800443746
      }
    },
    "sensitivities": {
      "fixed_weight_mesh": {
        "2": 0.006638448502787946,
        "4": 0.009141483700374766,
        "0": 0.007863505375904245
      },
      "double_particles": {
        "2": 0.02339932210675679,
        "4": 0.015641909218002674,
        "0": 0.01126054904988147
      },
      "half_dt": {
        "2": 0.029829998439110297,
        "4": 0.01349752351058444,
        "0": 0.012398286891856694
      }
    },
    "t95_multiplier_df3": 3.182446305284263,
    "flux": {
      "bulk_mean": -0.18636773527698747,
      "bulk_se": 0.0011643950494832711,
      "reference_mean": -0.19013665992789913,
      "reference_se": 0.0011647729920369507,
      "wall_mean": -0.18735052877662584,
      "wall_se": 0.001156037275432719,
      "wall_minus_bulk": -0.0009827934996383542,
      "wall_minus_bulk_se": 0.00010232411461678913
    }
  },
  "checks": {
    "dsmc-couette-base-361001/finite": true,
    "dsmc-couette-base-361001/boundary budget": true,
    "dsmc-couette-base-361001/physical collisions": true,
    "dsmc-couette-base-361001/collision probability": true,
    "dsmc-couette-base-361001/maxwell time resolution": true,
    "dsmc-couette-base-361001/mean free path resolution": true,
    "dsmc-couette-base-361002/finite": true,
    "dsmc-couette-base-361002/boundary budget": true,
    "dsmc-couette-base-361002/physical collisions": true,
    "dsmc-couette-base-361002/collision probability": true,
    "dsmc-couette-base-361002/maxwell time resolution": true,
    "dsmc-couette-base-361002/mean free path resolution": true,
    "dsmc-couette-base-361003/finite": true,
    "dsmc-couette-base-361003/boundary budget": true,
    "dsmc-couette-base-361003/physical collisions": true,
    "dsmc-couette-base-361003/collision probability": true,
    "dsmc-couette-base-361003/maxwell time resolution": true,
    "dsmc-couette-base-361003/mean free path resolution": true,
    "dsmc-couette-base-361004/finite": true,
    "dsmc-couette-base-361004/boundary budget": true,
    "dsmc-couette-base-361004/physical collisions": true,
    "dsmc-couette-base-361004/collision probability": true,
    "dsmc-couette-base-361004/maxwell time resolution": true,
    "dsmc-couette-base-361004/mean free path resolution": true,
    "dsmc-couette-fixed_weight_mesh-361001/finite": true,
    "dsmc-couette-fixed_weight_mesh-361001/boundary budget": true,
    "dsmc-couette-fixed_weight_mesh-361001/physical collisions": true,
    "dsmc-couette-fixed_weight_mesh-361001/collision probability": true,
    "dsmc-couette-fixed_weight_mesh-361001/maxwell time resolution": true,
    "dsmc-couette-fixed_weight_mesh-361001/mean free path resolution": true,
    "dsmc-couette-double_particles-361001/finite": true,
    "dsmc-couette-double_particles-361001/boundary budget": true,
    "dsmc-couette-double_particles-361001/physical collisions": true,
    "dsmc-couette-double_particles-361001/collision probability": true,
    "dsmc-couette-double_particles-361001/maxwell time resolution": true,
    "dsmc-couette-double_particles-361001/mean free path resolution": true,
    "dsmc-couette-half_dt-361001/finite": true,
    "dsmc-couette-half_dt-361001/boundary budget": true,
    "dsmc-couette-half_dt-361001/physical collisions": true,
    "dsmc-couette-half_dt-361001/collision probability": true,
    "dsmc-couette-half_dt-361001/maxwell time resolution": true,
    "dsmc-couette-half_dt-361001/mean free path resolution": true,
    "profile error/2": true,
    "primary precision/2": true,
    "reference precision/2": true,
    "profile error/4": true,
    "primary precision/4": true,
    "reference precision/4": true,
    "profile error/0": true,
    "primary precision/0": true,
    "reference precision/0": true,
    "stationarity/2": true,
    "stationarity/4": true,
    "stationarity/0": true,
    "bulk molecular flux agreement": true,
    "bulk molecular flux precision": true,
    "wall versus bulk molecular flux": true,
    "wall molecular flux precision": true,
    "half step sensitivity/2": true,
    "half step sensitivity/4": true,
    "half step sensitivity/0": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/index.json

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Sandia SPARTA developers (2026). SPARTA, pinned official HS collision/boundary implementation and independently evolved fields [accessed 2026-11-23]. https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399; review_level=primary-source-selected-functions-and-actual-reference-execution
Read selected official HS rate,boundary and moment definitions; execute36independent runs and87qualifiers. No full-original-book or whole-source audit claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Hard-sphere DSMC finite-Kn Fourier heat conduction

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-algorithm)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

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

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,2],"speeds":[0,0]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.


**Problem figure**

![Hard-sphere DSMC finite-Kn Fourier heat conduction: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en) (`dsmc-fourier`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-validation)

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

- [Finite-Kn hard-sphere Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-fourier-en) (`dsmc-fourier`; Same-problem reference · Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.
### Assumptions, units and boundaries

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,2],"speeds":[0,0]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

**Editorial clarification**

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

### Adopted numerical method

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

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

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

### Limits

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

### Stored measurements and decisions

```json
{
  "metrics": {
    "profile_comparison": {
      "4": {
        "error": 0.0046350333567375225,
        "combined_3se": 0.01986770882165603,
        "primary_3se": 0.018610142257145208,
        "reference_3se": 0.006956181351210389
      },
      "0": {
        "error": 0.006206560932103681,
        "combined_3se": 0.014725327832097481,
        "primary_3se": 0.012851725754092255,
        "reference_3se": 0.007188075187722132
      }
    },
    "stationarity": {
      "profile_equivalence": {
        "4": 0.06340714719603799,
        "0": 0.03983352063527729
      }
    },
    "sensitivities": {
      "fixed_weight_mesh": {
        "4": 0.02668632575679284,
        "0": 0.013283289135740131
      },
      "double_particles": {
        "4": 0.012688404465360077,
        "0": 0.009002412684556585
      },
      "half_dt": {
        "4": 0.008201282077196198,
        "0": 0.010766498591131742
      }
    },
    "t95_multiplier_df3": 3.182446305284263,
    "flux": {
      "bulk_mean": -0.5644605772254152,
      "bulk_se": 0.0023868795505760263,
      "reference_mean": -0.5756964840332293,
      "reference_se": 0.005479198503847574,
      "wall_mean": -0.566381423471522,
      "wall_se": 0.00224129249203519,
      "wall_minus_bulk": -0.00192084624610675,
      "wall_minus_bulk_se": 0.00029712049609058333
    }
  },
  "checks": {
    "dsmc-fourier-base-361101/finite": true,
    "dsmc-fourier-base-361101/boundary budget": true,
    "dsmc-fourier-base-361101/physical collisions": true,
    "dsmc-fourier-base-361101/collision probability": true,
    "dsmc-fourier-base-361101/maxwell time resolution": true,
    "dsmc-fourier-base-361101/mean free path resolution": true,
    "dsmc-fourier-base-361102/finite": true,
    "dsmc-fourier-base-361102/boundary budget": true,
    "dsmc-fourier-base-361102/physical collisions": true,
    "dsmc-fourier-base-361102/collision probability": true,
    "dsmc-fourier-base-361102/maxwell time resolution": true,
    "dsmc-fourier-base-361102/mean free path resolution": true,
    "dsmc-fourier-base-361103/finite": true,
    "dsmc-fourier-base-361103/boundary budget": true,
    "dsmc-fourier-base-361103/physical collisions": true,
    "dsmc-fourier-base-361103/collision probability": true,
    "dsmc-fourier-base-361103/maxwell time resolution": true,
    "dsmc-fourier-base-361103/mean free path resolution": true,
    "dsmc-fourier-base-361104/finite": true,
    "dsmc-fourier-base-361104/boundary budget": true,
    "dsmc-fourier-base-361104/physical collisions": true,
    "dsmc-fourier-base-361104/collision probability": true,
    "dsmc-fourier-base-361104/maxwell time resolution": true,
    "dsmc-fourier-base-361104/mean free path resolution": true,
    "dsmc-fourier-fixed_weight_mesh-361101/finite": true,
    "dsmc-fourier-fixed_weight_mesh-361101/boundary budget": true,
    "dsmc-fourier-fixed_weight_mesh-361101/physical collisions": true,
    "dsmc-fourier-fixed_weight_mesh-361101/collision probability": true,
    "dsmc-fourier-fixed_weight_mesh-361101/maxwell time resolution": true,
    "dsmc-fourier-fixed_weight_mesh-361101/mean free path resolution": true,
    "dsmc-fourier-double_particles-361101/finite": true,
    "dsmc-fourier-double_particles-361101/boundary budget": true,
    "dsmc-fourier-double_particles-361101/physical collisions": true,
    "dsmc-fourier-double_particles-361101/collision probability": true,
    "dsmc-fourier-double_particles-361101/maxwell time resolution": true,
    "dsmc-fourier-double_particles-361101/mean free path resolution": true,
    "dsmc-fourier-half_dt-361101/finite": true,
    "dsmc-fourier-half_dt-361101/boundary budget": true,
    "dsmc-fourier-half_dt-361101/physical collisions": true,
    "dsmc-fourier-half_dt-361101/collision probability": true,
    "dsmc-fourier-half_dt-361101/maxwell time resolution": true,
    "dsmc-fourier-half_dt-361101/mean free path resolution": true,
    "profile error/4": true,
    "primary precision/4": true,
    "reference precision/4": true,
    "profile error/0": true,
    "primary precision/0": true,
    "reference precision/0": true,
    "stationarity/4": true,
    "stationarity/0": true,
    "bulk molecular flux agreement": true,
    "bulk molecular flux precision": true,
    "wall versus bulk molecular flux": true,
    "wall molecular flux precision": true,
    "half step sensitivity/4": true,
    "half step sensitivity/0": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/index.json

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Sandia SPARTA developers (2026). SPARTA, pinned official HS collision/boundary implementation and independently evolved fields [accessed 2026-11-23]. https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399; review_level=primary-source-selected-functions-and-actual-reference-execution
Read selected official HS rate,boundary and moment definitions; execute36independent runs and87qualifiers. No full-original-book or whole-source audit claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
