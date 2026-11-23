import json
import numpy as np
from references import exact
import transport as solver

IDS=['ale-nonuniform-transport','cgrid-rotating-wave']


def execute(cfg,out,limits,cases=None):
    if cases is None:cases=[]
    for ident in IDS:
        rows=[];checks={};files=[]
        def gate(name,value,bound):checks[name]=bool(value<=bound)
        if ident==IDS[0]:
            time_ref=exact.ale_time_reference(cfg['time_n'],cfg['time_t'])
            time_loose=exact.ale_time_reference(cfg['time_n'],cfg['time_t'],rtol=1e-10)
            reference_gap=float(np.max(abs(time_ref-time_loose)))
            gate('adaptive-time reference qualification',reference_gap,limits['ode_qualification'])
            runs=[('space',n,None,False,cfg['ale_t']) for n in cfg['ale_grids']]
            runs+=[('gcl',cfg['time_n'],None,True,.37)]
            runs+=[('time',cfg['time_n'],s,False,cfg['time_t']) for s in cfg['ale_time_steps']]
            for family,n,steps,constant,t in runs:
                tag=f'{family}-n{n}'+('' if steps is None else f'-s{steps}')
                try:a=solver.ale_solve(n,t,cfg['ale_cfl'],steps,constant)
                except solver.NumericalFailure as failure:
                    np.savez_compressed(out/(ident+'-'+tag+'-failed-candidate.npz'),**failure.state)
                    raise
                ref=np.array([np.diff(x) if constant else exact.mass(x,tt) for x,tt in zip(a['geometry'],a['times'])])
                xi=np.linspace(0,1,n+1);q=a['m']/np.diff(a['x'])
                error=float(np.sum(abs(a['m']-ref[-1])))
                row=dict(id=tag,family=family,n=n,steps=len(a['stages']),time=t,error=error,
                         minimum_volume=float(a['stages'][:,2].min()),minimum_value=float(a['stages'][:,3].min()),
                         maximum_cfl=float(a['stages'][:,4].max()),mass_defect=float(abs(a['m'].sum()-a['initial_mass'].sum())),
                         step_mass_defect=float(abs(a['stages'][:,5]).max()),gcl_defect=float(abs(a['stages'][:,6]).max()),
                         geometry_error=float(max(np.max(abs(x-exact.faces(xi,tt))) for x,tt in zip(a['geometry'],a['times']))))
                if family=='time':row['temporal_error']=float(np.sqrt(np.mean((np.r_[a['x'],a['m']]-time_ref)**2)))
                if constant:row['constant_error']=float(max(np.max(abs(m/np.diff(x)-1)) for m,x in zip(a['history'],a['geometry'])))
                name=ident+'-'+tag+'.npz';np.savez_compressed(out/name,**a,reference_history=ref,reference_mass=ref[-1],q=q)
                files.append(name);rows.append(row)
                for key,bound in [('mass_defect',limits['mass']),('step_mass_defect',limits['mass']),('gcl_defect',limits['gcl']),('maximum_cfl',.5+1e-14)]:gate(tag+' '+key,row[key],bound)
                checks[tag+' positive volumes and values']=bool(row['minimum_volume']>0 and row['minimum_value']>0)
                checks[tag+' five saved times']=bool(len(a['times'])==5 and a['times'][-1]==t)
                (out/'partial-progress.json').write_text(json.dumps(dict(current_case=ident,records=rows,checks=checks,data_files=files),indent=2)+'\n')
            seq=[r for r in rows if r['family']=='space'];tmp=[r for r in rows if r['family']=='time']
            for j in [1,2]:gate('space refinement '+str(j),seq[j]['error']/seq[j-1]['error'],limits['ale_refinement'])
            for j in [1,2]:gate('time refinement '+str(j),tmp[j]['temporal_error']/tmp[j-1]['temporal_error'],limits['ale_time_ratio'])
            gate('finest transport error',seq[-1]['error'],limits['ale_error'])
            gate('constant-state GCL preservation',next(r for r in rows if r['family']=='gcl')['constant_error'],limits['gcl_constant'])
            gate('finest time error',tmp[-1]['temporal_error'],limits['ale_time_error'])
        else:
            runs=[('space',n,4*n,cfg['wave_t']) for n in cfg['wave_grids']]
            runs+=[('time',cfg['wave_time_n'],s,cfg['time_t']) for s in cfg['wave_time_steps']]
            runs+=[('zero',8,64,.5),('balance',16,64,.5)]
            for family,n,steps,t in runs:
                tag=f'{family}-n{n}-s{steps}';coeff=np.array([.01,0,0],dtype=complex)
                if family=='zero':initial=np.broadcast_to(exact.zero_mode(0)[:,None,None],(3,n,n)).copy()
                elif family=='balance':
                    L=exact.symbol(n);kx=float(L[0,1].imag*-1);ky=float(L[0,2].imag*-1);c=float(L[1,2].real)
                    coeff=np.array([.01,-1j*ky*.01/c,1j*kx*.01/c]);initial=exact.field(n,coeff)
                else:initial=exact.field(n,coeff)
                try:a=solver.cgrid_solve(initial,t,steps)
                except solver.NumericalFailure as failure:
                    np.savez_compressed(out/(ident+'-'+tag+'-failed-candidate.npz'),**failure.state)
                    raise
                if family=='zero':
                    refs=np.array([np.broadcast_to(exact.zero_mode(tt)[:,None,None],(3,n,n)) for tt in a['times']]);continuous=refs
                else:
                    refs=np.array([exact.field(n,exact.amplitudes(n,tt,coeff)) for tt in a['times']])
                    continuous=np.array([exact.field(n,exact.amplitudes(n,tt,coeff,False)) for tt in a['times']])
                scale=np.sqrt(np.mean(initial**2));error=float(np.sqrt(np.mean((a['state']-refs[-1])**2))/scale)
                row=dict(id=tag,family=family,n=n,steps=steps,time=t,semidiscrete_error=error,
                    continuous_error=float(np.sqrt(np.mean((a['state']-continuous[-1])**2))/scale),
                    mean_height_change=float(abs(np.mean(a['state'][0])-np.mean(initial[0]))),
                    relative_energy_change=float(abs(np.mean(a['state']**2)/np.mean(initial**2)-1)),
                    energy_rhs_defect=float(a['stages'][:,3].max()),
                    steady_change=float(np.max(abs(a['history']-initial[None]))))
                name=ident+'-'+tag+'.npz';np.savez_compressed(out/name,**a,initial=initial,reference_history=refs,continuous_reference_history=continuous)
                files.append(name);rows.append(row)
                for key,bound in [('mean_height_change',limits['mass']),('relative_energy_change',limits['energy']),('energy_rhs_defect',limits['energy_rhs'])]:gate(tag+' '+key,row[key],bound)
                checks[tag+' finite actual 2D RK arrays']=bool(np.isfinite(a['history']).all() and a['history'].shape==(5,3,n,n))
                (out/'partial-progress.json').write_text(json.dumps(dict(current_case=ident,records=rows,checks=checks,data_files=files),indent=2)+'\n')
            seq=[r for r in rows if r['family']=='space'];tmp=[r for r in rows if r['family']=='time']
            for j in [1,2]:gate('continuous spatial refinement '+str(j),seq[j]['continuous_error']/seq[j-1]['continuous_error'],limits['wave_space_ratio'])
            for j in [1,2]:gate('semidiscrete temporal refinement '+str(j),tmp[j]['semidiscrete_error']/tmp[j-1]['semidiscrete_error'],limits['wave_time_ratio'])
            gate('finest continuous error',seq[-1]['continuous_error'],limits['wave_error'])
            gate('finest semidiscrete error',seq[-1]['semidiscrete_error'],limits['wave_discrete_error'])
            gate('zero-mode temporal accuracy',next(r for r in rows if r['family']=='zero')['semidiscrete_error'],limits['zero_error'])
            gate('discrete geostrophic stationarity',next(r for r in rows if r['family']=='balance')['steady_change'],limits['balance'])
        for name,passed in exact.qualification().items():checks['reference '+name]=passed
        cases.append(dict(id=ident,passed=all(checks.values()),checks=checks,records=rows,
                          metrics={k:v for k,v in rows[-1].items() if isinstance(v,(int,float))},data_files=files))
    return cases
