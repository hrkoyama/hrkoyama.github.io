"""Small independent field, polynomial and ownership regressions."""
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np
import pytest
import steady
import references as R


def test_constant_reaction():
    assert np.array_equal(steady.operator(np.ones(16)),np.ones(16))


def test_periodic_constant_neutral():
    assert np.array_equal(steady.operator(np.ones(16),0),np.zeros(16))


def test_cosine_stencil_golden():
    c,s,w=steady.patterns()
    assert np.array_equal(steady.operator(c),9*c-2*s)


def test_sine_stencil_golden():
    c,s,w=steady.patterns()
    assert np.array_equal(steady.operator(s),2*c+9*s)


def test_nyquist_stencil_golden():
    c,s,w=steady.patterns()
    assert np.array_equal(steady.operator(w),17*w)


def test_forcing_independent_components():
    c,s,w=steady.patterns()
    assert np.array_equal(steady.operator(.5+.25*c),.5+2.25*c-.5*s)


def test_zero_forcing_equilibrium():
    h,stages,res=steady.evolve(np.zeros(16),np.zeros(16),.125,1,1)
    assert np.array_equal(h,np.zeros_like(h)) and np.array_equal(stages,np.zeros_like(stages))


def test_equilibrium_four_stages():
    c,s,w=steady.patterns();star=.5+.25*c
    h,stages,res=steady.evolve(star,.5+2.25*c-.5*s,1/32,1,1)
    assert np.array_equal(stages,np.tile(star,(1,4,1))) and np.array_equal(res,np.zeros_like(res))


def test_expansion_hand_fraction_golden():
    w=steady.patterns()[2];h,stages,res=steady.evolve(w,np.zeros(16),.25,1,1)
    assert np.max(np.abs(h[-1]-float(F(40433,6144))*w))<2e-14


def test_stage_uses_base_not_previous_stage():
    w=steady.patterns()[2];h,stages,res=steady.evolve(w,np.zeros(16),.25,1,1)
    assert np.max(np.abs(stages[0,1]-float(F(209,192))*w))<2e-15


def test_input_ownership():
    w=steady.patterns()[2];before=w.copy();forcing=np.zeros(16)
    steady.evolve(w,forcing,1/32,2,1)
    assert np.array_equal(w,before) and np.array_equal(forcing,np.zeros(16))


def test_progress_capture_does_not_alias_saved_path():
    snapshots=[]
    def see(**data):snapshots.append({k:np.array(v,copy=True) for k,v in data.items()})
    h,_,_=steady.evolve(np.ones(16),np.zeros(16),1/32,2,1,see)
    assert len(snapshots)==24 and np.array_equal(snapshots[0]['base'],np.ones(16))


def test_fraction_prior_classifications():
    assert all(R.qualify().values())


def test_neutral_reference_has_zero_residual():
    values,res=R.field_reference('1/32',8,'neutral_control')
    assert np.array_equal(values,np.ones((9,16))) and np.array_equal(res,np.zeros((9,16)))


def test_expanded_polynomial_exact_golden():
    assert R.polynomial((F(-17,4),F(0)))==(F(40433,6144),F(0))


def test_phase_reference_sign():
    value,res=R.field_reference('1/32',1,'steady_iteration')
    p=R.amplification('1/32',(9,2));c,s,w=steady.patterns()
    assert abs(float(np.sum((value[1]-(.5+.25*c))*s)/8)+p.imag)<1e-15


def test_fixed_input_protocol():
    cfg=json.loads((Path(__file__).parent/'inputs.json').read_text())['jameson-steady-linear-modes']
    assert [(x['id'],x['steps']) for x in cfg['runs']]==[('stable-h32',64),('stable-h16',32),('neutral-constant',8),('expanding-nyquist',4)]


def test_nonlinear_order_caveat():
    c=(F(0),F(1,4),F(1,3),F(1,2));b=(0,0,0,1)
    assert sum(bi*ci**2 for bi,ci in zip(b,c))==F(1,4)!=F(1,3)
