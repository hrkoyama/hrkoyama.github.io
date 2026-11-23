import time,json
import numpy as np
from scipy.sparse.linalg import spsolve
import operators as op
import multilevel as ml
from references import p1
IDS=['checkerboard-diffusion','rotated-anisotropic-diffusion']

def relative(x,y):return float(np.linalg.norm(x-y)/np.linalg.norm(y))

def execute(inp,out,limits,cases):
    refs={}
    for n in inp['reference_grids']:
        refs[n]=p1.solve(n);np.savez_compressed(out/f'checkerboard-reference-{n}.npz',field=refs[n])
    np.savez_compressed(out/'checkerboard-references.npz',**{str(n):u for n,u in refs.items()})
    for ident in IDS:
        scalar=ident==IDS[0]; checks={}; records=[];errors=[];reference_gaps=[]
        case=dict(id=ident,passed=False,checks=checks,metrics={'continuous_errors':errors,'reference_sensitivity':reference_gaps},records=records,termination='in_progress');cases.append(case)
        def checkpoint():
            (out/(ident+'-checkpoint.json')).write_text(json.dumps(case,indent=2,allow_nan=False)+'\n')
        for n in inp['grids']:
            if scalar:A,b,(X,Y,a),faces,boundary=op.scalar_fv(n)
            else:A,b,points,el,interior,g=op.q1(n)
            data={'A_data':A.data,'A_indices':A.indices,'A_indptr':A.indptr,'b':b};np.savez_compressed(out/f'{ident}-n{n}-candidate.npz',**data)
            direct=spsolve(A,b);data['direct']=direct;np.savez_compressed(out/f'{ident}-n{n}-candidate.npz',**data)
            if scalar:
                data.update(x=X,y=Y,coefficient=a)
                ref=[p1.evaluate(u,X,Y) for u in refs.values()];err=relative(direct,ref[-1]);gap=relative(ref[0],ref[-1]);reference_gaps.append(gap);data.update(reference=ref[-1],reference_coarse=ref[0])
            else:
                full=g.copy();full[interior]=direct;err,energy=op.q1_error(n,full);err6,_=op.q1_error(n,full,6);data.update(points=points,field=full,tensor=op.tensor())
                checks[f'n{n}_quadrature']=bool(abs(err6-err)<=limits['quadrature_fraction']*err)
            errors.append(err)
            checks[f'n{n}_symmetry']=bool(np.linalg.norm((A-A.T).data)<=limits['symmetry']*np.linalg.norm(A.data))
            for kind in ['geometric','amg']:
                start=time.monotonic();L=ml.hierarchy(A,kind,n,scalar);setup=time.monotonic()-start
                start=time.monotonic();u,info=ml.pcg(A,b,L,inp['tolerance'],inp['iteration_budget']);solve=time.monotonic()-start
                data[kind]=u;data[kind+'_history']=info['history'];np.savez_compressed(out/f'{ident}-n{n}-candidate.npz',**data)
                residual=b-A@u;true=float(np.linalg.norm(residual)/np.linalg.norm(b));forward=relative(u,direct);d=u-direct;energy_error=float(np.sqrt(np.sum(d*(A@d))/np.sum(direct*(A@direct))))
                prefix=f'n{n}_{kind}';checks[prefix+'_converged']=info['converged'];checks[prefix+'_true_residual']=true<=limits['residual'];checks[prefix+'_forward']=forward<=limits['forward'];checks[prefix+'_energy']=energy_error<=limits['energy'];checks[prefix+'_history']=abs(true-info['history'][-1])<=limits['history']
                row=dict(n=n,solver=kind,iterations=info['iterations'],true_residual=true,forward_error=forward,energy_error=energy_error,continuous_error=err,setup_seconds=setup,solve_seconds=solve,**ml.levels(L));records.append(row)
                data[kind]=u;data[kind+'_history']=info['history']
                if scalar:
                    flux=np.concatenate([t*(u[i]-u[j]) for i,j,t in faces]);boundary_flux=float(sum(np.sum(t*(u[i]-g0)) for i,t,g0 in boundary));defect=float(b.sum()-boundary_flux)
                    checks[prefix+'_flux_ledger']=bool(abs(defect-residual.sum())<=limits['ledger_roundoff']);checks[prefix+'_budget_residual_bound']=bool(abs(defect)<=np.sqrt(len(b))*np.linalg.norm(residual)+limits['ledger_roundoff']);data[kind+'_face_flux']=flux;row.update(boundary_flux=boundary_flux,source=float(b.sum()),budget_defect=defect,residual_sum=float(residual.sum()))
                checkpoint()
            np.savez_compressed(out/f'{ident}-n{n}.npz',**data)
        checks['refinement']=bool(errors[-1]<errors[0])
        if scalar:
            checks['reference_sensitivity']=bool(reference_gaps[-1]<=limits['reference_fraction']*errors[-1])
            A,b,(X,Y,a),faces,boundary=op.scalar_fv(16,True);u=spsolve(A,b);exact=np.where(X<.5,X,X*.01+.495)/.505
            q=[t*(u[i]-u[j]) for i,j,t in faces][1]*16
            checks['nonzero_harmonic_patch']=bool(relative(u,exact)<=limits['patch'] and np.max(abs(q+1/.505))<=limits['patch'])
        else:
            checks['l2_refinement_ratios']=bool(all(b/a<=limits['smooth_ratio'] for a,b in zip(errors,errors[1:])));checks['finest_l2']=bool(errors[-1]<=limits['finest_l2'])
            for mode in ['affine','xy']:
                A,b,points,el,interior,g=op.q1(8,mode);u=spsolve(A,b);checks[mode+'_patch']=bool(relative(u,g[interior])<=limits['patch'])
        # Small explicit implementation check supplements the construction's SPD argument.
        A=op.scalar_fv(4)[0] if scalar else op.q1(4)[0]
        checks['small_operator_spd']=bool(np.linalg.eigvalsh(A.toarray())[0]>0)
        for kind in ['geometric','amg']:
            L=ml.hierarchy(A,kind,4,scalar);B=np.column_stack([ml.cycle(L,e) for e in np.eye(A.shape[0])]);checks[kind+'_small_cycle_spd']=bool(np.linalg.norm(B-B.T)<=limits['cycle_symmetry']*np.linalg.norm(B) and np.linalg.eigvalsh((B+B.T)/2)[0]>0)
            _,info=ml.pcg(A,np.arange(1,A.shape[0]+1,dtype=float),L,1e-14,1)
            # Terminal direct solve may converge; use nonterminal grid below for budget fixture.
        A,b=op.scalar_fv(16)[:2];L=ml.hierarchy(A,'geometric',16,True);_,info=ml.pcg(A,b,L,1e-14,1);checks['intentional_budget']=bool(not info['converged'] and info['termination']=='iteration_budget' and info['iterations']==1)
        case.update(passed=bool(all(checks.values())),checks={k:bool(v) for k,v in checks.items()},termination='fixed_budget_completed');checkpoint()
