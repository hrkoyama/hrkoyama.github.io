# Cell-average spatial biology controls

All primary, reference and component rows are fixed before execution. A completed reproduction requires qualified references and all mandatory checks. Accuracy/order/positivity study targets keep their actual outcomes, including misses or null orders. Local solver tolerances and finite sensitivity differences are never called rigorous global error bounds. No figures or results are fabricated by preparation.

## Fisher–KPP

For D=r=1, U=(1+exp((x-ct)/sqrt6))^-2 solves U_t=U_xx+U(1-U) only at the special speed c=5/sqrt6. Substitution provides an authored identity check; putting c2 into this same profile is an explicit negative control. The leading-edge relation c=lambda+1/lambda>=2 is a distinct linear-selection fact. This protocol does not simulate steep-data selection of the minimum speed.

Nine primary rows separate space(h.5/.25/.125,dt=h²/20),time(h.25,dt.01/.005/.0025),and constant-endpoint boundary domainsL6/12/24. Exact time-dependent Dirichlet data are owned at SSPRK3 stage times t,t+dt,t+dt/2. Time accuracy is compared to a separately implemented95unknown same-MOL reference at two fixed DP5(4) tolerances, sampled at401endpoints. It is not measured against the continuum front and mislabeled as temporal error. Quarter-contour ambiguity is explicit.

For the constant-endpoint L12/L24 comparison, a real-arithmetic discrete maximum-principle barrier on |x|<=3 is2exp(sigma-18),sigma=1+128(cosh(.25)-1). Since cosh(.25)<=32/31,sigma<6,and2exp(-12)<1e-4. Positivity of Euler and the positive SSPRK3 stage polynomial justify the real discrete comparison. This is **not** a floating-point error certificate. Actual binary64 core differences and observed margin are saved separately; all full-domain errors and initial endpoint mismatches remain available.

## Schnakenberg2D

Solve u_t=.01Lap(u)+.1-u+u²v and v_t=Lap(v)+.9-u²v on[0,2pi]² toT2, about equilibrium(1,.9). There are three fixed initial profiles: Neumann(4,2),Neumann mixed(2,4)+.5(3,1),and equilibrium-Dirichlet sine(4,2). Exact cell averages of those point profiles initialize12/24/48cell grids. Results do not establish mature patterns or generic pattern selection.

Cell-average diffusion uses one internal face owner. Neumann faces have zero normal gradient. For Dirichlet equilibrium, deviations use ghost=-firstcell; a corner owns two distinct normal faces, not an extra diagonal face. The full two-dimensional CN map is applied with a qualified discrete eigenbasis; its symbols are independently checked against a face-flux Laplacian. Strang composition is CN(dt/2),local implicit-midpoint reaction(dt),CN(dt/2). Newton has cap12/residual1e-13 with no clipping. Boundary and midpoint source ledgers use the actual substep states.

The independent nonlinear Galerkin reference uses orthonormal tensor bases: Neumann mode0=1/sqrtL,other modes sqrt(2/L)cos(mpi x/L),m0..K-1;Dirichlet sqrt(2/L)sin(mpi x/L),m1..K. Array indices are lexicographic(m,n),not a radial truncation. The equilibrium is separated explicitly. Cell-average basis values are center values times sinc(m/(2N)),with sinc0=1. Legendre tensor quadrature reconstructs and projects the nonlinear reaction, independently from the FV helper.

For every IC retain four rows(K,Q,tolerance):12/96/1e-10,18/96/1e-10,18/192/1e-10,18/192/1e-12. Thus DeltaK changes onlyK,DeltaQ onlyQ,and Deltatol onlytolerance. This pre-execution Q64->96 correction preserves four rows while removing a confounded K/Q difference. Each row has a4000RHS cap and all snapshots0/.5/1/2. Each delta is the maximum over both fields,all snapshots and all three primary cell grids. Each and their sum must be<=2e-4,and the sum<=.1times the finest primary discrepancy when that discrepancy>1e-12. At/below that floor, reference-relative accuracy and order are unresolved, never certified by a zero denominator. These are finite sensitivity indicators, not a continuum enclosure. Additional N48 dt1/200 and1/400 rows compare directly with dt1/800states; a difference/3 is labeled a second-order Richardson **indicator**,not a proved temporal bound.

Fifty-four linear mode/time/grid/boundary actions use continuum and discrete2x2Jacobian exponentials, each compared through closed formulae and independent scaling/Taylor/squaring(216matrix actions). Constant equilibria, wrong-boundary and duplicated-corner negative controls prevent a purely shared-formula pass.

## Forced Keller–Segel

This is an authored smooth forced two-field system, not the full original biological model or a blow-up experiment. On[0,1]² toT.25,use n=1+A cospi x cospi y,A=.1e^-t; c=1+B cospi x cos2pi y,B=.05e^-2t. The streamfunction sinpi x sinpi y/pi gives exactly owned, divergence-free face averages and zero normal boundary velocity.

Use J=w avg(n)-Dn grad(n)+chi avg(n)grad(c),Dn.02,Dc.1,chi.2,r.1,tau=alpha=lambda1. External normal fluxes are zero. Both fields and all source terms use the same SSPRK3 stage, at0/1/half times with actual ledger weights1/6,1/6,2/3. No lagged c or clipped n is introduced.

The exact forcing is obtained by inserting the manufactured fields. Its primary expanded cell polynomial is independently checked against an unexpanded derivative/product integral formulation. Mean cos0=1,cosacosb=.5[cos(a-b)+cos(a+b)],and sinasinb=.5[cos(a-b)-cos(a+b)];these identities handle zero-frequency limits. Twelve frozen corner/face/interior points times three times give36source pairs. Two independently defined whole-grid states onN4at three times give96cell vector pairs. Wrong chi sign, omitted c coupling, stale source time and duplicated normal-face flux must be detected.

The eight primary rows consist of N12/24/48space series(1024steps),N24time64/128/256steps,N48half-dt2048steps,and one N24constant-unforced control256steps. Independent scalar face loops and separate unexpanded source integrals define the N24same-MOL DP5(4) reference at two tolerances,all65coarse endpoints,and4000RHS per row. Spatial error uses exact cell averages; temporal error uses the same MOL. Continuum integrals n=c=1,integral reaction_n=-rA²/4,integral source_n=+rA²/4,and integral source_c=0 are reported separately from the actual numerical stage ledger.

## Saved-data figures

Fisher uses a numerical space-time field and profile/boundary/convergence diagnostics. Schnakenberg shows all three actual2D final fields and saved Galerkin discrepancies. Keller–Segel shows actual density,exact cell-average field,error,and convergence/mass-ledger diagnostics. No solver is invoked by plot.py.


## One controlled Dirichlet reference extension after the first frozen failure

The complete first R4fixed run finished all49records without an exception or timeout. Only the original Dirichlet reference qualification failed:K12->18sensitivity4.995141182306817e-5,quadrature1.5543122344752192e-15,tolerance3.1374902675906924e-13. The total was below2e-4but above.1times the finest primary discrepancy9.088196030337947e-5. The actual first failure,source/input/criteria hashes and measurements remain in source-reading.json/prior_reference_qualification. It is not relabeled as a successful original protocol.

Keep all11primary evolutions,all12original nonlinear reference actions and all54linear actions. The original4Dreference rows are recomputed and saved as legacy qualification,including their actual qualified/unqualified outcome. Add exactly four D-only reference actions:(K24,Q128,rtol1e-10,atol1e-12),(K32,Q128,1e-10,1e-12),(K32,Q192,1e-10,1e-12),(K32,Q192,1e-12,1e-14). Each retains the4000RHS cap. Both newKvalues exceed the former finest18; this is not a narrowed comparison between already insufficient resolutions.

A single assessment function applies the unchanged maximum norm over both fields,all snapshots and all12/24/48primary grids. NewDeltaK,Q,tolerance each and their sum must be<=2e-4,and the sum<=.1times the NEW finest primary discrepancy above the unchanged1e-12denominator floor. Only if these qualify is the K32/Q192tight reference used to resolve Daccuracy/order goals. Otherwise the group remains nonPASS and affected goals remain NULL. There is no fallback to the unqualified K18reference,no tolerance relaxation,no dropped old row,and no automated resolution search. Sixteen nonlinear reference solves now belong to the fixed spatial protocol. The115s owned main and120s shared budgets remain unchanged; a cap stops with retained completed records and owned handled-failure evidence.
