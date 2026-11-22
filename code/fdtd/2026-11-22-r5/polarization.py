"""Original lossless TEz Yee / optical p-polarization verification.

The fixed experiments use an exact single-positive-ky reduction of the full
2-D periodic-y Yee update. Hz is at cell centers/integer time; Ex and Ey
are on their own edges at half time. Complex coefficients represent real
fields through Re[f(x,t) exp(i ky y)] at the component's own y location.
"""
import math
from fractions import Fraction
import numpy as np


def geometry(nx,ny,lengths,dt,eps1,eps2,interface,ky):
    lx,ly=lengths
    if min(nx,ny)<4 or not isinstance(nx,int) or not isinstance(ny,int):raise ValueError('integer grids >=4 required')
    if not all(math.isfinite(v) and v>0 for v in [lx,ly,dt,eps1,eps2,ky]):raise ValueError('positive finite parameters required')
    dx,dy=lx/nx,ly/ny
    if not 0<interface<lx or abs(interface/dx-round(interface/dx))>1e-9:raise ValueError('interface must align with Ey face')
    if ky*dy>=np.pi or abs(ky*ly/(2*np.pi)-round(ky*ly/(2*np.pi)))>1e-9:raise ValueError('resolved positive periodic ky required')
    if dt*np.hypot(1/dx,1/dy)/np.sqrt(min(eps1,eps2))>=1:raise ValueError('strict two-dimensional CFL required')
    x=np.arange(nx+1)*dx;xh=(np.arange(nx)+.5)*dx
    ex=np.where(xh<interface,eps1,eps2);ey=np.where(x<interface,eps1,eps2).astype(float);ey[int(round(interface/dx))]=.5*(eps1+eps2)
    return dict(nx=nx,ny=ny,lx=lx,ly=ly,dx=dx,dy=dy,dt=dt,x=x,xh=xh,epsx=ex,epsy=ey,ky=ky,K=2*np.sin(ky*dy/2)/dy,interface=interface,eps1=eps1,eps2=eps2)


def electric(state,g):
    h,ex,ey=state;xp=ex+g['dt']*1j*g['K']*h/g['epsx'];yp=ey.copy()
    yp[1:-1]-=g['dt']*np.diff(h)/(g['dx']*g['epsy'][1:-1]);yp[[0,-1]]=0
    return xp,yp


def step(state,g):
    h,_,_=state;xp,yp=electric(state,g)
    return h+g['dt']*(1j*g['K']*xp-np.diff(yp)/g['dx']),xp,yp


def full_step(state,g):
    """General real/complex full two-dimensional TEz update, not mode reduced."""
    h,ex,ey=state;xp=ex+g['dt']*(h-np.roll(h,1,axis=1))/(g['dy']*g['epsx'][:,None]);yp=ey.copy()
    yp[1:-1]-=g['dt']*np.diff(h,axis=0)/(g['dx']*g['epsy'][1:-1,None]);yp[[0,-1]]=0
    return h+g['dt']*((np.roll(xp,-1,axis=1)-xp)/g['dy']-np.diff(yp,axis=0)/g['dx']),xp,yp


def norm2(a):return np.real(a*np.conj(a))


def energy(state,g):
    h,ex,ey=state;xp,yp=electric(state,g);scale=.25*g['ly']*g['dx']
    modified=scale*(np.sum(norm2(h))+np.sum(g['epsx']*np.real(ex*np.conj(xp)))+np.sum(g['epsy']*np.real(ey*np.conj(yp))))
    physical=scale*(np.sum(norm2(h))+np.sum(g['epsx']*norm2(.5*(ex+xp)))+np.sum(g['epsy']*norm2(.5*(ey+yp))))
    return float(modified),float(physical)


def centered(state,g):
    h,ex,ey=state;xp,yp=electric(state,g)
    return h,.5*(ex+xp),.5*(ey+yp)


def region_energy(state,g,lo,hi):
    return physical_integral(centered(state,g),g,lo,hi)


def physical_integral(fields,g,lo,hi):
    h,ex,ey=fields;cells=(g['xh']>=lo)&(g['xh']<=hi);faces=((g['x']>=lo)&(g['x']<=hi)).astype(float)
    for z in [lo,hi]:
        if 0<z<g['lx']:faces[np.isclose(g['x'],z,rtol=0,atol=1e-9)]*=.5
    face_eps=g['epsy'].copy()
    if np.isclose(lo,g['interface']):face_eps[np.isclose(g['x'],lo)]=g['eps2']
    if np.isclose(hi,g['interface']):face_eps[np.isclose(g['x'],hi)]=g['eps1']
    return float(.25*g['ly']*g['dx']*(np.sum((norm2(h)+g['epsx']*norm2(ex))*cells)+np.sum(face_eps*norm2(ey)*faces)))


def face(state,g,x):
    h,ex,ey=centered(state,g);i=int(round(x/g['dx']))
    return .5*(h[i-1]+h[i]),ey[i]


def flux(h,e,g):return .5*g['ly']*np.real(e*np.conj(h))


def spectrum(p,case,period=None):
    P=p['reference_period'] if period is None else period;dk=2*np.pi/P
    k=np.arange(1,int(np.ceil(case['band'][1]/dk)))*dk;mask=(k>case['band'][0])&(k<case['band'][1]);k=k[mask]
    u=(k-case['carrier_kx'])/case['band_half_width']
    a=np.exp(-.5*(case['width']*(k-case['carrier_kx']))**2-u**8/(1-u*u))*dk
    # A fixed continuum normalization integral, independently refined with P.
    a/=case.get('spectral_normalization',1.)
    return k,a


def fresnel(k,ky,eps1,eps2):
    k=np.asarray(k,dtype=float)
    if np.any(k<=0) or min(eps1,eps2)<=0:raise ValueError('positive incident k and permittivities required')
    omega=np.sqrt((k*k+ky*ky)/eps1);q=np.sqrt((eps2*omega*omega-ky*ky).astype(complex))
    y1=k/eps1;y2=q/eps2;r=(y1-y2)/(y1+y2);t=1+r
    return dict(omega=omega,q=q,r=r,t=t,R=norm2(r),T=eps1/eps2*np.real(q)/k*norm2(t))


def amplitude(x,p,c,time,component='h',part='total',period=None):
    k,a=spectrum(p,c,period);z=fresnel(k,c['ky'],c['epsilon_left'],c['epsilon_right']);x=np.asarray(x);out=np.zeros(x.size,dtype=complex)
    interface=c['interface'];center=c['center']
    def term(xx,which):
        if which=='incident':phase=(xx[:,None]-center)*k;coef=np.ones_like(k);kx=k;eps=c['epsilon_left']
        elif which=='reflected':phase=(2*interface-xx[:,None]-center)*k;coef=z['r'];kx=-k;eps=c['epsilon_left']
        else:phase=(interface-center)*k+(xx[:,None]-interface)*z['q'];coef=z['t'];kx=z['q'];eps=c['epsilon_right']
        if component=='ex':coef=coef*(-c['ky']/(eps*z['omega']))
        if component=='ey':coef=coef*(kx/(eps*z['omega']))
        return np.sum(np.exp(1j*(phase-time*z['omega']))*(a*coef),axis=1)
    if part=='incident':return term(x,'incident')
    left=x<=interface
    if part in ['total','reflected']:out[left]=term(x[left],'reflected')+(term(x[left],'incident') if part=='total' else 0)
    if part in ['total','transmitted']:out[~left]=term(x[~left],'transmitted')
    return out


def fields(g,p,c,h_time,e_time,part='total',period=None):
    return (amplitude(g['xh'],p,c,h_time,'h',part,period),amplitude(g['xh'],p,c,e_time,'ex',part,period),amplitude(g['x'],p,c,e_time,'ey',part,period))


def field_norm(state,g):
    h,ex,ey=state
    return float(np.sum(norm2(h))+np.sum(g['epsx']*norm2(ex))+np.sum(g['epsy']*norm2(ey)))


def field_error(state,ref,g):return float(np.sqrt(field_norm(tuple(a-b for a,b in zip(state,ref)),g)/field_norm(ref,g)))


def incident_energy(p,c,period=None):
    P=p['reference_period'] if period is None else period;k,a=spectrum(p,c,period);z=fresnel(k,c['ky'],c['epsilon_left'],c['epsilon_right']);w=a*a
    return float(.5*c['lengths'][1]*P*np.sum(w)),float(np.sum(w*z['R'])/np.sum(w)),float(np.sum(w*z['T'])/np.sum(w))


def analytic_monitors(p,c,times,period=None):
    k,a=spectrum(p,c,period);z=fresnel(k,c['ky'],c['epsilon_left'],c['epsilon_right']);omega=z['omega'];a0=c['interface'];cc=c['center'];d=c['monitor_offset'];phase=np.exp(-1j*times[:,None]*omega)
    coefficients=[np.exp(1j*k*(a0-d-cc)),z['r']*np.exp(1j*k*(a0+d-cc)),z['t']*np.exp(1j*(k*(a0-cc)+z['q']*d))]
    kxs=[k,-k,z['q']];eps=[c['epsilon_left'],c['epsilon_left'],c['epsilon_right']];out=[]
    for coef,kx,epsilon in zip(coefficients,kxs,eps):out.extend([np.einsum('ij,j->i',phase,a*coef,optimize=False),np.einsum('ij,j->i',phase,a*coef*kx/(epsilon*omega),optimize=False)])
    out.append(np.einsum('ij,j->i',phase,a*z['t']*np.exp(1j*(k*(a0-cc)+z['q']*2*d)),optimize=False))
    return np.column_stack(out)


def discrete_k(omega,eps,g):
    z=eps*(np.sin(omega*g['dt']/2)/(g['dt']/2))**2-g['K']**2
    return 2/g['dx']*np.arcsin(np.sqrt(complex(z))*g['dx']/2)


def trapezoid(y,t):return np.trapezoid(y,x=t,axis=0)


def clock(p,c,nx,ny):
    lx,ly=c['lengths'];bx,by=c['meshes'][0];factor=nx//bx
    if nx!=factor*bx or ny!=factor*by or factor<1:raise ValueError('fixed jointly refined grids required')
    limit=p['courant']*np.sqrt(min(c['epsilon_left'],c['epsilon_right']))/np.hypot(bx/lx,by/ly)
    denominator=(Fraction(str(c['accuracy_time']))/Fraction(str(c['end_time']))).denominator
    base_steps=int(np.ceil(c['end_time']/limit/denominator))*denominator
    if base_steps>200000:raise ValueError('aligned accuracy clock requires too many steps')
    steps=base_steps*factor
    return steps,c['end_time']/steps


def transient_flux_error(numerical,reference,times):
    denominator=trapezoid(reference**2,times)
    if denominator<=0:raise ValueError('nonzero reference flux waveform required')
    return float(np.sqrt(trapezoid((numerical-reference)**2,times)/denominator))


def run_mesh(p,c,nx,ny):
    lx,ly=c['lengths'];steps,dt=clock(p,c,nx,ny)
    g=geometry(nx,ny,c['lengths'],dt,c['epsilon_left'],c['epsilon_right'],c['interface'],c['ky']);gh=geometry(nx,ny,c['lengths'],dt,c['epsilon_left'],c['epsilon_left'],c['interface'],c['ky'])
    raw=fields(g,p,c,0,-dt/2);state=tuple(z.copy() for z in raw);state[2][[0,-1]]=0
    clip_fraction=field_norm(tuple(a-b for a,b in zip(raw,state)),g)/field_norm(raw,g)
    home=fields(gh,p,c,0,-dt/2,'incident');home[2][[0,-1]]=0
    u0,v0=energy(state,g);incident,Rexact,Texact=incident_energy(p,c);lo,hi=c['flux_region'];r0=region_energy(state,g,lo,hi)
    history=[];monitors=[];drift=fluxbudget=0.;flint=frint=0.;last=None;maxright=0.;peak_right_time=0.;early_error=None;pre_error=None;pre_step=int(round(p['accuracy_time']/dt));early_step=int(round(c['accuracy_time']/dt))
    for j in range(steps+1):
        t=j*dt;u,v=energy(state,g);region=region_energy(state,g,lo,hi);right=region_energy(state,g,c['interface'],lx);
        if right/incident>maxright:maxright=right/incident;peak_right_time=t
        hl,el=face(state,g,lo);hr,er=face(state,g,hi);fl,fr=flux(hl,el,g),flux(hr,er,g)
        if last is not None:flint+=.5*dt*(last[0]+fl);frint+=.5*dt*(last[1]+fr)
        last=(fl,fr);drift=max(drift,abs(u/u0-1));fluxbudget=max(fluxbudget,abs(region-r0+frint-flint)/incident)
        hinc,einc=face(home,gh,c['interface']-c['monitor_offset']);hleft,eleft=face(state,g,c['interface']-c['monitor_offset']);htrans,etrans=face(state,g,c['interface']+c['monitor_offset']);hsecond,_=face(state,g,c['interface']+2*c['monitor_offset'])
        monitors.append([t,hinc,einc,hleft-hinc,eleft-einc,htrans,etrans,hsecond])
        history.append([c['id'],nx,ny,t,u,v,region,flint,frint,right])
        if j==pre_step:pre_error=field_error(state,fields(g,p,c,t,t-dt/2),g)
        if j==early_step:
            accuracy_ref=fields(g,p,c,t,t-dt/2);early_error=field_error(state,accuracy_ref,g);accuracy_period_error=field_error(accuracy_ref,fields(g,p,c,t,t-dt/2,period=2*p['reference_period']),g)
        if j<steps:state=step(state,g);home=step(home,gh)
    waves=np.asarray(monitors,dtype=complex);times=np.real(waves[:,0]);signals=waves[:,1:];an=analytic_monitors(p,c,times)
    f=np.column_stack([flux(signals[:,i],signals[:,i+1],g) for i in [0,2,4]]);fa=np.column_stack([flux(an[:,i],an[:,i+1],g) for i in [0,2,4]])
    flu=np.real(trapezoid(f,times));aflu=np.real(trapezoid(fa,times));R=-flu[1]/flu[0];T=flu[2]/flu[0];Ra=-aflu[1]/aflu[0];Ta=aflu[2]/aflu[0]
    carrier=fresnel(np.array([c['carrier_kx']]),c['ky'],c['epsilon_left'],c['epsilon_right']);omega=carrier['omega'][0];carrier_r=carrier['r'][0];carrier_t=carrier['t'][0]
    phase=np.exp(1j*omega*times);d=c['monitor_offset'];fnum=np.array([trapezoid(signals[:,i]*phase,times) for i in [0,2,4]]);fref=np.array([trapezoid(an[:,i]*phase,times) for i in [0,2,4]])
    kn=discrete_k(omega,c['epsilon_left'],g);qn=discrete_k(omega,c['epsilon_right'],g)
    rn=fnum[1]/fnum[0]*np.exp(-2j*kn*d);tn=fnum[2]/fnum[0]*np.exp(-1j*(kn+qn)*d)*np.cos(kn*g['dx']/2)/np.cos(qn*g['dx']/2)
    ra=fref[1]/fref[0]*np.exp(-2j*c['carrier_kx']*d);ta=fref[2]/fref[0]*np.exp(-1j*(c['carrier_kx']+carrier['q'][0])*d)
    h2num=trapezoid(signals[:,6]*phase,times);h2ref=trapezoid(an[:,6]*phase,times)
    kappa_num=float(-np.log(abs(h2num/fnum[2]))/d);kappa_ref=float(-np.log(abs(h2ref/fref[2]))/d)
    exact=fields(g,p,c,c['end_time'],c['end_time']-dt/2);doubled=fields(g,p,c,c['end_time'],c['end_time']-dt/2,period=2*p['reference_period'])
    # Initial exact scattering differs slightly from a truncated incident-only field.
    inc=fields(g,p,c,0,-dt/2,'incident');inc=tuple(np.where((g['x'] if i==2 else g['xh'])<=c['interface'],a,0.) for i,a in enumerate(inc))
    tail=field_norm(tuple(a-b for a,b in zip(raw,inc)),g)/field_norm(raw,g)
    cap_times=np.linspace(0,c['end_time'],min(steps+1,2049));caps=np.stack([amplitude(np.array([0.,lx]),p,c,t,'ey') for t in cap_times]);cap=float(np.max(np.abs(caps)))
    peak_ref=physical_integral(fields(g,p,c,peak_right_time,peak_right_time),g,c['interface'],lx)/incident
    row=dict(subcase=c['id'],nx=nx,ny=ny,dx=g['dx'],dy=g['dy'],dt=dt,steps=steps,ky=c['ky'],accuracy_time=float(early_step*dt),pre_interface_field_relative_l2=pre_error,field_relative_l2=early_error,late_field_relative_l2=field_error(state,exact,g),
        reflection_flux_fraction=float(R),transmission_flux_fraction=float(T),analytic_window_R=float(Ra),analytic_window_T=float(Ta),analytic_R=Rexact,analytic_T=Texact,
        reflection_error=float(abs(R-Ra)),transmission_error=float(abs(T-Ta)),transmitted_flux_waveform_relative_l2=transient_flux_error(f[:,2],fa[:,2],times),energy_fraction_closure=float(abs(R+T-1)),reference_window_energy_gap=float(max(abs(Ra-Rexact),abs(Ta-Texact))),
        carrier_rH_real=float(carrier_r.real),carrier_rH_imag=float(carrier_r.imag),carrier_tH_real=float(carrier_t.real),carrier_tH_imag=float(carrier_t.imag),
        numerical_rH_real=float(rn.real),numerical_rH_imag=float(rn.imag),numerical_tH_real=float(tn.real),numerical_tH_imag=float(tn.imag),reference_rH_real=float(ra.real),reference_rH_imag=float(ra.imag),reference_tH_real=float(ta.real),reference_tH_imag=float(ta.imag),complex_r_error=float(abs(rn-ra)),complex_t_error=float(abs(tn-ta)),carrier_complex_r_error=float(abs(rn-carrier_r)),carrier_complex_t_error=float(abs(tn-carrier_t)),
        reference_dft_r_error=float(abs(ra-carrier_r)),reference_dft_t_error=float(abs(ta-carrier_t)),carrier_incident_angle_degrees=float(np.degrees(np.arctan2(c['ky'],c['carrier_kx']))),
        carrier_q_real=float(carrier['q'][0].real),carrier_q_imag=float(carrier['q'][0].imag),numerical_decay_rate=kappa_num,reference_window_decay_rate=kappa_ref,decay_rate_error=abs(kappa_num-kappa_ref),carrier_decay_rate_error=abs(kappa_num-carrier['q'][0].imag),reference_decay_rate_error=abs(kappa_ref-carrier['q'][0].imag),modified_energy_max_relative_drift=float(drift),physical_flux_budget_max_relative_residual=float(fluxbudget),
        incident_fluence=float(flu[0]),analytic_incident_energy=incident,incident_fluence_energy_relative_error=float(abs(flu[0]/incident-1)),analytic_incident_fluence=float(aflu[0]),reference_incident_fluence_energy_error=float(abs(aflu[0]/incident-1)),
        max_right_stored_energy_fraction=float(maxright),peak_right_stored_time=float(peak_right_time),reference_right_energy_at_numerical_peak=float(peak_ref),peak_right_stored_energy_relative_error=abs(maxright-peak_ref)/max(abs(peak_ref),1e-30),final_right_stored_energy_fraction=float(right/incident),min_transmitted_instantaneous_flux=float(np.min(f[:,2])/incident),max_transmitted_instantaneous_flux=float(np.max(f[:,2])/incident),
        reference_period_doubling_relative_l2=max(accuracy_period_error,field_error(exact,doubled,g)),initial_secondary_field_norm_fraction=float(tail),initial_pec_clipping_field_norm_fraction=float(clip_fraction),analytic_cap_tangential_electric_max=cap,
        reference_period=p['reference_period'],spectrum_kmin=float(spectrum(p,c)[0][0]),spectrum_kmax=float(spectrum(p,c)[0][-1]))
    return row,history,(g['xh'],state[0],exact[0]),np.column_stack([times,signals,an,f,fa])
