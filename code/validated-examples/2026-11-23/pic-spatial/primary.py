"""Original full-f1D1V electrostatic CIC/FFT PIC with self-consistent Verlet.

rho=1-ne, E_x=rho, electron acceleration=-E. Matched CIC gathering and a
real skew spectral derivative conserve total particle momentum up to roundoff.
Even-grid Nyquist charge is reported separately; its derivative/field is zero.
No state clipping, prescribed-field substitution or retries are used.
"""
import time
import numpy as np


class ParticleFailure(ArithmeticError):
    def __init__(self,message,x,v,context):
        super().__init__(message);self.x=x.copy();self.v=v.copy();self.context=context


def field(position,grid,length,weights=None):
    x=np.asarray(position,dtype=float)
    if x.ndim!=1 or len(x)<2 or grid<4 or length<=0 or not np.isfinite(x).all():raise ValueError('Invalid periodic PIC coordinates/grid')
    weights=np.full(len(x),length/len(x)) if weights is None else np.asarray(weights,dtype=float)
    if weights.shape!=x.shape or not np.isfinite(weights).all() or np.any(weights<=0) or abs(weights.sum()-length)>1e-12*length:raise ValueError('Positive neutral particle weights required')
    z=(x%length)*(grid/length);left=np.floor(z).astype(int);fraction=z-left;left%=grid
    number=(np.bincount(left,weights=weights*(1-fraction),minlength=grid)+np.bincount((left+1)%grid,weights=weights*fraction,minlength=grid))*(grid/length)
    rho=1-number;wave=2*np.pi*np.fft.fftfreq(grid,d=length/grid);rh=np.fft.fft(rho);eh=np.zeros(grid,dtype=complex)
    active=wave!=0
    if grid%2==0:active[grid//2]=False
    eh[active]=rh[active]/(1j*wave[active]);e=np.fft.ifft(eh).real
    a=-((1-fraction)*e[left]+fraction*e[(left+1)%grid])
    diag=dict(charge_error=float(abs(rho.sum())*length/grid),resolved_gauss=float(np.max(abs((1j*wave*eh-rh)[active]))/grid),nyquist_charge=float(abs(rh[grid//2])/grid) if grid%2==0 else 0.,field_energy=float(.5*length/grid*np.sum(e*e)),mode_real=float(eh[1].real/grid),mode_imag=float(eh[1].imag/grid),maximum_acceleration=float(np.max(abs(a))))
    return a,e,rho,diag


COLUMNS=['step','time','mode_real','mode_imag','field_energy','total_energy','relative_energy_drift','normalized_momentum_drift','charge_error','resolved_gauss','nyquist_charge','maximum_abs_velocity','maximum_acceleration']


def advance(x0,v0,grid,length,dt,final_time,weights=None,deadline=None,save_every_step=False):
    if dt<=0 or final_time<=0 or x0.shape!=v0.shape:raise ValueError('Invalid PIC time/state')
    count=int(round(final_time/dt))
    if count<4 or count%4 or abs(count*dt-final_time)>1e-12:raise ValueError('Use fixed integer step count divisible byfour')
    x=x0.copy();v=v0.copy();weights=np.full(len(x),length/len(x)) if weights is None else weights.copy();a,e,rho,d=field(x,grid,length,weights)
    energy0=.5*np.sum(weights*v*v)+d['field_energy'];momentum0=np.sum(weights*v);pscale=length*max(1.,float(np.sqrt(np.sum(weights*v*v)/length)))
    xhist=[];vhist=[];ehist=[];rhist=[];times=[];history=[]
    for step in range(count+1):
        if not np.isfinite(v).all() or not np.isfinite(x).all():raise ParticleFailure('Nonfinite full-f state',x,v,dict(step=step,stage='observe'))
        energy=.5*np.sum(weights*v*v)+d['field_energy']
        history.append([step,step*dt,d['mode_real'],d['mode_imag'],d['field_energy'],energy,abs(energy-energy0)/energy0,abs(np.sum(weights*v)-momentum0)/pscale,d['charge_error'],d['resolved_gauss'],d['nyquist_charge'],float(np.max(abs(v))),d['maximum_acceleration']])
        if save_every_step or step%(count//4)==0:xhist.append(x.copy());vhist.append(v.copy());ehist.append(e.copy());rhist.append(rho.copy());times.append(step*dt)
        if step==count:break
        if deadline is not None and time.monotonic()>deadline:raise ParticleFailure('Fixed shared execution deadline',x,v,dict(step=step,stage='budget'))
        v+=.5*dt*a;x+=dt*v
        try:a,e,rho,d=field(x,grid,length,weights)
        except (ValueError,FloatingPointError) as error:raise ParticleFailure(str(error),x,v,dict(step=step,stage='new_self_consistent_field')) from error
        v+=.5*dt*a
    return dict(x_history=np.array(xhist),v_history=np.array(vhist),electric_history=np.array(ehist),rho_history=np.array(rhist),snapshot_times=np.array(times),history=np.array(history),history_columns=np.array(COLUMNS),x_initial=x0.copy(),v_initial=v0.copy(),particle_weights=weights,grid=np.array(grid),length=np.array(length),dt=np.array(dt),final_time=np.array(final_time),steps=np.array(count),state_clip_count=np.array(0),retries=np.array(0))
