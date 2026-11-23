import json
import numpy as np
import fem,annulus,boundary
from references import fields
IDS=['lshape-fem','annular-viscous-mms','poisson-neumann','poisson-robin']


def execute(cfg,out,L,cases=None):
    if cases is None:cases=[]
    for ident in IDS:
        rows=[];checks={};files=[]
        def gate(name,value,bound):checks[name]=bool(value<=bound)
        def checkpoint():
            (out/'partial-progress.json').write_text(json.dumps(dict(current_case=ident,records=rows,checks=checks,data_files=files),indent=2)+'\n')
        if ident==IDS[0]:
            for family in ['uniform','graded','square','warped']:
                for n in cfg['fem_grids']:
                    row,arrays=fem.solve(n,family);row['id']=family+'-n'+str(n);rows.append(row)
                    name=ident+'-'+row['id']+'.npz';np.savez_compressed(out/name,**arrays);files.append(name)
                    for key,b in [('residual',L['linear_residual']),('boundary_error',L['boundary']),('symmetry',L['symmetry']),('quadrature_relative_gap',L['quadrature_gap'])]:gate(row['id']+' '+key,row[key],b)
                    checks[row['id']+' positive geometry']=bool(row['minimum_area']>0 and row['minimum_angle_degrees']>L['minimum_angle'])
                    checkpoint()
            for family in ['uniform','graded','square','warped']:
                seq=[r for r in rows if r['family']==family]
                for key in ['l2','h1']:
                    for j in [1,2]:gate(family+' '+key+' refinement '+str(j),seq[j][key]/seq[j-1][key],L['corner_ratio'] if family in ['uniform','graded'] else L['smooth_ratio'])
            uniform=[r for r in rows if r['family']=='uniform'];graded=[r for r in rows if r['family']=='graded']
            checks['matched unknown counts']=bool([r['dofs'] for r in uniform]==[r['dofs'] for r in graded])
            gate('finest graded/uniform H1',graded[-1]['h1']/uniform[-1]['h1'],L['graded_improvement'])
            gate('finest graded H1',graded[-1]['h1'],L['corner_h1'])
        elif ident==IDS[1]:
            for n in cfg['annulus_grids']:
                candidate=ident+'-annulus-n'+str(n)+'-diagnostic-candidate.npz';files.append(candidate)
                row,arrays=annulus.solve(n,out/candidate);row['id']='annulus-n'+str(n);rows.append(row)
                name=ident+'-'+row['id']+'.npz';np.savez_compressed(out/name,**arrays);files.append(name)
                for key,b in [('residual',L['linear_residual']),('boundary_error',L['boundary']),('area_error',L['area']),('reaction_balance',L['reaction_balance']),('exact_flux_balance',L['exact_flux_balance']),('analytic_force_error',L['exact_flux_balance']),('work_identity',L['work']),('symmetry',L['symmetry'])]:gate(row['id']+' '+key,row[key],b)
                checkpoint()
            for key in ['relative_l2','relative_strain_l2','relative_traction_l2','traction_flux_balance']:
                for j in [1,2]:gate(key+' refinement '+str(j),rows[j][key]/rows[j-1][key],L['annulus_ratio'])
            for key,b in [('relative_l2',L['annulus_l2']),('relative_strain_l2',L['annulus_strain']),('relative_traction_l2',L['annulus_traction']),('traction_flux_balance',L['annulus_flux'])]:gate('finest '+key,rows[-1][key],b)
        else:
            kind='neumann' if ident==IDS[2] else 'robin'
            for n in cfg['poisson_grids']:
                row,arrays=boundary.solve(n,kind);row['id']=kind+'-n'+str(n);rows.append(row)
                name=ident+'-'+row['id']+'.npz';np.savez_compressed(out/name,**arrays);files.append(name)
                for key,b in [('residual',L['linear_residual']),('boundary_residual',L['boundary']),('flux_balance',L['poisson_flux']),('symmetry',L['symmetry'])]:gate(row['id']+' '+key,row[key],b)
                if kind=='neumann':
                    for key,b in [('compatibility',L['compatibility']),('mean_error',L['gauge']),('nullspace_defect',L['symmetry']),('solver_gap',L['solver_gap'])]:gate(row['id']+' '+key,row[key],b)
                checkpoint()
            for j in [1,2]:gate('L2 refinement '+str(j),rows[j]['l2']/rows[j-1]['l2'],L['poisson_ratio'])
            gate('finest L2',rows[-1]['l2'],L['poisson_l2'])
            if kind=='neumann':
                base,a=boundary.solve(cfg['gauge_grid'],'neumann');shift,b=boundary.solve(cfg['gauge_grid'],'neumann',.25)
                gauge_gap=float(np.max(abs(b['u']-a['u']-.25)));gate('mean gauge shifts only constant',gauge_gap,L['gauge_shift'])
                name=ident+'-gauge-shift.npz';np.savez_compressed(out/name,zero_mean=a['u'],shifted=b['u'],reference=a['reference']);files.append(name)
                try:boundary.solve(cfg['gauge_grid'],'neumann',forcing_offset=1.)
                except ValueError:checks['incompatible source rejected without projection']=True
                else:checks['incompatible source rejected without projection']=False
                rows[-1]['gauge_shift_error']=gauge_gap
            else:
                for j in [1,2]:gate('boundary flux refinement '+str(j),rows[j]['boundary_flux_error']/rows[j-1]['boundary_flux_error'],L['poisson_ratio'])
                gate('finest boundary flux',rows[-1]['boundary_flux_error'],L['robin_flux'])
        qualification=fields.qualify()
        for name,passed in qualification['checks'].items():checks['analytic '+name]=passed
        cases.append(dict(id=ident,passed=all(checks.values()),checks=checks,records=rows,metrics={k:v for k,v in rows[-1].items() if isinstance(v,(int,float))},data_files=files,reference_qualification=qualification))
    return cases
