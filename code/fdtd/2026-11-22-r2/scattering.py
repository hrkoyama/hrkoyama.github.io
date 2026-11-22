"""Original TMz Yee scattering and x-directed Berenger split-field PML.

E=Ex+Ey at integer x/y nodes and integer times; Hx at y halves,
Hy at x halves and both H components at half times. x caps are PEC;
y is periodic. gamma is a matched rate (sigma_e/epsilon=sigma_m/mu).
"""
import math
import numpy as np


def geometry(nx,ny,lx,ly,dt,epsilon_left=1.,epsilon_right=None,interface=None,
             pml_thickness=0.,pml_strength=0.,pml_order=3):
    if not isinstance(nx,int) or not isinstance(ny,int) or min(nx,ny)<4:
        raise ValueError('integer nx,ny >=4 required')
    if not all(math.isfinite(v) and v>0 for v in [lx,ly,dt,epsilon_left]):
        raise ValueError('positive finite lengths, dt and epsilon required')
    if epsilon_right is not None and (not math.isfinite(epsilon_right) or epsilon_right<=0):
        raise ValueError('positive finite right permittivity required')
    dx,dy=lx/nx,ly/ny
    if dt*np.sqrt(dx**-2+dy**-2)/np.sqrt(min(epsilon_left,epsilon_right or epsilon_left))>=1:
        raise ValueError('strict 2D Yee CFL required')
    if not (0<=pml_thickness<lx/2 and pml_strength>=0 and isinstance(pml_order,int) and pml_order>=1):
        raise ValueError('invalid PML profile')
    x=np.arange(nx+1)*dx;xh=(np.arange(nx)+.5)*dx
    eps=np.full(nx+1,epsilon_left)
    if epsilon_right is not None:
        if interface is None or not 0<interface<lx or abs(interface/dx-round(interface/dx))>1e-10:
            raise ValueError('dielectric interface must coincide with an electric node')
        eps[x>interface]=epsilon_right
        eps[int(round(interface/dx))]=.5*(epsilon_left+epsilon_right)
    def profile(z):
        if pml_thickness==0:return np.zeros_like(z)
        depth=np.maximum(np.maximum(pml_thickness-z,z-(lx-pml_thickness)),0)/pml_thickness
        return pml_strength*depth**pml_order
    return dict(nx=nx,ny=ny,lx=lx,ly=ly,dx=dx,dy=dy,dt=dt,x=x,xh=xh,
                eps=eps[:,None],ge=profile(x)[:,None],gh=profile(xh)[:,None],
                thickness=pml_thickness,strength=pml_strength,order=pml_order)


def inner(a,b,g,component='e',weight=1.):
    z=a*b*weight
    if component!='hy':
        z=z.copy();z[[0,-1]]*=.5
    return float(np.sum(z)*g['dx']*g['dy'])


def magnetic(e,hx,hy,g):
    dt=g['dt'];d=.5*dt*g['gh']
    xp=hx-dt*(np.roll(e,-1,axis=1)-e)/g['dy']
    yp=((1-d)*hy+dt*np.diff(e,axis=0)/g['dx'])/(1+d)
    return xp,yp


def step(state,g):
    ex,ey,hx,hy=state;e=ex+ey
    xp,yp=magnetic(e,hx,hy,g)
    en=np.zeros_like(ex);yn=np.zeros_like(ey)
    d=.5*g['dt']*g['ge']
    en[1:-1]=((1-d[1:-1])*ex[1:-1]+g['dt']*np.diff(yp,axis=0)/(g['eps'][1:-1]*g['dx']))/(1+d[1:-1])
    yn[1:-1]=ey[1:-1]-g['dt']*(xp[1:-1]-np.roll(xp[1:-1],1,axis=1))/(g['eps'][1:-1]*g['dy'])
    return en,yn,xp,yp


def energy(state,g):
    ex,ey,hx,hy=state;e=ex+ey
    xp,yp=magnetic(e,hx,hy,g)
    u=.5*(inner(e,e,g,weight=g['eps'])+inner(hx,xp,g,'hx')+inner(hy,yp,g,'hy'))
    v=.5*(inner(e,e,g,weight=g['eps'])+inner(.5*(hx+xp),.5*(hx+xp),g,'hx')+inner(.5*(hy+yp),.5*(hy+yp),g,'hy'))
    return u,v


def pml_work(old,new,g):
    """Independently evaluated exact discrete electric/magnetic PML work.

    NOT defined by an energy difference. Local split-field electric work can
    be signed; only the measured net work for each fixed packet is assessed.
    """
    ex,ey,hx,hy=old;en,yn,xp,yp=new
    _,ypp=magnetic(en+yn,xp,yp,g)
    ebar=.5*(ex+ey+en+yn);exbar=.5*(ex+en)
    hybar_old=.5*(hy+yp);hybar_new=.5*(yp+ypp)
    we=g['dt']*inner(ebar,exbar,g,weight=g['eps']*g['ge'])
    wh=.5*g['dt']*inner(yp,hybar_old+hybar_new,g,'hy',weight=g['gh'])
    return we,wh


def region_energy(state,g,xmin,xmax):
    ex,ey,hx,hy=state;e=ex+ey;xp,yp=magnetic(e,hx,hy,g)
    emask=((g['x']>=xmin)&(g['x']<=xmax)).astype(float)[:,None]
    # Half quadrature weights at internal endpoints partition adjacent regions.
    for boundary in [xmin,xmax]:
        if 0<boundary<g['lx']:
            emask[np.isclose(g['x'],boundary,rtol=0,atol=1e-10)]*=.5
    hmask=((g['xh']>=xmin)&(g['xh']<=xmax))[:,None]
    return .5*(inner(e,e,g,weight=g['eps']*emask)+inner(.5*(hx+xp),.5*(hx+xp),g,'hx',weight=emask)+inner(.5*(hy+yp),.5*(hy+yp),g,'hy',weight=hmask))


def physical_boundary_flux(state,g,xmin,xmax):
    ex,ey,hx,hy=state;e=ex+ey;_,yp=magnetic(e,hx,hy,g)
    hc=.5*(hy+yp)
    def flux(x):
        i=int(round(x/g['dx']))
        return float(-np.sum(e[i]*.5*(hc[i-1]+hc[i]))*g['dy'])
    return flux(xmax)-flux(xmin)


def continuum_packet(g,kx,ky,center,width,electric_time,magnetic_time,enforce_caps=True):
    """Exact continuum finite Fourier sum; Gaussian-weighted positive k spectrum.

    Analytic Gaussian Fourier weights are summed on a fixed 511-mode k grid,
    independent of Yee mesh and step. Both clocks and field positions differ.
    """
    dk=2*np.pi/64.;ks=np.arange(1,512)*dk
    amp=width/np.sqrt(2*np.pi)*np.exp(-.5*width**2*(ks-kx)**2)*dk
    om=np.sqrt(ks**2+ky**2)
    phase_e=np.exp(1j*((g['x'][:,None]-center)*ks[None,:]-electric_time*om[None,:]))
    phase_h=np.exp(1j*((g['x'][:,None]-center)*ks[None,:]-magnetic_time*om[None,:]))
    phase_y=np.exp(1j*((g['xh'][:,None]-center)*ks[None,:]-magnetic_time*om[None,:]))
    fy=np.exp(1j*ky*np.arange(g['ny'])*g['dy'])[None,:]
    fyh=np.exp(1j*ky*(np.arange(g['ny'])+.5)*g['dy'])[None,:]
    ex=np.sum(phase_e*(amp*ks**2/om**2),axis=1);ey=np.sum(phase_e*(amp*ky**2/om**2),axis=1)
    hx=np.sum(phase_h*(amp*ky/om),axis=1);hy=np.sum(phase_y*(-amp*ks/om),axis=1)
    out=[np.real(ex[:,None]*fy),np.real(ey[:,None]*fy),np.real(hx[:,None]*fyh),np.real(hy[:,None]*fy)]
    # Caps are far from the initial/reference packet; preserve prescribed PEC.
    if enforce_caps:
        out[0][[0,-1]]=0;out[1][[0,-1]]=0;out[2][[0,-1]]=0
    return tuple(out)


def gaussian(g,center,width,time,epsilon_left=1.,epsilon_right=None,interface=None):
    """Continuum normal-incidence pulse and exact Fresnel interface solution."""
    n1=np.sqrt(epsilon_left);x=g['x'][:,None];xh=g['xh'][:,None]
    f=lambda z:np.exp(-.5*((z-center)/width)**2)
    if epsilon_right is None:
        e=f(x-time/n1);hy=-n1*f(xh-time/n1)
    else:
        n2=np.sqrt(epsilon_right);r=(n1-n2)/(n1+n2);t=2*n1/(n1+n2);a=interface
        e=np.where(x<=a,f(x-time/n1)+r*f(2*a-x-time/n1),t*f(a+(x-a)*n2/n1-time/n1))
        hy=np.where(xh<a,-n1*f(xh-time/n1)+n1*r*f(2*a-xh-time/n1),-n2*t*f(a+(xh-a)*n2/n1-time/n1))
    return np.repeat(e,g['ny'],axis=1),np.zeros((g['nx']+1,g['ny'])),np.repeat(hy,g['ny'],axis=1)


def normal_initial(g,p):
    e,_,_=gaussian(g,p['center'],p['width'],0,p.get('epsilon_left',1.))
    _,hx,hy=gaussian(g,p['center'],p['width'],-g['dt']/2,p.get('epsilon_left',1.))
    e[[0,-1]]=0
    return e,np.zeros_like(e),hx,hy


def relative_field_error(state,reference,g,mask=None):
    ex,ey,hx,hy=state;e=ex+ey;er,xr,yr=reference
    return float(np.sqrt((inner(e-er,e-er,g,weight=g['eps'])+inner(hx-xr,hx-xr,g,'hx')+inner(hy-yr,hy-yr,g,'hy'))/
                         (inner(er,er,g,weight=g['eps'])+inner(xr,xr,g,'hx')+inner(yr,yr,g,'hy'))))


def run_interface(p,nx):
    lx,ly=p['lengths'];ny=p['transverse_cells'];dx=lx/nx
    maximum=p['courant']/np.sqrt(dx**-2+(ly/ny)**-2)/np.sqrt(1/min(p['epsilon_left'],p['epsilon_right']))
    steps=int(np.ceil(p['end_time']/maximum));dt=p['end_time']/steps
    g=geometry(nx,ny,lx,ly,dt,p['epsilon_left'],p['epsilon_right'],p['interface'])
    state=normal_initial(g,p);u0,v0=energy(state,g);history=[];drift=0.
    initial_exact=np.sqrt(np.pi)*p['width']*p['epsilon_left']*ly
    for n in range(steps+1):
        u,v=energy(state,g);drift=max(drift,abs(u/u0-1));history.append([nx,0.,n*dt,u,v,0.,0.])
        if n<steps:state=step(state,g)
    e=state[0]+state[1]
    ref_e,_,_=gaussian(g,p['center'],p['width'],p['end_time'],p['epsilon_left'],p['epsilon_right'],p['interface'])
    _,ref_hx,ref_hy=gaussian(g,p['center'],p['width'],p['end_time']-dt/2,p['epsilon_left'],p['epsilon_right'],p['interface'])
    ref=(ref_e,ref_hx,ref_hy)
    n1=np.sqrt(p['epsilon_left']);n2=np.sqrt(p['epsilon_right']);r=(n1-n2)/(n1+n2);t=2*n1/(n1+n2)
    shape_ref=np.exp(-.5*((2*p['interface']-g['x']-p['end_time']/n1-p['center'])/p['width'])**2)
    shape_trans=np.exp(-.5*((p['interface']+(g['x']-p['interface'])*n2/n1-p['end_time']/n1-p['center'])/p['width'])**2)
    left=g['x']<p['interface'];right=g['x']>p['interface']
    rf=float(np.sum(e[left]*shape_ref[left,None])/np.sum(np.repeat(shape_ref[left,None]**2,ny,axis=1)))
    tf=float(np.sum(e[right]*shape_trans[right,None])/np.sum(np.repeat(shape_trans[right,None]**2,ny,axis=1)))
    R=region_energy(state,g,0,p['interface'])/initial_exact
    T=region_energy(state,g,p['interface'],lx)/initial_exact
    metrics=dict(nx=nx,ny=ny,dx=dx,dt=dt,steps=steps,field_relative_l2=relative_field_error(state,ref,g),
                 reflection_amplitude=rf,transmission_amplitude=tf,analytic_r=float(r),analytic_t=float(t),
                 reflected_energy_fraction=R,transmitted_energy_fraction=T,analytic_R=float(r*r),analytic_T=float(n2/n1*t*t),
                 reflection_amplitude_error=abs(rf-r),transmission_amplitude_error=abs(tf-t),
                 reflected_energy_error=abs(R-r*r),transmitted_energy_error=abs(T-n2/n1*t*t),
                 energy_fraction_closure=abs(R+T-1),modified_energy_max_relative_drift=drift,
                 physical_energy_relative_error=abs(energy(state,g)[1]/initial_exact-1))
    snapshot=(g['x'],e[:,0],ref_e[:,0])
    return metrics,history,snapshot


def reflected_packet_monitor(g,p,ky,times):
    """Exact single-bounce continuum PEC-backed x-PML Ez at the monitor."""
    dk=2*np.pi/64.;ks=np.arange(1,512)*dk;om=np.sqrt(ks**2+ky**2)
    amp=p['width']/np.sqrt(2*np.pi)*np.exp(-.5*p['width']**2*(ks-p['carrier_kx'])**2)*dk
    integrated=p['pml_strength']*p['pml_thickness']/(p['pml_order']+1)
    weights=-amp*np.exp(-2*ks/om*integrated)*np.exp(1j*ks*(2*g['lx']-p['monitor_x']-p['center']))
    phase=np.exp(-1j*np.asarray(times)[:,None]*om[None,:])
    x=np.sum(phase*weights[None,:],axis=1)
    return np.real(x[:,None]*np.exp(1j*ky*np.arange(g['ny'])*g['dy'])[None,:])


def run_pml(p,nx,ny,ky):
    lx,ly=p['lengths'];dx=lx/nx;maximum=p['courant']/np.sqrt(dx**-2+(ly/ny)**-2)
    steps=int(np.ceil(p['end_time']/maximum));dt=p['end_time']/steps
    g=geometry(nx,ny,lx,ly,dt,pml_thickness=p['pml_thickness'],pml_strength=p['pml_strength'],pml_order=p['pml_order'])
    initial_unclipped=continuum_packet(g,p['carrier_kx'],ky,p['center'],p['width'],0,-dt/2,enforce_caps=False)
    state=continuum_packet(g,p['carrier_kx'],ky,p['center'],p['width'],0,-dt/2)
    analytic_return=reflected_packet_monitor(g,p,ky,np.arange(steps+1)*dt)
    reflection_error=0.;analytic_reflection=0.;
    squared_error=0.;gate_samples=0
    # Independently bounded reference uses identical Yee spacing on a larger box,
    # so subtraction isolates boundary reflection, not bulk grid dispersion.
    extra=2*nx;gr=geometry(5*nx,ny,5*lx,ly,dt)
    shifted={**p,'center':p['center']+2*lx}
    refstate=continuum_packet(gr,p['carrier_kx'],ky,shifted['center'],p['width'],0,-dt/2)
    u0,v0=energy(state,g);we=0.;wh=0.;budget=0.;history=[];reflection=0.;incident=0.;accuracy=None
    xa=p['pml_thickness'];xb=lx-p['pml_thickness']
    interior0=region_energy(state,g,xa,xb);outflux=0.;physical_budget=0.;last_flux=None
    initial_layer_energy_fraction=(region_energy(state,g,0,xa)+region_energy(state,g,xb,lx))/v0
    initial_cap_field_max=float(np.max(np.abs((initial_unclipped[0]+initial_unclipped[1])[[0,-1]])))
    layer=(g['x']<xa)|(g['x']>xb)
    initial_layer_field_max=float(np.max(np.abs((initial_unclipped[0]+initial_unclipped[1])[layer])))
    monitor=int(round(p['monitor_x']/dx));physical=(g['x']>=p['pml_thickness'])&(g['x']<=lx-p['pml_thickness'])
    first=int(round(p['accuracy_time']/dt));tfirst=first*dt
    vg=p['carrier_kx']/np.hypot(p['carrier_kx'],ky)
    # Gate starts after the incident packet has cleared the monitor, before the
    # earliest return from the outer PEC cap. Return monitor subtraction is used.
    gate=p['reflection_gate_start']
    waveforms=[]
    for n in range(steps+1):
        u,v=energy(state,g);budget=max(budget,abs((u+we+wh-u0)/u0))
        flux=physical_boundary_flux(state,g,xa,xb)
        if last_flux is not None:outflux+=.5*dt*(last_flux+flux)
        last_flux=flux
        ui=region_energy(state,g,xa,xb)
        physical_budget=max(physical_budget,abs(ui+outflux-interior0)/interior0)
        history.append([nx,ky,n*dt,u,v,we,wh,ui,outflux])
        field=state[0]+state[1];rfield=refstate[0]+refstate[1]
        returned=field[monitor]-rfield[extra+monitor]
        amp=float(np.sqrt(np.mean(returned**2)));refamp=float(np.sqrt(np.mean(rfield[extra+monitor]**2)))
        incident=max(incident,refamp)
        if n*dt>=gate:
            reflection=max(reflection,amp)
            analytic_reflection=max(analytic_reflection,float(np.sqrt(np.mean(analytic_return[n]**2))))
            difference=float(np.mean((returned-analytic_return[n])**2))
            reflection_error=max(reflection_error,np.sqrt(difference));squared_error+=difference;gate_samples+=1
        waveforms.append([nx,ky,n*dt,float(field[monitor,0]),float(rfield[extra+monitor,0]),amp,float(analytic_return[n,0]),float(returned[0])])
        if n==first:
            analytic=continuum_packet(g,p['carrier_kx'],ky,p['center'],p['width'],tfirst,tfirst-dt/2)
            accuracy=relative_field_error(state,(analytic[0]+analytic[1],analytic[2],analytic[3]),g)
        if n<steps:
            new=step(state,g);a,b=pml_work(state,new,g);we+=a;wh+=b;state=new;refstate=step(refstate,gr)
    final_e=state[0]+state[1];final_ref=refstate[0]+refstate[1]
    reference_same_box=final_ref[extra:extra+nx+1]
    physnorm=float(np.sqrt(np.sum((final_e[physical]-reference_same_box[physical])**2)*dx*g['dy']/v0))
    metrics=dict(nx=nx,ny=ny,dx=dx,dt=dt,steps=steps,ky=ky,carrier_angle_degrees=float(np.degrees(np.arctan2(ky,p['carrier_kx']))),
                 actual_accuracy_time=tfirst,field_relative_l2=accuracy,
                 reflection_amplitude_ratio=reflection/incident,reflected_peak_intensity_ratio=(reflection/incident)**2,
                 incident_monitor_rms_peak=incident,returned_monitor_rms_peak=reflection,
                 analytic_return_peak_ratio=analytic_reflection/incident,
                 reflected_waveform_max_error_ratio=reflection_error/incident,
                 reflected_waveform_rms_error_ratio=float(np.sqrt(squared_error/gate_samples)/incident),
                 carrier_finite_layer_attenuation_estimate=float(np.exp(-2*vg*p['pml_strength']*p['pml_thickness']/(p['pml_order']+1))),
                 initial_layer_energy_fraction=initial_layer_energy_fraction,initial_layer_electric_field_max=initial_layer_field_max,initial_unclipped_cap_electric_field_max=initial_cap_field_max,
                 spectrum_spacing=float(2*np.pi/64),spectrum_mode_count=511,spectrum_max_kx=float(511*2*np.pi/64),
                 reflection_gate_start=gate,reflection_gate_end=p['end_time'],
                 modified_energy_budget_relative_residual=budget,
                 electric_pml_work_fraction=we/u0,magnetic_pml_work_fraction=wh/u0,total_pml_work_fraction=(we+wh)/u0,
                 remaining_modified_energy_fraction=energy(state,g)[0]/u0,
                 physical_region_flux_budget_max_relative_residual=physical_budget,
                 physical_region_outgoing_flux_fraction=outflux/interior0,
                 physical_region_remaining_energy_fraction=ui/interior0,
                 remaining_physical_energy_fraction=energy(state,g)[1]/v0,
                 interior_return_field_relative_l2=physnorm,
                 reference_domain_length=5*lx,reference_boundary_distance=min(p['center']+2*lx,3*lx-p['center']),
                 pml_thickness=p['pml_thickness'],pml_cells=int(round(p['pml_thickness']/dx)),pml_strength=p['pml_strength'])
    return metrics,history,(g['x'],final_e[:,0],reference_same_box[:,0]),waveforms
