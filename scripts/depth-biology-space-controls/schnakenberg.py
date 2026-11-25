"""Cell-average2D reaction--diffusion with nonperiodic boundary and modal reference."""
from __future__ import annotations
from common import matmul,dot,array_norm
import math
import numpy as np
from common import adaptive,maxerr,order
L=2*math.pi
IC_IDS=['N-mode42','N-mixed','D-mode42']
SNAPS=[0.,.5,1.,2.]


def cell_mode(N,m,bc):
    x=(np.arange(N)+.5)*L/N
    wave=np.cos(m*math.pi*x/L) if bc=='N' else np.sin(m*math.pi*x/L)
    return wave*np.sinc(m/(2*N))


def initial(N,ic):
    bc=ic[0]
    z=np.outer(cell_mode(N,4,bc),cell_mode(N,2,bc))
    if ic=='N-mixed':z=np.outer(cell_mode(N,2,bc),cell_mode(N,4,bc))+.5*np.outer(cell_mode(N,3,bc),cell_mode(N,1,bc))
    return np.array([1+.02*z,.9-.006*z])


def eigbasis(N,bc):
    i=np.arange(N)+.5
    modes=np.arange(N) if bc=='N' else np.arange(1,N+1)
    E=np.cos(math.pi*np.outer(i,modes)/N) if bc=='N' else np.sin(math.pi*np.outer(i,modes)/N)
    E*=math.sqrt(2/N)
    if bc=='N':E[:,0]/=math.sqrt(2)
    else:E[:,-1]/=math.sqrt(2)
    lam=4*np.sin(modes*math.pi/(2*N))**2/(L/N)**2
    return E,lam[:,None]+lam[None,:]


def lapfaces(u,h,bc):
    # One owned internal face; external ghost-cell deviation is +/-firstcell.
    fx=np.zeros((u.shape[0]+1,u.shape[1]));fy=np.zeros((u.shape[0],u.shape[1]+1))
    fx[1:-1]=(u[1:]-u[:-1])/h;fy[:,1:-1]=(u[:,1:]-u[:,:-1])/h
    if bc=='D':
        fx[0]=2*u[0]/h;fx[-1]=-2*u[-1]/h
        fy[:,0]=2*u[:,0]/h;fy[:,-1]=-2*u[:,-1]/h
    return (fx[1:]-fx[:-1]+fy[:,1:]-fy[:,:-1])/h


def reaction(y):
    u,v=y;uv=u*u*v
    return np.array([.1-u+uv,.9-uv])


def reaction_midpoint(y,dt,budget):
    z=y.copy()
    for j in range(12):
        budget.augment(stage='reactionNewton',reaction_input=y,reaction_candidate=z,Newton_iteration=j)
        budget.tick('schnak_newton_iteration')
        mid=(y+z)/2;u,v=mid;r=z-y-dt*reaction(mid)
        budget.augment(reaction_midpoint=mid,reaction_residual=r)
        norm=float(np.max(np.abs(r)))
        if norm<=1e-13:return z,dt*reaction(mid),norm
        a=1-dt*(-1+2*u*v)/2;b=-dt*u*u/2
        c=dt*u*v;d=1+dt*u*u/2;det=a*d-b*c
        if not np.all(np.isfinite(det)) or np.min(np.abs(det))<1e-12:raise FloatingPointError('Singular reaction Newton system')
        du=(d*r[0]-b*r[1])/det;dv=(-c*r[0]+a*r[1])/det
        z-=np.array([du,dv])
        budget.augment(reaction_candidate=z)
        if not np.all(np.isfinite(z)):raise FloatingPointError('Nonfinite reaction Newton candidate')
    raise RuntimeError('Fixed reaction Newton cap exhausted')


def diffusion(y,duration,E,lam,bc,budget):
    out=np.empty_like(y);ledger=[]
    for k,D in enumerate([.01,1.]):
        base=[1.,.9][k];a=y[k]-base
        fac=(1-duration*D*lam/2)/(1+duration*D*lam/2)
        budget.augment(stage='CNdiffusion-input',diffusion_input=y,diffusion_field=k,diffusion_deviation=a,diffusion_factor=fac)
        b=matmul(matmul(E,(matmul(matmul(E.T,a),E))*fac),E.T);out[k]=base+b
        budget.augment(stage='CNdiffusion',diffusion_input=y,diffusion_field=k,diffusion_candidate=out[k])
        if not np.all(np.isfinite(out[k])):raise FloatingPointError('Nonfinite CN candidate')
        if bc=='N':ledger.append(0.)
        else:
            z=(a+b)/2
            ledger.append(-2*D*duration*(np.sum(z[0])+np.sum(z[-1])+np.sum(z[:,0])+np.sum(z[:,-1])))
        budget.tick('schnak_CN_field')
    return out,np.array(ledger)


def primary(N,ic,dt,budget):
    bc=ic[0];steps=int(round(2/dt));E,lam=eigbasis(N,bc);y=initial(N,ic)
    saved=[y.copy()];history=[[0.,float(y[0].mean()),float(y[1].mean())]]
    total_flux=np.zeros(2);total_source=np.zeros(2);mass0=y.sum(axis=(1,2))*(L/N)**2
    max_residual=0.;minimum=float(y.min())
    snapkeys={int(round(t/dt)) for t in SNAPS[1:]}
    for j in range(steps):
        budget.tick('schnak_primary_step');budget.own(case='Schnakenberg',ic=ic,N=N,step=j,state=y)
        y,flux1=diffusion(y,dt/2,E,lam,bc,budget)
        y,source,res=reaction_midpoint(y,dt,budget)
        y,flux2=diffusion(y,dt/2,E,lam,bc,budget)
        total_flux+=flux1+flux2;total_source+=source.sum(axis=(1,2))*(L/N)**2
        max_residual=max(max_residual,res);minimum=min(minimum,float(y.min()))
        if not np.all(np.isfinite(y)):raise FloatingPointError('Nonfinite Schnakenberg state')
        if j+1 in snapkeys:saved.append(y.copy())
        if (j+1)%max(1,steps//100)==0:history.append([(j+1)*dt,float(y[0].mean()),float(y[1].mean())])
    residual=y.sum(axis=(1,2))*(L/N)**2-mass0-total_flux-total_source
    return np.stack(saved),{'steps':steps,'dt':dt,'minimum':minimum,'max_Newton_residual':max_residual,
        'mass_balance_residual':residual,'mass_scale':1+np.abs(mass0)+np.abs(total_flux)+np.abs(total_source),
        'integrated_boundary_flux':total_flux,'integrated_reaction':total_source},np.array(history)


def matrix_exp(A):
    # Independent scaling/Taylor/squaring, fixed term cap128; dimension2 here.
    norm=float(np.max(np.sum(np.abs(A),axis=1)));s=max(0,int(math.ceil(math.log2(norm/.25)))) if norm>.25 else 0
    B=A/(2**s);term=np.eye(len(A));ans=term.copy()
    for k in range(1,129):
        term=matmul(term,B)/k;ans+=term
        if np.max(np.abs(term))<1e-18:break
    else:raise RuntimeError('Matrix series cap')
    for _ in range(s):ans=matmul(ans,ans)
    return ans


def exp2closed(A,t):
    tau=np.trace(A)/2;B=A-tau*np.eye(2);delta=float((matmul(B,B))[0,0])
    if abs(delta)<1e-24:return math.exp(tau*t)*(np.eye(2)+t*B)
    if delta>0:
        d=math.sqrt(delta);return math.exp(tau*t)*(math.cosh(d*t)*np.eye(2)+math.sinh(d*t)/d*B)
    d=math.sqrt(-delta);return math.exp(tau*t)*(math.cos(d*t)*np.eye(2)+math.sin(d*t)/d*B)


def basis(x,modes,bc):
    modes=np.asarray(modes)
    p=np.cos(math.pi*np.outer(x,modes)/L) if bc=='N' else np.sin(math.pi*np.outer(x,modes)/L)
    p*=math.sqrt(2/L)
    if bc=='N':p[:,0]=1/math.sqrt(L)
    return p


def modal_reference(ic,K,Q,rtol,atol,budget):
    bc=ic[0];modes=np.arange(K) if bc=='N' else np.arange(1,K+1)
    z,w=np.polynomial.legendre.leggauss(Q);x=(z+1)*L/2;w=w*L/2
    E=basis(x,modes,bc);W=E.T*w
    gram=maxerr(matmul(W,E),np.eye(K))
    if gram>1e-11:raise RuntimeError('Modal quadrature Gram qualification failed')
    eigen=(modes[:,None]**2+modes[None,:]**2)*(math.pi/L)**2
    y0=np.zeros((2,K,K));pairs=[(4,2,1.)] if ic!='N-mixed' else [(2,4,1.),(3,1,.5)]
    for m,n,amp in pairs:
        ii=int(np.where(modes==m)[0][0]);jj=int(np.where(modes==n)[0][0]);y0[:,ii,jj]=np.array([.02,-.006])*amp*L/2
    def rhs(t,z):
        a=z.reshape(2,K,K)
        # Authored Galerkin reaction; no primaryFV/reaction helper imports.
        u=1+matmul(matmul(E,a[0]),E.T);v=.9+matmul(matmul(E,a[1]),E.T)
        ru=.1-u+(u*u)*v;rv=.9-(u*u)*v
        return np.array([-.01*eigen*a[0]+matmul(matmul(W,ru),W.T),-eigen*a[1]+matmul(matmul(W,rv),W.T)]).reshape(-1)
    budget.own(case='Schnakenberg-Galerkin-reference',ic=ic,K=K,Q=Q,rtol=rtol,atol=atol)
    ys,ll=adaptive(rhs,y0.reshape(-1),SNAPS,budget,rtol,atol,4000,first_step=1e-3)
    projected={}
    for N in [12,24,48]:
        xc=(np.arange(N)+.5)*L/N
        B=basis(xc,modes,bc)*np.sinc(modes/(2*N))[None,:]
        arr=[]
        for state in ys.reshape(-1,2,K,K):arr.append(np.array([1+matmul(matmul(B,state[0]),B.T),.9+matmul(matmul(B,state[1]),B.T)]))
        projected[N]=np.stack(arr)
    return projected,{'K':K,'Q':Q,'Gram_error':gram,**ll},ys.reshape(-1,2,K,K)


def components(budget):
    checks={};records=[]
    J=np.array([[.8,1.],[-1.8,-1.]])
    count=0
    for bc in ['N','D']:
        for m,n in [(1,1),(4,2),(3,1)]:
            for N in [12,24,48]:
                h=L/N;wave=np.outer(cell_mode(N,m,bc),cell_mode(N,n,bc))
                lam=4/h**2*(math.sin(m*math.pi/(2*N))**2+math.sin(n*math.pi/(2*N))**2)
                residual=maxerr(lapfaces(wave,h,bc),-lam*wave)
                checks['mode/%s/%s/%s/%s'%(bc,m,n,N)]=residual<1e-11
                for t in [.1,.5,1.]:
                    cont=(m*m+n*n)*(math.pi/L)**2
                    A=J-np.diag([.01*lam,lam]);C=J-np.diag([.01*cont,cont])
                    error=max(maxerr(exp2closed(A,t),matrix_exp(A*t)),maxerr(exp2closed(C,t),matrix_exp(C*t)))
                    checks['exp/%s/%s/%s/%s/%s'%(bc,m,n,N,t)]=error<2e-11
                    records.append({'bc':bc,'mode':[m,n],'N':N,'time':t,'symbol_error':residual,'exponential_error':error});count+=1
    zero=np.zeros((12,12));checks['equilibrium-face-zero']=maxerr(lapfaces(zero,L/12,'D'),zero)==0
    for bc in ['N','D']:
        E,lam=eigbasis(12,bc);eq=np.array([np.ones((12,12)),np.full((12,12),.9)])
        y,_=diffusion(eq,1/1600,E,lam,bc,budget);y,_,_=reaction_midpoint(y,1/800,budget);y,_=diffusion(y,1/1600,E,lam,bc,budget)
        checks['constant-equilibrium/'+bc]=maxerr(y,eq)<=5e-13
    probe=initial(12,'D-mode42')[0]-1
    checks['wrong-boundary-control']=maxerr(lapfaces(probe,L/12,'N'),lapfaces(probe,L/12,'D'))>1e-4
    # A corner owns two distinct normalfaces; duplicating one has a measurable error.
    wrong=lapfaces(probe,L/12,'D').copy();wrong[0,0]-=2*probe[0,0]/(L/12)**2
    checks['corner-doublecount-control']=maxerr(wrong,lapfaces(probe,L/12,'D'))>1e-5
    checks['linear-action-count']=count==54
    return checks,records



def reference_assessment(references,primary):
    """The unchanged4-row K/Q/tolerance criteria, always against THIS finestreference."""
    deltas=[max(maxerr(references[a][N],references[b][N]) for N in [12,24,48]) for a,b in [(0,1),(1,2),(2,3)]]
    errors=[maxerr(primary[N],references[-1][N]) for N in [12,24,48]]
    denominator=errors[-1];total=sum(deltas)
    qualified=(max(deltas)<=2e-4 and total<=2e-4 and denominator>1e-12 and total<=.1*denominator)
    return deltas,errors,total,qualified

def run(rec,budget,inputs):
    extension_rows=inputs['Schnakenberg_D_reference_extension_rows']
    if len(extension_rows)!=4:raise ValueError('ExactlyfourreviewedD-onlyextensionrowsrequired;nofallback')
    checks,records=components(budget)
    for k,v in checks.items():rec.check('Schnakenberg/'+k,v)
    rec.row('schnakenberg-components',{'linear_actions':records,'matrix_actions_total':216})
    for ic in IC_IDS:
        prim={};err=[]
        for N in [12,24,48]:
            ys,diag,history=primary(N,ic,1/800,budget);prim[N]=ys
            rec.row('schnak-'+ic+'-N'+str(N),{'ic':ic,'N':N,**diag},time=np.array(SNAPS),state=ys,mean_history=history)
            rec.check('Schnakenberg/ledger/'+ic+'/'+str(N),np.max(np.abs(diag['mass_balance_residual'])/diag['mass_scale'])<=5e-11)
            rec.goal('Schnakenberg/positivity/'+ic+'/'+str(N),diag['minimum']>=-1e-12,minimum=diag['minimum'])
        references=[]
        for row in inputs['Schnakenberg_reference_rows']:
            proj,ll,modal=modal_reference(ic,row['K'],row['Q'],row['rtol'],row['atol'],budget)
            references.append(proj)
            rec.row('schnak-ref-'+ic+'-K%s-Q%s-t%s'%(row['K'],row['Q'],row['rtol']),ll,
                    time=np.array(SNAPS),modal=modal,cell_N48=proj[48])
        deltas,errors,sumdelta,qualified=reference_assessment(references,prim)
        reference_role='original4-rowreference'
        if ic=='D-mode42':
            # Retain original4rows and their actual unqualified outcome explicitly.
            rec.row('schnak-legacy-reference-summary-D-mode42',{
                'role':'legacy-reference-qualification','reference_rows':4,'reference_deltas':deltas,
                'reference_sum':sumdelta,'reference_qualified_in_this_run':qualified,
                'grid_errors':errors,'finest_denominator':errors[-1],
                'original_R4_first_qualification':'FAIL, preserved in source-reading.json#/prior_reference_qualification',
                'used_for_current_accuracy_goals':False,'relabelled_as_original_protocol_pass':False},
                time=np.array(SNAPS),legacy_cell_reference=references[-1][48],primary=prim[48])
            finer=[]
            for row in extension_rows:
                proj,ll,modal=modal_reference(ic,row['K'],row['Q'],row['rtol'],row['atol'],budget)
                finer.append(proj)
                rec.row('schnak-ref-extension-'+ic+'-K%s-Q%s-t%s'%(row['K'],row['Q'],row['rtol']),
                        {**ll,'role':'controlledD-onlyfinerreferenceextension'},
                        time=np.array(SNAPS),modal=modal,cell_N48=proj[48])
            # No fallback: failure/cap staysfailed; an unqualified newreference makesgoalsNULL.
            references=finer
            deltas,errors,sumdelta,qualified=reference_assessment(references,prim)
            reference_role='controlledD-onlyK24/32extension;newfineK32Q192tight'
        denom=errors[-1]
        rec.check('Schnakenberg/reference/'+ic,qualified)
        oo=order(errors[-2],errors[-1],max(20*sumdelta,1e-12))
        rec.goal('Schnakenberg/space-finest/'+ic,errors[-1]<=.02 if qualified else None,actual=errors[-1],target=.02)
        rec.goal('Schnakenberg/space-order/'+ic,oo>=1.6 if oo is not None and qualified else None,actual=oo,target=1.6)
        rec.row('schnak-summary-'+ic,{'reference_deltas':deltas,'reference_sum':sumdelta,'reference_qualified':qualified,
                'finest_denominator':denom,'zero_floor':1e-12,'grid_errors':errors,'spatial_order':oo,
                'reference_role':reference_role,'reference_scope':'Finite modal/quadrature/tolerance sensitivity indicators, not rigorous continuum bounds'},
                time=np.array(SNAPS),state=prim[48],reference=references[-1][48],error=prim[48]-references[-1][48])
        if ic=='N-mixed':
            tt=[];time_states=[]
            for dt in [1/200,1/400]:
                yy,ll,history=primary(48,ic,dt,budget);tt.append(maxerr(yy,references[-1][48]));time_states.append(yy)
                rec.row('schnak-time-'+str(round(1/dt)),ll,time=np.array(SNAPS),state=yy,mean_history=history)
            # Pairwise same-grid differences isolate time sensitivity without claiming a bound.
            time_states.append(prim[48]);d01=maxerr(time_states[0],time_states[1]);d12=maxerr(time_states[1],time_states[2])
            observed_time_order=order(d01,d12,max(20*sumdelta,1e-12))
            finest_time_indicator=d12/3
            rec.goal('Schnakenberg/time-order',observed_time_order>=1.7 if observed_time_order is not None else None,
                     actual=observed_time_order,target=1.7)
            rec.goal('Schnakenberg/time-contamination',finest_time_indicator<=.1*errors[-1] if qualified else None,
                     actual=finest_time_indicator,finest_spatial_discrepancy=errors[-1],scope='Secondorder Richardson indicator,notcertifiederrorbound')
            rec.row('schnak-time-summary',{'errors_to_continuum_reference':tt+[errors[-1]],
                    'same_grid_pair_differences':[d01,d12],'observed_order':observed_time_order,
                    'finest_time_indicator':finest_time_indicator})
