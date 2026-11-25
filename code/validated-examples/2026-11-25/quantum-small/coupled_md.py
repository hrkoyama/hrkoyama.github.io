"""DRAFT 95: one normalized two-state orbital coupled to a nuclear coordinate.

Dimensionless educational Hamiltonian, not first-principles molecular dynamics.
The CP-type mass convention is L=T_n+mu*theta_dot**2/2-E(Q,theta).
"""
import math
import random
import numpy as np


def ground_angle(q, c):
    return -.5 * math.atan2(c['g'] * q, c['delta'])


def ground_angle_gradient(q, c):
    return -.5 * c['g'] * c['delta'] / (c['delta']**2 + (c['g'] * q)**2)


def potential(q, theta, c):
    return .5*c['k']*q*q-c['delta']*math.cos(2*theta)+c['g']*q*math.sin(2*theta)


def bo_potential(q, c):
    return .5*c['k']*q*q-math.hypot(c['delta'], c['g']*q)


def forces(q, theta, c):
    return (-c['k']*q-c['g']*math.sin(2*theta),
            -2*c['delta']*math.sin(2*theta)-2*c['g']*q*math.cos(2*theta))


def bo_force(q, c):
    return -c['k']*q+c['g']**2*q/math.hypot(c['delta'], c['g']*q)


def rhs(y, c, mu):
    q, v, theta, omega = y
    if mu is None:
        return np.array([v, bo_force(q, c)/c['nuclear_mass'], 0., 0.])
    fq, ft = forces(q, theta, c)
    return np.array([v, fq/c['nuclear_mass'], omega, ft/mu])


def initial(c):
    return np.array([c['Q0'], c['V0'], ground_angle(c['Q0'], c),
                     ground_angle_gradient(c['Q0'], c)*c['V0']])


def ledger(y, c, mu):
    q, v, theta, omega = y
    nuclear = .5*c['nuclear_mass']*v*v
    electronic = 0. if mu is None else .5*mu*omega*omega
    energy = bo_potential(q, c) if mu is None else potential(q, theta, c)
    return {"extended_energy": nuclear+electronic+energy,
            "nuclear_BO_energy": nuclear+bo_potential(q, c),
            "fictitious_kinetic": electronic,
            "electronic_excitation": 0. if mu is None else energy-bo_potential(q, c),
            "orbital_norm_error": abs(math.cos(theta)**2+math.sin(theta)**2-1),
            "kinetic_temperature_single_DOF": c['nuclear_mass']*v*v}


def rk4_reference(c, mu, steps):
    y = initial(c)
    h = c['T']/steps
    for _ in range(steps):
        a=rhs(y,c,mu);b=rhs(y+h*a/2,c,mu);d=rhs(y+h*b/2,c,mu);e=rhs(y+h*d,c,mu)
        y=y+h*(a+2*b+2*d+e)/6
    if mu is None:
        y[2]=ground_angle(y[0],c);y[3]=ground_angle_gradient(y[0],c)*y[1]
    return y


def propagate(c, mu, dt, bath=None):
    y=initial(c);rows=[];heat=0.;rng=random.Random(c['bath']['seed'])
    # B A O A B; zero friction/noise is velocity Verlet for both coordinates.
    for step in range(round(c['T']/dt)+1):
        if mu is None:
            y[2]=ground_angle(y[0],c);y[3]=ground_angle_gradient(y[0],c)*y[1]
        rows.append(dict(step=step,time=step*dt,state=y.tolist(),bath_heat=heat,**ledger(y,c,mu)))
        if step==round(c['T']/dt):break
        f=rhs(y,c,mu);y[1]+=dt*f[1]/2
        if mu is not None:y[3]+=dt*f[3]/2
        y[0]+=dt*y[1]/2
        if mu is not None:y[2]+=dt*y[3]/2
        if bath:
            a=math.exp(-bath['gamma']*dt)
            b=math.sqrt(bath['temperature']/c['nuclear_mass']*(-math.expm1(-2*bath['gamma']*dt)))
            before=.5*c['nuclear_mass']*y[1]**2
            y[1]=a*y[1]+b*rng.gauss(0.,1.)
            heat+=.5*c['nuclear_mass']*y[1]**2-before
        y[0]+=dt*y[1]/2
        if mu is not None:y[2]+=dt*y[3]/2
        f=rhs(y,c,mu);y[1]+=dt*f[1]/2
        if mu is not None:y[3]+=dt*f[3]/2
    return rows


def run(c, save):
    rows=[];reference_sensitivity=[]
    for name,mu in [('bo',None),('cp-mu004',c['cp_mu'][0])]:
        references=[]
        for count in c['rk4_reference_steps']:
            reference=rk4_reference(c,mu,count);references.append(reference)
            save('95-'+name+'-rk4-reference-'+str(count),{'steps':count,'state':reference})
        size=2 if mu is None else 4
        reference_sensitivity.append({'model':name,'steps':c['rk4_reference_steps'],
                                      'state_difference':float(np.linalg.norm(references[0][:size]-references[1][:size]))})
        reference=references[-1]
        for index,dt in enumerate(c['dt']):
            trajectory=propagate(c,mu,dt);save('95-'+name+'-'+str(index)+'-trajectory',trajectory)
            e0=trajectory[0]['extended_energy']
            error=float(np.linalg.norm(np.array(trajectory[-1]['state'])[:2 if mu is None else 4]-reference[:2 if mu is None else 4]))
            rows.append({'id':name+'-'+str(index),'mu':mu,'dt':dt,'trajectory':trajectory,
                         'reference_state_error':error,'max_energy_drift':max(abs(x['extended_energy']-e0) for x in trajectory)})
    mu=c['cp_mu'][1];dt=c['dt'][-1]
    trajectory=propagate(c,mu,dt);save('95-cp-mu001-trajectory',trajectory)
    rows.append({'id':'cp-mu001','mu':mu,'dt':dt,'trajectory':trajectory,
                 'max_energy_drift':max(abs(x['extended_energy']-trajectory[0]['extended_energy']) for x in trajectory)})
    thermal=propagate(c,mu,dt,c['bath']);save('95-cp-OU-trajectory',thermal)
    e0=thermal[0]['extended_energy'];a=math.exp(-c['bath']['gamma']*dt)
    b=math.sqrt(c['bath']['temperature']/c['nuclear_mass']*(-math.expm1(-2*c['bath']['gamma']*dt)))
    return {'runs':rows,'thermal':thermal,'reference_sensitivity':reference_sensitivity,
            'thermal_heat_ledger_error':max(abs(x['extended_energy']-e0-x['bath_heat']) for x in thermal),
            'OU_conditional_variance_identity_error':abs(a*a+b*b*c['nuclear_mass']/c['bath']['temperature']-1),
            'scope':'Short two-state BO/CP-type dynamics and nuclear OU coupling only; no canonical sampling or long first-principles MD claim.'}
