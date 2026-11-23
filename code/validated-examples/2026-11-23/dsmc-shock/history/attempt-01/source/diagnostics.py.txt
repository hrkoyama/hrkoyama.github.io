"""Whole-run uncertainty and fixed-bin diagnostics, shared arithmetic only."""
import numpy as np
from dsmc import SIGMA,U1,U2,RHO2,TEMP2


def ensemble(values):
    values=np.asarray(values)
    if len(values)<2:raise ValueError('Independent seed ensemble required')
    return np.mean(values,axis=0),np.std(values,axis=0,ddof=1)/np.sqrt(len(values))


def rms(value):return float(np.sqrt(np.mean(np.asarray(value)**2)))


def scales(ident):
    if ident=='dsmc-couette':return {2:1.,4:1.,0:1.}
    if ident=='dsmc-fourier':return {4:1.,0:1.}
    return {0:RHO2-1,1:U1-U2,4:TEMP2-1,5:19/4-1}


def centroid(profiles,length):
    # Mass-excess position; no clipping, shifting or feedback pinning.
    return (RHO2*length-np.mean(profiles[...,0],axis=-1)*length)/(RHO2-1)


def stationarity(block_profiles,ident,length):
    # Shape: independent seeds, fixed time blocks, observation bins, fields.
    values=np.asarray(block_profiles)
    delta=np.mean(values[:,-2:],axis=1)-np.mean(values[:,:2],axis=1)
    mean,se=ensemble(delta)
    ratios={str(k):(rms(mean[:,k])+3*rms(se[:,k]))/scale for k,scale in scales(ident).items()}
    data={'profile_equivalence':ratios}
    if ident=='dsmc-planar-shock':
        centers=centroid(values,length)
        drift=np.mean(centers[:,-2:],axis=1)-np.mean(centers[:,:2],axis=1)
        m,s=ensemble(drift)
        data.update(centroid_blocks=centers.tolist(),centroid_drift_bound=float(abs(m)+3*s))
    return data


def resolution(profiles,cells,length,dt):
    # Local Maxwellian collision-time diagnostic, not the exact nonequilibrium
    # collision frequency. Measured collision/candidate counts are also retained.
    n=profiles[...,0];t=profiles[...,4]
    return {'dx_over_lambda':float(np.max(n)*length/cells),
            'dt_over_maxwell_tau':float(np.max(n*SIGMA*4*np.sqrt(t/np.pi))*dt)}


def profile_comparison(primary,reference,ident):
    pm,ps=ensemble(primary);rm,rs=ensemble(reference)
    combined=np.sqrt(ps*ps+rs*rs)
    return {str(k):{'error':rms(pm[:,k]-rm[:,k])/scale,
                    'combined_3se':3*rms(combined[:,k])/scale,
                    'primary_3se':3*rms(ps[:,k])/scale,
                    'reference_3se':3*rms(rs[:,k])/scale}
            for k,scale in scales(ident).items()}


def flux(values,ident):
    column=6 if ident=='dsmc-couette' else 7
    # Fixed spatial mean, one value per whole run; bins are not replicates.
    return np.mean(values[...,column],axis=-1)


def far_states(values,length):
    x=(np.arange(values.shape[-2])+.5)*length/values.shape[-2]
    left=(x>=1)&(x<=3);right=(x>=length-3)&(x<=length-1)
    output={}
    for side,mask,exact in [('upstream',left,[1,U1,1]),('downstream',right,[RHO2,U2,TEMP2])]:
        if not np.any(mask):raise ValueError('Empty frozen far-state window')
        for column,target,name in zip([0,1,4],exact,['n','ux','T']):
            estimates=np.mean(values[:,mask,column],axis=1);mean,se=ensemble(estimates)
            output[side+'_'+name]={'relative_error':float(abs(mean-target)/target),'relative_3se':float(3*se/target)}
    # Full kinetic flux values from raw velocities (not only peculiar moments).
    targets=[U1,U1**2+1,.5*U1*(U1**2+5)]
    for column,target,name in zip([8,9,10],targets,['mass','momentum','energy']):
        estimates=np.mean(values[...,column],axis=1);mean,se=ensemble(estimates)
        output['flux_'+name]={'relative_error':float(abs(mean-target)/target),'relative_3se':float(3*se/target)}
    return output
