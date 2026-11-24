import json
import numpy as np
import pytest
import slab,io_contract


def test_signed_angular_measure_and_flux_normalization():
    mu,w=slab.directions(16)
    assert np.sum(w)==pytest.approx(2.,abs=2e-15)
    assert np.sum(w*mu)==pytest.approx(0.,abs=2e-15)
    assert np.sum(w*mu*mu)==pytest.approx(2/3,abs=2e-15)
    assert np.sum(w[mu>0]*mu[mu>0])==pytest.approx(.5,abs=2e-15)


def test_invalid_angular_controls():
    for number in [0,1,3]:
        with pytest.raises(ValueError):slab.directions(number)


def test_invalid_physical_slab_controls():
    for depth,omega,n in [(-1.,.5,8),(1.,1.1,8),(1.,-.1,8),(1.,.5,1)]:
        with pytest.raises(ValueError):slab.solve_slab(depth,omega,n,8)


def test_zero_scattering_exact_discrete_beer_sweep():
    out=slab.solve_slab(.8,0.,16,8);h=.8/16;mu=out['mu']
    for i,speed in enumerate(mu):
        expected=(speed/(speed+h))**(np.arange(16)+1) if speed>0 else np.zeros(16)
        np.testing.assert_allclose(out['intensity'][i],expected,rtol=1e-14,atol=1e-14)
    assert out['R']==0.


def test_coupled_scattering_conserves_independent_absorption():
    out=slab.solve_slab(.7,.6,16,16)
    assert out['balance']<2e-13 and out['R']>0 and out['T']>0 and out['A']>0


def test_conservative_scattering_has_zero_absorbed_energy():
    out=slab.solve_slab(1.,1.,16,16)
    assert out['A']==0 and abs(out['R']+out['T']-1)<2e-13


def test_two_ordinate_transfer_matrix_independent_golden():
    length,omega,mu=1.,.5,.5
    generator=np.array([[-(1-omega/2),omega/2],[-omega/2,1-omega/2]])/mu
    wave=np.sqrt(1-omega)/mu;transfer=np.cosh(wave*length)*np.eye(2)+np.sinh(wave*length)/wave*generator;exact=np.array([-transfer[1,0]/transfer[1,1],1/transfer[1,1]])
    errors=[]
    for n in [32,64]:
        out=slab.solve_slab(length,omega,n,2);errors.append(np.max(abs(np.array([out['R'],out['T']])-exact)))
    assert errors[1]<.7*errors[0] and errors[1]<.015


def test_negative_ordinates_carry_actual_reflected_radiance():
    out=slab.solve_slab(1.,.8,16,16)
    assert np.max(out['intensity'][out['mu']<0])>0
    assert out['intensity'][0,0]>out['intensity'][0,-1]


def test_collocated_source_and_transport_residuals():
    out=slab.solve_slab(3.,.9,32,16)
    assert out['source_residual']<1e-12 and out['residual']<1e-12


def test_actual_frozen_sources_and_reference_qualification():
    c=io_contract.verify(io_contract.ROOT/'inputs.json')
    assert c['planned_primary_runs']==18


def test_rejects_nonboolean_reference_flag(tmp_path,monkeypatch):
    (tmp_path/'inputs.json').write_text('{}');(tmp_path/'references').mkdir()
    (tmp_path/'references/qualification.json').write_text(json.dumps({'passed':True,'checks':{'x':'true'}}))
    (tmp_path/'pre-run-contract.json').write_text(json.dumps({'files_sha256':{'inputs.json':io_contract.sha(tmp_path/'inputs.json')}}))
    monkeypatch.setattr(io_contract,'ROOT',tmp_path)
    with pytest.raises(ValueError,match='Unqualified'):io_contract.verify(tmp_path/'inputs.json')


def test_scientific_checks_are_json_native_booleans():
    c=io_contract.case('example');io_contract.check(c,'finite',1.,2.,np.bool_(True))
    assert type(c['checks']['finite']) is bool
    json.dumps(c,allow_nan=False)
