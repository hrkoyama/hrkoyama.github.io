"""Lossless oblique TMz dielectric scattering; original Yee/Fresnel example.

Ez is optical s/TE polarization for incidence in the x-y plane.  The y
direction is periodic; distant PEC x caps are retained, with no PML.  Exact
continuum modal Fresnel fields are evaluated by a finite spectral quadrature.
The packet-energy reference is a Parseval quadrature for the underlying
positive-k continuous spectrum, not an integral of a quasiperiodic sum over R.
"""
import numpy as np
from scattering import geometry,step,energy,inner,region_energy,relative_field_error


def spectrum(p,period=None):
    period=p['reference_period'] if period is None else period
    dk=2*np.pi/period
    k=np.arange(1,int(round(p['spectral_cutoff']/dk))+1)*dk
    a=p['width']/np.sqrt(2*np.pi)*np.exp(-.5*(p['width']*(k-p['carrier_kx']))**2)*dk
    return k,a


def fresnel(k,ky,eps1,eps2):
    k=np.asarray(k,dtype=float)
    if np.any(k<=0) or eps1<=0 or eps2<eps1 or ky<0:raise ValueError('positive propagating low-to-high interface required')
    omega=np.sqrt((k*k+ky*ky)/eps1)
    q=np.sqrt(eps2*omega*omega-ky*ky)
    r=(k-q)/(k+q);t=2*k/(k+q)
    return dict(omega=omega,q=q,r=r,t=t,R=r*r,T=q/k*t*t,qprime=eps2/eps1*k/q)


def modal_amplitudes(x,p,ky,time,component='e',part='total',period=None):
    """Complex x-amplitude at a component's own position and time."""
    k,a=spectrum(p,period);z=fresnel(k,ky,p['epsilon_left'],p['epsilon_right'])
    x=np.asarray(x);a0=p['interface'];center=p['center'];omega=z['omega']
    def add(which):
        if which=='incident':phase=(x[:,None]-center)*k;coefficient=np.ones_like(k);kx=k
        elif which=='reflected':phase=(2*a0-x[:,None]-center)*k;coefficient=z['r'];kx=-k
        else:phase=(a0-center)*k+(x[:,None]-a0)*z['q'];coefficient=z['t'];kx=z['q']
        if component=='hx':coefficient=coefficient*ky/omega
        if component=='hy':coefficient=coefficient*(-kx/omega)
        return np.sum(np.exp(1j*(phase-time*omega))*(a*coefficient),axis=1)
    if part!='total':return add(part)
    return np.where(x<=a0,add('incident')+add('reflected'),add('transmitted'))


def fields(g,p,ky,electric_time,magnetic_time,part='total',period=None):
    y=np.arange(g['ny'])*g['dy'];yh=y+.5*g['dy']
    return tuple(np.real(modal_amplitudes(xx,p,ky,tt,component,part,period)[:,None]*np.exp(1j*ky*yy)[None,:])
        for xx,yy,tt,component in [(g['x'],y,electric_time,'e'),(g['x'],yh,magnetic_time,'hx'),(g['xh'],y,magnetic_time,'hy')])


def reference_energy(p,ky,period=None):
    period=p['reference_period'] if period is None else period
    k,a=spectrum(p,period);z=fresnel(k,ky,p['epsilon_left'],p['epsilon_right'])
    weights=a*a;den=np.sum(weights)
    return (float(.5*p['epsilon_left']*p['lengths'][1]*period*den),
            float(np.sum(weights*z['R'])/den),float(np.sum(weights*z['T'])/den))


def norm_squared(f,g):
    return sum(inner(a,a,g,component,weight=g['eps'] if component=='e' else 1.)
               for a,component in zip(f,['e','hx','hy']))


def cap_trace(p,ky,times):
    # Evaluate both physical PEC caps before clipping, including the complete
    # incident/reflected/transmitted superposition at every simulation clock.
    k,a=spectrum(p);z=fresnel(k,ky,p['epsilon_left'],p['epsilon_right']);a0=p['interface'];c=p['center'];L=p['lengths'][0]
    phase=np.exp(-1j*times[:,None]*z['omega'])
    left=np.sum(phase*a*(np.exp(-1j*k*c)+z['r']*np.exp(1j*k*(2*a0-c))),axis=1)
    right=np.sum(phase*a*z['t']*np.exp(1j*(k*(a0-c)+z['q']*(L-a0))),axis=1)
    return float(max(np.max(np.abs(left)),np.max(np.abs(right))))


def face_flux(state,g,x):
    e=state[0]+state[1]
    from scattering import magnetic
    _,hp=magnetic(e,state[2],state[3],g);hc=.5*(state[3]+hp)
    i=int(round(x/g['dx']))
    return float(-np.sum(e[i]*.5*(hc[i-1]+hc[i]))*g['dy'])


def run_mesh(p,nx,ny,ky):
    lx,ly=p['lengths'];dx=lx/nx;dy=ly/ny
    maximum=p['courant']*np.sqrt(min(p['epsilon_left'],p['epsilon_right']))/np.hypot(1/dx,1/dy)
    steps=int(np.ceil(p['end_time']/maximum));dt=p['end_time']/steps
    g=geometry(nx,ny,lx,ly,dt,p['epsilon_left'],p['epsilon_right'],p['interface'])
    initial=fields(g,p,ky,0,-dt/2);state=(initial[0].copy(),np.zeros_like(initial[0]),initial[1].copy(),initial[2].copy())
    state[0][[0,-1]]=0;state[2][[0,-1]]=0
    clipping=float(norm_squared(tuple(a-b for a,b in zip([state[0],state[2],state[3]],initial)),g)/norm_squared(initial,g))
    u0,v0=energy(state,g);incident,Rexact,Texact=reference_energy(p,ky)
    a,b=p['flux_region'];region0=region_energy(state,g,a,b)
    history=[];drift=flux_error=0.;flux_left=flux_right=0.;last=None
    for n in range(steps+1):
        u,v=energy(state,g);region=region_energy(state,g,a,b)
        fl,fr=face_flux(state,g,a),face_flux(state,g,b)
        if last is not None:
            flux_left+=.5*dt*(last[0]+fl);flux_right+=.5*dt*(last[1]+fr)
        last=(fl,fr);drift=max(drift,abs(u/u0-1));flux_error=max(flux_error,abs(region-region0+flux_right-flux_left)/incident)
        history.append([nx,ny,ky,n*dt,u,v,region,flux_left,flux_right])
        if n<steps:state=step(state,g)
    exact=fields(g,p,ky,p['end_time'],p['end_time']-dt/2)
    reflected=fields(g,p,ky,p['end_time'],p['end_time']-dt/2,'reflected')
    transmitted=fields(g,p,ky,p['end_time'],p['end_time']-dt/2,'transmitted')
    e=state[0]+state[1];left=g['x']<p['interface'];right=g['x']>p['interface']
    def projection(mask,template):
        denominator=np.sum(template[mask]**2)
        gain=float(np.sum(e[mask]*template[mask])/denominator)
        error=float(np.sqrt(np.sum((e[mask]-template[mask])**2)/denominator))
        return gain,error
    rg,re=projection(left,reflected[0]);tg,te=projection(right,transmitted[0])
    R=region_energy(state,g,0,p['interface'])/incident;T=region_energy(state,g,p['interface'],lx)/incident
    # Initial secondary fields and the finite-window reference partition
    # quantify the two finite-packet approximations separately from Yee error.
    inc0=fields(g,p,ky,0,-dt/2,'incident');inc0=tuple(np.where((g['xh'] if j==2 else g['x'])[:,None]<p['interface'],f,0.) for j,f in enumerate(inc0))
    tail=float(norm_squared(tuple(a-b for a,b in zip(initial,inc0)),g)/norm_squared(initial,g))
    # Same-time continuum H for physical quadrature (not the Yee H average).
    physical_exact=fields(g,p,ky,p['end_time'],p['end_time'])
    def physical_region(f,lo,hi):
        xs=[g['x'],g['x'],g['xh']];total=0.
        for component,z,x in zip(['e','hx','hy'],f,xs):
            mask=((x>=lo)&(x<=hi)).astype(float)
            if component!='hy':
                for endpoint in [lo,hi]:
                    if 0<endpoint<lx:mask[np.isclose(x,endpoint,atol=1e-10,rtol=0)]*=.5
            total+=.5*inner(z,z,g,component,weight=mask[:,None]*(g['eps'] if component=='e' else 1.))
        return total
    Rwindow=physical_region(physical_exact,0,p['interface'])/incident;Twindow=physical_region(physical_exact,p['interface'],lx)/incident
    doubled=fields(g,p,ky,p['end_time'],p['end_time']-dt/2,period=2*p['reference_period'])
    period_error=float(np.sqrt(norm_squared(tuple(a-b for a,b in zip(exact,doubled)),g)/norm_squared(exact,g)))
    initial_same=fields(g,p,ky,0,0)
    initial_quadrature=physical_region(initial_same,0,lx)/incident
    carrier=fresnel(np.array([p['carrier_kx']]),ky,p['epsilon_left'],p['epsilon_right'])
    row=dict(nx=nx,ny=ny,ky=float(ky),dx=dx,dy=dy,dt=dt,steps=steps,
        incident_angle_degrees=float(np.degrees(np.arctan2(ky,p['carrier_kx']))),transmitted_angle_degrees=float(np.degrees(np.arctan2(ky,carrier['q'][0]))),
        carrier_r=float(carrier['r'][0]),carrier_t=float(carrier['t'][0]),carrier_R=float(carrier['R'][0]),carrier_T=float(carrier['T'][0]),
        analytic_incident_energy=incident,analytic_R=Rexact,analytic_T=Texact,
        field_relative_l2=relative_field_error(state,exact,g),
        reflected_template_gain=rg,transmitted_template_gain=tg,reflection_gain_error=abs(rg-1),transmission_gain_error=abs(tg-1),
        reflected_field_relative_l2=re,transmitted_field_relative_l2=te,
        reflected_energy_fraction=float(R),transmitted_energy_fraction=float(T),reflected_energy_error=abs(R-Rexact),transmitted_energy_error=abs(T-Texact),
        energy_fraction_closure=abs(R+T-1),initial_physical_energy_ratio=v0/incident,
        modified_energy_max_relative_drift=float(drift),physical_flux_budget_max_relative_residual=float(flux_error),
        initial_secondary_field_energy_fraction=tail,initial_pec_clipping_field_norm_fraction=clipping,analytic_cap_electric_max=cap_trace(p,ky,np.arange(steps+1)*dt),
        reference_period_doubling_relative_l2=period_error,reference_window_R=float(Rwindow),reference_window_T=float(Twindow),
        reference_window_energy_error=float(max(abs(Rwindow-Rexact),abs(Twindow-Texact))),reference_initial_energy_ratio=float(initial_quadrature),
        reference_final_interface_electric_max=float(abs(modal_amplitudes(np.array([p['interface']]),p,ky,p['end_time']))[0]),
        reference_period=p['reference_period'],spectrum_kmax=float(spectrum(p)[0][-1]),spectrum_dk=float(2*np.pi/p['reference_period']),
        flux_region_initial_energy=region0,flux_region_final_energy=float(region),flux_left_integral=float(flux_left),flux_right_integral=float(flux_right))
    return row,history,(g['x'].copy(),e[:,0].copy(),exact[0][:,0].copy())
