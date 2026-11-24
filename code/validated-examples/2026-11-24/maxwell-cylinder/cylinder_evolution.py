"""Actual two-dimensional complex Yee scattered-field evolution and native DFT."""
import numpy as np
import cylinder_draft as core


def solve(spec,ppw,amplitude,epsilon,output,name):
    n=int(round(spec['length']*ppw));h=spec['length']/n;period=2*np.pi/spec['omega']
    per_period=int(np.ceil(period/(spec['courant']*h/np.sqrt(2))))
    dt=period/per_period;burn=spec['burn_periods']*per_period;window=spec['sample_periods']*per_period;steps=burn+window
    g=core.build_grid(n,spec['length'],dt,spec['radius'],epsilon,spec['pml_thickness'],spec['pml_peak'],spec['pml_order'])
    state=core.zero_state(g);sums=[np.zeros_like(z) for z in [state[0],state[2],state[3]]]
    first=[np.zeros_like(z) for z in sums];second=[np.zeros_like(z) for z in sums]
    sample_steps=[0,burn//2,burn,burn+window//2,steps];snapshots={k:[] for k in ['E','Hx','Hy']};times=[];history=[];completed_step=0
    def record(step):
        times.append(step*dt)
        for key,z in zip(snapshots,[state[0]+state[1],state[2],state[3]]):snapshots[key].append(z.copy())
        np.savez_compressed(output/(name+'-current-state.npz'),step=np.array(step),time=np.array(step*dt),**{f'state{i}':z for i,z in enumerate(state)},history=np.array(history))
    record(0)
    try:
        for step in range(1,steps+1):
            state=core.advance(state,g,(step-1)*dt,spec['omega'],amplitude)
            completed_step=step
            if step>burn:
                E=state[0]+state[1];factors=[np.exp(1j*spec['omega']*step*dt),np.exp(1j*spec['omega']*(step-.5)*dt)]
                for k,(field,phase) in enumerate(zip([E,state[2],state[3]],[factors[0],factors[1],factors[1]])):
                    value=field*phase;sums[k]+=value
                    (first if step<=burn+window//2 else second)[k]+=value
            if step in sample_steps[1:]:record(step)
            if step%per_period==0:
                peak=max(float(np.max(abs(z))) for z in state)
                history.append([step*dt,peak])
                if not np.isfinite(peak):raise FloatingPointError('Nonfinite cylinder field')
    except BaseException:
        np.savez_compressed(output/(name+'-failed-state.npz'),step=np.array(completed_step),time=np.array(completed_step*dt),**{f'state{i}':z for i,z in enumerate(state)},history=np.array(history));raise
    fields=dict(x=g['x'],xh=g['xh'],epsilon=g['epsilon'],times=np.array(times),history=np.array(history),dt=np.array(dt),steps=np.array(steps),amplitude=np.array(amplitude),
                **{k:np.array(v) for k,v in snapshots.items()},
                **{k+'_phasor':z/window for k,z in zip(['E','Hx','Hy'],sums)},
                **{k+'_first':z/(window//2) for k,z in zip(['E','Hx','Hy'],first)},
                **{k+'_second':z/(window//2) for k,z in zip(['E','Hx','Hy'],second)})
    # Complete numerical candidate precedes any reference or flux diagnostic.
    np.savez_compressed(output/(name+'.npz'),**fields)
    np.savetxt(output/(name+'-history.csv'),np.array(history),delimiter=',',header='time,maximum_field',comments='',fmt='%.16e')
    return fields,g
