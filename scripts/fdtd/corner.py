"""Original four-side/corner Berenger TMz PML and controlled modal references.

Ex/Ey split Ez; Hx/Hy live at Yee half cells and half times. Every outer
edge is PEC. The finite standing Fourier packet excites four directions.
"""
import math
import numpy as np


def geometry(n, length, dt, thickness=2., strength=20., order=3):
    if isinstance(n,bool) or not isinstance(n,int) or n<8:
        raise ValueError('integer grid size >=8 required')
    if not all(math.isfinite(v) and v>0 for v in [length,dt]):
        raise ValueError('finite positive length/time required')
    if not 0<=thickness<length/2 or not math.isfinite(strength) or strength<0:
        raise ValueError('invalid matched layer')
    if not isinstance(order,int) or order<1:raise ValueError('invalid profile order')
    dx=length/n
    if dt*np.sqrt(2)/dx>=1:raise ValueError('strict Yee CFL required')
    if thickness and abs(thickness/dx-round(thickness/dx))>1e-10:
        raise ValueError('layer faces must align with electric nodes')
    x=np.arange(n+1)*dx;xh=(np.arange(n)+.5)*dx
    def gamma(z):
        if thickness==0:return np.zeros_like(z)
        depth=np.maximum(np.maximum(thickness-z,z-(length-thickness)),0)/thickness
        return strength*depth**order
    return dict(n=n,length=length,dx=dx,dy=dx,dt=dt,x=x,xh=xh,
                gx=gamma(x)[:,None],gy=gamma(x)[None,:],
                gxh=gamma(xh)[:,None],gyh=gamma(xh)[None,:],
                thickness=thickness,strength=strength,order=order)


def weights(g, component):
    cache=g.setdefault('_weights',{})
    if component in cache:return cache[component]
    n=g['n'];wx=np.ones(n if component=='hy' else n+1)
    wy=np.ones(n if component=='hx' else n+1)
    if component!='hy':wx[[0,-1]]*=.5
    if component!='hx':wy[[0,-1]]*=.5
    cache[component]=wx[:,None]*wy[None,:]*g['dx']**2
    return cache[component]


def magnetic(e,hx,hy,g):
    dt=g['dt'];dx=g['dx'];ax=.5*dt*g['gyh'];ay=.5*dt*g['gxh']
    xp=((1-ax)*hx-dt*np.diff(e,axis=1)/dx)/(1+ax)
    yp=((1-ay)*hy+dt*np.diff(e,axis=0)/dx)/(1+ay)
    return xp,yp


def step(state,g):
    ex,ey,hx,hy=state;e=ex+ey;xp,yp=magnetic(e,hx,hy,g)
    xn=np.zeros_like(ex);yn=np.zeros_like(ey);dt=g['dt'];dx=g['dx']
    ax=.5*dt*g['gx'][1:-1];ay=.5*dt*g['gy'][:,1:-1]
    xn[1:-1,1:-1]=((1-ax)*ex[1:-1,1:-1]+dt*np.diff(yp,axis=0)[:,1:-1]/dx)/(1+ax)
    yn[1:-1,1:-1]=((1-ay)*ey[1:-1,1:-1]-dt*np.diff(xp,axis=1)[1:-1,:]/dx)/(1+ay)
    return xn,yn,xp,yp


def energy(state,g):
    ex,ey,hx,hy=state;e=ex+ey;xp,yp=magnetic(e,hx,hy,g)
    we,wx,wy=(weights(g,c) for c in ['e','hx','hy'])
    u=.5*(np.sum(e*e*we)+np.sum(hx*xp*wx)+np.sum(hy*yp*wy))
    v=.5*(np.sum(e*e*we)+np.sum((.5*(hx+xp))**2*wx)+np.sum((.5*(hy+yp))**2*wy))
    return float(u),float(v)


def work_densities(old,new,g):
    ex,ey,hx,hy=old;en,yn,xp,yp=new;dt=g['dt']
    xpp,ypp=magnetic(en+yn,xp,yp,g)
    ebar=.5*(ex+ey+en+yn)
    electric_x=dt*ebar*g['gx']*.5*(ex+en)*weights(g,'e')
    electric_y=dt*ebar*g['gy']*.5*(ey+yn)*weights(g,'e')
    mx=.5*dt*xp*g['gyh']*(.5*(hx+xp)+.5*(xp+xpp))*weights(g,'hx')
    my=.5*dt*yp*g['gxh']*(.5*(hy+yp)+.5*(yp+ypp))*weights(g,'hy')
    return electric_x,electric_y,mx,my


def corner_sums(densities,g):
    d=g['thickness'];L=g['length'];x=g['x'];xh=g['xh']
    result={}
    for name,sx,sy in [('SW',False,False),('SE',True,False),('NW',False,True),('NE',True,True)]:
        total=0.
        for z,c in zip(densities,['e','e','hx','hy']):
            xx=xh if c=='hy' else x;yy=xh if c=='hx' else x
            xm=xx>L-d if sx else xx<d;ym=yy>L-d if sy else yy<d
            total+=float(np.sum(z*xm[:,None]*ym[None,:]))
        result[name]=total
    return result


def physical_energy_and_flux(state,g):
    ex,ey,hx,hy=state;e=ex+ey;xp,yp=magnetic(e,hx,hy,g)
    hxc=.5*(hx+xp);hyc=.5*(hy+yp);n=g['n'];d=g['thickness'];dx=g['dx']
    lo=int(round(d/dx));hi=n-lo
    if lo<1:raise ValueError('physical flux requires nonzero aligned layers')
    axis=np.zeros(n+1);axis[lo:hi+1]=1;axis[[lo,hi]]*=.5
    halves=np.zeros(n);halves[lo:hi]=1
    u=.5*dx*dx*(np.sum(e*e*axis[:,None]*axis[None,:])+
         np.sum(hxc*hxc*axis[:,None]*halves[None,:])+
         np.sum(hyc*hyc*halves[:,None]*axis[None,:]))
    wx=axis[lo:hi+1]
    sxlo=-e[lo,lo:hi+1]*.5*(hyc[lo-1,lo:hi+1]+hyc[lo,lo:hi+1])
    sxhi=-e[hi,lo:hi+1]*.5*(hyc[hi-1,lo:hi+1]+hyc[hi,lo:hi+1])
    sylo=e[lo:hi+1,lo]*.5*(hxc[lo:hi+1,lo-1]+hxc[lo:hi+1,lo])
    syhi=e[lo:hi+1,hi]*.5*(hxc[lo:hi+1,hi-1]+hxc[lo:hi+1,hi])
    flux=dict(left=float(-dx*np.dot(wx,sxlo)),right=float(dx*np.dot(wx,sxhi)),
              bottom=float(-dx*np.dot(wx,sylo)),top=float(dx*np.dot(wx,syhi)))
    return float(u),flux


def positive_densities(state,g):
    ex,ey,hx,hy=state;xp,yp=magnetic(ex+ey,hx,hy,g)
    return (.5*(ex+ey)**2*weights(g,'e'),.5*(.5*(hx+xp))**2*weights(g,'hx'),
            .5*(.5*(hy+yp))**2*weights(g,'hy'))


def initial_tail_diagnostics(state,unclipped,g):
    d=g['thickness'];L=g['length'];outside_energy=0.
    for z,c in zip(positive_densities(state,g),['e','hx','hy']):
        x=g['xh'] if c=='hy' else g['x'];y=g['xh'] if c=='hx' else g['x']
        mx=((x>d)&(x<L-d)).astype(float);my=((y>d)&(y<L-d)).astype(float)
        mx[np.isclose(x,d)|np.isclose(x,L-d)]=.5
        my[np.isclose(y,d)|np.isclose(y,L-d)]=.5
        outside_energy+=float(np.sum(z*(1-mx[:,None]*my[None,:])))
    e=unclipped[0]+unclipped[1];x=g['x'];mask=(x<d)|(x>L-d)
    capmax=max(np.max(np.abs(e[[0,-1]])),np.max(np.abs(e[:,[0,-1]])))
    layermax=max(np.max(np.abs(e[mask])),np.max(np.abs(e[:,mask])))
    splitmax=max(np.max(np.abs(a[mask])) for a in unclipped[:2])
    splitmax=max(splitmax,max(np.max(np.abs(a[:,mask])) for a in unclipped[:2]))
    halves=(g['xh']<d)|(g['xh']>L-d)
    hmax=max(np.max(np.abs(unclipped[2][mask])),np.max(np.abs(unclipped[2][:,halves])),
             np.max(np.abs(unclipped[3][halves])),np.max(np.abs(unclipped[3][:,mask])))
    return outside_energy,float(capmax),float(layermax),float(splitmax),float(hmax)


def spectrum(p,family,period=None):
    """A finite continuum cosine sum, not a Gaussian quadrature assertion."""
    period=p['reference_period'] if period is None else period
    dk=2*np.pi/period
    cutoff=p['spectral_cutoff'];k=np.arange(int(round(cutoff/dk))+1)*dk
    k0=p['axis_carrier'] if family=='axis' else p['diagonal_carrier'];w=p['width']
    centers=[(k0,0),(-k0,0),(0,k0),(0,-k0)] if family=='axis' else [(a*k0,b*k0) for a in [-1,1] for b in [-1,1]]
    c=sum(np.exp(-.5*w*w*((k[:,None]-a)**2+(k[None,:]-b)**2)) for a,b in centers)
    mult=np.full(len(k),2.);mult[0]=1
    c*=mult[:,None]*mult[None,:];c[0,0]=0;c/=c.sum()
    return k,c


def frequencies(k,g,discrete):
    if discrete:
        sx=2*np.sin(k*g['dx']/2)/g['dx'];q=np.hypot(sx[:,None],sx[None,:])
        # Modes above a coarse grid's Nyquist are absent from the fixed spectrum.
        omega=2*np.arcsin(.5*g['dt']*q)/g['dt']
        return sx,q,omega
    return k,np.hypot(k[:,None],k[None,:]),np.hypot(k[:,None],k[None,:])


def packet(g,p,family,electric_time,magnetic_time,discrete=False,period=None,clip=True):
    k,c=spectrum(p,family,period);s,q,omega=frequencies(k,g,discrete)
    inv=np.divide(1.,q,out=np.zeros_like(q),where=q>0)
    center=p['center'];x=g['x']-center;xh=g['xh']-center
    cx=np.cos(x[:,None]*k);sx=np.sin(xh[:,None]*k)
    cy=cx;sy=sx
    phase=np.cos(omega*electric_time)
    def product(a,b,z):
        return np.einsum('ij,jk->ik',np.einsum('ij,jk->ik',a,b,optimize=False),z,optimize=False)
    ex=product(cx,c*phase*(s[:,None]*inv)**2,cy.T)
    ey=product(cx,c*phase*(s[None,:]*inv)**2,cy.T)
    hphase=np.sin(omega*magnetic_time)
    hx=product(cx,c*hphase*s[None,:]*inv,sy.T)
    hy=-product(sx,c*hphase*s[:,None]*inv,cy.T)
    if clip:
        ex[[0,-1]]=0;ex[:,[0,-1]]=0;ey[[0,-1]]=0;ey[:,[0,-1]]=0
        hx[[0,-1]]=0;hy[:,[0,-1]]=0
    return ex,ey,hx,hy


def probes(p,family):
    c=p['center'];a=p['probe_offset']
    return np.array([(c-a,c),(c+a,c),(c,c-a),(c,c+a)] if family=='axis' else
                    [(c-a,c-a),(c+a,c-a),(c-a,c+a),(c+a,c+a)])


def modal_trace(g,p,family,times,discrete=True,period=None):
    k,c=spectrum(p,family,period);_,_,omega=frequencies(k,g,discrete)
    xy=probes(p,family)-p['center'];coeff=np.array([c*np.cos(k[:,None]*x)*np.cos(k[None,:]*y) for x,y in xy]).reshape(4,-1)
    dt=times[1]-times[0];osc=2*np.cos(omega.ravel()*dt);previous=np.cos(omega.ravel()*(times[0]-dt));current=np.cos(omega.ravel()*times[0]);out=[]
    for _ in times:
        out.append(coeff@current)
        previous,current=current,osc*current-previous
    return np.asarray(out)


def run_mesh(p,family,n,steps,zero_initial_layer=False):
    L=p['length'];dt=p['end_time']/steps
    g=geometry(n,L,dt,p['pml_thickness'],p['pml_strength'],p['pml_order'])
    initial_unclipped=packet(g,p,family,0,-dt/2,True,clip=False)
    state=tuple(a.copy() for a in initial_unclipped)
    state[0][[0,-1]]=0;state[0][:,[0,-1]]=0;state[1][[0,-1]]=0;state[1][:,[0,-1]]=0
    state[2][[0,-1]]=0;state[3][:,[0,-1]]=0
    if zero_initial_layer:
        d=g['thickness'];L=g['length']
        for a,component in zip(state,['e','e','hx','hy']):
            xx=g['xh'] if component=='hy' else g['x'];yy=g['xh'] if component=='hx' else g['x']
            a[(xx<d)|(xx>L-d),:]=0;a[:,(yy<d)|(yy>L-d)]=0
    times=np.arange(steps+1)*dt
    reference=modal_trace(g,p,family,times,True)
    continuum=modal_trace(g,p,family,times,False)
    incident=np.max(np.sqrt(np.mean(continuum[times<p['gate_start']]**2,axis=1)))
    ids=np.rint(probes(p,family)/g['dx']).astype(int)
    u0,v0=energy(state,g);interior0,_=physical_energy_and_flux(state,g)
    tail,capmax,layermax,splitmax,hmax=initial_tail_diagnostics(state,initial_unclipped,g);layer0=tail/v0
    we=wh=0.;corner={q:0. for q in ['SW','SE','NW','NE']};corner_abs=corner.copy();outflux={q:0. for q in ['left','right','bottom','top']}
    last_flux=None;budget=flux_budget=0.;history=[];returned=[];max_corner_field=corner.copy();snapshot=None;field_error=None
    direction_work=dict(electric_x=0.,electric_y=0.,magnetic_x=0.,magnetic_y=0.)
    early_step=int(round(p['accuracy_time']/dt))
    for j,t in enumerate(times):
        u,v=energy(state,g);interior,flux=physical_energy_and_flux(state,g)
        if last_flux is not None:
            for q in outflux:outflux[q]+=.5*dt*(last_flux[q]+flux[q])
        last_flux=flux
        budget=max(budget,abs(u+we+wh-u0)/u0)
        flux_budget=max(flux_budget,abs(interior+sum(outflux.values())-interior0)/interior0)
        e=state[0]+state[1];values=e[ids[:,0],ids[:,1]];returned.append(values-reference[j])
        history.append([n,family,t,u,v,we,wh,interior,*outflux.values()])
        m=int(round(p['pml_thickness']/g['dx']))
        for q,z in [('SW',e[:m,:m]),('SE',e[-m:,:m]),('NW',e[:m,-m:]),('NE',e[-m:,-m:])]:max_corner_field[q]=max(max_corner_field[q],float(np.max(np.abs(z))))
        if j==early_step:
            analytic=packet(g,p,family,t,t-dt/2,False)
            er=analytic[0]+analytic[1];x=state[0]+state[1]
            norm=sum(np.sum(a*a*weights(g,c)) for a,c in zip([er,analytic[2],analytic[3]],['e','hx','hy']))
            err=sum(np.sum((a-b)**2*weights(g,c)) for a,b,c in zip([x,state[2],state[3]],[er,analytic[2],analytic[3]],['e','hx','hy']))
            field_error=float(np.sqrt(err/norm));snapshot=(e.copy(),er.copy(),g)
        if j<steps:
            new=step(state,g);densities=work_densities(state,new,g)
            for name,z in zip(direction_work,densities):direction_work[name]+=float(np.sum(z))
            we+=float(np.sum(densities[0])+np.sum(densities[1]));wh+=float(np.sum(densities[2])+np.sum(densities[3]))
            for q,value in corner_sums(densities,g).items():corner[q]+=value;corner_abs[q]+=abs(value)
            state=new
    returned=np.asarray(returned);gate=times>=p['gate_start']
    norms=np.sqrt(np.mean(returned**2,axis=1))/incident
    gated_ids=np.where(gate)[0];gated_peak=gated_ids[np.argmax(norms[gate])];global_peak=int(np.argmax(norms))
    row=dict(family=family,nx=n,ny=n,dx=g['dx'],dt=dt,steps=steps,
        early_field_relative_l2=field_error,reflection_amplitude_ratio=float(norms[gated_peak]),
        return_peak_time=float(times[gated_peak]),global_return_peak_time=float(times[global_peak]),
        global_return_amplitude_ratio=float(norms[global_peak]),excluded_early_return_peak_ratio=float(np.max(norms[~gate])),
        incident_probe_reference_peak=float(incident),modified_energy_budget_relative_residual=float(budget),
        physical_flux_budget_relative_residual=float(flux_budget),total_pml_work_fraction=float((we+wh)/u0),
        remaining_physical_energy_fraction=float(energy(state,g)[1]/v0),initial_layer_energy_fraction=float(layer0),
        initial_unclipped_cap_electric_field_max=capmax,initial_layer_electric_field_max=layermax,
        initial_layer_split_electric_field_max=splitmax,initial_layer_magnetic_field_max=hmax,
        directional_work_fractions={q:v/u0 for q,v in direction_work.items()},
        pml_thickness=p['pml_thickness'],pml_strength=p['pml_strength'],pml_cells=int(round(p['pml_thickness']/g['dx'])),
        corner_work_fractions={q:value/u0 for q,value in corner.items()},corner_abs_work_fractions={q:value/u0 for q,value in corner_abs.items()},
        corner_max_electric_fields=max_corner_field,side_flux_fractions={q:value/interior0 for q,value in outflux.items()},
        reference_period=p['reference_period'],spectrum_mode_count=int(spectrum(p,family)[1].size),
        spectrum_kmax=float(spectrum(p,family)[0][-1]),spectrum_dk=float(2*np.pi/p['reference_period']),accuracy_time=float(times[early_step]))
    return row,history,snapshot,np.column_stack([times,returned/incident]),g
