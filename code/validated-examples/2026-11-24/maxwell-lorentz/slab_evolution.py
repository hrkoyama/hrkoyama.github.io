"""Actual matched material/vacuum single-ky Yee pulse trajectories, s and p."""
import numpy as np
import modal_yee_draft as core


def build(spec,h,ny):
    left,right=spec['domain'];n=int(round((right-left)/h));x=left+np.arange(n+1)*h;xf=left+(np.arange(n)+.5)*h
    dy=2*np.pi/spec['ky']/ny;maximum=spec['courant']/np.sqrt(1/h**2+1/dy**2)
    steps=int(np.ceil(spec['final_time']/maximum/4))*4;dt=spec['final_time']/steps
    a,b=spec['slab'];fraction=np.maximum(0,np.minimum(x+h/2,b)-np.maximum(x-h/2,a))/h
    ff=np.maximum(0,np.minimum(xf+h/2,b)-np.maximum(xf-h/2,a))/h;m=spec['material']
    result=dict(x=x,xf=xf,h=h,dy=dy,dt=dt,steps=steps,K=2*np.sin(.5*spec['ky']*dy)/dy,omega0=m['omega0'],gamma=m['gamma'],fraction_node=fraction,fraction_face=ff)
    for label,f in [('node',fraction),('face',ff)]:
        result['epsilon_'+label]=1+(m['epsilon_inf']-1)*f
        result['sigma_'+label]=m['sigma']*f
        result['strength_'+label]=m['delta_epsilon']*m['omega0']**2*f
        result['stretch_'+label]=(np.ones(len(f)),np.zeros(len(f)),np.ones(len(f)))
    return result


def initial(spec,g,polarization):
    n=len(g['xf']);h=g['h'];q=2*np.pi*np.fft.fftfreq(n,d=h);q0=np.sqrt(spec['carrier']**2-spec['ky']**2)
    mask=abs(q-q0)<=9/spec['width'];amplitude=np.zeros(n,complex)
    amplitude[mask]=np.sqrt(2*np.pi)*spec['width']/(n*h)*np.exp(-.5*((q[mask]-q0)*spec['width'])**2)*np.exp(1j*q[mask]*(g['x'][0]-spec['center']))
    Q=2*np.sin(.5*q*h)/h;O=np.sqrt(Q*Q+g['K']**2);omega=2*np.arcsin(.5*g['dt']*O)/g['dt']
    if np.any(~np.isfinite(omega)):raise ValueError('Vacuum initialization branch unresolved')
    def inverse(mult,face=False):
        z=np.fft.ifft(n*amplitude*mult*(np.exp(.5j*q*h) if face else 1.))
        return z if face else np.concatenate([z,z[:1]])
    zeros_node=np.zeros(n+1,complex);zeros_face=np.zeros(n,complex)
    half=np.exp(.5j*omega*g['dt'])
    if polarization=='s':
        E=inverse(np.ones(n));E[[0,-1]]=0.
        return E,inverse(g['K']/O*half),inverse(-Q/O*half,True),zeros_node.copy(),zeros_node.copy(),zeros_face.copy(),zeros_node.copy()
    Ex=inverse(-g['K']/O,True);Ey=inverse(Q/O);Ey[[0,-1]]=0.
    return Ex,Ey,inverse(half,True),zeros_face.copy(),zeros_node.copy(),zeros_face.copy(),zeros_node.copy(),zeros_face.copy(),zeros_node.copy()


def energy(state,g,polarization):
    dt=g['dt'];K=g['K'];h=g['h'];w=np.ones(len(g['x']));w[[0,-1]]=.5
    if polarization=='s':
        E,Hx,Hy,P,J=state[:5];xp=Hx-1j*dt*K*E;yp=Hy+dt*np.diff(E)/h
        node=.5*g['epsilon_node']*abs(E)**2+core.oscillator_energy(P,J,g['strength_node'],g['omega0'])+.5*np.real(Hx*np.conj(xp));face=.5*np.real(Hy*np.conj(yp))
    else:
        Ex,Ey,H,Px,Py,Jx,Jy=state[:7];hp=H+dt*(1j*K*Ex-np.diff(Ey)/h)
        face=.5*g['epsilon_face']*abs(Ex)**2+core.oscillator_energy(Px,Jx,g['strength_face'],g['omega0'])+.5*np.real(H*np.conj(hp))
        node=.5*g['epsilon_node']*abs(Ey)**2+core.oscillator_energy(Py,Jy,g['strength_node'],g['omega0'])
    return float(.5*(2*np.pi/(2*np.arcsin(.5*K*g['dy'])/g['dy']))*h*(np.sum(w*node)+np.sum(face)))


def physical_work(d,g,polarization):
    w=np.ones(len(g['x']));w[[0,-1]]=.5
    if polarization=='s':value=np.sum(w*(d['ohmic_density']+d['material_damping_density']))
    else:value=np.sum(d['ohmic_face']+d['material_damping_face'])+np.sum(w*(d['ohmic_node']+d['material_damping_node']))
    ky=2*np.arcsin(.5*g['K']*g['dy'])/g['dy']
    return float(np.pi/ky*g['h']*value)


def vacuum_grid(g):
    out=dict(g)
    for side in ['node','face']:
        out['epsilon_'+side]=np.ones_like(g['epsilon_'+side]);out['sigma_'+side]=np.zeros_like(g['sigma_'+side]);out['strength_'+side]=np.zeros_like(g['strength_'+side])
    return out


def solve(spec,h,ny,polarization,output,name):
    g=build(spec,h,ny);vac=vacuum_grid(g);material=initial(spec,g,polarization);vacuum=tuple(z.copy() for z in material)
    active_node=g['fraction_node']>0;active_face=g['fraction_face']>0
    frequency=np.array(spec['frequencies']);nf=len(frequency)
    # Monitor E_z(s) or H_z(p). H_z and its x coordinate are native halves.
    coords=g['x'] if polarization=='s' else g['xf'];mi=[int(np.argmin(abs(coords-y))) for y in [spec['left_monitor'],spec['right_monitor']]]
    monitors=np.zeros((2,2,nf),complex)
    if polarization=='s':integrals=[np.zeros((nf,int(active_node.sum())),complex) for _ in range(2)]
    else:integrals=[np.zeros((nf,int(active_face.sum())),complex),np.zeros((nf,int(active_node.sum())),complex),np.zeros((nf,int(active_face.sum())),complex),np.zeros((nf,int(active_node.sum())),complex)]
    steps=g['steps'];dt=g['dt'];scheduled={i*steps//4 for i in range(5)};snapshots={};times=[];history=[];work=0.;minimum_work=0.;completed=0;material_step=0;vacuum_step=0
    np.savez_compressed(output/(name+'-initial-state.npz'),**{f'material_state{i}':z for i,z in enumerate(material)},**{f'vacuum_state{i}':z for i,z in enumerate(vacuum)})
    initial_energy=energy(material,g,polarization);initial_vacuum=energy(vacuum,vac,polarization);max_budget=0.;max_vacuum_budget=0.
    def retain(step):
        np.savez_compressed(output/(name+'-current-state.npz'),step=np.array(step),time=np.array(step*dt),material_step=np.array(material_step),vacuum_step=np.array(vacuum_step),**{f'material_state{i}':z for i,z in enumerate(material)},**{f'vacuum_state{i}':z for i,z in enumerate(vacuum)},history=np.array(history),monitors=monitors)
    def snapshot(step):
        times.append(step*dt)
        for prefix,state in [('material',material),('vacuum',vacuum)]:
            count=5 if polarization=='s' else 7
            for i in range(count):snapshots.setdefault(prefix+'_state'+str(i),[]).append(state[i].copy())
        retain(step)
    snapshot(0);advance=core.advance_s if polarization=='s' else core.advance_p
    try:
        for step in range(1,steps+1):
            previous=material;material,diagnostic=advance(material,g);material_step=step
            vacuum,_=advance(vacuum,vac);vacuum_step=step;completed=step
            physical=physical_work(diagnostic,g,polarization);work+=physical;minimum_work=min(minimum_work,physical)
            budget=abs(energy(material,g,polarization)-initial_energy+work)/initial_energy
            vac_budget=abs(energy(vacuum,vac,polarization)-initial_vacuum)/initial_vacuum
            max_budget=max(max_budget,budget);max_vacuum_budget=max(max_vacuum_budget,vac_budget)
            time=(step if polarization=='s' else step-.5)*dt
            phase=np.exp(1j*frequency*time)*dt
            component=0 if polarization=='s' else 2
            for which,state in enumerate([material,vacuum]):
                for side,index in enumerate(mi):monitors[which,side]+=state[component][index]*phase
            ep=np.exp(1j*frequency*(step-.5)*dt)[:,None]*dt
            if polarization=='s':
                integrals[0]+=ep*.5*(material[0]+previous[0])[active_node];integrals[1]+=ep*.5*(material[4]+previous[4])[active_node]
            else:
                for integral,index,mask in zip(integrals,[0,1,5,6],[active_face,active_node,active_face,active_node]):integral+=ep*.5*(material[index]+previous[index])[mask]
            primary=material[component];history.append([step*dt,material[component][mi[0]].real,material[component][mi[0]].imag,material[component][mi[1]].real,material[component][mi[1]].imag,vacuum[component][mi[0]].real,vacuum[component][mi[0]].imag,vacuum[component][mi[1]].real,vacuum[component][mi[1]].imag,energy(material,g,polarization),work,budget,vac_budget,float(np.max(abs(primary)))])
            if not np.isfinite(history[-1]).all():raise FloatingPointError('Nonfinite slab trajectory')
            if step in scheduled:snapshot(step)
    except BaseException:
        retain(completed);raise
    fields=dict(x=g['x'],xf=g['xf'],times=np.array(times),history=np.array(history),omega=frequency,monitors=monitors,monitor_coordinates=coords[mi],initial_energy=np.array(initial_energy),maximum_budget=np.array(max_budget),maximum_vacuum_budget=np.array(max_vacuum_budget),minimum_work=np.array(minimum_work),dt=np.array(dt),steps=np.array(steps),h=np.array(h),dy=np.array(g['dy']),K=np.array(g['K']),
                **{n:np.array(v) for n,v in snapshots.items()},**{'integral'+str(i):v for i,v in enumerate(integrals)},fraction_node=g['fraction_node'],fraction_face=g['fraction_face'])
    np.savez_compressed(output/(name+'.npz'),**fields)
    np.savetxt(output/(name+'-history.csv'),fields['history'],delimiter=',',header='time,material_left_real,material_left_imag,material_right_real,material_right_imag,vacuum_left_real,vacuum_left_imag,vacuum_right_real,vacuum_right_imag,energy,physical_work,budget,vacuum_budget,peak',comments='',fmt='%.16e')
    return fields,g
