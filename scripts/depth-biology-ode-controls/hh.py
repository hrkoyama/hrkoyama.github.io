"""Pinned analytic-rate HH controls; no NEURON runtime/TABLE equivalence claim."""
from __future__ import annotations
from decimal import Decimal, localcontext
import math
import numpy as np
from common import adaptive, maxerr, order, rk4


def rates(v):
    def trap(x,y):
        return y if x==0 else x/math.expm1(x/y)
    return np.array([.1*trap(-(v+40),10),4*math.exp(-(v+65)/18),
                     .07*math.exp(-(v+65)/20),1/(math.exp(-(v+35)/10)+1),
                     .01*trap(-(v+55),10),.125*math.exp(-(v+65)/80)])


def rhs(y, current):
    v,m,h,n=y
    a,b,c,d,e,f=rates(float(v))
    return np.array([current-120*m**3*h*(v-50)-36*n**4*(v+77)-.3*(v+54.3),
                     a*(1-m)-b*m,c*(1-h)-d*h,e*(1-n)-f*n])


def reference_rhs(t,y,current):
    """Separate scalar formulation; never calls primary rate/current helpers."""
    v,m,h,n=map(float,y)
    xm=v+40;xn=v+55
    am=1.0 if xm==0 else .1*xm/(-math.expm1(-xm/10))
    an=.1 if xn==0 else .01*xn/(-math.expm1(-xn/10))
    bm=4*math.exp((-65-v)/18)
    ah=.07*math.exp((-65-v)/20)
    bh=1/(1+math.exp((-35-v)/10))
    bn=.125*math.exp((-65-v)/80)
    ina=(120*(m*m*m)*h)*(v-50)
    ik=(36*(n*n)*(n*n))*(v+77)
    il=.3*(v-(-54.3))
    return np.array([current-(ina+ik+il),am-(am+bm)*m,ah-(ah+bh)*h,an-(an+bn)*n])


def decimal_rates(v, precision):
    with localcontext() as c:
        c.prec=precision
        v=Decimal.from_float(float(v)) if not isinstance(v,Decimal) else v
        one=Decimal(1)
        def alpha(x,factor,limit):
            return Decimal(limit) if not x else Decimal(factor)*x/(one-(-x/10).exp())
        return [alpha(v+40,'.1','1'),4*((-v-65)/18).exp(),
                Decimal('.07')*((-v-65)/20).exp(),one/(one+((-v-35)/10).exp()),
                alpha(v+55,'.01','.1'),Decimal('.125')*((-v-65)/80).exp()]


def decimal_rest(precision):
    with localcontext() as ctx:
        ctx.prec=precision
        def balance(v):
            a,b,c,d,e,f=decimal_rates(v,precision)
            m=a/(a+b);h=c/(c+d);n=e/(e+f)
            return 120*m**3*h*(v-50)+36*n**4*(v+77)+Decimal('.3')*(v+Decimal('54.3'))
        lo=Decimal(-80);hi=Decimal(-50)
        fl=balance(lo);fh=balance(hi)
        if not fl*fh<0:raise ValueError('Rest root not bracketed')
        count=0
        while hi-lo>Decimal('1e-30') and count<256:
            mid=(lo+hi)/2;fm=balance(mid);count+=1
            if fm*fl>0:lo=mid;fl=fm
            else:hi=mid
        if hi-lo>Decimal('1e-30'):raise RuntimeError('Rest bisection cap')
        v=(lo+hi)/2
        a,b,c,d,e,f=decimal_rates(v,precision)
        return np.array(list(map(float,[v,a/(a+b),c/(c+d),e/(e+f)]))), {
            'lo':str(lo),'hi':str(hi),'iterations':count,'endpoint_signs':[str(balance(lo)),str(balance(hi))],
            'precision':precision,'uniqueness_claim':False}


def event_roots(times,states,currents,budget=None,event_rhs=rhs):
    """Inspect every accepted-interval Hermite cubic, not only endpoint sign changes.

    Critical points split each cubic into monotone pieces. This qualifies the
    interpolating polynomial model; it is not an event-completeness theorem for
    the exact continuous ODE between accepted states.
    """
    events=[];audit={'intervals':len(times)-1,'critical_point_intervals':0,
        'interior_crossings_without_endpoint_sign_change':0,
        'nonsimple_or_roundoff_unresolved_intervals':0,'maximum_cubic_roots_per_interval':0,
        'all_intervals_inspected':True,'exact_ODE_event_completeness_certified':False}
    previous_current=None;previous_fb=None
    for j in range(len(times)-1):
        ya=states[j];yb=states[j+1];dt=float(times[j+1]-times[j]);current=currents[j]
        if not dt>0:raise ValueError('Positive accepted event interval required')
        if previous_fb is not None and current==previous_current:fa=previous_fb
        else:
            fa=float(event_rhs(ya,current)[0])
            if budget:budget.tick('hh_event_endpoint_rhs')
        fb=float(event_rhs(yb,current)[0]);previous_fb=fb;previous_current=current
        if budget:budget.tick('hh_event_endpoint_rhs')
        a=2*ya[0]-2*yb[0]+dt*(fa+fb)
        b=-3*ya[0]+3*yb[0]-dt*(2*fa+fb)
        c=dt*fa;d=float(ya[0])
        if not all(math.isfinite(float(v)) for v in [a,b,c,d]):
            if budget:budget.own(case='HH-event',interval=j,left_state=ya,right_state=yb,coefficients=np.array([a,b,c,d]))
            raise FloatingPointError('Nonfinite event cubic')
        def poly(s):return ((a*s+b)*s+c)*s+d
        def slope(s):return ((3*a*s+2*b)*s+c)/dt
        A=3*a;B=2*b;C=c;critical=[]
        if A==0:
            if B!=0:critical=[-C/B]
        else:
            disc=B*B-4*A*C
            if disc>=0:
                root=math.sqrt(disc)
                q=-.5*(B+math.copysign(root,B))
                critical=[-B/(2*A)] if q==0 else [q/A,C/q]
        critical=sorted(set(float(x) for x in critical if 0<x<1))
        if critical:audit['critical_point_intervals']+=1
        knots=[0.,*critical,1.];values=[poly(x) for x in knots]
        guard=64*np.finfo(float).eps*(1+abs(a)+abs(b)+abs(c)+abs(d))
        unresolved=any(abs(poly(x))<=guard for x in critical)
        up=[];crossings=0
        for ka,kb,va,vb in zip(knots[:-1],knots[1:],values[:-1],values[1:]):
            if va<0<=vb:
                crossings+=1;lo=ka;hi=kb;calls=0
                while (hi-lo)*dt>1e-10 and calls<80:
                    mid=(lo+hi)/2
                    if poly(mid)<0:lo=mid
                    else:hi=mid
                    calls+=1
                ss=(lo+hi)/2;der=slope(ss)
                up.append({'time_ms':float(times[j]+ss*dt),'bracket':[float(times[j]+ka*dt),float(times[j]+kb*dt)],
                    'accepted_interval':[float(times[j]),float(times[j+1])],'slope':float(der),
                    'simple_upward':bool(der>0),'polynomial_evaluations':calls,
                    'endpoint_rhs':'fresh accepted endpoint or reused same-current accepted derivative',
                    'model':'accepted-interval cubic Hermite, not an exact-ODE event certificate'})
            elif va>=0>vb:crossings+=1
        if unresolved:audit['nonsimple_or_roundoff_unresolved_intervals']+=1
        if crossings and not (ya[0]<0<=yb[0] or ya[0]>=0>yb[0]):
            audit['interior_crossings_without_endpoint_sign_change']+=crossings
        audit['maximum_cubic_roots_per_interval']=max(audit['maximum_cubic_roots_per_interval'],crossings)
        events.extend(up)
        if len(events)>8:raise RuntimeError('Fixed event cap exceeded')
    return events,audit

def primary_trace(y0,h,end,pulse,budget):
    count=int(round(end/h));times=np.arange(count+1)*h;y=y0.copy();out=[y.copy()];curr=[]
    for k in range(count):
        # Own entire RK interval by integer segment key, including its right-end stage.
        t=k*h;current=10. if pulse and 10<=t<11 else 0.
        budget.tick('hh_primary_step');budget.tick('hh_primary_rhs',4)
        budget.own(case='HH',step=k,time=t,state=y,segment_current=current)
        previous=y
        y=rk4(lambda tt,z:rhs(z,current),t,y,h,budget)
        budget.augment(last_accepted_state=previous,candidate_state=y,stage='RK4acceptedcandidate')
        if not np.all(np.isfinite(y)):raise FloatingPointError('Nonfinite HH state')
        out.append(y.copy());curr.append(current)
    return times,np.stack(out),curr


def qualify(budget):
    voltages=[-120.,-80.,-65.,-55.,-40.,0.,80.]
    voltages += [base+delta for base in [-55.,-40.] for delta in [-1e-4,1e-4,-1e-8,1e-8]]
    rate_errors=[];precision_differences=[]
    for v in voltages:
        budget.tick('hh_rate_probe')
        p=rates(v);r80=decimal_rates(v,80);r120=decimal_rates(v,120)
        rate_errors.append(maxerr(p,list(map(float,r120))))
        precision_differences.append(maxerr(list(map(float,r80)),list(map(float,r120))))
    edge=[]
    for h in [.04,.02,.01]:
        for ta,owned in [(10-h,0),(10,10),(11-h,10),(11,0)]:
            stage_currents=[owned]*4
            # Pulse-only scalar component has no ionic contribution.
            actual=h*(stage_currents[0]+2*stage_currents[1]+2*stage_currents[2]+stage_currents[3])/6
            naive=[10. if 10<=ta+c*h<11 else 0. for c in [0,.5,.5,1]]
            naive_delta=h*(naive[0]+2*naive[1]+2*naive[2]+naive[3])/6
            edge.append({'h':h,'t':ta,'stage_currents':stage_currents,'increment':actual,
                         'expected':h*owned,'naive_increment':naive_delta})
    rest80,b80=decimal_rest(80);rest,b120=decimal_rest(120)
    # Stability is explicitly unclaimed: no unimplemented interval-Hurwitz certificate.
    checks={'rates_against_decimal':max(rate_errors)<2e-12,
            'precision_companion':max(precision_differences)<1e-13,
            'removable_singularities':rates(-40)[0]==1 and rates(-55)[4]==.1,
            'rest_bracket_companion':maxerr(rest,rest80)<1e-12 and maxerr(rhs(rest,0),np.zeros(4))<1e-10,
            'owned_stage_edges':all(abs(x['increment']-x['expected'])<1e-15 for x in edge),
            'naive_jump_control_detected':sum(abs(x['increment']-x['naive_increment'])>1e-8 for x in edge)>=6}
    return {'checks':checks,'rate_max_errors':rate_errors,'input_v64_hex':[v.hex() for v in voltages],
            'edge_actions':edge,'rest':rest,'root_companions':[b80,b120],
            'stability_status':'UNCLAIMED: bracketed equilibrium, no interval Hurwitz certificate; not a proof of uniqueness'},rest


def run(rec,budget,inputs):
    qual,rest=qualify(budget)
    for k,v in qual['checks'].items():rec.check('HH/'+k,v)
    rec.row('hh-components',qual,rest=rest)
    z0=np.array([.2,.8,.1]);clamp_errors={}
    for v in [-80.,-55.,-40.,0.]:
        rr=rates(v);alpha=rr[::2];lam=rr[::2]+rr[1::2];eq=alpha/lam
        for h in [.04,.02,.01]:
            steps=int(round(5/h));t=np.arange(steps+1)*h;z=z0.copy();ys=[z.copy()]
            for j in range(steps):
                budget.own(case='HH-clamp',V=v,h=h,step=j,state=z)
                budget.tick('hh_clamp_step');budget.tick('hh_primary_rhs',4)
                z=rk4(lambda tt,zz:alpha-lam*zz,t[j],z,h,budget);ys.append(z.copy())
                budget.own(case='HH-clamp',V=v,h=h,step=j,state=z)
            ys=np.stack(ys);truth=eq+(z0-eq)*np.exp(-t[:,None]*lam)
            err=maxerr(ys,truth);clamp_errors[(v,h)]=err
            rec.row('hh-clamp-%s-%s'%(int(v),str(h).replace('.','p')),{'V':v,'h':h,'max_all_time_error':err,
                    'gate_min':float(ys.min()),'gate_max':float(ys.max())},time=t,state=ys,exact=truth)
            rec.check('HH/clamp-finite-bounds/%s/%s'%(v,h),np.all(np.isfinite(ys)) and ys.min()>=-1e-12 and ys.max()<=1+1e-12)
        rec.goal('HH/clamp-original1e-8/%s'%v,clamp_errors[(v,.01)]<=1e-8,actual=clamp_errors[(v,.01)],target=1e-8,
                 scope='Maximum over ALL accepted times and all three gates; unmet outcomes retained')
    refs={};ref_ledgers={}
    for mode,end,segments in [('rest',20.,[(0.,20.,0.)]),('pulse',30.,[(0.,10.,0.),(10.,11.,10.),(11.,30.,0.)])]:
        companions=[];ledgers=[]
        for cfg in inputs['HH_reference_rows']:
            y=rest.copy();all_y=[y.copy()];all_t=[0.];currents=[];ledger=[]
            for lo,hi,current in segments:
                ts=np.linspace(lo,hi,int(round((hi-lo)/.01))+1)
                budget.own(case='HH-reference',mode=mode,method=cfg['method'],rtol=cfg['rtol'],segment=[lo,hi],current=current)
                yy,ll=adaptive(lambda t,z:reference_rhs(t,z,current),y,ts,budget,
                               cfg['rtol'],cfg['atol'],50000,cfg['method'],first_step=.001)
                all_y.extend(yy[1:]);all_t.extend(ts[1:]);currents.extend([current]*(len(ts)-1));y=yy[-1]
                ledger.append({'segment':[lo,hi],'current':current,**ll})
            companions.append(np.stack(all_y));ledgers.append(ledger)
        spread=max(maxerr(companions[0],companions[1]),maxerr(companions[2],companions[1]))
        qualified=spread<=1e-7
        rec.check('HH/reference/'+mode,qualified)
        tref=np.array(all_t)
        events,event_audit=event_roots(tref,companions[1],currents,budget,lambda z,I:reference_rhs(0,z,I)) if mode=='pulse' else ([],{})
        refs[mode]=(companions[1],events,qualified,spread)
        rec.row('hh-reference-'+mode,{'spread':spread,'qualified':qualified,'configurations':ledgers,'events':events,'event_audit':event_audit},
                time=tref,state=companions[1],reference0=companions[0],reference2=companions[2])
        for h in [.04,.02,.01]:
            t,ys,owned=primary_trace(rest,h,end,mode=='pulse',budget)
            # All canonical h are exact integer multiples of the reference0.01 key.
            target=companions[1][::int(round(h/.01))]
            err=np.max(np.abs(ys-target),axis=0)
            ev,primary_audit=event_roots(t,ys,owned,budget) if mode=='pulse' else ([],{})
            rec.row('hh-'+mode+'-'+str(h).replace('.','p'),{'h':h,'errors':err,'events':ev,'event_audit':primary_audit,
                    'rest_drift_mV':float(np.max(np.abs(ys[:,0]-rest[0]))),'gate_range':[float(ys[:,1:].min()),float(ys[:,1:].max())]},time=t,state=ys,reference=target)
            rec.check('HH/finite-gates/'+mode+'/'+str(h),np.all(np.isfinite(ys)) and ys[:,1:].min()>=-1e-12 and ys[:,1:].max()<=1+1e-12)
            if mode=='rest':rec.goal('HH/rest/'+str(h),bool(np.max(np.abs(ys[:,0]-rest[0]))<=1e-7),target_mV=1e-7)
            elif h==.01:
                rec.goal('HH/pulse-voltage',bool(err[0]<=.05) if qualified else None,actual=float(err[0]),target=.05,reference_spread=spread)
                rec.goal('HH/pulse-gates',bool(err[1:].max()<=1e-4) if qualified else None,actual=float(err[1:].max()),target=1e-4)
                eligible=qualified and len(ev)==len(events)==1 and ev[0]['simple_upward'] and events[0]['simple_upward'] and primary_audit['nonsimple_or_roundoff_unresolved_intervals']==0 and event_audit['nonsimple_or_roundoff_unresolved_intervals']==0
                eventerr=abs(ev[0]['time_ms']-events[0]['time_ms']) if eligible else None
                rec.goal('HH/pulse-event',eventerr<=.01 if eligible else None,actual_ms=eventerr,target_ms=.01,reason=None if eligible else 'reference/missing/multiple/nonsimple event',scope='ObservedHermiteeventcomparison;exactODEeventcompletenessnotcertified')
