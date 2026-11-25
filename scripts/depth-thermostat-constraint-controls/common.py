"""Shared educational utilities; authored source, no SciPy dependency."""
from __future__ import annotations
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np


def mm(a,b):
    """Explicit bilinear2Dproduct; caller owns any conjugation."""
    return np.einsum('ij,jk->ik',a,b,optimize=False)


def mv(a,b):
    return np.einsum('ij,j->i',a,b,optimize=False)


def dot(a,b):
    return np.einsum('i,i->',a,b,optimize=False)


def matmul(a,b):
    """Only the declared1D/2Dproducts, explicitCcontractions withoutBLAS."""
    a=np.asarray(a);b=np.asarray(b)
    if a.ndim==2 and b.ndim==2:return mm(a,b)
    if a.ndim==2 and b.ndim==1:return mv(a,b)
    if a.ndim==1 and b.ndim==2:return np.einsum('i,ij->j',a,b,optimize=False)
    if a.ndim==1 and b.ndim==1:return dot(a,b)
    raise ValueError('Only declared1D/2Dproducts supported')


def array_norm(a,order=None):
    """Scaled Euclidean/Frobenius norm or explicitmatrix infinitynorm."""
    absolute=np.abs(np.asarray(a))
    if order==np.inf:
        if absolute.ndim!=2:raise ValueError('Matrixinfinitynormrequires2D')
        if not np.all(np.isfinite(absolute)):raise FloatingPointError('Nonfiniteexplicitnorminput')
        return float(np.max(np.sum(absolute,axis=1)))
    if order is not None:raise ValueError('OnlydeclaredEuclidean/Frobenius/infinitynormsupported')
    scale=float(np.max(absolute))
    if not math.isfinite(scale):raise FloatingPointError('Nonfiniteexplicitnorminput')
    return 0. if scale==0 else scale*math.sqrt(float(np.sum((absolute/scale)**2)))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def plain(x):
    if isinstance(x, np.ndarray):
        return x.tolist()
    if isinstance(x, np.generic):
        return x.item()
    if isinstance(x, dict):
        return {str(k): plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [plain(v) for v in x]
    return x


def write_json(path, obj):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + '.partial')
    tmp.write_text(json.dumps(plain(obj), ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    os.replace(tmp, path)


SOURCE_FILES = ['LICENSE', 'PROTOCOL.md', 'README.md', 'acceptance.json', 'cases.json', 'common.py', 'constrained.py', 'deterministic.py', 'inputs.json', 'plot.py', 'requirements-plotting.txt', 'requirements.txt', 'run.py', 'source-reading.json', 'test_models.py']

def assert_frozen(root):
    """Verify the shipped public source subset; generated outputs are not inputs."""
    root=Path(root)
    f=json.loads((root/'freeze.json').read_text())
    if f.get('status')!='ROOT_PEER_REVIEWED_FROZEN' or not f.get('root_review') or not f.get('independent_peer_review'):
        raise ValueError('A root/peer reviewed source/input/acceptance freeze is required')
    if set(f['files_sha256'])!=set(SOURCE_FILES):
        raise ValueError('Freeze must bind exactly the public owned source/input/reference subset')
    for name,digest in f['files_sha256'].items():
        if sha(root/name)!=digest:raise ValueError('Frozen source changed: '+name)
    return f


def failure_plain(x):
    """Preserve nonfinite failure evidence without making invalid JSON."""
    if isinstance(x,np.ndarray):return failure_plain(x.tolist())
    if isinstance(x,np.generic):return failure_plain(x.item())
    if isinstance(x,float) and not math.isfinite(x):return {'nonfinite':repr(x)}
    if isinstance(x,dict):return {str(k):failure_plain(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [failure_plain(v) for v in x]
    return x


class Budget:
    def __init__(self, seconds):
        self.start = time.monotonic()
        self.seconds = float(seconds)
        self.counts = {}
        self.active = {}
    def tick(self, name='step', amount=1):
        self.counts[name] = self.counts.get(name, 0) + amount
        if time.monotonic() - self.start > self.seconds:
            raise TimeoutError('Shared scientific execution budget exhausted')
    def own(self, **state):
        self.active = state
    def augment(self, **state):
        self.active.update(state)
    @property
    def elapsed(self):
        return time.monotonic() - self.start


class Recorder:
    def __init__(self, output, budget, root):
        self.output = Path(output)
        self.output.mkdir(parents=True, exist_ok=False)
        self.budget = budget
        self.report = {'schema_version': 1, 'passed': False, 'termination': 'incomplete',
                       'input_sha256': sha(Path(root)/'inputs.json'),
                       'acceptance_sha256': sha(Path(root)/'acceptance.json'),
                       'runtime': {'python': __import__('sys').version, 'numpy': np.__version__},
                       'rows': [], 'checks': {}, 'study_goals': {}}
        self.save()
    def save(self):
        self.report['elapsed_seconds'] = self.budget.elapsed
        self.report['work_counts'] = self.budget.counts
        write_json(self.output/'result.json', self.report)
    def row(self, row_id, info, **arrays):
        if any(r['id'] == row_id for r in self.report['rows']):
            raise ValueError('Duplicate row ' + row_id)
        if arrays:
            np.savez(self.output/(row_id+'.npz'), **arrays)
        self.report['rows'].append({'id': row_id, **plain(info), 'data': row_id+'.npz' if arrays else None})
        self.save()
    def check(self, key, condition):
        self.report['checks'][key] = bool(condition)
    def goal(self, key, condition, **evidence):
        self.report['study_goals'][key] = {'observed': None if condition is None else bool(condition), **plain(evidence)}
    def failure(self, exc):
        state = self.budget.active
        arrays = {k: v for k, v in state.items() if isinstance(v, np.ndarray)}
        if arrays:
            np.savez(self.output/'failure-active-state.npz', **arrays)
        self.report.update(termination='failed', error={'type': type(exc).__name__, 'message': str(exc)},
                           active=failure_plain({k:v for k,v in state.items() if k not in arrays}))
        self.save()


def rk4(fun,t,y,h,budget=None):
    def evaluate(tt,z,stage):
        if budget:budget.augment(RK4_stage=stage,RK4_stage_time=tt,RK4_stage_input=z,last_accepted_state=y)
        return fun(tt,z)
    k1=evaluate(t,y,1)
    k2=evaluate(t+h/2,y+h*k1/2,2)
    k3=evaluate(t+h/2,y+h*k2/2,3)
    k4=evaluate(t+h,y+h*k3,4)
    yn=y+h*(k1+2*k2+2*k3+k4)/6
    if budget:budget.augment(candidate_state=yn)
    return yn


# Rational tableau data are mathematical formulae. Driver/ownership are authored.
DP_A = [[], [1/5], [3/40,9/40], [44/45,-56/15,32/9],
        [19372/6561,-25360/2187,64448/6561,-212/729],
        [9017/3168,-355/33,46732/5247,49/176,-5103/18656],
        [35/384,0,500/1113,125/192,-2187/6784,11/84]]
DP_C = [0,1/5,3/10,4/5,8/9,1,1]
DP_B = [35/384,0,500/1113,125/192,-2187/6784,11/84,0]
DP_LOW = [5179/57600,0,7571/16695,393/640,-92097/339200,187/2100,1/40]
CK_A = [[],[1/5],[3/40,9/40],[3/10,-9/10,6/5],
        [-11/54,5/2,-70/27,35/27],
        [1631/55296,175/512,575/13824,44275/110592,253/4096]]
CK_C = [0,1/5,3/10,3/5,1,7/8]
CK_B = [37/378,0,250/621,125/594,0,512/1771]
CK_LOW = [2825/27648,0,18575/48384,13525/55296,277/14336,1/4]


def adaptive(fun, y0, times, budget, rtol, atol, max_nfev, method='DP54', first_step=1e-3):
    """Independent embedded 5(4) reference; land at every requested time, no dense output.

    Local embedded estimates and finite refinement differences are NOT global bounds.
    Every stage is charged; no FSAL reuse, hidden retry or success cache.
    """
    if method == 'DP54':
        a,c,b,low = DP_A,DP_C,DP_B,DP_LOW
    elif method == 'CK54':
        a,c,b,low = CK_A,CK_C,CK_B,CK_LOW
    else:
        raise ValueError('Unknown tableau')
    ts = np.asarray(times, dtype=float)
    if len(ts)<1 or not np.all(np.diff(ts)>0):
        raise ValueError('Strictly increasing sample times required')
    y = np.array(y0, dtype=float, copy=True)
    context=dict(budget.active)
    t = float(ts[0]); h = float(first_step)
    out = [y.copy()]; accepted = rejected = nfev = 0
    for target in ts[1:]:
        while t < target:
            budget.own(**{**context,'reference_t':t,'reference_target':float(target),'last_accepted_state':y,
                'reference_samples':out,'reference_sample_times':ts[:len(out)],'reference_nfev':nfev,'reference_method':method})
            budget.tick('reference_attempt')
            hh = min(h, float(target)-t)
            if not hh > 0 or t+hh == t:
                raise FloatingPointError('Reference step stagnation')
            if nfev+len(c)>max_nfev:
                raise RuntimeError('Fixed reference RHS cap exhausted')
            ks=[]
            for ci, ai in zip(c,a):
                z=y.copy()
                for aj,kj in zip(ai,ks):
                    z += hh*aj*kj
                budget.own(**{**context,'reference_t':t,'reference_target':float(target),'last_accepted_state':y,
                    'stage_state':z,'stage_time':t+ci*hh,'reference_samples':out,'reference_sample_times':ts[:len(out)],
                    'reference_nfev':nfev,'reference_method':method})
                ks.append(np.asarray(fun(t+ci*hh,z), dtype=float))
                nfev += 1; budget.tick('reference_rhs')
            yn=y.copy(); err=np.zeros_like(y)
            for bj,lj,kj in zip(b,low,ks):
                yn += hh*bj*kj; err += hh*(bj-lj)*kj
            budget.augment(candidate_state=yn,candidate_embedded_error=err)
            if not np.all(np.isfinite(yn)) or not np.all(np.isfinite(err)):
                raise FloatingPointError('Nonfinite independent reference stage')
            scale=np.asarray(atol)+rtol*np.maximum(np.abs(y),np.abs(yn))
            en=float(np.max(np.abs(err)/scale))
            if en <= 1:
                y=yn; t=float(target) if hh==float(target)-t else t+hh
                accepted+=1
            else:
                rejected+=1
            h=hh*(5.0 if en==0 else min(5.0,max(.2,.9*en**(-.2))))
            budget.augment(reference_t=t,reference_target=float(target),reference_state=y,reference_nfev=nfev,
                           reference_method=method,reference_samples=out,reference_sample_times=ts[:len(out)])
        out.append(y.copy())
    return np.stack(out), {'method':method,'accepted':accepted,'rejected':rejected,'nfev':nfev,
                           'rtol':rtol,'atol':plain(np.asarray(atol)),'complete':True}


def maxerr(a,b):
    return float(np.max(np.abs(np.asarray(a)-np.asarray(b))))


def order(e1,e2, floor=1e-14):
    if not e1>floor or not e2>floor:
        return None
    return math.log(e1/e2,2)


def empirical_cdf_error(values, cdf):
    x=np.sort(np.asarray(values,dtype=float)); n=len(x)
    f=np.array([cdf(float(v)) for v in x])
    return float(max(np.max(np.arange(1,n+1)/n-f), np.max(f-np.arange(n)/n)))


def normal_cdf(x):
    return .5*math.erfc(-float(x)/math.sqrt(2))


def gamma_half_cdf(x, dof):
    """CDF of K=chi2(dof)/2 for integer dof1,2,3 (unit T)."""
    if x<=0:
        return 0.0
    if dof==1:
        return math.erf(math.sqrt(x))
    if dof==2:
        return -math.expm1(-x)
    if dof==3:
        return math.erf(math.sqrt(x))-2*math.sqrt(x/math.pi)*math.exp(-x)
    raise ValueError('Only f1/2/3 declared')


def corr(x,y):
    x=np.asarray(x);y=np.asarray(y)
    xc=x-np.mean(x);yc=y-np.mean(y)
    vx=float(np.mean(xc*xc));vy=float(np.mean(yc*yc));cov=float(np.mean(xc*yc))
    def rms(z):
        scale=float(np.max(np.abs(z)))
        return 0. if scale==0 else scale*math.sqrt(float(np.mean((z/scale)**2)))
    # Heuristic numerical-resolution diagnostic, not a physical mixing threshold.
    floorx=(64*np.finfo(float).eps*max(1.,rms(x)))**2
    floory=(64*np.finfo(float).eps*max(1.,rms(y)))**2
    reason='zero_variance' if vx==0 or vy==0 else 'roundoff_limited_variance' if vx<=floorx or vy<=floory else None
    return {'raw_product':float(np.mean(x*y)),'centered_product':cov,'variance_x':vx,'variance_y':vy,
            'variance_resolution_floor_x':floorx,'variance_resolution_floor_y':floory,
            'correlation':None if reason else cov/math.sqrt(vx*vy),'null_reason':reason,
            'resolution_scope':'heuristicbinary64resolutiononly,notphysicalmixingproof'}
