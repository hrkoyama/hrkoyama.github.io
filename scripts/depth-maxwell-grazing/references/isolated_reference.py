"""Independent homogeneous fully-discrete modal propagator, with no PML.

The local constitutive block is solved as a 3x3 linear system. The primary
uses scalar midpoint elimination instead. Diagonalizing the independent5x5
Yee update propagates a narrow, explicitly truncated kx Gaussian. Two large
periodic boxes must agree at every requested primary-grid point/time before
the smaller cache is usable as an isolated-boundary reference. This is a
same-discretization boundary reference, not an independent continuum PDE.
"""
import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.optimize import brentq


def update_matrix(q, transverse, h, dt, material):
    q=np.asarray(q);Q=2*np.sin(.5*q*h)/h;K=transverse
    ep=material['epsilon_inf'];sigma=material['sigma'];gamma=material['gamma']
    w0=material['omega0'];f=material['delta_epsilon']*w0*w0
    base=np.broadcast_to(np.eye(5,dtype=complex),(len(q),5,5)).copy()
    # State E,Hx,Hy,P,J, with Fourier phases evaluated at native locations.
    hx=base[:,1]-1j*dt*K*base[:,0]
    hy=base[:,2]+1j*dt*Q[:,None]*base[:,0]
    curl=1j*Q[:,None]*hy-1j*K*hx
    A=np.array([[ep/dt+sigma/2,0,.5],[0,1/dt,-.5],
                [-f/2,w0*w0/2,1/dt+gamma/2]],complex)
    rhs=np.stack([(ep/dt-sigma/2)*base[:,0]+curl-.5*base[:,4],
                  base[:,3]/dt+.5*base[:,4],
                  .5*f*base[:,0]-.5*w0*w0*base[:,3]+(1/dt-gamma/2)*base[:,4]],axis=1)
    solution=lu_solve(lu_factor(A),rhs.transpose(1,0,2).reshape(3,-1)).reshape(3,len(q),5).transpose(1,0,2)
    return np.stack([solution[:,0],hx,hy,solution[:,1],solution[:,2]],axis=1)


def continuum_frequency(kx,ky,material):
    w0=material['omega0'];f=material['delta_epsilon']*w0*w0
    # Lossless lower polariton: a continuum dispersion diagnostic only.
    return brentq(lambda w:w*w*(material['epsilon_inf']+f/(w0*w0-w*w))-kx*kx-ky*ky,
                  1e-9,w0*(1-1e-10),xtol=1e-13,rtol=1e-14)


def modal_packet(h,dt,ky,dy,material,carrier,angle,center,width,box_length,
                 primary_cells,primary_length,times,cutoff_sigma=9.,checkpoint=None):
    total=int(round(box_length/h));origin=-box_length/2
    if abs(total*h-box_length)>1e-10:raise ValueError('Reference box must align exactly')
    lossless={**material,'gamma':0.,'sigma':0.}
    w0=material['omega0'];eps=lossless['epsilon_inf']+lossless['delta_epsilon']*w0*w0/(w0*w0-carrier*carrier)
    qcenter=np.sqrt(eps)*carrier*np.cos(angle)
    # Fixed analytic truncation. No numerical state floor or adaptive cutoff.
    # Retain the exponentially small negative-k tail. A hard k>0 cutoff would
    # introduce an avoidable spatial algebraic tail/box-quadrature bias.
    allq=2*np.pi*np.fft.fftfreq(total,d=h);mask=abs(allq-qcenter)<=cutoff_sigma/width
    indices=np.flatnonzero(mask);q=allq[mask]
    K=0. if ky==0 else 2*np.sin(.5*ky*dy)/dy
    M=update_matrix(q,K,h,dt,material)
    if checkpoint is not None:checkpoint('completed-update-matrix-before-eigensolve',dict(q=q,update_matrix=M))
    values,vectors=np.linalg.eig(M)
    if checkpoint is not None:checkpoint('completed-raw-eigensystem-before-branch-selection',dict(q=q,eigenvalues=values,raw_eigenvectors=vectors))
    omega=-np.angle(values)/dt
    costs=np.where((omega>1e-8)&(omega<w0),abs(omega-carrier),np.inf)
    selected=np.argmin(costs,axis=1)
    if np.any(~np.isfinite(costs[np.arange(len(q)),selected])):raise ValueError('No positive lower-polariton branch')
    lam=values[np.arange(len(q)),selected];v=vectors[np.arange(len(q)),:,selected]
    if np.any(abs(v[:,0])<1e-8):raise ValueError('Ill-scaled electric mode')
    v=v/v[:,0,None]
    if checkpoint is not None:checkpoint('completed-eigensystem',dict(q=q,eigenvalues=values,selected=selected,eigenvectors=v))
    residual=np.einsum('qij,qj->qi',M,v)-lam[:,None]*v
    eigen_error=float(np.max(abs(residual))/max(1.,float(np.max(abs(v)))))
    coefficients=(np.sqrt(2*np.pi)*width/box_length)*np.exp(-.5*((q-qcenter)*width)**2)*np.exp(1j*q*(origin-center))
    primary_x=np.arange(primary_cells+1)*h
    node_indices=np.rint((primary_x-origin)/h).astype(int)%total
    face_indices=node_indices[:-1]
    result=[]
    for t in times:
        steps=int(round(t/dt))
        if abs(steps*dt-t)>1e-9:raise ValueError('Snapshot must be actual integer Yee time')
        amplitude=coefficients*lam**steps
        columns=[]
        for component in range(5):
            spectrum=np.zeros(total,complex);a=amplitude*v[:,component]
            if component==2:a=a*np.exp(.5j*q*h)
            spectrum[indices]=total*a
            native=np.fft.ifft(spectrum)
            columns.append(native[face_indices] if component==2 else native[node_indices])
        result.append(columns)
        if checkpoint is not None:checkpoint('completed-snapshot-'+str(steps),dict(times=np.array(times[:len(result)]),**{n:np.array([z[i] for z in result]) for i,n in enumerate(['E','Hx','Hy','P','J'])}))
    if checkpoint is not None:checkpoint('completed-five-time-packet-before-carrier-diagnostics',dict(times=np.array(times),**{n:np.array([z[i] for z in result]) for i,n in enumerate(['E','Hx','Hy','P','J'])}))
    carrier_matrix=update_matrix(np.array([qcenter]),K,h,dt,material)
    carrier_values=np.linalg.eigvals(carrier_matrix)[0]
    numerical=float(-np.angle(carrier_values[np.argmin(abs(-np.angle(carrier_values)/dt-carrier))])/dt)
    continuous=continuum_frequency(qcenter,ky,lossless)
    return dict(times=np.array(times),E=np.array([z[0] for z in result]),
                Hx=np.array([z[1] for z in result]),Hy=np.array([z[2] for z in result]),
                P=np.array([z[3] for z in result]),J=np.array([z[4] for z in result]),
                eigen_error=eigen_error,max_eigen_abs=float(np.max(abs(lam))),
                q_center=float(qcenter),carrier_numerical=numerical,carrier_continuum=continuous,
                discarded_gaussian_tail_bound=float(2*np.exp(-.5*cutoff_sigma**2)),
                active_modes=len(q),periodic_cells=total,box_length=box_length,
                native_h=h,dt=dt,ky=ky,K=K)
