"""DRAFT 97: eight NumPy full eigensolves, 824 native/24 selected eigenpairs."""
import math
from decimal import Decimal, localcontext
import numpy as np
from io_utils import eigh_owned, mm, mv, dot, norm


def decimal_pi(precision=90):
    # Machin formula, fixed alternating Taylor remainder < next term.
    with localcontext() as ctx:
        ctx.prec=precision+15
        def atan_inverse(n):
            x=Decimal(1)/n;term=x;total=term;k=1
            while True:
                term*=-x*x;part=term/(2*k+1);total+=part;k+=1
                if abs(part)<Decimal(10)**(-precision-5):break
            return total
        return +(16*atan_inverse(5)-4*atan_inverse(239))


def box_oracle(M,j):
    with localcontext() as ctx:
        ctx.prec=90
        z=Decimal(j)*decimal_pi()/(2*M);term=z;s=term
        for k in range(1,100):
            term*=-z*z/((2*k)*(2*k+1));s+=term
        return float(2*s*s*M*M)


def ho_samples(x,n):
    g=np.exp(-x*x/2)/math.pi**.25
    return [g,math.sqrt(2)*x*g,(2*x*x-1)/math.sqrt(2)*g][n]


def node_diagnostic(u,x,model,state):
    tau=128*np.finfo(float).eps*float(np.max(abs(u)))
    window=np.ones(len(x),dtype=bool) if model=='box' else abs(x)<=3
    retained=u[window & (abs(u)>tau)]
    return {'tau_draft_diagnostic':tau,'count':int(np.count_nonzero(retained[1:]*retained[:-1]<0)),
            'mask':(window & (abs(u)>tau)).tolist(),'expected':state-1 if model=='box' else state,
            'mandatory_gate':False,'reason':'Forward pointwise eigenvector uncertainty is not certified by a scaled residual.'}


def run(c,save):
    matrix=[]
    for M in c['box_M']:matrix.append(('box-M'+str(M),'box',0.,1.,M))
    for h in c['HO_L8_h']:matrix.append(('HO-L8-h'+str(h),'HO',-8.,8.,round(16/h)))
    for L in c['HO_domain_L']:
        if L!=8:matrix.append(('HO-L'+str(L)+'-h0.125','HO',-float(L),float(L),round(2*L/c['HO_domain_h'])))
    rows=[]
    for ident,model,a,b,M in matrix:
        h=(b-a)/M;x=a+h*np.arange(1,M);v=np.zeros_like(x) if model=='box' else x*x/2
        H=np.diag(1/h**2+v)+np.diag(np.full(M-2,-.5/h**2),1)+np.diag(np.full(M-2,-.5/h**2),-1)
        values,native=eigh_owned(H,'97-'+ident,save)
        # The native norm is tested before any representation conversion.
        native_norm_error=float(np.max(abs(np.sum(native[:,:3]**2,axis=0)-1)))
        u=native[:,:3].copy()/math.sqrt(h);pairs=[]
        for k in range(3):
            state=k+1 if model=='box' else k
            q=math.sqrt(2)*np.sin(state*math.pi*x) if model=='box' else ho_samples(x,state)
            exact=(state*math.pi)**2/2 if model=='box' else state+.5
            residual=float(norm(mv(H,u[:,k])-values[k]*u[:,k])*math.sqrt(h)/(norm(H,np.inf)+abs(values[k])))
            overlap=float(h*dot(u[:,k],q));phase=1 if overlap>=0 else -1
            phase_resolved=abs(overlap)>64*np.finfo(float).eps*math.sqrt(h*dot(q,q))
            field=min(float(norm(u[:,k]-q)*math.sqrt(h)),float(norm(u[:,k]+q)*math.sqrt(h)))
            pair={'state':state,'energy':float(values[k]),'continuum_energy':exact,'signed_energy_error':float(values[k]-exact),
                  'scaled_residual':residual,'field_error_raw_analytic':field,'raw_analytic_h_norm':float(math.sqrt(h*dot(q,q))),
                  'analytic_raw':q,'u':u[:,k]*phase,'phase_resolved':phase_resolved,'native_phase_overlap':overlap,
                  'nodes_diagnostic':node_diagnostic(u[:,k],x,model,state)}
            if model=='box':
                oracle=box_oracle(M,state);pair['same_grid_oracle']=oracle;pair['same_grid_relative_error']=abs(float(values[k])-oracle)/oracle
            else:pair['parity_residual']=float(norm(u[::-1,k]-(-1)**state*u[:,k])*math.sqrt(h))
            pairs.append(pair)
        rows.append({'id':ident,'model':model,'domain':[a,b],'M':M,'h':h,'x':x,'pairs':pairs,
                     'native_norm_error':native_norm_error,'physical_norm_error':float(np.max(abs(h*np.sum(u*u,axis=0)-1))),
                     'orthogonality_error':float(np.max(abs(mm(h*u.T,u)-np.eye(3))))})
    return {'rows':rows,'primary_API_calls':8,'native_eigenpairs':824,'selected_eigenpairs':24,
            'HO_wall_mesh_separation':'Signed fixed-L mesh and fixed-h domain differences are sensitivities, not separate certified wall and mesh errors.'}
