"""DRAFT scientific qualification tests; run only after root/peer freeze."""
import math
import numpy as np
import pytest
import coupled_md as md
import molecules as mol
import eigenpairs
import periodic_projector as periodic
from io_utils import mm, mv, dot, norm


@pytest.mark.parametrize('q',[-.4,0.,.4])
def test_two_level_ground_state_energy_and_force(q):
    c={'k':1.,'delta':1.,'g':.25};theta=md.ground_angle(q,c)
    assert abs(md.potential(q,theta,c)-md.bo_potential(q,c))<1e-14
    fq,ft=md.forces(q,theta,c)
    assert abs(ft)<1e-14
    assert abs(fq-md.bo_force(q,c))<1e-14
    assert md.potential(q,theta+.2,c)>md.bo_potential(q,c)


def test_coupled_force_is_energy_gradient():
    c={'k':1.,'delta':1.,'g':.25};q=.4;t=-.2;h=1e-5
    fq,ft=md.forces(q,t,c)
    dq=-(md.potential(q+h,t,c)-md.potential(q-h,t,c))/(2*h)
    dt=-(md.potential(q,t+h,c)-md.potential(q,t-h,c))/(2*h)
    assert abs(fq-dq)<1e-8 and abs(ft-dt)<1e-8
    assert abs(fq-(-q))>1e-3  # Removing real electronic/nuclear coupling is detected.


def test_fictitious_mass_and_coupled_conservative_power():
    c={'k':1.,'delta':1.,'g':.25,'nuclear_mass':20.};y=np.array([.4,.05,-.2,.03])
    a=md.rhs(y,c,.04);b=md.rhs(y,c,.01);fq,ft=md.forces(y[0],y[2],c)
    assert abs(b[3]-4*a[3])<1e-13 and a[1]==b[1]
    assert abs(-fq*y[1]-ft*y[3]+20*y[1]*a[1]+.04*y[3]*a[3])<1e-14
    assert abs(a[3]-ft/.01)>1  # Wrong fictitious mass is detected.


def test_native_norm_must_precede_representation_conversion():
    v=np.array([.6,.8]);bad=2*v
    assert abs(np.dot(v,v)-1)<1e-14
    assert abs(np.dot(bad,bad)-1)>1
    assert np.allclose(bad/np.linalg.norm(bad),v)  # Normalization would conceal the mutation.


def test_decimal_box_one_unknown_and_sign_invariance():
    assert abs(eigenpairs.box_oracle(2,1)-4)<1e-14
    u=np.array([.5,-.2]);q=-u
    assert min(np.linalg.norm(u-q),np.linalg.norm(u+q))==0


def test_normalized_one_center_primitive_integrals():
    a=.7;A=np.zeros(3);N=(2*a/math.pi)**.75
    assert abs(N*N*mol.overlap(a,A,a,A)-1)<1e-14
    assert abs(N*N*mol.kinetic(a,A,a,A)-1.5*a)<1e-14
    assert abs(N**4*mol.repulsion(a,A,a,A,a,A,a,A)-2*math.sqrt(a/math.pi))<1e-13


def test_two_center_integral_assembly_keeps_explicit_norm_callable():
    basis={'shells':[{'exponents':[.7],'coefficients':[1.]}]}
    S,h,g,enuc=mol.integrals([[0.,0.,0.],[0.,0.,1.4]],[1.,1.],basis)
    assert S.shape==(2,2) and h.shape==(2,2) and g.shape==(2,2,2,2)
    assert np.isfinite(S).all() and np.isfinite(h).all() and np.isfinite(g).all()
    assert np.max(abs(np.diag(S)-1))<1e-14
    assert abs(enuc-1/1.4)<1e-14


def test_fermion_sign_and_independent_matrix_assembly():
    assert mol.apply_ops(0,[(False,0)]) is None
    assert mol.apply_ops(1,[(True,0)]) is None
    h=np.array([[-1.,.07],[.07,.4]]);g=np.zeros((2,2,2,2))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):g[i,j,k,l]=1/(1+i+j+k+l)
    direct=mol.product_hamiltonian(h,g);operator=mol.fermion_reference(h,g)
    assert np.max(abs(direct-operator))<1e-14
    assert abs(direct[0,3]-g[0,1,0,1])<1e-14
    assert np.max(abs(direct-direct.T))<1e-14


def test_projector_derivative_and_cubic_oracle():
    c={'G':[-1,0,1],'local_V1':-.1,'projector_eta':.3,'projector_sigma':.8}
    H,dH,_=periodic.matrix(.25,.4,c);h=1e-5
    left=periodic.matrix(.25,.4-h,c)[0];right=periodic.matrix(.25,.4+h,c)[0]
    assert np.max(abs(H-H.conj().T))<1e-14
    assert np.max(abs((right-left)/(2*h)-dH))<1e-9
    assert np.max(abs(periodic.cubic_reference(np.diag([1.,2.,3.]))-[1,2,3]))<1e-14


def test_Fermi_fixed_N_entropy_and_symmetric_chemical_potential():
    r=periodic.occupations([[0.,.5,1.]],[1.],.1,3.)
    assert abs(r['electrons']-3)<1e-14
    assert abs(r['mu']-.5)<1e-14
    assert r['entropy']>0
    assert abs(r['free_energy']-(r['band_internal_energy']-.1*r['entropy']))<1e-14


def test_entropy_omission_gives_wrong_fixed_N_force():
    slopes=np.array([0.,1.,2.]);T=.3;N=2.;h=1e-5
    central=periodic.occupations([slopes],[1.],T,N)
    left=periodic.occupations([(1-h)*slopes],[1.],T,N)
    right=periodic.occupations([(1+h)*slopes],[1.],T,N)
    correct=-float(np.sum(central['f'][0]*slopes))
    fd_free=-(right['free_energy']-left['free_energy'])/(2*h)
    wrong=-(right['band_internal_energy']-left['band_internal_energy'])/(2*h)
    assert abs(correct-fd_free)<1e-8
    assert abs(correct-wrong)>1e-3


@pytest.mark.parametrize('complex_values',[False,True])
@pytest.mark.parametrize('strided',[False,True])
def test_explicit_contractions_match_scalar_fsum_without_hidden_conjugation(complex_values,strided):
    a=np.arange(30,dtype=float).reshape(5,6)[::2,::2]/7-.4
    b=np.arange(24,dtype=float).reshape(3,8)[:,::4]/5-.7
    if complex_values:
        a=a+1j*(a[::-1]+.2)/11
        b=b+1j*(b[::-1]-.3)/13
    # Own genuinely noncontiguous views even after complex construction.
    if strided:
        aa=np.zeros((6,6),dtype=a.dtype);aa[::2,::2]=a;a=aa[::2,::2]
        bb=np.zeros((6,4),dtype=b.dtype);bb[::2,::2]=b;b=bb[::2,::2]
        assert not a.flags.c_contiguous and not b.flags.c_contiguous
    else:
        a=a.copy();b=b.copy()
    def scalar_sum(left,right):
        products=[complex(x)*complex(y) for x,y in zip(left,right)]
        return complex(math.fsum(z.real for z in products),math.fsum(z.imag for z in products))
    def check(actual,left,right):
        reference=scalar_sum(left,right);n=len(left);eps=np.finfo(float).eps
        gamma=n*eps/(1-n*eps)
        # 16*gamma_n covers complex product rounding plus accumulation and
        # the independent fsum rounding; it is not a scientific accuracy gate.
        bound=16*gamma*max(1.,math.fsum(abs(complex(x))*abs(complex(y)) for x,y in zip(left,right)))
        assert abs(actual-reference)<=bound
    product=mm(a,b)
    for i in range(len(a)):
        for j in range(b.shape[1]):check(product[i,j],a[i],b[:,j])
    vector=mv(a,b[:,0])
    for i in range(len(a)):check(vector[i],a[i],b[:,0])
    check(dot(a[0],b[:,0]),a[0],b[:,0])
    gram=mm(a.conj().T,a)
    for i in range(a.shape[1]):
        for j in range(a.shape[1]):check(gram[i,j],a[:,i].conj(),a[:,j])
    frobenius=math.sqrt(math.fsum(abs(complex(x))**2 for x in a.flat))
    infinity=max(math.fsum(abs(complex(x)) for x in row) for row in a)
    tolerance=16*a.size*np.finfo(float).eps*max(1.,frobenius,infinity)
    assert abs(norm(a)-frobenius)<=tolerance
    assert abs(norm(a,np.inf)-infinity)<=tolerance


def test_explicit_norm_scaling_and_nonfinite_rejection():
    for scale in [1e-200,1e200]:
        value=norm(np.array([scale,-scale]))
        assert abs(value/math.hypot(scale,scale)-1)<4*np.finfo(float).eps
    assert norm(np.zeros(3))==0.
    with pytest.raises(FloatingPointError):norm(np.array([float('nan')]))
