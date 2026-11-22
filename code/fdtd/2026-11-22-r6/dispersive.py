"""Original 1D normal-incidence Yee / implicit-midpoint passive Lorentz ADE.

Units c=epsilon0=mu0=1. Complex fields represent two real quadratures;
all energies are sums of their real-field energies. E,P,J are at integer
nodes/times, H at cell centers and half times. PEC caps are not absorbers.
No outgoing field or Fresnel coefficient enters the time update.
"""
import math
import numpy as np


def material(omega, c):
    w=np.asarray(omega,dtype=float)
    if np.any(w<=0):raise ValueError('strictly positive frequencies required')
    f=c['delta_epsilon']*c['omega0']**2
    susceptibility=f/(c['omega0']**2-w*w-1j*c['gamma']*w) if f else np.zeros_like(w,dtype=complex)
    return c['epsilon_inf']+susceptibility+1j*c['sigma']/w


def slab(omega,c):
    w=np.asarray(omega,dtype=float);eps=material(w,c);n=np.sqrt(eps+0j);q=w*n;d=c['slab'][1]-c['slab'][0]
    rho=(1-n)/(1+n);z=np.exp(2j*q*d);den=1-rho*rho*z
    r=rho*(1-z)/den;t=(1-rho*rho)*np.exp(1j*q*d)/den
    a=(1+rho)/den;b=-rho*a*z
    return dict(epsilon=eps,n=n,q=q,r=r,t=t,a=a,b=b,R=abs(r)**2,T=abs(t)**2,A=1-abs(r)**2-abs(t)**2)


def direct_spectral_absorption(omega,c,points=128):
    """Independent volume integral of Ohmic + oscillator damping, not 1-R-T."""
    w=np.asarray(omega);z=slab(w,c);d=c['slab'][1]-c['slab'][0]
    if isinstance(points,bool) or not isinstance(points,int) or points<32 or points%32:raise ValueError('quadrature budget must be a positive multiple of 32')
    # Composite moderate-order Gauss avoids the weight roundoff of one
    # unnecessarily high-order rule near the lossy resonance.
    panels=points//32;nodes,weights=np.polynomial.legendre.leggauss(32)
    x=np.concatenate([(nodes+1)*d/(2*panels)+i*d/panels for i in range(panels)])
    weight=np.tile(weights*d/(2*panels),panels)
    e=z['a'][:,None]*np.exp(1j*z['q'][:,None]*x)+z['b'][:,None]*np.exp(-1j*z['q'][:,None]*x)
    f=c['delta_epsilon']*c['omega0']**2
    loss=c['sigma']+(c['gamma']*w*w*f/abs(c['omega0']**2-w*w-1j*c['gamma']*w)**2 if f else np.zeros_like(w))
    return loss*np.sum(abs(e)**2*weight,axis=1)


def spectrum(p,c,period=None):
    period=period or p['reference_period'];dw=2*np.pi/period
    w=np.arange(1,int(c['spectrum_max']/dw)+1)*dw
    a=c['width']/np.sqrt(2*np.pi)*np.exp(-.5*c['width']**2*(w-c['carrier'])**2)*dw
    return w,a


def geometry(nx,c,dt):
    if isinstance(nx,bool) or not isinstance(nx,int) or nx<8:raise ValueError('integer nx>=8 required')
    keys=['length','epsilon_inf','omega0'];positive=[c[k] for k in keys]+[dt]
    if not all(math.isfinite(v) and v>0 for v in positive):raise ValueError('finite positive geometry/material parameters required')
    if not all(math.isfinite(c[k]) and c[k]>=0 for k in ['sigma','delta_epsilon','gamma']):raise ValueError('passive material required')
    dx=c['length']/nx
    if not dt/dx<min(1.,np.sqrt(c['epsilon_inf'])):raise ValueError('strict epsilon-infinity Yee CFL required')
    lo,hi=c['slab']
    if not 0<lo<hi<c['length'] or any(abs(v/dx-round(v/dx))>1e-8 for v in [lo,hi]):raise ValueError('aligned interior slab required')
    x=np.arange(nx+1)*dx;xh=(np.arange(nx)+.5)*dx;fraction=((x>lo)&(x<hi)).astype(float);fraction[int(round(lo/dx))]=.5;fraction[int(round(hi/dx))]=.5
    eps=1+fraction*(c['epsilon_inf']-1);sigma=fraction*c['sigma'];f=fraction*c['delta_epsilon']*c['omega0']**2
    a=dt/2;b=1+a*c['gamma']+a*a*c['omega0']**2
    return dict(nx=nx,dx=dx,dt=dt,x=x,xh=xh,eps=eps,sigma=sigma,f=f,w0=c['omega0'],gamma=c['gamma'],a=a,b=b,den=eps/a+sigma+a*f/b)


def magnetic(e,h,g):return h+g['dt']/g['dx']*np.diff(e)


def step(state,g):
    e,h,p,j=state;hp=magnetic(e,h,g);curl=np.zeros_like(e);curl[1:-1]=np.diff(hp)/g['dx'];a=g['a'];b=g['b']
    free=np.where(g['f']>0,(j-a*g['w0']**2*p)/b,0)
    eb=(g['eps']/a*e+curl-free)/g['den'];eb[[0,-1]]=0
    jb=free+a*g['f']/b*eb
    en=2*eb-e;pn=np.where(g['f']>0,p+g['dt']*jb,0);jn=np.where(g['f']>0,2*jb-j,0)
    return en,hp,pn,jn


def integral(values,g,mask=None):
    z=np.asarray(values).copy()
    if mask is not None:z=z*mask
    z[[0,-1]]*=.5
    return float(np.sum(z)*g['dx'])


def oscillator_density(p,j,g):
    return np.divide(abs(j)**2+g['w0']**2*abs(p)**2,2*g['f'],out=np.zeros_like(g['f']),where=g['f']>0)


def energy(state,g,region=None):
    e,h,p,j=state;hp=magnetic(e,h,g);hc=(h+hp)/2
    emask=np.ones(e.shape);hmask=np.ones(h.shape)
    if region is not None:
        lo,hi=region;emask=((g['x']>=lo)&(g['x']<=hi)).astype(float);emask[int(round(lo/g['dx']))]*=.5;emask[int(round(hi/g['dx']))]*=.5;hmask=((g['xh']>lo)&(g['xh']<hi)).astype(float)
    electric=.5*integral(g['eps']*abs(e)**2,g,emask);polarization=integral(oscillator_density(p,j,g),g,emask)
    modified=electric+polarization+.5*g['dx']*float(np.sum(np.real(np.conj(h)*hp)*hmask))
    physical=electric+polarization+.5*g['dx']*float(np.sum(abs(hc)**2*hmask))
    return modified,physical,polarization


def work(old,new,g):
    eb=(old[0]+new[0])/2;jb=(old[3]+new[3])/2
    ohmic=g['dt']*integral(g['sigma']*abs(eb)**2,g)
    damping=g['dt']*integral(np.divide(g['gamma']*abs(jb)**2,g['f'],out=np.zeros_like(g['f']),where=g['f']>0),g)
    return ohmic,damping


def monitor(state,g,x):
    i=int(round(x/g['dx']));e,h,_,_=state;hp=magnetic(e,h,g);hc=(h+hp)/2
    return e[i],(hc[i-1]+hc[i])/2


def packet(x,t,p,c,component='e',period=None):
    """Continuum Fourier synthesis including causal passive slab transfer."""
    x=np.asarray(x);w,amp=spectrum(p,c,period);z=slab(w,c);lo,hi=c['slab'];base=np.exp(1j*w*(lo-c['center'])-1j*w*t)*amp;out=np.empty(x.shape,complex)
    left=x<lo;right=x>hi;inside=~(left|right)
    if np.any(left):
        inc=np.exp(1j*(x[left,None]-lo)*w)*base;ref=np.exp(-1j*(x[left,None]-lo)*w)*(base*z['r'])
        out[left]=np.sum(inc+ref if component=='e' else -inc+ref,axis=1)
    if np.any(right):
        v=np.sum(np.exp(1j*(x[right,None]-hi)*w)*(base*z['t']),axis=1);out[right]=v if component=='e' else -v
    if np.any(inside):
        forward=np.exp(1j*(x[inside,None]-lo)*z['q'])*(base*z['a']);back=np.exp(-1j*(x[inside,None]-lo)*z['q'])*(base*z['b'])
        out[inside]=np.sum(forward+back if component=='e' else -z['n']*(forward-back),axis=1)
    return out


def initial(g,p,c):
    w,amp=spectrum(p,c);wn=2/g['dt']*np.arcsin(g['dt']/g['dx']*np.sin(w*g['dx']/2))
    e=np.sum(np.exp(1j*(g['x'][:,None]-c['center'])*w)*amp,axis=1)
    h=-np.sum(np.exp(1j*(g['xh'][:,None]-c['center'])*w+1j*wn*g['dt']/2)*amp,axis=1)
    e[[0,-1]]=0
    return e,h,np.zeros_like(e),np.zeros_like(e)


def packet_material(x,t,p,c):
    """Continuum nodal volume-averaged P/J; half material at slab faces."""
    x=np.asarray(x);pol=np.zeros(x.shape,complex);current=pol.copy();lo,hi=c['slab'];inside=(x>=lo)&(x<=hi)
    if c['delta_epsilon']==0:return pol,current
    w,amp=spectrum(p,c);z=slab(w,c);xx=x[inside,None]-lo;phase=np.exp(1j*w*(lo-c['center'])-1j*w*t)*amp
    emode=(z['a']*np.exp(1j*xx*z['q'])+z['b']*np.exp(-1j*xx*z['q']))*phase
    chi=c['delta_epsilon']*c['omega0']**2/(c['omega0']**2-w*w-1j*c['gamma']*w)
    fraction=np.where((x[inside]==lo)|(x[inside]==hi),.5,1.)
    pol[inside]=fraction*np.sum(chi*emode,axis=1);current[inside]=fraction*np.sum(-1j*w*chi*emode,axis=1)
    return pol,current


def initial_tail_controls(g,p,c):
    w,amp=spectrum(p,c);incident=np.sum(np.exp(1j*(g['x'][:,None]-c['center'])*w)*amp,axis=1)
    hin=-np.sum(np.exp(1j*(g['xh'][:,None]-c['center'])*w+1j*w*g['dt']/2)*amp,axis=1)
    pol,j=packet_material(g['x'],0.,p,c);exact_energy=p['reference_period']*np.sum(amp*amp)
    return dict(initial_secondary_E_relative_l2=float(np.linalg.norm(packet(g['x'],0.,p,c)-incident)/np.linalg.norm(incident)),initial_secondary_H_relative_l2=float(np.linalg.norm(packet(g['xh'],-g['dt']/2,p,c,'h')-hin)/np.linalg.norm(hin)),initial_omitted_material_energy_fraction=integral(oscillator_density(pol,j,g),g)/exact_energy)


def clock(p,c,nx,factor=1):
    base=c['meshes'][0];quantum=c['time_quantum'];nquant=int(round(c['end_time']/quantum));minimum=quantum/(p['courant']*c['length']/base)
    nbase=int(np.ceil(minimum));n=int(nbase*(nx//base)*factor*nquant)
    return n,c['end_time']/n


def trapezoid(y,t):return float(np.trapezoid(y,t))


def reference_signals(times,p,c,period=None):
    w,a=spectrum(p,c,period);z=slab(w,c);lo,hi=c['slab'];xl,xr=c['monitors'];phase=np.exp(-1j*times[:,None]*w)
    inc=np.sum(phase*(a*np.exp(1j*w*(xl-c['center']))),axis=1)
    ref=np.sum(phase*(a*z['r']*np.exp(1j*w*(2*lo-xl-c['center']))),axis=1)
    trans=np.sum(phase*(a*z['t']*np.exp(1j*w*(lo+xr-hi-c['center']))),axis=1)
    return inc,ref,trans


def dft(y,t,w):return np.trapezoid(y*np.exp(1j*w*t),t)


def coefficients(signals,t,c,k):
    inc,ref,trans,base_right=signals;lo,hi=c['slab'];xl,_=c['monitors'];omega=c['carrier']
    r=dft(ref,t,omega)/dft(inc,t,omega)*np.exp(-2j*k*(lo-xl))
    z=dft(trans,t,omega)/dft(base_right,t,omega)*np.exp(1j*k*(hi-lo))
    return r,z


def run_mesh(p,c,nx,time_factor=1,keep=True):
    steps,dt=clock(p,c,nx,time_factor);g=geometry(nx,c,dt);vac=dict(c,epsilon_inf=1.,sigma=0.,delta_epsilon=0.);gv=geometry(nx,vac,dt)
    s=initial(g,p,c);v=initial(gv,p,c);u0,phys0,_=energy(s,g);r0=energy(s,g,c['monitors'])[1]
    initial_secondary=float(np.linalg.norm(s[0][g['x']>=c['slab'][0]])/np.linalg.norm(s[0]));times=np.arange(steps+1)*dt
    wave=np.empty((steps+1,9),complex);history=[];ws=wg=0.;drift=physical_drift=0.;snapshot=None
    accuracy_step=int(round(c['accuracy_time']/dt));region=np.empty(steps+1);worksum=np.empty(steps+1);matenergy=np.empty(steps+1)
    for n,t in enumerate(times):
        u,physical,polarization=energy(s,g);region[n]=energy(s,g,c['monitors'])[1];worksum[n]=ws+wg;matenergy[n]=polarization
        drift=max(drift,abs(u+ws+wg-u0)/u0);physical_drift=max(physical_drift,abs(physical+ws+wg-phys0)/u0)
        el,hl=monitor(s,g,c['monitors'][0]);er,hr=monitor(s,g,c['monitors'][1]);il,ih=monitor(v,gv,c['monitors'][0]);ir,irh=monitor(v,gv,c['monitors'][1])
        wave[n]=[t,il,ih,el-il,hl-ih,er,hr,ir,irh]
        if keep:history.append([c['id'],nx,t,u,physical,polarization,region[n],ws,wg,0.,0.])
        if n==accuracy_step:snapshot=(g['x'].copy(),s[0].copy(),packet(g['x'],t,p,c),s[2].copy(),s[3].copy())
        if n<steps:
            sn=step(s,g);a,b=work(s,sn,g)
            if keep:history[-1][-2:]=[a/dt,b/dt]
            ws+=a;wg+=b;s=sn;v=step(v,gv)
    incflux=-np.real(wave[:,1]*np.conj(wave[:,2]));refflux=np.real(wave[:,3]*np.conj(wave[:,4]));transflux=-np.real(wave[:,5]*np.conj(wave[:,6]));totalleft=-np.real((wave[:,1]+wave[:,3])*np.conj(wave[:,2]+wave[:,4]))
    incoming=trapezoid(incflux,times);R=trapezoid(refflux,times)/incoming;T=trapezoid(transflux,times)/incoming;A=(ws+wg)/incoming
    net=transflux-totalleft;flux=np.concatenate([[0.],np.cumsum((net[1:]+net[:-1])*dt/2)]);budget=region-r0+worksum+flux
    w,a=spectrum(p,c);z=slab(w,c);weights=a*a;analytic=np.array([np.sum(weights*z[k])/np.sum(weights) for k in ['R','T','A']]);exact_energy=p['reference_period']*np.sum(a*a)
    refs=reference_signals(times,p,c);refinc,refref,reftrans=refs;reference_fractions=np.array([trapezoid(abs(q)**2,times)/exact_energy for q in [refinc,refref,reftrans]])
    base_right=np.sum(np.exp(-1j*times[:,None]*w)*(a*np.exp(1j*w*(c['monitors'][1]-c['center']))),axis=1)
    rr,tt=coefficients([refinc,refref,reftrans,base_right],times,c,c['carrier'])
    k=2/g['dx']*np.arcsin(g['dx']/dt*np.sin(c['carrier']*dt/2));rn,tn=coefficients([wave[:,1],wave[:,3],wave[:,5],wave[:,7]],times,c,k);carrier=slab(np.array([c['carrier']]),c)
    x,e,eref,pol,j=snapshot;field=float(np.linalg.norm(e-eref)/np.linalg.norm(eref));ref2=packet(x,c['accuracy_time'],p,c,period=2*p['reference_period'])
    pref,jref=packet_material(x,c['accuracy_time'],p,c)
    material_errors=dict(polarization_relative_l2=float(np.linalg.norm(pol-pref)/np.linalg.norm(pref)) if np.linalg.norm(pref)>0 else 0.,current_relative_l2=float(np.linalg.norm(j-jref)/np.linalg.norm(jref)) if np.linalg.norm(jref)>0 else 0.)
    caps=np.array([packet(np.array([0.,c['length']]),t,p,c) for t in np.linspace(0,c['end_time'],257)])
    row=dict(subcase=c['id'],nx=nx,dx=g['dx'],dt=dt,steps=steps,accuracy_time=c['accuracy_time'],field_relative_l2=field,analytic_R=float(analytic[0]),analytic_T=float(analytic[1]),analytic_A=float(analytic[2]),reflection_fraction=R,transmission_fraction=T,absorption_direct_fraction=A,ohmic_absorption_fraction=ws/incoming,lorentz_absorption_fraction=wg/incoming,reflection_error=abs(R-analytic[0]),transmission_error=abs(T-analytic[1]),absorption_error=abs(A-analytic[2]),energy_fraction_closure=abs(R+T+A-1),modified_energy_max_relative_balance=drift,physical_energy_max_relative_balance=physical_drift,physical_flux_budget_max_relative_residual=float(np.max(abs(budget))/incoming),final_material_energy_fraction=float(matenergy[-1]/incoming),peak_material_energy_fraction=float(np.max(matenergy)/incoming),final_region_energy_fraction=float(region[-1]/incoming),incident_fluence_energy_relative_error=abs(incoming/exact_energy-1),reference_window_fluence_gap=float(max(abs(reference_fractions[0]-1),abs(reference_fractions[1]-analytic[0]),abs(reference_fractions[2]-analytic[1]))),reference_dft_r_error=float(abs(rr-carrier['r'][0])),reference_dft_t_error=float(abs(tt-carrier['t'][0])),complex_r_error=float(abs(rn-rr)),complex_t_error=float(abs(tn-tt)),carrier_complex_r_error=float(abs(rn-carrier['r'][0])),carrier_complex_t_error=float(abs(tn-carrier['t'][0])),numerical_r_real=float(rn.real),numerical_r_imag=float(rn.imag),numerical_t_real=float(tn.real),numerical_t_imag=float(tn.imag),analytic_carrier_r_real=float(carrier['r'][0].real),analytic_carrier_r_imag=float(carrier['r'][0].imag),analytic_carrier_t_real=float(carrier['t'][0].real),analytic_carrier_t_imag=float(carrier['t'][0].imag),reference_period_doubling_relative_l2=float(np.linalg.norm(ref2-eref)/np.linalg.norm(ref2)),analytic_cap_electric_max=float(np.max(abs(caps))),initial_secondary_field_norm_fraction=initial_secondary)
    row.update(initial_tail_controls(g,p,c));row.update(material_errors)
    row.update(initial_region_energy_fraction=r0/incoming,finite_window_energy_fraction_residual=abs(R+T+A+(region[-1]-r0)/incoming-1))
    waves=np.column_stack([wave,refinc,refref,reftrans,base_right,incflux,refflux,transflux,budget/incoming,matenergy/incoming])
    return row,history,snapshot,waves,s
