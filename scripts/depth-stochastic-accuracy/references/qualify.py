"""Bounded pre-trajectory moment/precision/resolution qualification."""
import argparse,hashlib,json,math,sys
from pathlib import Path
from decimal import Decimal,localcontext
import numpy as np
from scipy.special import roots_hermitenorm
from scipy.integrate import quad
from analytic import gbm,ou,strong,encode
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from paths import bridge_coefficients


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def slope(h,y):return float(np.polyfit(np.log(h),np.log(np.abs(y)),1)[0])


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise ValueError('Use a fresh reference output directory')
    a.output.mkdir(parents=True);cfg=json.loads(a.input.read_text());limits=json.loads((a.input.parent/'acceptance.json').read_text())['limits'];checks={};records={};details=[]
    def add(name,passed):checks[name]=bool(passed)
    for ident,c in cfg['cases'].items():
        rows=[]
        if ident.endswith('strong'):
            for n in c['steps']:
                row={}
                for method in ['em','milstein']:
                    lo=strong(c,n,method,80);hi=strong(c,n,method,120)
                    add(f'{ident}/{n}/{method}/precision',abs(lo['mse']-hi['mse'])<=Decimal(limits['reference_decimal_relative'])*hi['mse'])
                    row[method]=encode(lo)
                    tiny={**c,'T':c['T']/n,'initial':1.}
                    oracle=strong(tiny,1,method,120)['mse']
                    for order in [32,64]:
                        z,w=roots_hermitenorm(order);dw=z*np.sqrt(tiny['T']);h=tiny['T']
                        increment=c['mu']*h+c['sigma']*dw
                        if method=='milstein':increment+=.5*c['sigma']**2*(dw*dw-h)
                        difference=increment-np.expm1((c['mu']-.5*c['sigma']**2)*h+c['sigma']*dw)
                        measured=float(w@(difference*difference)/np.sqrt(2*np.pi))
                        add(f'{ident}/{n}/{method}/GH{order}',abs(measured-float(oracle))<=limits['reference_one_step_relative']*float(oracle))
                rows.append(row)
        else:
            function=gbm if c['kind']=='gbm' else ou
            for n in c['steps']:
                lo=function(c,n,80);hi=function(c,n,120)
                for obs in range(2):
                    add(f'{ident}/{n}/{obs}/variancepositive',lo['paired_variance'][obs]>0)
                    add(f'{ident}/{n}/{obs}/precision',abs(lo['paired_variance'][obs]-hi['paired_variance'][obs])<=Decimal(limits['reference_decimal_relative'])*hi['paired_variance'][obs])
                    if n in c['steps'][-2:]:
                        ratio=3*math.sqrt(float(lo['paired_variance'][obs])/(len(c['seeds'])*c['paths_per_batch']))/abs(float(lo['bias'][obs]))
                        details.append({'id':ident,'n':n,'observable_power':obs+1,'predicted_3MCSE_over_bias':ratio,'allocation_paths':len(c['seeds'])*c['paths_per_batch']})
                        add(f'{ident}/{n}/{obs}/pre_sampling_resolution',ratio<=limits['reference_resolution_3se_fraction'])
                if c['kind']=='ou':
                    k=c['kappa'];h=c['T']/n;decay=1-k*h
                    independent=c['sigma']**2*sum(decay**(n-1-j)*quad(lambda s:math.exp(-k*(c['T']-s)),j*h,(j+1)*h,epsabs=1e-14)[0] for j in range(n))
                    add(f'{ident}/{n}/independent_covariance',abs(independent-float(lo['joint_covariance']))<=2e-13)
                    alpha,beta=bridge_coefficients(k,h)
                    with localcontext() as ctx:
                        ctx.prec=80;kd=Decimal(str(k));hd=Decimal(str(h));cd=(1-(-kd*hd).exp())/kd;vd=(1-(-2*kd*hd).exp())/(2*kd)
                    add(f'{ident}/{n}/bridge_covariance',abs(alpha*h-float(cd))<=2e-13*float(cd))
                    add(f'{ident}/{n}/bridge_variance',abs(alpha*alpha*h+beta*beta-float(vd))<=2e-13*float(vd))
                rows.append(encode(lo))
            for obs in range(2):
                order=slope(np.array([c['T']/n for n in c['steps'][-3:]]),np.array([x['bias'][obs] for x in rows[-3:]]))
                add(f'{ident}/{obs}/analytic_order',limits['weak_analytic_order'][0]<=order<=limits['weak_analytic_order'][1])
        records[ident]=rows
        (a.output/'partial-reference.json').write_text(json.dumps({'checks':checks,'records':records,'details':details},indent=2,allow_nan=False)+'\n')
    result={'schema_version':1,'passed':all(checks.values()),'checks':checks,'records':records,'pre_sampling_resolution':details,'input_sha256':sha(a.input),'acceptance_sha256':sha(a.input.parent/'acceptance.json'),'source_sha256':{'analytic.py':sha(Path(__file__).with_name('analytic.py')),'qualify.py':sha(Path(__file__))},'scope':'Decimal80/120 precision,independent GH32/64one-step squared-error quadrature and OU piecewise covariance integral; no stochastic trajectory. These analytic moments are authored and reviewed identities,not a copied paper table.'}
    (a.output/'reference.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':result['passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}))
    if not result['passed']:raise SystemExit(1)

if __name__=='__main__':main()
