"""Independent scaled quadrature of ordinary importance moments; no sampling."""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import log_ndtr


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise ValueError('Fresh independent moment output required')
    cfg=json.loads(a.input.read_text());checks={};records={};limits=json.loads((a.input.parent/'acceptance.json').read_text())['limits']
    for threshold in cfg['cases']['normal-tail-importance']['thresholds']:
        logp=float(log_ndtr(-threshold));moments=[]
        for power in [1,2,3,4]:
            integral,error=quad(lambda z:math.exp(-power*threshold*z-.5*z*z),0,np.inf,epsabs=1e-13,epsrel=1e-13)
            independent_log=-power*threshold**2/2+math.log(integral)-.5*math.log(2*math.pi)
            formula_log=.5*power*(power-1)*threshold**2+float(log_ndtr(-power*threshold))
            checks[f'{threshold}/moment{power}']=bool(abs(math.expm1(independent_log-formula_log))<=limits['IS_reference_moment_relative'])
            moments.append(math.exp(formula_log))
        ptrue=math.exp(logp);var=ptrue*ptrue*math.expm1(math.log(moments[1])-2*logp)
        checks[f'{threshold}/erfc']=bool(abs(ptrue-.5*math.erfc(threshold/math.sqrt(2)))<=1e-12*ptrue)
        checks[f'{threshold}/variancepositive']=bool(var>0)
        checks[f'{threshold}/variancereduction']=bool(var/(ptrue*(1-ptrue))<limits['IS_analytic_variance_reduction_ratio'])
        checks[f'{threshold}/omitted_weight_negative']=bool(.5/ptrue>limits['IS_negative_control_min_ratio'])
        for point in [-2.,0.,3.]:
            ratio=math.exp(-point*point/2)/math.exp(-(point-threshold)**2/2);weight=math.exp(-threshold*point+.5*threshold**2)
            checks[f'{threshold}/weight_sign/{point}']=bool(abs(ratio-weight)<=1e-12*weight)
        records[str(threshold)]={'probability':ptrue,'moments1to4':moments,'variance':var,'direct_variance':ptrue*(1-ptrue),'reference_scope':'Independent scaled positive adaptive integral versus completed-square log-normal-tail formula.'}
    result={'schema_version':1,'passed':all(checks.values()),'checks':checks,'records':records,'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),'acceptance_sha256':hashlib.sha256((a.input.parent/'acceptance.json').read_bytes()).hexdigest(),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stochastic_samples':0}
    a.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({'passed':result['passed'],'checks':len(checks)}))
    if not result['passed']:raise SystemExit(1)

if __name__=='__main__':main()
