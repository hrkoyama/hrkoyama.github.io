"""Positive-weight Gauss-normal full-f quiet PIC; not a delta-f or iid method.

Each fixed Gaussian velocity node carries a randomly shifted uniform spatial
lattice, then an exact density-CDF map. Seeds randomize spatial shifts only.
Seed intervals are conditional on velocity quadrature, whose Nv bias is separate.
Every carrier is dynamically advanced and sources its own evolving field.
"""
import numpy as np
from scipy.special import roots_hermitenorm


def velocities(count,drift):
    if count<16 or count%4:raise ValueError('Velocity nodes must be divisible byfour')
    z,w=roots_hermitenorm(count if drift==0 else count//2);w=w/w.sum()
    if drift==0:return z,w
    return np.r_[drift+z,-drift-z],np.r_[.5*w,.5*w]


def load(spatial_strata,velocity_strata,length,amplitude,drift,seed):
    if spatial_strata<16 or length<=0 or not 0<=amplitude<.05:raise ValueError('Invalid quiet-load controls')
    vv,wv=velocities(velocity_strata,drift);rng=np.random.default_rng(seed);shift=rng.random(velocity_strata)
    phase=2*np.pi*(np.arange(spatial_strata)[None,:]+shift[:,None])/spatial_strata;theta=phase.copy()
    for _ in range(8):theta-=(theta+amplitude*np.sin(theta)-phase)/(1+amplitude*np.cos(theta))
    x=length/(2*np.pi)*theta.ravel();v=np.repeat(vv,spatial_strata);weights=np.repeat(length*wv/spatial_strata,spatial_strata)
    return x,v,weights,vv,wv


def qualification(x,v,weights,vtable,vweights,length,amplitude,drift):
    theta=2*np.pi*x/length;worst=0.;char=0.
    for mode in [0,1,2]:
        density=1. if mode==0 else amplitude/2 if mode==1 else 0.
        for eta in [0.,.5,1.]:
            empirical=np.sum(weights*np.exp(-1j*mode*theta-1j*eta*v))/length;factor=density*np.sum(vweights*np.exp(-1j*eta*vtable));worst=max(worst,float(abs(empirical-factor)))
    for eta in [0.,.5,1.,2.,4.,6.]:char=max(char,float(abs(np.sum(vweights*np.exp(-1j*eta*vtable))-np.exp(-.5*eta*eta)*np.cos(eta*drift))))
    fourth=drift**4+6*drift**2+3
    return dict(joint_low_mode_factorization_defect=worst,mean_velocity=float(np.sum(weights*v)/length),thermal_variance=float(np.sum(vweights*vtable*vtable)-drift**2),fourth_moment_relative_error=float(abs(np.sum(vweights*vtable**4)-fourth)/fourth),gaussian_characteristic_defect=char,density_mode_defect=float(abs(np.sum(weights*np.exp(-1j*theta))/length-amplitude/2)),minimum_weight=float(weights.min()),maximum_velocity=float(np.max(abs(vtable))))
