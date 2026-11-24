"""Every frozen coupled scattering input and controls; independent cached R/T/A."""
import numpy as np
import slab
from io_contract import ROOT,case,check,checkpoint,save_fields,run


def execute(cfg,limits,output,cases):
    c=case('isotropic-scattering-slab');cases.append(c);checkpoint(output,cases)
    with np.load(ROOT/'references/reference-cache.npz',allow_pickle=False) as r:reference_parameters=r['parameters'];reference_fluxes=r['fluxes']
    summary=[];sequences={}
    for i,parameters in enumerate(cfg['slabs']):
        depth,omega=parameters['depth'],parameters['albedo']
        if not np.array_equal(reference_parameters[i],[depth,omega]):raise ValueError('Wrong independent reference input')
        expected=reference_fluxes[i];rows=[]
        for j,mesh in enumerate([*cfg['refinement'],cfg['angular_probe']]):
            name=f'slab{i}-n{mesh["cells"]}-s{mesh["ordinates"]}';out=slab.solve_slab(depth,omega,**mesh);save_fields(output,name,out)
            values=np.array([out[k] for k in ['R','T','A']]);error=float(np.max(abs(values-expected)))
            row=dict(id=name,parameter_index=i,depth=depth,albedo=omega,**mesh,fields=name+'.npz',fluxes=values.tolist(),reference=expected.tolist(),maximum_flux_error=error)
            c['records'].append(row);rows.append(row)
            check(c,name+'/finite-positive',float(out['intensity'].min()),-limits['negative_intensity'],np.isfinite(out['intensity']).all() and out['intensity'].min()>=-limits['negative_intensity'])
            for field,bound in [('residual',limits['residual']),('source_residual',limits['source_residual']),('balance',limits['budget'])]:check(c,name+'/'+field,float(out[field]),bound,out[field]<=bound)
            check(c,name+'/physical-fluxes',values.tolist(),[0.,1.],np.min(values)>=-1e-12 and np.max(values)<=1+1e-12)
            summary.append([i,depth,omega,mesh['cells'],mesh['ordinates'],*values,*expected,error]);checkpoint(output,cases)
        for previous,current in zip(rows[:2],rows[1:3]):check(c,f'slab{i}/refinement-n{current["cells"]}',current['maximum_flux_error']/max(previous['maximum_flux_error'],1e-300),limits['refinement_ratio'],current['maximum_flux_error']<=limits['refinement_ratio']*previous['maximum_flux_error'])
        check(c,f'slab{i}/finest-independent-error',rows[2]['maximum_flux_error'],limits['finest_flux_error'],rows[2]['maximum_flux_error']<=limits['finest_flux_error'])
        for key,one,two,bound in [('space-probe',rows[1],rows[2],limits['space_probe_difference']),('angle-probe',rows[2],rows[3],limits['angle_probe_difference'])]:
            difference=float(np.max(abs(np.array(one['fluxes'])-np.array(two['fluxes']))));check(c,f'slab{i}/'+key,difference,bound,difference<=bound)
        sequences[str(i)]=rows
    from scipy.special import expn
    for i,control in enumerate(cfg['controls']):
        name='control'+str(i);out=slab.solve_slab(**control);save_fields(output,name,out)
        check(c,name+'/budget',float(out['balance']),limits['budget'],out['balance']<=limits['budget'])
        if control['albedo']==0:
            error=float(abs(out['T']-2*expn(3,control['depth'])));check(c,name+'/pure-absorption',error,limits['pure_absorption_error'],out['R']==0 and error<=limits['pure_absorption_error'])
        else:check(c,name+'/conservative',float(out['A']),0.,out['A']==0 and out['R']>0 and out['T']>0)
        c['records'].append(dict(id=name,fields=name+'.npz',**control));checkpoint(output,cases)
    np.savetxt(output/'isotropic-scattering-slab.csv',np.array(summary),delimiter=',',header='slab,depth,albedo,cells,ordinates,R,T,A,reference_R,reference_T,reference_A,max_error',comments='',fmt='%.16e')
    c['metrics']=dict(completed_runs=len(c['records']),scattering_slabs=4,continuum_angle_reference=True,separate_space_angle_probes=True,stochastic_runs=0)
    c['passed']=bool(all(c['checks'].values()));checkpoint(output,cases)
if __name__=='__main__':run(execute)
