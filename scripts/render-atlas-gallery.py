#!/usr/bin/env python3
"""Render scientific previews from stored values and nine fixed public-code examples.

Optional authoring command: use the code edition's pinned plotting requirements.
Normal refresh-site.py only checks the resulting receipts; it never reruns these solves.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json,platform,sys,textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
OUT=ATLAS/'gallery'
OUT.mkdir(exist_ok=True)
(OUT/'previews').mkdir(exist_ok=True)
CODE=json.loads((ROOT/'catalog/atlas-methods.json').read_text())['code_base']
sys.path.insert(0,str(ROOT/CODE.lstrip('/')))
from numart.benchmarks import get_problem
from numart.solvers import solve
from numart.linear import Boundary,poisson_boundary_1d,poisson_2d
from numart.krylov import CSR,apply,newton
from numart.runge_kutta import rk_step
from numart.stiff import integrate

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white','figure.facecolor':'white','axes.prop_cycle':plt.cycler(color=['#a05235','#3f685b','#355e83','#887133'])})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
config=json.loads((ROOT/'catalog/atlas-gallery.json').read_text())
problems={x['id']:x for x in json.loads((ROOT/'catalog/atlas-test-problems.json').read_text())['problems']}
receipts={'catalog/atlas-gallery.json':sha(ROOT/'catalog/atlas-gallery.json'),'scripts/render-atlas-gallery.py':sha(Path(__file__))}
for name in ['benchmarks.py','solvers.py','linear.py','krylov.py','runge_kutta.py','stiff.py']:
    path=CODE.lstrip('/')+'numart/'+name;receipts[path]=sha(ROOT/path)
cache={}
def data(path):
    if path not in cache:
        cache[path]=json.loads((ATLAS/path).read_text());receipts['numerical-methods-atlas/'+path]=sha(ATLAS/path)
    return cache[path]
def choose(rows,**where):return next(x for x in rows if all(x.get(k)==v for k,v in where.items()))
def curve(x,y,label,reference=False):
    return {'x':np.asarray(x).tolist(),'y':np.asarray(y).tolist(),'label':label,'reference':reference}
def plot(series,xlabel='x',ylabel='value',log=False):
    return {'series':series,'xlabel':xlabel,'ylabel':ylabel,'loglog':log}

def computed(id):
    if id=='double-rarefaction':
        p=get_problem(id);r=solve(p,128,riemann='hlle')
        w=p.equation.primitive(r.q);exact=p.equation.primitive(p.reference(r.x,r.time))
        error=float(np.mean(abs(w[:,0]-exact[:,0])))
        assert r.time==p.final_time and w[:,0].min()>0 and w[:,2].min()>0 and error<.08
        return {'inputs':{'problem':id,'n':128,'solver':'HLLE','final_time':p.final_time,'boundary':p.boundary},'checks':{'density_l1':error,'minimum_density':float(w[:,0].min()),'minimum_pressure':float(w[:,2].min())},'plot':plot([curve(r.x,w[:,0],'HLLE density'),curve(r.x,exact[:,0],'Pointwise reference',True)],ylabel='density')}
    if id in ['poisson-1d-neumann','poisson-1d-mixed','poisson-1d-robin']:
        n=31
        if id.endswith('neumann'):
            x,q=poisson_boundary_1d(n,-2.,Boundary.neumann(0.),Boundary.neumann(2.));exact=x*x
            exact-=(x[1]-x[0])*(exact.sum()-.5*(exact[0]+exact[-1]))
            inputs={'n':n,'forcing':-2,'outward_neumann':[0,2],'trapezoidal_mean':0};limit=1e-10
        elif id.endswith('mixed'):
            x,q=poisson_boundary_1d(n,-2.,Boundary.dirichlet(1.),Boundary.neumann(2.));exact=1+x*x
            inputs={'n':n,'forcing':-2,'left_dirichlet':1,'right_outward_neumann':2};limit=1e-10
        else:
            x,q=poisson_boundary_1d(n,lambda x:-np.exp(x),Boundary(2.,1.,1.),Boundary(1.,1.,2*np.e));exact=np.exp(x)
            inputs={'n':n,'forcing':'-exp(x)','left_robin':[2,1,1],'right_robin':[1,1,2*float(np.e)]};limit=.002
        error=float(np.max(abs(q-exact)));assert error<limit
        return {'inputs':inputs,'checks':{'maximum_error':error,'error_limit':limit},'plot':plot([curve(x,q,'Computed solution'),curve(x,exact,'Reference',True)],ylabel='u(x)')}
    if id=='poisson-2d-random':
        n=13;f=np.random.default_rng(8).normal(size=(n,n));x,y,q,_=poisson_2d(n,forcing=f)
        a=np.pad(q,1);residual=(4*q-a[:-2,1:-1]-a[2:,1:-1]-a[1:-1,:-2]-a[1:-1,2:])*(n+1)**2-f
        norm=float(np.linalg.norm(residual));assert norm<1e-8
        return {'inputs':{'n':n,'seed':8,'source':'normal random forcing','boundary':'zero Dirichlet'},'checks':{'discrete_residual_norm':norm,'residual_limit':1e-8},'plot':{'field':q.tolist(),'x':x[:,0].tolist(),'y':y[0,:].tolist(),'extent':[.5/(n+1),1-.5/(n+1),.5/(n+1),1-.5/(n+1)],'xlabel':'x','ylabel':'y','color_label':'discrete solution'}}
    if id=='bratu':
        errors=[]
        for n in [31,63]:
            x=np.arange(1,n+1)/(n+1);lam=2/np.cosh(.5)**2
            a=(2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1))*(n+1)**2
            def jac(u):
                d=a-np.diag(lam*np.exp(u));i,j=np.nonzero(d)
                return CSR.from_coo(i,j,d[i,j],d.shape)
            result=newton(lambda u:apply(a,u)-lam*np.exp(u),jac,np.zeros(n),linear_solver='gmres')
            assert result.converged
            exact=-2*np.log(np.cosh(x-.5)/np.cosh(.5));errors.append(float(np.max(abs(result.x-exact))))
        assert errors[0]/errors[1]>3.8 and errors[-1]<1e-4
        return {'inputs':{'n':63,'lambda':float(lam),'equation':'-u_xx=lambda*exp(u)','boundary':'u(0)=u(1)=0','solver':'damped Newton / GMRES'},'checks':{'errors_n31_n63':errors,'refinement_ratio':errors[0]/errors[1]},'plot':plot([curve(np.r_[0,x,1],np.r_[0,result.x,0],'Newton-Krylov'),curve(np.r_[0,x,1],np.r_[0,exact,0],'Reference',True)],ylabel='u(x)')}
    if id=='nonlinear-exp-ode':
        dt=.025;t=np.linspace(0,1,41);q=[1.]
        for time in t[:-1]:q.append(float(rk_step(lambda t,y:-y*y+np.exp(2*t)+np.exp(t),time,q[-1],dt,'rk4')))
        exact=np.exp(t);error=float(np.max(abs(np.array(q)-exact)));assert error<1e-5
        return {'inputs':{'equation':"y'=-y^2+exp(2t)+exp(t)",'initial':1,'dt':dt,'steps':40,'method':'RK4'},'checks':{'maximum_error':error,'error_limit':1e-5},'plot':plot([curve(t,q,'RK4'),curve(t,exact,'exp(t)',True)],xlabel='time',ylabel='y(t)')}
    if id=='nonlinear-rational-ode':
        f=lambda t,y:-y*y+np.sin(t)*(y-1/(1+t));jac=lambda t,y:np.diag(-2*y+np.sin(t))
        t,q=integrate(f,jac,[1.],dt=.025,method='sdirk2');exact=1/(1+t)
        error=float(np.max(abs(q[:,0]-exact)));assert error<.001
        return {'inputs':{'equation':"y'=-y^2+sin(t)*(y-1/(1+t))",'initial':1,'dt':.025,'final_time':1,'method':'SDIRK2'},'checks':{'maximum_error':error,'error_limit':.001},'plot':plot([curve(t,q[:,0],'SDIRK2'),curve(t,exact,'1/(1+t)',True)],xlabel='time',ylabel='y(t)')}
    if id=='cubic-root':
        r=newton(lambda x:x**3-1,lambda x:np.diag(3*x*x),[.1]);error=float(abs(r.x[0]-1));assert r.converged and error<1e-9
        return {'inputs':{'function':'x^3-1','initial':.1,'method':'Armijo-damped Newton'},'checks':{'root':float(r.x[0]),'root_error':error,'residual':float(r.residuals[-1])},'plot':{'series':[curve(np.arange(len(r.residuals)),np.maximum(r.residuals,1e-16),'Residual')],'xlabel':'Newton iteration','ylabel':'absolute residual (floor 1e-16)','semilogy':True}}
    raise ValueError(id)

def stored(item):
    kind=item['kind'];d=data(item['source'])
    if kind=='wave-profile':
        c=choose(d['cases'],id=item['case']);f=c['frames'][-1]
        curves=[curve(c['x'],f['u'],'Numerical')]
        if f.get('exact') is not None:curves.append(curve(c['x'],f['exact'],'Reference',True))
        return plot(curves,ylabel=c['field'])
    if kind=='cip-profile':
        c=choose(d['cases'],profile=item['profile'],speed=1.)
        return plot([curve(c['x'],c[k],label,k=='exact') for k,label in [('cip','CIP'),('linear','Linear interpolation'),('exact','Exact shift')]],ylabel='u(x)')
    if kind in ['reconstruction-profile','ppm-profile']:
        rows=d['cases'] if kind=='reconstruction-profile' else [c for c in d['ppm_cases'] if c['status']=='completed']
        c=choose(rows,problem=item['problem'])
        return plot([curve(c['x'],np.array(c['primitive'])[:,0],c.get('method',c.get('config','Computed')))],ylabel='density')
    if kind=='entropy-refinement':
        c=d['entropy'];return plot([curve(c['n'],v['errors'],v['label']) for v in c['series']],xlabel='grid cells',ylabel=c['norm'],log=True)
    if kind=='lbm-shear':
        c=d['lbm'];return plot([curve(c['shear_time'],c['shear_amplitude'],'LBM'),curve(c['shear_time'],c['shear_exact'],'Viscous reference',True)],xlabel='lattice time',ylabel='shear amplitude')
    if kind=='lbm-channel':
        c=d['lbm'];return plot([curve(c['channel_y_over_h'],c['channel_velocity'],'LBM'),curve(c['channel_y_over_h'],c['channel_exact'],'Reference',True)],xlabel='y / channel height',ylabel='velocity')
    if kind=='poisson-1d-refinement':
        rows=d['one_dimensional'];series=[]
        for method in sorted({c['method'] for c in rows}):
            c=sorted([r for r in rows if r['method']==method],key=lambda x:x['n']);series.append(curve([r['n'] for r in c],[r['continuous_rms'] for r in c],method))
        return plot(series,xlabel='interior nodes',ylabel='nodal RMS error',log=True)
    if kind=='multigrid-residual':
        r=np.array(d['metrics']['multigrid']['residual_history']);return {'series':[curve(np.arange(len(r)),r/r[0],'V-cycle residual')],'xlabel':'V-cycle','ylabel':'relative residual','semilogy':True}
    if kind=='hyperbolic-refinement':
        c=d['hyperbolic_diffusion'];return plot([curve(c['n'],c['l2'],'Steady solution')],xlabel='grid cells',ylabel='RMS error',log=True)
    if kind=='krylov-residual':
        return {'series':[curve(np.arange(len(c['residuals'])),c['residuals'],c['name']) for c in d['krylov']],'xlabel':'Krylov iteration','ylabel':'true relative residual','semilogy':True}
    if kind=='tree-force':
        rows=d['isolated_tree']['measurements'];series=[]
        for order in [0,2]:
            c=[r for r in rows if r['order']==order];series.append(curve([r['theta'] for r in c],[r['relative_rms_force_error'] for r in c],f'Expansion order {order}'))
        return {'series':series,'xlabel':'opening angle theta','ylabel':'relative RMS force error','semilogy':True}
    if kind=='hamiltonian-orbit':
        rows=[c for c in d['cases'] if c['system']==item['system'] and c['h']==.1 and c['method'] in ['verlet','rk4']];series=[]
        for c in rows:
            mask=np.array(c['t'])<=10;series.append(curve(np.array(c['q'])[mask],np.array(c['p'])[mask],c['method']))
        assert len(series)==2
        return plot(series,xlabel='position q',ylabel='momentum p')
    if kind=='stiff-refinement':
        return plot([curve(c['dt'],c['maximum_error'],c['method']) for c in d['stiff']],xlabel='time step',ylabel='maximum error',log=True)
    if kind=='basis-approximation':
        c=choose(d['approximations'],profile=item['profile'],degree=8)
        return plot([curve(d['x'],c[k],label,k=='exact') for k,label in [('projected','Projection'),('interpolated','Interpolation'),('exact','Original function')]],ylabel='function value')
    if kind=='rk-refinement':
        rows=[c for c in d['refinement'] if c['method'] in ['forward-euler','ssprk3','rk4']]
        return plot([curve(c['dt'],c['error'],c['method']) for c in rows],xlabel='time step',ylabel='final-time error',log=True)
    raise ValueError(kind)

def render(values,path):
    fig,ax=plt.subplots(figsize=(6.4,3.8),layout='constrained')
    if 'field' in values:
        field=np.array(values['field']);assert np.isfinite(field).all()
        im=ax.imshow(field.T,origin='lower',extent=values['extent'],cmap='viridis',aspect='auto')
        fig.colorbar(im,ax=ax,label=values['color_label'])
    else:
        assert values['series']
        for c in values['series']:
            x,y=np.array(c['x']),np.array(c['y']);assert x.shape==y.shape and x.ndim==1 and len(x)>1 and np.isfinite(x).all() and np.isfinite(y).all()
            fn=ax.loglog if values.get('loglog') else ax.semilogy if values.get('semilogy') else ax.plot
            fn(x,y,'--' if c['reference'] else '-',label=c['label'],linewidth=1.8,marker='o' if len(x)<12 else None,markersize=4)
        ax.legend(fontsize=8,loc='best');ax.grid(alpha=.18)
    ax.set(xlabel=values['xlabel'],ylabel=values['ylabel'])
    fig.savefig(path,dpi=130);plt.close(fig)

manifest=[];calculations={}
for item in config['items']:
    id=item['id'];assert id in problems
    if item['kind']=='image':
        path=(ROOT/item['source'].lstrip('/')) if item['source'].startswith('/') else (ATLAS/item['source']);receipts[path.relative_to(ROOT).as_posix()]=sha(path)
        image_url='/'+path.relative_to(ROOT).as_posix();kind='existing-figure'
    else:
        if item['kind']=='computed-preview':
            record=computed(id);calculations[id]=record;values=record['plot'];kind='computed-preview'
        else:values=stored(item);kind='stored-data-plot'
        path=OUT/'previews'/f'{id}.png';render(values,path)
        image_url='/numerical-methods-atlas/gallery/previews/'+id+'.png'
    with Image.open(path) as image:
        width,height=image.size
    manifest.append({'id':id,'image':image_url,'image_sha256':sha(path),'width':width,'height':height,'source_kind':kind,'caption':item['caption']})
assert len(manifest)==len(problems) and len(calculations)==9
(OUT/'calculations.json').write_text(json.dumps({'scope':'Nine fixed-input public-code visualizations. These nine previews do not create additional independent problem families; separately packaged atomic examples have their own execution records.','code_edition':CODE,'environment':{'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__},'cases':calculations},ensure_ascii=False,indent=2)+'\n')
(OUT/'preview-manifest.json').write_text(json.dumps({'schema_version':1,'reviewed_on':'2026-11-21','items':manifest,'source_sha256':receipts,'calculations_sha256':sha(OUT/'calculations.json')},ensure_ascii=False,indent=2)+'\n')
print('Prepared',len(manifest),'scientific visuals;',len(calculations),'new fixed-input previews.')
