"""Immigration--death SSA, exact finite-time laws and directed Decimal references."""
from __future__ import annotations
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
import bisect
import math
import numpy as np
from common import maxerr


class I:
    """Positive directed interval operations; Decimal.exp is correctly rounded first."""
    precision=80
    def __init__(self,lo,hi=None):
        self.lo=D(lo);self.hi=D(lo if hi is None else hi)
        if self.lo>self.hi:raise ValueError('Reversed interval')
    @staticmethod
    def cast(x):return x if isinstance(x,I) else I(x)
    def __add__(self,other):
        b=I.cast(other)
        with localcontext() as c:
            c.prec=I.precision;c.rounding=ROUND_FLOOR;lo=self.lo+b.lo
            c.rounding=ROUND_CEILING;hi=self.hi+b.hi
        return I(lo,hi)
    __radd__=__add__
    def __sub__(self,other):
        b=I.cast(other)
        with localcontext() as c:
            c.prec=I.precision;c.rounding=ROUND_FLOOR;lo=self.lo-b.hi
            c.rounding=ROUND_CEILING;hi=self.hi-b.lo
        return I(lo,hi)
    def __rsub__(self,other):return I.cast(other)-self
    def __mul__(self,other):
        b=I.cast(other)
        if self.lo<0 or b.lo<0:raise ValueError('Only nonnegative interval products')
        with localcontext() as c:
            c.prec=I.precision;c.rounding=ROUND_FLOOR;lo=self.lo*b.lo
            c.rounding=ROUND_CEILING;hi=self.hi*b.hi
        return I(lo,hi)
    __rmul__=__mul__
    def __truediv__(self,other):
        b=I.cast(other)
        if self.lo<0 or b.lo<=0:raise ValueError('Positive division only')
        with localcontext() as c:
            c.prec=I.precision;c.rounding=ROUND_FLOOR;lo=self.lo/b.hi
            c.rounding=ROUND_CEILING;hi=self.hi/b.lo
        return I(lo,hi)
    def exp(self):
        with localcontext() as c:
            c.prec=I.precision
            # exp ignores directed rounding; adjacent representables enclose it.
            lo=self.lo.exp().next_minus();hi=self.hi.exp().next_plus()
        return I(lo,hi)


class Factor:
    def __init__(self,weights,lower_tail,upper_tail):
        self.low=min(weights);self.high=max(weights);self.weights=weights
        total=sum(weights.values(),I(0));tails=lower_tail+upper_tail
        self.total=total;self.tail=tails/(total+tails)
        self.pm={k:I(w.lo,w.hi)/I(total.lo,(total+tails).hi) for k,w in weights.items()}
        self.prefix=[];prefix=I(0)
        for k in range(self.low,self.high+1):
            prefix=prefix+weights[k]
            lo=(prefix/I(total.lo,(total+tails).hi)).lo
            hi=((prefix+lower_tail)/total).hi
            self.prefix.append(I(max(D(0),lo),min(D(1),hi)))
        self.lower_probability=(lower_tail/I(total.lo,(total+tails).hi)).hi
    def cdf(self,k):
        if k<self.low:return I(0,self.lower_probability)
        if k>=self.high:return I(self.prefix[-1].lo,1)
        return self.prefix[k-self.low]


def factor(kind,param,p=None,target='1e-25',budget=None):
    """Mode-centred relative weights, finite tails and explicit2048halfwidth cap."""
    if budget:
        budget.augment(reference_factor_kind=kind,reference_factor_parameter=[str(param.lo),str(param.hi)] if isinstance(param,I) else str(param),
                       reference_factor_p=None if p is None else [str(I.cast(p).lo),str(I.cast(p).hi)],reference_factor_tail_target=target,reference_factor_precision=I.precision)
    if kind=='point':return Factor({int(param):I(1)},I(0),I(0))
    if kind=='poisson':
        mu=I.cast(param);mode=int(mu.lo)
        if mu.hi==0:return Factor({0:I(1)},I(0),I(0))
        def upper(k):return mu/(k+1)
        def lower(k):return I(k)/mu
    else:
        n=int(param);p=I.cast(p);q=1-p
        if p.lo<=0 or p.hi>=1:raise ValueError('Nondegenerate binomial required')
        mode=int((n+1)*p.lo)
        def upper(k):return (n-k)*p/((k+1)*q) if k<n else I(0)
        def lower(k):return k*q/((n-k+1)*p) if k>0 else I(0)
    weights={mode:I(1)};lo=hi=mode;lt=ut=I(1)
    for width in range(2049):
        if budget:
            budget.augment(reference_factor_center=mode,reference_factor_lower=lo,reference_factor_upper=hi,retained_weight_count=len(weights))
            try:budget.tick('ssa_reference_weight_round')
            except Exception:
                budget.augment(retained_relative_weights={str(k):[str(v.lo),str(v.hi)] for k,v in weights.items()},
                               lower_tail_weight=[str(lt.lo),str(lt.hi)],upper_tail_weight=[str(ut.lo),str(ut.hi)])
                raise
        total=sum(weights.values(),I(0)) if width%8==0 else None
        if lo==0:lt=I(0)
        else:
            nxt=weights[lo]*lower(lo);ratio=lower(lo-1)
            lt=nxt/(1-ratio) if ratio.hi<1 else I(0,D('1e100'))
        if kind=='binomial' and hi==int(param):ut=I(0)
        else:
            nxt=weights[hi]*upper(hi);ratio=upper(hi+1)
            ut=nxt/(1-ratio) if ratio.hi<1 else I(0,D('1e100'))
        if total is not None and ((lt+ut)/total).hi<D(target):
            return Factor(weights,lt,ut)
        if width==2048:break
        if lo>0:weights[lo-1]=weights[lo]*lower(lo);lo-=1
        if kind!='binomial' or hi<int(param):weights[hi+1]=weights[hi]*upper(hi);hi+=1
    raise RuntimeError('Directed law fixed halfwidth cap exhausted')


class Law:
    def __init__(self,n0,t,scale,budget):
        self.budget=budget
        budget.own(case='SSA-exact-law-reference',initial_law=n0,time=t,scale=scale,precision=I.precision)
        if n0=='stationary':
            self.b=factor('point',0);self.p=factor('poisson',I(6*scale),budget=budget)
        else:
            pp=I(-D(str(t))).exp()
            self.b=factor('point',0) if not n0 or t==0 else factor('binomial',int(n0)*scale,pp,budget=budget)
            if t==0:self.b=factor('point',int(n0)*scale)
            self.p=factor('poisson',6*scale*(1-pp),budget=budget)
        self.low=self.b.low+self.p.low;self.high=self.b.high+self.p.high
        self.cache={}
    def cdf(self,k):
        k=int(k)
        self.budget.augment(reference_CDF_argument=k)
        if k in self.cache:return self.cache[k]
        if k<0:return I(0)
        lo=I(0)
        for j,p in self.b.pm.items():lo=lo+p*self.p.cdf(k-j)
        # Omitted binomial mass could all be on either side; it never certifies success.
        ans=I(max(D(0),lo.lo),min(D(1),(lo+I(0,self.b.tail.hi)).hi))
        self.cache[k]=ans;return ans
    def bounds(self,tail=D(1)/D(8000)):
        # LargestL with P(X<L)<=tail; smallestU with P(X<=U)>=1-tail.
        lo=0;hi=self.high+1
        while lo<hi:
            mid=(lo+hi+1)//2
            if self.cdf(mid-1).hi<=tail:lo=mid
            else:hi=mid-1
        left=lo;lo=0;hi=self.high
        if self.cdf(hi).lo<1-tail:raise RuntimeError('Reference support cannot qualify upper tail')
        while lo<hi:
            mid=(lo+hi)//2
            if self.cdf(mid).lo>=1-tail:hi=mid
            else:lo=mid+1
        return left,lo
    def summary(self):
        return {'support':[self.low,self.high],'omitted_factor_tail_bounds':[str(self.b.tail.hi),str(self.p.tail.hi)],
                'precision':I.precision,'CDF_width_max':str(max((v.hi-v.lo for v in self.cache.values()),default=D(0)))}


def initial_table(budget):
    tables=[]
    for precision in [80,120]:
        I.precision=precision
        budget.own(case='SSA-initial-Poisson-table-reference',precision=precision,table_max_count=128)
        f=factor('poisson',I(6),target='1e-50',budget=budget);table=[]
        for k in range(129):
            x=f.cdf(k)
            with localcontext() as c:
                c.prec=precision
                a=int((x.lo*(1<<53)).to_integral_value(rounding=ROUND_CEILING))-1
                b=int((x.hi*(1<<53)).to_integral_value(rounding=ROUND_CEILING))-1
            if a!=b:raise RuntimeError('Poisson initialization integer threshold unresolved')
            table.append(a)
        tables.append(table)
    if tables[0]!=tables[1] or tables[1][-1]<(1<<53)-1:raise RuntimeError('InitialCDF companion failed')
    I.precision=80
    return tables[0]


def state_record(bitgen):
    s=bitgen.state['state']
    return [str(s['state']),str(s['inc'])]


class Stream:
    def __init__(self,record,seed,path,purpose,budget):
        self.key=[20261125,89,record,seed,path,purpose]
        self.g=np.random.PCG64(np.random.SeedSequence(self.key));self.initial=state_record(self.g)
        self.raw=0;self.rejections=0;self.budget=budget
    def u(self):
        for _ in range(8):
            self.raw+=1;self.budget.tick('ssa_raw_uint64')
            j=int(self.g.random_raw())>>11
            if j:
                return j*2.0**-53,j
            self.rejections+=1
        raise RuntimeError('Open-uniform zero-grid rejection cap')
    def ledger(self):
        return {'entropy':self.key,'initial':self.initial,'final':state_record(self.g),
                'raw_uint64':self.raw,'zero_rejections':self.rejections}


def choose_reaction(u,n):
    return 1 if u*(6+n)<6 else -1


def path(n0,observations,event_stream,budget,full=False,context=None):
    n=int(n0);t=0.;pending=None;sample=[];history=[[0.,n]];jumps=0;generated=0
    for obs in observations:
        while True:
            if pending is None:
                u1,_=event_stream.u();u2,_=event_stream.u();total=6+n
                tau=-math.log(u1)/total
                te=t+tau
                if not math.isfinite(te) or te==t:
                    budget.own(**{**(context or {}),'case':'SSA-failed-clock','last_accepted_time':t,'candidate_time':te,'count':n,'waiting_time':tau,'observation':obs})
                    raise FloatingPointError('SSA event time stagnation')
                kind=choose_reaction(u2,n)
                if n==0 and kind<0:raise AssertionError('Death from zero')
                pending=(te,kind);generated+=1
            if pending[0]>obs:break
            t,kind=pending;n+=kind;pending=None;jumps+=1
            budget.tick('ssa_accepted_jump')
            if jumps>4096:raise RuntimeError('SSA per-path jump cap')
            if n<0:raise AssertionError('Negative molecular count')
            if full:history.append([t,n])
            budget.own(**{**(context or {}),'case':'SSA','time':t,'count':n,'observation':obs,'jumps':jumps})
        sample.append(n)
    return sample,{'jumps':jumps,'pending_generated':generated,'censored_pending':pending,
                   'censored_events_apply_only_if_time_le_T':True},history


def components(budget,table):
    # Pure scheduling fixture: a pending event exactly on an observation is applied once.
    class Fixed:
        def __init__(self,vals):self.vals=iter(vals);self.calls=0
        def u(self):self.calls+=1;return next(self.vals),1
    f=Fixed([math.exp(-6*.5),.1,math.exp(-7*10),.1])
    edge_time=-math.log(math.exp(-6*.5))/6
    vals,ledger,_=path(0,[0,.25,edge_time,1],f,budget)
    right=vals==[0,0,1,1] and f.calls==4 and ledger['jumps']==1
    # Two observations before a pending event must not draw a fresh clock.
    no_resample=f.calls==4
    return {'pending_boundary_and_censoring':right,'pending_not_redrawn_at_observations':no_resample,
            'initial_inverse_monotone':all(a<=b for a,b in zip(table,table[1:])),
            'open_grid_limits':2.0**-53>0 and ((1<<53)-1)*2.0**-53<1,
            'reaction_equality_is_death':choose_reaction(.5,6)==-1,
            'wrong_stationarity_control':6*(1-math.exp(-.5))!=6}


def run(rec,budget,inputs):
    table=initial_table(budget)
    for k,v in components(budget,table).items():rec.check('SSA/'+k,v)
    # Qualify all seven per-path and seven ensemble-sum laws BEFORE drawing samples.
    keys=[(n,t) for n in [0,5] for t in [.5,2.,4.]]+[('stationary',0.)]
    laws={};law_rows=[]
    for scale in [1,2048]:
        for n,t in keys:
            companions=[];summaries=[]
            for precision in [80,120]:
                I.precision=precision;l=Law(n,t,scale,budget)
                bounds=l.bounds() if scale==2048 else None
                probes=range(l.low,l.high+1) if scale==1 else [max(0,l.low),sum(bounds)//2,*bounds,l.high]
                cs={int(k):(str(l.cdf(k).lo),str(l.cdf(k).hi)) for k in probes}
                summaries.append({'summary':l.summary(),'bounds':bounds,'cdf':cs})
                companions.append(l)
            qualified=(summaries[0]['bounds']==summaries[1]['bounds'] and all(D(b)-D(a)<=D('1e-18') for s in summaries for a,b in s['cdf'].values()))
            rec.check('SSA/law/%s/%s/%s'%(n,t,scale),qualified)
            laws[(n,t,scale)]=companions[-1]
            law_rows.append({'initial':n,'time':t,'scale':scale,'qualified':qualified,'companions':summaries})
    I.precision=120
    rec.row('ssa-exact-law-qualification',{'laws':law_rows,'nominal_ideal_IID_family_failure_bound':.01,
            'family_count':40,'per_family_delta':1/4000,'variance_goals_outside_family':True,
            'software_PRNG_coverage_guarantee':False,'finite_grid_initial_CDF_bound':1/((1<<53)-1)})
    observations=[0.,.5,2.,4.];records=[];all_ledgers=[];family_count=0
    for record in range(6):
        n0=[0,0,5,5,'stationary','stationary'][record];seed=[101,202]*3
        values=np.full((2048,4),-1,dtype=np.int64);initial_counts=np.full(2048,-1,dtype=np.int64);event_count=0
        for j in range(2048):
            context={'case':'SSA-ensemble','record':record,'path_index':j,'completed_counts':values[:j],
                     'completed_initial_counts':initial_counts[:j],'completed_rng_ledgers':all_ledgers}
            budget.own(**context)
            init=Stream(record,seed[record],j,0,budget);ev=Stream(record,seed[record],j,1,budget)
            try:
                if n0=='stationary':
                    _,rawj=init.u();start=bisect.bisect_left(table,rawj)
                    if start>128:raise RuntimeError('Frozen initialization table uncovered draw')
                else:start=n0
                out,ledger,_=path(start,observations,ev,budget,context=context)
            except Exception:
                budget.augment(current_initial_stream=init.ledger(),current_event_stream=ev.ledger())
                raise
            values[j]=out;initial_counts[j]=start;event_count+=ledger['jumps']
            if event_count>1000000:raise RuntimeError('SSA per-record jump cap')
            if budget.counts.get('ssa_raw_uint64',0)>17000000:raise RuntimeError('SSA global raw draw cap')
            all_ledgers.append({'record':record,'path':j,'init':init.ledger(),'events':ev.ledger(),**ledger})
        a=np.array(values,dtype=np.int64);diagnostics=[]
        for it,t in enumerate(observations):
            if t==0 and n0!='stationary':
                deterministic=bool(np.all(a[:,it]==n0));rec.check('SSA/t0/'+str(record),deterministic)
                diagnostics.append({'time':t,'deterministic_t0':True,'standardized_variance':None});continue
            key=('stationary',0.) if n0=='stationary' else (n0,t)
            law=laws[(*key,1)];summed=laws[(*key,2048)]
            xs=np.sort(a[:,it]);fs=[]
            for k in range(int(xs.max())+1):
                f=law.cdf(k);emp=float(np.mean(xs<=k));fs.append(max(abs(emp-float(f.lo)),abs(emp-float(f.hi))))
            dkw=max(fs);eps=math.sqrt(math.log(8000)/(2*2048));bounds=summed.bounds();total=int(xs.sum())
            mean_ok=bounds[0]<=total<=bounds[1];dkw_ok=dkw<=eps;family_count+=2
            p=math.exp(-t);mu=6 if n0=='stationary' else n0*p+6*(1-p)
            var=6 if n0=='stationary' else n0*p*(1-p)+6*(1-p)
            kappa4=6 if n0=='stationary' else n0*p*(1-p)*(1-6*p*(1-p))+6*(1-p)
            mu4=kappa4+3*var*var
            variance_se=math.sqrt((mu4-(2045/2047)*var*var)/2048)
            sample_var=float(np.var(xs,ddof=1))
            diagnostics.append({'time':t,'mean':float(xs.mean()),'exact_mean':mu,'variance':sample_var,'exact_variance':var,
                                'DKW_observed':dkw,'DKW_epsilon':eps,'DKW_nominal_pass':dkw_ok,
                                'sum':total,'exact_sum_acceptance_bounds':bounds,'mean_nominal_pass':mean_ok,
                                'variance_estimator_SE_ideal':variance_se,'variance_five_SE_goal':abs(sample_var-var)<=5*variance_se,
                                'precision_scope':'Ideal IID law only; not a rigorous PRNG/logarithm software error bound'})
            rec.goal('SSA/DKW/%s/%s'%(record,it),dkw_ok,actual=dkw,epsilon=eps)
            rec.goal('SSA/exact-mean/%s/%s'%(record,it),mean_ok,sum=total,bounds=bounds)
        rec.row('ssa-ensemble-'+str(record),{'record':record,'initial_law':n0,'seed_label':seed[record],
                'paths':2048,'accepted_jumps':event_count,'diagnostics':diagnostics},time=np.array(observations),counts=a)
    init=Stream(6,11,0,0,budget);ev=Stream(6,11,0,1,budget)
    values,ledger,history=path(5,observations,ev,budget,True)
    rec.row('ssa-display-path',{'initial':5,'seed_label':11,**ledger,'init_stream':init.ledger(),'event_stream':ev.ledger()},
            event_history=np.array(history),observation_time=np.array(observations),counts=np.array(values))
    from common import write_json
    write_json(rec.output/'ssa-rng-ledgers.json',all_ledgers)
    entropy=[tuple(x[k]['entropy']) for x in all_ledgers for k in ['init','events']]
    rec.check('SSA/exact-family-count',family_count==40)
    rec.check('SSA/stream-namespaces-unique',len(entropy)==len(set(entropy))==24576)
    all_streams=[x[k] for x in all_ledgers for k in ['init','events']]+[init.ledger(),ev.ledger()]
    initial_pairs=[tuple(x['initial']) for x in all_streams]
    all_entropy=[tuple(x['entropy']) for x in all_streams]
    rec.check('SSA/all-24578-initial-PCG-state-inc-pairs-unique',len(initial_pairs)==len(set(initial_pairs))==24578)
    rec.check('SSA/all-24578-stream-labels-unique',len(all_entropy)==len(set(all_entropy))==24578)
    rec.row('ssa-stream-state-audit',{'stream_count':len(initial_pairs),'unique_initial_state_inc_pairs':len(set(initial_pairs)),
             'unique_entropy_labels':len(set(all_entropy)),'independence_theorem_claimed':False,'includes_unused_initial_and_display_streams':True})
    rec.check('SSA/all-paths',len(all_ledgers)==12288)
