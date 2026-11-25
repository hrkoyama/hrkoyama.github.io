# HH and immigration–death controls

This is a new educational edition. The fixed equations, actions and caps are in inputs.json. acceptance.json separates mandatory component/reference qualification from original study goals. Preparing this source does not count as an execution or completion. Numerical execution requires a root/peer freeze of the exact bytes.

## Hodgkin–Huxley

Use the NEURON8.2.6 analytic absolute-mV convention at6.3°C, not its TABLE/cnexp discretization or the original1952 polarity. The pinned equations have unit capacitance and Na/K/leak conductances120/36/.3. The potassium beta rate is .125 exp(-(V+65)/80). Stable expm1 evaluation gives alpha_m(-40)=1 and alpha_n(-55)=.1. Fifteen actual binary64 voltages are separately evaluated by80/120digit Decimal formulae. Their hexadecimal inputs, absolute discrepancies and precision companions are retained.

At prescribed voltage, each gate has exact solution z_inf+(z0-z_inf)exp(-(alpha+beta)t). The error is the maximum over **all accepted times and gates**. The original1e-8finest-step target is a study target, never assumed true. In fact the earlier real-arithmetic RK4 lower-bound analysis atV=-80 rules out treating this universal target as a guaranteed pass. No final-only norm is substituted.

A Decimal bisection brackets a zero-current equilibrium in[-80,-50] with a1e-30width and256iteration cap. Both endpoint signs and precision companions are stored. The binary64 equilibrium is checked against the actual current balance. Uniqueness and interval-Hurwitz stability are **unclaimed**; a nearby residual alone is not such a certificate.

For the pulse, physical I=10 on10<=t<11. The integrator separately owns[0,10] atI0,[10,11] atI10,[11,30] atI0. All four stages in a step use its segment current, including the left-limit right endpoint. Restart with the right-limit force; store an event's endpoint derivative freshly at its accepted state. The RK4 k4 stage is not that derivative. Twelve pulse-only edge actions detect the endpoint mistake even when opposite area errors would cancel. Every accepted-interval Hermite cubic is split at its derivative critical points, including intervals without an endpoint sign change. All upward0mV crossings are retained with ownership(tn,tn+1],and multiple/interior/tangent or roundoff-ambiguous cases are audited explicitly. Manufactured cubics exercise two interior crossings,three roots and a tangent. This qualifies the interpolating polynomial model,not exact continuous-ODE event completeness. Missing/multiple or ambiguous firing comparisons remain unresolved outcomes.

Independent scalar RHS implementations use adaptive DP5(4), tighter DP5(4), and Cash–Karp5(4), landing at every .01ms comparison endpoint, without dense output or FSAL reuse. Three configurations times(rest+three pulse segments) give twelve propagations, each with a50000RHS cap. Finite agreement is a qualification indicator, not a rigorous global error bound. Voltage, gates, event timing, and rest drift remain separate study goals.

## Immigration–death SSA

The direct SSA uses rates6 and n. New clocks and reaction uniforms are drawn only when no pending event exists. A pending event is applied iff its time is<=the observation time; it is retained otherwise. Reaction equality belongs to death, and a death fromn0 is invalid. Time stagnation, negative counts and fixed caps terminate with retained evidence.

PCG64 is explicitly pinned to NumPy2.0.2. Each initialization/event stream has entropy[20261125,89,record,seed,path,purpose]. Raw uint64 values produce j=raw>>11; zero is rejected at most8times, and U=j2^-53 is strictly inside(0,1). No epsilon clipping, OS entropy or seed search is used. Fixed-start initialization streams may legitimately be unchanged. Uniqueness concerns both the24578actual initial(state,increment)pairs and their namespaces,including unused initialization streams and two display streams,not initial-versus-final inequality. Distinct initial states are not a theorem of statistical independence.

Each original particle survives independently with probability p=exp(-t). Independent Poisson immigrants survive with thinned mean integral_0^t6exp(-(t-s))ds=6(1-p); independence gives the Binomial-plus-Poisson law. Poisson6initial survivors have mean6p,so adding immigrant survivors preserves Poisson6. This is an authored elementary derivation,not an imported external scalar reference.

For deterministic n0, the ideal transient is Bin(n0,p)+Pois(6(1-p)),p=exp(-t). The stationary ideal law is Pois6. A finite deterministic-start transient is not stationary. Six ensembles each contain2048paths; a separate seed11display path is not substituted for ensemble evidence. Every initial/final generator state, increment, raw/rejection count, jump count and censored pending event is retained.

The mathematical law reference uses nonnegative directed Decimal interval arithmetic at80and120digits. Decimal.exp is correctly rounded first and enclosed by its neighboring representables, rather than incorrectly assuming directed exp rounding. Mode-centered positive relative weights have geometric omitted-tail bounds. Normalization uses the retained sum plus both tails. Binomial–Poisson CDFs are prefix convolutions, with omitted binomial mass allowed anywhere. Each factor has at most4097weights/2048halfwidth; tails target1e-25and CDF widths1e-18. Quantile bounds and initial inverse-CDF integer thresholds must agree across precisions. The Poisson6initial table uses k0..128,ceil(2^53F(k))-1; it is qualified before samples and has finite-grid discrepancy<=1/(2^53-1), rather than being called an exact continuous draw.

Seven unique per-path laws and seven sum laws are built before sampling. Twenty nondegenerate comparisons each have a DKW family and an exact-sum mean family, delta1/4000each, nominal union bound .01. The four deterministic time0 checks have zero variance and no artificial standardized statistic. The sum law is Bin(Mn0,p)+Pois(6M(1-p)) or Pois(6M), not a fitted Gaussian. Mean-tail acceptance uses P(sum<L)<=1/8000 and P(sum>U)<=1/8000. Five-SE variance goals use the exact fourth-cumulant formula and are outside that40-family bound. All actual goals, including nominal random failures, remain visible.

Coverage language concerns the ideal IID law. Directed CDF qualification is not a rigorous bound on the entire PRNG/grid/logarithm implementation. No general mixing inference follows from one fixed sample or displayed trajectory.

## Gallery

Both figures per case read saved NPZ/JSON data. HH shows actual voltage/gate phase portraits and clamp convergence. SSA shows a distinct path, an empirical probability heat map and all-six-ensemble distribution/mean diagnostics. Labels use English to avoid a font installation; descriptions are bilingual.

The concentration reference is Massart(1990),DOI10.1214/aop/1176990746,selected original abstract,and Reeve(2024),arXiv2403.16651v1,selected IID setup and theorem/corollaries. These support the ideal independent-sample CDF bound; detailed original proofs were not fully audited. Source-reading records the original Gillespie algorithm selected pp2343–2345/eq8–21 separately from this linear-model derivation.
