"""Independent SIR reference: SciPy DOP853, no educational solver imported.

Reference is numerical, not an exact solution; includes a tighter-tolerance check.
"""
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp


def main():
    root=Path(__file__).parent
    path=root/'inputs/sir-epidemic.json';p=json.loads(path.read_text())
    def rhs(t,y):
        incidence=p['beta']*y[0]*y[1]
        return [-incidence,incidence-p['gamma']*y[1],p['gamma']*y[1]]
    solutions=[]
    for rtol,atol in [(1e-11,1e-13),(1e-13,1e-15)]:
        sol=solve_ivp(rhs,[0,p['end']],p['initial'],method='DOP853',rtol=rtol,atol=atol,dense_output=True)
        if not sol.success:raise RuntimeError(sol.message)
        solutions.append({str(n):sol.sol(np.linspace(0,p['end'],n+1)).T for n in p['steps']})
    delta=max(float(abs(solutions[0][str(n)]-solutions[1][str(n)]).max()) for n in p['steps'])
    if delta>1e-9:raise RuntimeError('Reference tolerance check failed')
    result={'method':'independent SciPy solve_ivp DOP853','input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
            'rtol':1e-13,'atol':1e-15,'tolerance_refinement_max_difference':delta,
            'values':{n:y.tolist() for n,y in solutions[1].items()}}
    dest=root/'references/sir.json';dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':main()
