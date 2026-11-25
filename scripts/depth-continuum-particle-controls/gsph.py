"""Fixed educational Gaussian-convolution GSPH and separate SPH controls.

Linear specific-volume convolution and symmetric variable-h approximation from
Inutsuka2002, Eq52/79--85. Piecewise-constant pair Riemann states; not the
paper's cubic-overlap/MUSCL version. Total-energy pair flux is explicit.
"""
import numpy as np
import time as walltime
from failure_support import NumericalFailure,own_failure


class ContractFailure(NumericalFailure):
    def __init__(self, reason, diagnostics, state_arrays=None):
        super().__init__(reason)
        self.diagnostics = diagnostics
        self.state_arrays = state_arrays or {}


def scatter_pairs(i, j, force, power, mass):
    dv, dE = np.zeros(len(mass)), np.zeros(len(mass))
    np.add.at(dv,i,force/mass[i]);np.add.at(dv,j,-force/mass[j])
    np.add.at(dE,i,power/mass[i]);np.add.at(dE,j,-power/mass[j])
    return dv, dE


def assert_closed_energy(mass, initial, final, tolerance=1e-10):
    defect = float(np.sum(mass*(final-initial)))
    if abs(defect) > tolerance*max(1.,abs(float(np.sum(mass*initial)))):
        raise ContractFailure('Closed-system energy balance failed', {'defect':defect})
    return defect


def periodic_delta(x, length):
    d = x[:, None]-x[None, :]
    return d-length*np.floor(d/length+.5)


def gaussian(d, h):
    return np.exp(-(d/h)**2)/(np.sqrt(np.pi)*h)


def linear_overlap(Vi,Vj,distance,h):
    C = (Vi-Vj)/distance
    D = .5*(Vi+Vj)
    return .25*h*h*C*C+D*D


def gsph_pair_exchange(d,vi,vj,rhoi,rhoj,pi,pj,hi,hj,mi,mj,gamma=1.4):
    """Actual force and laboratory total-energy transfer to the first particle."""
    overlap_i=linear_overlap(1/rhoi,1/rhoj,np.abs(d),hi)
    overlap_j=linear_overlap(1/rhoi,1/rhoj,np.abs(d),hj)
    B=overlap_i*(-d/hi**2)*gaussian(d,np.sqrt(2)*hi)+overlap_j*(-d/hj**2)*gaussian(d,np.sqrt(2)*hj)
    direction=-np.sign(d)
    pstar,vstar,residual=riemann_star(rhoi,direction*vi,pi,rhoj,direction*vj,pj,gamma)
    force=-mi*mj*pstar*B
    return force,force*(direction*vstar),residual


def pair_swap_residual():
    values=[np.array([value]) for value in [-.11,.12,-.08,1.3,.7,1.2,.6,.09,.13,.2,.3]]
    d,vi,vj,rhoi,rhoj,pi,pj,hi,hj,mi,mj=values
    force,power,_=gsph_pair_exchange(d,vi,vj,rhoi,rhoj,pi,pj,hi,hj,mi,mj)
    swapped_force,swapped_power,_=gsph_pair_exchange(-d,vj,vi,rhoj,rhoi,pj,pi,hj,hi,mj,mi)
    return float(np.max(np.abs(force+swapped_force))),float(np.max(np.abs(power+swapped_power)))


def density_and_h(x, mass, h_seed, length, adaptive=True, eta=1.2, csmooth=2., rtol=1e-10, maxiter=100):
    d = periodic_delta(x, length)
    h = np.asarray(h_seed).copy()
    last = np.inf
    count = 0
    if adaptive:
        for count in range(1, maxiter+1):
            rho_smooth = np.einsum('ij,j->i', gaussian(d, csmooth*h[:, None]), mass, optimize=False)
            target = eta*mass/rho_smooth
            last = float(np.max(np.abs(target-h)/h))
            if not np.isfinite(target).all() or np.any(target <= 0) or np.max(target) > .15*length:
                raise ContractFailure('h left predeclared physical range', {'iteration':count, 'relative_residual':last}, {'x':x.copy(),'mass':mass.copy(),'h':h.copy(),'target_h':target.copy()})
            if last <= rtol:
                break
            h = .5*(h+target)
        else:
            raise ContractFailure('h fixedpoint did not converge', {'iterations':maxiter, 'relative_residual':last}, {'x':x.copy(),'mass':mass.copy(),'h':h.copy(),'target_h':target.copy()})
    rho = np.einsum('ij,j->i', gaussian(d, h[:, None]), mass, optimize=False)
    if not np.isfinite(rho).all() or np.min(rho) <= 0:
        raise ContractFailure('Invalid density', {'rho_min':float(np.min(rho))})
    return rho, h, {'h_iterations':count, 'h_relative_residual':0. if not adaptive else last}


def riemann_star(rL, vL, pL, rR, vR, pR, gamma=1.4, max_bracket=32, iterations=64):
    """Vectorized positive pressure bisection, independent of saved oracle code."""
    cL, cR = np.sqrt(gamma*pL/rL), np.sqrt(gamma*pR/rR)
    if np.any(vR-vL >= 2*(cL+cR)/(gamma-1)):
        raise ContractFailure('Vacuum pair outside fixed contract', {})

    def curve(p, r, pk, c):
        shock = (p-pk)*np.sqrt((2/((gamma+1)*r))/(p+(gamma-1)*pk/(gamma+1)))
        rare = 2*c/(gamma-1)*((p/pk)**((gamma-1)/(2*gamma))-1)
        return np.where(p > pk, shock, rare)

    def f(p):
        return curve(p,rL,pL,cL)+curve(p,rR,pR,cR)+vR-vL

    lo, hi = np.zeros_like(pL), np.maximum(pL,pR).copy()
    for bracket in range(max_bracket):
        mask = f(hi) < 0
        if not np.any(mask):
            break
        hi = np.where(mask, 2*hi, hi)
    else:
        raise ContractFailure('Pair pressure bracket failed', {'max_bracket':max_bracket})
    for _ in range(iterations):
        mid = .5*(lo+hi)
        mask = f(mid) < 0
        lo, hi = np.where(mask,mid,lo), np.where(mask,hi,mid)
    pressure = .5*(lo+hi)
    velocity = .5*(vL+vR+curve(pressure,rR,pR,cR)-curve(pressure,rL,pL,cL))
    residual = float(np.max(np.abs(f(pressure)))) if len(pressure) else 0.
    if residual > 1e-9 or not np.isfinite(pressure).all():
        raise ContractFailure('Pair Riemann residual failed', {'max_wave_residual':residual})
    return pressure, velocity, residual


def particle_rhs(state, mass, h_seed, length, gamma=1.4, mode='gsph'):
    x, velocity, specific_total = state
    rho, h, diagnostics = density_and_h(x, mass, h_seed, length, adaptive=mode=='gsph')
    internal = specific_total-.5*velocity**2
    pressure = (gamma-1)*rho*internal
    if np.min(internal) <= 0 or np.min(pressure) <= 0 or not np.isfinite(state).all():
        raise ContractFailure('Invalid particle thermodynamic state; no clipping', {'internal_min':float(np.min(internal))})
    delta = periodic_delta(x, length)
    i,j = np.triu_indices(len(x), 1)
    d = delta[i,j]
    active = (np.abs(d) > 1e-14*length) & (np.abs(d) < 4*np.sqrt(2)*np.maximum(h[i],h[j]))
    i,j,d = i[active],j[active],d[active]
    direction = -np.sign(d)  # Oriented from particle i to particle j.
    if mode == 'gsph':
        force,power,residual=gsph_pair_exchange(d,velocity[i],velocity[j],rho[i],rho[j],pressure[i],pressure[j],h[i],h[j],mass[i],mass[j],gamma)
        diagnostics['Riemann_residual'] = residual
    elif mode == 'sph':
        # Fixed initial per-particle h is a declared control, not adaptive grad-h SPH.
        grad_i = -2*d/h[i]**2*gaussian(d,h[i])
        grad_j = -2*d/h[j]**2*gaussian(d,h[j])
        approach = (velocity[i]-velocity[j])*d
        hbar = .5*(h[i]+h[j])
        mu = hbar*approach/(d*d+.01*hbar*hbar)
        cbar = .5*(np.sqrt(gamma*pressure[i]/rho[i])+np.sqrt(gamma*pressure[j]/rho[j]))
        viscosity = np.where(approach < 0,(-cbar*mu+2*mu*mu)/(.5*(rho[i]+rho[j])),0.)
        A, B = pressure[i]/rho[i]**2, pressure[j]/rho[j]**2
        mean_grad = .5*(grad_i+grad_j)
        force = -mass[i]*mass[j]*(A*grad_i+B*grad_j+viscosity*mean_grad)
        power = -mass[i]*mass[j]*(A*velocity[j]*grad_i+B*velocity[i]*grad_j+.5*viscosity*(velocity[i]+velocity[j])*mean_grad)
        diagnostics['Riemann_residual'] = 0.
    else:
        raise ValueError('Unknown particle mode')
    dv, dE = scatter_pairs(i,j,force,power,mass)
    diagnostics.update(rho=rho,h=h,pressure=pressure,pair_count=len(i),
                       momentum_derivative=float(np.sum(mass*dv)),energy_derivative=float(np.sum(mass*dE)))
    return np.array([velocity,dv,dE]),diagnostics


def evolve(state, mass, h_initial, length, final_time, mode='gsph', gamma=1.4, cfl=.15, max_steps=20000, deadline=None):
    state = np.asarray(state).copy()
    h_seed = np.asarray(h_initial).copy()
    initial_invariants = np.array([np.sum(mass),np.sum(mass*state[1]),np.sum(mass*state[2])])
    history = []
    time, steps = 0.,0
    while time < final_time:
        step_start_state=state.copy();step_h_seed=h_seed.copy()
        stage,stage_time,stage_state,stage_h='step-start',time,step_start_state,step_h_seed
        try:
            if deadline is not None and walltime.monotonic()>deadline:raise ContractFailure('Shared numerical wall budget exceeded',{'limit_seconds':90})
            k1,d1 = particle_rhs(state,mass,h_seed,length,gamma,mode)
            sound = np.sqrt(gamma*d1['pressure']/d1['rho'])
            dt = min(final_time-time,cfl*float(np.min(d1['h']/(sound+2*np.max(np.abs(state[1]))))))
            middle = state+.5*dt*k1
            middle[0] %= length
            stage,stage_time,stage_state,stage_h='midpoint',time+.5*dt,middle,d1['h'] if mode=='gsph' else h_initial
            k2,d2 = particle_rhs(stage_state,mass,stage_h,length,gamma,mode)
            candidate=step_start_state+dt*k2;candidate[0]%=length
            stage,stage_time,stage_state,stage_h='final',time+dt,candidate,d2['h'] if mode=='gsph' else h_initial
            _,final=particle_rhs(stage_state,mass,stage_h,length,gamma,mode)
            state=candidate
            if mode=='gsph':h_seed=d2['h']
        except Exception as error:
            failure=own_failure(error,stage,stage_time,steps,{'step_start_state':step_start_state,'step_start_h_seed':step_h_seed},{'failed_state':stage_state,'failed_stage_h_seed':stage_h,'mass':mass})
            failure.diagnostics['mode']=mode
            raise failure
        time += dt;steps += 1
        history.append([time,dt,float(np.min(final['rho'])),float(np.min(final['pressure'])),
                        float(np.min(final['h'])),float(np.max(final['h'])),
                        final['h_relative_residual'],final['Riemann_residual']])
        if steps >= max_steps:
            raise ContractFailure('Particle step cap', {'steps':steps,'physical_time':time,'stage':'step-cap','mode':mode}, {'step_start_state':step_start_state,'failed_state':state.copy(),'h':h_seed.copy(),'mass':mass.copy()})
    final_invariants = np.array([np.sum(mass),np.sum(mass*state[1]),np.sum(mass*state[2])])
    return dict(state=state,mass=mass,rho=final['rho'],h=final['h'],pressure=final['pressure'],
                history=np.asarray(history),initial_invariants=initial_invariants,
                final_invariants=final_invariants,defect=final_invariants-initial_invariants,
                steps=steps,time=time,method=mode,sampling='point primitive; m/rho volume quadrature')


def sod_initial(right_count, gamma=1.4, eta=1.2):
    """Periodic two-interface Sod; central interface is x=1 on [0,2)."""
    nL,nR = 8*right_count,right_count
    x = np.concatenate(((np.arange(nL)+.5)/nL,1+(np.arange(nR)+.5)/nR))
    mass = np.full(nL+nR,1/nL)
    model_rho = np.where(x < 1.,1.,.125)
    pressure = np.where(x < 1.,1.,.1)
    seed = eta*mass/model_rho
    rho,h,_ = density_and_h(x,mass,seed,2.)
    # Pressure is prescribed exactly against the actual kernel initial density.
    # The finite-h difference from the discontinuous continuum rho is saved.
    state = np.array([x,np.zeros_like(x),pressure/((gamma-1)*rho)])
    return state,mass,h,dict(model_density=model_rho,kernel_density=rho,pressure=pressure)


def smooth_initial(count, acoustic=False, jitter=False, gamma=1.4, eta=1.2, amplitude=1e-3):
    target = (np.arange(count)+.5)/count
    x = target.copy()
    if acoustic:
        for _ in range(12):
            residual = x+amplitude*(1-np.cos(2*np.pi*x))/(2*np.pi)-target
            x -= residual/(1+amplitude*np.sin(2*np.pi*x))
    if jitter:
        x += .08/count*np.sin(6*np.pi*np.arange(count)/count)
    x %= 1.
    mass = np.full(count,1/count)
    model_rho = 1+amplitude*np.sin(2*np.pi*x) if acoustic else np.ones(count)
    velocity = amplitude*np.sin(2*np.pi*x) if acoustic else np.zeros(count)
    pressure = 1/gamma+amplitude*np.sin(2*np.pi*x) if acoustic else np.full(count,1/gamma)
    rho,h,_ = density_and_h(x,mass,eta*mass/model_rho,1.)
    total = pressure/((gamma-1)*rho)+.5*velocity**2
    return np.array([x,velocity,total]),mass,h,dict(model_density=model_rho,kernel_density=rho,pressure=pressure)
