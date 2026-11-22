"""Minimal velocity-Verlet consumer of a converged BO energy/force callback.

Atomic units throughout: bohr, electron masses, atomic time, hartree. This is
an interface demonstration, without constraints, thermostat or a barostat.
"""
import numpy as np


def _state(positions,velocities,masses,dt):
    r=np.asarray(positions,dtype=float);v=np.asarray(velocities,dtype=float);m=np.asarray(masses,dtype=float)
    if r.ndim!=2 or r.shape[1]!=3 or v.shape!=r.shape or m.shape!=(len(r),):
        raise ValueError('Require Cartesian Nx3 positions/velocities and N masses')
    if not all(np.isfinite(x).all() for x in [r,v,m]) or np.any(m<=0) or not np.isfinite(dt) or dt<=0:
        raise ValueError('State/time must be finite, masses/time positive')
    return r,v,m


def checked_force(callback,positions):
    record=callback(positions)
    if not record.get('converged',False):raise RuntimeError('Unconverged electronic state cannot advance nuclei')
    e=record['energy_per_cell'];f=np.asarray(record['forces_cartesian'],dtype=float)
    if f.shape!=positions.shape or not np.isfinite(f).all() or not np.isfinite(e):
        raise FloatingPointError('Force callback returned an invalid energy/force')
    return record,f


def velocity_verlet_step(callback,positions,velocities,masses,dt,initial_record=None):
    r,v,m=_state(positions,velocities,masses,dt)
    if initial_record is None:initial_record,f=checked_force(callback,r)
    else:
        initial_record,f=checked_force(lambda _:initial_record,r)
        if 'positions_bohr' in initial_record and not np.allclose(initial_record['positions_bohr'],r,rtol=0,atol=1e-14):
            raise ValueError('Cached electronic state belongs to a different geometry')
    vhalf=v+.5*dt*f/m[:,None];rnew=r+dt*vhalf
    final_record,fnew=checked_force(callback,rnew)
    vnew=vhalf+.5*dt*fnew/m[:,None]
    return dict(positions_bohr=rnew.tolist(),velocities_bohr_per_atomic_time=vnew.tolist(),electronic_state=final_record,total_energy_hartree=float(final_record['energy_per_cell']+.5*np.sum(m[:,None]*vnew*vnew)))
