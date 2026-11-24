"""Long actual Yee/Lorentz/trapezoidal-PML trajectories; no spectral primary."""
import numpy as np
import centered_pml as core
import modal_yee_draft as material_core


def energy_and_work(state,new,diagnostic,g):
    # Reuse one look-ahead only for diagnostics. It never updates primary state.
    E,Hx,Hy,P,J=new[:5];xp,yp,next_h=core.magnetic(new,g)
    node=.5*g['epsilon_node']*abs(E)**2+material_core.oscillator_energy(P,J,g['strength_node'],g['omega0'])+.5*np.real(Hx*np.conj(xp))
    modified=float(core.integral(node,.5*np.real(Hy*np.conj(yp)),g))
    physical=float(core.integral(diagnostic['ohmic']+diagnostic['material_loss'],np.zeros_like(g['xf']),g))
    eb=.5*(state[0]+new[0])
    pml=float(g['dt']*np.real(core.integral(np.conj(eb)*diagnostic['psi_e'],.5*np.conj(Hy)*(diagnostic['psi_h']+next_h),g)))
    positive=float(core.integral(.5*g['epsilon_node']*abs(E)**2+material_core.oscillator_energy(P,J,g['strength_node'],g['omega0'])+.5*abs(Hx)**2,.5*abs(Hy)**2,g))
    memory=float(np.sqrt(core.integral(abs(new[6])**2,abs(new[5])**2,g)))
    return modified,physical,pml,positive,memory


def solve(spec,control,reference,output,name):
    peak=control.get('pml_peak',spec['pml_peak'])
    g=core.build(control['cells'],spec['length'],control['dy'],control['ky'],spec['courant'],control['material'],spec['pml_thickness'],peak,spec['pml_order'],spec['final_time'])
    if g['steps']!=control['steps'] or abs(g['dt']-control['dt'])>1e-15:raise ValueError('Reference and primary integer schedules differ')
    state=core.initialize(reference,g)
    np.savez_compressed(output/(name+'-initial-state.npz'),**{'state'+str(i):z for i,z in enumerate(state)})
    initial=core.modified_energy(state,g);work=0.;pml=0.;history=[];snapshots={};times=[];max_budget=0.;min_physical=0.;maximum_positive=initial;maximum_memory=0.;completed=0
    scheduled={i*g['steps']//4 for i in range(5)}
    def retain(step):
        np.savez_compressed(output/(name+'-current-state.npz'),step=np.array(step),time=np.array(step*g['dt']),history=np.array(history),**{'state'+str(i):z for i,z in enumerate(state)})
    def snapshot(step):
        times.append(step*g['dt'])
        for key,z in zip(['E','Hx','Hy','P','J','psi_H','psi_E'],state):snapshots.setdefault(key,[]).append(z.copy())
        retain(step)
    snapshot(0)
    try:
        for step in range(1,g['steps']+1):
            previous=state;state,diagnostic=core.advance(state,g);completed=step
            energy,physical,signed_pml,positive,memory=energy_and_work(previous,state,diagnostic,g)
            work+=physical;pml+=signed_pml;min_physical=min(min_physical,physical)
            defect=abs(energy-initial+work-pml)/initial;max_budget=max(max_budget,defect);maximum_positive=max(maximum_positive,positive);maximum_memory=max(maximum_memory,memory)
            history.append([step*g['dt'],energy,positive,work,pml,defect,memory])
            if not np.isfinite(history[-1]).all():raise FloatingPointError('Nonfinite long PML trajectory')
            if step in scheduled:snapshot(step)
    except BaseException:
        retain(completed);raise
    result=dict(x=g['x'],xf=g['xf'],times=np.array(times),history=np.array(history),dt=np.array(g['dt']),steps=np.array(g['steps']),h=np.array(g['h']),dy=np.array(control['dy']),ky=np.array(control['ky']),initial_energy=np.array(initial),maximum_budget=np.array(max_budget),minimum_physical_work=np.array(min_physical),maximum_positive_energy=np.array(maximum_positive),maximum_memory_norm=np.array(maximum_memory),reference_box_length=reference['box_length'],
                **{key:np.array(value) for key,value in snapshots.items()},**{'reference_'+key:reference[key] for key in ['E','Hx','Hy','P','J']})
    # Retain every actual native field and ledger BEFORE reference diagnostics.
    result.update(pml_peak=np.array(peak),pml_rate_node=g['rate_node'],pml_rate_face=g['rate_face'])
    np.savez_compressed(output/(name+'.npz'),**result)
    np.savetxt(output/(name+'-history.csv'),result['history'],delimiter=',',header='time,modified_energy,positive_energy,physical_material_work,signed_PML_work,budget_defect,memory_norm',comments='',fmt='%.16e')
    return result,g
