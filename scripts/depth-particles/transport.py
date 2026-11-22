"""Small original CIC-PIC, homogeneous Maxwell DSMC and absorption-S_N solvers."""
from math import pi
import numpy as np
from scipy.special import expn, gammainc
from scipy.stats import kstest


def poisson(rho,length):
    rho=np.asarray(rho,dtype=float)
    if rho.ndim!=1 or len(rho)<4 or not np.isfinite(rho).all() or not np.isfinite(length) or length<=0:
        raise ValueError('Finite one-dimensional periodic grid required')
    n=len(rho)
    compatibility=128*np.finfo(float).eps*max(1.,float(np.max(abs(rho))))
    if abs(float(np.mean(rho)))>compatibility:
        raise ValueError('Periodic Poisson requires zero-mean charge density')
    modes=2*pi*np.fft.fftfreq(n,d=length/n);r=np.fft.fft(rho);phi=np.zeros(n,complex)
    active=modes!=0;phi[active]=r[active]/modes[active]**2
    electric=-1j*modes*phi
    if n%2==0:electric[n//2]=0.  # Real skew-adjoint derivative has zero Nyquist mode.
    residual=np.max(np.abs((modes*modes*phi-r)[active]))/n
    return np.fft.ifft(electric).real,float(residual)


def cic_deposit(x,weight,n,length):
    if n<4 or length<=0 or weight<=0 or not np.isfinite(x).all():raise ValueError('Invalid CIC inputs')
    u=np.asarray(x)%length*n/length;j=np.floor(u).astype(int);f=u-j
    electrons=(np.bincount(j,weights=1-f,minlength=n)+np.bincount((j+1)%n,weights=f,minlength=n))*weight/(length/n)
    return 1.-electrons


def cic_gather(field,x,length):
    n=len(field);u=np.asarray(x)%length*n/length;j=np.floor(u).astype(int);f=u-j
    return (1-f)*field[j]+f*field[(j+1)%n]


def cold_plasma(n=128,ppc=16,dt=.02,end_time=2*pi,amplitude=.001):
    if not 0<amplitude<.01 or ppc<2 or dt<=0 or end_time<=0:raise ValueError('Small-amplitude quiet-start PIC only')
    length=2*pi;count=n*ppc;weight=length/count
    x0=(np.arange(count)+.5)*length/count;shape=np.sin(x0);x=x0+amplitude*shape;v=np.zeros(count)
    steps=int(np.ceil(end_time/dt));dt=end_time/steps;records=[];charge=0.;residual=0.
    def acceleration(position):
        nonlocal charge,residual
        rho=cic_deposit(position,weight,n,length);charge=max(charge,abs(rho.sum()*length/n))
        e,r=poisson(rho,length);residual=max(residual,r)
        return -cic_gather(e,position,length),.5*length/n*np.dot(e,e)
    a,field_energy=acceleration(x);initial=.5*weight*np.dot(v,v)+field_energy
    for step in range(steps+1):
        t=step*dt;mode=float(np.dot(x-x0,shape)/np.dot(shape,shape)/amplitude)
        energy=.5*weight*np.dot(v,v)+field_energy
        records.append(dict(time=t,mode=mode,exact_mode=float(np.cos(t)),energy=energy))
        if step==steps:break
        v+=.5*dt*a;x+=dt*v;a,field_energy=acceleration(x);v+=.5*dt*a
    return dict(max_mode_error=max(abs(r['mode']-r['exact_mode']) for r in records),
        charge_error=charge,poisson_residual=residual,
        relative_energy_defect=max(abs(r['energy']-initial) for r in records)/initial,
        dt=dt,particles=count,records=records)


def elastic_round(velocity,rng):
    """One random matching; isotropic equal-mass Maxwell-molecule collisions."""
    n=len(velocity)
    if n%2 or velocity.shape!=(n,3) or not np.isfinite(velocity).all():raise ValueError('Even N x 3 velocity array required')
    pair=rng.permutation(n).reshape(-1,2);i,j=pair.T
    center=.5*(velocity[i]+velocity[j]);speed=np.linalg.norm(velocity[i]-velocity[j],axis=1)
    mu=rng.uniform(-1,1,len(i));azimuth=rng.uniform(0,2*pi,len(i));radial=np.sqrt(1-mu*mu)
    direction=np.column_stack((radial*np.cos(azimuth),radial*np.sin(azimuth),mu))
    relative=.5*speed[:,None]*direction;velocity[i]=center+relative;velocity[j]=center-relative


def dsmc_ensemble(particles,seeds,rounds):
    if particles<16 or particles%2 or seeds<4 or rounds<1:raise ValueError('Even particle count>=16, >=4 seeds and positive rounds required')
    initial=np.zeros((particles,3));initial[:,0]=np.tile([-np.sqrt(3),np.sqrt(3)],particles//2)
    means=[];fourths=[];pooled=[];anisotropy=[];momentum_error=0.;energy_error=0.
    factor=(particles-2)/(2*(particles-1))
    for seed in range(seeds):
        rng=np.random.default_rng(7919+seed);v=initial.copy();history=[];energy=.5*np.sum(v*v)
        for r in range(rounds+1):
            covariance=np.mean(v*v,axis=0);history.append(float(covariance[0]-.5*(covariance[1]+covariance[2])))
            momentum_error=max(momentum_error,float(np.max(np.abs(v.sum(axis=0)))/particles))
            energy_error=max(energy_error,float(abs(.5*np.sum(v*v)-energy)/energy))
            if r<rounds:elastic_round(v,rng)
        means.append(np.mean(v*v,axis=0));fourths.append(np.mean(v**4,axis=0));pooled.append(np.sum(v*v,axis=1)/2)
        anisotropy.append(history)
    pooled=np.concatenate(pooled)
    # Maxwell kinetic energy: Gamma(shape=3/2, scale=T=1).
    ks=float(kstest(pooled,lambda x:gammainc(1.5,x)).statistic)
    history=np.mean(anisotropy,axis=0);exact=3*factor**np.arange(rounds+1)
    return dict(variance=np.mean(means,axis=0).tolist(),fourth_moment=np.mean(fourths,axis=0).tolist(),
        fourth_moment_standard_error=(np.std(fourths,axis=0,ddof=1)/np.sqrt(seeds)).tolist(),
        momentum_error=momentum_error,energy_error=energy_error,energy_cdf_ks=ks,
        anisotropy_max_error=float(np.max(np.abs(history-exact))),
        records=[dict(round=i,anisotropy=float(a),expected=float(b)) for i,(a,b) in enumerate(zip(history,exact))])


def absorption_slab(cells=256,ordinates=8,optical_depth=.7,scheme='upwind'):
    if cells<1 or ordinates<2 or optical_depth<=0 or scheme not in ('upwind','exponential'):
        raise ValueError('Positive absorbing slab, >=2 ordinates and supported scheme required')
    mu,w=np.polynomial.legendre.leggauss(ordinates);mu=(mu+1)/2;w=w/2
    increment=optical_depth/cells/mu
    transmission=1/(1+increment) if scheme=='upwind' else np.exp(-increment)
    intensities=transmission[None,:]**np.arange(cells+1)[:,None]
    exact=np.exp(-optical_depth*np.arange(cells+1)[:,None]/cells/mu)
    flux=2*pi*float(np.dot(w*mu,intensities[-1]));discrete_exact=2*pi*float(np.dot(w*mu,exact[-1]))
    continuum=2*pi*float(expn(3,optical_depth))
    absorbed=2*pi*optical_depth/cells*np.sum(intensities[1:]*w[None,:]) if scheme=='upwind' else float('nan')
    incoming=2*pi*float(np.dot(w,mu));balance=abs(incoming-flux-absorbed) if scheme=='upwind' else 0.
    return dict(flux=flux,discrete_ray_reference=discrete_exact,continuum_reference=continuum,
        spatial_flux_error=abs(flux-discrete_exact),angular_flux_error=abs(discrete_exact-continuum),total_flux_error=abs(flux-continuum),
        ray_max_error=float(np.max(np.abs(intensities-exact))),balance_error=balance,
        minimum_intensity=float(intensities.min()),maximum_intensity=float(intensities.max()))
