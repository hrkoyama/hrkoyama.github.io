"""Independent continuum linear dielectric and Volterra IVP, no PIC imports.

Electron convention exp(-i*omega*t), vth=1, neutral fixed ions. Landau Z uses
its entire Faddeeva continuation; lower-plane real-axis quadrature is NOT used.
For the separable initial perturbation, Phi(t)=exp[-(kt)^2/2]cos(k*u*t),
Efree/Ehat0=Phi and K(t)=t*Phi. Volterra e=Phi-K*e follows by integration
by parts of the linear Vlasov equation and ikE=-integral(delta f)dv.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import root,brentq
from scipy.special import wofz
from .estimate import fit


def dispersion(omega,k,drift):
    def term(speed):
        z=(omega-k*speed)/(np.sqrt(2)*k);return 1+z*(1j*np.sqrt(np.pi)*wofz(z))
    return 1+(term(0.) if drift==0 else .5*(term(drift)+term(-drift)))/(k*k)


def mode_root(k,drift):
    if drift==0:
        answers=[]
        for guess in [[1.3,-.1],[1.5,-.2]]:
            sol=root(lambda x:[dispersion(x[0]+1j*x[1],k,0).real,dispersion(x[0]+1j*x[1],k,0).imag],guess,tol=1e-11)
            if not sol.success:raise ValueError('Damped-root iteration failed')
            answers.append(complex(*sol.x))
        # Continue the least-damped positive-frequency Maxwell branch from k=.4.
        continued=1.28-.07j
        for kk in [.4,.45,k]:
            solved=root(lambda x:[dispersion(x[0]+1j*x[1],kk,0).real,dispersion(x[0]+1j*x[1],kk,0).imag],[continued.real,continued.imag],tol=1e-11)
            if not solved.success or not (1<solved.x[0]<2 and -.4<solved.x[1]<0):raise ValueError('Damped branch continuation failed')
            continued=complex(*solved.x)
        return answers[0],max(abs(answers[0]-answers[1]),abs(answers[0]-continued))
    a=brentq(lambda gamma:dispersion(1j*gamma,k,drift).real,.01,.6,xtol=1e-13)
    b=brentq(lambda gamma:dispersion(1j*gamma,k,drift).real,.02,.55,xtol=1e-13)
    return 1j*a,abs(a-b)


def upper_plane_integral(omega,k,drift,cutoff):
    if omega.imag<=0:raise ValueError('Real velocity integration is upper-plane only')
    def derivative(v):return -.5*((v-drift)*np.exp(-.5*(v-drift)**2)+(v+drift)*np.exp(-.5*(v+drift)**2))/np.sqrt(2*np.pi)
    fun=lambda v:derivative(v)/(v-omega/k)
    return 1-(quad(lambda v:fun(v).real,-cutoff,cutoff,epsabs=1e-11,epsrel=1e-11,limit=150)[0]+1j*quad(lambda v:fun(v).imag,-cutoff,cutoff,epsabs=1e-11,epsrel=1e-11,limit=150)[0])/(k*k)


def volterra(k,drift,final_time,dt):
    n=int(round(final_time/dt));t=np.arange(n+1)*dt;free=np.exp(-.5*(k*t)**2)*np.cos(k*drift*t);kernel=t*free;e=np.zeros(n+1);e[0]=1
    for j in range(1,n+1):
        # Composite trapezoid; K(0)=0 so the implicit endpoint vanishes.
        e[j]=free[j]-dt*(.5*kernel[j]*e[0]+np.einsum('i,i->',kernel[1:j],e[j-1:0:-1]))
    if not np.isfinite(e).all():raise ValueError('Nonfinite independent Volterra reference')
    return t,e


def qualify(case,cfg,limits):
    k,drift=cfg['k'],cfg['drift'];omega,gap=mode_root(k,drift)
    coarse_t,coarse=volterra(k,drift,cfg['final_time'],cfg['reference_dt']);t,fine=volterra(k,drift,cfg['final_time'],cfg['reference_dt']/2)
    cf=fit(case,coarse_t,coarse,cfg['fit_window'],omega);ff=fit(case,t,fine,cfg['fit_window'],omega)
    curve_gap=float(np.linalg.norm(coarse-np.interp(coarse_t,t,fine))/np.linalg.norm(coarse));fit_gap=abs(cf['gamma']-ff['gamma']);root_bias=abs(ff['gamma']-omega.imag)/abs(omega.imag)
    checks={}
    def add(name,value,bound,ok):checks[name]=dict(value=value,bound=bound,passed=bool(ok))
    add('dielectric root residual',float(abs(dispersion(omega,k,drift))),limits['root_residual'],abs(dispersion(omega,k,drift))<=limits['root_residual'])
    add('root initial/bracket agreement',float(gap),limits['root_sensitivity'],gap<=limits['root_sensitivity'])
    physical=(1<omega.real<2 and -.4<omega.imag<-.01) if drift==0 else (abs(omega.real)<1e-12 and .01<omega.imag<.6)
    add('physical selected branch',[omega.real,omega.imag],'damped Maxwell branch or positive imaginary symmetric-beam branch',physical)
    add('Volterra time quadrature curve gap',curve_gap,limits['reference_curve_gap'],curve_gap<=limits['reference_curve_gap'])
    add('Volterra fitted rate quadrature gap',fit_gap,limits['reference_rate_gap'],fit_gap<=limits['reference_rate_gap'])
    add('fixed-window transient bias versus pole',root_bias,limits['reference_window_bias'],root_bias<=limits['reference_window_bias'])
    add('fixed-window linear fit residual',ff['relative_fit_residual'],limits['reference_fit_residual'],ff['relative_fit_residual']<=limits['reference_fit_residual'])
    if drift==0:
        bias=abs(ff['omega']-omega.real)/omega.real;add('fixed-window frequency versus pole',bias,limits['reference_frequency_bias'],bias<=limits['reference_frequency_bias'])
    else:
        a=upper_plane_integral(omega,k,drift,12.);b=upper_plane_integral(omega,k,drift,14.)
        add('independent velocity integral dielectric residual',float(abs(b)),limits['velocity_integral_residual'],abs(b)<=limits['velocity_integral_residual'])
        add('independent velocity-tail quadrature gap',float(abs(a-b)),limits['velocity_integral_gap'],abs(a-b)<=limits['velocity_integral_gap'])
    return dict(passed=all(x['passed'] for x in checks.values()),checks=checks,omega_real=float(omega.real),gamma=float(omega.imag),fixed_window_fit=ff,curve_gap=curve_gap,rate_gap=fit_gap,root_window_relative_bias=root_bias),dict(times=t,normalized_field=fine,coarse_times=coarse_t,coarse_normalized_field=coarse)
