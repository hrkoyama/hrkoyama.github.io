"""Independent analytic sign and spatial/time-path checks; no large benchmark."""
import ast
from pathlib import Path
import numpy as np
import pytest
import primary
from references import scalar_pic
from run import fixture


def test_primary_analytic_field():
    n,l,x=fixture();a,e,r,_=primary.field(x,n,l);np.testing.assert_allclose(e,-.25*np.sin(2*np.arange(n)*l/n),atol=2e-14)

def test_scalar_analytic_field():
    n,l,x=fixture();a,e,r=scalar_pic.field(x,n,l);np.testing.assert_allclose(e,-.25*np.sin(2*np.arange(n)*l/n),atol=2e-14)

def test_primary_analytic_force():
    n,l,x=fixture();a,*_=primary.field(x,n,l);np.testing.assert_allclose(a,.25*np.sin(2*x),atol=2e-14)

def test_scalar_analytic_force():
    n,l,x=fixture();a,*_=scalar_pic.field(x,n,l);np.testing.assert_allclose(a,.25*np.sin(2*x),atol=2e-14)

def test_wrong_sign_negative_control():
    n,l,x=fixture();wrong,*_=scalar_pic.field(x,n,l,wrong_sign=True);assert np.max(abs(wrong-.25*np.sin(2*x)))>.49

@pytest.mark.parametrize('n',[7,8,15,16])
def test_scalar_vectorized_fields_match(n):
    x=np.random.default_rng(7).uniform(-5,15,51);a,e,r,_=primary.field(x,n,5.);b,f,s=scalar_pic.field(x,n,5.);np.testing.assert_allclose(a,b,atol=3e-14);np.testing.assert_allclose(e,f,atol=3e-14);np.testing.assert_allclose(r,s,atol=3e-14)

def test_scalar_positive_weights():
    rng=np.random.default_rng(8);x=rng.uniform(0,5,31);w=rng.uniform(.5,1.5,31);w*=5/w.sum();a,e,r=scalar_pic.field(x,16,5,w);assert abs(np.sum(w*a))<1e-14;assert abs(np.sum(r)*5/16)<1e-14

def test_scalar_nyquist_zero_force():
    x=np.repeat(np.arange(8)*2*np.pi/8,[3,1]*4);a,e,r=scalar_pic.field(x,8,2*np.pi);assert np.max(abs(e))<1e-14;assert np.max(abs(r))>.49

def test_scalar_uniform_periodic_equilibrium():
    x=np.arange(32)*2*np.pi/32+.04;v=np.full(32,.3);out=scalar_pic.advance(x,v,8,2*np.pi,.02,4);np.testing.assert_allclose(out['v'],np.full((5,32),.3),atol=1e-14)

def test_scalar_field_recomputed_each_kick(monkeypatch):
    calls=[];original=scalar_pic.field
    def wrapped(*args,**kwargs):calls.append(np.copy(args[0]));return original(*args,**kwargs)
    monkeypatch.setattr(scalar_pic,'field',wrapped);n,l,x=fixture();scalar_pic.advance(x,np.zeros_like(x),n,l,.02,4);assert len(calls)==5;assert np.max(abs(calls[-1]-calls[0]))>1e-6

def test_scalar_reverse_time():
    n,l,x=fixture();v=.1*np.cos(x);a=scalar_pic.advance(x,v,n,l,.02,4);b=scalar_pic.advance(a['x'][-1],-a['v'][-1],n,l,.02,4);np.testing.assert_allclose(b['x'][-1],x,atol=4e-15);np.testing.assert_allclose(b['v'][-1],-v,atol=4e-15)

def test_twelve_step_paired_dynamics():
    n,l,x=fixture();v=.1*np.cos(x);a=primary.advance(x,v,n,l,.02,.24,save_every_step=True);b=scalar_pic.advance(x,v,n,l,.02,12);np.testing.assert_allclose(a['x_history'],b['x'],atol=4e-14);np.testing.assert_allclose(a['v_history'],b['v'],atol=4e-14)

def test_independent_source_has_no_primary_or_fft_imports():
    source=Path(scalar_pic.__file__).read_text();tree=ast.parse(source);imports=[node for node in ast.walk(tree) if isinstance(node,(ast.Import,ast.ImportFrom))];assert not any('primary' in ast.unparse(node) for node in imports);assert 'np.fft' not in source;assert 'bincount' not in source

def test_even_and_odd_frequency_conventions_are_explicit():
    source=Path(scalar_pic.__file__).read_text();assert 'n%2==0' in source;assert 'm-n' in source

def test_scalar_rejects_nonpositive_weights():
    with pytest.raises(ValueError):scalar_pic.field([0.,1.],8,5.,[0.,5.])


def test_periodic_rounding_of_tiny_negative_coordinate():
    length=2*np.pi;x=np.arange(8)*length/8;x[0]=-1e-20
    for method in [primary.field,scalar_pic.field]:
        a,e,r,*_=method(x,8,length)
        np.testing.assert_allclose(r,0,atol=2e-15);np.testing.assert_allclose(a,0,atol=2e-15)
