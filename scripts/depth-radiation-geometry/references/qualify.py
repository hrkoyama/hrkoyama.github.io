"""Fixed characteristic-cell-mean and closed-M1 forcing qualification."""
import argparse,json,sys
from pathlib import Path
import numpy as np
from analytic import shadow,beams,crossed,mms_cells,mms_forcing_complex_step
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import geometry,mms


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Fresh reference output required')
    a.output.mkdir(parents=True,exist_ok=True);checks={};details=[]
    def add(key,value,bound):checks[key]=bool(value<=bound);details.append(dict(name=key,value=float(value),bound=bound,passed=checks[key]))
    for kind,function,grids,final in [('shadow',shadow,[24,48,96],1.1),('beams',beams,[24,48,96],.5),('mms',mms_cells,[16,32,64],.25),('crossed',crossed,[24,48,96],.25)]:
        for cells in grids:
            fields=[];times=np.linspace(0,final,5)
            for i,time in enumerate(times):
                low=function(cells,float(time),8);middle=function(cells,float(time),16);high=function(cells,float(time),32)
                d1=float(np.max(abs(middle-low)));d2=float(np.max(abs(high-middle)))
                add(f'{kind}/{cells}/{i}/finite',0. if np.isfinite(high).all() else 1.,0.)
                add(f'{kind}/{cells}/{i}/quadrature',d2,2e-4 if kind=='shadow' else 1e-10)
                add(f'{kind}/{cells}/{i}/refinement',d2,max(.5*d1,1e-10));fields.append(high)
            np.savez(a.output/f'{kind}-n{cells}.npz',times=times,moments=np.array(fields))
            (a.output/'completed.json').write_text(json.dumps(details,indent=2)+'\n')
    x=np.array([.031,.187,.443,.719,.913]);y=np.array([.089,.293,.527,.681,.853])
    for t in [0.,.117,.25]:
        _,force=mms.state_and_forcing(x,y,t);reference=mms_forcing_complex_step(x,y,t)
        add('M1/analytic-forcing/'+str(t),np.max(abs(force-reference)),2e-12)
    states=np.array([[0.,0.,0.],[1.,0.,0.],[1.,1.,0.],[1.,0.,1.],[1.,.2,.1]])
    pressure=geometry.pressure(states)
    add('M1/full3Dtrace',np.max(abs(pressure[:,0]+pressure[:,2]+pressure[:,3]-states[:,0])),2e-14)
    add('M1/isotropic',np.max(abs(pressure[1]-[1/3,0.,1/3,1/3])),2e-14)
    add('M1/single-beam',np.max(abs(pressure[2]-[1.,0.,0.,0.])),2e-14)
    add('M1/equal-two-beam-closure-defect',abs((1-pressure[1,0])-2/3),2e-14)
    for i,state in enumerate([[1.,1.1,0.],[0.,.1,0.],[-1.,0.,0.],[-1e-14,1.,0.]]):
        rejected=False
        try:geometry.pressure(np.array([state]))
        except ArithmeticError:rejected=True
        add('M1/invalid-state-rejected/'+str(i),0. if rejected else 1.,0.)
    result=dict(passed=all(checks.values()),checks=checks,check_count=len(checks),details=details,scope='Independent characteristic cell means and complex-step qualification of analytically derived CLOSED M1forcing;local tensor limits. No primary PDE execution.',PDE_primary_runs=0)
    (a.output/'qualification.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({'passed':result['passed'],'checks':len(checks)}))
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
