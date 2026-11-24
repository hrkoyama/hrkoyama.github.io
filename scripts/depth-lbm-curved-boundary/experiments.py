"""Fixed-input LBM cases; scientific gates are supplied by frozen acceptance.json."""
import csv
import json
from pathlib import Path
import numpy as np
from analytic import tgv,annulus,qualify_tgv,qualify_annulus
from diagnostics import (rms,relative,physical,budgets,ghia_tables,cavity_profiles,vortex,
                         cylinder_probes,interval_distance)
from evolution import trajectory,dump
from geometry import build,equilibrium,moments,full_field
from native import Native

IDS={'lbm-cavity':['lbm-cavity-re100'],'lbm-taylor-green':['lbm-taylor-green'],
     'lbm-curved-boundary':['lbm-cylinder-re20'],'lbm-annulus':['lbm-annular-couette-control']}

class Case:
    def __init__(self,ident,out,cases):
        self.out=out;self.data=dict(id=ident,passed=False,checks={},metrics={},records=[],data_files=[]);cases.append(self.data)
    def gate(self,name,value):self.data['checks'][name]=bool(value)
    def bound(self,name,value,limit):self.gate(name,np.isfinite(value) and value<=limit)
    def row(self,value):
        self.data['records'].append(value);dump(self.out/(self.data['id']+'-partial.json'),self.data)
    def finish(self,metrics):
        self.data['metrics']=metrics;self.data['passed']=bool(self.data['records'] and all(self.data['checks'].values()))

def common(case,label,f0,f,h,g,steps,nominal_lattice_speed,ma_limit,expected_time):
    metrics=budgets(f0,f,h,g,nominal_lattice_speed)
    case.gate(label+' finite arrays',np.all(np.isfinite(f)) and np.all(np.isfinite(h)))
    case.gate(label+' positive density',metrics['min_rho']>0)
    case.bound(label+' actual maximum Mach',metrics['max_mach'],ma_limit)
    case.bound(label+' mass ledger',metrics['mass_ledger'],1e-10)
    case.bound(label+' wall-open momentum ledger',metrics['momentum_ledger'],1e-10)
    case.gate(label+' all fixed integer steps',len(h)==steps)
    case.gate(label+' declared physical endpoint',abs(steps*g['dt']-expected_time)<=1e-12*max(1,expected_time))
    return metrics

def numeric_csv(path,rows):
    names=list(rows[0])
    with path.open('w',newline='') as stream:
        w=csv.DictWriter(stream,fieldnames=names);w.writeheader()
        for row in rows:
            if set(row)!=set(names) or not all(isinstance(x,(int,float,np.integer,np.floating)) and np.isfinite(x) for x in row.values()):
                raise ArithmeticError('Nonfinite/ragged numeric CSV row')
            w.writerow(row)

def run_cavity(root,out,inputs,limits,cases,native):
    case=Case('lbm-cavity-re100',out,cases);reference=ghia_tables(root);records=[]
    case.gate('Ghia printed table shape and anchors',all(reference[k].shape==(17,2) for k in ['u','v']) and
              reference['u'][8,1]==-.20581 and reference['v'][7,1]==-.24533)
    for n in inputs['N']:
        lid=inputs['lid_lattice'];nu=lid*n/inputs['Re'];tau=.5+3*nu;dt=lid/n
        g=build('cavity',n,1/n,dt,lid=lid);steps=int(inputs['convective_T']*n/lid)
        checkpoints=[int(t*n/lid) for t in inputs['checkpoints']]
        f0=equilibrium(np.ones(g['n']),np.zeros((2,g['n'])));label='lbm-cavity-re100-N'+str(n)
        f,h,states,arrays=trajectory(native,g,tau,steps,checkpoints,f0,out,label)
        m=common(case,str(n),f0,f,h,g,steps,lid,limits['max_mach'],inputs['convective_T'])
        _,u=moments(f);_,previous=moments(states[checkpoints[-2]])
        stationary=rms(u-previous)/rms(u)
        coordinate,up,vp=cavity_profiles(f,g,lid)
        uat=np.interp(reference['u'][:,0],coordinate,up);vat=np.interp(reference['v'][:,0],coordinate,vp)
        eu=float(np.max(abs(uat-reference['u'][:,1])));ev=float(np.max(abs(vat-reference['v'][:,1])))
        location=vortex(f,g,lid);verr=float(np.linalg.norm(location-np.array([.6172,.7344])))
        case.bound(str(n)+' closed cavity mass',m['mass_drift'],limits['mass_drift'])
        case.bound(str(n)+' late stationarity',stationary,limits['stationarity'])
        case.bound(str(n)+' vortex search residual distance',verr,limits['vortex_all_grids'])
        case.data['data_files'].append(label+'.npz')
        record=dict(n=n,steps=steps,tau=tau,dx=1/n,dt=dt,time=steps*dt,nu_physical=1/inputs['Re'],
                    u_error=eu,v_error=ev,vortex_x=float(location[0]),vortex_y=float(location[1]),
                    vortex_distance=verr,stationarity=stationary,**m)
        records.append(record);case.row(record)
        np.savez_compressed(out/(label+'-profiles.npz'),coordinate=coordinate,u=up,v=vp,
                            u_reference=reference['u'],v_reference=reference['v'],u_at_reference=uat,v_at_reference=vat,
                            vortex=location)
    fine=records[-1]
    case.bound('finest nominal-lid u centerline',fine['u_error'],limits['centerline'])
    case.bound('finest nominal-lid v centerline',fine['v_error'],limits['centerline'])
    case.bound('finest primary vortex',fine['vortex_distance'],limits['vortex_finest'])
    case.gate('u error decreases coarse to fine',fine['u_error']<records[0]['u_error'])
    case.gate('v error decreases coarse to fine',fine['v_error']<records[0]['v_error'])
    case.gate('all three prescribed cavity grids',len(records)==3)
    numeric_csv(out/'lbm-cavity-re100-summary.csv',records)
    case.finish(dict(finest=fine,reference='Ghia1982 printed Re100 tables; limited precision, independent numerical reference'))

def run_tgv(root,out,inputs,limits,cases,native):
    del root
    case=Case('lbm-taylor-green',out,cases);qualification=qualify_tgv()
    for name,value in qualification.items():case.bound('analytic reference '+name,value,2e-12)
    dump(out/'tgv-reference-qualification.json',qualification)
    specs=[dict(n=n,U=inputs['U'],ratio=.2,code=0) for n in inputs['N']]
    specs.extend(dict(n=32,U=U,ratio=.2,code=1) for U in inputs['amplitude_U'])
    specs.append(dict(n=32,U=.2,ratio=.1,code=2));records=[]
    for index,spec in enumerate(specs):
        n,U,ratio=spec['n'],spec['U'],spec['ratio'];dx=2*np.pi/n;dt=ratio*dx*dx;nu=inputs['nu']
        tau=.5+3*nu*ratio;steps=n*n//4 if ratio==.2 else n*n//2
        g=build('periodic',n,dx,dt);a0=tgv(g['x'],g['y'],0,U,nu)
        rho=1+3*(dt/dx)**2*a0['p'];f0=equilibrium(rho,np.array([a0['u'],a0['v']])*dt/dx)
        label='lbm-taylor-green-run'+str(index);checkpoints=[steps//4,steps//2,3*steps//4,steps]
        f,h,states,arrays=trajectory(native,g,tau,steps,checkpoints,f0,out,label)
        m=common(case,str(index),f0,f,h,g,steps,U*dt/dx,limits['max_mach'],inputs['T_over_pi2']*np.pi**2)
        rho,u,p=physical(f,g);exact=tgv(g['x'],g['y'],steps*dt,U,nu)
        target=np.array([exact['u'],exact['v']]);velocity_error=relative(u,target)
        pressure_error=relative(p,exact['p']);energy=float(np.mean(np.sum(u*u,axis=0))/2)
        ux=full_field(u[0],g);uy=full_field(u[1],g)
        div=(np.roll(ux,-1,1)-np.roll(ux,1,1)+np.roll(uy,-1,0)-np.roll(uy,1,0))/(2*dx)
        divergence=rms(div)/U;energy_error=abs(energy-exact['energy'])/exact['energy']
        meanmoment=max(abs(m['final_lattice_momentum_x']),abs(m['final_lattice_momentum_y']))/(g['n']*U*dt/dx)
        case.bound(str(index)+' periodic mass',m['mass_drift'],limits['mass_drift'])
        case.bound(str(index)+' zero mean momentum',meanmoment,limits['mean_momentum'])
        case.bound(str(index)+' normalized divergence',divergence,limits['divergence'])
        case.bound(str(index)+' mean kinetic energy',energy_error,limits['energy'])
        record=dict(run=index,configuration_code=spec['code'],n=n,U=U,steps=steps,dx=dx,dt=dt,tau=tau,
                    time=steps*dt,nu=nu,velocity_error=velocity_error,pressure_error=pressure_error,
                    energy=energy,energy_error=energy_error,divergence=divergence,mean_momentum=meanmoment,**m)
        records.append(record);case.row(record);case.data['data_files'].append(label+'.npz')
        times=[];energies=[];errors=[]
        for k,state in states.items():
            rr,uu,pp=physical(state,g);a=tgv(g['x'],g['y'],k*dt,U,nu)
            times.append(k*dt);energies.append(float(np.mean(np.sum(uu*uu,axis=0))/2))
            errors.append(relative(uu,np.array([a['u'],a['v']])))
        np.savez_compressed(out/(label+'-diagnostics.npz'),u=u,p=p,exact_u=target,exact_p=exact['p'],
                            snapshot_times=np.array(times),energy=np.array(energies),velocity_errors=np.array(errors),
                            exact_energy=np.array([tgv(g['x'],g['y'],t,U,nu)['energy'] for t in times]))
    order=np.log(records[1]['velocity_error']/records[2]['velocity_error'])/np.log(2)
    case.bound('finest combined velocity error',records[2]['velocity_error'],limits['velocity'])
    case.bound('finest pressure gauge error',records[2]['pressure_error'],limits['pressure'])
    case.gate('combined finest velocity order',np.isfinite(order) and order>=limits['combined_order'])
    case.gate('first diffusive refinement decreases velocity',records[1]['velocity_error']<records[0]['velocity_error'])
    case.gate('second diffusive refinement decreases velocity',records[2]['velocity_error']<records[1]['velocity_error'])
    case.gate('same physical endpoint all six runs',max(r['time'] for r in records)-min(r['time'] for r in records)<1e-13)
    case.gate('amplitude probes change actual Mach',records[4]['max_mach']>records[3]['max_mach']>records[1]['max_mach'])
    case.gate('exactly six distinct prescribed runs',len(records)==6)
    numeric_csv(out/'lbm-taylor-green-summary.csv',records)
    case.finish(dict(combined_velocity_order=float(order),reference_qualification=qualification,
                     scope='Diffusive grid/time/Mach refinement, amplitude/Re sensitivity, and coupled dt/Mach/tau probe; no pure time or pure Mach order.'))

def run_annulus(root,out,inputs,limits,cases,native):
    del root
    case=Case('lbm-annular-couette-control',out,cases);qualification=qualify_annulus()
    for name,value in qualification.items():case.bound('analytic reference '+name,value,2e-12)
    dump(out/'annular-reference-qualification.json',qualification);records=[]
    for variant in [0,1]:
        for n in inputs['N']:
            dx=1/n;tau=inputs['tau'];dt=(tau-.5)/3*dx*dx/inputs['nu'];steps=3*n*n//5
            g=build('annulus',n,dx,dt,inner_speed=inputs['inner_speed'],stair=bool(variant),interpolation_order=2)
            exact=annulus(g['x'],g['y']);p=exact['p']-np.mean(exact['p'])
            rho=1+3*(dt/dx)**2*p;f0=equilibrium(rho,np.array([exact['u'],exact['v']])*dt/dx)
            checkpoints=[3*steps//4,7*steps//8,steps];label=f'lbm-annular-couette-control-v{variant}-N{n}'
            f,h,states,arrays=trajectory(native,g,tau,steps,checkpoints,f0,out,label)
            m=common(case,f'{variant}-{n}',f0,f,h,g,steps,inputs['inner_speed']*dt/dx,limits['max_mach'],inputs['T'])
            rho,u,p=physical(f,g);_,prev_u,prev_p=physical(states[checkpoints[-2]],g)
            error=relative(u,np.array([exact['u'],exact['v']]))
            pressure_error=relative(p,exact['p']-np.mean(exact['p']))
            force_scale=dx**4/dt**2
            torque=float(np.mean(h[checkpoints[-2]:,8]))*force_scale
            torque_prev=float(np.mean(h[checkpoints[-3]:checkpoints[-2],8]))*force_scale
            torque_error=abs(torque-exact['torque'])/abs(exact['torque'])
            stationary=relative(u,prev_u);torque_drift=abs(torque-torque_prev)/abs(exact['torque'])
            prefix=f'{variant}-{n}'
            case.bound(prefix+' total mass drift diagnostic bound',m['mass_drift'],limits['mass_drift'])
            case.bound(prefix+' late velocity stationarity',stationary,limits['stationarity'])
            case.bound(prefix+' late torque stationarity',torque_drift,limits['torque_stationarity'])
            case.gate(prefix+' correct inner resisting torque sign',torque<0)
            record=dict(variant=variant,n=n,steps=steps,dx=dx,dt=dt,time=steps*dt,tau=tau,nu=inputs['nu'],
                        velocity_error=error,pressure_error=pressure_error,torque=torque,exact_torque=exact['torque'],
                        torque_error=torque_error,stationarity=stationary,torque_drift=torque_drift,**m)
            case.row(record);records.append(record);case.data['data_files'].append(label+'.npz')
            np.savez_compressed(out/(label+'-diagnostics.npz'),u=u,p=p,exact_u=np.array([exact['u'],exact['v']]),
                                exact_p=exact['p']-np.mean(exact['p']))
    fine=records[2];coarse=records[0];stairfine=records[5]
    case.bound('finest interpolated velocity',fine['velocity_error'],limits['velocity'])
    case.bound('finest interpolated pressure gauge',fine['pressure_error'],limits['pressure'])
    case.bound('finest interpolated torque',fine['torque_error'],limits['torque'])
    case.gate('interpolated velocity refinement',fine['velocity_error']<coarse['velocity_error'])
    case.gate('interpolated pressure refinement',fine['pressure_error']<coarse['pressure_error'])
    case.gate('interpolated improves finest stair velocity',fine['velocity_error']<stairfine['velocity_error'])
    case.gate('three grids with both boundary variants',len(records)==6)
    numeric_csv(out/'lbm-annular-couette-control-summary.csv',records)
    case.finish(dict(finest_interpolated=fine,finest_stair=stairfine,reference_qualification=qualification,
                     scope='Stationary rotating-wall annulus only; does not substitute for actual cylinder flow.'))

def run_cylinder(root,out,inputs,limits,cases,native):
    reference=json.loads((root/'references/cylinder-original-intervals.json').read_text())
    case=Case('lbm-cylinder-re20',out,cases);records=[]
    case.gate('original source definitions and interval anchors',reference['CD']==[5.57,5.59] and
              reference['CL']==[.0104,.0110] and reference['pressure_difference']==[.1172,.1176] and
              reference['recirculation_length']==[.0842,.0852] and reference['original_outlet_user_selected'] is True)
    for dx in inputs['dx']:
        dt=dx/6;nu=inputs['nu'];tau=.5+3*nu*dt/dx**2;steps=int(round(inputs['T']/dt))
        checkpoints=[int(round(t/dt)) for t in inputs['late_checkpoints']]
        g=build('cylinder',0,dx,dt,interpolation_order=2,outlet_mode='nee')
        ux=4*inputs['peak_U']*g['y']*(.41-g['y'])/.41**2
        initial_pressure=12*nu*inputs['mean_U']/.41**2*(2.2-g['x'])
        rho=1+3*(dt/dx)**2*initial_pressure
        f0=equilibrium(rho,np.array([ux,np.zeros(g['n'])])*dt/dx)
        label='lbm-cylinder-re20-dx'+str(dx);f,h,states,arrays=trajectory(native,g,tau,steps,checkpoints,f0,out,label)
        m=common(case,str(dx),f0,f,h,g,steps,inputs['mean_U']*dt/dx,limits['max_mach'],inputs['T'])
        probes,wake=cylinder_probes(f,g);previous,_=cylinder_probes(states[checkpoints[-2]],g)
        force_scale=dx**3/dt**2;normalization=2/(inputs['mean_U']**2*.1)
        late=np.mean(h[checkpoints[-2]:,6:8],axis=0)*force_scale*normalization
        before=np.mean(h[checkpoints[-3]:checkpoints[-2],6:8],axis=0)*force_scale*normalization
        CD,CL=[float(v) for v in late]
        cd_drift=abs(float(late[0]-before[0]))/abs(CD);cl_drift=abs(float(late[1]-before[1]))
        dp_drift=abs(probes['pressure_difference']-previous['pressure_difference'])/abs(probes['pressure_difference'])
        _,u,p=physical(f,g);_,prev_u,prev_p=physical(states[checkpoints[-2]],g)
        stationary=relative(u,prev_u)
        case.bound(str(dx)+' velocity stationarity',stationary,limits['stationarity'])
        case.bound(str(dx)+' drag late block drift',cd_drift,limits['drag_stationarity'])
        case.bound(str(dx)+' lift late block drift',cl_drift,limits['lift_stationarity'])
        case.bound(str(dx)+' pressure late drift',dp_drift,limits['pressure_stationarity'])
        case.gate(str(dx)+' positive downstream drag',CD>0)
        case.gate(str(dx)+' pressure front exceeds back',probes['pressure_difference']>0)
        record=dict(dx=dx,dt=dt,tau=tau,steps=steps,time=steps*dt,Re=20,CD=CD,CL=CL,
                    stationarity=stationary,drag_drift=cd_drift,lift_drift=cl_drift,pressure_drift=dp_drift,
                    **probes,**m)
        records.append(record);case.row(record);case.data['data_files'].append(label+'.npz')
        np.savez_compressed(out/(label+'-diagnostics.npz'),u=u,p=p,wake_u=wake,
                            initial_pressure=initial_pressure,force_coefficients=h[:,6:8]*force_scale*normalization)
    fine=records[-1]
    for key,scale,limit in [('CD',5.58,limits['drag_reference']),('CL',1.,limits['lift_reference']),
                            ('pressure_difference',.1174,limits['pressure_reference']),
                            ('recirculation_length',1.,limits['recirculation_reference'])]:
        case.bound('finest original range distance '+key,interval_distance(fine[key],reference[key])/scale,limit)
    case.bound('two-grid drag sensitivity',abs(records[0]['CD']-fine['CD'])/5.58,limits['drag_grid_difference'])
    case.gate('both prescribed actual full-domain cylinder grids',len(records)==2)
    numeric_csv(out/'lbm-cylinder-re20-summary.csv',records)
    case.finish(dict(finest=fine,reference_scope=reference['scope'],
                     outlet='All-nine poststream NEE: rho1,adjacent-poststream velocity; finite reservoir,not later FEATflow do-nothing',
                     initial_pressure='Straight Poiseuille-gradient guess, not a cylinder reference or imposed interior field'))

def execute(root,out,inputs,acceptance,cases):
    native=Native(root)
    try:
        dump(out/'compiler.json',native.compile_receipt)
        group=inputs['group']
        if group=='lbm-cavity':run_cavity(root,out,inputs['cavity'],acceptance['cavity'],cases,native)
        elif group=='lbm-taylor-green':run_tgv(root,out,inputs['tgv'],acceptance['tgv'],cases,native)
        elif group=='lbm-annulus':run_annulus(root,out,inputs['annulus'],acceptance['annulus'],cases,native)
        elif group=='lbm-curved-boundary':run_cylinder(root,out,inputs['cylinder'],acceptance['cylinder'],cases,native)
        else:raise ValueError('Unknown frozen group')
    finally:native.close()
