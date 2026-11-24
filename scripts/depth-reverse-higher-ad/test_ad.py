import ast
import json
from pathlib import Path
import numpy as np
import pytest
from tape import build,values,unbroadcast
from fixtures import rectangular,bratu,quadratic
from hessians import hvp,implicit_second
from references import smooth_reference,hvp_reference,precision_qualified,stopped_reference
from kinks import piece,max_tie,stopped,inactive_log
from experiments import expected_gate_keys,run_reverse,run_hvp


def test_forward_primitives():
    x=np.array([2.,4.]);v=np.array([.5,-1.])
    t,n,o=build(lambda z:z[0]*z[1]+z[0]/z[1],x,v)
    assert float(o.value)==8.5;assert float(o.tangent)==.25

def test_reverse_repeated_parent():
    t,n,o=build(lambda z:(z*z).sum(),np.array([1.,2.,3.]));g,_=t.reverse(o,np.array(1.))
    assert np.array_equal(g,[2.,4.,6.])

def test_broadcast_unreduce():
    t,n,o=build(lambda z:((z[[0,0,2]]+z[3])*(z[[0,0,2]]+z[3])).sum(),np.array([.25,-.5,.75,.5]))
    g,_=t.reverse(o,np.array(1.));assert np.array_equal(g,[3.,0.,2.5,5.5])
    assert unbroadcast(np.array([1.,2.,3.]),()).item()==6.

def test_duplicate_index_scatter_add():
    t,n,o=build(lambda z:z[[0,0,2]].sum(),np.array([.25,-.5,.75,.5]));g,_=t.reverse(o,np.array(1.))
    assert np.array_equal(g,[2.,0.,1.,0.])
    key=np.array([0,0,2]);t,n,o=build(lambda z:z[key].sum(),np.array([.25,-.5,.75,.5]));saved=float(o.value)
    key[:]=1;g,_=t.reverse(o,np.array(1.))
    assert float(o.value)==saved and np.array_equal(g,[2.,0.,1.,0.])

def test_division_rule():
    t,n,o=build(lambda z:z[0]/z[1],np.array([2.,4.]),np.array([.5,-1.]));g,_=t.reverse(o,np.array(1.))
    assert np.array_equal(g,[.25,-.125]);assert float(o.tangent)==.25

def test_exp_rule():
    v=np.array([1.,-.5,.25]);g,h,t,o=hvp(lambda z:z.exp().sum(),np.zeros(3),v)
    assert np.array_equal(g,np.ones(3));assert np.array_equal(h,v)

def test_sum_shape_rule():
    t,n,o=build(lambda z:(2*z).sum()/4,np.array([1.,2.,3.,4.]));g,_=t.reverse(o,np.array(1.))
    assert np.array_equal(g,np.full(4,.5))
    with pytest.raises(ValueError):t.reverse(o,np.ones(1))

def test_input_and_readonly_ownership():
    x=np.array([1.,2.,3.]);old=x.copy();view=x.view();view.setflags(write=False)
    t,n,o=build(lambda z:(z*z).sum(),view);g,_=t.reverse(o,np.array(1.))
    assert np.array_equal(x,old);assert not np.shares_memory(n.value,x);assert not np.shares_memory(g,n.cotangent)

def test_reset_and_old_return_ownership():
    t,n,o=build(lambda z:(z*z).sum(),np.array([1.,2.]));a,_=t.reverse(o,np.array(1.));old=a.copy()
    b,_=t.reverse(o,np.array(1.));c,_=t.reverse(o,np.array(-1.))
    assert np.array_equal(a,old)and np.array_equal(a,b)and np.array_equal(c,-a)

def test_rectangular_independent_jacobian():
    x=np.array([.25,-.5,.75,.5]);v=np.array([.5,-.25,1.,-.5]);w=np.array([.75,-.5,1.25])
    t,n,o=build(rectangular,x,v);g,_=t.reverse(o,w);y,j=smooth_reference('rectangular4x3',x)
    assert precision_qualified();assert np.allclose(values(o),y,atol=1e-13,rtol=0)
    assert np.allclose(values(o,'tangent'),np.einsum('ij,j->i',j,v),atol=1e-13,rtol=0)
    assert np.allclose(g,np.einsum('ij,i->j',j,w),atol=1e-13,rtol=0)

def test_weighted_adjoint_pairing():
    x=np.array([.25,-.5,.75,.5]);v=np.array([.5,-.25,1.,-.5]);w=np.array([.75,-.5,1.25])
    gx=np.array([1.,2.,4.,8.]);gy=np.array([[2.,.5,0.],[.5,1.,0.],[0.,0.,3.]])
    t,n,o=build(rectangular,x,v);gyw=np.einsum('ij,j->i',gy,w);adj=t.reverse(o,gyw)[0]/gx
    assert abs(np.sum(values(o,'tangent')*gyw)-np.sum(v*gx*adj))<1e-12
    assert not np.allclose(adj,t.reverse(o,w)[0],atol=1e-3,rtol=0)

def test_bratu_transpose_stencil():
    x=np.linspace(-.1,.2,7);w=np.arange(1.,8.)/8;t,n,o=build(bratu,x);g,_=t.reverse(o,w)
    _,j=smooth_reference('bratu7',x);assert np.allclose(g,np.einsum('ij,i->j',j,w),atol=1e-12,rtol=0)

def test_all_four_real_mutants_detected():
    x=np.array([.25,-.5,.75,.5]);w=np.array([.75,-.5,1.25]);_,j=smooth_reference('rectangular4x3',x);oracle=np.einsum('ij,i->j',j,w)
    for fault in ['drop-duplicate','broadcast-first','permuted-output','stale-cotangent']:
        t,n,o=build(rectangular,x)
        if fault=='stale-cotangent':t.reverse(o,w)
        bad=t.reverse(o,w,negative_control=fault)[0];assert np.sqrt(np.sum((bad-oracle)**2))>1e-8

def test_actual_rule_and_gate_counts():
    t,n,o=build(lambda z:(z*z).sum(),np.array([1.,2.]));t.reverse(o,np.array(1.))
    inv=t.inventory();assert inv['primal_rules']==2 and inv['backward_rules']==2 and inv['pullbacks']==1
    gates=expected_gate_keys();assert [len(gates[k])for k in gates]==[46,27,144]
    assert all(len(a)==len(set(a))for a in gates.values())

def test_exact_dyadic_quadratic_hvp():
    x=np.array([.25,-.5,.75,1.]);v=np.array([1.,-.5,.25,.75]);g,h,t,o=hvp(quadratic,x,v);gr,hr=hvp_reference('quadratic4',x,v)
    assert np.array_equal(g,gr);assert np.array_equal(h,hr)

def test_forward_over_reverse_exp_curvature():
    x=np.array([0.,0.]);v=np.array([.25,-.5]);g,h,t,o=hvp(lambda z:(z.exp()*z.exp()).sum(),x,v)
    assert np.array_equal(g,[2.,2.]);assert np.array_equal(h,4*v);assert t.second_rules==t.inventory()['primal_rules']

def test_implicit_state_first_second_rules():
    stages=[];a=implicit_second(checkpoint=lambda stage,**k:stages.append(stage))
    assert a['iterations'][0]['u']==3.;assert abs(a['F'])<=1e-12 and abs(a['R1'])<=1e-12 and abs(a['R2'])<=1e-12
    assert abs(a['total_curvature']-.23125)<=1e-12 and abs(a['fixed_state_partial']-.2)<=1e-12
    assert 'implicit-second-before-fixed-partial'in stages

def test_live_type_cannot_be_erased():
    t,n,o=build(lambda z:z*z,np.array(2.))
    with pytest.raises(TypeError):float(n)
    with pytest.raises(TypeError):np.asarray(n,dtype=float)
    source=ast.parse(Path('hessians.py').read_text())
    implicit=next(n for n in source.body if isinstance(n,ast.FunctionDef)and n.name=='implicit_second')
    assert not any(isinstance(n,ast.Attribute)and n.attr=='sqrt'for n in ast.walk(implicit))

def test_primary_hvp_no_dense_hessian():
    x=np.zeros(31);v=np.arange(31.)/31;g,h,t,o=hvp(lambda z:(z*z).sum(),x,v)
    assert t.inventory()['max_node_rank']<=1 and np.array_equal(h,2*v)
    assert not np.shares_memory(g,h)

def test_strict_kink_categories():
    for kind,point in [('abs',0.),('relu',0.),('clip',-1.),('clip',1.),('branch',0.)]:
        ans=piece(kind,point,1);assert ans['status']=='NONDIFFERENTIABLE';assert ans['classical_slope']is None
    assert piece('branch',0.,-1)['executed_branch_trace_slope']==0.

def test_max_directional_map_is_not_linear():
    a=max_tie((1,-1));b=max_tie((-1,1));c=max_tie((0,0))
    assert a['one_sided_directional']==1 and b['one_sided_directional']==1 and c['one_sided_directional']==0
    assert a['one_sided_directional']+b['one_sided_directional']!=c['one_sided_directional']

def test_literal_stop_predicate_and_jump():
    xs=[.25,.5,1.,.5-2.**-20,.5+2.**-20]
    assert [stopped(x)['K']for x in xs]==[1,2,3,2,3]
    for x in xs:
        k,y,g=stopped_reference(x);a=stopped(x);assert a['K']==k and a['value']==y and a['frozen_trace_slope']==g
    h=2.**-24;assert (stopped(.5+h)['value']-stopped(.5)['value'])/h==1/(16*h)+7/8
    assert all(stopped(x)['classical_slope']is None for x in [.25,.5,1.])

def test_inactive_invalid_log_not_evaluated():
    a=inactive_log();assert a['invalid_log_calls']==0 and a['value']==1. and a['classical_slope']==-2.

def test_completed_products_preserved_before_reference_failure(monkeypatch,tmp_path):
    import experiments
    def fail(*args):raise RuntimeError('intentional independent reference failure')
    first=tmp_path/'reverse';first.mkdir();monkeypatch.setattr(experiments,'smooth_reference',fail)
    with pytest.raises(RuntimeError):run_reverse(first)
    assert (first/'rectangular4x3-raw.npz').exists()and json.loads((first/'reverse-partial.json').read_text())[0]['id']=='rectangular4x3'
    second=tmp_path/'hvp';second.mkdir();monkeypatch.setattr(experiments,'hvp_reference',fail)
    with pytest.raises(RuntimeError):run_hvp(second)
    with np.load(second/'quadratic4-raw.npz')as raw:assert 'Hv'in raw and 'gradient'in raw
