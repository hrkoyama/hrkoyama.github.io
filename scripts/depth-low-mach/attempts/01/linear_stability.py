"""Frozen constant-state 2D Fourier diagnostics, not a nonlinear stability proof."""
import numpy as np
import lm_solver as solver


def energy_transform(rho,c):
    """Entropy and physical acoustic-energy variables; not unscaled p/velocity."""
    s=np.sqrt(rho)
    return np.array([[c/s,0,0,-1/(s*c)],[0,s,0,0],[0,0,s,0],[0,0,0,1/(s*c)]])


def matrices(rho,u,v,c,axis,variant,mach_cutoff):
    order=[0,1,2,3] if axis==0 else [0,2,1,3]
    un,ut=(u,v) if axis==0 else (v,u)
    a,unused=solver.normal_matrices(rho,un,ut,c,variant,mach_cutoff)
    # Columnwise application of the actual spatial dissipation; tests compare
    # this separately with an explicit full-matrix eigendecomposition oracle.
    d=np.stack([solver.dissipation_primitive(e,rho,un,ut,c,variant,mach_cutoff) for e in np.eye(4)],axis=1)
    return a[np.ix_(order,order)],d[np.ix_(order,order)]


def stability_scan(machs=(.1,.01),cfl=.2,wavenumbers=17,powers=(1,10,100)):
    if wavenumbers<5 or wavenumbers%2!=1:raise ValueError('Odd fixed Fourier grid required')
    result=[];u,v=1.,.5;rho=1.;identity=np.eye(4)
    ks=np.linspace(-np.pi,np.pi,wavenumbers)
    for mach in machs:
        c=np.hypot(u,v)/mach;s=energy_transform(rho,c);si=np.linalg.inv(s)
        dt=cfl/(abs(u)+abs(v)+2*c)
        for variant in ('roe','miczek'):
            ax,dx=matrices(rho,u,v,c,0,variant,mach);ay,dy=matrices(rho,u,v,c,1,variant,mach)
            radius=0.;forward_euler=0.;norm=0.;max_real=-float('inf');worst=None
            for kx in ks:
                for ky in ks:
                    l=-1j*(np.sin(kx)*ax+np.sin(ky)*ay)-(1-np.cos(kx))*dx-(1-np.cos(ky))*dy
                    scaled=s@l@si;z=dt*scaled;z2=z@z
                    r=identity+z+.5*z2+(z2@z)/6
                    spectral=float(np.max(abs(np.linalg.eigvals(r))))
                    if spectral>radius:radius=spectral;worst=[float(kx),float(ky)]
                    forward_euler=max(forward_euler,float(np.max(abs(np.linalg.eigvals(identity+z)))))
                    max_real=max(max_real,float(np.max(np.linalg.eigvals(scaled).real)))
                    for m in powers:norm=max(norm,float(np.linalg.norm(np.linalg.matrix_power(r,m),2)))
            result.append({'mach_far':mach,'variant':variant,'acoustic_dt_at_h1':dt,'wavenumbers_per_axis':wavenumbers,
                'sampled_2d_modes':wavenumbers*wavenumbers,'power_indices':list(powers),'maximum_SSPRK3_spectral_radius':radius,
                'maximum_energy_scaled_power_norm':norm,'maximum_forward_Euler_spectral_radius':forward_euler,
                'maximum_semidiscrete_eigenvalue_real_part':max_real,'worst_SSPRK3_mode':worst,
                'scope':'Constant uniform background only; selected Fourier grid/powers, not a nonlinear or continuous-mode stability theorem.'})
    return result
