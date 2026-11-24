"""Fixed genuine2D cylinder scattering; references loaded after raw candidates."""
import json
import numpy as np
import cylinder_draft as core
from poynting import physical_flux
import reference_draft as ref
from cylinder_evolution import solve
from io_contract import ROOT,case,check,save,csv,checkpoint,run


def analyze(fields,g,spec):
    ph=tuple(fields[n+'_phasor'] for n in ['E','Hx','Hy'])
    widths=[2*physical_flux(ph,g,-r,r) for r in spec['contours']]
    windows=[2*physical_flux(tuple(fields[n+'_'+label] for n in ['E','Hx','Hy']),g,-spec['contours'][0],spec['contours'][0]) for label in ['first','second']]
    exact=ref.cylinder_scattering_width(spec['omega'],spec['radius'],spec['epsilon'],24)
    X,Y=np.meshgrid(g['x'],g['x'],indexing='ij');radius=np.hypot(X,Y)
    mask=(radius>=spec['radius']+.15)&(abs(X)<=1.5)&(abs(Y)<=1.5)
    analytic=np.zeros_like(X,dtype=complex);analytic[mask]=ref.cylinder_exterior_field(X[mask],Y[mask],spec['omega'],spec['radius'],spec['epsilon'],24)
    numerical=fields['E_phasor'];field_error=float(np.linalg.norm(numerical[mask]-analytic[mask])/np.linalg.norm(analytic[mask]))
    sigma=float(exact['scattering']);width_error=abs(widths[0]/sigma-1)
    return dict(width=float(widths[0]),reference_width=sigma,width_relative=float(width_error),field_relative=field_error,contour_fraction=float(abs(widths[0]-widths[1])/max(abs(widths[0]),1e-30)),window_fraction=float(abs(windows[0]-windows[1])/max(abs(widths[0]),1e-30)),reference_E=analytic,reference_mask=mask,
                staircase_area=float(np.sum(g['epsilon']>1)*g['h']**2),exact_area=float(np.pi*spec['radius']**2))


def execute(cfg,limits,output,cases):
    spec=cfg['cylinder'];c=case(spec['id']);cases.append(c);checkpoint(output,cases);fields=[];rows=[]
    q=json.loads((ROOT/'references/qualification.json').read_text())
    check(c,'reference-and-new-components-qualified',q['actual_checks'],100,q['passed'] is True and q['actual_checks']==100)
    for ppw in spec['ppw']:
        name='cylinder-ppw'+str(ppw);raw,g=solve(spec,ppw,1.,spec['epsilon'],output,name)
        a=analyze(raw,g,spec);raw.update(reference_E=a.pop('reference_E'),reference_mask=a.pop('reference_mask'));save(output,name,raw)
        row=dict(id=name,ppw=ppw,cells=len(g['x'])-1,steps=int(raw['steps']),dt=float(raw['dt']),fields=name+'.npz',**a);c['records'].append(row);rows.append(row);fields.append(raw)
        check(c,name+'/finite',0,0,all(np.isfinite(raw[n]).all() for n in ['E','Hx','Hy','history']))
        check(c,name+'/outward-scattering-power',row['width'],0,row['width']>0)
        check(c,name+'/closed-contour-sensitivity',row['contour_fraction'],limits['cylinder_contour_fraction'],row['contour_fraction']<=limits['cylinder_contour_fraction'])
        check(c,name+'/fixed-window-sensitivity',row['window_fraction'],limits['cylinder_window_fraction'],row['window_fraction']<=limits['cylinder_window_fraction']);checkpoint(output,cases)
    fine=rows[-1]
    check(c,'finest-scattering-width',fine['width_relative'],limits['cylinder_width_relative'],fine['width_relative']<=limits['cylinder_width_relative'])
    check(c,'finest-exterior-scattered-field',fine['field_relative'],limits['cylinder_exterior_field_relative'],fine['field_relative']<=limits['cylinder_exterior_field_relative'])
    check(c,'coarse-to-finest-improvement',fine['width_relative'],rows[0]['width_relative'],fine['width_relative']<rows[0]['width_relative'])
    name='cylinder-half-amplitude';half,g=solve(spec,spec['ppw'][-1],.5,spec['epsilon'],output,name)
    linear=max(float(np.max(abs(2*half[n+'_phasor']-fields[-1][n+'_phasor'])))/max(1.,float(np.max(abs(fields[-1][n+'_phasor'])))) for n in ['E','Hx','Hy'])
    half_width=2*physical_flux(tuple(half[n+'_phasor'] for n in ['E','Hx','Hy']),g,-spec['contours'][0],spec['contours'][0])
    check(c,'complete-run-phasor-linearity',linear,limits['cylinder_linearity'],linear<=limits['cylinder_linearity'])
    power=abs(4*half_width/fine['width']-1.);check(c,'complete-run-power-quadratic',float(power),limits['cylinder_linearity'],power<=limits['cylinder_linearity'])
    c['records'].append(dict(id=name,ppw=spec['ppw'][-1],steps=int(half['steps']),amplitude=.5,fields=name+'.npz',linearity=linear))
    name='cylinder-vacuum';vacuum,g=solve(spec,spec['ppw'][0],1.,1.,output,name)
    zero=max(float(np.max(abs(vacuum[n]))) for n in ['E','Hx','Hy']);check(c,'zero-contrast-stored-snapshot-fields',zero,limits['cylinder_vacuum'],zero<=limits['cylinder_vacuum'])
    c['records'].append(dict(id=name,ppw=spec['ppw'][0],steps=int(vacuum['steps']),epsilon=1.,fields=name+'.npz',stored_snapshot_scattered_peak=zero))
    csv(output,spec['id'],['ppw','cells','steps','width','reference_width','width_relative','field_relative','contour_fraction','window_fraction','staircase_area','exact_area'],[[r[n] for n in ['ppw','cells','steps','width','reference_width','width_relative','field_relative','contour_fraction','window_fraction','staircase_area','exact_area']] for r in rows])
    c['metrics'].update(completed_primary_and_control_runs=5,spatial_dimensions=2,geometry='Explicitnodalstaircase,noorderclaim',scattering_is_power_integral=True,reference='IndependentordinarycylindricalJ/H1,notspherical',gallery_source=fields[-1]['E_phasor'].shape[0])
    c['metrics'].update(finest_scattering_width=fine['width'],independent_scattering_width=fine['reference_width'],finest_width_relative_error=fine['width_relative'],finest_exterior_field_relative_error=fine['field_relative'],complete_run_phasor_linearity=linear)
    c['passed']=all(c['checks'].values());checkpoint(output,cases)
if __name__=='__main__':run(execute)
