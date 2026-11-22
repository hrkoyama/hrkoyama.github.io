# Biology and stochastic numerical benchmarks / 生物・確率計算の検証例

Python 3.12. Install `python -m pip install -r requirements.txt`.
Run `python -m pytest -q`, then for example:

    python run.py --input inputs/logistic-growth.json --output output

Replace the input with sir-epidemic.json, mc-integral.json or gbm-sde.json.
Output is result.json (input SHA-256, environment, metrics, checks, termination)
and solution.csv. Exit: 0 accepted, 1 numerical criteria failed, 2 input/runtime error.
Existing nonempty output is refused. Inputs fix all budgets and tolerances.

Scope: dimensionless logistic population and closed homogeneous normalized SIR
(no spatial boundary), IID x² integration on U[0,1], and scalar Itô geometric
Brownian motion. These examples do not validate SEIR, reaction–diffusion,
Hodgkin–Huxley, MCMC, rare events or general SDEs. RK4 and Euler–Maruyama are
not unconditionally positivity preserving.

Logistic RK4 is compared at every output time with its analytic solution.
SIR RK4 is compared with independent SciPy DOP853; reference_sir.py imports
neither models.py nor run.py. Its saved reference includes two-tolerance agreement.
Regenerate it with `python reference_sir.py` before rerunning package checks.
Time refinement, nonnegativity and S+I+R conservation are checked independently.

Monte Carlo uses 256 independent PCG64 seeds; prefixes within each seed are
nested. Analytic integral 1/3 and single-sample variance 4/45 give RMS and N^-1/2
checks. 95% normal-interval coverage is an empirical diagnostic, not a guaranteed
confidence statement for other integrands or random seeds. GBM couples coarse
and fine Brownian increments with an exact endpoint. RMS strong convergence
and analytic mean sampling error are checked; no weak-order claim is made.

Original code: MIT (LICENSE). Inputs, numerical outputs, plots and prose retain
item-specific terms at https://hrkoyama.github.io/rights/ . No third-party paper
text or software source is bundled. NumPy/SciPy/pytest retain their own licenses.

Primary sources are linked in the bilingual Atlas execution entries and their
reading chapters; implementations are original educational code.
