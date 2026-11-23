import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm


def faces(xi,t,amplitude=.2):
    return xi+amplitude/(2*np.pi)*np.sin(2*np.pi*xi)*np.sin(2*np.pi*t)


def mesh_speed(xi,t,amplitude=.2):
    return amplitude*np.sin(2*np.pi*xi)*np.cos(2*np.pi*t)


def mass(edges,t,speed=.7):
    phase=2*np.pi*(edges-speed*t)
    return np.diff(edges)-.2/(2*np.pi)*np.diff(np.cos(phase))


def ale_time_reference(n,final_time,rtol=1e-12):
    """Independent adaptive integration of the SAME moving-cell FV ODE."""
    xi=np.linspace(0,1,n+1)
    initial=np.r_[xi,mass(xi,0)]
    def rhs(t,z):
        x=z[:n+1];m=z[n+1:];q=m/(x[1:]-x[:-1])
        w=.2*np.sin(2*np.pi*xi)*np.cos(2*np.pi*t)
        # Positive physical-minus-grid speeds for this frozen input.
        interface=np.r_[q[-1],q]
        transport=(.7-w)*interface
        return np.r_[w,transport[:-1]-transport[1:]]
    answer=solve_ivp(rhs,(0,final_time),initial,method='DOP853',rtol=rtol,atol=rtol*.01)
    if not answer.success:raise ArithmeticError(answer.message)
    return answer.y[:,-1]


def symbol(n,k=1,l=2,discrete=True):
    a,b=2*np.pi*k,2*np.pi*l
    if discrete:
        c=np.cos(a/(2*n))*np.cos(b/(2*n))
        a,b=2*n*np.sin(a/(2*n)),2*n*np.sin(b/(2*n))
    else:c=1.
    return np.array([[0,-1j*a,-1j*b],[-1j*a,0,c],[-1j*b,-c,0]],dtype=complex)


def amplitudes(n,t,initial=None,discrete=True,k=1,l=2):
    if initial is None:initial=np.array([.01,0.,0.],dtype=complex)
    return expm(t*symbol(n,k,l,discrete))@initial


def field(n,coeff,k=1,l=2):
    j,i=np.mgrid[:n,:n];x=(i+.5)/n;y=(j+.5)/n
    phases=[2*np.pi*(k*x+l*y),2*np.pi*(k*(x+.5/n)+l*y),2*np.pi*(k*x+l*(y+.5/n))]
    return np.array([np.real(c*np.exp(1j*p)) for c,p in zip(coeff,phases)])


def zero_mode(t):
    return np.array([.03,.02*np.cos(t)-.01*np.sin(t),-.02*np.sin(t)-.01*np.cos(t)])


def qualification():
    xi=np.linspace(0,1,81);t=.173
    a=faces(xi,t);w=mesh_speed(xi,t);h=1e-6
    gap=np.max(abs((faces(xi,t+h)-faces(xi,t-h))/(2*h)-w))
    matrix=symbol(32)
    return {'analytic moving-face velocity':bool(gap<1e-9),
            'periodic analytic mass':bool(abs(mass(a,t).sum()-1)<2e-15),
            'skew-Hermitian discrete symbol':bool(np.max(abs(matrix+matrix.conj().T))<1e-14),
            'continuous wave frequency':bool(abs(max(abs(np.linalg.eigvals(symbol(32,discrete=False))))-np.sqrt(1+20*np.pi**2))<1e-12)}
