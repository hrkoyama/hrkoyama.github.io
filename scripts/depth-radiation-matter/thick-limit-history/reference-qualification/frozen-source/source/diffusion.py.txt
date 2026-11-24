"""Conservative FV/BE Su-Olson1996 nondimensional diffusion/exchange.

epsilon*u_t-u_xx=v-u+Q; v_t=u-v.  Total density epsilon*u+v.
The half-space Marshak condition is represented by an explicit half-cell
resistance beta+h/2, not by fixing the first cell or wall temperature.
"""
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import splu


def operator(cells,length,closed=False):
    if closed:return diags([np.zeros(cells)],[0],format='csc'),np.zeros(cells)
    h=length/cells;beta=2/np.sqrt(3)
    diagonal=np.full(cells,2/h**2);diagonal[0]=1/h**2+1/(h*(beta+h/2));diagonal[-1]=3/h**2
    matrix=diags([-np.ones(cells-1)/h**2,diagonal,-np.ones(cells-1)/h**2],[-1,0,1],format='csc')
    boundary=np.zeros(cells);boundary[0]=1/(h*(beta+h/2))
    return matrix,boundary


def exchange_diagonal(dt,epsilon):return epsilon/dt+1/(1+dt)


def exchange_rhs(u,v,dt,epsilon,source):return epsilon/dt*u+v/(1+dt)+source


def material_recovery(v,u_new,dt):return (v+dt*u_new)/(1+dt)


def solve(config,partial=None):
    cells,length=config['cells'],config['length'];eps=config['epsilon'];h=length/cells
    if eps<=0:raise ValueError('Positive material-capacity parameter required')
    matrix,boundary=operator(cells,length);u=np.zeros(cells);v=np.zeros(cells)
    states=[np.stack([u,v])];times=[0.];history=[];factors={};t=0.;ledger=0.
    for target in config['times']:
        count=int(np.ceil((target-t)/config['max_dt']));dt=(target-t)/count
        if dt not in factors:factors[dt]=splu(matrix+diags([np.full(cells,exchange_diagonal(dt,eps))],[0],format='csc'))
        start=t
        for k in range(count):
            old_u,old_v=u,v
            stage="update"
            try:
                rhs=exchange_rhs(old_u,old_v,dt,eps,boundary)
                u=factors[dt].solve(rhs);v=material_recovery(old_v,u,dt)
                if not np.isfinite(u).all() or not np.isfinite(v).all() or min(u.min(),v.min())< -1e-13:raise ArithmeticError('Nonphysical diffusion state')
                beta=2/np.sqrt(3);left=(1-u[0])/(beta+h/2);right=2*u[-1]/h
                ledger+=dt*(left-right);t=start+(k+1)*dt
                history.append([t,h*np.sum(eps*u+v),ledger,abs(h*np.sum(eps*u+v)-ledger),u.min(),v.min(),float(np.max(abs((matrix@u)+(exchange_diagonal(dt,eps))*u-rhs)))])
            except Exception:
                if partial is not None:np.savez(partial,last_valid_u=old_u,last_valid_v=old_v,candidate_u=u,candidate_v=v,time=t,step=k,stage=stage)
                raise
        states.append(np.stack([u,v]));times.append(target)
    return dict(x=(np.arange(cells)+.5)*h,states=np.array(states),times=np.array(times),history=np.array(history),
                epsilon=np.array(eps),length=np.array(length),steps=np.array(len(history)))


def closed_advance(u,v,dt,epsilon,source):
    """Same local Schur-complement BE update used by the diffusion solve."""
    new_u=exchange_rhs(u,v,dt,epsilon,source)/exchange_diagonal(dt,epsilon)
    return new_u,material_recovery(v,new_u,dt)
