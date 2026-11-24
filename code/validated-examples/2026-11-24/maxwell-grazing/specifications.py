"""Pure scalar, fixed-record enumeration shared by qualification and runner."""
import math


def pml_specs(c):
    p=c['pml'];m=p['material'];w=p['carrier'];ep=m['epsilon_inf']+m['delta_epsilon']*m['omega0']**2/(m['omega0']**2-w*w)
    ky=math.sqrt(ep)*w*math.sin(math.radians(p['angle_degrees']))
    rows=[]
    for n,ny in zip(p['cells'],p['ny']):
        rows.append(dict(id='grazing-n'+str(n),cells=n,dy=2*math.pi/ky/ny,ky=ky,angle=math.radians(p['angle_degrees']),material=dict(m)))
    rows.append(dict(id='normal-n'+str(p['normal_control_cells']),cells=p['normal_control_cells'],dy=1.,ky=0.,angle=0.,material=dict(m)))
    rows.append({**rows[2],'id':'damped-grazing-n'+str(rows[2]['cells']),'material':{**m,'gamma':p['damping_companion_gamma']}})
    for s in rows:
        s['pml_peak']=p.get('pml_peak_by_cells',{}).get(str(s['cells']),p['pml_peak'])
        h=p['length']/s['cells'];maximum=p['courant']/math.sqrt(1/h**2+(0. if s['ky']==0 else 1/s['dy']**2))
        steps=math.ceil(p['final_time']/maximum/4)*4
        s.update(h=h,dt=p['final_time']/steps,steps=steps,times=[p['final_time']*i/4 for i in range(5)])
    return rows
