"""Fixed-input numerical checks. Exit 0=pass, 1=acceptance failed, 2=invalid/error.

No output is overwritten. Statistical thresholds are fixed in inputs, not fitted.
"""
import argparse
import csv
import hashlib
import json
import platform
from pathlib import Path
import sys
import numpy as np
from models import logistic, sir, monte_carlo, gbm


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(path):
    p = json.loads(path.read_text())
    case = p['case']
    metrics, checks, table = {}, {}, []
    if case in ('logistic-growth', 'sir-epidemic'):
        errors, minimum, balance = [], float('inf'), 0.
        reference_path = Path(__file__).parent/'references/sir.json'
        reference = json.loads(reference_path.read_text()) if case == 'sir-epidemic' else None
        if reference and reference['input_sha256'] != sha(path):
            raise ValueError('SIR reference belongs to a different input')
        for steps in p['steps']:
            t, y = (logistic if case == 'logistic-growth' else sir)(p, steps)
            if reference:
                ref = np.asarray(reference['values'][str(steps)])
            else:
                ref = (p['capacity']/(1+(p['capacity']/p['initial']-1)*np.exp(-p['rate']*t)))[:, None]
            error = float(np.abs(y-ref).max())
            errors.append(error)
            minimum = min(minimum, float(y.min()))
            if reference:
                balance = max(balance, float(np.abs(y.sum(axis=1)-sum(p['initial'])).max()))
            table.extend([[steps, float(time), *map(float, value), *map(float, target)]
                          for time, value, target in zip(t, y, ref)])
        orders = [float(np.log(a/b)/np.log(nb/na)) for a,b,na,nb in
                  zip(errors, errors[1:], p['steps'], p['steps'][1:])]
        metrics.update(errors=errors, observed_orders=orders, finest_max_error=errors[-1], minimum_state=minimum)
        checks.update(accuracy=errors[-1] <= p['acceptance']['max_error'],
                      refinement=min(orders) >= p['acceptance']['min_order'], nonnegative=minimum>=0)
        if reference:
            metrics['mass_balance_max'] = balance
            checks['mass_balance'] = balance <= p['acceptance']['mass_tolerance']
            metrics['reference_sha256'] = sha(reference_path)
        header = ['steps', 'time'] + (['S','I','R','S_reference','I_reference','R_reference'] if reference else ['population','analytic'])
    elif case == 'mc-integral':
        exact, variance = 1/3, 4/45  # Analytic integrals of x^2 and x^4 on [0,1].
        rms, ratios, coverages = [], [], []
        for n, estimates, se in monte_carlo(p):
            rms.append(float(np.sqrt(np.mean((estimates-exact)**2))))
            ratios.append(rms[-1]/np.sqrt(variance/n))
            coverages.append(float(np.mean(np.abs(estimates-exact)<=1.96*se)))
            table.extend([[n, seed, float(est), float(err), exact] for seed,est,err in zip(p['seeds'],estimates,se)])
        metrics.update(rms_errors=rms, rms_over_theory=ratios, coverage_95=coverages,
                       refinement_ratio=rms[-1]/rms[0], replications=len(p['seeds']))
        a=p['acceptance']
        checks.update(rms_scale=all(a['rms_ratio_min']<=r<=a['rms_ratio_max'] for r in ratios),
                      statistical_refinement=a['refinement_min']<=metrics['refinement_ratio']<=a['refinement_max'],
                      interval_calibration=all(a['coverage_min']<=c<=a['coverage_max'] for c in coverages))
        header=['samples','seed','estimate','estimated_standard_error','analytic_integral']
    elif case == 'gbm-sde':
        errors=[]
        for n, y, exact in gbm(p):
            errors.append(float(np.sqrt(np.mean((y-exact)**2))))
            table.extend([[n,j,float(v),float(e)] for j,(v,e) in enumerate(zip(y,exact))])
        orders=[float(np.log(a/b)/np.log(nb/na)) for a,b,na,nb in zip(errors,errors[1:],p['steps'],p['steps'][1:])]
        exact_mean=p['initial']*np.exp(p['mu']*p['end'])
        exact_variance=p['initial']**2*np.exp(2*p['mu']*p['end'])*np.expm1(p['sigma']**2*p['end'])
        z=abs(float(exact.mean())-exact_mean)/np.sqrt(exact_variance/p['paths'])
        metrics.update(strong_rms_errors=errors, observed_orders=orders, finest_rms_error=errors[-1], exact_sample_mean_z=float(z),paths=p['paths'])
        a=p['acceptance']
        checks.update(strong_accuracy=errors[-1]<=a['max_rms_error'],
                      strong_refinement=all(a['min_order']<=r<=a['max_order'] for r in orders),
                      brownian_sample_mean=z<=a['max_mean_z'])
        header=['steps','path','euler_maruyama_endpoint','coupled_exact_endpoint']
    else:
        raise ValueError('Unknown fixed-input case')
    checks={key:bool(value) for key,value in checks.items()}
    return dict(schema_version=1,case=case,input_sha256=sha(path),
                environment={'python':platform.python_version(),'numpy':np.__version__},
                termination='fixed_budget_completed',metrics=metrics,checks=checks,passed=all(checks.values())), header, table


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.output.exists() and any(args.output.iterdir()):
            raise ValueError('Output directory must be new or empty')
        result,header,rows=evaluate(args.input)
        args.output.mkdir(parents=True,exist_ok=True)
        (args.output/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
        with (args.output/'solution.csv').open('w',newline='') as f:
            writer=csv.writer(f);writer.writerow(header);writer.writerows(rows)
        print(json.dumps(result))
        return 0 if result['passed'] else 1
    except Exception as exc:
        print(str(exc),file=sys.stderr)
        return 2


if __name__=='__main__':
    sys.exit(main())
